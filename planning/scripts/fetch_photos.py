#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""给云南站抓景点图：Wikimedia Commons 搜索 + 下载 + Pillow 压缩。

用法：
    python fetch_photos.py           # 抓全部缺图景点
    python fetch_photos.py --id 1 2  # 只抓指定 id 的图

输出：
    planning/pics/<id>.jpg           ← 源图（压缩到 ≤900px）
    planning/data/photos.json        ← 引用关系（被 build_site.py 读）
"""
import json, shutil, time, urllib.parse, urllib.request, argparse
from pathlib import Path

UA = "TripYunnanPhotoTool/1.0 (https://github.com/jack975645419; trip-photo@example.com)"

ROOT = Path(__file__).resolve().parent.parent
REPO = Path(r"D:\Proj\Trip_2027_11_YunNan")
PLACES_JSON = ROOT / "data" / "places.json"
PHOTOS_JSON = ROOT / "data" / "photos.json"
PICS_SRC = ROOT / "pics"
PICS_SRC.mkdir(parents=True, exist_ok=True)

# 抓图搜索关键词（更精确，英文 + 中文 + 别名）
SEARCH = {
    "cui_lake":        ["Cuihu Park Kunming", "翠湖 昆明"],
    "yunnan_military": ["Yunnan Military Academy", "云南陆军讲武堂"],
    "jinma_biji":      ["Jinma Biji Fang Kunming", "金马碧鸡坊"],
    "daguan":          ["Daguan Pavilion Kunming", "大观楼"],
    "yunnan_museum":   ["Yunnan Provincial Museum"],
    "guandu":          ["Guandu Kunming", "官渡古镇"],
    "xishan":          ["Xishan Kunming", "西山龙门"],
    "jin_dian":        ["Kunming Golden Temple", "金殿 昆明"],
    "heshun":          ["Heshun Ancient Town", "和顺古镇"],
    "rehai":           ["Rehai Geothermal Park Tengchong", "腾冲热海"],
    "volcano":         ["Tengchong volcano", "腾冲火山"],
    "beihai":          ["Beihai Wetland Tengchong", "北海湿地"],
    "ginkgo":          ["Jiangdong Ginkgo Village", "银杏"],
    "dieshui":         ["Dieshui Waterfall Tengchong", "叠水河"],
    "war_memorial":    ["Tengchong National Cemetery", "国殇墓园"],
    "yzz_memorial":    ["Yunnan Burma War Museum", "滇缅抗战"],
    "qinghuahai":      ["Qinghuahai Baoshan wetland", "青华海"],
    "yiluo":           ["Yiluo Pond Baoshan", "易罗池"],
    "taibao":          ["Taibao Mountain Baoshan", "太保山"],
    "wofo":            ["Baoshan Wofo Temple", "卧佛 保山"],
    "heilongtan":      ["Heilongtan Park Kunming", "黑龙潭"],
    "jietou_ginkgo":   ["Jietou ginkgo Tengchong", "界头银杏"],
}


def commons_search(query: str, limit: int = 8):
    """返回 [{title, url, license, author}] 列表"""
    url = ("https://commons.wikimedia.org/w/api.php?action=query"
           f"&generator=search&gsrsearch={urllib.parse.quote(query)}"
           f"&gsrnamespace=6&gsrlimit={limit}"
           "&prop=imageinfo&iiprop=url|extmetadata&format=json")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
    except Exception as e:
        print(f"  ✗ search '{query}': {e}")
        return []
    pages = data.get("query", {}).get("pages", {})
    out = []
    for pid, p in pages.items():
        if "imageinfo" not in p:
            continue
        info = p["imageinfo"][0]
        url = info.get("url", "")
        # URL 形如 ...xxx.jpg?utm_source=...&utm_campaign=...
        # 先剥掉 query string 再判扩展名
        url_path = url.split("?")[0]
        if not url_path.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        meta = info.get("extmetadata", {})
        out.append({
            "title": p.get("title", ""),
            "url": url,
            "license": meta.get("LicenseShortName", {}).get("value", ""),
            "author": meta.get("Artist", {}).get("value", "")[:200],
            "width": info.get("width", 0),
            "height": info.get("height", 0),
        })
    return out


def download(url: str, target: Path):
    # 去掉 utm_* 跟踪参数（Wikimedia 加的；下载直连原始地址）
    if "?" in url:
        url = url.split("?")[0]
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Referer": "https://commons.wikimedia.org/",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        target.write_bytes(r.read())


def resize_jpeg(p: Path, max_w=900, quality=82):
    from PIL import Image
    im = Image.open(p)
    if im.mode != "RGB":
        im = im.convert("RGB")
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    im.save(p, "JPEG", quality=quality, optimize=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", nargs="*", help="只抓指定 id（默认全部缺图）")
    args = ap.parse_args()

    places = {p["id"]: p for p in json.loads(PLACES_JSON.read_text(encoding="utf-8"))}
    photos = json.loads(PHOTOS_JSON.read_text(encoding="utf-8")) if PHOTOS_JSON.exists() else {}

    targets = args.id or list(SEARCH.keys())
    ok, skip, fail = 0, 0, []

    for pid in targets:
        if pid not in SEARCH:
            print(f"  ✗ unknown id: {pid}")
            fail.append(pid); continue
        if pid in photos and photos[pid].get("files"):
            print(f"  · skip {pid} (已有)")
            skip += 1; continue

        name = places.get(pid, {}).get("name", pid)
        queries = SEARCH[pid]
        chosen = None
        for q in queries:
            print(f"  … search {pid}: {q}")
            results = commons_search(q, limit=8)
            if results:
                # 偏好：宽 ≥ 800px 的横向图
                results.sort(key=lambda r: -(r["width"] or 0))
                chosen = results[0]
                break
            time.sleep(1.0)

        if not chosen:
            print(f"  ✗ {name} no result")
            fail.append(pid); continue

        try:
            target = PICS_SRC / f"{pid}.jpg"
            download(chosen["url"], target)
            resize_jpeg(target)
            kb = target.stat().st_size // 1024
            photos[pid] = {
                "files": [{
                    "file": f"pics/{pid}.jpg",
                    "caption": name,
                    "source": "Wikimedia Commons",
                    "license": chosen["license"] or "CC",
                    "author": chosen["author"],
                    "commons_title": chosen["title"],
                    "commons_url": chosen["url"],
                }]
            }
            print(f"  ✓ {name}  ({kb} KB, {chosen['license']})")
            ok += 1
        except Exception as e:
            print(f"  ✗ {name} download: {e}")
            fail.append(pid)

        time.sleep(2.0)

    PHOTOS_JSON.write_text(json.dumps(photos, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n=== {ok} ok, {skip} skip, {len(fail)} fail ===")
    if fail:
        print("失败 id:", fail)


if __name__ == "__main__":
    main()
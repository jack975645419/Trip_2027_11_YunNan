# 2027-11 云南腾冲保山 · 赏秋 5 天

2027 年 11 月「我和灯灯」的云南腾冲 / 保山行程规划 + 可视化网站。纯静态站点，GitHub Pages 托管。

- **线上地址**：https://jack975645419.github.io/Trip_2027_11_YunNan/
- **现行方案**：`/d/` —— 广州 → 昆明 1 晚 → 腾冲 3 晚 → 保山 1 晚（短停）→ 深圳（4 晚 5 天）
- **需求与规划文档母文件夹**：`D:\Proj\Trip_2027_11_YunNan\planning\`

## 一、技术栈

| 层 | 选型 |
|---|---|
| 地图库 | **Leaflet 1.9.4**（jsdelivr CDN）|
| 底图瓦片 | **Esri World Street Map**（免 Key、免费）|
| 框架 | 无（原生 HTML + CSS + 内联 JS）|
| 数据加载 | `data/*.js` 以全局变量注入（不用 fetch）|
| 箭头/标记 | 自绘 SVG + `L.divIcon` |

详细说明与本仓库历史沿革参考姊妹项目 [2027-1-au-hu-cz-trip](https://github.com/jack975645419/2027-1-au-hu-cz-trip)。

## 二、目录结构

```
Trip_2027_11_YunNan/
├── index.html         主页（仅 1 方案 + 交通指引 + 3 段航班）
├── 交通指引.md          ★ 交通指引源文件（构建时渲染成 guide/）
├── guide/index.html    交通指引网页版
├── d/index.html        ★ 方案 D 主页（5 天行程 + 20 个景点 + 9 家酒店）
├── data/               渲染产物
└── planning/           源数据 + 脚本 + 文档
    ├── data/places.json (20 个景点：昆明 8 + 腾冲 8 + 保山 4)
    ├── data/hotels.json (9 家候选：每城 3 家)
    ├── data/itineraries.json (方案 D 单方案)
    ├── data/transit.json (5 POINTS + 2 METRO)
    ├── data/photos.json (空 - 本次未抓图)
    ├── scripts/build_site.py
    ├── scripts/smoke.py
    ├── scripts/version.py
    ├── scripts/write_data.py (一次性写入 data/)
    └── 旅行需求.md
```

## 三、脚本

全部在 `planning/scripts/`：

| 脚本 | 作用 |
|---|---|
| `write_data.py` | 一次性写入 places/hotels/itineraries/transit.json |
| `build_site.py` | 渲染整站 |
| `smoke.py` | Playwright 冒烟验证（pageerror / 标记数 / 日程数 / 0 JS 异常）|
| `version.py` | 生成版本号 + 时间戳（提交前跑）|

```bash
cd D:\Proj\Trip_2027_11_YunNan\planning\scripts
python build_site.py "改动说明"
python smoke.py
python version.py "改动说明"
git add -A && git commit -m "..." && git push origin main
```

期望值（smoke.py）：20 places / 5 days / 3 酒店区 / 0 JS 异常。

## 四、行程速览（11/17 → 11/21）

| 日期 | 城市 | 主要安排 |
|---|---|---|
| 11/17 周三 | 昆明（1 晚）| 落地 KMG → 翠湖 / 讲武堂 / 金马碧鸡坊 / 大观楼 / 省博 |
| 11/18 周四 | 腾冲（1 晚）| 13:35 飞 TCG → 老城三馆（叠水河 + 国殇墓园 + 滇缅抗战博物馆）|
| 11/19 周五 | 腾冲（1 晚）| 和顺古镇 + 热海泡温泉 |
| 11/20 周六 | 腾冲（1 晚）| 火山公园 + 北海湿地 + **银杏村**（11 月下旬最佳期）|
| 11/21 周日 | 保山（短停）| 上午包车 3h → 易罗池 + 青华海 → 18:30 去 BSD → 20:30 飞深圳 |

详见 `planning/旅行需求.md`。
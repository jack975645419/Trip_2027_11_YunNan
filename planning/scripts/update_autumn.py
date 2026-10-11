"""更新 places + itinerary：黑龙潭 + 界头银杏林 + 二选一标记（idempotent）"""
import json

base = r'D:\Proj\Trip_2027_11_YunNan\planning\data'
with open(f'{base}\\places.json', encoding='utf-8') as f:
    places = json.load(f)

# 加 2 个新点（如已存在则跳过）
new_spots = [
    ("heilongtan", "黑龙潭公园", "昆明", 25.1400436, 102.7453852,
     "Heilongtan Park", "1.5h", "免费",
     "昆明秋景圣地；'龙泉探梅'（12–1 月梅花）前的秋色——古枫、水杉、栾树、银杏满园。地铁 5 号线 蒜村站 C 出口。"),
    ("jietou_ginkgo", "界头镇银杏林", "腾冲", 25.4281405, 98.6474418,
     "Jietou Ginkgo Forest", "3h", "免费",
     "腾冲北部高海拔银杏密集区；15 万亩连片，比江东银杏村更野、规模更大。**与江东银杏村（11/20）二选一**：江东更出名、游客多；界头更小众、漫山遍野。"),
]
existing = {p['id'] for p in places}
for sid, name, city, lat, lon, en, dur, book, desc in new_spots:
    if sid not in existing:
        places.append({"id":sid,"name":name,"city":city,"lat":lat,"lon":lon,
                       "en":en,"dur":dur,"book":book,"desc":desc})
    else:
        # 更新已有
        for p in places:
            if p['id'] == sid:
                p.update({"name":name,"lat":lat,"lon":lon,"en":en,"dur":dur,"book":book,"desc":desc})

# 把"银杏村（江东）"重命名为"江东银杏村（固东镇江东）"
for p in places:
    if p['id'] == 'ginkgo':
        p['name'] = "江东银杏村（固东镇江东）"

with open(f'{base}\\places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
print(f"places.json: {len(places)} 个景点")

# itinerary
with open(f'{base}\\itineraries.json', encoding='utf-8') as f:
    itins = json.load(f)
D = itins['D']

D['days'][0]['items'] = ["黑龙潭公园", "云南陆军讲武堂", "翠湖公园", "金马碧鸡坊", "大观楼", "云南省博物馆"]
D['days'][0]['note'] = (
    "广州白云 T3 → 昆明长水；落地后地铁 6 号线入市区；"
    "上午地铁 5 号线蒜村站直达黑龙潭（秋景圣地，古枫+水杉+银杏）→ "
    "下午回市区讲武堂+翠湖+金马碧鸡坊（步行连游）→ "
    "大观楼看滇池日落 → 晚饭祥云美食城"
)
D['days'][0]['stay'] = "昆明"

D['days'][2]['items'] = ["和顺古镇", "热海（地热温泉）", "界头镇银杏林"]
D['days'][2]['note'] = (
    "上午和顺古镇（4h），下午热海泡温泉（14:00–17:00 旺季后段，避开早 10–13 点温泉池拥挤）；"
    "晚归腾冲市区。<br><b>银杏主题二选一</b>：如今天改去<b>界头镇银杏林</b>（腾冲北部 40 km，海拔更高、秋色更早到），"
    "11/20 可放弃<b>江东银杏村</b>改为休闲腾冲老城；反之亦然。"
)

D['days'][3]['items'] = ["火山地热国家地质公园", "北海湿地", "江东银杏村（固东镇江东）"]
D['days'][3]['note'] = (
    "全天包车线路：早 8:30 火山公园（小空山 1.5h）→ 北海湿地（1.5h）→ "
    "<b>江东银杏村</b>（2h，<b>与 11/19 界头镇银杏林二选一</b>）；回腾冲市区晚饭"
)

with open(f'{base}\\itineraries.json', 'w', encoding='utf-8') as f:
    json.dump(itins, f, ensure_ascii=False, indent=2)

# 验证
used = set()
for d in D['days']:
    for nm in d.get('items', []):
        used.add(nm)
orphans = [p['name'] for p in places if p['name'] not in used]
print(f"used={len(used)}, orphans={orphans if orphans else '✅none'}")
print("\n=== 11/17-20 items ===")
for d in D['days'][:4]:
    print(f"  {d['date']} {d['w']} {d['city']}: {d['items']}")
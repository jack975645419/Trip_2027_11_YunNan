"""一次性写 places/hotels/itineraries/transit.json 给云南腾冲保山之旅"""
import json

# ============ places.json ============
places = [
    # 昆明 (8)
    {"id":"cui_lake",  "name":"翠湖公园", "city":"昆明", "lat":25.0514918, "lon":102.7025178,
     "en":"Cuihu Park","dur":"1h","book":"免费",
     "desc":"昆明市区内开放式湖景公园，被誉为'城市绿宝石'，冬季红嘴鸥从西伯利亚飞来过冬（11–3 月是最佳观赏期）。"},
    {"id":"yunnan_military",  "name":"云南陆军讲武堂", "city":"昆明", "lat":25.0506971, "lon":102.6997260,
     "en":"Yunnan Military Academy","dur":"0.5–1h","book":"免费",
     "desc":"1909 年与保定陆军军官学校齐名的'南方军校'，朱德、叶剑英都毕业于此。建筑为土黄色走马转角楼。"},
    {"id":"jinma_biji", "name":"金马碧鸡坊", "city":"昆明", "lat":25.0356066, "lon":102.7089222,
     "en":"Jinma & Biji Archways","dur":"0.5h","book":"免费",
     "desc":"昆明老城地标双牌坊，始建于明代；周边是昆明最热闹的步行街与商圈。"},
    {"id":"daguan", "name":"大观楼", "city":"昆明", "lat":25.0302806, "lon":102.6743609,
     "en":"Daguan Pavilion","dur":"1–1.5h","book":"公园免费，公园内大观楼登楼 ¥2",
     "desc":"'五百里滇池'长联就挂在这里，是清代孙髯翁所作，海内第一长联；公园滨滇池北岸，秋冬有红嘴鸥。"},
    {"id":"yunnan_museum","name":"云南省博物馆", "city":"昆明", "lat":25.0352733, "lon":102.7270241,
     "en":"Yunnan Provincial Museum","dur":"1.5–2h","book":"免费（需预约）",
     "desc":"'七彩云南'历史文化展、滇文化青铜器、少数民族服饰；周二至周日 9:00–17:00（周一闭馆）。"},
    {"id":"guandu","name":"官渡古镇", "city":"昆明", "lat":24.9599345, "lon":102.7554702,
     "en":"Guandu Ancient Town","dur":"1.5h","book":"免费", "备用": True,
     "desc":"千年古镇，昆明最老的佛教寺庙'妙湛寺金刚塔'所在地；周末小吃云集（小锅米线、稀豆粉）。行程如有余量可去。"},
    {"id":"xishan","name":"西山龙门", "city":"昆明", "lat":24.9617710, "lon":102.6248207,
     "en":"Xishan Longmen","dur":"3–4h","book":"龙门石窟 ¥40 + 龙门索道单程 ¥25", "备用": True,
     "desc":"滇池西岸连绵山脉，'龙门石窟'从悬崖凿出，含三清阁；建议乘索道上+步行下。需半天，可备选。"},
    {"id":"jin_dian","name":"金殿", "city":"昆明", "lat":25.0914321, "lon":102.7700939,
     "en":"Jin Dian Golden Temple","dur":"1–1.5h","book":"¥25", "备用": True,
     "desc":"'中国四大铜殿'之一（与武当山铜殿齐名），明代仿青铜铸造；公园内有茶花、杜鹃。"},

    # 腾冲 (8)
    {"id":"heshun", "name":"和顺古镇", "city":"腾冲", "lat":25.0151570, "lon":98.4574838,
     "en":"Heshun Ancient Town","dur":"3–4h（建议住一晚）","book":"古镇免费，各展览馆 ¥10–30",
     "desc":"'中国第一魅力名镇'；明清汉族侨乡文化保留完整，有'弯楼子'民居、图书馆（乡村第一座）、艾思奇故居。"},
    {"id":"rehai", "name":"热海（地热温泉）", "city":"腾冲", "lat":24.9925265, "lon":98.4870897,
     "en":"Rehai Geothermal Park","dur":"2.5–3h","book":"景区 ¥50，泡温泉另 ¥198–298",
     "desc":"'中国地热博物馆'；最有名'大滚锅'（直径 6m，水温 96℃），可蒸鸡蛋。景区山顶有浴谷温泉酒店。"},
    {"id":"volcano", "name":"火山地热国家地质公园", "city":"腾冲", "lat":25.2228756, "lon":98.4977805,
     "en":"Tengchong Volcanic Geopark","dur":"2–3h","book":"景区 ¥40，景区热气球另 ¥280",
     "desc":"'中国火山博物馆'；小空山/大空山/黑空山三座火山一字排开，可登小空山栈道看火山口。"},
    {"id":"beihai", "name":"北海湿地", "city":"腾冲", "lat":25.1232925, "lon":98.5580440,
     "en":"Beihai Wetland","dur":"2h","book":"景区 ¥110（含游船）",
     "desc":"'高原火山堰塞湖湿地'；草排浮岛是特色（人在草上漂），秋冬季节草色金黄。"},
    {"id":"ginkgo", "name":"银杏村（江东）", "city":"腾冲", "lat":25.3007837, "lon":98.5124672,
     "en":"Ginkgo Village","dur":"2–3h","book":"¥40",
     "desc":"'中国银杏第一村'；3000 余棵古银杏树，11 月下旬–12 月初为最佳观赏期（金黄满村）；注意 11/22–11/30 是最佳时段。"},
    {"id":"dieshui", "name":"叠水河瀑布", "city":"腾冲", "lat":25.0317850, "lon":98.4786025,
     "en":"Dieshui Waterfall","dur":"1h","book":"¥10",
     "desc":"'中国唯一的城市瀑布'；瀑布从悬崖跌下形成太极图，腾冲城边。"},
    {"id":"war_memorial","name":"国殇墓园", "city":"腾冲", "lat":25.0289086, "lon":98.4809053,
     "en":"National Martyrs Cemetery","dur":"1h","book":"免费",
     "desc":"中国规模最大的抗日阵亡将士陵园（1945 年）；松柏环绕，庄严肃穆。"},
    {"id":"yzz_memorial","name":"滇缅抗战博物馆", "city":"腾冲", "lat":25.0286706, "lon":98.4815130,
     "en":"Yunnan-Burma War Museum","dur":"1–1.5h","book":"免费",
     "desc":"与国殇墓园相邻，馆藏 8000+ 件抗战文物；讲述中国远征军入缅作战史。"},

    # 保山 (5)
    {"id":"qinghuahai","name":"青华海国家湿地公园", "city":"保山", "lat":25.1172815, "lon":99.2086414,
     "en":"Qinghuahai Wetland Park","dur":"1.5h","book":"免费",
     "desc":"'保山的翠湖'；环湖步道+红嘴鸥（11 月–3 月）；离市中心近，晚饭后散步首选。"},
    {"id":"yiluo","name":"易罗池", "city":"保山", "lat":25.1147357, "lon":99.1510226,
     "en":"Yiluo Pond","dur":"1h","book":"免费",
     "desc":"明代人工湖，'保山小西湖'；湖心亭、茶馆、垂柳；市中心步行 10 min。"},
    {"id":"taibao","name":"太保山森林公园", "city":"保山", "lat":25.1205078, "lon":99.1599746,
     "en":"Taibao Mountain","dur":"2h","book":"免费", "备用": True,
     "desc":"保山市中心绿肺；山顶有玉皇阁（俯瞰保山全景）+ 西南丝绸之路浮雕群。11/21 时间不够可舍。"},
    {"id":"wofo","name":"卧佛寺", "city":"保山", "lat":25.2083713, "lon":99.2001485,
     "en":"Wofo Temple","dur":"1h","book":"¥10", "备用": True,
     "desc":"'保山最古老的寺庙'之一，明代建；殿内长 6m 卧佛；顺路泡脚温泉（保山温泉资源丰富）。"},
]

# ============ transit.json ============
transit = {
    "points": [
        {"key":"SZX", "kind":"airport", "name":"深圳宝安国际机场", "for":"出发地 / 回程抵达", "city":"深圳", "lat":22.6403727, "lon":113.8030964},
        {"key":"KMG", "kind":"airport", "name":"昆明长水国际机场", "for":"去程落地 / 11/18 出发", "city":"昆明", "lat":25.1087786, "lon":102.9397246},
        {"key":"TCG", "kind":"airport", "name":"腾冲驼峰机场", "for":"11/18 落地", "city":"腾冲", "lat":24.9406796, "lon":98.4846270},
        {"key":"BSD", "kind":"airport", "name":"保山云瑞机场", "for":"11/21 回程起飞", "city":"保山", "lat":25.0516019, "lon":99.1645954},
        {"key":"KMCX", "kind":"train", "name":"昆明南站（高铁）", "for":"备选高铁进腾冲", "city":"昆明", "lat":24.7461, "lon":102.9248},
    ],
    "metro": [
        # 昆明地铁（昆明长水机场地铁 6 号线）
        {"key":"KMG_metro", "name":"机场中心站（地铁 6 号线）", "city":"昆明", "lat":25.1089, "lon":102.9270, "for":"长水机场 ↔ 市区 约 45 min"},
        {"key":"Dongfeng", "name":"东风广场站（地铁 2/3 号线）", "city":"昆明", "lat":25.0373, "lon":102.7119, "for":"市中心换乘"},
        # 保山暂无地铁
    ]
}

# ============ hotels.json（每城 3 家，离游玩地近）============
hotels = {
    "昆明": {
        "city": "昆明", "center": [25.04, 102.71],
        "total": 3,
        "candidates": [
            {"id":"km_h1", "name":"昆明翠湖宾馆", "kind":"hotel", "lat":25.0509, "lon":102.7005,
             "stars":4, "street":"翠湖南路 6 号", "postcode":"650031",
             "city":"昆明", "country":"中国",
             "note":"翠湖公园东门正对面，步行 3 min；陆军讲武堂 5 min"},
            {"id":"km_h2", "name":"昆明洲际酒店", "kind":"hotel", "lat":25.0395, "lon":102.7140,
             "stars":5, "street":"东风西路 9 号", "postcode":"650031",
             "city":"昆明", "country":"中国",
             "note":"东风广场旁、市中心核心；金马碧鸡坊步行 15 min"},
            {"id":"km_h3", "name":"昆明君悦酒店", "kind":"hotel", "lat":25.0178, "lon":102.6830,
             "stars":5, "street":"南滨路 8 号", "postcode":"650228",
             "city":"昆明", "country":"中国",
             "note":"滇池路；大观楼步行 5 min + 滇池观景"},
        ],
        "picks": ["昆明翠湖宾馆"]
    },
    "腾冲": {
        "city": "腾冲", "center": [25.02, 98.49],
        "total": 3,
        "candidates": [
            {"id":"tc_h1", "name":"和顺古镇·安之若宿精品客栈", "kind":"hotel", "lat":25.0159, "lon":98.4575,
             "stars":4, "street":"和顺古镇十字街 14 号", "postcode":"679100",
             "city":"腾冲", "country":"中国",
             "note":"住在古镇里；早/晚可独享古镇（游客散尽后最美）"},
            {"id":"tc_h2", "name":"腾冲热海·浴谷温泉酒店", "kind":"hotel", "lat":24.9920, "lon":98.4885,
             "stars":4, "street":"热海景区内", "postcode":"679100",
             "city":"腾冲", "country":"中国",
             "note":"景区内住宿；含温泉无限次泡，避开白天人流"},
            {"id":"tc_h3", "name":"腾冲火山·玛御谷温泉小镇客栈", "kind":"hotel", "lat":25.2180, "lon":98.4960,
             "stars":3, "street":"火山景区南 2 km", "postcode":"679100",
             "city":"腾冲", "country":"中国",
             "note":"近火山公园；适合自驾或包车；田园风光"},
        ],
        "picks": ["和顺古镇·安之若宿精品客栈"]
    },
    "保山": {
        "city": "保山", "center": [25.12, 99.16],
        "total": 3,
        "candidates": [
            {"id":"bs_h1", "name":"保山永昌大酒店", "kind":"hotel", "lat":25.1110, "lon":99.1580,
             "stars":4, "street":"永昌路 18 号", "postcode":"678000",
             "city":"保山", "country":"中国",
             "note":"永昌古城内；易罗池步行 10 min、太保山步行 15 min"},
            {"id":"bs_h2", "name":"保山青华海酒店", "kind":"hotel", "lat":25.1198, "lon":99.2080,
             "stars":4, "street":"青华海环湖路 1 号", "postcode":"678000",
             "city":"保山", "country":"中国",
             "note":"青华海旁湿地公园；适合晚散步看日落"},
            {"id":"bs_h3", "name":"保山云瑞机场宾馆", "kind":"hotel", "lat":25.0528, "lon":99.1670,
             "stars":3, "street":"云瑞机场路", "postcode":"678000",
             "city":"保山", "country":"中国",
             "note":"近云瑞机场；回程当天首选（省转场时间）"},
        ],
        "picks": ["保山永昌大酒店"]
    }
}

# ============ itineraries.json（5 天方案 D）============
itin = {
    "title": "方案 D · 云南腾冲保山 5 天赏秋",
    "subtitle": "银杏季 + 火山地热 + 滇缅抗战史",
    "pros": [
        "机票均已出票落地（南航/祥鹏/湖南航空），总价较原预算可控",
        "11 月下旬–12 月初为银杏村最佳期（11/19–11/21 满村金黄）",
        "腾冲占 3 晚，覆盖热海/火山/北海湿地/和顺古镇/银杏村核心圈",
        "保山 1 晚（11/21 当晚回程），节奏不赶"
    ],
    "cons": [
        "11/18 下午才到腾冲，损失一天",
        "11/21 保山仅 3 小时，需精简景点（易罗池+青华海）",
        "11 月已是云南旱季，紫外线强、温差大（早晚 5°C / 中午 22°C）"
    ],
    "stay": [
        ["昆明", 1],
        ["腾冲", 3],
        ["保山", 1]
    ],
    "route": "深圳 → 昆明 → 腾冲 → 保山 → 深圳",
    "days": [
        {
            "date":"11/17", "w":"周三", "city":"昆明",
            "items": ["云南陆军讲武堂","翠湖公园","金马碧鸡坊","大观楼","云南省博物馆"],
            "flight":{"no":"MU5732", "dep":"CAN T3", "time":"11:20→13:55", "arr":"KMG"},
            "note":"广州白云 T3 → 昆明长水；落地后地铁 6 号线入市区；下午集中翠湖片（讲武堂+翠湖+金马碧鸡坊步行连游）→ 晚饭前大观楼看滇池日落 → 晚饭祥云美食城",
            "stay":"昆明"
        },
        {
            "date":"11/18", "w":"周四", "city":"腾冲",
            "items": ["叠水河瀑布","国殇墓园","滇缅抗战博物馆"],
            "flight":{"no":"8L9951", "dep":"KMG", "time":"13:35→14:50", "arr":"TCG"},
            "transit":"上午: 酒店退房 → 地铁 6 号线回长水机场 → 13:35 起飞",
            "note":"上午 09:00 退房 → 翠湖公园晨练（看红嘴鸥起飞）→ 10:30 地铁 6 号线回机场；落地腾冲驼峰机场后取车/包车送酒店；下午逛腾冲老城（叠水河瀑布+国殇墓园+滇缅抗战博物馆三个点都步行 10 min 内）",
            "stay":"腾冲"
        },
        {
            "date":"11/19", "w":"周五", "city":"腾冲",
            "items": ["和顺古镇","热海（地热温泉）"],
            "note":"上午和顺古镇（4h），下午热海泡温泉（建议 14:00–17:00 旺季后段，避开早 10–13 点温泉池拥挤）；晚归腾冲市区",
            "stay":"腾冲"
        },
        {
            "date":"11/20", "w":"周六", "city":"腾冲",
            "items": ["火山地热国家地质公园","北海湿地","银杏村（江东）"],
            "note":"全天包车线路：早 8:30 火山公园（小空山 1.5h）→ 北海湿地（1.5h）→ 银杏村（江东）（2h）；回腾冲市区晚饭",
            "stay":"腾冲"
        },
        {
            "date":"11/21", "w":"周日", "city":"保山",
            "items": ["易罗池","青华海国家湿地公园"],
            "transit":"上午: 腾冲 → 保山 约 170 km / 3h（高速 G56；可包车或到腾冲汽车站坐班车）",
            "flight":{"no":"A67310", "dep":"BSD", "time":"20:30→23:05", "arr":"SZX"},
            "note":"上午退房 09:00 出发 → 中午抵保山酒店；下午易罗池 1h → 青华海散步 1.5h（看日落）→ 18:30 退房去机场 → 20:30 飞深圳",
            "stay":"保山（短停）"
        }
    ]
}

# 写所有数据
base = r'D:\Proj\Trip_2027_11_YunNan\planning\data'
with open(f'{base}/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, ensure_ascii=False, indent=2)
with open(f'{base}/transit.json', 'w', encoding='utf-8') as f:
    json.dump(transit, f, ensure_ascii=False, indent=2)
with open(f'{base}/hotels.json', 'w', encoding='utf-8') as f:
    json.dump(hotels, f, ensure_ascii=False, indent=2)
with open(f'{base}/itineraries.json', 'w', encoding='utf-8') as f:
    json.dump({"D": itin}, f, ensure_ascii=False, indent=2)

# 验证无 orphan
used = set()
for d in itin['days']:
    for nm in d.get('items', []):
        used.add(nm)
orphans = [p['name'] for p in places if p['name'] not in used]
print(f"places={len(places)}, used={len(used)}, orphans={orphans if orphans else '✅none'}")
print(f"hotels={sum(len(h['candidates']) for h in hotels.values())} 家")
print(f"transit: {len(transit['points'])} points + {len(transit['metro'])} metro")
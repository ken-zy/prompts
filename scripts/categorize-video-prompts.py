"""
categorize-video-prompts.py

Prompt categorization script for YouMind Seedance 2.0 video prompt library.
Classifies 1753+ video prompts into a 13-category taxonomy using regex keyword rules.

Tasks implemented:
  Task 1 - Taxonomy data structure and keyword rules
  Task 2 - Classification function
  Task 3 - Markdown generation
  Task 4 - Main pipeline and validation
"""

import json
import os
import re
import shutil
import sys
from collections import defaultdict

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

INPUT_FILE = "40_Reference/Articles/20260414/youmind-seedance-2.0-all-prompts.json"
OUTPUT_DIR = "prompts_video"

# ---------------------------------------------------------------------------
# Task 1: Taxonomy
# ---------------------------------------------------------------------------

TAXONOMY = {
    "电影感与叙事": [
        "电影级短片",
        "预告片与片头",
        "情感叙事",
        "一镜到底",
        "综合电影",
    ],
    "动作与格斗": [
        "武术格斗",
        "追逐与爆炸",
        "超级英雄",
        "综合动作",
    ],
    "舞蹈与音乐": [
        "街舞与现代舞",
        "古典与传统舞",
        "音乐节奏",
        "综合舞蹈",
    ],
    "动漫与动画": [
        "日系动漫",
        "卡通动画",
        "定格动画",
        "综合动画",
    ],
    "广告与商业": [
        "产品广告",
        "美食饮料广告",
        "奢侈品广告",
        "品牌宣传",
        "综合广告",
    ],
    "科幻与奇幻": [
        "赛博朋克",
        "太空科幻",
        "奇幻魔法",
        "末日废土",
        "综合科幻",
    ],
    "恐怖与悬疑": [
        "恐怖短片",
        "悬疑惊悚",
        "暗黑氛围",
        "综合恐怖",
    ],
    "自然与风景": [
        "自然风光",
        "城市景观",
        "航拍与延时",
        "综合风景",
    ],
    "人物与肖像": [
        "电影肖像",
        "Vlog风格",
        "情侣与浪漫",
        "综合人物",
    ],
    "萌宠与可爱": [
        "猫咪",
        "狗狗",
        "其他动物",
        "综合萌宠",
    ],
    "时尚与生活": [
        "时装展示",
        "运动健身",
        "日常生活",
        "综合时尚",
    ],
    "特效与实验": [
        "VFX特效",
        "转场效果",
        "风格实验",
        "综合特效",
    ],
    "其他": [
        "未分类",
    ],
}

# ---------------------------------------------------------------------------
# Subcategory keyword rules
# Order matters: more specific patterns first within each category group.
# All patterns are matched case-insensitively against concatenated prompt text.
# ---------------------------------------------------------------------------

SUBCATEGORY_RULES = {
    # ---- 电影感与叙事 ----
    "一镜到底": [
        r"一镜到底",
        r"single.*shot",
        r"one.*take",
        r"one.?shot.*film",
        r"oner.*shot",
        r"long.*take",
        r"continuous.*shot",
        r"uncut.*shot",
    ],
    "预告片与片头": [
        r"预告片",
        r"trailer",
        r"片头",
        r"title.*sequence",
        r"opening.*sequence",
        r"opening.*credits",
        r"intro.*sequence",
        r"teaser.*trailer",
        r"movie.*trailer",
        r"film.*trailer",
        r"片尾",
        r"end.*credits",
    ],
    "情感叙事": [
        r"情感.*叙事",
        r"emotional.*storytelling",
        r"emotional.*narrative",
        r"情感.*故事",
        r"感人.*故事",
        r"touching.*story",
        r"heartfelt.*story",
        r"dramatic.*story",
        r"narrative.*film",
        r"短故事",
        r"short.*story.*film",
        r"感人.*短片",
        r"催泪",
    ],
    "电影级短片": [
        r"电影.*短片",
        r"电影.*级",
        r"cinematic.*short",
        r"short.*film",
        r"短片",
        r"电影.*场景",
        r"cinematic.*scene",
        r"film.*scene",
        r"电影感",
        r"cinematic.*shot",
        r"cinematic.*footage",
        r"cinema.*quality",
        r"film.*quality",
        r"电影.*画面",
        r"电影.*风格",
        r"cinematic.*style",
        r"电影.*感",
        r"cinematic",
        r"电影",
    ],
    "综合电影": [
        r"叙事.*视频",
        r"narrative.*video",
        r"storytelling.*video",
        r"剧情.*视频",
        r"drama.*video",
        r"film.*video",
        r"multi.*shot.*film",
        r"多镜头.*短片",
        r"multi.*scene.*film",
        r"多场景.*短片",
        r"documentary.*style",
        r"纪录片.*风格",
        r"历史.*短片",
        r"historical.*short.*film",
        r"战争.*短片",
        r"war.*short.*film",
        r"对话.*场景",
        r"dialogue.*scene",
        r"喜剧.*场景",
        r"comedy.*scene",
        r"情景喜剧",
        r"sitcom",
        r"警察.*场景",
        r"police.*scene",
        r"hospital.*scene",
        r"医院.*场景",
        r"ktv.*场景",
        r"派对.*场景",
        r"party.*scene.*video",
        r"博物馆.*场景",
        r"museum.*scene",
        r"古风.*短片",
        r"甜宠",
        r"short.*drama",
        r"短剧",
        r"言情.*视频",
        r"角色.*一致性",
        r"character.*consistency",
        r"保持.*一致",
        r"参考.*视频.*生成",
        r"reference.*video.*generation",
        r"视频.*对比",
        r"video.*comparison",
        r"角色.*转换",
        r"character.*transform",
        r"pov.*interaction",
        r"ai.*girlfriend",
        r"ai.*女友",
        r"角色扮演.*模特",
        r"实验室.*工作",
        r"laboratory.*scene",
    ],

    # ---- 动作与格斗 ----
    "武术格斗": [
        r"武术",
        r"格斗",
        r"打斗",
        r"martial.*art",
        r"kung.*fu",
        r"功夫",
        r"combat.*fight",
        r"fighting.*scene",
        r"fight.*choreograph",
        r"sword.*fight",
        r"刀.*打",
        r"剑.*打",
        r"武打",
        r"搏斗",
        r"拳击",
        r"boxing",
        r"kickboxing",
        r"mma.*fight",
        r"ufc.*fight",
        r"ninja.*fight",
        r"忍者",
        r"samurai.*fight",
        r"武士",
        r"gladiator",
        r"battle.*scene",
        r"战斗.*场景",
        r"combat.*scene",
        r"fight.*video",
        r"战斗.*序列",
        r"battle.*sequence",
        r"warrior.*fight",
        r"战士.*战斗",
        r"nunchaku",
        r"双截棍",
        r"擂台",
        r"combat.*sequence",
    ],
    "追逐与爆炸": [
        r"追逐",
        r"car.*chase",
        r"chase.*scene",
        r"explosion",
        r"爆炸",
        r"high.*speed.*chase",
        r"action.*chase",
        r"pursuit.*scene",
        r"action.*sequence",
        r"stunt.*action",
        r"crash.*scene",
        r"action.*packed",
        r"high.*octane",
        r"坍塌",
        r"collapse.*scene",
        r"destruction.*scene",
        r"disaster.*scene",
        r"灾难.*场景",
        r"摩托车.*场景",
        r"motorcycle.*scene",
        r"race.*scene",
        r"赛车",
        r"street.*racing",
        r"竞速",
    ],
    "超级英雄": [
        r"超级英雄",
        r"superhero",
        r"super.*hero",
        r"marvel.*style",
        r"dc.*hero",
        r"hero.*power",
        r"superpower",
        r"超能力",
        r"变身.*英雄",
        r"hero.*transformation",
    ],
    "综合动作": [
        r"动作.*片",
        r"action.*movie",
        r"action.*film",
        r"动作.*场景",
        r"action.*scene",
        r"action.*video",
        r"动作.*视频",
        r"运动.*动作",
        r"intense.*action",
        r"action.*sequence",
    ],

    # ---- 舞蹈与音乐 ----
    "街舞与现代舞": [
        r"街舞",
        r"hip.*hop.*(?<![Ss][Ee][Ee])dance",
        r"k.?pop.*(?<![Ss][Ee][Ee])dance",
        r"breakdance",
        r"break.*(?<![Ss][Ee][Ee])dance",
        r"breaking.*(?<![Ss][Ee][Ee])dance",
        r"popping.*(?<![Ss][Ee][Ee])dance",
        r"locking.*(?<![Ss][Ee][Ee])dance",
        r"urban.*(?<![Ss][Ee][Ee])dance",
        r"freestyle.*(?<![Ss][Ee][Ee])dance",
        r"contemporary.*(?<![Ss][Ee][Ee])dance",
        r"tiktok.*(?<![Ss][Ee][Ee])dance",
        r"现代舞",
        r"爵士舞",
        r"jazz.*(?<![Ss][Ee][Ee])dance",
        r"krump",
        r"waacking",
        r"michael.*jackson.*(?<![Ss][Ee][Ee])dance",
        r"moonwalk.*(?<![Ss][Ee][Ee])dance",
        r"迈克尔.*杰克逊.*舞",
        r"嘻哈.*舞",
    ],
    "古典与传统舞": [
        r"古典.*舞",
        r"古典舞",
        r"ballet",
        r"芭蕾",
        r"民族舞",
        r"traditional.*(?<![Ss][Ee][Ee])dance",
        r"folk.*(?<![Ss][Ee][Ee])dance",
        r"classical.*(?<![Ss][Ee][Ee])dance",
        r"中国.*舞",
        r"chinese.*(?<![Ss][Ee][Ee])dance",
        r"flamenco",
        r"tango.*(?<![Ss][Ee][Ee])dance",
        r"waltz",
        r"传统.*舞蹈",
        r"宫廷.*舞",
        r"汉唐.*舞",
        r"宝莱坞",
        r"bollywood.*(?<![Ss][Ee][Ee])dance",
        r"bollywood",
        r"敦煌.*飞天",
        r"飞天.*舞",
        r"歌舞.*古典",
        r"古风.*舞",
        r"国风.*舞",
    ],
    "音乐节奏": [
        r"音乐.*节奏",
        r"music.*rhythm",
        r"music.*video",
        r"mv.*制作",
        r"mv.*风格",
        r"music.*clip",
        r"音乐.*视频",
        r"beat.*sync",
        r"rhythm.*sync",
        r"音乐.*短片",
        r"演唱.*视频",
        r"concert.*video",
        r"live.*performance.*video",
        r"音乐.*表演",
    ],
    "综合舞蹈": [
        r"舞蹈",
        r"(?<![Ss][Ee][Ee])dance\b",
        r"跳舞",
        r"(?<![Ss][Ee][Ee])dancer\b",
        r"舞者",
        r"舞步",
        r"(?<![Ss][Ee][Ee])dancing\b",
    ],

    # ---- 动漫与动画 ----
    "日系动漫": [
        r"日系动漫",
        r"动漫.*风格",
        r"anime.*style",
        r"anime.*video",
        r"anime.*animation",
        r"日本.*动漫",
        r"二次元.*动画",
        r"anime.*film",
        r"manga.*animation",
        r"动漫.*短片",
        r"日漫",
        r"anime",
        r"动漫",
    ],
    "定格动画": [
        r"定格动画",
        r"stop.*motion",
        r"claymation",
        r"clay.*animation",
        r"puppet.*animation",
        r"frame.*by.*frame",
        r"逐帧.*动画",
    ],
    "卡通动画": [
        r"卡通.*动画",
        r"cartoon.*animation",
        r"animated.*cartoon",
        r"disney.*style",
        r"pixar.*style",
        r"3d.*animation",
        r"cgi.*animation",
        r"animated.*film",
        r"animation.*short",
        r"动画.*短片",
        r"卡通.*短片",
        r"animated.*video",
        r"动画.*视频",
    ],
    "综合动画": [
        r"动画",
        r"animation",
        r"animated",
        r"卡通",
        r"cartoon",
    ],

    # ---- 广告与商业 ----
    "美食饮料广告": [
        r"美食.*广告",
        r"food.*commercial",
        r"food.*ad",
        r"饮料.*广告",
        r"drink.*commercial",
        r"drink.*ad",
        r"coffee.*commercial",
        r"coffee.*ad",
        r"beverage.*ad",
        r"restaurant.*ad",
        r"cuisine.*ad",
        r"burger.*ad",
        r"food.*brand",
        r"食品.*广告",
        r"美食.*视频",
    ],
    "奢侈品广告": [
        r"奢侈品.*广告",
        r"luxury.*commercial",
        r"luxury.*ad",
        r"luxury.*brand",
        r"高端.*广告",
        r"premium.*commercial",
        r"fashion.*commercial",
        r"fashion.*ad",
        r"jewel.*commercial",
        r"jewel.*ad",
        r"perfume.*commercial",
        r"perfume.*ad",
        r"香水.*广告",
        r"珠宝.*广告",
        r"高奢.*广告",
    ],
    "产品广告": [
        r"产品.*广告",
        r"product.*commercial",
        r"product.*ad",
        r"商品.*广告",
        r"tech.*commercial",
        r"tech.*ad",
        r"phone.*commercial",
        r"car.*commercial",
        r"汽车.*广告",
        r"车.*广告",
        r"电子.*广告",
        r"科技.*广告",
        r"产品.*宣传",
    ],
    "品牌宣传": [
        r"品牌.*宣传",
        r"brand.*promotion",
        r"brand.*video",
        r"企业.*宣传",
        r"corporate.*video",
        r"company.*video",
        r"brand.*film",
        r"宣传.*片",
        r"品牌.*片",
        r"promotional.*video",
        r"brand.*story",
        r"品牌.*故事",
    ],
    "综合广告": [
        r"广告",
        r"commercial",
        r"\bad\b.*video",
        r"video.*\bad\b",
        r"advertisement",
        r"宣传.*视频",
        r"营销.*视频",
        r"marketing.*video",
    ],

    # ---- 科幻与奇幻 ----
    "赛博朋克": [
        r"赛博朋克",
        r"cyberpunk",
        r"赛博.*城市",
        r"cyber.*city",
        r"neon.*city",
        r"neon.*future",
        r"dystopian.*city",
        r"futuristic.*neon",
        r"blade.*runner",
        r"bladerunner",
        r"cyber.*future",
        r"霓虹.*城市",
        r"赛博",
    ],
    "太空科幻": [
        r"太空",
        r"space.*sci.*fi",
        r"sci.*fi.*space",
        r"outer.*space",
        r"spacecraft",
        r"spaceship",
        r"宇宙飞船",
        r"星际",
        r"interstellar",
        r"galaxy.*sci",
        r"astronaut",
        r"宇航员",
        r"space.*travel",
        r"space.*station",
        r"太空.*探索",
        r"star.*wars.*style",
        r"space.*battle",
        r"宇宙.*战争",
    ],
    "末日废土": [
        r"末日",
        r"废土",
        r"post.*apocalyptic",
        r"post.*apocalypse",
        r"dystopian",
        r"dystopia",
        r"apocalypse",
        r"wasteland",
        r"末世",
        r"末日.*世界",
        r"灾后",
        r"zombie.*apocalypse",
        r"nuclear.*wasteland",
    ],
    "奇幻魔法": [
        r"奇幻",
        r"魔法",
        r"fantasy.*magic",
        r"magic.*world",
        r"magical.*world",
        r"dragon.*fantasy",
        r"魔幻",
        r"fantasy.*realm",
        r"enchanted",
        r"wizard.*magic",
        r"witch.*magic",
        r"巫师",
        r"中世纪.*奇幻",
        r"medieval.*fantasy",
        r"high.*fantasy",
        r"epic.*fantasy",
        r"神话.*世界",
        r"mythology.*video",
    ],
    "综合科幻": [
        r"科幻",
        r"sci.*fi",
        r"science.*fiction",
        r"futuristic",
        r"未来.*世界",
        r"future.*world",
        r"alien",
        r"外星",
        r"robot.*future",
        r"机器人.*未来",
        r"高科技.*世界",
        r"high.*tech.*world",
        r"mech.*suit",
        r"机甲",
        r"mecha",
        r"android",
        r"安卓",
        r"robot.*scene",
        r"machine.*future",
        r"3d.*geometric",
        r"geometric.*space",
        r"几何.*空间",
        r"infinite.*space",
        r"无限.*空间",
    ],

    # ---- 恐怖与悬疑 ----
    "恐怖短片": [
        r"恐怖.*短片",
        r"horror.*short",
        r"horror.*film",
        r"horror.*video",
        r"scary.*short",
        r"scary.*video",
        r"horror.*clip",
        r"恐怖.*视频",
    ],
    "悬疑惊悚": [
        r"悬疑",
        r"惊悚",
        r"thriller",
        r"mystery.*film",
        r"mystery.*video",
        r"suspense.*film",
        r"suspense.*video",
        r"psychological.*thriller",
        r"心理.*惊悚",
        r"crime.*thriller",
        r"detective.*scene",
        r"noir.*film",
        r"noir.*scene",
    ],
    "暗黑氛围": [
        r"暗黑",
        r"dark.*atmosphere",
        r"dark.*aesthetic",
        r"gothic.*video",
        r"gothic.*scene",
        r"ominous.*scene",
        r"creepy.*atmosphere",
        r"eerie.*scene",
        r"sinister.*scene",
        r"dark.*cinematic",
        r"黑暗.*氛围",
        r"阴暗.*氛围",
        r"诡异",
    ],
    "综合恐怖": [
        r"恐怖",
        r"horror",
        r"scary",
        r"frightening",
        r"fear.*video",
        r"ghost.*video",
        r"鬼",
        r"haunted",
    ],

    # ---- 自然与风景 ----
    "航拍与延时": [
        r"航拍",
        r"aerial.*shot",
        r"aerial.*footage",
        r"drone.*shot",
        r"drone.*footage",
        r"bird.*eye.*view",
        r"鸟瞰",
        r"延时",
        r"time.*lapse",
        r"timelapse",
        r"hyperlapse",
        r"超时空",
        r"4k.*drone",
        r"aerial.*video",
    ],
    "城市景观": [
        r"城市.*景观",
        r"cityscape.*video",
        r"city.*view.*video",
        r"urban.*landscape",
        r"城市.*夜景",
        r"city.*night.*view",
        r"skyline.*video",
        r"street.*scene.*video",
        r"城市.*风光",
        r"metropolitan.*scene",
        r"城市.*街道",
        r"city.*street.*video",
    ],
    "自然风光": [
        r"自然.*风光",
        r"natural.*scenery",
        r"nature.*footage",
        r"nature.*video",
        r"landscape.*video",
        r"mountain.*scenery",
        r"forest.*scenery",
        r"ocean.*scenery",
        r"sunset.*scenery",
        r"sunrise.*scenery",
        r"自然.*风景",
        r"大自然",
        r"natural.*beauty",
        r"scenic.*video",
        r"outdoor.*footage",
        r"wilderness.*video",
        r"海景",
        r"山景",
        r"风景.*视频",
        r"surfing",
        r"冲浪",
        r"underwater.*scene",
        r"water.*scene",
        r"ocean.*video",
        r"sea.*scene",
        r"coral.*reef",
        r"珊瑚礁",
        r"水下.*场景",
        r"海洋.*场景",
        r"海浪",
        r"wave.*video",
        r"windsurfing",
        r"峡谷",
        r"canyon",
        r"翼装",
        r"wingsuit",
        r"skydiv",
        r"钟表匠",
        r"乡村.*场景",
        r"rural.*scene",
    ],
    "综合风景": [
        r"风景",
        r"scenery",
        r"landscape",
        r"scene.*view",
        r"vista",
        r"panorama",
        r"风光",
        r"美景",
    ],

    # ---- 人物与肖像 ----
    "情侣与浪漫": [
        r"情侣",
        r"couple.*video",
        r"romantic.*video",
        r"romance.*film",
        r"love.*story.*video",
        r"爱情.*故事",
        r"romantic.*scene",
        r"浪漫.*场景",
        r"约会.*视频",
        r"date.*video",
        r"婚礼.*视频",
        r"wedding.*video",
        r"爱情.*短片",
    ],
    "Vlog风格": [
        r"vlog",
        r"daily.*vlog",
        r"travel.*vlog",
        r"lifestyle.*vlog",
        r"日常.*vlog",
        r"旅行.*vlog",
        r"点评.*视频",
        r"review.*video",
        r"pov.*video",
        r"first.*person.*video",
        r"第一视角",
    ],
    "电影肖像": [
        r"电影.*肖像",
        r"cinematic.*portrait.*video",
        r"portrait.*video",
        r"人物.*特写",
        r"close.*up.*portrait",
        r"人物.*肖像",
        r"character.*portrait",
        r"人物.*刻画",
    ],
    "综合人物": [
        r"人物.*视频",
        r"人物.*短片",
        r"人像.*视频",
        r"portrait.*film",
        r"人物.*故事",
        r"个人.*短片",
        r"young.*man.*cafe",
        r"young.*woman.*cafe",
        r"男子.*咖啡",
        r"女子.*咖啡",
        r"甜品.*自拍",
        r"selfie.*scene",
        r"人物.*写真.*视频",
        r"character.*portrait.*video",
    ],

    # ---- 萌宠与可爱 ----
    "猫咪": [
        r"猫",
        r"\bcat\b",
        r"kitten",
        r"猫咪",
        r"猫.*视频",
        r"cat.*video",
        r"feline",
        r"tabby",
        r"persian.*cat",
        r"british.*shorthair",
        r"maine.*coon",
        r"猫.*动作",
    ],
    "狗狗": [
        r"狗",
        r"\bdog\b",
        r"puppy",
        r"狗狗",
        r"狗.*视频",
        r"dog.*video",
        r"canine",
        r"doggy",
        r"golden.*retriever",
        r"labrador",
        r"poodle",
        r"husky",
        r"柴犬",
    ],
    "其他动物": [
        r"动物.*视频",
        r"animal.*video",
        r"wildlife.*video",
        r"bird.*video",
        r"bird.*flight",
        r"鸟.*飞",
        r"野生.*动物",
        r"wild.*animal",
        r"horse.*video",
        r"马.*视频",
        r"rabbit.*video",
        r"兔.*视频",
        r"panda.*video",
        r"熊猫",
        r"bear.*video",
        r"bear.*scene",
        r"dolphin",
        r"shark",
        r"鲨",
        r"鲸",
        r"whale",
        r"orca",
        r"虎鲸",
        r"恐龙",
        r"dinosaur",
        r"dragon.*creature",
        r"dragon.*video",
        r"龙.*视频",
        r"黑曜石.*龙",
        r"水晶.*龙",
        r"kaiju",
        r"怪兽",
        r"monster.*creature",
        r"腊肠犬",
        r"dachshund",
        r"parrot",
        r"鹦鹉",
        r"wolf",
        r"狼",
        r"lightning.*wolf",
        r"leopard",
        r"豹子",
        r"hamster",
        r"仓鼠",
        r"巨兽",
        r"prehistoric.*beast",
        r"史前.*兽",
        r"whale.*video",
        r"鱼.*视频",
        r"fish.*video",
    ],
    "综合萌宠": [
        r"宠物",
        r"\bpet\b",
        r"cute.*animal",
        r"可爱.*动物",
        r"萌.*宠",
        r"cute.*pet",
        r"animal.*cute",
    ],

    # ---- 时尚与生活 ----
    "时装展示": [
        r"时装.*展示",
        r"fashion.*show",
        r"fashion.*video",
        r"fashion.*film",
        r"时装.*秀",
        r"runway.*video",
        r"model.*walk",
        r"catwalk",
        r"fashion.*week.*video",
        r"时尚.*视频",
        r"服装.*展示",
        r"outfit.*video",
        r"穿搭.*视频",
        r"styling.*video",
        r"lookbook.*video",
    ],
    "运动健身": [
        r"运动.*视频",
        r"fitness.*video",
        r"workout.*video",
        r"gym.*video",
        r"exercise.*video",
        r"sport.*video",
        r"athlete.*video",
        r"training.*video",
        r"运动.*短片",
        r"健身.*视频",
        r"跑步",
        r"running.*video",
        r"basketball.*video",
        r"basketball.*scene",
        r"篮球",
        r"football.*video",
        r"soccer.*video",
        r"极限.*运动",
        r"extreme.*sport",
        r"skateboard",
        r"parkour",
        r"跑酷",
        r"冲浪.*运动",
        r"surf.*sport",
        r"sport.*scene",
    ],
    "日常生活": [
        r"日常.*生活",
        r"daily.*life.*video",
        r"everyday.*life.*video",
        r"生活.*场景",
        r"life.*scene.*video",
        r"日常.*场景",
        r"slice.*of.*life",
        r"生活.*记录",
        r"morning.*routine",
        r"生活.*片段",
    ],
    "综合时尚": [
        r"时尚",
        r"fashion",
        r"生活.*方式",
        r"lifestyle.*video",
        r"\blifestyle\b.*video",
        r"生活.*video",
        r"日常.*video",
    ],

    # ---- 特效与实验 ----
    "VFX特效": [
        r"vfx",
        r"visual.*effect",
        r"特效",
        r"cgi.*video",
        r"cgi.*scene",
        r"motion.*graphic",
        r"动态图形",
        r"particle.*effect",
        r"粒子.*特效",
        r"explosion.*effect",
        r"爆炸.*特效",
        r"魔法.*特效",
        r"magic.*effect",
        r"light.*effect.*video",
        r"发光.*特效",
        r"fire.*effect",
        r"water.*effect",
        r"smoke.*effect",
        r"变身.*效果",
        r"transformation.*effect",
        r"变形.*效果",
        r"morph.*effect",
        r"万花筒",
        r"kaleidoscope",
        r"dimensional.*slash",
        r"空间斩",
        r"glowing.*effect",
        r"light.*trail",
        r"光轨",
    ],
    "转场效果": [
        r"转场",
        r"transition.*effect",
        r"transition.*video",
        r"seamless.*transition",
        r"smooth.*transition",
        r"morph.*transition",
        r"warp.*transition",
        r"cut.*effect",
        r"场景.*转换",
        r"换装",
        r"outfit.*change",
        r"costume.*change",
        r"变装",
        r"color.*change.*video",
        r"色彩.*变换",
        r"color.*transition",
    ],
    "风格实验": [
        r"风格.*实验",
        r"experimental.*video",
        r"experimental.*film",
        r"avant.*garde",
        r"abstract.*video",
        r"abstract.*film",
        r"glitch.*art",
        r"glitch.*video",
        r"lo.*fi.*video",
        r"retro.*effect",
        r"vintage.*effect",
        r"film.*grain",
        r"aesthetic.*video",
        r"art.*film",
        r"实验.*短片",
        r"抽象.*视频",
        r"梵高.*风格",
        r"van.*gogh.*style.*video",
        r"印象派.*视频",
        r"impressionist.*video",
        r"impressionism.*video",
        r"monet.*style.*video",
        r"卢梭.*风格",
        r"rousseau.*style.*video",
        r"油画.*风格.*视频",
        r"painting.*style.*video",
        r"水墨.*风格.*视频",
        r"ink.*style.*video",
        r"艺术.*风格.*视频",
        r"art.*style.*video",
        r"britto.*style",
        r"turner.*style",
        r"超现实.*视频",
        r"surreal.*video",
    ],
    "综合特效": [
        r"特效.*视频",
        r"effect.*video",
        r"视觉.*效果",
        r"visual.*video",
        r"3d.*video",
        r"render.*video",
        r"rendered.*video",
        r"cg.*video",
        r"数字.*艺术.*视频",
        r"digital.*art.*video",
    ],
}

# ---------------------------------------------------------------------------
# Related pairs (bidirectional, ~25 curated pairs)
# ---------------------------------------------------------------------------

RELATED_PAIRS = [
    ("电影级短片", "预告片与片头"),
    ("电影级短片", "电影肖像"),
    ("一镜到底", "电影级短片"),
    ("情感叙事", "情侣与浪漫"),
    ("武术格斗", "追逐与爆炸"),
    ("武术格斗", "超级英雄"),
    ("日系动漫", "卡通动画"),
    ("日系动漫", "VFX特效"),
    ("赛博朋克", "太空科幻"),
    ("赛博朋克", "城市景观"),
    ("末日废土", "太空科幻"),
    ("奇幻魔法", "VFX特效"),
    ("产品广告", "品牌宣传"),
    ("美食饮料广告", "日常生活"),
    ("奢侈品广告", "时装展示"),
    ("恐怖短片", "悬疑惊悚"),
    ("暗黑氛围", "悬疑惊悚"),
    ("航拍与延时", "自然风光"),
    ("航拍与延时", "城市景观"),
    ("猫咪", "综合萌宠"),
    ("狗狗", "综合萌宠"),
    ("时装展示", "品牌宣传"),
    ("街舞与现代舞", "音乐节奏"),
    ("VFX特效", "转场效果"),
    ("风格实验", "VFX特效"),
]

# ---------------------------------------------------------------------------
# Derived lookups
# ---------------------------------------------------------------------------

# subcategory -> category
SUB_TO_CAT: dict[str, str] = {}
for _cat, _subs in TAXONOMY.items():
    for _sub in _subs:
        SUB_TO_CAT[_sub] = _cat

# bidirectional related map
RELATED_MAP: defaultdict[str, set] = defaultdict(set)
for _a, _b in RELATED_PAIRS:
    RELATED_MAP[_a].add(_b)
    RELATED_MAP[_b].add(_a)

ALL_SUBCATEGORIES: set[str] = set(SUB_TO_CAT.keys())
ALL_CATEGORIES: set[str] = set(TAXONOMY.keys())

# ---------------------------------------------------------------------------
# Task 2: Classification functions
# ---------------------------------------------------------------------------


def get_match_text(prompt: dict) -> str:
    """Concatenate title + description + content + translatedContent, lowercased."""
    parts = [
        prompt.get("title", "") or "",
        prompt.get("description", "") or "",
        prompt.get("content", "") or "",
        prompt.get("translatedContent", "") or "",
    ]
    return " ".join(parts).lower()


def classify_prompt(prompt: dict) -> tuple[str, str, list[str]]:
    """
    Classify a prompt dict into (category, subcategory, related_list).

    Iterates SUBCATEGORY_RULES in dict order (specificity ordering).
    Collects ALL matching subcategories.
    Primary = first match.
    Cross-category related = other matches from DIFFERENT parent categories (max 3).
    No match -> ("其他", "未分类", []).
    """
    text = get_match_text(prompt)

    matched_subs: list[str] = []

    for subcategory, patterns in SUBCATEGORY_RULES.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                if subcategory not in matched_subs:
                    matched_subs.append(subcategory)
                break  # no need to check remaining patterns for this subcategory

    if not matched_subs:
        return ("其他", "未分类", [])

    primary_sub = matched_subs[0]
    primary_cat = SUB_TO_CAT[primary_sub]

    # Cross-category related: other matches from DIFFERENT parent categories
    cross_cat_related: list[str] = []
    for sub in matched_subs[1:]:
        cat = SUB_TO_CAT[sub]
        if cat != primary_cat and sub not in cross_cat_related:
            cross_cat_related.append(sub)
        if len(cross_cat_related) >= 3:
            break

    return (primary_cat, primary_sub, cross_cat_related)


# ---------------------------------------------------------------------------
# Task 2: Test cases
# ---------------------------------------------------------------------------


def test_classification() -> None:
    """Run 5 synthetic test cases and print PASS/FAIL."""
    test_cases = [
        # (prompt_dict, expected_category, expected_subcategory, description)
        (
            {"title": "赛博朋克城市霓虹夜景", "description": "cyberpunk neon city night", "content": "", "translatedContent": ""},
            "科幻与奇幻",
            "赛博朋克",
            "赛博朋克 title",
        ),
        (
            {"title": "Hip hop dance freestyle", "description": "urban dance battle in the street", "content": "", "translatedContent": ""},
            "舞蹈与音乐",
            "街舞与现代舞",
            "hip hop dance description",
        ),
        (
            {"title": "Cat playing in the garden", "description": "cute kitten video", "content": "", "translatedContent": "猫咪在花园里玩耍"},
            "萌宠与可爱",
            "猫咪",
            "cat/kitten keyword match",
        ),
        (
            {"title": "Cinematic short film scene", "description": "A cinematic quality short film about love", "content": "", "translatedContent": ""},
            "电影感与叙事",
            "电影级短片",
            "cinematic short film",
        ),
        (
            {"title": "Something completely unrelated abc xyz 123", "description": "", "content": "", "translatedContent": ""},
            "其他",
            "未分类",
            "Unrelated → 其他/未分类",
        ),
    ]

    passed = 0
    failed = 0

    for prompt, exp_cat, exp_sub, desc in test_cases:
        cat, sub, related = classify_prompt(prompt)
        ok = (cat == exp_cat) and (sub == exp_sub)
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {desc}")
        if not ok:
            print(f"       Expected: {exp_cat}/{exp_sub}")
            print(f"       Got:      {cat}/{sub}")

    print(f"\nResults: {passed} passed, {failed} failed out of {len(test_cases)} tests")


# ---------------------------------------------------------------------------
# Taxonomy stats (for structure check)
# ---------------------------------------------------------------------------


def print_taxonomy_stats() -> None:
    """Print taxonomy statistics."""
    total_subs = sum(len(subs) for subs in TAXONOMY.values())
    total_rules = sum(len(patterns) for patterns in SUBCATEGORY_RULES.values())

    print("=== Taxonomy Stats ===")
    print(f"Categories:     {len(TAXONOMY)}")
    print(f"Subcategories:  {total_subs}")
    print(f"Rule entries:   {len(SUBCATEGORY_RULES)}")
    print(f"Total patterns: {total_rules}")
    print(f"Related pairs:  {len(RELATED_PAIRS)}")
    print()

    # Verify all subcategories have rules (excluding '未分类' which is a fallback)
    FALLBACK_SUBS = {"未分类"}
    subs_without_rules = (ALL_SUBCATEGORIES - set(SUBCATEGORY_RULES.keys())) - FALLBACK_SUBS
    if subs_without_rules:
        print(f"WARNING: subcategories without rules: {subs_without_rules}")
    else:
        print("All subcategories have rules (未分类 is intentionally fallback-only).")

    # Verify related pairs reference valid subcategories
    invalid_pairs = []
    for a, b in RELATED_PAIRS:
        if a not in ALL_SUBCATEGORIES:
            invalid_pairs.append(f"{a} (unknown)")
        if b not in ALL_SUBCATEGORIES:
            invalid_pairs.append(f"{b} (unknown)")
    if invalid_pairs:
        print(f"WARNING: invalid subcategories in RELATED_PAIRS: {invalid_pairs}")
    else:
        print("All related pairs reference valid subcategories.")


# ---------------------------------------------------------------------------
# Task 3: Markdown generation
# ---------------------------------------------------------------------------


def format_prompt_entry(prompt: dict, index: int) -> str:
    """Format one video prompt as a Markdown entry."""
    lines = []

    title = prompt.get("title") or "Untitled"
    lines.append(f"### {index}. {title}")
    lines.append("")

    # Meta line: Author, Date, Language
    meta_parts = []

    author_obj = prompt.get("author") or {}
    author_name = author_obj.get("name") or "" if isinstance(author_obj, dict) else ""
    author_link_url = author_obj.get("link") or "" if isinstance(author_obj, dict) else ""
    source_link = prompt.get("sourceLink") or ""

    if author_name:
        if source_link:
            meta_parts.append(f"**作者**: [{author_name}]({source_link})")
        elif author_link_url:
            meta_parts.append(f"**作者**: [{author_name}]({author_link_url})")
        else:
            meta_parts.append(f"**作者**: {author_name}")

    published_at = prompt.get("sourcePublishedAt") or ""
    if published_at:
        date_str = published_at[:10]
        meta_parts.append(f"**日期**: {date_str}")

    language = prompt.get("language") or ""
    if language:
        meta_parts.append(f"**语言**: {language}")

    if meta_parts:
        lines.append("  ".join(meta_parts))
        lines.append("")

    # Description blockquote
    description = prompt.get("description") or ""
    if description:
        for desc_line in description.strip().splitlines():
            lines.append(f"> {desc_line}")
        lines.append("")

    # Video section: use first video in videos array
    videos = prompt.get("videos") or []
    if videos and isinstance(videos, list) and len(videos) > 0:
        first_video = videos[0]
        if isinstance(first_video, dict):
            source_url = first_video.get("sourceUrl") or ""
            thumbnail = first_video.get("thumbnail") or ""
            if source_url or thumbnail:
                if source_url:
                    lines.append(f"**视频**: [观看视频]({source_url})")
                if thumbnail:
                    lines.append(f"![缩略图]({thumbnail})")
                lines.append("")

    # Prompt content in fenced code block
    content = prompt.get("content") or ""
    lines.append("**Prompt:**")
    lines.append("````")
    lines.append(content)
    lines.append("````")
    lines.append("")

    return "\n".join(lines)


def format_prompt_related(related_subs: list[str]) -> str:
    """Format the Related line with validated subcategory wiki links."""
    valid_links = [sub for sub in related_subs if sub in ALL_SUBCATEGORIES]
    if not valid_links:
        return ""
    links_str = "、".join(f"[[{sub}]]" for sub in valid_links)
    return f"**Related**: {links_str}"


def generate_subcategory_file(
    cat: str,
    sub: str,
    prompts_in_sub: list,  # list of (prompt_dict, related_list)
    related_subs: list[str],
) -> str:
    """Generate full subcategory .md content."""
    lines = []

    count = len(prompts_in_sub)

    # YAML frontmatter
    lines.append("---")
    lines.append(f"category: {cat}")
    lines.append(f"subcategory: {sub}")
    lines.append(f"count: {count}")
    lines.append("---")
    lines.append("")

    # Heading
    lines.append(f"# {sub}")
    lines.append("")

    # Upward link
    lines.append(f"所属大类：[[_{cat}]]")
    lines.append("")

    # Horizontal related links (validated against ALL_SUBCATEGORIES)
    valid_related = [s for s in related_subs if s in ALL_SUBCATEGORIES]
    if valid_related:
        links_str = "、".join(f"[[{s}]]" for s in valid_related)
        lines.append(f"相关分类：{links_str}")
        lines.append("")

    # Count line
    lines.append(f"共 {count} 个提示词")
    lines.append("")

    # All prompt entries separated by ---
    entries = []
    for idx, (prompt, prompt_related) in enumerate(prompts_in_sub, start=1):
        entry = format_prompt_entry(prompt, idx)

        # Add per-prompt related links
        related_line = format_prompt_related(prompt_related)
        if related_line:
            entry = entry.rstrip("\n") + "\n\n" + related_line + "\n\n"

        entries.append(entry)

    lines.append("---\n\n".join(entries))

    return "\n".join(lines)


def generate_category_index(cat: str, subcategory_counts: dict[str, int]) -> str:
    """Generate _{cat}.md content."""
    lines = []

    total = sum(subcategory_counts.values())

    lines.append(f"# {cat}")
    lines.append("")
    lines.append(f"共 {total} 个提示词")
    lines.append("")
    lines.append("## 子分类")
    lines.append("")

    # Sort by count descending
    sorted_subs = sorted(subcategory_counts.items(), key=lambda x: x[1], reverse=True)
    for sub, cnt in sorted_subs:
        lines.append(f"- [[{sub}]] ({cnt})")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("[[../00-Index.md|返回总索引]]")
    lines.append("")

    return "\n".join(lines)


def generate_master_index(category_stats: dict[str, dict[str, int]]) -> str:
    """Generate 00-Index.md content."""
    lines = []

    total_prompts = sum(
        cnt for sub_counts in category_stats.values() for cnt in sub_counts.values()
    )
    cat_count = len(category_stats)

    lines.append("# Seedance 2.0 Video Prompts")
    lines.append("")
    lines.append(f"共 {total_prompts} 个提示词，{cat_count} 个分类")
    lines.append("")
    lines.append("## 分类索引")
    lines.append("")

    for cat, sub_counts in category_stats.items():
        cat_total = sum(sub_counts.values())
        lines.append(f"### [[_{cat}]] ({cat_total})")
        lines.append("")
        sorted_subs = sorted(sub_counts.items(), key=lambda x: x[1], reverse=True)
        for sub, cnt in sorted_subs:
            lines.append(f"- [[{sub}]] ({cnt})")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Task 4: Main pipeline and validation
# ---------------------------------------------------------------------------


def run_pipeline() -> bool:
    """Load, classify, generate Markdown files, validate links."""
    # 1. Load JSON
    input_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        INPUT_FILE,
    )
    print(f"Loading prompts from: {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    prompts = data.get("prompts") or data
    if isinstance(prompts, dict):
        prompts = list(prompts.values())
    total = len(prompts)
    print(f"Loaded {total} prompts")

    # 2. Classify all prompts
    # classified[cat][sub] = list of (prompt, related_list)
    classified: defaultdict = defaultdict(lambda: defaultdict(list))
    for prompt in prompts:
        cat, sub, related = classify_prompt(prompt)
        classified[cat][sub].append((prompt, related))

    # 3. Compute category_stats
    category_stats: dict[str, dict[str, int]] = {}
    for cat in TAXONOMY:
        category_stats[cat] = {}
        for sub in TAXONOMY[cat]:
            cnt = len(classified[cat][sub])
            if cnt > 0:
                category_stats[cat][sub] = cnt
        if not category_stats[cat]:
            del category_stats[cat]

    # Also handle "其他" if it has entries
    other_cnt = len(classified.get("其他", {}).get("未分类", []))
    if other_cnt > 0:
        category_stats["其他"] = {"未分类": other_cnt}

    # 4. Print statistics report
    print("\n=== 分类统计 ===")
    unclassified_count = len(classified["其他"]["未分类"])
    unclassified_pct = unclassified_count / total * 100

    for cat, sub_counts in category_stats.items():
        cat_total = sum(sub_counts.values())
        cat_pct = cat_total / total * 100
        print(f"\n{cat} ({cat_total}, {cat_pct:.1f}%)")
        for sub, cnt in sorted(sub_counts.items(), key=lambda x: x[1], reverse=True):
            sub_pct_of_cat = cnt / cat_total * 100 if cat_total > 0 else 0
            warn = " ⚠" if (sub.startswith("综合") and sub_pct_of_cat > 40) else ""
            print(f"  {sub}: {cnt} ({sub_pct_of_cat:.1f}% of cat){warn}")

    print(f"\n未分类: {unclassified_count} ({unclassified_pct:.1f}%)")

    # 5. Validate quality thresholds
    if unclassified_pct >= 8.0:
        print(f"\n[ERROR] 未分类比例 {unclassified_pct:.1f}% >= 8%，质量不达标")
        return False

    for cat, sub_counts in category_stats.items():
        cat_total = sum(sub_counts.values())
        for sub, cnt in sub_counts.items():
            if sub.startswith("综合"):
                pct = cnt / cat_total * 100 if cat_total > 0 else 0
                if pct > 40:
                    print(f"\n[ERROR] {cat}/{sub} 占比 {pct:.1f}% > 40%，综合分类过重")
                    return False

    print("\n[OK] 质量验证通过")

    # 6. Generate output files
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        OUTPUT_DIR,
    )
    os.makedirs(output_dir, exist_ok=True)

    # Clean existing category dirs and index files
    for item in os.listdir(output_dir):
        item_path = os.path.join(output_dir, item)
        if os.path.isdir(item_path) and item in ALL_CATEGORIES:
            shutil.rmtree(item_path)
        elif os.path.isfile(item_path) and (
            item == "00-Index.md"
            or (item.startswith("_") and item.endswith(".md"))
        ):
            os.remove(item_path)

    link_targets: set[str] = set()

    for cat, sub_counts in category_stats.items():
        cat_dir = os.path.join(output_dir, cat)
        os.makedirs(cat_dir, exist_ok=True)

        # Write category index
        cat_index_content = generate_category_index(cat, sub_counts)
        cat_index_path = os.path.join(output_dir, f"_{cat}.md")
        with open(cat_index_path, "w", encoding="utf-8") as f:
            f.write(cat_index_content)
        link_targets.add(f"_{cat}")

        # Write subcategory files
        for sub in sub_counts:
            prompts_in_sub = classified[cat][sub]
            related_subs = list(RELATED_MAP.get(sub, set()))

            sub_content = generate_subcategory_file(cat, sub, prompts_in_sub, related_subs)
            sub_path = os.path.join(cat_dir, f"{sub}.md")
            with open(sub_path, "w", encoding="utf-8") as f:
                f.write(sub_content)
            link_targets.add(sub)

    # Write master index
    master_index_content = generate_master_index(category_stats)
    master_index_path = os.path.join(output_dir, "00-Index.md")
    with open(master_index_path, "w", encoding="utf-8") as f:
        f.write(master_index_content)
    link_targets.add("00-Index.md")

    # Also add all taxonomy names as valid link targets (even if no prompts in that sub)
    for _cat in ALL_CATEGORIES:
        link_targets.add(f"_{_cat}")
    for _sub in ALL_SUBCATEGORIES:
        link_targets.add(_sub)

    print(f"\n[OK] 生成文件完毕，共 {len(link_targets)} 个链接目标")

    # 7. Validate links: scan all .md files for [[...]], check against link_targets
    # Only scan lines OUTSIDE fenced code blocks (``` blocks)
    print("\n=== 链接验证 ===")
    dangling_links: list[tuple[str, str]] = []
    wiki_link_pattern = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*?)?\]\]")

    def is_placeholder_link(text: str) -> bool:
        """Return True if the link text looks like a template variable or placeholder."""
        if re.match(r'^[A-Z][A-Z0-9_]{2,}$', text):
            return True
        if '.' not in text and '/' not in text and len(text.split()) > 4:
            return True
        if text.startswith('argument') or text.startswith('your ') or text.startswith('insert'):
            return True
        return False

    for root, dirs, files in os.walk(output_dir):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            # Strip fenced code blocks before scanning for wiki links
            content_outside_code = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
            content_outside_code = re.sub(r'````.*?````', '', content_outside_code, flags=re.DOTALL)
            for match in wiki_link_pattern.finditer(content_outside_code):
                link_text = match.group(1).strip()
                if is_placeholder_link(link_text):
                    continue
                check_name = link_text
                if check_name not in link_targets:
                    base_name = os.path.basename(check_name)
                    if base_name not in link_targets:
                        rel_path = os.path.relpath(fpath, output_dir)
                        dangling_links.append((rel_path, link_text))

    if dangling_links:
        print(f"发现 {len(dangling_links)} 个悬空链接:")
        for fpath, link in dangling_links[:20]:
            print(f"  {fpath}: [[{link}]]")
        if len(dangling_links) > 20:
            print(f"  ... 还有 {len(dangling_links) - 20} 个")
    else:
        print("[OK] 无悬空链接")

    # 8. Print summary
    total_files = sum(
        len(files)
        for _, _, files in os.walk(output_dir)
        if True
    )
    print(f"\n=== 生成摘要 ===")
    print(f"总提示词: {total}")
    print(f"已分类:   {total - unclassified_count} ({(total - unclassified_count) / total * 100:.1f}%)")
    print(f"未分类:   {unclassified_count} ({unclassified_pct:.1f}%)")
    print(f"大类数:   {len(category_stats)}")
    print(f"子分类数: {sum(len(s) for s in category_stats.values())}")
    print(f"输出文件: {total_files}")
    print(f"输出目录: {output_dir}")

    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print_taxonomy_stats()
        print()
        print("=== Classification Tests ===")
        test_classification()
    else:
        success = run_pipeline()
        sys.exit(0 if success else 1)

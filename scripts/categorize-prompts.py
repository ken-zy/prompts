"""
categorize-prompts.py

Prompt categorization script for YouMind Nano Banana Pro prompt library.
Classifies 12465+ prompts into a 14-category taxonomy using regex keyword rules.

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

INPUT_FILE = "40_Reference/Articles/20260414/youmind-nano-banana-pro-all-prompts.json"
OUTPUT_DIR = "prompts_imgae"

# ---------------------------------------------------------------------------
# Task 1: Taxonomy
# ---------------------------------------------------------------------------

TAXONOMY = {
    "人像摄影": [
        "电影感肖像",
        "镜面自拍",
        "街拍写真",
        "证件照与正式照",
        "群像与多人",
        "综合人像",
    ],
    "时尚与造型": [
        "时装大片",
        "运动休闲",
        "婚纱婚礼",
        "Cosplay",
        "综合时尚",
    ],
    "产品与广告": [
        "食品饮料",
        "科技产品",
        "美妆护肤",
        "品牌广告",
        "综合产品",
    ],
    "艺术风格": [
        "浮世绘与日本传统",
        "水彩",
        "油画",
        "像素艺术",
        "手绘素描",
        "综合艺术",
    ],
    "3D与微缩": [
        "微缩模型与立体模型",
        "3D渲染",
        "蒸汽朋克机械",
        "综合3D",
    ],
    "信息图表": [
        "Bento网格信息图",
        "数据可视化",
        "地图",
        "综合图表",
    ],
    "海报与设计": [
        "电影海报",
        "活动海报",
        "名片与Logo",
        "贴纸",
        "综合设计",
    ],
    "建筑与空间": [
        "室内设计",
        "建筑摄影",
        "城市场景",
        "综合建筑",
    ],
    "动漫与卡通": [
        "日系动漫",
        "Q版角色",
        "LINE贴图",
        "漫画风",
        "综合动漫",
    ],
    "节日与主题": [
        "圣诞节",
        "新年",
        "万圣节",
        "情人节",
        "综合节日",
    ],
    "奇幻与科幻": [
        "赛博朋克",
        "奇幻世界",
        "超现实",
        "概念艺术",
        "综合奇幻",
    ],
    "食物与生活": [
        "美食摄影",
        "宠物",
        "旅行",
        "综合生活",
    ],
    "工具与模板": [
        "JSON结构化提示",
        "批量模板",
        "风格迁移",
        "修复与增强",
        "综合工具",
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
    # ---- 人像摄影 ----
    "镜面自拍": [
        r"镜面自拍",
        r"mirror.*selfie",
        r"selfie.*mirror",
        r"bathroom.*mirror",
        r"mirror.*shot",
        r"自拍.*镜",
    ],
    "电影感肖像": [
        r"电影感.*肖像",
        r"电影感.*portrait",
        r"cinematic.*portrait",
        r"portrait.*cinematic",
        r"电影感.*人像",
        r"cinematic.*人像",
        r"film.*portrait",
        r"portrait.*film",
        r"cinematic.*headshot",
        r"cinematic.*woman",
        r"cinematic.*girl",
        r"cinematic.*man",
        r"cinematic.*person",
        r"cinematic.*model",
        r"cinematic.*photo",
        r"photo.*cinematic",
        r"电影感.*女",
        r"電影.*女性",
        r"シネマティック.*女",
        r"电影感.*场景",
        r"cinematic.*scene",
        r"电影感.*提示",
        r"cinematic.*lighting",
        r"电影感.*镜",
        r"シネマティック",
    ],
    "街拍写真": [
        r"街拍",
        r"street.*photo",
        r"street.*portrait",
        r"street.*style.*photo",
        r"urban.*photo",
        r"写真",
        r"photo.*shoot",
        r"photoshoot",
        r"outdoor.*portrait",
        r"natural.*light.*portrait",
        r"lifestyle.*portrait",
        r"casual.*portrait",
    ],
    "证件照与正式照": [
        r"证件照",
        r"id.*photo",
        r"passport.*photo",
        r"正式照",
        r"headshot",
        r"professional.*photo",
        r"corporate.*photo",
        r"linkedin.*photo",
    ],
    "群像与多人": [
        r"群像",
        r"group.*photo",
        r"group.*portrait",
        r"多人",
        r"family.*photo",
        r"team.*photo",
        r"ensemble",
    ],
    "综合人像": [
        r"肖像",
        r"portrait",
        r"人像",
        r"face.*photo",
        r"photo.*face",
        r"model.*photo",
        r"posed.*photo",
        r"女性.*写真",
        r"女性.*撮影",
        r"女性.*シネマ",
        r"女の子.*写真",
        r"人物.*写真",
        r"人物.*撮影",
        r"人物.*シネマ",
    ],

    # ---- 时尚与造型 ----
    "Cosplay": [
        r"cosplay",
        r"costume.*play",
        r"角色扮演",
        r"cos.*服",
        r"cos.*装",
    ],
    "婚纱婚礼": [
        r"婚纱",
        r"wedding.*dress",
        r"bridal",
        r"婚礼",
        r"wedding",
        r"bride",
        r"groom",
        r"婚照",
    ],
    "运动休闲": [
        r"运动.*服",
        r"运动.*穿",
        r"sport.*wear",
        r"athletic.*wear",
        r"gym.*outfit",
        r"fitness.*look",
        r"运动风",
        r"休闲.*装",
        r"casual.*wear",
        r"streetwear",
        r"运动员.*装",
        r"sportswear",
        r"activewear",
        r"gym",
    ],
    "时装大片": [
        r"时装.*大片",
        r"时装.*广告",
        r"haute.*couture",
        r"high.*fashion",
        r"editorial.*fashion",
        r"fashion.*editorial",
        r"fashion.*shoot",
        r"时尚.*大片",
        r"时装.*秀",
        r"runway",
        r"vogue.*style",
        r"时装",
        r"fashion.*photo",
        r"fashion.*look",
    ],
    "综合时尚": [
        r"穿搭",
        r"\boutfit\b",
        r"\bootd\b",
        r"look.*book",
        r"lookbook",
        r"style.*guide",
        r"fashion.*style",
        r"fashion.*look",
        r"fashion.*shoot",
        r"fashion.*model",
        r"fashion.*week",
        r"street.*fashion",
        r"时尚.*造型",
        r"时尚.*穿",
        r"fashion.*trend",
        r"wardrobe.*style",
        r"造型.*搭配",
        r"搭配.*穿",
        r"穿.*造型",
    ],

    # ---- 产品与广告 ----
    "食品饮料": [
        r"食品",
        r"饮料",
        r"food.*ad",
        r"food.*commercial",
        r"drink.*ad",
        r"burger",
        r"coffee.*ad",
        r"coffee.*product",
        r"beverage",
        r"snack.*photo",
        r"food.*product",
        r"cuisine.*product",
        r"restaurant.*product",
        r"food.*packaging",
        r"drink.*packaging",
    ],
    "科技产品": [
        r"科技产品",
        r"tech.*product",
        r"technology.*product",
        r"smartphone.*ad",
        r"laptop.*ad",
        r"phone.*product",
        r"gadget",
        r"electronics.*ad",
        r"device.*ad",
        r"tech.*ad",
        r"product.*tech",
        r"headphone.*ad",
        r"earphone.*ad",
        r"watch.*product",
        r"smartwatch",
    ],
    "美妆护肤": [
        r"美妆",
        r"护肤",
        r"makeup.*product",
        r"skincare.*product",
        r"cosmetic",
        r"beauty.*product",
        r"lipstick",
        r"foundation.*makeup",
        r"perfume",
        r"fragrance",
        r"serum",
        r"moisturizer",
        r"beauty.*ad",
        r"化妆品",
        r"护肤品",
    ],
    "品牌广告": [
        r"品牌.*广告",
        r"brand.*ad",
        r"brand.*campaign",
        r"commercial.*ad",
        r"advertisement",
        r"广告.*创意",
        r"品牌.*推广",
        r"brand.*visual",
        r"marketing.*visual",
        r"ad.*campaign",
        r"promotional",
    ],
    "综合产品": [
        r"产品.*摄影",
        r"product.*photo",
        r"product.*shoot",
        r"商品.*摄影",
        r"产品.*展示",
        r"product.*display",
        r"product.*visual",
        r"产品",
        r"product",
        r"商品",
    ],

    # ---- 艺术风格 ----
    "浮世绘与日本传统": [
        r"浮世绘",
        r"ukiyo",
        r"woodblock.*print",
        r"japanese.*traditional",
        r"edo.*period",
        r"hokusai",
        r"hiroshige",
        r"japanese.*art",
        r"日本.*传统.*艺术",
        r"大和绘",
        r"日本画",
    ],
    "水彩": [
        r"水彩",
        r"watercolor",
        r"watercolour",
        r"aquarelle",
        r"水墨",
        r"ink.*wash",
        r"wash.*painting",
    ],
    "油画": [
        r"油画",
        r"oil.*paint",
        r"oil.*canvas",
        r"impressionist",
        r"impressionism",
        r"acrylic.*paint",
        r"canvas.*painting",
        r"renaissance.*paint",
        r"baroque.*paint",
        r"monet.*style",
        r"van.*gogh.*style",
    ],
    "像素艺术": [
        r"像素艺术",
        r"pixel.*art",
        r"pixelated",
        r"8.*bit",
        r"16.*bit",
        r"retro.*game.*art",
        r"pixel.*character",
        r"dot.*art",
        r"mosaic.*art",
    ],
    "手绘素描": [
        r"手绘",
        r"素描",
        r"sketch",
        r"pencil.*draw",
        r"pencil.*art",
        r"charcoal.*draw",
        r"chalkboard",
        r"chalk.*art",
        r"line.*art",
        r"lineart",
        r"ink.*draw",
        r"pen.*draw",
        r"doodle",
        r"手稿",
        r"draft.*draw",
        r"插画",
        r"\billustration\b",
        r"cutout.*paper",
        r"paper.*cut",
        r"剪纸",
        r"stencil.*art",
        r"flat.*illustration",
        r"vector.*illustration",
    ],
    "综合艺术": [
        r"艺术.*风格",
        r"art.*style",
        r"painting.*style",
        r"illustration.*style",
        r"digital.*art",
        r"概念.*绘画",
        r"graphic.*art",
        r"fine.*art",
        r"绘画.*风格",
        r"插画.*风格",
        r"插画.*作品",
        r"art.*illustration",
        r"illustration.*art",
        r"digital.*illustration",
        r"digital.*painting",
        r"art.*painting",
        r"\bartwork\b",
        r"艺术.*作品",
        r"艺术.*创作",
        r"artistic.*style",
        r"visual.*art",
        r"mixed.*media",
        r"art.*piece",
    ],

    # ---- 3D与微缩 ----
    "蒸汽朋克机械": [
        r"蒸汽朋克",
        r"steampunk",
        r"clockwork",
        r"steam.*mech",
        r"victorian.*mech",
        r"brass.*gear",
        r"gear.*mech",
        r"retro.*futur.*mech",
    ],
    "微缩模型与立体模型": [
        r"微缩",
        r"miniature",
        r"diorama",
        r"tilt.*shift",
        r"tiltshift",
        r"scale.*model",
        r"小人国",
        r"立体模型",
        r"model.*kit",
        r"figurine",
        r"tabletop.*miniature",
        r"\blego\b",
        r"lego.*set",
        r"lego.*model",
        r"plastic.*model",
        r"toy.*model",
    ],
    "3D渲染": [
        r"3d.*render",
        r"3d.*rendering",
        r"blender.*render",
        r"c4d",
        r"cinema4d",
        r"octane.*render",
        r"isometric.*3d",
        r"isometric.*render",
        r"low.*poly",
        r"3d.*model",
        r"cgi.*render",
        r"unreal.*engine",
        r"vray",
        r"keyshot",
        r"3d.*visualization",
    ],
    "综合3D": [
        r"3d",
        r"三维",
        r"sculpt",
        r"雕塑",
        r"zbrush",
        r"3d.*art",
        r"3d.*design",
        r"dimensional",
    ],

    # ---- 信息图表 ----
    "Bento网格信息图": [
        r"bento.*grid",
        r"bento.*layout",
        r"bento.*infograph",
        r"网格.*信息",
        r"liquid.*glass.*info",
        r"液态玻璃.*信息",
        r"bento.*card",
        r"bento.*box.*info",
        r"bento.*design",
        r"bento",
    ],
    "数据可视化": [
        r"数据可视化",
        r"data.*visualiz",
        r"data.*viz",
        r"chart.*visual",
        r"dashboard.*visual",
        r"bar.*chart",
        r"pie.*chart",
        r"line.*chart",
        r"graph.*visual",
        r"infographic.*data",
        r"analytics.*visual",
        r"statistics.*visual",
        r"数据.*图表",
        r"信息图",
        r"\binfograph",
        r"可视化.*提示",
        r"visualiz.*prompt",
        r"exploded.*view",
        r"anatomy.*infograph",
        r"recipe.*infograph",
        r"food.*infograph",
        r"diagram.*visual",
    ],
    "地图": [
        r"地图",
        r"\bmap\b",
        r"geographic.*visual",
        r"cartograph",
        r"world.*map",
        r"city.*map",
        r"travel.*map",
        r"illustrated.*map",
    ],
    "综合图表": [
        r"\bdiagram\b",
        r"流程图",
        r"flowchart",
        r"mind.*map",
        r"思维导图",
        r"图表.*设计",
        r"\bchart\b.*design",
        r"\bdashboard\b.*design",
        r"可视化.*图表",
        r"chart.*template",
        r"graph.*template",
    ],

    # ---- 海报与设计 ----
    "电影海报": [
        r"电影海报",
        r"movie.*poster",
        r"film.*poster",
        r"cinema.*poster",
        r"movie.*cover",
        r"dvd.*cover",
        r"theatrical.*poster",
    ],
    "活动海报": [
        r"活动海报",
        r"event.*poster",
        r"concert.*poster",
        r"festival.*poster",
        r"flyer",
        r"event.*flyer",
        r"banner.*design",
        r"promotion.*poster",
        r"海报.*活动",
        r"节日.*海报",
        r"节庆.*海报",
        r"春节.*海报",
        r"新年.*海报",
        r"年.*海报",
        r"holiday.*poster",
        r"seasonal.*poster",
        r"celebration.*poster",
        r"粗野主义.*海报",
        r"复古.*海报",
        r"retro.*poster",
        r"vintage.*poster",
        r"minimalist.*poster",
        r"abstract.*poster",
        r"poster.*design",
        r"海报.*设计",
        r"海报.*生成",
        r"海报.*创作",
    ],
    "名片与Logo": [
        r"名片",
        r"business.*card",
        r"logo.*design",
        r"\blogo\b",
        r"badge.*design",
        r"emblem",
        r"brand.*identity",
        r"brand.*logo",
        r"icon.*design",
        r"brand.*mark",
    ],
    "贴纸": [
        r"贴纸",
        r"sticker.*design",
        r"sticker.*pack",
        r"emoji.*design",
        r"sticker.*sheet",
        r"vinyl.*sticker",
        r"cute.*sticker",
        r"sticker",
    ],
    "综合设计": [
        r"海报",
        r"\bposter\b",
        r"graphic.*design",
        r"typography",
        r"layout.*design",
        r"visual.*design",
        r"平面设计",
        r"ui.*design",
        r"ux.*design",
        r"design.*template",
        r"design.*concept",
        r"creative.*design",
        r"设计.*海报",
        r"设计.*作品",
        r"设计.*方案",
    ],

    # ---- 建筑与空间 ----
    "室内设计": [
        r"室内",
        r"interior.*design",
        r"interior.*decor",
        r"home.*decor",
        r"家居",
        r"furniture.*design",
        r"living.*room",
        r"bedroom.*design",
        r"kitchen.*design",
        r"bathroom.*design",
        r"interior.*photo",
        r"室内.*摄影",
    ],
    "建筑摄影": [
        r"建筑.*摄影",
        r"architect.*photo",
        r"building.*photo",
        r"skyscraper.*photo",
        r"facade.*photo",
        r"architectural.*photo",
        r"建筑.*外观",
        r"exterior.*photo",
        r"structure.*photo",
    ],
    "城市场景": [
        r"城市场景",
        r"cityscape",
        r"skyline",
        r"urban.*scene",
        r"street.*scene",
        r"downtown.*scene",
        r"metropolitan",
    ],
    "综合建筑": [
        r"建筑.*设计",
        r"建筑.*风格",
        r"建筑.*摄影",
        r"architect.*design",
        r"architectural.*style",
        r"architectural.*render",
        r"building.*design",
        r"building.*architecture",
        r"interior.*space",
        r"spatial.*design",
        r"environment.*design",
        r"space.*design",
    ],

    # ---- 动漫与卡通 ----
    "LINE贴图": [
        r"line贴图",
        r"line.*sticker",
        r"line.*emoji",
        r"messaging.*sticker",
        r"chat.*sticker",
    ],
    "Q版角色": [
        r"q版",
        r"chibi",
        r"kawaii.*character",
        r"mascot.*character",
        r"cute.*mascot",
        r"可爱.*角色",
        r"萌.*角色",
        r"super.*deformed",
    ],
    "日系动漫": [
        r"日系动漫",
        r"anime.*character",
        r"anime.*style",
        r"anime.*art",
        r"manga.*character",
        r"二次元",
        r"动漫.*角色",
        r"anime.*girl",
        r"anime.*boy",
        r"shounen",
        r"shoujo",
        r"isekai",
        r"waifu",
        r"动漫",
        r"anime",
    ],
    "漫画风": [
        r"漫画.*风",
        r"漫画.*风格",
        r"manga.*style",
        r"comic.*style",
        r"comic.*art",
        r"comic.*book",
        r"graphic.*novel",
        r"漫画",
        r"\bmanga\b",
        r"comic.*strip",
        r"sequential.*art",
    ],
    "综合动漫": [
        r"卡通",
        r"cartoon",
        r"character.*design",
        r"角色.*设计",
        r"animation.*style",
        r"animated.*character",
        r"2d.*character",
        r"flat.*character",
    ],

    # ---- 节日与主题 ----
    "圣诞节": [
        r"圣诞",
        r"christmas",
        r"santa.*claus",
        r"xmas",
        r"holiday.*christmas",
        r"christmas.*tree",
        r"winter.*holiday",
        r"advent",
    ],
    "新年": [
        r"新年",
        r"new.*year",
        r"元旦",
        r"春节",
        r"chinese.*new.*year",
        r"lunar.*new.*year",
        r"year.*celebration",
        r"happy.*new.*year",
        r"年夜",
        r"过年",
    ],
    "万圣节": [
        r"万圣",
        r"halloween",
        r"pumpkin.*lantern",
        r"jack.*o.*lantern",
        r"trick.*or.*treat",
        r"spooky.*halloween",
        r"ghost.*halloween",
        r"witch.*halloween",
    ],
    "情人节": [
        r"情人节",
        r"valentine",
        r"romantic.*holiday",
        r"hearts.*day",
        r"love.*day",
        r"couples.*day",
    ],
    "综合节日": [
        r"节日",
        r"festival",
        r"birthday.*party",
        r"party.*celebration",
        r"celebration",
        r"holiday",
        r"生日",
        r"anniversary",
        r"纪念日",
    ],

    # ---- 奇幻与科幻 ----
    "赛博朋克": [
        r"赛博朋克",
        r"cyberpunk",
        r"neon.*city",
        r"neon.*light.*city",
        r"dystopian.*city",
        r"cyber.*city",
        r"futuristic.*neon",
        r"bladerunner",
        r"blade.*runner",
        r"neon.*sign",
        r"城市.*夜景",
        r"night.*city",
        r"city.*night.*neon",
    ],
    "奇幻世界": [
        r"奇幻",
        r"fantasy.*world",
        r"fantasy.*land",
        r"magic.*world",
        r"dragon",
        r"medieval.*fantasy",
        r"epic.*fantasy",
        r"high.*fantasy",
        r"magical.*realm",
        r"wizard",
        r"elf",
        r"dwarf.*fantasy",
        r"fantasy.*creature",
        r"神兽",
        r"神话",
        r"mythology",
        r"mythical",
        r"giant.*woman",
        r"giant.*person",
        r"titanic.*figure",
        r"colossal.*figure",
        r"巨型",
        r"giant.*city",
        r"macro.*miniature",
    ],
    "超现实": [
        r"超现实",
        r"surreal",
        r"dreamlike",
        r"dream.*scene",
        r"surrealism",
        r"surrealist",
        r"dreamscape",
        r"bizarre.*scene",
        r"dali.*style",
        r"magritte.*style",
    ],
    "概念艺术": [
        r"概念艺术",
        r"concept.*art",
        r"sci.*fi.*art",
        r"science.*fiction.*art",
        r"space.*art",
        r"mech.*design",
        r"mecha",
        r"futuristic.*design",
        r"speculative.*design",
        r"worldbuilding",
    ],
    "综合奇幻": [
        r"幻想",
        r"fictional.*world",
        r"fantasy",
        r"sci.*fi",
        r"science.*fiction",
        r"space.*scene",
        r"alien",
        r"futuristic",
        r"magic",
    ],

    # ---- 食物与生活 ----
    "美食摄影": [
        r"美食.*摄影",
        r"food.*photography",
        r"food.*photo",
        r"cuisine.*photo",
        r"restaurant.*photo",
        r"dish.*photo",
        r"food.*styling",
        r"flat.*lay.*food",
        r"food.*art",
        r"gourmet.*photo",
        r"food.*portrait",
    ],
    "宠物": [
        r"宠物",
        r"\bpet\b",
        r"cat.*photo",
        r"dog.*photo",
        r"animal.*photo",
        r"kitten",
        r"puppy",
        r"猫.*摄影",
        r"狗.*摄影",
        r"feline",
        r"canine",
        r"pet.*portrait",
        r"animal.*portrait",
    ],
    "旅行": [
        r"旅行",
        r"travel.*photo",
        r"travel.*scene",
        r"landscape.*photo",
        r"beach.*photo",
        r"sunset.*photo",
        r"nature.*photo",
        r"mountain.*photo",
        r"scenic.*photo",
        r"vacation.*photo",
        r"destination.*photo",
        r"travel.*landscape",
        r"outdoor.*photo",
    ],
    "综合生活": [
        r"生活.*方式",
        r"\blifestyle\b",
        r"daily.*life",
        r"日常.*生活",
        r"life.*style",
        r"everyday.*life",
        r"life.*scene",
        r"生活.*场景",
        r"生活.*记录",
    ],

    # ---- 工具与模板 ----
    "JSON结构化提示": [
        r"\bjson\b",
        r"structured.*prompt",
        r"\{.*scene.*subject",
        r"\{.*\"scene\"",
        r"\{.*\"subject\"",
        r"json.*format.*prompt",
        r"structured.*output",
        r"prompt.*json",
        r"json.*schema.*prompt",
    ],
    "批量模板": [
        r"批量.*模板",
        r"batch.*template",
        r"batch.*prompt",
        r"parameteriz",
        r"template.*prompt",
        r"\[插入",
        r"\[insert",
        r"\[your.*",
        r"fill.*in.*blank",
        r"variable.*prompt",
        r"批量.*生成",
    ],
    "风格迁移": [
        r"风格迁移",
        r"style.*transfer",
        r"image.*to.*image",
        r"img2img",
        r"reimagin",
        r"style.*conversion",
        r"artistic.*transfer",
        r"render.*style",
        r"transform.*style",
        r"以.*风格.*重绘",
        r"重绘.*风格",
    ],
    "修复与增强": [
        r"修复",
        r"restore.*photo",
        r"photo.*restoration",
        r"enhance.*photo",
        r"photo.*enhance",
        r"upscale",
        r"coloriz",
        r"colorize",
        r"deblur",
        r"denoise",
        r"inpaint",
        r"outpaint",
        r"增强.*图像",
        r"图像.*增强",
        r"老照片.*修复",
        r"图像.*编辑",
        r"image.*edit",
        r"photo.*edit",
        r"图像.*调整",
        r"image.*adjust",
        r"edit.*photo",
        r"remove.*background",
        r"change.*background",
        r"图片.*编辑",
    ],
    "综合工具": [
        r"提示词.*工具",
        r"prompt.*tool",
        r"tutorial.*prompt",
        r"guide.*prompt",
        r"how.*to.*prompt",
        r"prompt.*guide",
        r"prompt.*tutorial",
        r"prompt.*template",
        r"参数化.*提示",
        r"workflow.*prompt",
        r"prompt.*workflow",
        r"提示词.*模板",
        r"提示词.*教程",
    ],
}

# ---------------------------------------------------------------------------
# Related pairs (bidirectional, ~23 curated pairs)
# ---------------------------------------------------------------------------

RELATED_PAIRS = [
    ("电影感肖像", "电影海报"),
    ("电影感肖像", "街拍写真"),
    ("镜面自拍", "运动休闲"),
    ("街拍写真", "城市场景"),
    ("时装大片", "电影感肖像"),
    ("时装大片", "品牌广告"),
    ("Cosplay", "日系动漫"),
    ("Cosplay", "奇幻世界"),
    ("食品饮料", "美食摄影"),
    ("科技产品", "3D渲染"),
    ("浮世绘与日本传统", "风格迁移"),
    ("水彩", "手绘素描"),
    ("蒸汽朋克机械", "微缩模型与立体模型"),
    ("蒸汽朋克机械", "概念艺术"),
    ("Bento网格信息图", "数据可视化"),
    ("日系动漫", "漫画风"),
    ("Q版角色", "LINE贴图"),
    ("Q版角色", "贴纸"),
    ("赛博朋克", "城市场景"),
    ("赛博朋克", "概念艺术"),
    ("超现实", "概念艺术"),
    ("JSON结构化提示", "批量模板"),
    ("修复与增强", "风格迁移"),
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
            {"title": "电影感肖像写真拍摄", "description": "", "content": "", "translatedContent": ""},
            "人像摄影",
            "电影感肖像",
            "电影感肖像 title",
        ),
        (
            {"title": "My Room", "description": "mirror selfie bedroom aesthetic", "content": "", "translatedContent": ""},
            "人像摄影",
            "镜面自拍",
            "mirror selfie description",
        ),
        (
            {
                "title": "Info Card Layout Design",
                "description": "A grid-based info layout",
                "content": "",
                "translatedContent": "Bento网格信息图设计参考",
            },
            "信息图表",
            "Bento网格信息图",
            "English title + Bento网格信息图 in translatedContent",
        ),
        (
            {"title": "赛博朋克城市夜景", "description": "", "content": "", "translatedContent": ""},
            "奇幻与科幻",
            "赛博朋克",
            "赛博朋克城市夜景",
        ),
        (
            {"title": "Something completely unrelated abc", "description": "", "content": "", "translatedContent": ""},
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
    """Format one prompt as a Markdown entry."""
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
        # Wrap each paragraph in blockquote
        for desc_line in description.strip().splitlines():
            lines.append(f"> {desc_line}")
        lines.append("")

    # Images from media array
    media = prompt.get("media") or []
    if media:
        for item in media:
            if isinstance(item, dict):
                url = item.get("url") or item.get("src") or ""
                alt = item.get("alt") or item.get("title") or title
            elif isinstance(item, str):
                url = item
                alt = title
            else:
                continue
            if url:
                lines.append(f"![{alt}]({url})")
        lines.append("")

    # Prompt content in fenced code block
    content = prompt.get("content") or ""
    lines.append("```")
    lines.append(content)
    lines.append("```")
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

    lines.append("# Nano Banana Pro Prompts")
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
        # Some JSON formats have nested structures
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

    # Clean existing category dirs (but preserve prompts_imgae or any non-category content)
    # Category dirs are named after categories in TAXONOMY, and _ prefixed index files
    for item in os.listdir(output_dir):
        item_path = os.path.join(output_dir, item)
        # Remove category subdirectories (named after taxonomy categories)
        if os.path.isdir(item_path) and item in ALL_CATEGORIES:
            shutil.rmtree(item_path)
        # Remove category index files _{cat}.md and 00-Index.md
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
        # All-caps identifiers like USE_REFERENCE_FACE, VARIABLE_NAME
        if re.match(r'^[A-Z][A-Z0-9_]{2,}$', text):
            return True
        # Contains spaces and looks like a natural language phrase (not a file name)
        if '.' not in text and '/' not in text and len(text.split()) > 4:
            return True
        # Argument-style placeholders
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
            for match in wiki_link_pattern.finditer(content_outside_code):
                link_text = match.group(1).strip()
                # Skip placeholder/variable links
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

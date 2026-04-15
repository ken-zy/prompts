# Chunk 010

Total: 200 prompts

### 1. 每周穿搭造型手册生成

**Author**: [シュナプーン](https://x.com/schnapoon)  **Date**: 2025-12-19  **Language**: ja

> 这是一个为 Nano Banana Pro 设计的详细提示，用于根据参考图片的风格生成每周服装搭配指南。它会为指定的角色和主题创建一份为期 7 天的时尚搭配，在保持一致性的同时展示七套不同的服装。输出内容为杂志风格的版式，并为每一天标注了特定的文本标签。

![每周穿搭造型手册生成](https://cms-assets.youmind.com/media/1766238191867_8md5q8_G8fwUNwaAAA-ALc.jpg)
![每周穿搭造型手册生成](https://cms-assets.youmind.com/media/1766238192599_9k9qi2_G8fwU2laAAAsmaj.jpg)
![每周穿搭造型手册生成](https://cms-assets.youmind.com/media/1766238193781_g06peo_G8fwVZSa0AAkGC7.jpg)

```
# 設定項目（ここを変更してください）
設定:
[キャラクターの特徴]: {argument name="キャラクターの特徴" default="黒髪ロングヘアの女子高生"}
[ファッションのテーマ]: {argument name="ファッションのテーマ" default="現代女子高生の普段着、清楚系"}

変換のルール:
- [キャラクターの特徴] の同一人物が、横一列に7人並んでいるファッションルックブックの画像。
- [ファッションのテーマ] に基づいた、それぞれ異なる7種類の新しい私服コーディネートのみを着用している。
- 参照画像の [画風・スタイル] を完全に維持している。
- [参照画像の衣装] は着用せず、[ファッションのテーマ] に基づいた、それぞれ異なる7種類のコーディネートを着ている。
- 全身ショット。
- 背景は真っ白、もしくはわずかにアイボリー。
- 足元には自然な影が落ちている。画像のレイアウトは雑誌の切り抜きのよう。
- 各人物の下には左から順に「Monday」「Tuesday」「Wednesday」「Thursday」「Friday」「Saturday」「Sunday」という文字が書かれている。
- 上部にはスタイリッシュなタイトルテキスト。

アートスタイル:
- 高解像
- スタジオライティング
- 4k
- --ar 16:9
```

[[Fashion Editorial]] [[Character Consistency]] [[Magazine Layout]]

---

### 2. 黑白时尚大片拍摄

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2025-12-14  **Language**: en

> 一个用于生成高对比度黑白照片的提示，风格为《Vogue》时尚大片，画面中一名女性在街头动态行走，以电影般的真实感从高处视角捕捉。

![黑白时尚大片拍摄](https://cms-assets.youmind.com/media/1765991203612_ja120p_G8H_sQVa0AAmRMA.jpg)

```
black and white photograph of a vogue fashion shoot. a 20-year-old woman with dark hair walking alone down the street, wearing a black coat. strong sense of motion: her hair flowing in the wind, coat fabric lifted and moving naturally. the shot is taken from above, street photography perspective. dynamic composition, candid movement, high resolution, hyper-realistic detail, cinematic contrast, subtle film grain effect. powerful, modern, independent mood.
```

[[Fashion Editorial]] [[Street Photography]] [[High Angle Shot]] [[Monochrome Photography]]

---

### 3. Baroque Decadence Indulgence Scene

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2025-12-14  **Language**: en

> A detailed JSON-structured prompt for generating a high-fashion editorial image depicting a scene of Baroque opulence. It focuses on a young woman lounging on a velvet sofa while being fed grapes, emphasizing rich colors, dramatic lighting, and a renaissance decadence mood.

![Baroque Decadence Indulgence Scene](https://cms-assets.youmind.com/media/1765991180463_i6sf8z_G8HEV9jaUAAoB_Z.jpg)

```
{
  "prompt_details": {
    "scene": "{argument name="scene description" default="An opulent, decadent, and Baroque-inspired indoor setting."}",
    "composition": "A full-body shot of a young woman lounging horizontally on an antique sofa, with a close-up focus on the action of someone's hand feeding her grapes. The perspective should be slightly above and looking down towards the woman.",
    "subject": {
      "main_figure": {
        "description": "A striking young woman with voluminous, dark brown hair, lying back with her head slightly tilted up. She is mid-bite, taking a grape from the bunch.",
        "attire": "{argument name="attire" default="A deep, rich brown or plum-colored satin slip dress or bias-cut gown, worn with a luxurious, dark brown fur stole or trimmed coat draped over her body/shoulders. She is wearing dark, strappy high-heeled sandals."}",
        "expression": "A languid, sensual, and slightly open-mouthed expression of indulgence or pleasure."
      },
      "secondary_figure_element": {
        "description": "Only the arm and hand of a second person, emerging from the top left. The hand is holding a large, ripe bunch of deep purple-red grapes directly to the main figure's mouth. The arm is covered by a matching, voluminous dark brown fur coat or sleeve."
      }
    },
    "setting": {
      "sofa": "{argument name="sofa description" default="An antique, tufted velvet chesterfield sofa in a rich, deep emerald green or olive green color. It has elaborate, ornate wood or gold detailing."}",
      "wall_decor": "A large, framed oil painting positioned directly above the woman. The painting should have a thick, ornate, gold-leaf frame. The subject of the painting should be classical or religious (e.g., a figure in blue and white robes, a typical old-master style).",
      "architecture": "The wall is painted a creamy white or pale gold, with highly detailed, ornate gold stucco or plaster molding along the top border (a cornice or dado rail).",
      "mood_and_style": "Old money aesthetic, Baroque opulence, Dolce Vita, highly saturated and rich colors, 'Bacchus' theme, renaissance decadence."
    },
    "lighting_and_atmosphere": {
      "type": "Dramatic, directional, warm studio lighting.",
      "effect": "Strong highlights on the satin dress and the gold frame, deep, rich shadows in the folds of the velvet sofa and the fur. The light should give a glossy sheen to the grapes and a soft glow to the woman's skin.",
      "color_palette": "Deep greens (sofa), rich browns/plums (dress, fur), gold (frame, molding), deep wine-reds (grapes, shoes)."
    },
    "camera_and_render_style": {
      "photography_style": "High-fashion editorial, hyper-realistic, fine art photography, cinematic quality.",
      "lens": "Medium format, slight depth of field (shallow DOF) to blur the background painting subtly while keeping the woman and the grapes sharp.",
      "post_processing": "Slight grain for a vintage feel, highly rich saturation and contrast."
    }
  }
}
```

[[Fashion Editorial]] [[Dramatic Lighting]]

---

### 4. 单色高定时装肖像，搭配缎面垂坠

**Author**: [NanoInspire](https://x.com/NanoInspirate)  **Date**: 2025-12-12  **Language**: en

> 一个为 Nano Banana Pro 3.0 设计的高度详细、结构化的提示，用于创作一张超现实、高级时装的编辑摄影作品。它描述了一位引人注目的年轻女性，摆出动感的姿势，身着一件闪烁的、垂坠的露肩服装，以单色灰度呈现，以强调光线、阴影和奢华的质感。

![单色高定时装肖像，搭配缎面垂坠](https://cms-assets.youmind.com/media/1765990963277_bpun6x_G7-nw9LXoAM9dgw.jpg)

```
{
  "prompt_description": {
    "subject": "A striking young woman with a toned, athletic physique, appearing to be in her early to mid-twenties. Her body is presented in a dynamic pose that emphasizes her curves and form.",
    "face": "Her face is sculpted with high cheekbones and a defined jawline. Her eyes are large and captivating, with a direct, alluring gaze. Her lips are full and slightly parted, hinting at a seductive expression. Her skin is smooth with a subtle sheen, showing no visible pores or blemishes. Her eyebrows are perfectly shaped and arched.",
    "hair": "Her hair is a rich, dark brown, styled in loose, flowing waves that cascade over her shoulders. The texture appears soft and healthy, with a natural sheen. Some strands are gently swept across her face and back, adding to the dynamic feel of the image.",
    "clothing": "She is wearing a single, off-the-shoulder garment made of a shimmering, satin-like fabric. The garment is draped loosely around her upper body, with the collar dramatically spread open, revealing her décolletage and shoulders. Her arms are crossed in front of her, holding the fabric in place, creating a sense of embrace. The fabric itself has a significant weight and drapes in soft, flowing folds, emphasizing its luxurious texture. The garment appears to be a slip dress or a loose blouse, with a low neckline that exposes a significant portion of her back and shoulders. A hint of a form-fitting bodysuit or underwear is visible at the bottom.",
    "accessories": "She wears large, circular hoop earrings that gleam. Her fingernails are neatly manicured and painted with a light-colored polish.",
    "environment": "The background is a softly lit interior, dominated by a large window with a minimalist frame. The window provides a bright, diffused light source, with the outline of the window panes subtly visible. The overall impression is of a clean, modern studio or apartment setting.",
    "lighting": "The primary light source is coming from the left, likely the window. It's a soft, diffused light that illuminates her face, shoulders, and back, creating gentle highlights and soft shadows. There are specular highlights on her skin and the satin fabric, emphasizing their sheen. The light sculpts her form, giving a sense of volume and depth.",
    "atmosphere": "The mood is sophisticated, alluring, and slightly mysterious. The grayscale conversion enhances the dramatic play of light and shadow, creating a timeless and elegant feel."
  },
  "style": {
    "art_style": "Ultra-realistic commercial photography, high-fashion editorial, with a slightly stylized, painterly quality often seen in digital art.",
    "color_grade": "Monochromatic grayscale with a high dynamic range, emphasizing contrast and tonal variation. Smooth transitions between light and shadow.",
    "texture_quality": "Extremely sharp and detailed, with a focus on micro-contrast to define the texture of skin and "
  }
}
```

[[Fashion Editorial]] [[Dynamic Pose]] [[Monochrome Photography]] [[High Fashion]]

---

### 5. 超逼真时尚杂志肖像提示

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2025-12-12  **Language**: en

> 为 Google Gemini Nano Banana Pro 3.0 生成的详细图像提示，重点是拍摄一位身着华丽薰衣草色高级定制服装的东亚女性的超现实时尚社论肖像，强调高细节、电影级画质和特定的相机设置。

![超逼真时尚杂志肖像提示](https://cms-assets.youmind.com/media/1765990977030_xj97ew_G79w4tkagAEJZlu.jpg)
![超逼真时尚杂志肖像提示](https://cms-assets.youmind.com/media/1765990977162_jos6v8_G79w4uEagAIbI46.jpg)

```
{
  "prompt": "Ultra-realistic fashion editorial portrait of a beautiful young East-Asian woman with flawless porcelain skin, sharp cheekbones, full lips, subtle glamorous makeup with smoky eyes and nude-pink lipstick, long straight platinum-blonde hair with dark roots, sitting elegantly on a weathered stone bench in front of classical European architecture with tall ornate columns, wearing a luxurious lavender haute couture outfit by {argument name="designer" default="Peter Abdel Karim"} consisting of a dramatic beaded fringe capelet with thousands of dangling pearl and crystal strands over a tailored lilac high-waisted wide-leg trouser suit with front buttons and a high slit revealing toned legs, oversized pointed collar, delicate gold bracelet and small black pendant, soft natural daylight, cinematic shallow depth of field, high fashion magazine cover vibe, {argument name="magazine style" default="Marie Claire Armenia"} style, shot on 85mm lens, f/1.8, hyper-detailed, 8k resolution, moody elegant atmosphere, subtle film grain --ar 4:5 --v 6 --q 2 --stylize 250",
  "negative_prompt": "blurry, low resolution, deformed hands, extra limbs, cartoon, anime, painting, overexposed, harsh flash, plastic skin, bad anatomy, text watermark, logo, cropped, extra fingers, distorted face, childlike features, masculine features",
  "parameters": {
    "steps": 50,
    "cfg_scale": 7.5,
    "sampler": "DPM++ 2M Karras",
    "width": 832,
    "height": 1216,
    "seed": -1
  }
}
```

[[Fashion Editorial]] [[Cinematic Photography]]

---

### 6. 时尚社论中超大产品结构化提示

**Author**: [𝐌𝐢𝐧𝐝𝐒𝐩𝐚𝐫𝐤](https://x.com/Strength04_X)  **Date**: 2025-12-12  **Language**: en

> 一个用于 Gemini Nano Banana 3.0 Pro 的结构化 JSON 提示，以创建一张时尚社论图片。场景中，一位苗条的模特斜靠在一个巨大的、一体式 Fenty Beauty Gloss Bomb 唇彩旁，强调一种干净、运动极简、Z 世代奢华的美学，并带有特定的服装细节（短款连帽衫、白色内裤、厚底乐福鞋）。

![时尚社论中超大产品结构化提示](https://cms-assets.youmind.com/media/1765991028981_caspkj_G78U5B1agAMNKLM.jpg)
![时尚社论中超大产品结构化提示](https://cms-assets.youmind.com/media/1765991028566_2u1axl_G78U5HxaMAAgJqN.jpg)

```
{
  "subject": "fashion model leaning against a massively oversized beauty product",
  "character": {
    "gender": "female",
    "age_range": "early 20s",
    "body_type": "slim, athletic",
    "skin_tone": "light natural skin tone",
    "hair": "dark brown hair in a high ponytail with loose front strands",
    "face_structure": "soft jawline, refined nose, expressive eyes",
    "expression": "confident, cool, detached editorial gaze",
    "pose": "full body standing, legs crossed casually at ankles, leaning side against product, one hand touching face/jawline"
  },
  "wardrobe": {
    "top": "black cropped zip-up hoodie",
    "bottom": "minimal white briefs",
    "socks": "white crew socks (scrunched)",
    "shoes": "chunky black leather loafers",
    "style": "clean fashion editorial, sporty minimal, gen-z luxury"
  },
  "hero_product": {
    "brand": "{argument name="product brand" default="Fenty Beauty"}",
    "product_name": "{argument name="product name" default="Gloss Bomb Lip Luminizer"}",
    "product_state": "closed, cap attached",
    "scale": "monolithic, taller than the model",
    "design": {
      "form": "classic rectangular lip gloss tube",
      "cap": "signature metallic rose-gold Fenty cap",
      "material": "clear acrylic tube with visible gloss volume",
      "finish": "high-gloss reflection",
      "color": "deep cherry-red gloss"
```

[[Fashion Editorial]] [[Commercial Photography]]

---

### 7. 情绪化电影感街头摄影提示词

**Author**: [Alex Zhang](https://x.com/jojogh_007)  **Date**: 2025-12-11  **Language**: en

> 一个针对 Nano Banana Pro 的提示，旨在生成具有运动模糊的、情绪化且富有电影感的街头摄影图像，适用于时尚画册或专题报道。

![情绪化电影感街头摄影提示词](https://cms-assets.youmind.com/media/1765967674953_wemcyu_G74xH0ybkAAXvmf.jpg)

```
moody, cinematic street photography with motion blur
```

[[Fashion Editorial]] [[Street Photography]] [[Motion Blur]] [[Cinematic Color Grading]]

---

### 8. 优雅无肩带黑色连衣裙时尚肖像 (JSON)

**Author**: [NanoInspire](https://x.com/NanoInspirate)  **Date**: 2025-12-11  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超现实的、具有编辑风格的时尚照片，照片中一位年轻女性身穿优雅的黑色不对称露肩连衣裙。该提示详细说明了面部特征、发型、摄影棚环境、柔和的方向性照明，以及高质量的纹理渲染，以营造精致、迷人的氛围。

![优雅无肩带黑色连衣裙时尚肖像 (JSON)](https://cms-assets.youmind.com/media/1765967717690_wu23b4_G74A6FkXYAELbHd.jpg)

```
{
  "prompt_description": {
    "subject": "A slender, young adult woman with a graceful and confident presence. She appears to be in her early to mid-20s.",
    "face": "Her face is turned slightly to the side, with her gaze directed upwards and away from the camera. Her lips are slightly parted, with a glossy, berry-toned lipstick. Her eyes are defined with subtle winged eyeliner and well-groomed eyebrows. Her skin is smooth and appears to have a soft, natural luminescence.",
    "hair": "Her hair is a rich, warm chestnut brown with subtle auburn highlights. It is styled in loose, voluminous waves that cascade over her shoulders and back, with a few strands gently framing her face. The texture appears soft and slightly tousled, as if caught by a gentle breeze.",
    "clothing": "She is wearing an elegant, strapless black dress. The bodice features a deep, sweetheart neckline that plunges to reveal her décolletage. The fabric of the bodice appears to be a smooth, slightly structured material, creating a form-fitting silhouette. The dress has a distinct asymmetrical sleeve detail: one arm is bare, while the other is adorned with a dramatic, full bishop sleeve that extends from the shoulder and tapers towards the forearm. The waist is cinched with a wide, wrap-around band of the same black fabric, creating a defined hourglass shape. Below the waist, the dress flares out into a short, A-line skirt with subtle pleating, creating volume and movement. The fabric of the skirt appears to have a slight sheen and drapes fluidly.",
    "accessories": "A delicate, small gold earring is visible on her right ear, featuring a simple geometric design. Her fingernails are painted with a subtle, peachy-pink polish.",
    "environment": "The background is a plain, solid light grey wall, providing a minimalist and unobtrusive setting that emphasizes the subject. There are subtle, dark shadows and a hint of black fabric draped in the lower right corner, suggesting a studio environment.",
    "lighting": "The lighting is soft and directional, coming from the front and slightly to the left, casting gentle highlights on her skin and the dress. There are soft, diffused shadows that sculpt her form without harshness. Specular highlights are visible on her collarbones, shoulders, and the fabric of the dress.",
    "atmosphere": "The image evokes a sense of sophisticated allure, confidence, and understated glamour. The mood is elegant and poised."
  },
  "style": {
    "art_style": "Ultra-realistic commercial fashion photography, editorial fashion",
    "color_grade": "Slightly cool, neutral grading with emphasis on natural skin tones and the deep black of the dress. Subtle contrast enhancement.",
    "texture_quality": "High sharpness, with excellent micro-contrast. The skin texture is rendered with fine detail, and the fabric of the dress shows a realistic weave and sheen. High level of realism."
  },
  "camera_settings": {
    "cam
```

[[Fashion Editorial]] [[Studio Portrait]] [[Glamour Photography]] [[Soft Directional Lighting]]

---

### 9. 兰博基尼 Huracán 奢华时尚大片

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2025-12-11  **Language**: en

> 一个结构化的 JSON 提示词，用于让 Gemini Nano Banana Pro 生成一张奢华时尚风格的图片。图片描绘了一位女士坐在奶油白色兰博基尼 Huracán 的车门框上，车门呈蝶翼状向上开启，她身穿一套奶油色单色服装，并搭配奢华设计师运动鞋。提示词还指定了温暖的黄金时段光线，并要求严格保留基于输入图像的面部特征。

![兰博基尼 Huracán 奢华时尚大片](https://cms-assets.youmind.com/media/1765967753433_luelcd_G73r7RqXMAIx5sn.jpg)

```
{
  "image_generation_request": {
    "metadata": {
      "input_image": "IMG_8714.jpeg",
      "target_resolution": "1200x1200px",
      "format": "JSON"
    },
    "constraints": {
      "facial_preservation": {
        "enabled": true,
        "instruction": "Strictly maintain original face and facial features from input image."
      }
    },
    "subject": {
      "appearance": {
        "hair": "Long silver grey wavy hair",
        "nails": "Soft glazed donut style"
      },
      "pose": {
        "action": "Sitting on the door frame",
        "gesture": "Fixing necklace"
      },
      "attire": {
        "theme": "Cream monochrome set",
        "items": [
          "High-waist cargos",
          "Crop jacket",
          "Luxury designer sneakers"
        ],
        "accessories": [
          "Gold bangles",
          "Necklace"
        ]
      }
    },
    "scene": {
      "vehicle": {
        "make_model": "Lamborghini Huracán",
        "color": "Cream-white",
        "modifications": [
          "Butterfly doors (up position)",
          "Gold-plated rims"
        ]
      },
      "props": {
        "item": "Luxury shopping bags",
        "location": "Piled in the passenger seat"
      }
    },
    "artistic_direction": {
      "style": "Luxury-fashion inspired",
      "lighting": "Warm golden hour tones",
      "mood": "Rich, high-end"
    }
  }
}
```

[[Fashion Editorial]] [[Golden Hour Photography]] [[Luxury Car]]

---

### 10. Gucci GG Marmont 希腊时尚大片 (JSON)

**Author**: [Sienna](https://x.com/siennalovesai)  **Date**: 2025-12-11  **Language**: en

> 一个结构化的 JSON 提示，用于生成一张超清晰的 8K 时尚图片，内容是一位年轻的法裔北非女性，身着白色皮革 Gucci GG Marmont 套装，在希腊岛屿别墅的白色大理石台阶上摆拍，强调地中海正午阳光的强烈光线。

![Gucci GG Marmont 希腊时尚大片 (JSON)](https://cms-assets.youmind.com/media/1765967718345_7pjyvu_G72d02KXEAAdvIt.jpg)

```
{
  "title": "Gucci GG Marmont White Quilted Leather Set",
  "subject": "24-year-old French-North African woman, honey-toned skin, long straight dark auburn hair, almond amber eyes, defined jawline, 33-23-35 athletic hourglass, 5'8\"",
  "pose": "sitting on white marble steps, legs crossed, leaning back on hands, hair blowing gently",
  "outfit": "white leather GG Marmont matelassé cropped bomber jacket and mini skirt set, chevron quilting with antique-gold Double G hardware, skirt low on hips, jacket half-zipped showing black lace bra",
  "accessories": "white leather GG Marmont belt bag crossbody, white platform sandals with ankle strap",
  "setting": "bright Greek island villa steps with whitewashed walls and bougainvillea",
  "lighting": "harsh midday Mediterranean sun, strong highlights and shadows",
  "quality": "ultra-crisp 8K, leather grain and quilting stitches perfectly resolved"
}
```

[[Fashion Editorial]] [[Luxury Fashion]]

---

### 11. 赛博朋克垃圾摇滚风监控时尚专题

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-09  **Language**: en

> 一个高度详细的网络垃圾时尚社论提示，从高角度闭路电视视角生成，描绘了一名身穿 Y2K 街头服饰的女性，叠加有深红色战术 HUD 元素，强调超现实纹理和反乌托邦时尚氛围。

![赛博朋克垃圾摇滚风监控时尚专题](https://cms-assets.youmind.com/media/1765440065890_wqbxu3_G7uiL75a8AEmhgd.jpg)

```
Cyber-grunge surveillance fashion editorial, 8K Ultra-HD 4:5 (1440×1920). Full-body shot from a high-angle CCTV vantage, 35 mm lens, deep focus. A cool detached woman (early 20s) mid-stride across sun-bleached grey plaza tiles, late-afternoon golden-hour light carving harsh diagonal shadows leftward. Chin-length textured bob with casual bangs, thick black sunglasses, head slightly down. Oversized white tee with rust-red raglan sleeves and small chest logo, loosely tucked into baggy black carpenter jeans (white stitching), burgundy loafers, fine gold pendant. In left hand iced-coffee/chocolate plastic cup with straw, right hand half-eaten pastry. Hyperreal skin pores, fabric weave, pavement grit. Cool urban palette: neutral greys, white, rust-red, denim black, punctuated by vivid crimson tactical HUD overlays: red bounding boxes, crosshairs, telemetry glyphs, scanlines, timecode “18/02”, ID strings “CCWW | TR521”, numeric stream “19 5 3 21 18 9 20 25”, hashtags “#83575// #25747//”. Fragmented layout: main full-body frame plus three inset crops (face/drink, torso, pants cuff) linked by thin red vector lines. Grain, subtle chromatic aberration, high sharpness, raw photoreal fidelity. Mood: Y2K streetwear, dystopian chic, candid privacy-invasion moment, urban nonchalance under omnipresent gaze.
```

[[Fashion Editorial]] [[Cyberpunk Aesthetic]] [[High Angle Shot]] [[Y2K Streetwear]]

---

### 12. 超逼真海军时尚大片拍摄

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2025-12-09  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张超现实、电影感、全身的女性时尚图片。图片中，女性身着全海军蓝服装，背景为纯海军蓝色，并明确要求保留主体在上传参考图片中的确切身份和发型。

![超逼真海军时尚大片拍摄](https://cms-assets.youmind.com/media/1765440074154_n7lmzf_G7uUHBHbIAAITOf.jpg)
![超逼真海军时尚大片拍摄](https://cms-assets.youmind.com/media/1765440074455_8wa645_G7uUHDTbgAAs-2c.jpg)

```
{
  "type": "image_generation_prompt",
  "style": "hyper-realistic, cinematic, full-body fashion photoshoot",
  "subject": {
    "gender": "female",
    "age": 26,
    "height": "5'5\"",
    "identity_preservation": {
      "use_uploaded_image": true,
      "alter_face": false,
      "notes": "Exact face and hairstyle from the uploaded image must be preserved"
    },
    "pose": {
      "body_position": "leaning back on deep navy blue bean bag",
      "arm_position": "one arm resting on the edge of the bean bag",
      "leg_position": "legs slightly apart",
      "expression": "confident"
    }
  },
  "wardrobe": {
    "jacket": "navy blue denim jacket",
    "top": "white t-shirt",
    "bottoms": "navy blue denim jeans",
    "footwear": "chunky sneakers",
    "accessories": [
      "silver wristwatch"
    ]
  },
  "scene": {
    "background": {
      "color": "solid navy blue"
    },
    "props": [
      "deep navy blue bean bag"
    ]
  },
  "lighting": {
    "type": "cinematic studio lighting",
    "mood": "clean, confident",
    "contrast": "balanced",
    "texture_emphasis": true
  },
  "camera": {
    "framing": "full-body",
    "look": "fashion editorial",
    "details": "sharp focus, realistic skin texture"
  },
  "quality": {
    "resolution": "ultra high",
    "realism": "photorealistic",
    "detail_level": "hyper-detailed fabrics and accessories"
  },
  "output_goal": "Create a hyper-realistic cinematic full-body fashion image of the woman, preserving her exact identity, hairstyle, and proportions while presenting a confident all-navy fashion look against a solid navy background."
}
```

[[Fashion Editorial]] [[Face Consistency]] [[Full Body Shot]]

---

### 13. Y2K 可爱时尚画报提示

**Author**: [Glitter Gal](https://x.com/GlitterPixely)  **Date**: 2025-12-09  **Language**: en

> 一个高度详细、结构化的 JSON 提示，用于生成多面板、风格一致的 Y2K 卡哇伊时尚编辑图片，重点关注超广角透视、超女性化美学，以及模特的特定服装和生物特征。

![Y2K 可爱时尚画报提示](https://cms-assets.youmind.com/media/1765440060030_2mx80j_G7syXMgXAAAkkha.jpg)

```
{
  "meta_control": {
    "generation_mode": "multi_panel_consistent",
    "priority_stack": ["identity_lock", "perspective_physics", "material_fidelity", "environmental_coherence"],
    "quality_target": "editorial_print_ready"
  },
  "intent": {
    "primary": "Y2K Kawaii-fashion editorial with extreme wide-angle perspective study",
    "secondary": "Technical demonstration of foreshortening in a hyper-feminine aesthetic",
    "publication_context": "Double-page spread, pop-culture magazine collage layout"
  },
  "frame": {
    "aspect_ratio": "9:16",
    "layout": {
      "type": "2x2 grid collage",
      "gutter_width": "2px pink or seamless",
      "panel_uniformity": "identical dimensions per panel"
    }
  },
  "subject": {
    "type": "Human female fashion model",
    "identity_lock": {
      "enforcement_level": "strict",
      "anchor_features": ["face_geometry", "skin_tone", "body_proportions", "hair_color"]
    },
    "biometrics": {
      "age_presentation": "20-24",
      "height_cm": 170,
      "build": "Slender, petite model frame",
      "ethnicity_presentation": "Caucasian / Northern European features"
    },
    "facial_signature": {
      "structure": "Soft oval face shape, full cheeks, rounded feminine jawline",
      "eyes": "Large, expressive, bright blue, defined lashes with rhinestone accents",
      "nose": "Small, delicate button nose, slightly upturned",
      "lips": "Very full, plush and pillowy, glossy bubblegum pink",
      "skin": "Porcelain fair, smooth texture, heavy blush on nose and cheeks, highlighter glow",
      "expression_default": "Playful cute, duck face, winking, blowing kiss"
    },
    "hair": {
      "style": "Long golden blonde hair, half-up pigtails with fluffy scrunchies",
      "texture": "Silky, voluminous, crimped sections",
      "behavior": "Bouncing, dynamic movement"
    },
    "wardrobe": {
      "jacket": {
        "item": "Cropped faux-fur jacket",
        "material": "High-pile mongolian fur",
        "color": "Pastel baby pink",
        "state": "Slouched off shoulders",
        "light_behavior": "Soft diffusion, halo effect on fur tips"
      },
      "top": {
        "item": "Heart-shaped corset top",
        "material": "Satin with all-over rhinestone coverage",
        "color": "Hot pink",
        "fit": "Structured, push-up",
        "details": "Crystal straps, glitter trim"
      },
      "pants": {
        "item": "Wide-leg parachute pants",
        "material": "Iridescent nylon fabric",
        "color": "Metallic rose gold",
        "details": "Drawstrings, butterfly patches, sequin pockets"
      },
      "footwear": {
        "item": "Mega-platform boots",
        "color": "White patent leather with glitter soles",
        "condition": "Pristine, reflective",
        "details": "Furry leg warmers attached"
      }
    },
    "accessories": {
      "neck": "Choker with large heart-shaped pendant"
    }
  }
```

[[Fashion Editorial]] [[Y2K Aesthetic]] [[Kawaii Aesthetic]] [[Multi-Panel Layout]]

---

### 14. Nano Banana Pro 的 9 场景时尚拼贴网格提示

**Author**: [Abbay](https://x.com/LearnWithAbbay)  **Date**: 2025-12-09  **Language**: en

> 一个为 Nano Banana Pro 设计的高度详细的提示，用于根据上传的角色图像生成 3x3 网格拼贴照片。该提示指定了九个独立的、高时尚、互联网潮流的场景，每个场景都详细描述了特定的服装（街头服饰、睡裙、瑜伽服、Y2K 风格、晚礼服、赛博朋克、西装、比基尼、静奢风）和相应的背景，旨在达到高端杂志社论的品质。

![Nano Banana Pro 的 9 场景时尚拼贴网格提示](https://cms-assets.youmind.com/media/1765440081690_1toqiy_G7sZ6h1bEAAEjTP.jpg)

```
Based on [uploaded character image] and strictly maintaining unchanged facial features, generate a highly fashionable and internet-trendy 3x3 grid collage photo, with the nine independent scenes respectively showing the character wearing: cool streetwear black Oversized hoodie paired with cargo pants ({argument name="streetwear background" default="graffiti neon back alley background"}), pure and sexy white silk slip nightgown with an outer knitted sweater ({argument name="nightgown background" default="soft light lazy bedroom window-side background"}), tight body-shaping fashionable yoga set ({argument name="yoga background" default="high-end lighting gym background"}), retro Y2K hot girl crop top paired with low-waist denim skirt ({argument name="Y2K background" default="millennial colorful CD-filled room background"}), glamorous black high-slit sequin evening gown ({argument name="evening gown background" default="city skyline rooftop bar night scene background"}), avant-garde cyberpunk functional strap outfit ({argument name="cyberpunk background" default="futuristic rainy night street blue-purple light background"}), urban modern silhouette suit with inner crop top ({argument name="suit background" default="minimalist high-end art gallery background"}), hot vacation bikini paired with transparent sun-protective cover-up ({argument name="bikini background" default="luxurious sea-view pool sunset background"}), and quiet luxury old money rough tweed little black jacket suit set ({argument name="quiet luxury background" default="classical European manor courtyard background"}), with the overall image pursuing high-end magazine editorial quality, captivating light and shadow, and rich trendy tension.
```

[[Fashion Editorial]] [[3x3 Grid Layout]]

---

### 15. 高级时装玛丽莲·梦露姿势重现提示

**Author**: [Super Edge AI 🦸🦸](https://x.com/KimAkiyama81)  **Date**: 2025-12-08  **Language**: en

> 一个详细的提示，用于生成一张东亚女性的高级时装编辑图片，她正在城市人行道格栅上重现玛丽莲·梦露（Marilyn Monroe）标志性的“七年之痒”姿势。提示中指定了 20 世纪 50 年代的波波头、黑金露背连衣裙、动感的姿势以及柔和、漫射的自然日光，以营造复古魅力美学。

![高级时装玛丽莲·梦露姿势重现提示](https://cms-assets.youmind.com/media/1765438599405_lb2ks3_G7qadyCWsAAbJzP.jpg)

```
{
"subject": {
"description": "East Asian female subject standing on a city sidewalk grate in a pose reminiscent of the Marilyn Monroe 'Seven Year Itch' scene. She is leaning forward with knees bent and pressed together, holding the front hem of her dress down as the skirt billows upward in a wide, circular flare around her hips. Her posture is dynamic and joyful.",
"age": "Early to mid 20s",
"expression": "Ecstatic laughter, head tilted slightly back, eyes squeezed shut in joy, wide open-mouth smile showing teeth.",
"hair": {
"color": "Jet black",
"style": "Chin-length vintage 1950s-style bob with voluminous, sculpted waves and a deep side part."
},
"clothing": {
"top": {
"type": "Halter-neck bodice",
"color": "Black with gold trim",
"details": "Deep V-neckline plunging to mid-torso, metallic gold piping along the neckline and waist, pleated fabric texture."
},
"bottom": {
"type": "Pleated circle skirt",
"color": "Black with gold trim",
"details": "Accordian pleats, metallic gold hemline, billowing upward in a rigid, parachute-like shape due to air from below."
},
"shoes": {
"type": "High-heeled sandals",
"color": "Black",
"details": "Minimalist design, thin ankle strap with buckle, slender toe strap, stiletto heel."
}
},
"face": {
"preserve_original": true,
"makeup": "Matte porcelain skin finish, sharp winged black eyeliner, defined dark eyebrows, vibrant matte red lipstick."
}
},
"accessories": {
"jewelry": {
"earrings": "Large, sparkling crystal/diamond cluster stud earrings with a vintage floral shape."
}
},
"photography": {
"camera_style": "High-fashion editorial, sharp digital photography",
"angle": "Full-body shot, slightly low angle to emphasize the skirt's volume",
"shot_type": "Vertical portrait",
"aspect_ratio": "2:3",
"texture": "Clean, high contrast, soft focus background"
},
"background": {
"setting": "Urban street corner, storefront exterior",
"wall_color": "Dark charcoal grey/black",
"elements": [
"Storefront window with white text 'Fleurette Jewelry'",
"Doorway number '590' on glass transom",
"Classic architectural columns with molding",
"Metal subway grate on concrete sidewalk"
],
"atmosphere": "Retro-glamour, joyous, metropolitan",
"lighting": "Soft, diffused natural daylight (overcast), even illumination on subject"
}
}
```

[[Fashion Editorial]] [[Diffused Natural Light]] [[East Asian Model]]

---

### 16. 巴洛克洛丽塔连衣裙时尚提示

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-08  **Language**: en

> 一张图像生成提示，详细描述了创建一张逼真的日本年轻女性图像，她身穿一件华丽的深蓝色和白色洛丽塔连衣裙，裙身带有巴洛克设计元素、金色饰边和精致的蕾丝细节。

![巴洛克洛丽塔连衣裙时尚提示](https://cms-assets.youmind.com/media/1765438622912_5uhiku_G7p32dpakAELS0u.jpg)
![巴洛克洛丽塔连衣裙时尚提示](https://cms-assets.youmind.com/media/1765438623692_w0d7o3_G7p36OqbMAAmSjx.jpg)

```
A beautiful japanese young woman Navy blue and white Lolita dress with ornate baroque design and gold trim details. White puff sleeves with lace ruffles and navy ribbon ties. Navy blue bodice with gold embroidered motifs and lace-up front corset styling. White lace collar with decorative brooch detail. Navy blue full skirt with gold embroidered patterns and brocade fabric. White lace apron overlay with ruffled edges. Navy and white hair bow accessory with lace and ribbon details. Classic Lolita style with navy, white, and gold color palette. Baroque elegant aesthetic with ornate decorative elements. NOT casual wear, NOT minimalist design, NOT modern styling.
```

[[Fashion Editorial]]

---

### 17. 超写实时尚编辑人像提示词

**Author**: [NanoInspire](https://x.com/NanoInspirate)  **Date**: 2025-12-08  **Language**: en

> 一个高度详细、结构化的提示，专为超现实主义的时尚编辑摄影而设计，重点是一幅身穿黑色西装外套的年轻女性的戏剧性、高对比度黑白肖像。它详细说明了拍摄对象的细节、光线、氛围以及精确的相机设置，如镜头和光圈，以实现最大的照片级真实感。

![超写实时尚编辑人像提示词](https://cms-assets.youmind.com/media/1765438592035_gss8eh_G7oU4w7WwAAwS_7.jpg)

```
{
  "prompt_description": {
    "subject": "A young adult woman, likely in her early to mid-twenties, with a slender build and a confident, poised demeanor.",
    "face": "Angular facial structure with high cheekbones and a defined jawline. Eyes are open and alert, with a direct, engaging gaze. Lips are slightly parted, conveying a subtle sensuality. Skin has a visible texture, with fine pores and subtle freckling across the décolletage. Expression is neutral but intense.",
    "hair": "Dark brown, shoulder-length hair with a wet or slicked-back appearance. A few strands are artfully draped across her face, adding a touch of drama.",
    "clothing": "A black blazer, worn open to reveal the upper chest. The blazer has a sharp lapel and appears to be made of a structured fabric that holds its shape. The neckline is a deep V, exposing the collarbones and upper chest. The fit of the blazer is tailored but not restrictive, with the front edges falling away from the body.",
    "accessories": "No visible accessories.",
    "environment": "A plain, dark, studio background. The background is uniformly dark, creating a strong contrast with the subject and emphasizing her form. There is a subtle gradient in the darkness, suggesting a controlled lighting setup rather than a flat wall.",
    "lighting": "Dramatic, high-contrast studio lighting. A key light source appears to be positioned slightly above and to the side of the subject, creating strong highlights on her face, collarbones, and the fabric of the blazer. Deep shadows are present, particularly on the right side of her face and in the background, adding depth and sculpting her features. Specular highlights catch the moisture in her hair and the subtle sheen of her skin.",
    "atmosphere": "Sophisticated, alluring, and powerful. The mood is one of confident sensuality and high fashion."
  },
  "style": {
    "art_style": "Ultra-realistic editorial fashion photography",
    "color_grade": "Monochromatic (black and white), with a high-contrast grade. Deep blacks, bright whites, and a wide range of grays are present, emphasizing texture and form.",
    "texture_quality": "Extremely sharp and detailed, with a focus on micro-contrast. Every pore, strand of hair, and fabric texture should be rendered with photorealistic clarity. Minimal to no digital grain."
  },
  "camera_settings": {
    "camera": "Medium Format or high-end DSLR",
    "lens": "85mm or 105mm portrait lens, implying slight compression and beautiful bokeh",
    "aperture": "f/2.8 - f/4.0 (suggesting a shallow depth of field, but with enough in focus to capture facial details clearly)",
    "iso": "Low ISO (e.g., 100-200) to ensure maximum detail and minimal noise",
    "shutter_speed": "Fast shutter speed to freeze motion perfectly",
    "white_balance": "Neutral or slightly cool white balance to enhance the monochrome tones."
  },
  "composition": {
    "framing": "Medium shot - upper chest to head"}
```

[[Fashion Editorial]] [[High Contrast Lighting]] [[Black And White Portrait]]

---

### 18. 日本辣妹杂志校服专题

**Author**: [cppp](https://x.com/mmm53096445)  **Date**: 2025-11-22  **Language**: ja

> 一个用于生成日式辣妹风杂志专题页面的提示，内容聚焦于校服穿搭造型。

![日本辣妹杂志校服专题](https://cms-assets.youmind.com/media/1763885594270_mwd5m6_G6WYLU0bwAAvl24.jpg)

```
日本のギャル雑誌。制服の着こなし特集ページ。
```

[[Fashion Editorial]] [[School Uniform]]

---

### 19. 奢华露台夜景魅力自拍

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-04-07  **Language**: en

> 这是一个高度详细且结构化的提示词，用于生成一张苗条、运动型女性的魅力自拍图像（使用参考图）。提示词指定了服装（奶油色深 V 领迷你裙）、场景（夜间户外奢华露台，背景为城市天际线）、构图（高角度自拍，广角镜头畸变）以及光照（正面闪光灯/环形灯），旨在实现超写实的商业时尚摄影效果。

![奢华露台夜景魅力自拍](https://cms-assets.youmind.com/media/1775631287517_ndjcvm_HFUQ-aNbAAAFUTZ.jpg)

```
{
  "image_description": {
    "subject": {
      "use_reference_image": true,
      "override": false,
      "physique": {
        "build": "Slim-curvy, athletic",
        "pose": "Selfie perspective, one arm extended toward the camera, other hand resting on hip, slight body tilt"
      }
    },
    "attire": {
      "outfit": "Form-fitting cream/off-white mini dress",
      "neckline": "Extremely deep plunging V-neck",
      "sleeves": "Long sleeves with slightly structured/padded shoulders",
      "accessories": "Wide, silver rhinestone-embellished belt at the waist, large thin silver hoop earrings"
    },
    "setting": {
      "location": "Outdoor luxury terrace or resort at night",
      "foreground": "Smooth beige stone or concrete walkway",
      "midground": "Sharp, dark green palm tree fronds and tropical foliage",
      "background": "Nighttime city skyline, distant glowing skyscrapers, blurred urban lights, silhouette of a bridge or landmark in the far distance"
    },
    "composition_and_lighting": {
      "camera_angle": "High-angle selfie, wide-angle lens distortion on the extended arm",
      "lighting_type": "Frontal flash or ring light creating a 'deer-in-the-headlights' glamor effect",
      "lighting_effects": "High contrast between the bright subject and the dark night background, soft bokeh on city lights",
      "color_palette": "Warm golds, creams, and tans contrasted against deep greens and navy-blue night sky",
      "aspect_ratio": "4:5 (Vertical)"
    },
    "technical_tags": [
      "8k resolution",
      "photorealistic",
      "highly detailed skin texture",
      "commercial fashion photography",
      "shot on iPhone 15 Pro",
      "sharp focus on face",
      "glamour photography"
    ]
  }
}
```

[[Fashion Photography]] [[City Skyline Background]]

---

### 20. Nano Banana Pro 编辑级摄影构图提示词

**Author**: [Picts by AI](https://x.com/pictsbyai)  **Date**: 2026-04-06  **Language**: en

> 一份高度详细、结构化的提示词，用于生成编辑级摄影作品。重点关注构图、色彩配置、光影和技术规格，旨在打造具有高对比度和柔和漫射光效果的精致都市肖像风格。

![Nano Banana Pro 编辑级摄影构图提示词](https://cms-assets.youmind.com/media/1775544741876_1m562y_HFNQy2gX0AAnj80.jpg)

```
{
"metadata": {
"image_type": "photograph",
"primary_purpose": "editorial/social media"
},
"composition": {
"rule_applied": "rule of thirds/asymmetry",
"aspect_ratio": "4:5",
"layout": "single subject with deep background context",
"focal_points": [
"White coffee cup and subject's face/sunglasses",
"Silver watch on the subject's left wrist"
],
"visual_hierarchy": "Eye immediately catches the high-contrast white cup and face, moves down the black outfit to the silver watch, and sweeps out to the textured stone wall and deep street background.",
"balance": "asymmetric - solid, close-up weight of the subject and stone wall on the right is balanced by the open spatial depth of the street on the left"
},
"color_profile": {
"dominant_colors": [
{
"color": "Black",
"hex": "#111111",
"percentage": "45%",
"role": "primary subject"
},
{
"color": "Cool Stone Gray",
"hex": "#C4C6C5",
"percentage": "40%",
"role": "background/foreground architecture"
},
{
"color": "Off-White",
"hex": "#E8E7E3",
"percentage": "10%",
"role": "background architecture"
},
{
"color": "Bright White",
"hex": "#FFFFFF",
"percentage": "5%",
"role": "accent/focal point"
}
],
"color_palette": "monochromatic/neutral",
"temperature": "cool",
"saturation": "desaturated",
"contrast": "high contrast between subject and background, soft contrast within lighting"
},
"lighting": {
"type": "natural window/diffused outdoor",
"source_count": "single source - overcast sky",
"direction": "diffused from above/front",
"directionality": "diffused",
"quality": "soft light/even",
"intensity": "moderate",
"contrast_ratio": "low contrast (flat/even lighting)",
"mood": "calm/casual/professional",
"shadows": {
"type": "soft gradual edges",
"density": "gray/faint",
"placement": "under jawline, under clothing folds, soft drop shadow on wall behind subject",
"length": "short"
},
"highlights": {
"treatment": "subtle/specular on metallic surfaces",
"placement": "on silver watch, sunglasses frames, and slight sheen on leather/fabric edges"
},
"ambient_fill": "present",
"light_temperature": "cool (blue tint in grays)"
},
"technical_specs": {
"medium": "digital photography",
"style": "realistic",
"texture": "sharp/detailed",
"sharpness": "tack sharp on subject and foreground, slightly soft background",
"grain": "none/minimal digital noise",
"depth_of_field": "medium - subject and immediate wall are sharp, background street gracefully falls slightly out of focus",
"perspective": "straight on/eye level"
},
"artistic_elements": {
"genre": "portrait/street fashion",
"influences": [
"Modern streetwear editorial",
"Scandinavian minimalist fashion photography"
],
"mood": "sophisticated/calm/polished",
"atmosphere": "A crisp, cool urban morning capturing a quiet, stylish moment.",
"visual_style": "clean/structured/minimal color"
},
"typography": {
"present":
```

[[Fashion Photography]] [[High Contrast Lighting]] [[Soft Diffused Light]] [[Urban Portrait]]

---

### 21. Nano Banana Pro 编辑级摄影构图提示词

**Author**: [Picts by AI](https://x.com/pictsbyai)  **Date**: 2026-04-06  **Language**: en

> 一份高度详细、结构化的提示词，用于生成编辑级摄影作品。重点关注构图、色彩配置、光影和技术规格，旨在打造具有高对比度和柔和漫射光效果的精致都市肖像风格。

![Nano Banana Pro 编辑级摄影构图提示词](https://cms-assets.youmind.com/media/1775544741876_1m562y_HFNQy2gX0AAnj80.jpg)

```
{
"metadata": {
"image_type": "photograph",
"primary_purpose": "editorial/social media"
},
"composition": {
"rule_applied": "rule of thirds/asymmetry",
"aspect_ratio": "4:5",
"layout": "single subject with deep background context",
"focal_points": [
"White coffee cup and subject's face/sunglasses",
"Silver watch on the subject's left wrist"
],
"visual_hierarchy": "Eye immediately catches the high-contrast white cup and face, moves down the black outfit to the silver watch, and sweeps out to the textured stone wall and deep street background.",
"balance": "asymmetric - solid, close-up weight of the subject and stone wall on the right is balanced by the open spatial depth of the street on the left"
},
"color_profile": {
"dominant_colors": [
{
"color": "Black",
"hex": "#111111",
"percentage": "45%",
"role": "primary subject"
},
{
"color": "Cool Stone Gray",
"hex": "#C4C6C5",
"percentage": "40%",
"role": "background/foreground architecture"
},
{
"color": "Off-White",
"hex": "#E8E7E3",
"percentage": "10%",
"role": "background architecture"
},
{
"color": "Bright White",
"hex": "#FFFFFF",
"percentage": "5%",
"role": "accent/focal point"
}
],
"color_palette": "monochromatic/neutral",
"temperature": "cool",
"saturation": "desaturated",
"contrast": "high contrast between subject and background, soft contrast within lighting"
},
"lighting": {
"type": "natural window/diffused outdoor",
"source_count": "single source - overcast sky",
"direction": "diffused from above/front",
"directionality": "diffused",
"quality": "soft light/even",
"intensity": "moderate",
"contrast_ratio": "low contrast (flat/even lighting)",
"mood": "calm/casual/professional",
"shadows": {
"type": "soft gradual edges",
"density": "gray/faint",
"placement": "under jawline, under clothing folds, soft drop shadow on wall behind subject",
"length": "short"
},
"highlights": {
"treatment": "subtle/specular on metallic surfaces",
"placement": "on silver watch, sunglasses frames, and slight sheen on leather/fabric edges"
},
"ambient_fill": "present",
"light_temperature": "cool (blue tint in grays)"
},
"technical_specs": {
"medium": "digital photography",
"style": "realistic",
"texture": "sharp/detailed",
"sharpness": "tack sharp on subject and foreground, slightly soft background",
"grain": "none/minimal digital noise",
"depth_of_field": "medium - subject and immediate wall are sharp, background street gracefully falls slightly out of focus",
"perspective": "straight on/eye level"
},
"artistic_elements": {
"genre": "portrait/street fashion",
"influences": [
"Modern streetwear editorial",
"Scandinavian minimalist fashion photography"
],
"mood": "sophisticated/calm/polished",
"atmosphere": "A crisp, cool urban morning capturing a quiet, stylish moment.",
"visual_style": "clean/structured/minimal color"
},
"typography": {
"present":
```

[[Fashion Photography]] [[High Contrast Lighting]] [[Soft Diffused Light]] [[Urban Portrait]]

---

### 22. 复古跑车上的超写实夏季生活方式摄影

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-03  **Language**: en

> 一个用于生成超写实、高对比度时尚大片的提示词，画面为一名身穿亮绿色泳装的年轻女性躺在阳光明媚的停车场中，一辆光泽感十足的白色复古跑车引擎盖上。

![复古跑车上的超写实夏季生活方式摄影](https://cms-assets.youmind.com/media/1775284650245_2he84v_HFBHOZVagAA9r_C.jpg)
![复古跑车上的超写实夏季生活方式摄影](https://cms-assets.youmind.com/media/1775284650235_pc77u8_HFBHNybaEAEbJZk.jpg)
![复古跑车上的超写实夏季生活方式摄影](https://cms-assets.youmind.com/media/1775284650342_ouxs25_HFBHNAlbQAAXLOa.jpg)
![复古跑车上的超写实夏季生活方式摄影](https://cms-assets.youmind.com/media/1775284651299_aeqyqv_HFBHPAMaAAAYRpO.jpg)

```
ultra realistic photo of a young woman lying on the hood of a luxury vintage sports car,

pose: relaxed pose stretched on car hood, one hand on forehead blocking sunlight, eyes softly closed or half-open, natural calm expression,

appearance: long dark hair spread naturally, glowing sun-kissed skin, minimal makeup, effortless beauty,

outfit: {argument name="swimsuit color" default="bright green"} one-piece swimsuit, clean minimal design, smooth fabric, tight fit,

environment: outdoor parking lot under bright sunlight, minimal background, clean asphalt, subtle greenery in distance,

car: classic luxury sports car with smooth curves, glossy white finish, premium details,

lighting: harsh natural sunlight, strong highlights, deep shadows, high contrast, summer vibe,

camera: top-down slightly angled shot, lifestyle photography, sharp focus, natural perspective,

style: editorial fashion photography, luxury summer aesthetic, ultra detailed, realistic skin tones,

no watermark, no text, no UI elements --ar 2:3 --style raw --v 7 --stylize 100
```

[[Fashion Photography]]

---

### 23. 高定时装的公式化提示结构

**Author**: [Gadgetify](https://x.com/Gdgtify)  **Date**: 2026-03-01  **Language**: en

> 一个非 JSON 的公式化提示结构，用于比较 Nano Banana 和 Nano Banana 2。它通过结合模型、设置、氛围、相机设备（哈苏）和灯光等元素来定义目标图像，同时减去杂乱和塑料感皮肤等不需要的元素。

![高定时装的公式化提示结构](https://cms-assets.youmind.com/media/1772433517542_pefdzo_HCHvJJtWEAAV5jI.jpg)
![高定时装的公式化提示结构](https://cms-assets.youmind.com/media/1772433517592_esz27e_HCHtqSLWkAEvxK_.jpg)

```
Render_Target =  ( [MODEL] * Structural_High_Fashion_Attire ) +  ( [SETTING] * AI_Calculated_Environment_Lighting ) +  ( [OCCASION/VIBE] * Model_Expression_And_Pose ) +  ( Hasselblad_H6D_100c * Sharp_Focus * 1.5 ) + ( Geometric_Shadows_OR_Studio_Strobes * 1.2 ) -  ( Clutter / 2 ) -  ( Plastic_Skin / 2 ) -  ( Amateur_Photography / 2 )  # System Note: The AI must adapt the "AI_Calculated_Environment_Lighting" dynamically to whatever [SETTING] is inputted.
```

[[Fashion Photography]] [[Prompt Engineering]]

---

### 24. 时尚摄影提示：阳光迪斯科氛围

**Author**: [Zainab Fatima](https://x.com/Zainabfat2728)  **Date**: 2026-02-27  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张充满活力、高对比度的时尚照片：一名年轻的红发女子跪在户外，手持一个银色迪斯科球，背景是明亮的绿色墙壁，置于强烈自然阳光下。

![时尚摄影提示：阳光迪斯科氛围](https://cms-assets.youmind.com/media/1772259945305_9wrbtv_HCKZsFqaAAABqiV.jpg)
![时尚摄影提示：阳光迪斯科氛围](https://cms-assets.youmind.com/media/1772259945427_fyt0z7_HCKZsF3acAAwC3j.jpg)

```
{
  "id": "img_001",
  "title": "Sunlit Disco Vibes",
  "category": "Fashion Photography",
  "description": "A stylish young woman with fair skin and red hair tied in a high ponytail is kneeling on a concrete surface while holding a reflective silver disco ball. She is dressed in a red swimsuit with white trim and white sneakers. The vibrant green backdrop behind her creates a bold color contrast with her outfit. Bright natural sunlight casts defined shadows on the ground, enhancing the dramatic and modern aesthetic of the image.",
  "subject": {
    "gender": "female",
    "hair_color": "red",
    "hairstyle": "high ponytail",
    "accessories": ["sunglasses"],
    "outfit": {
      "type": "swimsuit",
      "color": "red",
      "details": "white trim",
      "footwear": "white sneakers"
    }
  },
  "environment": {
    "location_type": "outdoor",
    "floor": "concrete",
    "background": "bright green wall",
    "props": ["silver disco ball"]
  },
  "lighting": {
    "type": "natural sunlight",
    "intensity": "bright",
    "shadow_effect": "sharp and defined"
  },
  "composition": {
    "camera_angle": "slightly elevated",
    "focus": "subject and reflective disco ball",
    "style": "modern, vibrant, high-contrast"
  },
  "mood": [
    "confident",
    "energetic",
    "stylish",
    "summer vibe",
    "bold"
  ],
  "color_palette": {
    "primary": "red",
    "secondary": "green",
    "accent": "silver",
    "neutral": "white"
  },
  "resolution_type": "high quality digital photograph"
}
```

[[Fashion Photography]] [[Strong Natural Sunlight]]

---

### 25. 超逼真时尚摄影提示

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-02-27  **Language**: en

> 一个用于 Nano Banana Pro 的提示，生成一张超现实电影风格的时尚大片，画面中一名年轻男子身穿超大号深巧克力色街头服饰，随意地坐在白色懒人沙发上，背景是极简的灰色。

![超逼真时尚摄影提示](https://cms-assets.youmind.com/media/1772259929892_pqaff1_HCJ6YQcbAAAeV-m.jpg)

```
Hyper-realistic cinematic fashion photoshoot of a young man. He has a refined slim face with a lean, youthful, and elegant physique. Seated casually on a deep white bean bag, he wears bold all-dark chocolate oversized streetwear: a stylish trench coat over a clean white inner t-shirt, wide white pants, chunky sneakers, and a silver watch. The background is minimal with an aesthetic grey tone.
```

[[Fashion Photography]] [[Cinematic Style]]

---

### 26. 皇家马德里足球迷自拍提示词

**Author**: [Pinodi](https://x.com/PinodiArt)  **Date**: 2026-02-22  **Language**: en

> 一个详细、结构化的提示，用于生成一张年轻女性身穿皇家马德里球衣和极简比基尼下装，趴着自拍的图像。该提示详细说明了极端的解剖细节、光线、姿势和场景元素，强调了夸张的沙漏型身材和详细的足部解剖结构。

![皇家马德里足球迷自拍提示词](https://cms-assets.youmind.com/media/1771828732562_sg8w3g_HBuP2ORW0AAZsiS.jpg)

```
{
  "subject": {
    "description": "Young woman with silver-grey hair, tied in a messy, textured bun with loose, wispy strands framing the face. Facial features include striking green eyes, clear skin, and a defined jawline. Her mouth is closed with a neutral to slightly soft expression. She is captured in a prone selfie pose on a bed.",
    "body": {
      "physique": "Extraordinarily pronounced hourglass figure with an extreme waist-to-hip ratio. Her waist is extremely narrow, contrasting with very large, prominent, and full rounded glutes. Wide pelvic structure with an exaggerated lower body curve and voluminous thighs.",
      "details": "Slender, toned upper body and limbs with anatomically precise skin textures, realistic pores, and subtle muscle definition in the lower back (lumbar lordosis). The pose emphasizes the lateral flare of the hips and the significant volume of the posterior. Detailed and anatomically correct feet with five distinct, well-defined toes and realistic sole textures including natural skin folds."
    }
  },
  "wardrobe": {
    "top": "A classic Real Madrid home soccer jersey in crisp white with subtle textures, featuring high-fidelity fabric mesh. All sponsor logos, the club crest, and any text on the jersey must be rendered with extreme sharpness and clarity, appearing authentic and legible, not blurred or distorted.",
    "bottom": "A minimalist, thin black string bikini bottom with a high-cut design to further accentuate the hip width and gluteal volume.",
    "accessories": "A delicate silver ring on the ring finger. Holding a matte pink smartphone."
  },
  "pose_action": {
    "description": "Lying prone on a bed, propped up on elbows. The subject is holding a pink phone with her right hand to take a mirror-style selfie. Her legs are bent at the knees and crossed at the ankles, with her feet raised high toward the ceiling exactly as in the reference image. The soles of her feet are tilted and facing directly toward the camera, showing detailed sole anatomy and toe alignment.",
    "expression": "Neutral to slightly soft expression with green eyes directed toward the phone screen, lips together and closed."
  },
  "scene": {
    "setting": "A dimly lit, moody modern bedroom at night. The subject is on a white quilted comforter that reflects the soft ambient light.",
    "background": "Large window showing a dark night sky with a faint glow of distant city lights. The interior walls are in deep, soft shadows, creating an intimate atmosphere.",
    "elements": "A bedside lamp providing a warm, localized glow, natural nighttime indoor ambiance."
  },
  "lighting": {
    "type": "Low-light atmospheric lighting with warm accent highlights.",
    "details": "Soft, warm illumination from a nearby bedside lamp creating a gentle rim light on the subject's silhouette and hair bun. Subtle blueish ambient light from the window provides a cool contrast i
```

[[Fashion Photography]]

---

### 27. Billie Eilish 身着白色皮质束身衣和靴子的 4K 高清照片

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-02-04  **Language**: en

> 一个结构化的提示，用于生成 Billie Eilish 的 4K 高清照片。它详细描述了她的服装（白色皮革无肩带紧身胸衣、迷你裙、及膝靴）、姿势（蹲在混凝土上）和环境（带有风化胶合板和红砖墙的室外建筑角落），强调高纹理细节和逼真的色彩。

![Billie Eilish 身着白色皮质束身衣和靴子的 4K 高清照片](https://cms-assets.youmind.com/media/1770273450639_whkve7_HATxS_NasAAKktK.jpg)
![Billie Eilish 身着白色皮质束身衣和靴子的 4K 高清照片](https://cms-assets.youmind.com/media/1770273450707_mlidgd_HATxUNCboAAITWY.jpg)

```
{ "prompt_metadata": { "version": "1.0", "target_quality": "4K HD Photograph", "aspect_ratio": "9:16" }, "subject": { "name": "{argument name="subject name" default="Billie Eilish"}", "appearance": { "hair": "Blonde hair", "facial_features": [ "Full natural look", "Defined eyebrows", "Plump lips" ], "accessories": [ "Large silver hoop earrings", "Beaded bracelet on right wrist" ] }, "attire": { "top": "White leather strapless corset top", "bottom": "White mini skirt", "footwear": "White knee-high boots" }, "pose": "Crouched on concrete, looking directly at camera, right hand resting on knee, left arm extended downwards" }, "environment": { "location": "Outdoor architectural corner", "ground_texture": "Smooth concrete floor", "background_elements": { "left_side": "Weathered plywood wall featuring a white-framed window", "right_side": "Red brick wall with a white fluted column and concrete base" } }, "technical_specifications": { "lighting": "Natural daylight with soft, diffused shadows", "focus": "Sharp focus on subject", "texture_detail": [ "High-detail leather grain", "Realistic hair strands", "Weathered wood grain", "Tactile brick texture" ], "color_profile": "Realistic coloring, high dynamic range" } }
```

[[Fashion Photography]] [[4K Resolution]] [[Mini Skirt]] [[Knee-High Boots]]

---

### 28. 逼真的名人自拍风格肖像

**Author**: [Nobara](https://x.com/Nobarakia)  **Date**: 2026-02-03  **Language**: en

> 一个详细的 JSON 提示，用于生成一张名人自拍风格的超写实肖像，重点突出 Sydney Sweeney 的外貌，具体描述了她的发型、妆容（柔和魅力妆）、黑色紧身胸衣上衣，以及柔和、漫射的美颜光线。

![逼真的名人自拍风格肖像](https://cms-assets.youmind.com/media/1770187171422_i1ghwk_HAPR92aWgAEamF4.jpg)

```
{
  "prompt": {
    "subject": {
      "appearance": {
        "hair": {
          "color": "Honey blonde with lighter balayage highlights",
          "style": "Long, voluminous loose waves",
          "texture": "Silky, shiny, healthy",
          "parting": "Middle part",
          "framing": "Face-framing curtain layers"
        },
        "face": {
          "shape": "Heart-shaped with soft jawline",
          "eyes": "Large, almond-shaped, blue/green, heavy-lidded/sultry",
          "lips": "Full, pillowy, natural pink",
          "skin": "Fair, flawless, radiant, dewy finish"
        },
        "makeup": {
          "style": "Soft glam / 'Clean girl' aesthetic",
          "eyes": "Subtle winged eyeliner, defined lashes, champagne shimmer",
          "cheeks": "Rosy flush blush, soft highlight on cheekbones",
          "lips": "Glossy nude-pink lip tint"
        }
      },
      "clothing": {
        "type": "Strapless corset top / bustier",
        "color": "{argument name="clothing color" default="Black"}",
        "fabric": "Satin or silk",
        "neckline": "Sweetheart with a twisted/bow-front detail",
        "fit": "Form-fitting, accentuating décolletage"
      },
      "poses": [
        "Playful pout with head tilted slightly",
        "Looking over shoulder with a soft smile",
        "Direct gaze holding a makeup item",
        "Framing face with hands in a V-shape under chin"
      ]
    },
    "environment": {
      "location": "Indoor setting, likely a bathroom or dressing room",
      "background": {
        "texture": "Horizontal wooden paneling or textured beige tiles",
        "colors": "Neutral tones, warm beige, light wood",
        "objects": "Hint of a mirror edge or towel bar in background"
      }
    },
    "lighting": {
      "type": "Soft, diffuse beauty lighting",
      "source": "Front-facing vanity light or ring light",
      "effect": "Even illumination on face, 'catchlights' in eyes, soft shadows"
    },
    "technical_specs": {
      "camera": "High-end smartphone front camera or mirrorless portrait lens",
      "focal_length": "35mm to 50mm equivalent",
      "aperture": "f/2.8 for slight depth of field",
      "resolution": "8k, Ultra High Definition",
      "style": "Photorealistic, celebrity selfie style, candid but polished"
    },
    "mood": "Flirty, confident, glamorous, playful, intimate"
  }
}
```

[[Fashion Photography]] [[Hyperrealistic Portrait]]

---

### 29. 镜面自拍，夸张的比例，以及分段染发

**Author**: [Pinodi](https://x.com/PinodiArt)  **Date**: 2026-01-31  **Language**: en

> 一个结构化的提示，用于生成一张女性的镜面自拍图像，该女性具有特定、夸张的解剖特征（极致沙漏身材）和分层染发。该提示着重强调在镜面反射中保持解剖学上的一致性，并详细说明了服装、姿势和灯光细节，以实现高分辨率、专业影棚品质的输出。

![镜面自拍，夸张的比例，以及分段染发](https://cms-assets.youmind.com/media/1769927665585_rf5fkf_G__RBpGXkAEnGwU.jpg)

```
{
  "subject": {
    "description": "Young woman with long, wavy split-dyed hair (half jet black, half platinum blonde) and straight-cut bangs. Facial features include soft doe-eyes with winged eyeliner and a delicate nose.",
    "body": "Extraordinarily pronounced hourglass figure with an extreme waist-to-hip ratio. Her waist is extremely narrow, contrasting with very large, prominent, and full rounded glutes. Wide pelvic structure with an exaggerated lower body curve and voluminous thighs. Slender, toned upper body and limbs with anatomically precise skin textures and subtle muscle definition in the lower back."
  },
  "wardrobe": {
    "top": "Simple pink cropped tank top.",
    "bottom": "Minimalist thin black bikini bottom with high-cut side straps; the garment is designed to emphasize the extreme lower body proportions and the voluminous curvature of the large glutes.",
    "feet": "Bare feet, no socks, natural skin texture.",
    "accessories": "Smartphone with a pink case."
  },
  "pose_action": {
    "position": "Lying prone on a white bed, propped up on elbows. Chin resting on one hand, while the other hand holds the phone for a mirror selfie.",
    "legs": "Legs bent at the knees, feet raised vertically toward the ceiling."
  },
  "scene": {
    "environment": "Minimalist bedroom with neutral-toned walls. Large bed with rumpled white linens and plush pillows.",
    "background": "Soft window light entering from the side, creating a clean, domestic atmosphere.",
    "reflection_integrity": "Mirror reflection must accurately synchronize the subject's pose, hair color split, and the phone case position. Reflection rules apply to maintain anatomical consistency."
  },
  "lighting": {
    "type": "Soft, natural daylight from a lateral window source.",
    "effects": "Gentle shadows emphasizing the deep curvature of the hips and the texture of the bedding; high dynamic range."
  },
  "camera": {
    "aspect_ratio": "9:16",
    "angle": "Eye-level mirror shot, medium-full body framing.",
    "technical": "High-resolution portrait photography, sharp focus on the subject with soft background bokeh, 8k resolution, professional studio quality."
  },
  "negative_constraints": [
    "no socks",
    "no logos",
    "no text",
    "no beautify smoothing",
    "no extra limbs",
    "no watermark",
    "no distorted proportions in reflection"
  ]
}
```

[[Fashion Photography]] [[Hourglass Figure]]

---

### 30. 高端电商肖像与 UI 叠加提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个复杂的提示结构，旨在生成高端、全身的电商影棚肖像，并叠加模拟的手机浏览器界面（UI 层），强调主体上的体积光和叠加层扁平、简洁的数字图形。

![高端电商肖像与 UI 叠加提示](https://cms-assets.youmind.com/media/1769236026207_pbqo1r_G_VlG8kaAAA-o42.jpg)

```
"Subject Reference: A full-body portrait of \[INSERT SUBJECT NAME\]. Scene Description: A full-body, centered portrait of the subject \[INSERT POSE DESCRIPTION\]. The subject has \[INSERT EXPRESSION\], staring directly at the camera. The immediate background behind the subject is a \[INSERT BACKGROUND TYPE, e.g., seamless, pure high-key white studio backdrop\]. Crucially, the subject is lit with volumetric studio lighting that creates deep definitions, realistic shadows, and a strong 3D quality on her body and the folds of the outfit, distinguishing her sharply from the flat background without casting shadows on the floor. CRITICAL DETAIL (UI Layer): The entire photographic image is digitally layered beneath a simulated mobile phone browser interface overlay. Four distinct, clean, white, rectangular browser window elements are stacked vertically and angled slightly, segmenting the subject. Each window bar contains the sharp text '{argument name="browser text" default="[INSERT LINK OR TEXT HERE]"}'. The area outside the active white browser windows is a solid, uniform, dark charcoal gray/black matte UI frame, with absolutely no light bleed or color gradients. Style: Hybrid Composition: A highly realistic, three-dimensional studio photograph with deep color depth, overlaid with flat, clean digital graphics. Lighting Quality: Specific volumetric studio lighting focused ONLY on the subject. Soft, directional light from slightly off-center to sculpt the body and the rich texture of the fabric, creating depth. The background must remain completely flat. Color Palette: High contrast. \[INSERT OUTFIT COLOR\] outfit against \[INSERT BACKGROUND COLOR\] backdrop, framed by the dark matte gray UI. Texture and Mood: Realistic skin and rich fabric texture contrasting with the smooth digital elements of the UI. Intentional inclusion of subtle digital noise/grain to mimic a screen capture. Full body, centered portrait. Ensure the head and feet are fully within the frame before segmentation. Angle: Straight eye-level view, perpendicular to the subject. Framing Elements: Four overlapping, white browser windows/tabs. The pose is elegant and fluid. The bottom interface elements (e.g., 'Private', 'Done') must be clean and visible. Focal Length: Standard portrait lens (approx. 50mm equivalent) for realistic proportions. Camera Type: Simulated high-quality smartphone screen capture of a professional photo. Depth of Field: Shallow enough to focus sharply on the subject, allowi
```

[[Fashion Photography]] [[Studio Photography]] [[Volumetric Light]]

---

### 31. 生成韩流偶像风格图片

**Author**: [ROMI｜美容・女性向けLPデザイナー](https://x.com/hiro___design)  **Date**: 2026-01-23  **Language**: ja

> 一位用户使用 Nano Banana 为 Instagram 快拍制作了一张图片，特别要求角色摆出韩国偶像的姿势和造型。

![生成韩流偶像风格图片](https://cms-assets.youmind.com/media/1769236039917_vdekhz_G_Vj36naoAARwpY.jpg)

```
プロンプトには韓国アイドルみたいにしてって笑
```

[[Fashion Photography]]

---

### 32. 现代家居中的暗示性室内肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个高度详细的提示，用于生成一张逼真的、具有暗示性的室内肖像，描绘一位年轻女性在一个现代、明亮的家居环境中俏皮地蹲着。该提示详细说明了低角度全身视角、黑色高开叉服装（露脐上衣、短裤、透明连裤袜、厚底高跟鞋）以及干净、极简主义的背景（白色橱柜、木地板），强调动态姿势和高对比度。

![现代家居中的暗示性室内肖像](https://cms-assets.youmind.com/media/1769235969975_a84eub_G_UOr5ZbkAAF27Z.jpg)
![现代家居中的暗示性室内肖像](https://cms-assets.youmind.com/media/1769235970031_cx1due_G_UOr1jagAAULPX.jpg)
![现代家居中的暗示性室内肖像](https://cms-assets.youmind.com/media/1769235970249_c13o4s_G_UOr8QbAAIwSvl.jpg)

```
{
  "prompt_type": "photorealistic suggestive indoor portrait",
  "main_composition": "low-angle full-body view of a single young woman squatting playfully in a modern bright home interior, knees bent wide apart with hands resting on thighs, teasing confident expression looking directly at camera with subtle pout and raised eyebrows, dynamic pose emphasizing curves and legs, bright natural indoor lighting with clean white cabinets and wooden floor in background",
  "subject": {
    "description": "beautiful young woman in her early 20s, attractive feminine features with light natural makeup (defined dark eyeliner, long lashes, subtle contour, glossy nude lips), large expressive eyes, fair smooth skin with healthy glow, long loose wavy blonde hair with natural volume falling over shoulders and slight tousle",
    "clothing": "fitted black long-sleeve mock-neck crop top or bodysuit with subtle stretch fabric ending at waist, paired with very short black high-cut shorts riding high on hips, sheer black pantyhose or tights with subtle opacity, completed with chunky black platform high-heeled shoes or loafers with thick soles",
    "details": "playful teasing expression with direct eye contact and faint pout, hair naturally wavy with soft strands framing face, manicured neutral nails visible on hands, confident relaxed pose with knees wide and slight forward lean creating dramatic leg emphasis"
  },
  "environment": {
    "foreground": "light wooden or laminate floor with subtle reflections",
    "midground": "woman centered in open space",
    "background": "modern bright home interior with white built-in cabinets or shelves containing books and decor, clean minimalist design with no clutter, subtle hallway or adjacent room visible"
  },
  "lighting_and_atmosphere": "bright even indoor daylight (likely from off-frame window) creating soft natural glow with warm highlights on skin, hair, black fabric sheen, and sheer pantyhose translucency, gentle shadows enhancing pose depth and curves, playful intimate casual vibe with high contrast between black outfit and light surroundings, photorealistic detail evoking teasing confidence",
  "technical_quality": "highly detailed, sharp focus on subject with realistic fabric textures (stretch crop top matte, sheer pantyhose subtle pattern, platform shoe shine), hair movement, skin glow, and subtle makeup details, 8k resolution, professional candid selfie or portrait photography style with natural depth of field softly blurring distant cabinets",
  "negative_prompt_suggestions": "blurry, deformed, extra limbs, harsh shadows, overexposed floor reflections, underexposed outfit details, low quality, cartoon, anime, text watermark except optional '{argument name="watermark text" default="Did you notice? 👀"}', extra people, cluttered background, unnatural proportions"
}
```

[[Fashion Photography]] [[Low Angle Shot]] [[High Contrast Photography]] [[Dynamic Pose]]

---

### 33. 诱人的郊区别墅天鹅绒连衣裙肖像提示

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-21  **Language**: en

> 一个结构化的提示，用于生成一张电影般专业时尚的照片：一名穿着黑色丝绒迷你连衣裙、后背系带的性感女子，白天站在郊区车道上。该提示强调浓妆、逼真的面料光泽，并加入一支点燃的香烟，营造出一种忧郁而迷人的氛围。

![诱人的郊区别墅天鹅绒连衣裙肖像提示](https://cms-assets.youmind.com/media/1769063205015_ymu9f2_G_MH_YOWoAAzDWG.jpg)

```
{
  "subject": {
    "type": "human",
    "age": "early 20s",
    "gender": "female",
    "ethnicity": "western",
    "expression": "seductive and confident",
    "hair": {
      "color": "blonde",
      "length": "long",
      "style": "straight",
      "bangs": "full straight bangs framing face"
    },
    "makeup": {
      "eyeliner": "heavy dark",
      "eyeshadow": "smoky",
      "lipstick": "bold red"
    },
    "skin": "flawless"
  },
  "props": {
    "cigarette": {
      "status": "lit",
      "smoke": "gently curling upward"
    },
    "jewelry": {
      "necklace": "black choker with small beads/chain details",
      "ring": "silver ring on finger"
    },
    "nails": "black polish"
  },
  "clothing": {
    "dress": {
      "color": "black",
      "material": "velvet",
      "style": "mini, tight, bodycon fit",
      "straps": "thin spaghetti",
      "back": "lace-up corset-style with ribbons",
      "length": "above mid-thigh"
    }
  },
  "pose": {
    "angle": "three-quarter",
    "orientation": "standing sideways",
    "hip": "slightly cocked",
    "hand": "one resting on hip"
  },
  "background": {
    "location": "outdoor suburban driveway",
    "time": "daytime",
    "lighting": "natural sunlight, soft shadows",
    "scene_elements": ["residential house", "lawn"]
  },
  "visual_style": {
    "photography_style": "cinematic, professional fashion",
    "resolution": "8k",
    "details": {
      "skin_texture": "highly detailed",
      "fabric_sheen": "velvet realistic",
      "smoke": "realistic"
    },
    "atmosphere": "moody yet glamorous",
    "focus": "sharp"
  },
  "face_reference": {
    "use_same_face": true,
    "preserve_facial_features": true
  }
}
```

[[Fashion Photography]] [[Cigarette Prop]]

---

### 34. T 恤文字定制提示

**Author**: [Gen](https://x.com/Gen15191)  **Date**: 2026-01-21  **Language**: ja

> Nano Banana Pro 用户只需简单操作，即可复制提示词，然后更改生成图像中服装上显示的文本。这表明该提示词很可能是一个图生图或人物固定提示词。

![T 恤文字定制提示](https://cms-assets.youmind.com/media/1769063244771_7q64we_G_LYtFBbkAAepAr.jpg)

```
1.プロンプトをコピーして貼り付け 
2.服の文字を変更 完了！
```

[[Fashion Photography]] [[Image-To-Image]]

---

### 35. 身穿黑色服装的金发女性的三种变体

**Author**: [Isha 🪡](https://x.com/Isha8x)  **Date**: 2026-01-20  **Language**: en

> 一组三个不同的图像生成提示，旨在创建一位金发碧眼、身穿黑衣的年轻女性的不同版本，在保持主体核心外观的同时，将场景和风格在阳光明媚的花园、黄金时段的城市屋顶和专业影棚拍摄之间进行戏剧性转换。

![身穿黑色服装的金发女性的三种变体](https://cms-assets.youmind.com/media/1768977333629_uw0roo_G_GfnrzWYAAUOLj.jpg)

```
{
"action": "image_generation",
"action_input": "{ "prompt": "A high-quality, realistic full-body shot of a young woman with blonde hair and blue eyes, wearing a stylish black outfit. She is standing in a lush, sunlit garden surrounded by vibrant flowers and greenery. The lighting is soft and natural, creating a warm and inviting atmosphere. The composition is artistic and well-balanced, focusing on her serene expression and the beautiful outdoor setting." }",
"thought": "The user wants to generate different images based on the provided photos. I will create a prompt that captures the essence of the woman's appearance (blonde hair, blue eyes) and her style (black clothing) but places her in a completely new, high-quality setting like a sunlit garden to provide a 'different' image as requested."
}
{
"action": "image_generation",
"action_input": "{ "prompt": "A cinematic, high-resolution portrait of a young woman with blonde hair and striking blue eyes. She is wearing an elegant black evening dress and is posed in a modern, minimalist urban rooftop setting during the golden hour. The city skyline is visible in the background with soft bokeh. The lighting is dramatic and warm, highlighting her features and the texture of the dress." }",
"thought": "For the second variation, I'll change the environment to a modern urban rooftop at sunset. This maintains the character's core look but offers a different mood and background compared to the original indoor and hayfield settings."
}
{
"action": "image_generation",
"action_input": "{ "prompt": "A professional studio photography shot of a young woman with blonde hair tied in a bun and blue eyes. She is wearing a sleek, black athletic zip-up top. The background is a clean, neutral grey. The lighting is sharp and professional, emphasizing the contours of her face and the fit of the clothing. High detail, 8k resolution." }",
"thought": "For the third image, I will focus on a studio setting that mirrors the 'selfie' style of the first image but elevates it to a professional photography level. This provides a clean, focused alternative while staying true to the visual elements found in the source images."
}
```

[[Fashion Photography]] [[Style Transfer]]

---

### 36. 电影级 AI 摄影关键词列表

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-01-15  **Language**: en

> 以下是一系列关键词和短语，旨在引导 AI 图像生成器创作出高质量、超现实、电影级的时尚摄影和肖像作品，同时模拟专业相机和镜头的效果。

![电影级 AI 摄影关键词列表](https://cms-assets.youmind.com/media/1768544863304_3jaog4_G-rUXx5boAEjutH.jpg)

```
AI cinematic photography, nano banana pro 4k, higgsfield ai, ai fashion photography, cinematic portrait ai, outdoor editorial photoshoot, film look ai images, realistic ai photography, cinema lens simulation, ai camera rendering, fashion ai visuals, hyper realistic ai portraits, creative ai photography, ai image generation tools, professional ai photos
```

[[Fashion Photography]] [[AI Prompt Engineering]]

---

### 37. 编辑肖像联系表美学

**Author**: [Keskin](https://x.com/craftian_keskin)  **Date**: 2026-01-14  **Language**: en

> 这是一个详细的图像生成提示，旨在创建一张年轻女性的超现实、编辑风格肖像，以四格胶片密纹片的形式呈现。它详细说明了拍摄对象的容貌、服装、多样的姿势和表情，强调了带有可见胶片颗粒和柔和直射光线的复古模拟摄影美学。

![编辑肖像联系表美学](https://cms-assets.youmind.com/media/1768468549796_yyhsvi_G-oRD_XXQAAW0bL.jpg)

```
A photorealistic editorial-style portrait composed as a four-frame grid, resembling a contact sheet from a film photoshoot. Each frame features the same young woman posing against a neutral gray studio wall, captured in slightly different natural poses and expressions.
She has voluminous dark hair styled loose with soft movement, strong brows, defined cheekbones, and natural glam makeup emphasizing her eyes and lips. She is wearing a fitted white tank top with a deep neckline, cropped just above the waist, revealing subtle midriff in some frames.
Across the frames, her poses vary: one with a hand lightly gripping the fabric near her chest, another standing straight with relaxed shoulders, another with arms raised above her head, and one adjusting the hem of the top. Her expressions range from calm and confident to softly introspective.
The lighting is soft but direct, similar to on-camera flash, creating gentle highlights on skin and fabric while preserving natural texture. The image includes visible film grain, dust, and minor imperfections, enhancing a vintage analog photography aesthetic. The overall mood is confident, sensual in a restrained editorial way, and timeless.

Style & Quality Cues
Photorealistic, fashion editorial photography, film contact sheet aesthetic, subtle grain, natural skin texture, high detail, minimal retouching

Lighting
Soft direct flash, even illumination, low ambient shadows, realistic contrast

Camera
Medium portrait framing, eye-level angle, shallow depth of field, 35mm film look

Negative Prompt
 exaggerated anatomy, glossy commercial lighting, heavy retouching, plastic skin, cartoon or illustration style, AI artifacts, distortion
```

[[Fashion Photography]] [[Multiple Poses]]

---

### 38. 高级时尚超跑展厅肖像

**Author**: [Javeriya ✨](https://x.com/JadoonKhan281)  **Date**: 2026-01-14  **Language**: en

> 一个 JSON 提示，用于生成一张高定时尚的超写实图像：一位身材苗条的金发女子，身穿透明金色网眼迷你连衣裙，在豪华展厅内，一辆带有金色装饰的白色超级跑车前优雅地摆姿势。该提示详细说明了高端时尚摄影典型的美学、光线和构图。

![高级时尚超跑展厅肖像](https://cms-assets.youmind.com/media/1768468561966_l0xrt7_G-lyb84bEAAd_kD.jpg)
![高级时尚超跑展厅肖像](https://cms-assets.youmind.com/media/1768468562138_3agjki_G-lyb-RaQAAjJJs.jpg)

```
{
  "image_description": {
    "subject": {
      "person": "A slender blonde woman with long hair, wearing a sheer, shimmering {argument name="dress color" default="gold"} mesh mini dress with thin spaghetti straps and a vertical gold zipper detail.",
      "accessories": "Layered gold necklaces, gold bracelets, and metallic gold high-heeled sandals.",
      "pose": "Standing elegantly in front of a luxury car, legs crossed at the ankles, looking directly at the camera."
    },
    "vehicle": {
      "type": "A sleek, modern {argument name="car color" default="white"} supercar with gold accents.",
      "details": "High-gloss white paint, metallic gold rims, gold trim around the windows, and low-profile body styling."
    },
    "environment": {
      "location": "A bright, high-end luxury car showroom.",
      "lighting": "Clean, architectural indoor lighting with soft reflections on the polished white floor.",
      "background": "Large floor-to-ceiling glass windows showing other vehicles in a blurred outdoor setting."
    },
    "technical_style": {
      "composition": "Full-body shot, eye-level angle, centered subject.",
      "aesthetic": "High-fashion photography, photorealistic, sharp focus on the subject with a shallow depth of field (bokeh) in the background.",
      "color_palette": "Dominant white and gold, with neutral grey and black architectural tones."
    }
  }
}
```

[[Fashion Photography]] [[Blonde Model]]

---

### 39. 电影感黑白机车手肖像

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-01-13  **Language**: en

> 生成一张电影风格、高对比度的黑白肖像照的提示词，画面中一位英俊的年轻男士身穿皮质机车夹克，戴着墨镜，站在开阔的田野中，回头望向镜头，强调强烈的景深和时尚摄影风格。

![电影感黑白机车手肖像](https://cms-assets.youmind.com/media/1768466975451_il8pos_G-iAe2ga4AAVzbA.jpg)

```
A cinematic black and white portrait of a handsome young man standing in an open field. He is wearing a classic leather biker jacket and dark Wayfarer-style sunglasses. He has a styled pompadour haircut and light stubble. The man is turned away from the camera, looking back over his left shoulder directly at the viewer. The background consists of a blurred field of tall grass and distant trees, creating a strong depth of field (bokeh) effect. The lighting is soft and natural, emphasizing the texture of the leather and the contours of his face. High-contrast fashion photography style.
```

[[Fashion Photography]] [[High Contrast Portrait]]

---

### 40. 3x3 Black and White Photo Collage

**Author**: [Favori](https://x.com/yuanguand)  **Date**: 2026-01-13  **Language**: en

> A prompt designed to create a 3x3 grid photo collage in a high-contrast black and white aesthetic, reminiscent of classic photographers like Irving Penn or Avedon. It mandates strict face preservation across all nine frames while varying the pose and expression dramatically.

![3x3 Black and White Photo Collage](https://cms-assets.youmind.com/media/1768466905224_a0xyqr_G-hXc0UbYAAWMG-.jpg)

```
{
  "Objective": "Create a 3x3 grid photo collage with high contrast black and white aesthetics",
  "FaceReference": {"Mode": "Strict face preservation", "Instruction": "Use uploaded reference for exact facial features", "Consistency": "Face identical across all nine frames"},
  "GridComposition": {"Layout": "3x3 grid", "PoseVariety": ["Intense direct stare", "Silhouette backlit", "Hands covering face peek", "Profile strong jaw", "Full body power stance", "Eyes only close-up", "Motion blur", "Contemplative downward", "Laughing candid"]},
  "PersonaDetails": {"Subject": {"Type": "Same as reference", "Wardrobe": "{argument name="wardrobe item" default="Simple black turtleneck"}", "OverallPresence": "Timeless, artistic"}},
  "Environment": {"Setting": "Minimal studio", "Background": "Grey gradient or geometric", "Lighting": {"Style": "Dramatic directional", "Quality": "Hard shadows, extreme contrast"}},
  "ImageQuality": {"Resolution": "8K black and white", "Details": "Fine art grain", "Aesthetic": "Irving Penn/Avedon portrait"},
  "NegativePrompt": ["color", "flat lighting", "different face", "altered facial features"],
  "ResponseFormat": {"Layout": "3x3 grid", "AspectRatio": "1:1"}
}
```

[[Fashion Photography]] [[3x3 Grid Layout]]

---

### 41. 南非海岸悬崖上的黄金时段人像

**Author**: [Aylin](https://x.com/kashmir_ki_lark)  **Date**: 2026-01-12  **Language**: en

> 一个用于生成超逼真电影级肖像的提示：一名女子在南非的黄金时段，于戏剧性的海岸悬崖上摆姿势。提示详细描述了她的着装（石灰绿色绞花针织毛衣和牛仔裤）、玳瑁太阳镜，并强调了自然的皮肤纹理、飘逸的头发，以及 8K 时尚杂志风格的高动态范围。

![南非海岸悬崖上的黄金时段人像](https://cms-assets.youmind.com/media/1768319092338_s5t56s_G-eXsnyasAAx1fu.jpg)

```
ultra-photorealistic cinematic portrait of a stunning young woman posing playfully on a dramatic coastal cliff in South Africa. Long, silky blonde hair flowing naturally in the ocean breeze, individual strands softly backlit. Warm, genuine smile with a highly realistic, detailed face, natural skin texture, subtle freckles, balanced facial proportions, natural makeup. Brown tortoiseshell sunglasses with glossy frames and realistic reflections.
Wearing an oversized light lime-green cable-knit cropped sweater with clearly defined knit patterns, rich fabric texture, natural folds, relaxed fit; paired with high-waisted light blue denim jeans with fine stitching and realistic denim grain.
Expansive cinematic environment: lush green rolling hills, rugged rocky cliffs, vast deep-blue ocean stretching to the horizon, white waves crashing along the coastline. Golden hour sunlight, warm highlights, soft shadows, glowing rim light around hair, subtle sky gradient. Cinematic composition, shallow depth of field, creamy background bokeh, ultra-sharp focus on subject, high dynamic range, vibrant yet natural color grading, fashion editorial photography style, natural beauty, hyper-realistic detail, 8K quality.
```

[[Fashion Photography]] [[Golden Hour Lighting]]

---

### 42. 时尚试衣间自拍提示

**Author**: [Aylin](https://x.com/kashmir_ki_lark)  **Date**: 2026-01-09  **Language**: en

> 一个详细的提示，用于生成一张逼真的时尚摄影图片：一名年轻女子坐在一间现代试衣间里，身穿黑色不对称露脐上衣和褪色牛仔裤，表情诱惑，画面焦点锐利。

![时尚试衣间自拍提示](https://cms-assets.youmind.com/media/1768143653597_ggzfq1_G-M3urNXUAE-Kh5.jpg)

```
"A beautiful young woman with fair skin, long straight light brown hair with subtle highlights, blue-green eyes, full lips, and a subtle seductive expression, sitting on the floor in a modern clothing store fitting room or showroom. She is wearing a fitted black long-sleeve ribbed crop top with an asymmetric off-shoulder design, high choker neckline, and a long thin strap that she is holding loosely in one hand. Paired with high-waisted faded gray skinny jeans that hug her figure. Pose is relaxed yet confident: one knee up, the other leg extended, slight lean forward, gazing directly at the camera. Background shows racks of hanging clothes in neutral tones like beige, black, and brown, soft indoor lighting, clean minimalist store interior, highly detailed, photorealistic, sharp focus, fashion photography style, masterpiece, best quality, ultra realistic, 8k --ar 9:16 --stylize 250 --v 6 --q 2 --style raw"
```

[[Fashion Photography]] [[Sharp Focus]]

---

### 43. 时尚摄影组合提示（工作流程步骤）

**Author**: [Rez Karim](https://x.com/rezkhere)  **Date**: 2026-01-07  **Language**: en

> 这是一个工作流程的分步说明，其中提示词只是将多个产品图片组合成一张时尚摄影图片的指令。

```
Now, copy and paste all the product images. As input, connect all the images to the output node. Then give a prompt to combine these into a fashion photoshoot image.
```

[[Fashion Photography]]

---

### 44. 身着工装裤的时尚人士置身于空灵的风景中

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-01-01  **Language**: en

> 生成一张高清照片的提示词：一位时尚的年轻人，戴着太阳镜，身穿深色衬衫和蓝色工装裤，自信地走着。背景是迷雾缭绕、空灵的风景，色调柔和的青色中隐约可见数字“2026”。

![身着工装裤的时尚人士置身于空灵的风景中](https://cms-assets.youmind.com/media/1767456281483_kfsn8t_G9jblOXa0AAvZNn.jpg)

```
{
  "HD photo of a stylish beautiful young person wearing {argument name="Accessory" default="sunglasses"}, a solid black or dark charcoal shirt (replacing the white and blue batan shirt for better contrast), paired with {argument name="Pants Type" default="blue cargo pants"}, and carrying a black backpack in the left hand while walking confidently across a soft blurred foreground. Background is a misty ethereal landscape with muted teal,

2026 in the background
```

[[Fashion Photography]] [[Typography Overlay]]

---

### 45. 超现实童年卡通时尚大片

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-30  **Language**: en

> 一个复杂的多部分 JSON 提示，专为超现实图像生成而设计，重点是时尚摄影，其中人物与汤姆和杰瑞、皮卡丘、Ben 10 和粉红豹等经典卡通人物的巨大 3D 写实渲染图摆拍。

![超现实童年卡通时尚大片](https://cms-assets.youmind.com/media/1767454987323_gv2gbk_G9Z_Lc3bEAArkpH.jpg)

```
[
  {
    "image_generation": {
      "quality": "hyper-realistic",
      "face": { "preserve_original": true },
      "subject": {
        "clothing": "light grey knitted sweater, blue high-waisted jeans, white high-top sneakers",
        "pose": "standing with arm around giant 3D Tom; Jerry on Tom's shoulder",
        "expression": "fun, mischievous",
        "character_element": {
          "name": "Tom & Jerry",
          "type": "3D photorealistic duo",
          "interaction": "Tom posing confidently, Jerry playfully"
        }
      },
      "environment": "clean grey-blue backdrop"
    }
  },
  {
    "image_generation": {
      "quality": "hyper-realistic",
      "face": { "preserve_original": true },
      "subject": {
        "clothing": "electric yellow knitted sweater, black high-waisted jeans, white/black high-top sneakers",
        "pose": "arm resting on giant 3D Pikachu",
        "expression": "energetic, cheerful",
        "character_element": {
          "name": "Pikachu",
          "type": "giant 3D photorealistic render",
          "interaction": "smiling up at person"
        }
      },
      "environment": "vibrant yellow backdrop"
    }
  },
  {
    "image_generation": {
      "quality": "hyper-realistic, professional fashion photoshoot",
      "face": { "preserve_original": true },
      "subject": {
        "clothing": "Ben 10 themed green/black sweater, dark grey jeans, white/green sneakers",
        "pose": "standing beside giant 3D Ben 10 activating Omnitrix",
        "expression": "confident, energetic",
        "character_element": {
          "name": "Ben Tennyson (Classic Ben 10)",
          "type": "giant 3D photorealistic render with cartoon accuracy",
          "details": "accurate green jacket outfit, glowing green Omnitrix on wrist",
          "interaction": "Ben activates Omnitrix with dynamic green glow"
        }
      },
      "environment": {
        "background": "neon-green and black circuitry patterns",
        "lighting": "dynamic green glow reflecting from Omnitrix",
        "mood": "sci-fi hero fashion shoot"
      }
    }
  },
  {
    "image_generation": {
      "quality": "hyper-realistic",
      "face": { "preserve_original": true },
      "subject": {
        "clothing": "pastel pink knitted sweater, white high-waisted jeans, white/pink sneakers",
        "pose": "posing fashionably beside tall 3D Pink Panther",
        "expression": "elegant, stylish",
        "character_element": {
          "name": "Pink Panther",
          "type": "giant 3D render",
          "interaction": "striking a suave pose"
        }
      },
      "environment": "light pastel pink backdrop"
    }
  }
]
```

[[Fashion Photography]]

---

### 46. 编辑部自助洗衣店肖像提示

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2025-12-29  **Language**: en

> 一个详细的 JSON 提示，描述了在城市自助洗衣店中创作一组编辑类生活方式肖像照。该提示详细说明了拍摄对象的形象、服装（高领毛衣和灯芯绒长裤）、环境细节（工业洗衣机），以及照明（顶置荧光灯）和色彩分级（暖色调）等技术规格。

![编辑部自助洗衣店肖像提示](https://cms-assets.youmind.com/media/1767166906600_pr3sw4_G9UB39ma4AAIPlO.jpg)

```
{
"image_type": "photograph",
"genre": "editorial lifestyle portrait",
"composition": {
"framing": "medium-full shot",
"orientation": "vertical",
"subject_position": "centered",
"pose": "standing with arms extended outward, hands resting on washing machines",
"camera_height": "eye-level",
"perspective": "straight-on",
"depth_of_field": "shallow to moderate, subject sharp with softly blurred background"
},
"subject": {
"count": 1,
"appearance": {
"gender_presentation": "female-presenting",
"age_range": "young adult",
"skin_tone": "light",
"expression": "neutral to subtly confident",
"gaze": "directly at camera",
"hair": {
"color": "light brown",
"length": "long",
"style": "loose, slightly tousled, natural texture",
"parting": "off-center"
}
},
"clothing": {
"top": {
"type": "long-sleeve fitted turtleneck",
"color": "dark charcoal or black",
"texture": "smooth knit"
},
"bottom": {
"type": "high-waisted trousers",
"color": "rust brown",
"material": "corduroy",
"fit": "relaxed with pleats"
}
},
"accessories": "none visible"
},
"environment": {
"location_type": "laundromat",
"setting_style": "urban, utilitarian",
"background_elements": [
"industrial washing machines",
"metal ducts and pipes",
"fluorescent ceiling lights",
"signage with laundry-related text"
],
"surface_materials": [
"stainless steel",
"painted metal",
"plastic"
]
},
"lighting": {
"type": "ambient artificial",
"source": "overhead fluorescent lights",
"quality": "soft but slightly flat",
"direction": "top-down with mild frontal fill",
"contrast": "moderate",
"shadows": "soft, minimal harsh shadowing"
},
"color_palette": {
"dominant_colors": [
"warm brown",
"rust",
"charcoal",
"muted beige"
],
"accent_colors": [
"silver",
"off-white",
"faded green"
],
"temperature": "warm-leaning despite industrial setting",
"saturation": "moderate, slightly desaturated"
},
"technical_details": {
"camera_style": "DSLR or mirrorless",
"lens_characteristics": "standard to short telephoto",
"aperture_estimate": "f/2.8–f/4",
"iso_estimate": "400–800",
"shutter_speed_estimate": "1/125–1/250",
"focus": "sharp on subject face and torso"
},
"artistic_style": {
"mood": "casual, confident, contemporary",
"aesthetic": "modern editorial with vintage undertones",
"influences": [
"fashion editorial",
"urban lifestyle photography"
]
},
"background_treatment": {
"clarity": "slightly softened",
"distractions": "minimal, structured repetition of machines",
"depth_cues": "linear perspective from machines and ceiling fixtures"
},
"post_processing": {
"color_grading": "warm tones emphasized",
"contrast_adjustment": "slightly lifted blacks",
"sharpness": "moderate, natural",
"grain": "minimal to none"
},
"text_elements": {
"presence": true,
"style": "industrial signage",
"legibility": "partially legible, not focal"
}
}
```

[[Fashion Photography]] [[Fluorescent Lighting]] [[Warm Color Grading]]

---

### 47. 摩纳哥奢华旅行生活方式肖像

**Author**: [Abbay](https://x.com/LearnWithAbbay)  **Date**: 2025-12-27  **Language**: en

> 一个用于生成摩纳哥年轻女性奢华旅行生活方式照片的结构化提示。该提示详细描述了拍摄对象的形象、时尚的服装（米色露肩上衣、白色长裤）、姿势以及特定场景（俯瞰赌场广场附近摩纳哥赛道的露台）。它还包括用于品牌宣传的排版元素，并指定了柔和、漫射的自然日光。

![摩纳哥奢华旅行生活方式肖像](https://cms-assets.youmind.com/media/1766987728951_6otc00_G8lx4PDbcAAGA3_.jpg)

```
{
  "subject": {
    "person": "Young woman, early 20s, Caucasian",
    "hair": "Golden blonde hair with loose curls and subtle flyaways",
    "pose": "Seated on ledge, legs crossed at ankles, shoulders relaxed",
    "expression": "Gentle, composed, understated smile"
  },
  "outfit": {
    "top": "{argument name=\"top style\" default=\"Cream off-shoulder fitted top\"}",
    "bottoms": "High-waisted white trousers",
    "accessories": "Mini handbag, pearl studs, thin chain necklace"
  },
  "action": {
    "hands": "Hands resting loosely on knees"
  },
  "location": {
    "setting": "Terrace overlooking Monaco circuit near Casino Square",
    "background": "Luxury hotels, racetrack walls, cloudy sky"
  },
  "typography": {
    "text": "{argument name=\"branding text\" default=\"MONTE-CARLO, UBS branding\"}"
  },
  "lighting": {
    "type": "Natural ambient daylight",
    "quality": "Soft, evenly diffused"
  },
  "composition": {
    "style": "Luxury travel lifestyle photograph, medium portrait, 4:5",
    "color_palette": "Warm creams and muted greys"
  }
}
```

[[Fashion Photography]] [[Travel Lifestyle Photography]]

---

### 48. 电商产品列表：刺绣细条纹西装外套

**Author**: [Amanpreet Singh](https://x.com/amanxdesign)  **Date**: 2025-12-27  **Language**: en

> 一个专门为电商产品列表量身定制的提示词，重点是生成一张模特穿着高度精细、刺绣深色细条纹西装外套的全身图像。该提示词确保精确复制参考图像中的刺绣图案，并将场景设定在一个优雅、柔和照明的现代客厅中，优先考虑纹理和准确的色彩表现。

![电商产品列表：刺绣细条纹西装外套](https://cms-assets.youmind.com/media/1766987643356_u7ygkf_G87uQzFagAAXVtM.jpg)
![电商产品列表：刺绣细条纹西装外套](https://cms-assets.youmind.com/media/1766987645161_v4gbyg_G87uQzQawAAZwNe.jpg)

```
{
  "description": "Full-body image of an American woman wearing the exact same embroidered dark pinstripe blazer as in the reference image. The blazer must have the same embroidery patterns — including the red heart, colorful eye, pink text, yellow lightning bolt, and multi-colored patch details — all placed identically on the front panels and sleeves. The blazer should have a slightly oversized fit, sharp lapels, front pockets, and a single-button closure. The model wears a simple black top and short skirt underneath, maintaining the same styling. She has a confident, welcoming expression with a soft smile, exuding creativity and personality. She can stand casually with one hand holding a small handbag or resting by her side.",
  
  "style": "Chic indoor lifestyle aesthetic. The scene is set in a modern living room with soft, cozy decor — neutral tones, a stylish sofa, coffee table, indoor plant, and subtle art on the wall. The overall vibe is elegant yet contemporary, matching the artistic flair of the blazer.",
  
  "lighting": "Soft warm indoor lighting (between 3300K–3800K). Use diffused artificial light from lamps or ceiling fixtures to highlight the blazer texture and embroidery details. Avoid sunlight, window glare, or natural daylight. Lighting should evenly illuminate the model and outfit with soft shadows for realism.",
  
  "camera": "Full-body, vertical orientation at eye level. The model should be clearly visible from head to toe, standing naturally on the floor with balanced framing and slight space above the head. The photo should feel authentic, as if part of a lifestyle shoot inside a designer’s apartment.",
  
  "focus": "Crisp focus on the outfit’s embroidery, textures, and fabric weave. Maintain natural skin tones and accurate color representation of the blazer. The background can have a slight depth blur to keep the focus on the model and her outfit.",
  
  "environment": "Warm, cozy living room with beige or neutral tones, wooden flooring, soft furnishings, and minimalistic modern furniture. Decor accents like a lamp, indoor plant, or abstract painting can enhance the realism and elegance of the setting.",
  
  "negative_prompt": [
    "sunlight or daylight",
    "studio backdrop",
    "cropped frame",
    "different embroidery placement",
    "flat or smooth fabric",
    "cold lighting",
    "harsh shadows",
    "stylized or AI-art look"
  ]
}
```

[[Fashion Photography]]

---

### 49. 逼真时尚图像的负面提示

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2025-12-24  **Language**: en

> 这是与主提示词一起使用的负面提示词，旨在确保生成的图像避免常见的伪影和低质量元素，专注于实现干净、逼真且专业的时尚美学。

![逼真时尚图像的负面提示](https://cms-assets.youmind.com/media/1766935958145_eu93jx_G86Vi29aAAAiAjO.jpg)

```
low quality, bad quality, sketches, painting, artwork, illustration, cartoon, anime, bad anatomy, bad hands, missing fingers, extra fingers, cropping, blurry, out of frame, distortion, deformity, ugly, watermark, text, signature
```

[[Fashion Photography]] [[Negative Prompt]]

---

### 50. 金属红色亮片西装时尚照片

**Author**: [毎日の活力⚡](https://x.com/_dailyboost)  **Date**: 2025-12-20  **Language**: en

> 一个高分辨率的时尚摄影提示，要求 AI 为上传的参考图片中的女性穿上闪闪发光的金属红色亮片三件套西装（超大款西装外套、打结抹胸、宽松长裤），强调腰部，并使用特定的 Canon 相机和镜头设置。

![金属红色亮片西装时尚照片](https://cms-assets.youmind.com/media/1766385944478_6sal3g_G8nDk-IbkAA9TZs.jpg)

```
A high-resolution studio fashion photograph taken with a Canon EOS R5 and an RF 85mm f/1.2L USM lens captures the woman from the image wearing a shimmering metallic {argument name="suit color" default="red"} sequined three-piece suit. The outfit consists of an oversized blazer, a knotted bandeau bra top,which reveals her midriff and navel and loose-fitting trousers with her hands in the pockets. Her long, wavy black hair falls over her shoulders, and she wears a delicate double-layered silver necklace.
```

[[Fashion Photography]]

---

### 51. 电影级黑白高定肖像

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2025-12-14  **Language**: en

> 这是一个为 Nano banana Pro 设计的提示，旨在生成一张电影风格的黑白肖像，描绘一位年轻女性侧身行走。它指定了强烈的侧光以营造高对比度和深阴影，详细的服装（宽松的黑色 T 恤、修身牛仔裤、海军部队手表），以及现代混凝土背景，目标是呈现一种优雅、极简、高级时装摄影的风格。

![电影级黑白高定肖像](https://cms-assets.youmind.com/media/1765991325046_0a51xi_G8HdKcAboAEWGLc.jpg)

```
A cinematic black-and-white portrait of a young woman (the attached person reference, 100% exact facial features and 100% exact hairstyle) walking in profile view. Side lighting casts strong contrast and deep shadows across her face and body. She is wearing a loose black T-shirt paired with fitted jeans, accessorized with a black Navy Force watch on her right wrist. Her stride is confident, with her hair slightly moving in the air. She weighs {argument name="weight" default="75 kg"} and is {argument name="height" default="170 cm"} tall. The background features a modern concrete wall with vertical texture, creating a moody and artistic atmosphere. Lighting is soft yet directional from the left side, emphasizing realistic texture and depth. The composition is elegant and minimalist, in a professional high-fashion photography style.
```

[[Fashion Photography]] [[High Contrast]] [[Minimalist Aesthetic]] [[Monochrome Photography]]

---

### 52. 船上户外生活方式照片

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2025-12-14  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张逼真的户外生活方式肖像照：一名身穿黄色比基尼的女性，坐在船尾，重点突出自然光线和自信、放松的情绪。

![船上户外生活方式照片](https://cms-assets.youmind.com/media/1765991242256_7ibm1r_G8HaMdtacAAS_xC.jpg)

```
{
  "scene_type": "outdoor lifestyle photo on water",
  "camera": {
    "device": "smartphone or mirrorless camera",
    "angle": "slightly low, rear three-quarter angle",
    "framing": "full upper body with emphasis on seated pose",
    "orientation": "portrait",
    "aspect_ratio": "3:4",
    "focus": "sharp subject with clear background"
  },
  "subject": {
    "gender": "female",
    "age_range": "young adult",
    "skin_tone": "light to lightly tanned",
    "body_type": "curvy, athletic",
    "posture": {
      "body_position": "sitting on the back edge of a boat seat",
      "torso": "upright with slight twist toward camera",
      "hips": "seated firmly, weight centered",
      "shoulders": "relaxed",
      "head": "turned over shoulder toward camera"
    },
    "expression": {
      "facial": "neutral to mildly confident",
      "eyes": "looking directly toward camera",
      "mouth": "relaxed lips",
      "emotion": "calm, confident, composed"
    },
    "hair": {
      "color": "light brown to blonde",
      "length": "medium to long",
      "texture": "straight",
      "style": "tied up in a messy bun",
      "loose_strands": "few strands framing face"
    },
    "face_details": {
      "makeup": "minimal or natural",
      "features": "defined brows, natural skin texture"
    },
    "upper_body": {
      "clothing": "yellow bikini top",
      "style": "string-tie back",
      "fit": "snug and supportive",
      "breast_size": "medium, proportionate to frame"
    },
    "lower_body": {
      "clothing": "matching yellow bikini bottoms",
      "style": "string-tie sides",
      "fit": "fitted, athletic cut"
    },
    "hands_and_arms": {
      "hand_position": {
        "action": "one hand resting on seat",
        "fingers": "relaxed, slightly bent"
      }
    },
    "feet": {
      "footwear": "barefoot",
      "toes": "naturally relaxed, light nail polish"
    }
  },
  "environment": {
    "location": "on a boat",
    "surface": "padded boat seat with light upholstery",
    "background": {
      "water": "calm lake or river",
      "shoreline": "green trees and shrubs",
      "sky": "clear blue with light clouds"
    }
  },
  "lighting": {
    "type": "natural daylight",
    "direction": "even sunlight",
    "quality": "bright and clear",
    "shadows": "soft, minimal"
  },
  "style": {
    "realism": "photorealistic",
    "aesthetic": "summer lifestyle photography",
    "mood": "relaxed, confident, outdoorsy"
  },
  "quality_tags": [
    "high detail",
    "natural lighting",
    "realistic skin texture",
    "clean composition",
    "no text",
    "no watermark",
    "no logo"
  ]
}
```

[[Fashion Photography]] [[Natural Light]] [[Outdoor Lifestyle]] [[Yellow Bikini]]

---

### 53. 碎玻璃肖像风格提示词

**Author**: [空想写真家](https://x.com/KusoPhoto)  **Date**: 2025-12-12  **Language**: ja

> 一个详细的提示，用于生成指定女性的电影特写肖像，通过破碎的镜子或碎玻璃观看，创造出超现实的万花筒效果。它指定了技术细节，例如使用 50mm 镜头、f/1.4 光圈以获得极致的焦外虚化、霓虹粉色/青色的反射，以及一种忧郁、未来主义、时尚驱动的美学。

![碎玻璃肖像风格提示词](https://cms-assets.youmind.com/media/1765991079596_f075aq_G79WkM3agAUQR9Q.jpg)
![碎玻璃肖像风格提示词](https://cms-assets.youmind.com/media/1765991080341_ur1cww_G79Wll4acAAfDiU.jpg)

```
指定の女性を、顔の前に置かれた断片的な鏡を通して捉えた、映画的なクローズアップポートレート。極端なボケ効果を得るため50mmレンズでf/1.4で撮影され、彼女の顔立ちは鏡の破片に多重化され歪み、シュールな万華鏡効果を生み出している。ただ片方の瞳だけが鮮明に焦点され、鋭い眼差しでレンズを直視している。ネオンピンクとティール色の光がガラスに反射し、現代的な美意識の輝きを添える。雰囲気は陰鬱でありながら未来的で、編集的な精神を帯び、光沢のあるハイライトと柔らかな映画的な影が特徴だ。微妙なデジタルグレインとカラーグレーディングが、夢幻的でありながらファッション主導の美学へと押し上げ、最先端のキャンペーンに完璧な仕上がりとなっている。
```

[[Fashion Photography]] [[50mm Lens]] [[Futuristic Aesthetic]]

---

### 54. 别致白色服装时尚大片提示

**Author**: [NanoInspire](https://x.com/NanoInspirate)  **Date**: 2025-12-12  **Language**: en

> 一个为 Google Gemini Nano Banana Pro 3.0 设计的详细图像生成提示，用于创作一张超现实的时尚摄影作品：一位年轻女性身穿白色短款背心和 A 字迷你裙，置身于一个明亮、现代的工作室中，光线柔和、漫射的自然光，旨在呈现出干净、精致、时尚的美学效果。

![别致白色服装时尚大片提示](https://cms-assets.youmind.com/media/1765990985945_m1trd6_G79Naw8XQAA0LkK.jpg)

```
{
  "prompt_description": {
    "subject": "A young woman, appearing to be in her late teens or early twenties, with a slender and athletic build.",
    "face": "A soft, slightly downturned gaze, with parted lips that create a subtle pout. Her eyebrows are perfectly sculpted, and her eyeliner is sharp and winged. Her skin appears smooth and flawless, with minimal visible texture. Subtle blush on her cheeks.",
    "hair": "Long, dark brown hair that falls in loose, soft waves past her shoulders. The hair has a natural shine and appears to be styled smoothly, with no flyaways. A few strands gently frame her face.",
    "clothing": "A two-piece outfit. The top is a white, form-fitting cropped tank top with thin spaghetti straps. The neckline is a flattering sweetheart shape. The fabric appears to have a slight stretch, with subtle tension around the bust. The skirt is a high-waisted, a-line mini skirt, also in white. It flares out from the waist in a structured yet fluid manner, with a clean hemline. The fabric of the skirt appears to be a heavier, slightly stiff material that holds its shape well, creating a smooth, almost sculptural silhouette. There is no visible tension or stretching at the waistband.",
    "accessories": "A delicate, thin bracelet on her left wrist, possibly silver or rose gold, with a small charm. Small, subtle stud earrings in her earlobes. A very faint, almost unnoticeable tattoo on her left forearm.",
    "environment": "An indoor setting that resembles a bright, modern studio or a minimalist living space. A large window with black mullions is visible in the background, draped with sheer, light-colored curtains. A sleek, white table is positioned in front of the window, with its legs slightly visible. On the table are two small potted green plants. Another framed artwork with a botanical illustration is on a shelf or surface behind the plants. The floor is light-colored wood.",
    "lighting": "Soft, diffused natural light streaming in from the window, creating gentle highlights on her skin and the fabric of her outfit. There are subtle specular highlights on her cheekbones and shoulders. The shadows are soft and have a slightly diffused quality, suggesting a large light source or an overcast day. The overall lighting is bright and airy.",
    "atmosphere": "Serene, chic, fashionable, and slightly alluring. The mood is clean and sophisticated, with a sense of youthful elegance."
  },
  "style": {
    "art_style": "Ultra-realistic commercial fashion photography, high-end editorial.",
    "color_grade": "Clean, bright, and slightly desaturated. Dominant tones are white, natural skin tones, and soft, muted greens and grays in the background. A very subtle coolness to the overall image.",
    "texture_quality": "Extremely sharp and detailed, with high micro-contrast. Every pore and fabric weave should be discernible. Photorealistic."
  },
  "camera_settings": {
    "camera": "Medium Format"
  }
}
```

[[Fashion Photography]] [[Soft Natural Light]] [[Studio Photography]] [[Minimalist Aesthetic]]

---

### 55. 电影时尚肖像提示

**Author**: [Anissa](https://x.com/SimplyAnnisa)  **Date**: 2025-12-12  **Language**: en

> 一个高度详细的提示，用于生成一张超逼真的 8K 电影级时尚肖像，描绘一位短黑发、穿着羊毛夹克的时尚女性，她站在一辆亮黑色汽车前，强调纹理、柔和的色彩和高端杂志社论的氛围。

![电影时尚肖像提示](https://cms-assets.youmind.com/media/1765990863621_zn6u37_G78TNuva8AApn9w.jpg)

```
A ultra-realistic 8K cinematic fashion portrait of a woman with short, soft-textured black hair, edgy and elegant. She wears a brown shearling jacket with black quilted details, a dark, slightly open-chested t-shirt, and loose-fitting black pants with earthy tones. Her forward-leaning pose with a focused gaze creates the impression of a high-end magazine editorial. Her long, dark brown hair, healthy waves, flawless peach lip makeup, and a tattoo on her neck.

The backdrop of a glossy black car adds dramatic reflections and a touch of urban elegance. The soft, film-like lighting, muted and cool-toned colors, subtle depth of field, and the texture of the fabric and shearling fur are highly visible. The mood is expensive, modern, and minimalist, like a premium brand catalog shoot. The face remains unchanged.
```

[[Fashion Photography]] [[Magazine Editorial]]

---

### 56. 超现实混合媒体时尚肖像拼贴画

**Author**: [Alex Zhang](https://x.com/jojogh_007)  **Date**: 2025-12-10  **Language**: en

> 一个高度详细的 JSON 提示，用于创建超现实的混合媒体数字拼贴画。它将蹲伏模特的时尚摄影与充满活力的扁平矢量动物插图（兔子、鹿、狼）结合在一起，这些插图超现实地缠绕在她的身体周围，旨在呈现孟菲斯/波普艺术风格的俏皮、前卫的编辑外观。

![超现实混合媒体时尚肖像拼贴画](https://cms-assets.youmind.com/media/1765509690665_fn6l6i_G70WzcnaQAEFrr8.jpg)

```
{
"image_request": {
"goal": "Create a surreal mixed-media fashion portrait with intertwining animal illustrations",
"meta": {
"image_type": "Mixed Media Art",
"quality": "8K",
"color_mode": "Full Color with Graphic Overlay",
"style_mode": "mixed_media_illustration",
"aspect_ratio": "1:1",
"resolution": "1080x1080px"
},
"creative_style": "Mixed Media Digital Collage combining high-fashion photography with vibrant, flat vector illustrations in a Memphis/Pop Art style. The composition blends a realistic crouching model with stylized vector animals that surrealistically wrap and coil around her body, creating a playful yet edgy editorial look.",
"overall_theme": "artistic fashion collage",
"mood_vibe": "playful surreal chic",
"style_keywords": [
"mixed media",
"digital collage",
"vector art overlay",
"Memphis design",
"fashion editorial",
"surrealism",
"floral illustration",
"wrapping animals",
"pop art",
"vibrant colors"
],
"subject": {
"count": "1",
"type": "female",
"identity": "elegant young woman with slicked-back dark hair",
"identity_preservation": {
"description": "Preserve the realistic fashion photography aspect of the model while allowing the graphic animals to wind around her",
"notes": "Seamless integration of 2D art wrapping around 3D form"
},
"age_appearance": "young adult",
"skin": "natural tan, realistic texture",
"makeup": {
"lips": "natural matte",
"eyes": "neutral (one eye obscured by art)",
"general": "polished fashion makeup"
},
"facial_features": {
"expression": "intense serious gaze",
"eyes": {
"gaze": "direct at viewer",
"intensity": "piercing"
},
"lips": {
"gesture": "closed, hands resting near chin"
}
},
"hair": {
"length": "medium",
"texture": "straight",
"style": "slicked back into a neat bun, adorned with a drawn floral headband/crown",
"lighting_interaction": {
"light": "studio lighting",
"shadow_play": "soft shadows"
}
},
"clothing": {
"top": "floral print long-sleeve dress",
"bottom": "matching skirt (dress)",
"full_description": "fitted white dress with red and pink floral patterns",
"accessories": "strappy high-heeled sandals with crystal embellishments, dark blue nail polish"
},
"props": {
"bouquet": "none",
"wine_glass": "none",
"other": "vector illustrations of animals (yellow rabbit, deer, wolf) stylized to elongate and wrap physically around the model's torso, arms, and legs"
}
},
"pose_action": {
"description": "Crouching/squatting in a compact fashion pose, elbows resting on knees, hands framing the face and chin, interacting with the illustrated animals winding around her.",
"overall_pose": "crouching fashion pose",
"head_turn": "facing forward",
"gaze": "direct",
"body_position": "compact squat",
"hands": "fingers gently touching cheeks/chin",
"movement": "static pose, dynamic flow of wrapping art"
},
"multiple_frames_expressions": [],
"environment": {
"setting": "Minimalist studio",
"location": "indoor",
"weather": "n/a",
"time_of_day": "studio lighting",
"}
```

[[Fashion Photography]] [[Surrealism]]

---

### 57. 电影感都市夜景与数字广告牌

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2025-12-09  **Language**: en

> 一个详细的图像生成提示，用于创作一个电影般、超现实的都市夜景，画面中一位时尚女性站在街角，指向一块巨大的数字广告牌，上面展示着她自己的高级时装肖像。

![电影感都市夜景与数字广告牌](https://cms-assets.youmind.com/media/1765440034657_iaro9w_G7u73RTacAALXLM.jpg)

```
{
  "image_generation_prompt": {
    "subject_details": {
      "description": "Young stylish woman with long straight brown hair",
      "expression": "Subtle, confident smile",
      "outfit": {
        "top": "Soft pink T-shirt under an open black casual jacket",
        "bottom": "Fitted dark jeans",
        "shoes": "Polished black shoes"
      },
      "pose": "Standing on a street corner facing the camera, pointing with one hand toward a building behind her"
    },
    "background_scene": {
      "setting": "Vibrant modern city at night",
      "key_element": "Giant digital billboard on a tall glass building",
      "billboard_content": {
        "visual": "Portrait of the same woman in the same outfit, posed like a high-fashion magazine cover",
        "text_headline": "VOUGHT STYLE",
        "text_subheading": "Smaller indistinct magazine-style text"
      },
      "atmosphere": [
        "Neon lights",
        "Glowing billboards",
        "Moving cars with motion blur",
        "Wet pavement with reflections"
      ]
    },
    "technical_specs": {
      "style": "Cinematic, Photorealistic, Urban Night",
      "camera": "35mm lens",
      "depth_of_field": "Shallow with soft bokeh on city lights",
      "lighting": "Mixed neon ambient, directional light from billboard, moody shadows",
      "resolution": "8k, high definition"
    }
  }
}
```

[[Fashion Photography]] [[Neon Lighting]] [[Cinematic Scene]] [[Urban Night Photography]]

---

### 58. 超广角动态透视提示

**Author**: [D. Humann](https://x.com/dhumann)  **Date**: 2025-12-08  **Language**: en

> 将现有照片转换为戏剧性、超逼真、超广角照片的详细指令提示。它要求采用极端的相机角度（低角度或高角度）来制造透视缩短效果，使近处的身体部位显得巨大，而其余部分则在透视中后退，同时保持时尚的姿势和一致的背景。

![超广角动态透视提示](https://cms-assets.youmind.com/media/1765438602746_fc2y6k_G7rULWrbYAA_Ti7.jpg)

```
Transform the original photo into a dramatic, photorealistic, ultra wide-angle shot with an extreme camera angle (including views from directly below or above), where one or more body parts are right next to the lens and look huge, the rest of the body recedes in perspective, and the same person strikes a stylish, complex, powerful pose in a consistent, expanded version of the original environment.
```

[[Fashion Photography]] [[Forced Perspective]] [[Perspective Distortion]]

---

### 59. 优雅的印度 Lehengas 时尚摄影提示

**Author**: [Vivek HY](https://x.com/Vivekhy)  **Date**: 2025-12-08  **Language**: en

> 一个详细的图像生成提示，用于创建一张超详细的 8K 时尚照片，照片中一位女士身着优雅、刺绣精美的淡紫色-粉色 Lehenga，强调柔和的室内日光和优雅、喜庆的氛围。

![优雅的印度 Lehengas 时尚摄影提示](https://cms-assets.youmind.com/media/1765438620289_j4vpan_G7p37QnaMAAriyG.jpg)

```
{
  "prompt": {
    "scene": {
      "setting": "Indoor modern hall with large glass windows, soft natural daylight entering from outside.",
      "mood": "Elegant, festive, graceful Indian traditional fashion aesthetic."
    },
    "subject": {
      "type": "adult woman",
      "pose": "Standing with both arms raised slightly outward in a playful expressive pose.",
      "expression": "Soft playful expression with lips puckered as if blowing a kiss.",
      "appearance": {
        "hair": "Long straight or slightly wavy hair left open.",
        "makeup": "Subtle glam makeup with soft pink tones.",
        "jewelry": "Statement earrings and minimal accessories."
      }
    },
    "outfit": {
      "lehenga": {
        "color": "{argument name="lehenga color" default="Pastel lavender-pink"} with shimmer accents.",
        "details": "Heavy floral embroidery with pastel threadwork, sequins, bead detailing, layered net fabric.",
        "silhouette": "Full flared lehenga with rich volume and detailed hemline."
      },
      "choli": {
        "description": "Matching embroidered choli blouse with intricate floral patterns, short sleeves, and a modern fitted cut.",
        "color": "Soft pastel lavender with metallic embellishments."
      },
      "dupatta": {
        "description": "Sheer net dupatta draped over one shoulder, adorned with scattered floral embroidery and sequins.",
        "style": "Soft, flowing, translucent fabric."
      }
    },
    "composition": {
      "camera_angle": "Full-body portrait captured from a slightly lower angle to enhance the lehenga's flare.",
      "lighting": "Soft diffused indoor daylight with balanced highlights.",
      "colors": "Soft pastels, lavender, pink, mint green embroidery accents.",
      "ratio": "4:5 or 3:4 portrait format."
    },
    "render_style": {
      "quality": "Ultra-detailed 8K fashion photography.",
      "tones": "Soft pastel luxury tones with realistic shimmer and embroidery texture.",
      "focus": "Sharp focus on lehenga details and subject's pose; smooth bokeh background."
    }
  }
}
```

[[Fashion Photography]] [[8K Photography]]

---

### 60. 社论式牛仔肖像，保留面部特征

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2025-11-24  **Language**: en

> 一个 JSON 风格的提示，用于创建一张 8K 编辑级时尚肖像，描绘一个身穿牛仔服和羊羔绒夹克的人，同时保持其面部与参考照片一致。

![社论式牛仔肖像，保留面部特征](https://cms-assets.youmind.com/media/1764209287561_cussb9_G6ffMXfbQAABUWE.jpg)
![社论式牛仔肖像，保留面部特征](https://cms-assets.youmind.com/media/1764209290078_kmguwq_G6ffMYaaoAA9ko6.jpg)

```
{
  "photo": {
    "type": "editorial_fashion_photo",
    "quality": "8k photorealistic",
    "lens": "50mm shallow depth of field",
    "composition": "medium portrait, editorial framing, no text, no watermark",
    "face": {
      "preserve_original": true,
      "reference_match": true,
      "description": "The model's face must remain 100% identical to the provided reference picture in all facial features, proportions, makeup style, and expression."
    },
    "model_pose": {
      "position": "seated",
      "legs": "relaxed pose with one leg bent",
      "hands": "one hand supporting the head",
      "expression": "calm, minimalist mood"
    },
    "wardrobe": {
      "jacket": {
        "type": "cream shearling jacket",
        "texture": "shaggy, fluffy, tactile"
      },
      "shirt": {
        "type": "denim shirt",
        "layered": true
      },
      "pants": {
        "type": "light blue jeans"
      },
      "boots": {
        "type": "black leather Chelsea boots",
        "texture": "smooth polished leather"
      },
      "socks": {
        "color": "beige"
      }
    },
    "textures": {
      "emphasis": [
        "fluffy shearling fibers",
        "rugged denim fabric",
        "smooth leather boots",
        "visible seams",
        "visible stitches"
      ]
    },
    "environment": {
      "backdrop": "clean light gray studio backdrop",
      "lighting": {
        "style": "soft natural studio lighting",
        "key_light": "gentle side key light",
        "fill_light": "subtle fill",
        "shadows": "soft shadows"
      }
    },
    "color_grade": {
      "type": "cinematic",
      "balance": "neutral warm-cool tone balance"
    }
  }
}
```

[[Fashion Photography]] [[Face Identity Matching]] [[Editorial Fashion Portrait]]

---

### 61. 床上的分开的衣物

**Author**: [CHAO2U AI](https://x.com/CHAO2U_AI)  **Date**: 2025-11-22  **Language**: en

> 一个编辑风格的提示，它以一个参考人物为基础，将她的每件衣服单独平铺在床上。

![床上的分开的衣物](https://cms-assets.youmind.com/media/1763885776121_5wbi8e_G6WmWG4awAAOfG8.jpg)
![床上的分开的衣物](https://cms-assets.youmind.com/media/1763885779430_5x8s1g_G6WmXAvaoAA_wYG.jpg)

```
Give each piece of her clothing separately on the bed
```

[[Fashion Photography]] [[Flat Lay Photography]]

---

### 62. 杂乱衣橱中的高角度仙女垃圾摇滚偶像

**Author**: [Mani](https://x.com/JustMani)  **Date**: 2025-11-22  **Language**: en

> 一个长篇、高度详细的图像生成规范，描述了一个东亚偶像以高角度镜头倒躺在一个凌乱的衣橱里，具有仙女垃圾摇滚风格、纹身以及特定的服装和环境细节。最好在有参考姿势图像时使用。

![杂乱衣橱中的高角度仙女垃圾摇滚偶像](https://cms-assets.youmind.com/media/1763885730864_glu6vm_G6VuGawW0AACHQW.jpg)
![杂乱衣橱中的高角度仙女垃圾摇滚偶像](https://cms-assets.youmind.com/media/1763885733855_y32rdc_G6VuGauWYAAZNir.jpg)
![杂乱衣橱中的高角度仙女垃圾摇滚偶像](https://cms-assets.youmind.com/media/1763885736139_cwr7iu_G6VuGatW8AAFsGz.jpg)
![杂乱衣橱中的高角度仙女垃圾摇滚偶像](https://cms-assets.youmind.com/media/1763885739425_oqyfk9_G6S2x1xaYAAZ_N6.jpg)
![杂乱衣橱中的高角度仙女垃圾摇滚偶像](https://cms-assets.youmind.com/media/1763885743286_ybd5vb_G6S2x1ybIAAlOt6.jpg)

```
High-angle bird's-eye view shot of a female east Asian idol subject lying on the floor of a cluttered closet, strictly following the upside-down pose and anatomical structure shown in {argument name="reference_image" default="image_0.png"}. She is wearing a rich blue lace-overlay mini dress with a milkmaid bodice, sweetheart neckline, cap sleeves, and a lettuce hem. She wears heavy, knee-high red leather boots with a vertical front seam. Visible tattoos include a barbed wire band on the thigh and stick-and-poke heart and key motifs on the chest. The floor is covered in piles of mixed textiles, tulle, and clothing. The background walls are painted yellow, featuring white wire shelving, semi-transparent plastic storage drawers, and a packed clothing rack. Lighting is overhead tungsten, creating a warm sepia, vintage 90s disposable camera filter look. The mood is exhaustive, messy, and romantically grunge.

Fairy grunge aesthetic, girl in rich blue dress and red leather boots lying upside-down in cluttered closet with yellow walls, pose from {argument name="reference_image_short" default="image_0.png"}, sepia tone, high angle shot.

minimalism, clean floor, bright daylight, cold lighting, organized, empty space, modern furniture, neon colors, hd digital look, glossy finish, wide angle, fisheye, distorted limbs, missing tattoos, incorrect pose.
```

[[Fashion Photography]] [[Editorial Photography]] [[High Angle Shot]]

---

### 63. 时尚女性的超逼真环境肖像提示（部分）

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2025-11-21  **Language**: en

> JSON 格式的提示词，描述了一位时尚年轻女性在茂密热带竹林中的超写实环境肖像，其中包含详细的服装和姿势说明，但内容被截断。

![时尚女性的超逼真环境肖像提示（部分）](https://cms-assets.youmind.com/media/1763887334848_gzjofv_G6RKPI-aEAEZgWt.jpg)
![时尚女性的超逼真环境肖像提示（部分）](https://cms-assets.youmind.com/media/1763887337289_yifyi6_Vz-uac6Ps38VOCVE.jpg)

```
{
  "prompt": "Hyper-realistic environmental portrait of a stylish young woman standing in a dense tropical bamboo forest. She is wearing a wide-brimmed black fedora hat, round dark sunglasses with thin metal frames, a plain black crew-neck t-shirt tucked in, and dark grey high-waisted trousers. She stands with a confident posture, leaning slightly forward, with her right
```

[[Fashion Photography]] [[Photorealism]] [[Tropical Setting]]

---

### 64. 元旦特辑：2026 祝福四格拼图

**Author**: [松果先森](https://x.com/songguoxiansen)  **Date**: 2025-12-30  **Language**: zh

> 这是一个为 Nano Banana Pro 设计的详细多面板提示，用于创建一个 2x2 网格照片拼贴画。画面中，一位女性角色身着四套不同的服装，在四个不同的场景中拼凑一个拼图，拼图的中心显示“2026 新年快乐”。该提示详细说明了面部特征的精确保留、服装细节、背景元素以及时尚杂志风格的照片参数。

![元旦特辑：2026 祝福四格拼图](https://cms-assets.youmind.com/media/1767455034932_ivuvu0_G9V-MszakAEAIBw.jpg)

```
[关键:保持精确的面部特征,保留原始脸部结构,图中角色与上传参考图完全一致] 高级摄影棚2x2宫格写真。左上格(海军蓝背景):人物穿海军蓝色制服风连衣裙,金色纽扣装饰,复古卷发配蓝色贝雷帽和珍珠耳环,她双手托举一块巨大的拼图块(左上角块,上面有"20"数字),向画面中心方向移动,眼神专注地看向中心拼图区域,表情认真,嘴角微笑,背景有海军条纹、船锚、"启航新年"字样。右上格(樱花粉背景):同一女性穿粉色蕾丝连衣裙,珍珠项链,公主头配粉色玫瑰花发夹和水晶耳环,她双手托举右上角拼图块(上面有"26"数字)向中心移动与左上格拼接,眼神看向拼图接缝处,表情专注期待,身体前倾,背景有粉色樱花、"美好相遇"字样、蝴蝶、花瓣。左下格(薄荷绿背景):同一女性穿薄荷绿色棉麻连衣裙,文艺风格,自然长发配绿色发带和木质耳环,她双手托举左下角拼图块(上面有"元旦"字样)向上移动与左上格对接,眼神看向拼图,表情认真,嘴巴微微抿起,背景有绿色植物、"希望生长"字样、新芽、叶子。右下格(柠檬黄背景):同一女性穿黄色连衣裙,向日葵图案,双马尾配黄色蝴蝶结,她双手托举最后一块右下角拼图(上面有"快乐"字样)完成拼图,四块拼图在画面中心完美拼成"2026元旦快乐"完整图案,她头后仰,眼睛看向完成的拼图,脸上洋溢着成功喜悦的笑容,画面中心爆出金色光芒和彩纸,背景有黄色太阳、"圆满成功"字样、笑脸、向日葵。四格之间拼图从四角汇聚到中心形成完整画面,清透妆容,明亮环形光,85mm镜头,f/1.8光圈,拼图互动四联构图,时尚杂志风格。
```

[[Fashion Portrait]] [[Character Consistency]] [[2x2 Grid Layout]] [[Photo Collage]]

---

### 65. 干净极简的影棚肖像，带着俏皮的眨眼

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-25  **Language**: en

> 一个用于 Nano Banana Pro 的结构化提示词，旨在生成一张干净、极简的影棚肖像，描绘一位年轻女性（人物身份与参考图片保持一致），她身穿黑色露肩连衣裙，并带有俏皮的眨眼和微微伸出的舌头。

![干净极简的影棚肖像，带着俏皮的眨眼](https://cms-assets.youmind.com/media/1774508276490_oh1cvn_HEQlEQwa0AA5iBP.jpg)
![干净极简的影棚肖像，带着俏皮的眨眼](https://cms-assets.youmind.com/media/1774508276494_x5tf4g_HEQlDN_bcAAIKSL.jpg)
![干净极简的影棚肖像，带着俏皮的眨眼](https://cms-assets.youmind.com/media/1774508276500_23b9qb_HEQlDtMbcAAzvTk.jpg)

```
{
"photo_type":"studio portrait, clean minimal aesthetic",

"subject":{
"type":"young woman",
"use_reference_image":true,
"face_reference":true,
"preserve_identity":true,
"instruction":"strictly use reference face, do NOT change facial structure, skin tone, eye color, or hair color",
"pose":"leaning slightly forward, shoulders angled, playful expression with one eye wink and tongue slightly out",
"expression":"confident, flirty, natural candid"
},

"appearance":{
"hair":"same as reference image, natural texture, unchanged",
"eyes":"same as reference image, unchanged color",
"skin":"natural texture, soft glow, no over smoothing",
"makeup":"soft glam, blush, glossy lips"
},

"outfit":{
"clothing":"{argument name="clothing item" default="black off-shoulder fitted dress"}",
"style":"elegant going-out look"
},

"accessories":{
"details":[
"gold necklace with heart pendant",
"minimal earrings"
]
},

"environment":{
"location":"studio",
"background":"plain light neutral wall"
},

"lighting":{
"type":"soft studio lighting",
"setup":"even front light, subtle shadows"
},

"camera":{
"angle":"eye level",
"framing":"tight mid portrait",
"focus":"sharp on face"
},

"color_grading":{
"style":"clean natural",
"tones":"warm skin tones",
"contrast":"medium"
},

"details":{
"must_include":[
"reference face unchanged",
"same hair and eye color",
"playful wink expression",
"natural skin texture"
],
"avoid":[
"face distortion",
"changing identity",
"AI plastic skin",
"different hair color"
]
}
}
```

[[Fashion Portrait]] [[Playful Expression]] [[Identity Reference]]

---

### 66. 电影感的女性特写 (Nano Banana Pro)

**Author**: [空想写真家](https://x.com/KusoPhoto)  **Date**: 2026-03-25  **Language**: ja

> 一个详细的提示词，用于图像生成 (Nano Banana Pro) 和随后的视频生成 (Kling 3.0 Omni)。该提示词描述了电影般的特写镜头：一位女性正在化妆并戴上眼镜，随后做出了一个迷人的姿势。

```
柔らかな光に包まれた女性のシネマティックなクローズアップ。メイクブラシで肌を整え、丁寧にリップを塗った後、両手でそっと眼鏡をかけて照れくさそうに微笑む。準備を終えてカメラに小さく手を振り、首をかしげる愛らしい仕草が、美しいボケ味とともに滑らかにフェードアウトしていくエモーショナルな映像。
```

[[Fashion Portrait]] [[Film Cinematic]]

---

### 67. 霓虹 人像 提示词

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-03-24  **Language**: en

> 一个 Nano Banana 2 提示词，用于生成一张高端时尚肖像，描绘了一位留着深色短波波头的女性，以戏剧性的霓虹粉和蓝色灯光为特色，背景为深紫色。

![霓虹 人像 提示词](https://cms-assets.youmind.com/media/1774421474343_tssh2v_HEJua6KbIAAgPjk.jpg)

```
A portrait of a woman with a short dark bob haircut looking over her shoulder, dramatic neon pink and blue lighting on her face and shoulder, dark purple background, high-end fashion photography style, sharp focus, 8k.
```

[[Fashion Portrait]] [[High Fashion Photography]]

---

### 68. Gemini Nano Banana Pro 的闪耀猎豹肖像提示

**Author**: [Sadie 🥀](https://x.com/NameIsSudee)  **Date**: 2026-03-22  **Language**: en

> 一个详细、结构化的 JSON 提示词，用于 Gemini Nano Banana Pro 生成一张年轻女性的超写实肖像，她身穿闪亮的豹纹上衣，置身室内，重点突出特定的面部特征、姿势和光线。

![Gemini Nano Banana Pro 的闪耀猎豹肖像提示](https://cms-assets.youmind.com/media/1774248308166_gjsihf_HEBrgEGaMAAX8eY.jpg)
![Gemini Nano Banana Pro 的闪耀猎豹肖像提示](https://cms-assets.youmind.com/media/1774248308168_eo948m_HEBrf-3aQAAMaMo.jpg)
![Gemini Nano Banana Pro 的闪耀猎豹肖像提示](https://cms-assets.youmind.com/media/1774248308161_209ea6_HEBrf9waUAA0Ziq.jpg)

```
{
  "image_prompt": {
    "subject": {
      "type": "young woman",
      "features": {
        "hair": "bright red, tied back in a loose ponytail with some face-framing strands",
        "eyes": "blue",
        "skin": "fair with light freckles",
        "expression": "neutral, serious, maintaining direct eye contact with the camera"
      }
    },
    "clothing": {
      "garment": "long-sleeve, form-fitting top",
      "pattern": "leopard print (tan, brown, and black spots)",
      "texture": "subtle glittery or sparkly finish"
    },
    "pose": {
      "stance": "standing sideways, body angled slightly away but face turned towards the viewer",
      "arms": "right hand resting naturally on her hip"
    },
    "environment": {
      "setting": "indoor room, likely a home office, streaming room, or bedroom",
      "background_elements": [
        "white desk",
        "black computer monitors",
        "white spherical microphone on a small tripod stand",
        "black desk mat or keyboard",
        "plain white walls"
      ]
    },
    "photography_style": {
      "lighting": "soft, bright, natural-looking indoor daylight",
      "focus": "shallow depth of field (sharp subject, slightly blurred background)",
      "aesthetic": "photorealistic, high-resolution portrait photography"
    }
  }
}
```

[[Fashion Portrait]] [[Glamour Photography]] [[Indoor Setting]]

---

### 69. 电影般呈现一个年轻人离开咖啡馆的场景

**Author**: [Harboris](https://x.com/harboriis)  **Date**: 2026-03-22  **Language**: en

> 一个详细的超现实提示，用于 Nano Banana Pro 生成一张电影般的全景编辑肖像，描绘一位年轻男子走出一家现代咖啡馆的场景，强调动感、服装、背景细节（星巴克招牌）和相机技术规格。

![电影般呈现一个年轻人离开咖啡馆的场景](https://cms-assets.youmind.com/media/1774248306645_sju58o_HEBHE4vbIAAZfMR.jpg)

```
Ultra-realistic, full-body portrait of the same young man (ensure strict facial consistency with prior reference), captured mid-step as he walks out through the glass doors of a modern café. His body is slightly angled forward, with one leg stepping ahead naturally, conveying motion.
He holds a takeaway coffee cup in his left hand close to his chest, while his right hand rests casually inside his pocket. A black backpack hangs effortlessly over one shoulder. His head is turned slightly to the side, gaze directed away from the camera, with a calm, confident, and composed expression.
He is dressed in an oversized red t-shirt, black cargo pants, black-and-white sneakers, and a minimal thin chain necklace, styled in a contemporary urban fashion aesthetic.
The background features glass doors with visible Starbucks signage and logo, with warm indoor lighting spilling outward. The café interior appears softly blurred, creating depth, while natural daylight illuminates the subject from outside.
Shot with a 50mm lens, shallow depth of field, cinematic composition, realistic lighting and shadows, high dynamic range, and ultra-detailed textures.
Aspect ratio: 4:5
Resolution: 8K
Style: photorealistic, cinematic, editorial fashion photography
```

[[Fashion Portrait]] [[Film Cinematic]]

---

### 70. Seedream 4.5 与 Nano Banana 2 输出对比

**Author**: [Adam也叫吉米](https://x.com/Adam38363368936)  **Date**: 2026-03-22  **Language**: zh

> 以下是使用相同提示词，由 Seedream 4.5 和 Nano Banana 2 生成的图像对比。值得注意的是，Seedream 的美学风格更符合亚洲女性的审美标准，而 Nano Banana 的结果虽然不错，但“过于写实”。提示词描述的是一位身着特定服饰、置身特定场景的年轻亚洲美女。

![Seedream 4.5 与 Nano Banana 2 输出对比](https://cms-assets.youmind.com/media/1774248320754_rsbp6b_HEA1ElmbAAAxFk8.jpg)
![Seedream 4.5 与 Nano Banana 2 输出对比](https://cms-assets.youmind.com/media/1774248320810_knodk1_HEA1ElLbEAAPxI9.jpg)

```
生成图片：{argument name="人物描述" default="年轻亚裔美女，冷白皮美女，黑色长卷发"}，穿{argument name="服装" default="白色吊带+酒红杂色开衫+酒红长裤"}，站在{argument name="场景" default="室内简约场景（桌面摆红酒+手机），背景墙简约挂画"}，{argument name="光线和氛围" default="夜景，室内暗光，中景构图，慵懒随性的日常穿搭氛围，画面细节真实自然"}。
```

[[Fashion Portrait]] [[AI Model Comparison]] [[Model Comparison]]

---

### 71. 现代楼梯上的日本女性肖像

**Author**: [Alice](https://x.com/youngcatwoman)  **Date**: 2026-03-19  **Language**: en

> 为 Nano Banana Pro 设计的结构化提示词，用于生成一张逼真的肖像，描绘一位美丽的日本年轻女性，身着白色西装外套和白色乳胶紧身衣，坐在现代木质楼梯上。

![现代楼梯上的日本女性肖像](https://cms-assets.youmind.com/media/1773988995967_007l2q_HDPtqa1bQAAV7qu.jpg)

```
{
"prompt": "Photorealistic portrait of a beautiful young Japanese woman with long platinum blonde hair sitting on modern wooden stairs. She wears a plunging white blazer over a white latex t-front bodysuit and glossy white stilettos. Symmetrical pose with legs apart. --ar 3:4",
"subject": {
"appearance": "Beautiful young Japanese woman, fair skin, dark brown eyes.",
"hair": "Extra-long, straight, platinum blonde.",
"jewelry": "Silver hoop earrings, thin silver chain with small round pendant."
},
"outfit": {
"clothing": "White tailored blazer styled as a bodysuit, deeply unbuttoned.",
"shoes": "Glossy white patent leather stiletto pumps."
},
"pose": {
"body": "Sitting upright on a stair tread facing the camera.",
"legs": "Spread wide apart, knees bent at an angle.",
"hands": "Left hand resting gently near the chin, right hand placed down on the step between her thighs."
},
"background": {
"environment": "Modern indoor staircase.",
"structure": "Light oak wooden treads with crisp white painted risers and white side walls."
},
"color_grading": "Soft, diffused indoor lighting. Natural color palette with a clean, ethereal look matching the bright blonde hair and white clothing.",
"exact_colors": {
"outfit_white": "#F8F8F8",
"hair_blonde": "#EAE5D9",
"skin_tone": "#EADDD7",
"stair_wood": "#9B7653",
"stair_white": "#F4F4F4",
"shoe_white": "#FFFFFF",
"eye_brown": "#3D2314"
}
}
```

[[Fashion Portrait]]

---

### 72. 奢华编辑肖像照，带硬锁定面部参考

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-02-27  **Language**: en

> 生成一张超写实时尚肖像的提示词，描绘一位自信的女性，拥有特定身材（S 形身材，大腿丰满），要求与硬锁定的参考图像实现 100% 面部匹配，背景设定在地中海阳台的黄金时段，旨在呈现奢华的时尚杂志风格。

![奢华编辑肖像照，带硬锁定面部参考](https://cms-assets.youmind.com/media/1772259951152_v9csaq_HCJFgtqa0AAhhH7.jpg)
![奢华编辑肖像照，带硬锁定面部参考](https://cms-assets.youmind.com/media/1772259951162_cqltue_HCJFguKaUAAKeuJ.jpg)
![奢华编辑肖像照，带硬锁定面部参考](https://cms-assets.youmind.com/media/1772259951446_fers8b_HCJFgzTaMAAaI6y.jpg)

```
Create a hyper-realistic(With my hardlocked reference face. No changes to face or Tattoos. 100% face match). She has S figure with thick thighs and toned waist. Photorealistic fashion portrait of a confident woman with smooth warm-toned skin, long hair in a soft updo with a pink flower, natural makeup and expressive eyes.
She’s wearing a pastel pink lace mini dress with thin straps, fitted corset-style bodice, sweetheart neckline, semi-sheer floral lace texture, and a layered ruffled short skirt, holding a glossy shell-shaped pink clutch.
Pose: relaxed flirty stance, one leg slightly crossed forward,body angled naturally toward the camera.
Background: Mediterranean balcony overlooking the ocean at golden hour, warm sunlight, pastel sky, white stone railings, soft depth of field.
Ultra-realistic photography, 8K detail, sharp subject, soft cinematic bokeh, natural light, luxury editorial look.
```

[[Fashion Portrait]] [[Golden Hour Light]]

---

### 73. 日落船景，比基尼人物造型夸张

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-02-20  **Language**: en

> 一个高度具体、结构化的提示，用于生成一张垂直照片：两名女性身穿比基尼，身材呈夸张的沙漏形，坐在一艘船的船尾，背景是热带日落。照片强调黄金时段的光线和特定团队主题的泳装。

![日落船景，比基尼人物造型夸张](https://cms-assets.youmind.com/media/1771655071628_lu8han_HBnfmONXUAAFI8U.jpg)

```
{
  “subject”: {
    “description”: “A vertical photograph of two young women with strikingly attractive physiques in string bikinis, seated on the stern of a boat during a scenic sunset cruise.”,
    “body”: {
      “physique”: “Both women possess highly sculpted, hourglass figures with very defined, cinched waists and prominent, curvaceous glutes and hips. Their toned abdominal muscles and lean limbs are emphasized by their poses. Their skin is smooth, bronzed, and glowing.”,
      “pose”: “The blonde woman on the left sits turned, looking back over her shoulder at the camera with a alluring smile, her posture dramatically accentuating the curve of her lower back and shapely glutes. The dark-haired woman on the right reclines slightly, holding a glass of white wine aloft with her eyes closed, the pose highlighting her taut midsection and full bust.”,
“features”: “The blonde woman has long, flowing blonde hair and a captivating smile. The dark-haired woman has long, dark, glossy hair and a sultry, relaxed expression.”
    }
  },
  “wardrobe”: {
    “outfit”: “The blonde woman wears a purple and yellow string bikini that snugly fits and accentuates her exaggerated curves, particularly the thong bottom. The dark-haired woman wears a green and white string bikini that emphasizes her bust and narrow waist, with a Boston Celtics logo visible.”
  },
  “pose_action”: “Two women with highly defined, attractive physiques relaxing on the back of a boat at sunset, posing to highlight their body contours.”,
  “scene”: {
    “environment”: “The stern of a modern motorboat moving through tropical waters at sunset.”,
    “elements”: “A wide, frothy white wake trails behind the boat. In the background, there are lush, prominent tropical mountains silhouetted against a dramatic sky filled with fiery orange, pink, and purple clouds.”,
“composition”: “A vertical photograph capturing the two women from the mid-thigh up, centered on the back of the boat against the expansive sunset backdrop.”
  },
  “lighting”: {
    “setup”: “Warm, golden hour light from the setting sun.”,
    “details”: “The low sun casts a warm, golden glow, perfectly sculpting their bodies and highlighting their defined muscles and curves, while casting soft, long shadows. The light catches the moisture on their skin, making it glisten.”
  },
  “camera”: {
    “technical”: “A sharp, high-resolution photograph with vibrant, warm colors and a candid, photorealistic quality.”,
    “aspect_ratio”: “3:4”,
    “constraints”: [
      “Two women with highly exaggerated, attractive hourglass figures.”,
      “Posing to dramatically highlight their curves and physiques.”,
“Specific Lakers and Celtics-themed string bikinis.”,
      “Sitting on the back of a boat with a wake visible.”,
      “Dramatic tropical mountain sunset with colorful clouds.”,
      “Vertical photograph, golden hour lighting, photorealistic style.”
    ]
  }
}
```

[[Fashion Portrait]] [[Golden Hour Light]]

---

### 74. 充满活力的街机摩托车游戏肖像提示

**Author**: [bengi](https://x.com/p3rikly)  **Date**: 2026-01-30  **Language**: en

> 一个结构化的提示，用于生成一张充满活力、生动的年轻女性肖像，她坐在一辆街机摩托车游戏机上，强调饱和色彩、高对比度照明和突出她身材的特定服装。

![充满活力的街机摩托车游戏肖像提示](https://cms-assets.youmind.com/media/1769841080331_wyd05x_G_7J8TVWAAA6mq9.jpg)

```
{
"prompt_structure": {     "subject": {       "appearance": "Young woman with long, wavy blonde hair and a radiant, joyful expression featuring a wide smile.",       "pose": "Seated on a electric fuchsia arcade motorcycle game, leaning slightly forward with hands on the handlebars, body angled in profile while turning head to face the camera making visible clearly her fit curvaceous low back."     },     "attire": {       "top": "Strapless red knit crop top with deep V neckline featuring distressed/ripped texture and a decorative buckle strap across the chest.",       "bottoms": "Matching tight white latex shorts.",       "accessories": "Visible white {argument name="brand" default="Dolce & Gabbana"} waistband with black logo text peering above the shorts."     },     "environment": {       "location": "Indoor amusement arcade.",       "foreground": "Bright electric yellow 'SUPER KEOR BIKES' arcade racing cabinet with a realistic motorcycle seat and dashboard.",       "background": "Blurry array of other arcade machines, including game screens and a neon sign reading 'Ready to Play?.",       "lighting": "Vibrant, high-contrast arcade lighting with dominant orange LED strips outlining the machines and cool electric blue ambient light in the background."     },     "style": {       "aesthetic": "Energetic, playful, and vibrant.",       "color_palette": "Saturated red and pink (outfit), neon orange, electric blue, and deep shadows.",       "photography_style": "Medium shot, high-flash or bright environmental lighting, sharp focus on the subject with a shallow depth of field background."     }   } }
```

[[Fashion Portrait]] [[Neon Lighting]] [[Curvy Figure]] [[Arcade Game Machine]]

---

### 75. 生动街机肖像提示

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2026-01-29  **Language**: en

> 一个详细的 JSON 提示，用于生成一张充满活力、高对比度的图像，描绘一位年轻女性（悉尼·斯威尼/萨迪·辛克类型）坐在一辆粉色街机摩托车游戏机上，强调鲜艳的红色服装、霓虹灯照明和俏皮的审美。

![生动街机肖像提示](https://cms-assets.youmind.com/media/1769755029256_tbqkqn_G_1dv3_agAE7PID.jpg)
![生动街机肖像提示](https://cms-assets.youmind.com/media/1769755029336_nrjlq9_G_1duW8bUAYeOmW.jpg)

```
{
  "subject": {
    "appearance": "Young woman with long, wavy blonde hair and a radiant, joyful expression featuring a wide smile.",
    "pose": "Seated on a pink arcade motorcycle game, leaning slightly forward with hands on the handlebars, body angled in profile while turning head to face the camera."
  },
  "attire": {
    "top": "Strapless bright red knit crop top (bandeau style) featuring distressed/ripped texture and a decorative buckle strap across the chest.",
    "bottoms": "Matching tight bright red shorts.",
    "accessories": "Visible white Calvin Klein waistband with black logo text peering above the shorts."
  },
  "environment": {
    "location": "Indoor amusement arcade.",
    "foreground": "Bright pink 'SUPER BIKES' arcade racing cabinet with a realistic motorcycle seat and dashboard.",
    "background": "Blurry array of other arcade machines, including game screens and a neon sign reading 'Fly O'Clock'.",
    "lighting": "Vibrant, high-contrast arcade lighting with dominant neon pink LED strips outlining the machines and cool blue ambient light in the background."
  },
  "style": {
    "aesthetic": "Energetic, playful, and vibrant.",
    "color_palette": "Saturated bright red (outfit), neon pink, electric blue, and deep shadows.",
    "photography_style": "Medium shot, high-flash or bright environmental lighting, sharp focus on the subject with a shallow depth of field background."
  }
}
```

[[Fashion Portrait]] [[High Contrast]] [[Neon Lighting]] [[Vibrant Colors]]

---

### 76. 经典单色肖像风格

**Author**: [Banana Prompts](https://x.com/bananaprompts)  **Date**: 2026-01-28  **Language**: en

> 一个简短、风格化的提示，用于生成一张经典、高对比度的单色图像，传达自信和低调的魅力，暗示这是一张高质量的肖像或时尚大片。

![经典单色肖像风格](https://cms-assets.youmind.com/media/1769668527949_kyxcpu_G_yP8e6XsAAXH0X.jpg)

```
Classic in monochrome where confidence meets quiet glamour.
High contrast, higher standards.
```

[[Fashion Portrait]] [[High Contrast Monochrome]]

---

### 77. 超逼真编辑肖像提示

**Author**: [Crystal](https://x.com/Cicily_aura)  **Date**: 2026-01-28  **Language**: en

> 一个详细的提示，用于生成一张超逼真的编辑肖像照：一位年轻女性，金色的头发，化着浓烈的焦橙色眼影，身穿猩红色紧身衣，上面有日文汉字，并带有精致的细线纹身，背景是极简主义的白色，光线为自然散射的日光。

![超逼真编辑肖像提示](https://cms-assets.youmind.com/media/1769668436339_lgujw1_G_v3HACbgAAbn4U.jpg)

```
{
  "prompt_data": {
    "subject": {
      "type": "Young woman",
      "hair": "warm golden blonde hair, center-parted, softly cascading over shoulders",
      "skin_tone": "Fair, porcelain-like complexion",
      "facial_features": "Balanced facial symmetry, confident direct gaze, calm yet alluring expression"
    },
    "makeup": {
      "eyes": "Intense burnt-orange eyeshadow with gradient blending, sharp extended winged eyeliner, precisely groomed brows",
      "lips": "Velvet matte crimson-red lipstick"
    },
    "apparel": {
      "item": "One-piece swimsuit / fashion bodysuit",
      "color": "{argument name="bodysuit color" default="Vivid scarlet red"}",
      "details": [
        "Contrasting black piping outlining the silhouette",
        "Thin black spaghetti straps",
        "Vertical black Japanese Kanji text '平和' (Peace) printed on the chest"
      ]
    },
    "accessories_and_body_art": {
      "jewelry": [
        "Delicate silver chain necklace with minimalist pendant",
        "Slim silver ring on left hand",
        "Subtle silver bracelet on left wrist"
      ],
      "tattoos": [
        "Minimal black heart outline tattoo on upper left thigh",
        "Visible fine-line tattoo on inner right arm"
      ]
    },
    "pose_and_framing": {
      "stance": "Standing casually while leaning against a smooth wall",
      "arms": "Right arm lifted with elbow bent overhead, left arm relaxed with fingers resting on thigh",
      "framing": "Mid-length portrait shot, vertical composition"
    },
    "environment": {
      "background": "Softly blurred white and light-grey minimalist wall",
      "lighting": "Natural diffused daylight, gentle shadows, evenly lit facial highlights"
    },
    "style_tags": [
      "Ultra-photorealistic",
      "High-detail skin texture",
      "Editorial portrait photography",
      "Creamy bokeh background",
      "8K ultra-high resolution"
    ]
  }
}
```

[[Fashion Portrait]] [[Natural Diffused Light]]

---

### 78. 安娜·德·阿玛斯 (Ana de Armas) 金色礼服庭院肖像提示

**Author**: [Selena 🔥](https://x.com/Queen_khan143)  **Date**: 2026-01-26  **Language**: en

> 一个结构化提示，用于生成一张安娜·德·阿玛斯（Ana de Armas）身穿金色金属闪光晚礼服，在优雅的石砌庭院中低蹲的超逼真时尚肖像。该提示详细说明了她的姿势（回眸过肩）、光线（柔和的自然光）以及对织物和石头纹理的强调。

![安娜·德·阿玛斯 (Ana de Armas) 金色礼服庭院肖像提示](https://cms-assets.youmind.com/media/1769495375120_xh429x_G_m9EPfbsAADbh6.jpg)
![安娜·德·阿玛斯 (Ana de Armas) 金色礼服庭院肖像提示](https://cms-assets.youmind.com/media/1769495375131_raktke_G_m9ckqakAA6c2r.jpg)
![安娜·德·阿玛斯 (Ana de Armas) 金色礼服庭院肖像提示](https://cms-assets.youmind.com/media/1769495375267_gipx7s_G_m9auybAAQkBlW.jpg)

```
{
  "prompt_type": "photorealistic_fashion_portrait",
  "subject": {
    "identity": {
      "entity_type": "human",
      "gender": "female",
      "public_figure": true,
      "name": "Ana de Armas"
    },
    "pose": {
      "body_position": "squat",
      "height_level": "low",
      "torso_orientation": "forward",
      "head_orientation": "turned_back_over_shoulder"
    },
    "expression": {
      "primary": "confident",
      "secondary": "playful"
    },
    "eye_direction": "toward_camera"
  },
  "environment": {
    "scene_type": "outdoor",
    "location_style": "elegant_courtyard",
    "architectural_features": {
      "arches": {
        "material": "stone",
        "style": "classical"
      },
      "stairs": {
        "type": "wide_steps",
        "material": "stone"
      }
    }
  },
  "wardrobe": {
    "primary_outfit": {
      "category": "evening_gown",
      "color": "gold",
      "finish": "metallic_shimmer",
      "structure": {
        "back": "open",
        "straps": "thin",
        "length": "floor_length",
        "side_slits": "high"
      }
    },
    "footwear": {
      "type": "high_heels",
      "color": "gold",
      "match_with_outfit": true
    }
  },
  "styling": {
    "hair": {
      "texture": "wavy",
      "arrangement": "loose",
      "accessories": {
        "type": "hair_accessory",
        "material": "gold",
        "placement": "one_side"
      }
    }
  },
  "camera": {
    "shot_type": "portrait",
    "angle": "eye_level",
    "framing": "medium_full_body",
    "focus": {
      "depth_of_field": "shallow",
      "subject_focus": "sharp",
      "background_blur": "soft"
    }
  },
  "lighting": {
    "quality": "soft",
    "style": "natural",
    "contrast": "moderate"
  },
  "rendering": {
    "detail_level": "high",
    "realism": "photorealistic",
    "texture_emphasis": [
      "fabric",
      "skin",
      "stone"
    ]
  },
  "composition": {
    "aspect_ratio": {
      "width": 3,
      "height": 4
    }
  }
}
```

[[Fashion Portrait]] [[Soft Natural Light]] [[Low Squat Pose]] [[Over-Shoulder Glance]]

---

### 79. 现代艺术画廊中的时尚肖像

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-19  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张逼真的图像：一位年轻女性身穿性感的灰色露背上衣和牛仔迷你短裤，自信地站立在现代明亮的艺术画廊中。提示词详细说明了环境（白墙、抽象画）和柔和的自然光线，以营造专业的时尚摄影风格。

![现代艺术画廊中的时尚肖像](https://cms-assets.youmind.com/media/1768890656813_noam1r_G_ClGgKWMAU2X5-.jpg)

```
{
  "meta_data": {
    "prompt_version": "2.0",
    "use_case": "Photorealistic Image Generation",
    "main_subject_count": 1
  },
  "subject_layer": {
    "anatomy": {
      "demographics": {
        "gender": "Female",
        "age_group": "Young adult",
        "ethnicity": "Western",
        "skin_tone": "Tanned"
      },
      "face_detail": {
        "same_as_reference": true,
        "expression": "Slight smirk",
        "makeup": "Natural"
      },
      "hair": {
        "color": "Blonde",
        "length": "Long",
        "style": "Straight"
      },
      "body": {
        "pose": "Standing confidently",
        "attire": {
          "top": "Sexy grey halter-neck draped top with deep plunge neckline",
          "bottom": "Light blue denim mini shorts"
        }
      }
    }
  },
  "environment_layer": {
    "location": "Modern bright art gallery",
    "elements": [
      "Contemporary abstract paintings",
      "White walls",
      "High ceiling with skylight",
      "Polished concrete floor"
    ],
    "lighting": "Soft natural gallery lighting"
  },
  "photography_layer": {
    "style": "Professional fashion photography",
    "resolution": "8k",
    "details": "Ultra detailed, realistic"
  }
}
```

[[Fashion Portrait]] [[Natural Light Photography]] [[Confident Pose]]

---

### 80. Coquette 风格卧室姿势（抬腿）

**Author**: [Kai | Neural Art](https://x.com/PromptLogicLabs)  **Date**: 2026-01-12  **Language**: en

> 一个极其详细、结构化的 JSON 提示词，用于生成一张年轻女性全身肖像，姿势独特且风格化：她仰卧在床上，双腿垂直抬起，手持一朵白色玫瑰。该提示词指定了“洛丽塔（coquette）美学”，包括带有粉色丝带蝴蝶结的白色渔网袜、柔顺的金发，以及现代卧室环境中柔和的自然日光。

![Coquette 风格卧室姿势（抬腿）](https://cms-assets.youmind.com/media/1768319191966_v1p3qg_G-cfTmPXAAA_Haf.jpg)
![Coquette 风格卧室姿势（抬腿）](https://cms-assets.youmind.com/media/1768319191901_wxvn9t_G-cfTmNXUAAKTNl.jpg)

```
{
  "scene": "indoor bedroom, lying on back pose, legs raised, looking at camera",
  "subject": {
    "character": "YOUNG WOMAN, blonde hair, slender frame",
 
    "face": {
      "structure": "soft delicate features, youthful",
      "skin": "fair porcelain, natural clear",
      "eyes": {
        "shape": "large",
        "color": "blue/green",
        "expression": "direct gaze at camera, soft neutral expression"
      },
      "mouth": {
        "lips": "full, natural pink, relaxed"
      },
      "makeup": "minimal natural, barely there"
    },
    
    "hair": {
      "color": "BLONDE",
      "length": "long",
      "texture": "soft waves, voluminous",
      "style": "loose, resting on pillow",
      "shine": "healthy shine, silky",
      "visible": "fully visible"
    },
    
    "accessories": {
      "hat": null,
      "bag": null
    }
  },

  "pose": {
    "overall": "lying on back on bed, legs raised vertically",
    
    "position": {
      "base": "lying flat on white linen bed",
      "orientation": "face up, body aligned vertically"
    },
    
    "legs": {
      "position": "raised straight up into the air",
      "thighs": "vertical",
      "feet": "pointed towards the ceiling"
    },
    
    "hips": {
      "position": "flat on the bed",
      "emphasis": "neutral"
    },
    
    "torso": {
      "direction": "facing up",
      "back": "on the mattress",
      "twist": "none"
    },
    
    "arms": {
      "position": "resting on chest, holding a {argument name="item held" default="white rose"}"
    },
    
    "head": {
      "turn": "facing straight up at camera",
      "expression": "soft, calm, direct gaze"
    }
  },

  "outfit": {
    "top": {
      "type": "white ribbed crop top",
      "style": "short sleeve, fitted",
      "color": "white",
      "back": "covered"
    },
    
    "bottom": {
      "type": "white fishnet tights",
      "wash": null,
      "fit": "tight",
      "details": "cutouts along the side of legs held by small pastel pink ribbon bows",
      "style": "coquette aesthetic"
    },
    
    "shoes": {
      "type": "none",
      "style": null,
      "color": null
    }
  },

  "body": {
    "type": "slender",
    "back": "on bed",
    "skin": "fair"
  },

  "environment": {
    "location": "indoor, modern bedroom",
    
    "background": {
     "wall": "dark grey concrete finish",
     "headboard": "textured grey upholstered"
    },
    
    "ground": {
      "surface": "bed with white linen bedding",
    }
  },

  "lighting": {
    "type": "soft natural daylight",
    
    "quality": {
      "intensity": "soft, diffused, even",
      "mood": "gentle, intimate"
    },
    
    "on_subject": {
      "skin": "soft even lighting from the left",
      "hair": "illuminated from the side"
    }
  },

  "photography": {
    "angle": "medium shot, vertical orientation, looking down slightly",
    "framing": "full body on bed"
  }
}
```

[[Fashion Portrait]] [[Coquette Aesthetic]]

---

### 81. 雨中街头的电影感时尚肖像

**Author**: [Hoor](https://x.com/hoor_world06)  **Date**: 2026-01-11  **Language**: en

> 一个简短、结构化的提示，用于生成一张叙事性的电影时尚肖像：一位女性穿着时尚的海军蓝色风衣，自信地走在湿漉漉的城市街道上。提示强调了环境细节，如倒影、霓虹灯和雨滴。

![雨中街头的电影感时尚肖像](https://cms-assets.youmind.com/media/1768226013068_ezoxs0_G-ZGpl6a8AA1FDx.jpg)

```
{
  "render_goal": "Narrative cinematic fashion portrait",
  "subject": {
    "pose": "female walking, holding umbrella, relaxed stride",
    "expression": "playful confident smirk"
  },
  "wardrobe": "sleek navy trench coat with leather boots",
  "environment": {
    "location": "glossy wet city street",
    "props": "reflections on pavement, neon lights, raindrops"
  }
}
```

[[Fashion Portrait]] [[Neon Reflection]]

---

### 82. 奢华酒店时尚肖像提示，附 Kuromi 夹子

**Author**: [AI Tales - Not by Humans](https://x.com/AITalesNBH)  **Date**: 2026-01-10  **Language**: en

> 一个为 Nano Banana Pro 设计的超写实时尚肖像提示词，描绘了一位留着凌乱盘发的姜金色头发女性，身穿紧身灰粉色天鹅绒迷你连衣裙，佩戴一个迷你黑色库洛米 (Kuromi) 发夹，置身于一间拥有温暖电影感灯光的豪华酒店卧室中。

![奢华酒店时尚肖像提示，附 Kuromi 夹子](https://cms-assets.youmind.com/media/1768143851531_p4oouy_G-UfMswWMAAbODn.jpg)

```
Use the same face from the reference image without changing any facial features.

A photorealistic fashion portrait of a beautiful young western woman with fair skin and long ginger-blonde hair styled in a voluminous messy updo bun. She has large light blue-green eyes, dramatic long eyelashes, sharp winged eyeliner, and glossy pink-peach lips. She wears a tiny black {argument name="hair clip brand" default="Kuromi"} hair clip with purple accents, a delicate crescent moon tattoo on her upper chest, and a small heart-shaped pendant necklace.

She is dressed in a tight off-shoulder dusty-rose pink velvet minidress with a ruched twisted bust, very low neckline, deep cleavage, short puff sleeves, fisnhets, and a form-fitting bodycon silhouette. She poses sensually with one hand gently touching her neck and cheek, looking slightly upward with a dreamy, seductive expression.

The scene is set in {argument name="hotel name" default="burj al arab"} luxury hotel bedroom with dark walls, subtle mirror reflections, soft fog in the air, and warm cinematic lighting with golden rim light. Shallow depth of field, soft bokeh background, ultra-detailed realistic skin texture, high-end makeup, sharp focus, shot on an 85mm lens, RAW photo, 8k quality.
```

[[Fashion Portrait]] [[Bedroom Setting]] [[Warm Cinematic Lighting]]

---

### 83. 柔美少女风田园时尚肖像

**Author**: [Iris](https://x.com/xIrissy)  **Date**: 2026-01-10  **Language**: en

> 一个详细的 JSON 提示，用于生成一张具有柔和的 Coquette/Cottagecore 美学风格的超逼真时尚肖像。它详细说明了拍摄对象的形象、服装（复古碎花迷你连衣裙）、姿势、环境（奢华内饰）和技术细节（8k 分辨率、柔和照明、电影构图）。

![柔美少女风田园时尚肖像](https://cms-assets.youmind.com/media/1768225972771_fnshnw_G-UOveEbMAADa2a.jpg)
![柔美少女风田园时尚肖像](https://cms-assets.youmind.com/media/1768225974079_4svyj7_G-UOveEacAASRmD.jpg)

```
{
  "prompt_type": "Soft Coquette / Cottagecore Fashion Portrait",
  "subject": {
    "demographics": "Young woman",
    "appearance": {
      "skin": "Fair to medium complexion, smooth texture, soft natural glow",
      "hair": "Long, layered dark blonde / bronde hair with lighter highlights, styled in loose, voluminous waves framing the face",
      "face": "Soft, feminine features, gentle smile, head tilted slightly to the side",
      "makeup": "Natural 'no-makeup' glam, rosy cheeks, nude-pink lips, defined lashes"
    },
    "pose": {
      "stance": "Standing playful pose",
      "hands": "Hidden behind the back",
      "body_language": "Shy yet confident, sweet and approachable"
    }
  },
  "fashion": {
    "garment": {
      "item": "Vintage-inspired floral mini dress",
      "color_palette": "Butter yellow base with delicate white and green floral print",
      "silhouette": "Fit-and-flare / Skater dress style",
      "details": [
        "Puff cap sleeves",
        "Deep V-neckline",
        "Corset-style bodice structure",
        "Voluminous, pleated mini skirt",
        "Tulle underlayer peaking out slightly for volume"
      ]
    },
    "aesthetic": "Coquette, Cottagecore, Soft Girl, Princess-core"
  },
  "environment": {
    "location": "Classic luxury interior / Hotel room or Boutique",
    "background_elements": {
      "walls": "Cream-colored walls with decorative molding / wainscoting",
      "curtains": "Heavy, floor-length beige/gold drapes with gathered fabric texture",
      "fixtures": "White electrical outlets visible on the wall (adding realism)"
    },
    "atmosphere": "Elegant, warm, intimate"
  },
  "lighting": {
    "type": "Soft indoor ambient light",
    "quality": "Diffused, flattering, warm undertones",
    "direction": "Side lighting coming from the window (near the curtains)"
  },
  "camera_settings": {
    "shot_type": "Medium-full shot (thigh-up)",
    "perspective": "Eye-level",
    "focus": "Sharp focus on the subject and dress texture",
    "depth_of_field": "Slightly shallow to separate subject from the wall"
  },
  "technical_details": {
    "resolution": "8k",
    "quality_tags": [
      "Ultra Photorealistic",
      "High-detail fabric texture",
      "Soft lighting",
      "Unreal Engine 5 render style",
      "Cinematic composition"
    ]
  }
}
```

[[Fashion Portrait]] [[Soft Lighting]] [[Cinematic Composition]] [[Luxury Interior]]

---

### 84. 高级时装编辑肖像照，带尘埃颗粒

**Author**: [Hoor](https://x.com/hoor_world06)  **Date**: 2026-01-10  **Language**: en

> 一个简洁的提示，用于生成一张时尚、特写、编辑风格的肖像照。画面聚焦于一位表情沉着、优雅的女性，她身着柔和的象牙色高级定制领口服装，置身于一个温暖的影棚环境中，细小的半透明尘埃颗粒在她脸庞附近轻轻飘浮。

![高级时装编辑肖像照，带尘埃颗粒](https://cms-assets.youmind.com/media/1768143833905_l3ph8y_G-TAN9abMAAaqZ2.jpg)

```
{
  "render_goal": "High-fashion close-up editorial portrait",
  "subject": {
    "pose": "female close-up with relaxed shoulders",
    "expression": "composed elegant smile"
  },
  "wardrobe": "clean couture neckline in soft ivory",
  "environment": {
    "location": "studio with warm lighting",
    "props": "fine translucent dust particles floating gently near face"
  }
}
```

[[Fashion Portrait]]

---

### 85. 空灵瀑布自拍肖像，带自然瑕疵

**Author**: [Lex](https://x.com/katmanai)  **Date**: 2026-01-08  **Language**: en

> 一个详细的 JSON 提示，用于生成一张年轻女性在瀑布旁自拍的超逼真时尚肖像。该提示强调空灵之美、铂金色头发、冰蓝色眼睛，并要求逼真的皮肤纹理，带细微瑕疵，同时使用特定的相机和光照细节。

![空灵瀑布自拍肖像，带自然瑕疵](https://cms-assets.youmind.com/media/1767967390547_tgdt53_G-KznTaXoAA9f6l.jpg)

```
{
  "prompt": "Close-up selfie portrait of a young woman, 18-22 years old, ethereal and delicate beauty, very pale porcelain skin with subtle natural freckles, striking icy blue eyes, intense direct gaze straight at camera, soft melancholic expression, full lips with natural pinkish tone slightly parted, long wavy platinum blonde hair with natural messy voluminous texture, strands falling over face and shoulders, golden hour soft diffused natural lighting, shallow depth of field, cinematic bokeh, detailed skin texture with tiny imperfections and pores, realistic photography style, shot on high-end mirrorless camera, 85mm lens, f/1.4, ultra detailed, 8k resolution",
  "negative_prompt": "cartoon, anime, drawing, painting, illustration, deformed, blurry, low resolution, overexposed, underexposed, plastic skin, heavy makeup, eyeliner, mascara, lipstick, filters, beauty filter, smooth skin without pores, extra limbs, distorted face, asymmetrical eyes, ugly, bad anatomy, text, watermark, logo, crowded background",
  "reference_image": {
    "enabled": true,
    "strength": 0.75,
    "description": "Use the provided reference image as strong style and facial feature guide: young woman with long wavy blonde hair, blue eyes, natural look, outdoor nature waterfall background, black fuzzy jacket over white top with red checkered trim, selfie angle slightly from above"
  },
  "style": "photorealistic fashion portrait",
  "aspect_ratio": "9:16",
  "lighting": "soft natural daylight, gentle shadows, mossy green and rocky waterfall backdrop",
  "camera": "shot with Sony A7R IV, 85mm prime lens at f/1.8, natural ambient light",
  "additional_details": [
    "wearing oversized dark charcoal black fleece jacket with visible texture",
    "white cropped top underneath with small red-white gingham checkered frill trim visible at neckline",
    "background: lush green moss-covered rocks, small waterfall cascading down, natural forest stream setting, ferns and greenery",
    "hair: very long, voluminous, slightly wet-looking ends from environment humidity, natural waves and flyaways",
    "expression: calm, slightly serious/introspective, subtle pout, direct eye contact",
    "no heavy editing, keep realistic skin texture and minor imperfections"
  ],
  "seed": "random or fixed for consistency if needed",
  "cfg_scale": 7.5,
  "steps": 35
}
```

[[Fashion Portrait]]

---

### 86. 巨型泰迪熊时尚大片提示

**Author**: [Shanvi](https://x.com/Skurmii)  **Date**: 2026-01-06  **Language**: en

> 一个高度详细的 JSON 提示，用于生成逼真的时尚杂志摄影棚照片。它要求保留参考图像中的面部特征，指定拍摄对象的姿势（侧身坐着，抱着一个道具），服装（来自第二张参考图像中的确切服装，高跟鞋），以及道具本身：一个巨大的、150 厘米高的泰迪熊，所有这些都设置在无缝的纯粉色背景下，并采用高调照明。

![巨型泰迪熊时尚大片提示](https://cms-assets.youmind.com/media/1767804033190_xbl4k0_G98wvEMbcAQxw7q.jpg)

```
{
  "prompt_type": "image_generation",
  "image_style": "realistic fashion editorial, DSLR studio photography",
  "camera": {
    "type": "professional full-frame DSLR",
    "lens": "85mm prime",
    "aperture": "f/5.6",
    "iso": 100,
    "shutter_speed": "1/160s",
    "white_balance": "5000-5200K (warm studio tone)"
  },
  "framing": {
    "shot_type": "full body",
    "camera_angle": "eye-level, neutral perspective"
  },
  "subject": {
    "identity": {
      "use_reference_image": true,
      "preserve_facial_identity": true
    },
    "expression": "calm, confident, relaxed facial muscles",
    "face_angle": "three-quarter view toward the camera",
    "gaze": "direct eye contact with the camera",
    "pose": {
      "body_position": "seated sideways",
      "torso_rotation": "approximately 45 degrees toward the camera",
      "legs": {
        "front_leg": "extended forward",
        "back_leg": "bent and slightly elevated"
      },
      "weight_distribution": "resting on the hip"
    },
    "hands": {
      "right_arm": "wrapped around a large object at chest height",
      "left_hand": "resting gently on the object"
    }
  },
  "wardrobe": {
    "outfit": "exact outfit from the second provided reference image",
    "shoes": "closed-toe high heels with glossy finish and thin stiletto heel"
  },
  "hair": {
    "style": "loose hair with soft, controlled waves",
    "finish": "clean, smooth, no frizz"
  },
  "makeup": {
    "style": "editorial glamorous makeup, medium-to-high visual impact",
    "skin": "even tone with natural glow",
    "eyebrows": "defined",
    "eyes": {
      "eyeshadow": "pink eyeshadow extended above the crease",
      "eyeliner": "subtle",
      "mascara": "defined lashes"
    },
    "contour": "soft contouring",
    "lips": "satin finish, natural pink tone"
  },
  "manicure": {
    "nails": "almond-shaped, medium length",
    "finish": "glossy pink"
  },
  "environment": {
    "background": "seamless solid {argument name="background color" default="pink"} studio backdrop",
    "floor_to_background_transition": "smooth and continuous"
  },
  "lighting": {
    "style": "high-key studio lighting",
    "key_light": {
      "position": "front, slightly above eye level",
      "quality": "large, diffused"
    },
    "fill_light": "uniform frontal fill",
    "shadows": "extremely soft"
  },
  "props": {
    "object": "giant seated teddy bear",
    "scale": {
      "height": "approximately 150 cm",
      "width": "approximately 110 cm",
      "comparison": "similar in size to a large single-seat sofa"
    }
  },
  "effects": {
    "filters": "none",
    "post_processing": "none"
  },
  "output_quality": {
    "resolution": "high resolution",
    "realism": "photorealistic",
    "genre": "fashion editorial studio photography"
  }
}
```

[[Fashion Portrait]] [[Studio Photography]] [[High Key Lighting]]

---

### 87. 戏剧性低调单色肖像提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-06  **Language**: en

> 一个用于生成戏剧性、高对比度黑白肖像的提示，背景为低调工作室，强调明暗对比照明。它指定了构图（特写、垂直）、姿势（用张开的手指部分遮盖脸部）和技术细节（85mm 镜头、f/2 光圈、胶片颗粒叠加），以营造一种情绪化、时尚杂志般的黑色电影氛围。

![戏剧性低调单色肖像提示](https://cms-assets.youmind.com/media/1767804013829_y4lxiq_G98vCOYbcAETm4P.jpg)
![戏剧性低调单色肖像提示](https://cms-assets.youmind.com/media/1767804014511_ot1as7_G98u_dzbcAA_ZH_.jpg)

```
Portrait Of A Person From Input Photo In A Dramatic Low-key Studio Setting, Framed Vertically In A Tight Close-up From Upper Chest To Just Above The Beanie, Background Falling Into Pure Matte Black (#000000) The Subject Faces Camera, But Turns Slightly So Only One Eve Is Visible, Raising One Hand To Partially Cover The Face With Spread Fingers, The Visible Eye Staring Intensely Through The Gap While The Rest Of The Face Disappears Into Shadow; Expression Serious And Enigmatic Style Them In A Ribbed Knit Beanie And Simple Dark T-shirt For Subtle Detail Light The Scene With A Single Hard, Focused Key Light From High Camera-right, Cool-neutral (-5200k But Rendered In Monochrome), Carving Sharp Highlights Along The Lit Side Of The Beanie, Fingers, Eye Cheekbone, And Rim Of The Ear, While The Opposite Side Of The Face And Background Fall Into Deep Shadow For Extreme Contrast And Strong Chiaroscuro Shoot With An {argument name="lens focal length" default="85mm"} Lens At Around {argument name="aperture" default="F/2"}, Keeping The Eye And Top Of The Hand Crisply In Focus While The Rest Gently Softens, Emphasizing Skin Texture, Fabric Grain Of The Beanie, And Fine Stubble With A Delicate Film-grain Overlay Convert To Rich Black-and-white With Deep Blacks And Luminous Midtones For A Moody, Fashion-editorial, Almost Noir Atmosphere Editorial Modern, High-detail, Cinematic Composition, Ultra-realistic Textures, Professional Fashion Photography Style
```

[[Fashion Portrait]] [[Chiaroscuro Lighting]] [[85mm Lens]] [[Film Noir]]

---

### 88. 庭院花园中的静奢时尚肖像

**Author**: [Hoor](https://x.com/hoor_world06)  **Date**: 2026-01-05  **Language**: en

> 一个提示，旨在生成一张以“静奢风”为主题的女性时尚肖像。它指定了在阳光漂白的园墙前摆出放松的姿势，身穿结构感丝绸礼服，强调柔和的对比和画报般的构图。

![庭院花园中的静奢时尚肖像](https://cms-assets.youmind.com/media/1767682106118_fyczun_G95vsm2bgAAGi9b.jpg)

```
{
  "render_goal": "Quiet luxury fashion portrait",
  "subject": {
    "pose": "female leaning lightly against a sun-bleached garden wall",
    "expression": "relaxed, understated smile"
  },
  "wardrobe": "structured silk gown in {argument name="gown color" default="warm off-white"}, clean neckline",
  "environment": {
    "location": "courtyard garden with aged stone walls",
    "props": "subtle wall texture, natural shadows"
  },
  "camera_style": "editorial composition, soft contrast"
}
```

[[Fashion Portrait]] [[Quiet Luxury Aesthetic]] [[Garden Setting]]

---

### 89. 高级时装多重曝光肖像提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-05  **Language**: en

> 一个用于创建电影感、时尚半身像的提示，具有梦幻般的杂志风格。它利用多重曝光模糊来产生重影效果和垂直条纹，背景是蓝色渐变，高对比度照明营造出超现实、未来主义的数字青年美学。

![高级时装多重曝光肖像提示](https://cms-assets.youmind.com/media/1767682136070_1o1i53_G94K06gbgAATq7Q.jpg)
![高级时装多重曝光肖像提示](https://cms-assets.youmind.com/media/1767682136189_ht2fc7_G94KI8GbsAAJBu_.jpg)

```
Create a cinematic, high-fashion half-length portrait from the input photo with a dreamy editorial vibe. Use multi-exposure blur for ghosting and vertical streaks. Set against a blue gradient background (#0033A0 to #66CCFF), the subject wears an oversized white T-shirt. Apply high-contrast lighting (cool blue wash + orange/yellow edge highlights) for a futuristic glow. Expression: neutral/introspective, eyes softly lit. Simulate 50-85mm lens at f/1.8 with shallow depth of field. Enhance with motion blur and chromatic separation, keeping central details sharp. Aim for a surreal, digital-youth mood blending minimalism and light play.
```

[[Fashion Portrait]] [[Blue Gradient Background]]

---

### 90. 惊艳时尚摄影提示

**Author**: [blogbursthub](https://x.com/blogbursthub)  **Date**: 2025-12-31  **Language**: en

> 一个用于使用 Gemini Nano Banana 生成令人惊艳的时尚照片的提示，重点关注高质量的视觉元素和风格。该提示位于推文的替代文本中。

![惊艳时尚摄影提示](https://cms-assets.youmind.com/media/1767456269423_361w08_G9dW2HkaoAAcrtB.jpg)

```
A stunning, high-fashion editorial photograph of a female model. The model is wearing a dramatic, voluminous gown made of iridescent, deep emerald green silk. The gown features exaggerated ruffles and a long train, catching the light dynamically. She is standing on a polished, obsidian floor in a minimalist, brutalist architectural space. The lighting is dramatic, using hard side-lighting to emphasize the texture of the silk and create deep, sharp shadows. The model has a strong, direct gaze and minimal, avant-garde makeup. Shot on a medium format film camera, ultra-high resolution, cinematic color grading, 8k.
```

[[Fashion Portrait]]

---

### 91. 时尚人像与蝴蝶翅膀壁画

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2025-12-30  **Language**: en

> 一个详细的 Gemini Nano Banana Pro 提示，用于生成一张年轻女性的时尚肖像。她身着休闲装（粉色衬衫系在腰间，搭配牛仔裤），背景是一面绘有巨大黑色蝴蝶翅膀的墙壁壁画。构图旨在通过柔和、漫射的灯光和干净、时尚的美学，营造出一种天使般或蜕变般的幻觉。

![时尚人像与蝴蝶翅膀壁画](https://cms-assets.youmind.com/media/1767455077522_qql0xc_G9bPn2Ha8AAYaZu.jpg)

```
{ "composition": { "framing": "vertical portrait, mid-thigh to head", "subject_placement": "centered, symmetrical alignment", "pose": "front-facing, both hands raised touching hair near temples", "visual_balance": "strong bilateral symmetry created by butterfly wings aligned behind subject", "perspective": "eye-level camera angle", "crop_style": "fashion/editorial portrait crop" }, "subject": { "type": "human female", "approx_age": "young adult", "expression": "soft smile, relaxed and confident", "gaze": "direct eye contact with camera", "skin_tone": "light to medium warm undertone", "body_language": "open, confident, styled pose" }, "hair": { "color": " dark brown", "style": "messy top bun with loose face-framing strands", "texture": "smooth with soft flyaways", "finish": "natural sheen" }, "facial_features": { "makeup_style": "soft glam", "eyes": "defined brows, neutral eyeshadow, eyeliner, mascara", "cheeks": "rosy blush", "lips": "matte or satin nude-pink lipstick", "overall_finish": "polished yet natural" }, "wardrobe": { "top_layer": { "item": "button-down shirt", "color": "light pastel pink", "fit": "relaxed", "styling": "open front, tied knot at waist" }, "inner_top": { "item": "crop tank top", "color": "white", "fit": "fitted" }, "bottom": { "item": "jeans", "color": "medium blue denim", "fit": "high-waisted, fitted" }, "style_category": "casual fashion with feminine styling" }, "background": { "type": "painted wall mural", "design": "large black butterfly wings", "color_palette": "black wings on white wall", "interaction_with_subject": "wings positioned to appear attached to subject", "texture": "flat painted surface" }, "color_palette": { "primary_colors": ["soft pink", "white", "black"], "secondary_colors": ["blue denim", "warm skin tones"], "overall_mood": "light, feminine, clean" }, "lighting": { "type": "soft natural or diffused studio light", "direction": "front-facing, even illumination", "shadows": "minimal, soft shadows", "contrast": "low to moderate", "skin_rendering": "smooth and flattering" }, "technical_traits": { "focus": "sharp focus on subject", "depth_of_field": "moderate, background still clear", "image_quality": "high resolution, clean detail", "noise": "minimal to none" }, "artistic_elements": { "visual_metaphor": "angelic or butterfly-wing illusion", "aesthetic_style": "modern lifestyle portrait with whimsical element", "theme": "femininity, confidence, transformation" }, "typography": { "presence": "none" }, "overall_style_summary": { "genre": "fashion portrait photography", "tone": "bright, approachable, stylish", "usage_fit": ["social media content", "UGC influencer imagery", "fashion branding", "lifestyle marketing"] } }
```

[[Fashion Portrait]] [[Diffused Lighting]]

---

### 92. 2026 新年高分辨率逼真影棚时尚肖像

**Author**: [Adam也叫吉米](https://x.com/Adam38363368936)  **Date**: 2025-12-29  **Language**: en

> 一个详细、结构化的图像生成提示，用于创建一张高分辨率、超逼真的影棚时尚肖像。主体是一位庆祝 2026 年新年的成年女性，其中包含表情、服装、道具（20 和 26 形状的金色箔气球）的特定细节，以及精确的影棚灯光和纹理要求。

![2026 新年高分辨率逼真影棚时尚肖像](https://cms-assets.youmind.com/media/1767166992932_c7bmil_G9VdWgsbMAAIiFw.jpg)

```
{
Use the face without any change.
  "type": "image_prompt",
  "description": "High-resolution photorealistic studio fashion portrait",
  "subject": {
    "gender": "adult woman",
    "hair": "long light brown hair with golden blonde highlights, loose curls",
    "expression": "{argument name="expression" default="playful, cheeky, thinking face, lips pursed"}",
    "pose": "looking off to the side, shoulders relaxed"
  },
  "outfit": {
    "hat": "gold shimmering party hat",
    "dress": "{argument name="outfit" default="gold sequin party dress with modern asymmetric neckline cutout"}"
  },
  "props": {
    "balloons": "gold foil balloons shaped as numbers 20 and 26, one in each hand, raised near shoulders"
  },
  "environment": {
    "setting": "clean studio",
    "background": "neutral beige backdrop",
    "lighting": "soft studio lighting with gentle shadows"
  },
  "details": {
    "realism": "editorial-quality photorealism",
    "textures": "visible skin texture, detailed hair strands, sharp sequin detail",
    "materials": "metallic balloon shine with realistic creases and highlights"
  },
  "constraints": [
    "no text",
    "no logos",
    "no branding",
    "no watermarks"
  ]
}
```

[[Fashion Portrait]] [[Studio Photography]] [[Glamour Photography]] [[Holiday Theme]]

---

### 93. 波斯地毯风格肖像提示

**Author**: [simply](https://x.com/kingofdairyque)  **Date**: 2025-12-29  **Language**: en

> 生成一张年轻女孩超写实肖像的提示词，胸部以上构图，适合社交媒体。图片中，主体身着波斯地毯图案连衣裙，怀抱一只波斯猫，置身于奢华的波斯红地毯背景中，并辅以戏剧性的侧光。

![波斯地毯风格肖像提示](https://cms-assets.youmind.com/media/1767166919626_tc3izn_G9TYzbHaEAAXCHf.jpg)

```
A 4K ultra-realistic portrait of a young girl, framed from the chest up (not full body), designed for Instagram story or profile picture. The background is a luxurious {argument name="carpet design" default="Persian red carpet design"} (only behind her, not on the ground). Sunlight shines from one side,casting natural warm light across half of her face. She is wearing an elegant dress inspired by Persian carpet patterns,with authentic Iranian colors and motifs. Her facial features remain unchanged.She is holding a {argument name="animal" default="Persian cat"} in her hands
```

[[Fashion Portrait]] [[Dramatic Side Lighting]] [[Cultural Fashion]]

---

### 94. 写实天鹅绒连衣裙肖像

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2025-12-28  **Language**: en

> 一个高度结构化的提示，用于生成一张年轻女性的超写实肖像，她身穿深勃艮第色天鹅绒露肩连衣裙，坐在一张华丽的花卉大马士革高背椅中，强调丰富的纹理和柔和的自然光线。

![写实天鹅绒连衣裙肖像](https://cms-assets.youmind.com/media/1767061766539_4ukl2x_G9P-tW5aQAAjYSB.jpg)
![写实天鹅绒连衣裙肖像](https://cms-assets.youmind.com/media/1767061766807_zyf405_G9P-tX4agAEcGOa.jpg)

```
{
  "image_type": "photorealistic portrait",
  "resolution": "8K ultra high definition",
  "aspect_ratio": "vertical portrait",
  "camera_perspective": {
    "framing": "mid-length portrait",
    "angle": "slightly elevated eye-level angle",
    "focus": "sharp focus on subject, background slightly softer"
  },
  "subject": {
    "gender": "female",
    "age_appearance": "young adult",
    "skin_tone": "fair, smooth, even complexion",
    "facial_features": {
      "face_shape": "oval",
      "eyes": {
        "color": "light blue-grey",
        "expression": "calm, introspective, distant gaze",
        "direction": "looking slightly to her left (viewer’s right)"
      },
      "eyebrows": "natural, medium thickness, softly arched",
      "nose": "slim, straight",
      "lips": {
        "color": "soft natural pink",
        "expression": "neutral, relaxed"
      }
    },
    "hair": {
      "color": "medium brown",
      "texture": "soft, slightly wavy",
      "style": "loosely tied low bun with fine strands framing the face",
      "finish": "natural, matte"
    }
  },
  "pose_and_body_language": {
    "position": "seated",
    "posture": "relaxed, slightly leaning back into chair",
    "shoulders": "gently angled",
    "arms": "both arms resting on lap",
    "hands": {
      "position": "fingers loosely interlaced",
      "detail": "natural nails, no visible nail polish"
    }
  },
  "clothing": {
    "dress_type": "off-shoulder evening dress",
    "fabric": "velvet",
    "color": "{argument name="dress color" default="deep burgundy / wine red"}",
    "texture_detail": "rich velvet sheen with visible light absorption and soft highlights",
    "design_details": {
      "neckline": "off-shoulder with thin straps",
      "bodice": "pleated vertical gathers",
      "waist": "fitted with horizontal ruching",
      "decorative_element": "fabric rose on left shoulder strap",
      "skirt": "flowing, smooth velvet drape extending downward"
    }
  },
  "accessories": {
    "necklace": {
      "type": "delicate chain",
      "pendant": "small heart-shaped pendant",
      "material": "gold-toned"
    },
    "bracelet": {
      "wrist": "right wrist",
      "style": "thin chain bracelet",
      "material": "gold-toned"
    },
    "earrings": {
      "type": "small stud earrings",
      "color": "pearl white"
    }
  },
  "chair": {
    "type": "wingback armchair",
    "upholstery": {
      "pattern": "ornate floral damask",
      "colors": [
        "beige base",
        "muted gold",
        "soft pink",
        "olive green"
      ],
      "texture": "woven fabric with visible pattern depth"
    },
    "contrast": "enhanced contrast making floral patterns prominent"
  },
  "environment": {
    "setting": "indoor",
    "background": {
      "wall": "light-colored vertical paneling",
      "visibility": "partially visible behind chair",
      "detail_level": "minimal, clean"
    }
  },
  "lighting": {
    "type": "soft natural light",
    "direc
```

[[Fashion Portrait]] [[Soft Natural Light]]

---

### 95. 高品质波点时尚肖像

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2025-12-28  **Language**: en

> 一个结构化的提示，用于生成一张高质量、风格化的年轻女性时尚肖像，其服装和配饰均采用一致的黑白波点主题，置身于室内休息室，并配以柔和的影棚灯光。

![高品质波点时尚肖像](https://cms-assets.youmind.com/media/1767061760365_rb2ki2_G9OGQGDXQAAtNbN.jpg)

```
{
  "image_description": "A high-quality portrait of a young woman with a glamorous, stylized aesthetic, featuring a consistent black and white polka dot theme.",
  "subject": {
    "pose": "Sitting on a neutral-toned couch, leaning forward slightly with legs crossed at the knees and arms resting on her lap; one hand is elegantly touching the frame of her glasses.",
    "features": "Long, straight honey-blonde hair with face-framing highlights, styled into two small 'space buns' on top. Glamorous makeup with sharp winged eyeliner, heavy lashes, rosy blush, and glossy red lips. Long, pointed acrylic nails with a nude/brown gradient.",
    "attire": "A black and white polka dot mini dress, a matching oversized polka dot bow tie worn as a choker over a pearl necklace, and a matching polka dot bow in her hair."
  },
  "accessories": "Frameless, rectangular rimless glasses with decorative silver/diamond accents on the bridge and hinges.",
  "environment": {
    "setting": "Indoor lounge or living area with a soft, warm-toned gray wall in the background.",
    "lighting": "Soft, direct studio-style lighting that creates a gentle shadow against the back wall and highlights the textures of the fabric and makeup.",
    "color_palette": "Dominated by monochromatic black and white patterns, complemented by warm skin tones, honey-blonde hair, and a pop of {argument name="lip color" default="red"} from the lipstick."
  },
  "technical_style": "High-resolution fashion photography, shallow depth of field, sharp focus on facial features and accessories, smooth skin texture."
}
```

[[Fashion Portrait]] [[Studio Photography]] [[Soft Studio Lighting]]

---

### 96. 老钱风美学：身着小黑裙的女性在宏伟楼梯上

**Author**: [Iris](https://x.com/xIrissy)  **Date**: 2025-12-27  **Language**: en

> 一个用于生成“老钱风”或巴黎时尚美学风格照片的详细提示。画面中，一位身材苗条的女士身着小黑裙，戴着透明歌剧手套和珍珠首饰，在一个带有华丽锻铁栏杆的宏伟室内楼梯上摆姿势，在温暖柔和的人造灯光下被捕捉。

![老钱风美学：身着小黑裙的女性在宏伟楼梯上](https://cms-assets.youmind.com/media/1766987657494_ukf2lk_G9MDxydbQAE6xQf.jpg)

```
{
  "image_analysis_prompt": {
    "subject": {
      "demographics": "Young woman, slender build, light skin tone",
      "hair": "Dark brunette, styled in a sleek, tight low bun with a middle part",
      "expression": "Neutral, elegant, looking off-camera to her right"
    },
    "apparel": {
      "dress": "Little black dress (LBD), mini length, sleeveless straps, sweetheart neckline, fitted bodice with a flared skater-style skirt",
      "legwear": "Sheer black tights (pantyhose)",
      "footwear": "Black patent pointed-toe heels with gold hardware accents",
      "gloves": "Sheer black opera-length gloves"
    },
    "accessories": {
      "jewelry": [
        "Single-strand pearl choker necklace",
        "Large pearl stud earrings"
      ],
      "handbag": "Small, black quilted leather handbag (reminiscent of Chanel) held in the right hand"
    },
    "pose_and_action": {
      "stance": "Standing on a staircase landing, legs crossed at the ankles",
      "hands": "Right hand resting on the banister holding the bag, left hand gently lifting the edge of the dress skirt",
      "orientation": "Body facing forward, head turned in profile to the left"
    },
    "environment": {
      "location": "Grand interior staircase (possibly a hotel or chateau)",
      "architectural_details": [
        "Curved cream stone walls",
        "Ornate black wrought-iron railing with elaborate gold leaf scrollwork",
        "Polished gold handrail",
        "Red and beige patterned stair runner carpet"
      ],
      "background_decor": [
        "Classic oil painting in a gold frame hanging on the upper wall",
        "Antique wooden chest/commode visible on the upper landing",
        "Brass wall sconce with candle-style bulbs"
      ]
    },
    "lighting_and_style": {
      "lighting": "Warm, soft indoor artificial lighting creating gentle shadows",
      "aesthetic": "Old Money, Parisian chic, luxury, formal, elegant, high-class fashion"
    }
  }
}
```

[[Fashion Portrait]] [[Old Money Aesthetic]] [[Opera Gloves]]

---

### 97. 优雅肖像生成提示

**Author**: [Abbay](https://x.com/LearnWithAbbay)  **Date**: 2025-12-21  **Language**: en

> 一个结构化的提示，用于生成一张年轻女性的图像，她姿态优雅、沉着地站在玻璃栏杆旁，重点突出其细致的外貌、服装和表情。

![优雅肖像生成提示](https://cms-assets.youmind.com/media/1766489481672_5o9t2p_G8lxxmfasAAFTiE.jpg)

```
{
  "subject": {
    "person": "{argument name="person description" default="Young woman, early 20s, Caucasian"}",
    "hair": "{argument name="hair style" default="Soft ash-blonde hair, loose waves with natural movement, slightly wind-blown"}",
    "pose": "{argument name="pose" default="Standing near glass railing, torso angled slightly right, gaze off-camera left"}",
    "expression": "{argument name="expression" default="Composed, calm, subtle elegant smile"}"
  },
  "outfit": {
    "top": "{argument name="top outfit" default="Ivory off-shoulder fitted knit top with clean neckline"}",
    "bottoms": "{argument name="bottom outfit" default="High-waisted beige tailored trousers"}"
  }
}
```

[[Fashion Portrait]] [[Outdoor Lifestyle Photography]]

---

### 98. 香槟杯秋千椅上的休闲肖像

**Author**: [Sienna](https://x.com/siennalovesai)  **Date**: 2025-12-11  **Language**: en

> 生成一张肖像画的提示词：一位女士优雅地坐在一间私人休息室的透明亚克力香槟杯秋千椅上。提示词要求 AI 精确匹配附件图片中人物的面部特征，并指定她的着装（露背深红色缎面礼服）以及深红色和金色霓虹灯光。

![香槟杯秋千椅上的休闲肖像](https://cms-assets.youmind.com/media/1765967664571_16n37x_G76AungXIAAJUha.jpg)

```
A 20-year-old woman (matching the attached subjects facial features exactly, only polishing to match the theme of the prompt) with sleek auburn hair in a low chignon, wearing a backless {argument name="dress color" default="crimson"} satin gown with a thigh-high slit, crystal heels dangling from her toes. She sits elegantly in a clear acrylic champagne coupe swing chair, one finger tracing the rim of a glass, gazing with quiet intensity off-camera. The private lounge glows deep red and gold neon, creating an intoxicating, exclusive mood. Keep the face 100% exact same as I uploaded no alteration
```

[[Fashion Portrait]] [[Neon Lighting]] [[Glamour Photography]]

---

### 99. 生成“穿舞会礼服的火辣白人女孩”的提示（失败案例）

**Author**: [毒猫猫🤔](https://x.com/NekoStranding)  **Date**: 2025-12-11  **Language**: en

> 在一个关于模型倾向于“正确性”以及难以生成某些类型图像的讨论中，提到了一个提示词，具体是“穿着舞会礼服的火辣白人女孩”。这被认为是一个由于模型限制而未能产生预期结果的提示词。

![生成“穿舞会礼服的火辣白人女孩”的提示（失败案例）](https://cms-assets.youmind.com/media/1765967768898_uvsd02_G75ypQnakAAvUxr.jpg)
![生成“穿舞会礼服的火辣白人女孩”的提示（失败案例）](https://cms-assets.youmind.com/media/1765967770352_48urb5_G75ymaqbYAE6QCw.jpg)

```
hot white girl in prom dress
```

[[Fashion Portrait]]

---

### 100. 写实风格的沙滩生活肖像

**Author**: [𝐌𝐢𝐧𝐝𝐒𝐩𝐚𝐫𝐤](https://x.com/Strength04_X)  **Date**: 2025-12-11  **Language**: en

> 一个生成逼真生活方式肖像的提示，描绘了一位年轻女性在海滩上，详细说明了她的外貌（充满活力、被风吹拂的深红色头发，雀斑）、着装（紧身衣和牛仔裤）、姿势，以及特定的地点参考（亨廷顿海滩救生塔）。它强调了刺眼的日光、电影般的夏日氛围和 8K 分辨率。

![写实风格的沙滩生活肖像](https://cms-assets.youmind.com/media/1765967725856_45l3aj_G744iplboAEanhK.jpg)
![写实风格的沙滩生活肖像](https://cms-assets.youmind.com/media/1765967726107_4oqzqu_G744iewb0AAF90l.jpg)

```
Photorealistic lifestyle portrait of a young woman in her early 20s with vibrant windswept dark red hair and a dusting of freckles. She is wearing a dark brown spaghetti-strap bodysuit and high-waisted relaxed blue jeans. She is seated on the sand, body angled to the side, one hand behind her head, looking off-camera to the left. Background features a white lifeguard tower on a wooden pier similar to Huntington Beach, with ocean waves crashing. Natural bright daylight, harsh sun creating distinct shadows, cinematic summer vibe, sharp focus on subject, 8k resolution.
```

[[Fashion Portrait]] [[Cinematic Color Grading]]

---

### 101. 优雅曲线美女性回眸一笑

**Author**: [Riccardo Wolf](https://x.com/WolfRiccardo)  **Date**: 2025-12-10  **Language**: en

> 一个 JSON 提示，旨在生成一张照片级真实的图像：一位身材曲线玲珑的女性，身穿紧身白色罗纹连衣裙，在夜晚优雅的室内环境中。她的姿势是背对镜头，然后回眸一笑，突出其夸张的沙漏型轮廓。

![优雅曲线美女性回眸一笑](https://cms-assets.youmind.com/media/1765509695445_l70146_G7z-LlcWQAAcZRO.jpg)

```
{
  "subject": {
    "description": "Young woman standing in an elegant indoor setting at night, turning her body slightly away from the camera while looking back over her shoulder. Her appearance matches the blonde glasses-character expressive eyes. No tattoos anywhere on the body. Her physique is noticeably fuller, curvier, and more dramatic in silhouette, closely matching the proportions seen in the reference image.",
    
    "face": {
      "structure": "delicate jawline, soft cheekbones, small natural nose, smooth skin texture, gentle feminine proportions",
      "expression": "calm, confident, with a slightly curious or subtle soft smile expression while looking at the camera over her shoulder",
      "glasses": "clear-frame or thin metal-frame glasses resting naturally on her face"
    },

    "hair": {
      "color": "light blonde",
      "style": "long, loose waves with a soft natural shine, falling over her back and one shoulder",
      "texture": "smooth with gentle movement, reflecting warm interior lighting"
    },

    "body": {
      "proportions": "dramatically curvy lower body, fuller hips, and rounded silhouette in line with the reference pose; narrow defined waist, natural upper body proportions; soft smooth skin with natural highlights",
      "posture": "upright with a distinct S-curve created by the exaggerated hip and waist shape, emphasizing the hourglass form"
    },

    "clothing": {
      "dress": {
        "type": "form-fitting ankle-length sleeveless white dress",
        "material": "soft ribbed stretch fabric that hugs the curves closely, emphasizing the dramatic hip silhouette and narrow waist",
        "color": "clean bright white with subtle warm reflections from indoor lighting",
        "fit_details": "fabric lightly wrinkled around the waist and lower back due to body curvature, smooth taut fit over hips and thighs, minimal seams"
      }
    }
  },

  "pose_and_composition": {
    "description": "standing at the threshold of an open doorway, body turned slightly to the side while looking back at the camera over her shoulder. One arm is extended slightly forward to rest on the doorframe, creating a gentle diagonal line, while the other arm is bent naturally with her hand resting on her waist, creating a confident and elegant pose.",
    "hand_positions": {
      "left_hand": "placed securely on the waist, thumb resting forward, fingers following the curve of her hip, adding to the hourglass silhouette",
      "right_hand": "lightly touching the edge of the doorframe, arm extended but relaxed, elbow soft and natural"
    },
    "head_position": "chin angled slightly down while eyes look over her shoulder toward the camera, enhancing the refined confident energy",
    "torso_and_hips": "torso rotated gently while hips remain squared backward, emphasizing the dramatic curvature of the lower body"
  },

  "environment_and_background": {
    "setting": "luxur"
  }
}
```

[[Fashion Portrait]] [[Hourglass Figure]]

---

### 102. 芭比风生日女孩派对

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2025-12-09  **Language**: en

> 一个详细的 JSON 格式提示，用于生成一张逼真的图片：一位年轻女性正在庆祝生日，她手捧蛋糕，身穿粉色图案两件套服装，头戴毛茸茸的头饰，背景是充满粉色气球的场景（芭比核心美学）。

![芭比风生日女孩派对](https://cms-assets.youmind.com/media/1765440049617_cg7w10_G7vXlMUawAA8JSL.jpg)

```
{
  "subject": {
    "type": "young woman",
    "pose": "leaning slightly forward while holding a cake with both hands, smiling widely at the camera",
    "expression": "happy, excited, celebratory",
    "face_details": {
      "skin_tone": "fair",
      "hair": "long straight blonde hair",
      "makeup": "soft glam makeup with glossy lips and defined eyes"
    },
    "outfit": {
      "type": "two-piece party outfit",
      "top": "long-sleeve crop top with front tie, pink transparent fabric with darker pink heart/spot print",
      "skirt": "short mini skirt matching the top, same pattern and material",
      "accessories": {
        "necklace": "thin silver choker necklace",
        "headpiece": "pink fluffy birthday tiara/crown"
      }
    }
  },
  "scene": {
    "setting": "indoor party room",
    "decorations": {
      "balloons": {
        "colors": ["light pink", "hot pink", "metallic pink"],
        "types": ["round balloons", "heart-shaped balloons", "star-shaped balloons"],
        "quantity": "large number filling the ceiling and background",
        "strings": "long white strings hanging down from the balloons"
      }
    },
    "furniture": {
      "visible_items": [
        "cream-colored plush stuffed toy or cushion on the floor",
        "dining chairs partially visible on the right"
      ]
    }
  },
  "cake": {
    "color": "pastel pink",
    "shape": "round",
    "details": {
      "decoration": "pearl-like edible beads on top",
      "base": "soft pink piped frosting border"
    },
    "presentation": "placed on a white cake board held by the woman"
  },
  "props": {
    "handheld_item": {
      "type": "pink light-up wand or toy with glowing tip",
      "design": "cute animal-like figure at the end"
    }
  },
  "lighting": {
    "type": "soft indoor lighting",
    "mood": "warm, bright, festive",
    "source": "ceiling lights with ambient glow"
  },
  "colors_theme": "dominant pink theme throughout outfit, balloons, cake, mood",
  "camera": {
    "angle": "eye-level, slightly close-up",
    "framing": "portrait orientation, subject centered with balloons filling background",
    "focus": "sharp on subject, slightly blurred background for depth"
  },
  "vibe": "birthday celebration, playful, feminine, fun, Barbie-core aesthetic",
  "style": {
    "realism": "photorealistic",
    "aesthetic": "soft party glamour with pink color palette"
  }
}
```

[[Fashion Portrait]]

---

### 103. 增强的电影黑色仰视视角

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-09  **Language**: en

> 一个极其详细、技术性强的提示词，用于生成一张电影般的赛博朋克黑色电影图像，采用排水管道内部的极端仰视视角。它细致地描述了拍摄对象的外观（亚洲女性、精灵短发、猫眼太阳镜、乙烯基飞行员夹克）、配饰（银戒指、龙纹身）、构图（强制透视、张开的手指）、灯光（钠蒸汽灯、体积雾、青橙色调色）以及相机/后期处理规格。

![增强的电影黑色仰视视角](https://cms-assets.youmind.com/media/1765440101180_tpohe9_G7u-y_ka0AAr1AV.jpg)

```
Subject & Wardrobe: A striking Asian female with a razor-sharp jet-black pixie cut (textured with pomade, asymmetrical fringe grazing her right brow), sporting matte-black oversized cat-eye sunglasses (acetate frames with micro-scratches). Her fingers are adorned with 5 silver rings: a skull signet, a serpent coil, a geometric cube, a band with etched runes, and a cracked obsidian stone. She wears a crimson vinyl bomber jacket (high-gloss, ribbed cuffs), collar popped, catching the backlight like liquid fire. Beneath, a sleeveless mesh top reveals a dragon tattoo creeping up her forearm. 

Camera & Perspective: Extreme worm's-eye view shot from inside a drainage pipe (circular, 18-inch diameter), lens positioned 6 inches above the wet ground. Forced perspective distortion makes her hand a monumental, terrifying presence—fingers elongated, knuckles massive, veins bulging. The circular frame vignettes the image, creating a keyhole peep-show effect. 

Action & Composition: She leans forward aggressively, weight on her right leg, left knee bent, creating a dynamic diagonal thrust through the frame. Her right hand lunges toward camera, fingers splayed, index finger extended, casting a shadow that eclipses the dice. Her face is 3/4 obscured by the sunglasses and hair; only her pierced lower lip (silver hoop) and clenched jaw are visible, exuding predatory focus. 

Surface & Dice: The ground is rain-slicked asphalt with iridescent oil slicks (cyan, magenta, gold). 12 translucent red casino dice (precision-edged, pips glowing like embers) are scattered in chaotic abandon—some stacked, some mid-roll. Water beads cling to them, refracting light. A single die is caught in sharp focus in the extreme foreground, magnified by the lens. 

Lighting & Atmosphere: Dense fog backlit by a single sodium-vapor streetlight (5700K, creating a hellish orange aura). Volumetric light rays pierce the fog, haloing her jacket. Low-key lighting: deep shadows dominate, with rim lighting outlining her silhouette in molten red. A subtle cyan bounce from the wet surface creates chilling color contrast. Lens flare: anamorphic horizontal streaks and circular bokeh orbs. 

Technical Specs: Shot on ARRI Alexa 65, 12mm Laowa Probe Lens (f/2. 8, 1/1000s shutter), 8K resolution, ISO 6400 for grit. Deep focus from foreground die to her face. Cinematic aspect ratio: 2. 39:1 (though can be cropped to 4:5). Shot in Log-C, graded with Teal & Orange + Neon Noir LUT. 

Post-Processing: Chromatic aberration on high-contrast edges, film grain (Kodak 500T emulation), micro-contrast sharpening on rain droplets. Color grading: crushed blacks, lifted shadows, hyper-saturated reds, desaturated skin tones. Subtle vignette from the pipe's darkness. 

Mood & Narrative: Neo-noir tension — a high-stakes underground gamb
```

[[Fashion Portrait]] [[Cyberpunk Aesthetic]] [[Neon Lighting]] [[Forced Perspective]]

---

### 104. 病毒式 Chrome 粉色宝马自拍提示词 (JSON 格式)

**Author**: [AISauce](https://x.com/aisauce_x)  **Date**: 2025-12-08  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张“病毒式”风格的自拍图像，画面中一位年轻女性，散发着“主角光环”，斜倚在一辆镀铬粉色宝马 i8 旁。该提示详细说明了拍摄对象的姿势、表情、服装（超短露脐上衣和迷你短裤）以及都市奢华的背景。

![病毒式 Chrome 粉色宝马自拍提示词 (JSON 格式)](https://cms-assets.youmind.com/media/1765438539724_gwo6pb_G7pryyCakAAQ7zX.jpg)

```
{
  "subject": {
    "description": "Young woman taking selfie next to chrome pink BMW i8, casual main character energy",
    "setting_rules": "street scene, luxury car, urban modern backdrop",
    "age": "early 20s",
    
    "expression": {
      "eyes": "focused on phone screen, taking selfie, casual confidence",
      "mouth": "relaxed, soft, natural",
      "brows": "relaxed, effortless",
      "overall": "unbothered, 'just casually next to a pink supercar' energy"
    },
    
    "hair": {
      "color": "platinum blonde",
      "style": "loose, flowing from under cap",
      "details": "messy-pretty, some pieces falling forward, effortless waves",
      "length": "medium-long, past shoulders"
    },
    
    "body": {
      "frame": "petite, slim, toned",
      "waist": "tiny, fully exposed midriff",
      "legs": "toned, athletic, fully visible",
      "stance": "casual lean against car, weight shifted"
    },
    
    "pose": {
      "position": "standing next to driver door of car, leaning slightly against it",
      "upper_body": {
        "action": "one arm UP holding phone for selfie",
        "phone_angle": "high, classic selfie position",
        "other_arm": "relaxed at side"
      },
      "lower_body": {
        "stance": "one leg straight, one slightly crossed or bent",
        "weight": "casual lean, hip near car",
        "energy": "relaxed but aware of angles"
      },
      "overall": "the 'caught me with this random supercar' pose that's definitely not random"
    },
    
    "clothing": {
      "top": {
        "type": "ultra cropped baby tee",
        "color": "bright YELLOW, sunshine yellow",
        "graphic": "small star or cute graphic on chest (or BANANA logo)",
        "fit": {
          "length": "EXTREME crop - ends just below chest, full stomach exposed",
          "tightness": "fitted, hugging curves",
          "sleeves": "short sleeves, casual"
        },
        "effect": "entire midriff visible from just under chest to shorts"
      },
      "bottom": {
        "type": "ultra mini athletic shorts",
        "color": "WHITE, clean bright white",
        "fit": {
          "style": "tight fitted athletic shorts",
          "length": "very short, upper thigh",
          "waist": "high-waisted, sits at natural waist",
          "effect": "shows full leg length, hugs curves"
        },
        "material": "stretchy athletic fabric, smooth"
      },
      "shoes": {
        "type": "white sneakers",
        "style": "clean, casual, athletic vibe",
        "effect": "completes sporty-cute look"
      }
    },
    
    "face": {
      "features": "pretty, big eyes, small nose, soft lips",
      "makeup": "natural, minimal, fresh-faced",
      "expression": "focused on selfie, casual pretty"
    }
  },

  "accessories": {
    "headwear": {
      "type": "baseball cap",
      "color": "BLACK",
      "style": "worn forward, classic",
      "logo": "small pa"
```

[[Fashion Portrait]] [[Luxury Car Portrait]]

---

### 105. 超逼真时尚照片，带精确面部匹配提示

**Author**: [𝙕ar⭕on](https://x.com/Zar_xplorer)  **Date**: 2025-12-07  **Language**: en

> 这是一个给 Gemini Nano Banana Pro 的提示，用于创建一张超逼真的 8K 单反风格照片，主角是一位时尚的年轻男士。提示详细说明了他的着装（白色连帽衫，带有黑色 Gucci 标志；浅蓝色工装裤）、姿势、背景（抽象的白色/浅蓝色结构），并严格要求男士的面部和发型与提供的参考照片一致。

![超逼真时尚照片，带精确面部匹配提示](https://cms-assets.youmind.com/media/1765421953215_vry4tp_G7jfzGVaIAARkOS.jpg)
![超逼真时尚照片，带精确面部匹配提示](https://cms-assets.youmind.com/media/1765421953881_uvkeyh_G7jfzPAb0AAalhh.jpg)

```
“Create an ultra-realistic 8K DSLR-style photo of a stylish young man striking a cool pose. He is wearing a white hoodie with a black Gucci logo, slightly unzipped at the collar, light blue cargo pants, and white sneakers. He is holding black sunglasses casually in one hand. The background should feature abstract, textured white and light-blue structures for a clean, modern look. Make sure the man's face and hairstyle match exactly with the reference photo.”
```

[[Fashion Portrait]] [[Face Matching]] [[Men's Fashion Photography]] [[Cargo Pants]]

---

### 106. 身穿棕色迷你连衣裙的优雅女士肖像提示

**Author**: [Shreya Yadav](https://x.com/ShreyaYadav___)  **Date**: 2025-12-03  **Language**: en

> 一个 JSON 封装的提示词，描述了一位穿着浅棕色迷你连衣裙的自信女性，置身于昏暗温暖的室内，适合用于时尚风格的 AI 肖像。

![身穿棕色迷你连衣裙的优雅女士肖像提示](https://cms-assets.youmind.com/media/1764909282430_jvg9fi_G7Ot69-aIAAflyJ.jpg)
![身穿棕色迷你连衣裙的优雅女士肖像提示](https://cms-assets.youmind.com/media/1764909284385_n83fmn_G7Ot60qbkAAQjDx.jpg)

```
{
  "prompt": "A beautiful woman with long, flowing brown hair poses confidently. She is wearing a form-fitting, light brown mini dress that accentuates her figure. Her left hand is raised to her head, and she looks directly at the viewer with a captivating gaze. The background is dimly lit, featuring warm wall sconces and a glimpse of a dark leather couch, creating an intimate and stylish atmosphere. The lighting highlights her hair and the contours of her body."
}
```

[[Fashion Portrait]] [[Warm Indoor Lighting]] [[Elegant Female Portrait]] [[Brown Mini Dress]]

---

### 107. Gemini 3 Pro 的高角度时尚肖像提示

**Author**: [𝙕arᎧon](https://x.com/Xxaroon)  **Date**: 2025-11-21  **Language**: en

> 回复包含一个详细的提示，用于拍摄一名年轻亚洲男士在大理石楼梯上的高角度时尚肖像。

![Gemini 3 Pro 的高角度时尚肖像提示](https://cms-assets.youmind.com/media/1763887324615_650und_G6P-AKiacAAf0BH.jpg)

```
High-angle fashion portrait of a 25-year-old Asian man, with the
same facial features as the man in the reference photo, messy hairstyle framed on his face, leaning casually on a
white marble staircase
```

[[Fashion Portrait]] [[High Angle Shot]]

---

### 108. 地铁门旁的甜美日系女孩

**Author**: [志辉](https://x.com/iamzhihui)  **Date**: 2025-11-20  **Language**: zh

> 一个中文提示，用于生成一个站在地铁门旁边的日系可爱女孩，适合时尚或角色形象。

![地铁门旁的甜美日系女孩](https://cms-assets.youmind.com/media/1763886849353_zxiybl_G6MBmWmacAk9lnc.jpg)

```
生成一张日式风的美女图片，站在地铁门口，甜美动人
```

[[Fashion Portrait]] [[Character Design]] [[Urban Scene]]

---

### 109. 巴黎夜派对舞蹈

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-04-10  **Language**: en

> 这是一个图像到图像（image-to-image）的提示词，旨在保持人物特征的同时，生成一张女性在巴黎夜派对上伴随动感灯光跳舞的场景。

![巴黎夜派对舞蹈](https://cms-assets.youmind.com/media/1776129406614_hhmgjl_HFim4IbXgAAy6J2.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "night_party_dance"
    },
    "input": {
      "mode": "image_to_image",
      "preserve_identity": true,
      "notes": "{argument name="scene notes" default="Paris night party. Woman dancing confidently, sparkling dress, motion blur, neon + warm lights mix, energetic vibe."}"
    }
  }
}
```

[[Female Portrait]] [[Image-To-Image]] [[Dance Photography]]

---

### 110. 欧洲街头身着风衣、发丝随风飘动的女性

**Author**: [Sarah](https://x.com/AIwithSarah_)  **Date**: 2026-04-09  **Language**: en

> 这是一条详细的提示词，用于生成一张动态的中景照片，展现一位留着棕色长发、身穿灰褐色风衣的年轻女性在户外城市背景下的形象，强调随风飘动的氛围和柔和的大地色调。

![欧洲街头身着风衣、发丝随风飘动的女性](https://cms-assets.youmind.com/media/1776096294808_h82dj3_HFdFNnZbkAA5qTx.jpg)

```
A dynamic medium shot captures a young Caucasian woman with long brown hair in an outdoor urban setting. Her hair, blown dramatically by the wind, frames her face, which features high cheekbones and a bold gaze directed over her shoulder. She wears an oversized taupe trench coat with black buttons over a black garment. Her right hand is adorned with gold rings, and she carries a light beige suede bag. The backdrop features a classical European street scene with ornate stone buildings and arcade walkways receding into the distance. The street is momentarily empty, adding to the cinematic and windswept mood. The lighting is diffused and cool, typical of overcast weather, casting soft shadows. The palette predominantly consists of muted earth tones: taupe, beige, gray, and soft blues. The photograph appears captured with a wide-angle lens, allowing for exaggerated perspective, and conveys a sense of motion and energy.
```

[[Female Portrait]] [[Candid Photography]] [[Wind Effect]] [[European Street Scene]]

---

### 111. 金发美女与 G-Wagon 的结构化提示词

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2026-04-08  **Language**: en

> 一份针对 Nano Banana 2 的结构化 JSON 提示词，详细描述了一位时尚的年轻金发女性站在欧洲城市街道的黑色梅赛德斯 G-Wagon 前，强调奢华生活方式、网红审美以及具有特定相机和光影设置的抓拍街拍风格。

![金发美女与 G-Wagon 的结构化提示词](https://cms-assets.youmind.com/media/1775717430964_iaej72_HFZAmwQa8Aki4xu.jpg)

```
{
  "prompt": "A stylish young blonde woman with long wavy hair standing on a European city street, in front of a black Mercedes G-Wagon. She is holding a green juice in a clear cup with a straw, wearing a fitted white long-sleeve crop top and loose light-wash jeans. She has a pink shoulder bag, minimal gold jewelry, and natural makeup. Background features elegant beige townhouse buildings with white trim and balconies, soft overcast lighting, luxury lifestyle aesthetic, candid street photography.",
  "style": "photorealistic, luxury lifestyle, influencer aesthetic",
  "camera": "iPhone photo, 50mm lens look, shallow depth of field",
  "lighting": "natural daylight, soft overcast, diffused lighting",
  "quality": "ultra realistic, 8k, high detail",
  "composition": "centered subject, full body, slightly angled pose, street-level perspective",
  "aspect_ratio": "9:16"
}
```

[[Female Portrait]] [[Influencer Aesthetic]] [[Luxury Car Portrait]] [[European City Street]]

---

### 112. 花园中女性的写实肖像

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-04-08  **Language**: en

> 一份详细的提示词，用于生成一张电影感照片级写实肖像：一位年轻女性坐在细雨蒙蒙的绿色花园中，手持芋头叶作为雨伞。重点刻画其外貌、服饰、妆容细节以及梦幻般的氛围。

![花园中女性的写实肖像](https://cms-assets.youmind.com/media/1775717428893_k34c31_HFWod1XbsAA1Ljt.jpg)

```
Realistic portrait of a young woman sitting in the middle of a green garden filled with small white and pink flowers as a light rain falls. She has long wavy dark brown hair. She held a soft green large taro leaf as umbrella, with raindrops clearly visible on its surface. She look at camera, smile softly and sparkling eyes. 

She wore a long ivory white dress (light and flowy material) with a Peter Pan collar detail and a small bow at the neck. Her makeup is soft douyin style makeup (glowing skin, clean matte foundation, soft blended pink blush, subtle highlights on the nose and cheekbones, thin eyeliner , soft pink eyeshadow, natural brow and long manhwa lashes, glossy pink lips. 

The background is a stretch of green grass with a shallow depth of field, slightly blurred wildflowers, and the effect of slowly falling rain with dreamy vibe. Soft natural lighting, little backlight from the cloudy sky. fresh, clean, and cinematic photorealistic feel.
```

[[Female Portrait]] [[Cinematic Photography]]

---

### 113. 使用 Nano Banana Pro 创作空灵肖像的提示词

**Author**: [ShaHid WaNii](https://x.com/meng_dagg695)  **Date**: 2026-04-07  **Language**: en

> 一份高度详细的提示词，用于生成一张空灵且细节丰富的户外肖像：一位身着田园风连衣裙的年轻女性坐在梦幻森林的庭院长椅上，指尖停着一只发光的蓝色蝴蝶。

![使用 Nano Banana Pro 创作空灵肖像的提示词](https://cms-assets.youmind.com/media/1775631281522_jc7mw0_HFR1MeOaEAAbQsT.jpg)
![使用 Nano Banana Pro 创作空灵肖像的提示词](https://cms-assets.youmind.com/media/1775631282518_pn1ms1_HFR1MeTbYAATXVq.jpg)

```
An ethereal, high-detail outdoor portrait of a young woman seated on a moss-covered, ornate wrought-iron garden bench in a dreamy forest setting. She has long, braided, wavy brown hair and a soft, curious expression as she gazes at a delicate, glowing blue butterfly resting on her outstretched left index finger.
She wears a cottagecore-inspired dress in light blue and white, featuring wide satin straps, a sweetheart neckline, and a structured white bust panel adorned with intricate blue floral embroidery, ribbon details, central flower appliqués, and small black bow accents. The skirt includes a sheer white tulle overlay decorated with tiny blue floral sprigs.
Her right arm rests gently by her side, while her left arm is raised toward the butterfly. She accessorizes with a light-blue beaded headpiece with a soft veil and small pearl floral earrings.
The environment is lush and magical, with soft, dappled natural light filtering through trees. Fine details are visible in the embroidery, moss texture, and the butterfly’s wings. Shot with a shallow depth of field, creating a soft, dreamy bokeh background of blurred foliage. Ultra-realistic, cinematic, 8K resolution.
```

[[Female Portrait]] [[Fantasy Portrait]]

---

### 114. 使用 Nano Banana 2 创作的高级时装大片提示词

**Author**: [Synthia](https://x.com/AIwithSynthia)  **Date**: 2026-04-07  **Language**: en

> 一个用于生成高级时装大片图像的提示词：一位时尚的年轻女性坐在俯瞰现代城市的屋顶上，身穿大胆的红色人造皮草外套和牛仔裤，具有电影般的构图和超逼真的细节。

![使用 Nano Banana 2 创作的高级时装大片提示词](https://cms-assets.youmind.com/media/1775631281676_s99njb_HFRrljKa4AApv_r.jpg)

```
A stylish young woman sitting casually on the edge of a rooftop overlooking a dense modern city, wearing a bold {argument name="coat color" default="red"} faux fur coat, light blue relaxed-fit jeans, and brown leather ankle boots. She has short, slightly messy black hair and a calm, confident expression. The city below is highly detailed with streets, cars, and buildings stretching into the distance, with a famous tower visible in the background. Shot in natural daylight with soft shadows, cinematic composition, wide-angle perspective, ultra-realistic, high fashion editorial style, shallow depth of field, 8k detail.
```

[[Female Portrait]] [[Cinematic Composition]]

---

### 115. 山顶城市景观全身照提示词

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-06  **Language**: en

> 一份详细的提示词，用于生成一张超写实的全身照，展示一名女性站在山顶俯瞰大型城市景观。重点在于强烈的自然阳光、清晰的地平线视野，并保持上传参考图中人物的精确特征。

![山顶城市景观全身照提示词](https://cms-assets.youmind.com/media/1775544746949_4p5i9s_HFQMwlNbMAAVnaF.jpg)
![山顶城市景观全身照提示词](https://cms-assets.youmind.com/media/1775544747047_56lsyk_HFQMwCkbcAAtWSg.jpg)

```
{
  "scene": {
    "setting": "hilltop viewpoint overlooking a large city",
    "background": "expansive cityscape stretching into distance with buildings and skyline softened by light atmospheric haze, dry grass and natural terrain in foreground, clear vibrant blue sky with no clouds, crisp horizon visibility",
    "lighting": "strong natural sunlight with clear direction, bright highlights and defined shadows, realistic sun angle, enhanced clarity with balanced exposure, vivid daylight rendering with no haze in sky"
  },
  "subject": {
    "type": "female",
    "pose": "standing on dirt path with body slightly turned away from camera, torso twisted back toward camera, one arm bent near waist, posture confident and natural with slight hip shift",
    "expression": "neutral confident expression with soft gaze toward camera",
    "face": "Use uploaded reference image, keep identity exact, natural facial structure with realistic skin texture, visible pores and minor imperfections, accurate sunlight interaction",
    "hair": "Use uploaded reference image, keep identity exact, straight dark hair with natural shine and slight movement from breeze",
    "eyes": "Use uploaded reference image, keep identity exact, clearly visible eyes, no sunglasses",
    "skin": "sunlit warm skin tone with realistic highlights and shadows, natural texture, no smoothing"
  },
  "clothing": {
    "top": "{argument name="top color" default="white"} fitted sleeveless crop top with smooth fabric and natural stretch",
    "bottom": "{argument name="bottom color" default="white"} high-waisted fitted pants with soft fabric folds and natural movement",
    "footwear": "minimal shoes or subtle sneakers with realistic ground interaction",
    "accessories": "no sunglasses, minimal jewelry"
  },
  "environment_details": {
    "props": "natural dirt trail, dry grass and small plants, distant city buildings",
    "textures": "earthy ground texture, plant detail, fabric texture, realistic skin detail, atmospheric depth"
  },
  "camera": {
    "angle": "slightly low angle behind subject with twist toward camera",
    "framing": "full body shot capturing subject and wide background view",
    "focus": "sharp focus on subject with gradual background depth blur",
    "lens": "portrait lens with slight compression and natural perspective"
  },
  "style": {
    "realism": "ultra realistic",
    "color_tone": "bright natural tones with strong blue sky and balanced warm skin tones",
    "effects": "subtle HDR, crisp contrast, clean color grading, no artificial filters",
    "details": "high detail textures, accurate lighting interaction, realistic shadows, no over-processing"
  }
}
```

[[Female Portrait]] [[Outdoor Photography]] [[Strong Natural Sunlight]]

---

### 116. 热带阳台全身照提示词

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-06  **Language**: en

> 一份用于生成超写实女性全身照的详细提示词，场景设定在热带阳台。重点在于明亮的自然光、鲜艳的热带色调，并确保完全保留上传参考图中的人物特征。

![热带阳台全身照提示词](https://cms-assets.youmind.com/media/1775544743250_kbtpu7_HFPQRSgbMAEl7Nz.jpg)
![热带阳台全身照提示词](https://cms-assets.youmind.com/media/1775544743336_65ztkj_HFPQQlXacAA6RCD.jpg)
![热带阳台全身照提示词](https://cms-assets.youmind.com/media/1775544744034_rzljzu_HFPQSqTbgAAFVfk.jpg)

```
{
  "scene": {
    "setting": "outdoor porch balcony in a tropical residential area",
    "background": "white wooden balcony railings and pillars, lush green palm trees and bushes, modern coastal houses in the distance, clear bright blue sky",
    "lighting": "natural bright sunlight from upper left creating strong highlights and soft shadows, warm golden-hour tone with slight lens glow, high dynamic range with balanced exposure"
  },
  "subject": {
    "type": "female",
    "pose": "standing relaxed on balcony, body slightly angled, one hand resting casually on white railing, other arm relaxed by side, weight shifted to one leg for natural posture",
    "expression": "soft smile with relaxed confident expression, slightly playful and warm mood",
    "face": "Use uploaded reference image, keep identity exact, oval face shape, soft defined cheekbones, natural skin texture with visible pores and minor imperfections, realistic light falloff on facial contours",
    "hair": "Use uploaded reference image, keep identity exact",
    "eyes": "Use uploaded reference image, keep identity exact, almond-shaped eyes, natural brows with soft arch",
    "skin": "light tan skin tone with sunlit highlights, realistic texture with slight sheen from sunlight, no over-smoothing"
  },
  "clothing": {
    "top": "soft {argument name="outfit color" default="pink"} fitted sleeveless top with subtle shimmer texture and small front tie detail",
    "bottom": "soft {argument name="outfit color" default="pink"} mini skirt with soft pleats and drawstring waist, flowy fabric with natural folds",
    "footwear": "not clearly visible, implied casual summer footwear",
    "accessories": "small shoulder bag in neutral tone, minimal jewelry including bracelet"
  },
  "environment_details": {
    "props": "clean white wooden architecture, tropical plants with detailed leaves, distant residential structures",
    "textures": "wood grain on railings, soft fabric folds, natural foliage detail, slight sunlight reflections on surfaces"
  },
  "camera": {
    "angle": "eye-level slightly low angle",
    "framing": "full body shot with subject centered",
    "focus": "sharp focus on subject with slightly softened background for depth",
    "lens": "50mm portrait lens with natural perspective and shallow depth of field"
  },
  "style": {
    "realism": "ultra realistic",
    "color_tone": "bright vibrant tropical tones with strong blues and greens, warm skin highlights",
    "effects": "subtle HDR effect, gentle lens glow, soft shadow gradients, natural color grading, slight film grain for realism",
    "details": "high detail skin texture, realistic lighting interaction, accurate fabric rendering, no over-processing or artificial smoothing"
  }
}
```

[[Female Portrait]] [[Natural Light Photography]] [[Tropical Setting]] [[Outdoor Lifestyle]]

---

### 117. 火车站台上女性的电影感肖像

**Author**: [Lovart 公式 (ラブアート)](https://x.com/lovart_jp)  **Date**: 2026-04-06  **Language**: ja

> 这是一个详细的电影感肖像提示词，适用于多种 AI 模型（Midjourney、Nano Banana Pro、GPT Image 1.5、Nano Banana 2），旨在生成一张年轻日本女性独自坐在新宿火车站台长椅上的图像。该提示词强调了她静止的状态与疾驰而过的列车所形成的动态对比。

![火车站台上女性的电影感肖像](https://cms-assets.youmind.com/media/1775544747024_3tuftx_HE-wDUzaAAAV2ge.jpg)
![火车站台上女性的电影感肖像](https://cms-assets.youmind.com/media/1775544747049_1k1hyb_HE-wEdoboAAWRHh.jpg)
![火车站台上女性的电影感肖像](https://cms-assets.youmind.com/media/1775544748129_x4v1yj_HE-wE5uaIAA7KlV.jpg)
![火车站台上女性的电影感肖像](https://cms-assets.youmind.com/media/1775544748226_73i3b4_HE-wD8qbYAAXbhj.jpg)

```
新宿電車のホームのベンチに一人座る日本若い女性を、画面中央に配置し、穏やかでやや真剣な表情でカメラをまっすぐ見つめる、映画のようなポートレート。彼女はオーバーサイズのダークグリーンのコート、薄手のセーター、ライトブルーのジーンズ、そして黒いブーツを身に着けている。髪はゆるく、少し乱れている。背景には地下鉄の電車が猛スピードで走り去る様子が写っており、強いモーションブラー処理によってスピード感と彼女の静止した姿とのコントラストが強調されている。浅い被写界深度、被写体へのシャープなフォーカス、柔らかな自然光、都市環境、落ち着いた色調、高精細、プロによる撮影、50mmレンズ、長時間露光効果、左右対称の構図。
```

[[Female Portrait]] [[Cinematic Photography]] [[Motion Blur Background]] [[Solitary Figure]]

---

### 118. 适用于 Google Gemini Nano Banana Pro 的极简时尚人像提示词

**Author**: [Cherry 2.O](https://x.com/Mind_Boticni)  **Date**: 2026-04-06  **Language**: en

> 这是一份用于生成全身、高细节时尚人像的提示词，背景为纯浅灰色，强调极简主义摄影棚美学及柔和均匀的布光。

![适用于 Google Gemini Nano Banana Pro 的极简时尚人像提示词](https://cms-assets.youmind.com/media/1775544741510_vmz3al_HFMqHArbQAAFtvp.jpg)

```
Full-body portrait of a stylish young man standing against a plain light gray background, wearing a fitted black button-up shirt with sleeves rolled up, dark gray slim-fit trousers, and black polished dress shoes. He is posing casually with one hand in his pocket and the other hand near his mouth, slightly lifting one leg. The lighting is soft and even, highlighting his natural features, with a clean minimalist studio aesthetic. Realistic proportions, high-detail, sharp focus, fashion photography style.
```

[[Female Portrait]] [[Fashion Photography]] [[Soft Even Lighting]]

---

### 119. 手持菠萝的超写实热带海滩漫步

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-05  **Language**: en

> 这是一个为 Nano Banana Pro 准备的详细 JSON 提示词，用于生成一张超写实的图像：一位女性在热带海滩岸边行走，手持菠萝，画面呈现明亮的自然阳光、高度鲜艳的色彩，并包含关于人物面部、姿势以及黑色连体泳衣的具体细节。

![手持菠萝的超写实热带海滩漫步](https://cms-assets.youmind.com/media/1775458527409_krzb9c_HFKp8jKawAA_rNo.jpg)
![手持菠萝的超写实热带海滩漫步](https://cms-assets.youmind.com/media/1775458527480_elsi4e_HFKp9OwasAAWxZo.jpg)
![手持菠萝的超写实热带海滩漫步](https://cms-assets.youmind.com/media/1775458527814_c7in15_HFKp94oacAAF4KF.jpg)
![手持菠萝的超写实热带海滩漫步](https://cms-assets.youmind.com/media/1775458528650_ydu9jw_HFKp-qPagAAXkkK.jpg)

```
{
  "scene": {
    "setting": "tropical beach shoreline",
    "background": "clear bright blue ocean water with vivid turquoise tones, gentle waves, sunlit reflections on surface, clean sandy beach, horizon softly visible under clear sky",
    "lighting": "bright natural sunlight, high exposure with balanced highlights, strong clarity, enhanced vibrance, soft shadows with clean light falloff"
  },
  "subject": {
    "type": "female",
    "pose": "walking along shoreline toward camera, one hand holding a pineapple, other arm relaxed slightly extended, natural stride with confident posture",
    "expression": "soft relaxed smile, calm and content expression, eyes gently lowered",
    "face": "Use uploaded reference image, keep identity exact, oval face shape, smooth skin with natural texture and minor imperfections, full lips, straight nose, balanced facial proportions",
    "hair": "Use uploaded reference image, keep identity exact",
    "eyes": "Use uploaded reference image, keep identity exact, almond-shaped eyes, natural brows with soft arch",
    "skin": "light to medium warm skin tone with sunlit glow, realistic texture, slightly enhanced highlights from bright sunlight"
  },
  "clothing": {
    "top": "{argument name="swimsuit color" default="black"} one-piece swimsuit with deep neckline and fitted silhouette",
    "bottom": "integrated with swimsuit",
    "footwear": "barefoot on sand",
    "accessories": "flower tucked in hair, hoop earrings, bracelet, necklace"
  },
  "environment_details": {
    "water": "bright blue and turquoise ocean with high clarity and sparkle, enhanced saturation and luminance",
    "sand": "light beige sand with soft texture, slightly reflective near water",
    "atmosphere": "clean tropical air with high visibility and vibrant colors"
  },
  "camera": {
    "angle": "eye-level angle",
    "framing": "medium full-body shot centered on subject",
    "focus": "sharp focus on subject, background slightly softened",
    "lens": "portrait lens with natural depth of field"
  },
  "style": {
    "realism": "ultra realistic",
    "color_tone": "highly vibrant with boosted blues and warm skin tones",
    "details": "enhanced contrast, increased saturation, crisp highlights, realistic reflections on water, no over-smoothing"
  }
}
```

[[Female Portrait]] [[Natural Sunlight]] [[Vibrant Colors]]

---

### 120. 火车站台上女性的电影感肖像

**Author**: [Lovart 公式 (ラブアート)](https://x.com/lovart_jp)  **Date**: 2026-04-06  **Language**: ja

> 这是一个详细的电影感肖像提示词，适用于多种 AI 模型（Midjourney、Nano Banana Pro、GPT Image 1.5、Nano Banana 2），旨在生成一张年轻日本女性独自坐在新宿火车站台长椅上的图像。该提示词强调了她静止的状态与疾驰而过的列车所形成的动态对比。

![火车站台上女性的电影感肖像](https://cms-assets.youmind.com/media/1775544747024_3tuftx_HE-wDUzaAAAV2ge.jpg)
![火车站台上女性的电影感肖像](https://cms-assets.youmind.com/media/1775544747049_1k1hyb_HE-wEdoboAAWRHh.jpg)
![火车站台上女性的电影感肖像](https://cms-assets.youmind.com/media/1775544748129_x4v1yj_HE-wE5uaIAA7KlV.jpg)
![火车站台上女性的电影感肖像](https://cms-assets.youmind.com/media/1775544748226_73i3b4_HE-wD8qbYAAXbhj.jpg)

```
新宿電車のホームのベンチに一人座る日本若い女性を、画面中央に配置し、穏やかでやや真剣な表情でカメラをまっすぐ見つめる、映画のようなポートレート。彼女はオーバーサイズのダークグリーンのコート、薄手のセーター、ライトブルーのジーンズ、そして黒いブーツを身に着けている。髪はゆるく、少し乱れている。背景には地下鉄の電車が猛スピードで走り去る様子が写っており、強いモーションブラー処理によってスピード感と彼女の静止した姿とのコントラストが強調されている。浅い被写界深度、被写体へのシャープなフォーカス、柔らかな自然光、都市環境、落ち着いた色調、高精細、プロによる撮影、50mmレンズ、長時間露光効果、左右対称の構図。
```

[[Female Portrait]] [[Cinematic Photography]] [[Motion Blur Background]] [[Solitary Figure]]

---

### 121. 适用于 Google Gemini Nano Banana Pro 的极简时尚人像提示词

**Author**: [Cherry 2.O](https://x.com/Mind_Boticni)  **Date**: 2026-04-06  **Language**: en

> 这是一份用于生成全身、高细节时尚人像的提示词，背景为纯浅灰色，强调极简主义摄影棚美学及柔和均匀的布光。

![适用于 Google Gemini Nano Banana Pro 的极简时尚人像提示词](https://cms-assets.youmind.com/media/1775544741510_vmz3al_HFMqHArbQAAFtvp.jpg)

```
Full-body portrait of a stylish young man standing against a plain light gray background, wearing a fitted black button-up shirt with sleeves rolled up, dark gray slim-fit trousers, and black polished dress shoes. He is posing casually with one hand in his pocket and the other hand near his mouth, slightly lifting one leg. The lighting is soft and even, highlighting his natural features, with a clean minimalist studio aesthetic. Realistic proportions, high-detail, sharp focus, fashion photography style.
```

[[Female Portrait]] [[Fashion Photography]] [[Soft Even Lighting]]

---

### 122. 手持菠萝的超写实热带海滩漫步

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-05  **Language**: en

> 这是一个为 Nano Banana Pro 准备的详细 JSON 提示词，用于生成一张超写实的图像：一位女性在热带海滩岸边行走，手持菠萝，画面呈现明亮的自然阳光、高度鲜艳的色彩，并包含关于人物面部、姿势以及黑色连体泳衣的具体细节。

![手持菠萝的超写实热带海滩漫步](https://cms-assets.youmind.com/media/1775458527409_krzb9c_HFKp8jKawAA_rNo.jpg)
![手持菠萝的超写实热带海滩漫步](https://cms-assets.youmind.com/media/1775458527480_elsi4e_HFKp9OwasAAWxZo.jpg)
![手持菠萝的超写实热带海滩漫步](https://cms-assets.youmind.com/media/1775458527814_c7in15_HFKp94oacAAF4KF.jpg)
![手持菠萝的超写实热带海滩漫步](https://cms-assets.youmind.com/media/1775458528650_ydu9jw_HFKp-qPagAAXkkK.jpg)

```
{
  "scene": {
    "setting": "tropical beach shoreline",
    "background": "clear bright blue ocean water with vivid turquoise tones, gentle waves, sunlit reflections on surface, clean sandy beach, horizon softly visible under clear sky",
    "lighting": "bright natural sunlight, high exposure with balanced highlights, strong clarity, enhanced vibrance, soft shadows with clean light falloff"
  },
  "subject": {
    "type": "female",
    "pose": "walking along shoreline toward camera, one hand holding a pineapple, other arm relaxed slightly extended, natural stride with confident posture",
    "expression": "soft relaxed smile, calm and content expression, eyes gently lowered",
    "face": "Use uploaded reference image, keep identity exact, oval face shape, smooth skin with natural texture and minor imperfections, full lips, straight nose, balanced facial proportions",
    "hair": "Use uploaded reference image, keep identity exact",
    "eyes": "Use uploaded reference image, keep identity exact, almond-shaped eyes, natural brows with soft arch",
    "skin": "light to medium warm skin tone with sunlit glow, realistic texture, slightly enhanced highlights from bright sunlight"
  },
  "clothing": {
    "top": "{argument name="swimsuit color" default="black"} one-piece swimsuit with deep neckline and fitted silhouette",
    "bottom": "integrated with swimsuit",
    "footwear": "barefoot on sand",
    "accessories": "flower tucked in hair, hoop earrings, bracelet, necklace"
  },
  "environment_details": {
    "water": "bright blue and turquoise ocean with high clarity and sparkle, enhanced saturation and luminance",
    "sand": "light beige sand with soft texture, slightly reflective near water",
    "atmosphere": "clean tropical air with high visibility and vibrant colors"
  },
  "camera": {
    "angle": "eye-level angle",
    "framing": "medium full-body shot centered on subject",
    "focus": "sharp focus on subject, background slightly softened",
    "lens": "portrait lens with natural depth of field"
  },
  "style": {
    "realism": "ultra realistic",
    "color_tone": "highly vibrant with boosted blues and warm skin tones",
    "details": "enhanced contrast, increased saturation, crisp highlights, realistic reflections on water, no over-smoothing"
  }
}
```

[[Female Portrait]] [[Natural Sunlight]] [[Vibrant Colors]]

---

### 123. 湖畔码头黄金时刻日落人像

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-05  **Language**: en

> 一份详细的 Nano Banana Pro 提示词，用于生成一张女性在日落时分坐在木质码头上的超写实人像。强调温暖的黄金时刻光影、柔和的倒影，并使用参考图以确保面部特征的精确还原。

![湖畔码头黄金时刻日落人像](https://cms-assets.youmind.com/media/1775458533298_188k6d_HFKh7-wa8AA2o3q.jpg)
![湖畔码头黄金时刻日落人像](https://cms-assets.youmind.com/media/1775458533282_05nc8m_HFKh80wakAARIXj.jpg)
![湖畔码头黄金时刻日落人像](https://cms-assets.youmind.com/media/1775458533335_m4e83u_HFKh9jObgAAHCAW.jpg)
![湖畔码头黄金时刻日落人像](https://cms-assets.youmind.com/media/1775458534494_70sal0_HFKh-PHacAAyBhL.jpg)

```
{
  "scene": {
    "setting": "outdoor lakeside dock during sunset",
    "background": "calm water reflecting warm sunset tones, distant tree line, soft gradient sky transitioning from orange near horizon to blue above",
    "lighting": "natural golden hour lighting, soft warm sunlight casting gentle highlights on subject, subtle reflections from water, low contrast shadows"
  },
  "subject": {
    "type": "female",
    "pose": "sitting on wooden dock with knees pulled close to chest, arms wrapped around legs, body slightly turned sideways, head resting gently on arms while facing camera",
    "expression": "warm natural smile, soft joyful expression with slight teeth visibility, relaxed eyes conveying calm and comfort",
    "face": "Use uploaded reference image, keep identity exact, oval face shape, soft defined cheekbones, natural skin texture with visible pores and minor imperfections, full lips, straight nose, balanced facial proportions",
    "hair": "Use uploaded reference image, keep identity exact",
    "eyes": "Use uploaded reference image, keep identity exact, almond-shaped eyes, natural brows with soft arch",
    "skin": "light to medium skin tone with warm sunset glow, realistic texture with subtle imperfections"
  },
  "clothing": {
    "top": "{argument name="top garment" default="oversized cream knitted sweater"} with visible texture and patterns",
    "bottom": "{argument name="bottom garment" default="blue denim jeans"} with relaxed fit",
    "footwear": "white athletic sneakers with clean design",
    "accessories": "minimal or no visible accessories"
  },
  "environment_details": {
    "dock": "wooden dock with visible grain and lines, slightly weathered texture",
    "water": "calm lake surface with gentle ripples reflecting sky colors",
    "surroundings": "quiet natural setting with distant trees and open horizon"
  },
  "camera": {
    "angle": "eye-level slightly angled perspective",
    "framing": "medium full-body shot with subject placed slightly off-center",
    "focus": "sharp focus on subject, soft background blur",
    "lens": "portrait lens with natural depth of field"
  },
  "style": {
    "realism": "ultra realistic",
    "color_tone": "warm golden hour tones with natural color balance",
    "details": "high detail textures in clothing and skin, realistic lighting and reflections, no over-smoothing"
  }
}
```

[[Female Portrait]] [[Golden Hour Lighting]] [[Water Reflection]] [[Sunset Photography]]

---

### 124. 优雅夜间酒廊人像：斑马纹连衣裙

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-04-05  **Language**: en

> 这是为 Nano Banana 2 设计的结构化详细提示词，旨在生成一张女性坐在高档酒廊中的精致人像。提示词明确了主体细节、服装（斑马纹迷你裙）、环境（温暖的琥珀色灯光、模糊背景）以及专业相机参数（3:4 人像比例、浅景深）。

![优雅夜间酒廊人像：斑马纹连衣裙](https://cms-assets.youmind.com/media/1775458530231_lj4i52_HFJme_pakAAidz6.jpg)
![优雅夜间酒廊人像：斑马纹连衣裙](https://cms-assets.youmind.com/media/1775458530242_dj7jhq_HFJme_wa8AAbW1P.jpg)
![优雅夜间酒廊人像：斑马纹连衣裙](https://cms-assets.youmind.com/media/1775458530296_ariggz_HFJme_6awAEfjtg.jpg)
![优雅夜间酒廊人像：斑马纹连衣裙](https://cms-assets.youmind.com/media/1775458531317_wuufp1_HFJme_rbIAEYSLN.jpg)

```
{
  "image_analysis": {
    "subject_details": {
      "use_reference_image": {argument name="use reference image" default="true"},
      "override": false,
      "pose": "Seated on a light-colored bench, leaning back comfortably with the left arm raised, hand resting near the side of the head"
    },
    "attire_and_accessories": {
      "clothing": {
        "style": "Form-fitting mini dress",
        "pattern": "Vertical zebra-style animal print in dark brown and creamy beige",
        "neckline": "Deep, structured sweetheart neckline with a corset-style bodice"
      },
      "jewelry": {
        "neckwear": "Thin, delicate gold chain necklace with a small pendant",
        "wristwear": "Multiple stacked gold-tone bangles and a beaded bracelet on the left wrist"
      },
      "handbag": "Small, white quilted leather handbag with a gold interlocking logo (Chanel-style), positioned on the lap"
    },
    "environment_and_atmosphere": {
      "setting": "Interior of an upscale lounge, bar, or restaurant at night",
      "background_objects": {
        "seating": "Cream-colored upholstered sofa or banquette with a clean, modern design",
        "lighting": "Warm, amber-toned ambient lighting creating a soft glow throughout the room",
        "details": "Blurred background showing architectural wooden panels, indoor greenery/plants illuminated by warm spotlights, and distant glowing lights"
      },
      "color_palette": "Dominated by warm neutrals including beige, cream, chocolate brown, and amber gold",
      "mood": "Elegant, sophisticated, and intimate"
    },
    "technical_specifications": {
      "composition": "Medium shot (waist-up), slightly low-angle perspective",
      "aspect_ratio": "3:4 portrait orientation",
      "focus": "Sharp focus on the subject in the foreground with a shallow depth of field (bokeh) blurring the background elements",
      "lighting_style": "Soft-box or ring-light style illumination on the face, contrasting with the dim, warm background lighting"
    }
  }
}
```

[[Female Portrait]] [[Bokeh Background]] [[Amber Lighting]]

---

### 125. 奢华生活方式杂志人像

**Author**: [David](https://x.com/tealdog2)  **Date**: 2026-04-05  **Language**: en

> 这是为 Nano Banana Pro 准备的一条简单文本提示词，旨在请求生成一张在度假村拍摄的女性人像，用于奢华生活方式杂志编辑。

![奢华生活方式杂志人像](https://cms-assets.youmind.com/media/1775458530861_w417ey_HFGuGQobEAAvP62.jpg)

```
Beautiful woman at a resort for a  luxury lifestyle editorial.
```

[[Female Portrait]] [[Editorial Photography]]

---

### 126. 现代健身房高分辨率健身生活方式人像

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-04-03  **Language**: en

> 一个结构化的 JSON 提示词，用于生成在现代健身房场景中女性的写实健身人像，强调自然的运动后光泽、特定光影效果以及自信的表情。

![现代健身房高分辨率健身生活方式人像](https://cms-assets.youmind.com/media/1775284650377_fa77t0_HFAaALaaMAAEEag.jpg)
![现代健身房高分辨率健身生活方式人像](https://cms-assets.youmind.com/media/1775284650316_j6ph6h_HFAaAJsb0AAm6fA.jpg)
![现代健身房高分辨率健身生活方式人像](https://cms-assets.youmind.com/media/1775284650386_34zw6o_HFAaAS8XkAAd9JS.jpg)
![现代健身房高分辨率健身生活方式人像](https://cms-assets.youmind.com/media/1775284651299_ga4dno_HFAaAWrWYAA9mlb.jpg)

```
{
  "prompt": "A high-resolution fitness lifestyle portrait of a young athletic woman in a modern gym, leaning forward against a workout bench. She is wearing {argument name="shorts color" default="bright pink"} athletic shorts and a {argument name="bra color" default="light white"} sports bra, with wireless earbuds in her ears. Her skin is slightly sweaty, giving a natural post-workout glow. She is looking back over her shoulder toward the camera with a confident, relaxed expression. The gym background includes treadmills, dumbbells, and large windows with soft natural light, and a neon written 'KeorUnreal'. Clean, contemporary indoor setting, realistic lighting, sharp focus, and detailed skin texture.",
  "negative_prompt": "blurry, low resolution, distorted anatomy, extra limbs, poorly drawn face, unnatural skin, oversaturated colors, cluttered composition, bad lighting, harsh shadows, watermark, text",
  "style": "fitness lifestyle photography",
  "camera": {
    "angle": "rear three-quarter angle",
    "framing": "waist-up to mid-thigh portrait",
    "lens": "50mm"
  },
  "lighting": {
    "type": "natural window light mixed with soft indoor lighting",
    "mood": "fresh, energetic, realistic"
  },
  "subject": {
    "pose": "leaning on workout bench, torso slightly twisted, looking back",
    "expression": "confident and relaxed",
    "hair": "tied back in a ponytail",
    "outfit": "yellow athletic shorts, gray sports bra, wireless earbuds"
  },
  "setting": {
    "location": "modern gym interior",
    "elements": ["treadmills", "dumbbells", "large windows"],
    "time_of_day": "daytime"
  },
  "quality": {
    "photorealistic": true,
    "high_detail": true,
    "skin_texture": "natural with sweat",
    "resolution": "high"
  }
}
```

[[Female Portrait]] [[Sports Photography]] [[Post-Workout Glow]]

---

### 127. 超写实更衣室抓拍人像

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-04-03  **Language**: en

> 一份高度详细的 JSON 提示词，用于生成一张超写实、抓拍风格的女性更衣室人像。画面捕捉了女性在更衣室中动作瞬间的动态，重点展现私密氛围、自然的皮肤质感以及具体的面部结构细节。

![超写实更衣室抓拍人像](https://cms-assets.youmind.com/media/1775284653152_8uj9hy_HE_uLjRb0AE7E4n.jpg)

```
{ "type": "image_prompt", "description": { "style": { "genre": "ultra photorealistic cinematic dressing room portrait", "mood": "intimate, candid, slightly tense with a teasing undertone", "color_palette": "warm indoor lighting, soft skin tones, muted beige and cream fabrics", "visual_tone": "high-end editorial realism, natural indoor lighting, zero CGI look" }, "identity_details": { "character_type": "Sydney Sweeney lookalike (NOT the real person)", "gender": "female", "age_range": "mid 20s", "ethnicity": "fair skin with warm undertones", "resemblance_notes": "strong resemblance through soft rounded face, large blue eyes, blonde features, and full lips while clearly being a different individual" }, "character": { "build": "fit feminine physique with natural curves, medium-full bust, softly defined waist, fuller thighs", "height_impression": "average height", "presence": "vulnerable yet confident, caught mid-moment with natural sensuality" }, "face_structure": { "face_shape": "rounded oval with soft cheek fullness", "forehead": "smooth and balanced", "eyebrows": "light blonde, softly arched", "eyes": "large blue eyes opened wider than usual", "nose": "small straight nose with soft tip", "cheekbones": "softly defined", "lips": "full lips with natural volume", "jawline": "soft taper", "chin": "rounded" }, "facial_details": { "skin_texture": "visible pores with soft indoor glow", "complexion": "fair with warm highlights", "makeup": "minimal soft glam slightly smudged or natural", "eyes_detail": "strong catchlights from mirror bulbs", "lips_detail": "natural soft texture with slight gloss", "imperfections": "natural asymmetry and subtle skin variation" }, "hair": { "color": "light golden blonde", "style": "loose slightly messy hair", "texture": "soft strands with natural volume", "placement": "partially falling over shoulders with slight movement as if mid-action" }, "accessories": { "jewelry": "minimal delicate necklace and small earrings", "props": "clothing partially in hands or hanging nearby" }, "expression": { "emotion": "surprised, caught off guard", "eyes": "wide open looking directly toward camera", "mouth": "slightly open in shock", "overall_expression": "unexpected interruption with a mix of surprise and subtle tension" }, "pose": { "body_position": "standing inside changing room mid-motion", "torso_angle": "slightly twisted as if turning toward camera suddenly", "shoulders": "raised slightly due to surprise", "head": "slightly pulled back with alert posture", "arm_position": "one hand holding or adjusting clothing near chest, other hand paused mid-motion near waist", "leg_position": "one leg slightly bent creating natural imbalance", "pose_energy": "dynamic, candid, interrupted moment with natural realism" }, "clothing": { "outfit": "incomplete changing state", "top": "soft fitted bra with thin straps and subtle fabric texture", "bottom": "matching panties"
```

[[Female Portrait]] [[Candid Photography]] [[Natural Skin Texture]] [[Intimate Atmosphere]]

---

### 128. 照片级写实的女性浇花场景

**Author**: [空想写真家](https://x.com/KusoPhoto)  **Date**: 2026-04-03  **Language**: ja

> 这是一个用于通过 Nano Banana Pro 生成四张图像的提示词，随后使用 Kling 3.0 Omni 将其拼接成视频。该提示词描述了一个照片级写实、具有电影感的女性浇灌室内植物的场景。

```
女性がジョウロで観葉植物に水をやりながら微笑む、映画のような映像。彼女は身を乗り出し、濡れたみずみずしい緑の葉に愛情を込めて息を吹きかけ、それからゆっくりとカメラを見上げ、優しく無邪気な微笑みを浮かべながら満足そうに頷く。温かみのある自然光、非常に精緻でフォトリアリスティックな描写。
```

[[Female Portrait]] [[Video Frame Image]] [[Cinematic Lifestyle]]

---

### 129. 台阶上的女性肖像及细节服饰

**Author**: [Serrah ❀](https://x.com/Serreh131306)  **Date**: 2026-04-02  **Language**: en

> 这是一个为 Gemini Nano Banana Pro 设计的结构化提示词，详细描述了一位坐在赤陶台阶上的年轻女性肖像，涵盖了她的外貌、服装（蕾丝吊带背心、格子裙、蕾丝连裤袜）、配饰、场景以及光影效果，旨在生成高质量的写实图像。

![台阶上的女性肖像及细节服饰](https://cms-assets.youmind.com/media/1775198502883_pcrm82_HE7D7iBawAA0VFJ.jpg)

```
{
  "visual_details": {
    "subject": "Young woman, long dark hair, brown eyes.",
    "pose": "Sitting on steps, hand on chin, looking directly at camera.",
    "clothing": "Black lace camisole, brown plaid mini skirt, black floral lace tights.",
    "accessories": "Tortoiseshell cat-eye glasses, layered silver necklaces, bracelets, rings, black quilted chain bag.",
    "setting": "Terracotta tiled steps, white tiled wall, dark doorway with 'STUDIO' text.",
    "lighting": "Bright natural daylight, sharp shadows."
  },
  "prompt": "Portrait of a young woman sitting on terracotta steps. Long dark hair, tortoiseshell cat-eye glasses, black lace camisole, brown plaid skirt, black floral lace tights. Layered silver jewelry. Hand resting on chin, serious expression, holding black quilted chain bag. White tiled wall background, dark doorway marked 'STUDIO'. Bright sunlight. 4k ultra quality, 9:16 canvas."
}
```

[[Female Portrait]] [[Plaid Skirt]]

---

### 130. 高对比度钢笔淡彩肖像

**Author**: [Minahil](https://x.com/Minahil42298354)  **Date**: 2026-03-30  **Language**: en

> 这是为 Gemini Nano Banana 设计的提示词，旨在生成一张高对比度的钢笔淡彩年轻女性肖像。通过复杂的交叉排线和点画技巧营造深度，模拟纹理纸张上的技术绘图效果。

![高对比度钢笔淡彩肖像](https://cms-assets.youmind.com/media/1774939630161_t4klck_HEqp23hXYAE9ENi.jpg)

```
A high-contrast pen and ink portrait of a young woman with a soulful gaze, based on a delicate pencil sketch. The style features intricate cross-hatching and fine-line stippling to create depth and shadow. Her hair is styled in a loose, messy bun with wispy, flyaway strands framing her face. The linework should be sharp and precise, mimicking a technical drawing pen on textured paper. Deep, dense ink shadows contrast against bright highlights on her skin, emphasizing her sharp cheekbones and expressive eyes. Minimalist background with subtle ink splatters and hatching.
```

[[Female Portrait]]

---

### 131. 在火车上吃面的女性写实生活照

**Author**: [Dockie](https://x.com/Document195)  **Date**: 2026-03-28  **Language**: en

> 这是一个为 Nano Banana Pro 设计的详细结构化提示词，旨在生成一张写实风格的生活照，展示一位年轻女性在舒适现代的旅行环境中享用方便面的场景。

![在火车上吃面的女性写实生活照](https://cms-assets.youmind.com/media/1774766198255_hrbyqr_HEf70pmagAEcFfD.jpg)
![在火车上吃面的女性写实生活照](https://cms-assets.youmind.com/media/1774766198373_ldy4k6_HEf70pnbkAAJxXl.jpg)

```
{
  "prompt": "A young woman with long blonde hair sitting comfortably in a modern train or airplane seat, wearing large over-ear headphones. She is casually eating instant noodles from a red cup using a fork, looking slightly toward the camera with a relaxed, natural expression. She wears a soft beige tank top, light patterned shorts, and cozy socks. The setting feels like a premium travel cabin with soft lighting, muted tones, and a clean, minimal interior. A small snack package is visible beside her, adding to the casual travel vibe. The scene is candid, lifestyle-focused, and intimate.",
  "style": "photorealistic, lifestyle photography, soft aesthetic",
  "lighting": "soft ambient cabin lighting, natural skin tones",
  "camera": {
    "angle": "eye-level, slightly close framing",
    "focus": "sharp focus on subject, shallow depth of field",
    "lens": "50mm"
  },
  "details": [
    "instant noodle cup with steam",
    "over-ear headphones",
    "comfortable travel seat",
    "subtle textures in clothing",
    "clean modern interior design"
  ],
  "mood": "relaxed, cozy, travel aesthetic",
  "resolution": "high detail, 4k"
}
```

[[Female Portrait]]

---

### 132. 狗仔队风格 夜间照片 提示词，直射闪光

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-27  **Language**: en

> 一个适用于 Nano Banana Pro 的超逼真夜间摄影提示词，旨在生成一张高对比度、狗仔队风格的图像，描绘一位女性倚靠在豪华跑车上，通过使用刺眼的直射相机闪光灯，以营造出电影般的、富有氛围感的效果。

![狗仔队风格 夜间照片 提示词，直射闪光](https://cms-assets.youmind.com/media/1774679882303_bfv8u1_HEcR8lhbUAALCTh.jpg)
![狗仔队风格 夜间照片 提示词，直射闪光](https://cms-assets.youmind.com/media/1774679882451_hghx2x_HEcR9EQbwAAo8sc.jpg)
![狗仔队风格 夜间照片 提示词，直射闪光](https://cms-assets.youmind.com/media/1774679882493_ss3e9d_HEcR90JaAAAvQkO.jpg)

```
ultra realistic night photo of a woman leaning on the hood of a luxury sports car, dark outdoor setting, taken with direct flash, strong shadows and highlights, cinematic night mood,

car: sleek modern sports car, matte dark grey/black finish, glossy reflections, aggressive headlights slightly visible,

outfit: tight black fitted t-shirt with minimal text ("CODE"), high-waisted loose grey jeans, casual streetwear aesthetic,

appearance: long straight dark hair, natural makeup, soft glow skin, confident relaxed expression,

pose: leaning back on car hood with both hands, slight tilt of head, looking directly at camera, effortless attitude,

lighting: harsh direct camera flash, high contrast, bright subject with dark background, realistic flash shadows, paparazzi vibe,

composition: slightly top-down angle, centered subject, car filling background, moody framing,

style: luxury street aesthetic, night lifestyle photography, candid but editorial, ultra detailed, sharp focus, realistic skin texture, no watermark --ar 2:3 --style raw --v 7 --stylize 100
```

[[Female Portrait]] [[Direct Flash Photography]] [[Cinematic Atmosphere]] [[Luxury Sports Car]]

---

### 133. 坦率的夜间都市肖像

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-03-18  **Language**: en

> 一个结构化的提示，用于生成一张年轻女性的坦率特写肖像，她靠在夜间户外停车场的一辆深色 SUV 旁，画面中有一只画外的手捏着她的脸颊，呈现出一种 playful 的互动。该提示详细说明了相机设置、灯光、色彩科学和具体的身体比例。

![坦率的夜间都市肖像](https://cms-assets.youmind.com/media/1773902659931_s0b7ei_HDuh6JjaIAEj7KR.jpg)

```
{
  "aspect_ratio": "3:4",
  "photo_style": "casual everyday smartphone photo",
  "subject": "A young woman with long, straight dark hair, wearing a light blue zip-up long-sleeve top with contrast stitching, having her cheek playfully pinched by an out-of-frame hand.",
  "environment": "An outdoor parking lot at night, paved ground, several parked cars in the background, and distant apartment buildings with warm interior lights.",
  "scene_structure": "Subject in the immediate foreground leaning against a dark SUV on the left; an arm enters from the right mid-ground; background features a receding line of cars and urban architecture.",
  "composition": "Close-up portrait shot, subject slightly off-center to the left, leaning against a car that creates a diagonal leading line; eye-level framing.",
  "pose_structure": "Subject leaning back against the car; head tilted slightly toward the camera; neutral, slightly pouted expression; right cheek compressed by a hand pinching it; arms down at sides (implied).",
  "camera": {
    "device": "smartphone camera",
    "angle": "slight high-angle downward tilt",
    "height": "chest level",
    "distance": "close-up",
    "perspective": "natural wide-angle smartphone perspective",
    "depth_of_field": "deep focus"
  },
  "lighting": {
    "type": "natural night ambient light",
    "source": "overhead street lamps and distant building lights",
    "direction": "top-down and frontal fill",
    "shadow_softness": "soft natural shadows",
    "exposure": "balanced smartphone exposure with preserved highlights on skin"
  },
  "color_science": {
    "style": "natural smartphone colors",
    "white_balance": "neutral with slight warm highlights",
    "contrast": "normal",
    "saturation": "natural slightly vibrant"
  },
  "body_proportions": "Slender build with visible curves; prominent bust size relative to a narrow waist; petite frame; long, thin neck; symmetrical shoulder alignment.",
  "facial_details": "Large light-colored eyes with long lashes; groomed dark eyebrows; full lips with a slight pout; soft facial contouring with pinkish blush; natural skin texture.",
  "materials_and_textures": "Ribbed or soft jersey fabric of the blue top; metallic and glossy finish of the car; matte asphalt texture; silky hair texture.",
  "atmosphere": "Candid, late-night urban vibe; casual and playful interaction.",
  "generation_prompt": "A 3:4 casual smartphone photo of a young woman with long straight black hair and light eyes leaning against a dark car at night in a parking lot. She wears a light blue zip-up top with blue contrast stitching. An out-of-frame hand is pinching her right cheek, causing a slight pout. The woman has a slender waist and a proportionally large bust. High-angle perspective, deep focus with parked cars and city buildings visible behind her. Natural night lighting from street lamps, realistic skin texture, slight sensor noise, everyday candid snapshot, 3:4 aspect ratio.",
  "negati
```

[[Female Portrait]] [[Bokeh Background]] [[Night Photography]] [[Playful Interaction]]

---

### 134. 超逼真高定时装社论肖像

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-03-18  **Language**: en

> 一个为 Nano Banana 2 设计的详细 JSON 提示，旨在生成一张超写实、高端时尚的女性肖像，置身于复古摩登的高档霓虹俱乐部场景中，重点突出强烈的灯光、锐利的细节和自信的氛围。

![超逼真高定时装社论肖像](https://cms-assets.youmind.com/media/1773902653764_d68ita_HDsmZZaa4AAJ6uX.jpg)
![超逼真高定时装社论肖像](https://cms-assets.youmind.com/media/1773902653896_7p4vo5_HDsmZVVXUAALGyn.jpg)
![超逼真高定时装社论肖像](https://cms-assets.youmind.com/media/1773902653744_n23d9m_HDsmZiVbQAAwgvJ.jpg)

```
{
  "prompt": {
    "core": "Ultra-photorealistic raw-style 8K iPhone 15 Pro Max high-fashion editorial portrait, vertical 9:16, medium-full body from mid-thigh up",
    "subject": "young woman, light warm skin with realistic pores & natural sheen, long blonde voluminous wavy hair, warm brown eyes with intense confident direct gaze, subtle closed-mouth smile",
    "outfit": "white sleeveless ribbed turtleneck top, short white pleated skirt with ruffle hem, sheer black floral lace thigh-high stockings, glossy black slingback stiletto heels with bow accents, thin silver bracelet on right wrist"
  },
  "environment": {
    "setting": "retro-modern upscale neon club interior",
    "background": "dark polished wood floor with reflections, round marble tables, glowing neon signs including small elegant 'KeorUnreal', pin-up artwork & vintage posters on walls",
    "atmosphere": "moody bold nightlife luxury with intense neon drama"
  },
  "lighting": {
    "description": "clashing neon pink & green flood, dramatic high-contrast shadows, vivid specular highlights on hair, skin, lace, fabrics, leather & heels, strong rim & neon wrap"
  },
  "camera": {
    "framing": "medium-full body, eye-level slight upward tilt, straight-on to three-quarter view",
    "focus": "deep DoF, razor-sharp across subject and readable background",
    "aspect_ratio": "9:16"
  },
  "style": {
    "aesthetic": "ultra-photorealistic high-fashion editorial, raw iPhone capture, cinematic neon drama, confident modern luxury vibe",
    "quality": "8K hyper-detailed, realistic skin texture, hair strands, lace pattern, fabric details, neon reflections, no smoothing, no plastic look"
  }
}
```

[[Female Portrait]] [[Dramatic Lighting]] [[High Fashion Editorial]]

---

### 135. 路边一位女士的随拍智能手机照片

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-03-16  **Language**: en

> 一个高度结构化的 JSON 提示，用于 Nano Banana Pro，详细描述了一张年轻女性坐在郊区水泥路边，随手用智能手机拍摄的日常照片，其中指定了长宽比、主体细节、环境、构图、相机设置和光线。

![路边一位女士的随拍智能手机照片](https://cms-assets.youmind.com/media/1773729523482_mp4h53_HDjaIHyXMAA8-t5.jpg)

```
{
  "aspect_ratio": "3:4",
  "photo_style": "casual everyday smartphone photo",
  "subject": "A young woman with long, wavy light brown hair and curtain bangs, sitting casually on a concrete curb. She is wearing a yellow and green 'BRASIL' tank top and matching green athletic shorts with yellow stripes. She has a small gold cross necklace and a simple silver bracelet.",
  "environment": "A suburban residential sidewalk during the late afternoon. Behind her are green manicured bushes, palm trees, and a two-story house with a brown tiled roof under a clear blue sky.",
  "composition": "Full body shot, centered subject, sitting on the edge of the curb with legs extended toward the bottom left corner. The camera is at a slightly high angle, looking down.",
  "camera": {
    "angle": "slightly high angle",
    "distance": "medium shot",
    "perspective": "eye-level point-of-view from a standing person",
    "depth_of_field": "deep focus"
  },
  "lighting": {
    "type": "natural light",
    "source": "late afternoon sun",
    "shadow_softness": "soft natural shadows",
    "exposure": "normal"
  },
  "color_science": {
    "style": "natural colors",
    "white_balance": "neutral",
    "contrast": "normal"
  },
  "materials_and_textures": "Ribbed cotton fabric of the tank top, smooth concrete sidewalk, leafy textures of suburban shrubbery, and realistic skin texture with natural sheen.",
  "atmosphere": "Relaxed, casual summer afternoon vibe.",
  "generation_prompt": "A casual everyday smartphone photo with a 3:4 aspect ratio. A young woman with wavy light brown hair and bangs sits on a concrete sidewalk curb in a sunny suburban neighborhood. She is wearing a yellow tank top that says 'BRASIL' in green letters and matching green shorts. The background shows green bushes, palm trees, and a house with a tile roof. Everything is in sharp focus with no background blur. Natural late afternoon sunlight, simple shadows, and realistic skin tones. No professional editing, no filters, looks like a quick snapshot taken on a phone camera."
}
```

[[Female Portrait]] [[Smartphone Photography]]

---

### 136. 赛博朋克肖像 JSON 提示词

**Author**: [Ralph the Creator](https://x.com/RalphTheMaker)  **Date**: 2026-03-16  **Language**: en

> 一个结构化的 JSON 提示词，用于 Nano Banana Pro 生成一张超详细的赛博朋克风格赛博哥特女性肖像，该女性带有霓虹电路纹身，重点突出光照、风格和高分辨率质量。

![赛博朋克肖像 JSON 提示词](https://cms-assets.youmind.com/media/1773729507119_ods2s4_HDhw-rXXAAAZnvv.jpg)

```
{
  "subject": "{argument name="subject" default="cybergoth woman with neon circuit tattoos"}",
  "description": "pale synthetic complexion, dark metallic lipstick, intense gaze directed at the viewer",
  "lighting": "vivid holographic glow with magenta and cyan edge lighting",
  "camera": "captured on a futuristic mirrorless sensor rig, 85mm f/1.2 lens, deep atmospheric bokeh",
  "style": "cyberpunk portraiture, techno-goth aesthetic, high-contrast digital realism",
  "quality": "ultra high resolution, hyper-detailed textures, cinematic sci-fi realism"
}
```

[[Female Portrait]] [[Dramatic Lighting]] [[Sci-Fi Portrait]]

---

### 137. 明亮清晨街头时尚肖像

**Author**: [Nikhil](https://x.com/NikhilRajX)  **Date**: 2026-03-16  **Language**: en

> 为 Nano Banana 2 生成一张编辑风格、超细节图像的详细提示，描绘了一位穿着街头时尚的年轻女性在日出时分坐在城市人行道边，其中包含具体的服装和光照细节。

![明亮清晨街头时尚肖像](https://cms-assets.youmind.com/media/1773729509536_f3mpai_HDgpHuPaEAAzQkx.jpg)

```
Bright morning street fashion: young woman sitting relaxed on city sidewalk curb at sunrise, wearing {argument name="outfit" default="black oversized hoodie, light gray cargo pants, white sneakers, black baseball cap worn backward"}, silver chain necklace, small black crossbody bag placed beside her, holding phone casually in one hand, leaning back in relaxed pose with other hand on head, golden warm sunrise light, urban arches background, editorial style photography, highly detailed, 8K
```

[[Female Portrait]] [[Natural Lighting]] [[Editorial Fashion Portrait]]

---

### 138. 赛博朋克科学肖像

**Author**: [Aijaz](https://x.com/iamsofiaijaz)  **Date**: 2026-03-15  **Language**: en

> 一个电影特写镜头提示，用于 Nano Banana 2 生成一张年轻女性的肖像，她头发湿漉漉的，脸上投射着数学公式和科学方程式，呈现出黑暗、忧郁、高对比度的赛博朋克美学。

![赛博朋克科学肖像](https://cms-assets.youmind.com/media/1773643978890_2n6bg6_HDdEWxPbkAAAmCm.jpg)

```
Make a cinematic close-up portrait of a young woman’s face in side profile, wet hair strands on her skin, intense reflective eyes, mathematical formulas and scientific equations projected across her face and neck, glowing white handwritten symbols, physics diagrams and abstract calculations overlay, futuristic holographic projection, dark moody background, dramatic lighting, high contrast, detailed skin texture, cyberpunk science aesthetic, shallow depth of field, volumetric lighting, photorealistic, 8k, film still, sci-fi atmosphere.
```

[[Female Portrait]] [[Cyberpunk Aesthetic]] [[Wet Hair Portrait]]

---

### 139. 单色粉红时尚大片与猫咪

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-03-14  **Language**: en

> 一个用于生成高度风格化、单色粉色时尚编辑肖像的提示。图像中，一位女性自信地坐在一张长毛绒粉色人造毛扶手椅上，周围对称地环绕着多只毛茸茸的猫咪，强调奢华的质感和超逼真的高细节美学。

![单色粉红时尚大片与猫咪](https://cms-assets.youmind.com/media/1773556642929_jnmuv8_HDWZyaxaMAg7jF_.jpg)

```
Using the uploaded picture as the only reference and without changing the face, create a fashion editorial portrait of a woman sitting confidently in a plush oversized pink faux-fur armchair against a soft pastel pink background; she wears a fluffy pink jacket, white trousers and white lace-up boots, seated with legs crossed and a calm confident expression; surrounded symmetrically by multiple fluffy long-haired cats in cream, gray and white tones perched on the chair arms, backrest and floor around her; highly stylized monochromatic pink aesthetic, soft studio lighting, clean background, luxurious textures in fur fabric and cat fur, centered composition, fashion magazine style, high detail, shallow depth of field, ultra-sharp textures, high dynamic range, 8k ultra-photorealism, masterpiece quality.
```

[[Female Portrait]] [[Fashion Editorial Portrait]]

---

### 140. 灵动肖像，俏皮眨眼

**Author**: [Luxerelia](https://x.com/_dailyboost)  **Date**: 2026-03-13  **Language**: en

> 一个详细的提示，用于生成一张空灵、电影感的年轻女性肖像，她正在俏皮地眨眼。提示中指定了柔和、发光的皮肤纹理，休闲时尚的街头服饰（白色背心、橄榄色飞行夹克、牛仔裤），温暖的午后阳光营造出光晕效果，以及带有奶油般虚化的浅景深。

![灵动肖像，俏皮眨眼](https://cms-assets.youmind.com/media/1773469783915_gqfyx9_HDT0X9KaMAEbeBj.jpg)

```
Ethereal portrait of a charming young woman in her early twenties, captured in a relaxed candid moment, giving a gentle playful wink toward the camera with a dreamy, slightly mischievous expression. Her skin appears porcelain-smooth with a natural glow, lightly dusted with faint freckles across the bridge of her nose and cheeks. She has soft glossy lips with subtle natural makeup, delicate blush on her cheeks, and luminous skin tones that catch the warm afternoon sunlight.
Her hair falls naturally around her shoulders, softly tousled by a light breeze, with individual strands illuminated by golden sunlight. The lighting creates a glowing halo effect around her silhouette, producing a dreamy, almost cinematic atmosphere.
She is wearing a simple white cropped tank top paired with a loose olive-green bomber jacket draped casually over her shoulders, giving a relaxed yet stylish street-fashion vibe. The outfit is completed with light-wash vintage-style denim jeans and a classic black belt, creating a balanced casual-chic look that feels effortless and modern.
The background is softly blurred with creamy bokeh, suggesting an outdoor urban setting during a warm afternoon. The sunlight filters through the environment, creating soft highlights, gentle shadows, and a nostalgic film-photography aesthetic. The scene feels airy, romantic, and slightly whimsical.
Shot in a cinematic film photography style using a high-end portrait lens ({argument name="lens focal length" default="85mm"}, f/1.4), shallow depth of field, soft focus falloff, natural color grading, subtle film grain, and warm tones. Ultra-realistic skin texture, visible pores and fine details, photorealistic lighting, high dynamic range, extremely detailed fabric textures, professional fashion photography composition, masterpiece quality, 8k ultra-high resolution.
```

[[Female Portrait]] [[Natural Light Photography]] [[Candid Expression]]

---

### 141. 安雅·泰勒-乔伊 (Anya Taylor-Joy) 相似者的超逼真肖像

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-03-13  **Language**: en

> 一个为 Nano Banana 2 设计的详细、超真实感提示，用于生成一张酷似安雅·泰勒-乔伊 (Anya Taylor-Joy) 的女性的私密、抓拍肖像。该提示细致地定义了场景、光线（柔和的室内日光）、拍摄对象的着装（格子套装配红色蝴蝶结）、姿势（坐在白色亚麻布上），以及诸如涂有亮红色指甲油的完美赤脚等具体细节。

![安雅·泰勒-乔伊 (Anya Taylor-Joy) 相似者的超逼真肖像](https://cms-assets.youmind.com/media/1773469775721_o70s6a_HDTChPlWkAIeAca.jpg)

```
{
    “quality”: “ultra_photorealistic, raw style, 8k”,
    “camera”: “iPhone 15 Pro Max”,
    “lighting”: “soft, natural indoor daylight, subtle bedroom shadows”,
    “style”: “intimate, candid portrait, detailed focus”,
    “aspect_ratio”: “3:4”
  },
  “scene”: {
    “location”: “A minimalist, bright indoor bedroom setting. A bed with white rumpled linen sheets and pillows against a plain white wall.”,
    “atmosphere”: “Candid, stylish, relaxed.”
  },
  “subject”: {
    “gender”: “female”,
    “name”: “{argument name="celebrity lookalike" default="Anya Taylor-Joy"}”,
    “body”: {
      “type”: “Naturally slim and toned physique, in a seated pose on the white bed sheets, legs crossed with one leg extended forward and the other tucked. All visible skin on her body, including her legs, feet, and ankles, is completely smooth, clean, flawless, and free of any tattoos or marks.”
    },
“face”: {
      “features”: “Striking features with a clear direct gaze towards the camera, detailed eye makeup with winged eyeliner, and a soft red lip color. Her platinum blonde hair is styled with soft waves and adorned with a large, prominent bright red bow headband.”,
      “expression”: “Confident, direct gaze.”
    },
    “outfit”: {
      “description”: “A two-piece blue and white gingham coordinate set. Spaghetti strap crop top with red embroidery (heart and cherry cluster motif) on the chest and white scalloped lace trim. Matching pleated mini-skirt with matching scalloped lace hem, in a classic mini length.”,
      “fit”: “Tailored, form-fitting, chic.”,
      “accessory”: “Blue cube-like geometric stud earrings. A small white clutch purse with gold hardware is visible on the bed in the foreground corner.”
    },
“pose”: “Seated on the white bed sheets, legs crossed with one foot resting on the sheet and the other tucked. Left arm extended backward, right hand supporting her on the sheet, with a direct gaze at the camera.”,
    “footwear”: “Explicitly and completely barefoot. No mules or slippers.”,
    “details”: “Her bare toes are clearly visible resting on the white linen sheet, and all toenails are painted with a vibrant, glossy, polished red nail polish.”
  },
  “composition”: “Medium full-body shot, capturing her from head to foot, high-angle perspective. Sharp focus on all details: Anya Taylor-Joy’s face, the red bow, the intricate gingham fabric of the classic mini-skirt, and the barefoot toes with glossy red polish. The white bed setting and clutch are clear but softly blurred.”
}
```

[[Female Portrait]] [[Photorealistic Portrait]] [[Face Preservation]] [[Anya Taylor-Joy]]

---

### 142. Nano Banana Pro 2.0 的街头艺术数字插画提示

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-12  **Language**: en

> 一个用于 Nano Banana Pro 2.0 的提示，将一张年轻女性的上传照片转换为细节丰富的数字插画，采用充满活力的街头艺术风格，并指定发色、配饰和背景纹理。

![Nano Banana Pro 2.0 的街头艺术数字插画提示](https://cms-assets.youmind.com/media/1773383495584_l52gkg_HDN6ZKkXcAAOLZJ.jpg)

```
A highly detailed, 4K digital illustration of a smiling young woman [ use the uploaded photo as reference] in a medium close-up portrait. She has voluminous curly ombre hair transitioning from dark blue to neon green, accessorized with a pearl headband and dangling earrings. She wears a black top, and her shoulder features vibrant floral tattoos. Bright, even lighting illuminates her face. The background is a textured light gray wall covered in energetic black, red, yellow, and blue paint splatters. The overall mood is cheerful, artistic, and vibrant. Highly detailed, vertical portrait.
```

[[Female Portrait]] [[Digital Illustration]]

---

### 143. 弱光 iPhone 写实连帽衫肖像提示词，适用于 Nano Banana 2

**Author**: [babydoll](https://x.com/bananababydoll)  **Date**: 2026-03-12  **Language**: en

> 一个结构化的 JSON 提示词，用于 Nano Banana 2 生成一张超写实、低光照的纹身女性肖像，她穿着一件超大号连帽衫，模拟 iPhone 摄像头的真实感，并包含特定的光照、姿势和身体细节。

![弱光 iPhone 写实连帽衫肖像提示词，适用于 Nano Banana 2](https://cms-assets.youmind.com/media/1773383496952_kdcv59_HDNn2w-WgAEGHnF.jpg)
![弱光 iPhone 写实连帽衫肖像提示词，适用于 Nano Banana 2](https://cms-assets.youmind.com/media/1773383496995_ib9yl0_HDNn2ifbQAQgXee.jpg)

```
{
  "meta": {
    "camera": "iPhone 17 Pro",
    "lens": "48mm",
    "aspect_ratio": "2:3",
    "style": "low light iphone realism, dark influencer mood",
    "quality": "ultra photorealistic",
    "time_of_day": "1:07 AM",
    "lighting_temperature": "warm side lamp 3000K with cool shadow falloff",
    "natural_mobile_hdr": true,
    "slight_handheld_motion": true,
    "realistic_depth_of_field": true,
    "authentic_iphone_color_science": true
  },

  "character_lock": {
    "face": "pale alternative beauty, confident calm expression",
    "body": "extreme hourglass silhouette, narrow waist, pronounced hips",
    "hair": "dark, damp, brushed back loosely",
    "tattoos": "large chest piece, mandala abdomen tattoo, full sleeve tattoos"
  },

  "scene": {
    "location": "dark loft bedroom",
    "background": "minimal industrial wall, dim warm lamp"
  },

  "pose": {
    "position": "sitting on bed edge, one knee raised",
    "expression": "slow controlled half-smirk",
    "camera_angle": "slightly low handheld candid"
  },

  "outfit": {
    "top": "oversized deep charcoal hoodie, worn without bra, fabric softly draped over chest",
    "bottom": "bare legs visible, hoodie hem resting high on thighs"
  },

  "details": {
    "tattoo_visibility": "chest and arm tattoos softly highlighted under warm light",
    "skin_texture": "subtle damp glow, visible oblique definition",
    "grain": "soft night grain preserved"
  }
}
```

[[Female Portrait]] [[Photorealistic Rendering]] [[Low Light Photography]] [[iPhone Camera Simulation]]

---

### 144. 动作视频游戏角色 Cosplay 镜面自拍提示词，适用于 Nano Banana Pro

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-03-12  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana Pro 生成一张逼真的、自然的镜子自拍，内容是一位年轻女性穿着动作视频游戏角色扮演服装，其中详细说明了服装、配饰、环境和构图。

![动作视频游戏角色 Cosplay 镜面自拍提示词，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1773383491890_c4n0p5_HDMF1V9WwAAqJO_.jpg)

```
{
  "image_prompt": {
    "subject": {
      "gender": "female",
      "age_appearance": "young adult",
      "hair": "long, straight, light brown hair with face-framing bangs",
      "expression": "thoughtful or slightly pouting, with one index finger resting near her lip",
      "pose": "kneeling or sitting on the floor, taking a mirror selfie"
    },
    "attire": {
      "top": "white sleeveless crop top",
      "bottom": "black pleated mini skirt with a branded waistband",
      "hosiery": "black sheer tights or pantyhose",
      "accessories": [
        "black fingerless gauntlet gloves extending up the forearms with silver and red accents",
        "black straps or suspenders over the shoulders",
        "black band around the left upper arm"
      ],
      "style": "action video game character cosplay"
    },
    "props": {
      "item": "white smartphone",
      "details": "white pop-it style textured phone case"
    },
    "environment": {
      "setting": "casual indoor bedroom or living space",
      "flooring": "textured beige or light grey carpet",
      "background_elements": [
        "white paneled interior door",
        "wall covered with a collage of photos and a white angel wings decoration",
        "white shelving unit holding various small items and plushies",
        "white sofa or futon",
        "large blue and white plush cushion",
        "pink tumbler cup sitting on the floor"
      ]
    },
    "composition": {
      "camera_angle": "high angle, mirror reflection",
      "lighting": "soft indoor room lighting",
      "style": "photorealistic, candid mirror selfie"
    }
  }
}Add this face

{
  "image_prompt": {
    "subject": {
      "gender": "female",
      "age_appearance": "young adult",
      "hair": "long, straight, light brown hair with face-framing bangs",
      "expression": "thoughtful or slightly pouting, with one index finger resting near her lip",
      "pose": "kneeling or sitting on the floor, taking a mirror selfie"
    },
    "attire": {
      "top": "white sleeveless crop top",
      "bottom": "black pleated mini skirt with a branded waistband",
      "hosiery": "black sheer tights or pantyhose",
      "accessories": [
        "black fingerless gauntlet gloves extending up the forearms with silver and red accents",
        "black straps or suspenders over the shoulders",
        "black band around the left upper arm"
      ],
      "style": "action video game character cosplay"
    },
    "props": {
      "item": "white smartphone",
      "details": "white pop-it style textured phone case"
    },
    "environment": {
      "setting": "casual indoor bedroom or living space",
      "flooring": "textured beige or light grey carpet",
      "background_elements": [
        "white paneled interior door",
        "wall covered with a collage of photos and a white angel wings decoration",
        "white shelving unit holding various small items and plushies",
```

[[Female Portrait]] [[Photorealistic Rendering]] [[Mirror Selfie Portrait]] [[Cosplay Photography]]

---

### 145. 创意数字合成智能手机快照提示

**Author**: [Layla 🌙](https://x.com/BananaPromptPro)  **Date**: 2026-03-11  **Language**: en

> 一个极其详细的 JSON 格式提示，专为 Nano Banana Pro 设计，用于创建一张创意数字合成图像：一位年轻女性似乎从智能手机屏幕中探出身来，强调逼真的皮肤纹理、生物特征以及特定的服装/姿势细节。

![创意数字合成智能手机快照提示](https://cms-assets.youmind.com/media/1773297039037_8o4jx0_HDJI-xHbEAAV0lH.jpg)

```
{
  "photo_type": "Creative digital composite smartphone snapshot",
  "subject": {
    "age": "Early 20s",
    "body_type": "Slim",
    "description": "A young American woman appearing to lean out of an iPhone screen into the physical world, creating a 3D pop-out effect.",
    "ethnicity": "American",
    "expression": "Playful pouting duck-face with eyes looking slightly upward",
    "gender": "Female",
    "mirror_rules": "Not a mirror selfie; the subject is framed within a camera app UI on a smartphone screen held by another hand.",
    "pose_description": "Leaning forward with both hands extended forward, one hand holding a small round pastry topped with sesame seeds and jam.",
    "tattoos": "None"
  },
  "clothing": {
    "bottom": {
      "color": "Not visible",
      "details": "N/A",
      "fabric": "N/A",
      "type": "N/A"
    },
    "fit_and_physics": "The cotton t-shirt shows minor bunching at the armpits as she leans forward; the baseball cap sits naturally on her head with a stiff brim.",
    "outerwear": {
      "color": "N/A",
      "details": "N/A",
      "fabric": "N/A",
      "type": "N/A"
    },
    "shoes": {
      "color": "N/A",
      "details": "N/A",
      "fabric": "N/A",
      "type": "N/A"
    },
    "top": {
      "color": "Chocolate brown and dusty pink",
      "details": "Ringer-style t-shirt with pink sleeves and brown torso",
      "fabric": "Soft cotton jersey",
      "type": "Short-sleeve t-shirt"
    }
  },
  "hair": {
    "color": "blond",
    "interaction": "Tucked behind ears and under the baseball cap",
    "style": "Straight, medium-length hair falling over her shoulders"
  },
  "face": {
    "description": "Youthful features with a soft jawline and rounded cheeks accentuated by the pout.",
    "eyebrows": "Groomed and arched",
    "eyes": "Dark brown with sharp corneal reflections and visible wetness on the lower lids",
    "lips": "Pursed and pouting, natural pink tint",
    "makeup": "Minimal, no-makeup look with a slight sheen on the lips"
  },
  "skin_texture": "Natural skin with visible micro-pores on the nose and cheeks, slight oily sheen on the T-zone, and fine lines around the mouth from the expression.",
  "biological_features": {
    "eye_complexity": "Realistic sclera with faint vascularity; detailed iris patterns.",
    "hair_strand_physics": "Individual stray hairs visible near the temples and under the cap brim.",
    "skin_micro_texture": "Fine vellus hair (peach fuzz) visible along the jawline under the bright light.",
    "subsurface_scattering": "Visible through the fingertips holding the phone and the edges of the ears.",
    "vascularity_and_pigment": "Faint blue veins visible on
```

[[Female Portrait]] [[Photorealistic Rendering]] [[Surreal Photography]] [[Skin Texture]]

---

### 146. 超写实肖像，强调乳沟和质感

**Author**: [Jessia](https://x.com/itsjessiababy)  **Date**: 2026-03-11  **Language**: en

> 为 Nano Banana Pro 设计的、高度具体且结构化的提示，旨在生成一张超逼真的年轻女性图像。该女性拥有深色波浪发、锐利的眼神，身穿紧身白色背心，对皮肤纹理、光线以及胸部的解剖学细节进行了极致的刻画。

![超写实肖像，强调乳沟和质感](https://cms-assets.youmind.com/media/1773297031809_mi7op3_HDIT7rTWsAAFthU.jpg)

```
{
"subject": "A beautiful young woman with tanned skin, visible skin pores, and natural skin texture. She has voluminous, dark brown wavy hair that falls heavily over her right shoulder and cascades onto the white bedding. Her facial features include striking light green-hazel eyes, dark dramatic eyelashes, shaped eyebrows, rosy cheeks, and full, glossy pink lips. She is wearing a tight, thin, white ribbed tank top with a deep scoop neckline and delicate lace trim. The subject has an exceptionally large, heavy, and natural bust with deep cleavage clearly emphasized by the fitted top, gravity, and forward projection. Bust depth is visibly greater than the ribcage depth. She is also wearing light blue denim shorts, unbuttoned at the waist to reveal her lower stomach and navel.",
"pose": "Reclining backward onto a soft, heavily textured white duvet or pillow surface. Her right shoulder is angled slightly forward. Her left arm is bent, with her left hand resting naturally near her hip and upper thigh. Her spine has a slight arch. Her head is tilted slightly down, but her gaze is directed upwards, making intense, direct eye contact with the camera.",
"environment": "An indoor room setting. The immediate background is a large, rumpled, textured white blanket or soft pillow supporting the subject. Further back, there is a wall featuring gray and beige geometric panels, and a framed glass or mirror surface reflecting a small, spiky green potted plant.",
"camera": "Medium close-up shot captured from a slightly elevated, high angle, looking down at the subject. The framing and perspective heavily prioritize the foreground depth and volume of the chest relative to the face and torso. Strong three-dimensional depth with no first-person, selfie, or mirror-selfie framing.",
"lighting": "Soft, diffused natural daylight coming from the front and slightly left, creating glowing specular highlights on her nose, cheekbones, lips, collarbones, and upper chest. Soft shadows accurately define the cleavage and facial contours without harsh contrast, preserving natural subsurface skin scattering.",
"mood_and_expression": "Confident, sultry, relaxed, and alluring. She has a subtle, slightly parted-lip expression with a captivating and intense upward gaze.",
"style_and_realism": "Ultra-photorealistic, high-fidelity, unedited raw photography. Strict anatomical fidelity, maintaining exact body proportions, soft tissue weight, and visible micro-details. No airbrushing, no beauty filters, and no artificial smoothing.",
"colors_and_tone": "Warm, golden bronze skin tones contrasting against crisp white fabric and bedding. Muted cool grays, beiges, and organic greens in the background. Natural white balance, accurate skin tone, and natural dynamic range.",
"quality_and_technical_details": "8k resolution, razor-sharp focus on the face and eyes, highly detailed fabric textures showcasing the cotton "
}
```

[[Female Portrait]] [[Photorealistic Rendering]] [[Skin Texture Detail]] [[Dark Wavy Hair]]

---

### 147. 超现实强迫透视微缩女人

**Author**: [Hania Ai](https://x.com/HaniaAi12)  **Date**: 2026-03-11  **Language**: en

> 给 Nano Banana 2 的一个提示：生成一张超现实的、高角度的、第一人称视角的图像，画面中一只手拿着智能手机，一个迷你女人通过强制透视从手机中出现，摄影师的脚在画面底部可见。

![超现实强迫透视微缩女人](https://cms-assets.youmind.com/media/1773297032680_mvkcjh_HDF3k6jaMAUtfwn.jpg)

```
A surreal, high-angle first-person perspective looking down at a sunlit paved sidewalk with dappled shadows. A hand wearing a watch and bracelet holds a smartphone displaying a camera UI. A miniature woman emerges from the device via forced perspective: her lower half stands inside the digital screen, while her upper torso, wearing a light blue strapless dress and black shoulder bag, extends physically into the real world. The subject features the uploaded face as reference. The photographer's sandaled feet appear at the bottom edge. Shot with a 24mm lens, bright natural daylight, 8k Octane Render, raytracing, highly intricate textures, subsurface scattering.. 2:3r
```

[[Female Portrait]] [[Surreal Photography]] [[Forced Perspective]] [[Overhead Shot]]

---

### 148. 特写肖像与参考提示

**Author**: [David](https://x.com/tealdog2)  **Date**: 2026-03-10  **Language**: en

> 一个详细的提示，用于生成一张年轻女性的特写肖像，具有特定的面部特征、珠宝和光线，使用参考图像（来自 Grok Imagine）但排除头巾，使用 Nano Banana Pro 生成。

![特写肖像与参考提示](https://cms-assets.youmind.com/media/1773210656679_kxhonl_HDE-gB0aMAE5_ee.jpg)

```
Close-up portrait of a young woman with a natural smile, looking at the camera. She has long dark hair, parted in the middle. Her striking green eyes have long lashes and dark, full eyebrows. She wears a silver crescent nose ring and multiple ear piercings on her right ear, including a silver dangle earring with a dark square stone. Her lips are glossy pink, showing white teeth. Her fingers with light pink nails gently touch the hair on the right. She wears a delicate silver chain necklace. Soft, natural lighting against a blurred dark grey background. Realistic photography, natural aesthetic.
```

[[Female Portrait]] [[Photorealistic Rendering]] [[Face Reference Photography]]

---

### 149. 手持镜子自拍的详细 JSON 提示词

**Author**: [Layla 🌙](https://x.com/BananaPromptPro)  **Date**: 2026-03-09  **Language**: en

> 一个高度详细的 JSON 格式提示，用于 Nano Banana 2 生成一张年轻女性手持镜子自拍快照。该提示详细说明了主体体型、服装合身度（紧绷在丰满胸部上的开衫）、纹身、发型以及镜子外观（镜像文字、指纹）。它明确要求使用上传的角色参考图像来生成面部。

![手持镜子自拍的详细 JSON 提示词](https://cms-assets.youmind.com/media/1773124334815_cuwb1j_HC_GVWQaYAAfhyz.jpg)

```
{
  "photo_type": "Handheld mirror selfie snapshot captured on an iPhone 16 Pro front camera with typical arm distortion and lens curvature.",
  "subject": {
    "age": "Early 20s",
    "body_type": "Young Woman, Large round breast shape, prominent projected profile, fuller bust measurement, large-breasted proportions, fuller chest frame, shapely upper silhouette, top-heavy silhouette, buxom figure, high waist-to-hip contrast, defined waistline, Large fuller glute measurement, curvy, prominent hips, rounded hip contour, curvy lower body, thick, powerful thighs, full thighs, push-up bra effect.",
    "description": "The subject is a young woman with a buxom figure and a heart-shaped face, sporting short dark wavy hair and extensive black ink tattoos across her chest and neck.",
    "ethnicity": "Na",
    "expression": "Direct gaze with a slight, seductive pout",
    "gender": "Female",
    "mirror_rules": "Tattoos and text should appear mirrored; faint fingerprints and dust on the mirror surface reflect the indoor ceiling light.",
    "pose_description": "Subject is taking a selfie with a phone, one hand is brought up to her chin with a finger lightly resting on her lip, showing off hand tattoos and long decorated nails.",
    "tattoos": "Location: Forehead, neck, chest, hand. Motif: Black script 'Bite' on forehead, large intricate moth with spread wings on the chest, black ornamental linework on the neck, and 'yours' script with a heart on the hand."
  },
  "clothing": {
    "bottom": {
      "color": "Unknown",
      "details": "Out of frame",
      "fabric": "Unknown",
      "type": "Casual bottoms"
    },
    "fit_and_physics": "The ribbed cardigan is strained over the fuller chest frame, showing fabric tension and horizontal compression creases across the knit.",
    "outerwear": {
      "color": "Dark grey",
      "details": "Open front, chunky knit texture",
      "fabric": "Ribbed wool blend",
      "type": "Cardigan"
    },
    "shoes": {
      "color": "None",
      "details": "Out of frame",
      "fabric": "None",
      "type": "None"
    },
    "top": {
      "color": "None",
      "details": "Chest visible under open cardigan",
      "fabric": "None",
      "type": "None"
    }
  },
  "hair": {
    "color": "Dark brown to black",
    "interaction": "Slightly damp strands falling over the forehead and tucked behind ears.",
    "style": "Short, chin-length bob with a thick, wavy, and damp wet-look texture."
  },
  "face": {
    "description": "Use the uploaded character reference image, keep all facial details 100% unchanged",
    "eyebrows": "Thick, dark, and well-defined arches",
    "eyes": "Almond-shaped with dark irises and heavy, voluminous false lashes",
    "lips": "Full, symmetrical with a distinct Cupid's bow and matte nude lipstick",
    "makeup": "Heavy black eyeliner with winged tips, groomed eyebrows, and matte facial finish."
  },
  "skin_texture"
```

[[Female Portrait]] [[Photorealistic Rendering]] [[Candid Snapshot]] [[Face Reference Photography]]

---

### 150. 超写实偷拍卧室肖像

**Author**: [RavelAI](https://x.com/Ravelberger)  **Date**: 2026-02-10  **Language**: en

> 一个为 Nano Banana Pro 设计的详细 JSON 提示，旨在生成一张超写实、自然的年轻女性倚靠卧室门框的肖像。该提示强调自然美、真实的皮肤纹理（细微毛孔，无修饰），以及电影般的灯光（柔和漫射的自然窗光），以实现专业而亲密的智能手机风格照片效果。

![超写实偷拍卧室肖像](https://cms-assets.youmind.com/media/1770792232872_s4ntel_HAuiIXkbgAEk4qS.jpg)

```
{
"subject": {
"description": "Attractive young woman 22-25 years old, natural beauty, fair to light olive skin with subtle pores and faint freckles, long natural wavy brown hair slightly messy, soft everyday makeup with glossy lips and light mascara, slim-toned athletic body with natural curves, realistic proportions",
"clothing": "Fitted white cropped tank top slightly riding up, high-waisted light denim shorts hugging hips naturally, barefoot",
"body_details": "Detailed realistic skin texture with visible pores, subtle veins on arms, natural soft shadows under curves, no airbrushed or plastic look, authentic human imperfections"
},
"pose": {
"type": "Casual seductive lean against bedroom doorframe, one hip cocked to the side, one hand in hair, other resting on thigh, looking directly at camera with soft sultry smile and bedroom eyes",
"expression": "Inviting yet natural confident gaze, slightly parted lips, relaxed shoulders",
"limbs": "Weight shifted to one leg creating gentle S-curve, soft arch in back emphasizing natural waist-to-hip ratio"
},
"environment": {
"setting": "Cozy modern bedroom in soft morning light through sheer curtains, wooden floor, unmade bed in soft focus background",
"foreground": "Subtle natural clutter like phone on nightstand, realistic depth"
},
"lighting": {
"source": "Soft diffused natural window light from side, gentle volumetric god rays, HDR for balanced shadows and highlights",
"quality": "Cinematic yet everyday realism, subsurface scattering on skin, no harsh studio flash"
},
"camera": {
"shot": "Shot on Canon EOS R5 with 85mm lens at f/1.8, creamy bokeh background, shallow depth of field focusing on face and body",
"style": "Hyper-photorealistic candid smartphone-style portrait turned pro, 8k resolution, raw photo feel, natural color grading"
},
"negative_prompt": ["plastic skin", "smooth airbrushed", "CGI", "deformed anatomy", "blurry", "overexposed", "cartoon", "extra limbs", "childlike", "unnatural shine"]
}
```

[[Female Portrait]] [[Hyperrealistic Photography]] [[Skin Texture Detail]] [[Intimate Photography]]

---

### 151. 令人惊叹的夜间人像照片提示

**Author**: [blogbursthub](https://x.com/blogbursthub)  **Date**: 2026-02-10  **Language**: en

> 这是一个专为 Gemini Nano Banana 模型设计的提示词，用于生成一张令人惊艳的高质量夜间肖像照片。用户指出完整的提示词文本可在图像的替代文本中找到。

![令人惊叹的夜间人像照片提示](https://cms-assets.youmind.com/media/1770792209572_e2ylqp_HAxUJ1qbEAAlAQb.jpg)

```
Stunning night time portrait photo
```

[[Female Portrait]] [[Cinematic Photography]]

---

### 152. 地中海生活方式旅行写真

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-02-10  **Language**: en

> 一个详细的 JSON 提示，用于 Gemini Nano Banana Pro 生成一组明亮、通透的地中海村庄生活方式旅行肖像。该提示详细说明了拍摄对象的姿势（站立，回头过肩）、波西米亚风格的服装（白色钩针上衣，蓝色长裙）以及环境（粉刷过的灰泥墙、蓝色门、粉色九重葛），以营造阳光明媚的希腊海岛度假美学。

![地中海生活方式旅行写真](https://cms-assets.youmind.com/media/1770792232674_wfr4jw_HAxKe9LbUAAmyDB.jpg)

```
{ "composition": { "framing": "three-quarter body portrait", "orientation": "vertical", "perspective": "slightly angled side-back view", "balance": "subject placed slightly right of center with architectural elements counterbalancing", "depth": "moderate depth with subject clearly separated from background", "leading_lines": "white wall edges and walkway guide the eye toward the subject" }, "subject": { "type": "single human subject", "pose": "standing, torso turned back toward camera, relaxed posture", "expression": "soft smile with playful confidence", "gaze": "directed toward camera over shoulder", "hair": "long, light brown hair with soft waves", "emotion": "carefree, cheerful, relaxed" }, "apparel": { "top": "white cropped knit top with open crochet pattern and flared sleeves", "bottom": "high-waisted blue tiered maxi skirt with soft drape", "style": "Mediterranean summer casual, bohemian-inspired" }, "accessories": { "eyewear": "black sunglasses worn on head", "bag": "dark red shoulder tote worn on back", "handheld": "disposable coffee cup", "jewelry": "minimal or not clearly visible" }, "color_palette": { "dominant_colors": ["white", "blue"], "secondary_colors": ["pink", "red", "black"], "contrast": "high contrast between bright white architecture and saturated blue accents" }, "lighting": { "type": "natural daylight", "direction": "top-right directional sunlight", "quality": "bright and crisp", "shadows": "defined shadows on wall and ground", "exposure": "high-key with strong highlights and clear detail" }, "environment": { "setting": "Mediterranean exterior", "location_type": "whitewashed residential or boutique street", "materials": ["stucco walls", "painted wood door", "stone pavement"], "context": "coastal or island village atmosphere" }, "background_details": { "architecture": "white stucco walls with vivid blue door and window frames", "natural_elements": ["pink bougainvillea flowers"], "background_activity": "quiet, no visible movement" }, "camera": { "shot_type": "lifestyle travel portrait", "lens_look": "standard focal length with mild background compression", "focus": "sharp focus on subject", "bokeh": "minimal, background mostly in focus", "resolution_feel": "clean, social-media-ready clarity" }, "artistic_style": { "genre": "travel lifestyle photography", "aesthetic": "bright, airy, summery", "editing": "vibrant blues and pinks with clean whites", "inspiration": "Greek island or Mediterranean vacation imagery" }, "textures": { "fabric": ["open-knit crochet", "lightweight flowing cotton"], "surfaces": ["smooth stucco", "painted wood", "stone walkway"], "natural": ["bougainvillea petals"] }, "mood": { "overall_feel": "lighthearted, sunny, leisurely", "seasonal_hint": "summer" }, "typography": { "text_present": false } }
```

[[Female Portrait]] [[Travel Photography]] [[Golden Light]] [[Bohemian Fashion]]

---

### 153. 纽约高级街头时尚（极简奢华风）

**Author**: [Aylin](https://x.com/Ai_aylinfc)  **Date**: 2026-02-10  **Language**: en

> 一个详细的电影风格提示，用于生成一张高级时装街头摄影图片。画面中，一位金发女性身着米白色极简奢华套装（罗纹针织上衣和透明不对称雪纺半身裙），走在经典的纽约市街道上（SoHo/West Village）。该提示包含广泛的技术规格（85mm 镜头，f/1.8 光圈，电影构图，8K 分辨率），以实现《Vogue》/《Harper's Bazaar》杂志的编辑美学效果。

![纽约高级街头时尚（极简奢华风）](https://cms-assets.youmind.com/media/1770792211333_odmw9x_HAxFqH_aAAUIi6e.jpg)

```
Blonde girl with soft golden hair flowing naturally, styled loose with subtle volume, wearing an elegant cream-white minimalist luxury ensemble — a finely woven ribbed knit cropped top with delicate texture, flattering fit, clean neckline and refined craftsmanship, paired with a sheer asymmetric chiffon skirt featuring layered translucent panels, high-low hemline, fluid movement, and graceful drape that catches the sunlight with every step, transparent feather-accent sandals with barely-there straps, airy and couture-inspired, walking mid-stride through a New York City street ({argument name="location" default="SoHo / West Village"} atmosphere), classic urban backdrop with stone buildings, boutique storefronts, fire escapes, blurred yellow taxis and pedestrians in the distance, sunny late-morning summer light, natural golden highlights, soft shadows on concrete, gentle breeze lifting fabric and hair, candid unposed street-style moment, effortless confidence, relaxed shoulders, serene facial expression, minimalist jewelry, natural glowing skin, soft neutral makeup, editorial composition, shallow depth of field, creamy bokeh, cinematic framing, fashion magazine street photography, ultra-detailed fabric textures, realistic skin tones, luxury lifestyle aesthetic, modern femininity, timeless elegance, high fashion minimalism, shot on 85mm lens, f/1.8, ISO 100, sharp focus on subject, subtle motion blur in background, photorealistic, hyper-real detail, Vogue / Harper’s Bazaar street fashion style, 8K ultra-high resolution
```

[[Female Portrait]] [[Street Photography]] [[85mm Lens]] [[Editorial Fashion]]

---

### 154. 详细的室内生活方式肖像提示

**Author**: [なぁさん｜SNSで1億円](https://x.com/nasan_0422)  **Date**: 2026-02-10  **Language**: en

> 一个高度详细的 JSON 格式提示，用于 Gemini Nano Banana Pro，其中指定了构图、主体细节（年轻女性，深棕色头发，特定服装）、背景（现代咖啡馆）、灯光、调色板和技术相机设置，以生成一张时尚的生活方式肖像。

![详细的室内生活方式肖像提示](https://cms-assets.youmind.com/media/1770792224860_9ib2r3_HAw_CxvbQAAgbXM.jpg)

```
{ "image_type": "photograph", "genre": "indoor lifestyle portrait", "composition": { "framing": "medium close-up", "orientation": "vertical", "subject_position": "center-right, seated at a table", "camera_angle": "slightly above eye-level", "depth_of_field": "shallow to moderate, subject sharply isolated from softly blurred background", "leading_lines": "table edge and ceiling lines subtly guide focus toward the subject", "balance": "asymmetrical, balanced by negative space and interior geometry" }, "subject": { "count": 1, "description": "young woman seated indoors in a modern public space", "pose": "leaning forward with elbow on table, chin resting on hand", "expression": "neutral to contemplative, calm and introspective", "gaze": "directed slightly off-camera to the left", "hair": { "color": "dark brown", "style": "short to medium length, softly wavy with straight fringe/bangs", "finish": "natural texture with light volume" }, "face_details": { "makeup": "natural glam with soft blush, defined brows, subtle lip color", "eyewear": "round metal-frame sunglasses with dark lenses" }, "clothing": { "top": { "type": "knit sweater or rugby-style pullover", "color": "cream base with navy blue panels and red collar accent", "details": "textured knit fabric, ribbed cuffs, embroidered red lettering on chest" } } }, "background": { "environment": "modern indoor café or bookstore-style space", "elements": [ "wooden table and seating", "open interior with high ceiling", "track lighting and recessed lights", "bookshelves or retail fixtures in distance" ], "depth": "background softly defocused to emphasize subject", "architectural_style": "minimalist, contemporary" }, "lighting": { "type": "mixed natural and artificial light", "source": "large windows combined with overhead interior lighting", "quality": "soft, even illumination", "direction": "frontal-side lighting from window direction", "highlights": "gentle highlights on cheekbones and hair", "shadows": "soft, minimal shadow falloff" }, "color_palette": { "dominant_colors": [ "cream", "navy blue", "soft gray" ], "accent_colors": [ "red", "warm wood tones" ], "color_temperature": "neutral to slightly warm" }, "technical_details": { "camera_type": "digital camera or high-end smartphone", "lens_look": "standard portrait focal length", "aperture_estimate": "f/2–f/3.5", "iso_estimate": "low ISO", "shutter_speed_estimate": "moderate, suitable for indoor ambient light", "image_sharpness": "high on facial features and clothing texture", "noise": "minimal" }, "artistic_elements": { "mood": "calm, introspective, modern", "style": "fashion-forward lifestyle portrait", "aesthetic": "clean, understated, editorial casual", "contrast": "moderate", "saturation": "natural, slightly muted" }, "post_processing": { "skin_tones": "smooth and natural", "color_grading": "balanced neutrals with soft contrast", "retouching_level": "light", "clarity": "enhanced on subject, subdue
```

[[Female Portrait]] [[Fashion Photography]] [[Soft Natural Light]] [[Social Media Aesthetic]]

---

### 155. 月亮投影剪影的低调肖像

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一张戏剧性、低调的女性写实肖像，以高分辨率的满月盘作为其身后的主要光源和图形元素。它指定了纯黑色背景、投射在月亮上的清晰阴影轮廓，以及高对比度，以营造强烈、神秘的氛围。

![月亮投影剪影的低调肖像](https://cms-assets.youmind.com/media/1770706189606_6dcmgc_HAwCiA5aAAEWPfZ.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "photoreal_low_key_moon_projection_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_MOON_DISK_SHADOW_SILHOUETTE_LOWKEY"
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "high",
      "num_images": 4
    },
    "scene": {
      "concept": "a dramatic low-key portrait using a moon projection as both backdrop and key graphic element",
      "environment": "pure black seamless background, no visible walls, no props, minimal set",
      "composition": "3/4 portrait, subject placed slightly right of center; oversized moon disk behind head and shoulders, moon fills mid-frame"
    },
    "subject": {
      "person": "adult woman",
      "wardrobe": {
        "top": "black bandeau top, matte fabric",
        "bottom": "dark denim jeans, subtle texture"
      },
      "hair_makeup": {
        "hair": "long dark hair, natural volume, bangs/fringe across forehead",
        "makeup": "subtle smoky eyes, glossy lips, realistic skin texture, no plastic smoothing"
      },
      "pose": "3/4 body turn, arms crossed over chest in a self-embrace, shoulders slightly raised",
      "expression": "mysterious, calm, slightly intense gaze back at camera"
    },
    "projection": {
      "content": "high-resolution full moon disk with crisp crater detail",
      "placement": "behind the subject, centered at head/shoulder level",
      "shadow_behavior": "hard-edged shadow silhouette cast onto the moon disk, clearly readable profile/shoulder outline",
      "notes": "moon must look like real projected light, not a pasted graphic; preserve crater texture and edge falloff"
    },
    "camera": {
      "shot": "low-key projection portrait",
      "lens_mm": 50,
      "aperture": 2.2,
      "focus": "sharp on eyes, lips, and moon crater texture; deep blacks preserved",
      "quality_tags": "ultra-photoreal, crisp, subtle film grain, clean edges"
    },
    "lighting": {
      "style": "single hard projector key light + minimal fill",
      "notes": "high contrast, controlled highlights on cheekbones and lips, deep shadows, crisp shadow silhouette on moon disk, no visible background spill"
    },
    "color_grade": {
      "palette": "deep blacks, cool moon grays, neutral skin tones with slight cinematic warmth",
      "contrast": "high, low-key",
      "effects": "subtle grain, very mild halation only on brightest moon edges"
    },
    "negative_prompt": "text, logo, watermark, border, frame, bright background, softbox look, low contrast, blurry moon, flat graphic moon, overexposed face, plastic skin, over-smoothed, extra fingers, deformed hands, distorted anatomy, heavy artifacts, banding"
  }
}
```

[[Female Portrait]] [[Dramatic Lighting]] [[High Contrast]]

---

### 156. 楼梯上的黄金时段时尚肖像

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真的时尚肖像照：一位女士身穿红色吊带裙，在黄金时段坐在石阶上，强调光线、构图和特定的相机设置（50mm 镜头，f/2.8 光圈）。

![楼梯上的黄金时段时尚肖像](https://cms-assets.youmind.com/media/1770706202095_1bmar6_HAv6LefboAAFw1j.jpg)
![楼梯上的黄金时段时尚肖像](https://cms-assets.youmind.com/media/1770706202204_4sj1p2_HAv6Leda0AEGExx.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "photoreal_golden_hour_fashion_stairs_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_RED_DRESS_FAN_STAIRS_GOLDEN_HOUR"
    },
    "output": {
      "aspect_ratio": "1:1",
      "resolution": "high",
      "num_images": 4
    },
    "scene": {
      "concept": "a warm golden-hour fashion portrait on textured stone stairs",
      "environment": "wide concrete/stone staircase with repeating lines, minimal modern railing, clear sky",
      "composition": "subject seated mid-stairs, strong leading lines from steps, clean negative space above"
    },
    "subject": {
      "person": "adult woman",
      "wardrobe": {
        "dress": "flowing {argument name="dress color" default="red"} slip dress with a high slit, lightweight fabric, natural drape"
      },
      "accessories": "vintage hand fan, small necklace, red flower behind ear",
      "hair_makeup": {
        "hair": "long wavy dark hair, slightly wind-touched",
        "makeup": "natural warm glow, soft highlight, realistic skin texture"
      },
      "pose": "seated confidently, one leg bent and visible through slit, relaxed hand on step, fan held naturally",
      "feet": "barefoot, natural relaxed toes",
      "expression": "calm, confident, sunlit"
    },
    "camera": {
      "shot": "fashion portrait",
      "lens_mm": 50,
      "aperture": 2.8,
      "focus": "sharp on face and dress texture; background stairs slightly softer",
      "quality_tags": "ultra-photoreal, crisp textures, subtle film grain"
    },
    "lighting": {
      "style": "golden hour direct sunlight",
      "notes": "warm highlights, crisp shadows, avoid blown skin highlights, keep red dress saturated but natural"
    },
    "color_grade": {
      "palette": "warm golds, natural skin tones, deep red dress, neutral stone",
      "contrast": "medium-high (sunlight look) with controlled rolloff",
      "tone": "Mediterranean summer, sensual but classy"
    },
    "negative_prompt": "text, logo, watermark, overexposed skin, plastic skin, bad anatomy, extra fingers, warped stairs, blurry face, studio lighting, CGI, cartoon, lowres, heavy artifacts"
  }
}
```

[[Female Portrait]] [[Hyperrealistic Photography]] [[50mm Lens]] [[Red Dress]]

---

### 157. 电影时装弓箭手肖像

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真的电影级全身肖像，描绘一位优雅的女模特，身着香槟色象牙白缎面紧身胸衣礼服，摆出弓箭手姿势，置身于深勃艮第色天鹅绒背景前，采用低调工作室照明，并融入古典绘画风格。

![电影时装弓箭手肖像](https://cms-assets.youmind.com/media/1770706204769_sur5l8_HAvjmKbaAAAWe_K.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "photoreal_cinematic_couture_archer_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_BURGUNDY_DRAPE_SATIN_ARCHER"
    },
    "output": {
      "aspect_ratio": "9:16",
      "resolution": "high",
      "num_images": 4
    },
    "scene": {
      "environment": "deep {argument name="backdrop color" default="burgundy"} velvet draped backdrop, dark studio floor with subtle fabric folds",
      "mood": "baroque, dramatic, elegant, quiet tension",
      "composition": "full-body, side profile, centered with negative space in the direction of the arrow"
    },
    "subject": {
      "description": "elegant female model, side profile, calm focused expression",
      "pose": "archer stance: left arm extended holding bow, right hand pulling string to cheekbone, arrow perfectly aligned",
      "wardrobe": "champagne-ivory satin corset gown, structured bodice, subtle gold leaf embroidery on the bust, long flowing satin skirt with heavy train pooling on the floor",
      "props": "realistic recurve bow, clean arrow with natural feather fletching"
    },
    "camera": {
      "shot": "full-body editorial portrait",
      "lens_mm": 85,
      "aperture": 2.8,
      "focus": "sharp face, hands, bowstring and embroidery; controlled depth of field",
      "quality_tags": "ultra-photoreal, micro-texture, crisp fabric weave, accurate specular highlights"
    },
    "lighting": {
      "style": "low-key studio with classical painting influence",
      "key_light": "soft directional key from camera-left, Rembrandt triangle feel",
      "fill": "minimal fill to keep shadows rich",
      "rim_light": "subtle rim behind subject to separate from burgundy backdrop",
      "notes": "avoid blown satin highlights; preserve skin tone neutrality"
    },
    "color_grade": {
      "palette": "burgundy / near-black shadows, warm champagne satin, natural warm skin",
      "contrast": "cinematic, deep blacks, controlled highlights"
    },
    "negative_prompt": "text, logo, watermark, cartoon, anime, CGI, plastic skin, blur, lowres, bad anatomy, extra fingers, deformed hands, warped bow, broken string, duplicated limbs, messy face, noise artifacts"
  }
}
```

[[Female Portrait]] [[Studio Photography]] [[Low Key Lighting]]

---

### 158. 超大容量游艇魅力肖像

**Author**: [Maya](https://x.com/mayadelmare)  **Date**: 2026-02-09  **Language**: en

> 一个高度具体的 JSON 提示，旨在生成一张“精英能量”的超写实女性图像，背景为豪华游艇甲板，强调极度夸张的沙漏型身材、未经修饰的真实皮肤（包括妊娠纹），以及强烈的正午阳光。

![超大容量游艇魅力肖像](https://cms-assets.youmind.com/media/1770706202234_0w51ey_HAvU10FXoAAFNfk.jpg)

```
{
"subject": {
"demographics": "Mid-20s woman, elite athletic physique with hyper-pronounced non-normalized hourglass architecture.",
"hair": "Wavy brunette-to-blonde ombre, saturated with saltwater, clumping in high-definition wet strands across the shoulders.",
"face": "Sun-kissed complexion with light natural makeup; expressive eyes framed by salt-crusted lashes; direct, high-fashion gaze.",
"anatomy": "Anatomy focused on soft tissue mass and gravity. Significant natural bust with realistic gravity-dependent displacement toward the torso. Extremely narrow, tapered waist transitioning into hyper-voluminous, wide-set hips and deep lateral gluteal projection. Skin exhibits unfiltered realism: visible pores, epidermal oil sheen from sun exposure, and faint striae (stretch marks) on the curvature of the hips. Thighs possess athletic density, showing natural soft tissue compression against the yacht cushions without artificial firming or digital smoothing.",
"attire": "Glossy {argument name="swimsuit color" default="black"} liquid-look synthetic one-piece swimsuit. Features aggressive side cutouts exposing the lateral ribcage and the transition to the iliac crest. Fabric exhibits high-specular highlights and tactile tension over the curves.",
"accessories": "70mm polished silver hoop earrings; a reflective silver mirror-finish visor with embossed 'BALENCIAGA' block typography."
},
"pose": {
"type": "Reclining oblique / Sunbathing",
"details": "Subject is reclining on her side/back on a yacht deck. Legs are crossed at the calves, elongating the lower body. Left arm is extended back to support the torso, while the right hand rests delicately on the voluminous hip curvature. Head is angled toward the camera."
},
"environment": {
"location": "Luxury yacht deck in open sapphire-blue Mediterranean water.",
"elements": "White upholstered sunpad cushions, polished chrome safety railings, sparkling deep-blue water with high-frequency wave patterns and caustic light reflections."
},
"camera": {
"shot_type": "Full-body reclining shot",
"focal_length": "50mm (Portrait lens to preserve anatomical volume without wide-angle distortion).",
"perspective": "Slightly elevated, looking down at the subject to emphasize the hourglass silhouette."
},
"lighting": {
"type": "Hard zenith sunlight",
"details": "Direct high-noon solar illumination creating sharp, high-contrast shadows. Intense specular highlights on the wet skin, metallic visor, and glossy swimsuit fabric."
},
"mood_and_expression": {
"vibe": "Elite luxury lifestyle, confident, unfiltered glamour.",
"expression": "Slightly parted lips, neutral but intense 'editorial' expression."
},
"style_and_realism": {
"fidelity": "Unfiltered skin texture, visible salt-water droplets, realistic soft tissue mass responding to gravity, no artificial lift."
},
"colors_and_tone": {
"palette": "Deep noir, reflective silver, vibrant sapphire blue, warm sun-drenched golden skin tones.",
"saturation": "
```

[[Female Portrait]] [[Natural Skin Texture]] [[Hourglass Figure]] [[Luxury Lifestyle]]

---

### 159. 电影感街头摄影：运动模糊效果

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-02-09  **Language**: en

> 生成一张超现实、电影感的街头摄影图像的提示词。画面中，一位留着灰金色波波头、戴眼镜的年轻女子在高峰时段繁忙的城市人行横道上静止站立，而商务人士则以动态模糊的效果从她身边走过。构图强调戏剧性对比、柔和色调和 8K 画质。

![电影感街头摄影：运动模糊效果](https://cms-assets.youmind.com/media/1770706226356_y2vo4y_HAu4HPqaAAIf398.jpg)

```
A cinematic, hyper-realistic street photography shot of a young woman standing still in the middle of a busy city crosswalk during rush hour. She has short {argument name="hair color" default="ash-gray"} bob hair, round glasses, and a calm, introspective expression while everyone else moves around her. She’s wearing an oversized dark gray sweater, a black pleated midi skirt, brown leather lace-up boots, and a backpack, holding a few books close to her chest. Business people in formal attire walk past her in motion blur, some holding coffee cups. Modern urban cityscape with tall buildings, muted tones, overcast daylight, shallow depth of field, soft natural lighting, cinematic composition, ultra-detailed, 35mm lens, f/1.8, realistic skin texture, dramatic contrast, photorealistic, 8K quality
```

[[Female Portrait]] [[Motion Blur]] [[8K Photography]] [[Urban Portrait]]

---

### 160. 逼真的冬季热水浴缸自拍

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-02-09  **Language**: en

> 一个极其详细、照片般逼真的 JSON 提示，专注于解剖学上的忠实度和纹理真实感，用于拍摄一位女性在户外冬季热水浴缸中穿着小比基尼上衣的特写自拍，强调自然的皮肤纹理和重力对主体胸部的影响。

![逼真的冬季热水浴缸自拍](https://cms-assets.youmind.com/media/1770706201584_obs95g_HAuyZZybYAIBDZE.jpg)

```
{
"subject": {
"description": "A young woman with shoulder-length, wet, dark brown hair swept back from her face. She has fair skin with visible natural texture, including slight flushing on the chest and cheeks consistent with hot water or cold air exposure. She is wearing a light {argument name="bikini color" default="pink"}, halter-style string bikini top with a center tie. The bikini top is very small relative to her anatomy, tightly fitted.",
"anatomical_fidelity": {
"bust_volume": "Extremely voluminous and heavy bust, significantly above average size. The breast mass exhibits natural weight and gravity, sitting low and full. The bikini top struggles to contain the volume, creating deep, pressed cleavage and significant projection.",
"proportions": "Accurate representation of a heavy, full-bust natural figure. Shoulders are soft and slightly rounded. Soft tissue deformation is visible where the bikini strap presses into the neck and skin.",
"skin_details": "High-fidelity skin texture with pores, natural discoloration, moles, and wet sheen from the water."
},
"pose": {
"type": "Close-up selfie",
"orientation": "Body angled slightly to the viewer's left. Face turned forward towards the lens.",
"head_position": "Head tilted slightly to her right, chin tucked slightly down.",
"limbs": {
"left_arm": "Extended forward and out of frame towards the bottom right, clearly holding the camera device (selfie posture).",
"right_arm": "Partially submerged in the water, resting near the edge of the wooden tub."
},
"spine_curvature": "Slight forward lean."
},
"environment": {
"setting": "Outdoor winter spa or hot tub.",
"elements": [
"Rustic wooden hot tub planks",
"Dark water surface",
"Piles of white natural snow in the immediate background",
"Rough-hewn wooden post or log structure behind the subject"
],
"context": "Cold winter weather contrasted with a warm soak."
},
"camera": {
"shot_type": "Close-up selfie shot (POV).",
"perspective": "High angle looking slightly down at the subject.",
"focal_length": "Wide-angle smartphone lens equivalent (approx 24mm), creating slight foreshortening of the foreground.",
"depth_of_field": "Deep depth of field, keeping both the subject and the immediate snow/wood background relatively sharp.",
"framing": "Framed from the chest up, cutting off at the mid-upper arm."
},
"lighting": {
"type": "Natural overcast daylight.",
"quality": "Soft, diffused, and shadowless.",
"direction": "Global, ambient winter light.",
"shadows": "Very soft occlusion shadows in the cleavage and under the hair.",
"highlights": "Subtle wet specular highlights on the skin and hair."
},
"mood_and_expression": {
"emotion": "Alluring, calm, relaxed.",
"gaze": "Direct eye contact with the lens, soft and engaging.",
"mouth": "Lips naturally full, slightly parted, neutral expression."
},
"style_and_realism": {
"aesthetic": "Candid social media photo, raw and unedited.",
"rendering": "Photorealistic, 8k resolution.",
"textures": "Wet hair strands,"
}
```

[[Female Portrait]] [[Natural Skin Texture]] [[Close-Up Selfie]] [[Outdoor Photography]]

---

### 161. 薰衣草连衣裙曲线女性模特的详细 JSON 提示

**Author**: [Jessia](https://x.com/itsjessiababy)  **Date**: 2026-02-09  **Language**: en

> 一个极其详细的 JSON 提示，重点在于生成一张年轻、曲线玲珑的成年女性的超写实图像。该提示详细说明了复杂的解剖细节（脊柱前凸、臀部突出）、特定的姿势（回头看肩膀）以及详细的服装（薰衣草色迷你连衣裙，带有褶皱“收缩”细节），置于高角度摄像机取景的户外住宅环境中。

![薰衣草连衣裙曲线女性模特的详细 JSON 提示](https://cms-assets.youmind.com/media/1770706222016_p9tvgi_HAum9FNboAAJHOA.jpg)

```
{
"subject": {
"demographics": "Young female adult, appearing in her early 20s, with a fit and curvy physique.",
"hair": "Dark brown hair pulled up into a high, messy ponytail. Distinct chunky blonde face-framing highlights (money piece) at the front. The ponytail falls down the back of the neck.",
"face": "Looking back over the left shoulder directly at the camera. Defined eyebrows, winged eyeliner, contouring, and mauve-toned matte lipstick. Skin has a warm, light tan tone.",
"body_and_anatomy": "Hourglass figure with emphasized lower body curves due to pose and camera angle. Visible side profile of the chest showing full, natural projection on the left side. Deep arch in the lower back (lordosis). Prominent, rounded glutes accentuated by the garment's cut. Left hand is raised, touching the upper left chest/shoulder area near the collarbone. Small tattoo visible on the outer left hand/wrist.",
"outfit": "A tight-fitting, long-sleeved, {argument name=\"dress color\" default=\"lavender or light lilac\"} mini dress (or romper/bodysuit). The fabric appears to be a matte, stretchy activewear material (spandex/nylon blend). Features a large, open-back cutout exposing the mid and upper back. Distinctive ruched 'scrunch' detailing along the vertical seam of the buttocks to accentuate shape."
},
"pose": {
"orientation": "Standing, angled away from the camera (dorsal/rear view), twisting the torso to look back over the left shoulder.",
"spine_and_posture": "Pronounced arch in the lower back. Shoulders are angled downwards relative to the camera view. The neck is rotated to the left.",
"limbs": "Left arm is bent at the elbow, hand resting near the clavicle. Right arm is extended downwards, partially obscured. Legs are straight, standing on a paved surface.",
"head_tilt": "Chin slightly tucked, face angled upward towards the camera lens.",
"details": "Barefoot with white toenail polish visible."
},
"environment": {
"location": "Outdoor driveway or patio area.",
"ground": "Light grey concrete slabs or pavers with visible seams.",
"background_elements": "A textured beige stucco pillar or wall on the immediate left foreground. Background contains blurred green trees and foliage, suggesting a residential or park-like setting.",
"depth": "Shallow depth of field; the subject is sharp, while the background vegetation is soft and out of focus."
},
"camera": {
"angle": "High angle shot (camera positioned above the subject looking down at roughly 45 degrees).",
"framing": "Medium-full shot, capturing from the top of the head down to the ankles/feet.",
"perspective": "Perspective foreshortening emphasizes the head and shoulders while tapering towards the feet. The downward angle accentuates the curvature of the back and hips.",
"lens_characteristics": "Sharp focus on the subject, slight background bokeh."
},
"lighting": {
"type": "Natural daylight, likely overcast or open shade.",
"quality": "Soft, diffused lighting with no harsh, direct sun highlights on the sk
```

[[Female Portrait]] [[Hyperrealistic Photography]] [[High Angle Shot]] [[Outdoor Portrait]]

---

### 162. 歌剧院包厢里的名人偷拍

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-02-09  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张超现实、抓拍的女性名人生活方式照片。照片中，一位女性坐在一间奢华的金色和红色歌剧院包厢座位上，重点突出巴洛克建筑、温暖的人造光线，以及她黑色缎面连衣裙和配饰的具体细节。

![歌剧院包厢里的名人偷拍](https://cms-assets.youmind.com/media/1770706178557_eo872i_HAumtuybUAASI7I.jpg)
![歌剧院包厢里的名人偷拍](https://cms-assets.youmind.com/media/1770706178536_vvxtsl_HAumuJwbgAASLFI.jpg)
![歌剧院包厢里的名人偷拍](https://cms-assets.youmind.com/media/1770706178634_wisb0j_HAumtziaYAAL9nG.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman with long, straight light brown hair and a subtle, friendly smile.",
      "pose": "Sitting in a theater box seat, body turned slightly sideways away from the camera but head turned to face the viewer. Left arm resting casually on the red velvet box railing.",
      "clothing": "Black satin dress with spaghetti straps and a low back, featuring a large black decorative bow at the lower back.",
      "accessories": "Apple Watch with a metallic band on the left wrist, delicate bracelets, small earrings.",
      "expression": "Relaxed, happy, engaging eye contact."
    },
    "environment": {
      "location": "Grand historic European opera house interior (resembling the Vienna State Opera).",
      "architecture": "Multi-tiered private box seating (loges) featuring ornate gold Baroque/Rococo molding and stucco work. Deep red velvet curtains and wall coverings inside the boxes.",
      "background_details": "Several levels of balconies visible behind her, filled with other patrons in formal wear. Warm ambient lighting from wall sconces and theater chandeliers.",
      "foreground": "Red velvet cushioned railing and the back of a red theater seat."
    },
    "lighting_and_atmosphere": {
      "type": "Warm indoor artificial lighting mixed with soft camera flash.",
      "tone": "Golden, opulent, elegant, atmospheric.",
      "quality": "High dynamic range (HDR), evenly lit face, soft fall-off in the background."
    },
    "technical_specs": {
      "style": "Ultra-realistic, Photorealistic, Candid celebrity lifestyle photography.",
      "resolution": "8k UHD, highly detailed textures.",
      "camera_angle": "Eye-level, medium shot.",
      "aspect_ratio": "9:16 (Vertical/Long)",
      "lens_simulation": "35mm or 50mm portrait lens, aperture f/2.8 for slight depth of field blurring the background layers."
    },
    "full_combined_prompt": "A vertical ultra-realistic 8k photo of a young woman sitting in a lavish gold and red opera house box seat. She has long straight brunette hair, wearing a black backless satin dress with a large bow. She is smiling over her shoulder at the camera, arm resting on the red velvet railing. Background features ornate golden multi-tiered theater balconies filled with people, baroque architecture, warm chandelier lighting. High detailed texture, UHD, HDR, cinematic lighting, shot on 35mm lens --ar 9:16 --q 2 --v 6.0"
  }
}
```

[[Female Portrait]] [[Luxury Lifestyle Photography]] [[Black Satin Dress]]

---

### 163. 情绪化垂直卧室肖像，带约束条件

**Author**: [RavelAI](https://x.com/Ravelberger)  **Date**: 2026-02-09  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张超逼真的垂直照片，描绘一名女性躺在床上，置身于阴郁、昏暗的氛围中。该提示词对体型（沙漏型身材，无纹身）、特定服装（不对称露脐上衣，细带比基尼下装）、详细场景元素（毛绒玩具）和灯光（冷紫色/蓝色调）有严格的限制。

![情绪化垂直卧室肖像，带约束条件](https://cms-assets.youmind.com/media/1770706153138_ow147z_HAuhM9ybgAAbnmJ.jpg)

```
{
  “subject”: {
    “description”: “An ultra-realistic vertical photograph of her with long dual-toned hair lying on a bed in a moody atmosphere.”,
    “body”: {
      “physique”: “A slender yet curvy hourglass figure characterized by a very narrow, defined waist and wider hips. The stomach is flat and toned. The skin is flawless and completely free of any tattoos.”,
      “pose”: “Lying on her back on soft bedding, captured from a slightly low angle. Her head rests on a fluffy grey pillow, and she gazes directly at the camera with a pouty expression. Her left arm is bent with the hand near her hair, and her right arm extends forward.”,
“features”: “Long straight hair featuring a mix of {argument name="hair color 1" default="platinum blonde"} and {argument name="hair color 2" default="dark brown"} streaks. Striking blue-grey eyes and full lips.”
    }
  },
  “wardrobe”: {
    “top”: “A white, tight-fitting asymmetric crop top with a single strap design.”,
    “bottom”: “A black string bikini bottom worn high on the hips.”,
    “accessories”: “Small silver hoop earrings and a silver chain bracelet on the right wrist.”
  },
  “pose_action”: “Relaxed lounging pose on a bed, creating an intimate and moody atmosphere.”,
  “scene”: {
    “environment”: “A bedroom setting focused on the bed area.”,
    “elements”: “White bed sheets and pillows surrounding the subject. Several plush toys are scattered nearby, including pink and white stuffed bunnies and a round black cat plush with a white eye patch.”,
    “composition”: “Vertical 9:16 aspect ratio. Close-up shot framing the torso and face.”
  },
“lighting”: {
    “setup”: “Atmospheric, dim ambient lighting dominated by cool purple and blue tones.”,
    “details”: “The colored light washes over the scene, highlighting the contours of the body and the textures of the fluffy pillow and hair, creating a distinct moody aesthetic.”
  },
  “camera”: {
    “technical”: “Ultra-realistic, high-resolution photograph. Sharp focus on the face and eyes. The low angle emphasizes the body’s curves.”,
    “constraints”: [
      “Aspect Ratio 9:16”,
      “Subject must have NO TATTOOS (skin must be completely clear)”,
      “Maintain the specific hourglass physique described”,
      “Replicate the purple/blue mood lighting exactly”,
      “Include the specific plush toys described”
    ]
  }
}
```

[[Female Portrait]] [[Intimate Photography]] [[Bedroom Photography]] [[Atmospheric Lighting]]

---

### 164. 梦幻般的艺术编辑肖像：双重曝光

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-02-09  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张超高分辨率、梦幻般的艺术编辑肖像，描绘一位年轻女性，强调浅景深、柔和漫射光、柔和鼠尾草绿色调，以及带有漂浮花朵的微妙、诗意的双重曝光效果。

![梦幻般的艺术编辑肖像：双重曝光](https://cms-assets.youmind.com/media/1770706206829_pmaawy_HAuggYPbwAAmZIC.jpg)
![梦幻般的艺术编辑肖像：双重曝光](https://cms-assets.youmind.com/media/1770706207241_caoca3_HAuggXdaMAAS4LT.jpg)

```
{
  "meta": {
    "title": "Dreamy Fine-Art Editorial Portrait",
    "version": "1.0",
    "type": "image-generation-prompt",
    "quality_target": "ultra-high resolution 8K"
  },
  "reference": {
    "face_identity": "use exact facial structure, proportions, and identity from the provided reference image",
    "identity_preservation": "high",
    "notes": "do not alter facial features, age, or likeness"
  },
  "subject": {
    "description": "Young woman with soft, natural facial features",
    "expression": "calm, introspective, emotionally serene",
    "makeup": "minimal, natural skin-focused makeup",
    "pose": "front-facing or slight profile, relaxed posture"
  },
  "composition": {
    "style": "editorial fine-art photography",
    "framing": "tight portrait crop",
    "depth_of_field": "shallow depth of field with cinematic softness",
    "aesthetic": "elegant, minimalist, painterly realism"
  },
  "lighting": {
    "type": "gentle diffused natural light",
    "highlights": "soft smooth highlights on skin",
    "skin_texture": "natural texture preserved, no over-smoothing"
  },
  "background": {
    "color_palette": "muted pastel {argument name="background color" default="sage green"} tones",
    "texture": "soft, seamless, non-distracting"
  },
  "foreground_effects": {
    "elements": "delicate flowers drifting across the frame",
    "motion": "intentional slow-shutter motion blur",
    "light_effects": "soft streaks of light and dreamy bloom"
  },
  "artistic_effects": {
    "double_exposure": "subtle and poetic, lightly layered across the face",
    "motion_blur": "soft, flowing, slow-shutter inspired",
    "mood": "dreamy, emotional, serene"
  },
  "rendering": {
    "style": "ultra-realistic fine-art portrait",
    "sharpness": "sharp facial focus with soft cinematic falloff",
    "color_grading": "pastel, filmic, gentle contrast",
    "resolution": "8K ultra-HD",
    "detail_level": "extreme realism with painterly softness"
  }
}
```

[[Female Portrait]] [[Dreamlike Aesthetic]] [[Fine Art Photography]]

---

### 165. 奢华冬季高级定制美妆大片

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-09  **Language**: en

> 这是一个高度结构化的 JSON 提示，用于图像到图像的生成任务，重点是创建一张奢华冬季高级定制美容时尚肖像。它要求在保留参考图像身份和面部特征的同时，应用特定的高级时装造型、妆容、灯光（柔和漫射主光、微妙轮廓光）和色彩分级（象牙色、柔和灰色、冷粉色），以营造出一种冷峻奢华的优雅氛围。

![奢华冬季高级定制美妆大片](https://cms-assets.youmind.com/media/1770706154553_whhlet_HAuc7krWEAIizzo.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "luxury_winter_editorial_beauty_series",
      "language": "en",
      "priority": "highest",
      "style_version": "v1.0_ICE_FUR_COUTURE"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_makeup_style": true,
      "notes": "Use the reference image as the primary anchor. Maintain facial proportions, eye shape, lips, hair color, and the white fur hat and coat."
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 3,
      "sharpness": "high_but_filmic",
      "grain": "subtle_fine_analog"
    },
    "scene": {
      "concept": "luxury winter couture beauty editorial",
      "environment": "minimal studio background in soft cool gray",
      "time": "timeless_editorial",
      "weather": "studio_winter_mood"
    },
    "subject": {
      "primary": {
        "description": "a high-fashion woman in winter couture styling",
        "hair": "dark brown hair flowing naturally from under a fluffy white fur hat",
        "makeup": {
          "eyes": "soft icy shimmer eyeshadow, subtle winged liner, long separated lashes",
          "skin": "porcelain skin with cool rosy blush, soft luminous finish",
          "lips": "glossy nude-to-soft-brown lips with hydrated shine",
          "brows": "natural full brows softly shaped"
        },
        "wardrobe": "luxurious white faux-fur hat and matching white fur coat framing the face",
        "expression": "calm, dreamy, confident winter glamour",
        "poses": [
          "front-facing calm gaze",
          "head tilted softly to the side",
          "eyes closed, hands gently touching the fur hat"
        ]
      }
    },
    "composition": {
      "framing": "beauty portrait and upper torso",
      "camera_height": "eye_level",
      "depth_of_field": "shallow_creamy_background",
      "focus": "sharp_on_eyes_lips_and_fur_texture",
      "series_consistency": "editorial_multi_pose_continuity"
    },
    "cinematography": {
      "camera_model": "full_frame_cinema_camera",
      "lens": "85mm_prime",
      "aperture": "f1.8",
      "iso": "200",
      "look": "high_fashion_winter_film_still",
      "dynamic_range": "high",
      "highlight_rolloff": "soft_filmic"
    },
    "lighting": {
      "key": "large_soft_diffused_light_front",
      "fill": "gentle_fill_preserving_depth",
      "rim": "subtle_rim_light_defining_fur_edges",
      "skin_lighting": "even_soft_beauty_lighting",
      "mood": "cold_luxury_elegance"
    },
    "color_grading": {
      "palette": "ivory_white_soft_gray_cool_pink_nude",
      "contrast": "low_to_moderate",
      "saturation": "controlled_editorial",
      "skin_tones": "cool_neutral_balanced",
      "black_levels": "soft_not_crushed"
    },
    "texture_details": {
      "fur"
```

[[Female Portrait]] [[Image-To-Image]] [[Soft Diffused Lighting]]

---

### 166. 奢华社论美妆微距系列搭配巧克力

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-09  **Language**: en

> 一个高度技术化、JSON 结构的提示，用于生成一个奢侈美妆专题宏观系列，重点描绘一位时尚女性与黑巧克力互动，并指定了相机设置（100mm 微距）、灯光、色彩校正（巧克力棕色），同时要求保留参考图像中的身份和面部特征。

![奢华社论美妆微距系列搭配巧克力](https://cms-assets.youmind.com/media/1770706171957_1nenyi_HAuanfqaIAEP13p.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "luxury_editorial_beauty_macro_series",
      "language": "en",
      "priority": "highest",
      "style_version": "v1.0_CHOCOLATE_GLOSS_COUTURE"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_makeup_palette": true,
      "notes": "Use the reference collage as the primary anchor. Maintain the same face, lips shape, eye makeup style, and chocolate interaction."
    },
    "output": {
      "aspect_ratio": "1:1",
      "resolution": "ultra_high",
      "num_images": 4,
      "sharpness": "macro_crisp_filmic",
      "grain": "very_subtle_analog"
    },
    "scene": {
      "concept": "sensual luxury beauty editorial with chocolate as tactile element",
      "environment": "minimal studio background, soft warm neutral tones",
      "time": "timeless_editorial",
      "weather": "studio"
    },
    "subject": {
      "primary": {
        "description": "a high-fashion woman captured in intimate beauty close-ups",
        "hair": "soft brown hair framing the face naturally, slight movement",
        "makeup": {
          "eyes": "smoky brown-black eye makeup with elongated winged liner, soft lashes",
          "skin": "natural skin texture visible, rosy blush on cheeks, soft glow",
          "lips": "deep chocolate-brown ultra-glossy lips, wet shine, high specular highlights",
          "brows": "natural full brows, softly defined"
        },
        "interaction": "holding and gently biting a piece of dark chocolate between glossy lips",
        "expression": "sensual, calm, introspective gaze"
      }
    },
    "composition": {
      "framing": "beauty close-up and extreme macro variations (lips and eyes)",
      "camera_height": "eye_level",
      "depth_of_field": "very_shallow_creamy_bokeh",
      "focus": "razor_sharp_on_lips_and_eyes",
      "series_layout": "editorial_multi_frame_consistency"
    },
    "cinematography": {
      "camera_model": "full_frame_cinema_camera",
      "lens": "100mm_macro_prime",
      "aperture": "f2.8",
      "iso": "100",
      "look": "luxury_beauty_film_still",
      "dynamic_range": "high",
      "highlight_rolloff": "soft_filmic"
    },
    "lighting": {
      "key": "soft_diffused_beauty_light_from_front",
      "fill": "minimal_fill_to_keep_depth",
      "rim": "subtle_gloss_highlight_rim_on_lips",
      "skin_lighting": "even_soft_no_harsh_shadows",
      "mood": "intimate_warm_sensual"
    },
    "color_grading": {
      "palette": "chocolate_browns_warm_beige_soft_rose",
      "contrast": "low_to_moderate",
      "saturation": "controlled_luxury",
      "skin_tones": "warm_natural_balanced",
      "black_levels": "soft_filmic"
    },
    "texture_details": {
      "lips": "high_gloss_wet_texture_micro_reflections",
      "chocolate": "realistic_dark_chocolate_te
```

[[Female Portrait]] [[Macro Photography]]

---

### 167. 和毛绒玩具一起的忧郁自拍

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-02-09  **Language**: en

> 一个详细、结构化的提示，用于生成一张超现实的垂直自拍照，照片中一名女性面朝下躺在床上，在昏暗的紫色/蓝色灯光下，同时捕捉到她的脸部和臀部，并对外观和包含的毛绒玩具提出了具体限制。

![和毛绒玩具一起的忧郁自拍](https://cms-assets.youmind.com/media/1770706166491_vx2o43_HAuZXXEWAAAu2dX.jpg)

```
{
  “subject”: {
    “description”: “An ultra-realistic vertical selfie photograph taken by a young woman with long dual-toned hair, lying face down on a bed in a moody atmosphere.”,
    “body”: {
      “physique”: “A slender yet curvy hourglass figure. The pose highlights the curve of her lower back and round glutes accentuated by the black bikini bottoms. The skin is flawless and completely free of any tattoos.”,
      “pose”: “Lying face down on her stomach, holding a smartphone to take a mirror-style selfie (likely reflecting off a surface or using a wide-angle lens). Her head is turned to look at the phone screen/camera with a pouty expression. Her upper body is slightly propped, showing her face, while her lower body extends behind her, showing the back of the bikini bottom and glutes.”,
“features”: “Long straight hair with platinum blonde and dark brown streaks framing her face. Striking blue-grey eyes gazing at the camera, full lips.”
    }
  },
  “wardrobe”: {
    “top”: “A white, tight-fitting asymmetric crop top with a single strap design (visible on the upper body).”,
    “bottom”: “A black string bikini bottom worn high on the hips (visible at the back).”,
    “accessories”: “Small silver hoop earrings and a silver chain bracelet on the right wrist (holding the phone).”
  },
  “pose_action”: “Taking a selfie while lying face down, capturing both her face and rear figure in the frame.”,
  “scene”: {
    “environment”: “A bedroom setting focused on the bed area.”,
    “elements”: “White bed sheets and pillows. The specific plush toys (pink/white bunnies, round black cat with white eye patch) are visible on the bed near her.”,
“composition”: “Vertical 9:16 aspect ratio selfie shot. The frame captures her face, torso, and extends to show the glutes from behind.”
  },
  “lighting”: {
    “setup”: “Atmospheric, dim ambient lighting dominated by cool purple and blue tones, plus the light from the smartphone screen on her face.”,
    “details”: “The colored moody light washes over the scene and her hair/body. The phone screen casts a brighter, cooler light directly onto her face and eyes.”
  },
  “camera”: {
    “technical”: “Ultra-realistic selfie photograph. Sharp focus on the face and eyes, with the rear body also visible in the frame. The angle is high-down or wide-angle selfie perspective.”,
“constraints”: [
      “Aspect Ratio 9:16 (Selfie)”,
      “Subject must be taking the photo herself (Selfie)”,
      “Face MUST be visible with pouty expression”,
      “Rear glutes/bikini bottom MUST be visible in the same shot”,
      “Subject must have NO TATTOOS”,
      “Replicate the purple/blue mood lighting exactly”,
      “Include the specific plush toys”
    ]
  }
}
```

[[Female Portrait]] [[Intimate Photography]] [[Bedroom Photography]]

---

### 168. 高端运动时尚编辑滑雪

**Author**: [Bethany](https://x.com/JustBethanyai)  **Date**: 2026-02-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一张高端运动时尚的编辑摄影作品：一位自信的女性（基于参考图像），身穿黑色运动服，佩戴 Fendi 配饰，手持滑雪板，置身于白雪皑皑的高山景观中。

![高端运动时尚编辑滑雪](https://cms-assets.youmind.com/media/1770706213432_15j3e9_HAuM-IjXQAAjEuz.jpg)
![高端运动时尚编辑滑雪](https://cms-assets.youmind.com/media/1770706213449_pu66rv_HAuNATwaIAAhmvA.jpg)
![高端运动时尚编辑滑雪](https://cms-assets.youmind.com/media/1770706213556_fxd9ir_HAuM_NVXYAIQGtG.jpg)
![高端运动时尚编辑滑雪](https://cms-assets.youmind.com/media/1770706214754_ivq0bx_HAuNBFgaMAANYHq.jpg)

```
{
  "subject": {
    "identity": "Reference-based female",
    "description": "A confident woman in snowy alpine mountains, carrying a snowboard resting diagonally on her shoulder. Face and hair color should match the reference image, with all other features as described.",
    "appearance": {
      "hair": "Color and style from reference image (placeholder)",
      "skin": "Fair, natural texture",
      "body_type": "Athletic yet feminine physique",
      "face": "Facial features based on reference image",
      "expression": "Confidence, calm strength, poised elegance"
    },
    "emotion": "Confident, composed, powerful elegance"
  },
  "composition": {
    "framing": "Full-body shot",
    "camera_angle": "Slightly low-angle perspective",
    "lens": "Wide-angle lens",
    "composition_style": "Centered composition",
    "pose": "Stable, grounded, confident stance",
    "dynamic_elements": "Snowboard positioned diagonally to introduce visual tension and dynamism"
  },
  "environment": {
    "location": "Snow-covered alpine mountain landscape",
    "foreground": "Woman, snowboard, fresh snow with clearly visible crystalline texture",
    "background": "Snowy pine trees, mountain slopes, distant snow-covered hills, clean blue sky",
    "depth_of_field": "Medium depth of field, subject sharply in focus, background gently softened"
  },
  "lighting": {
    "type": "Natural daylight",
    "conditions": "Bright sunny winter weather",
    "shadows": "Soft, natural shadows",
    "highlights": "Clean, crisp highlights reflecting off snow"
  },
  "wardrobe_and_accessories": {
    "top": "Black cropped, form-fitting athletic top emphasizing a sporty silhouette",
    "bottom": "Minimalist black athletic lower garment",
    "gloves": "Black gloves",
    "headwear": "Brown-and-black patterned {argument name="brand" default="Fendi"} headband",
    "footwear": "High winter boots featuring Fendi pattern detailing",
    "eyewear": "Large dark luxury sunglasses",
    "equipment": "Dark snowboard with contrasting bindings"
  },
  "materials_and_textures": {
    "clothing": "Elastic performance fabric with clearly defined texture",
    "accessories": "Textile and fur elements in headband and boots",
    "snow": "Highly detailed crystalline snow structure",
    "snowboard": "Composite and wood materials with subtle matte finish",
    "bindings_and_glasses": "Plastic and metal components with realistic reflections"
  },
  "color_and_grading": {
    "palette": "Cold, natural winter color palette",
    "contrast": "Soft, balanced contrast",
    "sharpness": "High clarity without aggressive sharpening",
    "retouching": "Minimal, realistic fashion retouching preserving natural skin texture"
  },
  "style_and_mood": {
    "genre": "High-end sporty fashion editorial photography",
    "aesthetic": "Modern winter luxury",
    "mood": "Confidence, strength, refined femininity, visua"
  }
}
```

[[Female Portrait]] [[Mountain Landscape]]

---

### 169. 原始纪录片风格汽车内饰肖像

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-02-09  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张原始、超清晰、广角、全身的女性照片，她以“大爷式坐姿”坐在老式汽车的副驾驶座上。它指定了服装（Van Halen T 恤、颈链）、相机角度（车门外、与视线齐平），并要求深景深（f/11）和高对比度、未经编辑的胶片美学，皮肤毛孔清晰可见。

![原始纪录片风格汽车内饰肖像](https://cms-assets.youmind.com/media/1770706162166_78gcq5_HAt--zUW4AAbVgr.jpg)
![原始纪录片风格汽车内饰肖像](https://cms-assets.youmind.com/media/1770706162517_ts5k9n_HAt--zIXMAAY4s4.jpg)

```
{
  "image_analysis": {
    "subject_pose_correction": {
      "body_position": "Sitting with legs spread wide apart (manspreading pose) in a casual, unladylike posture.",
      "legs": "Knees bent and angled outward, thighs fully visible, creating a triangular composition.",
      "arms": "Left elbow firmly planted on the center console box, left hand propping up the cheek/chin. Right arm resting loosely and extended over the right knee.",
      "head_tilt": "Head tilted slightly to the left, resting heavy in the hand.",
      "interaction": "The subject is sunk deep into the seat, looking bored or effortlessly cool."
    },
    "framing_and_composition": {
      "camera_angle": "Eye-level or slightly low angle, shot from outside the car through the open passenger door.",
      "field_of_view": "Wide angle (24mm or 35mm) to capture the full body, legs, and the car's interior context.",
      "foreground_elements": "The red metal door frame of the car is visible on the edge, fully sharp and textured (no foreground blur).",
      "focus": "Deep depth of field, edge-to-edge sharpness, hyper-focal distance."
    }
  },
  "revised_prompt": {
    "format": "JSON",
    "style": "Raw, Documentary, Sharp Focus, High Fidelity"
  },
  "final_prompt": {
    "text_to_image_prompt": "A raw, ultra-sharp wide-angle full-body shot of a tanned young woman sitting in the passenger seat of a vintage car with a red door frame. She is sitting in a relaxed, 'manspreading' pose with her knees wide apart. Her left elbow rests firmly on the center console, propping up her chin with her hand, while her right arm rests loosely on her right knee. She is wearing a vintage black {argument name="shirt type" default="Van Halen t-shirt"}, a black choker, and white sneakers. The camera captures her through the open car door. Golden hour sunlight hits her messy brown hair from behind. Shot on 35mm film stock, f/11 aperture for deep depth of field, ensuring the foreground red door frame, the woman, and the wooden dashboard are all in crisp focus. Visible skin pores, sensory details, film grain, slight noise, chromatic aberration, high contrast, unedited aesthetic, crystal clear textures.",
    "negative_prompt": "bokeh, blurred background, depth of field, blurry foreground, soft focus, tilt-shift, close up, portrait crop, legs crossed, ladylike sitting, knees together, zoomed in, headshot, studio lighting, airbrushed, smooth skin, plastic, 3d render, cartoon, vignette."
  }
}
```

[[Female Portrait]] [[Wide Angle Shot]] [[Vintage Car Interior]]

---

### 170. 现代室内生活方式肖像提示（结构化）

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2026-02-09  **Language**: en

> 一个结构化的提示，用于生成一张现代室内生活方式肖像，描绘一位年轻女性斜倚在弧形沙发上，并详细说明了灯光、调色板（红色紧身衣、铂金色头发）、姿势以及豪华公寓的场景。

![现代室内生活方式肖像提示（结构化）](https://cms-assets.youmind.com/media/1770706258321_j6sa38_HAt92jzbUAA5MX6.jpg)

```
{
  "prompt": "Modern interior lifestyle portrait, young woman with long platinum white blonde wavy hair, reclining on cream white curved sofa, one hand under chin in thoughtful pose, wearing {argument name="attire" default="red fitted bodysuit"} with thin straps, looking at camera with soft neutral expression, light blue green eyes, natural makeup with nude pink lips, fair skin, modern luxury apartment interior, dark olive green curtains in background, large window with wooden frame, white walls, soft natural daylight, elegant relaxed pose, contemporary lifestyle aesthetic, 3:4",
  "negative_prompt": "outdoor, studio backdrop, heavy makeup, harsh lighting, dark moody, nighttime",
  "style": "modern lifestyle portrait, luxury interior photography, elegant relaxed aesthetic",
  "aspect_ratio": "3:4",
  "camera": {
    "type": "professional or high-end smartphone camera",
    "angle": "front facing, eye level with reclining subject",
    "framing": "medium shot, full body visible on sofa"
  },
  "lighting": {
    "type": "soft natural daylight from window",
    "quality": "diffused natural light, soft shadows, flattering illumination",
    "atmosphere": "bright modern interior with natural light"
  },
  "mood": "elegant, relaxed, sophisticated, calm, contemporary, lifestyle",
  "color_palette": "platinum blonde, red bodysuit, cream white sofa, dark olive green curtains, wooden accents, neutral tones",
  "subject_features": {
    "hair": "long platinum white blonde, soft wavy texture, flowing past shoulders and onto sofa",
    "skin": "fair, natural, healthy glow",
    "eyes": "light blue green, direct gaze at camera",
    "lips": "natural nude pink, soft relaxed",
    "eyebrows": "natural, well groomed",
    "expression": "soft neutral, thoughtful, relaxed confident"
  },
  "makeup": {
    "style": "natural minimal makeup",
    "base": "natural flawless skin",
    "eyes": "subtle natural eyeshadow, natural lashes",
    "lips": "nude pink natural"
  },
  "wardrobe": {
    "outfit": "red fitted bodysuit or one-piece, scoop neckline, thin spaghetti straps, simple minimal design"
  },
  "pose": {
    "position": "reclining on side on sofa, propped up on one elbow",
    "right_hand": "under chin in thoughtful pose",
    "left_hand": "resting on sofa cushion",
    "body": "elegant relaxed reclining position",
    "gaze": "looking directly at camera"
  },
  "setting": {
    "location": "modern luxury apartment living room",
    "furniture": "cream white curved contemporary sofa",
    "background": "dark olive green floor-length curtains, large window with wooden frame, white walls",
    "atmosphere": "sophisticated modern interior, elegant minimalist design"
  }
}
```

[[Female Portrait]] [[Fashion Photography]] [[Platinum Hair]]

---

### 171. 植物皮肤图案电影人像

**Author**: [Baby Meme X](https://x.com/babymemexx)  **Date**: 2026-02-09  **Language**: en

> 一个提示，用于生成一张女性的电影特写肖像，她的皮肤上覆盖着精致的植物花卉图案，一只眼睛上方有一个大胆的艺术形状，以油画写实风格呈现，带有戏剧性的影棚灯光和复古背景。

![植物皮肤图案电影人像](https://cms-assets.youmind.com/media/1770706168164_id5w4j_HAty5AubAAAfko7.jpg)

```
Close up cinematic portrait of a woman whose skin is covered with intricate botanical floral patterns, one eye marked with a bold {argument name="eye marking color" default="red"} artistic shape, painterly oil painting realism, {argument name="background color" default="teal"} vintage background, dramatic soft studio lighting, ultra detailed ornamental textures, editorial fine art aesthetic, shallow depth of field, cinematic color grading.
```

[[Female Portrait]] [[Fantasy Portrait]] [[Dramatic Studio Lighting]] [[Oil Painting Style]]

---

### 172. JSON 提示：调情早晨自拍肖像

**Author**: [tusina](https://x.com/tusinaai)  **Date**: 2026-02-09  **Language**: en

> 一个 JSON 提示，用于生成一张模仿真实、亲密早晨自拍的编辑写实图像。主体是一位身穿白色背心、扎着凌乱发髻的年轻女性，在柔和的自然窗光下被捕捉，眼神略带挑逗，强调自然的皮肤纹理和生活方式影响者的美学。

![JSON 提示：调情早晨自拍肖像](https://cms-assets.youmind.com/media/1770706231174_f8ktmp_HAtw0viWwAAaC7V.jpg)

```
{
  "scene": "waist-up selfie portrait of a young woman indoors",
  "composition": "handheld smartphone selfie, camera slightly above chest level, cropped at waist, intimate framing, subject centered but relaxed",
  "outfit": "simple {argument name=\"top color\" default=\"white\"} tank top, soft cotton texture, casual homewear aesthetic",
  "hair": "messy bun, loose strands framing the face naturally",
  "expression": "flirty gaze into the camera, soft half-smile, playful confidence",
  "pose": "one shoulder slightly forward, relaxed posture, natural selfie angle",
  "lighting": "soft natural window light from the side, gentle highlights on skin, warm indoor ambience",
  "environment": "minimal cozy interior background, blurred depth of field, neutral tones, lifestyle influencer vibe",
  "camera": "smartphone front camera look, slight lens distortion, shallow depth, authentic selfie realism",
  "mood": "flirty, intimate, casual, morning-at-home energy",
  "style": "editorial realism, influencer photography, natural skin texture, no heavy retouching",
  "details": "subtle collarbone highlight, soft shadows, candid moment feeling, authentic social media aesthetic",
  "negative_prompt": "over-posed, studio glamour lighting, heavy makeup look, exaggerated body proportions, artificial skin smoothing, plastic texture, stiff posture, fashion magazine styling"
}
```

[[Female Portrait]] [[Natural Skin Texture]] [[Intimate Photography]] [[Soft Window Light]]

---

### 173. 海边阳台上年轻女性的高角度自拍

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-02-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一张年轻亚洲女性在海边阳台上的高角度自拍照，重点是俏皮、略带挑逗的度假氛围，头发被风吹拂，并有具体的服装细节，例如米色罗纹上衣。该提示强调照片的真实感和“男朋友视角”的亲密感。

![海边阳台上年轻女性的高角度自拍](https://cms-assets.youmind.com/media/1770706180285_d7lhol_HAtryBTbQAE4PJ-.jpg)

```
{ "subject": { "description": "A young Asian woman taking a high-angle selfie on a seaside balcony, exuding a playful and flirtatious holiday vibe.", "mirror_rules": "N/A", "age": "Early 20s", "expression": { "eyes": { "look": "Winking right eye, left eye gazing warmly at camera", "energy": "Playful, charming, slightly squinting against the light", "direction": "Direct eye contact" }, "mouth": { "position": "Soft closed smile", "energy": "Relaxed, corners uplifted" }, "overall": "Effortlessly cute and engaging" }, "face": { "preserve_original": true, "makeup": "Natural Korean style, soft coral lip tint, subtle blush" }, "hair": { "color": "Dark brown/Black", "style": "Shoulder-length bob, layered", "effect": "Chaotic windblown texture, strands messy across face and lips, dynamic motion" }, "body": { "frame": "Slim, feminine curves", "waist": "Not visible", "chest": "Visible cleavage due to low-cut top and high camera angle", "legs": "Not visible", "skin": { "visible_areas": "Face, neck, chest", "tone": "Fair, warm undertone", "texture": "Smooth, hydrated, soft-focus pores", "lighting_effect": "Natural daylight reflecting soft sheen on collarbones and forehead" } }, "pose": { "position": "Leaning slightly forward", "base": "Standing", "overall": "High-angle selfie pose, head tilted slightly to the right" }, "clothing": { "top": { "type": "Ribbed knit long-sleeve top", "color": "Beige / Cream", "details": "Deep U-neck or V-neck, tight fitting, vertical texture", "effect": "Soft fabric draping over curves" }, "bottom": { "type": "N/A", "color": "N/A", "details": "N/A" } } }, "accessories": { "jewelry": "Silver dainty necklace with a small heart pendant, small stud earring", "headwear": "N/A", "device": "N/A", "prop": "N/A" }, "photography": { "camera_style": "Smartphone selfie camera", "angle": "High angle, slightly tilted clockwise, close-up", "shot_type": "Upper body portrait", "aspect_ratio": "4:5", "texture": "High definition but organic, slight motion blur on hair", "lighting": "Soft overcast natural daylight, diffuse shadows, no harsh contrast", "depth_of_field": "Background slightly out of focus (bokeh)" }, "background": { "setting": "Outdoor terrace or balcony", "wall_color": "N/A", "elements": [ "Glass balustrade railing", "Sandy beach visible through glass", "Ocean waves with white foam", "Wooden deck floor" ], "atmosphere": "Breezy, seaside, open-air, vacation", "lighting": "Bright natural sky light" }, "the_vibe": { "energy": "Dynamic, windy, cheerful", "mood": "Flirty, relaxed, holiday romance", "aesthetic": "K-pop idol daily life, Instagram influencer, effortless beauty", "authenticity": "High, emphasized by messy hair and spontaneous wink", "intimacy": "Boyfriend perspective selfie", "story": "A quick selfie sent to a lover during a beach trip", "caption_energy": "Windy day at the beach! 🌬️💖" }, "constraints": { "must_keep": [ "Windblown hair effect", "Winking expression", "Beige ribbed top text"}
```

[[Female Portrait]] [[Wind-Blown Hair]] [[Coastal Setting]]

---

### 174. 超逼真夏日度假照片提示，带极致人物形象

**Author**: [LexiPrompt](https://x.com/Artist04048661)  **Date**: 2026-02-09  **Language**: en

> 一个高度详细的提示，旨在实现最大的照片真实感，特别关注皮肤和纺织品纹理，使用智能手机相机语言。场景描绘了一个拥有夸张沙漏身材的女孩，穿着白色泳衣，坐在海边的沙滩椅上，强调温暖的傍晚光线和精英度假村的氛围。

![超逼真夏日度假照片提示，带极致人物形象](https://cms-assets.youmind.com/media/1770706251164_xl2yw8_HAtmNn4aMAAqKIX.jpg)

```
- [ ] UHD photos taken on a smartphone with a high-end mobile CMOS sensor, 9:16 vertical format, natural 5600K lighting, f/1.8 aperture, realistic optical depth with subtle natural bokeh, slight authentic sensor noise, no beauty filters, no post-processing or AI smoothing; hyper-realistic skin reproduction with physically accurate subsurface scattering, visible pores, fine vellus hair, natural sebum and micro-shine in the T-zone, real skin displacement and slight wrinkles at contact points; extremely detailed textile realism with visible texture at the fiber level, looped knit structure, realistic pilling, fabric weight, drape and tension wrinkles; realistic materials and surfaces, preserved microcontrast, clear focus on skin texture and eyes, no artificial glow, blur, retouching, maximum photographic realism. Photo of a girl lying on a deck chair by the sea, holding a "{argument name="magazine title" default="LE POPPI"}" magazine in her hands and drinking a drink from a pink can with a straw. The girl has a natural natural appearance. She has an extreme "hourglass" figure: very large, naturally full breasts, an extremely narrow waist and wide hips. She is dressed in a {argument name="swimsuit color and style" default="white swimsuit with black inserts"} and white high-heeled shoes. Her long blond hair is loose, voluminous, she wears narrow black sunglasses. The background is a coast overlooking the blue sea, rocks and hills with houses, emphasizing the summer atmosphere of a vacation at an elite resort. The lighting is bright, evening, warm.
```

[[Female Portrait]] [[Evening Light]]

---

### 175. 高端时尚大片：镜面反射

**Author**: [Aylin](https://x.com/Ai_aylinfc)  **Date**: 2026-02-09  **Language**: en

> 一个高度详细的提示，用于生成一张超现实的时尚大片图像：一位年轻女性身着优雅的黑色晚礼服，站在镜子前，形成完美的倒影。强调奢华的电影感氛围、柔和的漫射光，以及专业的 85mm 镜头美学。

![高端时尚大片：镜面反射](https://cms-assets.youmind.com/media/1770706174273_ui2v72_HAtUf7kbcAAL3Li.jpg)

```
A breathtaking young woman in her early twenties with long, silky blonde hair flowing naturally down her back and over her shoulders, each strand finely detailed and softly illuminated. She is standing gracefully in front of a tall, elegant mirror, creating a realistic and perfectly aligned mirror reflection that adds depth and visual interest to the composition. She is wearing an exquisite {argument name="dress color" default="black"} evening gown crafted from premium fabric, featuring delicate crystal-embellished straps that catch and reflect the light with subtle sparkle. The dress fits her figure flawlessly, with a refined silhouette that exudes timeless elegance and high-fashion sophistication.
Her pose is calm, confident, and editorial—one shoulder slightly turned, chin gently lifted, arms relaxed, conveying effortless luxury and poise. Her facial expression is serene and composed, with softly defined features, natural makeup, smooth glowing skin, subtle contouring, and muted nude lips, suitable for a couture fashion shoot. Her eyes are sharp and expressive, focused either on her reflection or slightly past the camera, adding a sense of mystery and allure.
The setting features a rich wooden wall backdrop with warm tones and visible texture, complementing the black dress and enhancing the upscale atmosphere. The mirror frame is minimal and elegant, blending seamlessly into the environment. Soft, diffused lighting wraps gently around her body and face, creating smooth highlights and shadows without harsh contrast. The lighting emphasizes realistic skin texture, fine fabric details, crystal reflections, and natural depth, producing a luxurious cinematic mood.
The image is captured in ultra-high resolution with professional fashion photography aesthetics, shallow depth of field, crisp focus on the subject, and softly blurred background. Realistic hair movement, precise anatomy, accurate proportions, and natural posture are maintained throughout. The overall style resembles a high-end fashion editorial or luxury brand campaign, shot with a full-frame DSLR or mirrorless camera using an 85mm lens, studio-quality optics, advanced color grading, balanced exposure, and refined contrast, delivering a hyper-realistic, magazine-cover-ready result.
```

[[Female Portrait]] [[85mm Lens]] [[Soft Diffused Light]] [[Black Evening Gown]]

---

### 176. 梦幻般的双重曝光艺术肖像

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-02-09  **Language**: en

> 一个用于生成超现实主义年轻女性艺术肖像的提示，其特点是梦幻而富有诗意的氛围。它以柔和的鼠尾草绿色背景为特色，前景中漂浮着带有动态模糊的精致花朵，脸部则带有微妙的双重曝光/慢速快门效果。

![梦幻般的双重曝光艺术肖像](https://cms-assets.youmind.com/media/1770706184661_wiufmv_HAtAx1GbIAAbojs.jpg)
![梦幻般的双重曝光艺术肖像](https://cms-assets.youmind.com/media/1770706185065_sndyzl_HAtAxyeboAAVTwe.jpg)

```
Ultra-realistic fine-art portrait of a young woman with soft natural features, minimal makeup, and calm introspective expression. Pastel muted background in sage green tones. Delicate flowers drifting across the frame in the foreground, creating intentional motion blur and soft streaks of light. Subtle double exposure and slow-shutter motion effects across the face, dreamy and poetic atmosphere. Gentle diffused lighting with smooth highlights on skin, natural texture preserved. Elegant minimalist composition, emotional and serene mood, editorial fine-art photography style, shallow depth of field, cinematic softness, painterly realism, ultra-high resolution, 8K quality.
```

[[Female Portrait]] [[Motion Blur]] [[Surrealist Portrait]] [[Dreamlike Aesthetic]]

---

### 177. Sadie Sink 录音室肖像

**Author**: [Sadia](https://x.com/SadiaMalik182)  **Date**: 2026-02-09  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张年轻女性（参考对象为 Sadie Sink）在专业录音棚隔音间内的中景肖像。提示词详细描述了她的外貌（红发、雀斑）、着装（白色背心、粉色运动裤）、配饰（耳机、麦克风）以及环境（深色吸音板），并指定了柔和、直射的录音棚灯光。

![Sadie Sink 录音室肖像](https://cms-assets.youmind.com/media/1770706159948_21drn8_HAskNIFasAAIZ_F.jpg)

```
{
  "image_description": "A portrait of a young woman in a recording studio, wearing headphones and looking upwards.",
  "subject": {
    "appearance": "Young woman with long, wavy vibrant {argument name="hair color" default="red"} hair, fair skin with visible freckles, and blue eyes.",
    "expression": "Contemplative, looking upwards and slightly to the right, away from the camera.",
    "pose": "Seated or leaning back with hands resting on hips/upper thighs, body angled slightly towards the right.",
    "makeup": "Natural look with minimal makeup, highlighting freckles."
  },
  "attire": {
    "top": "White ribbed tank top, cropped length, fitting snugly.",
    "bottom": "Pink baggy sweatpants or lounge pants.",
    "accessories": [
      "Black over-ear studio headphones with a cable draping down",
      "Multiple bracelets on the left wrist",
      "Rings on fingers",
      "Manicured nails"
    ]
  },
  "environment": {
    "setting": "Professional recording studio booth.",
    "foreground": "Large silver condenser microphone with a black pop filter and shock mount (partially out of focus on the right).",
    "background": "Dark acoustic soundproofing panels on the walls, a section of wooden paneling, and an electrical outlet near the floor."
  },
  "technical_details": {
    "lighting": "Soft, direct studio lighting illuminating the subject's face and upper body.",
    "angle": "Eye-level or slightly high angle shot.",
    "composition": "Medium shot capturing the subject from the thighs up."
  }
}
```

[[Female Portrait]] [[Casual Fashion]] [[Red Hair]]

---

### 178. 复古未来主义街机摄影肖像

**Author**: [Human AI Gallery | Prompt Architect](https://x.com/HumanAIGallery)  **Date**: 2026-02-09  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张详细的赛博朋克风格编辑快照，描绘一名年轻女性身处昏暗、拥挤的复古街机厅中，重点突出科技服饰美学、RGB 照明和高对比度摄影风格。

![复古未来主义街机摄影肖像](https://cms-assets.youmind.com/media/1770706200354_3w7xai_HAsHChyWgAAbuFo.jpg)

```
{
  "image_prompt": {
    "meta": {
      "aspect_ratio": "9:16",
      "style": "Retro-futuristic arcade photography"
    },
    "subject": {
      "description": "22-year-old woman with a tech-wear aesthetic",
      "face": "Wearing clear-rimmed glasses that reflect the neon 'GAME OVER' screen in bright pink and cyan, focused gaze",
      "skin": "Bathed in RGB light, glowing pores, high-contrast shadows",
      "hair": "Short 'bixie' cut with neon-colored tips",
      "pose": "Leaning against the joystick of a Street Fighter cabinet, holding a colorful juice box, looking into the lens with an 'it-girl' attitude",
      "outfit": "Sheer mesh long-sleeve top with abstract prints, silver chunky jewelry, low-rise mini skirt"
    },
    "environment": {
      "location": "A dim, crowded retro arcade in {argument name="city" default="Tokyo"} or Seoul",
      "background_elements": [
        "Blurred rows of glowing gaming cabinets",
        "Neon signs reflecting on the greasy floor",
        "Dust motes dancing in the projector beams"
      ]
    },
    "lighting": {
      "type": "Direct RGB glow from the game screen",
      "characteristics": [
        "Dual-tone lighting (pink on one side, teal on the other)",
        "Deep shadows emphasizing facial structure",
        "High saturation levels"
      ]
    },
    "photography_style": {
      "style": "Cyberpunk editorial snapshot",
      "camera_look": "35mm vintage lens with high contrast",
      "imperfections": "Lens flare from arcade screens, film-like grain, saturated color bleeding",
      "mood": "Nocturnal, nostalgic, electric, cool"
    }
  }
}
```

[[Female Portrait]]

---

### 179. 2026 年全国新闻日社论海报

**Author**: [2next](https://x.com/merdesalamongan)  **Date**: 2026-02-09  **Language**: en

> 一个高度详细且结构化的提示，用于生成一张超现实的印度尼西亚国家新闻日官方编辑海报，海报中有一位女性记者被描绘成精致的赛博格，呈现出正式的肖像，象征着人类良知与技术的平衡，并对灯光、排版和文本内容提出了具体要求。

![2026 年全国新闻日社论海报](https://cms-assets.youmind.com/media/1770706167575_otdxpr_HArvC6qaAAApcdK.jpg)
![2026 年全国新闻日社论海报](https://cms-assets.youmind.com/media/1770706167532_ob89qz_HArvC67bAAAA9f-.jpg)

```
Ultra-realistic official editorial poster for Hari Pers Nasional 2026, dignified, human-centered, and authoritative.

A close-up formal portrait of an Indonesian female journalist portrayed as a refined female cyborg, representing the balanced integration of human conscience and advanced technology in national journalism.

Her expression is tenang, tegas, dan penuh empati, reflecting integrity, responsibility, and commitment to truth.
Her gaze is steady and composed behind elegant rose-gold tinted cat-eye sunglasses with subtle reflective lenses, conveying clarity and credibility.
Her long silver-white hair is styled in a neat, elegant high ponytail, orderly and controlled, with minimal soft strands framing the face. No wind, no dramatic motion — formal editorial portrait.

Subtle signs of professional fatigue blend with quiet dignity, symbolizing dedication and service.
 Restrained, refined cybernetic detailing on the neck and shoulders integrates seamlessly with natural human skin, conveying technological advancement with ethical restraint.

She holds a simple pen close to her chest, softly illuminated, symbolizing integrity, conscience, and responsibility of the press.
Background: softly blurred with shallow depth of field, featuring understated newspaper headlines, archival press imagery, and minimal digital light accents — secondary, subdued, and respectful.

Lighting: warm, soft, and controlled. Natural key light highlights the face with gentle contrast, formal editorial lighting suitable for official publications.

Typography (mandatory, clear, and formal):
Classic editorial serif typeface inspired by newspaper and state publications. High-contrast white or light gray text on a darker background, clean alignment, official layout.

Printed text on poster (must be clearly legible):

“Selamat Hari Pers Nasional 2026”
“Di tengah disrupsi digital, mari kita dukung pers yang sehat untuk mencerdaskan bangsa dan menjaga kedaulatan informasi.”

“Pers Sehat, Ekonomi Berdaulat, Bangsa Kuat.”

Small formal editorial credit at the bottom corner (sharp and readable):
 “didesain oleh promptverse”

Ultra-high resolution, static and symmetrical composition, calm authority, respectful national tone.
Appropriate for official government, institutional, and national commemorative media.

🔧 Optional Negative Prompt

dynamic pose, wind-blown hair, exaggerated cyberpunk style, chaotic lighting,
aggressive expression, action scene, messy composition, unreadable text,
distorted typography, blur, dramatic effects
#haripersnasional #HPN2026
```

[[Female Portrait]] [[Cyberpunk Aesthetic]] [[Surrealist Portrait]]

---

### 180. 英式乡村花园中的优雅夏日肖像

**Author**: [Aylin](https://x.com/Ai_aylinfc)  **Date**: 2026-02-09  **Language**: en

> 生成一张超现实主义的年轻女性全身肖像的提示词，背景是黄金时段的经典英式乡村花园。她身穿淡粉色碎花连衣裙，强调柔和的日落光线、奶油般的焦外虚化和超精细的纹理，营造出梦幻、浪漫、宁静的审美效果。

![英式乡村花园中的优雅夏日肖像](https://cms-assets.youmind.com/media/1770706182789_6nogcj_HArbBVDbcAAj-ic.jpg)

```
Photorealistic full-length portrait of an elegant young woman, around 22 years old, with fair glowing skin and soft medium-brown hair flowing naturally in a gentle summer breeze. She is standing gracefully in a classic English country garden at golden hour, bathed in warm sunset light with soft sun rays filtering through lush greenery. She is wearing a feminine pastel pink cotton sundress with a delicate floral print, sleeveless design, square neckline, fitted bodice accentuating the waist, and a flowing flared skirt with a subtle ruffled hem ending at mid-calf. A simple, elegant pearl necklace rests at her collarbone, adding a timeless, romantic touch. Her makeup is natural and refined: luminous skin, subtle rosy blush, soft neutral eyeshadow, lightly defined lashes, and natural pink lips. She has a gentle, dreamy smile and is looking directly at the camera with a calm, confident expression, one hand lightly touching her hair in a candid, effortless pose.
She is surrounded by tall blooming {argument name="flower type" default="pink hydrangeas"} in the foreground, with neatly trimmed deep-green boxwood hedges framing the scene. In the background, a charming English countryside brick cottage with a traditional thatched roof appears softly blurred, creating depth and atmosphere. The overall mood is dreamy, romantic, and serene, evoking a classic European summer aesthetic. Shallow depth of field with creamy bokeh, ultra-realistic skin texture, highly detailed fabric folds, lifelike lighting and shadows. Shot as a high-end fashion and lifestyle photograph on Canon EOS R5, 85mm lens, f/1.8, cinematic composition, natural color grading, ultra-sharp focus, hyper-realistic, editorial-quality photography, 8K resolution.
```

[[Female Portrait]] [[Golden Hour]] [[Full Body Portrait]] [[Floral Dress]]

---

### 181. 超逼真的海滩时尚摄影，具有特定的身体约束

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-02-08  **Language**: en

> 一个高度受限且细节丰富的提示词，用于生成一张在多云海滩上的女性超写实照片，重点关注特定的身体特征（沙漏型身材、丰满挺拔的胸部、无纹身）和服装（米色三角比基尼）。该提示词包含严格的约束条件，以保持所需的体格和环境。

![超逼真的海滩时尚摄影，具有特定的身体约束](https://cms-assets.youmind.com/media/1770706252925_5zlpmf_HArBs7gWYAA1o5O.jpg)
![超逼真的海滩时尚摄影，具有特定的身体约束](https://cms-assets.youmind.com/media/1770706252966_63zzu1_HArBssLXYAAn9Eo.jpg)

```
{
  “subject”: {
    “description”: “An ultra-realistic photograph of a beautiful young woman with long blonde hair, standing on a windswept beach under a cloudy sky.”,
    “body”: {
      “physique”: “A well-defined, athletic hourglass figure with visible abdominal muscles and curvy hips. She has significantly large, very firm, and perky breasts that are prominent in her silhouette. Her skin is smooth, naturally tanned, and completely free of any tattoos.”,
      “pose”: “Standing facing slightly to the right, looking out at the ocean. Her left hand is adjusting the side strap of her bikini bottom, and her right hand is near her hip. Her blonde hair is blowing in the wind.”,
      “features”: “Long blonde hair tied back with loose strands blowing forward. Beautiful, natural, and sexy facial features with a fresh, makeup-free look, gazing towards the sea. She wears small gold hoop earrings.”
    }
  },
“wardrobe”: {
    “top”: “A beige/nude triangle bikini top with thin spaghetti straps that emphasizes the large size and firm shape of her breasts.”,
    “bottom”: “A matching beige/nude string bikini bottom with thin side straps worn high on the hips.”,
    “accessories”: “Small gold hoop earrings.”
  },
  “pose_action”: “Standing on the beach, adjusting her bikini bottom while looking at the ocean, capturing a natural and alluring moment.”,
  “scene”: {
    “environment”: “A sandy tropical beach on a cloudy, overcast day, with the ocean in the background.”,
    “elements”: “Turquoise ocean waves breaking gently, a rocky outcrop on the right side, and a heavy, cloudy grey sky. The sand is light-colored and wet near the water.”,
    “composition”: “Vertical 4:5 aspect ratio. A medium shot framing the woman from the mid-thigh up, capturing her against the ocean and sky background, with the large rock on the right.”
  },
“lighting”: {
    “setup”: “Soft, diffused, natural daylight from the overcast sky.”,
    “details”: “The light is even and flattering, highlighting the natural texture of her skin, muscle definition, and the wet sand without harsh shadows.”
  },
  “camera”: {
    “technical”: “Ultra-realistic, high-resolution photograph. Sharp focus on the woman. The background is slightly blurred but retains detail.”,
    “constraints”: [
      “Aspect Ratio 4:5”,
      “Maintain the specific pose and body shape described”,
      “Breasts must be large, firm, and perky”,
      “The subject must have NO TATTOOS (skin must be completely clear)”,
      “Maintain the specific beige bikini style and color”,
      “The subject’s face must be beautiful, natural, and sexy”,
      “Replicate the overcast beach environment and lighting”
    ]
  }
}
```

[[Female Portrait]] [[Hourglass Figure]] [[Bikini Photography]]

---

### 182. Pastel Meadow 时尚大片，带胶片雾化效果

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-08  **Language**: en

> 一个高度详细、结构化的提示，用于创作一组梦幻、怀旧的时尚大片图像，背景设定在阳光明媚的夏日草甸。它指定了一位身穿腮红粉色紧身胸衣迷你连衣裙的女性主体，采用 35mm 胶片效果，带有微妙的机载闪光灯和薄雾，以营造柔和、略微过曝的模拟美学。

![Pastel Meadow 时尚大片，带胶片雾化效果](https://cms-assets.youmind.com/media/1770706220233_vvbx26_HAqxDo0WAAECYQT.jpg)

```
{
 "generation_request": {
 "meta_data": {
 "task_type": "pastel_meadow_fashion_editorial",
 "priority": "highest",
 "language": "en",
 "style_version": "v1.0_summer_meadow_pink_dress_flash_haze"
 },

 "output": {
 "aspect_ratio": "4:5",
 "resolution": "high",
 "num_images": 1
 },

 "scene": {
 "environment": "sunny summer meadow with tall green grass, distant wildflowers in soft focus",
 "atmosphere": "dreamy, warm, romantic, nostalgic",
 "composition": "subject sitting in grass, upper body and legs visible, background softly blurred"
 },

 "subject": {
 "gender": "female",
 "pose": "sitting on the grass with legs angled to the side, both arms raised holding hair, relaxed shoulders",
 "expression": "eyes closed, serene face, peaceful and sensual but elegant",
 "hair": "dark brown hair, soft volume, loose natural waves",
 "makeup": {
 "skin": "sun-kissed glow, luminous highlights on cheekbones and shoulders, natural texture preserved",
 "eyes": "soft neutral eye makeup",
 "lips": "soft nude-pink lipstick, satin finish"
 }
 },

 "wardrobe": {
 "dress": {
 "color": "{argument name=\"dress color\" default=\"powder blush pink\"}",
 "type": "strapless corset-style mini dress",
 "details": "structured bodice with subtle seams, soft skirt with gentle volume, romantic silhouette",
 "fabric": "lightweight satin or chiffon blend with delicate sheen"
 },
 "jewelry": {
 "earrings": "small delicate studs",
 "bracelet": "thin minimal bracelet"
 }
 },

 "camera": {
 "camera_type": "35mm film look",
 "lens": "35mm lens",
 "aperture": "f/2.8",
 "focus": "sharp on face and dress, gentle falloff into grass",
 "framing": "mid-wide portrait, lifestyle editorial composition"
 },

 "lighting": {
 "type": "soft daylight with subtle on-camera flash",
 "key_light": "natural sun diffused by light haze",
 "flash": "gentle fill flash creating glossy highlights on skin and a slightly overexposed dreamy look",
 "shadows": "very soft, minimal harshness"
 },

 "color_grading": {
 "palette": "pastel greens, warm golden skin tones, blush pink dress",
 "white_balance": "slightly warm",
 "saturation": "soft, slightly reduced for a nostalgic feel",
 "look": "dreamy summer film editorial"
 },

 "film_effects": {
 "grain": "fine to medium 35mm film grain",
 "haze": "soft film haze / glow",
 "halation": "subtle highlight bloom",
 "softness": "slight analog softness, not digitally sharp",
 "vignette": "very subtle natural vignette"
 },

 "global_constraints": {
 "rating": "PG-13",
 "no_nudity": true,
 "no_explicit_sexual_content": true,
 "no_text": true,
 "no_logos": true,
 "no_watermark": true,
 "no_ai_plastic_skin": true,
 "no_over_sharpening": true,
 "no_distortion": true
 }
 }
```

[[Female Portrait]] [[35mm Film Aesthetic]] [[Corset Mini Dress]]

---

### 183. 适用于 Nano Banana Pro 的牛仔女郎时尚摄影提示

**Author**: [bengi](https://x.com/p3rikly)  **Date**: 2026-02-08  **Language**: en

> 一个为 Nano Banana Pro 设计的详细 JSON 提示，用于生成一张女性身着牛仔/西部风格服装的半身时尚照片。提示详细说明了拍摄对象的身体特征（曲线健美、金色编发）、姿势（手叉腰、手持酒杯）以及一套具体且详细的服装（无肩带白色/黄色露脐上衣、牛仔马裤式短裤、红色牛仔帽）。场景设置为纯色浅色摄影棚背景墙，采用柔和的前置照明，强调俏皮、自信和迷人的美学。

![适用于 Nano Banana Pro 的牛仔女郎时尚摄影提示](https://cms-assets.youmind.com/media/1770619736238_mgk1px_HAqPdLkbMAA2btL.jpg)

```
{   
"subject": {     "character": "woman in the referance images",     "age": "20-30",     "body_type": "curvy athletic",     "skin_tone": "same as referance images",     "face": {       "features": "soft, symmetrical, high cheekbones",       "expression": "confident, slightly playful, lips slightly parted",       "eyes": "same as reference images"     }   },   "pose": {     "stance": "one hand on hip, other hand holding a wine glass",     "body_angle": "slightly turned to camera",     "posture": "confident, relaxed",     "legs": "slightly apart"   },   "outfit": {     "theme": "cowgirl / western inspired",     "top": {       "type": "strapless bandeau crop top",       "colors": "white base with yellow band across chest",       "details": "red piping line, silver circular buckle at center"     },     "armwear": {       "left": "yellow armband with red ribbon detail",       "right": "yellow armband with red ribbon detail"     },     "bottom": {       "type": "high-waisted denim shorts",       "details": "front cutout like a chaps-style, white side panels"     },     "belt": {       "color": "brown leather",       "buckle": "large ornate gold buckle"     },     "hat": {       "type": "wide-brimmed cowgirl hat",       "color": "{argument name="hat color" default="red"} with white stitching",       "position": "centered, slightly tilted"     }   },   "hair": {     "color": "blonde",     "style": "two long braids",     "part": "middle part",     "loose_strands": "soft face-framing strands"   },   "accessories": {     "earrings": "small gold hoops",     "glass": "clear wine glass with white wine",     "makeup": {       "lips": "natural pink",       "eyes": "soft eyeliner, neutral eyeshadow",       "cheeks": "subtle blush"     }   },   "mood_and_style": {     "vibe": "playful, confident, glamorous",     "genre": "fashion photography, cosplay-inspired",     "aesthetic": "clean, bright, slightly retro"   },   "background": {     "type": "plain wall",     "color": "{argument name="background color" default="light neutral (off-white)"}",     "details": "minimal, studio-like"   },   "lighting": {     "type": "soft studio lighting",     "direction": "frontal",     "shadows": "minimal",     "tone": "warm, natural"   },   "camera": {     "angle": "eye-level",     "frame": "mid shot (waist up)",     "lens": "50mm",     "depth_of_field": "shallow background blur"   },   "composition": {     "crop": "centered subject",     "spacing": "balanced negative space",     "focus": "sharp on face and outfit details"   },   "negative_prompt": [     "cartoon",     "blurry",     "low quality",     "extra limbs",     "deformed anatomy",     "wrong outfit",     "incorrect hat",     "incorrect colors",     "background clutter",     "text",     "watermark"   ] }
```

[[Female Portrait]] [[Studio Background]] [[Cowboy Hat]]

---

### 184. 巴西国旗比基尼海滩照片提示

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-02-08  **Language**: en

> 一个复杂的 JSON 提示，旨在生成一张年轻女性（参考 Sadie Sink/Natalia Dyer）坐在沙滩上，身穿巴西国旗图案比基尼的超逼真图像。该提示详细说明了人物特征（湿润的姜色头发、明显的雀斑、皮肤上的沙粒）、环境（阴沉的天空、大块岩石、海浪），并包含用于 Stable Diffusion 和 Midjourney 格式的示例提示字符串。

![巴西国旗比基尼海滩照片提示](https://cms-assets.youmind.com/media/1770619730946_vu4v1j_HAp5LD7aQAAUTo2.jpg)
![巴西国旗比基尼海滩照片提示](https://cms-assets.youmind.com/media/1770619730871_3tvdvj_HAp5LDdawAEGqRV.jpg)

```
{
  "image_analysis": {
    "subject": {
      "gender": "female",
      "hair": "wet, shoulder-length, ginger/reddish-brown, messy texture",
      "skin": "fair, prominent freckles on face and arms, sand grains clinging to skin",
      "clothing": {
        "item": "string bikini",
        "colors": ["green", "yellow", "blue"],
        "pattern": "Brazilian flag motif",
        "style": "triangle top, side-tie bottom"
      },
      "pose": "sitting on sand, body angled away from camera, looking back over left shoulder, weight supported by left arm, legs extended and bent"
    },
    "environment": {
      "location": "beach coastline",
      "weather": "overcast, cloudy, grey sky",
      "elements": [
        "beige sand",
        "large dark granite rocks",
        "ocean waves",
        "distant green hills/vegetation"
      ]
    },
    "technical": {
      "lighting": "soft, diffuse, natural overcast light, no harsh shadows",
      "angle": "eye-level, medium shot",
      "style": "candid photography, realistic, high definition"
    }
  },
  "prompt_strings": {
    "stable_diffusion_format": "photograph of a young woman with wet ginger hair and freckled skin sitting on a sandy beach, wearing a green and yellow Brazilian flag bikini, looking back at viewer over shoulder, sand on skin, overcast sky, large rocks in background, ocean waves, wet hair strands, soft natural lighting, cloudy day, high resolution, 8k, realistic skin texture, candid beach photography",
    "midjourney_format": "/imagine prompt: A realistic photo of a young woman with wet red hair and freckles sitting on a beach, wearing a green and yellow Brazil bikini. She is looking back at the camera. Sand is stuck to her skin. Background of large rocks, ocean waves, and a cloudy grey sky. Soft diffuse lighting, shot on 35mm lens, photorealistic, highly detailed --ar 3:4 --v 6.0",
    "descriptive_long": "A high-resolution, photorealistic shot of a young woman with fair skin and freckles sitting on a sandy shore. She has wet, messy red hair that falls to her shoulders. She is wearing a green and yellow string bikini with a Brazilian flag design. Her pose is relaxed, sitting on the sand and leaning back on one hand while looking directly at the camera over her shoulder. Grains of sand are clinging to her legs and thighs. The background features a moody, overcast sky, churning ocean waves, and large coastal rock formations. The lighting is flat and natural, typical of a cloudy day at the beach."
  }
}
```

[[Female Portrait]] [[Freckled Skin]] [[Wet Hair]] [[Beach Photography]]

---

### 185. 冰雪节拍：戴耳机的冬日森林肖像

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-02-08  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超现实的年轻女性肖像，她戴着耳机，半躺在寂静冬季森林的深厚积雪中。该提示指定了技术细节，例如相机设备（Sony A7R V）、特定的色彩分级（Kodak Portra 400），以及高频纹理细节，如自然雀斑和瓷器般肌肤。

![冰雪节拍：戴耳机的冬日森林肖像](https://cms-assets.youmind.com/media/1770619687604_w90sdq_HAp3DRXbkAAoBp7.jpg)
![冰雪节拍：戴耳机的冬日森林肖像](https://cms-assets.youmind.com/media/1770619687551_a8hyhs_HAp3DQrXMAEmM1y.jpg)
![冰雪节拍：戴耳机的冬日森林肖像](https://cms-assets.youmind.com/media/1770619687664_xg2r9v_HAp3DRNaIAAkvg1.jpg)

```
{
  "prompt_data": {
    "subject": {
      "appearance": "Young woman with waist-length, voluminous, wavy fiery copper-red hair, middle part.",
      "complexion": "Porcelain pale skin with high-frequency texture and natural golden freckles.",
      "eyes": "Piercing light blue/grey eyes, direct eye contact.",
      "expression": "Serene, soft, neutral, and calm."
    },
    "attire": {
      "headwear": "Large, matte dark blue over-ear wireless headphones.",
      "top": "Tight-fitting, heather grey, ribbed knit short-sleeved crop top.",
      "bottoms": "Matching heather grey ribbed knit sweatpants."
    },
    "pose": {
      "position": "Semi-reclined directly on fresh powder snow.",
      "body_language": "Leaning back on right hand (hand sinking into snow), left arm resting on surface. Legs extended, left knee slightly bent."
    },
    "environment": {
      "setting": "Silent outdoor winter forest.",
      "ground": "Deep, pristine white powder snow.",
      "background": "Dense evergreen forest laden with heavy snow, rendered with bokeh."
    },
    "technical_details": {
      "camera_gear": "{argument name="camera gear" default="Sony A7R V, 50mm f/1.2 GM lens"}.",
      "camera_settings": "Aperture f/2.8, ISO 100, Shutter 1/500s.",
      "quality": "16-bit RAW, 8K Ultra HD, hyper-realistic.",
      "lighting": "Overcast natural softbox lighting, diffuse and shadowless.",
      "post_processing": "{argument name="color grading" default="Kodak Portra 400 color grading"}, sharp focus on eyes, subsurface scattering enabled."
    }
  }
}
```

[[Female Portrait]] [[Snow Scene]] [[Kodak Portra 400]] [[Porcelain Skin]]

---

### 186. 电影院里的抓拍肖像

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-02-08  **Language**: en

> 一个高度结构化的提示，用于生成一张 8K 超高清、超逼真的年轻女性肖像，她随意地坐在电影院座位上。提示详细描述了她的外貌、着装（黑色 T 恤、阔腿牛仔裤）、姿势和环境，强调电影般的氛围照明和抓拍的摄影风格。

![电影院里的抓拍肖像](https://cms-assets.youmind.com/media/1770619674141_n3159g_HApy-lkbkAAP0yt.jpg)

```
{
  "prompt_schema": {
    "meta": {
      "aspect_ratio": "9:16",
      "orientation": "Vertical Long",
      "resolution": "8K UHD",
      "quality_preset": "Ultra Realistic HDR"
    },
    "subject": {
      "demographics": "Young woman, early 20s, fair complexion",
      "hair": {
        "color": "Dark brown",
        "style": "Long, wavy layers with curtain bangs",
        "texture": "Silky, voluminous"
      },
      "face": {
        "expression": "Soft smile, direct eye contact, relaxed demeanor",
        "makeup": "Subtle natural glam, soft peach blush, nude lip",
        "pose_details": "Resting chin on right palm, right elbow propped on leg/armrest"
      },
      "body_pose": "Sitting relaxed in a cinema seat, leaning slightly forward, legs spread comfortably, left hand resting on left knee"
    },
    "apparel": {
      "top": "Solid black crew-neck t-shirt, short sleeves, fitted but comfortable",
      "bottom": "Wide-leg light blue denim jeans, vintage wash, loose fit",
      "footwear": "White casual sneakers, clean aesthetic"
    },
    "distinctive_features": {
      "tattoos": "Small, detailed butterfly tattoo on the inner right wrist",
      "accessories": "Minimalist/none visible"
    },
    "environment": {
      "location": "Movie theater / Cinema hall",
      "foreground": "Red plush cinema seat with black leather headrest",
      "background": "Multiple rows of empty matching red stadium seats extending into depth",
      "details": "Gold '43X' branding text on seat headrests, dim atmospheric interior"
    },
    "lighting_and_atmosphere": {
      "type": "Cinematic ambient lighting",
      "sources": "Soft overhead ceiling lights, warm glow reflecting on the subject's face",
      "mood": "Cozy, casual, anticipating, evening vibe",
      "shadows": "Soft shadows in the background rows, creating depth"
    },
    "camera_settings": {
      "shot_type": "Full body portrait / Medium shot",
      "angle": "Eye-level, straight on",
      "focus": "Sharp focus on subject, slight bokeh/depth of field on background seats",
      "style": "Photorealistic, candid style photography, high fidelity textures"
    }
  }
}
```

[[Female Portrait]] [[8K Portrait]]

---

### 187. 身穿校服的雀斑素颜自拍

**Author**: [Crystal](https://x.com/Cicily_aura)  **Date**: 2026-02-08  **Language**: en

> 一个结构化的提示，用于生成一张年轻女性（类似安娜·德·阿玛斯或比莉·艾利什）身穿校服/商务休闲装的逼真、抓拍的智能手机自拍照。提示重点关注具体的面部细节（明显的雀斑、俏皮的嘟嘴、翻白眼）、公园环境以及带有斑驳阴影的自然日光。

![身穿校服的雀斑素颜自拍](https://cms-assets.youmind.com/media/1770619678467_5odptg_HApxMTga4AAEQO2.jpg)
![身穿校服的雀斑素颜自拍](https://cms-assets.youmind.com/media/1770619678507_7jalv8_HApxMTgawAAtUrt.jpg)

```
{
  "image_prompt_data": {
    "subject": {
      "demographics": "Young woman, approximately late teens to early 20s",
      "facial_features": {
        "skin": "Fair complexion with prominent, natural freckles scattered across the nose and cheeks",
        "eyes": "Light-colored eyes looking upward in an exaggerated eye-roll",
        "mouth": "Lips puckered in a playful pout or 'duck face' expression",
        "hair": "Light brown/dirty blonde hair tied back, with loose strands framing the face (curtain bangs style)"
      },
      "pose": "Selfie perspective with arm extended, high-angle shot looking down at the subject"
    },
    "attire": {
      "style": "School uniform or formal business casual",
      "items": [
        "Black tailored blazer or suit jacket",
        "White button-down collared shirt (slightly unkempt)",
        "Loose black necktie",
        "Black skirt (partially visible)"
      ]
    },
    "action": {
      "primary": "Taking a selfie",
      "secondary": "Holding a clear plastic cup containing iced coffee with a straw in the left hand"
    },
    "environment": {
      "location": "Park promenade (resembling Central Park, NYC)",
      "foreground": "Paved asphalt path with cobblestone drainage edges",
      "midground": "Rows of green wooden park benches lining both sides of the path",
      "background": "Stone bridge with stairs, large green trees forming a canopy, crowd of people walking away in the distance",
      "lighting": "Bright natural daylight, dappled sunlight filtering through trees, distinct shadows cast on the ground"
    },
    "technical_specifications": {
      "quality": "4K Ultra HD",
      "resolution": "High resolution",
      "texture_quality": "Hyper-realistic skin texture showing pores and freckles, detailed fabric textures",
      "visual_style": "Candid smartphone photography, photorealistic",
      "lighting_style": "Natural outdoor lighting, sunny day"
    }
  }
}
```

[[Female Portrait]] [[Playful Expression]] [[Smartphone Selfie]] [[Park Setting]]

---

### 188. 病毒式日光浴曲线身材提示

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-02-08  **Language**: en

> 一个详细的 JSON 提示，旨在生成一张丰满女性在躺椅上日光浴的逼真图像。该提示着重于解剖细节（极其丰满的胸部，软组织自然下垂）、着装（极少遮盖的黑色细绳比基尼）、姿势（斜倚，遮挡眼睛）和光线（强烈、高对比度的直射阳光），以实现一种抓拍式的、生活化的美学效果。

![病毒式日光浴曲线身材提示](https://cms-assets.youmind.com/media/1770619734004_74tdt7_HApnXXdWsAAeDCY.jpg)

```
{
"subject": {
"description": "Young woman with a voluptuous, hourglass figure lying on a sun lounger.",
"hair": "Long, platinum blonde hair, wavy texture, cascading over the lounger mesh.",
"face": "Eyes closed or shielded, heavy eyelashes, tanned complexion, hand raised to forehead blocking the sun.",
"body_type": "Curvy, fit physique with extremely voluminous bust. High body fat distribution in chest area, maintaining exact heavy mass and fullness relative to the torso. Clear forward and outward projection despite reclining pose. Soft tissue naturally settling with gravity.",
"attire": {
"garment": "Black two-piece string bikini.",
"top": "Triangle cup style, fabric stretched, providing minimal coverage for large bust volume, deep cleavage prominent.",
"bottom": "High-cut black bikini bottoms, sitting high on the hips."
},
"skin": "Deep tan, smooth texture with realistic skin pores, slight sheen from sun or oil."
},
"pose": {
"type": "Reclining supine on a chaise lounge.",
"head": "Tilted slightly back, face angled towards the sky but shielded by hand.",
"arms": {
"left_arm": "Raised, elbow bent, hand placed partly over forehead/eyes to shield from sunlight.",
"right_arm": "Bent at elbow, hand resting gently on the lower abdomen/hip area, fingers relaxed."
},
"torso": " arched slightly, chest projected upward, ribcage expanded.",
"legs": "Extended downwards, upper thighs visible, resting on the lounger."
},
"environment": {
"location": "Outdoor patio or pool deck.",
"ground": "Light grey/white square tiled flooring.",
"background": "White horizontal slat fence/railing. Large white cylindrical concrete planter filled with dark grey stones and the base of a palm tree trunk directly behind the subject's head.",
"furniture": "Grey mesh chaise lounge with a curved silver metal frame."
},
"camera": {
"perspective": "High angle shot, looking down at the subject.",
"framing": "Medium shot capturing the subject from the top of the head to the upper thighs.",
"focal_length": "35mm to 50mm equivalent, no wide-angle distortion.",
"depth_of-field": "Sharp focus on the subject, slight fall-off in the background fence."
},
"lighting": {
"source": "Natural direct sunlight (high noon).",
"quality": "Hard, bright, high-contrast.",
"shadows": "Distinct, sharp shadow cast by the raised hand across the face. Shadow of the subject cast onto the mesh lounger. Highlights on the upper chest, shoulders, and legs."
},
"mood_and_expression": {
"mood": "Relaxed, sunbathing, luxurious, summery.",
"expression": "Serene, resting, eyes shielded."
},
"style_and_realism": {
"style": "Photorealistic, candid lifestyle photography.",
"fidelity": "High fidelity to textures (mesh, skin, concrete, plant bark).",
"details": "Visible texture of the grey mesh fabric, distinct ridges on the palm tree trunk, individual stones in the planter."
},
"colors_and_tone": {
"palette": "Neutral whites and greys in background, stark black swimsuit, gol
```

[[Female Portrait]] [[Bikini Photography]]

---

### 189. 斜倚的曼妙身姿卧室提示词

**Author**: [Jessia](https://x.com/itsjessiababy)  **Date**: 2026-02-08  **Language**: en

> 一个高度明确的 JSON 提示，着重于生成一张曲线玲珑的年轻女性斜倚在床上的超写实图像。该提示细致地描述了主体的解剖特征（强调受重力影响的丰满胸部）、着装（不匹配的比基尼/内衣）、姿势（斜倚在床头板上）、环境（凌乱的床单、粉色环境光）以及技术方面（高保真超写实主义、抓拍的社交媒体美学）。

![斜倚的曼妙身姿卧室提示词](https://cms-assets.youmind.com/media/1770619729912_p7b495_HApf11MbgAAgvEN.jpg)

```
{
"subject": "Young woman with long, layered dark brown hair and fair skin lying on a bed. She has a curvaceous figure with a very full, heavy natural bust that is significantly voluminous and clearly affected by gravity in the reclining position. She is wearing a mismatching bikini/lingerie set: a sparkly, textured red/dark pink triangle top with thin straps that barely contains the chest volume, and solid black thong-style bottoms. Her skin texture is natural with subtle variations, showing soft stomach contours and a visible navel. The bust projects forward and outward, maintaining significant mass relative to the ribcage.",
"pose": "Reclining pose on a bed, leaning back against a white headboard. Her body is angled slightly diagonally across the frame. Her right arm is raised, elbow bent, with her hand resting on the top edge of the headboard. Her head is tilted slightly to her right, facing the camera directly. Her torso is relaxed, allowing soft tissue to settle naturally. Her hips are slightly turned, and her legs extend towards the bottom right of the frame.",
"environment": "A bedroom interior. The subject is on a bed with messy white sheets and pillows. Behind her is a white, textured upholstered headboard. A crumpled dark grey or teal piece of clothing lies on the pillows behind her shoulder. To the right, a floor lamp with a gold stand and a pink shade stands against a white wall, casting a soft magenta/purple glow. A small white square device (possibly a thermostat or remote) sits on the mattress in the foreground.",
"camera": "Medium shot captured from a slightly elevated angle looking down at the bed. The framing captures the subject from the top of the head to the upper thighs. The perspective emphasizes the depth of the torso and the volume of the chest. Sharp focus on the subject's face and upper body.",
"lighting": "Soft, diffused interior lighting. The primary light source illuminates the subject from the front-left, creating gentle highlights on the skin and defining the curvature of the body. Secondary lighting comes from the lamp in the background, adding a pink/purple ambient hue to the right side of the image and the back wall. Shadows are soft and natural.",
"mood_and_expression": "Relaxed, intimate, and inviting. The subject has a gentle, pleasant smile and is making direct, engaging eye contact with the viewer. The atmosphere is casual and comfortable.",
"style_and_realism": "High-fidelity photorealism with a candid, social media aesthetic. The image retains natural skin texture, realistic body physics, and unpolished details like messy sheets, avoiding a hyper-processed or studio-artificial look.",
"colors_and_tone": "Natural skin tones contrasted with the bright white of the bedding and the pop of red/pink from the bikini top. The background features cool white walls warmed by the pink lamp light. The overall palette is soft with a mix of neutral whites
```

[[Female Portrait]] [[Social Media Aesthetic]] [[Hourglass Figure]] [[Intimate Photography]]

---

### 190. 粉色美学洛可可生日蛋糕编辑肖像

**Author**: [gauche](https://x.com/gaucheai)  **Date**: 2026-02-08  **Language**: en

> 生成一张女性化、带有娇媚美学风格的编辑肖像的提示，描绘一位年轻女性，拥有铂金色头发，手持一颗樱桃，坐在一块复古心形粉色生日蛋糕旁。提示中指定了柔和的漫射影室灯光和纯色柔和粉色背景。

![粉色美学洛可可生日蛋糕编辑肖像](https://cms-assets.youmind.com/media/1770619705966_3d85i6_HApetakW4AIHr-w.jpg)
![粉色美学洛可可生日蛋糕编辑肖像](https://cms-assets.youmind.com/media/1770619705980_hhbked_HApenPHa8AAAYsn.jpg)

```
{
  "prompt": "Pink aesthetic birthday cake editorial portrait, young woman with long platinum silver blonde wavy hair, holding red cherry to lips about to eat, looking to the side with soft sultry expression, light green blue eyes, natural makeup with red cherry lips, diamond crystal choker necklace, wearing pink strapless top, sitting at table with pink vintage heart-shaped cake decorated with pink frosting roses and red cherries on top, one slice cut out of cake, holding cake knife in other hand, solid {argument name="background color" default="pink pastel"} background, soft studio lighting, feminine coquette aesthetic, Valentine birthday party editorial style, romantic girly mood, 3:4",
  "negative_prompt": "outdoor, dark background, heavy dramatic makeup, casual clothing, harsh lighting, masculine aesthetic",
  "style": "feminine editorial photography, coquette aesthetic, pink birthday cake portrait, romantic girly style",
  "aspect_ratio": "3:4",
  "camera": {
    "type": "professional studio photography",
    "angle": "front facing, eye level, medium close-up",
    "framing": "upper body portrait with cake on table in foreground"
  },
  "lighting": {
    "type": "soft diffused studio lighting",
    "quality": "even flattering pink-toned light, soft shadows",
    "atmosphere": "dreamy feminine pink studio setup"
  },
  "mood": "romantic, feminine, playful, coquette, girly, sweet, flirty",
  "color_palette": "platinum silver blonde, pastel pink background, pink frosting, red cherries, silver diamond necklace, soft pink tones throughout",
  "subject_features": {
    "hair": "long platinum silver blonde, soft wavy texture, middle parted, flowing past shoulders",
    "skin": "fair, natural, soft glow",
    "eyes": "light green blue, looking to the side, natural lashes",
    "lips": "red cherry color, holding cherry to lips",
    "eyebrows": "natural, well groomed",
    "expression": "soft sultry, playful, about to eat cherry"
  },
  "makeup": {
    "style": "natural with red lip accent",
    "base": "natural flawless skin",
    "eyes": "subtle natural eye makeup, defined lashes",
    "lips": "red matching cherry color"
  },
  "accessories": {
    "necklace": "diamond crystal choker necklace with teardrop pendant, sparkly elegant"
  },
  "wardrobe": {
    "top": "pink strapless tube top or dress, matching pink aesthetic"
  },
  "props": {
    "cake": "vintage style heart-shaped pink cake with elaborate pink frosting roses and piping, decorated with red maraschino cherries on top, one slice cut and removed",
    "knife": "cake knife held in right hand on table",
    "cherry": "red cherry held to lips in left hand"
  },
  "pose": {
    "body": "sitting at table, leaning slightly forward",
    "left_hand": "holding cherry stem bringing cherry to lips",
    "right_hand": "holding cake knife on table",
    "gaze": "looking to the side, not at camera"
  },
  "setting": {
    "background": "solid pastel pink seamless b
```

[[Female Portrait]] [[Soft Studio Lighting]] [[Platinum Hair]]

---

### 191. 戴牛仔帽和靴子的原始时尚人像

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-02-08  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张超现实、未经修饰的编辑时尚肖像，描绘一名女性俯卧在摄影棚地板上。它指定了戏剧性的明暗对比照明、极致的纹理细节（可见毛孔、汗毛、皮革纹理），以及特定的相机设置（Sony A7R V, 85mm f/1.4 GM），以实现未经修饰、高保真的外观。

![戴牛仔帽和靴子的原始时尚人像](https://cms-assets.youmind.com/media/1770619672282_0038up_HAot8Dna8AA4Gqk.jpg)
![戴牛仔帽和靴子的原始时尚人像](https://cms-assets.youmind.com/media/1770619672304_b9bt6s_HAot8DHXMAAZJYp.jpg)
![戴牛仔帽和靴子的原始时尚人像](https://cms-assets.youmind.com/media/1770619672277_tuayha_HAot8DiaUAAQs6j.jpg)

```
{
  "image_analysis": {
    "subject": {
      "type": "Young woman",
      "hair": "Long, straight, light brown/brunette, draped over shoulders, individual strands visible",
      "expression": "Calm, confident, slightly sultry gaze",
      "gaze": "Directly at the camera",
      "makeup": "Subtle, winged eyeliner visible, natural skin finish without smoothing"
    },
    "attire": {
      "headwear": "Large structured beige/tan felt cowboy hat with a distinct crown divot and wide brim, visible felt fibers",
      "clothing": "Sleeveless brown/bronze bodysuit or tight-fitting top, showing fabric weave",
      "footwear": "Dark brown leather cowboy boots with western stitching/embroidery; sole of the left boot is prominently visible showing scuffs and wear",
      "accessories": "Thin delicate chain necklace, thin gold bracelet on the left wrist"
    },
    "pose_and_action": {
      "posture": "Lying prone (on stomach) on the floor",
      "legs": "Bent upward at the knees, feet raised in the air behind her",
      "arms": "Left arm propped up, hand formed into a loose fist resting under the chin/cheek to support the head",
      "composition": "Front-facing, eye-level angle"
    },
    "setting_and_lighting": {
      "background": "Seamless, solid neutral beige/taupe studio backdrop",
      "lighting_style": "Dramatic studio lighting (Chiaroscuro), directional soft light from the left",
      "shadows": "Deep shadow cast over the upper face/eyes by the hat brim; soft shadows on the floor beneath the body",
      "color_palette": "Warm earth tones, beige, brown, bronze, tan",
      "kelvin_temp": "5500K (Daylight balanced)"
    },
    "technical_specs": {
      "camera": "Sony A7R V",
      "lens": "85mm f/1.4 GM",
      "settings": "ISO 100, f/2.8, 1/125s shutter speed",
      "file_format": "RAW (ARW), uncompressed",
      "quality": "8K High Fidelity",
      "style": "Photorealistic, Editorial Fashion Photography, Raw Candid",
      "texture_details": "Hyper-realistic skin texture, visible pores, vellus hair (peach fuzz), natural skin imperfections, mole/freckle details, tactile fabric textures, leather grain, dust motes in light",
      "focus": "Sharp focus on the eyes and face, creamy bokeh falloff in background",
      "post_processing": "Zero smoothing, natural color grading, slight film grain"
    }
  },
  "generative_prompt": "A hyper-realistic, raw studio portrait of a young woman lying on her stomach, shot on a Sony A7R V with an 85mm f/1.4 lens. She wears a large beige felt cowboy hat casting a dramatic shadow over her eyes, a sleeveless bronze bodysuit, and worn brown leather cowboy boots. Her legs are bent, feet kicked up, showing scuffed soles. She rests her chin on her fist, gazing confidently. Lighting is dramatic Chiaroscuro with deep shadows. 8K resolution, uncompressed RAW style. Extremely detailed skin texture with visible pores, micro-hairs, and natural imperfections; no skin smoothing. Hig"
```

[[Female Portrait]] [[Chiaroscuro Lighting]] [[Cowboy Hat]] [[Floor Pose]]

---

### 192. 都市街头服饰发型肖像提示

**Author**: [Sudee🥀](https://x.com/NameIsSudee)  **Date**: 2026-02-08  **Language**: en

> 一个为 Gemini Nano Banana Pro 模型设计的详细 JSON 提示，重点在于生成一张年轻女性的超逼真肖像，她留着一种特定的新发型（深勃艮第色头发，带有修饰脸型的辫子），置身于都市环境中。该提示详细说明了服装（渔网露脐上衣、工装裤）、姿势（手触碰头发）、光线（强烈阳光）和街头服饰美学。

![都市街头服饰发型肖像提示](https://cms-assets.youmind.com/media/1770619725863_i0a5id_HAotxLLakAA4Jb0.jpg)

```
{
  "prompt": {
    "subject": {
      "description": "Young woman  long, dark burgundy hair",
      "hair_style": "Straight with two small braided strands framing the face",
      "expression": "Looking down, contemplative, soft pout"
    },
    "outfit": {
      "top_layer": "White open-weave fishnet mesh long-sleeve crop top (shrug style)",
      "base_layer": "White fitted tank top with a scoop neckline",
      "bottoms": "Light beige loose-fitting cargo pants or joggers",
      "accessories": [
        "Small white shoulder bag with silver hardware",
        "Small hoop earrings"
      ]
    },
    "pose": {
      "action": "Both hands raised touching hair near temples",
      "posture": "Standing straight, facing forward, relaxed torso"
    },
    "setting": {
      "location": "Outdoor urban environment",
      "background": "Modern building with gray rectangular tiles and a large beige architectural pillar/archway",
      "sky": "Clear, bright blue sky"
    },
    "lighting": {
      "type": "Natural hard sunlight",
      "shadows": "Distinct shadows cast by the subject and building architecture",
      "time_of_day": "Mid-day"
    },
    "style": {
      "aesthetic": "Streetwear, summer fashion, casual chic",
      "quality": "High resolution, photorealistic, sharp focus"
    "aspect_ratio":"5:6"
    }
  }
}
```

[[Female Portrait]] [[Street Fashion]] [[Strong Sunlight]]

---

### 193. 复古魅力钢琴系列提示

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-02-08  **Language**: en

> 这是一个为 Nano Banana Pro 模型设计的结构化 JSON 提示，用于生成一系列四格图像。图像内容为一位年轻女性，身处复古、迷人的场景中，并带有一架复古钢琴。该提示详细说明了每一帧的特定服装、环境、灯光和独特姿势，强调高对比度、超现实的复古美学。

![复古魅力钢琴系列提示](https://cms-assets.youmind.com/media/1770619725504_qzlnds_HAncN4Db0AA3dYI.jpg)
![复古魅力钢琴系列提示](https://cms-assets.youmind.com/media/1770619725526_48hk0w_HAoO8-ZWsAAdLCj.jpg)

```
{
  "project_title": "Vintage Glamour Piano Series",
  "common_elements": {
    "subject": "Young woman with dark hair, straight bangs, and red lipstick.",
    "outfit": "Sheer, dusty red halter-neck bodysuit covered in large iridescent crystals and sequins, with a fringed skirt layer.",
    "environment": "Ornate vintage hotel room with pink damask wallpaper, heavy maroon curtains, patterned beige carpet, and a retro green upright piano.",
    "lighting_and_style": "Direct flash photography, high contrast, vintage aesthetic, fisheye or wide-angle lens distortion, saturated colors, 4k resolution, hyper-realistic textures."
  },
  "frames": [
    {
      "frame_id": 1,
      "position": "Top Left",
      "visual_prompt": "Low-angle fisheye shot. The subject is perched on top of a green upright piano, leaning back with knees bent. One leg is extended dramatically toward the camera lens, making the foot appear larger than life. She wears red fishnet socks and red strappy heels with crystal details. The focus is sharp on the texture of the fishnet and shoe in the foreground, blurring slightly toward her face.",
      "pose_details": "Sitting on piano, leg extended, looking away casually."
    },
    {
      "frame_id": 2,
      "position": "Top Right",
      "visual_prompt": "High-angle wide shot looking down at the subject seated at the green piano. She is looking up at the camera with a soft expression. Her right hand rests on the piano keys, fingers spread, showcasing a large ring. The wide-angle lens elongates her arm and hand. The background shows an unmade bed with gold satin sheets and a vintage lamp.",
      "pose_details": "Seated at keys, hand on piano, head tilted up."
    },
    {
      "frame_id": 3,
      "position": "Bottom Left",
      "visual_prompt": "Dynamic medium shot. The subject stands with her back to the camera, turning her head to look over her left shoulder. Her left arm is raised toward the camera, creating a motion-blurred foreground element. The side profile of the bodysuit reveals a backless design and hanging crystal fringe. The lighting highlights the sparkle of the gems and the curve of her shoulder.",
      "pose_details": "Standing/turning away, looking back, arm in motion."
    },
    {
      "frame_id": 4,
      "position": "Bottom Right",
      "visual_prompt": "Close-up extreme wide-angle shot, similar to a 0.5x selfie. The subject leans forward into the lens, distorting the perspective so her head appears larger. She looks directly at the viewer with a piercing gaze. The intricate detailing of the crystal bodice is highly visible. The green piano keys are visible in the lower right corner.",
      "pose_details": "Leaning forward, direct eye contact, close-up."
    }
  ]
}
```

[[Female Portrait]] [[High Contrast Photography]] [[Retro Aesthetic]] [[Four Panel Grid]]

---

### 194. 奢华室内内衣拍摄，展现夸张身材

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-02-08  **Language**: en

> 生成一张超现实、全身女性照片的详细提示，照片中女性身穿粉色蕾丝内衣，突出夸张的沙漏型身材（极细的腰部，丰满的胸部）。场景设定在豪华的室内起居空间，环境光线温暖呈金色，重点表现沙发上的纹理和姿态。

![奢华室内内衣拍摄，展现夸张身材](https://cms-assets.youmind.com/media/1770619707817_6h5614_HAoKIlMagAAs74g.jpg)
![奢华室内内衣拍摄，展现夸张身材](https://cms-assets.youmind.com/media/1770619707829_8np1v9_HAoKIeYb0AAvGT4.jpg)

```
{
  “ar”: “4:5”,
  “subject”: {
    “type”: “adult woman”,
    “age”: “early 20s”,
    “character_outline”: “Strikingly attractive woman with an exaggerated, sexy hourglass physique; features a very slim, cinched waist contrasting sharply with wide, voluptuous hips and a significantly fuller, large bust (appearing as size 90 bra size); long dark brown hair with distinct blunt bangs framing the face”,
    “expression”: “Sultry, direct gaze looking at the camera with slightly parted lips”,
    “gaze”: “Fixed directly on the camera lens”,
    “details”: “Clear skin completely free of any tattoos on arms or body; natural, alluring makeup”
  },
  “wardrobe”: {
    “lingerie”: “{argument name="lingerie color" default="Light pink/pale white"} lace bra (filled by large bust) and matching lace thong set”,
“hosiery”: “Sheer nude thigh-high stockings with a wide lace top band”,
    “accessories”: “Simple rings on fingers”
  },
  “pose_action”: {
    “shot_type”: “Full-body photograph, seated on a couch, capturing the exact pose from the reference”,
    “stance": “Sitting sideways on the beige fabric sofa; left leg is tucked back with the knee resting on the couch cushions; right leg is extended prominently forward over the edge of the couch towards the camera, with the arched bare foot clearly visible pointing down towards the marble floor; torso is twisted to face the camera, left arm resting elegantly on the back of the couch, right hand resting on her thigh near the hip”
  },
  “scene”: {
    “location”: “Luxurious indoor living space in the evening”,
    “foreground”: “Beige textured fabric sofa section; white marble floor tiles with grey veining visible beneath the extended foot”,
“background”: “Cream-colored wall with decorative molding panels; a warm-toned wall lamp is lit above and behind the subject, casting a soft glow”,
    “atmosphere”: “Intimate, warm, quiet, and luxurious evening ambiance”
  },
  “lighting”: {
    “type”: “Warm indoor ambient light”,
    “look”: “Soft, golden glow originating from the lamp behind the subject, creating gentle highlights on her hair, shoulders, and the curves of her hourglass figure, with soft, defining shadows”
  },
  “camera”: {
    “device_vibe”: “High-end digital photograph”,
    “focus": “Sharp focus on the subject’s face, body contours, and the texture of the lace and stockings”,
    “style”: “Ultra-realistic, natural colors, highly detailed capture of skin texture, fabric weave, and lighting nuances”
  }
}
```

[[Female Portrait]] [[Hourglass Figure]]

---

### 195. 被禁用的图片提示词：女性仰视视角

**Author**: [秦淮孤月 (蓝V互关）](https://x.com/qhgy)  **Date**: 2026-02-08  **Language**: zh

> 一位用户分享了一个详细的图像提示，其中指定了低角度仰视视角、构图（近大远小）、人物姿势（慵懒地斜靠着，双腿交叉）、服装（黑色丝袜，红底高跟鞋）和表情（手托着脸，厌恶的表情，头部略微倾斜看向镜头），并指出此特定提示现已禁用。

![被禁用的图片提示词：女性仰视视角](https://cms-assets.youmind.com/media/1770619738350_hjftbm_HAoHZDVasAAX22Z.jpg)

```
腿部向上拍呈仰视，用近大远小构图；人物慵懒靠扶手、翘二郎腿，穿{argument name="服装" default="黑丝+红底高跟鞋"}；一手撑脸，表情嫌弃，头微倾看镜头
```

[[Female Portrait]]

---

### 196. 一位身穿黑色皮夹克和牛仔裤的女性模特坐在公园草地上，超高清 4K 肖像。

**Author**: [Minhaa](https://x.com/tabu_8114)  **Date**: 2026-02-08  **Language**: en

> 这是一个高度结构化的图像生成提示，专为 Gemini Nano Banana Pro 设计，详细说明了主体身份、外貌、着装（黑色皮夹克、浅蓝色牛仔裤）、姿势（斜倚坐在草地上）、场景细节（公园、秋叶）以及摄影技术参数（4K 超高清、9:16 宽高比、纹理锐利对焦）。

![一位身穿黑色皮夹克和牛仔裤的女性模特坐在公园草地上，超高清 4K 肖像。](https://cms-assets.youmind.com/media/1770619711780_jdfva8_HAn39iba4AAXCZh.jpg)
![一位身穿黑色皮夹克和牛仔裤的女性模特坐在公园草地上，超高清 4K 肖像。](https://cms-assets.youmind.com/media/1770619711822_rvbw37_HAn39kyb0AAAklv.jpg)
![一位身穿黑色皮夹克和牛仔裤的女性模特坐在公园草地上，超高清 4K 肖像。](https://cms-assets.youmind.com/media/1770619711783_rnj869_HAn39gsacAArRGo.jpg)

```
{
  "image_generation_request": {
    "content": {
      "subject_details": {
        "identity": {
          "name": "{argument name="model name" default="England model"}",
          "gender": "female"
        },
        "appearance": {
          "hair": {
            "color": "dark brown",
            "texture": "straight",
            "length": "long"
          },
          "expression": "smiling gently",
          "makeup": {
            "style": "light",
            "lip_color": "rosy"
          }
        },
        "action_and_pose": {
          "posture": "reclined sitting",
          "placement": "on grass",
          "gaze": "direct at camera",
          "arm_position": "hands behind back supporting body"
        },
        "attire": {
          "outerwear": {
            "item": "cropped jacket",
            "material": "leather",
            "color": "black",
            "state": "buttoned open"
          },
          "upper_body": {
            "item": "form-fitting top",
            "color": "black",
            "layer": "under jacket"
          },
          "lower_body": {
            "item": "jeans",
            "material": "denim",
            "wash": "light blue",
            "fit": "high-waisted"
          }
        }
      },
      "scene_details": {
        "environment": {
          "type": "park",
          "ground_surface": "green grass",
          "ground_elements": [
            "scattered dry autumn leaves"
          ]
        },
        "background_elements": [
          "lush green trees",
          "tall hedge on the left",
          "black metal fence",
          "gravel path in the distance"
        ],
        "lighting_conditions": {
          "source": "natural daylight",
          "quality": [
            "bright",
            "clear"
          ]
        }
      }
    },
    "execution_parameters": {
      "photography_style": {
        "shot_type": "photograph",
        "aesthetic": [
          "clean",
          "natural",
          "detailed"
        ],
        "composition": {
          "camera_angle": "eye-level",
          "framing": "well-structured"
        },
        "focus_and_texture": {
          "focus": "sharp",
          "priority_textures": [
            "hair",
            "leather",
            "denim",
            "grass"
          ]
        }
      },
      "technical_specs": {
        "resolution": "4K Ultra HD",
        "aspect_ratio": "9:16"
      }
    }
  }
}
```

[[Female Portrait]]

---

### 197. 亚洲女性 ATV 沙滩比基尼提示

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-02-08  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张亚洲女性的超逼真图像，她拥有独特的沙漏型身材和傲人曲线，在阳光明媚的海滩上骑着沙滩车摆姿势。该提示详细说明了光泽、油亮的皮肤质感，独特的比基尼细节（数字“9”和动漫图案），以及技术性灯光（混合了自然阳光和直射闪光），以营造出自信、迷人的夏日氛围。

![亚洲女性 ATV 沙滩比基尼提示](https://cms-assets.youmind.com/media/1770619734089_8i4ygu_HAn3YhOXEAAiTCm.jpg)

```
{
"subject": {
"description": "Young Asian woman with a fit, hourglass physique and prominent curves.",
"hair": "Long, straight jet-black hair styled with small accent braids framed by gold hair rings/cuffs. Hair falls past shoulders.",
"skin": "Tan, sun-kissed skin tone with a highly glossy, oily, or wet texture, exhibiting strong specular highlights on the chest, stomach, and shoulders. Realistic skin texture with visible pores and natural imperfections.",
"apparel": {
"bikini_top": "Black triangle bikini top. The wearer's right cup features a large white number '9' in a sporty font. The wearer's left cup features a colorful pink and blue anime/cartoon girl graphic.",
"bikini_bottom": "Matching black string bikini bottoms featuring the colorful anime graphic and the word 'SUPER' on the waistband strap.",
"accessories": "Thin gold necklace, multiple bracelets on both wrists including a dark beaded bracelet on the left wrist, gold rings."
},
"anatomy_constraints": "Bust volume must appear full and heavy with natural gravity. Clear forward projection. Waist is slim, hips are wide. Distinct collarbones and abdominal definition visible under the glossy skin texture."
},
"pose": {
"description": "Standing medium shot, leaning casually back against the front bumper/grill of a black ATV. Body is facing forward.",
"arms": "Both arms are extended slightly outwards and down, with hands resting on the metal bars of the ATV's front bumper.",
"head": "Head tilted slightly to the side, chin down, facing the camera directly.",
"spine_and_hips": "Spine slightly arched, hips shifted slightly to the right, creating a natural curve.",
"gaze": "Direct, intense eye contact with a sultry expression."
},
"environment": {
"location": "Sunny sandy beach during the day.",
"background_elements": "A large black UTV/ATV (all-terrain vehicle) directly behind the subject, serving as a prop. The vehicle has a roll cage, headlights, and aggressive tire treads visible on the left. Behind the vehicle is a sandy beach leading to a calm blue ocean and a horizon line with a clear blue sky and faint clouds."
},
"camera": {
"shot_type": "Medium shot (mid-thigh up).",
"perspective": "Eye-level or slightly low angle, emphasizing the subject's stature.",
"lens_characteristics": "Sharp focus on the subject, slight depth of field blurring the distant ocean horizon but keeping the ATV relatively sharp.",
"framing": "Centered composition."
},
"lighting": {
"type": "Mixed lighting: Strong natural sunlight combined with direct flash photography.",
"characteristics": "Hard lighting typical of outdoor flash photography. Bright specular highlights on the oily skin (forehead, chest, stomach). Sharp shadows cast by the hair and bikini strings. The flash illuminates the subject evenly against the slightly darker/bluer background sky.",
"direction": "Frontal flash, overhead sunlight."
},
"mood_and_expression": {
"mood": "Confident, glamorous, summer vibe."
```

[[Female Portrait]] [[Hourglass Figure]]

---

### 198. 一位身着蓝宝石色露背吊带裙的女性，在巴黎的屋顶上，呈现出超现实的电影感肖像。

**Author**: [Javeriya 🇺🇸](https://x.com/JadoonKhan281)  **Date**: 2026-02-08  **Language**: en

> 一个详细的提示，用于创作一张超现实电影风格的女性垂直肖像（9:16），很可能是波琳娜·加加林娜（Polina Gagarina），从背面视角拍摄于巴黎的屋顶。重点突出奢华的午夜蓝宝石色丝缎露背吊带礼服、她的姿态（回眸望向身后）、空灵的月光，以及背景中散发着焦外虚化光芒的埃菲尔铁塔。

![一位身着蓝宝石色露背吊带裙的女性，在巴黎的屋顶上，呈现出超现实的电影感肖像。](https://cms-assets.youmind.com/media/1770619719892_wm6e3e_HAnhWY4bkAApHt3.jpg)
![一位身着蓝宝石色露背吊带裙的女性，在巴黎的屋顶上，呈现出超现实的电影感肖像。](https://cms-assets.youmind.com/media/1770619719980_b68fdm_HAnhWIwbMAARME8.jpg)
![一位身着蓝宝石色露背吊带裙的女性，在巴黎的屋顶上，呈现出超现实的电影感肖像。](https://cms-assets.youmind.com/media/1770619720076_ectw74_HAnhWceaEAAPPK4.jpg)

```
[
  {
    "subject": "The same young woman from the previous images, featuring identical facial features and long voluminous blonde waves with soft tendrils",
    "pose": "captured from a rear-view perspective, standing at the ornate wrought-iron balcony, torso turned gracefully to look back over her shoulder directly at the camera, one hand resting lightly on the railing, highlighting the elegant curve of her back",
    "clothing": {
      "dress": "opulent {argument name="dress color" default="midnight sapphire blue"} silk-satin slip gown, featuring a dramatic ultra-deep draped cowl back that cascades in fluid gathered layers down to the waist, whisper-thin spaghetti straps with one delicately slipping down her arm, bias-cut silhouette hugging the lower back and hips"
    },
    "accessories": {
      "earrings": "elongated sapphire chandelier drops visible as she turns her head",
      "bracelet": "thin gold chain on the wrist resting on the railing",
      "rings": "stacked diamond eternity bands"
    },
    "makeup": "consistent porcelain-dewy skin, soft smoky indigo eyeshadow wing visible in profile, and high-shine berry lip gloss",
    "lighting": "ethereal moonlight striking her shoulders and the silk folds of the cowl back, warm amber glow from candles on the floor creating a soft rim light, cinematic volumetric light rays",
    "setting": "luxurious moonlit Parisian rooftop terrace, the {argument name="landmark" default="Eiffel Tower"} glowing in the soft-focus bokeh background, marble floor scattered with white rose petals",
    "photography_style": "hyper-realistic cinematic vertical portrait 9:16 aspect ratio, focusing on the texture of the satin and the soft glow of skin, 8K photorealistic editorial quality",
    "composition": "medium-full shot from behind, slightly angled to showcase the deep back design of the dress and her over-the-shoulder gaze"
  }
]
```

[[Female Portrait]] [[Cinematic Photography]] [[Backless Dress]]

---

### 199. 游艇上的生活方式肖像，身着荧光绿针织衫

**Author**: [ShaHid WaNii](https://x.com/meng_dagg695)  **Date**: 2026-02-08  **Language**: en

> 一个结构化提示，用于生成一张户外生活方式肖像：一名女性站在游艇上，身穿霓虹酸橙绿钩针编织套装，背景是现代城市天际线。提示详细描述了姿势、服装质感和自然阳光效果。

![游艇上的生活方式肖像，身着荧光绿针织衫](https://cms-assets.youmind.com/media/1770619707943_2nd471_HAnesFlaEAAEEJU.jpg)
![游艇上的生活方式肖像，身着荧光绿针织衫](https://cms-assets.youmind.com/media/1770619707843_3id29c_HAnesDzbcAAF5w-.jpg)
![游艇上的生活方式肖像，身着荧光绿针织衫](https://cms-assets.youmind.com/media/1770619707855_u393i7_HAnesIda8AAkX1T.jpg)

```
{
  "image_overview": {
    "scene_type": "Outdoor lifestyle portrait",
    "setting": "On a yacht over open water with a modern city skyline in the background",
    "time_of_day": "Daytime (natural sunlight)",
    "camera_orientation": "Vertical",
    "aspect_ratio": "3:4"
  },
  "subject": {
    "count": 1,
    "gender_presentation": "Female-presenting",
    "pose": {
      "body_position": "Standing, body slightly angled",
      "support": "Leaning with right hand resting on yacht railing",
      "left_hand": "Raised to hair, fingers touching side of head",
      "legs": "Close together, weight shifted to one side"
    },
    "expression": {
      "mouth": "Soft smile",
      "head_direction": "Turned slightly to the left",
      "gaze": "Looking away from camera"
    }
  },
  "appearance": {
    "hair": {
      "color": "Black",
      "length": "Medium to long",
      "texture": "Wavy",
      "styling": "Loose, wind-swept"
    },
    "skin_tone": "Medium",
    "face_details": {
      "makeup_visibility": "Minimal, natural-looking",
      "visible_features": "Smooth skin, defined jawline"
    }
  },
  "clothing": {
    "outfit_type": "Two-piece knit set",
    "top": {
      "color": "{argument name="outfit color" default="Neon lime green"}",
      "material": "Crochet knit",
      "pattern": "Repeating lace-like geometric pattern",
      "sleeves": "Long sleeves",
      "fit": "Relaxed fit",
      "neckline": "Round neckline"
    },
    "skirt": {
      "color": "Neon lime green",
      "material": "Crochet knit",
      "pattern": "Matching lace-like knit pattern",
      "length": "Mid-calf length",
      "opacity": "Semi-sheer with visible knit texture"
    },
    "footwear": {
      "type": "Heels",
      "color": "Black",
      "style": "Closed-toe"
    }
  },
  "accessories": {
    "sunglasses": {
      "color": "Black",
      "style": "Rectangular",
      "lens": "Dark tinted"
    },
    "earrings": {
      "type": "Stud or small drop earrings",
      "color": "Gold with pearl-like detail"
    }
  },
  "environment": {
    "foreground": {
      "surface": "Yacht deck with wooden planks",
      "railing": {
        "material": "Metal",
        "finish": "Polished stainless steel",
        "design": "Horizontal bars with curved supports"
      }
    },
    "midground": {
      "water": {
        "type": "Sea or large body of water",
        "color": "Deep blue",
        "texture": "Small visible ripples"
      }
    },
    "background": {
      "cityscape": {
        "buildings": "Tall modern skyscrapers",
        "architecture_style": "Contemporary glass and steel towers",
        "distance": "Far background",
        "focus": "Slightly soft compared to subject"
      },
      "sky": {
        "color": "Clear pale blue",
        "clouds": "No visible clouds"
      }
    }
  },
  "lighting": {
    "type": "Natural sunlight",
    "direction": "From the right side of the frame",
    "effects": {
      "highlights": "Visible on fa
```

[[Female Portrait]] [[Natural Sunlight]] [[City Skyline Background]]

---

### 200. 超逼真黄金时段镜面自拍提示词

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-02-08  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超现实的年轻女性在金色时段舒适卧室里拍摄的镜面自拍照，突出花卉挂毯紧身胸衣上衣和及膝麂皮靴等特定复古时尚单品，并带有戏剧性的暖光效果。

![超逼真黄金时段镜面自拍提示词](https://cms-assets.youmind.com/media/1770619670859_n5hxlv_HAnVq62XkAAWJJN.jpg)
![超逼真黄金时段镜面自拍提示词](https://cms-assets.youmind.com/media/1770619670937_kxguic_HAnVq7UaoAACPjy.jpg)

```
{
  "image_analysis": {
    "subject_details": {
      "demographics": "Young woman, light skin tone",
      "hair": "Long, dark brunette, wavy texture, voluminous, highlighted by strong sunlight",
      "face": "Soft makeup, rosy blush, winged eyeliner, neutral to slight smile expression, looking into the mirror (phone screen)"
    },
    "apparel_details": {
      "top": "Strapless corset-style top with a vintage floral tapestry print in muted yellow, green, and red tones",
      "bottoms": "Light wash blue denim shorts with frayed hems",
      "footwear": "Knee-high brown suede boots with fringe details (moccasin/boho style), prominence in the foreground"
    },
    "accessories_details": {
      "phone_case": "Cow print pattern (black and white patches)",
      "jewelry": "Small silver hoop earrings",
      "tech": "iPhone (triple lens camera configuration)"
    },
    "scene_details": {
      "setting": "Cozy bedroom interior",
      "background_elements": [
        "Unmade bed with cream-colored bedding",
        "Chunky knit beige throw blanket",
        "White plush stuffed animal (bear) in the upper right corner",
        "Minimalist wall art featuring a black arrow and reversed text '1831 MI'"
      ],
      "flooring": "Light beige textured carpet"
    },
    "lighting_and_atmosphere": {
      "type": "Natural sunlight, Golden Hour",
      "quality": "High contrast, warm directional light streaming from the left, creating bright highlights on hair and legs and deep shadows",
      "vibe": "Aesthetic, cozy, casual, Pinterest-style, warm, intimate"
    }
  },
  "technical_specifications": {
    "quality": "4k HD, 8k resolution, highly detailed",
    "style": "Photorealistic, Mirror Selfie, Lifestyle photography",
    "visual_fidelity": "Sharp focus on subject, detailed textures (suede, hair strands, fabric weave), accurate lighting physics"
  },
  "master_prompt": "A hyper-realistic 4k HD mirror selfie of a young woman sitting on a beige carpeted bedroom floor during golden hour. She has long, voluminous wavy dark brown hair illuminated by intense, warm sunlight coming from the left. She is wearing a vintage strapless floral tapestry corset top, light blue denim cut-off shorts, and distinctive knee-high brown suede boots with fringe detailing. One leg is extended towards the camera, emphasizing the texture of the suede boots. She holds a smartphone with a cow-print case, taking the photo in a large mirror. The background is a cozy, slightly messy bed with a chunky knit cream blanket, a white stuffed bear prop, and minimalist wall art with an arrow. The lighting is dramatic and warm, creating a soft, aesthetic sun-kissed glow."
}
```

[[Female Portrait]] [[Cozy Bedroom Setting]]

---

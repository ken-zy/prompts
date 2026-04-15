# Chunk 009

Total: 200 prompts

### 1. 时尚杂志文章全文

**Author**: [fofr](https://x.com/fofrAI)  **Date**: 2025-11-20  **Language**: en

> 生成一张光面杂志文章平铺在桌上的照片，其中包含所有提供的文本，并带有精心设计的排版、照片和引文。

![时尚杂志文章全文](https://cms-assets.youmind.com/media/1763887054878_tg7sxg_G6NXhzHWUAAL6HP.jpg)
![时尚杂志文章全文](https://cms-assets.youmind.com/media/1763887057441_xspa3g_G6NXqKsWAAAPRpy.jpg)
![时尚杂志文章全文](https://cms-assets.youmind.com/media/1763887060611_v5mhxw_G6NWMceXMAA4Yn8.jpg)

```
Put this whole text, verbatim, into a photo of a glossy magazine article on a desk, with photos, beautiful typography design, pull quotes and brave formatting. The text: {argument name="article_text" default="[...the unformatted article]"}
```

[[Editorial Photography]] [[Print Design]] [[Typography Layout]]

---

### 2. 编辑角度参考表

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-02-07  **Language**: en

> 一个针对 Google Nano Banana Pro 在 Gemini 上生成 3x3 图像网格（4:5 宽高比）的高度具体提示，要求在九个不同的编辑角度（例如，侧面、低角度、荷兰倾斜）展示一个单一主体。它强制要求所有面板中的面部 100% 一致性，并需要附带一张自拍照作为身份参考，重点是高端时尚摄影风格。

![编辑角度参考表](https://cms-assets.youmind.com/media/1770532819165_3kp3jk_HAiGoHJbEAABLoE.jpg)

```
High-resolution Editorial Angle Reference Sheet. Perfect 3x3 grid. Aspect ratio 4:5. Strictly use attached selfie as identity reference. Maintain 100% facial consistency across all 9 panels (same face, age, hair, skin tone, proportions). Wardrobe (fixed for all panels): Oversized red suit jacket and trousers, white dress shirt, black necktie. Clean editorial oversized fit. Background: neutral light-grey studio cyclorama. Lighting: soft professional studio lighting with subtle fill. Camera: 85mm portrait look, shallow depth of field, sharp focus on face and outfit. Composition: centered subject in every cell, consistent framing, balanced spacing. Grid labels: clean white sans-serif text at bottom center of each cell showing the angle. Row 1 (Top): 1. Front Medium — front-facing waist-up, direct gaze. 2. Close-Up — extreme close-up on face and eyes. 3. Three-Quarter — 3/4 turn of torso and face. Row 2 (Middle): 4. Profile — exact side profile. 5. Low Angle Full — full body from slightly below. 6. High Angle — camera slightly above. Row 3 (Bottom): 7. Over Shoulder — over-the-shoulder look back. 8. Dutch Tilt — slight camera tilt. 9. Mid Walk — natural mid-step candid pose. Style: editorial fashion photography, cinematic, high-end. Render quality: ultra photorealistic, sharp text, visible fabric texture, natural skin, consistent lighting. Negative prompts: identity change, distorted anatomy, extra limbs, inconsistent clothing, busy background
```

[[Face Consistency]] [[High Fashion Photography]]

---

### 3. Nano Banana 提示：角色跳投动作保持一致

**Author**: [路飞 🏴‍☠️ AI 研究员🧐](https://x.com/0xluffy_eth)  **Date**: 2026-02-07  **Language**: zh

> 使用 Nano Banana 保持多镜头（跳切）中面部和服装一致性的说明，通过上传面部和场景（如楼梯镜头）的源图像。这是一个作为提示的工作流程说明。

![Nano Banana 提示：角色跳投动作保持一致](https://cms-assets.youmind.com/media/1770532842179_z5xkq4_HAhuG3lacAIZNhE.jpg)

```
为保持脸部和服装一致，可用 Nano Banana 制作额外的跳切。

上传脸部的源图像，和楼梯镜头：
```

[[Face Consistency]]

---

### 4. 发型照片拼贴提示

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成高质量照片拼贴的提示，拼贴中是同一个人，在多个相框中保持一致的面部特征和表情，每个相框展示不同的发型（例如，精灵短发、编发皇冠、凌乱发髻）。它指定了 4x3 的网格布局和编辑级美妆造型。

![发型照片拼贴提示](https://cms-assets.youmind.com/media/1769236057568_mwc36t_G_YjnB2W0AA8KiL.jpg)

```
A high-quality photo collage featuring the same person with identical facial features and expression, shown in multiple frames with different hairstyles. Each panel displays a unique hairstyle such as {argument name="hairstyle 1" default="long straight hair"}, {argument name="hairstyle 2" default="high ponytail"}, {argument name="hairstyle 3" default="messy bun"}, pixie cut, braided crown, soft waves, short bob with bangs, low bun, side braid, and loose curls. Consistent neutral outfit and makeup across all images, soft studio lighting, warm blurred background, realistic skin texture, symmetrical face consistency, ultra-detailed, editorial beauty look, 4x3 grid layout, professional portrait photograph
```

[[Face Consistency]]

---

### 5. 仰视视角电影感肖像提示词，带身份锁定

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个为 Nano Banana Pro 设计的结构化 JSON 提示，用于生成一张高端、电影级的超写实肖像，采用超低角度（虫眼视角）。该提示明确要求使用参考图像来确保面部一致性，并详细说明了室内环境、暖钨丝灯照明和柯达 Portra 400 胶片美学。

![仰视视角电影感肖像提示词，带身份锁定](https://cms-assets.youmind.com/media/1769235977739_ewdmts_G_VkiQ4aAAAUcAF.jpg)

```
{ "prompt\_type": "photorealistic\_portrait", "subject": { "name": "person in the reference image", "identity\_rules": "use the exact same person and facial identity from the reference image, preserve facial structure and proportions, no face swap, no identity change", "appearance": "authentic detailed facial features matching the reference image, soft skin texture, slight smile, looking upwards away from camera, relaxed expression", "hair": "messy high bun, blonde highlights, loose wispy strands framing the face, casual updo" }, "attire": { "clothing": "{argument name="clothing color" default="dark burgundy"} ribbed knit long-sleeve top, tight fit, crew neck, casual style", "accessories": "none visible" }, "props": { "main\_prop": "none", "details": "no visible weapons, no sword visible in frame, clean foreground, no objects obstructing the subject" }, "environment": { "setting": "indoor interior with vintage aesthetics", "background": "dark wooden coffered ceiling, architectural beams, antique style brass chandelier with glowing bulbs", "atmosphere": "warm, cozy, slightly dramatic due to angle" }, "camera\_and\_perspective": { "angle": "extreme low angle shot, worm's-eye view, looking up at the subject", "shot\_type": "medium close-up", "focus": "sharp focus on face, depth of field with softly blurred background only" }, "lighting": { "type": "warm artificial indoor lighting", "source": "ceiling chandelier lights", "effect": "soft warm glow on face, highlights on cheeks and nose, shadows under jawline, ambient tungsten color tone" }, "technical\_specs": { "resolution": "8k", "quality": "masterpiece, high fidelity, raw photo style", "film\_stock": "Kodak Portra 400 vibe, slight grain" } }
```

[[Face Consistency]] [[Tungsten Lighting]] [[Worm Eye View]] [[Film Photography]]

---

### 6. 四格韩式美妆专题拼贴提示（玻璃肌）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个高度具体的 JSON 提示，用于生成韩式四格美妆编辑拼贴画，强调“玻璃肌”、水润湿发造型和宿醉腮红。它要求所有画面中的面部特征保持严格一致，并详细说明了妆容（娃娃眼、美瞳、水光唇）、灯光（柔和影棚灯光 + 美妆闪光灯）以及每个画面的构图（超特写、全脸、戴复古帽的半脸）。

![四格韩式美妆专题拼贴提示（玻璃肌）](https://cms-assets.youmind.com/media/1769236001103_f6pc99_G_VkWJhawAEPL0F.jpg)
![四格韩式美妆专题拼贴提示（玻璃肌）](https://cms-assets.youmind.com/media/1769236000816_un9tni_G_VkVgrbAAEw7ws.jpg)

```
{ "collage": { "style": { "type": "ultra high-quality hyper-realistic beauty editorial collage", "layout": "4 photo panels arranged in a tilted diagonal grid layout", "grid\_details": "clean white borders separating each frame, forming a modern high-end beauty campaign collage. Each frame is slightly rotated at a different angle, creating a dynamic diagonal composition.", "resolution": "8K UHD, hyper-realistic, beauty editorial photoshoot", "consistency": "All panels clearly show the same woman, face identity consistent, original facial structure preserved, do not change the face." }, "subject": { "hair": "Rambut coklat pendek di atas bahu (bob) sedikit messy, baby hair halus di dahi dan pelipis.", "accessories": "Anting emas kecil dan kalung emas detail bunga lily.", "specific\_accessory": "Topi plaid cokelat vintage di salah satu frame." }, "makeup": { "skin": "Kulit porcelain glass skin super glowing, dewy wet look, tekstur kulit nyata dan detail. Highlight basah kuat di tulang pipi, bawah mata, dan ujung hidung.", "blush": "Blush pink rosy intens gaya igari blush, menyebar dari pipi ke bawah mata dan batang hidung.", "eyes": "Mata besar doll-like, softlens abu-abu kebiruan sangat jelas dan tajam. Bulu mata panjang lentik ala Douyin, lower lashes tipis tapi nyata. Eyeshadow pink–peach dengan shimmer lembut, inner corner berkilau. Eyeliner cokelat tipis rapi.", "lips": "Bibir pink glossy juicy, tampak lembap dan reflektif." }, "frames": \[ { "id": 1, "shot\_type": "extreme close-up pipi & mata", "focus": "fokus glass skin dan blush" }, { "id": 2, "shot\_type": "full face beauty portrait", "focus": "menghadap kamera" }, { "id": 3, "shot\_type": "half-face close-up", "focus": "dengan topi plaid cokelat" }, { "id": 4, "shot\_type": "extreme close-up mata & hidung", "focus": "highlight basah jelas" } \], "lighting\_and\_mood": { "lighting": "Soft studio lighting + beauty flash glow. High contrast glow tapi tetap natural. Ultra sharp focus, depth detail tinggi.", "mood": "glossy • dreamy • doll-like • high-end • Korean beauty editorial" } } }
```

[[Face Consistency]] [[Beauty Photography]] [[Photo Grid]] [[Glass Skin]]

---

### 7. 面部一致性压力测试提示（震惊表情，低角度）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个为 Nano Banana Pro 设计的结构化 JSON 提示词，旨在测试极端条件下的面部一致性：一个极度震惊的表情，以及一个虫眼视角、低角度特写。该提示词明确将面部身份锁定到参考图像，同时将表情和环境更改为一种抓拍的、略带颗粒感的智能手机摄影风格。

![面部一致性压力测试提示（震惊表情，低角度）](https://cms-assets.youmind.com/media/1769235989551_wvj7ex_G_VkE8BawAAxYQG.jpg)

```
Use the same face from the reference image without changing facial features { "image\_description": { "subject": { "person": "Young woman with blonde hair and fair skin", "expression": "Extremely shocked and surprised, mouth wide open in a gasp, eyes rolled slightly upward, dramatic facial expression", "pose": "Reclining or lying down, captured from a low-angle perspective looking up" }, "clothing\_and\_style": { "top": "Purple sheer or mesh top with a solid chest panel featuring a large, colorful butterfly print (yellow, orange, and red wings)", "details": "Small iridescent sequins or rhinestones on the fabric, dark nail polish on visible hand" }, "environment": { "background": "A patterned pillow with a floral or leaf motif in shades of burgundy and beige, plain off-white wall behind it", "lighting": "Soft, indoor ambient lighting, slightly shadowed" }, "technical\_attributes": { "camera\_angle": "Close-up, extreme low angle (worm's eye view)", "image\_quality": "Slightly grainy, candid smartphone photography style, soft focus", "color\_palette": "Deep purples, vibrant yellows from the butterfly print, and muted earth tones in the background" } } }
```

[[Face Consistency]] [[Smartphone Photography]] [[Worm Eye View]]

---

### 8. 四格工作室编辑电影拼贴画提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个复杂的 JSON 提示，用于生成一个超逼真、高端电影级的时尚工作室拼贴画，包含四个不同的面板。它定义了全局资产，以确保头发、皮肤（水润、玻璃肌效果）和服装（针织迷你连衣裙）的一致性，然后为每个面板指定了独特的摄像机角度、动作（吃草莓、胎儿坐姿）和视觉锚点，旨在营造出奢华杂志版面的美学效果。

![四格工作室编辑电影拼贴画提示](https://cms-assets.youmind.com/media/1769235994665_4zrzjz_G_VjpCPaQAEejva.jpg)

```
{ "realism\_level": "Ultra-photorealistic", "texture\_quality": "8k", "lighting\_simulation": "Ray-traced studio lighting" } }, "global\_assets": { "subject\_definition": { "hair": { "style": "Long, loosely wavy, voluminous", "texture": "Natural, individual strands defined", "behavior": "Messy but styled, framing face and shoulders" }, "complexion": { "skin\_texture": "Porous, hyper-realistic", "finish": "Dewy, glass-skin effect", "makeup": { "cheeks": "Heavy flush/blush", "lips": "High-gloss, plump, natural pink", "eyes": "Clean, defined lashes, natural brows" } }, "wardrobe": { "item": "Mini dress", "fit": "Bodycon / Tight", "fabric": { "material": "Soft textured knit / Boucle", "tactility": "Fuzzy, light-catching fibers", "color": "{argument name="dress color" default="Soft mauve"} or neutral taupe" }, "details": "Spaghetti straps, mid-thigh length" } }, "environment\_definition": { "studio\_setup": { "background": "Seamless paper, soft off-white/beige", "atmosphere": "Clean, warm, intimate" }, "lighting\_rig": { "key\_light": "Large diffuse softbox (Front-Left)", "fill\_light": "Reflector (Right)", "highlights": "Specular highlights on lips, cheekbones, and shoulders" } } }, "panel\_architecture": \[ { "position": "Top-Left (1)", "shot\_type": "Extreme Close-Up (Macro)", "composition": { "angle": "Low angle, looking up slightly", "focus": "Mouth and nose area", "depth\_of\_field": "Shallow" }, "action": { "primary": "Eating a strawberry", "nuance": "Delicate finger hold, lips slightly parted" }, "visual\_anchors": \[ "Moisture on strawberry surface", "Gloss reflection on lips", "Baby hairs at temple" \] }, { "position": "Top-Right (2)", "shot\_type": "Medium Shot (Thigh-up)", "composition": { "angle": "Eye level", "pose\_dynamic": "Leaning forward slightly towards lens" }, "action": { "stance": "Standing straight on", "arms": "Relaxed at sides", "expression": "Direct gaze, alluring pout" }, "visual\_anchors": \[ "Texture of knit dress", "Collarbone shadows", "Curvature of waist" \] }, { "position": "Bottom-Left (3)", "shot\_type": "Full Body (Seated)", "composition": { "angle": "Side profile", "framing": "Subject compacted on floor" }, "action": { "pose": "Knees to chest (fetal position variation)", "interaction": "Cheek resting on knee,"

The prompt is structured with global assets for hair, skin, makeup, and wardrobe to maintain consistency, followed by a panel-based architecture. Each panel has its own camera angle, framing, and action:

* An extreme close-up macro shot focus
```

[[Face Consistency]] [[Luxury Fashion]] [[Magazine Editorial]] [[Photo Grid]]

---

### 9. 发型变化的编辑美容拼贴画

**Author**: [路飞 🏴‍☠️ AI 研究员🧐](https://x.com/0xluffy_eth)  **Date**: 2026-01-23  **Language**: zh

> 一个结构化的提示，旨在生成一个 4x3 网格拼贴画，展示同一主体，在所有面板中保持完美的脸部一致性和表情，同时展示十种不同的发型，非常适合使用参考图像进行美妆编辑或虚拟试戴。

![发型变化的编辑美容拼贴画](https://cms-assets.youmind.com/media/1769236032856_wa76oj_G_VTy33bAAQaEo_.jpg)

```
{
  '场景类型': '{argument name="场景类型" default="编辑美妆拼贴"}',
  '主体': {
    '身份锁定': true,
    '面部一致性': '在所有画面中完美匹配',
    '表情': '不变、中性且放松',
    '肌肤': '逼真纹理、自然毛孔、高保真'
  },
  '布局': {
    '网格': '4x3',
    '构图': '等大小肖像面板',
    '一致性': '每帧面部对齐对称'
  },
  '发型变化': [
    '{argument name="发型1" default="光滑长直发"}',
    '高马尾',
    '纹理蓬乱发髻',
    '超短发',
    '辫子皇冠',
    '柔软飘逸波浪',
    '齐肩短发',
    '低束发髻',
    '侧边辫',
    '蓬松卷'
  ],
  '造型': {
    '服装': '所有面板中相同中性服装',
    '妆容': '每张照片相同干净美妆'
  },
  '光线': {
    '类型': '柔和棚拍光',
    '色调': '温暖',
    '阴影': '温柔自然'
  },
  '背景': {
    '风格': '微妙模糊棚拍背景',
    '颜色': '温暖中性色调'
  },
  '质量': {
    '细节': '超详细',
    '摄影': '专业肖像',
    '效果': '高端编辑风格'
  }
}
```

[[Face Consistency]] [[Beauty Photography]]

---

### 10. G-Wagon 冬季时尚肖像与面部一致性提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-23  **Language**: en

> 一个详细的文本提示，用于生成一张超逼真的冬季肖像，描绘一名男子身穿蓬松的黑色皮草大衣，站在雪景中的黑色 G 级越野车旁，并严格指示保持参考照片中（面部锁定）精确的面部结构和外观。

![G-Wagon 冬季时尚肖像与面部一致性提示](https://cms-assets.youmind.com/media/1769236031235_0ot7jf_G_UQFe2bAAAENsX.jpg)

```
Highly detailed close-up photograph, ultra-photorealistic, 8K resolution shot on a digital camera with 100mm f/2.8 studio portrait lens. Impeccable sharpness, extreme details, cinematic depth of field, consistent neutral color grading with uniform tones across the entire image, no color shifts. He is dressed in black wide-leg trousers and a black t-shirt He wears a voluminous black fur coat, fashionable sunglasses, and black leather gloves His hairstyle matches exactly the reference from the app: clean, medium-shortlength, neatly styled, smooth and controlled, natural volume, no curls, no wet efect Strictly maintain the facial structure and overall appearance from the attached first photo without distortion. The man stands next to a black {argument name="car model" default="G-Wagon"}, striking a stylish pose; one of his hands is slightly raised, while the other holds the edge of the fur coat, creating a confident and fashionable mood. The background is a snow-covered landscape with tall trees, snowflakes gently falling to the ground, adding a subtle cinematic atmosphere. Natural lighting with balanced exposure and consistent color temperature, emphasizing the outfit and winter environment. Focus on facial detalls, ⚫ realistic skin texture, and the textures of the clothing
```

[[Face Consistency]] [[Snow Scene]]

---

### 11. Nano Banana Pro 双人肖像提示词：机场和咖啡馆场景

**Author**: [行者AI视频](https://x.com/joshesye)  **Date**: 2026-01-22  **Language**: zh

> 以下是 Nano Banana Pro 的两个不同的图像生成提示，两者都要求 AI 保持参考图像的面部特征。第一个提示描述了一位年轻的亚洲女性在机场休息室里，穿着灰色仿皮草大衣，呈现出高对比度、都市酷感的审美。第二个提示则是在一个极简主义的白色咖啡馆里，同一位女性穿着白色蕾丝连衣裙，强调明亮、纯净、透明的视觉风格。

![Nano Banana Pro 双人肖像提示词：机场和咖啡馆场景](https://cms-assets.youmind.com/media/1769149366696_xhf6xd_G_OwLXzbQAApGp_.jpg)
![Nano Banana Pro 双人肖像提示词：机场和咖啡馆场景](https://cms-assets.youmind.com/media/1769149367302_sxh55e_G_OwLYeXoAArQ78.jpg)
![Nano Banana Pro 双人肖像提示词：机场和咖啡馆场景](https://cms-assets.youmind.com/media/1769149366734_p86c26_G_OwLXxaQAA7WSh.jpg)
![Nano Banana Pro 双人肖像提示词：机场和咖啡馆场景](https://cms-assets.youmind.com/media/1769149368373_xus369_G_OwLXvbIAAlKgU.jpg)

```
提示词1：使用参考图像中的同一张脸，不改变面部特征，

一名留着{argument name="发型" default="黑色中短发和轻盈空气刘海"}的年轻亚洲女性，坐在现代机场候机室的灰色长椅上。她身穿一件厚实的灰色仿皮草外套，内搭灰色高领针织衫，下身穿着带有精致菱格纹理的灰色连裤袜，双腿交叠。她正低头专注地玩着手中的智能手机，身侧挎着一个黑色的绗缝皮质链条包。背景是宽敞明亮的航站楼，巨大的落地玻璃窗引入了清冷的自然光，远处可见其他乘客的身影，地面光洁且带有淡淡的倒影。整体画面呈现出一种高级灰的都市冷淡风调色，细节真实且富有生活气息。

提示词1：

使用参考图像中的同一张脸，不改变面部特征,

一位气质出众的长发亚洲女性，穿着{argument name="服装" default="洁白的露肩蕾丝连衣裙"}，优雅地席地而坐在极简风格的咖啡厅吧台前。她的双腿修长并向前延伸，脚踩银色细带高跟鞋。背景是纯白色的木质板条墙和简洁的货架，陈列着整齐的白色器皿。在她面前的地板上，放着一盘色泽金黄的可颂面包。室内光线明亮且均匀，呈现出一种高级、纯净且通透的视觉风格，皮肤细腻有质感。
```

[[Face Consistency]] [[Asian Female Portrait]]

---

### 12. 热带时尚编辑拼贴画提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-21  **Language**: en

> 一个高度结构化的提示，用于生成一个由 4 个面板组成的超写实时尚专题拼贴画，场景设定在热带海滩环境。它指定了一件石灰绿色露背上衣和一条薄荷绿色亮片迷你裙，要求严格锁定参考图像中的面部身份，并详细说明了每个面板的构图，包括纹理特写。

![热带时尚编辑拼贴画提示](https://cms-assets.youmind.com/media/1769063215305_evxcer_G_NBUktXoAEp2DG.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_fashion_editorial_collage",
      "version": "v1.0_LIME_ORCHID_SEQUIN_4PANEL_EN",
      "priority": "highest",
      "language": "en"
    },
    "references": {
      "reference_image_subject": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "FACE_IDENTITY_LOCK",
        "strict_lock": true,
        "face_similarity_priority": "MAX",
        "no_identity_blending": true,
        "no_beautify": true,
        "no_age_shift": true,
        "preserve_skin_texture": true,
        "preserve_facial_proportions": true
      },
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "WARDROBE_MOOD_COMPOSITION_ANCHOR",
        "strict_lock": false,
        "preserve_outfit": true,
        "preserve_color_palette": true,
        "preserve_setting": true,
        "preserve_collage_layout": true
      }
    },
    "global_constraints": {
      "rating": "G",
      "no_nudity": true,
      "no_explicit_content": true,
      "no_text": true,
      "no_logos": true,
      "no_watermark": true
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "high_end_fashion_editorial_photoreal",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle",
      "color_grade": "warm_tropical_daylight",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "creative_prompt": {
      "scene_summary": "A 4-panel fashion editorial collage in a tropical beach setting with palm trees and sandy ground. The same woman appears in three panels wearing a {argument name="top color" default="lime-green"} halter draped top with an orchid flower clasp at the neckline and a {argument name="skirt color" default="mint-green"} sequin mini skirt made of large round reflective discs. One panel is a texture close-up of the sequin discs. The subject’s face must be clearly visible and match the reference identity exactly (100%).",
      "collage_layout": {
        "format": "2x2 grid collage",
        "panel_1": "Full-body front pose by a palm tree, holding a fresh green coconut at hip level, confident relaxed stance, face clearly visible.",
        "panel_2": "Tight neckline close-up showing the orchid flower clasp and draped fabric folds, partial face/jawline acceptable but keep identity consistent, realistic skin texture.",
        "panel_3": "Macro texture close-up of the mint-green round sequin discs (no face), glossy reflective surface detail.",
        "panel_4": "Three-quarter back/side pose looking over shoulder toward camera, face fully visible, palm trees in background, outfit back drape visible."
      },
      "subject": {
        "count": 1,
        "identity": "Use the exact face identity from the subject reference with 100% similarity across panels.",
        "age": "adu"
```

[[Face Consistency]] [[Four Panel Collage]]

---

### 13. 奢华度假村时尚大片，彰显独特个性

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-21  **Language**: en

> 一个详细的 JSON 提示，用于创建一套超高分辨率、照片级的时尚大片肖像，背景设定在豪华度假村。它包含严格的限制、特定的输出设置（2:3 宽高比、热带色彩分级），以及关于拍摄对象姿势、表情和服装（橄榄绿露背长裙、金色花卉胸针）的详细创意说明。它要求提供两张参考图片：一张用于严格的面部识别锁定，另一张用于风格/姿势锚定。

![奢华度假村时尚大片，彰显独特个性](https://cms-assets.youmind.com/media/1769063252826_khh1t6_G_M9zHSXMAAYonL.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_fashion_editorial_single",
      "version": "v1.0_OLIVE_HALTER_SLIT_RESORT_EN",
      "priority": "highest",
      "language": "en"
    },
    "references": {
      "reference_image_subject": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "FACE_IDENTITY_LOCK",
        "strict_lock": true,
        "face_similarity_priority": "MAX",
        "no_identity_blending": true,
        "no_beautify": true,
        "no_age_shift": true,
        "preserve_skin_texture": true,
        "preserve_facial_proportions": true
      },
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "WARDROBE_POSE_LIGHTING_ANCHOR",
        "strict_lock": false,
        "preserve_outfit": true,
        "preserve_pose": true,
        "preserve_setting": true,
        "preserve_color_palette": true
      }
    },
    "global_constraints": {
      "rating": "G",
      "no_nudity": true,
      "no_explicit_content": true,
      "no_text": true,
      "no_logos": true,
      "no_watermark": true
    },
    "output_settings": {
      "aspect_ratio": "2:3",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "luxury_resort_fashion_editorial_photoreal",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle",
      "color_grade": "warm_sunlit_tropical",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "creative_prompt": {
      "scene_summary": "A high-end resort fashion editorial portrait in lush tropical greenery and pale stone steps. The same woman with 100% face identity match to the subject reference is wearing an olive-green halter maxi dress with a deep neckline, gathered waist, high thigh slit, and a gold floral brooch at the hip. Elegant jewelry and polished glam styling, but realistic skin texture and natural detail.",
      "subject": {
        "count": 1,
        "identity": "Face must match the subject reference exactly (100% similarity).",
        "age": "adult",
        "pose": "standing with one hand on hip, weight shifted, slit revealing one leg, confident editorial stance",
        "expression": "calm confident, slightly serious gaze, looking off-camera",
        "hair": "sleek pulled-back style or tight updo, neat flyaways minimal",
        "makeup": "glam but natural texture, defined eyes and lips, no heavy retouch"
      },
      "wardrobe_details": {
        "dress": "olive-green halter maxi dress, deep neckline, ruched waist, high thigh slit, gold floral brooch at hip",
        "accessories": "statement earrings, stacked bangles/bracelets, optional chunky cuff, subtle rings",
        "shoes": "not mandatory; if visible, minimal strappy heels in neutral tone"
      },
      "environment": {
        "location": "luxury tropical villa cour"}
    }
  }
}
```

[[Face Consistency]] [[Pose Reference]]

---

### 14. 超写实美妆编辑拼贴画 (结构化 JSON)

**Author**: [Mikasa](https://x.com/Mikasa_rose729)  **Date**: 2026-01-21  **Language**: en

> 一个结构化的 JSON 提示词，用于创建一个超高质量、超现实的美容编辑拼贴画，其中包含一位身份一致的女性。该提示词详细说明了特定的韩式美容编辑妆容技巧（玻璃肌、宿醉腮红、戴着美瞳的娃娃眼），并指定了一个动态的对角线网格布局，包含四个特写照片面板，每个面板都聚焦于不同的面部特征或配饰。

![超写实美妆编辑拼贴画 (结构化 JSON)](https://cms-assets.youmind.com/media/1769063167018_trtqr0_G_M2EmoXYAccq6H.jpg)

```
{
  "collage": {
    "style": {
      "type": "ultra high-quality hyper-realistic beauty editorial collage",
      "layout": "4 photo panels arranged in a tilted diagonal grid layout",
      "grid_details": "clean white borders separating each frame, forming a modern high-end beauty campaign collage. Each frame is slightly rotated at a different angle, creating a dynamic diagonal composition.",
      "resolution": "8K UHD, hyper-realistic, beauty editorial photoshoot",
      "consistency": "All panels clearly show the same woman, face identity consistent, original facial structure preserved, do not change the face."
    },
    "subject": {
      "hair": "Rambut coklat pendek di atas bahu (bob) sedikit messy, baby hair halus di dahi dan pelipis.",
      "accessories": "Anting emas kecil dan kalung emas detail bunga lily.",
      "specific_accessory": "Topi plaid cokelat vintage di salah satu frame."
    },
    "makeup": {
      "skin": "Kulit porcelain glass skin super glowing, dewy wet look, tekstur kulit nyata dan detail. Highlight basah kuat di tulang pipi, bawah mata, dan ujung hidung.",
      "blush": "Blush pink rosy intens gaya igari blush, menyebar dari pipi ke bawah mata dan batang hidung.",
      "eyes": "Mata besar doll-like, softlens abu-abu kebiruan sangat jelas dan tajam. Bulu mata panjang lentik ala Douyin, lower lashes tipis tapi nyata. Eyeshadow pink–peach dengan shimmer lembut, inner corner berkilau. Eyeliner cokelat tipis rapi.",
      "lips": "Bibir pink glossy juicy, tampak lembap dan reflektif."
    },
    "frames": [
      {
        "id": 1,
        "shot_type": "extreme close-up pipi & mata",
        "focus": "fokus glass skin dan blush"
      },
      {
        "id": 2,
        "shot_type": "full face beauty portrait",
        "focus": "menghadap kamera"
      },
      {
        "id": 3,
        "shot_type": "half-face close-up",
        "focus": "dengan topi plaid cokelat"
      },
      {
        "id": 4,
        "shot_type": "extreme close-up mata & hidung",
        "focus": "highlight basah jelas"
      }
    ],
    "lighting_and_mood": {
      "lighting": "Soft studio lighting + beauty flash glow. High contrast glow tapi tetap natural. Ultra sharp focus, depth detail tinggi.",
      "mood": "glossy • dreamy • doll-like • high-end • Korean beauty editorial"
    }
  }
}
```

[[Face Consistency]] [[Four Panel Collage]] [[Glass Skin]]

---

### 15. 模拟闪光摄影人像提示词，带身份锁定

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-21  **Language**: en

> 一个高度具体的 JSON 提示，用于生成一张模拟复古风格的年轻女性数字肖像。它强制执行严格的身份锁定（100% 面部准确度），指定“快乐、俏皮”的表情，并要求采用复古胶片闪光摄影照明，具有强烈、柔和的高光和真实的闪光对比度，背景为简约的白墙。

![模拟闪光摄影人像提示词，带身份锁定](https://cms-assets.youmind.com/media/1769063177082_tvlvm8_G_MyEjhbAAAjwLc.jpg)
![模拟闪光摄影人像提示词，带身份锁定](https://cms-assets.youmind.com/media/1769063177177_gx9a96_G_MyEhBa0AEB1YC.jpg)
![模拟闪光摄影人像提示词，带身份锁定](https://cms-assets.youmind.com/media/1769063177136_bmpcwf_G_MyEfcagAALUzJ.jpg)

```
{
  "image_request": {
    "subject": {
      "type": "Young adult woman",
      "identity_constraint": "100% identical face — original facial structure and proportions must remain completely unchanged (NO editing or alteration)",
      "expression": "Joyful, playful, carefree",
      "gaze": "Eyes closed while smiling brightly",
      "emotion": "Flirtatious, candid, confident"
    },

    "pose_and_posture": {
      "body_angle": "Body angled slightly to the side",
      "lean": "Leaning forward gently",
      "hands": "Hands raised near the face in a soft, expressive gesture",
      "shoulders": "Relaxed posture, natural stance"
    },

    "hair_and_accessories": {
      "hair": {
        "color": "Dark brown",
        "style": "Loose textured updo",
        "details": [
          "Soft tassels framing the face",
          "Natural flyaways",
          "Casual, effortless styling"
        ]
      },
      "accessories": {
        "earrings": "Large rectangular gold statement earrings",
        "necklace": "None"
      }
    },

    "face_and_makeup": {
      "skin": {
        "tone": "Warm, glowing",
        "texture": "Visible pores and realistic skin texture",
        "finish": "Natural, non-plastic, non-retouched"
      },
      "makeup_style": "Soft glamour",
      "features": {
        "brows": "Defined but natural",
        "eyes": {
          "liner": "Winged eyeliner",
          "lashes": "Long, separated lashes"
        },
        "cheeks": {
          "blush": "Soft natural blush",
          "highlight": "Subtle warm streaks on cheekbones"
        },
        "lips": {
          "color": "Glossy nude pink",
          "texture": "Realistic lip texture"
        }
      }
    },

    "outfit": {
      "dress": {
        "type": "Sleeveless mini dress",
        "color": "Solid black",
        "neckline": "High neck",
        "fabric": "Smooth matte fabric",
        "fit": "Tight, body-hugging",
        "design": "Minimalist, no patterns"
      }
    },

    "environment": {
      "location": "Indoor setting",
      "background": {
        "description": "Simple white wall with a closed door",
        "details": "Clean panel lines, no decorations",
        "distractions": "None"
      },
      "vibe": "Clean, nostalgic, intimate indoor atmosphere"
    },

    "lighting": {
      "type": "Direct on-camera flash",
      "style": "Vintage film flash photography",
      "effects": [
        "Strong but soft highlights on skin",
        "Authentic flash contrast",
        "Slight shadow cast behind the subject",
        "Natural flash flare"
      ],
      "restrictions": [
        "No modern studio lighting",
        "No artificial glow"
      ]
    },

    "camera_and_quality": {
      "lens": "35mm lens look",
      "depth_of_field": "Shallow but realistic",
      "focus": "Sharp focus on subject",
      "style": "Analog-inspired digital photography",
      "resolution": "High detail, photorealistic"
    }
   }
```

[[Face Consistency]] [[Playful Expression]]

---

### 16. 高定湿发造型编辑网格

**Author**: [NGINAI](https://x.com/Enginverse58966)  **Date**: 2026-01-21  **Language**: en

> 一个结构化的 JSON 提示词，用于生成 3x3 垂直照片网格的特写、高端时尚编辑肖像。其主要特点是“湿发”造型，湿漉漉的发丝垂落在脸上，光泽感与自然的瑕疵形成对比。该提示词要求纯白色影棚背景、明亮均匀的影棚灯光，并要求模特在所有九个面板中保持相同的面部特征，同时大幅改变面部表情。

![高定湿发造型编辑网格](https://cms-assets.youmind.com/media/1769063168742_w46yde_G_MjBVxXQAAuBi4.jpg)

```
{ "type": "image_to_image",  "prompt": "Keep the same face and identity. Vertical high-fashion beauty collage arranged in a 3x3 grid of close-up portraits against a clean, seamless pure white studio background. Bright, even front-facing studio lighting with soft fill, eliminating harsh shadows and creating a glossy editorial look. Subtle highlights on cheekbones, nose bridge, lips, and the neckline of a white T-shirt, while the background remains uniformly white. Young woman framed from mid-neck upward, shoulders square and facing the camera in every panel. Long, loose, wet hair falling naturally over the shoulders and partially across the face, with a few damp strands lightly clinging to cheeks and jawline and some falling toward the lips, adding movement and a raw, effortless aesthetic. The damp texture has a soft sheen that catches the light, contrasting gloss with natural imperfection. Across the grid, she changes facial expressions dramatically; one expression includes sticking out her tongue.", "aspect_ratio": "2:3", "style": "high-fashion editorial", "lighting": "bright even studio lighting, soft fill", "background": "pure white seamless studio", "output": { "grid": "3x3", "orientation": "vertical", "framing": "mid-neck upward" } }
```

[[Face Consistency]] [[Close-Up Portrait]] [[White Studio Background]] [[Wet Hair]]

---

### 17. 摩托车特写肖像，带换脸提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-21  **Language**: en

> 生成一张逼真、抓拍、手持智能手机拍摄的年轻男子坐在 Chrome Continental GT 650 摩托车上的照片。要求将主体面部替换为上传的参考图像，严格保持身份锁定，并强调强烈的早晨阳光、自然的皮肤纹理和特定的服装细节（白色背心、黑色皮夹克、深色牛仔裤）。

![摩托车特写肖像，带换脸提示](https://cms-assets.youmind.com/media/1769063215635_wxh632_G_MVtjaWwAAdtJE.jpg)

```
Realistic outdoor bright morning handheld smartphone photo, random candid and unposed. Replace the subject’s face with my uploaded reference exactly  same identity, facial structure, proportions, and skin tone.
A young man sitting on a Chrome edition Continental GT 650 motorcycle parked on a roadside at night. He is seated on the bike seat, torso slightly leaned forward. He placed his right hand on top of the helmet which is placed over the fuel tank, Chrome finished motorcycle helmet with hidden engraved af4ash logo in same chrome finish. The left hand is on backside of the neck as if adjusting back hair. looking directly into the camera.
creating strong sunlight on the face and upper body with soft background shadows. The face has a natural glass skin glow. with real skin texture visible. Sun kissed effect on face.
Wearing a sleeveless white tank top not tucked in, black plain leather jacket with spread collar. worn open, dark grey loose-fit jeans. Square Transparent frame black lens sunglasses. Army dog tag necklace. Medium length messy hair with natural. Natural fylways, Slim youthful build. Confident look on face.
Motorcycle fuel tank clearly visible with official “{argument name="motorcycle brand" default="Royal Enfield"}” branding. Background includes a limestone wall, trees above, and a flyover roadside. Bright morning sunshine, natural lens flare. 
Shot at eye level with natural smartphone perspective, sharp but realistic focus, slight low-light grain, No smile, No filters, no cinematic grading, natural realistic look.
```

[[Face Consistency]] [[Lifestyle Portrait]]

---

### 18. 韩式美妆编辑拼贴画提示

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2026-01-21  **Language**: zh

> 一个高度详细的多面板提示，用于制作超现实的韩国美妆编辑拼贴画，强调“玻璃肌”、浓郁的玫瑰色腮红（宿醉妆风格）、洋娃娃般的眼睛和水润的嘴唇。它指定了倾斜的对角线网格布局，并要求所有四个画面中的面部特征保持严格一致。

![韩式美妆编辑拼贴画提示](https://cms-assets.youmind.com/media/1769063213397_l12f99_G_LxLf2XIAAjqqn.jpg)
![韩式美妆编辑拼贴画提示](https://cms-assets.youmind.com/media/1769063213438_gumrac_G_LxLf2WwAAArNS.jpg)

```
{
  "collage": {
    "style": {
      "type": "ultra high-quality hyper-realistic beauty editorial collage",
      "layout": "4 photo panels arranged in a tilted diagonal grid layout",
      "grid_details": "clean white borders separating each frame, forming a modern high-end beauty campaign collage. Each frame is slightly rotated at a different angle, creating a dynamic diagonal composition.",
      "resolution": "8K UHD, hyper-realistic, beauty editorial photoshoot",
      "consistency": "All panels clearly show the same woman, face identity consistent, original facial structure preserved, do not change the face."
    },
    "subject": {
      "hair": "Rambut coklat pendek di atas bahu (bob) sedikit messy, baby hair halus di dahi dan pelipis.",
      "accessories": "Anting emas kecil dan kalung emas detail bunga lily.",
      "specific_accessory": "Topi plaid cokelat vintage di salah satu frame."
    },
    "makeup": {
      "skin": "Kulit porcelain glass skin super glowing, dewy wet look, tekstur kulit nyata dan detail. Highlight basah kuat di tulang pipi, bawah mata, dan ujung hidung.",
      "blush": "Blush pink rosy intens gaya igari blush, menyebar dari pipi ke bawah mata dan batang hidung.",
      "eyes": "Mata besar doll-like, softlens abu-abu kebiruan sangat jelas dan tajam. Bulu mata panjang lentik ala Douyin, lower lashes tipis tapi nyata. Eyeshadow pink–peach dengan shimmer lembut, inner corner berkilau. Eyeliner cokelat tipis rapi.",
      "lips": "Bibir pink glossy juicy, tampak lembap dan reflektif."
    },
    "frames": [
      {
        "id": 1,
        "shot_type": "extreme close-up pipi & mata",
        "focus": "fokus glass skin dan blush"
      },
      {
        "id": 2,
        "shot_type": "full face beauty portrait",
        "focus": "menghadap kamera"
      },
      {
        "id": 3,
        "shot_type": "half-face close-up",
        "focus": "dengan topi plaid cokelat"
      },
      {
        "id": 4,
        "shot_type": "extreme close-up mata & hidung",
        "focus": "highlight basah jelas"
      }
    ],
    "lighting_and_mood": {
      "lighting": "Soft studio lighting + beauty flash glow. High contrast glow tapi tetap natural. Ultra sharp focus, depth detail tinggi.",
      "mood": "glossy • dreamy • doll-like • high-end • Korean beauty editorial"
    }
  }
}
```

[[Face Consistency]] [[Beauty Photography]] [[Glass Skin]]

---

### 19. 超逼真的咖啡馆生活方式肖像，带有身份锁定提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-21  **Language**: en

> 一个高度限制性的提示，用于在现代咖啡馆中生成超现实的生活方式肖像，要求 100% 的面部准确性，并保留上传图像中的真实皮肤纹理。它指定了拍摄对象在带有 LED 照明的圆形木框内的姿势，强调纯粹的真实感和温暖、干净的美感。

![超逼真的咖啡馆生活方式肖像，带有身份锁定提示](https://cms-assets.youmind.com/media/1769063184530_y5bs4o_G_LiM0JakAAUQ2O.jpg)

```
Create an ultra-realistic, high-end lifestyle portrait of one adult subject, captured in a calm, elegant, modern café environment. The subject is seated casually inside a circular wooden frame embedded with warm LED rim lighting, surrounded by lush green foliage and soft floral decor. The pose is relaxed and natural: one leg crossed over the other, body slightly angled, shoulders relaxed, hands resting naturally while holding a small bouquet of fresh flowers. Overall mood is warm, clean, elegant, youthful, and approachable — pure realism only. No stylization, no fantasy, no cinematic exaggeration.

Use my uploaded face image as the ONLY facial identity reference

Maintain 100% facial accuracy: exact bone structure, eye shape, eyelid fold, eyebrow shape, nose bridge and tip, lip shape, jawline, chin, cheek volume, hairline, and facial proportions

Identity must remain perfectly consistent from all angles (front, 3/4, side, seated pose, slight head tilt)

No face blending, no beautification, no symmetry correction

No AI face drift

Preserve real skin texture: pores, fine lines, natural imperfections

Expression: soft, natural smile, relaxed and genuine

Soft pastel long-sleeve knit top (dusty pink / muted rose tone)

High-waisted, straight-fit beige or cream trousers

Clean white chunky sneakers

Minimal accessories only (simple earrings, smartwatch or minimal wrist accessory)

Hair neatly styled, natural, pulled back or softly tied

Natural makeup: realistic skin tones, no heavy retouching

Modern café or lifestyle studio interior

Circular wooden structure with embedded warm LED light ring

Green plants and floral arrangements integrated into the frame

Soft bokeh background with warm ambient lighting

Clean, uncluttered setting with depth and realism

Full-body or 3/4 body vertical portrait

Eye-level camera angle

50mm–85mm lens look

Natural perspective, no distortion

Subject centered within the circular frame

Shallow depth of field, background softly blurred

Soft, warm, diffused lighting

LED rim light gently outlining the circular frame

Even facial illumination with natural shadow falloff

No harsh highlights, no blown whites

Realistic skin reflections and depth

Negative prompt:

No stylization

No cinematic color grading

No beauty filters

No smooth or plastic skin

No exaggerated proportions

No painterly or illustrated look

No artificial glow

No face morphing or identity shift

Ultra-photorealistic

Editorial lifestyle photography quality

Natural colors, true-to-life skin tones

Identity remains unchanged and accurate from every angle
```

[[Face Consistency]] [[LED Lighting]] [[Authentic Skin Texture]]

---

### 20. 90 年代时尚大片，以马匹和身份锁为主题的提示词

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-21  **Language**: en

> 一个用于生成具有 90 年代美学的单色艺术时尚社论照片的提示。它要求保留参考图像中的面部，将主体（穿着宽松深色服装和太阳镜）置于极简主义凳子上，身后是一匹强壮的黑马，背景是高对比度、过度曝光的自然景观。

![90 年代时尚大片，以马匹和身份锁为主题的提示词](https://cms-assets.youmind.com/media/1769063185379_emeno0_G_LiIAkWMAAKmPm.jpg)

```
Without changing the face from the reference image. Monochrome fine-art fashion editorial photograph of the woman with wavy hair, now wearing dark sunglasses and dark oversized layered clothing with wide-leg trousers and leather boots. She is sitting low on a minimalist metal stool, legs spread forward in a relaxed, grounded pose, with one hand loosely resting between her knees holding thin leather reins. A strong black horse stands closely behind her, partially overlapping her silhouette. The setting is an open natural landscape with rough ground, wild grass, and a bright overexposed sky creating strong negative space. High contrast lighting with deep blacks, soft highlights, and a matte texture. Timeless cinematic mood, medium-format film look with subtle grain.
```

[[Face Consistency]] [[90s Aesthetic]]

---

### 21. 精致都市阳台肖像提示

**Author**: [Javeriya ✨](https://x.com/JadoonKhan281)  **Date**: 2026-01-21  **Language**: en

> 生成一张逼真照片的结构化提示：一位优雅的女士（与参考图片匹配）站在现代高层阳台上，夕阳西下，强调温暖、自然的灯光和优雅、宁静的氛围，背景是城市天际线。

![精致都市阳台肖像提示](https://cms-assets.youmind.com/media/1769063229807_6zlogv_G_KtVPsbsAAnLOG.jpg)
![精致都市阳台肖像提示](https://cms-assets.youmind.com/media/1769063229795_yhb0bz_G_KtVSDaoAMe1SP.jpg)

```
{
  "image_request": {
    "subject": {
      "gender": "woman",
      "hair": {
        "color": "blonde",
        "style": "long",
        "reference": "match_uploaded_image_exactly"
      },
      "face": {
        "features": "match_uploaded_image_exactly",
        "expression": "tranquil / sophisticated"
      },
      "attire": {
        "description": "simple, sleeveless, fitted black dress",
        "color": "black"
      },
      "pose": "standing, alternative style"
    },
    "environment": {
      "location": "modern high-rise apartment balcony",
      "features": [
        "glass railing",
        "modern architecture",
        "geometrically arranged green spaces"
      ],
      "background": {
        "view": "urban skyline",
        "elements": ["glass skyscrapers", "apartment towers"]
      }
    },
    "lighting_and_atmosphere": {
      "time_of_day": "sunset",
      "lighting_style": "warm, soft, natural",
      "mood": ["tranquil", "sophisticated", "modern", "elegant"],
      "effects": ["sunlight reflection", "depth of field"]
    },
    "technical_specs": {
      "resolution": "8K",
      "style": "realistic photography",
      "negative_prompt": [
        "blurry", "low quality", "distortion", "extra fingers", 
        "mutated hands", "deformed face", "cartoon", "painting", 
        "unrealistic skin", "overexposed", "underexposed", 
        "artificial light", "noisy background", "watermark", 
        "text", "logo", "duplicate person", "bad anatomy", 
        "exaggerated proportions"
      ]
    }
  }
}
```

[[Face Consistency]] [[Warm Natural Light]] [[City Skyline]] [[Sunset Photography]]

---

### 22. 带猎豹肖像的霸气黑帮老大提示

**Author**: [Gravity X](https://x.com/GravityX_MW)  **Date**: 2026-01-21  **Language**: en

> 生成一张强劲、时尚的图像，描绘一位散发着“霸道黑帮大佬气质”的男士，他坐在一张天鹅绒沙发上。关键元素是一只猎豹，它慵懒地趴在他的腿上，身上佩戴着沉重的金链，这与男士的高级定制深色服装形成鲜明对比，展现出动物的原始力量，同时严格保留上传的男士面部特征。

![带猎豹肖像的霸气黑帮老大提示](https://cms-assets.youmind.com/media/1769063207462_kg0578_G_Kkr7AWQAATBUr.jpg)

```
GENERATE A POWERFUL AND STYLISH IMAGE OF THE UPLOADED MAN, 100 PERCENT FACE RESERVED, RADIATING BOSSY GANGSTER VIBES. HE IS SEATED CONFIDENTLY ON A LUXURIOUS VELVET SOFA, LEANING BACK IN A RELAXED YET COMMANDING POSE. A CHEETAH, ADORNED WITH HEAVY GOLD CHAINS, SITS ACROSS HIS LAP, ITS SLEEK BODY DRAPED NATURALLY OVER HIM.

THE MAN'S HEAD IS TURNED SLIGHTLY DOWNWARD, GAZING AT THE CHEETAH WITH A COOL, COMPOSED EXPRESSION, SUNGLASSES ENHANCING HIS AURA OF DOMINANCE AND STYLE. ONE HAND RESTS CASUALLY ON THE CHEETAH'S BACK WHILE THE OTHER RESTS ALONG THE ARM OF THE SOFA, SHOWING BOTH CONTROL AND EASE.

HE IS DRESSED IN HIGH-FASHION DARK ATTIRE - EITHER A PINSTRIPE SUIT OR AN OPEN-COLLARED SILK SHIRT LAYERED WITH BOLD GOLD JEWELRY. THE CHEETAH HAS A FIERCE, OPEN-MOUTH EXPRESSION, MIRRORING THE MAN'S AURA OF RAW POWER.
```

[[Face Consistency]] [[Luxury Fashion]]

---

### 23. 浪漫奢华肖像提示（红裙）

**Author**: [Adam也叫吉米](https://x.com/Adam38363368936)  **Date**: 2026-01-21  **Language**: en

> 一个用于 Nano Banana Pro 的 JSON 提示，旨在生成一张高质量、富有戏剧性和浪漫色彩的肖像照。肖像主体（基于上传图片）身着鲜红色露背连衣裙，强调奢华感、直视镜头，并突出流畅面料与玫瑰、链条等几何元素之间的对比。

![浪漫奢华肖像提示（红裙）](https://cms-assets.youmind.com/media/1769063240600_as6wnm_G_KcHGsakAA--Ur.jpg)
![浪漫奢华肖像提示（红裙）](https://cms-assets.youmind.com/media/1769063240435_1t6tbu_G_KcHGkaoAIKSYu.jpg)

```
{
  "image_metadata": {
    "title": "Romantic Opulence",
    "subject_identity": "The person I uploaded",
    "aspect_ratio": "3:4",
    "aesthetic_category": "Curated Luxury / Theatrical Romance"
  },
  "visual_composition": {
    "subject_pose": {
      "body_position": "Seated/leaning forward",
      "head_orientation": "Turned back toward camera",
      "interaction": "Breaking the fourth wall / direct eye contact",
      "expression": "Playful, confident, knowing engagement"
    },
    "wardrobe_details": {
      "garment": {
        "type": "{argument name="garment type" default="Red dress"}",
        "color_profile": "Vibrant / Passionate",
        "construction": "Open back, gathered fabric at waist and hips",
        "texture": "Fluid, elegant movement"
      },
      "adornments": {
        "material": "Delicate gold chain jewelry",
        "placement": "Draped across shoulders and spine",
        "visual_style": "Ceremonial, architectural"
      }
    },
    "environmental_props": {
      "primary_prop": "Round luxury box of {argument name="flower color" default="red"} roses",
      "floral_characteristics": "Tight, repetitive forms; dense arrangement",
      "symbolic_weight": ["Desire", "Devotion", "Abundance"]
    }
  },
  "thematic_analysis": {
    "psychological_layers": {
      "vulnerability": "Exposed by the open-back design",
      "agency": "Reframed as power through controlled posture and gaze",
      "intent": "Intentional luxury rather than accidental beauty"
    },
    "visual_contrasts": [
      {
        "element_a": "Organic fluidity (fabric and skin)",
        "element_b": "Geometric repetition (roses and chains)"
      }
    ]
  },
  "artistic_direction": {
    "lighting": "Softly defined, highlighting contours of the back and jewelry",
    "styling": "Neat hair, polished makeup",
    "audience_role": "Observer-turned-participant"
  }
}
```

[[Face Consistency]] [[Luxury Red Roses]] [[Red Backless Dress]]

---

### 24. 写实奢华酒吧人像 (豹纹连衣裙)

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-20  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真的编辑肖像，描绘一位自信的女性身穿豹纹吊带裙，坐在一间豪华鸡尾酒吧里。强调暖琥珀色灯光、相机闪光灯效果，并严格要求面部完全可见且清晰对焦，需要提供参考图像以确定姿势和构图。

![写实奢华酒吧人像 (豹纹连衣裙)](https://cms-assets.youmind.com/media/1768977308385_u7we2o_G_JG6nfXwAAgU3p.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_luxury_bar_portrait",
      "version": "v1.1_LEOPARD_DRESS_BAR_FACE_VISIBLE_NO_TEXT",
      "priority": "highest",
      "language": "tr"
    },

    "references": {
      "reference_image_1": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "POSE_COMPOSITION_STYLE_ANCHOR",
        "strict_lock": true,
        "preserve_pose": true,
        "preserve_body_proportions": true,
        "no_body_rescale": true
      }
    },

    "global_constraints": {
      "rating": "PG-13",
      "no_explicit_sexual_content": true,
      "no_text": true,
      "no_logos": true,
      "no_watermark": true
    },

    "output_settings": {
      "aspect_ratio": "3:4",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "ultra_photoreal_editorial_night_flash",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "color_grade": "warm_amber_luxury_bar",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },

    "creative_prompt": {
      "scene_summary": "Lüks, koyu ahşap kaplamalı klasik kokteyl barında gece çekimi. Leopar desenli ipek/saten slip elbise giyen kadın barda oturuyor ve elinde martini kadehi var. Işık sıcak ve sinematik, ortam premium ve şık.",

      "key_change_request": "YÜZ TAMAMEN GÖRÜNSÜN: saç yüzü kapatmasın. Saç yana taranmış veya arkaya atılmış olsun; iki göz, kaşlar ve burun net şekilde görünür. Yüz kameraya 3/4 dönük veya doğrudan kameraya bakıyor.",

      "environment": {
        "location": "luxury hotel bar / classic cocktail bar",
        "background": "parlak koyu ahşap paneller, bar şişeleri ve cam raflar, yumuşak bokeh ışıklar",
        "lighting": "on-camera flash hissi + sıcak ortam ışıkları; doğal gölgeler; gerçekçi yansımalar"
      },

      "subject": {
        "count": 1,
        "pose": "bar taburesinde oturuyor, bir koluyla barı destekliyor, diğer elinde martini kadehi hafif yukarıda",
        "expression": "cool, confident, relaxed",
        "hair": "yüzü kapatmayan dalgalı saç; saç gözlerin üstüne düşmesin; yüz açık ve net",
        "makeup": "soft glam, doğal ama belirgin göz makyajı, hafif ışıltılı cilt (retouch yok)",
        "wardrobe": "{argument name="dress pattern" default="leopard print"} slip dress (saten/ipek hissi), ince askılı",
        "details": "gerçekçi tırnaklar, minimal takı ve saat"
      },

      "camera_style": {
        "framing": "3:4, medium-full portrait",
        "lens_feel": "35mm-50mm feel, shallow depth of field",
        "focus": "GÖZLER RAZOR SHARP; yüz net; kadeh ve el doğal netlikte",
        "look": "real photo, not CGI, not painterly"
      },

      "quality_guards": {
        "no_ai_look": true,
        "no_beauty_filter": true,
        "no_hdr": true,
        "no_over_sharpening": true,
        "faces_must_be_clean": true,
        "hands_and_fingers
```

[[Face Consistency]] [[Warm Amber Lighting]]

---

### 25. 社论美容拼贴发型变化提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-20  **Language**: en

> 一个专为 Gemini App 上的 Nano Banana Pro 模型设计的详细 JSON 提示词。它能从一张参考图像生成一个 4x3 网格的编辑美容拼贴画，在展示十种不同发型变化的同时，保持完美的脸部一致性和中性表情。这非常适合虚拟试戴或高保真编辑造型手册。

![社论美容拼贴发型变化提示](https://cms-assets.youmind.com/media/1768977280828_app57s_G_Gb9dlXMAAYbxU.jpg)

```
{
  "scene_type": "editorial beauty collage",
  "subject": {
    "identity_lock": true,
    "face_consistency": "perfectly matched across all frames",
    "expression": "unchanged, neutral and relaxed",
    "skin": "realistic texture, natural pores, high fidelity"
  },
  "layout": {
    "grid": "4x3",
    "framing": "equal-sized portrait panels",
    "consistency": "symmetrical facial alignment in every frame"
  },
  "hairstyle_variations": [
    "{argument name="hairstyle 1" default="sleek long straight hair"}",
    "{argument name="hairstyle 2" default="high ponytail"}",
    "textured messy bun",
    "pixie haircut",
    "braided crown",
    "soft flowing waves",
    "short bob with bangs",
    "low tied bun",
    "side braid",
    "loose defined curls"
  ],
  "styling": {
    "outfit": "same neutral wardrobe across all panels",
    "makeup": "identical clean beauty makeup in every shot"
  },
  "lighting": {
    "type": "soft studio lighting",
    "tone": "warm",
    "shadows": "gentle and natural"
  },
  "background": {
    "style": "subtle blurred studio backdrop",
    "color": "warm neutral tones"
  },
  "quality": {
    "detail": "ultra-detailed",
    "photography": "professional portrait",
    "finish": "high-end editorial look"
  }
}
```

[[Face Consistency]] [[Beauty Editorial]] [[Grid Collage]]

---

### 26. 10 种发型照片拼贴提示

**Author**: [Karthik R](https://x.com/karthik_rangan)  **Date**: 2026-01-20  **Language**: en

> 一个提示，要求制作同一人物的高质量照片拼贴，在 10 种不同的指定发型中保持相同的面部和表情，这对于角色设计或视觉一致性测试非常有用。

![10 种发型照片拼贴提示](https://cms-assets.youmind.com/media/1768977314727_tpzo6p_G_EbAqMXQAAAK7N.jpg)

```
High quality photo collage of the same person, identical face &amp; expression, in 10 hairstyles:
 
{argument name="hairstyle 1" default="long straight"}, 
{argument name="hairstyle 2" default="high ponytail"}, 
{argument name="hairstyle 3" default="messy bun"}, 
pixie cut, 
braided crown, 
soft waves, 
short bob w/ bangs, 
low bun, 
side braid, 
loose curls.
```

[[Face Consistency]] [[Photo Collage]] [[Beauty Editorial]]

---

### 27. 1x3 网格手机动态编辑 JSON 提示

**Author**: [SDT🌿](https://x.com/SDT_side)  **Date**: 2025-12-08  **Language**: ja

> 一个为 Nano Banana Pro 设计的高度详细的 JSON 提示结构，用于生成 1x3 的图像网格。其主要功能是“手机动态编辑”，用户可以上传人物照片和手机屏幕内容，以确保身份一致性并实现特定的姿势，例如看手机、将手机举向前以及跳切。

![1x3 网格手机动态编辑 JSON 提示](https://cms-assets.youmind.com/media/1765438658264_y9ab5y_G7o9xAGbAAApmgM.jpg)

```
{
  "layout": {
    "type": "grid_1x3"
  },

  "global": {
    "edit_type": "phone_motion_edit",

    "source": {
      "mode": "EDIT",
      "reference_images": {
        "first": "base_photo_person_and_environment",
        "second": "screen_content_for_phone"
      },
      "preserve_from_first": {
        "same_person_or_group": true,
        "same_faces": true,
        "same_hairstyles": true,
        "same_outfits": true,
        "same_environment_style": true
      }
    },

    "identity": {
      "keep_identity_consistent": true,
      "expression": "bright_natural_smile"
    },

    "phone": {
      "allowed": true,
      "holding_styles": [
        "one_handed",
        "two_handed",
        "near_chest",
        "near_hip",
        "tilted",
        "sideways",
        "partially_toward_lens"
      ],
      "rules": {
        "each_person_may_hold_one_phone": true,
        "screen_should_be_naturally_visible": true,
        "do_not_force_phone_directly_toward_camera": true
      }
    },

    "screen_replacement": {
      "use_second_reference_image_as_content": true,
      "fit_without_distortion": true,
      "no_ui": true
    },

    "environment": {
      "preserve_environment_style_from_reference": true,
      "lighting_consistent_with_reference": true
    },

    "constraints": {
      "no_new_characters": true,
      "no_costume_change": true,
      "no_change_to_reference_location_type": true
    }
  },

  "panels": [
    {
      "id": "panel_2",
      "role": "phone_view_soft",
      "edit": true,
      "pose": {
        "pose_can_change": true,
        "style_tags": ["looking_at_phone", "face_close", "natural_pose"],
        "focus_on_expressive_hands": true
      }
    },

    {
      "id": "panel_3",
      "role": "phone_forward",
      "edit": true,
      "pose": {
        "pose_can_change": true,
        "style_tags": ["hand_forward", "phone_front_soft", "arm_extended"],
        "focus_on_expressive_hands": true
      },
      "camera_effect": {
        "perspective": "wide_angle",
        "near_objects_appear_large": true
      }
    },

    {
      "id": "panel_4",
      "role": "jump_cut",
      "edit": true,
      "use_preset": "jump_frame"
    }
  ],

  "pose_presets": {
    "jump_frame": {
      "pose": {
        "pose_can_change": true,
        "style_tags": ["jump", "lively", "mid_air"],
        "focus_on_expressive_hands": true
      },
      "camera_effect": {
        "perspective": "wide_angle",
        "allow_view_from_below": true
      }
    }
  }
}
```

[[Face Consistency]] [[Grid Layout]]

---

### 28. Nano Banana Pro 2x2 网格手机屏幕更换 JSON 提示

**Author**: [SDT🌿](https://x.com/SDT_side)  **Date**: 2025-12-08  **Language**: ja

> 这是一个为 Nano Banana Pro 设计的复杂 JSON 提示结构，用于创建一个 2x2 网格图像序列。序列中，一个人正拿着智能手机，手机屏幕上显示的内容被替换为第二张上传的图片。该结构保持了身份一致性，并为每个面板定义了特定的姿势和相机效果。

![Nano Banana Pro 2x2 网格手机屏幕更换 JSON 提示](https://cms-assets.youmind.com/media/1765438666510_p35cdr_G7n_dRsbQAAmEYS.jpg)

```
{
  "layout": {
    "type": "grid_2x2"
  },

  "global": {
    "edit_type": "phone_motion_edit",

    "source": {
      "mode": "EDIT",
      "reference_images": {
        "first": "base_photo_person_and_environment",
        "second": "screen_content_for_phone"
      },
      "preserve_from_first": {
        "same_person_or_group": true,
        "same_faces": true,
        "same_hairstyles": true,
        "same_outfits": true,
        "same_environment_style": true
      }
    },

    "identity": {
      "keep_identity_consistent": true,
      "expression": "bright_natural_smile"
    },

    "phone": {
      "allowed": true,
      "holding_styles": [
        "one_handed",
        "two_handed",
        "near_chest",
        "near_hip",
        "tilted",
        "sideways",
        "partially_toward_lens"
      ],
      "rules": {
        "each_person_may_hold_one_phone": true,
        "screen_should_be_naturally_visible": true,
        "do_not_force_phone_directly_toward_camera": true
      }
    },

    "screen_replacement": {
      "use_second_reference_image_as_content": true,
      "fit_without_distortion": true,
      "no_ui": true
    },

    "environment": {
      "preserve_environment_style_from_reference": true,
      "lighting_consistent_with_reference": true
    },

    "constraints": {
      "no_new_characters": true,
      "no_costume_change": true,
      "no_change_to_reference_location_type": true
    }
  },

  "panels": [
    {
      "id": "panel_1",
      "role": "soft_intro",
      "edit": true,
      "pose": {
        "pose_can_change": true,
        "style_tags": ["walk", "soft_motion", "side_by_side"],
        "focus_on_expressive_hands": true
      }
    },

    {
      "id": "panel_2",
      "role": "phone_view_soft",
      "edit": true,
      "pose": {
        "pose_can_change": true,
        "style_tags": ["looking_at_phone", "face_close", "natural_pose"],
        "focus_on_expressive_hands": true
      }
    },

    {
      "id": "panel_3",
      "role": "phone_forward",
      "edit": true,
      "pose": {
        "pose_can_change": true,
        "style_tags": ["hand_forward", "phone_front_soft", "arm_extended"],
        "focus_on_expressive_hands": true
      },
      "camera_effect": {
        "perspective": "wide_angle",
        "near_objects_appear_large": true
      }
    },

    {
      "id": "panel_4",
      "role": "jump_cut",
      "edit": true,
      "use_preset": "jump_frame"
    }
  ],

  "pose_presets": {
    "jump_frame": {
      "pose": {
        "pose_can_change": true,
        "style_tags": ["jump", "lively", "mid_air"],
        "focus_on_expressive_hands": true
      },
      "camera_effect": {
        "perspective": "wide_angle",
        "allow_view_from_below": true
      }
    }
  }
}
```

[[Face Consistency]] [[Grid Layout]]

---

### 29. 假日优雅肖像，带面部参考

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2025-12-08  **Language**: en

> 一个高度结构化的 JSON 提示词，用于 Gemini Nano Banana Pro，旨在生成一张逼真、优雅的假日肖像（半身照），描绘一位身穿黑色高领毛衣和外套的女性主体，站在一棵装饰好的圣诞树前。至关重要的是，它要求使用上传的图像以实现 100% 的面部准确性和特征保留。

![假日优雅肖像，带面部参考](https://cms-assets.youmind.com/media/1765438645226_bm9igi_G7mu1kta4AA_pd9.jpg)

```
{
  "image_prompt": {
    "face_requirements": {
      "use_reference_face": true,
      "accuracy": "100% identical",
      "preserve_features": [
        "same facial proportions",
        "same eye shape and lashes",
        "same eyebrows structure",
        "same nose shape",
        "same lips and smile",
        "same skin tone and texture"
      ]
    },

    "subject": {
      "gender": "female",
      "description": "A well-dressed woman posing indoors in front of a decorated Christmas tree.",
      "pose": {
        "body": "standing straight with relaxed posture",
        "arms": "hands gently resting together in front without holding anything",
        "head": "slightly tilted toward the camera",
        "expression": "warm, friendly smile"
      },
      "hair": {
        "style": "sleek high ponytail",
        "texture": "smooth, glossy black hair"
      },
      "makeup": {
        "style": "soft glam",
        "details": "defined lashes, shaped brows, natural blush, glossy lips"
      },
      "clothing": {
        "outfit": "black turtleneck sweater and long black coat",
        "accessories": {
          "earrings": "small black star-shaped studs",
          "other_items": "no handbag"
        }
      }
    },

    "background": {
      "setting": "indoor holiday environment",
      "elements": [
        "large Christmas tree decorated with red and gold ornaments",
        "warm fairy lights",
        "gift boxes under the tree",
        "modern interior with soft warm lighting"
      ],
      "atmosphere": "festive, cozy, elegant"
    },

    "lighting": {
      "type": "warm indoor lighting",
      "effects": "soft highlights on the face, gentle shadows",
      "source": "overhead lighting and Christmas tree lights"
    },

    "photography": {
      "style": "realistic portrait",
      "camera_angle": "eye-level",
      "framing": "mid-shot (waist up)",
      "sharpness": "high clarity with natural detail",
      "color_tone": "warm festive palette"
    },

    "aesthetic": {
      "mood": "holiday elegance",
      "keywords": [
        "Christmas vibes",
        "winter indoor portrait",
        "festive lighting",
        "natural skin texture"
      ]
    },

    "output_settings": {
      "aspect_ratio": "3:4",
      "quality": "ultra-high-resolution",
      "negative_prompt": [
        "handbag",
        "distorted face",
        "extra limbs",
        "text",
        "watermarks",
        "logos"
      ]
    }
  }
}
```

[[Face Consistency]] [[Warm Lighting]] [[Christmas Theme]] [[Black Turtleneck]]

---

### 30. 面部一致的摇滚乐队海报

**Author**: [Kris Kashtanova](https://x.com/icreatelife)  **Date**: 2025-11-22  **Language**: en

> 一个英文提示，用于生成一张摇滚乐队海报，其中包含几位参考人物，并保持他们面部特征的一致性，同时添加乐队名称。

![面部一致的摇滚乐队海报](https://cms-assets.youmind.com/media/1763885639610_ebcaun_G6WO0TCXQAAXVBN.jpg)
![面部一致的摇滚乐队海报](https://cms-assets.youmind.com/media/1763885643172_nkrvvb_G6WK0amXwAA0NQd.jpg)

```
make a rock band poster with these people. Keep faces consistent. Add "{argument name="band_name" default="The AI Syndicate"}" name of the band.
```

[[Face Consistency]]

---

### 31. 虚拟服装试穿，含东京街头场景选项

**Author**: [iX | AI Video Creator & Vibe Coder](https://x.com/iX00AI)  **Date**: 2025-11-22  **Language**: en

> 一个多行提示，用于将上传的参考图片中的人物穿上另一张上传图片中的衣服，同时保留面部和发型，让他们摆出可爱的姿势，并以写实风格渲染，可选择中性或东京街头背景。

![虚拟服装试穿，含东京街头场景选项](https://cms-assets.youmind.com/media/1763885908542_4w3o8l_G6UZNI_boAASbOX.jpg)
![虚拟服装试穿，含东京街头场景选项](https://cms-assets.youmind.com/media/1763885911279_ci30iu_G6UZNJBaMAAZ_4g.jpg)
![虚拟服装试穿，含东京街头场景选项](https://cms-assets.youmind.com/media/1763885914157_v6vyac_G6UZNI9aEAAyuPL.jpg)

```
Generate an image of the person from the uploaded reference image, keeping the face and hairstyle exactly as in the uploaded image.
Dress the person in the clothing from the uploaded clothing image, preserving the style, color, and details of the garment.
Pose the person in a cute and natural pose, looking towards the camera.
Realistic photo style, natural lighting, high resolution.
Background optional, neutral or {argument name="background_location" default="Tokyo street"} setting.
```

[[Face Consistency]] [[Costume Transfer]]

---

### 32. 替换服装，同时保持身份和姿势

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2025-11-21  **Language**: en

> 一个详细的编辑提示，在保留用户面部、姿势和环境的同时，将服装更改为与参考连衣裙相匹配。

![替换服装，同时保持身份和姿势](https://cms-assets.youmind.com/media/1763887033975_wjaosj_G6QZeymWsAAO5Fz.jpg)
![替换服装，同时保持身份和姿势](https://cms-assets.youmind.com/media/1763887037307_fb0uko_G6QZeyjWwAABIbR.jpg)

```
Keep my exact face, pose, body, and environment from my original photo.
Change ONLY the clothing and accessories so they match the dress and accessories from the second reference image with full accuracy.
Do not alter my hairstyle, makeup, body proportions, camera angle, or
```

[[Face Consistency]] [[Costume Transfer]] [[Pose Reference]] [[Fashion Editing]]

---

### 33. 老照片修复：打造单反级人像画质

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-04-03  **Language**: en

> 这是一个结构化提示词，旨在将老照片修复为自然、高细节、单反级别的肖像，确保色彩还原准确、清晰度高，并完整保留原图的面部特征。

![老照片修复：打造单反级人像画质](https://cms-assets.youmind.com/media/1775284637569_jrjsom_HE9Oo94awAAfF0n.jpg)
![老照片修复：打造单反级人像画质](https://cms-assets.youmind.com/media/1775284637690_vj2ozb_HE9Oo80b0AAyTID.jpg)

```
{
  "prompt": "Restore old photo into natural DSLR-quality portrait (Canon EOS R6 II level), high detail, accurate colors, sharp clarity, preserve exact facial features",
  "quality": "high",
  "style": "photorealistic"
}
```

[[Face Preservation]] [[Photo Enhancement]] [[Old Photo Restoration]]

---

### 34. Nano Banana Pro（内容创作者工作室）的图像转换提示

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-03-18  **Language**: en

> 一个用于 Google Nano Banana Pro 的提示，指示模型通过将主体置于现代内容创作者工作室环境中、添加专业的播客设备、隔音泡沫和电影级 LED 照明来转换现有图像，同时保留主体的面部。

![Nano Banana Pro（内容创作者工作室）的图像转换提示](https://cms-assets.youmind.com/media/1773902654437_eb5buk_HDuy3wKb0AAGQlp.jpg)
![Nano Banana Pro（内容创作者工作室）的图像转换提示](https://cms-assets.youmind.com/media/1773902654564_ymnw9n_HDuy3wLb0AAB7dv.jpg)

```
Transform this image into a modern content creator studio. Place the subject sitting at a desk with a professional podcast setup, including a mounted microphone arm and studio microphone in front of them. Add acoustic foam panels on the walls for a soundproof studio look. Include colorful LED tube lights (blue and pink tones) in the background for a cinematic YouTube aesthetic. He's wearing a nice jacket with nice apple airpods.Keep the subject’s face realistic and unchanged, with natural skin tones. Add soft, professional lighting on the face (key light + subtle rim light).
Style: high-quality YouTube creator setup, cinematic lighting, vibrant but clean colors, sharp focus, professional studio environment, modern and minimal.
```

[[Face Preservation]] [[Image Transformation]] [[Modern Interior]] [[LED Lighting]]

---

### 35. Nano Banana 2 的 3D Q 版角色转换提示

**Author**: [Kaan](https://x.com/kaanakz)  **Date**: 2026-03-18  **Language**: en

> 一个详细的提示，用于 Nano Banana 2 将参考图像中的主体转换为可爱的 3D 动漫 Q 版角色。该提示强调在应用经典的 Q 版比例、将其渲染为高质量、光泽的 3D 模型，并具有鲜艳的色彩和高级收藏品美感的同时，保留主体的肖像、种族和肤色。

![Nano Banana 2 的 3D Q 版角色转换提示](https://cms-assets.youmind.com/media/1773902663550_hdapcp_HDuBDxWXkAAr5b_.jpg)
![Nano Banana 2 的 3D Q 版角色转换提示](https://cms-assets.youmind.com/media/1773902664337_4ae77o_HDuBDzdWYAE3UeK.jpg)

```
Transform the subjects into a cute anime chibi characters rendered as a clean 3D model, while preserving the subject's original race, ethnicity, skin tone, and recognizable facial likeness, including hairstyle, hair color, and clothing colors. The character must remain clearly the same person with the same skin tone and ethnic appearance as the original input, translated into a chibi form. The character should have classic chibi proportions: a very large head, small torso, simplified cute facial features, and large expressive anime-style eyes. Translate the subject's facial features into a chibi style while keeping their recognizable likeness. Frame the character from the torso up, with the camera slightly closer and cropped in, so the upper body and head fill most of the frame. The character should be looking directly into the camera, with an energetic and expressive anime-style pose. Use a slightly dynamic camera angle, such as a subtle tilt or off-axis perspective, similar to modern anime promotional artwork. The camera can be slightly lower than the character's face, creating a playful upward Tr angle that makes the character feel lively and engaging. Render the character as a high-quality glossy 3D anime-style model, similar to a polished Blender render or premium collectible figure. The materials should be smooth, reflective, and toy-like, with strong highlights, soft reflections, and shiny surfaces. The overall look should clearly resemble a 3D rendered character, not a flat 2D illustration. Use bright anime-style shading with vibrant but polished colors, giving the character a premium anime aesthetic. Place the character in front of a colorful gradient background. Behind the character, include a small number of large, translucent decorative shapes such as bubbles, stars, or rounded forms. These shapes should appear semi-transparent, glossy, and subtle, similar to clear acrylic or glass, softly floating in the background without drawing attention away from the character. The background elements should remain light, minimal, and softly visible, acting as stylish accents rather than prominent objects. The final image should look like a dynamic, glossy 3D chibi character render, with polished materials, vibrant colors, and a premium collectible aesthetic,while clearly maintaining the subject's original race, skin tone, and recognizable identity.
```

[[Face Preservation]] [[3D Rendering]] [[Anime Style]] [[Collectible Figure]]

---

### 36. 奢华时尚人像摄影提示词，适用于 Nano Banana 2

**Author**: [David](https://x.com/tealdog2)  **Date**: 2026-03-18  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana 2 生成一张超写实的女性时尚编辑照片，该女性与参考面部匹配。该提示指定了一套米色和米白色定制服装、详细的配饰（金色珠宝、皮带）、一个特定的姿势（坐在藤制沙发上，手持瓷杯）以及技术相机设置（Canon EOS R5、85mm 镜头、f/1.8、浅景深），以实现具有 Kodak Vision3 50D 胶片效果的奢华美学。

![奢华时尚人像摄影提示词，适用于 Nano Banana 2](https://cms-assets.youmind.com/media/1773902665491_kttmly_HDqieazbEAEK7k3.jpg)

```
{
  "subject": "woman matching reference face, hair styled in a low polished ponytail with volume at the roots and loose baby hairs catching sunlight, wearing a cream and off-white tailored outfit: structured light wool blazer with visible silk lining, ribbed cashmere-silk tank top, high-waisted wide-leg trousers, brown cognac leather belt with large gold buckle, gold chain bracelet, minimalist watch with rose gold case and brown leather strap, gold rings and coin pendant necklace, large round sunglasses with thin gold frame",

  "composition": "seated on a clear wicker sofa outdoors, body slightly leaning forward, right leg crossed over left, right hand holding a thin porcelain cup with gold rim near lips, left hand resting inside pants pocket, direct gaze toward camera through sunglasses, relaxed yet confident posture, upper-body portrait framing",

  "environment": "outdoor patio setting with clear wicker furniture, bright open-air background softly blurred into bokeh, minimal distractions emphasizing subject and textures",

  "lighting_geometry": "intense natural midday sunlight, directional light creating defined shadows and crisp contrast, highlights catching on hair, skin, porcelain cup, and gold accessories, subtle reflections visible on sunglasses",

  "materials_and_texture": "fine wool fibers with visible structure, ribbed knit texture of tank top, smooth porcelain cup with glossy finish and gold edge, polished leather belt, metallic gold jewelry reflections, realistic skin texture with visible pores, soft makeup blending with matte-luminous finish",

  "camera_optics": "Canon EOS R5 full-frame camera, RF 85mm lens at f/1.8, extremely shallow depth of field, creamy bokeh background, sharp focus on eyes visible behind sunglasses and fine material textures",

  "color_strategy": "neutral cream and off-white palette, warm brown leather accents, gold metallic highlights, natural skin tones under bright sunlight with balanced contrast",

  "rendering_intent": "ultra-realistic editorial fashion photography, luxury aesthetic, Kodak Vision3 50D film look with subtle grain, clean and refined image quality, sophisticated and powerful atmosphere",

  "aspect_ratio": "4:5 vertical",

  "negative_prompt": "stylization, illustration, plastic skin, over-smoothed textures, distorted anatomy, exaggerated proportions, low detail, flat lighting, harsh HDR",

  "control": {
    "reference_face": "use attached image for identity consistency"
  }
}
```

[[Face Preservation]] [[Gold Jewelry]]

---

### 37. 油画风格肖像提示词，带参考图

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-17  **Language**: en

> 一个为 Gemini Nano Banana Pro 2.0 设计的详细提示，用于创作一幅充满活力、艺术感十足的微笑人物油画肖像，并使用上传的照片作为面部参考。画风结合了油画、水墨画和水彩纹理，背景为纯米色，并带有动感的飞溅颜料效果。

![油画风格肖像提示词，带参考图](https://cms-assets.youmind.com/media/1773816071502_j146qg_HDovoSQbsAArcf-.jpg)
![油画风格肖像提示词，带参考图](https://cms-assets.youmind.com/media/1773816071772_xd4nho_HDovoR3XkAAlpfM.jpg)

```
Create a vibrant and artistic oil painting of a smiling, beautiful person, using the uploaded photo as a facial reference without altering their features or appearance. The background is pure beige, filled with dynamic and expressive splashes of oil paint in {argument name="splash colors" default="blue, orange, and purple"} that organically spread across the scene. In the foreground, a realistic human hand holds a painter's palette knife as if actively painting the man's sweatshirt sleeve, creating the illusion that the portrait is being painted in that very moment. The visual style combines detailed ink drawings with loose watercolor textures, including paint drips, fine splashes, soft pigment diffusion, watercolor bloom effects, and the natural texture of the paper. The image features strong contrast, an expressive and dynamic artistic look, a clear hand-painted aesthetic, a focused composition, soft lighting, a high level of detail, and a modern illustration style. 9:16 aspect ratio.
```

[[Face Preservation]] [[Mixed Media Art]]

---

### 38. 充满活力的水彩肖像，点缀动感飞溅的颜料

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-17  **Language**: en

> 一个详细的提示，用于生成一张微笑人物的专业水彩画，使用上传的照片作为面部参考。风格结合了细致的墨线艺术和随性的水彩纹理，具有强烈的对比和动态、富有表现力的美感。

![充满活力的水彩肖像，点缀动感飞溅的颜料](https://cms-assets.youmind.com/media/1773816073404_ibb6tx_HDlRudmXYAAFsAh.jpg)
![充满活力的水彩肖像，点缀动感飞溅的颜料](https://cms-assets.youmind.com/media/1773816073471_nx1p34_HDlRud-bEAI7Sx5.jpg)

```
Create a vibrant and artistic watercolor painting of a smiling person, using the uploaded photo as the facial reference without altering their facial features or appearance. The background is clean white, filled with dynamic and expressive watercolor paint splashes in {argument name="splash colors" default="blue, orange, and purple"} spreading organically across the scene. In the foreground, a realistic human hand holds a paintbrush as if actively painting the sleeve of the man's hoodie, creating the illusion that the portrait is being painted at that exact moment. The visual style combines detailed ink line art with loose watercolor textures, including paint drips, fine splatters, soft pigment diffusion, watercolor blooming effects, and natural paper texture. The image features strong contrast, an expressive and dynamic artistic look, a clear hand-painted aesthetic, centered composition, soft lighting, high level of detail, and a modern illustration style. Aspecto vertical 9:16.
```

[[Face Preservation]] [[Mixed Media Art]] [[Ink Line Art]]

---

### 39. 时尚六人肖像拼贴提示

**Author**: [Smiling Khan](https://x.com/AIwithkhan)  **Date**: 2026-03-17  **Language**: en

> 给 Nano Banana 的一个提示：制作一张时尚拼贴画，其中包含同一位女性的六张方形肖像（使用上传的照片作为面部参考），排列成 2x3 的网格。每个画框都展现出不同的表情和姿势，女性穿着相同的服装并戴着反光太阳镜。背景是充满活力的春日美学，有明亮的蓝色天空和五彩斑斓的花朵，旨在呈现 8K 高级时尚杂志风格和现代 Instagram 拼贴美学。

![时尚六人肖像拼贴提示](https://cms-assets.youmind.com/media/1773816078582_k5d9w2_HDklYFWbEAA9sFX.jpg)

```
stylish collage made from six square portraits of the same woman (use the uploaded photo as the face reference), arranged in a clean 2x3 grid. Each frame shows a different expression and pose of the same person: {argument name="expression 1" default="smiling"}, {argument name="expression 2" default="laughing"}, {argument name="expression 3" default="surprised"}, {argument name="expression 4" default="playful wink"}, {argument name="expression 5" default="thoughtful look"}, and {argument name="expression 6" default="confident serious expression"}. The woman wears the same outfit and reflective sunglasses, with wind-blown hair. Bright blue sky and colorful flowers surround the frames, creating a vibrant spring aesthetic. Each panel has slightly different angles and gestures, like reaching toward the camera, tilting the head, or adjusting sunglasses. High-fashion editorial style, ultra-detailed, vibrant colors, soft sunlight, photorealistic, sharp focus, modern Instagram collage aesthetic, 8K.
```

[[Face Preservation]] [[Luxury Fashion Editorial]] [[2x3 Grid Layout]]

---

### 40. Enka CD 封面设计与 Nano Banana 2

**Author**: [なお](https://x.com/Naonekozamurai)  **Date**: 2026-03-16  **Language**: ja

> 为 Nano Banana 2 提供一个详细的提示，用于创建一张演歌（日本传统民谣）风格的 CD 封面，并使用一张人物参考图片。该提示详细说明了设计元素、戏剧性氛围、标题要求（演歌风格、毛笔字体）以及要排除的元素（条形码、徽标等）。

![Enka CD 封面设计与 Nano Banana 2](https://cms-assets.youmind.com/media/1773729536008_9dpnzm_HDkB0VvbEAALDpd.jpg)
![Enka CD 封面设计与 Nano Banana 2](https://cms-assets.youmind.com/media/1773729536000_7f776h_HDkBxkUaoAASriN.jpg)
![Enka CD 封面设计与 Nano Banana 2](https://cms-assets.youmind.com/media/1773729536040_i80rig_HDkBzDqbgAAXacn.jpg)
![Enka CD 封面设计与 Nano Banana 2](https://cms-assets.youmind.com/media/1773729536860_2js86a_HDkB10QaoAA8G_D.jpg)

```
リファレンス画像に写っている人物を同一人物として使用し、その人物がリリースした「演歌のCDジャケット」をデザインしてください。

重要:
・人物の顔や特徴はリファレンス画像から忠実に再現する
・元画像の構図、カメラアングル、ポーズ、背景には縛られない
・新しくCDジャケット用に構図を大胆に再構成する
・実在する演歌CDジャケットのような完成度の高いデザインにする

デザイン要素:
・演歌らしいドラマチックで情緒的な雰囲気
・昭和～現代演歌のCDジャケットのようなデザイン
・人物は中央または印象的な配置
・強い感情表現（哀愁、決意、切なさなど）
・背景は自由に変更してよい。演歌の世界観を表現する情緒的でドラマチックな背景にすること。

タイトル:
・リファレンス画像の人物の雰囲気やキャラクターから推測して
「それらしい演歌のタイトル」を新しく作る
・タイトルは大きくジャケットに表示する
・演歌風の日本語タイトル
・筆文字風フォント

追加要素:
・本物のCDジャケットのようなレイアウト
・高品質、印刷用レベルのクオリティ

スタイル:
日本の演歌CDジャケット
ドラマチックなライティング
映画ポスターのような構図
高解像度
プロのグラフィックデザイン

以下の要素は一切表示しない：
・バーコード
・価格表示
・JANコード
・レコード会社ロゴ
・CDレーベルロゴ
・コピーライト表記
・発売日
・型番
・商品番号
・キャンペーンシール
・ステッカー
・宣伝バッジ
・帯（オビ）
・販売用ラベル
・ストリーミングサービスのロゴ
・Spotify / Apple Music などのアイコン
・QRコード

文字情報は「演歌タイトル」と「歌手名」のみ表示すること。「サブタイトル」は表示してもよい。
それ以外の文字・記号・数字は一切表示しない。
商業CDパッケージに見られる販売情報はすべて禁止。
```

[[Face Preservation]]

---

### 41. 船上的超写实肖像

**Author**: [Chryz leen](https://x.com/Chryzleenprompt)  **Date**: 2026-03-16  **Language**: en

> 一个为 Gemini Nano Banana 设计的详细、超现实摄影提示，其中指定了相机设置（Sony A7R V, 85mm f/1.8）、构图（9:16 宽高比，坐在船甲板上的拍摄对象）、身体描述、服装、灯光和背景（海洋和岛屿），同时要求与参考图像高度相似。

![船上的超写实肖像](https://cms-assets.youmind.com/media/1773729517358_9odcmw_HDh0_1VbcAAoJxa.jpg)

```
Create image: Use the attached reference image as a visual guide for the character’s appearance, maintaining strong resemblance to the person in the reference. Preserve key visual traits such as facial structure and overall proportions, while allowing small natural variations typical of real photography. The generated subject should clearly resemble the reference while remaining a natural photographic interpretation.
Aspect Ratio: 9:16.
A hyper-realistic, ultra-realistic photograph shot on a Sony A7R V with an 85mm f/1.8 lens, settings at ISO 100, shutter speed 1/500s, aperture f/2.8, capturing an upper-body to medium-long shot with a moderately shallow depth of field creating a pleasing bokeh effect. The aspect ratio is 9:16. The camera angle is slightly downward, positioned at eye-level with the seated subject. The subject, possessing a slender and graceful build with smooth, light-medium warm-toned skin displaying realistic texture, reclines on the white deck of a boat. The subject is angled approximately 20 degrees towards the camera's right. The subject's left arm is extended and gently rests on the boat's edge, supporting the upper body, fingers relaxed. The right arm is bent at the elbow, with the hand resting on the raised right knee. The left leg is extended across the boat's surface, while the right leg is bent at the knee, creating a relaxed posture. The gaze is directed straight at the camera with a calm, composed, and captivating expression, head held level. The dark brown hair is long, straight, parted slightly off-center, and cascades over the subject's left shoulder and partially down the back, with a few strands softly wind-blown around the face. The subject wears a form-fitting, black midi-length halter-neck dress made of a soft, stretchy knit fabric, featuring a high slit on the left side that exposes the upper thigh. A delicate silver pendant necklace with a small circular charm rests at the base of the subject's throat. The subject's facial style includes defined, natural-looking eyebrows, subtle eyeshadow, thin eyeliner, mascara, and soft pink lips with a hint of gloss, complemented by natural-looking foundation. The lighting is bright, natural daylight, coming from above and slightly in front, creating soft highlights on the skin and dress, with minimal, gentle shadows that sculpt the form. The color grading is vibrant and natural, with rich blue tones in the water and sky, and lush greens on the distant islands. The overall mood is tranquil, glamorous, and natural. The background features an expansive, clear blue ocean with subtle ripples and distant green, lush islands under a clear blue sky, rendered with a soft bokeh. The foreground includes the crisp white deck of the boat with hints of its structure and railings. The image has a clean, crisp, and hyper-photorealistic finish, absent of any film grain or digital noise.
```

[[Face Preservation]] [[Natural Light Photography]] [[9:16 Aspect Ratio]] [[Ocean Background]]

---

### 42. 专业照片修复与画质提升

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-03-16  **Language**: en

> 一个给 nano-banana-pro 的提示，用于使用先进的放大算法将旧照片修复成专业的、高质量肖像，确保自然的效果并保留精确的面部特征。

![专业照片修复与画质提升](https://cms-assets.youmind.com/media/1773729514440_zw75mb_HDfqanlaMAEF_AL.jpg)
![专业照片修复与画质提升](https://cms-assets.youmind.com/media/1773729514648_233qcx_HDfqausaIAARpKK.jpg)

```
Restore this old photo into professional portrait of DLSR - quality colour and detail, using an advanced upscaling algorithm comparable to the results from canon EOS R6 II. Ensure the restored the image looks natural, retains exact facial features, has great clarity......
```

[[Face Preservation]] [[Photo Restoration]] [[Old Photo Enhancement]] [[Historical Photo Restoration]]

---

### 43. 手持鲜花自拍

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-15  **Language**: en

> 一个针对 Gemini Nano Banana Pro 2.0 的高度具体提示，使用“PersonaFusion-vX.03 协议”生成一张超现实、清晰的智能手机自拍，画面中人物手持鲜花，要求面部特征与参考图像完全一致，并着重强调数字清晰度和 HDR 光照。

![手持鲜花自拍](https://cms-assets.youmind.com/media/1773643978107_l2ghvn_HDd-0HobcAAbhps.jpg)

```
Initiate PersonaFusion-vX.03 protocol: Use the exact facial identity taken from the attached reference image (or from the user's provided face) with zero alteration.
A hyper-realistic, ultra-sharp photograph taken on a modern smartphone, characterized by its digital clarity, like a Google Pixel 8. The image captures a low-angle perspective looking up through a vibrant canopy of large, colorful flowers, mostly seen from their undersides with visible petals and stems in shades of {argument name="flower colors" default="pink, orange, red, and yellow"}, framing the scene and the subject. A person with long, dark, wavy hair, appearing modern and well-maintained with a slight wind-blown effect, smiles broadly with their head tilted back, looking upwards. Their right arm is extended towards the camera, adorned with a thin gold-toned bracelet. They wear light wash denim overalls over a white sleeveless top, and carry a woven shoulder bag featuring a cheerful beaded pattern of orange fruit and green leaves. Their natural makeup highlights dewy, creamy skin. A bright, clear blue sky is visible in the gaps between the flowers, with the sun positioned behind the subject's head, creating a gentle sunburst effect. Shadows are noticeably lifted, indicating bright and even illumination typical of modern smartphone HDR. The entire scene is rendered with absolute sharp focus, devoid of any background blur or bokeh, showcasing realistic digital textures.
Details are incredibly sharp, revealing subtle textures in the clothing and realistic skin with visible pores, without any film grain, though a subtle digital noise is present, characteristic of a high-resolution smartphone image. Vertical portrait.
```

[[Face Preservation]] [[Photorealistic Portrait]]

---

### 44. 浪漫情侣镜中自拍吻

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-15  **Language**: en

> 一个用于 Nano Banana 2 和 Pro 的提示，生成一张超逼真的印度情侣浪漫镜面自拍，要求精确保留之前参考图片中的面部、服装、背景和手机壳，只改变姿势。

![浪漫情侣镜中自拍吻](https://cms-assets.youmind.com/media/1773643979660_swzsyc_HDd4Htyb0AAHm8m.jpg)

```
Ultra-realistic romantic mirror selfie of same Indian couple, use reference faces exactly.
Couple face to face, gently kissing on lips.
Boy holding phone in same position, phone visible.
Same clothes, same background, same phone cover as previous image.
Only pose changed.
Soft studio lighting, natural skin tones, DSLR, cinematic, ultra-realistic.full length photo pls
```

[[Face Preservation]] [[Photorealistic Portrait]]

---

### 45. 老照片修复与增强

**Author**: [simeon-sanai](https://x.com/Naiknelofar788)  **Date**: 2026-03-15  **Language**: en

> 这是一个针对 Nano Banana 2 的提示，旨在修复和增强旧照片。它指示模型去除照片损坏，改善光照和对比度，添加现代高质量色调，并提高分辨率，同时保留拍摄对象的身份和历史服饰。

![老照片修复与增强](https://cms-assets.youmind.com/media/1773643974285_62s8a5_HDdhROFbwAEuGzo.jpg)
![老照片修复与增强](https://cms-assets.youmind.com/media/1773643974287_4al5ek_HDdhRPybAAAgSVd.jpg)

```
Restore this old photo and enhance it with modern, high-quality color tones similar to today's professional cameras.
Add natural, vibrant, balanced colors with realistic skin tones and clean highlights.
Improve lighting, contrast, and depth to match modern
DSLR/mirrorless camera output.
Remove all scratches, noise, blur, and fading.
Preserve the person's identity, facial features, expression, and historical clothing while giving the photo a fresh, newly-captured look.
Increase resolution to 4K..
```

[[Face Preservation]] [[Photo Restoration]] [[Old Photo Enhancement]] [[Historical Photo Restoration]]

---

### 46. 东亚女孩老照片修复

**Author**: [Noor 🌸](https://x.com/Noor_ul_ain43)  **Date**: 2026-03-13  **Language**: en

> 一个专门用于将老式照片修复至高分辨率专业品质的提示。它描述了场景（一位身穿淡黄色连衣裙的年轻东亚女孩，身处一间带有文化壁画的室内房间）、光线（柔和自然），以及所需的输出（清晰的细节、鲜艳的色彩、去除与年代相关的损坏）。

![东亚女孩老照片修复](https://cms-assets.youmind.com/media/1773469784611_i5npts_HDU356ybUAAV7x0.jpg)
![东亚女孩老照片修复](https://cms-assets.youmind.com/media/1773469784668_uh0sht_HDU356ubkAA03gm.jpg)

```
A high-resolution, professional restoration of a vintage photograph. A young East Asian girl with short, dark hair stands in the center wearing a simple, pale yellow sleeveless cotton dress. The setting is an indoor room with polished light-wood flooring. In the background, a large mural depicts people in traditional cultural attire. To the right, a small wooden table is draped with a patterned fringe cloth. The lighting is soft and natural, with sharp facial details, clean textures, and vibrant, realistic colors that remove all age-related damage, scratches, and fading."
```

[[Face Preservation]] [[Photo Restoration]] [[Old Photo Enhancement]] [[Historical Photo Restoration]]

---

### 47. 老照片修复

**Author**: [workflow ai tools](https://x.com/workflowaitools)  **Date**: 2026-03-13  **Language**: en

> 一个通用提示，用于将饱经岁月、破损的纪念品转换为超清晰、DSLR（数码单反相机）质量的数字传家宝，暗示这是一项照片修复任务。

![老照片修复](https://cms-assets.youmind.com/media/1773469789555_gdujyz_HDTnGTLbMAArE5f.jpg)
![老照片修复](https://cms-assets.youmind.com/media/1773469789816_vx2z6x_HDTnGTcbsAA3wgW.jpg)

```
Convert your age-worn, damaged keepsakes into ultra-sharp, DSLR-quality digital heirlooms.
```

[[Face Preservation]] [[Photo Restoration]] [[Old Photo Enhancement]] [[Historical Photo Restoration]]

---

### 48. 超逼真生日剪贴簿拼贴画

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-15  **Language**: en

> 一个提示，用于创建高分辨率、照片级的数字剪贴簿拼贴画，其中包含一位身穿红色波点连衣裙的女性（身份通过上传照片锁定）的五张照片，照片以宝丽来相框、花卉边框和剪贴簿贴纸排列，强调欢快、怀旧的情绪。

![超逼真生日剪贴簿拼贴画](https://cms-assets.youmind.com/media/1773643995134_detagf_HDbAEzeaMAI-3B9.jpg)

```
Use the uploaded photo as the ONLY facial reference. Face must remain identical to reference. A high-resolution, photorealistic digital scrapbook collage featuring five photos of a woman with long wavy dark hair wearing a red sleeveless sweetheart-neckline dress with white polka dots. Center a square portrait, surrounded by four tilted Polaroid-style photos showing her in various poses. Use soft, warm natural lighting against light gray backgrounds within the photos. Elegant bold red cursive text reading "{argument name="text" default="HAPPY BIRTHDAY"}" on The top of the collage. Set the layout on a white grid paper background framed by pastel pink and green floral borders. Add sticker-like scrapbook decorations: pink paper tape, pink ribbon bows, red and pink hearts, hand-drawn black arrows, butterflies, and small stars. Create a cheerful, nostalgic, and romantic mood with sharp fabric textures and highly detailed features, vertical portrait, 4K quality.
```

[[Face Preservation]] [[Nostalgic Mood]]

---

### 49. 暖色调录音棚中的写实肖像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-03-15  **Language**: en

> 一个给 Nano Banana Pro 的详细提示，用于生成一张照片级写实图像：一个留着长卷发的人，坐在一张木桌旁，身处一个温暖的录音室中，保持与参考图像完全一致的面部特征，并着重表现柔和、舒适的灯光。

![暖色调录音棚中的写实肖像](https://cms-assets.youmind.com/media/1773644001899_7aer5z_HDabN46aMAIeQYR.jpg)

```
A person seated at a wooden table with long wavy hair (no hat), with an empty hand near a studio microphone. Preserve exact facial identity from the reference. Photorealistic skin texture. Expression: Calm and focused, making direct eye contact with the camera, with a slightly relaxed mouth. Outfit: Black oversized T-shirt and black slim-fit pants. Action: Sitting and leaning slightly forward, one hand resting empty near the studio microphone (no phone), the other resting near a dark glass on the tabletop. Environment: Warm recording studio with dark curtains, wooden shelving with plants, a wall clock, and a wooden table. Lighting: Soft, warm studio lighting with natural shadows and a cozy atmosphere. Art Style: High-resolution photorealism matching the original studio look. Details: Retain original composition, camera angle, studio microphone, chair, and background props.
```

[[Face Preservation]] [[Photorealistic Portrait]]

---

### 50. 带参考图像保真度的风格化都市肖像提示

**Author**: [Saul Goodman](https://x.com/Goodmanprotocol)  **Date**: 2026-03-14  **Language**: en

> 一个给 Gemini Nano Banana 2 的详细提示，要求绘制一张风格化的低角度胸部以上城市肖像，强调严格使用参考图像来确定主体的面部和身份，同时将风格转换为大胆的图形数字插画。

![带参考图像保真度的风格化都市肖像提示](https://cms-assets.youmind.com/media/1773556637820_jf2hf2_HDaPBkMaEAA4vNA.jpg)
![带参考图像保真度的风格化都市肖像提示](https://cms-assets.youmind.com/media/1773556637750_mbq060_HDaPBiEaMAAivcr.jpg)

```
Use the provided reference image strictly for the subject’s face and identity. Only translate the face into the new illustration style while maintaining accurate facial features.
Create a stylized low-angle chest-up urban portrait. The subject’s head is slightly raised, giving a confident, street-inspired attitude.
Appearance & StylingOrange-tinted sunglasses
Gold chain necklace
Patterned orange streetwear jacket
Prominent neck and face tattoos
Art Style

Bold graphic digital illustration style with sharp shading, clean edges, and strong contrast, similar to a modern urban poster or street-art inspired artwork.
Background

A large, orange-filled circle, made with brush strokes, is placed behind the subject, with grunge paint splashes on a dark grey, textured background, creating a strong graphic composition.
Lighting & Mood

Warm reflections on the sunglasses and skin tones, high-contrast poster lighting, dramatic urban aesthetic, crisp illustration details, 4:5 aspect ratio.
Maintain strong facial identity fidelity from the reference image while changing only the artistic style of the portrait.
```

[[Face Preservation]] [[Urban Background]]

---

### 51. 时尚专题：巨型高跟鞋上的女人

**Author**: [Diamond](https://x.com/DiamondZPetSpa)  **Date**: 2026-02-26  **Language**: en

> 生成一张时尚杂志风格图片的提示词：一位女性优雅地坐在巨大的高跟鞋边缘，画面聚焦于奢华时尚摄影美学，柔和的漫射光，并严格保留上传女性的面部结构。

![时尚专题：巨型高跟鞋上的女人](https://cms-assets.youmind.com/media/1772174112758_pfw0yp_HCEWJQHaMAEe68w.jpg)
![时尚专题：巨型高跟鞋上的女人](https://cms-assets.youmind.com/media/1772174112848_qlspb7_HCEWK3CaMAAIlJC.jpg)

```
Produce a fashion-editorial style studio image of the uploaded woman sitting elegantly on the edge of a giant high-heel shoe. The shoe features detailed leather texture and realistic stitching. Clean white background, soft diffused lighting, luxury fashion photography look. Do not modify facial structure.
```

[[Face Preservation]] [[Soft Diffused Light]] [[Surreal Fashion Photography]]

---

### 52. 老照片修复至数码单反相机 (DSLR) 质量提示（截断）

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-02-26  **Language**: en

> 一个用于将旧照片修复为专业级高清人像的提示片段，要求达到数码单反相机 (DSLR) 质量，并侧重于使用高级放大算法保留精确的面部特征和清晰度。

![老照片修复至数码单反相机 (DSLR) 质量提示（截断）](https://cms-assets.youmind.com/media/1772174114033_1h1mp3_HCDTBZ1XUAA85wE.jpg)
![老照片修复至数码单反相机 (DSLR) 质量提示（截断）](https://cms-assets.youmind.com/media/1772174114085_1foemv_HCDTBaIW4AAkazn.jpg)

```
"Restore this old photo into professional portrait of DLSR - quality colour and detail, using an advanced upscaling algorithm comparable to the results from canon EOS R6 II. Ensure the restored the image looks natural, retains exact facial features, has great clarity......"
```

[[Face Preservation]] [[Photo Restoration]] [[Image Upscaling]]

---

### 53. 人像修图：面部修复与黄金时段光线

**Author**: [degen_dev - d/acc](https://x.com/__degen_dev__)  **Date**: 2026-02-24  **Language**: en

> 一个简单的提示，指示 AI 编辑一张美丽女性的照片，重点是应用强烈的黄金时段定向光照以创建清晰的阴影，同时严格保留主体的面部。

![人像修图：面部修复与黄金时段光线](https://cms-assets.youmind.com/media/1772001503310_kokg9a_HB9VMK3W4AA3Qbj.jpg)

```
Edit this photo without changing the face a beautiful woman with fair skin lit by bright morning sunlight from a strong golden directional light source creating clear shadows on her face and hair
```

[[Face Preservation]]

---

### 54. 极简主义黑白时尚三联画

**Author**: [کٲشُر](https://x.com/RealDreamer01)  **Date**: 2026-02-24  **Language**: en

> 一个用于生成极简主义单色时尚专题三联画的提示，要求保留参考图像中模特的脸部、比例和外部特征。输出应包含三幅堆叠的电影风格画面，描绘一位留着深色短发的年轻男子。

![极简主义黑白时尚三联画](https://cms-assets.youmind.com/media/1772001536141_1hwb4a_HB6BVtKb0AIMUQ8.jpg)

```
Preserve the face, proportions, and external features of the model as in the reference. A minimalist monochrome fashion editorial triptych featuring three stacked cinematic frames. The subject is a young man with short dark hair and a
```

[[Face Preservation]] [[Clean Composition]]

---

### 55. 锦鲤池塘上方电影般的漂浮镜头

**Author**: [Dr. Samia](https://x.com/oye_samia)  **Date**: 2026-02-23  **Language**: en

> 一个高度详细的提示，用于生成一张电影般的高分辨率俯视照片：一名女子平静地仰卧漂浮在黑暗的天然池塘中，周围环绕着锦鲤和睡莲，强调忧郁的艺术美学，并要求面部与参考图像保持一致。

```
Create a high-resolution, cinematic overhead photograph of a 24 year old woman floating calmly on her back in a dark, natural pond. The camera angle is a perfect top-down (90-degree overhead) view, centered composition.
The woman is an adult female with medium build, light-to-medium skin tone, short neatly styled black hair. expression relaxed and serene, eyes hidden behind the glasses.
She is dressed in a black shirt, fully soaked and clinging naturally to the body, full body covered.  On her right wrist, she is wearing a black wristwatch with a minimal design.
Her arms are spread loosely outward, palms relaxed, body floating naturally with gentle ripples forming around him. The water is deep charcoal to black in color, with subtle reflections and soft circular ripples radiating from her body.
Surrounding her in the water are seven koi fish, swimming calmly. The koi are orange and white, with natural pattern variations, positioned at different distances around the body, creating a balanced, aesthetic composition. Their movement appears slow and peaceful.
Floating on the surface are large green lily pads, some partially submerged, with visible natural textures and veins. In the upper left area, two white lotus flowers with yellow centers bloom gracefully above the water, adding contrast and softness to the dark pond.
Lighting is soft, diffused natural light, no harsh shadows, giving a moody, fine-art feel. Colors are muted and elegant, with strong contrast between the dark water and the white clothing. The overall mood is calm, surreal, luxurious, and editorial, resembling a high-end fashion or conceptual fine-art photograph.
Ultra-sharp focus, realistic water physics, natural skin texture, high dynamic range, professional photography quality.
Keep the face exact same. (Use the attached image)
```

[[Face Preservation]]

---

### 56. 旧照片修复至单反相机画质

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-02-11  **Language**: en

> 一个用于图像修复的提示，指示 AI 将旧照片转换为专业级的数码单反相机质量肖像，并增强色彩和细节，效果可与 Canon EOS R6 II 相媲美。它强调保留精确的面部特征并实现自然的清晰度。

![旧照片修复至单反相机画质](https://cms-assets.youmind.com/media/1770878345359_2xsndl_HA3Ymu9bUAA5AWE.jpg)
![旧照片修复至单反相机画质](https://cms-assets.youmind.com/media/1770878345345_0868oh_HA3YnCEbYAAUmEp.jpg)

```
"Restore this old photo into professional portrait of DLSR - quality colour and detail, using an advanced upscaling algorithm comparable to the results from canon EOS R6 II. Ensure the restored the image looks natural, retains exact facial features, has great clarity......"
```

[[Face Preservation]] [[Photo Restoration]] [[DSLR Quality Enhancement]]

---

### 57. 专业单反相机画质的老照片修复提示词

**Author**: [半吊子程序猿大铭](https://x.com/CoderDaMing)  **Date**: 2026-02-07  **Language**: zh

> 这是一个专为 Gemini 上的 Nano Banana Pro 模型设计的提示，指示 AI 将旧照片修复到专业级数码单反相机（DSLR）的质量水平，重点是增强色彩、细节和自然外观，同时使用相当于 Canon EOS R6 II 的高级放大算法。

![专业单反相机画质的老照片修复提示词](https://cms-assets.youmind.com/media/1770532843410_kbvxvx_HAioOARasAAX1bU.jpg)
![专业单反相机画质的老照片修复提示词](https://cms-assets.youmind.com/media/1770532843536_v9rh3r_HAioOLwacAEHjnT.jpg)

```
将这张老照片还原成专业单反相机级别的人像 - 色彩和细节质量更好，使用与佳能EOS R6 II相当的先进放大算法。确保还原的图像看起来自然，保留精确的面部特征，清晰度高......
```

[[Face Preservation]] [[Old Photo Restoration]] [[DSLR Quality Enhancement]] [[Photo Upscaling]]

---

### 58. 超逼真热带风情编辑，带面部保留提示词

**Author**: [Sienna](https://x.com/siennalovesai)  **Date**: 2025-12-20  **Language**: en

> 一个高度详细的 JSON 提示，用于图像编辑，专门设计用于将主体的身体、服装和环境转换为高级热带美学，同时以最高精度保持参考图像中的面部特征。它指定了超现实渲染、热带光线（黄金时段）以及详细的服装和发型（编有兰花的辫子）。

![超逼真热带风情编辑，带面部保留提示词](https://cms-assets.youmind.com/media/1766385960188_6v52wo_G8pFN-KW8AAk0Um.jpg)

```
{
  "model": "image_editing_pro",
  "task": "hyper_realistic_face_preserved_edit",
  "core_intent": "Transform body, outfit, and environment into a premium tropical aesthetic while maintaining the reference face with absolute accuracy and zero identity drift.",
  "reference_handling": {
    "source_face": "attached_image",
    "face_lock": true,
    "identity_protection_level": "maximum",
    "allowed_changes": "none_on_face"
  },
  "subject_design": {
    "appearance": "{argument name="appearance" default="young woman with fair natural skin and long Korean-inspired wavy hair in a soft brown-blonde shade, styled into a loose, thick braid"}",
    "hair_details": "{argument name="hair details" default="braid decorated with a large light-purple orchid clip and delicate white flowers subtly woven throughout for an elegant tropical touch"}"
  },
  "wardrobe_styling": {
    "top": "{argument name="top description" default="plunging v-neck top in satin with delicate embroidery, highlighting graceful curves"}",
    "bottom": "{argument name="bottom description" default="flowing pants with side slits, in shimmering fabric for a captivating movement"}",
    "arm_accessories": "layered thin bangles that jingle softly, adding to the enchanting vibe"
  },
  "pose_and_expression": {
    "body_language": "side profile turn with a glance over shoulder, radiating sultry confidence",
    "facial_expression": "subtle pout with smoldering gaze, preserving the reference's emotional core"
  },
  "environment": {
    "location": "palm-shaded tropical pathway",
    "background_elements": "overhanging leaves and distant ocean glimpses, creating a private escape",
    "sky": "golden hour with warm ambers and soft shadows, enhancing intimacy"
  },
  "lighting_design": {
    "type": "authentic tropical sunlight",
    "characteristics": "realistic highlights, dynamic yet soft shadows, accurate skin reflections without artificial glow",
    "contrast_balance": "natural high contrast with smooth tonal transitions"
  },
  "visual_style": {
    "rendering": "ultra-hyperrealistic",
    "skin_texture": "true-to-life, visible fine details without filters",
    "color_theme": "warm ambers, greens, shimmers, and inviting tones",
    "overall_mood": "romantic, tropical, premium, sultry and elegant"
  },
  "camera_setup": {
    "lens": "85mm portrait",
    "angle": "eye-level",
    "depth_of_field": "shallow with creamy background blur",
    "composition": "large foreground subject dominance"
  },
  "technical_specs": {
    "resolution": "8K",
    "detail_level": "extreme fine detail",
    "quality": "maximum realism",
    "aspect_ratio": "3:2"
  },
  "restrictions": {
    "face_editing": "strictly forbidden",
    "beauty_filters": "disabled",
    "ai_face_reconstruction": "not_allowed"
  },
  "final_goal": "Create a visually striking tropical portrait where the reference face remains 100% unchanged, while the body styling and environment deliver a high-end, editorial-quality transformation.",
  "signature": "@siennalovesai"
}
```

[[Face Preservation]] [[Golden Hour Light]] [[Image Editing]] [[Hyperrealistic Rendering]]

---

### 59. 面部参考和眼镜特写肖像

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2025-12-11  **Language**: en

> 一个简单直接的提示，用于生成一张严格遵循所提供面部参考图像的特写肖像，同时添加特定配饰（圆形黑框眼镜）和场景细节（温暖的室内餐厅灯光、稻草天花板装饰），并保持自然的皮肤纹理。

![面部参考和眼镜特写肖像](https://cms-assets.youmind.com/media/1765967721088_6p0yca_G733nSsaMAQc7-o.jpg)

```
Close up portrait using my facial reference image. Keep my face exactly as in the reference. Do not alter facial structure, eyes, nose, mustache, or skin texture. Add round black glasses, warm indoor restaurant lighting, soft diffused shadows, straw ceiling decor, candid expression, natural skin texture. Use 1:1 aspect ratio.
```

[[Face Preservation]] [[Close-Up Portrait]]

---

### 60. iPad 屏幕上倒映着飞机客舱内的超逼真肖像

**Author**: [Web3菜菜子| bird🕊](https://x.com/jiucaicai250131)  **Date**: 2025-12-11  **Language**: zh

> 一个高度详细、超现实的提示，旨在生成一张完美无瑕皮肤的女性倒映在飞机小桌板上的 iPad 屏幕上的图像。该提示细致地描述了场景（商务舱客舱）、女性的外貌（服装、发型、妆容、姿势）以及构图（iPad 界面可见、柔和的灯光、9:16 垂直比例）。它特别要求不对脸部进行任何改动。

![iPad 屏幕上倒映着飞机客舱内的超逼真肖像](https://cms-assets.youmind.com/media/1765991046890_nbhr1w_G73VfrTaMAQffk7.jpg)

```
这是一幅高度写实、构图紧凑的画面，展现了一位肤色白皙、肌肤完美无瑕的女子映照在飞机折叠餐桌上的iPad屏幕上，一副太阳镜作为点缀置于前景。iPad周围是米灰色的机舱座椅。iPad屏幕上，女子半斜倚在座椅上，左手托着下巴，手指轻触太阳穴，姿态放松。右手拿着{argument name="手机型号" default="iPhone 16 Pro Max"}拍照，部分脸部出现在平板电脑屏幕上。她神情柔和，目光微微向下，给人一种梦幻而宁静的感觉。

她穿着一件{argument name="上衣颜色" default="米色"}超大号连帽衫，面料厚实柔软，帽子拉到头上。手腕上戴着简约的银色戒指，指甲是法式美甲。她的头发是{argument name="发色" default="深棕色"}，带有淡淡的挑染，长直发，层次分明，蓬松饱满，中分刘海轻柔地遮住额头，修饰脸型。她的肌肤白皙透亮，无瑕疵，化着精致的韩式淡妆。双颊泛着淡淡的腮红，嘴唇涂着水润的玫瑰粉色唇膏，眼线纤细，睫毛卷翘。

透过倒影可以看到，画面中的环境简约而充满活力：一架高级/商务舱飞机的客舱内部。宽大的舷窗映照出窗外柔和的蓝色天空光线。iPad 的相机界面——快门按钮、小图标和程序坞——清晰地显示在屏幕上。

柔和温暖的粉彩色调。采用“韩式柔光”风格编辑。9:16 竖屏比例，高清，高品质。 **请勿更改人脸。
```

[[Face Preservation]]

---

### 61. 海贼王恶魔果实变身模板

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-11  **Language**: en

> 这是一个为 Nano Banana Pro 设计的复杂、结构化的提示模板，旨在将真实人物的照片转化为逼真的《海贼王》恶魔果实能力者。该提示要求用户输入恶魔果实名称，并详细说明 AI 应如何以动态、真人风格解释和应用该能力（例如，火焰、冰、伸长的肢体），同时严格保留主体的面部和背景。

![海贼王恶魔果实变身模板](https://cms-assets.youmind.com/media/1765967743852_zgvjw7_G73CEAja8AA6zsg.jpg)
![海贼王恶魔果实变身模板](https://cms-assets.youmind.com/media/1765967744196_t3swpz_G73CD_iaMAMXIVp.jpg)
![海贼王恶魔果实变身模板](https://cms-assets.youmind.com/media/1765967744576_avo7m9_G73CEBXaMAQJjup.jpg)

```
{
  "version": "1.0",
  "description": "Transform a real person in a photo into a One Piece-style Devil Fruit ability user: dynamic pose, dramatic camera angle, ability-specific SFX, and a photorealistic manifestation of the specified Devil Fruit’s power.",
  "variables": {
    "DEVIL_FRUIT_NAME": {
      "type": "string",
      "value": "<<DEVIL FRUIT NAME>>",
      "description": "The canonical Devil Fruit name whose ability should be interpreted and applied to the subject (e.g., Gum-Gum Fruit, Flame-Flame Fruit, Ice-Ice Fruit, Sand-Sand Fruit, Rumble-Rumble Fruit, Flower-Flower Fruit, Dark-Dark Fruit, Paw-Paw Fruit, etc.)."
    }
  },
  "steps": [
    {
      "name": "DEVIL_FRUIT_ABILITY_EDIT",
      "goal": "Apply a dynamic One Piece-style pose, dramatic camera angle, ability-specific manga SFX, and a photorealistic manifestation of the specified Devil Fruit’s ability.",
      "instructions": "Use the uploaded photo as the base.\n\nKeep the person photorealistic (eyes, face, skin texture, hair, makeup). Do NOT convert the scene into manga. Do NOT replace the background.\n\n=====================================\nDEVIL FRUIT ABILITY TRANSFORMATION\n=====================================\nInsert your Devil Fruit name here: {argument name="Devil Fruit Name" default="[DEVIL_FRUIT_NAME]"}\n\nInterpret the canon ability of [DEVIL_FRUIT_NAME] realistically and apply it to the body or surrounding environment. The effect must look like a live-action One Piece movie.\n\nExamples:\n- Gum-Gum Fruit: stretched limbs, elastic skin, tension folds, rubber reflection\n- Flame-Flame Fruit: realistic flames, heat distortion, warm illumination\n- Ice-Ice Fruit: frost buildup, ice crystals, cold vapor\n- Rumble-Rumble Fruit: lightning arcs, photoreal sparks\n- Sand-Sand Fruit: sand disintegration, sandstorm motion\n- Flower-Flower Fruit: photoreal arms blooming from surfaces\n- Paw-Paw Fruit: shockwave compression ripples\n- Dark-Dark Fruit: gravitational distortion, dark smoke tendrils\n\nRules:\n- The face must remain recognizable.\n- Effects must integrate into real lighting and shadows.\n- No cartoon filters — supernatural physics must look real.\n\n=====================================\nONE PIECE-STYLE POSE TRANSFORMATION\n=====================================\nRepose the body into a dramatic battle pose:\n- wide stance, strong dynamic gestures\n- stretched arm for Gum-Gum, open palm for shockwave, ignition stance for flame, elemental charge-up for logias, etc.\n- clothing should deform."
```

[[Face Preservation]] [[Anime Style]]

---

### 62. 温馨圣诞市集人像，保留身份信息

**Author**: [Crediva AI](https://x.com/credivaIO)  **Date**: 2025-12-10  **Language**: en

> 一个高度结构化的 JSON 提示，专为 Google Nano Banana Pro 设计，旨在生成一张在圣诞市集背景下，超现实、电影级的肖像照。该提示明确要求保留主体在参考图像中的面部特征，同时添加节日元素，如红色冬大衣、飘落的雪花和温暖的市集灯光。

![温馨圣诞市集人像，保留身份信息](https://cms-assets.youmind.com/media/1765509738773_r9n8o1_G72JQMiXIAAhkrG.jpg)

```
{
  "prompt": {
    "scene": "Cinematic front-facing Christmas market portrait captured outdoors at night with softly falling snow.",
    "subject": {
      "identity": "Preserve all facial features exactly as in uploaded image",
      "pose": "Standing upright, centered in frame, facing the camera directly",
      "attire": {
        "outerwear": "{argument name="coat color" default="Red"} winter coat, cozy and fitted, with visible texture",
        "accessories": ["Matching scarf optional", "Gloves optional"]
      },
      "hair": "Natural hair with snowflakes gently resting on strands",
      "expression": "Neutral, relaxed, softly smiling or calm"
    },
    "environment": {
      "weather": "Soft snow falling, snow accumulating lightly on coat and hair",
      "lighting": "Warm ambient Christmas market lights, softly illuminating subject and background",
      "background_elements": [
        "Decorated Christmas tree with glowing ornaments",
        "Bokeh of market stalls and festive lights",
        "Softly blurred pedestrians or distant decorations"
      ]
    },
    "camera": {
      "angle": "Front-facing, eye-level",
      "framing": "Centered medium shot capturing subject from head to mid-thigh",
      "lens": "{argument name="lens" default="85mm"} portrait lens",
      "aperture": "{argument name="aperture" default="f/1.8"} for shallow depth of field",
      "focus": "Sharp focus on subject, softly blurred background",
      "resolution": "4K",
      "color_tone": "Warm, cozy, festive glow"
    },
    "style": "Ultra-realistic cinematic photography, soft winter tones, festive mood",
    "mood": "Cozy, elegant, holiday-inspired, softly illuminated nighttime scene",
    "constraints": [
      "Preserve all facial features and identity from uploaded reference",
      "Do not alter hair style or face",
      "Ensure snowflakes appear natural on coat and hair"
    ]
  }
}
```

[[Face Preservation]] [[Winter Fashion]]

---

### 63. 圣诞树灾难行动冻结（猫和老鼠风格）

**Author**: [Shine by Nous ✨](https://x.com/Shinebynous)  **Date**: 2025-12-10  **Language**: en

> 一个 Nano Banana Pro 提示，能将一张主体正在圣诞树上挂星星的现有照片，转化为一个充满活力的喜剧灾难场景。它要求保留主体的面部和身体，同时加入卡通般的混乱元素，特别是要参考《猫和老鼠》的风格，让圣诞树倾倒，装饰品四处飞溅。

![圣诞树灾难行动冻结（猫和老鼠风格）](https://cms-assets.youmind.com/media/1765509736307_8lfk34_G70jvAkXgAEI-58.jpg)

```
Transform this photo into a holiday living room scene. Keep the subject's face and body exactly as they are, reaching up to place a star on top of a Christmas tree.
The Disaster: The tree is tipping over dangerously onto the subject. {argument name="character 1" default="Tom"} is clinging to the top branches, looking terrified, eyes bulging. {argument name="character 2" default="Jerry"} is at the bottom of the tree, having just sawed through the trunk with a tiny saw.
Style: Dynamic action freeze, flying ornaments, cozy fireplace lighting in the background.
```

[[Face Preservation]]

---

### 64. 迷你 Q 版头像生成提示词

**Author**: [Mr Leslie.Y](https://x.com/Leslieyu0)  **Date**: 2025-12-10  **Language**: zh

> 一个通用提示词，旨在生成与上传照片完美匹配的 Q 版（萌版）玩偶或头像，同时保留人物的面部和服装。这是一个图生图提示词，用于创建个性化的迷你版自己。

![迷你 Q 版头像生成提示词](https://cms-assets.youmind.com/media/1765509804723_m46ylk_G70Xa1yaYAEA1LO.jpg)
![迷你 Q 版头像生成提示词](https://cms-assets.youmind.com/media/1765509804705_jilpca_G70Xa1zaMAIi2tD.jpg)
![迷你 Q 版头像生成提示词](https://cms-assets.youmind.com/media/1765509804833_g3n5w6_G70Xa12a4AAw8pe.jpg)
![迷你 Q 版头像生成提示词](https://cms-assets.youmind.com/media/1765509806244_3s9oyr_G70Xa1yb0AA_8kW.jpg)

```
拥抱那个 Q 版的自己。生成一个穿同款衣服、长得一样的 Q 版公仔！完美支持锁脸锁衣，男女通用。
```

[[Face Preservation]] [[Chibi Style]]

---

### 65. OOTD 杂志时尚拼贴提示词 (JSON/YAML)

**Author**: [Miu (みう) /Japanese beauty from Okinawa🌺](https://x.com/AI8263353539674)  **Date**: 2025-12-10  **Language**: ja

> 这是一个为 Nano Banana Pro 设计的高度结构化的 YAML/JSON 提示，旨在创建专业的“今日穿搭”（OOTD）杂志风格时尚拼贴画。它详细说明了布局比例、如何保留输入图像中的面部特征和服装细节、产品网格排列、排版和美学风格。

![OOTD 杂志时尚拼贴提示词 (JSON/YAML)](https://cms-assets.youmind.com/media/1765509814466_vc6zwh_G7ztZR2aoAABXkm.jpg)

```
{
  "target": "NanoBanana",
  "role_task": "Create a professional OOTD magazine-style fashion collage",
  "layout": {
    "left": {
      "width_ratio": 0.60,
      "preserve": {
        "face": true,
        "hairstyle": true,
        "outfit": true
      },
      "photo_style": "clean, bright, magazine-quality",
      "pose": "cute, amusing, slightly quirky, realistic atmosphere"
    },
    "right": {
      "width_ratio": 0.40,
      "background": "white",
      "product_grid": {
        "quantity": "[quantity]",
        "arrangement": "vertical",
        "final_module": "underwear_estimated_from_image",
        "module_fields": [
          "product_image_cutout_white_bg",
          "product_name",
          "price_yen"
        ]
      }
    }
  },
  "example_products": [
    {"id":1, "name":"{argument name="Product 1 Name" default="[Product 1]"}", "price":"¥{argument name="Product 1 Price" default="[price]"}", "image":"[path_or_url_or_placeholder]"},
    {"id":2, "name":"{argument name="Product 2 Name" default="[Product 2]"}", "price":"¥{argument name="Product 2 Price" default="[price]"}", "image":"[path_or_url_or_placeholder]"},
    {"id":3, "name":"{argument name="Product 3 Name" default="[Product 3]"}", "price":"¥{argument name="Product 3 Price" default="[price]"}", "image":"[path_or_url_or_placeholder]"},
    {"id":4, "name":"{argument name="Product 4 Name" default="[Product 4]"}", "price":"¥{argument name="Product 4 Price" default="[price]"}", "image":"[path_or_url_or_placeholder]"},
    {"id":5, "name":"{argument name="Product 5 Name" default="[Product 5]"}", "price":"¥{argument name="Product 5 Price" default="[price]"}", "image":"[path_or_url_or_placeholder]"},
    {"id":6, "name":"{argument name="Product 6 Name" default="[Product 6] (final underwear)"}", "price":"¥{argument name="Product 6 Price" default="[price]"}", "image":"[path_or_url_or_placeholder]"}
  ],
  "typography": {
    "font_family": "modern_sans_serif",
    "product_name_weight": "medium",
    "price_weight": "bold"
  },
  "style": {
    "aesthetic": "bright, fresh, professional, Instagram fashion-blogger",
    "layout": "clean with generous white space",
    "color_palette": ["natural_tones", "white", "soft_gray"],
    "photo_quality": "professional_ecommerce_photography"
  },
  "output_requirements": {
    "file_format": "PNG or JPG at editorial resolution",
    "left_image_handling": "preserve original pixels for face/hair/outfit (no warp)",
    "right_images_handling": "clip to white background, consistent lighting and scale",
    "notes": "final module must reflect underwear inferred from uploaded image"
  }
}
```

[[Face Preservation]] [[Magazine Layout]] [[Fashion Collage]]

---

### 66. 8K 明暗对照肖像 JSON

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2025-12-10  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张超现实的 8K 肖像，采用明暗对比画法，强调戏剧性的对比效果，一束细长的阳光照亮眼睛，并保持所提供参考图像的面部特征。

![8K 明暗对照肖像 JSON](https://cms-assets.youmind.com/media/1765509730949_3pkvsp_G7zs72kaMAAATU-.jpg)

```
{
  "Objective": "Generate a hyper-realistic 8K chiaroscuro-style portrait of a woman based on the provided reference image.",
  
  "Identity_Safety": "Maintain facial features, hairstyle, and general appearance consistent with the provided reference image without altering identity.",

  "Subject": {
    "Gender": "Female",
    "Appearance": {
      "Hair": "Straight hair falling naturally across her forehead",
      "Pose": "Gazing slightly upward and to the side",
      "Expression": "Soft, calm, and introspective",
      "Lips": "Glossy, slightly parted, catching subtle highlights"
    }
  },

  "Lighting": {
    "Style": "Chiaroscuro dramatic contrast",
    "Key_Effects": [
      "A thin ray of sunlight illuminating her eyes and upper cheek",
      "Deep, rich shadows covering the background and lower half of her face",
      "Strong separation between light and dark regions",
      "High emotional and visual depth"
    ]
  },

  "Scene": {
    "Background": "Minimal, falling into dark shadow",
    "Atmosphere": "Intimate, dramatic, painterly, cinematic"
  },

  "Visual_Style": {
    "Resolution": "8K hyper-realistic",
    "Aesthetic": [
      "Ultra-detailed skin texture",
      "Natural highlights on lips and eyes",
      "Soft hair detailing",
      "Fine contrast control typical of chiaroscuro portraiture"
    ],
    "Color_Profile": "Warm natural skin tones against deep shadow background"
  },

  "Output_Requirements": {
    "Format": "Image",
    "Orientation": "Portrait",
    "Quality": "High-end cinematic and photographic realism"
  }
}
```

[[Face Preservation]] [[High Contrast Photography]] [[Chiaroscuro Lighting]] [[Portrait Photography]]

---

### 67. 现代健身房中的镜面自拍，面部清晰可见

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2025-12-10  **Language**: en

> 一个高度结构化的 JSON 提示词，旨在生成一张年轻女性在现代健身房里蹲姿的镜面自拍。该提示词包含面部保留、姿势、服装（运动内衣和运动裤）、环境、灯光和负面提示词的详细规范，旨在营造一种社交媒体美学。

![现代健身房中的镜面自拍，面部清晰可见](https://cms-assets.youmind.com/media/1765509686981_z4mjb0_G7x38zQakAAVfjY.jpg)

```
{
  "image_prompt": {
    "face_preservation": {
      "use_reference_face": true,
      "accuracy": "match face exactly from reference image",
      "preserve_details": [
        "face shape",
        "eyebrows and eye structure",
        "natural makeup style",
        "lip shape and color",
        "hairline and hairstyle"
      ]
    },

    "subject": {
      "gender": "female",
      "description": "young woman taking a mirror selfie while squatting gracefully indoors",
      "pose": {
        "body_position": "squatting low with one knee forward, leaning slightly toward mirror",
        "head": "tilted slightly downward while looking at phone screen",
        "hands": [
          "right hand holding phone in front of face",
          "left hand resting on knee"
        ],
        "expression": "soft, calm expression"
      },
      "hair": {
        "style": "long dark brown hair in a half-up ponytail with a small clip",
        "texture": "smooth and straight"
      },
          "clothing": {
          "top": {
            "type": "sports bra",
            "color": "off-white",
            "details": "tight, form-fitting material with slight sheen"
          },
          "bottom": {
            "type": "loose sweatpants",
            "color": "dark brown",
            "fit": "relaxed, high-waisted"
          }
        },
        "nails": "black nail polish"
      }
    },

        "shoes": "white Snickers",
        "accessories": [
          "silver necklace",
          "bracelet",
          "rings"
        ]
      }
    },

    "environment": {
      "setting": "modern indoor gym with mirrored walls",
      "details": {
        "equipment": [
          "chest press machine",
          "various gym machines in background"
        ],
        "flooring": "wood-textured gym flooring",
        "walls": "full-height mirrors reflecting gym interior",
        "lighting": "soft overhead LED lighting with warm ambient accents"
      }
    },

      }
    },

    "props": {
      "phone": {
        "type": "smartphone",
        "case": "glitter silver phone case",
        "position": "held vertically towards the mirror"
      }
    },

    "style": {
      "photography": "mirror selfie, social media aesthetic",
      "color_grade": "soft warm tones",
      "sharpness": "medium-high clarity",
      "mood": "feminine, elegant, gentle"
    },

    "composition": {
      "framing": "full body squatting pose, centered",
      "angle": "eye-level mirror perspective",
      "focus": "sharp focus on face and outfit",
      "aspect_ratio": "4:5"
    },

    "output": {
      "resolution": "8K high quality",
      "negative_prompt": [
        "incorrect face",
        "wrong hairstyle",
        "extra limbs",
        "different dress pattern",
        "distorted proportions",
        "text or watermark"
      ]
    }
  }
}
```

[[Face Preservation]] [[Social Media Aesthetic]] [[Gym Mirror Selfie]] [[Squat Pose]]

---

### 68. 在昏暗房间里，一位年轻女性的低角度风格化肖像

**Author**: [Melis✨](https://x.com/miilesus)  **Date**: 2025-12-02  **Language**: en

> 一个结构化的 JSON 提示词，用于 Gemini Nano Banana Pro 生成一张高清低角度照片：一位年轻女性身处昏暗、温暖、紫色调的房间中，同时保留她的面部特征，并指定发型、姿势、服装和灯光。

![在昏暗房间里，一位年轻女性的低角度风格化肖像](https://cms-assets.youmind.com/media/1764909151110_x4ha7i_G7LzJ3EWkAAFpRr.jpg)
![在昏暗房间里，一位年轻女性的低角度风格化肖像](https://cms-assets.youmind.com/media/1764909153758_n65s2j_G67Pf1oWMAAXXwP.jpg)

```
{
  "image_generation_request": {
    "constraints": {
      "preservation_instruction": "Without changing my facial features and face",
      "strictness": "High"
    },
    "technical_specifications": {
      "medium": "Photograph",
      "resolution": "High-definition",
      "camera_angle": "Low-angle perspective"
    },
    "subject_details": {
      "demographics": "Young woman",
      "physical_appearance": {
        "hair": {
          "style": "Messy updo",
          "details": "Loose strands"
        }
      },
      "pose_and_action": {
        "stance": "Standing",
        "positioning": "Positioned",
        "gesture": "Touching the collar",
        "vibe": "Looking stylish"
      },
      "attire": {
        "upper_body": {
          "item": "Cropped t-shirt",
          "color": "Dark blue",
          "texture": "Ribbed",
          "details": [
            "White trim",
            "White logo"
          ]
        },
        "lower_body": {
          "item": "Pajama pants",
          "pattern": "Striped",
          "color": "White"
        }
      }
    },
    "scene_environment": {
      "setting_type": "Room",
      "lighting": {
        "intensity": "Dimly lit",
        "temperature": "Warm",
        "color_tone": "Enhanced purple-toned",
        "sources": [
          "Ceiling fixture",
          "Hidden cove lights"
        ]
      }
    }
  }
}
```

[[Face Preservation]] [[Low Angle Portrait]]

---

### 69. F1 赛车 VIP 粉丝超逼真自拍编辑

**Author**: [Nano Banana Labs](https://x.com/NanoBanana_labs)  **Date**: 2025-11-24  **Language**: en

> 一个详尽的提示，可将用户的自拍照转换为一张 8K 超逼真照片，照片中用户身着时尚的 F1 粉丝服饰，置身于一场高端汽车活动中，同时保留其真实面部特征，仅改变服装和场景。

![F1 赛车 VIP 粉丝超逼真自拍编辑](https://cms-assets.youmind.com/media/1764209297048_n7xo8a_G6jRUN9WAAAsoLO.jpg)
![F1 赛车 VIP 粉丝超逼真自拍编辑](https://cms-assets.youmind.com/media/1764209299373_as206e_G6jRUVAWsAA60lX.jpg)
![F1 赛车 VIP 粉丝超逼真自拍编辑](https://cms-assets.youmind.com/media/1764209301563_vql86q_G6jRUcoW4AAsbyw.jpg)

```
Create a hyper-realistic image in 8K resolution, keeping exactly my real face, features, skin color, eyes, and hair as per the reference image.
I am the {argument name="subject_gender_role" default="woman"} in the photo; preserve my confident, charming, and elegant expression, with a slight smile and relaxed posture.
I am at an outdoor automotive event, in a grandstand or VIP box, with a wide view of the track and the crowd in the background. The weather is sunny, with an intense blue sky and natural sunlight, enhancing the colors and creating a vibrant racing atmosphere.
The framing is a medium shot, capturing the upper body and the busy background with a slight depth-of-field blur.
The look is sporty fashion with a sophisticated touch, composed of:
 * {argument name="cap_brand" default="Red Ferrari"} cap, with the yellow prancing horse (cavallino rampante) logo on the front and the number "{argument name="driver_number" default="16"}" in white on the brim;
 * Strapless top in structured denim, tight and with visible stitching, enhancing the décolletage and silhouette;
 * {argument name="sunglasses_brand" default="Miu Miu"} sunglasses with brown gradient lenses and a rectangular metallic frame, partially covering the eyes;
 * Double necklace – one with large golden links and another with delicate diamonds close to the neck;
   * Geometric gold earrings;
   * Silver bracelet on the right wrist;
   * Discreet red bag hanging on the shoulder, partially visible beside the arm.
Hair: natural, loose.
The makeup is impeccable and glamorous, with illuminated skin, defined eyes, pink lipstick, and warm blush.
The nails are long and decorated with nail art in shades of pink and red with white details, visible while holding the glass.
The pose conveys attitude and sophistication:
 * Right hand holding the brim of the cap, adjusting it slightly;
 * Left hand holding a glass of {argument name="drink_type" default="white wine"}, with the arm relaxed;
 * Body slightly leaned, face turned towards the camera.
The lighting is natural and intense, with subtle solar reflections on the face and hair.
The color palette is vibrant – shades of red, denim blue, gold, and caramel, contrasting with the sunny background.
The general atmosphere is modern, luxurious, and relaxed – transmitting the style of someone who lives exclusive experiences, with elegance and a striking presence at a premium automotive event.
Quality: 8K hyper-realistic photo, sharp focus on the face and outfit, background slightly blurred with a colorful crowd and the track in the sun.
Important:
 * Keep my face, hair, and skin color original.
 * Preserve the authentic p
```

[[Face Preservation]]

---

### 70. 带有宝丽来相框的双模特时尚大片

**Author**: [Cherry 2.O](https://x.com/Mind_Boticni)  **Date**: 2026-04-09  **Language**: en

> 一份详细的提示词，用于生成一张高分辨率摄影棚照片，展示两位身着不同服装的女性模特，背景为灰粉色，并置于一个大型的空白白色方形宝丽来风格道具框中。

![带有宝丽来相框的双模特时尚大片](https://cms-assets.youmind.com/media/1776096297103_2ctobq_HFb3j67a8AUR6Rj.jpg)

```
A high-resolution studio photograph featuring two female models posing against a solid dusty rose background. On the left, a model with dark hair wearing a light brown felt fedora hat, a patterned plaid trench coat in shades of light blue, white, and brown over a pale pink lace-hemmed slip dress, and silver metallic chunky-heeled platform sandals with pastel pink socks. On the right, a blonde-haired model wearing an open solid pale pink long coat over an olive green slip dress, holding a pink and white checkered patterned clutch bag, and a silver necklace, and wearing light beige pointed-toe ankle boots. The models are centered within a large, empty white square polaroid-style frame, as if it is a physical prop framing their upper bodies and heads, with their legs and shoes extending below the frame, still against the dusty rose background. Both models look directly and engagingly at the camera with warm expressions. The lighting is soft and even, highlighting the textures of the fabrics. The composition is clean and focused solely on the models, their apparel, and the central white frame, with all surrounding space being a clean, uninterrupted dusty rose color. The style is a minimalist fashion editorial photograph.
```

[[Fashion Editorial]] [[Studio Photography]]

---

### 71. 九宫格舞蹈编辑网格，带身份锁定

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-25  **Language**: en

> 一个复杂且结构化的提示词，用于生成一个 3x3 的编辑网格，内容是一名女性表演现代舞姿。它需要使用图像到图像模式（图生图模式），以确保在所有九个面板中锁定面部特征，同时生成一套全新且一致的服装（奶油黄色舞蹈服）和一个干净的摄影棚背景，最终呈现出一种高级时尚的舞蹈宣传片效果。

![九宫格舞蹈编辑网格，带身份锁定](https://cms-assets.youmind.com/media/1774508269751_noiv1j_HERChY_W8AEFw9y.jpg)

```
Create a photorealistic 3x3 editorial grid featuring one woman repeated across all nine panels with locked facial identity. Use the uploaded reference image only for facial identity, facial proportions, skin tone, and recognizability. Do not copy, preserve, inherit, reinterpret, or transfer any clothing, styling, accessories, pose, or background from the reference image. Ignore the original outfit completely.

SUBJECT: The woman should have a polished elegant hairstyle and refined editorial makeup with luminous skin and defined eyes, visually consistent across all panels. She wears an entirely new luxurious butter-yellow contemporary dance outfit generated from scratch: a fitted asymmetrical one-shoulder top in soft draped satin-stretch fabric with sculpted waist definition, paired with high-waisted fluid wide-leg dance trousers with graceful movement, elegant drape, and elongated leg lines.

SCENE: Clean minimal premium editorial studio background, visually consistent across all panels. Mood: confident, artistic, expressive, feminine, high-fashion, dance-driven.

PANEL DIRECTIONS:
- Panel 1: Strong standing dance pose with one arm lifted overhead and the other extended outward, long elegant line
- Panel 2: Seated dance pose with one knee folded, torso angled, expressive hand placement
- Panel 3: Deep torso curve with asymmetrical arm line, sculptural contemporary dance energy
- Panel 4: Floor-based pose with one arm reaching upward and the body leaning into a graceful side arc
- Panel 5: Hero center pose, grounded and powerful, strong stage presence, striking silhouette
- Panel 6: Kneeling pose with lifted chest, elongated neck, refined lyrical arm movement
- Panel 7: Off-balance standing pose with one leg extended and dynamic asymmetrical upper body shape
- Panel 8: Low seated or half-floor pose with curved spine and controlled expressive gesture
- Panel 9: Final signature pose with both arms raised, subtle hip shift, memorable campaign silhouette

TECHNICAL: 4:5 portrait aspect ratio, ultra high resolution. Cinematic editorial realism style with editorial crisp sharpness, subtle film grain, soft clean high-end dynamic range, warm editorial color grade. 3x3 grid layout with thin gutter and no outer border.

MOTION & PHYSICS: Perfect anatomy, believable balance, physically correct posture, elegant joint articulation. Realistic gravity-driven drape and subtle movement response. Clean realistic hands with correct fingers, no distortion.

CAMERA: Mixed full-body, mid-body, and seated editorial compositions with clean premium studio angles. Sharp focus on facial detail, pose lines, hands, and fabric texture. Clean studio clarity depth of field.

LIGHTING: Soft directional editorial lighting with gentle sculpting, elegant highlights, subtle shadows. Real skin texture, no plastic effect.

MUST HAVE: 3x3 grid layout, different dance pose in every panel, reference face identity preserved, consistent hair across all panels, consistent makeup across all panels, new butter-yellow dance outfit generated from prompt only, no clothing copied from reference, consistent studio background, photoreal quality, perfect anatomy, realistic hands, sharp face in every panel, no text.

NEGATIVE PROMPT: No reference outfit transfer, no copied clothing from source image, no same outfit as reference, no source styling retained, no reference accessories preserved, no reference pose copied, no different identity in each panel, no cheap dance costume, no sportswear, no awkward limbs, no bad anatomy, no extra fingers, no missing fingers, no deformed hands, no broken wrists, no stiff body, no unnatural spine, no plastic skin, no blurry face, no duplicate limbs, no text, no logo, no watermark.
```

[[Fashion Editorial]] [[Image-To-Image]] [[Studio Photography]] [[3x3 Grid Layout]]

---

### 72. 柔和电影风格工作室编辑提示

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-25  **Language**: en

> 一个结构化的 JSON 提示词，用于 Nano Banana Pro 生成一张柔和、柔彩色调的电影感影棚时尚大片，描绘一位年轻女性。该提示词要求严格使用参考面部，并包含具体细节，例如一件浅蓝色缎面迷你连衣裙和一双白色长款缎面手套。

![柔和电影风格工作室编辑提示](https://cms-assets.youmind.com/media/1774508279373_tzu9hb_HEQzPYoaIAAtzX9.jpg)
![柔和电影风格工作室编辑提示](https://cms-assets.youmind.com/media/1774508279316_jap651_HEQzQOCbAAAy9AH.jpg)
![柔和电影风格工作室编辑提示](https://cms-assets.youmind.com/media/1774508279510_0yale4_HEQzOsmacAAdsTJ.jpg)

```
{
"photo_type":"studio editorial, soft pastel minimal aesthetic",

"subject":{
"type":"young woman",
"use_reference_image":true,
"face_reference":true,
"preserve_identity":true,
"instruction":"strictly use the provided reference face, do NOT change facial structure, skin tone, eye color, or hair color",
"pose":"kneeling on the floor, body leaning slightly forward, hands placed on ground, legs folded back, elegant posture",
"expression":"soft dreamy expression, slightly distant gaze, relaxed lips"
},

"appearance":{
"hair":"same as reference image, long soft waves, unchanged color",
"eyes":"same as reference image, unchanged",
"skin":"smooth glowing skin with soft highlights",
"makeup":"soft glam, pastel tones, subtle blush and glossy lips"
},

"outfit":{
"clothing":"light blue satin mini dress with delicate details",
"accessories":[
"long white satin gloves",
"pearl anklet",
"heels with soft embellishments"
],
"style":"feminine, doll-like, high fashion"
},

"environment":{
"location":"studio",
"background":"plain pastel blue seamless backdrop",
"floor":"matching pastel tone, clean and minimal"
},

"lighting":{
"type":"soft studio lighting",
"setup":[
"diffused even lighting",
"low shadow contrast",
"soft glow on skin",
"clean editorial look"
]
},

"camera":{
"angle":"slightly low and front angle",
"framing":"full body with negative space",
"focus":"sharp subject, smooth background"
},

"color_grading":{
"style":"pastel cinematic",
"tones":"baby blue, soft white, light skin tones",
"contrast":"low",
"saturation":"soft and airy"
},

"details":{
"must_include":[
"reference face unchanged",
"same hair and eye color",
"pastel blue background",
"soft feminine pose",
"clean studio aesthetic"
],
"avoid":[
"dark tones",
"harsh shadows",
"overediting",
"busy background"
]
}
}
```

[[Fashion Editorial]] [[Identity Reference]] [[Film Aesthetic]]

---

### 73. 黄昏时分的屋顶编辑风格人像摄影

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-03-23  **Language**: en

> 针对 Nano Banana Pro 的极高细节、写实级提示词，旨在生成一张 Sydney Sweeney 的全身时尚大片。画面中，她身着单色白色定制套装，置身于黄昏时分的现代屋顶露台，重点突出专业摄影参数、光影效果及构图。

![黄昏时分的屋顶编辑风格人像摄影](https://cms-assets.youmind.com/media/1774334465713_x1wg37_HEGRx4XbsAAA5cy.jpg)

```
A person from the reference photo stands upright on a rooftop terrace, facing forward with a confident posture. One hand is in the trouser pocket, the other holds a small structured handbag. Shoulders relaxed, head straight with a natural tilt, gaze forward with a calm, self-assured expression.

Outfit:
Monochromatic white tailored look — sleeveless draped blouse tucked into high-waisted wide-leg trousers with clean pleats. A matching structured blazer is draped over the shoulders. Pointed high heels in a neutral tone. Accessories include layered delicate necklaces, medium hoop earrings, a bracelet, and a small top-handle handbag.
Setting:
Modern rooftop terrace with glass railing overlooking a city skyline at dusk. Background buildings glow with soft lights, creating a subtle bokeh effect. Cool blue evening sky contrasts with warm city lights.

Composition & Camera:
Full-body vertical portrait (9:16), subject centered. Eye-level perspective capturing the full outfit and stance. Clean architectural framing with balanced space.
Lighting:
Soft natural twilight mixed with subtle artificial city lighting. Even, diffused illumination with gentle shadows. Neutral-to-cool color tones with slight warm highlights.

Style & Quality:
Professional editorial / lifestyle photography, photorealistic. Shot as if on Canon EOS 5D Mark IV, 85mm lens, f/2.0. Sharp focus on subject, realistic depth of field, smooth transitions, natural skin texture, visible details, no over-processing. Ultra-detailed, 8K quality.
Negative Prompt:
CGI, 3D render, fake/plastic skin, over-smoothing, AI artifacts, distortions, extra limbs, bad anatomy, heavy filters, excessive retouching, harsh HDR, motion blur, out of focus.
```

[[Fashion Editorial]] [[Celebrity Likeness]] [[Dusk Lighting]]

---

### 74. 深色连体泳衣的柔和编辑肖像

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-03-20  **Language**: en

> 一个详细的 JSON 提示，用于 Nano Banana 2，重点是生成一张柔和、逼真的室内编辑肖像，描绘一位留着黑色短波波头、身穿深灰色镂空露背连体泳衣的女性，斜倚在沙发上，强调温暖的定向照明和宁静、沉思的氛围。

![深色连体泳衣的柔和编辑肖像](https://cms-assets.youmind.com/media/1774074516618_rkzlx6_HD34_CnWgAAd385.jpg)
![深色连体泳衣的柔和编辑肖像](https://cms-assets.youmind.com/media/1774074516551_87rg4e_HD34-8FWkAEpwPB.jpg)
![深色连体泳衣的柔和编辑肖像](https://cms-assets.youmind.com/media/1774074516743_j1d7sn_HD34--OWAAAnO8o.jpg)
![深色连体泳衣的柔和编辑肖像](https://cms-assets.youmind.com/media/1774074517552_ia1fen_HD34_LebYAAKz5F.jpg)

```
{
  "subject": {
    "description": "adult woman, short black bob with long wispy bangs, reclining on sofa in dark gray cutout halter monokini",
    "expression": "calm, slightly distant, soft heavy-lidded gaze through bangs, slightly parted lips, quiet pensive mood",
    "face": "small delicate features, soft jawline, natural lip shape, light natural makeup, subtle eyeliner, muted peach-beige lips"
  },
  "hair": {
    "color": "deep black",
    "style": "short layered bob, long uneven bangs over eyes/cheeks, fine strands, soft warm sheen"
  },
  "body": {
    "frame": "slim curvy, defined waist, full bust emphasized by monokini, smooth long legs",
    "skin": "fair warm beige tone, velvety smooth natural texture, visible shoulders/neck/chest/arms/abdomen/hips/thighs"
  },
  "pose": {
    "position": "reclining diagonally on soft sofa",
    "action": "one arm raised above head touching hair, other hand relaxed on seat, one knee raised toward camera, one leg extended"
  },
  "clothing": {
    "type": "red cutout halter monokini",
    "details": "thin neck strap, deep central cutout, high-cut legs, matte stretched fabric with tension folds"
  },
  "photography": {
    "style": "realistic soft editorial indoor portrait",
    "angle": "slightly above eye level, close intimate",
    "shot_type": "medium close vertical portrait, 2:3 aspect",
    "focus": "sharp on subject, shallow DoF with smooth background blur"
  },
  "lighting": {
    "description": "warm soft directional front-left indoor light, low contrast, gentle highlights on hair/skin, dim background"
  },
  "background": {
    "setting": "indoor lounge/bedroom",
    "elements": "light gray sofa, muted cushions, dark brown/charcoal wall/curtain, neon written 'KeorUnreal' on wall",
    "atmosphere": "quiet warm late-evening stillness"
  },
  "the_vibe": {
    "energy": "low slow intimate",
    "mood": "calm private detached",
    "aesthetic": "soft realistic sensuality, understated elegance, lived-in authenticity"
  },
  "constraints": {
    "must_keep": [
      "adult",
      "short black bob + long bangs",
      "dark gray cutout monokini",
      "reclining sofa pose",
      "arm raised to hair",
      "knee lifted foreground",
      "warm soft light",
      "dark minimal background",
      "natural skin & anatomy"
    ],
    "avoid": [
      "anime/cartoon",
      "extra limbs",
      "plastic skin",
      "harsh flash",
      "busy background",
      "text/logos",
      "over-retouching"
    ]
  },
  "negative_prompt": [
    "underage",
    "anime",
    "extra fingers/limbs",
    "bad anatomy",
    "plastic skin",
    "harsh lighting",
    "text/watermark",
    "low res",
    "blurry subject"
  ]
}
```

[[Fashion Editorial]] [[Warm Directional Light]]

---

### 75. 高级时尚单色影棚肖像

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-20  **Language**: en

> 一个详细的 JSON 提示，用于 Nano Banana 2 在极简主义的单色工作室中生成一张高级时装社论肖像，重点是复杂的姿势构图（手臂框住脸部）、明确的光线和超真实的纹理保留。

![高级时尚单色影棚肖像](https://cms-assets.youmind.com/media/1774074514695_93kefu_HD3er3Cb0AAmRQb.jpg)
![高级时尚单色影棚肖像](https://cms-assets.youmind.com/media/1774074514668_lsitla_HD3er3AboAQyvXI.jpg)
![高级时尚单色影棚肖像](https://cms-assets.youmind.com/media/1774074514720_d36ajf_HD3er4kbsAE85QW.jpg)

```
{
  "style": {
    "genre": "high-fashion editorial portrait",
    "aesthetic": "minimalist monochrome studio",
    "color_palette": ["black", "white", "charcoal gray", "soft silver"],
    "finish": "ultra-realistic, fine art photography",
    "contrast": "medium-high contrast with soft tonal transitions",
    "grain": "subtle film grain for editorial authenticity"
  },
  "subject": {
    "type": "woman",
    "age": "mid-20s",
    "ethnicity": "ambiguous / globally appealing features",
    "physique": "slender, elegant proportions",
    "facial_features": {
      "structure": "defined cheekbones, soft jawline",
      "skin": "smooth, luminous, natural texture preserved",
      "eyes": "expressive, slightly narrowed gaze",
      "lips": "softly parted, natural shape"
    },
    "hair": {
      "style": "loose, slightly tousled",
      "texture": "soft with natural movement",
      "placement": "falling around face and shoulders with subtle volume"
    },
    "expression": "calm, introspective, slightly mysterious"
  },
  "pose": {
    "composition": "asymmetrical, fashion-forward",
    "body_position": "upright with slight lean",
    "arm_position": {
      "primary_arm": "raised across the face",
      "gesture": "partially obscuring one eye and cheek",
      "fingers": "relaxed, elongated, graceful positioning"
    },
    "head_tilt": "slight tilt to enhance dynamic tension",
    "gaze": "direct or slightly off-camera through arm framing"
  },
  "wardrobe": {
    "top": {
      "type": "loose white blouse",
      "fabric": "lightweight cotton or silk",
      "fit": "oversized, softly draped",
      "details": [
        "subtle folds and creases",
        "natural fabric texture visible",
        "open or relaxed collar"
      ]
    },
    "styling": "minimalist, effortless high-fashion look"
  },
  "lighting": {
    "setup": "studio lighting",
    "type": "soft yet directional",
    "key_light": {
      "position": "45 degrees from subject",
      "quality": "diffused but defined",
      "effect": "sculpting facial features and fabric folds"
    },
    "fill_light": {
      "intensity": "low",
      "purpose": "retain shadow depth without losing detail"
    },
    "shadow": {
      "style": "soft-edged shadows with depth",
      "contrast": "balanced for editorial look"
    }
  },
  "background": {
    "type": "studio backdrop",
    "color": "clean white to light gray gradient",
    "texture": "smooth, distraction-free",
    "depth": "slight falloff to create separation"
  },
  "camera": {
    "framing": "portrait, mid-shot to close-up",
    "angle": "slightly below or eye-level for subtle drama",
    "lens": "85mm prime",
    "aperture": "f/2.0",
    "focus": "sharp on visible eye and hand",
    "depth_of_field": "shallow with soft background blur"
  },
  "composition": {
    "rule_of_thirds": true,
    "negative_space": "balanced for editorial layout",
    
  }
}
```

[[Fashion Editorial]] [[Skin Texture Detail]] [[Minimalist Studio]]

---

### 76. Karina (aespa) 象牙白与紫色发色造型

**Author**: [Alice](https://x.com/youngcatwoman)  **Date**: 2026-03-20  **Language**: en

> 一个高度描述性的提示，用于生成 K-pop 偶像 Karina (aespa) 坐在灰色地毯上的优雅高级时尚肖像。它强调了她纤细的身材、瓷器般的肌肤、猫科动物般的面部特征、充满活力的深紫色头发，以及带有蕾丝细节的复杂象牙白色服装，所有这些都置于一个带有柔和灯光的极简主义摄影棚背景中。

![Karina (aespa) 象牙白与紫色发色造型](https://cms-assets.youmind.com/media/1774074527498_hxq4xn_HDz_EpvboAAAKXU.jpg)
![Karina (aespa) 象牙白与紫色发色造型](https://cms-assets.youmind.com/media/1774074527495_d2bskj_HDz-9AwacAAF3oj.jpg)

```
In a vertical composition of elegant proportions, Karina from aespa is seated upon a soft, grey-carpeted floor, her figure captured in a moment of poised, modern grace. She possesses a lithe and delicately curvaceous build, her skin radiating a luminous, porcelain fairness that speaks of her Korean heritage, smooth and ethereal against the muted backdrop. Her presence is one of striking aesthetic harmony, characterized by her sharp, feline-like facial features, refined symmetry, and a sophisticated, supermodel-like allure. Long, silken tresses of vibrant deep purple flow downward, veiling her shoulders and reaching toward the floor in a vivid cascade of color. She holds a dark smartphone before her face, her slender fingers adorned with a simple ring and pale, manicured nails, creating a focal point of contemporary mystery. She is dressed in a complex, ivory-white ensemble that blends delicate textures; a high-collared, sleeveless bodice features a circular cutout at the chest and draped, voluminous sleeves that gather at the wrists. The garment is cinched at the waist with intricate lace-up detailing, flowing into a sheer, skirt-like overlay that rests against her legs. Complementing the attire are white lace garters cinched around her thighs, adding a layer of intricate detail to the soft contours of her physique. The setting is minimalist and serene, defined by the neutral, textured carpet below and a backdrop of heavy, white draped fabric that falls in soft, vertical folds. The lighting is diffused and even, casting gentle shadows that define the subtle musculature of her arms and the graceful curve of her pose, bathing the entire scene in a clean, high-fashion glow that emphasizes the vivid violet of her hair against the pristine whites of her surroundings. —ar 9:16
```

[[Fashion Editorial]] [[Minimalist Studio]]

---

### 77. 极简高对比度影棚时尚大片

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-20  **Language**: en

> 一个结构化的 JSON 提示词，用于 nano-banana-pro 生成一张高对比度的影棚时尚大片，画面中人物身着垂坠感单肩白色连衣裙，利用单一硬光源营造锐利阴影，并强调肌肤的真实感。

![极简高对比度影棚时尚大片](https://cms-assets.youmind.com/media/1774074531289_iftbq6_HD10CHDaoAEJSWQ.jpg)
![极简高对比度影棚时尚大片](https://cms-assets.youmind.com/media/1774074531433_r1u8w4_HD10CLuboAIwXAw.jpg)
![极简高对比度影棚时尚大片](https://cms-assets.youmind.com/media/1774074531547_z4dxvk_HD10CPBXMAA94hv.jpg)

```
{
  "photo_type": "Studio fashion editorial (minimal high-contrast realism)",

  "subject": {
    "face": {
      "description": "Use uploaded reference image, keep identity 100% unchanged"
    },

    "pose_description": "Standing upright with relaxed posture, body slightly angled, one leg forward, arms relaxed, shoulders slightly dropped",

    "expression": "Soft neutral expression, slightly parted lips, relaxed eyes",

    "body_details": [
      "natural posture, not stiff",
      "subtle hip shift",
      "slight asymmetry in stance"
    ]
  },

  "clothing": {
    "type": "draped one-shoulder fabric dress",

    "details": [
      "white cloth wrapped loosely around body",
      "one shoulder exposed",
      "natural folds and wrinkles",
      "asymmetrical draping",
      "fabric hanging unevenly",
      "soft cotton or linen texture"
    ],

    "physics": [
      "gravity-based folds",
      "fabric bunching at waist",
      "natural tension points"
    ]
  },

  "hair": {
    "style": "loose messy updo",

    "details": [
      "strands falling across face",
      "slightly imperfect styling",
      "natural flyaways",
      "soft texture"
    ]
  },

  "skin_realism": {
    "details": [
      "visible pores",
      "natural skin tone variation",
      "subtle shadows on body",
      "no smoothing filter"
    ]
  },

  "lighting": {
    "type": "single hard studio light",

    "setup": [
      "one strong light source from upper side",
      "no fill light",
      "direct hard lighting"
    ],

    "effects": [
      "sharp defined shadow on background",
      "high contrast on body",
      "strong light falloff",
      "clear shadow edges",
      "highlight on one side of body, other side darker"
    ],

    "color_temperature": "neutral studio light 5000K"
  },

  "shadow_control": {
    "details": [
      "distinct shadow cast on wall",
      "shadow follows body shape",
      "sharp edges not blurred",
      "angled slightly behind subject"
    ]
  },

  "background": {
    "type": "plain studio wall",

    "details": [
      "neutral beige or off-white tone",
      "no texture",
      "clean seamless backdrop"
    ]
  },

  "camera": {
    "type": "professional DSLR",

    "lens": "50mm",

    "settings": {
      "aperture": "f/4",
      "iso": "ISO 100",
      "shutter_speed": "1/160s"
    },

    "focus": "sharp full body",

    "lens_behavior": [
      "natural perspective",
      "no distortion",
      "clean edges"
    ],

    "sensor_behavior": [
      "high detail",
      "clean image",
      "subtle tonal depth"
    ]
  },

  "color_grading": {
    "style": "editorial minimal",

    "rules": [
      "soft neutral tones",
      "slightly warm skin",
      "clean whites",
      "no heavy contrast boost"
    ]
  },

  "imperfections": [
    "natural fabric wrinkles",
    "slight uneven drapi
```

[[Fashion Editorial]] [[Skin Texture Detail]]

---

### 78. 高对比度夜间人像：闪光灯与城市灯光

**Author**: [Picts by AI](https://x.com/pictsbyai)  **Date**: 2026-03-20  **Language**: en

> 一个高度详细的 JSON 格式提示，用于 Gemini Nano Banana Pro，旨在生成一张高对比度、精致的夜间生活方式肖像。该提示细致地定义了构图、色彩配置文件（互补的暖/冷色调）和光照（主体上的强闪光灯与背景中的城市环境光）。

![高对比度夜间人像：闪光灯与城市灯光](https://cms-assets.youmind.com/media/1774074541910_bo5acs_HD1zamiXkAAxg2t.jpg)

```
{
"metadata": {
"image_type": "photograph",
"primary_purpose": "social media/portrait/lifestyle"
},
"composition": {
"rule_applied": "center composition",
"aspect_ratio": "4:5",
"layout": "single subject foreground with expansive deep background",
"focal_points": [
"Subject's brightly lit face and crisp white shirt",
"Clasped hands displaying luxury watch",
"Glowing band of city lights in the background"
],
"visual_hierarchy": "Viewer eye starts at the smiling face, travels down the bright V-shape of the unbuttoned white shirt to the posed hands and watch, then moves outward to the horizontal band of glowing city lights and mountain silhouette.",
"balance": "symmetric subject placement contrasted by slightly asymmetric background landscape (mountain on the right)"
},
"color_profile": {
"dominant_colors": [
{
"color": "Deep Black/Navy",
"hex": "#0D1117",
"percentage": "55%",
"role": "background night sky and suit jacket"
},
{
"color": "Crisp White",
"hex": "#FFFFFF",
"percentage": "15%",
"role": "primary subject shirt"
},
{
"color": "Warm Skin Tone",
"hex": "#C68767",
"percentage": "15%",
"role": "primary subject face and hands"
},
{
"color": "Golden Yellow",
"hex": "#F4C430",
"percentage": "10%",
"role": "accent city lights"
}
],
"color_palette": "complementary (warm golden/orange lights vs cool dark blue/black shadows)",
"temperature": "warm foreground against a cool/neutral dark background",
"saturation": "moderate (skin tones and lights are vivid, shadows are deeply desaturated)",
"contrast": "high contrast"
},
"lighting": {
"type": "mixed (direct artificial flash on subject, ambient practical lights in background)",
"source_count": "multiple sources - single dominant flash foreground, thousands of pinpoint ambient lights background",
"direction": "front/slightly elevated",
"directionality": "highly directional flash",
"quality": "hard light (creating crisp shadows under chin, collar, and hands)",
"intensity": "bright on subject/low-key overall",
"contrast_ratio": "high contrast (dramatic foreground isolation)",
"mood": "energetic/polished/glamorous",
"shadows": {
"type": "harsh defined edges",
"density": "deep black",
"placement": "under chin, behind shirt collar, under hands, beneath lapels",
"length": "short"
},
"highlights": {
"treatment": "specular",
"placement": "on nose tip, forehead, hair texture, and watch face"
},
"ambient_fill": "absent in foreground",
"light_temperature": "neutral/slightly warm flash"
},
"technical_specs": {
"medium": "digital photography",
"style": "realistic/lifestyle",
"texture": "glossy (hair, watch) contrasted with smooth fabric and skin",
"sharpness": "tack sharp on subject",
"grain": "digital noise present in the deep background sky",
"depth_of_field": "medium (subject crisp, background distant but structurally visible, minimal bokeh)",
"per
```

[[Fashion Editorial]]

---

### 79. 高级时装工作室编辑肖像

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-03-20  **Language**: en

> 一个用于生成高定时尚、超写实编辑肖像的提示，主体（提示中名为 Emma Stone，但推文中指的是 Emily Rudd）置身于极简主义影棚中。它详细说明了相机设备（哈苏 H6D-400c）、戏剧性的轮廓光，以及详细的服装和姿势描述。

![高级时装工作室编辑肖像](https://cms-assets.youmind.com/media/1774074526824_eqnrf2_HD1cgdwboAMSoC-.jpg)

```
“quality”: “ultra_photorealistic, raw style, 8k”,
    “camera”: “Hasselblad H6D-400c, 80mm lens”,
    “lighting”: “professional studio lighting, dramatic rim lighting”,
    “style”: “high-fashion magazine editorial”,
    “aspect_ratio”: “9:16”
  },
  “scene”: {
    “location”: “A minimalist studio with a delicate dusty rose pink background wall and a clean white floor with subtle shadows.”,
    “atmosphere”: “Sophisticated, high-end fashion.”
  },
  “subject”: {
    “gender”: “female”,
    “name”: “Emma Stone”,
    “body”: {
      “type”: “Athletic and toned physique”
    },
    “face”: {
      “features”: “Large expressive green eyes, signature vibrant red hair styled in elegant waves, subtle freckles, distinct facial features, intense editorial gaze.”,
      “expression”: “Serious and poised.”
    },
    “outfit”: {
      “description”: “Black fitted sleeveless crop top with delicate spaghetti straps, a pleated pink plaid skirt, black sheer hosiery with lace detailing, black high-heeled pumps.”,
      “fit”: “Designer, sleek, tailored.”,
      “accessory”: “Posing with a small dark wooden stool.”
    },
    “pose”: “Professional fashion pose. Standing with her right leg elevated, foot resting on a small stool to create a dynamic silhouette. Head turned toward the lens.”
  },
  “composition”: “Full-body vertical shot, balanced composition, sharp focus on subject and fabric textures. Clean studio aesthetic.”
}
```

[[Fashion Editorial]] [[Minimalist Studio]] [[Hasselblad Camera]] [[Couture Fashion Photography]]

---

### 80. Google Nano Banana Pro 电影人像提示词

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-03-20  **Language**: en

> 一个给 Google Nano Banana Pro 的提示，用于生成一张时尚男士的超现实电影感肖像。重点在于戏剧性的光线（明暗对比法、聚光灯）营造出金色光晕效果，以及他锐利、专注地看向镜头的眼神。

![Google Nano Banana Pro 电影人像提示词](https://cms-assets.youmind.com/media/1774074507050_l7a8ti_HD0BCw4bAAAdfQF.jpg)

```
Ultra-realistic cinematic portrait of a stylish man in a black suit, captured from behind with his head turned over his shoulder, giving a sharp, intense look toward the camera. Short textured hair with subtle highlights, well-groomed beard. Dramatic spotlight from above creating a warm golden halo effect on his hair and face, fading into a dark background. Strong chiaroscuro lighting with deep shadows and soft highlights.
```

[[Fashion Editorial]] [[Chiaroscuro Lighting]]

---

### 81. 艾玛·斯通 (Emma Stone) 身着粉色格子高定服装拍摄时尚大片

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-03-19  **Language**: en

> 一个详细的 JSON 提示，用于 Nano Banana Pro 生成一张艾玛·斯通（Emma Stone）的超逼真、高级时装编辑图片。图片中，艾玛·斯通身穿黑色露脐上衣和粉色格子短裙，在一个脏粉色背景前，动态地摆姿势坐在凳子上。

![艾玛·斯通 (Emma Stone) 身着粉色格子高定服装拍摄时尚大片](https://cms-assets.youmind.com/media/1773988997531_2czpl9_HDytxHGWUAEDlzB.jpg)
![艾玛·斯通 (Emma Stone) 身着粉色格子高定服装拍摄时尚大片](https://cms-assets.youmind.com/media/1773988997683_83p8jx_HDytw-GWcAEShVk.jpg)
![艾玛·斯通 (Emma Stone) 身着粉色格子高定服装拍摄时尚大片](https://cms-assets.youmind.com/media/1773988997710_7uxzbj_HDytxD5WwAAjxm_.jpg)

```
{
  “meta”: {
    “quality”: “ultra_photorealistic, raw style, 8k”,
    “camera”: “Hasselblad H6D-400c, 80mm lens”,
    “lighting”: “professional studio lighting, dramatic rim lighting”,
    “style”: “high-fashion magazine editorial”,
    “aspect_ratio”: “9:16”
  },
  “scene”: {
    “location”: “A minimalist studio with a delicate dusty rose pink background wall and a clean white floor with subtle shadows.”,
    “atmosphere”: “Sophisticated, high-end fashion.”
  },
  “subject”: {
    “gender”: “female”,
    “name”: “Emma Stone”,
    “body”: {
      “type”: “Athletic and toned physique”
    },
    “face”: {
      “features”: “Large expressive green eyes, signature vibrant red hair styled in elegant waves, subtle freckles, distinct facial features, intense editorial gaze.”,
      “expression”: “Serious and poised.”
    },
    “outfit”: {
      “description”: “Black fitted sleeveless crop top with delicate spaghetti straps, a pleated pink plaid skirt, black sheer hosiery with lace detailing, black high-heeled pumps.”,
      “fit”: “Designer, sleek, tailored.”,
      “accessory”: “Posing with a small dark wooden stool.”
    },
    “pose”: “Professional fashion pose. Standing with her right leg elevated, foot resting on a small stool to create a dynamic silhouette. Head turned toward the lens.”
  },
  “composition”: “Full-body vertical shot, balanced composition, sharp focus on subject and fabric textures. Clean studio aesthetic.”
}
```

[[Fashion Editorial]] [[Celebrity Likeness]] [[Black Crop Top]]

---

### 82. Ana de Armas 风格的低蹲姿势编辑肖像

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-19  **Language**: en

> 一个详细的 JSON prompt，用于 Nano Banana 2 生成一张超逼真的时尚编辑肖像，灵感来自 Ana de Armas，特点是低蹲姿势、丝绸衬衫、黑色迷你裙和透明过膝袜。

![Ana de Armas 风格的低蹲姿势编辑肖像](https://cms-assets.youmind.com/media/1773988997348_zdz55n_HDyrL7HbUAAMz2l.jpg)
![Ana de Armas 风格的低蹲姿势编辑肖像](https://cms-assets.youmind.com/media/1773988997409_7ixoqj_HDyrL-lbcAAx463.jpg)

```
{
  "meta": {
    "title": "Ana de Armas Inspired Editorial Portrait",
    "aspect_ratio": "2:3",
    "resolution": "8k",
    "quality": "ultra_photorealistic",
    "style": "high-fashion editorial, cinematic realism",
    "camera": "Canon EOS R5",
    "lens": "85mm f/1.4",
    "color_profile": "neutral studio tones with warm highlights",
    "grain": "subtle film grain"
  },

  "subject": {
    "identity": "Ana de Armas inspired lookalike",
    "gender": "female",
    "age": "mid 20s to early 30s",
    "skin": "smooth luminous skin with natural texture",
    "face": {
      "structure": "soft oval face, high cheekbones, delicate jawline",
      "eyes": "almond-shaped brown eyes, soft smoky eyeliner",
      "eyebrows": "naturally full and well-defined",
      "lips": "full lips with bold red lipstick",
      "expression": "confident, slightly serious, intense gaze directed at camera"
    },
    "hair": {
      "color": "dark brown",
      "style": "sleek low bun with subtle loose strands framing face",
      "finish": "soft shine, slightly textured"
    }
  },

  "outfit": {
    "clothing": {
      "top": {
        "type": "silk blouse",
        "color": "burnt orange",
        "material": "satin silk",
        "fit": "slightly loose with structured collar",
        "details": "soft folds, glossy reflections, partially tucked"
      },
      "bottom": {
        "type": "mini skirt",
        "color": "black",
        "material": "silk or satin blend",
        "fit": "high-waisted, form-fitting"
      },
      "legwear": {
        "type": "sheer thigh-high stockings",
        "color": "black",
        "details": "lace band at top, semi-transparent finish"
      },
      "footwear": {
        "type": "high heels",
        "style": "classic pumps",
        "color": "black",
        "heel_height": "high stiletto"
      },
      "accessories": {
        "glasses": "thin rectangular reading glasses",
        "earrings": "small gold hoops",
        "additional": "smartphone held in both hands"
      }
    }
  },

  "pose": {
    "position": "low squat pose",
    "legs": "bent deeply, knees forward, balanced posture",
    "arms": "hands holding smartphone naturally",
    "head": "slightly tilted downward, eyes looking up toward camera",
    "gesture": "engaged with phone while maintaining eye contact"
  },

  "scene": {
    "location": "minimalist studio",
    "background": {
      "color": "neutral gray",
      "texture": "smooth seamless backdrop"
    },
    "environment": "clean, distraction-free editorial setup"
  },

  "lighting": {
    "type": "studio soft lighting",
    "setup": "key light front-left, fill light soft, subtle rim light",
    "effect": "soft shadows, even skin tones, gentle highlights on silk fabric",
    "mood": "balanced, modern, slightly dramatic"
  },

  "composition": {
    "framing": "full-body portrait",
    "angle": "slightly low angle",
    "focus": "sharp focus on subject",
    "depth_of_field": "shallow background blur",
```

[[Fashion Editorial]] [[Celebrity Likeness]]

---

### 83. Sabrina Carpenter 风格时尚大片肖像

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-19  **Language**: en

> 一个详细的 JSON 提示，用于 Nano Banana 2 生成一张写实时尚编辑图片：一位女性模仿 Sabrina Carpenter，坐在影棚地板上，身穿白色 T 恤、粉色裹身系带和白色蕾丝连裤袜。

![Sabrina Carpenter 风格时尚大片肖像](https://cms-assets.youmind.com/media/1773988994179_n7807q_HDvaAEMbkAEcz2Z.jpg)

```
{
  "style": {
    "genre": "fashion editorial photography",
    "aesthetic": "minimal studio fashion",
    "mood": "soft, playful, slightly flirtatious",
    "color_palette": ["mint green", "soft white", "light pink", "cream"]
  },
  "character": {
    "identity_placeholder": "a young woman channeling Sabrina Carpenter",
    "gender_presentation": "feminine",
    "age_range": "young adult",
    "body_type": "hourglass — full bust, defined narrow waist, wide hips, voluptuous curves",
    "skin_tone": "light to medium neutral tone"
  },
  "hair": {
    "color": "dark brown",
    "length": "long",
    "style": "messy ponytail",
    "strands": "loose strands falling around face",
    "texture": "slightly tousled"
  },
  "accessories": {
    "earrings": "medium silver hoop earrings",
    "other": []
  },
  "expression": {
    "facial_expression": "soft neutral expression",
    "mood": "calm and relaxed",
    "gaze": "looking back over shoulder toward camera"
  },
  "pose": {
    "body_position": "sitting on studio floor",
    "torso": "upright but slightly leaned to the side",
    "legs": "crossed and extended forward",
    "feet_position": "feet on the floor with heels slightly lifted",
    "head_angle": "slightly tilted toward camera",
    "pose_vibe": "elegant and flirty editorial fashion pose — curves naturally accentuated"
  },
  "clothing": {
    "top": {
      "type": "short sleeve fitted t-shirt",
      "color": "White",
      "fit": "tight — hugging bust and waist"
    },
    "waist_detail": {
      "type": "thin bubblegum pink wrap tie around waist",
      "style": "ribbon-like strap tied at back, emphasizing narrow waist"
    },
    "bottom": {
      "type": "lace tights / lace leggings",
      "color": "white",
      "pattern": "floral lace pattern",
      "opacity": "semi-sheer"
    },
    "shoes": {
      "type": "open toe mule heels",
      "color": "bubblegum pink",
      "heel_height": "mid heel",
      "material": "smooth leather"
    }
  },
  "camera": {
    "angle": "low rear three-quarter angle",
    "framing": "full body",
    "focus": "sharp focus on subject",
    "lens": "50mm fashion photography lens",
    "depth_of_field": "moderate shallow depth"
  },
  "lighting": {
    "type": "soft studio lighting",
    "setup": "large softbox",
    "direction": "front-left soft light",
    "shadows": "very soft minimal shadows",
    "contrast": "low contrast"
  },
  "background": {
    "type": "seamless studio backdrop",
    "color": "warm cream",
    "texture": "smooth matte",
    "environment": "minimalist studio"
  },
  "composition": {
    "subject_placement": "centered slightly left",
    "negative_space": "large empty background",
    "editorial_style": "magazine fashion shoot",
    "aspect_ratio": "3:4"
  },
  "quality": {
    "resolution": "high resolution",
    "detail_level": "high detail fabric texture",
    "photorealism": "photorealistic",
    "post_processing": "clean edito
```

[[Fashion Editorial]] [[Celebrity Likeness]]

---

### 84. 现代楼梯上的 K-pop 偶像 Rosé 肖像

**Author**: [Alice](https://x.com/youngcatwoman)  **Date**: 2026-03-19  **Language**: en

> 为 Nano Banana Pro 设计的结构化提示，用于生成 K-pop 偶像 Rosé 坐在现代木质楼梯上，身穿深 V 粉色乳胶西装紧身衣和粉色细高跟鞋的超逼真肖像。

![现代楼梯上的 K-pop 偶像 Rosé 肖像](https://cms-assets.youmind.com/media/1773988995832_8dok5h_HDPsELdbQAEvs80.jpg)

```
{
"prompt": "Photorealistic portrait of K-pop idol Rosé with long platinum blonde hair sitting on modern wooden stairs. She wears a plunging pink latex blazer bodysuit and glossy pink stilettos with red soles. Symmetrical pose with legs apart. --ar 3:4",
"subject": {
"appearance": "Young woman, K-pop idol Rosé, fair skin, dark brown almond eyes.",
"hair": "Extra-long, straight, platinum blonde.",
"jewelry": "Silver hoop earrings, thin silver chain with small round pendant."
},
"outfit": {
"clothing": "Pink latex tailored blazer styled as a bodysuit, deeply unbuttoned.",
"shoes": "Glossy pink patent leather stiletto pumps featuring red bottoms."
},
"pose": {
"body": "Sitting upright on a stair tread facing the camera.",
"legs": "Spread wide apart, knees bent at an angle.",
```

[[Fashion Editorial]] [[Celebrity Likeness]]

---

### 85. 电影风格的时尚动作骑手肖像

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-03-16  **Language**: en

> 为 Nano Banana Pro 提供一个高度具体的提示，以生成一张电影级的时尚动作肖像：一名骑手在日落时分加速穿越崎岖地形，重点突出强烈的背光、深邃的色彩渐变和运动模糊，以增强真实感。

![电影风格的时尚动作骑手肖像](https://cms-assets.youmind.com/media/1773729508871_wd21ko_HDi1S7_acAAC6D6.jpg)

```
CINEMATIC FASHION-ACTION PORTRAIT OF A RIDER ACCELERATING ACROSS RUGGED TERRAIN AT SUNSET. DEEP GRADIENT SKY TRANSITION FROM BURNT ORANGE NEAR HORIZON TO DARK TEAL ABOVE. SUBJECT CAPTURED MID-MOTION, SLIGHTLY LIFTED FROM THE SEAT AS THE REAR WHEEL KICKS UP DIRT AND GRAVEL. FINE DUST PARTICLES SUSPENDED IN THE AIR, ILLUMINATED BY BACKLIGHT. HAIR: SHORT DARK HAIR OR CLOSELY CROPPED — WIND-PRESSED. NATURAL TEXTURE. OUTFIT: MINIMALIST PERFORMANCE STYLING — MATTE BLACK COMPRESSION TOP, STRUCTURED CARGO SHORTS OR TECHNICAL PANTS, SUBTLE NEON ACCENT FOOTWEAR. (ACID GREEN OR ELECTRIC BLUE). NO VISIBLE LOGOS. CLEAN, MODERN SILHOUETTE. BIKE: MODERN DIRT BIKE IN CUSTOM COLORWAY — MUTED FOREST GREEN, MATTE SILVER, OR DEEP RED. NO BRAND NAMES VISIBLE. LIGHTING: STRONG WARM BACKLIGHT FROM LOW SUN CREATING RIM GLOW AROUND RIDER AND DUST. COOLER FILL LIGHT ON FRONT SIDE OF SUBJECT FOR CONTRAST. HIGH DYNAMIC RANGE WITH RICH SHADOWS AND GLOWING HIGHLIGHTS. COLOR GRADE: CINEMATIC CONTRAST. WARM HIGHLIGHTS, COOL SHADOWS, SLIGHT GRAIN TEXTURE. HIGH CLARITY ON DUST PARTICLES. CAMERA: LOW ANGLE TRACKING PERSPECTIVE. 35MM LENS. SHALLOW DEPTH OF FIELD WITH SHARP SUBJECT, SOFT BACKGROUND. SLIGHT MOTION BLUR ON DIRT AND REAR WHEEL FOR REALISM. MOOD: CONTROLLED CHAOS. POWER IN MOTION. SUNSET ADRENALINE.
```

[[Fashion Editorial]] [[Motion Blur]] [[Action Sports Photography]]

---

### 86. 淹没在水中的复古汽车上的时尚女性

**Author**: [Synthia](https://x.com/AIwithSynthia)  **Date**: 2026-03-13  **Language**: en

> 一个用于 nano-banana-pro 的详细图像生成提示，描述了一个电影般的时尚编辑场景：一位时尚的年轻女性自信地摆姿势，坐在一辆部分浸没在清澈海水中的经典豪华轿车引擎盖上，强调鲜艳的色彩和高细节。

![淹没在水中的复古汽车上的时尚女性](https://cms-assets.youmind.com/media/1773469800231_uyqp8e_HDRkUNubQAAYkwM.jpg)

```
A stylish young woman with short pastel blue hair and red sunglasses stands confidently on the hood of a classic luxury vintage sedan partially submerged in crystal clear shallow ocean water. She wears an oversized colorful striped polo shirt tucked into loose baggy denim jeans with a red scarf tied around the waist, layered silver chains, and casual sneakers. One hand rests in her pocket while the other makes a playful gesture toward the camera. A designer handbag sits beside her on the car hood. The scene is set in a bright sunny coastal landscape with rocky islands and turquoise water in the background, cinematic fashion editorial style, vibrant colors, ultra realistic, high detail, wide angle composition, summer luxury vibe.
```

[[Fashion Editorial]] [[Surreal Photography]] [[Cinematic Scene]] [[Vibrant Colors]]

---

### 87. Nano Banana 2 的长曝光光绘时尚肖像提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-12  **Language**: en

> 一个高度结构化的 JSON 提示词，专为 Nano Banana 2 设计，用于图像到图像的生成，将参考图像转换为具有琥珀色和金橙色调的长曝光光绘效果的逼真时尚编辑肖像。

![Nano Banana 2 的长曝光光绘时尚肖像提示](https://cms-assets.youmind.com/media/1773383499207_zazr6j_HDNqSpxWgAMFTIe.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "Nano Banana 2",
      "task_type": "long_exposure_light_painting_fashion_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_AMBER_LIGHT_WAVE_EDITORIAL"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_pose": true,
      "preserve_composition": true,
      "preserve_mood": true
    },
    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "render_style": "photoreal_editorial_fashion",
      "sharpness": "editorial_crisp",
      "grain": "subtle_film",
      "color_grade": "warm_amber_cinematic",
      "dynamic_range": "deep_contrast_luminous",
      "skin_rendering": "real_texture_refined"
    },
    "subject": {
      "model": {
        "type": "adult woman",
        "pose": "graceful standing fashion pose with one arm raised high and the other bent above the head",
        "expression": "calm, introspective, elegant, softly sensual",
        "hair": "sleek dark bob or short dark hair",
        "styling": "minimalist luxury fashion styling"
      },
      "wardrobe": {
        "top": "white halter-style cut-out bandeau top with circular center detail",
        "bottom": "soft white draped fitted skirt",
        "accessories": "minimal statement earrings"
      }
    },
    "scene": {
      "environment": "dark studio with black background",
      "lighting": "low-key studio lighting combined with long-exposure light painting",
      "light_effects": "flowing amber and golden-orange luminous trails wrapping around the figure in vertical organic waves",
      "mood": "cinematic, mysterious, elegant, sculptural, luxurious"
    },
    "composition": {
      "framing": "centered full-body portrait",
      "camera_angle": "straight-on fashion editorial perspective",
      "focus": "sharp subject with controlled motion-blur light trails",
      "visual_balance": "strong vertical composition with glowing curves framing the body"
    },
    "details": {
      "emphasis": "light painting, graceful silhouette, warm glow, body contours, premium fashion atmosphere",
      "texture": "smooth fabric, luminous skin highlights, silky light trails, deep black negative space",
      "palette": [
        "amber",
        "burnt orange",
        "golden light",
        "warm ivory",
        "deep black"
      ],
      "aesthetic": "high-end fashion editorial, long-exposure photography, cinematic fine art portrait"
    },
    "negative_prompt": {
      "avoid": [
        "extra limbs",
        "deformed hands",
        "bad anatomy",
        "messy light trails",
        "flat lighting",
        "cheap studio look",
        "blurry face",
        "overexposed skin",
        "cartoon style",
        "busy background",
        "watermark",
        "unrelated text"
```

[[Fashion Editorial]] [[Photorealistic Rendering]] [[Image-To-Image Generation]]

---

### 88. 窗边黄金时段电影感人像系列

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-03-10  **Language**: en

> 为 Gemini Nano Banana Pro 生成的提示，用于创作一系列电影感肖像照：一位美丽女子在黄金时段坐在大窗边。提示中指定了柔和、温暖的日落光线，沉思的姿势，透过玻璃的倒影，以及都市天际线背景，旨在呈现编辑时尚摄影风格。

![窗边黄金时段电影感人像系列](https://cms-assets.youmind.com/media/1773210660015_qhagj0_HDFmGmBa8AA33SY.jpg)

```
Cinematic portrait series of a beautiful woman with long wavy brown hair sitting by a large window during golden hour, soft warm sunset light illuminating her face. She wears a dark minimalist sweater, natural makeup, and small earrings. The photos show different thoughtful and emotional poses — hand on chin, looking outside, touching hair, looking down, subtle smile. Shot through glass creating soft reflections and dreamy overlays. Urban city skyline with a domed building blurred in the background. Moody, artistic atmosphere, shallow depth of field, soft shadows, warm earthy tones, editorial fashion photography, 85mm lens, ultra-realistic, high detail, filmic color grading.
```

[[Fashion Editorial]] [[Female Portrait]] [[Golden Hour Lighting]] [[City Skyline Background]]

---

### 89. 在工作室里深蹲的丰腴女性

**Author**: [EroticJSON ㌹](https://x.com/EvrDjM)  **Date**: 2026-03-09  **Language**: en

> 一个用于 Gemini Nano Banana Pro 的 JSON 提示，用于生成一张超高分辨率、逼真的图像：一位身材惊艳的年轻女性，拥有丰满的天然胸部，在明亮的白色背景工作室中赤裸上身蹲着，穿着高腰蓝色牛仔裤，手持一个黑色 Dior Lady 手袋。

![在工作室里深蹲的丰腴女性](https://cms-assets.youmind.com/media/1773038331452_e37ocd_HC7l6vKakAAH_Is.jpg)

```
{
  "prompt": "A stunningly beautiful young woman with long wavy dark brown hair, seductive brown eyes with heavy makeup, full lips, perfect symmetrical face, flawless tanned skin, extremely voluptuous figure with massive natural breasts, tiny waist, wide hips, squatting pose on the floor in a bright studio with white background, completely topless exposing bare large breasts and nipples, wearing high-waisted blue denim jeans, black ankle boots, gold hoop earrings, gold bracelet, holding a black {argument name="handbag brand" default="Dior Lady"} handbag with logo pattern in front of her, confident expression looking at camera, detailed skin texture, realistic, photorealistic, ultra high resolution, professional studio lighting"
}
```

[[Fashion Editorial]] [[Photorealistic Rendering]] [[White Studio Background]]

---

### 90. Sydney Sweeney 和 Ana de Armas 海滩姿势

**Author**: [Pinodi](https://x.com/PinodiArt)  **Date**: 2026-03-01  **Language**: en

> 一个极其详细、结构化的提示，用于生成一张西德尼·斯威尼（Sydney Sweeney）和安娜·德·阿玛斯（Ana de Armas）身穿泳装、用前臂撑在毛巾上的照片级真实图像。该提示详细说明了生物特征细节、精确的服装颜色（十六进制代码）、材料科学、姿势以及场景细节（海滩/泳池边背景，可见白色美甲）。

![Sydney Sweeney 和 Ana de Armas 海滩姿势](https://cms-assets.youmind.com/media/1772433509726_d40u4n_HCUlk3yWkAAzUKE.jpg)

```
{
  "subject": {
    "identities": [
      {
        "biometric_reference": "Sydney Sweeney",
        "facial_structure": {
          "shape": "oval with defined cheekbones",
          "eye_morphology": "almond-shaped, hooded eyelid characteristic",
          "dentition": "natural alignment, bright white",
          "iris_pattern": "light blue-grey with radial stroma fibers"
        },
        "body_morphology": {
          "somatotype": "hourglass mesomorph, slightly shorter frame relative to subject_2",
          "waist_to_hip_ratio": "0.68",
          "skin_physics": {
            "tone_hex": "#F8D1B4",
            "texture": "dewy, high specular highlights, subsurface scattering enabled",
            "details": "opaque white lacquer on toenails, anatomical bone structure of feet clearly visible"
          }
        },
        "wardrobe": {
          "item": "two-piece ribbed bikini",
          "material": "textured elastane/nylon blend",
          "color_hex": "#191970",
          "fit": "low-rise bottom, secure top with thin straps"
        }
      },
      {
        "biometric_reference": "Ana de Armas",
        "facial_structure": {
          "shape": "oval/heart blend with distinct high cheekbones and balanced jawline",
          "dentition": "natural alignment, bright white",
          "iris_pattern": "complex green/hazel with detailed gold flecks and dark limbal rings",
          "lip_morphology": "balanced cupid's bow, full lower lip"
        },
        "body_morphology": {
          "somatotype": "slim hourglass mesomorph somatotype, average height frame, proportional dimensions",
          "waist_to_hip_ratio": "0.71",
          "skeletal_proportions": "proportional femur and torso lengths",
          "skin_physics": {
            "tone_hex": "#FAD6A5",
            "texture": "pores visible, high specular highlights on solar-exposed areas, natural light olive complexion texture",
            "details": "opaque white lacquer on toenails, natural skin texture on soles of feet"
          }
        },
        "wardrobe": {
          "item": "one-piece scoop-neck swimsuit",
          "material": "honeycomb waffle-knit texture",
          "color_hex": "#FFFFFF",
          "fit": "high-cut leg, form-fitting body contour"
        }
      }
    ]
  },
  "pose_action": {
    "description": "Propped up on forearms in a semi-recumbent position, leaning on elbows with upper torso elevated",
    "interaction": "Both subjects facing forward, looking directly into the camera lens with soft expressions",
    "arm_placement": "Forearms resting on towels to support body weight, hands resting naturally",
    "leg_position": "Legs extended straight forward toward the lower edge of the frame, showcasing white pedicures",
    "symmetry": "Side-by-side alignment with subject_1 on the left (white towel) and subject_2 on the right (red towel)"
  },
  "scene": {
    "en"
  }
}
```

[[Fashion Editorial]] [[Photorealistic Portrait]] [[Swimwear Photography]]

---

### 91. 豪华汽车编辑照片提示

**Author**: [Picts by AI](https://x.com/pictsbyai)  **Date**: 2026-03-01  **Language**: en

> 一个高度结构化的提示，用于生成一张在豪华 SUV 驾驶座上的年轻男子的精致编辑摄影作品。它通过三分法、详细的色彩配置文件、高对比度的自然窗户照明和技术规格，精心定义了构图，以实现传达财富和休闲的逼真、精致美学。

![豪华汽车编辑照片提示](https://cms-assets.youmind.com/media/1772433494699_3xbk8w_HCT-tVabEAQ40y-.jpg)

```
{
"metadata": {
"image_type": "photograph",
"primary_purpose": "editorial"
},
"composition": {
"rule_applied": "rule of thirds",
"aspect_ratio": "3:4",
"layout": "layered",
"focal_points": [
"Subject's face illuminated by natural light",
"Black gloved left hand resting on the steering wheel"
],
"visual_hierarchy": "Eye starts at the subject's brightly lit face, moves down to the black gloved left hand on the steering wheel, sweeps right across the center console to the relaxed right hand, and finally moves up to the exterior landscape visible through the windows.",
"balance": "asymmetric"
},
"color_profile": {
"dominant_colors": [
{
"color": "Black",
"hex": "#111111",
"percentage": "50%",
"role": "primary subject clothing, driving gloves, and vehicle interior"
},
{
"color": "Pine Green",
"hex": "#2D4C1E",
"percentage": "15%",
"role": "background landscape"
},
{
"color": "Sky Blue",
"hex": "#4A90E2",
"percentage": "10%",
"role": "background sky through sunroof"
},
{
"color": "Warm Tan",
"hex": "#C49A6C",
"percentage": "10%",
"role": "accent interior wood trim"
}
],
"color_palette": "complementary",
"temperature": "neutral",
"saturation": "moderate",
"contrast": "high contrast"
},
"lighting": {
"type": "natural window",
"source_count": "multiple sources",
"direction": "front-top",
"directionality": "highly directional",
"quality": "soft light",
"intensity": "bright",
"contrast_ratio": "high contrast (dramatic shadows)",
"mood": "sophisticated",
"shadows": {
"type": "soft gradual edges",
"density": "deep black",
"placement": "under the jaw, across the right side of the face, deep in the lower footwell of the car",
"length": "short"
},
"highlights": {
"treatment": "preserved",
"placement": "on face, cheekbones, nose bridge, steering wheel chrome accents, and center console silver switches"
},
"ambient_fill": "present",
"light_temperature": "neutral"
},
"technical_specs": {
"medium": "digital photography",
"style": "realistic",
"texture": "sharp",
"sharpness": "tack sharp",
"grain": "none",
"depth_of_field": "medium",
"perspective": "straight on"
},
"artistic_elements": {
"genre": "editorial",
"influences": [
"Luxury automotive lifestyle photography"
],
"mood": "sophisticated",
"atmosphere": "luxurious, calm, and highly polished aesthetic conveying wealth and leisure",
"visual_style": "clean"
},
"typography": {
"present": false,
"fonts": [],
"placement": "none",
"integration": "none"
},
"subject_analysis": {
"primary_subject": "Young male model sitting in driver's seat of luxury SUV wearing black coat and black leather gloves",
"positioning": "left",
"scale": "medium",
"interaction": "interacting with environment",
"facial_expression": {
"mouth": "closed neutral",
"smile_intensity": "no smile",
"eyes": "looking away upward",
"eyebrows": "relaxed",
"overall_emotion": "confident",
"aut
```

[[Fashion Editorial]] [[Natural Window Light]]

---

### 92. Ralph Lauren 马术时尚编辑肖像

**Author**: [Human AI Gallery | Prompt Architect](https://x.com/HumanAIGallery)  **Date**: 2026-02-28  **Language**: en

> 一个详细的 JSON 提示，用于生成一张高动态范围的传统肖像，风格为 Ralph Lauren 马术广告。画面中，一位身着骑马装（马裤、白衬衫、黑色靴子）的女士倚靠在一个质朴、光线昏暗的木制马具室里，强调明暗对比照明和皮革、灰尘等真实纹理。

![Ralph Lauren 马术时尚编辑肖像](https://cms-assets.youmind.com/media/1772346687941_1njoig_HCSJMJtW4AA6Hwb.jpg)

```
{
  "image_prompt": {
    "meta": {
      "aspect_ratio": "9:16",
      "style": "British Countryside, Equestrian editorial"
    },
    "subject": {
      "description": "24-year-old woman with a sharp, aristocratic profile",
      "face": "Flushed cheeks from a morning ride, natural matte skin, intense and commanding gaze looking slightly off-camera",
      "skin": "A light sheen of sweat on the neck, soft morning light hitting the jawline",
      "hair": "Messy low bun, pieces falling out and sticking to the neck",
      "pose": "Standing in a dimly lit tack room, leaning against a wooden wall, pulling off a tight leather riding glove by the fingertips",
      "outfit": "Tailored beige jodhpurs (riding pants), a crisp white cotton shirt unbuttoned deeply at the collar, tall polished black leather riding boots covered in light dust"
    },
    "environment": {
      "location": "A rustic, century-old wooden tack room in a countryside estate",
      "background_elements": [
        "Worn leather saddles and brass bridles hanging on the walls",
        "Hay dust floating in the air",
        "Rich, dark oak wood textures"
      ]
    },
    "lighting": {
      "type": "Morning Sun piercing through a small, dusty window",
      "characteristics": [
        "God-rays illuminating the floating dust motes",
        "Warm, earthy color palette (browns, golds, deep blacks)",
        "Chiaroscuro lighting emphasizing the textures of leather and wood"
      ]
    },
    "photography_style": {
      "style": "Ralph Lauren-style lifestyle campaign",
      "camera_look": "Medium format digital, high dynamic range",
      "imperfections": "Dust in the air, authentic dirt on the boots, raw unpolished edges",
      "mood": "Powerful, grounded, traditional, alluring"
    }
  }
}
```

[[Fashion Editorial]] [[Chiaroscuro Lighting]]

---

### 93. 废弃温泉中的斯堪的纳维亚之美

**Author**: [David](https://x.com/tealdog2)  **Date**: 2026-02-28  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张时尚大片编辑图片：一位身材丰腴的斯堪的纳维亚女性，坐在一处工业废墟（废弃的温泉）中。提示强调了她精致的白色细绳比基尼与厚重的橄榄卡其色冬季派克大衣之间的对比，重点关注了特定的光线、纹理和沉思的表情。

![废弃温泉中的斯堪的纳维亚之美](https://cms-assets.youmind.com/media/1772346686651_hnk5cb_HCRuu2kasAEqQks.jpg)
![废弃温泉中的斯堪的纳维亚之美](https://cms-assets.youmind.com/media/1772346686580_1erw31_HCRuwwGbEAMH4P0.jpg)

```
{ "subject": { "description": "A stunning Scandinavian beauty with a voluptuous figure, sitting in an industrial ruin, wearing a delicate white string bikini contrasted with a heavy winter parka draped off her shoulders.", "mirror_rules": "N/A", "age": "early 20s", "expression": { "eyes": { "look": "pensive and slightly melancholic", "energy": "quiet thoughtfulness", "direction": "looking to the side, towards the camera" }, "mouth": { "position": "lips slightly parted, relaxed", "slight smile", "energy": "soft and relaxed" }, "overall": "serene, contrasting deeply with the harsh environment" }, "face": { "preserve_original": true, "makeup": "exquisite Japanese editorial makeup, soft peach blush, delicate eyeliner, glossy pink lips, flawless foundation" }, "hair": { "color": "Golden brown", "style": "tied back into a loose ponytail with wispy bangs framing the face", "effect": "held back by a white mesh headband, slightly messy from the environment" }, "body": { "frame": "hourglass, curvy, prominent cleavage, slim toned waist", "chest": "large and full, beautifully highlighted by the bikini", "waist": "slender and smooth", "legs": "long, gracefully bent", "skin": { "visible_areas": "torso, arms, chest, thighs", "tone": "fair, translucent cold-white tone", "texture": "feels powdery and velvety soft, a stark contrast to the cold, stone surrounding her", "lighting_effect": "sliced by harsh, distinct geometric shadows cast by an unseen source" } }, "pose": { "position": "sitting on the tiled ground, leaning back slightly", "base": "weight supported by her hands resting beside her thighs, right knee raised", "overall": "a static, vulnerable posture that feels accidentally captured" }, "clothing": { "top": { "type": "string bikini top", "color": "pure white", "details": "tiny triangle cups, thin tie straps", "effect": "struggling to contain her curves" }, "bottom": { "type": "string bikini bottom", "color": "pure white", "details": "very thin side straps riding high on the hips" }, "outerwear": { "type": "heavy winter parka", "color": "olive khaki green", "details": "thick faux fur hood, unzipped, intentionally falling off her shoulders to expose her upper body" } } }, "accessories": { "headwear": "wide white mesh headband", "jewelry": "gold hoop earrings, a thick black leather choker with a small golden rabbit", "prop": "clear plastic high heels carelessly removed and resting near her bare feet" }, "photography": { "camera_style": "professional DSLR, high-fashion editorial gravure photography", "angle": "high angle, shooting downwards to emphasize her form and the ground", "shot_type": "full body to three-quarter shot", "aspect_ratio": "2:3", "texture": "hyper-realistic, sharp focus on the skin and fabric, and background", "lighting": "har" } }
```

[[Fashion Editorial]] [[White Bikini]]

---

### 94. Coquette 花园编辑与兔子

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2026-02-28  **Language**: en

> 一个详细的提示，用于生成一张超逼真的时尚编辑图片：一位年轻的金发女性（形似 Sydney Sweeney），身穿黄色格子泡泡迷你裙。场景设定在黄金时段的茂盛正式花园中，女性手持三只黑色小兔子的牵引绳，强调一种异想天开、超现实和娇媚的审美。

![Coquette 花园编辑与兔子](https://cms-assets.youmind.com/media/1772346682674_xhutaf_HCQOrtFacAArgWe.jpg)
![Coquette 花园编辑与兔子](https://cms-assets.youmind.com/media/1772346682674_re0vn3_HCQOrqbbEAAe72T.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young blonde woman",
      "hair": "Signature voluminous blonde hair with a thick, feathered curtain fringe (bangs); styled in soft, bouncy bombshell blow-out waves that drape over the shoulders.",
      "face": "Playful and elegant expression with a slight smirk; soft, matte skin texture with detailed eyelashes and a soft mauve lip color.",
      "body": "Slender and toned physique with smooth skin; leaning forward at the waist in a graceful, whimsical posture."
    },
    "attire": {
      "clothing": "A strapless {argument name="dress color" default="yellow and white"} plaid puff-ball mini dress with a structured concert bodice and a voluminous, ruffled bubble skirt; paired with sheer yellow thigh-high stockings featuring delicate lace trim at the tops, a little written in black embroidered 'KeorUnreal' on the dress border, glossy yellow high heels. "
      "style": "Avant-Garde Coquette / High Fashion Pastoral."
    },
    "styling_and_accessories": {
      "jewelry": [
        "Single-strand pearl choker necklace",
        "Pearl stud earrings",
        "Three black small rabbits on long, ornate pearl-strand leashes held in each hand"
      ]
    },
    "environment": {
      "setting": "A lush, manicured formal garden or estate lawn during the golden hour.",
      "background": "Deep green manicured hedges, mature deciduous trees, a stone tiger statue to the left, and a multi-tiered stone dolphin fountain centered in the background.",
      "water": "Gentle, shimmering water droplets spraying from a tiered fountain into a stone basin."
    },
    "pose": {
      "posture": "Bending forward at the hips toward the camera, creating a playful and dynamic silhouette.",
      "arms": "Arms extended downward, hands grasping the pearl leashes of three rabbits on the grass.",
      "angle": "Eye-level shot with a slight wide-angle perspective to capture the full environment."
    },
    "lighting_and_mood": {
      "lighting": "Soft, natural golden hour sunlight providing a warm glow on the skin and highlighting the texture of the grass and hair.",
      "mood": "Whimsical, surreal, and high-fashion editorial.",
      "colors": "A vibrant palette of meadow green, sky blue, crisp white, yellow, and warm golden tones."
    },
    "camera_and_technical": {
      "style": "Ultra Photorealistic, RAW photo.",
      "lens": "35mm prime lens.",
      "aperture": "f/2.8 for a sharp subject with a natural, soft-focus background roll-off.",
      "quality_tags": [
        "8k resolution",
        "highly detailed",
        "volumetric lighting",
        "ray tracing reflections",
        "hyper-realistic texture",
        "Hasselblad photography",
        "vogue editorial style"
      ]
    }
  }
}
```

[[Fashion Editorial]] [[Golden Hour Photography]] [[Coquette Aesthetic]]

---

### 95. 20 世纪 60 年代里维埃拉时尚快艇编辑提示

**Author**: [Human AI Gallery | Prompt Architect](https://x.com/HumanAIGallery)  **Date**: 2026-02-27  **Language**: en

> 一个高度详细的 JSON 提示，用于 Gemini Nano Banana Pro，旨在呈现 20 世纪 60 年代里维埃拉的时尚美学，类似于 Slim Aarons 的摄影作品。它描述了一位阳光亲吻的女性，乘坐一艘复古木质 Riva 快艇，强调刺眼的午间光线、高对比度和真实的胶片颗粒感。

![20 世纪 60 年代里维埃拉时尚快艇编辑提示](https://cms-assets.youmind.com/media/1772259936516_ec4bgz_HCLdpKdXMAAEIMc.jpg)

```
{
  "image_prompt": {
    "meta": {
      "aspect_ratio": "9:16",
      "style": "1960s Riviera chic, Slim Aarons aesthetic"
    },
    "subject": {
      "description": "25-year-old woman with a sun-kissed, effortless Mediterranean beauty",
      "face": "Looking back over her shoulder with a relaxed, confident smile, vintage tortoiseshell sunglasses pushed down slightly, natural glossy lips",
      "skin": "Tanned, glowing with natural oils and sea spray, sharp highlights on the collarbones",
      "hair": "Tied back loosely with a silk Hermès-style scarf, strands blowing wildly in the sea breeze",
      "pose": "Sitting on the polished mahogany deck of a classic wooden speedboat, leaning back on one arm, the other hand holding a wide-brimmed straw hat",
      "outfit": "White linen shirt completely unbuttoned over a classic black retro one-piece swimsuit, delicate gold watch"
    },
    "environment": {
      "location": "Back of a vintage wooden Riva speedboat speeding across a deep blue lake",
      "background_elements": [
        "White foam and splashing water in the boat's wake",
        "Lush green mountains and classic Italian villas in the blurred distance",
        "High-gloss mahogany wood and chrome detailing of the boat"
      ]
    },
    "lighting": {
      "type": "Harsh Midday Mediterranean Sun",
      "characteristics": [
        "High contrast, blinding specular highlights on the water and polished wood",
        "Deep, crisp shadows",
        "Vibrant, saturated blues and warm wood tones"
      ]
    },
    "photography_style": {
      "style": "Vintage high-society editorial",
      "camera_look": "35mm film, Kodachrome color palette, sharp focus",
      "imperfections": "A few water droplets on the lens, authentic film grain, wind-blown chaos",
      "mood": "Wealthy, carefree, nostalgic, sun-drenched"
    }
  }
}
```

[[Fashion Editorial]] [[Film Grain]]

---

### 96. 电影感都市街头服饰人像，搭配霓虹灯光

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-02-27  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张超现实电影风格的时尚肖像照，描绘一位身着现代都市街头服饰的年轻男士。场景设定在夜晚的城市隧道中，利用戏剧性的霓虹灯光（青色和橙色调色）和浅景深低角度拍摄，营造出大胆、高端时尚的活力。

![电影感都市街头服饰人像，搭配霓虹灯光](https://cms-assets.youmind.com/media/1772259914957_8j4bat_HCK4X-3aUAApCct.jpg)
![电影感都市街头服饰人像，搭配霓虹灯光](https://cms-assets.youmind.com/media/1772259915073_3sm2e7_HCK4YBTbEAA0Evk.jpg)

```
{
  "master_prompt": {
    "scene_type": "ultra-realistic cinematic fashion portrait",
    "subject": {
      "description": "young man with round glasses",
      "pose": "looking down at the camera",
      "camera_angle": "low angle shot",
      "expression": "confident and calm"
    },
    "outfit": {
      "upper_wear": "oversized light-colored hoodie",
      "inner_layer": "warm orange sweater visible at neckline",
      "style": "modern urban streetwear"
    },
    "environment": {
      "location": "urban tunnel at night",
      "lighting_elements": "bright orange and yellow neon lights",
      "atmosphere": "night city vibe with glowing reflections"
    },
    "lighting": {
      "type": "dramatic neon lighting",
      "color_grading": "strong teal and orange",
      "contrast": "intense contrast with vibrant highlights",
      "face_lighting": "focused dramatic illumination on face and hoodie"
    },
    "camera": {
      "lens": "35mm",
      "depth_of_field": "shallow",
      "background_effect": "soft bokeh",
      "resolution": "ultra-detailed, cinematic clarity"
    },
    "mood": "bold, vibrant, high-fashion urban energy"
  }
}
```

[[Fashion Editorial]] [[Low Angle Shot]] [[Neon Lighting]]

---

### 97. 极简主义艺术画廊时尚编辑提示

**Author**: [Maercih](https://x.com/Maercihh)  **Date**: 2026-02-27  **Language**: en

> 为 Nano Banana Pro 生成一张高度详细的提示，内容为一张精致的当代时尚编辑照片：一位年轻男士和一只边境牧羊犬混血狗，置身于一个明亮、空旷的白色墙壁当代艺术画廊中，强调柔和的自然漫射日光和逼真的纹理。

![极简主义艺术画廊时尚编辑提示](https://cms-assets.youmind.com/media/1772259931004_5xzjs8_HCKAOGcawAEnGni.jpg)

```
A highly detailed minimalist art gallery portrait of this young man with fair skin, sharp cheekbones, medium beard, tousled light brown wavy hair, and a calm, introspective gaze directed at the camera, sitting relaxed on a simple black wooden stool with legs crossed in a bright, empty white-walled contemporary art space. He wears an oversized black linen button-up shirt tucked loosely into matching wide-leg black trousers, black socks, and open-toe black leather gladiator-style sandals. At his feet lies a friendly black-and-white border collie mix dog with tongue out, panting happily, next to a small woven rope toy on the smooth concrete floor. Directly behind him hangs a massive square abstract painting with rich earthy brown tones, subtle texture, and deep shadowy gradients dominating the wall. The overall style is sophisticated contemporary fashion editorial photography, soft natural diffused daylight with gentle shadows emphasizing fabric textures, dog fur, and paint surface, realistic.
```

[[Fashion Editorial]] [[Young Male Portrait]]

---

### 98. 草莓地高级时装编辑肖像摄影提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-26  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张逼真的时尚编辑肖像照：一位身穿草莓印花连衣裙的女士置身于草莓田中，重点突出她唇上草莓汁的微妙光泽。

![草莓地高级时装编辑肖像摄影提示](https://cms-assets.youmind.com/media/1772174126653_4xqrx2_HCHNRo4XUAAgYpp.jpg)

```
{
 "meta": {
 "project": "Strawberry_Field_Editorial_Bold",
 "model_intent": "photoreal_high_fashion",
 "language": "en",
 "notes": "Romantic countryside fashion portrait with subtle strawberry juice detail on lips. Sensual yet elegant summer editorial."
 },

 "prompt": {
 "logline": "A beautiful woman in a pink spaghetti-strap dress with tiny strawberry prints stands in a sunlit strawberry field, holding a basket of fresh berries, with subtle strawberry juice glossing her lips in a bold yet elegant fashion editorial style.",

 "subject": {
 "gender": "female",
 "pose": "holding woven basket at waist level, slightly tilting head",
 "expression": "soft but confident, lips slightly parted",
 "wardrobe": [
 "light pink spaghetti-strap summer dress",
 "mini strawberry print pattern",
 "flowing cotton fabric",
 "soft pink headscarf tied delicately"
 ],
 "beauty_style": [
 "natural freckles",
 "glowy sun-kissed skin",
 "subtle flushed cheeks",
 "strawberry juice gloss lightly staining lips",
 "barely smudged natural red tint"
 ],
 "hair": "long dark hair softly flowing beneath scarf"
 },

 "detail_focus": {
 "lip_detail": "natural strawberry juice sheen with subtle deep red tint",
 "effect": "fresh, glossy, organic, not exaggerated",
 "texture": "realistic moisture reflection under sunlight"
 },

 "environment": {
 "location": "lush strawberry field rows",
 "background": [
 "green leaves with ripe red berries",
 "soft countryside horizon",
 "gentle breeze movement"
 ],
 "atmosphere": "warm early summer harvest glow"
 },

 "composition": {
 "orientation": "vertical portrait",
 "framing": "medium close-up",
 "focus": "sharp on lips and strawberries",
 "background_blur": "soft creamy bokeh"
 },

 "camera": {
 "shot_type": "editorial fashion portrait",
 "movement": "steady handheld realism",
 "angle": "slightly below eye level for subtle power presence"
 },

 "lens": {
 "focal_length_mm": 85,
 "aperture": "f/1.8",
 "sensor": "full-frame",
 "depth_of_field": "shallow with creamy background separation"
 },

 "lighting": {
 "style": "golden hour natural sunlight",
 "key_light": "warm side sunlight creating soft glow",
 "fill": "gentle bounce from greenery",
 "highlight_control": "controlled gloss reflection on lips",
 "shadow_quality": "soft cinematic shadows"
 },

 "color_palette": {
 "primary": [
 "soft blush pink",
 "deep strawberry red",
 "fresh leafy green"
 ],
 "grade": {
 "white_balance": "warm daylight (~5500K)",
 "saturation": "enhanced reds, balanced skin tones",
 "tone_curve": "soft cinematic contrast with lifted mids"
 }
 },

 "texture_details": [
 "visible strawberry seeds",
 "woven basket texture",
 "fabric movement in breeze",
 "natural skin pores",
 "subtle lip moisture detail"
 ],

 "quality_tags": [
 "photorealistic",
 "high fashion editorial",
 "romantic countryside",
 "bold lip detail",
 "cinematic natural light",
 "luxury summer campaign"
 ]
 },

 "negative_prompt": [
 "overly glossy lipstick",
 "h
```

[[Fashion Editorial]]

---

### 99. 奢华酒店大堂里的女人

**Author**: [Stark](https://x.com/katmanai)  **Date**: 2026-02-22  **Language**: en

> 一个为 Nano Banana Pro 设计的详细图像生成提示，描述了一位年轻女性，她具有特定的面部特征和着装（闪闪发光的紫色无肩带上衣、深色短裤、缀饰高跟凉鞋），坐在一张图案地毯上，身处豪华酒店大堂。该提示还详细说明了背景元素、灯光和构图。

![奢华酒店大堂里的女人](https://cms-assets.youmind.com/media/1771828719968_f1evol_HBvGwvyWMAATLtW.jpg)

```
{
  "prompt": "A young woman with long brown hair, whose face is based on the provided reference image, is sitting on a patterned rug in a luxurious hotel lobby. She is wearing a sparkling purple strapless top and dark shorts, with embellished high-heeled sandals on her feet. Her legs are extended forward, and she is holding a small silver clutch bag. She leans back slightly, resting one hand on the rug. The background features a large grey marble wall, warm ambient lighting, and blurred elements of the upscale interior."
}
```

[[Fashion Editorial]] [[Glamour Portrait]]

---

### 100. 两位人物的室内生活方式肖像（结构化）

**Author**: [Rowund](https://x.com/rowundd)  **Date**: 2026-02-21  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana Pro 生成一张逼真的室内生活肖像，其中包含两位人物（Ariana Grande 和 Jenna Ortega / Selena Gomez 和 Miley Cyrus / Demi Lovato 和 Anya Taylor Joy）。该提示指定了精确的相机设置（35mm 等效焦距，低角度），每位人物复杂、不对称的姿势（一位坐在地毯上，一位坐在沙发上），以及详细的配套服装，包括特定的丝袜和厚底高跟鞋。

![两位人物的室内生活方式肖像（结构化）](https://cms-assets.youmind.com/media/1771741702724_79feez_HBtc-9QWIAA76Bx.jpg)
![两位人物的室内生活方式肖像（结构化）](https://cms-assets.youmind.com/media/1771741702696_x6w7d7_HBtc-waWsAEMQdF.jpg)
![两位人物的室内生活方式肖像（结构化）](https://cms-assets.youmind.com/media/1771741702783_3zb41i_HBtc_NCWMAE_nN2.jpg)

```
{   "prompt_type": "image_generation",   "language": "English",   "style": "photorealistic indoor lifestyle photography, soft natural light, cinematic realism, non-CGI",   "output": {     "image_count": 1,     "aspect_ratio": "portrait",     "resolution": "ultra high resolution",     "detail_level": "extreme",     "photorealism": "very high"   },   "camera": {     "shot_type": "two-subject seated portrait",     "camera_height_cm": 45,     "vertical_tilt_degrees": -8,     "horizontal_yaw_degrees": 0,     "roll_degrees": 0,     "lens": "35mm equivalent",     "distance_to_subject_1_m": 1.6,     "distance_to_subject_2_m": 1.9,     "focus": "sharp on faces, gentle falloff toward legs",     "depth_of_field": "moderate and natural"   },   "subjects": {     "count": 2,     "subject_1": {ariana grande       "age": "adult (20+)",       "position_reference": "photo 1",       "pose": {         "body": "seated low on a soft rug, leaning back against cushions",         "torso_angle_degrees": 25,         "legs": {           "right_leg": "bent and grounded",           "left_leg": "extended upward",           "extension_angle_degrees": 55,           "foot_angle_degrees": 12,           "crossing": "none"         },         "arms": "relaxed, asymmetrical",         "head": {           "tilt_degrees": 5,           "gaze": "direct to camera",           "expression": "soft smile"         }       },       "outfit": {         "reference": "photo 3",         "top": "fitted long-sleeve pastel yellow knit top",         "skirt": "short black A-line skirt",         "hosiery": "black semi-transparent floral lace tights",         "socks": "yellow ankle socks with lace trim",         "shoes": "white platform heels, 15cm heel"       }     },     "subject_2": { jenna ortega       "age": "adult (20+)",       "position_reference": "photo 2",       "pose": {         "body": "seated upright on a sofa",         "torso_angle_degrees": 10,         "legs": {           "one_leg": "folded on sofa",           "other_leg": "extended forward",           "extension_angle_degrees": 35,           "foot_angle_degrees": 8,           "crossing": "none"         },         "arms": "one hand on thigh, one supporting on sofa",         "head": {           "tilt_degrees": 3,           "gaze": "toward camera",           "expression": "calm and composed"         }       },       "outfit": {         "reference": "photo 4",         "top": "light yellow fitted long-sleeve top with black underlayer at waist",         "skirt": "short structured black skirt",         "hosiery": "light yellow semi-transparent tights",         "socks": "pastel white crew socks",         "shoes": "white Mary Jane platform heels, 15cm heel"       }     }   },   "environment": {     "setting": "bright cozy living room",     "elements": [       "fabric sofa",       "soft cushions",       "plush rug",
```

[[Fashion Editorial]] [[Low Angle Shot]]

---

### 101. 白金发色女性池畔的详细 JSON 提示词

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-02-21  **Language**: en

> 一个高度结构化的 JSON 提示，用于 Nano Banana Pro 生成一张垂直的、写实风格的图像：一位年轻女性，留着铂金色长发，身穿轻薄的浅淡绿色比基尼，在泳池边摆姿势，对纹身和场景有严格的限制。

![白金发色女性池畔的详细 JSON 提示词](https://cms-assets.youmind.com/media/1771741704329_tsxdl8_HBsgGARWIAA1fvb.jpg)
![白金发色女性池畔的详细 JSON 提示词](https://cms-assets.youmind.com/media/1771741704387_epf521_HBsgGD9WcAAayyJ.jpg)

```
{
  “subject”: {
    “description”: “A vertical photograph of a young woman with long platinum blonde hair, posing poolside.”,
    “body”: {
      “physique”: “She has a slender, toned figure with a visible belly button piercing, free of any tattoos.”,
      “pose”: “Standing slightly angled to the side, looking directly at the camera with a sultry expression. Her left hand touches the side of her bikini bottom, while her right hand holds the strap near her hip. Her head is tilted slightly.”,
      “features”: “Long, wavy platinum blonde hair cascading over her shoulders. She has a pink frangipani flower tucked behind her left ear. Her skin is flawless and smooth, without any tattoos on her arms, torso, or legs.”
    },
“wardrobe”: {
      “outfit”: “A skimpy, light pastel green string bikini. The top is a triangle style, and the bottom is a high-cut thong style with thin side straps.”
    }
  },
  “pose_action”: “Posing poolside, looking at the camera while adjusting her bikini bottom.”,
  “scene”: {
    “environment”: “A bright, sunny poolside setting.”,
    “elements”: “She is standing next to lush green tropical plants and foliage. In the background, there’s a glimpse of a white tiled pool edge and bright sunlight suggesting a warm, clear day.”,
    “composition”: “Vertical 9:16 aspect ratio photograph capturing the subject from the mid-thigh up.”
  },
  “lighting”: {
    “setup”: “Bright, natural sunlight.”,
    “details”: “The sunlight is strong, casting soft shadows and highlighting the texture of her skin and the vibrant green of the plants. The light catches her hair and the flower.”
  },
“camera”: {
    “technical”: “High-resolution photograph with a sharp focus on the subject and a slightly blurred background (bokeh) from the plants. Realistic colors and natural skin tones.”,
    “aspect_ratio”: “9:16”,
    “constraints”: [
      “CRITICAL: The subject must have NO TATTOOS.”,
      “CRITICAL: Hair must be PLATINUM BLONDE with a PINK FRANGIPANI FLOWER.”,
      “CRITICAL: Outfit must be the LIGHT GREEN STRING BIKINI.”,
      “CRITICAL: Setting must be SUNNY POOLSIDE with TROPICAL PLANTS.”,
      “The final image must be a photorealistic vertical 9:16 photograph.”
    ]
  }
}
```

[[Fashion Editorial]] [[Hyperrealistic Photography]] [[Vertical Portrait]]

---

### 102. 超逼真巴黎咖啡馆生活方式摄影

**Author**: [Iqra Saifi](https://x.com/IqraSaifiii)  **Date**: 2026-02-21  **Language**: en

> 一个为 Nano Banana Pro 生成超逼真生活方式图像的详细 JSON 提示。场景设定在巴黎一家户外咖啡馆，埃菲尔铁塔清晰可见，一位年轻女子身着白色结构感迷你连衣裙，姿态俏皮，展现出别致的审美。提示中明确了光线（柔和的午后阳光）、相机设置（35mm/50mm 镜头，f/2.8-f/4 光圈）以及高纹理保真度。

![超逼真巴黎咖啡馆生活方式摄影](https://cms-assets.youmind.com/media/1771741697713_h0on9g_HBn27ztbgAEjE9J.jpg)

```
"prompt_type": "Ultra-Photorealistic Lifestyle Photography",
  "subject": {
"description": "Young woman in the reference image with a chic, luxurious aesthetic",
"hair": "Same colour in the reference image, styled in a messy yet elegant updo with loose strands framing the face",
"apparel": {
"outfit": "White structured mini dress or romper with a square neckline, short sleeves, and large white buttons down the front",
"accessories": [
"Black oval sunglasses",
"Silver luxury logo brooch on the left chest",
"Silver bracelet/watch on left wrist",
"Small rings"
],
"footwear": "Not visible, implied chic heels or sandals"
},
"pose": "Seated on a cafe chair, legs crossed at the knee, body slightly angled towards the camera, right hand raised near the face in a 'blowing a kiss' or cute posing gesture, left hand resting on the chair frame, lips puckered slightly"
  },
  "environment": {
"location": "Outdoor street-side cafe in Paris",
"background": {
"landmark": "The Eiffel Tower visible in the distance down the street center",
"architecture": "Classic Parisian Haussmann-style limestone buildings with balconies",
"street": "Parked cars lining the right side, paved sidewalk"
},
"foreground_elements": {
"furniture": "Typical round bistro table, grey metal cafe chair",
"items": "Black quilted luxury handbag (resembling Lady Dior) sitting on the table, wine glasses, white napkins",
"decor": "Black and white striped awning overhead, signage reading 'DI VINO'"
}
  },
  "lighting": {
"type": "Natural daylight",
"quality": "Soft afternoon sun, creating gentle shadows and highlights on the subject's skin and dress",
"sky": "Blue sky with scattered white clouds"
  },
  "camera_settings": {
"style": "High-end lifestyle photography, influencer travel aesthetic",
"lens": "35mm or 50mm portrait lens",
"aperture": "f/2.8 to f/4 (keeping the subject sharp while softly blurring the distant background context)",
"resolution": "8k, Ultra HD",
"focus": "Sharp focus on the subject and immediate foreground",
"texture_quality": "High fidelity textures on the fabric of the dress, the quilted bag leather, and the stone buildings"
  },
  "mood": "Chic, elegant, cosmopolitan, relaxed luxury, travel wanderlust, Parisian dreamy"
}
```

[[Fashion Editorial]] [[Golden Hour Light]]

---

### 103. 结构化时尚肖像，姿势精准，服装细节考究

**Author**: [Rowund](https://x.com/rowundd)  **Date**: 2026-02-21  **Language**: en

> 一个高度结构化的 JSON 提示，用于 Nano Banana Pro，定义了一个超高分辨率、照片级的时尚肖像。它细致地描述了相机设置（50mm 镜头，f/5.6）、拍摄对象的姿势（坐在地板上，脚踝交叉）以及服装（淡粉色粗花呢迷你连衣裙、象牙色不透明连裤袜和手套）。

![结构化时尚肖像，姿势精准，服装细节考究](https://cms-assets.youmind.com/media/1771741697739_hbmqx3_HBrAlAaWEAArYBO.png)
![结构化时尚肖像，姿势精准，服装细节考究](https://cms-assets.youmind.com/media/1771741697780_2owo4k_HBrAkPZWsAAO2PH.png)
![结构化时尚肖像，姿势精准，服装细节考究](https://cms-assets.youmind.com/media/1771741697796_i8wdrb_HBrAkpKWIAA9Cp6.png)
![结构化时尚肖像，姿势精准，服装细节考究](https://cms-assets.youmind.com/media/1771741698845_a4qn0j_HBrAlQ_WwAM-inl.png)

```
{
  "prompt_type": "image_generation",
  "language": "English",
  "output": {
    "image_count": 1,
    "aspect_ratio": "portrait",
    "resolution": "ultra high resolution",
    "detail_level": "extreme",
    "photorealism": "very high"
  },
  "camera": {
    "shot_type": "full-body seated portrait",
    "camera_height": "slightly above floor level",
    "angle": "slight downward angle",
    "lens": "50mm",
    "focus": "sharp from face to feet",
    "depth_of_field": "moderate, subject fully clear"
  },
  "subject": {
    "type": "Young Woman",
    "pose": {
      "body_position": "seated on the floor, back gently resting against the wall",
      "torso": "upright with relaxed shoulders",
      "legs": {
        "position": "both legs extended forward",
        "crossing": {
          "status": "legs crossed",
          "exact_crossing": "right leg crossed over left leg at ankle level only",
          "anatomical_precision": "ankles crossed cleanly, knees not overlapping"
        },
        "feet": {
          "orientation": "toes pointing forward",
          "distance_from_camera": "slightly closer than torso, but not dominating the frame"
        }
      },
      "arms": {
        "position": "hands resting naturally on thighs",
        "gloves": "hands fully gloved"
      },
      "head": {
        "position": "centered above torso",
        "tilt": "very slight forward tilt",
        "gaze": "direct eye contact with the camera",
        "expression": "calm, composed, elegant"
      }
    }
  },
  "face": {
    "visibility": "fully visible",
    "skin": "smooth with realistic texture",
    "makeup": {
      "style": "soft glam",
      "eyes": "defined lashes, subtle eyeliner",
      "lips": "natural pink satin finish"
    }
  },
  "hair": {
    "color": "warm chestnut brown",
    "style": "long loose waves",
    "parting": "center part",
    "length": "reaching mid-torso",
    "accessories": "wide cream headband"
  },
  "outfit": {
    "dress": {
      "type": "tailored tweed mini dress",
      "color": "soft pastel pink",
      "fabric": "textured tweed",
      "details": {
        "buttons": "decorative gold buttons aligned vertically",
        "fit": "structured but elegant"
      }
    },
    "hosiery": {
      "type": "opaque tights",
      "color": "ivory / soft cream",
      "denier": "60–80 denier",
      "opacity": "fully opaque",
      "texture": "smooth matte microfiber",
      "finish": "velvety, uniform color",
      "fit": {
        "leg_fit": "even compression following natural leg anatomy",
        "ankle_fit": "clean, no bunching",
        "foot_coverage": "fully covering feet with seamless toe area"
      },
      "details": {
        "fabric_tension": "consistent stretch with no transparency",
        "surface": "no shine, soft matte appearance",
        "wrinkles": "minimal, only natural micro-folds at ankles"
      }
```

[[Fashion Editorial]] [[Studio Photography]] [[50mm Lens Portrait]]

---

### 104. 漫展 Cosplay 服装提示

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-02-21  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张年轻女性在室内展厅内自信摆姿势的图像，她身穿一件精致的黑色蕾丝和皮革风格服装。该提示详细说明了人物细节、服装材质、姿势、环境和灯光。

![漫展 Cosplay 服装提示](https://cms-assets.youmind.com/media/1771741713810_xwl2vl_HBqraDEasAALMHE.jpg)

```
{
  "scene_description": "A young woman posing confidently at what appears to be a convention or expo hall, wearing an elaborate black lace and leather-inspired outfit with thigh-high platform boots and long gloves. She stands in the center of a large indoor venue with blurred attendees and booths in the background.",

  "characters": [
    {
      "name": "Unknown",
      "age": "Early to mid 20s",
      "gender": "Female",
      "ethnicity": "Unclear (possibly Latina or mixed ethnicity)",
      "skin_tone": "Light to medium tan",
      "hair": {
        "style": "Long, straight hair pulled into a high ponytail with volume at the crown",
        "color": "Dark brown"
      },
      "clothing": {
        "head": "No hat; wearing large clear-framed eyeglasses",
        "torso": "Black lace and mesh bodysuit with structured bra cups, high neckline collar detail, heart-shaped cutout at the midriff, decorative beading and lace trim",
        "legs": "Sheer black lace panels at hips with dangling bead accents",
        "feet": "Black thigh-high platform boots with very high chunky heels",
        "materials": ["lace", "mesh", "leather or faux leather", "synthetic stretch fabric", "metal beading"]
      },
      "pose": "Standing upright with one hand resting on her hip and the other relaxed at her side, legs slightly apart in a confident stance",
      "facial_expression": "Neutral to confident expression, lips slightly pursed, direct eye contact with the camera",
      "accessories": [
        "Large dangling silver chandelier earrings",
        "Clear-framed eyeglasses",
        "Long black opera gloves extending above the elbows"
      ],
      "held_objects": [],
      "position_in_scene": "Foreground, center",
      "emotions": ["confident", "poised", "self-assured"]
    }
  ],

  "environment": {
    "setting": "Indoor convention or expo hall",
    "background_elements": [
      "Blurred crowd of attendees walking",
      "Vendor booths with banners and posters",
      "Tables covered with cloths",
      "Large open walkway"
    ],
    "architectural_features": [
      "High industrial ceiling",
      "Rows of ceiling lights",
      "Polished concrete floor"
    ],
    "weather": "Not visible (indoor setting)",
    "lighting": {
      "type": "Artificial",
      "sources": ["Overhead ceiling lights"],
      "shadows": "Soft and diffused beneath subject",
      "reflections": "Subtle reflections on polished floor and glossy boots"
    },
    "atmosphere": "Busy but blurred, convention ambiance with shallow depth of field"
  },

  "objects": [
    {
      "name": "Convention Booths",
      "type": "Furniture/Display",
      "position": "Background, left and right",
      "appearance": "Tables with banners and vertical posters behind them",
      "materials": ["fabric tablecloth", "vinyl banners", "paper posters"],
      "interaction": "No direct interaction"
    },
    {
      "name": "Overhead Lights",
      "typ
```

[[Fashion Editorial]] [[Confident Pose]]

---

### 105. 动态人像，电影级运动模糊

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-02-21  **Language**: en

> 一个为 Nano Banana Pro 设计的提示，专注于创作动态、高对比度的时尚编辑肖像，利用电影般的运动模糊、慢速快门效果和抽象运动，以打造现代、病毒式的视觉美学。

![动态人像，电影级运动模糊](https://cms-assets.youmind.com/media/1771741695863_zj3q3t_HBqQj8EaoAAMHsL.jpg)
![动态人像，电影级运动模糊](https://cms-assets.youmind.com/media/1771741695841_7k8frw_HBqQj8LbgAA5ZwW.jpg)
![动态人像，电影级运动模糊](https://cms-assets.youmind.com/media/1771741695879_b5ws24_HBqQj8HbcAAOM6D.jpg)
![动态人像，电影级运动模糊](https://cms-assets.youmind.com/media/1771741696658_jfwrpw_HBqQj8EaMAAfzix.jpg)

```
Dynamic portrait with cinematic motion blur, editorial fashion photography, slow shutter effect, motion streaks. High contrast lighting, color grading aesthetic, abstract movement. Modern visual storytelling, artistic style, creative direction, experimental visuals. Viral image style, AI-generated fashion, visual impact, dramatic silhouette, trending photography aesthetics.
```

[[Fashion Editorial]] [[High Contrast Photography]] [[Cinematic Style]]

---

### 106. 时尚大片：下探

**Author**: [D. Humann](https://x.com/dhumann)  **Date**: 2026-02-13  **Language**: en

> 一个详细的提示，用于生成一张时尚大片风格的图片：一位商务人士优雅地坐在电梯旁的地板上，看起来疲惫但沉着，旁边打开的笔记本电脑上显示着财务预测，营造出一种企业美学。

![时尚大片：下探](https://cms-assets.youmind.com/media/1771050449043_t0f87k_HBAhN5ZaIAAmMbq.jpg)

```
The subject is wearing a blue-grey sleeveless business dress with black stiletto heels, a red lanyard loosely around her neck with an ID badge attached, and the same accessories as the uploaded person. The subject is seated gracefully on the floor, leaning slightly against a wall next to an elevator. Both legs are bent, wearing nude stockings, creating an elegant yet relaxed posture. Her expression is calm and composed but slightly exhausted, looking up toward the ceiling with a subtle air of exasperation. The minimalist background features a sleek, modern hallway with an elevator, emphasizing clean lines and smooth surfaces. Nearby, a beige handbag, smartphone, glasses, and an open laptop are placed on the floor. The laptop screen displays the UI of a professional investment app with downward projections, contributing to the modern corporate aesthetic. The lighting is soft and natural, illuminating the subject and creating a serene, high-fashion editorial atmosphere.
```

[[Fashion Editorial]]

---

### 107. 安娜·德·阿玛斯电影垃圾拼贴肖像

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-02-12  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张具有暗黑垃圾摇滚美学的超逼真编辑时尚肖像，主体置于由黑灰色剪纸和微妙轮廓光组成的叠层艺术拼贴墙前。

![安娜·德·阿玛斯电影垃圾拼贴肖像](https://cms-assets.youmind.com/media/1770964559139_7aarfb_HA9-mQQbsAYaNTM.jpg)

```
{
  "meta": {
    "title": "Cinematic Grunge Collage Portrait",
    "quality": "ultra photorealistic",
    "resolution": "8K",
    "aspect_ratio": "2:3",
    "camera": "full-frame DSLR",
    "lens": "50mm prime lens",
    "aperture": "f/1.8",
    "lighting": "cinematic studio lighting with soft rim light",
    "color_grade": "dark grunge aesthetic, muted blacks and cool grays with subtle warm skin tones",
    "texture": "subtle analog film grain",
    "style": "editorial fashion photography, high detail, realistic skin texture"
  },

  "subject": {
    "gender": "female",
    "age": "young adult (early 20s)",
    "body_type": "slim, natural proportions",
    "pose": {
      "description": "confident fashion pose",
      "right_hand": "gently touching or resting near her face",
      "left_hand": "casually placed inside pants pocket",
      "posture": "relaxed yet assertive stance, shoulders slightly angled"
    },
    "expression": "calm, self-assured, subtle confident gaze directed at camera",
    "hair": {
      "type": "voluminous curly hair",
      "length": "shoulder-length",
      "texture": "defined curls with natural bounce",
      "color": "dark brown"
    },
    "outfit": {
      "top": {
        "type": "loose black shirt",
        "fabric": "soft cotton with natural folds",
        "fit": "slightly oversized",
        "details": "minimalist, matte texture"
      },
      "bottom": {
        "type": "light beige pants",
        "fit": "tailored yet relaxed",
        "fabric": "smooth woven fabric",
        "color_tone": "warm neutral beige"
      }
    }
  },

  "background": {
    "type": "artistic collage wall",
    "theme": "black-and-gray grunge aesthetic",
    "elements": [
      {
        "object": "police car",
        "style": "monochrome newspaper-style cutout",
        "placement": "partially layered behind subject"
      },
      {
        "object": "Pegasus (flying horse)",
        "style": "mythological illustration, black-and-white ink style",
        "placement": "upper section of collage"
      },
      {
        "object": "perfume bottle",
        "style": "high-fashion advertisement cutout",
        "placement": "mid-right background"
      },
      {
        "object": "newspaper text clippings",
        "style": "random layered typography fragments",
        "texture": "slightly torn paper edges"
      },
      {
        "object": "record label logo",
        "style": "vintage vinyl record stamp aesthetic",
        "placement": "subtle overlay near lower corner"
      },
      {
        "object": "abstract paint textures",
        "style": "dark brush strokes and splatter effects",
        "color_palette": "charcoal, gray, muted white"
      }
    ],
    "depth_effect": "slight blur and parallax depth to separate subject from background"
  },

  "effects": {
    "outline": {
      "type": "soft white glow",
      "intensity": "subtle",
```

[[Fashion Editorial]] [[Rim Lighting]]

---

### 108. 时尚编辑肖像系列网格模板

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-02-12  **Language**: en

> 一个结构化的 JSON 模板，旨在生成多帧编辑时尚肖像系列（网格样式）。它概述了常见的元素，如光线（直射闪光/黄金时段、高对比度）和真实感，并为两个不同的帧提供了可定制的插槽，允许用户为网格的每个部分定义特定的姿势、角度和视觉提示，同时保持面部一致性。

![时尚编辑肖像系列网格模板](https://cms-assets.youmind.com/media/1770964580040_ugnq6k_HA9rUZGbsAU8H8W.jpg)
![时尚编辑肖像系列网格模板](https://cms-assets.youmind.com/media/1770964580016_mxa9j4_HA9rUbYbAAARY6l.jpg)

```
{
  "meta": {
    "purpose": "Editorial fashion portrait series (multi-frame grid style, high virality)",
    "version": "Nano Banana Pro optimized",
    "aspect_ratio": "16:9 or 1:1 grid"
  },
  "common_elements": {
    "subject": "[e.g., Young woman with {argument name=\"hair description\" default=\"long dark hair\"}, {argument name=\"skin tone\" default=\"fair skin\"}]",
    "face_constraint": "Preserve original face structure and proportions exactly from reference",
    "lighting_and_style": "Direct flash or golden hour, high contrast, vintage/cinematic aesthetic, saturated colors, hyper-realistic textures, 8K"
  },
  "frames": [
    {
      "frame_id": 1,
      "position": "{argument name=\"frame 1 position\" default=\"Top Left\"}",
      "visual_prompt": "{argument name=\"frame 1 visual prompt\" default=\"Low-angle shot, subject perched on object, leg extended dramatically toward camera, sharp foreground texture\"}",
      "pose_details": "[e.g., Leaning back, looking away casually]"
    },
    {
      "frame_id": 2,
      "position": "[e.g., Top Right]",
      "visual_prompt": "[e.g., High-angle shot looking down, hand on prop, wide lens distortion]",
      "pose_details": "[e.g., Seated, head tilted up]"
    }
  ],
  "negative": ["blurry", "plastic skin", "distorted face", "low res", "cartoon", "artifacts"]
}
```

[[Fashion Editorial]] [[Golden Hour Lighting]] [[Identity Consistency]] [[Direct Flash]]

---

### 109. 迪斯科梦想时尚社论肖像

**Author**: [Miz](https://x.com/mizq06)  **Date**: 2026-02-12  **Language**: en

> 生成一张红发女性手持巨大银色迪斯科球的时尚编辑肖像照的提示。背景是时尚杂志剪报和《Vogue》封面的拼贴画。指定使用影棚灯光，带直射闪光，高对比度，以及现代时尚摄影美学。

![迪斯科梦想时尚社论肖像](https://cms-assets.youmind.com/media/1770964569621_7uab0s_HA9gxHqbsAckjM_.jpg)
![迪斯科梦想时尚社论肖像](https://cms-assets.youmind.com/media/1770964569628_9iee5h_HA9gxHraMAAKSdU.jpg)

```
Editorial fashion portrait of a red-haired woman with voluminous curly hair wearing a deep red velvet bodysuit, holding a large silver disco ball. She stands in front of a wall covered with fashion magazine cutouts and Vogue covers, creating a collage backdrop. Studio lighting with direct flash, sharp focus, high detail, bold red lipstick, confident pose, modern fashion shoot, 35mm lens look, high contrast, clean white wall.
```

[[Fashion Editorial]] [[Studio Flash Lighting]]

---

### 110. 涂鸦背景下凌乱床上女性的电影肖像

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-02-12  **Language**: en

> 一个详细的提示，用于生成一张高质量的电影级中景特写肖像，描绘一位具有垃圾摇滚美学的女性，包括特定的服装、发型，以及一个充满活力的涂鸦背景和戏剧性的灯光。

![涂鸦背景下凌乱床上女性的电影肖像](https://cms-assets.youmind.com/media/1770964551011_tdijme_HA9EuP3bsAA0ScD.jpg)

```
A high-quality, cinematic medium close portrait of a me sitting on a messy bed. She is wearing a white t-shirt with a "{argument name="logo" default="Queen"}" logo and light blue, loose-fitting cargo pants. Her hair is styled in a messy bun, and she has a relaxed, direct gaze. The background is a vibrant wall covered with graffiti (featuring the word "{argument name="graffiti word" default="ZARA"}" in orange and blue) and numerous vintage posters of musicians and bands. The lighting is moody and dramatic. 8k, detailed, cinematic light, urban aesthetic, grunge fashion.
```

[[Fashion Editorial]] [[Dramatic Lighting]] [[Grunge Aesthetic]]

---

### 111. 低角度时尚肖像：皮草大衣与裸露双腿

**Author**: [Stark](https://x.com/katmanai)  **Date**: 2026-02-12  **Language**: en

> 一个用于生成时尚大片编辑照片的提示，从低角度拍摄，聚焦于一位女性（身份信息保留自参考图像），她优雅地蹲伏在一件蓬松的金色-橙色长毛皮草大衣中，突出她裸露的双腿和穿着白色细带凉鞋的精致双脚。

![低角度时尚肖像：皮草大衣与裸露双腿](https://cms-assets.youmind.com/media/1770964546932_5cn7qh_HA6m63wX0AEIFRZ.jpg)

```
{
  "positive_prompt": "A high-fashion editorial photograph, captured from a low angle, showing a woman with the likeness of the person in the reference image. She is crouching elegantly, wearing a voluminous, textured golden-orange shaggy fur coat that billows around her. The main focus is on her bare legs and beautifully detailed feet in white strappy sandals, positioned prominently in the foreground. Her toenails have a clean pedicure. The lighting is soft studio light in a minimalist, off-white concrete room. The woman gazes confidently at the camera.",
  "negative_prompt": "blurry, low quality, distorted, ugly, deformed feet, missing toes, extra toes, dirty, poorly rendered, nudity, explicit, watermark, text, signature",
  "face_reference_image": "image_1.png",
  "parameters": {
    "face_restoration": true,
    "face_reference_strength": 0.9,
    "guidance_scale": 7.5,
    "num_inference_steps": 30
  }
}
```

[[Fashion Editorial]] [[Crouching Pose]]

---

### 112. 花海中的浪漫时尚大片

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-11  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张俯视角度的时尚编辑照片，内容为一名女性躺在密集的亮粉色花海中。该提示指定了自上而下的构图、浅粉色连衣裙、柳条篮道具、黄金时段光线，以及为达到照片级真实感而严格遵守的解剖学准确性规则。

![花海中的浪漫时尚大片](https://cms-assets.youmind.com/media/1770878343532_iq3q16_HA5LAUFbsAUJATe.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "photoreal_fashion_editorial_flower_field_overhead",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_PINK_DRESS_FLOWER_BED_HEART_BAG"
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 4,
      "sharpness": "high",
      "grain": "subtle_analog"
    },
    "scene": {
      "concept": "overhead romantic fashion editorial of a woman lying in a dense flower bed",
      "environment": "lush ground cover packed with small hot-pink blossoms and green leaves, hints of purple flowers in corners, full-frame botanical texture",
      "composition": "top-down overhead shot, full-body diagonal pose, subject centered, floral carpet filling entire background, basket of pink flowers near chest/shoulder",
      "mood": "spring romance, dreamy, joyful, vibrant"
    },
    "subject": {
      "person": "adult woman",
      "expression": "bright joyful smile, relaxed eyes, confident and warm",
      "pose": "lying on her back in the flowers, one leg bent slightly, arms hugging a wicker basket of flowers close to the chest",
      "hair": "dark brown hair, styled neatly with soft volume, swept back from face",
      "makeup": "fresh glam: soft blush, glossy pink lips, subtle highlight, defined lashes",
      "wardrobe": {
        "dress": "light pink off-shoulder mini dress with a large bow detail on the bodice, structured waist, soft skirt folds, crisp fabric texture and highlights"
      },
      "shoes": "light pastel heels or sandals, elegant and minimal",
      "accessories": "delicate ring on finger, minimal jewelry"
    },
    "props": {
      "basket": "wicker basket overflowing with pink flowers (carnations/roses mix), placed near the subject’s upper torso",
      "handbag": "transparent pink heart-shaped clutch placed on top of the flowers in the basket, glossy plastic texture with realistic reflections"
    },
    "camera": {
      "shot_type": "overhead fashion editorial",
      "lens": "35mm",
      "aperture": "f/4",
      "focus": "subject face and dress sharp, flowers crisp with slight natural falloff",
      "framing": "4:5 vertical, full-body top-down"
    },
    "lighting": {
      "time_of_day": "golden hour or late afternoon",
      "key_light": "strong warm sunlight with natural leaf shadows across the scene",
      "contrast": "medium-high with crisp sunlit highlights on skin and dress",
      "skin_tone": "realistic, warm glow, visible natural texture"
    },
    "color_grading": {
      "palette": "hot pink flowers + fresh greens + pastel pink dress",
      "look": "bright editorial, clean whites, punchy florals, warm sun tone",
      "contrast": "medium-high",
      "saturation": "vivid but controlled (no neon clipping)"
    },
    "quality_rules": {
      "anatomy_accuracy": "strict",
      "hands": "correct fingers, natural joints, no extra digits",
```

[[Fashion Editorial]]

---

### 113. 祖母绿缎面连衣裙时尚大片

**Author**: [Aylin](https://x.com/Ai_aylinfc)  **Date**: 2026-02-11  **Language**: en

> 一个详细的时尚摄影提示，用于生成一张社论图片：一位年轻女性身穿优雅的祖母绿缎面中长连衣裙，裙摆高开衩，站在一座现代建筑外，强调面料质感、光线和精致自信的表情。

![祖母绿缎面连衣裙时尚大片](https://cms-assets.youmind.com/media/1770878353501_3lwk7t_HA4shkHaYAM1gvX.jpg)

```
Young woman with long light brown hair styled in a sleek high ponytail, a few soft strands gently framing her face, wearing an elegant emerald green midi dress crafted from luxurious satin or silk that catches the light with a subtle luminous sheen. The dress features a deep V-neck wrap front that enhances the silhouette, short softly puffed sleeves adding a romantic touch, and a perfectly cinched waist defined by a matching tie belt that creates a flattering hourglass shape. The skirt falls gracefully below the knees in a flowy, gathered design, moving naturally with every step, with an asymmetrical high slit on one side that reveals a glimpse of her leg and adds a refined yet bold edge.

She stands gracefully outside a sleek modern building with clean architectural lines and glass panels reflecting the daylight, giving a sophisticated fashion event atmosphere. She wears delicate gold strappy heeled sandals that complement the rich emerald tone of the dress, along with minimal elegant jewelry for a polished finish. Her makeup is natural and glowing—soft foundation, subtle contour, lightly flushed cheeks, neutral eyeshadow, defined lashes, and a muted rose lip color. Her expression is soft yet confident, poised and effortlessly stylish.

Photorealistic, ultra-detailed, sharp focus, realistic skin texture, natural daylight illumination, cinematic depth, editorial fashion photography style, 85mm lens look, shallow depth of field, luxury event vibe, high resolution, crisp fabric texture, subtle fabric folds, natural body proportions, balanced composition.
```

[[Fashion Editorial]] [[Fabric Texture Detail]]

---

### 114. 台球桌上的前卫时尚摄影提示

**Author**: [Natty Windstorm](https://x.com/NattyWindstorm)  **Date**: 2026-02-11  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张高分辨率的时尚编辑照片：一名女性躺在绿色台球桌上，身穿豹纹服装，光线 moody 且富有电影感。

![台球桌上的前卫时尚摄影提示](https://cms-assets.youmind.com/media/1770878326350_qg79iy_HA4bkeKagAEjWzT.jpg)
![台球桌上的前卫时尚摄影提示](https://cms-assets.youmind.com/media/1770878326613_07efhl_HA4bkeJbEAAb9VW.jpg)

```
{
  "type": "image_prompt",
  "description": {
    "subject": "A young woman with long blonde hair lies on her back, looking toward the camera with a playful, confident expression and one eye slightly closed.",
    "clothing": "She wears a leopard-print fitted top and matching shorts with small black bow details.",
    "pose": "Lying flat with hair spread out, one hand resting on her chest while the other arm reaches forward toward the camera, creating a strong sense of depth.",
    "setting": "A green billiards table surface.",
    "props": [
      "Scattered red and yellow billiard balls around her",
      "A pool cue positioned along the side"
    ],
    "lighting": "Moody, cinematic lighting with warm highlights and soft shadows.",
    "mood": "Playful, bold, stylish, slightly edgy.",
    "color_palette": [
      "green",
      "leopard brown",
      "yellow",
      "red",
      "black"
    ],
    "style": "High-resolution editorial fashion photography with a dramatic, modern aesthetic",
    "camera": {
      "framing": "top-down medium shot",
      "angle": "overhead perspective",
      "focus": "shallow depth of field emphasizing the subject and foreground hand"
    },
    "details": "Visible tattoos on arms and legs, necklace with a cross pendant, expressive hand gesture toward the lens"
  }
}
```

[[Fashion Editorial]]

---

### 115. 浪漫时尚杂志肖像提示

**Author**: [Miz](https://x.com/mizq06)  **Date**: 2026-02-11  **Language**: en

> 一个结构化的 JSON 提示，用于生成一张高分辨率的时尚编辑肖像照，描绘一位身穿粉色缎面连衣裙的年轻女性，照片中融入了浪漫和异想天开的元素，如一个大泰迪熊和红玫瑰。

![浪漫时尚杂志肖像提示](https://cms-assets.youmind.com/media/1770878326351_rwv5hl_HA4X6DnbIAEUzHa.jpg)
![浪漫时尚杂志肖像提示](https://cms-assets.youmind.com/media/1770878326418_rajfpw_HA4X6D4a0AAnnO_.jpg)

```
{
  "type": "image_prompt",
  "description": {
    "subject": "A young woman with fair skin and long auburn hair sits on a decorative bench, looking directly at the camera with a calm, neutral expression.",
    "clothing": "She wears a pink satin slip-style dress with thin ribbon straps and a ruffled hem.",
    "pose": "Seated with relaxed posture, one hand resting near her chest and the other holding a single red rose.",
    "setting": "Indoor studio setting with a soft neutral background.",
    "props": [
      "An oversized beige teddy bear positioned closely behind her",
      "A bouquet of red roses placed beside her"
    ],
    "lighting": "Soft, even studio lighting with gentle highlights on skin and fabric.",
    "mood": "Romantic, intimate, slightly whimsical.",
    "color_palette": [
      "pink",
      "red",
      "beige",
      "soft white"
    ],
    "style": "High-resolution fashion photography, editorial portrait style",
    "camera": {
      "framing": "medium shot",
      "angle": "eye level",
      "focus": "sharp subject focus with minimal background distraction"
    }
  }
}
```

[[Fashion Editorial]] [[High Resolution Portrait]] [[Pink Satin Dress]]

---

### 116. 三联画构图提示，用于抽象时尚专题报道

**Author**: [KTDS](https://x.com/KTDS_Official)  **Date**: 2026-02-08  **Language**: en

> 一个复杂的多面板提示，旨在生成一个垂直三联画（三个堆叠图像），描绘同一个高光泽、雕塑感的主题。该提示通过极端的特写镜头技术（低角度、微距、倾斜角度、选择性模糊）来规定不断升级的亲密感和强度，从而在不依赖环境或道具的情况下，创造出一种动态、抽象的时尚编辑风格。

![三联画构图提示，用于抽象时尚专题报道](https://cms-assets.youmind.com/media/1770619708000_wd22mq_HAoLvZvawAA-v1y.jpg)

```
THE TASK
Act as a world-class fashion photographer shooting a defining editorial campaign. Create a cohesive 3-panel vertical triptych (stacked top, middle, bottom) of the same subject. The sequence escalates intimacy and intensity through extreme proximity, revealing tactile hyper-realism and restrained dynamic power purely via photographic technique — no environmental changes, no added elements.
TRIPTYCH COMPOSITION
(VERTICAL STACK – ESCALATING CLOSE-UP INTENSITY)
Top Panel – Presence (Intense Dominant Close-Up)
Dynamic low 3/4 angle close-up (camera below the main form, tilted upward) to create looming, commanding scale.
Tight crop: the subject’s primary focal feature and sharp contours dominate; one side falls into deep shadow.
Subtle implied motion via slight rotational tilt and micro-blur only on far-edge highlights — keep the central zone razor-sharp.
Specular streaks rake across glossy surfaces like wet lacquer, emphasizing curvature and fine material imperfections.
Background: pure high-key white with faint gradient falloff — identical across all panels, no environmental cues.
Middle Panel – Control (Kinetic Structural Sweep)
Canted-angle macro from the side with aggressive perspective distortion.
Crop frames the central structural zone, with key elements off-center and partially cut by frame edges.
Highlights slice diagonally across contoured channels and ridges due to the dramatic angle.
Very shallow depth of field: nearest surface tack-sharp, farther planes melt softly to suggest velocity and tension.
Same pure high-key white background and exact tonal range — variation achieved solely through camera angle and lens proximity.
Bottom Panel – Essence (Extreme Graphic Detail)
Extreme macro from an aggressive angle evoking a controlled whip-pan. Choose one signature detail and make it feel alive with implied motion while remaining graphically pristine:

A protruding or extending element shot from below, strongly foreshortened, reaching toward the lens,
Or a central geometric/functional feature shot on a steep diagonal, highlights spiraling like motion trails,
Or a sharp edge or blade-like contour shot from behind, catching a razor-thin specular line.

Apply controlled directional blur only to a secondary trailing plane; keep the primary micro-texture impeccably crisp.
Frame so tight it becomes near-abstract: beveled edges, micro-scratches, gloss pooling, subtle material stress marks, fine imperfections.
No debris, no additional elements — identical high-key white background maintained.
STYLING & BOLD CHOICES (CRITICAL)
Subject: {argument name="subject material" default="any high-gloss, sculpted form with precise contours and reflective surfaces"}.
No additional objects, characters, props, text, or logos.
All sense of energy and motion derived exclusively from camera technique: low/canted angles, foreshortening, shallow depth of field, controlled selective blur, and highlight flow.
Identical lighting rig across all three panels — consistent
```

[[Fashion Editorial]] [[Extreme Close-Up]]

---

### 117. 超逼真吻痕美妆大片

**Author**: [Maya](https://x.com/mayadelmare)  **Date**: 2026-02-07  **Language**: en

> 生成一张超现实主义美妆时尚编辑照片的高度具体提示，要求模特的身份和特征与上传的参考图片匹配，照片中模特面部和胸部带有戏剧性的妆容和逼真的红色唇印。

![超逼真吻痕美妆大片](https://cms-assets.youmind.com/media/1770532767376_zw55oz_HAj3jXNW4AAlrWu.jpg)
![超逼真吻痕美妆大片](https://cms-assets.youmind.com/media/1770532767375_0cpdaq_HAj3dVEXEAEbC-W.jpg)

```
Ultra-realistic beauty fashion editorial photograph, taking reference from the uploaded image (exact facial features, skin tone, makeup placement, hair color and texture, proportions, accessories).

A confident woman posed against a clean white studio background, wearing a red beret and oversized red heart-shaped sunglasses with translucent lenses. She lifts the sunglasses slightly with a red satin glove, gazing past the camera with a bold, expressive look.

Her makeup is dramatic and editorial: glossy deep red lips, defined brows, clean skin texture. Red lipstick kiss marks are stamped across her face, neck, shoulders, and upper chest — realistic transfer texture, uneven edges, natural opacity variation.

Soft studio lighting with gentle shadows, even exposure, accurate reds without oversaturation.

True-to-life skin texture with visible pores, natural highlights, realistic lipstick shine, authentic fabric folds in gloves and beret.

Shot on a full-frame DSLR, 85mm lens, f/4, beauty editorial realism, RAW photo look.

Feels like a real fashion magazine shoot confident, playful, provocative, not stylized or artificial.

NEGATIVE PROMPT:
AI-generated look, CGI, illustration, airbrushed skin, plastic texture, warped facial features, fake gloss, exaggerated highlights, symmetry artifacts, unreadable makeup texture, painterly style, HDR glow, uncanny valley, over-smoothing.
```

[[Fashion Editorial]] [[Hyperrealistic Photography]] [[Face Matching]]

---

### 118. 安娜·德·阿玛斯 (Ana de Armas) 身穿白衬衫的编辑肖像

**Author**: [Sadia](https://x.com/SadiaMalik182)  **Date**: 2026-02-05  **Language**: en

> 一个结构化的提示，用于生成安娜·德·阿玛斯（Ana de Armas）在极简主义摄影棚中的高端编辑肖像，重点是简洁美学、柔和灯光以及特定的服装细节，例如挺括的白色纽扣衬衫和金色蜜蜂形纽扣。

![安娜·德·阿玛斯 (Ana de Armas) 身穿白衬衫的编辑肖像](https://cms-assets.youmind.com/media/1770359977950_hcvljy_HAZg5vZW8AAM3BB.jpg)
![安娜·德·阿玛斯 (Ana de Armas) 身穿白衬衫的编辑肖像](https://cms-assets.youmind.com/media/1770359977952_tocao9_HAZg5v7XsAAc-ZM.jpg)
![安娜·德·阿玛斯 (Ana de Armas) 身穿白衬衫的编辑肖像](https://cms-assets.youmind.com/media/1770359977970_plsrhg_HAZg5s8WQAABfQu.jpg)

```
{
  "subject": {
    "person": "{argument name="person name" default="Ana de Armas"}",
    "facial_features": {
      "expression": "Soft, confident smile and neutral, relaxed gaze",
      "eyes": "Hazel-brown, expressive",
      "makeup": "Natural 'no-makeup' look, soft rose-tinted lips, subtle eyeliner, well-defined brows",
      "hair": "Chestnut brown with honey highlights, long, wavy, parted slightly off-center"
    },
    "attire": {
      "top": "Crisp white long-sleeved button-down shirt, structured pointed collar, gold bee-shaped decorative buttons or pins along the placket",
      "bottom": "High-waisted black tailored trousers",
      "jewelry": "Small gold hoop earrings, stacked gold rings on fingers"
    }
  },
  "composition": {
    "shot_type": "Medium shot / waist-up portrait",
    "poses": [
      "Front-facing with hand resting on stomach",
      "Hand tucked into pocket",
      "Hand raised slightly near shoulder displaying rings"
    ],
    "background": "Solid, clean, {argument name="background color" default="off-white / eggshell"} studio backdrop"
  },
  "technical_aesthetic": {
    "lighting": "Soft, even studio lighting with minimal shadows, bright and airy feel",
    "color_palette": ["White", "Black", "Gold", "Natural skin tones"],
    "style": "High-end editorial, professional headshot, minimalist, clean aesthetic",
    "quality": "Sharp focus, high resolution, realistic textures"
  }
}
```

[[Fashion Editorial]] [[Studio Portrait]] [[Soft Studio Lighting]] [[Minimalist Aesthetic]]

---

### 119. 天台时尚摄影的 JSON 提示

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-02-05  **Language**: en

> 一个结构化的 JSON 提示词，用于 Gemini Nano Banana Pro 生成一张高质量的、未经修饰的时尚编辑照片。照片内容为：一位时尚女性身着奢华街头服饰，在日落黄金时段的天台，重点突出都市奢华和自信的氛围。

![天台时尚摄影的 JSON 提示](https://cms-assets.youmind.com/media/1770359937516_2d3htr_HAXWX75acAMw6Fw.jpg)

```
{
  "type": "image_generation_prompt",
  "aspect_ratio": "4:5",
  "style": "raw, editorial fashion photography",
  "quality": "high",
  "subject": {
    "gender": "female",
    "description": "A stylish woman in luxury streetwear standing confidently on a rooftop",
    "pose": "relaxed but confident stance, facing camera with natural posture",
    "outfit": "high-end luxury streetwear fashion, modern and stylish"
  },
  "environment": {
    "location": "rooftop",
    "background": "wide city skyline",
    "scene": "urban landscape"
  },
  "lighting": {
    "time": "sunset golden hour",
    "style": "warm natural light with cinematic glow"
  },
  "photography": {
    "genre": "editorial fashion",
    "composition": "balanced framing, subject in focus, skyline visible",
    "depth_of_field": "shallow to moderate"
  },
  "mood": "confident, stylish, modern urban luxury"
}
```

[[Fashion Editorial]] [[Candid Style]] [[Urban Setting]] [[Luxury Streetwear]]

---

### 120. 汽车后备箱里的时尚大片与白玫瑰

**Author**: [Aditi Menon](https://x.com/Aditi_Menon_123)  **Date**: 2026-01-31  **Language**: en

> 一个结构化的提示，用于生成一组时尚编辑图片：场景设定在地下停车场，一个女孩坐在一辆黑色大 G 汽车的敞开后备箱里，后备箱里装满了白色玫瑰，强调闪光摄影和优雅的氛围。

![汽车后备箱里的时尚大片与白玫瑰](https://cms-assets.youmind.com/media/1769927659987_znkwyf_G_-kJ9caEAAfsnA.jpg)
![汽车后备箱里的时尚大片与白玫瑰](https://cms-assets.youmind.com/media/1769927659985_potbmg_G_-kJpXbEAAGqmz.jpg)

```
{
 "A girl sitting in the black open trunk of a Gelik in an underground parking lot, surrounded by many flowers; the entire trunk is filled with white roses. She is wearing a black tracksuit. Her hair is long, styled in the Old Money style. Her lips are painted soft matte pink, and her eyelashes are lush. She is looking at the flowers in the trunk, posing like a fashion shoot.",
      "pose": "Seated inside the trunk with legs bent slightly, hands lightly touching the flowers, looking at the roses with a gentle, contemplative expression."
    },
    "environment": {
      "location": "Underground parking lot",
      "lighting": "Flash photography, high contrast to highlight the girl and white roses, subtle reflections on the car's surface",
      "background": "Concrete walls and floor of parking lot, dim ambient light"
    },
    "objects": [
      {
        "type": "Car",
        "model": "{argument name="car model" default="Gelik"}",
        "color": "Black",
        "position": "Open trunk facing camera"
      },
      {
        "type": "Flowers",
        "species": "Roses",
        "color": "White",
        "placement": "Entire trunk filled, some spilling slightly around the girl"
      }
    ],
    "style": {
      "photography": "Fashion editorial, flash photography, cinematic",
      "format": "3:4",
      "mood": "Elegant, serene, high-end fashion vibe"
    },
    "reference_image_ids": ["<your_uploaded_photo_id>"]}
```

[[Fashion Editorial]] [[Flash Photography]]

---

### 121. 极简主义 Calvin Klein 时尚大片提示词

**Author**: [Pan](https://x.com/sebatheepan)  **Date**: 2026-01-30  **Language**: en

> 一个高度具体的提示，用于生成一张现代、干净、极简主义的时尚编辑图片，画面中一名女性身着 Calvin Klein 内衣躺在纯白色表面上，采用头顶漫射照明拍摄。

![极简主义 Calvin Klein 时尚大片提示词](https://cms-assets.youmind.com/media/1769841081992_p8gtkz_G_8xXeNWcAA6o32.jpg)
![极简主义 Calvin Klein 时尚大片提示词](https://cms-assets.youmind.com/media/1769841081988_x7e373_G_8xZpVWwAAbx-C.jpg)
![极简主义 Calvin Klein 时尚大片提示词](https://cms-assets.youmind.com/media/1769841082004_vjze97_G_8xYnBW4AMlOcz.jpg)
![极简主义 Calvin Klein 时尚大片提示词](https://cms-assets.youmind.com/media/1769841082795_xo5gvm_G_8xarlW0AABpOK.jpg)

```
SHOT:  • Composition: Overhead full-body shot, subject centered, vertical orientation  • Camera Settings: ISO 400, f/4.0, 1/125 s, full-frame sensor  • Film Grain: None, clean digital image  LENS EFFECTS:  • Optics: Sharp focus on subject, no distortion  • Artifacts: None  • Depth of Field: Deep, all subject in focus  SUBJECT:  • Description: Woman lying on back with arms above head, long dark hair spread, neutral expression  • Wardrobe: White {argument name="brand" default="Calvin Klein"} long sleeve crop top, white Calvin Klein briefs, white socks, white sneakers  • Grooming: Natural makeup, long dark loose hair, clear skin  SCENE:  • Location: Plain white background surface  • Time of Day: Neutral indoor lighting, no natural light indication  • Environment: Minimalist studio setting  VISUAL DETAILS:  • Action: Reclining pose, legs slightly crossed at ankles  • Props: None  • Physics: Hair spread naturally on floor, relaxed posture  CINEMATOGRAPHY:  • Lighting: Soft, diffuse lighting with minimal shadows  • Tone: Neutral, clean, minimalistic  • Color Palette: Predominantly white with skin tones and dark hair contrast  TEXT ELEMENTS:  • Visible Text: Calvin Klein logo on waistband of top and briefs  • Typography: Sans-serif, bold lettering  • Placement: Logo centered and repeated on garment bands  STYLE:  • Visual Aesthetic: Modern, clean, minimalistic, fashion editorial style
```

[[Fashion Editorial]]

---

### 122. Sadie Sink 内省电梯肖像提示

**Author**: [Maercih](https://x.com/Maercihh)  **Date**: 2026-01-30  **Language**: en

> 一个结构化提示，用于生成一张萨迪·辛克 (Sadie Sink) 在现代电梯内的时尚编辑照片，重点突出静谧的忧郁氛围、冷色调的顶灯，以及特定的服装和相机设置 (50mm 镜头，f1.8)。

![Sadie Sink 内省电梯肖像提示](https://cms-assets.youmind.com/media/1769841059335_8kxevh_G_4roCebUAYIEct.jpg)
![Sadie Sink 内省电梯肖像提示](https://cms-assets.youmind.com/media/1769841059431_etdjw7_G_58nf6aEAE8zCT.jpg)

```
{
  "subject": "{argument name="subject name" default="Sadie Sink"} standing alone inside a modern elevator, holding a small bouquet of yellow flowers at chest level",
  "mood": "quiet melancholy, restrained emotion, intimate stillness",
  "setting": {
    "location": "brushed metal elevator interior",
    "environment": "enclosed, reflective walls, subtle symmetry"
  },
  "wardrobe": {
    "outerwear": "soft beige wool coat with natural texture",
    "innerwear": "pale yellow button-up shirt",
    "accessories": "small gold hoop earrings"
  },
  "appearance": {
    "hair": "slightly damp, natural texture, loosely parted",
    "makeup": "minimal editorial makeup, visible skin texture, soft blush, natural lips",
    "expression": "neutral, introspective gaze directly into camera"
  },
  "composition": {
    "framing": "centered portrait, mid-torso crop",
    "camera_angle": "eye-level, straight-on",
    "depth_of_field": "shallow, background softly blurred"
  },
  "lighting": {
    "type": "overhead fluorescent elevator lighting",
    "quality": "soft but cool-toned, gentle falloff on face",
    "contrast": "low to medium, cinematic realism"
  },
  "color_palette": "muted greens and steel tones contrasted with warm yellows",
  "camera": {
    "lens": "50mm",
    "aperture": "f1.8",
    "film_look": "subtle grain, cinematic color grading, no HDR"
  },
  "style_constraints": [
    "photorealistic",
    "editorial fashion photography",
    "no over-smoothing",
    "no exaggerated bokeh",
    "natural skin texture preserved"
  ],
  "overall_vibe": "a paused moment between destinations, emotionally unresolved but visually calm"
}
```

[[Fashion Editorial]] [[Celebrity Likeness]] [[50mm Lens]]

---

### 123. 高级定制沙漏肖像提示词 (Gemini Nano Banana Pro)

**Author**: [七表哥](https://x.com/seven_cuz)  **Date**: 2026-01-30  **Language**: en

> 一个高度详细、结构化的 JSON 提示词，专为 Gemini Nano Banana Pro 设计，用于生成一张高级时装编辑肖像。它强调沙漏型身材、冷艳气质、特定的亮片连衣裙细节、戏剧性妆容以及低角度居中构图。

![高级定制沙漏肖像提示词 (Gemini Nano Banana Pro)](https://cms-assets.youmind.com/media/1769841145072_r6963k_G_48Ji6bUAIF69s.jpg)

```
{
  "subject": {
    "core_identity": "Use the same face from the reference image without changing facial features, fair skin with warm golden undertones, long voluminous wavy jet-black hair, striking beauty with dramatic makeup",
    "skin_and_facial_details": "hyper-detailed photorealistic skin:1.4, smooth luminous texture with visible fine pores on cheeks and nose, strong subsurface scattering creating soft radiant glow, subtle natural imperfections, highly detailed irises with rich radial patterns and intense catchlights from ring light and studio flash, thick winged eyeliner, long curled lashes, sculpted contouring, full glossy lips with rich red color and high shine:1.3",
    "hair": "long voluminous wavy jet-black hair with silky gloss, cascading over shoulders and down back, realistic strand separation, strong specular shine and soft bounce under dramatic studio lighting:1.2",
    "body_figure": "voluptuous hourglass silhouette with pronounced feminine curves:1.3, full natural bust accentuated by deep side cut-outs and sheer sequin fabric, extremely narrow defined waist, curvaceous hips and rounded glutes tightly hugged by high-slit dress, long toned legs with smooth skin visible through high side slits, natural asymmetry in dynamic standing pose",
    "micro_expression": "direct sultry gaze with slightly hooded eyes, subtly parted glossy lips in seductive pout, faint confident smirk at corners, conveying intense allure, bold self-assurance and high-fashion sensuality through strong eye contact and poised expression:1.2"
  },
  "apparel_and_materials": "{argument name="apparel description" default="silver-grey sequin-covered sleeveless high-neck maxi dress with dramatic side cut-outs and criss-cross lace-up details exposing skin, high side slit revealing leg"}, tight bodycon fit with realistic sequin texture sparkle and light reflection, sheer mesh panels at sides, fabric showing strong compression wrinkles at waist and hips from pose tension:1.3",
  "pose_and_action": "powerful full-body studio portrait pose, standing with slight hip pop and weight on one leg, torso twisted to accentuate curves and cut-outs, arms relaxed or one hand on hip, head tilted subtly, posture conveys high-fashion glamour, seductive confidence and dramatic elegance through arched back, chest forward emphasis and leg extension through slit:1.2",
  "scene_and_environment": "modern luxury studio interior space, dark matte grey or black walls, large softbox or ring light setup creating controlled dramatic illumination, clean minimalist background w"
}
```

[[Fashion Editorial]] [[Hourglass Figure]] [[Sequin Dress]] [[Dramatic Makeup]]

---

### 124. 柔和高定时装编辑肖像提示 (Nano Banana Pro)

**Author**: [bengi](https://x.com/p3rikly)  **Date**: 2026-01-29  **Language**: en

> 一个高度结构化的 JSON 提示词，用于 Nano Banana Pro 生成一张超写实、高级时装的编辑肖像。它指定了柔和的色彩（粉色和青绿色）、湿发造型、柔和的灯光，以及一个独特的姿势，即双手呈防御姿态环绕脸部。

![柔和高定时装编辑肖像提示 (Nano Banana Pro)](https://cms-assets.youmind.com/media/1769841152118_a6vq6a_G_3XRZwXoAASdcP.jpg)

```
{
"prompt_type": "photorealistic high-fashion editorial portrait",   "character": {     "description": "{argument name="character description" default="REPLACE_WITH_YOUR_CHARACTER"}",     "gender": "female",     "age_range": "early 20s",     "skin_texture": "natural smooth skin with visible realistic texture",     "facial_expression": "soft confident expression, lips slightly parted, calm and self-assured",     "gaze": "looking slightly downward into the camera",     "hair": {       "style": "slicked straight back",       "finish": "wet-look",       "parting": "no visible part"     }   },   "makeup": {     "base": "natural satin finish",     "eyes": {       "eyeshadow": "pastel turquoise-green",       "eyeshadow_hex": "#8FBFC1",       "application": "softly blended",       "mascara": "minimal",       "eyeliner": "none"     },     "lips": {       "color": "natural pink",       "finish": "soft satin"     }   },   "styling": {     "outfit": {       "top": {         "material": "sheer knitted mesh fabric",         "color": "pastel pink",         "color_hex": "#F2B6C8",         "texture": "fine open-knit, semi-transparent",         "fit": "relaxed elegant drape",         "sleeve_ends": "decorated with fluffy feathers and delicate fringe/püsküller",         "sleeve_end_detail_hex": "#F6C1D3"       },       "scarf": {         "material": "fluffy feathery yarn",         "color": "pastel pink",         "color_hex": "#F6C1D3",         "placement": "loosely wrapped around shoulders and neckline"       }     },     "accessories": {       "earrings": {         "type": "statement dangling",         "material": "gold-toned metal",         "color_hex": "#D4AF37",         "design": "sunburst floral"       }     }   },   "pose": {     "hands": {       "position": "raised as if in a guard stance, framing face but not touching or covering it",       "entry_point": "upper left and upper right frame edges",       "palms": "angled inward and slightly downward",       "wrists": "softly bent, relaxed",       "fingers": "open, naturally curved",       "fingertips_direction": "slightly upward and inward",       "coverage": "partially over chest/torso, following sleeve ends, hands slightly under fabric edge",       "focus": "hands slightly out of focus, face in sharp focus"     }   },   "camera": {     "lens": "85mm portrait",     "aperture": "f/2.8",     "angle": "slightly low angle",     "depth_of_field": "shallow"   },   "lighting": {     "type": "soft diffused frontal light",     "contrast": "low",     "shadow_quality": "very soft"   },   "background": {     "color": "{argument name="background color" default="warm orange"}",     "color_hex": "#F36F45",     "texture": "flat seamless studio backdrop"   },   "mood": {     "style": "Vogue-style high fashion editorial",     "emotion": "dreamy, confident, serene"   },   "post_processing": {     "color_grading": "slightly warm editorial finish",     "retouching": "minimal"   },   "negative_prompt": [     "harsh shadows",     "busy background",     "low quality",     "extra fingers",     ""]
```

[[Fashion Editorial]] [[Soft Lighting]]

---

### 125. 超现实自然时尚融合肖像

**Author**: [Weinberg](https://x.com/weiinberg)  **Date**: 2026-01-29  **Language**: en

> 一个用于生成超现实、平静氛围的时尚编辑照片的提示。照片中，一个人身穿超大号蓝色羽绒服和棒球帽，身体和脸部被绿色植物以及白色和黄色小花完全遮盖，与自然环境融为一体。

![超现实自然时尚融合肖像](https://cms-assets.youmind.com/media/1769754979607_1c1ofs_G_1J8ykaoAAytiB.jpg)

```
A human figure standing in a flower-filled field wearing an oversized blue puffer jacket and blue baseball cap, body and face fully covered in green foliage and small white and yellow flowers; identity obscured by plants; soft natural daylight, pale blue sky background, shallow depth of field with blurred flowers in the foreground, editorial fashion photography style, calm and surreal mood, soft color palette, nature fashion fusion aesthetic.
```

[[Fashion Editorial]] [[Studio Portrait]] [[Surrealist Photography]] [[Ethereal Mood]]

---

### 126. Y2K 影响力人物美学肖像提示词

**Author**: [Crystal](https://x.com/Cicily_aura)  **Date**: 2026-01-29  **Language**: en

> 一个高度详细的结构化提示，用于 Gemini Nano Banana Pro，旨在生成一张具有 Y2K 潮流影响者美学风格的年轻女性竖版高分辨率肖像，其中包含特定的发型、服装、妆容和灯光细节，包括直接的机内闪光灯。

![Y2K 影响力人物美学肖像提示词](https://cms-assets.youmind.com/media/1769755013463_vdliql_G_0_wwMa0AA6pCe.jpg)

```
{
  "prompt_structure": {
    "subject": {
      "demographics": "{argument name="demographics" default="Young woman, light skin tone"}",
      "hair": "Long, straight dark brown hair with bold bright pink chunky highlights framing the face (money pieces), clean center part, hair flowing naturally with slight movement",
      "expression": "Playful soft pout with a confident subtle smirk, relaxed glossy lips, direct eye contact with the camera",
      "pose": "Full-body standing pose facing forward, one hand lifting a strand of hair outward at shoulder height, the other resting lightly on the collarbone, relaxed but confident posture"
    },
    "outfit": {
      "top": "Black strapless corset top with sweetheart neckline, visible structured boning, premium fabric texture, sharply fitted silhouette",
      "bottom": "High-waisted black pants or mini skirt (minimalist, clean lines) to balance the corset",
      "accessories": [
        "Black lace fingerless gloves covering hands and wrists",
        "Metallic choker necklace with silver and black circular details, reflective finish",
        "Silver chain belt draped loosely at the waist/hip with subtle shine"
      ]
    },
    "makeup": {
      "skin": "Natural skin texture with soft flash highlights, realistic pores, subtle glow",
      "eyes": "Defined lashes, crisp sharp winged eyeliner, softly arched groomed brows",
      "lips": "Soft pink high-gloss lipstick with strong reflective shine"
    },
    "environment": {
      "location": "Wide indoor gallery-style hallway with depth and symmetry",
      "background": "Large framed contemporary artwork on a beige wall, dark blue horse silhouette in motion, softly blurred for depth separation",
      "floor": "Polished neutral-toned flooring with subtle reflections"
    },
    "lighting_and_style": {
      "aesthetic": "Early-2000s digital camera aesthetic, elevated Y2K influencer look",
      "lighting": "Direct on-camera flash with controlled diffusion, bright subject illumination, gentle background falloff",
      "composition": "Vertical big-format composition, subject centered with breathing room, cinematic framing",
      "quality": "Ultra-high resolution, poster-ready, sharp focus, realistic skin texture, clean edges, candid yet fashion-editorial snapshot vibe"
    },
    "technical_settings": {
      "aspect_ratio": "2:3 or 3:4",
      "resolution": "Ultra high-resolution (8K+), suitable for large prints",
      "camera_style": "High-end digital camera emulating early-2000s flash photography"
    }
  }
}
```

[[Fashion Editorial]] [[On-Camera Flash]] [[Makeup Detail]] [[Structured Prompt]]

---

### 127. 霓虹灯下的活力街机肖像 (重复)

**Author**: [unforgettwble](https://x.com/xbella_bee)  **Date**: 2026-01-29  **Language**: en

> 一个详细的提示，用于生成一张充满活力、动感的年轻女性在游乐场街机厅的肖像。该提示详细说明了拍摄对象的样貌（金发，灿烂的笑容）、服装（橙色针织露脐上衣和短裤，露出 Calvin Klein 腰带）、姿势（坐在摩托车街机游戏机上），以及高对比度的霓虹灯环境。（这是推文 2016823118518485087 的副本）。

![霓虹灯下的活力街机肖像 (重复)](https://cms-assets.youmind.com/media/1769754983876_249uq6_G_0_LgjbUAIkypM.jpg)

```
{
  "prompt_structure": {
    "subject": {
      "appearance": "Young woman with long, wavy blonde hair and a radiant, joyful expression featuring a wide smile.",
      "pose": "Seated on a pink arcade motorcycle game, leaning slightly forward with hands on the handlebars, body angled in profile while turning head to face the camera."
    },
    "attire": {
      "top": "Strapless orange knit crop top (bandeau style) featuring distressed/ripped texture and a decorative buckle strap across the chest.",
      "bottoms": "Matching tight orange shorts.",
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
      "color_palette": "Saturated orange (outfit), neon pink, electric blue, and deep shadows.",
      "photography_style": "Medium shot, high-flash or bright environmental lighting, sharp focus on the subject with a shallow depth of field background."
    }
  }
}
```

[[Fashion Editorial]] [[High Contrast Lighting]] [[Neon Lighting]] [[Blonde Model]]

---

### 128. 意大利别墅金色时段时尚大片

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-29  **Language**: en

> 一份详细的提示，用于拍摄一张意大利别墅露台上年轻男子的超逼真时尚杂志照片。它具体描述了拍摄对象的形象：身穿一件双排扣深橄榄色灯芯绒西装，以及拍摄环境（赤陶砖、柠檬树、柏树）。光线设定为黄金时段，营造出温暖的阳光和长长的阴影，并指定了具体的相机设置（哈苏 X2D 100C、80mm 镜头、柯达 Portra 400 色彩分级），以呈现电影般的视觉效果。

![意大利别墅金色时段时尚大片](https://cms-assets.youmind.com/media/1769755000404_ymvtb6_G_04VaRbUAEKjWj.jpg)

```
A young man with slightly longer dark hair and green eyes; full body, looking into the camera, confident relaxed pose, eye-level angle, slight 3/4 turn: wearing a double-breasted dark-olive wide-wale corduroy suit (6x2 jacket with peak lapels, brown buttons, breast pocket with a green pocket square, flap pockets), classic white shirt, dark-green tie, pressed trousers with creases, brown leather derby shoes; location: terrace of an Italian villa - terracotta tiles, stone columns and arches, ceramic planters with lemon trees, cypresses and hills in the distance; atrnosphere: golden hour, warm sunlight, long soft shadows, light atmospheric haze, gentle rim and side lighting, delicate highlights on the corduroy texture; cinematic artistic frame, photorealism, fashion editorial shoot; shot on {argument name="camera model" default="Hasselblad X2D 100C"}, {argument name="lens focal length" default="80mm"} f/1.9 lens, Kodak Portra 400 color grading, natural warm skin tones, realistic fabric texture, high detail, shallow depth of field, clean bokeh -ar 9:16-style raw -s 200
```

[[Fashion Editorial]] [[Golden Hour Photography]] [[Travel Photography]] [[Men's Fashion]]

---

### 129. 霓虹灯下的活力街机肖像

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2026-01-29  **Language**: en

> 一个详细的提示，用于生成一张充满活力、动感的年轻女性在游乐场街机厅的肖像。该提示详细说明了拍摄对象的样貌（金发，灿烂的笑容）、着装（橙色针织露脐上衣和短裤，露出 Calvin Klein 腰带）、姿势（坐在摩托车街机游戏机上）以及高对比度的霓虹灯环境。

![霓虹灯下的活力街机肖像](https://cms-assets.youmind.com/media/1769754976900_jzycnv_G_0x6ueacAADatO.jpg)
![霓虹灯下的活力街机肖像](https://cms-assets.youmind.com/media/1769754976899_nl8s6s_G_0x6uaa8AAjrEw.jpg)
![霓虹灯下的活力街机肖像](https://cms-assets.youmind.com/media/1769754976197_zk6f6e_G_0x6ufbUAEV6t3.jpg)

```
{
  "prompt_structure": {
    "subject": {
      "appearance": "Young woman with long, wavy blonde hair and a radiant, joyful expression featuring a wide smile.",
      "pose": "Seated on a pink arcade motorcycle game, leaning slightly forward with hands on the handlebars, body angled in profile while turning head to face the camera."
    },
    "attire": {
      "top": "Strapless orange knit crop top (bandeau style) featuring distressed/ripped texture and a decorative buckle strap across the chest.",
      "bottoms": "Matching tight orange shorts.",
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
      "color_palette": "Saturated orange (outfit), neon pink, electric blue, and deep shadows.",
      "photography_style": "Medium shot, high-flash or bright environmental lighting, sharp focus on the subject with a shallow depth of field background."
    }
  }
}
```

[[Fashion Editorial]] [[High Contrast Lighting]] [[Neon Lighting]] [[Blonde Model]]

---

### 130. 高级时装牛仔编辑提示

**Author**: [gauche](https://x.com/gaucheai)  **Date**: 2026-01-29  **Language**: en

> 一个用于高端时尚牛仔编辑肖像的详细图像生成提示，描绘了一位留着铂金色长发的年轻女性，躺在米色摄影棚地板上，身穿一件超大号深蓝色牛仔夹克，强调自然美和极简主义美学。

![高级时装牛仔编辑提示](https://cms-assets.youmind.com/media/1769755058656_omaqis_G_0brzXbUAMnccZ.jpg)

```
{
  "prompt": "Fashion denim editorial portrait, young woman with long platinum white blonde wavy hair, lying on side on beige tan studio floor, head resting near floor with hair spread out, wearing oversized dark blue denim jacket draped loosely open, looking directly at camera with soft neutral expression, light green grey eyes, natural minimal makeup with nude pink lips, fair skin with light natural freckles, relaxed reclining pose on side, warm beige tan seamless studio background, soft diffused studio lighting, high fashion denim campaign aesthetic, intimate close-up portrait, editorial beauty style",
  "negative_prompt": "outdoor, harsh lighting, heavy makeup, dark hair, standing pose, cluttered background, bright colors",
  "style": "high fashion denim editorial, studio portrait, intimate beauty photography, minimalist aesthetic",
  "aspect_ratio": "4:3",
  "camera": {
    "type": "professional studio photography",
    "angle": "eye level, close to floor, intimate close-up",
    "framing": "close-up portrait, face and upper body, horizontal composition"
  },
  "lighting": {
    "type": "soft diffused studio lighting",
    "quality": "warm soft even illumination, minimal shadows, flattering beauty lighting",
    "atmosphere": "clean professional studio setup"
  },
  "mood": "intimate, relaxed, natural beauty, effortless, editorial, soft",
  "color_palette": "platinum blonde, dark indigo blue denim, warm beige tan background, natural fair skin tones",
  "subject_features": {
    "hair": "long platinum white blonde, soft wavy texture, spread out on floor, natural tousled",
    "skin": "fair, natural, light freckles on nose and cheeks",
    "eyes": "light green grey, soft direct gaze at camera, natural lashes",
    "lips": "natural nude pink, soft relaxed",
    "eyebrows": "natural brown, soft shape",
    "expression": "soft, neutral, relaxed, intimate, slight vulnerability"
  },
  "makeup": {
    "style": "natural minimal makeup",
    "base": "natural skin showing freckles, dewy finish",
    "eyes": "minimal, natural lashes",
    "lips": "nude pink, natural"
  },
  "wardrobe": {
    "jacket": "oversized dark indigo blue denim jacket, classic western style with button front, chest pockets with flap and buttons, worn open and draped loosely over shoulders"
  },
  "pose": {
    "position": "lying on right side on studio floor",
    "body": "reclining sideways, denim jacket draped over body",
    "head": "resting near floor, turned toward camera",
    "hair": "spread out flowing on beige floor",
    "gaze": "direct eye contact with camera"
  },
  "setting": {
    "location": "professional photography studio",
    "background": "warm beige tan seamless backdrop and floor",
    "floor": "smooth beige surface",
    "atmosphere": "clean minimalist studio environment"
  }
}
```

[[Fashion Editorial]] [[Minimalist Aesthetic]] [[Platinum Blonde Model]] [[Natural Beauty]]

---

### 131. 低角度高级时装编辑肖像摄影提示

**Author**: [EvrDjM㌹ IA](https://x.com/EvrDjM)  **Date**: 2026-01-28  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超逼真的女性高级时装编辑肖像。关键特点是低角度透视，强调修长的比例。主体身着黑色紧身连衣裙，置身于窗户附近的现代室内，光线指定为柔和的窗户日光，以实现自信、简约和高端的编辑效果。

![低角度高级时装编辑肖像摄影提示](https://cms-assets.youmind.com/media/1769668458919_8xbshd_G_yAhEmXYAA23Jy.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_high_fashion_editorial_portrait",
      "version": "v1.0_BLACK_BODYCON_DRESS_LOW_ANGLE_EDITORIAL_NO_TEXT_EN",
      "priority": "highest",
      "language": "en"
    },
    "references": {
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE",
        "purpose": "POSE_CAMERA_ANGLE_LIGHTING_ATTITUDE_ANCHOR",
        "strict_lock": false,
        "preserve_pose": true,
        "preserve_composition": true,
        "preserve_vibe": true
      }
    },
    "output_settings": {
      "aspect_ratio": "3:4",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "ultra_photoreal_fashion_editorial",
      "sharpness": "crisp_subject_soft_falloff",
      "film_grain": "very_subtle_editorial",
      "dynamic_range": "balanced_cinematic_not_hdr",
      "color_grade": "neutral_warm_skin_tones_with_dark_contrast",
      "skin_rendering": "natural_skin_texture_high-end_retouch",
      "lens_and_camera": {
        "camera": "full_frame_fashion_camera_or_equivalent",
        "lens": "35mm_prime",
        "aperture": "f2.0",
        "focus_style": "upper_body_sharp_lower_frame_soft"
      },
      "lighting": {
        "key": "soft_window_daylight",
        "fill": "subtle_interior_bounce",
        "mood": "confident_minimal_editorial"
      },
      "background": {
        "environment": "modern_interior_with_window",
        "decor": "minimal_clean_surfaces",
        "cleanliness": "high-end_minimal"
      }
    },
    "scene": {
      "global_description": "A high-fashion editorial portrait of a young adult woman photographed from a low-angle perspective inside a modern interior. She stands near a window, looking downward toward the camera with a confident, composed expression. The image emphasizes strong lines, posture, and attitude through perspective and lighting.",
      "subject_details": {
        "woman": {
          "wardrobe": "black fitted sleeveless mini dress with sculpted cut-out neckline, smooth matte fabric, bodycon silhouette",
          "hair_makeup": "dark hair slicked back neatly, polished editorial makeup, defined eyebrows, neutral lips",
          "accessories": "small hoop earrings, minimal jewelry, subtle ring on hand",
          "pose": "standing upright, one hand resting near the upper chest, shoulders relaxed, chin slightly raised"
        }
      },
      "composition": "low-angle fashion composition, subject centered, elongated proportions emphasized by perspective, clean vertical lines",
      "micro_details": [
        "fabric stretch and seams visible",
        "natural skin tone with smooth gradients",
        "soft window light highlights on face and shoulders",
        "clean edges and high-end editorial finish",
        "no artificial glow or heavy smoothing"
      ]
    },
    "negative_prompt": [
      "cartoon"
```

[[Fashion Editorial]] [[Structured JSON Prompt]] [[Window Light]] [[Modern Interior]]

---

### 132. 黄金时段街头服饰电影感户外人像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-28  **Language**: en

> 一个用于生成电影感户外肖像的提示，描绘了一个身穿超大号街头服饰的人物，坐在一处混凝土结构上。它指定了黄金时段的光线、简约的青蓝色天空背景，以及模拟 50mm 镜头的技术细节，以呈现出现代、编辑风格的时尚摄影效果。

![黄金时段街头服饰电影感户外人像](https://cms-assets.youmind.com/media/1769668483327_wiv8a3_G_w67HSa8AAD7_Q.jpg)

```
Cinematic Outdoor Portrait Captured In Warm Natural Daylight, With The Subject Seated Casually On The Edge Of A Textured Concrete Structure. The Framing Is Slightly Low-angled And Mid-distance, Placing The Subject Against A Vast, Uninterrupted Sky In Soft Cyan-blue (#8ec9e8), Creating A Clean, Minimalist Backdrop. Lighting Is Golden-hour Warm (-6200k), Casting Soft Highlights Across The Face And Clothing, While Producing A Long, Crisp Shadow On The Wall Below, The Pose Is Relaxed And Editorial: Hands Resting At The Sides, Legs Extended With One Foot Slightly Raised, And A Calm, Introspective Facial Expression Directed Toward The Camera. Wardrobe Features Oversized Casual Streetwear-muted Rust-colored Hoodie, Wide Beige Corduroy Pants, Striped Socks, And Clean White Sneakers-styled In Matte Textures That Absorb The Sunlight Softly. The Concrete Surface Adds Subtle Grain And Visual Weight, Contrasting With The Airy Sky. Lens Simulation Approximates A 50mm Full-frame At F/2.8, Providing Moderate Depth Of Field With Sharp Detail On The Subject And Gentle Natural Falloff Into The Sky. The Color Palette Blends Warm Earth Tones With Bright Atmospheric Blues, Creating A Serene, Youthful, And Editorial Mood. Editorial, Modern, High-detail, Cinematic Composition, Ultra-realistic Textures, Professional Fashion Photography Style
```

[[Fashion Editorial]]

---

### 133. 街头服饰时尚编辑工作室肖像提示

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-01-28  **Language**: en

> 一个高度结构化的提示，详细说明了构图、主体特征（雀斑、辫子）、街头服饰（IDOL 棒球帽、亚特兰大佐治亚州运动衫）以及技术摄影棚灯光规格，用于生成一张冷色调、轻松、年轻的时尚杂志肖像。

![街头服饰时尚编辑工作室肖像提示](https://cms-assets.youmind.com/media/1769668509803_si8z2h_G_wCU60bAAA-fwp.jpg)

```
{ "composition": { "framing": "medium full-body portrait", "orientation": "vertical", "camera_angle": "slightly above eye-level", "pose": "seated on floor with one knee raised, head resting on hand", "subject_position": "centered", "depth_of_field": "moderate, background fully in focus", "cropping": "full body visible within frame" }, "subject": { "gender_presentation": "female", "approximate_age_range": "teen to young adult", "skin_tone": "light with neutral undertones", "facial_features": { "face_shape": "round to oval", "eyes": "light brown or hazel", "eyebrows": "natural, straight", "nose": "small, rounded tip", "lips": "medium fullness, muted pink", "expression": "relaxed, mildly introspective" }, "hair": { "color": "medium brown", "length": "long", "texture": "straight with slight natural wave", "parting": "center", "styling": "two low braids with loose front strands" }, "distinct_features": { "freckles": "visible across cheeks and nose" } }, "clothing_and_accessories": { "headwear": { "type": "baseball cap", "color": "dark green", "text": "IDOL", "style": "casual streetwear" }, "top": { "type": "oversized sweatshirt", "color": "dark green", "material": "cotton fleece", "graphics": "large collegiate-style typography", "text": "Atlanta Georgia", "details": "white V-neck trim, logo patch on sleeve" }, "bottoms": { "type": "track pants", "color": "black", "material": "velour or plush fabric", "details": "white side piping" }, "footwear": { "type": "sneakers", "color": "black and white", "style": "classic skate or street sneaker" }, "jewelry": { "necklaces": "layered thin chain necklaces", "other": "none visible" } }, "lighting": { "type": "studio lighting", "key_light": "soft diffused frontal light", "fill_light": "gentle fill reducing shadows", "highlights": "soft highlights on cheeks and nose", "shadows": "minimal, soft-edged", "color_temperature": "neutral to slightly cool" }, "color_palette": { "dominant_colors": [ "dark green", "black", "gray" ], "accent_colors": [ "white", "gold", "muted yellow" ], "overall_tone": "cool, muted, modern" }, "background": { "environment": "studio setting", "background_type": "seamless backdrop", "background_color": "light gray", "texture": "smooth, matte", "distractions": "none" }, "technical_traits": { "camera_type": "DSLR or mirrorless camera", "lens_effect": "standard portrait lens", "estimated_focal_length": "35–50mm equivalent", "sharpness": "high overall clarity", "noise": "none visible", "exposure": "even and balanced" }, "artistic_style": { "genre": "studio lifestyle portrait", "mood": "casual, relaxed, youthful", "aesthetic": "streetwear fashion editorial", "post_processing": { "skin_retouching": "very minimal", "color_grading": "cool-neutral balance", "contrast": "low to moderate", "vignette": "none" } }, "typography": { "text_present": true, "text_style": "collegiate varsity lettering", "text_color": "white and gold", "placement": "center chest and sleeve" }, "ov
```

[[Fashion Editorial]] [[Freckle Detail]] [[Braided Hair]]

---

### 134. 金色时段编辑：豪车与名人替身

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-01-28  **Language**: en

> 一个结构化的提示，用于生成一张时尚、电影感的编辑图片，画面中一对情侣（以 Kylie Jenner 和 Timothée Chalamet 为原型）在黄金时段与一辆金属深灰色 Lamborghini Huracán Spyder 摆拍。该提示详细说明了服装、姿势和技术细节，以营造超现实、奢华的氛围。

![金色时段编辑：豪车与名人替身](https://cms-assets.youmind.com/media/1769668478467_4abaeg_G_v6FtlWIAEuqz5.jpg)

```
{
  "image_generation_prompt": {
    "subjects": {
      "female_model": {
        "pose": "Standing elegantly, leaning back against the rear quarter panel of the car",
        "attire": "Navy blue floor-length evening gown, deep plunging V-neckline, gold geometric waist belt, high thigh slit revealing leg, black strappy gladiator heels",
        "appearance": "Long dark wavy hair, red lipstick, sophisticated expression, soft skin texture"
      },
      "male_model": {
        "pose": "Sitting in the driver's seat of the convertible, car door wide open, one leg stepped out onto the pavement, leaning forward slightly",
        "attire": "Tailored dark navy blue suit, crisp white dress shirt, unbuttoned collar, no tie, black dress shoes",
        "appearance": "Groomed brown hair, stubble beard, intense gaze looking at camera"
      }
    },
    "objects": {
      "vehicle": {
        "type": "Lamborghini Huracán Spyder convertible",
        "color": "Metallic dark grey exterior",
        "interior": "Vibrant orange leather bucket seats and trim",
        "details": "Silver alloy rims, aggressive aerodynamic lines, open roof"
      }
    },
    "environment": {
      "location": "Upscale tropical residential street or driveway",
      "flora": "Large overhanging tree with green leaves and white frangipani flowers in the foreground",
      "background": "Blurred white colonial-style architecture, luxurious villa, soft bokeh effect"
    },
    "lighting_and_mood": {
      "lighting": "Warm golden hour natural sunlight, dappled light filtering through tree branches, soft lens flare, high contrast",
      "mood": "Wealth, luxury, romance, high-fashion editorial, cinematic, expensive"
    },
    "technical_specifications": {
      "quality": "Ultra realistic, 8k UHD, HDR, photorealistic, masterpiece",
      "camera_settings": "Shot on 85mm portrait lens, f/1.8 aperture, shallow depth of field, sharp focus on models",
      "resolution": "Super-resolution, highly detailed textures (skin, fabric, metal)"
    }
  },
  "generation_parameters": {
    "aspect_ratio": "9:16",
    "orientation": "Vertical",
    "chaos": "Low",
    "stylize": "High"
  }
}
```

[[Fashion Editorial]] [[Cinematic Glamour]]

---

### 135. 时尚专题：夏日野餐风情

**Author**: [Dockie](https://x.com/Document195)  **Date**: 2026-01-27  **Language**: en

> 一个详细的 JSON 提示，用于生成一张照片级的时尚大片图像：一位时尚的年轻女性在阿尔卑斯山草甸的野餐毯上放松，强调鲜艳的色彩、特定的服装和低角度坐姿视角。

![时尚专题：夏日野餐风情](https://cms-assets.youmind.com/media/1769581917968_qmpqgb_G_rZ934bwAAW9Xs.jpg)

```
{
  "prompt": "A stylish young woman relaxing on a {argument name="blanket color" default="red plaid"} picnic blanket in a lush alpine meadow. She wears a red crop top and matching mini skirt, white knit beanie, white socks with red graphic text, and red-and-white chunky sneakers. One leg is playfully raised while she leans back on her hands, biting a piece of chocolate. Blonde hair, natural makeup, confident and carefree expression. Colorful prayer flags stretch across the background with green hills and mountains under a vivid blue sky filled with fluffy clouds. Fashion editorial style, playful summer energy, ultra-realistic photography.",
  "style": "photorealistic, fashion editorial",
  "lighting": "bright natural daylight, soft shadows",
  "camera": {
    "type": "DSLR",
    "lens": "35mm",
    "aperture": "f/2.0",
    "angle": "low seated perspective"
  },
  "color_palette": "vibrant reds, lush greens, bright blue sky",
  "mood": "playful, carefree, youthful, summer picnic vibes",
  "quality": "high detail, sharp focus, ultra high resolution, 8k",
  "aspect_ratio": "3:4"
}
```

[[Fashion Editorial]] [[Structured JSON Prompt]]

---

### 136. 超逼真电影感人像，搭配豪华跑车

**Author**: [Snow](https://x.com/iamrealsnow)  **Date**: 2026-01-27  **Language**: en

> 生成一张超现实电影风格肖像的提示词，描绘一个 20 岁男孩，身旁是一辆豪华跑车，置身于沙漠色单色工作室中。该提示词要求保留参考图中人物的面部和身体特征，详细描述一套时尚的米色风衣穿搭，柔和的自然光线，以及一种精致、宁静的氛围。

![超逼真电影感人像，搭配豪华跑车](https://cms-assets.youmind.com/media/1769581996171_lv8r1t_G_qwxgNbAAIi2Wk.jpg)

```
REFERENCE: KEEP THE SAME BOY’S FACE AND SLIM, ELEGANT BODY.PROMPT: HYPER-REALISTIC CINEMATIC PORTRAIT OF A 20-YEAR-OLD BOY BESIDE A LUXURY SPORTS CAR IN A WARM, DESERT-SAND MONOCHROME STUDIO. THE LIGHTING IS SOFT AND NATURAL, BLENDING ORGANIC EARTH TONES WITH MODERN LUXURY.OUTFIT: A STYLISH LIGHT TAN TRENCH COAT OR CAR COAT OVER A CREAM OR PALE GOLD TURTLENECK SWEATER, SLIM-FIT BROWN TROUSERS, AND CHIC BROWN LEATHER LACE-UP SHOES. A SLEEK WRISTWATCH FOR A TOUCH OF REFINEMENT.POSE: LEANING GENTLY AGAINST THE SPORTS CAR’S HOOD OR FENDER, ONE HAND IN HIS COAT POCKET, WITH A GENTLE YET CONFIDENT AND THOUGHTFUL https://t.co/atBNLFepsH: A SLEEK, MATTE GOLD OR DESERT-SAND COLORED LUXURY SPORTS CAR, SUCH AS A {argument name="car brand" default="LAMBORGHINI"} OR PORSCHE, REFLECTING SOFT GRADIENTS OF BEIGE, GOLD, AND FAWN https://t.co/9MvH1nckgu: WARM, SOFT AMBIENT LIGHTING FILLS THE STUDIO, CREATING SUBTLE HIGHLIGHTS AND NATURAL SHADOWS. A HINT OF DUST OR SOFT HAZE IN THE AIR ADDS TO THE DESERT-INSPIRED, MONOCHROME ATMOSPHERE.MOOD: SERENE YET SOPHISTICATED — A CINEMATIC FUSION OF NATURAL EARTH TONES AND UNDENIABLE https://t.co/JoyhzvleuV: MONOCHROME DESERT-SAND EDITORIAL PHOTOGRAPHY.
```

[[Fashion Editorial]] [[Soft Natural Light]] [[Luxury Sports Car]]

---

### 137. 豪华时尚杂志与保时捷 GT3 RS (重复)

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 一个用于生成垂直、超逼真时尚编辑图片的综合提示。图片中，一位时尚的金色头发女士站在一辆深绿色保时捷 911 GT3 RS 旁，置身于一座豪华现代别墅中，强调高对比度、锐利焦点和 8K 画质。（重复 2016015363436351709）

![豪华时尚杂志与保时捷 GT3 RS (重复)](https://cms-assets.youmind.com/media/1769582003600_9gblz7_G_pdhlpbAAANKhH.jpg)
![豪华时尚杂志与保时捷 GT3 RS (重复)](https://cms-assets.youmind.com/media/1769582003661_yt5wgg_G_pcxMVWQAASuuK.jpg)
![豪华时尚杂志与保时捷 GT3 RS (重复)](https://cms-assets.youmind.com/media/1769582003542_mqoi7v_G_pcxFpbAAUb9I-.jpg)
![豪华时尚杂志与保时捷 GT3 RS (重复)](https://cms-assets.youmind.com/media/1769582004858_57b6ij_G_pdhj3bAAQrnbt.jpg)

```
{
  "prompt_generation": {
    "positive_prompt": "High-end lifestyle fashion editorial, ultra-photorealistic, vertical full-body shot, cinematic realism. A stylish young woman with soft honey-blonde waves and sun-kissed highlights stands casually beside the rear quarter of a dark forest green {argument name="car model" default="Porsche 911 GT3 RS"}. She wears a relaxed white vintage graphic tee slightly cropped at the waist with faded 'Lucky Club' lettering, loose-fit washed blue jeans sitting low on the hips, minimalist gold jewelry, and sleek black oval sunglasses. Her posture is effortless and confident, weight shifted to one leg, one hand resting near the pocket. The massive carbon-fiber rear wing and GT3 RS emblem are prominently visible, paint reflecting palm trees and sky. In the background, slightly blurred, a bald man in dark sunglasses and a clean white polo shirt leans near the entrance of a luxury modern villa. The setting features white concrete architecture, expansive glass panels, flowing sheer curtains, and sharp Mediterranean sunlight. Strong natural highlights, deep shadows, high contrast, shallow depth of field, razor-sharp focus on the subject, hyper-detailed textures, realistic skin detail, pores visible, editorial grade, HDR, UHD, 8K, masterpiece photography.",
    "negative_prompt": "low resolution, soft focus, blur, overexposed, underexposed, flat lighting, bad anatomy, extra limbs, missing fingers, warped proportions, cartoon, CGI, illustration, painting, anime, watermark, logo overlay, text artifacts, noisy image, grain, distorted vehicle, incorrect reflections, wrong perspective",
    "subject_details": {
      "primary_character": {
        "gender": "female",
        "hair": "long honey-blonde wavy hair with subtle highlights",
        "apparel": "white vintage-style cropped tee with faded 'Lucky Club' text, relaxed blue denim jeans, gold chain necklace, black oval sunglasses",
        "pose": "casual editorial stance, relaxed confidence, weight on one leg"
      },
      "secondary_character": {
        "gender": "male",
        "hair": "shaved head",
        "apparel": "white polo shirt, jeans, sunglasses",
        "position": "background near villa entrance, softly out of focus"
      }
    },
    "environment_details": {
      "vehicle": "Porsche 911 GT3 RS, dark forest green, rear-quarter angle, carbon fiber wing, glossy reflections",
      "location": "Luxury modern villa driveway, white minimalist architecture, floor-to-ceiling glass, sheer curtains, palm reflections"
    },
    "technical_settings": {
      "image_quality": "Ultra-realistic, HDR, UHD, 8K",
      "lighting": "Bright natural sunlight, hard shadows, cinematic contrast",
      "camera_angle": "Slight rear-quarter perspective, eye-level",
      "aspect_ratio": "9:16",
      "orientation": "Vertical"
    }
  }
}
```

[[Fashion Editorial]] [[High Contrast Lighting]] [[8K Photography]] [[Vertical Format]]

---

### 138. 保时捷 GT3 RS 奢华时尚大片

**Author**: [Crystal](https://x.com/Cicily_aura)  **Date**: 2026-01-27  **Language**: en

> 一个用于生成垂直、超逼真时尚编辑图片的综合提示。图片中，一位时尚的金发女士站在一辆深绿色保时捷 911 GT3 RS 旁，置身于一栋豪华现代别墅中，强调高对比度、锐利焦点和 8K 画质。

![保时捷 GT3 RS 奢华时尚大片](https://cms-assets.youmind.com/media/1769581999571_5ebd5q_G_pTR59bAAIXaV2.jpg)

```
{
  "prompt_generation": {
    "positive_prompt": "High-end lifestyle fashion editorial, ultra-photorealistic, vertical full-body shot, cinematic realism. A stylish young woman with soft honey-blonde waves and sun-kissed highlights stands casually beside the rear quarter of a dark forest green {argument name="car model" default="Porsche 911 GT3 RS"}. She wears a relaxed white vintage graphic tee slightly cropped at the waist with faded 'Lucky Club' lettering, loose-fit washed blue jeans sitting low on the hips, minimalist gold jewelry, and sleek black oval sunglasses. Her posture is effortless and confident, weight shifted to one leg, one hand resting near the pocket. The massive carbon-fiber rear wing and GT3 RS emblem are prominently visible, paint reflecting palm trees and sky. In the background, slightly blurred, a bald man in dark sunglasses and a clean white polo shirt leans near the entrance of a luxury modern villa. The setting features white concrete architecture, expansive glass panels, flowing sheer curtains, and sharp Mediterranean sunlight. Strong natural highlights, deep shadows, high contrast, shallow depth of field, razor-sharp focus on the subject, hyper-detailed textures, realistic skin detail, pores visible, editorial grade, HDR, UHD, 8K, masterpiece photography.",
    "negative_prompt": "low resolution, soft focus, blur, overexposed, underexposed, flat lighting, bad anatomy, extra limbs, missing fingers, warped proportions, cartoon, CGI, illustration, painting, anime, watermark, logo overlay, text artifacts, noisy image, grain, distorted vehicle, incorrect reflections, wrong perspective",
    "subject_details": {
      "primary_character": {
        "gender": "female",
        "hair": "long honey-blonde wavy hair with subtle highlights",
        "apparel": "white vintage-style cropped tee with faded 'Lucky Club' text, relaxed blue denim jeans, gold chain necklace, black oval sunglasses",
        "pose": "casual editorial stance, relaxed confidence, weight on one leg"
      },
      "secondary_character": {
        "gender": "male",
        "hair": "shaved head",
        "apparel": "white polo shirt, jeans, sunglasses",
        "position": "background near villa entrance, softly out of focus"
      }
    },
    "environment_details": {
      "vehicle": "Porsche 911 GT3 RS, dark forest green, rear-quarter angle, carbon fiber wing, glossy reflections",
      "location": "Luxury modern villa driveway, white minimalist architecture, floor-to-ceiling glass, sheer curtains, palm reflections"
    },
    "technical_settings": {
      "image_quality": "Ultra-realistic, HDR, UHD, 8K",
      "lighting": "Bright natural sunlight, hard shadows, cinematic contrast",
      "camera_angle": "Slight rear-quarter perspective, eye-level",
      "aspect_ratio": "9:16",
      "orientation": "Vertical"
    }
  }
}
```

[[Fashion Editorial]] [[High Contrast Lighting]] [[8K Photography]]

---

### 139. 保时捷 911 GT3 RS 高级时装大片

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-01-27  **Language**: en

> 一个用于创作超现实时尚大片杰作的综合图像生成提示。它描述了一名女性身穿露脐上衣和宽松牛仔裤，在一栋豪华现代别墅旁，一辆深绿色保时捷 911 GT3 RS 旁边摆姿势的垂直全身照，强调高对比度、硬阴影和 8k 分辨率。

![保时捷 911 GT3 RS 高级时装大片](https://cms-assets.youmind.com/media/1769581976262_l5m3nx_G_pEYFWW4AAUlbn.jpg)
![保时捷 911 GT3 RS 高级时装大片](https://cms-assets.youmind.com/media/1769581976262_xtszw8_G_pEYErXgAEjipF.jpg)
![保时捷 911 GT3 RS 高级时装大片](https://cms-assets.youmind.com/media/1769581976340_7bqjwz_G_pEYFmXAAAR2UQ.jpg)

```
{
  "prompt_generation": {
    "positive_prompt": "Ultra-realistic fashion editorial masterpiece, vertical full shot, medium distance. A stunning young woman with long wavy blonde hair and chunky highlights stands in the foreground, wearing a white oversized t-shirt rolled up into a crop top with '{argument name="shirt text" default="Lucky Club"} vintage script text', baggy blue denim jeans, and black oval sunglasses. She is posing next to the rear of a dark moss green Porsche 911 GT3 RS, highlighting the massive carbon fiber rear wing and GT3 RS badging. In the background, a man with a shaved head and sunglasses wears a matching white polo shirt, standing near the modern villa entrance. Background features a luxurious white modern mansion with floor-to-ceiling glass windows and sheer curtains. Natural bright sunlight, hard shadows, high contrast, crisp focus, 8k resolution, UHD, HDR, cinematic depth of field, hyper-detailed textures, skin pores visible, masterpiece.",
    "negative_prompt": "blurry, low quality, pixelated, distorted features, bad anatomy, extra limbs, missing fingers, cartoonish, illustration, painting, drawing, watermark, text overlay, grainy, noise, deformed car, wrong perspective, dull colors, low contrast.",
    "subject_details": {
      "primary_character": {
        "gender": "female",
        "hair": "long blonde wavy with highlights",
        "apparel": "white crop top with 'Lucky Club' text, blue baggy jeans, gold necklace, black sunglasses",
        "pose": "standing confidently, hand on belt, holding a small handbag"
      },
      "secondary_character": {
        "gender": "male",
        "hair": "bald/shaved",
        "apparel": "white oversized polo with matching text, jeans, sunglasses",
        "position": "background, slightly out of focus"
      }
    },
    "environment_details": {
      "vehicle": "Porsche 911 GT3 RS, dark green, rear view, large wing, high gloss finish",
      "location": "Modern luxury villa driveway, white architecture, glass windows, palm trees reflected"
    },
    "technical_settings": {
      "image_quality": "Ultra Realistic, HDR, UHD, 8k",
      "lighting": "Natural daylight, sunny, high dynamic range",
      "camera_angle": "Eye-level, medium shot",
      "aspect_ratio": "9:16",
      "orientation": "Vertical (Long Image)"
    }
  }
}
```

[[Fashion Editorial]] [[8K Photography]]

---

### 140. 高级定制幻象蕾丝紧身胸衣礼服大片

**Author**: [The Prompt Engineer](https://x.com/rorschachvibes)  **Date**: 2026-01-26  **Language**: en

> 生成一张时尚大片风格的女性图片，她身穿无肩带幻象蕾丝紧身胸衣礼服，重点突出裸色底衬、黑色蕾丝刺绣、可见的鱼骨细节以及戏剧性的薄纱拖尾的精致之处。

![高级定制幻象蕾丝紧身胸衣礼服大片](https://cms-assets.youmind.com/media/1769495332984_qk8cnf_G_oKJkEbAAAKZBc.jpg)

```
Create a high-fashion editorial look featuring a woman wearing a strapless sheer corset gown, also known as an illusion lace evening gown. The dress has a nude skin-tone base with intricate {argument name="lace color" default="black"} lace embroidery layered over transparent fabric. The corset-style bodice includes visible boning that cinches and shapes the waist, while the strapless neckline highlights the shoulders and collarbone. A dramatic {argument name="train color" default="black"} tulle train or skirt is attached at the back, adding volume, movement, and elegance to the silhouette. The overall aesthetic is luxurious, refined, and couture-focused, emphasizing structure, transparency, and contrast between nude fabric and black detailing.
```

[[Fashion Editorial]]

---

### 141. 象牙色蕾丝迷你连衣裙的超逼真时尚肖像（复制）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-20  **Language**: en

> 一个高度详细、结构化的 JSON 提示，用于生成超现实、高级时尚的编辑肖像。该提示指定了严格的身份保留、双腿交叉的曲线姿势、象牙色蕾丝迷你连衣裙、金属金色高跟鞋，以及用于 8k 分辨率输出的专业影棚灯光设置。（这是 2013588573065220479 的副本）。

![象牙色蕾丝迷你连衣裙的超逼真时尚肖像（复制）](https://cms-assets.youmind.com/media/1768977270428_ps065l_G_IV8zSWIAAzb2P.jpg)
![象牙色蕾丝迷你连衣裙的超逼真时尚肖像（复制）](https://cms-assets.youmind.com/media/1768977270547_aysyyl_G_IV8x0XwAY7YzI.jpg)

```
{
  "project_metadata": {
    "version": "2.0",
    "target_quality": "Hyper-Realistic / Photogrammetric",
    "aspect_ratio": "3:4",
    "reference_parameters": {
      "identity_preservation": "High (Strictly maintain facial geometry and hairstyle from reference image)",
      "facial_integrity": "Unmodified facial features, zero distortion"
    }
  },
  "subject_details": {
    "human_attributes": {
      "physique": "Curvy, well-defined silhouette",
      "skin_texture": "Pore-level detail, natural skin sheen, realistic subsurface scattering",
      "gaze": "Direct eye contact with camera, engaging and confident expression"
    },
    "hair_specification": {
      "style": "Exact match to attached photo",
      "texture": "Fine strands, realistic sheen, high-fidelity fiber rendering",
      "interaction": "Naturally draped based on the seated pose"
    },
    "pose_composition": {
      "action": "Seated on a minimalist surface",
      "orientation": "Torso leaning slightly forward toward the lens",
      "lower_body": "Legs crossed and elevated/raised to foreground",
      "focal_emphasis": "Emphasis on leg length and high-heeled footwear"
    }
  },
  "wardrobe_and_styling": {
    "primary_garment": {
      "item": "Minidress",
      "color": "Ivory / Off-white",
      "material": "Silk or satin base with intricate lace overlay",
      "design_elements": [
        "Delicate spaghetti straps",
        "Subtle 3D floral embroidery",
        "Fine lace scalloped edges",
        "Form-fitting curvy silhouette"
      ]
    },
    "footwear": {
      "type": "Stiletto high-heeled sandals",
      "finish": "Metallic gold, reflective",
      "fastening": "Delicate ankle straps with micro-buckle detail",
      "presentation": "Polished, catching the studio light"
    },
    "accessories": {
      "earrings": "Small minimalist gold studs or hoops",
      "jewelry_tone": "Warm metallic gold"
    }
  },
  "environment_and_lighting": {
    "setting": "High-end minimalist studio or neutral architectural background",
    "lighting_setup": {
      "primary": "Softbox key light for even skin tones",
      "secondary": "Subtle rim lighting to define the body curves and hair texture",
      "ambience": "Clean, sophisticated, high-fashion editorial aesthetic"
    },
    "color_palette": [
      "Ivory",
      "Warm Gold",
      "Neutral Skin Tones",
      "Soft Muted Background"
    ]
  },
  "technical_render_specs": {
    "camera": {
      "lens": "85mm prime lens (portrait specialty)",
      "aperture": "f/2.8 for sharp subject focus and soft background blur",
      "sensor": "Full-frame CMOS",
      "shot_type": "Full body / Medium shot"
    },
    "resolution_quality": [
      "8k UHD",
      "Highly detailed textures",
      "Ray-traced reflections on metallic surfaces",
      "Masterpiece quality"
    ]
  }
}
```

[[Fashion Editorial]] [[8K Resolution]] [[Hyperrealistic Photography]] [[Studio Portrait]]

---

### 142. 优雅秋日城市公园编辑场景

**Author**: [Banana Prompts](https://x.com/bananaprompts)  **Date**: 2026-01-20  **Language**: en

> 一个描述性的提示，用于创作一组精致的电影感专题图片，场景设定在深秋时节一个宁静的城市公园。该提示侧重于营造氛围（平静、优雅、内省），模特的造型（黑色长袖迷你连衣裙，带花卉刺绣，透明丝袜，经典高跟鞋），以及环境（阴沉的天空，散落的落叶，极简主义金属长凳）。它还指定了浅景深和冷色调、中性色彩分级，以营造巴黎风格的美感。

![优雅秋日城市公园编辑场景](https://cms-assets.youmind.com/media/1768977372767_xemu8y_G_IIVMPWEAA0R--.jpg)

```
"Create a refined editorial-style scene set in a quiet city park during {argument name="season" default="late autumn"}. The subject is seated sideways on a minimalist metal bench, posture relaxed yet intentional, one leg extended and the other gently bent, heels resting on textured stone paving. Fallen leaves scatter around the ground, bare tree branches framing the background under a soft, overcast sky. The subject’s head is turned slightly away from the camera, suggesting introspection, with one hand resting near the bench edge and the other subtly adjusting hair or holding a small structured handbag. The overall mood is calm, elegant, and cinematic, with muted natural tones and a shallow depth of field that keeps focus on the subject while softly blurring the park surroundings.

Style the subject in a fitted black long-sleeve mini dress with delicate cream floral embroidery, sheer black tights, and classic black pointed heels. Hair is long, dark, and softly flowing, catching a light breeze. Makeup is natural with defined eyes, enhancing a timeless, Parisian-inspired elegance. The color grading leans cool and neutral, emphasizing contrast between the dark outfit and pale autumn leaves, evoking quiet confidence and femininity."
```

[[Fashion Editorial]] [[Cinematic Color Grading]]

---

### 143. 身穿蕾丝迷你连衣裙的女性超写实时尚肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-20  **Language**: en

> 一个高度具体的 JSON 提示，用于生成超逼真、摄影测量质量的时尚肖像。它详细描述了拍摄对象的体格、姿势（坐姿，双腿抬高）、服装（象牙色蕾丝迷你连衣裙和金属金色细高跟鞋）以及技术相机设置（85mm 镜头，f/2.8 光圈），以营造高端时尚编辑美学，并要求严格保留参考图像中的身份。

![身穿蕾丝迷你连衣裙的女性超写实时尚肖像](https://cms-assets.youmind.com/media/1768977250133_37tsb4_G_IAuIwXQAEFEHr.jpg)
![身穿蕾丝迷你连衣裙的女性超写实时尚肖像](https://cms-assets.youmind.com/media/1768977250648_sai8p7_G_IAuM9XYAAgT_I.jpg)
![身穿蕾丝迷你连衣裙的女性超写实时尚肖像](https://cms-assets.youmind.com/media/1768977250684_ewaqmr_G_IAuDkWkAAYVk7.jpg)
![身穿蕾丝迷你连衣裙的女性超写实时尚肖像](https://cms-assets.youmind.com/media/1768977252092_7j77qk_G_IAuOhWAAAx2Mg.jpg)

```
{
  "project_metadata": {
    "version": "2.0",
    "target_quality": "Hyper-Realistic / Photogrammetric",
    "aspect_ratio": "3:4",
    "reference_parameters": {
      "identity_preservation": "High (Strictly maintain facial geometry and hairstyle from reference image)",
      "facial_integrity": "Unmodified facial features, zero distortion"
    }
  },
  "subject_details": {
    "human_attributes": {
      "physique": "Curvy, fit, well-defined silhouette",
      "skin_texture": "Pore-level detail, natural skin sheen, realistic subsurface scattering",
      "gaze": "Direct eye contact with camera, engaging and confident expression"
    },
    "hair_specification": {
      "style": "Exact match to attached photo",
      "texture": "Fine strands, realistic sheen, high-fidelity fiber rendering",
      "interaction": "Naturally draped based on the seated pose"
    },
    "pose_composition": {
      "action": "Seated on a minimalist surface",
      "orientation": "Torso leaning slightly forward toward the lens",
      "lower_body": "Legs crossed and elevated/raised to foreground",
      "focal_emphasis": "Emphasis on leg length and high-heeled footwear"
    }
  },
  "wardrobe_and_styling": {
    "primary_garment": {
      "item": "Minidress",
      "color": "Ivory / Off-white",
      "material": "Silk or satin base with intricate lace overlay",
      "design_elements": [
        "Delicate spaghetti straps",
        "Subtle 3D floral embroidery",
        "Fine lace scalloped edges",
        "Form-fitting curvy silhouette"
      ]
    },
    "footwear": {
      "type": "Stiletto high-heeled sandals",
      "finish": "Metallic gold, reflective",
      "fastening": "Delicate ankle straps with micro-buckle detail",
      "presentation": "Polished, catching the studio light"
    },
    "accessories": {
      "earrings": "Small minimalist gold studs or hoops",
      "jewelry_tone": "Warm metallic gold"
    }
  },
  "environment_and_lighting": {
    "setting": "Contemporary architectural background",
    "lighting_setup": {
      "primary": "Softbox key light for even skin tones",
      "secondary": "Subtle rim lighting to define the body curves and hair texture",
      "ambience": "Clean, sophisticated, high-fashion editorial aesthetic"
    },
    "color_palette": [
      "Ivory",
      "Warm Gold",
      "Neutral Skin Tones",
      "Soft Muted Background"
    ]
  },
  "technical_render_specs": {
    "camera": {
      "lens": "85mm prime lens (portrait specialty)",
      "aperture": "f/2.8 for sharp subject focus and soft background blur",
      "sensor": "Full-frame CMOS",
      "shot_type": "Full body / Medium shot"
    },
    "resolution_quality": [
      "8k UHD",
      "Highly detailed textures",
      "Ray-traced reflections on metallic surfaces",
      "Masterpiece quality"
    ]
  }
}
```

[[Fashion Editorial]] [[Hyperrealistic Photography]] [[Studio Portrait]] [[Luxury Fashion]]

---

### 144. 象牙色蕾丝迷你连衣裙的超逼真高级时装肖像

**Author**: [Adam也叫吉米](https://x.com/Adam38363368936)  **Date**: 2026-01-20  **Language**: en

> 这个 Nano Banana Prompt 旨在生成超现实、摄影测量级的图像，重点是高保真纹理渲染（毛孔级的皮肤细节、细微的发丝）。它指定了一个身穿象牙色蕾丝迷你连衣裙的主体，置身于专业打光的时尚摄影棚中，强调了腿部长度和金属金色配饰。

![象牙色蕾丝迷你连衣裙的超逼真高级时装肖像](https://cms-assets.youmind.com/media/1768977354427_2c5cs1_G_G6p3_WIAAar_K.jpg)
![象牙色蕾丝迷你连衣裙的超逼真高级时装肖像](https://cms-assets.youmind.com/media/1768977354489_f6uq2y_G_G6rsrXUAAJ7gg.jpg)

```
{
  "project_metadata": {
    "version": "2.0",
    "target_quality": "Hyper-Realistic / Photogrammetric",
    "aspect_ratio": "3:4",
    "reference_parameters": {
      "identity_preservation": "High (Strictly maintain facial geometry and hairstyle from reference image)",
      "facial_integrity": "Unmodified facial features, zero distortion"
    }
  },
  "subject_details": {
    "human_attributes": {
      "physique": "Curvy, well-defined silhouette",
      "skin_texture": "Pore-level detail, natural skin sheen, realistic subsurface scattering",
      "gaze": "Direct eye contact with camera, engaging and confident expression"
    },
    "hair_specification": {
      "style": "Exact match to attached photo",
      "texture": "Fine strands, realistic sheen, high-fidelity fiber rendering",
      "interaction": "Naturally draped based on the seated pose"
    },
    "pose_composition": {
      "action": "Seated on a minimalist surface",
      "orientation": "Torso leaning slightly forward toward the lens",
      "lower_body": "Legs crossed and elevated/raised to foreground",
      "focal_emphasis": "Emphasis on leg length and high-heeled footwear"
    }
  },
  "wardrobe_and_styling": {
    "primary_garment": {
      "item": "Minidress",
      "color": "Ivory / Off-white",
      "material": "Silk or satin base with intricate lace overlay",
      "design_elements": [
        "Delicate spaghetti straps",
        "Subtle 3D floral embroidery",
        "Fine lace scalloped edges",
        "Form-fitting curvy silhouette"
      ]
    },
    "footwear": {
      "type": "Stiletto high-heeled sandals",
      "finish": "Metallic gold, reflective",
      "fastening": "Delicate ankle straps with micro-buckle detail",
      "presentation": "Polished, catching the studio light"
    },
    "accessories": {
      "earrings": "Small minimalist gold studs or hoops",
      "jewelry_tone": "Warm metallic gold"
    }
  },
  "environment_and_lighting": {
    "setting": "High-end minimalist studio or neutral architectural background",
    "lighting_setup": {
      "primary": "Softbox key light for even skin tones",
      "secondary": "Subtle rim lighting to define the body curves and hair texture",
      "ambience": "Clean, sophisticated, high-fashion editorial aesthetic"
    },
    "color_palette": [
      "Ivory",
      "Warm Gold",
      "Neutral Skin Tones",
      "Soft Muted Background"
    ]
  },
  "technical_render_specs": {
    "camera": {
      "lens": "85mm prime lens (portrait specialty)",
      "aperture": "f/2.8 for sharp subject focus and soft background blur",
      "sensor": "Full-frame CMOS",
      "shot_type": "Full body / Medium shot"
    },
    "resolution_quality": [
      "8k UHD",
      "Highly detailed textures",
      "Ray-traced reflections on metallic surfaces",
      "Masterpiece quality"
    ]
  }
}
```

[[Fashion Editorial]] [[Hyperrealistic Photography]] [[Studio Portrait]] [[Luxury Fashion]]

---

### 145. K-Pop 偶像专题：都市背景下的玻璃肌与牛仔风尚

**Author**: [QuestGlitch](https://x.com/AIRevSpot)  **Date**: 2026-01-20  **Language**: en

> 一个高度技术化的 JSON 提示词，用于生成一张 K-pop 偶像原型人物的超写实 8K 编辑图片，重点突出“玻璃肌”质感、特定相机光学参数（50mm, f/2.8）和服装细节（无肩带文胸、未扣的牛仔夹克），背景为模糊的城市天际线。

![K-Pop 偶像专题：都市背景下的玻璃肌与牛仔风尚](https://cms-assets.youmind.com/media/1768977312640_altyik_G_GxzmxXIAAWa74.jpg)

```
{ "output_schema": { "metadata": { "camera_simulation": { "hardware": "Sony A7R IV | Canon EOS R5", "lens_optics": { "focal_length_mm": "50mm (natural eye perspective, slight intimacy)", "aperture_f": "f/2.8 (subject sharp, city background creamy bokeh)", "shutter_speed": "1/125s (freezing the pose)", "ISO": "100 (pristine image quality, no grain)" “aspect_ratio”: 4:5 }, "exposure_profile": { "dynamic_range": "High: preserved highlights in window, detailed shadows in denim", "metering": "Spot metering on face", "lighting_setup": "Natural soft window light from left, acting as a large softbox" } }, "digital_quality_profile": { "sensor_excellence": [ "60MP_full_frame_resolution: distinct fabric weave and eyelash definition", "14-bit_raw_depth: subtle skin tone transitions", "sharpness_tuned: high frequency detail on eyes and lips" ], "post_processing": [ "kpop_idol_grading: slight cool tone shadows, porcelain skin brightness", "commercial_polish: clean colors, high contrast but preserved details", "zero_noise: smooth gradients" ] } }, "anatomical_physics_displacement": { "proportions": { "ethnicity": "Korean K-pop Idol archetype, pale porcelain skin", "body_type": "Petite, slender frame, toned 11-line abs, delicate collarbones", "waist_hip_ratio": "Slim waist with subtle feminine curve" }, "physics_triggers": { "gravity": "Hair falling naturally with head tilt; denim jacket sliding off shoulder", "skin_texture": "Glass skin finish with visible pores close up, slight glow on cheekbones", "facial_features": "Doe eyes, gradient lip tint, straight eyebrows, sharp jawline", "pose_tension": "Elongated neck, relaxed torso lean, hand gently gripping hair roots" } }, "wardrobe_stress_mechanics": { "top_details": { "type": "Black branded triangle bralette (Calvin Klein style)", "fit": "Snug elastic band sitting flush against ribcage", "texture": "Cotton jersey fabric, soft sheen" }, "outerwear_details": { "type": "Oversized black denim jacket", "interaction": "Draped loosely over arms, revealing shoulders and chest, rigid denim texture" }, "bottom_details": { "type": "Black denim jeans", "state": "Unbuttoned top button, relaxed fit at hips, revealing waistband of underwear",
"fabric": "Heavyweight denim grain vs soft skin contrast" } }, "compositional_noise": { "framing": "Medium shot, subject leaning back against window sill", "background": "Blurred high-rise city skyline through glass, daylight", "atmosphere": "Chic, urban, intimate but professional editorial vibe" }, "prompt_text": { "instruction": "Generate a photorealistic 8k image. Start with the {argument name="subject type" default="K-pop idol"} subject and petite physique. Describe the specific pose leaning against the window. Detail the outfit ({argument name="outfit details" default="black bralette, unbuttoned jeans, denim jacket"}). Focus on the 'glass skin' texture and high-end photography aesthetic. End with environment details.", "mandatory_phrases": [ "Korean k-pop idol", "extremely sexy petite physique", "porcelain glass skin", "black c"
```

[[Fashion Editorial]] [[8K Portrait]] [[K-Pop Aesthetic]] [[Urban Background]]

---

### 146. 电影级奢华人像：女人调整袖扣

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-01-20  **Language**: en

> 一个用于生成高端时尚编辑肖像的提示，描绘一位自信的女性身穿海军蓝定制西装。图像聚焦于她调整袖扣的动作，背景是温暖的渐变影棚，配以富有戏剧性但平衡的影棚灯光，以增强深度和奢华感。

![电影级奢华人像：女人调整袖扣](https://cms-assets.youmind.com/media/1768977338843_jvwvit_G_GjdJdWQAAJz7J.jpg)

```
{
  "type": "image_generation_prompt",
  "language": "English",
  "style": "editorial fashion portrait, cinematic luxury",
  "aspect_ratio": "4:5",
  "subject": {
    "gender": "female",
    "appearance": {
      "outfit": {
        "suit": "navy blue tailored suit with a feminine cut",
        "shirt": "crisp white shirt",
        "tie": "none"
      },
      "accessories": [
        "aviator sunglasses",
        "gold wristwatch",
        "small elegant lapel pin"
      ]
    },
    "pose": {
      "action": "adjusting cufflinks",
      "framing": "waist-up portrait"
    },
    "expression": "confident, composed, elegant"
  },
  "background": {
    "type": "studio backdrop",
    "color": "warm brown to olive gradient",
    "texture": "smooth, minimal"
  },
  "lighting": {
    "style": "dramatic yet balanced studio lighting",
    "key_light": "upper left",
    "effect": "soft gradient shadows enhancing depth and luxury"
  },
  "camera": {
    "shot_type": "editorial portrait",
    "focus": "sharp focus on subject",
    "depth_of_field": "shallow, softly separating subject from background"
  },
  "mood": {
    "vibe": "luxurious, modern, self-assured",
    "aesthetic": "high-end fashion editorial"
  },
  "quality": {
    "realism": "high",
    "detail": "fine fabric texture, realistic skin tones, polished accessories",
    "finish": "cinematic, professional studio look"
  },
  "output_goal": "Create a cinematic, luxurious editorial portrait of a confident woman in a navy blue tailored suit, adjusting her cufflinks against a warm gradient studio backdrop with dramatic yet refined lighting."
}
```

[[Fashion Editorial]] [[Dramatic Lighting]] [[Studio Portrait]]

---

### 147. 霓虹蓝上衣的忧郁电影感肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-20  **Language**: en

> 一个提示，用于创作一张情绪化、电影感的年轻女性肖像，她皮肤白皙，深棕色头发，穿着优雅的霓虹蓝色上衣。重点在于深色、极简的背景，柔和的漫射前置照明，微妙的胶片颗粒感，以及高端的杂志美学。

![霓虹蓝上衣的忧郁电影感肖像](https://cms-assets.youmind.com/media/1768977266674_mcc7rd_G_GcH8qXQAABodX.jpg)
![霓虹蓝上衣的忧郁电影感肖像](https://cms-assets.youmind.com/media/1768977266670_qft35w_G_GcH4FWoAAc9dt.jpg)
![霓虹蓝上衣的忧郁电影感肖像](https://cms-assets.youmind.com/media/1768977266686_we8x2m_G_GcH5UWEAAyCWU.jpg)

```
Create Moody cinematic portrait of a young woman with clear fair skin and barely-there makeup, warm natural lips. Loose dark brown hair, softly textured. Calm, self-assured expression. She’s wearing a neon blue top elegance. Dark minimal background fading into black. Gentle diffused front light, soft shadows, subtle film grain, organic color grading, shallow depth of field, high-end editorial feel.
```

[[Fashion Editorial]] [[Cinematic Portrait]] [[Film Grain Aesthetic]] [[Minimalist Background]]

---

### 148. 单色前卫时尚大片拍摄提示

**Author**: [Gravity X](https://x.com/GravityX_MW)  **Date**: 2026-01-20  **Language**: en

> 一个详细的文本提示，用于生成一张单色艺术时尚编辑图片。画面中，一个人物低坐于崎岖地形上的极简凳子上，身着深色、宽松叠穿的服装并戴着太阳镜，一匹强壮的黑马保护性地站在其身后。该提示强调高对比度、深邃的黑色、哑光质感，以及带有微妙颗粒感的中画幅胶片效果。

![单色前卫时尚大片拍摄提示](https://cms-assets.youmind.com/media/1768977294252_mq2cq4_G_FjHY_WQAA0Svs.jpg)

```
Photograph me sitting low on a minimalist metal stool, legs spread forward in a relaxed, grounded pose, feet planted on uneven outdoor terrain. One hand loselt resting between the knees holding thin leather jacket reins, shoulders slightly slouched, head tilted downward in a calm, introspection expression, the subject wears dark oversized layered clothing, wide- leg trousers, leather boots and dark sunglasses. A strong black {argument name="animal" default="horse"} stands closely behind the seated figure aligned procetectively and partially overlapping the subjects silhouette,. Open Natural landscapes with rough ground and wild grass, bright overexposed sky creating strong negative space. High contrast lighting, deep blacks, soft highlight, mmatte texture, timeless, cinematic mood. Medium format firm look.Subtle grain. Monochrome fine art fashion editorial, advant garde luxury photography, don't harm the equality of the picture give me in 1080p quality
```

[[Fashion Editorial]] [[High Contrast Photography]]

---

### 149. 私人飞机上的高级时装编辑肖像

**Author**: [AI Tales - Not by Humans](https://x.com/AITalesNBH)  **Date**: 2026-01-20  **Language**: en

> 一个复杂的 JSON 格式提示，旨在生成一张华丽女性坐在私人飞机内的极致奢华、高级时装编辑图片。它详细描述了拍摄对象的容貌、姿势、服装、场景环境和相机技术规格。

![私人飞机上的高级时装编辑肖像](https://cms-assets.youmind.com/media/1768977244090_f1kbda_G_Fd6PoXsAEswFO.jpg)

```
{
"template": "MONB",
"project": "Private Jet Muse — Luxury Passenger Editorial",
"version": "MONB-1.3",
"engine_compatibility": ["Nano Banana", "Midjourney v6+", "SDXL"],
"intent": "Create a maximalist, high-fashion editorial image of a luxurious private jet passenger. The subject is a brunette woman in her mid twenties, seated inside a flying private airplane, embodying modern glamour and sensual elegance. Her presence subtly evokes the confident, cinematic femininity associated with Scarlett Johansson–like features and aura (style reference only, not a direct portrayal).",
"frame": {
"aspect_ratio": "3:4",
"shot_type": "seated fashion editorial portrait",
"camera_angle": "slightly front-facing, eye-level",
"camera_height": "seated chest level",
"composition": "subject centered with elegant cabin symmetry; aircraft window and soft clouds visible behind",
"lens": "50mm full-frame equivalent",
"depth_of_field": "moderate, subject sharply defined, background softly cinematic",
"editorial_notes": "luxury lifestyle, cover-ready composition with strong feminine presence"
},
"scene": {
"location": "interior of a flying private jet",
"environment_details": [
"plush cream leather airplane chair",
"polished wood veneer side panels",
"gold-accented cabin fixtures",
"large oval aircraft window with sky and clouds in motion",
"quiet, intimate luxury atmosphere"
],
"flight_state": "airplane cruising at altitude",
"atmosphere": "exclusive, indulgent, cinematic calm"
},
"subject": {
"type": "luxury female passenger",
"age": "mid twenties",
"style_reference": "modern glamorous femininity reminiscent of Scarlett Johansson (soft strength, sensual confidence)",
"pose": {
"position": "seated comfortably in a luxury airplane chair",
"legs": "crossed elegantly, emphasizing fashion silhouette",
"torso": "upright with a subtle relaxed lean",
"arms": "one arm resting on the armrest, the other relaxed near the table",
"head": "slightly tilted",
"gaze": "looking directly at the camera",
"expression": "charming, confident smile with subtle allure"
},
"appearance": {
"hair": {
"color": "brunette",
"style": "softly styled, polished, gently framing the face"
},
"makeup": {
"eyes": "light blue mascara",
"lips": "soft rosy red",
"skin": "luminous, high-end editorial finish"
}
}
},
"wardrobe": {
"outfit": {
"style": "luxury passenger couture",
"top": "elegant fitted blouse or top in light pastel blue tones",
"skirt": {
"type": "very short tailored skirt",
"style": "fashion-forward, sleek, tasteful"
},
"jacket": {
"type": "light elegant jacket",
"details": [
"refined tailoring",
"subtle gold accents"
]
}
}
}
```

[[Fashion Editorial]] [[Cinematic Portrait]] [[Luxury Lifestyle Photography]]

---

### 150. 西瓜与未来主义太阳镜的超风格化特写

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2026-01-20  **Language**: en

> 一个用于生成超风格化、高对比度特写镜头的提示，聚焦于一位女性，她湿润的头发向后梳理，涂着大胆的红唇，戴着超大号的未来感黑色太阳镜。核心道具是一大片西瓜，她性感地将其靠近嘴边，背景是高调的白色摄影棚，配以强烈的定向照明。

![西瓜与未来主义太阳镜的超风格化特写](https://cms-assets.youmind.com/media/1768977337050_c13amh_G_FDIRVXkAAZLWS.jpg)
![西瓜与未来主义太阳镜的超风格化特写](https://cms-assets.youmind.com/media/1768977337044_8cza6c_G_FDIRVWIAAGUke.jpg)
![西瓜与未来主义太阳镜的超风格化特写](https://cms-assets.youmind.com/media/1768977337007_d2q45o_G_FDIRUXUAA0lNi.jpg)

```
{
  "shot": {
    "composition": "Hyper-stylized close-up, 85mm lens, shallow depth of field, shot on RED Komodo 6K",
    "camera_motion": "static",
    "frame_rate": "24fps",
    "film_grain": "digital clean with gloss post-grade"
  },
  "subject": {
    "description": "A woman with wet slicked-back hair, bold glossy red lips, wearing oversized black futuristic sunglasses",
    "wardrobe": "bare shoulders, likely nude or minimal to enhance focus on face and accessories",
    "props": "large slice of juicy {argument name="fruit" default="watermelon"} held in front of her mouth"
  },
  "scene": {
    "location": "high-key white background studio with strong directional light",
    "time_of_day": "midday impression (stylized lighting)",
    "environment": "wet gloss aesthetic with moisture drops on skin"
  },
  "visual_details": {
    "action": "she holds the watermelon close to her mouth, lips parted sensually",
    "lighting_effects": "hard light reflections on sunglasses, wet skin and watermelon surface"
```

[[Fashion Editorial]] [[High Key Lighting]]

---

### 151. 霓虹蓝上衣的电影感人像提示

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-01-20  **Language**: en

> 一个文本提示，用于生成一张年轻女性的电影感肖像，情绪低沉，皮肤清透，妆容极简。提示中指定了蓬松的深棕色头发，平静的表情，身穿霓虹蓝色上衣，置身于黑暗简约的背景中。它强调柔和的漫射光，柔和的阴影，微妙的胶片颗粒感，以及有机色彩分级，以营造高端的杂志编辑感。

![霓虹蓝上衣的电影感人像提示](https://cms-assets.youmind.com/media/1768977291971_eckawb_G_FC3FVXQAEs9cd.jpg)
![霓虹蓝上衣的电影感人像提示](https://cms-assets.youmind.com/media/1768977291977_vzi6dx_G_FC3FbXUAELI-W.jpg)
![霓虹蓝上衣的电影感人像提示](https://cms-assets.youmind.com/media/1768977292030_fw481q_G_FC3FVXQAAquCs.jpg)

```
Create Moody cinematic portrait of a young woman with clear fair skin and barely-there makeup, warm natural lips. Loose dark brown hair, softly textured. Calm, self-assured expression. She’s wearing a {argument name="clothing color" default="neon blue"} top elegance. Dark minimal background fading into black. Gentle diffused front light, soft shadows, subtle film grain, organic color grading, shallow depth of field, high-end editorial feel.
```

[[Fashion Editorial]] [[Cinematic Portrait]] [[Film Grain Aesthetic]] [[Diffused Lighting]]

---

### 152. 时尚大片：女子躺在保时捷旁的柏油路上

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-20  **Language**: en

> 一个用于创建高对比度、高时尚感的鸟瞰视角编辑图像的提示。画面中，一名身穿酒红色紧身衣和黑色连裤袜的女子，以动感的姿势躺在沥青上，旁边是一辆橙色的保时捷 911。风格忧郁且富有电影感，使用单一的明亮闪光灯营造出深邃的阴影和高光，强调纹理和锐利的细节。

![时尚大片：女子躺在保时捷旁的柏油路上](https://cms-assets.youmind.com/media/1768977336385_1ailum_G_EdB9MWAAAlmXI.jpg)
![时尚大片：女子躺在保时捷旁的柏油路上](https://cms-assets.youmind.com/media/1768977336488_qfi27i_G_EdB6zX0AATT1V.jpg)

```
Create a high fashion editorial look: a bird's eye view of a woman lying on the asphalt, leaning against an {argument name="car color" default="orange"} Porsche 911 sports car, wearing a {argument name="outfit color" default="burgundy"} off-the-shoulder bodysuit, sheer black tights, and black stiletto heels. The pose is dynamic and elegant: legs slightly bent, hair down, arms relaxed and at the sides, with slight tension in the hips and shoulders. A moody nighttime street scene with a single bright flash from above creates strong contrast, deep shadows, and bright highlights on the car's red paint. Emphasize texture: the glossy surface of the car, the matte fabric, and the visible tire tracks on the asphalt. Use a cinematic color palette: rich reds, deep blacks, warm, natural flesh tones, subtle film grain, high contrast, and sharp details. Use high-resolution details. Use high resolution, ASR resolution, and a shallow depth of field to slightly reduce the background and focus on the clothing.
```

[[Fashion Editorial]] [[High Contrast Photography]] [[Luxury Automobile]]

---

### 153. 藤椅上的绯红时尚大片

**Author**: [Aylin](https://x.com/kashmir_ki_lark)  **Date**: 2026-01-19  **Language**: en

> 生成一张电影级、时尚大片风格的图片，描绘一位年轻女性身着深红色两件套服装，慵懒地躺在悬挂的藤制茧形椅中。提示中详细说明了瓷器般光滑的皮肤、蓝绿色的眼睛、蓬松的发髻、哑光深红色嘴唇，以及黄金时段的侧逆光，以呈现超现实的 8K 效果。

![藤椅上的绯红时尚大片](https://cms-assets.youmind.com/media/1768890655291_ymy6kv_G_CeZS7WkAAGrXI.jpg)

```
Stunning young woman in her early twenties with flawless porcelain skin and striking blue-green eyes that catch the light, conveying a calm, dreamy serenity. Her facial features are refined and harmonious, with high cheekbones and soft contours. Blonde hair is styled in a luxurious, soft, voluminous updo, gently lifted at the crown, with a few delicate wisps and loose tendrils framing her face for an effortless, romantic feel. Makeup is cinematic and elegant: subtle smokey eyes with blended charcoal and warm brown tones, softly defined brows, long natural lashes, luminous glowing skin with a hint of warmth, and bold matte crimson-red lips that stand out dramatically yet tastefully.

She wears an off-shoulder crimson red two-piece outfit designed to emphasize grace and femininity. The top is a puffy long-sleeve crop top with gathered fabric and soft volume, exposing her collarbones and shoulders, while the high-waisted flowing red maxi skirt drapes fluidly over her legs, revealing a toned midriff and creating elegant movement in the fabric. The rich red fabric appears silky and luxurious, catching light beautifully and adding depth and saturation to the scene.

The woman is lounging gracefully inside a large cream-colored hanging rattan cocoon chair, suspended gently, its woven texture adding a natural, bohemian element. Her posture is relaxed and poised, body slightly reclined, hands resting naturally, radiating effortless elegance. The setting is a modern boho-chic interior featuring neutral tones, soft textiles, natural wood, and organic materials, minimal yet stylish, enhancing the subject without distraction.

Lighting is golden hour side lighting, warm and directional, casting gentle shadows across her face and body, highlighting skin texture, fabric folds, and the woven chair. The atmosphere feels cinematic and intimate, like a high-end fashion film still. The color palette emphasizes rich saturated reds contrasted against soft creams and warm neutrals. Shot with shallow depth of field for a dreamy background blur, ultra-detailed, hyper-realistic, high fashion editorial quality, masterpiece, 8k resolution.
```

[[Fashion Editorial]] [[Hyperrealistic Photography]] [[Golden Hour Photography]] [[8K Portrait]]

---

### 154. Y2K 复古魅力写真拍摄

**Author**: [Miz](https://x.com/mizq06)  **Date**: 2026-01-19  **Language**: en

> 一个结构化的图像提示，用于生成一张复古风格、高细节的时尚编辑照片：一名女性在夜晚倚靠在一辆老爷车旁，采用 Y2K 美学和直射闪光摄影。

![Y2K 复古魅力写真拍摄](https://cms-assets.youmind.com/media/1768890635360_o3easa_G_B1ulNXsAEj-W_.jpg)
![Y2K 复古魅力写真拍摄](https://cms-assets.youmind.com/media/1768890636823_3gcdvj_G_B1ulPWwAANCBN.jpg)

```
{
  "prompt": "A retro-inspired nighttime photoshoot of a red-haired woman leaning into a pink vintage convertible. She wears a {argument name="top" default="leopard-print off-shoulder top"} and white denim shorts, accessorized with a red necklace. Her long wavy hair cascades over one shoulder. The scene is lit with flash photography against a dark blue night sky and tree silhouettes, creating a bold contrast. Playful yet sultry mood, early 2000s aesthetic, glossy magazine editorial style.",
  "style": [
    "photorealistic",
    "Y2K aesthetic",
    "retro glamour",
    "editorial fashion"
  ],
  "camera": {
    "angle": "eye-level",
    "lens": "35mm",
    "lighting": "direct flash",
    "depth_of_field": "moderate"
  },
  "environment": "outdoor roadside setting at night with vintage car",
  "mood": "flirty, confident, nostalgic",
  "quality": "high detail, sharp focus, magazine-quality"
}
```

[[Fashion Editorial]] [[Flash Photography]] [[Y2K Aesthetic]] [[Night Photography]]

---

### 155. 情绪化电影感人像

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-01-19  **Language**: en

> 一个用于生成情绪化、高端时尚的年轻女性肖像的提示，重点突出清晰的皮肤、柔和的灯光、极简的背景和微妙的胶片颗粒美学。

![情绪化电影感人像](https://cms-assets.youmind.com/media/1768890637628_z9v1aj_G_BycivWIAAAcaW.jpg)
![情绪化电影感人像](https://cms-assets.youmind.com/media/1768890637657_qnspfr_G_BychdWEAASnd8.jpg)
![情绪化电影感人像](https://cms-assets.youmind.com/media/1768890638575_lij2xd_G_BycgvWYAAnK1S.jpg)
![情绪化电影感人像](https://cms-assets.youmind.com/media/1768890639470_omjhiz_G_BychzXEAAwPkn.jpg)

```
Moody cinematic portrait of a young woman with clear fair skin and barely-there makeup, warm natural lips. Loose dark brown hair, softly textured. Calm, self-assured expression. She's wearing a fitted black turtleneck sweater, clean lines, understated elegance. Dark minimal background fading into black. Gentle diffused front light, soft shadows, subtle film grain, organic color grading, shallow depth of field, high-end editorial feel.
```

[[Fashion Editorial]] [[Film Grain Aesthetic]] [[Minimalist Background]] [[Diffused Lighting]]

---

### 156. 巴黎街头情绪人像摄影

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-19  **Language**: en

> 一个高度详细的提示，用于生成一张在巴黎黄昏时分的超写实、情绪化的街头编辑肖像。它详细描述了拍摄对象的样貌、精致的服装（带羊毛领的超大棕色皮大衣）以及复杂的背景元素（复古店面、窗户上的法文、模糊的室内物品），以营造出一种电影扫描般的舒适冬季美学。

![巴黎街头情绪人像摄影](https://cms-assets.youmind.com/media/1768890681948_8164u2_G_BwUJvXAAAoetG.jpg)

```
Ultra-realistic moody Paris street editorial portrait, shot outside a vintage shopfront at dusk/overcast twilight, film-scanned look. A young woman (early–mid 20s), fair skin, slim build, shoulder-length light brown/dark blonde hair with a soft center/loose part, slightly tousled ends. Expression: calm, distant, slightly tired gaze; lips relaxed, almost pouting; eyes looking straight at camera with subtle softness. Pose: standing close to the shop entrance, shoulders slightly forward, body angled 3/4; one hand tucked into the coat pocket (hand visible at pocket opening), the other arm relaxed inside the oversized coat. She is framed from mid-thigh to a little above head, vertical portrait.

Wardrobe: oversized {argument name="coat material" default="brown leather/bomber-style coat"} with a worn matte sheen, slightly wrinkled texture; very large fit with dropped shoulders. Collar: thick black shearling/faux-fur collar folded up around the neck. No visible logos, no jewelry emphasis.

Location / Background details:

•She stands at the edge of a dark green/black painted wooden doorframe with aged patina; the frame runs vertically on the right side of the image.

•Behind her is a large shop window with reflective glass showing faint street reflections (trees/sky shapes), but interior objects remain visible.

•At the very top of the window, large curved cream lettering reads: “{argument name="window text" default="VINS DE PROPRIÉTÉS"}” (French text, arched across the glass).

•Inside the shop window, a botanical poster is visible on the left side (green leaves illustration), slightly blurred due to depth/reflection.

•Lower left inside the window: a display area with dark surfaces and small objects (bottles/produce-like shapes), dimly lit.

•On the far right edge, partially inside the frame, a black menu/chalkboard with small white writing is visible (text not fully readable), aligned vertically near the doorframe.

Lighting: natural ambient street light, soft and diffused; gentle highlights on cheekbones and nose; shadows are deep but not crushed. No direct flash. The shop interior glows faintly warm compared to the cooler exterior.

Color / Tone / Aesthetic: muted brown, olive-green, charcoal palette; cinematic, slightly desaturated; subtle warm sundayfunday undertone in skin and shop interior; overall dark, cozy, rainy-winter vibe (even if no rain visible). Film grain present, slight halation on highlights, mild vignette, soft contrast roll-off. Background softly blurred but readable; subject sharpest point is face and coat collar. Cooks. 

Composition / Camera: vertical portrait (approx 4:5 feel), subject centered slightly left; window text occupies upper third; doorframe and menu board anchor the right third; medium shot at eye level, ~50mm perspective, shallow-to-moderate depth of field, realistic lens softness toward edges.

Surface / python Texture cues: aged paint on doorframe, smudged window reflections, leather coat creases, fur collar fibers visible, fine pores and natural skin texture
```

[[Fashion Editorial]] [[Winter Fashion]] [[Overcast Lighting]]

---

### 157. 奢华度假村比基尼肖像提示

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-01-19  **Language**: en

> 一个详细的 JSON 提示，用于生成一张中景、照片级的女性肖像，背景设在豪华热带度假村。它详细说明了拍摄对象的体格（健美、曲线优美、晒黑的皮肤）、服装（白色纹理抹胸比基尼，带泡泡袖）、姿势（坐在白色沙发上）和光线（来自大玻璃门的柔和、漫射的自然日光），以营造宁静、度假氛围的时尚编辑美学。

![奢华度假村比基尼肖像提示](https://cms-assets.youmind.com/media/1768890696274_kot6aw_G_A1EepXkAE0Eas.jpg)

```
{
"subject": {
"description": "Young woman with a fit, curvaceous physique and tanned skin, seated indoors.",
"hair": "Shoulder-length, wavy dirty blonde to light brown hair, parted in the center, loose and framing the face.",
"face": "Oval face shape, neutral to soft expression, full lips, defined eyebrows, minimal natural makeup, direct eye contact.",
"body": "Athletic yet soft figure, prominent bust visually matching reference volume, toned abdomen, defined waistline, soft skin texture with natural tan.",
"clothing": "{argument name="bikini color" default="White"} textured 'smocked' or 'crinkle' fabric bikini set. Top is a straight bandeau style with detached off-the-shoulder short puff sleeves. Bottoms are matching textured fabric with side ties, sitting low on the hips.",
"accessories": "Small gold hoop earrings, a delicate gold pendant necklace."
},
"pose": {
"posture": "Seated on a white sofa, body slightly angled to the viewer's right, face turned forward.",
"arms": "Right arm extended straight down with palm resting on the sofa cushion. Left arm relaxed, hand resting gently on the upper left thigh.",
"legs": "Legs are bent at the knees and angled together towards the viewer's right, creating a diagonal line across the lower frame.",
"head": "Upright, facing the camera directly with a calm gaze."
},
"environment": {
"setting": "Bright, upscale interior living space, likely a tropical resort villa.",
"foreground": "White upholstered sofa with plush cushions, textured woven rug on the floor.",
"background": "Large floor-to-ceiling wooden-framed glass sliding doors leading to an outdoor patio. Visible through the glass are lush green palm trees and white resort-style buildings with brown tiled roofs.",
"ceiling": "White ceiling with prominent dark wood exposed beams.",
"decor": "Minimalist luxury, white curtains bunched at the sides of the glass doors."
},
"camera": {
"shot_type": "Medium shot, captured from knees up.",
"angle": "Eye-level, straight on.",
"focal_length": "50mm equivalent, standard perspective with minimal distortion.",
"depth_of_field": "Subject in sharp focus, background slightly softened but distinct enough to identify architectural details.",
"framing": "Centered subject, balanced composition with headroom below the ceiling beams."
},
"lighting": {
"source": "Natural daylight entering from the large glass doors behind and to the side of the subject.",
"quality": "Soft, diffuse, high-key lighting.",
"shadows": "Gentle, natural shadows on the right side of the subject's face and body (viewer's left), indicating light source dominance from the background/right.",
"skin_rendering": "Realistic subsurface scattering, capturing the glow of tanned skin without artificial gloss."
},
"mood_and_expression": {
"emotion": "Calm, confident, relaxed, sultry.",
"atmosphere": "Serene, vacation vibe, luxurious, bright.",
"gaze": "Direct, engaging, unsmiling but pleasant."
},
"style_}
```

[[Fashion Editorial]] [[Lifestyle Portrait]] [[Bikini Fashion]] [[Diffused Natural Light]]

---

### 158. 欧洲街头的电影感夜间人像

**Author**: [Sandip Sharma✍](https://x.com/SandipSharmaEng)  **Date**: 2026-01-19  **Language**: en

> 一个 JSON 提示，用于生成一张年轻女性在夜晚的欧洲老街上，身穿金属银色紧身连衣裙的超逼真电影感肖像。它强调戏剧性元素，如大胆的红色口红、城市灯光形成的深邃焦外虚化，以及温暖的金色街灯照明，以营造出精致而神秘的氛围。

![欧洲街头的电影感夜间人像](https://cms-assets.youmind.com/media/1768890683429_0u8ymy_G_AtpbIXIAAMQQm.jpg)
![欧洲街头的电影感夜间人像](https://cms-assets.youmind.com/media/1768890683510_au6ve9_G_AtpbBWMAAcFh9.jpg)
![欧洲街头的电影感夜间人像](https://cms-assets.youmind.com/media/1768890683958_4ifyxo_G_AtpdgXkAA3OqJ.jpg)

```
{
  "image_type": "Photorealistic cinematic portrait",
  "subject": {
    "person": "Young woman (fictional model)",
    "facial_features": {
      "skin": "Smooth with natural sheen and realistic texture",
      "eyes": "Deep hazel-green with sharp focus and catchlight",
      "lips": "Bold matte {argument name="lipstick color" default="red"} lipstick",
      "expression": "Alluring and mysterious, looking back over the shoulder"
    },
    "hair": {
      "color": "Dark chocolate brown",
      "style": "Long, voluminous loose waves",
      "texture": "Silky with high shine"
    },
    "attire": {
      "garment": "Bodycon maxi dress",
      "material": "{argument name="dress material" default="Metallic silver fabric"} with a liquid metal effect",
      "design_details": [
        "Dramatic open back",
        "Thin criss-cross lace-up straps",
        "High thigh-high side slit"
      ],
      "accessories": "Large crystal hoop earrings"
    }
  },
  "environment": {
    "location": "Old European street at night",
    "architecture": "Baroque style facades and cobblestone pavement",
    "atmosphere": "Sophisticated, romantic, and moody"
  },
  "technical_details": {
    "lighting": "Warm golden street lamps with soft rim lighting",
    "background": "Deep bokeh effect with blurred city lights",
    "composition": "Medium-full shot, over-the-shoulder pose"
  }
}
```

[[Fashion Editorial]] [[Night Photography]] [[Metallic Dress]]

---

### 159. 芥末色毛衣美学肖像提示词

**Author**: [Maercih](https://x.com/Maercihh)  **Date**: 2026-01-19  **Language**: en

> 一个结构化的提示，用于生成一张具有 Instagram 美学风格的时尚编辑肖像照，照片中一位年轻女性身穿芥末黄色针织毛衣。强调柔和的闪光灯照明、电影般的阴影、35 毫米镜头效果，以及粗糙水泥墙背景下对高细节皮肤纹理的超清晰聚焦。

![芥末色毛衣美学肖像提示词](https://cms-assets.youmind.com/media/1768890689116_d9o21b_G_AOc2KXEAEVYiT.jpg)

```
{
  "prompt_title": "Mustard Sweater Aesthetic Portrait",
  "subject": {
    "description": "Young woman",
    "hair": "Long black hair",
    "pose": "Resting face on hand",
    "expression": "Neutral, relaxed"
  },
  "styling": {
    "eyewear": "Round transparent glasses",
    "makeup": "Soft natural makeup, glossy lips, defined eyelashes",
    "vibe": "Instagram aesthetic, fashion editorial"
  },
  "apparel": {
    "outerwear": "{argument name="sweater color" default="Mustard yellow"} knitted sweater",
    "layering": "Black mesh top underneath",
    "texture": "Knitted, mesh"
  },
  "environment": {
    "setting": "Indoor",
    "background": "Rough concrete wall",
    "atmosphere": "Cozy, moody"
  },
  "photography_technical": {
    "angle": "Shot from slightly above",
    "lighting": "Soft flash lighting, cinematic shadows, warm color tones",
    "camera_style": "35mm lens look, realistic photography",
    "focus": "Shallow depth of field, ultra sharp focus",
    "details": "High detail skin texture, HD quality",
    "aspect_ratio": "9:13"
  }
}
```

[[Fashion Editorial]] [[Skin Texture Detail]] [[Instagram Aesthetic]] [[Concrete Wall Background]]

---

### 160. 时尚专题肖像与叙事 JSON 提示

**Author**: [Lexi](https://x.com/missbehaveai)  **Date**: 2026-01-18  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张具有叙事元素的时尚编辑肖像照，描绘一位年轻女性走进公寓走廊，嘴里叼着钥匙，身穿风衣，内搭内衣。它详细说明了姿势、环境和技术风格。

![时尚专题肖像与叙事 JSON 提示](https://cms-assets.youmind.com/media/1768804205667_9hicvp_G--j4JmXsAAoWOl.jpg)

```
{
  "prompt_type": "descriptive_portrait",
  "subject_details": {
    "demographics": "Young female, light skin, tall.",
    "facial_features": {
      "expression": "Holding a set of keys between her teeth, smiling with eyes, looking relieved and mischievous.",
      "eyes": "Grey-blue eyes.",
      "hair": "Straight light brown/dark blonde hair, silky and shiny."
    },
    "apparel": {
      "dress": "A long beige trench coat aimed to be taken off, open wide to reveal a black lace bodysuit/lingerie underneath.",
      "accessories": "A shoulder bag slipping off her arm.",
      "footwear": "One high heel shoe on, the other kicked off on the floor."
    }
  },
  "pose_and_action": {
    "body_position": "Standing in the hallway, leaning back against the closed door.",
    "hands": "One hand struggling with the coat, the other holding the phone high.",
    "camera_angle": "Full body reflection in a tall hallway mirror."
  },
  "background_environment": {
    "location": "Apartment hallway / entryway.",
    "lighting_source": "Warm overhead hallway light.",
    "objects": {
      "entry": "A coat rack, a mail table with letters, the door behind her."
    }
  },
  "technical_specs": {
    "style": "Fashion editorial meets candid life, sharp details, glamorous.",
    "aspect_ratio": "4:5"
  }
}
```

[[Fashion Editorial]] [[Cinematic Portrait]]

---

### 161. 现代楼梯上的奢华时尚大片

**Author**: [Emma](https://x.com/emmagpt0)  **Date**: 2026-01-18  **Language**: en

> 为 Gemini Nano Banana Pro 提供的详细文本提示，用于生成一张专业的时尚照片：一位铂金发色女性身穿海军蓝连衣裙，自信地摆姿势站在现代简约的悬浮楼梯上，强调奢华生活方式美学和明亮的自然光线。

![现代楼梯上的奢华时尚大片](https://cms-assets.youmind.com/media/1768804275829_mpv73d_G--b_INXQAAI_w6.jpg)
![现代楼梯上的奢华时尚大片](https://cms-assets.youmind.com/media/1768804276199_bdllpt_G--b_IDW8AAhg4J.jpg)

```
"A platinum blonde woman with long flowing hair standing on modern wooden staircase looking back over shoulder at camera with warm smile, wearing elegant navy blue dress with sheer mesh turtleneck collar detail, wide kimono-style short sleeves, fitted bodycon ruched mini skirt showing long tanned bare legs, navy blue patent leather high heels with platform, one hand on metal stair railing, other hand raised touching white wall, confident pose with legs apart ascending stairs, tan healthy skin glowing in natural light, side profile view showing feminine curves and athletic legs, modern minimalist interior with light wood floating stairs, brushed steel cable railings, white walls, bright natural lighting creating soft shadows, clean contemporary architecture, professional fashion photography, editorial style, photorealistic quality, high resolution, elegant sophisticated aesthetic, luxury lifestyle imagery",
  
  "negative_prompt": "blurry, low quality, distorted proportions, unrealistic anatomy, oversaturated colors, harsh lighting, grainy, pixelated, cartoon, anime, illustration, heavy filters, poor composition, dark muddy colors, artificial look, bad focus, cluttered background",
  
  "details": {
    "subject": "Long platinum blonde hair past shoulders, warm smile looking back, navy blue dress with sheer mesh high neck, kimono sleeves, fitted ruched mini skirt, bare tanned legs, navy patent platform heels, confident ascending pose on stairs",
    "setting": "Modern floating staircase with light wood steps, steel cable railings, white minimalist walls, bright natural diffused lighting, clean contemporary residential interior",
    "composition": "Side back three-quarter view, subject on stairs looking over shoulder, dynamic diagonal lines from staircase, elegant feminine pose with one hand on railing and one on wall",
    "style": "Professional editorial fashion photography, luxury lifestyle aesthetic, bright clean lighting, high-end commercial quality, sophisticated elegant mood"
  }
```

[[Fashion Editorial]] [[Natural Light Photography]] [[Luxury Lifestyle]]

---

### 162. 女性主题的高级时装编辑图片提示

**Author**: [Sandip Sharma✍](https://x.com/SandipSharmaEng)  **Date**: 2026-01-18  **Language**: en

> 这个详细的图像生成提示以 JSON 格式构建，描述了一位女性主体身着华丽红色亮片礼服的全身时尚编辑照片。它包含了关于外貌、服装、带有抽象金色道具的极简主义影棚环境以及电影级灯光的精确细节，旨在呈现出超现实、高端时尚杂志的美感。

![女性主题的高级时装编辑图片提示](https://cms-assets.youmind.com/media/1768804243291_i4nhng_G-9Gx6kWcAAM2b_.jpg)
![女性主题的高级时装编辑图片提示](https://cms-assets.youmind.com/media/1768804243281_t05pa2_G-9GyAZWkAAME7K.jpg)
![女性主题的高级时装编辑图片提示](https://cms-assets.youmind.com/media/1768804243425_b7cv3i_G-9Gx6nWkAEe-_A.jpg)
![女性主题的高级时装编辑图片提示](https://cms-assets.youmind.com/media/1768804244964_j1p4ca_G-9GyBRXoAEZ7tg.jpg)

```
{
  "image_description": {
    "subject": {
      "gender": "female",
      "appearance": {
        "hair": "Dark brown, mid-length, styled in voluminous glamorous waves with a side part",
        "makeup": "Sultry smokey eye shadow, defined brows, and a matte nude-rose lipstick",
        "pose": "Full-body frontal shot, standing with one leg forward through a slit, slight head tilt, and hand resting gracefully on the hip"
      },
      "attire": {
        "dress_type": "Floor-length evening gown",
        "material": "{argument name="dress material" default="Red sequined fabric with a metallic shimmer"}",
        "features": [
          "Deep plunging V-neckline",
          "Sleeveless design",
          "Gathered/wrapped waist detail",
          "High thigh-high side slit"
        ],
        "footwear": "Classic black pointed-toe stiletto heels",
        "jewelry": "Silver or diamond-encrusted long drop earrings"
      }
    },
    "environment": {
      "setting": "Minimalist high-fashion studio",
      "background_color": "Charcoal grey and slate",
      "props": "Two large, abstract, fluid-shaped sculptures in a polished metallic gold finish",
      "lighting": "Soft, cinematic directional lighting creating subtle shadows and highlighting the texture of the sequins"
    },
    "composition": {
      "framing": "Centrally framed subject",
      "color_palette": ["Burgundy Red", "Gold", "Charcoal Grey", "Black"],
      "style": "Editorial fashion photography"
    }
  }
}
```

[[Fashion Editorial]] [[Minimalist Studio]] [[Sequin Dress]] [[Full Body Fashion Shot]]

---

### 163. 博物馆里的红裙时尚肖像

**Author**: [ARWEN](https://x.com/VOIDRNETWORK)  **Date**: 2026-01-18  **Language**: en

> 一个写实风格的时尚肖像提示，描绘了一位女性（艾米丽·拉塔科夫斯基 Emily Ratajkowski 的形象）坐在一座宏伟艺术博物馆的大理石壁架上。该提示强调了她醒目的红色露背迷你连衣裙与背景中柔和的、镶金边的古典油画之间的对比，旨在营造一种柔和漫射光下的高级时尚杂志风格。

![博物馆里的红裙时尚肖像](https://cms-assets.youmind.com/media/1768804232345_ezgcgx_G-8HoTjXAAEG1o2.jpg)

```
{
  "prompt_type": "photorealistic fashion portrait",
  "main_composition": "medium full-body view of a single young woman sitting elegantly on the edge of a marble table or display ledge in a grand art museum gallery, legs crossed with one hand resting on the surface for balance, subtle confident gaze directed at camera with slight head tilt, bold red dress contrasting classical paintings behind, sophisticated museum setting with velvet rope barrier",
  "subject": {
    "description": "beautiful young woman in her early 20s, attractive feminine features with light glamorous makeup (defined eyeliner, long lashes, subtle contour, neutral glossy lips), long loose wavy light brown or auburn hair with natural volume cascading over shoulders, fair smooth skin with healthy glow, slim athletic hourglass figure",
    "clothing": "striking bright {argument name=\"dress color\" default=\"red\"} halter-neck mini dress with intricate geometric cutouts across bodice and midriff creating bold revealing design, fitted stretch fabric ending mid-thigh, paired with sheer black pantyhose or stockings with subtle opacity",
    "details": "relaxed seated pose with legs elegantly crossed and slight forward lean, manicured neutral nails, hair naturally tousled with soft waves, confident subtle expression with direct eye contact and faint smile"
  },
  "environment": {
    "foreground": "polished warm-toned wooden parquet floor reflecting light, black velvet rope stanchion barrier on left",
    "midground": "woman centered on marble-topped display table or ledge with veined pinkish stone",
    "background": "grand art museum gallery with dark gray or charcoal walls adorned with large ornate gold-framed classical oil paintings (Rococo or Neoclassical style depicting figures in period dress), subtle informational plaques below paintings, elegant formal museum interior"
  },
  "lighting_and_atmosphere": "soft diffused museum overhead lighting with warm ambient glow highlighting skin, red dress fabric, and gold frames, gentle shadows enhancing cutout details and painting textures, sophisticated luxurious art gallery vibe with high contrast between bold red dress and muted classical backdrop, photorealistic detail evoking high-fashion editorial in cultural setting",
  "technical_quality": "highly detailed, sharp focus on dress cutouts, fabric texture, hair strands, skin glow, and painting frame details, 8k resolution, realistic material sheen on red fabric and marble surface, professional fashion photography style with natural depth of field softly blurring distant paintings",
  "negative_prompt_suggestions": "blurry, deformed, extra limbs, harsh museum flash, overexposed dress, underexposed paintings, low quality, cartoon, anime, text watermark, extra people, cluttered gallery, modern art, bright daylight"
}
```

[[Fashion Editorial]] [[Soft Diffused Light]] [[Red Mini Dress]] [[Museum Setting]]

---

### 164. Vogue 杂志在科莫湖 Riva 游艇上的社论

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-01-18  **Language**: en

> 为《Vogue》杂志社论风格照片生成超现实图像的提示，照片中一位优雅的亚洲女性身着高级定制白色长裙，坐落在意大利科莫湖上一艘经典的木制 Riva 船中。该提示详细描述了拍摄对象的特征、配饰、风景环境以及 8K 分辨率、电影级灯光和 9:16 宽高比等技术规格，旨在营造一种“老钱”美学。

![Vogue 杂志在科莫湖 Riva 游艇上的社论](https://cms-assets.youmind.com/media/1768804293866_xa73y8_G-6lai7WMAA9IP8.jpg)

```
{
  "image_prompt_structure": {
    "subject": {
      "description": "Sophisticated Asian woman sitting in a luxury wooden motorboat",
      "features": "Long straight black hair, flawless fair skin, red lipstick, elegant pose adjusting sunglasses",
      "action": "One hand touching sunglasses frame, other hand resting on boat seat near handbag"
    },
    "apparel": {
      "dress": "White strapless pleated chiffon maxi dress, flowing fabric, high couture style",
      "accessories": "Oversized brown gradient sunglasses, layered gold chain necklace, gold bracelets, beige quilted luxury handbag (Lady Dior style)"
    },
    "environment": {
      "location": "{argument name="location" default="Lake Como Italy"}, middle of the lake",
      "boat": "Classic Riva style wooden boat, polished mahogany wood finish, cream beige leather upholstery",
      "background": "Scenic mountains, lush green coastline with Italian villas, deep blue water with boat wake, blue sky with soft clouds"
    },
    "technical_specs": {
      "style": "Ultra realistic, 8k resolution, cinematic photography, vogue editorial aesthetic, old money vibe",
      "lighting": "Bright natural daylight, harsh sunlight creating sharp shadows, high contrast, glossy finish",
      "camera": "Shot on 35mm lens, f/2.8, sharp focus on subject, detailed textures"
    },
    "parameters": {
      "aspect_ratio": "--ar 9:16",
      "quality": "--q 2",
      "stylize": "--s 750",
      "version": "--v 6.0"
    }
  },
  "full_prompt_string": "A sophisticated Asian woman sitting in a classic wooden Riva boat on Lake Como, wearing a white strapless pleated maxi dress and layered gold necklaces, adjusting oversized sunglasses, red lipstick, beige quilted luxury handbag on the cream leather seat, scenic mountains and Italian villas in background, deep blue water with wake, bright natural sunlight, cinematic lighting, ultra realistic, 8k, vogue editorial, old money aesthetic --ar 9:16 --v 6.0 --style raw"
}
```

[[Fashion Editorial]] [[Old Money Aesthetic]] [[9:16 Vertical Format]]

---

### 165. 冬季社论低角度下蹲姿势提示（iPhone 风格）

**Author**: [inanna](https://x.com/inannaai)  **Date**: 2026-01-17  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张超现实的冬季时尚编辑照片：一名女性在雪中深蹲，从低角度拍摄，强调高级时装的疏离感、原始的智能手机真实感，并包含服装、姿势和相机设置（iPhone 16 Pro Max）的具体细节。

![冬季社论低角度下蹲姿势提示（iPhone 风格）](https://cms-assets.youmind.com/media/1768717551636_k85sdf_G-1RiiqXkAAGVwZ.jpg)

```
{
  "subject": {
    "character": "uploaded_photo",
    "face_consistency": "true",
    "body_consistency": "true",
    "gender": "female",
    "age_appearance": "young adult, early 20s",
    "ethnicity": "Northern European",
    "emotion": "cold confidence, composed, stoic, high-fashion detachment",

    "hair": {
      "color": "icy platinum blonde",
      "length": "shoulder-length",
      "style": "loose waves peeking out from under a hat",
      "texture": "soft, slightly tousled by winter air",
      "placement": "framing the face and falling over the shoulders"
    },

    "face": {
      "visibility": "partially visible",
      "profile_visibility": "front-facing",
      "skin_tone": "porcelain, pale",
      "expression": "neutral, relaxed mouth, editorial gaze behind glasses"
    }
  },

  "meta": {
    "aspect_ratio": "1:1",
    "camera": "iPhone 16 Pro Max rear main camera",
    "lens": "24mm f/1.78 smartphone wide lens",
    "focal_character": "sharp focus on subject, natural depth of field",
    "quality": "ultra-realistic, high-resolution photography",
    "style": "outdoor winter editorial, raw smartphone realism, authentic skin texture, sharp details"
  },

  "visibility_rules": {
    "mirror_only": false,
    "no_direct_subject_visibility": false,
    "no_body_parts_outside_mirror": false
  },

  "camera_angle": {
    "vertical_position": "low angle, camera positioned at subject knee height looking slightly up",
    "horizontal_alignment": "centered on subject",
    "tilt": "slight upward tilt to capture the crouched pose",
    "yaw": "camera facing directly at the subject",
    "roll": "0 degrees, perfectly level horizon",
    "distance_to_mirror_meters": 0,
    "handheld_behavior": "stable handheld shot"
  },

  "body_angle": {
    "global_orientation": "front-facing, crouched",
    "torso_rotation_degrees": 0,
    "shoulder_alignment": "square to camera",
    "hip_rotation_degrees": 0,
    "weight_distribution": "evenly distributed in a deep squat",
    "posture": "crouched low to the ground, balanced"
  },

  "head_angle": {
    "rotation_degrees": 0,
    "tilt": "perfectly level",
    "chin_position": "neutral",
    "neck_tension": "relaxed"
  },

  "phone_angle": {
    "phone_model": "none",
    "height_relative_to_face": "n/a",
    "distance_from_face_cm": 0,
    "angle": "n/a",
    "coverage": "none"
  },

  "pose": {
    "legs": {
      "stance": "crouched/squatting",
      "front_leg": "knees bent outward",
      "back_leg": "knees bent outward"
    },
    "hips": {
      "action": "lowered to heels"
    },
    "arms": {
      "right_hand": "hand raised to temple, fingers lightly touching the frame of the sunglasses",
      "left_hand": "arm extended downward, hand reaching toward the snow surface, fingers spread"
    }
  },

  "clothing": {
    "outfit_type": "long-sleeve bodysuit",
    "color": "dark charcoal grey",
    "material": "ribbed cotton or technica"
  }
}
```

[[Fashion Editorial]] [[Low Angle Shot]] [[High Fashion]] [[Snow Scene]]

---

### 166. 奢华零售编辑场景与象征性苹果

**Author**: [AI Tales - Not by Humans](https://x.com/AITalesNBH)  **Date**: 2026-01-16  **Language**: en

> 一个用于生成名为“都市欲望”的奢侈品零售编辑图片的结构化 JSON 提示。场景设定在一个极简主义的旗舰科技店中，拥有玻璃和光线构筑的建筑。画面中，一位女士手持一个高举的苹果，一名男士在背景中不经意地看着她，暗示着微妙的吸引。该提示侧重于象征性的克制、电影般的构图（50mm 定焦镜头）以及干净、现代的美学。

![奢华零售编辑场景与象征性苹果](https://cms-assets.youmind.com/media/1768631192732_0wcxb7_G-zmqzzW8AABAaf.jpg)

```
{
"project": "Nano Banana – Urban Desire | Retail Editorial Scene",
"version": "NB-2.3",

"input_required": {
"upload_person_image": false,
"customization_note": "Generates original characters with consistent identity and controlled narrative focus."
},

"scene_meta": {
"category": "Luxury Retail Editorial",
"aesthetic": "Modern, cinematic, symbolic restraint",
"narrative_density": "Implied symbolism",
"brand_safety": "No logos emphasized, no readable UI text"
},

"frame": {
"aspect_ratio": "4:5",
"camera": {
"sensor_format": "Full-frame",
"lens": "50mm prime",
"aperture": "f/1.8",
"focus": "Primary focus on woman's face and raised hand with apple"
},
"shot_type": "Medium-full body",
"angle": "Eye-level",
"composition": "Foreground dominance with elevated hand entering upper frame, background softly receding"
},

"environment": {
"location_type": "Minimalist flagship tech retail store",
"interior_style": "Clean, modern, glass-and-light architecture",
"materials": [
"Light wood tables",
"Glass surfaces",
"White walls",
"Soft reflective flooring"
],
"background_activity": {
"secondary_subject": "Man standing behind the woman",
"action": "Holding a displayed smartphone",
"gaze_direction": "Looking discreetly at the woman rather than the device",
"behavior_note": "Subtle, restrained attraction conveyed through eye-line and posture only"
}
},

The prompt continues in the first comment
```

[[Fashion Editorial]] [[Cinematic Composition]]

---

### 167. 时尚大片：口红留言的镜中自拍

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-15  **Language**: en

> 一个高优先级的提示，用于生成一张逼真的时尚编辑肖像，描绘一位女性手持红色口红，站在一面复古金色边框镜子前。关键特征是镜子上用口红写着“Happy International Bagel Day”字样，将俏皮的信息与感性、自信的美学融为一体。

![时尚大片：口红留言的镜中自拍](https://cms-assets.youmind.com/media/1768544846329_4nsgj0_G-uNNKObQAMywqv.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_fashion_editorial_mirror_message",
      "version": "v1.0_INTERNATIONAL_BAGEL_DAY_MIRROR_LIPSTICK",
      "priority": "highest"
    },

    "output_settings": {
      "aspect_ratio": "3:4",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "luxury_fashion_editorial",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_film",
      "color_grade": "warm_golden_sunset",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_glow"
    },

    "creative_prompt": {
      "scene_summary": "A photorealistic high-fashion editorial portrait of a woman standing in front of a vintage gold-framed mirror, holding a red lipstick. On the mirror, written clearly in red lipstick handwriting, is the phrase: '{argument name="mirror text" default="Happy International Bagel Day"}', accompanied by a subtle lipstick kiss mark.",
      
      "subject": {
        "appearance": {
          "hair": "wet, softly wavy hair, slightly tousled",
          "makeup": "glossy red lips, luminous skin, natural sculpted makeup",
          "accessories": "gold hoop earrings",
          "outfit": "elegant red satin slip dress"
        },
        "expression": "confident, sensual, calm gaze slightly off-camera"
      },

      "environment": {
        "location": "sunlit interior",
        "background": "soft blurred background with warm daylight reflections",
        "mirror": "ornate vintage gold frame, clean reflective surface"
      },

      "text_on_mirror": {
        "exact_text": "Happy International Bagel Day",
        "style": "handwritten lipstick text",
        "color": "classic lipstick red",
        "placement": "upper right area of the mirror, clearly legible",
        "additional_element": "small lipstick kiss mark near the text"
      },

      "lighting": {
        "key_light": "warm natural sunlight from the side",
        "highlights": "soft glow on skin and lips",
        "shadows": "gentle and cinematic"
      },

      "mood": [
        "playful",
        "sensual",
        "editorial",
        "celebratory",
        "confident"
      ]
    },

    "negative_prompt": [
      "cartoon",
      "illustration",
      "blurry text",
      "misspelled words",
      "extra text",
      "logos",
      "watermark",
      "harsh flash lighting",
      "overexposed skin",
      "cheap makeup look"
    ]
  }
}
```

[[Fashion Editorial]]

---

### 168. 电影级冬季时尚提示（Sophie Rain 形象）

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-01-10  **Language**: en

> 一个详细的 JSON 提示，用于生成一张受 Sophie Rain 启发的电影级特写时尚照片，照片中人物在采尔马特（Zermatt）一家豪华酒店外的夜晚大雪中摆出动感的芭蕾舞姿，强调单色红白乳胶/羽绒服服装，以及高细节纹理。

![电影级冬季时尚提示（Sophie Rain 形象）](https://cms-assets.youmind.com/media/1768143858041_2m8415_G-UoVw7WoAAWHvV.jpg)

```
{
  "image_generation_request": {
    "aspect_ratio": "3:4",
    "style": "Cinematic Close-up Fashion Photography",
    "quality": "8K / Ultra-High Detail",
    "subject": {
      "identity": "Young adult woman, {argument name="subject likeness" default="Sophie Rain"}-inspired likeness",
      "pose": {
        "description": "Dynamic balletic stance, spontaneous and joyful",
        "position": "Balancing on one leg, other leg bent and lifted high, body slightly tilted",
        "arms": "One arm raised catching snowflakes with open palm, other arm following the flow of movement"
      },
      "expression": {
        "mood": "Genuinely happy and lively",
        "features": "Wide natural smile, slightly parted lips, eyes sparkling with emotion, cheeks flushed from cold"
      },
      "physical_details": {
        "skin": "Realistic texture, fine pores, subtle asymmetry, soft highlights, no plastic smoothing",
        "hair": "Long blonde hair flowing from beanie, damp strands clinging to cheeks/forehead from melting snow"
      }
    },
    "apparel": {
      "theme": "Monochrome Red-white winter look",
      "layers": [
        {
          "item": "Oversized open puffer jacket",
          "details": "Thick creamy-white, fluffy texture, visible stitching, realistic down volume and compression folds"
        },
        {
          "item": "Cropped hoodie",
          "details": "Glossy red latex with V deep cleavage making visible her big bust, gentle wrinkles, worn underneath jacket"
        },
        {
          "item": "High-waisted red latex leggings,
          "details": "Glossy stretch fabric, cremisi-red, subtle tension at knees and hips"
        }
      ],
      "accessories": [
        {
          "item": "Knit beanie",
          "details": "Extra-fluffy, visible yarn texture, red"
        },
        {
          "item": "Mittens",
          "details": "Long creamy-white fluffy fibers, catching falling snowflakes"
        }
      ],
      "footwear": {
        "style": "Pink Moon-boot inspired lace-up winter boots",
        "details": "White fur-lined, realistic rubber soles, snow buildup around the edges"
      }
    },
    "environment": {
      "setting": "Nighttime exterior of a modern luxury building hotel in {argument name="location" default="zermatt"}",
      "architecture": "Sharp geometric wood with triangular patterns",
      "props": "Luxury green lime Lamborghini Urus SUV with red alloy wheels parked nearby, partially covered in frost and snow",
      "ground": "Thick uneven snow blanket with visible footprints and compression points",
      "weather": "Heavy dense snowfall, large snowflakes frozen in mid-motion with slight blur"
    },
    "lighting_and_atmosphere": {
      "primary_lighting": "Cold blue-white ambient winter light",
      "secondary_lighting": "Warm orange glow from building interior/windows",
      "visual_effects": [
        "Cinematic color separation",
        "Soft bokeh highlights in background",
      ]
```

[[Fashion Editorial]]

---

### 169. 赛博朋克电影风格人像，搭配霓虹灯光分割效果

**Author**: [A.D.BARRY](https://x.com/aiwithadb)  **Date**: 2026-01-10  **Language**: en

> 一个结构化的 JSON 提示词，用于生成赛博朋克风格的高对比度电影级影棚肖像，强调面部锐利对焦、可见的皮肤纹理，以及使用青色/蓝色和红色/洋红色霓虹色调在纯黑色背景下营造的戏剧性分割布光。此提示词专为专业、高冲击力的编辑视觉效果而设计。

![赛博朋克电影风格人像，搭配霓虹灯光分割效果](https://cms-assets.youmind.com/media/1768143873000_5avjlc_G-UeEtaXAAASbBY.jpg)
![赛博朋克电影风格人像，搭配霓虹灯光分割效果](https://cms-assets.youmind.com/media/1768143873553_kqlc2v_G-UeEtnWEAAOeHG.jpg)

```
{
"image_type": "studio portrait",
"composition": {
"framing": "tight head-and-shoulders close-up",
"camera_angle": "eye-level",
"orientation": "vertical",
"symmetry": "near-perfect central symmetry",
"focus": "sharp focus on eyes and facial features",
"depth_of_field": "shallow, background fully blurred to black"
},
"subject": {
"pose": "frontal, facing camera directly",
"expression": "calm, confident, intense gaze",
"eye_direction": "looking straight into lens",
"facial_features": {
"skin_texture": "visible pores and fine lines, realistic skin detail",
"eyes": "light-colored eyes emphasized by catchlights"
},
"hair": {
"style": "medium-length, brushed back",
"texture": "natural, slightly tousled",
"color": "dark brown with subtle gray highlights"
}
},
"wardrobe": {
"top": "white crew-neck t-shirt",
"outerwear": "dark jacket or coat with soft texture",
"accessories": "thin chain necklace partially visible"
},
"lighting": {
"style": "cinematic, high-contrast neon lighting",
"key_light": {
"position": "front-left",
"color": "{argument name="key light color" default="cool cyan/blue"}",
"effect": "dominant illumination across face and torso"
},
"rim_light": {
"position": "rear-right",
"color": "{argument name="rim light color" default="saturated red/magenta"}",
"effect": "strong edge highlight on hair and face contour"
},
"fill_light": "minimal to none",
"contrast_level": "high",
"mood": "dramatic, futuristic, intense"
},
"color_palette": {
"dominant_colors": ["cyan blue", "deep red", "black"],
"color_temperature": "mixed cool and warm neon tones",
"saturation": "high saturation on lighting, neutral clothing tones",
"color_grading": "stylized cyberpunk-inspired grading"
},
"background": {
"environment": "studio",
"details": "pure black background with no visible texture or objects",
"separation": "strong subject-background separation via rim lighting"
},
"technical_details": {
"camera_style": "professional studio photography",
"lens_effect": "slight compression typical of portrait lens",
"estimated_focal_length": "85mm equivalent",
"image_sharpness": "high",
"noise": "minimal",
"dynamic_range": "controlled highlights with deep shadows"
},
"artistic_style": {
"genre": "cinematic portrait",
"influences": ["cyberpunk", "neo-noir", "editorial fashion"],
"visual_aesthetic": "bold, modern, high-impact",
"post_processing": {
"skin_retouching": "subtle, realistic",
"color_enhancement": "strong split-toning blue/red",
"clarity": "enhanced micro-contrast"
}
},
"overall_impression": {
"tone": "powerful and enigmatic",
"intended_use": "editorial, album cover, cinematic poster, AI style reference",
"style_recreation_keywords": [
"cinematic neon portrait",
"blue and red split lighting",
"black background",
"intense direct gaze",
"cyberpunk color grading",
"high-contrast studio lighting"
]
}
}
```

[[Fashion Editorial]] [[Black Background]]

---

### 170. 纽约《Vogue》杂志时尚大片拍摄

**Author**: [Willy](https://x.com/jw660227)  **Date**: 2026-01-10  **Language**: en

> 一个高度详细的提示，指定了相机设备（哈苏、85 毫米镜头）、场景（纽约市人行横道，黄金时段）和拍摄对象（身着奢华时装的欧亚女性和西方男性）。该提示侧重于超现实主义、面料纹理、电影级色彩分级（青色和橙色）以及动态行走姿势，旨在营造高端时尚大片的美感。

![纽约《Vogue》杂志时尚大片拍摄](https://cms-assets.youmind.com/media/1768143875943_noryee_G-TCdVqasAMMvMh.jpg)

```
Shot on Hasselblad medium format camera, 85mm lens, f/2.8 aperture, ultra-realistic full body side profile shot of a stunning young woman in her early 20s Eurasian beauty with perfect symmetrical facial features, flawless glowing skin, sharp defined jawline, high cheekbones, large expressive almond-shaped hazel eyes with dramatic long thick eyelashes and perfect winged eyeliner, perfectly shaped arched eyebrows, full glossy nude-pink lips, subtle rosy natural blush, long flowing wavy auburn hair styled cascading over her shoulders, walking confidently across a busy New York City crosswalk, arm in arm with a handsome, impeccably dressed man, looking at each other with loving eyes; the man in his early 30s, Western European features, chiseled face, dark hair neatly styled, wearing a tailored dark grey suit, crisp white shirt, elegant black overcoat, and polished leather shoes; yellow taxi cabs blurred in motion behind them, towering glass skyscrapers and luxury brand storefronts in background, pedestrians in business attire walking in distance, steam rising from subway grate, autumn leaves scattered on pavement. She is wearing a luxurious oversized structured {argument name="coat color" default="camel"} Burberry wool coat with wide lapels, underneath a crisp white high-collar silk blouse with pussy bow detail, paired with tailored high-waisted charcoal gray wide-leg Gucci trousers, classic black patent leather Manolo Blahnik pointed-toe stiletto heels with red soles. Accessories include a large structured black Hermes Birkin bag in one hand, oversized black Chanel cat-eye sunglasses with gold CC logo on temples, elegant wide-brimmed black felt fedora hat tilted slightly, delicate gold Cartier love bracelet, diamond stud earrings, thin gold watch peeking from sleeve. Side angle full body shot taken from street level, dynamic walking pose with coat flowing slightly from movement, one heel lifted mid-step, confident powerful posture, Anna Wintour protégé vibes; golden hour morning light casting long shadows, cinematic color grading with slight teal and orange tones, shallow depth of field with sharp focus on subjects and soft bokeh on background traffic, photorealistic 8K resolution, highly detailed fabric textures showing cashmere weave and leather grain, editorial Vogue magazine fashion photography style, busy metropolitan atmosphere, high-end luxury fashion campaign aesthetic.. A stylish handwritten signature Willy is elegantly and small letters placed at the Bottom Right corner.
```

[[Fashion Editorial]] [[85mm Lens]] [[Luxury Fashion]] [[Hasselblad Camera]]

---

### 171. 单色橙色高级时装编辑提示

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-01-10  **Language**: en

> 一个结构化的 JSON 提示，用于生成一张受 Sydney Sweeney 启发、超逼真的高级时装编辑图片，其特色是单色橙色美学，包括羽毛连衣裙、配套的细高跟鞋和纯橙色影棚背景，并详细说明了多种姿势和相机设置。

![单色橙色高级时装编辑提示](https://cms-assets.youmind.com/media/1768143870080_2mx9rq_G-SLJd-W0AAz8zY.jpg)

```
{
  "project_meta": {
    "title": "Monochromatic Orange High-Fashion Editorial",
    "style": "Ultra-photorealistic, 8K, luxury magazine aesthetic",
    "mood": "Bold, glamorous, confident, seductive"
  },
  "environment": {
    "setting": "Minimalist professional studio",
    "background": "Solid seamless vibrant {argument name="color" default="orange"} backdrop and floor",
    "props": "None (clean surface)",
    "lighting": "Soft frontal key light, warm calibration, controlled shadows"
  },
  "subject": {
    "likeness": "{argument name="celebrity likeness" default="Sydney Sweeney"}-inspired (not identical)",
    "demographics": "Female, mid-20s, slim toned physique",
    "features": {
      "skin": "Natural white, glossy bronzed highlights, realistic texture",
      "hair": "Long light blonde, voluminous, side-parted",
      "face": "Soft oval, full lips, bright expressive eyes",
      "makeup": "High-glam, sculpted contour, smoky eyes, glossy nude lips"
    }
  },
  "wardrobe": {
    "dress": "Strapless mini dress, dense soft orange feather texture",
    "shoes": "Matching orange pointed-toe stilettos",
    "jewelry": "Gold hoop earrings, thin chain, stacked bangles, rings"
  },
  "technical": {
    "gear": "Full-frame DSLR, 85mm prime lens",
    "settings": "Aperture f/4, ISO 100, Shutter 1/125s",
    "focus": "Tack-sharp on subject, subtle background separation"
  },
  "composition": {
    "angles": "Eye-level to subtle low-angle",
    "framing": ["Full-body", "Three-quarter", "Tight portrait"],
    "poses": [
      "Kneeling with legs folded",
      "Seated with one knee raised",
      "Standing with hip pop",
      "Leaning back supported by hands",
      "Looking over shoulder"
    ]
  },
  "consistency_rules": {
    "fixed_elements": ["Character identity", "Feather dress", "Orange background"],
    "variable_elements": ["Pose", "Camera angle", "Framing"]
  }
}
```

[[Fashion Editorial]] [[Celebrity Inspired Portrait]] [[Orange Studio Background]]

---

### 172. Vogue 风格红色羽绒服肖像提示

**Author**: [Aijaz](https://x.com/iamsofiaijaz)  **Date**: 2026-01-10  **Language**: en

> 这是一个为 Nano Banana Pro 设计的电影级时尚肖像提示，用于生成一张超现实的女性图像，她身穿大胆的红色羽绒服，戴着橙色墨镜，采用 85mm 镜头美学、低角度拍摄，并利用温暖的黄金时段阳光，打造出《Vogue》杂志般的时尚大片效果。

![Vogue 风格红色羽绒服肖像提示](https://cms-assets.youmind.com/media/1768143915686_uup0d4_G-RvL5fasAQYF49.jpg)

```
A cinematic fashion portrait of a young woman with a short wavy bob haircut and wispy bangs, wearing round orange-tinted sunglasses, pearl drop earrings, a black turtleneck and a bold red puffer jacket, soft glossy lips, natural makeup, wind gently moving her hair, photographed from a low angle, shallow depth of field, ultra realistic, 85mm lens, f1.8, warm golden hour sunlight, clean blue sky background, editorial fashion photography, high detail skin texture, soft shadows, cinematic color grading, Vogue style, ultra sharp focus, professional studio quality
```

[[Fashion Editorial]] [[Low Angle Shot]] [[85mm Lens Aesthetic]] [[Golden Hour Sunlight]]

---

### 173. 极简主义高对比度影棚肖像

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-01-07  **Language**: en

> 这是一个为 Nano Banana Pro 设计的提示，旨在生成一张高对比度、现代时尚的编辑肖像。画面中，一名匿名男子戴着黑色无边帽、太阳镜和口罩，置身于纯色鲜黄色背景前，利用戏剧性的定向照明营造出超锐利的焦点。

![极简主义高对比度影棚肖像](https://cms-assets.youmind.com/media/1767966087807_niwb7v_G-FBFDpaYAAUn79.jpg)

```
A minimalist studio portrait of a man standing front-facing against a solid vibrant yellow background. He is wearing a black beanie, matte black sunglasses, and a black face mask covering his nose and mouth, creating a mysterious anonymous look. He has on a black padded winter jacket zipped up fully. The lighting is dramatic and directional, with strong contrast and soft shadows, emphasizing texture in the jacket and clean facial contours. Ultra-sharp focus, high contrast, modern fashion editorial style, cinematic lighting, symmetrical composition, professional studio photography, 4K realism.
```

[[Fashion Editorial]]

---

### 174. 超豪华时尚社论肖像

**Author**: [Creator Backstage](https://x.com/CBackstageAI)  **Date**: 2026-01-06  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超豪华、高级时装的女性肖像编辑照片，她坐在一座白色大理石壁炉架上。提示中指定了高对比度的电影级灯光、设计师服饰（蕾丝紧身胸衣、皮草大衣、 monogram 连裤袜）和优雅的巴黎室内环境，旨在达到《Vogue》杂志的品质。

![超豪华时尚社论肖像](https://cms-assets.youmind.com/media/1767804103093_u6q20g_G99luCcWAAA8LRe.jpg)

```
{
  "prompt": {
    "style": "ultra-luxury fashion editorial portrait",
    "shot_type": "full-body",
    "subject": {
      "gender": "female",
      "appearance": {
        "pose": "sitting confidently on a white marble fireplace mantel",
        "legs": "crossed elegantly",
        "expression": "powerful and confident",
        "hair": {
          "length": "long",
          "texture": "straight and silky",
          "color": "light brown",
          "part": "center",
          "styling": "perfectly styled"
        },
        "accessories": {
          "sunglasses": "oversized black sunglasses",
          "handbag": "small vintage-style designer monogram handbag"
        },
        "makeup": {
          "style": "bold nude makeup",
          "contour": "sharp contour",
          "lips": "glossy"
        }
      },
      "outfit": {
        "top": "black lace corset bodysuit with deep neckline",
        "tights": "sheer designer monogram tights",
        "shoes": "black pointed high heels",
        "outerwear": "{argument name="coat color" default="rich brown"} faux-fur coat draped loosely over shoulders"
      }
    },
    "environment": {
      "location": "elegant Parisian-style interior",
      "background_elements": [
        "classic white wall panels",
        "gold-framed mirror",
        "champagne bottles on the mantel"
      ],
      "vibe": "luxury and high fashion"
    },
    "photography": {
      "lighting": "cinematic soft lighting",
      "contrast": "high contrast",
      "focus": "sharp focus",
      "depth_of_field": "shallow",
      "quality": "fashion magazine quality",
      "style_reference": "Vogue editorial",
      "realism": "ultra-realistic",
      "resolution": "4K"
    },
    "aesthetic": [
      "premium luxury aesthetic",
      "Instagram model photography",
      "clean composition"
    ],
    "constraints": {
      "text": "none",
      "watermark": "none"
    }
  }
}
```

[[Fashion Editorial]] [[Fur Coat]]

---

### 175. 3x3 编辑网格，带粉色心形气球和身份锁

**Author**: [Özge](https://x.com/astroozge)  **Date**: 2026-01-05  **Language**: en

> 一个复杂的提示，旨在生成一个由社论肖像组成的 3x3 网格拼贴画。它要求严格保留参考图像中的身份，并强制所有九个画面的服装、背景和光线保持一致，唯一的区别是主体摆出的姿势以及与粉色心形气球的互动。

![3x3 编辑网格，带粉色心形气球和身份锁](https://cms-assets.youmind.com/media/1767682119568_7n90pr_G97LEKkWwAAlL6C.jpg)

```
{
  "request_metadata": {
    "model": "Nano Banana Pro",
    "content_type": "photoreal_editorial_pink_heart_balloon_3x3_grid",
    "quality_preset": "ultra",
    "format_aspect_ratio": "1:1",
    "output": "3x3_grid"
  },
  "references": {
    "reference_images": {
      "female_reference": "UPLOAD_FEMALE_REFERENCE_IMAGE (REQUIRED)"
    },
    "reference_rules": {
      "exactly_one_reference_only": true,
      "preserve_identity_female": true,
      "identity_lock_strength_female": 0.995,
      "face_similarity_priority": "MAX",
      "preserve_facial_proportions": true,
      "preserve_eye_shape_nose_lips_jawline": true,
      "no_identity_blending": true,
      "no_beautify_no_face_morph": true
    }
  },
  "layout": {
    "type": "3x3_grid",
    "description": "Same woman in all 9 frames. Same outfit, same background, same lighting, same lens/grade. Only pose, hand placement, and gaze change per frame.",
    "grid_style": {
      "borders": "thin white separators",
      "consistency_rule": "identical color grading and softness across all frames"
    },
    "frame_labels": [
      "1) Balloon hugged at chest, shy gaze",
      "2) Balloon angled near shoulder, soft smile",
      "3) Balloon raised overhead, playful look",
      "4) Balloon close to face, dreamy gaze",
      "5) Balloon centered at chest, classic editorial",
      "6) Balloon overhead, confident stance",
      "7) Balloon cradled low, eyes closed",
      "8) Balloon above head, hair touch",
      "9) Balloon overhead, profile glance"
    ]
  },
  "global_scene": {
    "environment": {
      "background": "plain warm off-white studio wall, smooth texture, no props, no text"
    },
    "lighting": {
      "type": "soft studio light",
      "setup": "large diffused key + gentle fill",
      "quality": "low contrast, flattering highlights, no harsh shadows"
    },
    "style": {
      "look": "clean editorial",
      "diffusion": "very subtle soft haze",
      "grain": "very subtle film grain",
      "retouching": "minimal; keep natural skin texture"
    },
    "camera": {
      "lens": "50mm editorial portrait feel",
      "aperture": "f/2.8 feel",
      "sharpness": "crisp subject with soft diffusion"
    },
    "consistency_locks": {
      "same_outfit": true,
      "same_background": true,
      "same_lighting": true,
      "same_color_grade": true
    }
  },
  "subject_profile": {
    "gender": "female",
    "age_group": "young_adult",
    "identity": "EXACT same face as the reference (no drift)",
    "hair": {
      "style": "long, soft waves",
      "color": "soft blonde / golden blonde, consistent across all frames (do not change face identity)"
    },
    "makeup": {
      "style": "soft glam",
      "skin": "natural texture",
      "lips": "soft rose-pink satin",
      "eyes": "defined but soft"
    },
    "wardrobe": {
      "dress": "{argument name="dress color" default="pink"} satin slip dress/top, elegant and fully opaque, thin straps, subtle sheen (satin refle"
    }
  }
}
```

[[Fashion Editorial]] [[Studio Portrait]] [[Identity Consistency]]

---

### 176. 摩天大楼屋顶边缘上的高角度时尚大片

**Author**: [Bananai](https://x.com/aibananai)  **Date**: 2026-01-05  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超逼真的时尚社论图片，描绘一名女性躺在摩天大楼屋顶狭窄的混凝土边缘上。它指定了高角度、陡峭的向下倾斜视角、高对比度的自然日光，以及她服装的详细描述（超大羊毛大衣、皮裙、猫眼太阳镜），以营造一个大胆、令人眩晕的都市场景。

![摩天大楼屋顶边缘上的高角度时尚大片](https://cms-assets.youmind.com/media/1767682176483_o1azra_G95wBLIWwAA98bD.jpg)
![摩天大楼屋顶边缘上的高角度时尚大片](https://cms-assets.youmind.com/media/1767682177492_dvq63j_G95wBJ9W4AAXhmj.jpg)

```
{
  "meta": {
    "aspect_ratio": "4:5",
    "quality": "ultra_photorealistic",
    "resolution": "8k",
    "camera": "DSLR camera",
    "lens": "24mm wide-angle",
    "style": "high-end editorial fashion photography, cinematic urban realism, natural daylight"
  },
  "scene": {
    "location": "skyscraper rooftop ledge",
    "environment": [
      "concrete building ledge with expansion joints",
      "glass facade of adjacent skyscraper reflecting city",
      "dizzying vertical drop to city street below",
      "traffic and cars visible on multi-lane road",
      "dense urban landscape with various buildings",
      "clear daylight sky"
    ],
    "time": "day",
    "atmosphere": "daring, stylish, vertiginous, high-altitude urban energy"
  },
  "lighting": {
    "type": "natural daylight",
    "key_light": "bright sun from upper left",
    "fill_light": "ambient light reflecting off buildings",
    "contrast": "high contrast between bright ledge and deep shadows of the street below",
    "effect": "sharp shadows, realistic highlights on leather and wool textures"
  },
  "camera_perspective": {
    "pov": "high-angle shot, looking down",
    "angle": "steep downward tilt",
    "framing": "full body of subject on ledge, expansive view of street below",
    "distance": "medium distance",
    "focus": "sharp focus on subject, deep depth of field showing city details"
  },
  "subject": {
    "gender": "female",
    "age": "late 20s / early 30s",
    "ethnicity": "mixed race / Black",
    "body": {
      "pose": "lying on back on narrow concrete ledge, head tilted back, one leg straight, one slightly bent",
      "posture": "relaxed yet controlled, confident",
      "expression": "calm, confident gaze upwards, protected by sunglasses"
    },
    "hair": {
      "color": "dark brown / black",
      "style": "voluminous curly high bun (pineapple updo)",
      "texture": "natural curls"
    },
    "face": {
      "accessories": {
        "sunglasses": "oversized tortoiseshell cat-eye sunglasses",
        "earrings": "small gold hoop earrings"
      }
    },
    "outfit": {
      "coat": {
        "type": "long oversized wool coat",
        "color": "{argument name="coat color" default="brown / taupe"}",
        "texture": "heavy wool fabric, realistic folds and drape"
      },
      "dress": {
        "type": "strapless midi dress",
        "color": "beige / nude",
        "material": "soft leather or faux leather",
        "fit": "fitted",
        "details": "visible seam lines, slight creases"
      },
      "gloves": {
        "type": "short leather gloves",
        "color": "black",
        "material": "smooth leather"
      },
      "boots": {
        "type": "heeled ankle boots",
        "color": "black",
        "material": "leather",
        "style": "pointed toe"
      },
      "bag": {
        "type": "quilted leather shoulder bag with chain strap (Chanel style)",
        "color": "black",
        "placement": "resting "
      }
    }
  }
}
```

[[Fashion Editorial]] [[Natural Daylight]] [[High Angle Shot]] [[Rooftop Setting]]

---

### 177. 乡村奢华时尚大片，搭配 YSL 手袋

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-01-05  **Language**: en

> 一个 JSON 提示，用于生成一张超高分辨率的时尚图片，图中一位优雅的女士身穿黑色露背连体衣和飘逸的白色缎面长裙，坐在一张柳条椅上，置身于质朴的地中海石砌庭院中。图片指定了黄金时段的光线，并突出展示了一个黑色绗缝 Saint Laurent 手袋作为道具。

![乡村奢华时尚大片，搭配 YSL 手袋](https://cms-assets.youmind.com/media/1767682185595_u1d62e_G95uKYfWAAA896r.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Elegant young woman sitting relaxed in a wicker chair",
      "hair": "Long wavy honey blonde hair with highlights",
      "attire": "Black halter-neck bodysuit with keyhole cutout, floor-length flowing {argument name="skirt color" default="white"} satin skirt, black strappy high heels",
      "accessories": "Gold hoop earrings, rings"
    },
    "props": {
      "main_item": "Black quilted Saint Laurent (YSL) handbag with gold logo placed on the stone floor"
    },
    "environment": {
      "setting": "Rustic Mediterranean stone courtyard",
      "background": "Textured stone wall, wooden beam, potted lush green plants with purple flowers",
      "flooring": "Natural stone pavement"
    },
    "lighting": {
      "type": "Golden hour, warm natural sunlight",
      "shadows": "Soft sun-drenched shadows"
    },
    "technical_specs": {
      "resolution": "Ultra-high resolution, 12K image",
      "quality_tags": "Highly detailed, realistic, photorealistic, sharp focus, 8k textures",
      "file_type": "PNG format",
      "camera_style": "Editorial fashion photography, cinematic composition, depth of field"
    }
  }
}
```

[[Fashion Editorial]] [[Golden Hour Light]]

---

### 178. 电影级奢华社论肖像：石阶之上

**Author**: [Hoor](https://x.com/hoor_world06)  **Date**: 2026-01-05  **Language**: en

> 一个简洁的提示，用于生成一张电影般的奢华时尚肖像，描绘一位女士优雅地站立在历史悠久的石阶上。重点在于服饰（结构化的丝绸缎面礼服）和环境（拥有自然光线的历史建筑内部）。

![电影级奢华社论肖像：石阶之上](https://cms-assets.youmind.com/media/1767682102586_fycln8_G95XwvVXEAA3wMT.jpg)

```
{
  "render_goal": "Cinematic luxury editorial portrait",
  "subject": {
    "pose": "female standing mid-staircase, relaxed elegant posture",
    "expression": "composed confidence with a soft smile"
  },
  "wardrobe": "structured silk satin gown in {argument name="gown color" default="warm ivory"}, clean neckline, subtle drape",
  "environment": {
    "location": "historic interior with a wide stone staircase",
    "props": "natural light from tall windows, soft shadow fall"
  }
}
```

[[Fashion Editorial]]

---

### 179. 黑白男性编辑肖像拼贴 JSON 提示

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2026-01-05  **Language**: en

> 一个详细的 JSON 提示，用于生成一个 3x3 网格拼贴画，内容是男性对象的黑白工作室肖像，重点在于多样的表情和姿势（如假笑、指点和假装痛苦），同时保持一致的风格、高对比度和时尚/编辑美学。

![黑白男性编辑肖像拼贴 JSON 提示](https://cms-assets.youmind.com/media/1767682190496_6z7jfq_G93wZj1aIAAnLdr.jpg)

```
{
"image_type": "studio portrait collage",
"layout": {
"structure": "3x3 grid",
"aspect ratio": "2:3",
"orientation": "vertical",
"spacing": "even margins between frames",
"consistency": "same subject and styling across all frames"
},
"subject": {
"count": 1,
"gender_presentation": "male",
"age_range": "late 20s to early 30s",
"ethnicity": "unclear / ambiguous",
"build": "athletic, lean",
"hair": {
"color": "dark brown",
"style": "short sides with voluminous swept-back top",
"texture": "smooth with natural wave"
},
"facial_hair": {
"type": "light stubble",
"density": "low to medium"
},
"wardrobe": {
"top": "long-sleeve knit sweater",
"color": "black",
"fit": "slim fit",
"texture": "fine ribbed or waffle knit"
}
},
"expressions_and_poses": [
"smirking with hand on chin",
"pulling sweater collar to mouth",
"thoughtful side gaze with hand near lips",
"animated mid-gesture with expressive hands",
"boxing/fist-forward dynamic pose",
"finger-to-lips 'shh' gesture",
"direct gaze with pointing finger",
"mock pain or exaggerated discomfort expression",
"head resting on hand, fatigued or bored"
],
"composition": {
"framing": "medium close-up to medium shot",
"camera_angle": "eye-level",
"cropping": "consistent head-and-torso framing",
"negative_space": "minimal, subject-centered"
},
"lighting": {
"style": "studio",
"setup": "single key light with soft fill",
"direction": "front-left dominant",
"contrast": "medium to high",
"shadow_quality": "soft-edged shadows with sculpted facial definition"
},
"color_and_tone": {
"palette": "monochrome",
"treatment": "black and white",
"contrast": "high contrast",
"midtones": "well-preserved skin detail",
"highlights": "controlled, non-blown"
},
"background": {
"type": "seamless studio backdrop",
"color": "dark gray to near-black",
"texture": "smooth, matte",
"distractions": "none"
},
"technical_details": {
"lens_equivalent": "50mm–85mm portrait range",
"depth_of_field": "moderate, subject fully in focus",
"sharpness": "high",
"grain": "minimal to none",
"resolution": "high-resolution editorial quality"
},
"artistic_style": {
"genre": "fashion/editorial portraiture",
"mood": "confident, playful, expressive",
"influences": "modern menswear editorial, actor portfolio photography",
"storytelling": "personality exploration through varied expressions"
},
"post_processing": {
"skin_retouching": "natural, minimal",
"contrast_curve": "strong S-curve",
"clarity": "moderate",
"vignette": "subtle or none"
},
"typography": {
"present": false
},
"overall_aesthetic": "clean, masculine, contemporary studio portrait series optimized for branding, modeling, or editorial use"
}
```

[[Fashion Editorial]] [[Studio Portrait]] [[High Contrast Monochrome]] [[Expression Variation]]

---

### 180. Jil Sander 美学时尚大片：人与马

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-05  **Language**: en

> 生成一张干净、极简的时尚大片图像的提示词，画面中一位男模特和一匹棕色马在冰岛的河流附近。要求采用俯视视角（哈苏 85mm 镜头），柔和的对比度，自然的皮肤纹理，以及 Jil Sander 品牌那种宁静的户外美学。

![Jil Sander 美学时尚大片：人与马](https://cms-assets.youmind.com/media/1767682228422_y2drdr_G93l0ENb0AA7iI_.jpg)

```
High angle shot looking down at the male model and brown horse from above, revealing the full scene composition near the Icelandic river. The model stands relaxed in baggy cream trousers, white sweater, and brown leather boots, positioned thoughtfully relative to the horse drinking water. The riverbank, stones, and moss create a natural pattern beneath them. Clean, minimalistic fashion editorial framing with balanced negative space, air-brushed soft rendering, muted contrast, natural skin texture preserved, slightly enhanced green tones in landscape, soft natural overcast light. Hasselblad 85mm overhead perspective, vertical 9:16, Jil Sander serene outdoor aesthetic.
```

[[Fashion Editorial]] [[Natural Skin Texture]]

---

### 181. 折射式高级时装社论肖像

**Author**: [zayan](https://x.com/HustleXR)  **Date**: 2026-01-04  **Language**: en

> 一个用于生成高端时尚社论肖像的提示，该肖像利用实验性光学效果，特别是通过棱镜玻璃和水晶元素进行拍摄。目标是在华丽、低调而富有戏剧性的宴会厅氛围中，呈现柔和、梦幻的焦点，并带有强烈的彩虹色散和分层玻璃效果。

![折射式高级时装社论肖像](https://cms-assets.youmind.com/media/1767607023755_ur7ii9_G9ys-IDaQAA5ZWL.jpg)

```
"Refractive photography",
    "Fine art portrait"
  ],
  "photography_style": {
    "genre": "High-end fashion editorial portrait with experimental optical effects",
    "technique": "Shooting through prismatic glass and crystal elements for artistic refraction",
    "era": "Contemporary 2020s luxury fashion photography",
    "influences": "Paolo Roversi soft focus, Tim Walker whimsical elegance, Sofia Coppola period opulence"
  },
  "critical_elements_summary": {
    "must_include": [
      "Large crystal prism creating rainbow dispersion on entire left side of frame",
      "Subject visible through transparent glass table in center creating layered effect",
      "Flower arrangement right side with chromatic aberration on petals",
      "Multiple crystal chandeliers with warm candlelight creating bokeh in background",
      "Deep black background with selective lighting on subject",
      "Elaborate diamond necklace and earrings catching light",
      "Soft dreamy focus quality throughout",
      "Strong rainbow spectrum colors from prismatic refraction - full red through violet",
      "Transparent layered glass effects creating ghosting and doubling",
      "Warm amber candlelight bokeh circles scattered in background",
      "Low-key dramatic lighting with subject emerging from darkness",
      "Opulent formal ballroom atmosphere"
    ]
  }
}
```

[[Fashion Editorial]]

---

### 182. 全息 2026 取景器时尚肖像提示（JSON 格式）

**Author**: [BeautyVerse](https://x.com/BeautyVerse_Lab)  **Date**: 2025-12-31  **Language**: en

> 一个为 Nano Banana Pro 设计的高度结构化 JSON 提示，用于图像到图像的生成。它创建了一个时尚编辑肖像，其中主体（基于参考图像）以“取景器”手势握住双手。在这个框架内，一个巨大的、强烈发光的“2026”全息投影出现，将彩色光投射到主体上。背景中有一个大型的、重叠的杂志标题“BeautyVerse”。

![全息 2026 取景器时尚肖像提示（JSON 格式）](https://cms-assets.youmind.com/media/1767456250092_l6kzci_G9d-yQQa4AA5a-s.jpg)

```
{
  "project_title": "BeautyVerse Editorial - Chest-Level Holographic Viewfinder (Large 2026) & Winking Smile",
  "structure": "Single full-frame composition. Professional studio photography. No borders or collage elements.",
  "aspect_ratio": "3:4",
  "aesthetic_theme": {
    "style": "High-fashion magazine cover aesthetic with a touch of playful futuristic glow.",
    "mood": "Confident, playful, energetic, sophisticated",
    "color_grading": "Prism glow effect: A base of clean studio lighting mixed with the strong specific colored light cast by the large holographic element. High-contrast professional fashion retouching.",
    "textures": [
      "High-definition skin pores and fine fabric weave",
      "Intense smooth holographic light refractions on hands and chest",
      "Matte, bold printed magazine ink texture for background text"
    ]
  },
  "framing_and_borders": {
    "type": "None",
    "details": [
      "The image fills the entire frame completely.",
      "Clean, borderless presentation focused from the waist up."
    ]
  },
  "subject_reference": {
    "source": "image_1.png",
    "instruction": "Maintain the subject's features and outfit from image_1.png, but change the facial expression as described in the pose section."
  },
  "composition_details": {
    "main_frame": {
      "type": "Medium Portrait (Waist-Up)",
      "composition_rule": "Central focus on the large glowing element in the hands and the subject's expressive face, backed by prominent background typography.",
      "setting_description": "A high-end, minimalist studio wall serving as the backdrop for the large text.",
      "subject_pose": "The subject is looking directly at the camera, giving a **playful wink with one eye and a broad, warm smile**. She holds both hands at chest level, with her thumbs and index fingers forming a rectangular 'camera viewfinder' gesture centered over her heart area. Floating directly inside this finger-frame, the numbers '{argument name="年份" default="2026"}' appear as a **large, prominent, and intensely vibrant** glowing holographic projection that **significantly fills the space within her fingers**. This large glowing element casts a strong, noticeable soft colored light onto her fingers, palms, and the fabric of her outfit on her chest.",
      "key_element_description": {
        "object": "Large Background Magazine Title",
        "text_content": "{argument name="杂志标题" default="BeautyVerse"}",
        "alignment": "The single block of text is positioned behind the subject's upper body and head. The subject's torso slightly overlaps the lower part of the letters, creating depth.",
        "text_style": "Bold, high-impact, authoritative editorial magazine header typeface (thick, el"
      }
    }
  }
}
```

[[Fashion Editorial]] [[2026 New Year]]

---

### 183. 雪山中的电影感剪辑

**Author**: [Kemal Öztürk](https://x.com/kemalartt)  **Date**: 2025-12-29  **Language**: en

> 生成一张高质量电影级编辑照片的提示词，照片中一名女性坐在晶莹的雪地上，旁边放着一个粉色手提箱。场景设定在紫色和蓝色黄昏天空下的壮丽雪山峰峦之间，强调柔和、寒冷的自然光和广角电影构图。

![雪山中的电影感剪辑](https://cms-assets.youmind.com/media/1767166860497_y8vymk_G9VQocjXQAEJBxG.jpg)
![雪山中的电影感剪辑](https://cms-assets.youmind.com/media/1767166860704_30ddnz_G9VQocjWIAAAXIa.jpg)
![雪山中的电影感剪辑](https://cms-assets.youmind.com/media/1767166861943_qlrbc3_G9VQoceWwAARQKi.jpg)

```
"Use the product and model from the image. A high-quality, cinematic editorial lifestyle photograph featuring a woman seated comfortably in a relaxed pose on a crisp, crystalline snow surface next to a pink minimalist hard-shell suitcase. The woman wears a beige wool coat, a white turtleneck sweater, and black pants. The background showcases sharp snowy mountain peaks under a dramatic purple and blue dusk sky. Soft, cold natural light illuminates the scene, highlighting the texture of the snow and the shadows on the woman's face. 8k resolution, wide-angle cinematic composition."
```

[[Fashion Editorial]] [[Cinematic Photography]] [[Golden Hour]] [[Travel Photography]]

---

### 184. 费尔蒙发夹弯的女性编辑肖像

**Author**: [Abbay](https://x.com/LearnWithAbbay)  **Date**: 2025-12-29  **Language**: en

> 一个详细的图像生成提示，以 JSON 格式构建，旨在创作一幅年轻女性在俯瞰摩纳哥费尔蒙发夹弯的阳台上拍摄的编辑类生活肖像，重点关注特定的时尚、光线和构图细节。

![费尔蒙发夹弯的女性编辑肖像](https://cms-assets.youmind.com/media/1767166969749_w974ez_G8lrEYKbgAAMZ2_.jpg)

```
{
  "subject": {
    "person": "{argument name="person description" default="Young woman, early 20s, Caucasian"}",
    "hair": "Warm blonde hair with loose textured waves and natural volume",
    "pose": "Standing casually with one hip leaned against a railing, shoulders relaxed",
    "expression": "Relaxed, composed, faint smile"
  },
  "outfit": {
    "top": "Ivory off-shoulder cotton blend top with subtle texture",
    "bottoms": "High-rise taupe wide-leg trousers",
    "accessories": "Compact leather shoulder bag, thin gold hoops, simple rings, nude nails"
  },
  "action": {
    "hands": "One hand tucked into trouser pocket; other resting on railing"
  },
  "location": {
    "setting": "Balcony overlooking the Fairmont Hairpin",
    "background": "Hairpin curve, red-and-white curbs, hillside buildings, cloudy afternoon light"
  },
  "typography": {
    "text": "Heineken 0.0 and MONTE-CARLO branding on barriers"
  },
  "lighting": {
    "type": "Natural overcast daylight",
    "quality": "Soft, cinematic, evenly diffused"
  },
  "composition": {
    "style": "Editorial lifestyle portrait, medium framing, deep focus, 4:5 portrait",
    "color_palette": "Cool greys and warm neutrals"
  }
}
```

[[Fashion Editorial]] [[Cinematic Photography]] [[Travel Lifestyle Photography]]

---

### 185. 前卫时尚肖像与幽灵分身

**Author**: [Dr.duet](https://x.com/Sheldon056)  **Date**: 2025-12-29  **Language**: en

> 一个超现实、8K 电影级工作室肖像的提示，描绘了一个人物穿着一件不拘一格的飞行员夹克，背景是赭黄色，独特的艺术元素是一个半透明、动态模糊的幽灵分身，传达出时间扭曲感。

![前卫时尚肖像与幽灵分身](https://cms-assets.youmind.com/media/1767166981123_op2md4_G9ThdBKaMAA-Op9.jpg)

```
An ultra-realistic 8K cinematic studio portrait framed from mid-thigh up, featuring a figure standing confidently against a vibrant {argument name="background color" default="ochre-yellow"} background. The subject wears an oversized, highly textured bomber jacket with an eclectic, abstract patchwork pattern in muted and vivid reds, blues, greens, and beiges, paired with loose drab olive cargo pants and a white T-shirt. Lighting is harsh and frontal, creating crisp shadows an￼ emphasizing fabric textures.
A defining artistic element is a translucent, motion-blurred ghost duplicate of the subject positioned slightly behind and to the right, streaking horizontally with colorful trails that convey rapid movement or temporal distortion. The background remains uniform but subtly graded, adding depth without distraction. Shot in a high-fashion editorial style with sharp focus on the primary figure, shallow depth of field, and precise studio realism, delivering a bold,￼ experimental, avant-garde mood.use the provided image as reference.￼
```

[[Fashion Editorial]] [[Studio Portrait]] [[Cinematic Photography]]

---

### 186. Nano Banana Pro 编辑闪光摄影提示

**Author**: [Bananai](https://x.com/aibananai)  **Date**: 2025-12-28  **Language**: en

> 一个高度详细、复杂的图像生成提示，旨在通过强烈的闪光摄影，创作一张原始、垃圾时尚风格的编辑快照。场景设定在一个拥有粗野主义和现代元素的宽敞公寓内部，聚焦于一位身穿黑色蕾丝紧身衣、正在咬香蕉的女性主体，捕捉一种坦率、未经修饰的夜间派对氛围。此提示详细说明了相机设置、灯光、环境和主体特征，以实现逼真的效果。

![Nano Banana Pro 编辑闪光摄影提示](https://cms-assets.youmind.com/media/1767061694551_qlb9u6_G9Rypavb0AAWOpi.jpg)
![Nano Banana Pro 编辑闪光摄影提示](https://cms-assets.youmind.com/media/1767061694779_z56mp3_G9Rypava0AIRaEb.jpg)

```
{
  "meta": {
    "aspect_ratio": "4:5",
    "quality": "raw_photorealism",
    "resolution": "8k",
    "camera_simulation": "Contax T2",
    "film_stock": "Kodak Portra 800",
    "style": "flash photography, candid snapshot, trashy-chic, raw editorial, unpolished, high-flash intensity"
  },

  "scene": {
    "location": "lofty apartment interior",
    "environment": [
      "raw concrete wall on the left (brutalist texture)",
      "dark wooden flooring",
      "dining area in background with walnut table",
      "grey upholstered dining chairs",
      "multi-colored striped woven rug on the floor (red, blue, beige, green horizontal stripes)"
    ],
    "lighting": {
      "type": "direct on-camera hard flash",
      "shadows": "sharp, defined drop shadow behind the subject on the green chair and wall",
      "vignette": "natural heavy vignetting from point-and-shoot camera",
      "reflections": "flash bounce on the forehead and the banana skin",
      "atmosphere": "nighttime indoor party vibe, harsh but realistic"
    },
    "background_details": {
      "table_objects": [
        "glass reed diffuser bottle",
        "red hardcover book with white text 'Basquiat' on spine"
      ],
      "wall_art": {
        "description": "framed poster on the wall behind the chair",
        "visual": "a yellow graphic shape resembling a helmet or abstract form",
        "text_content": "bold black handwritten text reading '@aibananai' inside the yellow shape",
        "style": "neo-expressionist graffiti style"
      }
    }
  },

  "subject": {
    "gender": "female",
    "ethnicity": "East Asian",
    "age": "approx 20-25 years old",
    "skin": {
      "texture": "realistic pores, slight oiliness on T-zone from flash, no airbrushing, natural skin tone",
      "imperfections": "visible skin grain"
    },
    "hair": {
      "style": "completely wrapped in a thick white terry-cloth bath towel",
      "shape": "high turban wrap, voluminous"
    },
    "face": {
      "expression": "vacant candid stare, mouth slightly open biting a banana",
      "gaze": "looking off-camera to the left",
      "makeup": "minimal, bare-faced aesthetic, faint sheen on cheeks"
    },
    "body": {
      "posture": "slouching deeply in the chair, relaxed",
      "limbs": [
        "right arm relaxed holding banana",
        "left arm bent, hand resting near chest with watch visible",
        "right hand dangling loosely over the chair edge towards the floor",
        "legs bent and crossed, draped high over the left armrest of the chair"
      ]
    },
    "outfit": {
      "main": {
        "item": "black lace bodysuit",
        "material": "sheer floral lace pattern with solid black piping",
        "cut": "halter-neck style with strappy chest details, high-cut leg",
        "fit": "tight against skin"
      },
      "jewelry": {
        "left_wrist": "silver metal link watch (loose fit)",
        "right_wrist": "thin s"
```

[[Fashion Editorial]] [[Flash Photography]]

---

### 187. 编辑生活方式肖像：摩纳哥大奖赛屋顶

**Author**: [Abbay](https://x.com/LearnWithAbbay)  **Date**: 2025-12-28  **Language**: en

> 一个详细的提示，用于生成一张年轻女性的编辑生活方式肖像，她在一个私人屋顶上俯瞰摩纳哥大奖赛赛道，重点是中性大地色调、柔和的日光，以及背景中的特定品牌元素。

![编辑生活方式肖像：摩纳哥大奖赛屋顶](https://cms-assets.youmind.com/media/1767061763343_m49rnl_G8lx42Va8AAHZFb.jpg)

```
{
  "subject": {
    "person": "Young woman, early 20s, Caucasian",
    "hair": "Soft blonde hair, loose waves with natural shine",
    "pose": "Standing casually with shoulders open, gaze off-camera",
    "expression": "Peaceful, confident, subtle smile"
  },
  "outfit": {
    "top": "Beige off-shoulder knit top",
    "bottoms": "High-rise tailored taupe trousers",
    "accessories": "Small leather bag, minimalist jewelry, nude nails"
  },
  "action": {
    "hands": "One hand resting on railing; other by side"
  },
  "location": {
    "setting": "Private rooftop overlooking Monaco Grand Prix circuit",
    "background": "Street circuit, hillside apartments, cloudy afternoon"
  },
  "typography": {
    "text": "{argument name="brand name" default="Heineken 0.0"} visible on safety walls"
  },
  "lighting": {
    "type": "Natural daylight",
    "quality": "Soft, cloud-diffused"
  },
  "composition": {
    "style": "Editorial lifestyle portrait, medium framing, deep depth, 4:5",
    "color_palette": "Neutral earth tones"
  }
}
```

[[Fashion Editorial]] [[Natural Light Photography]] [[Travel Lifestyle Photography]] [[Rooftop Portrait]]

---

### 188. 元旦特辑：雪中的故宫

**Author**: [Adam也叫吉米](https://x.com/Adam38363368936)  **Date**: 2025-12-28  **Language**: zh

> 一个电影级的、超详细的提示，用于生成一张具有传统东方美学风格的图像，画面中一位身着华丽旗袍的女性置身于白雪覆盖的故宫红墙前，并配有特定的灯光和相机设置，以达到顶级时尚杂志的编辑水准。

![元旦特辑：雪中的故宫](https://cms-assets.youmind.com/media/1767061777877_z1v75d_G9RE-E4aoAA2Yjs.jpg)

```
电影级摄影杰作，中景镜头。画面主体为参考图中的女性（需完全保留其面部特征与轮廓）。她身着奢华的{argument name="服装颜色" default="酒红色"}丝绒旗袍，领口有白色皮草饰边，伫立在雪后的故宫红墙前。漫天细雪轻舞。身侧是一枝傲雪红梅和一只写有“{argument name="灯笼文字" default="元旦"}”字样的烫金灯笼。光影效果：温暖的橘色灯光与清冷的暮雪形成对比，雪花边缘带有电影感轮廓光。Phase One 系统拍摄，85mm 焦距，大光圈虚化，顶级时尚大片质感，细节极其精致。
```

[[Fashion Editorial]] [[Winter Scene]] [[Cultural Portrait]]

---

### 189. 超写实时尚社论肖像：夜行

**Author**: [Javeriya ✨](https://x.com/JadoonKhan281)  **Date**: 2025-12-28  **Language**: en

> 为 Gemini Nano Banana Pro 模型设计，一个详细、超现实的提示，用于生成一张女性夜间漫步的高端时尚编辑肖像，重点关注具体的身体特征、服装细节和电影般的灯光效果。

![超写实时尚社论肖像：夜行](https://cms-assets.youmind.com/media/1767061760130_3bezb9_G9RDuNYbsAET13v.jpg)

```
{
  "image_concept": {
    "title": "Editorial Fashion Portrait - Night Walk",
    "style": "Hyper-realistic high-end fashion editorial",
    "pose": "Classic 'follow me' style, looking back over shoulder with a gentle smile, holding hand of person behind camera",
    "subject": {
      "gender": "Female",
      "hair": {
        "color": "{argument name="hair color" default="Blonde"}",
        "style": "Long, voluminous, soft waves",
        "texture": "Natural, visible strands"
      },
      "eyes": {
        "color": "Brown",
        "details": "Curled eyelashes"
      },
      "makeup": {
        "palette": "Soft pink tones",
        "quality": "Flawless, professional"
      },
      "physique": {
        "build": "Naturally curvy, athletic",
        "features": ["Hourglass waist", "Rounded hips", "Full bust", "Sculpted/lifted rear"]
      },
      "skin": "Real human texture with visible natural pores"
    },
    "outfit_and_accessories": {
      "jacket": "Short beige long-sleeved tweed, subtle shiny details, white lining",
      "pants": "Wide-leg washed blue jeans",
      "bag": "Small black LV bag, silver chain strap",
      "jewelry_tech": "Cream-colored smartwatch"
    },
    "environment": {
      "location": "Residential housing complex street",
      "time_of_day": "Night",
      "atmosphere": "Light cold mist",
      "lighting": "Cinematic glow from elegant streetlamps",
      "background_elements": [
        "Aesthetically pleasing lampposts",
        "Iron fences",
        "Walls covered in white flowering plants"
      ]
    },
    "technical_metadata": {
      "resolution": "8K UHD",
      "render_engine_filter": "PixelPotions effect",
      "bokeh": "Low (background clearly visible)",
      "constraints": [
        "No CGI",
        "No 3D render",
        "No animation/cartoon",
        "No distorted anatomy",
        "100% identity preservation"
      ]
    }
  }
}
```

[[Fashion Editorial]] [[Cinematic Photography]] [[Night Portrait]] [[Urban Lifestyle Photography]]

---

### 190. 日落时分女士与经典敞篷车的图像生成提示

**Author**: [Karthik Reddy](https://x.com/mbkartikreddy)  **Date**: 2025-12-28  **Language**: en

> 这是一个图像生成提示，用于比较不同模型（Gemini Nano banana Pro 和 ChatGPT）的输出质量。该提示描述了一张高质量的电影级照片：在黄金时段，一位美丽的年轻女子身穿红色皮夹克，站在一辆银色敞篷车旁，置身于欧洲鹅卵石街道上。

![日落时分女士与经典敞篷车的图像生成提示](https://cms-assets.youmind.com/media/1767061701038_gmt3lx_G9QWJO7bsAAtN1b.jpg)
![日落时分女士与经典敞篷车的图像生成提示](https://cms-assets.youmind.com/media/1767061701383_uxreul_G9QWJQObgAEGiOY.jpg)

```
A high-quality, full-body photograph of a beautiful young woman with long wavy hair, wearing a stylish {argument name="jacket color" default="red"} leather jacket over a black silk top and black skinny jeans, standing confidently next to a classic {argument name="car color" default="silver"} convertible sports car on a European cobblestone street. The lighting is warm golden hour sunset, with historic buildings and {argument name="background element" default="palm trees"} in the soft-focus background. 1:1 aspect ratio, cinematic composition
```

[[Fashion Editorial]] [[Cinematic Photography]] [[Golden Hour]]

---

### 191. 电影时尚大片：雪中豪车离场

**Author**: [TeeJay](https://x.com/T_JayTalks)  **Date**: 2025-12-28  **Language**: en

> 一个复杂、结构化的提示，用于生成一张超现实的电影级时尚大片，画面中一位优雅的女士在黄昏时分，从一辆豪华黑色轿车中走出，置身于白雪皑皑的都市环境中，重点突出服装细节和电影般的灯光效果。

![电影时尚大片：雪中豪车离场](https://cms-assets.youmind.com/media/1767061766975_6x7d48_G9PHbJeW8AA7793.jpg)

```
[
  {
    "id": 1,
    "main_subject": {
      "persona": "Elegant high-fashion woman",
      "action": "Stepping out of a luxury black sedan",
      "physical_appearance": "Hair styled in soft voluminous waves side-parted, refined makeup emphasizing sculpted cheekbones and natural lips",
      "expression": "Confident and glamorous"
    },
    "wardrobe": {
      "main_outfit": "Deep navy blue velvet evening gown with plunging neckline and high thigh slit",
      "outerwear": "Long matching navy coat featuring plush gray fur trim on collar and cuffs",
      "accessories": ["Black quilted designer clutch with gold hardware", "Sparkling statement earrings", "Pointed metallic high heels"]
    },
    "environment": {
      "location": "Snowy urban street",
      "time_of_day": "Dusk",
      "key_elements": ["Luxury black sedan with open door", "Gently falling snowflakes", "Blurred city buildings in background", "Warm street lights creating cinematic bokeh"],
      "mood": ["Sophisticated", "Cold winter elegance", "Luxury lifestyle"]
    },
    "cinematography": {
      "style": ["Ultra-realistic", "Cinematic fashion editorial", "Magazine cover quality"],
      "composition": "Full-body portrait, vertical orientation, subject centered slightly off-axis, leading lines from car and street",
      "lighting": "Soft natural dusk light mixed with warm city street lamps, subtle rim lighting, balanced contrast",
      "technical_details": {
        "camera": "Professional DSLR",
        "lens": "85mm prime",
        "aperture": "f/1.8 (shallow depth of field)",
        "focus": "Sharp focus on subject"
      }
    },
    "parameters": {
      "quality": ["Ultra high detail", "Photorealistic skin texture", "Realistic fabric physics", "Cinematic depth"],
      "negative_prompt": "low resolution, blurry, flat lighting, harsh shadows, distorted anatomy, extra fingers, poorly drawn hands, unnatural skin texture, overprocessed, watermark, text, logo, cropped head, out of frame"
    }
  }
]
```

[[Fashion Editorial]] [[Cinematic Photography]] [[Snow Scene]] [[Luxury Automobile]]

---

### 192. 雪地里的冬季时尚大片

**Author**: [Aylin](https://x.com/kashmir_ki_lark)  **Date**: 2025-12-28  **Language**: en

> 一个结构化的 JSON 提示，用于生成一组在冬季广阔雪地中拍摄的逼真时尚大片。它详细描述了拍摄对象的着装，包括一顶 {argument name="hat type" default="蓬松米色皮草俄式棉帽"} 和一件奶油色羊羔绒飞行员夹克，置于戏剧性的阴天光线之下。

![雪地里的冬季时尚大片](https://cms-assets.youmind.com/media/1767061714739_19tpg7_G9N4FpdbgAQH_kv.jpg)

```
{
  "type": "image_prompt",
  "subject": {
    "gender": "female",
    "age": "young adult",
    "appearance": {
      "hair": "long, straight, dark",
      "expression": "serious, elegant",
      "makeup": "subtle glamorous makeup with bold red matte lipstick"
    },
    "pose": "standing confidently, hands in pockets",
    "gaze": "looking directly at the camera"
  },
  "clothing": {
    "hat": "{argument name="hat type" default="fluffy beige fur ushanka"}",
    "jacket": "cream-colored shearling aviator jacket with thick sherpa lining and collar",
    "top": "white turtleneck sweater",
    "pants": "light blue high-waisted wide-leg jeans"
  },
  "environment": {
    "season": "winter",
    "setting": "vast open snowy field",
    "details": [
      "patches of grass and rocks",
      "bare trees in the background",
      "white SUV parked distantly to the left"
    ],
    "atmosphere": "cold winter atmosphere"
  },
  "lighting": {
    "type": "natural",
    "conditions": "dramatic overcast cloudy sky with rays of sunlight breaking through"
  },
  "style": {
    "genre": "fashion editorial",
    "look": "photorealistic",
    "composition": "cinematic",
    "detail_level": "high detail"
  },
  "camera": {
    "framing": "medium to full body",
    "perspective": "eye-level",
    "focus": "sharp subject with expansive background"
  },
  "mood": "confident, elegant, dramatic"
}
```

[[Fashion Editorial]] [[Winter Fashion]] [[Overcast Lighting]] [[Snow Landscape]]

---

### 193. 写实时尚社论肖像

**Author**: [Sudee🥀](https://x.com/NameIsSudee)  **Date**: 2025-12-27  **Language**: en

> 一个为 Gemini Nano Banana Pro 设计的详细 JSON 提示，用于生成一张超逼真的时尚杂志图片。该提示指定了一位身材高挑、曲线玲珑的年轻女性，留着铂金色白发，身穿深勃艮第色中长连衣裙，置身于铺有赤陶砖的室内场景中，光线柔和自然。

![写实时尚社论肖像](https://cms-assets.youmind.com/media/1766987787729_5dq8z8_G9LeosYbgAMmw2u.jpg)
![写实时尚社论肖像](https://cms-assets.youmind.com/media/1766987787904_xtcsqp_G9Leof_aYAArujn.jpg)

```
{
  "project_metadata": {
    "format": {
      "aspect_ratio": "9:16",
      "resolution": "4K Ultra HD",
      "style": "Photorealistic Fashion Editorial"
    }
  },
  "subject_model": {
    "physical_attributes": {
      "demographics": "Young adult female, American, fair skin",
      "anatomy": {
        "build": "Slim-curvy silhouette",
        "bust_specification": "Prominent, larger bust size",
        "height": "Tall aesthetic"
      },
      "hair": {
        "color": "Platinum white",
        "style": "Long, center-parted, smooth natural waves"
      }
    },
    "performance": {
      "pose": "Full body, weight on one leg, 3/4 view",
      "expression": "Neutral, calm, looking away from camera",
      "angles": "Eye-level framing, head tilted left"
    }
  },
  "apparel_system": {
    "main_garment": {
      "type": "Bodycon midi dress",
      "fabric": "Deep burgundy Dreamy white",
      "design_specs": {
        "neckline": "Deep V-neck with lace trim",
        "straps": "Spaghetti straps",
        "length": "Mid-calf"
      }
    },
    "footwear": {
      "type": "Open-toe nude heels",
      "features": "Ankle straps, visible toes"
    }
  },
  "environment_geometry": {
    "interior_design": {
      "flooring": "Warm orange-brown terracotta tiles",
      "architecture": "Cream walls, decorative molding, frosted glass door",
      "props": {
        "furniture": "Dark polished wood console table",
        "decor": "Ceramic vase with single light pink rose"
      }
    }
  },
  "optical_engine": {
    "lighting": {
      "source": "Natural daylight from left",
      "quality": "Soft, minimal shadows, even skin illumination"
    },
    "technical": {
      "focus": "Sharp focus on subject, high dynamic range",
      "negative_constraints": [
        "blur",
        "distortion",
        "plastic skin",
        "extra limbs",
        "cartoon"
      ]
    }
  }
}
```

[[Fashion Editorial]] [[Soft Natural Light]] [[Platinum Hair]]

---

### 194. 勃艮第丝绒连衣裙的超逼真时尚大片

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-27  **Language**: en

> 一个为超逼真时尚杂志大片精心构建的详细提示。它描述了一位深色头发的年轻女性，身穿一件深酒红色压花天鹅绒紧身中长连衣裙，裙边饰有蕾丝。场景设定在铺有赤陶砖的室内，自然日光充足，旨在实现高质量、锐利且阴影极少、肤色均匀的图像。

![勃艮第丝绒连衣裙的超逼真时尚大片](https://cms-assets.youmind.com/media/1766987735747_9l5cld_G9LEge2bIAA1Dlw.jpg)
![勃艮第丝绒连衣裙的超逼真时尚大片](https://cms-assets.youmind.com/media/1766987735203_w942i9_G9LEgowbsAAxv91.jpg)

```
{
  "project_metadata": {
    "format": {
      "aspect_ratio": "9:16",
      "resolution": "4K Ultra HD",
      "style": "Photorealistic Fashion Editorial"
    }
  },
  "subject_model": {
    "physical_attributes": {
      "demographics": "Young adult female, American, fair skin",
      "anatomy": {
        "build": "Slim-curvy silhouette",
        "bust_specification": "Prominent, larger bust size",
        "height": "Tall aesthetic"
      },
      "hair": {
        "color": "{argument name=\"hair color\" default=\"dark Cadbury black\"} ",
        "style": "Long, center-parted, smooth natural waves"
      }
    },
    "performance": {
      "pose": "Full body, weight on one leg, 3/4 view",
      "expression": "Neutral, calm, looking away from camera",
      "angles": "Eye-level framing, head tilted left"
    }
  },
  "apparel_system": {
    "main_garment": {
      "type": "Bodycon midi dress",
      "fabric": "Deep burgundy crushed velvet",
      "design_specs": {
        "neckline": "Deep V-neck with lace trim",
        "straps": "Spaghetti straps",
        "length": "Mid-calf"
      }
    },
    "footwear": {
      "type": "Open-toe nude heels",
      "features": "Ankle straps, visible toes"
    }
  },
  "environment_geometry": {
    "interior_design": {
      "flooring": "Warm orange-brown terracotta tiles",
      "architecture": "Cream walls, decorative molding, frosted glass door",
      "props": {
        "furniture": "Dark polished wood console table",
        "decor": "Ceramic vase with single light pink rose"
      }
    }
  },
  "optical_engine": {
    "lighting": {
      "source": "Natural daylight from left",
      "quality": "Soft, minimal shadows, even skin illumination"
    },
    "technical": {
      "focus": "Sharp focus on subject, high dynamic range",
      "negative_constraints": [
        "blur",
        "distortion",
        "plastic skin",
        "extra limbs",
        "cartoon"
      ]
    }
  }
}
```

[[Fashion Editorial]] [[Natural Daylight]]

---

### 195. 现代奢华时尚社论肖像提示

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2025-12-27  **Language**: en

> 一个结构化的 JSON 提示词，用于让 Nano Banana Pro 生成一张超写实的时尚杂志肖像照：一位时尚男士置身于现代都市背景中，强调自信、沉着的情绪和极简奢华的美学，并采用低角度视角。

![现代奢华时尚社论肖像提示](https://cms-assets.youmind.com/media/1766987718122_kmwws1_G9KpxesaQAAkfX4.jpg)

```
{
  "Objective": "Create a stylish, ultra-realistic fashion portrait with a modern luxury aesthetic and confident masculine presence.",
  "Persona_Details": {
    "Subject": "Stylish man in his mid-20s",
    "Grooming": {
      "Beard": "Neat, well-groomed beard",
      "Hair": "Slicked-back hair, clean and polished"
    },
    "Expression_and_Pose": {
      "Mood": "Confident, composed",
      "Posture": "Strong, upright stance",
      "Hand_Positions": {
        "Right_Hand": "Gripping the overcoat lapel",
        "Left_Hand": "Resting in pocket with a visible ring"
      }
    },
    "Accessories": {
      "Eyewear": "Dark sunglasses",
      "Jewelry": "Ring on left hand"
    }
  },
  "Wardrobe": {
    "Outerwear": "Light grey overcoat",
    "Inner_Layers": {
      "Sweater": "Black sweater",
      "Shirt": "White dress shirt",
      "Tie": "Slim black tie"
    },
    "Style": "Modern, sharp, minimalist luxury"
  },
  "Scene_and_Environment": {
    "Location": "Outdoor urban setting",
    "Background": {
      "Material": "Dark marble wall",
      "Detail": "Light veining for texture",
      "Accents": "Subtle greenery",
      "Atmosphere": "Modern, refined, upscale"
    }
  },
  "Lighting": {
    "Type": "Soft natural or diffused outdoor light",
    "Effect": "Enhances textures, contrast, and fabric detail",
    "Mood": "Clean, elegant, understated"
  },
  "Camera_and_Composition": {
    "Camera_Angle": "Low-angle",
    "Framing": "Medium-close shot",
    "Perspective": "Heroic, confidence-enhancing viewpoint",
    "Depth_of_Field": "Moderate with slight background separation"
  },
  "Photography_Style": {
    "Genre": "Fashion editorial portrait",
    "Aesthetic": "Modern luxury",
    "Tone": "Confident, polished, aspirational"
  },
  "Color_and_Grading": {
    "Palette": [
      "Light grey",
      "Black",
      "White",
      "Deep charcoal marble tones",
      "Natural green accents"
    ],
    "Grading": "Clean, subtle contrast with refined highlights"
  },
  "Quality_Tags": [
    "Ultra-realistic",
    "Fashion editorial",
    "Modern luxury",
    "Urban portrait",
    "High-detail textures",
    "Professional photography"
  ],
  "Negative_Prompts": [
    "Text",
    "Logo",
    "Watermark",
    "Overly dramatic lighting",
    "Cartoon or CGI look",
    "Distorted anatomy"
  ],
  "Output_Constraints": {
    "Text_Overlay": false,
    "Branding": false,
    "Watermark": false
  },
  "Response_Format": {
    "Type": "Single image",
    "Aspect_Ratio": "4:5 or 3:4 recommended",
    "Use_Case": "Men’s fashion editorial, luxury branding, lifestyle campaign"
  }
}
```

[[Fashion Editorial]] [[Low Angle Shot]] [[Men's Fashion]] [[Confident Expression]]

---

### 196. 巴黎咖啡馆里的高端时尚大片

**Author**: [TeeJay](https://x.com/T_JayTalks)  **Date**: 2025-12-27  **Language**: en

> 一个全面的提示，用于生成一张高分辨率、时尚杂志风格的图像，描绘一位优雅女士在巴黎咖啡馆的情景。该提示详细描述了拍摄对象的着装（米色缎面连衣裙、白色西装外套）、背景（远处埃菲尔铁塔、奥斯曼建筑）、柔和的日光照明以及相机规格（50mm 或 85mm 镜头、浅景深），以实现别致、精致的美感。

![巴黎咖啡馆里的高端时尚大片](https://cms-assets.youmind.com/media/1766987728170_pm0nry_G9KdutQXkAAAoFd.jpg)

```
{
  "prompt": {
    "subject": {
      "description": "A fashionable, elegant woman seated at a Parisian café",
      "pose": "Seated with legs crossed, holding a small coffee cup in one hand",
      "expression": "Composed, confident, contemplative",
      "gaze": "Looking slightly to the side, away from the camera",
      "appearance": {
        "gender": "female",
        "age_range": "mid-20s to early-30s",
        "skin_tone": "light to medium",
        "hair": {
          "color": "blonde",
          "style": "long, loose waves, center-parted"
        },
        "makeup": {
          "style": "soft luxury glam",
          "details": "defined brows, neutral eyeshadow, subtle contour, nude lipstick"
        }
      }
    },
    "wardrobe": {
      "outfit": "{argument name=\"outfit description\" default=\"Elegant beige satin dress\"}",
      "outerwear": "White tailored blazer draped over shoulders",
      "footwear": "Beige pointed-toe high heels",
      "accessories": [
        "Luxury black quilted handbag with gold chain strap",
        "Gold wristwatch",
        "Minimal rings"
      ]
    },
    "setting": {
      "location": "Outdoor Parisian café terrace",
      "city": "Paris",
      "background_landmarks": [
        "Eiffel Tower visible in the distance",
        "Classic Parisian Haussmann buildings"
      ],
      "furniture": [
        "Round marble café tables",
        "Woven bistro chairs"
      ],
      "foreground_elements": [
        "White shopping bag with luxury branding",
        "Coffee cup and saucer"
      ]
    },
    "lighting": {
      "type": "Natural daylight",
      "time_of_day": "Late morning or afternoon",
      "quality": "Soft, diffused, overcast light",
      "effect": "Even skin tones with gentle shadows"
    },
    "camera": {
      "shot_type": "Full-body portrait",
      "angle": "Eye-level",
      "lens": "50mm or 85mm fashion lens",
      "depth_of_field": "Moderate depth of field, slightly blurred background"
    },
    "composition": {
      "framing": "Subject centered between café tables",
      "balance": "Symmetry between foreground objects and background architecture",
      "leading_lines": "Café railing and street perspective leading toward Eiffel Tower"
    },
    "mood": {
      "atmosphere": "Chic, refined, Parisian luxury lifestyle",
      "emotion": "Confidence, calm sophistication"
    },
    "style": {
      "aesthetic": "High-end fashion editorial",
      "influences": [
        "Paris street style photography",
        "Luxury lifestyle branding",
        "Editorial fashion magazines"
      ]
    },
    "image_quality": {
      "resolution": "Ultra high resolution",
      "detail_level": "Highly detailed fabrics, accessories, and facial features",
      "sharpness": "Crisp subject focus",
      "color_grading": "Neutral beige tones with soft contrast"
    }
  },
  "negative_prompt": [
    "blurry",
    "low resolution",
    "harsh lighting",
    "overexpos"
  ]
}
```

[[Fashion Editorial]] [[Natural Daylight]]

---

### 197. 高级时装花园大片，呈现倾斜石碑效果

**Author**: [BeautyVerse](https://x.com/BeautyVerse_Lab)  **Date**: 2025-12-24  **Language**: en

> 一个复杂的 JSON 结构化提示，用于生成一张高定时装社论图片。图片中，一个角色（基于参考图片）斜倚在一块对角线放置的巨石上。构图呈对角线分割：右下角是带有文字（“BeautyVerse”）的巨大石结构，左上角是一个郁郁葱葱的植物园。提示指定了专业的色彩分级（柯达 Portra 400 胶片），纹理细节，并要求主体与相机保持眼神交流，将高定时装美学与概念艺术融为一体。

![高级时装花园大片，呈现倾斜石碑效果](https://cms-assets.youmind.com/media/1766936039886_bded5k_G85m2KtagAAUNTc.jpg)
![高级时装花园大片，呈现倾斜石碑效果](https://cms-assets.youmind.com/media/1766936041091_3qrn6j_G85m2KxakAEAmhj.jpg)

```
{
  "project_title": "High-Fashion Garden Editorial - Borderless Diagonal Supine Recline with Direct Gaze",
  "structure": "Single full-frame composition. Edge-to-edge photography. No borders or collage elements.",
  "aspect_ratio": "3:4",
  "aesthetic_theme": {
    "style": "High-fashion garden editorial with professional magazine color grading",
    "mood": "Sophisticated, confident, serene, high-end catalog",
    "color_grading": "Professional fashion filter: Subtle Kodak Portra 400 aesthetics, soft diffused natural highlights, rich greens in the garden section, slightly desaturated cool tones on the stone text, and refined contrast.",
    "textures": [
      "Fine magazine paper grain",
      "Aged stone and moss textures on text",
      "Lush botanical textures in upper left"
    ]
  },
  "framing_and_borders": {
    "type": "None",
    "details": [
      "No borders, no frames, no black lines.",
      "The image fills the entire frame completely to the edges."
    ]
  },
  "subject_reference": {
    "source": "image_1.png",
    "instruction": "The subject's physical appearance, complete outfit, and accessories must exactly match the person in image_1.png. Maintain visual consistency."
  },
  "composition_details": {
    "main_frame": {
      "type": "Conceptual Full-Bleed Portrait",
      "composition_rule": "The composition is defined by a natural physical diagonal boundary running from the top-right corner to the bottom-left corner.",
      "setting_description": "The frame is seamlessly divided by the subject and the structure. The lower-right half is a massive, solid stone 'BeautyVerse' structure. The upper-left half is filled with a lush, soft-focus botanical garden.",
      "subject_pose": "The subject is reclining supine (lying on her back) along the diagonal edge of the stone structure, body angled from top-right to bottom-left. **Her head is slightly turned or angled upwards to allow her eyes to gaze directly and intensely into the camera lens.** She maintains a relaxed but engaging high-fashion expression while making eye contact. Her back is in direct contact with the stone surface.",
      "key_element_description": {
        "object": "A massive, edge-filling topographical stone monolith.",
        "text_content": "{argument name=\"Stone Text\" default=\"BeautyVerse\"}",
        "alignment": "The text structure completely fills the lower-right diagonal triangle of the frame. The diagonal edge of these letters forms the 'bed' the subject lies upon.",
        "text_style": "Massive, bold"
```

[[Fashion Editorial]] [[Kodak Portra 400 Film]]

---

### 198. 魅惑单色黑夜外出时尚大片

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2025-12-23  **Language**: en

> 一个结构化的 JSON 提示，用于生成一张迷人、高端时尚的黑白编辑摄影作品，内容为一名年轻女性在夜晚的繁华都市街道上，强调奢华造型、特定灯光和精致、非挑衅的氛围。

![魅惑单色黑夜外出时尚大片](https://cms-assets.youmind.com/media/1766673132937_81eox3_G839BK6XYAAgqxQ.jpg)

```
{
  "subject": {
    "description": "Young woman with long, wavy jet-black hair.",
    "pose": "Standing facing the camera, slight elegant smile, arms relaxed and natural.",
    "expression": "Soft, confident, and engaging.",
    "makeup": "Classic black smoky eye makeup, softly contoured cheeks, natural satin skin finish, nude/rose lip.",
    "styling_notes": [
      "Elegant, tasteful cleavage (not deep, not provocative)",
      "Refined luxury mood"
    ]
  },
  "outfit": {
    "top": "Elegant black blouse with a tasteful neckline: sweetheart neckline or soft V-neck (moderate depth), structured bust seams, no sheer fabric, no cutouts.",
    "outerwear": "Large plush black faux fur coat worn off the shoulders, draped around the elbows.",
    "bottoms": "Black sequined trousers or black sequined skirt, partially visible.",
    "accessories": "Small black clutch handbag (matte leather or satin) held in hand.",
    "jewelry": [
      "Black diamond heart-shaped pendant necklace on a delicate chain (resting above the neckline)"
    ],
    "color_rule": "All clothing and accessories are black (monochrome black-on-black styling)."
  },
  "environment": {
    "location": "Upscale city street at night ({argument name="city" default="London"} implied by Union Jack flags).",
    "background_elements": [
      "Grand building entrance with large stone columns.",
      "Union Jack flags hanging from the building facade.",
      "Ornate black metal gate.",
      "Large green hedge covered in warm white fairy lights.",
      "Parked black luxury car (Rolls-Royce style) on the street.",
      "City streetlights and blurred pedestrians in the distance."
    ]
  },
  "lighting": {
    "type": "Nighttime ambient city lighting.",
    "qualities": "Warm glow from building and fairy lights mixed with cool street lighting. Subject is cleanly illuminated by a nearby street lamp or storefront spill light, with natural night grain."
  },
  "style": {
    "aesthetic": "Glamorous night out, luxury lifestyle, influencer snapshot (elegant, not provocative).",
    "perspective": "Eye-level, medium shot.",
    "camera_feel": "High-quality smartphone photo, slight night grain, candid-but-posed, realistic skin texture (no beauty retouch)."
  },
  "negative_prompt": [
    "deep_plunging_neckline",
    "extreme_cleavage",
    "lingerie",
    "see_through_top",
    "chest_cutout",
    "underboob",
    "overly_sexual_pose",
    "studio_lighting",
    "beauty_retouch",
    "plastic_skin",
    "over_sharpening",
    "text",
    "logo",
    "watermark",
    "extra_people_in_foreground"
  ]
}
```

[[Fashion Editorial]]

---

### 199. 奢华室内泳池时尚大片提示

**Author**: [Synthorigen](https://x.com/synthorigenn)  **Date**: 2025-12-21  **Language**: en

> 一个全面的 JSON 提示，用于生成一张超写实的时尚杂志摄影作品。它详细描述了场景（一位女士坐在大窗户旁的室内大理石无边泳池边缘）、服装（勃艮第色人造皮草夹克、蕾丝连裤袜）、灯光（自然日光营造柔和阴影）和技术规格（85mm 镜头、浅景深），以达到奢华杂志的品质。

![奢华室内泳池时尚大片提示](https://cms-assets.youmind.com/media/1766489459800_kzanah_G8s0eLYXsAAZVnB.jpg)

```
{
  "model": "nano-banana-pro",
  "prompt": "Hyper-realistic fashion editorial photograph. A young woman is sitting on the marble edge of a modern indoor infinity pool beside a large floor-to-ceiling glass window. She wears a deep burgundy faux fur jacket with dense realistic fur texture and matching burgundy lace tights. Her posture is elegant and calm, legs crossed, one hand placed naturally on the marble surface, the other resting softly on her thigh. She has fair skin with natural skin texture, soft glam makeup, nude glossy lips, subtle blush, and defined eyelashes. Her facial expression is thoughtful, eyes looking slightly upward and out of frame. Hair is medium-length, light brown with soft blonde highlights, styled in loose natural waves with curtain bangs. Natural daylight fills the room, creating soft shadows and accurate color tones. Outside the glass window is a sunny hillside residential area with trees and modern houses, slightly blurred with realistic depth of field. Pool water is clear with gentle ripples reflecting light onto white marble. Shot on a professional DSLR camera, 85mm lens, shallow depth of field, cinematic framing, luxury fashion magazine quality, ultra-detailed fabrics, realistic hair strands, natural skin pores, no distortion.",
  "negative_prompt": "illustration, painting, cartoon, anime, 3D render, CGI, doll-like face, plastic skin, harsh lighting, artificial colors, oversharpening, blur, low resolution, watermark, logo, text, cropped body, deformed anatomy, extra fingers, extra limbs",
  "style": "photorealistic fashion editorial",
  "lighting": "soft natural daylight",
  "camera": {
    "lens": "85mm",
    "aperture": "f/1.8",
    "iso": 100
  },
  "quality": "ultra",
  "resolution": "4096x2304",
  "guidance_scale": 7.5,
  "seed": 123456
}
```

[[Fashion Editorial]] [[Natural Daylight]] [[85mm Lens]]

---

### 200. 海岸别致双格拼贴肖像

**Author**: [CALLISTUS 🥷🏖️](https://x.com/Callistus200)  **Date**: 2025-12-19  **Language**: en

> 一个为 Gemini Nano Banana Pro 设计的图像生成提示，详细描述了一幅由两幅拼贴画组成的年轻女性肖像，风格为 Y2K 影响下的海岸时尚美学。该提示详细说明了拍摄对象的特征、妆容（“洁净女孩”审美）、服装（解构式白色露背上衣）和配饰（银色翅膀吊坠），背景设定在黄金时段俯瞰地中海风格城市的户外阳台。

![海岸别致双格拼贴肖像](https://cms-assets.youmind.com/media/1766238164206_271r65_G8ibnENWYAEXWF8.jpg)

```
{
  "subject": {
    "identity": "Young woman with a slim build and sun-kissed complexion",
    "pose": "Two-panel collage; left side showing a profile view looking away, right side showing a playful frontal view with tongue slightly out",
    "expression": "Left: Serene and poised; Right: Playful, energetic, and expressive"
  },
  "face_and_makeup": {
    "features": "Doe-shaped brown eyes, well-defined dark eyebrows, slender nose, and full lips",
    "makeup": "Soft 'clean girl' aesthetic: shimmering bronze eyeshadow, winged eyeliner, peach-toned blush, and a lined glossy mauve lip",
    "details": "Subtle nose stud on the nostril"
  },
  "hair": {
    "style": "Curly high bun (updo) with a textured, wet-look finish",
    "details": "Two distinct face-framing curly tendrils hanging down the forehead and sides",
    "color": "Dark espresso / black"
  },
  "clothing": {
    "top": "Deconstructed {argument name="top color" default="white"} halter-neck top with an asymmetrical, ruffled hemline",
    "fabric": "Textured gauze or lightweight linen with crochet/knit detailing on the bust",
    "fit": "Cropped, exposing the midriff with thin string ties"
  },
  "accessories": {
    "necklace": "Large silver statement pendant shaped like a detailed bird wing",
    "rings": "Ornate silver rings, including a matching wing-shaped wrap ring and a chunky band",
    "jewelry_other": "Small silver hoop earrings and a dark-jeweled navel piercing"
  },
  "environment": {
    "location": "Outdoor balcony overlooking a coastal Mediterranean-style city",
    "background_elements": [
      "Deep blue ocean with luxury yachts and cruise ships",
      "Palm trees and lush greenery",
      "White multi-story resort or apartment buildings",
      "Bright, diffused natural daylight"
    ]
  },
  "style_and_composition": {
    "aesthetic": "Summer luxury, Y2K-influenced coastal chic",
    "lighting": "Bright, warm golden hour sunlight with soft shadows",
    "color_palette": "Dominant whites and blues contrasted with warm skin tones and silver accents",
    "image_type": "High-resolution digital photography, portrait orientation"
  }
}
```

[[Fashion Editorial]] [[Y2K Aesthetic]] [[Golden Hour]] [[Clean Girl Aesthetic]]

---

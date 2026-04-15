# Chunk 016

Total: 200 prompts

### 1. 四格复古生活方式拼贴画，带身份锁

**Author**: [آیت شاہ](https://x.com/kashmir_ki_lark)  **Date**: 2025-12-20  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一个女性主体的 2x2 拼贴画，要求基于参考图像实现 100% 的身份、姿势和摄像机角度锁定。场景是一个浪漫的复古室内房间，主体穿着一件白色和蓝色花卉泡泡袖连衣裙，头发上系着一个米色丝带蝴蝶结。

![四格复古生活方式拼贴画，带身份锁](https://cms-assets.youmind.com/media/1766385985701_ys81vv_G8kgrNzbMAAM43Z.jpg)

```
{
  "image_prompt": {
    "reference": {
      "face_identity": "uploaded reference image",
      "identity_lock": true,
      "pose_lock": true,
      "camera_angle_lock": true,
      "expression_lock": true,
      "face_preservation": "100% identical facial structure, proportions, eyes, lips, nose, brows, skin texture"
    },

    "composition": {
      "layout": "2x2 collage",
      "aspect_ratio": "1:1",
      "pose_matching": "exactly match reference image poses, angles, framing, and body orientation",
      "no_variation_allowed": true
    },

    "panel_1": {
      "view": "front-facing portrait",
      "pose": "head slightly tilted, eyes toward camera, soft lips",
      "framing": "chest-up selfie angle",
      "expression": "calm, elegant",
      "match_reference": true
    },

    "panel_2": {
      "view": "back view",
      "pose": "standing facing mirror, arms raised slightly",
      "focus": "back of head and bow hairstyle",
      "framing": "upper-body rear shot",
      "match_reference": true
    },

    "panel_3": {
      "view": "mirror selfie",
      "pose": "phone covering part of face, body angled sideways",
      "framing": "waist-up",
      "match_reference": true
    },

    "panel_4": {
      "view": "side portrait",
      "pose": "head turned over shoulder looking into camera, holding bouquet close to chest",
      "expression": "soft romantic gaze",
      "framing": "upper torso",
      "match_reference": true
    },

    "subject": {
      "gender": "female",
      "ethnicity": "Asian",
      "skin_tone": "fair with soft blush"
    },

    "hair": {
      "style": "long straight hair, half-up",
      "accessory": "large cream ribbon bow",
      "placement": "exact position as reference image"
    },

    "outfit": {
      "dress": {
        "color": "white",
        "pattern": "blue floral print",
        "style": "vintage puff-sleeve dress",
        "neckline": "square neckline"
      },
      "jewelry": [
        "pearl necklace",
        "delicate gold pendant"
      ]
    },

    "environment": {
      "location": "vintage-style indoor room",
      "background": [
        "ornate mirror",
        "cream walls",
        "soft floral decor",
        "classic furniture"
      ],
      "match_reference_background": true
    },

    "lighting": {
      "type": "soft indoor daylight",
      "quality": "even, gentle, warm",
      "shadow": "minimal",
      "match_reference": true
    },

    "photography_style": {
      "style": "romantic vintage lifestyle",
      "lens": "DSLR portrait lens",
      "depth_of_field": "shallow",
      "color_grading": "soft pastel"
    },

    "render_quality": {
      "realism": "photorealistic",
      "resolution": "high",
      "texture_detail": "natural skin and fabric detail",
      "no_cartoon": true
    }
  }
}
```

[[Identity Locking]]

---

### 2. 高清复古闪光肖像提示词

**Author**: [Ezgi Subaşı 👩🏼‍💻](https://x.com/ezgisubasi)  **Date**: 2025-12-19  **Language**: en

> 一个为 Nano Banana Pro 设计的详细 JSON 提示，旨在将输入照片转换为高清、暖色调的复古肖像。它规定了严格的身份锁定规则、真实的皮肤纹理保留、复古色彩分级，以及一个带有闪光灯照明和构图细节的特定室内走廊场景。

![高清复古闪光肖像提示词](https://cms-assets.youmind.com/media/1766238201047_o2h084_G8kcg1RWcAMqusY.jpg)
![高清复古闪光肖像提示词](https://cms-assets.youmind.com/media/1766238202424_p9opgk_G8kcmm3XAAAP4AE.jpg)

```
{
"meta":{
"quality":"High-Definition",
"type":"Evening indoor flash portrait",
"ratio":"4:5 vertical",
"device":"iPhone 16 Pro",
"style_reference":"Transform the INPUT PHOTO into this exact aesthetic.",
"look":"Evening flash, warm-toned vintage, real grain, realistic skin texture (NO smoothing)."
},

"identity_lock":{
"preserve_face": true,
"strict": true,
"rules":[
"The face MUST remain IDENTICAL to the input photo.",
"No changes to facial structure, proportions, expression, or identity.",
"No smoothing, no beautify, no retouch, no AI facial alterations."
]
},

"skin_texture_rules":{
"keep_texture": true,
"no_smoothing": true,
"no_blur": true,
"realistic_details": "natural texture preserved.",
"flash_behavior":"Flash highlights should reveal texture, not hide it."
},

"vintage_effect":{
"warmth":"+18",
"contrast":"+22",
"highlights":"-5",
"shadows":"+12",
"grain":"Medium (film-like)",
"vignette":"Soft",
"color_grade":"Warm beige vintage tint",
"sharpness":"Slightly reduced to mimic old camera softness"
},

"global_context":{
"scene_description":"Indoor hallway with wall decor, mirror reflection, white walls and warm flash lighting.",
"time_of_day":"Evening",
"lighting":"Direct warm flash illuminating the subject with strong falloff into the background.",
"environment_details":[
"Mirror behind the subject with reflection visible.",
"White paneled walls.",
"Marble/stone console table with a floral arrangement.",
"Soft shadows created by harsh flash."
]
},

"composition":{
"camera_angle":"Eye-level, straight-on portrait",
"framing":"Knees-up full portrait",
"pose":"Body leaning slightly forward with one hand on console table and the other arm across the torso.",
"expression":"Confident, pouty, soft glamorous gaze.",
"flash_effect":"Glossy highlights on skin and dress."
},

"subject":{
"makeup":{
"style":"Soft glam.",
"lips":"Pink-brown gloss with warm undertone.",
"eyes":"Eyeliner + lashes.",
"blush":"Warm peach."
},
"skin":"Natural undertone, realistic texture, NOT smoothed.",
"outfit":{
"dress":"White mini halter dress with deep neckline and satin-like shine.",
"fabric_behavior":"Flash creates bright reflections and visible folds."
}
},

"background_objects":[
{
"id":"mirror",
"description":"Large wall mirror reflecting the subject's pose.",
"lighting":"Flash reflection visible but subdued."
},
{
"id":"flowers",
"description":"Vibrant bouquet on the table (yellow, purple, green)."
},
{
"id":"wall",
"description":"White paneled wall with framed signage."
}
],

"rules":{
"identity_constant": true,
"no_face_change": true,
"no_ai_artifacts": true,
"realism":"Ultra realistic evening flash aesthetic with vintage tones."
}
}
Use the uploaded photo as the input image. Generate the image.
```

[[Identity Locking]] [[Natural Skin Texture]] [[Flash Lighting]]

---

### 3. 花卉咖啡馆里的仙女风镜面自拍

**Author**: [Zaylee](https://x.com/zayleeai)  **Date**: 2025-12-19  **Language**: en

> 这是一个针对 Gemini Nano Banana Pro 的高度具体的图像生成提示，要求严格遵循参考照片的面部特征。该提示详细描述了一个全身镜面自拍姿势（低蹲），呈现出浪漫的仙女核心美学，并指定了淡粉色紧身胸衣连衣裙、蝴蝶装饰高跟鞋以及迷人的花卉咖啡馆室内场景，目标是实现 8K 超真实感。

![花卉咖啡馆里的仙女风镜面自拍](https://cms-assets.youmind.com/media/1766238163896_2rf84u_G8kPCD-WkAIaqRk.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "reference_adherence": "Strictly match the provided reference photo face exactly",
      "facial_features": [
        "Preserve exact face shape",
        "Match eye structure and eyebrow shape",
        "Retain lip shape and natural color"
      ],
      "hair": "{argument name="hair color" default="black"}, exact hairstyle from reference",
      "makeup": "Natural style as per reference",
      "expression": "Soft, calm, looking at phone screen"
    },

    "apparel": {
      "main_garment": "Soft pastel {argument name="dress color" default="pink"}, romantic corset-style mini dress inspired by a fairy-core aesthetic. Off-shoulder neckline with delicate gathered fabric, lace-up corset bodice that cinches the waist, and a flowy chiffon skirt with layered movement. Long, sheer, flared sleeves that drape gracefully with light fabric transparency. Dress matches exactly the reference pink dress in color, silhouette, and romantic style.",
      "fabric_physics": "Lightweight chiffon and satin blend, airy movement, natural folds, soft wind-like flow",
      "footwear": "Pastel blush {argument name="shoe color" default="pink"} satin high-heeled sandals with a square toe. Delicate thin straps adorned with embroidered 3D butterfly appliqués across the front and ankle straps. Slim feminine heel, elegant fairy-core aesthetic, matching exactly the reference butterfly heels in color, texture, and romantic detail.",
      "accessories": [
        "Silver necklace",
        "Silver bracelet",
        "Silver rings"
      ]
    },

    "pose_and_action": {
      "type": "Full-body mirror selfie",
      "stance": "Squatting low gracefully, one knee forward, leaning slightly toward mirror",
      "head_position": "Tilted slightly downward",
      "hands": {
        "right_hand": "Holding phone vertically in front of face",
        "left_hand": "Resting gently on knee"
      },
      "props": "Smartphone with soft pink phone case, soft pastel tone, minimal design"
    },

    "environment": {
      "location": "Charming floral cafe interior",
      "background": "Romantic European-style floral cafe with stone-textured walls, hanging wicker baskets, dried flower arrangements, pastel floral bouquets, vintage wooden shelves, rustic beams, and soft decorative mirrors. Warm neutral stone tones mixed with soft pinks, greens, creams, and lavender florals. Cozy, aesthetic, feminine atmosphere.",
      "flooring": "Vintage patterned tile floor with subtle reflections"
    },

    "lighting_and_atmosphere": {
      "quality": "Soft, ambient cafe lighting with gentle highlights",
      "mood": "Feminine, romantic, elegant, fairy-core, social media aesthetic"
    },

    "technical_specifications": {
      "quality": "8K resolution, photorealistic, high fidelity",
      "focus": "Sharp focus on face and outfit",
      "perspective": "Eye-level mirror perspective",
      "aspect_ratio": "4:5"
    }
  }
}
```

[[Identity Locking]] [[8K Hyperrealistic Photography]]

---

### 4. 画廊墙面肖像，带身份锁

**Author**: [ttmouse - 豆爸](https://x.com/ttmouse)  **Date**: 2025-12-19  **Language**: zh

> 一个用于图像生成的提示，它使用一张参考照片来保持主体的身份，同时将其置于一个戏剧性的、高级时装的场景中。主体被置于一面无缝墙壁前，墙壁上完全覆盖着他们自己的黑白肖像，强调电影般的超写实品质。

![画廊墙面肖像，带身份锁](https://cms-assets.youmind.com/media/1766238100501_aik8te_G8kBFCuXEAA5m5o.jpg)
![画廊墙面肖像，带身份锁](https://cms-assets.youmind.com/media/1766238100825_9udbml_G8kBFCuW8AAcSTu.jpg)
![画廊墙面肖像，带身份锁](https://cms-assets.youmind.com/media/1766238102217_d59lws_G8kBFCsWcAAC3vD.jpg)

```
基于【参考照片人物】
A high-quality 9:16 vertical portrait, 4k resolution. 
**Framing:** Medium-long shot (framed from the knees up, focusing on torso and head). 
**Subject:** The woman from the reference image, standing in 3/4 profile facing left, looking at the lens. She wears a structured black long trench coat. 
**Background:** An infinite, edge-to-edge gallery wall completely covered in a dense, seamless grid of black and white fashion portraits of herself. The photo wall fills 100% of the background frame behind her. No floor visible, no ceiling visible, just the texture of the photos. 
**Lighting:** Even, professional gallery lighting highlighting the coat's texture and the details of the background prints. 
**Quality:** Ultra-photorealistic, sharp focus, cinematic depth.
--ar 9:16 --v 6.0
```

[[Identity Locking]]

---

### 5. 黄金时刻海滩自拍提示词

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-06  **Language**: en

> 一份用于生成超写实黄金时刻海滩自拍的详细提示词，重点在于自然阳光、真实的皮肤纹理、具体的服装细节，并确保生成的图像与上传的参考图主体身份完全一致。

![黄金时刻海滩自拍提示词](https://cms-assets.youmind.com/media/1775544742848_u18455_HFPS7heboAAuwAK.jpg)
![黄金时刻海滩自拍提示词](https://cms-assets.youmind.com/media/1775544742917_svp913_HFPS27faoAEqf2o.jpg)
![黄金时刻海滩自拍提示词](https://cms-assets.youmind.com/media/1775544742945_q4rffs_HFPS5DKbYAAyLkw.jpg)
![黄金时刻海滩自拍提示词](https://cms-assets.youmind.com/media/1775544743903_87c4mt_HFPS9E6bEAAdfnN.jpg)

```
{
  "scene": {
    "setting": "outdoor beach environment during golden hour",
    "background": "warm sandy beach with textured grains, tall coastal trees with soft green foliage, subtle distant beach elements slightly blurred, clear blue sky with soft clouds",
    "lighting": "natural golden hour sunlight from side angle creating warm highlights on skin and hair, soft shadows with smooth falloff, slightly directional light enhancing facial contours, realistic sun glow"
  },
  "subject": {
    "type": "female",
    "pose": "selfie-style pose with arm extended toward camera, torso slightly angled, shoulders relaxed, head slightly tilted with natural posture",
    "expression": "soft relaxed expression with subtle confident gaze, slightly parted lips for natural candid feel",
    "face": "Use uploaded reference image, keep identity exact, oval face shape, soft defined cheekbones, natural skin texture with visible pores and minor imperfections, realistic highlight and shadow balance",
    "hair": "Use uploaded reference image, keep identity exact",
    "eyes": "Use uploaded reference image, keep identity exact, almond-shaped eyes, natural brows with soft arch",
    "skin": "light warm skin tone with golden sunlight highlights, realistic texture with slight natural sheen, no over-smoothing"
  },
  "clothing": {
    "top": "lightweight sheer {argument name="top color" default="white"} blouse with soft fabric transparency, flowy sleeves, front tie detail, natural wrinkles and fabric folds",
    "bottom": "blue denim jeans with realistic texture and slight fading",
    "footwear": "not visible",
    "accessories": "delicate necklace with small beads, minimal jewelry"
  },
  "environment_details": {
    "props": "natural beach elements with textured sand and scattered footprints",
    "textures": "fine sand grain detail, soft fabric translucency, natural hair strands, foliage depth with light passing through leaves"
  },
  "camera": {
    "angle": "slightly high selfie angle",
    "framing": "medium close-up with upper body dominant",
    "focus": "sharp focus on subject with softly blurred background",
    "lens": "wide smartphone lens with slight perspective distortion, natural depth of field"
  },
  "style": {
    "realism": "ultra realistic",
    "color_tone": "warm golden tones with rich contrast between skin and background, natural blues and greens",
    "effects": "subtle HDR, gentle sun flare, soft highlight bloom, natural color grading, slight film grain",
    "details": "high detail skin texture, realistic lighting interaction, accurate fabric translucency, no artificial smoothing or over-processing"
  }
}
```

[[Identity Preservation]] [[Lifestyle Photography]] [[Skin Texture]] [[Beach Photography]]

---

### 6. 户外花园人像，柔和阳光照耀

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-05  **Language**: en

> 一份详细的 Nano Banana Pro 提示词，用于生成一张超写实的女性户外花园中景人像。重点在于强烈的自然阳光、温暖的高光效果，并使用参考图以确保面部特征精准还原。

![户外花园人像，柔和阳光照耀](https://cms-assets.youmind.com/media/1775458532482_u8w1l1_HFK5Akab0AAM4TF.jpg)
![户外花园人像，柔和阳光照耀](https://cms-assets.youmind.com/media/1775458532463_k4c8jl_HFK5B9zacAEYZK8.jpg)
![户外花园人像，柔和阳光照耀](https://cms-assets.youmind.com/media/1775458532481_8yoz4o_HFK5BOKaYAEhwPk.jpg)

```
{
  "scene": {
    "setting": "outdoor garden pathway in a landscaped park",
    "background": "green manicured lawn with trimmed bushes, tall trees, and a fountain in the distance, clear blue sky with bright daylight",
    "lighting": "strong natural sunlight, high clarity with crisp shadows, warm highlights on skin, balanced exposure with realistic contrast"
  },
  "subject": {
    "type": "female",
    "pose": "standing on pathway, one arm raised with hand touching hair, other hand slightly extended forward, torso facing camera with slight angle",
    "expression": "soft confident expression with subtle smile, direct eye contact with camera, relaxed and poised mood",
    "face": "Use uploaded reference image, keep identity exact, oval face shape, soft defined cheekbones, natural skin texture with visible pores and minor imperfections, full lips, straight nose, balanced facial proportions",
    "hair": "Use uploaded reference image, keep identity exact",
    "eyes": "Use uploaded reference image, keep identity exact, almond-shaped eyes, natural brows with soft arch",
    "skin": "light to medium skin tone with natural sunlight glow, realistic texture, subtle highlights and shadows"
  },
  "clothing": {
    "top": "{argument name="top garment" default="black fitted corset-style top"} with structured seams and strapless design",
    "bottom": "{argument name="bottom garment" default="blue denim jeans"} with natural texture",
    "footwear": "not visible",
    "accessories": "necklace, rings, bracelet"
  },
  "environment_details": {
    "pathway": "light gravel or stone pathway with natural texture",
    "garden": "symmetrical landscaping with trimmed bushes and greenery",
    "fountain": "water fountain in background adding depth and elegance"
  },
  "camera": {
    "angle": "eye-level angle",
    "framing": "medium shot focused on upper body",
    "focus": "sharp focus on subject, background softly blurred",
    "lens": "portrait lens with shallow depth of field"
  },
  "style": {
    "realism": "ultra realistic",
    "color_tone": "natural vibrant tones with enhanced greens and warm skin highlights",
    "details": "high detail skin texture, fabric definition, realistic lighting and shadows, no over-smoothing"
  }
}
```

[[Identity Preservation]] [[Female Portrait]] [[Natural Sunlight]] [[Mid-Shot Composition]]

---

### 7. 户外花园人像，柔和阳光照耀

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-05  **Language**: en

> 一份详细的 Nano Banana Pro 提示词，用于生成一张超写实的女性户外花园中景人像。重点在于强烈的自然阳光、温暖的高光效果，并使用参考图以确保面部特征精准还原。

![户外花园人像，柔和阳光照耀](https://cms-assets.youmind.com/media/1775458532482_u8w1l1_HFK5Akab0AAM4TF.jpg)
![户外花园人像，柔和阳光照耀](https://cms-assets.youmind.com/media/1775458532463_k4c8jl_HFK5B9zacAEYZK8.jpg)
![户外花园人像，柔和阳光照耀](https://cms-assets.youmind.com/media/1775458532481_8yoz4o_HFK5BOKaYAEhwPk.jpg)

```
{
  "scene": {
    "setting": "outdoor garden pathway in a landscaped park",
    "background": "green manicured lawn with trimmed bushes, tall trees, and a fountain in the distance, clear blue sky with bright daylight",
    "lighting": "strong natural sunlight, high clarity with crisp shadows, warm highlights on skin, balanced exposure with realistic contrast"
  },
  "subject": {
    "type": "female",
    "pose": "standing on pathway, one arm raised with hand touching hair, other hand slightly extended forward, torso facing camera with slight angle",
    "expression": "soft confident expression with subtle smile, direct eye contact with camera, relaxed and poised mood",
    "face": "Use uploaded reference image, keep identity exact, oval face shape, soft defined cheekbones, natural skin texture with visible pores and minor imperfections, full lips, straight nose, balanced facial proportions",
    "hair": "Use uploaded reference image, keep identity exact",
    "eyes": "Use uploaded reference image, keep identity exact, almond-shaped eyes, natural brows with soft arch",
    "skin": "light to medium skin tone with natural sunlight glow, realistic texture, subtle highlights and shadows"
  },
  "clothing": {
    "top": "{argument name="top garment" default="black fitted corset-style top"} with structured seams and strapless design",
    "bottom": "{argument name="bottom garment" default="blue denim jeans"} with natural texture",
    "footwear": "not visible",
    "accessories": "necklace, rings, bracelet"
  },
  "environment_details": {
    "pathway": "light gravel or stone pathway with natural texture",
    "garden": "symmetrical landscaping with trimmed bushes and greenery",
    "fountain": "water fountain in background adding depth and elegance"
  },
  "camera": {
    "angle": "eye-level angle",
    "framing": "medium shot focused on upper body",
    "focus": "sharp focus on subject, background softly blurred",
    "lens": "portrait lens with shallow depth of field"
  },
  "style": {
    "realism": "ultra realistic",
    "color_tone": "natural vibrant tones with enhanced greens and warm skin highlights",
    "details": "high detail skin texture, fabric definition, realistic lighting and shadows, no over-smoothing"
  }
}
```

[[Identity Preservation]] [[Female Portrait]] [[Natural Sunlight]] [[Mid-Shot Composition]]

---

### 8. Emma Myers 角色扮演风格的超写实镜面自拍

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-04-05  **Language**: en

> 一份为 Nano Banana Pro 准备的详细 JSON 提示词，旨在生成一张 Emma Myers 的超写实镜面自拍。重点刻画其面部特征、自信的姿态，以及细节丰富的角色扮演风格服装，包括罗纹短款上衣、超短粉色热裤和过膝袜，背景设定在光线柔和自然的极简主义房间内。

![Emma Myers 角色扮演风格的超写实镜面自拍](https://cms-assets.youmind.com/media/1775458527179_ik0mcb_HFJ3aRLWMAAQJw9.jpg)
![Emma Myers 角色扮演风格的超写实镜面自拍](https://cms-assets.youmind.com/media/1775458527234_r6d7jx_HFJ3aNpWoAAzJKe.jpg)
![Emma Myers 角色扮演风格的超写实镜面自拍](https://cms-assets.youmind.com/media/1775458527625_gpgk7n_HFJ3aRGaQAAxYR9.jpg)

```
{
  “meta”: {
    “quality”: “photorealistic, raw style, 8k, detailed skin texture”,
    “camera”: “Shot on a modern smartphone (e.g., iPhone 15 Pro Max) as a mirror selfie, shallow depth of field, natural lighting”,
    “style”: “cosplay photography, casual snapshot, single-person focus”,
    “aspect_ratio”: “4:5”
  },
  “scene”: {
    “location”: “A minimalist white paneled room with two closed white doors and brass knobs.”,
    “atmosphere”: “Casual, clean, intimate, personal snapshot.”
  },
  “subject”: {
    “name”: “{argument name="subject name" default="Emma Myers"}”,
“features”: “Clear and full view of Emma Myers’ distinct facial features with expressive blue eyes, distinct nose, and a pointed cupid’s bow on a prominent top lip. Her face is naturally beautiful with defined features and a realistic, non-plastic appearance. Her naturally medium-blonde hair is styled in sleek, wavy layers falling over her shoulders, combined with graduated face-framing strands. The camera focus is sharp on her features.”,
    “pose”: “A centered medium-shot mirror selfie. She holds the smartphone in her right hand to capture the image. Her left hand is making a two-finger peace sign towards the mirror. Her body is mostly forward, looking directly at the camera through the mirror. The camera is held up but to the side, not obscuring her face.”,
    “expression”: “A clear, confident, and genuine smile, looking direct.”
  },
  “wardrobe”: {
“top”: “A detailed, white ribbed drawstring ruched crop top with the drawstring tie visible and centered on the chest.”,
    “bottom”: “Ultra-mini, tight-fitting pink hotpants (booty shorts) with a distinct ribbed texture. They sit high on the hips and cut high on the thighs, tightly hugging and accentuating her athletic fitness figure.”,
    “legwear”: “White thigh-high stockings visible on the upper legs, above the knee.”,
    “accessories”: “A silver beaded bracelet on the left wrist and a subtle pendant necklace.”
  },
  “phone_case”: {
    “description”: “She holds the smartphone which is encased in a detailed pink Rilakkuma (bear-eared) phone case with an adorable face design, held clearly to the side of her face or lower, not obscuring it.”
  },
  “lighting”: {
    “type”: “Soft, even indoor lighting from an unseen overhead source, casting natural shadows and highlights on the fabrics and skin.”
  },
“physique_details”: {
    “description”: “Emma Myers’ fit, athletic, and somewhat sharp fitness-style curvy physique, rendered naturally as seen in casual snapshots, filling out the form-fitting clothing.”,
    “constraints”: [
      “Body shape must be naturally athletic-curvy.”,
      “Shorts must be ultra-mini and skin-tight/booty shorts style.”
    ]
  },
  “composition”: “A centered, detailed, photorealistic mirror selfie, waist-up perspective, capturing the pose and setting accurately. A cluster of small, delicate pink cherry blossoms (sakur
```

[[Identity Preservation]] [[Natural Light]] [[Cosplay Photography]]

---

### 9. 超写实电影感肖像：破碎玻璃与奢华配饰

**Author**: [a Kid called | Dgod](https://x.com/DG0DNFT)  **Date**: 2026-04-05  **Language**: en

> 这是一个为 Gemini Nano Banana 设计的高细节提示词，旨在根据上传的人脸参考图创作 8K 超写实电影感肖像，包含破碎玻璃、情绪化灯光，以及参考第二张图片中的特定奢华配饰（劳力士手表和戒指）。

![超写实电影感肖像：破碎玻璃与奢华配饰](https://cms-assets.youmind.com/media/1775458523886_7g28oj_HFJNcLNbIAAfDI8.jpg)
![超写实电影感肖像：破碎玻璃与奢华配饰](https://cms-assets.youmind.com/media/1775458523756_bnjkle_HFJNcKkWUAA-WcW.jpg)

```
Ultra-realistic 8K cinematic portrait of image1- use face reference exactly — with facial features identical to the uploaded image no mouth or nose. He looks directly into the camera with a powerful, thoughtful expression, one hand resting on his chin in a confident pose.
Surround him with shattered glass and broken mirror fragments reflecting distorted versions of his own face, creating a dramatic and commanding visual effect. Lighting is low-key and moody, with rich shadows and selective golden highlights accentuating his face and suit. The background remains dark and atmospheric. On the left hand only, add a Rolex watch and a Ring image2 reference. Style: hyper-realistic digital painting, luxury cinematic tone, deep contrast, refined details, and a bold, high-end editorial finish.
Close in zoom capturing the face watch and ring closeup, the character should remain exactly the same unchanged with white gloves
```

[[Identity Preservation]] [[Cinematic Portrait]] [[Dramatic Lighting]]

---

### 10. 具有身份锁定功能的高端海滩生活方式照片

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-03  **Language**: en

> 一个用于 Nano Banana Pro 的提示词，旨在生成一张年轻女性在洁白沙滩上的高端美学生活方式照片。该提示词要求严格保持参考图像的身份特征，并指定了极简夏季服装、自然自信的姿势，以及明亮柔和的自然日光，以营造超写实、高时尚且轻盈的氛围。

![具有身份锁定功能的高端海滩生活方式照片](https://cms-assets.youmind.com/media/1775284646711_gc9dqa_HE_q1-ja4AAZEIR.jpg)
![具有身份锁定功能的高端海滩生活方式照片](https://cms-assets.youmind.com/media/1775284646700_yehtda_HE_q1hAbgAACwu5.jpg)
![具有身份锁定功能的高端海滩生活方式照片](https://cms-assets.youmind.com/media/1775284646771_562xee_HE_q2kXaoAQiUfr.jpg)

```
A high-end aesthetic lifestyle photo of a young woman standing on a bright white sand beach with a clear turquoise ocean and soft blue sky in the background, use reference image face and preserve identity strictly, do not change facial features, proportions, skin tone, or expression, maintain exact likeness.
Outfit: minimal summer outfit featuring a soft light-toned crop top and a flowy short skirt, lightweight fabric, clean and elegant style.
Pose: natural confident stance, holding a smartphone casually in one hand, relaxed posture, direct gaze toward camera.
Lighting: bright natural daylight, soft sunlight evenly illuminating skin, clean highlights, no harsh shadows, slightly diffused light for smooth skin tones.
Environment: tropical beach setting with clear horizon line, calm ocean, minimal distractions, soft shadows from nearby elements (like tree leaves) lightly visible on sand.
Camera: eye-level shot, 50mm lens, sharp focus on subject, shallow depth of field, background slightly softened but still visible.
Style: ultra realistic, high-fashion summer aesthetic, clean and minimal composition, fresh and airy mood, Instagram/editorial style.
Quality: 8k, HDR, photorealistic, high detail, natural skin texture, crisp clarity.
```

[[Identity Preservation]] [[Confident Pose]] [[Bright Natural Light]]

---

### 11. iPhone 户外自然光摄影

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-03  **Language**: en

> 一个高度结构化的 JSON 提示词，用于生成一张由 iPhone 17 Pro 拍摄的超写实、抓拍风格户外照片。该提示词强调保留参考图像中的精确面部特征、强烈的自然阳光，以及在阳光明媚的路边场景中呈现真实、随意的生活方式美感。

![iPhone 户外自然光摄影](https://cms-assets.youmind.com/media/1775284639562_4f5g5m_HE_Y4LbasAEupDO.jpg)
![iPhone 户外自然光摄影](https://cms-assets.youmind.com/media/1775284639634_pc6o4l_HE_Y3daaEAAjB6Z.jpg)
![iPhone 户外自然光摄影](https://cms-assets.youmind.com/media/1775284639774_tzhg4h_HE_Y40jaUAAhP2q.jpg)

```
{
  "meta": {
    "camera": "iPhone 17 Pro",
    "lens": "24mm wide",
    "aspect_ratio": "9:16",
    "quality": "ultra photorealistic, 8K, HDR",
    "style": "iphone outdoor photography, natural sunlight, slight grain, real-life candid look"
  },

  "subject": {
    "identity": "use reference image face",
    "identity_lock": "strictly preserve exact facial features, proportions, skin tone, eye color, and hair color from reference image, no changes",

    "expression": "natural smile, friendly, relaxed confidence",
    
    "skin": "realistic skin texture, visible pores, slight sun highlights, no over-smoothing",
    
    "hair": {
      "style": "soft natural waves",
      "behavior": "slight movement from outdoor breeze, realistic strands"
    },

    "body": {
      "type": "natural proportions",
      "details": "relaxed posture, realistic anatomy"
    }
  },

  "scene": {
    "location": "sunny roadside with palm trees",
    "environment": "open street, light traffic, tropical vibe, clear blue sky with clouds",
    "details": "restaurant-style outdoor setting, signboard in background, casual environment",
    "atmosphere": "bright, warm, everyday real-life moment"
  },

  "lighting": {
    "main": "direct sunlight",
    "effect": "strong highlights, natural shadows, slightly harsh contrast, realistic outdoor exposure"
  },

  "camera": {
    "perspective": "casual iphone shot",
    "angle": "eye-level slightly tilted",
    "framing": "mid-body shot",
    "imperfection": "slight overexposure in highlights, natural shadow fall, handheld feel"
  },

  "pose": {
    "body": "standing relaxed",
    "arms": "one hand resting on hip, other hanging naturally",
    "head": "slightly tilted with direct gaze"
  },

  "outfit": {
    "top": "fitted white long-sleeve top with logo detail",
    "bottom": "bright orange shorts",
    "details": "clean, sporty casual look"
  },

  "vibe": {
    "energy": "friendly, confident, approachable",
    "mood": "sunny day, casual lifestyle",
    "realism": "feels like a real outdoor photo taken on iphone"
  }
}
```

[[Identity Preservation]] [[Lifestyle Photography]] [[Candid Photography]] [[Strong Natural Sunlight]]

---

### 12. 身着红色礼服的电影感影棚肖像

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-03  **Language**: en

> 这是一个为 Nano Banana Pro 设计的详细 JSON 提示词，旨在生成超写实、电影感的影棚肖像。该提示词要求基于参考图像进行严格的身份锁定，主体身着优雅的露肩红色缎面礼服，斜倚在地板上，背景为无缝暖米色，并利用柔和的定向影棚灯光营造出奢华的杂志大片质感。

![身着红色礼服的电影感影棚肖像](https://cms-assets.youmind.com/media/1775284648071_3peeww_HE_RL-1aEAE6C48.jpg)
![身着红色礼服的电影感影棚肖像](https://cms-assets.youmind.com/media/1775284648049_jrxqfq_HE_RN1YbIAALJc3.jpg)
![身着红色礼服的电影感影棚肖像](https://cms-assets.youmind.com/media/1775284648342_g7xopm_HE_RM1EaQAAZwSu.jpg)
![身着红色礼服的电影感影棚肖像](https://cms-assets.youmind.com/media/1775284648890_j196r1_HE_ROoiaEAAjH24.jpg)

```
{
  "meta": {
    "camera": "iPhone 17 Pro",
    "lens": "24mm wide",
    "aspect_ratio": "16:9",
    "quality": "ultra photorealistic, 8K, HDR",
    "style": "cinematic studio photography, warm tones, soft grain, high-end editorial look"
  },

  "subject": {
    "identity": "use reference image face",
    "identity_lock": "strictly preserve exact facial features, bone structure, proportions, skin tone, eye color, and hair color from reference image, no changes",

    "expression": "calm, confident, slightly intense gaze, relaxed lips",
    
    "skin": "natural skin texture, soft highlights, realistic tone, no over-smoothing",
    
    "hair": {
      "style": "sleek, straight or softly styled back",
      "behavior": "controlled, clean, minimal flyaways"
    },

    "body": {
      "type": "natural proportions",
      "details": "elegant posture, realistic anatomy, no exaggeration"
    }
  },

  "scene": {
    "location": "minimal studio with seamless warm beige backdrop",
    "environment": "clean empty space, no distractions, smooth floor blending into background",
    "atmosphere": "luxury editorial, calm and powerful"
  },

  "lighting": {
    "main": "soft directional studio light from side",
    "effect": "warm golden tones, gentle shadow gradients, subtle contrast, soft highlight on skin and fabric folds"
  },

  "camera": {
    "perspective": "editorial fashion",
    "angle": "slightly low angle",
    "framing": "wide horizontal composition",
    "focus": "sharp on subject, soft falloff on background"
  },

  "pose": {
    "body": "reclined on floor with upper body slightly raised",
    "legs": "extended to side in relaxed position",
    "arms": "one arm supporting body, other resting naturally",
    "head": "upright with direct gaze toward camera"
  },

  "outfit": {
    "dress": "elegant off-shoulder red gown with structured bodice and voluminous sleeves",
    "fabric": "soft matte satin with natural folds and weight",
    "details": "rich color depth, subtle texture, premium finish"
  },

  "vibe": {
    "energy": "powerful, composed, luxurious",
    "mood": "cinematic elegance, quiet dominance",
    "realism": "feels like a high-end fashion campaign shot"
  }
}
```

[[Identity Preservation]] [[Luxury Fashion Editorial]] [[Floor Pose]]

---

### 13. 具有身份锁定功能的 8K 风格化数字肖像

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-04-03  **Language**: en

> 一个用于创建 8K 风格化数字肖像插画的 Nano Banana 2 高细节提示词。该提示词要求基于上传的图片保持严格的身份准确性，并详细指定了面部细节、发型、服装（格子夹克）、构图（头部和肩部、居中）、光照（柔和的定向光）以及带有醒目橙色背景方块的半写实绘画风格。

![具有身份锁定功能的 8K 风格化数字肖像](https://cms-assets.youmind.com/media/1775284643702_b9k37h_HE_KUWBWoAABmbP.jpg)
![具有身份锁定功能的 8K 风格化数字肖像](https://cms-assets.youmind.com/media/1775284643842_binzj6_HE_KUcRaEAA1jpZ.jpg)
![具有身份锁定功能的 8K 风格化数字肖像](https://cms-assets.youmind.com/media/1775284643977_et5fjy_HE_KUfrbcAAvyUj.jpg)
![具有身份锁定功能的 8K 风格化数字肖像](https://cms-assets.youmind.com/media/1775284644901_zc1d90_HE_KUe4aUAAEK4R.jpg)

```
Create an 8k high-detail stylized digital portrait illustration of a person with a slightly happy, gently uplifted expression, maintaining realistic facial structure and natural imperfections, captured at an eye-level camera angle with the subject looking directly into the camera.
Use the uploaded image as the primary identity reference.
Face Accuracy (Critical)
Match the face with 100% identity accuracy. Preserve exact facial structure, bone anatomy, grooming details, jawline, cheekbones, and forehead proportions.
Subject & Expression:
The person has natural eyes with visible iris details. His face shows noticeable forehead lines. His expression feels subtly warm and introspective, with a faint, relaxed softness around the eyes and a very slight, natural hint of a smile — not exaggerated, just a mild uplift in mood while preserving realism.
Hair:
Natural-length, natural colour hair, slightly naturally messy, with textured strands highlighted in lighter colour tones to add depth and volume.
Outfit:
He wears a dark green and brown plaid (tartan) jacket with a loose, painterly pattern. Underneath is a muted beige/tan button-down shirt with a neatly tucked collar. The clothing should feel grounded, simple, and slightly worn.
Composition & Framing (IMPORTANT):
Head-and-shoulders portrait only (no full body)
Subject perfectly centered in the frame
Shoulders must NOT touch the edges — maintain clean breathing space
Bottom of the artwork should fade into a soft, rough, painterly edge (subtle cut-out feel)
Negative space below the portrait to draw focus upward to the face
Background:
Minimal cream background. Behind the head, place a bold orange square with slightly rough, painterly edges to create contrast and a halo-like framing effect.
Lighting:
Soft directional lighting from the upper left, creating gentle highlights on the forehead, nose bridge, and cheek, with subtle shadows on the opposite side to enhance facial structure and depth.
Style & Rendering:
Semi-realistic illustration blending editorial portrait art and graphic novel style
Strong sketch-like linework with expressive strokes
Visible textured brushwork and painterly shading
Dry brush effects, especially around the shoulders, where the image softly dissolves
Natural skin texture with varied tones (subtle reds, neutral hues, faint bluish undertones for stubble effect)
No beautification — preserve raw realism and imperfections
Quality Tags:
ultra-detailed, 8k high resolution, sharp focus, textured brush strokes, cinematic portrait, centered composition, premium illustration style
Aspect ratio 4:5
```

[[Identity Preservation]] [[8K Resolution]]

---

### 14. 保持参考图一致性的电影级影棚肖像

**Author**: [Harboris](https://x.com/harboriis)  **Date**: 2026-04-03  **Language**: en

> 这是一份针对 Nano Banana Pro 的详细提示词，要求模型在生成身着特定服装、处于特定场景下的年轻男性电影级影棚肖像时，必须保持上传参考图中的面部、发型和胡须完全一致。

![保持参考图一致性的电影级影棚肖像](https://cms-assets.youmind.com/media/1775284626699_r1hwlz_HE-ttQWa0AAob8w.jpg)

```
Use The Uploaded Reference Photo As The Model For The Face, Hairstyle, And Beard, Keeping Them Exactly As In The Reference. Render A Cinematic Studio Portrait Of A Young Man With A Sporty Body Sitting Casually On A Futuristic, Minimalistic, Designer Chair, Legs Crossed. Outfit: Brown Suit (#483c32 Jacket And Pants), Black Shirt Under The Jacket, Dark Brown Loafers, Black Oneplus Watch 346mm On Left Wrist. Background: Solid #483c32 With A Large White Circle Behind The Head, Filled And Slightly Glowing. Lighting: Bright Soft Studio Light, Producing Sharp Shadows And Moody Atmosphere. Pose: Relaxed, Slightly Leaning, One Hand On The Chair's Backrest, Face Turned To The Side. Ultra-detailed, Photo Realistic, Cinematic Contrast, Fabric Texture Emphasized. Ensure The Hairstyle, Beard, And Face Remain Exactly As In The Uploaded Reference Photo.
```

[[Identity Preservation]] [[Cinematic Lighting]] [[Costume Portrait]]

---

### 15. 在埃菲尔铁塔附近遮阳的女性旅行抓拍

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-03  **Language**: en

> 一份详细的 JSON 提示词，用于生成一张逼真的旅行抓拍照片，主角为特定年轻女性（通过参考图锁定身份），她站在埃菲尔铁塔附近的户外，正用手遮挡正午强烈的阳光。

![在埃菲尔铁塔附近遮阳的女性旅行抓拍](https://cms-assets.youmind.com/media/1775284634015_4z27c7_HE-KMHJagAEXCJ7.jpg)
![在埃菲尔铁塔附近遮阳的女性旅行抓拍](https://cms-assets.youmind.com/media/1775284634031_agkvsa_HE-KKnFa0AAQ8kd.jpg)
![在埃菲尔铁塔附近遮阳的女性旅行抓拍](https://cms-assets.youmind.com/media/1775284634031_noxcwf_HE-KLNOaYAAavDK.jpg)
![在埃菲尔铁塔附近遮阳的女性旅行抓拍](https://cms-assets.youmind.com/media/1775284634887_gql6a9_HE-KM_WbQAAARcn.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman standing outdoors near the Eiffel Tower in daylight, shielding eyes with hand, Use uploaded reference image, keep identity exact",
      "identity_lock": "STRICT — Use uploaded reference image, keep identity exact. No facial or feature changes.",
      "pose": {
        "body_position": "standing upright",
        "torso": "slightly angled",
        "arms": "one hand raised shading eyes, one holding bag strap",
        "hands": "relaxed, natural",
        "head": "slightly tilted",
        "gaze": "toward camera",
        "expression": "neutral, composed"
      }
    },
    "face_details": {
      "instruction": "Use uploaded reference image, keep identity exact",
      "skin": "natural texture, slight sunlit warmth",
      "eyes": "soft daylight reflections",
      "lips": "natural matte finish",
      "imperfections": "subtle skin variation"
    },
    "hair": {
      "instruction": "Use uploaded reference image, keep identity exact",
      "style": "long dark hair, loose",
      "details": "natural strands, slight movement",
      "lighting_interaction": "warm sunlight highlights"
    },
    "attire": {
      "outfit": {
        "top": "black sleeveless fitted top with side ties",
        "bottom": "beige mini skirt with utility pockets",
        "accessories": "black shoulder bag, sunglasses on head"
      },
      "fabric_behavior": "natural folds, fitted textures",
      "realism": "true fabric detail"
    },
    "body_details": {
      "anatomy": "natural proportions",
      "lighting_effects": "strong sunlight shadows",
      "skin_interaction": "warm highlights, soft contrast"
    },
    "environment": {
      "setting": "Paris outdoor viewpoint",
      "background": {
        "elements": "Eiffel Tower, cityscape, greenery, stone railing",
        "lighting": "bright midday sun",
        "depth": "deep and clear"
      }
    },
    "lighting": {
      "type": "natural sunlight",
      "direction": "top/front",
      "behavior": "bright with defined shadows",
      "imperfections": "slight overexposed highlights",
      "color_temperature": "warm daylight"
    },
    "camera": {
      "type": "smartphone",
      "lens": "wide",
      "angle": "eye-level",
      "distance": "full-body",
      "focus": "sharp",
      "depth_of_field": "deep",
      "imperfections": "minor noise"
    },
    "composition": {
      "framing": "vertical full-body",
      "balance": "subject centered with landmark",
      "realism": "travel candid style"
    },
    "quality": {
      "resolution": "high",
      "detail": "realistic textures",
      "rendering": "photorealistic"
    },
    "consistency_controls": {
      "guidance_scale": 7.5,
      "steps": 35
    },
    "negative_prompt": [
      "altered identity",
      "beautified skin",
      "cgi look",
      "cartoon",
```

[[Identity Preservation]] [[Travel Photography]] [[Outdoor Portrait]]

---

### 16. 具有戏剧性分割光效的超写实产品摄影

**Author**: [Muhammad Ali](https://x.com/I_Muhammadali44)  **Date**: 2026-04-03  **Language**: en

> 这是一个用于生成超写实电影感人像的提示词，专注于产品植入，特别是高端能量饮料。它要求保留参考图像中的原始面部特征，并使用深色极简背景下的戏剧性分割光效，以呈现奢华的商业广告风格。

![具有戏剧性分割光效的超写实产品摄影](https://cms-assets.youmind.com/media/1775284639987_9dxcej_HE-A_QvbgAAEk-g.jpg)

```
"Ultra-realistic cinematic portrait (keep original face). Subject holding a premium energy drink labeled “AI Talks” toward the camera. Dramatic split lighting, dark minimal background with circular spotlight. Clean formal outfit, sharp focus, glossy high-end can, cool cinematic color grading, luxury commercial style."
```

[[Identity Preservation]] [[Dark Minimalist Background]]

---

### 17. 现代室内环境中人物的写实生活照

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-04-03  **Language**: en

> 一个用于生成写实生活照的提示词，画面主体为特定人物（通过参考图锁定身份），身处现代室内居住空间，身着灰色紧身连体衣，场景由自然光照亮。

![现代室内环境中人物的写实生活照](https://cms-assets.youmind.com/media/1775284630227_rsnk0q_HE9_517bEAAgJ8j.jpg)
![现代室内环境中人物的写实生活照](https://cms-assets.youmind.com/media/1775284630290_viufir_HE9_52SagAATTbR.jpg)
![现代室内环境中人物的写实生活照](https://cms-assets.youmind.com/media/1775284630556_pwx9ek_HE9_51uaoAEqWhR.jpg)
![现代室内环境中人物的写实生活照](https://cms-assets.youmind.com/media/1775284631515_su7d0g_HE9_52QbcAAVt4M.jpg)

```
Use the provided reference image for the subject’s identity, face, body proportions, hair, and overall likeness. Do not change the subject’s appearance.

The subject is standing front-facing in a modern indoor residential space, leaning the right hand against a white doorframe while the left arm rests naturally at the side.

She is wearing a tight-fitting sleeveless grey marl bodysuit made of thin jersey fabric, featuring spaghetti straps and a rounded scoop neckline. Accessories include a thin gold chain bracelet with a black four-leaf clover charm on the right wrist, and two stacked thin gold bangles on the left wrist.

The environment features a white paneled door with a circular satin-nickel handle, white walls, and a clean modern interior. The floor is light-toned hardwood or laminate. In the background, there is a large potted green plant near a window, a grey and white patterned area rug, a stainless steel cylindrical bin or container, and a large mirror or archway visible further back.

Lighting is abundant natural daylight coming from a side window, creating soft, diffused shadows and bright, even illumination.

Medium shot (mid-thigh to head), eye-level, straight-on angle. Portrait orientation (4:5). Sharp focus on the subject with a shallow depth of field softly blurring the background. Neutral color palette dominated by whites, greys, natural wood tones, and touches of green. Photorealistic, high-resolution lifestyle image.
```

[[Identity Preservation]] [[Natural Light]] [[Modern Interior]] [[Casual Portrait]]

---

### 18. 高级时尚超现实棋盘大片

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-04-03  **Language**: en

> 一份详细的提示词，用于生成一张以特定年轻女性（通过参考图锁定身份）为主角的高级时尚概念摄影作品，场景置于超现实的棋盘环境中，配有超大号的亮面粉色和白色棋子，采用柔和的摄影棚光影及马卡龙色调。

![高级时尚超现实棋盘大片](https://cms-assets.youmind.com/media/1775284633670_tdr9cb_HE98QFdasAAoElk.jpg)
![高级时尚超现实棋盘大片](https://cms-assets.youmind.com/media/1775284633703_xpcphv_HE98Qr6aEAABb3k.jpg)
![高级时尚超现实棋盘大片](https://cms-assets.youmind.com/media/1775284633716_jr75mq_HE98RMhaEAA-Wul.jpg)

```
A high-fashion conceptual lifestyle photograph of a young woman placed inside a surreal chessboard environment.
Use the provided reference image for the face and identity — strictly preserve exact facial structure, proportions, skin tone, eye color, and hair color. Do not alter identity, expression, or realism.
The scene features a large-scale black-and-white checkered floor resembling a chessboard, surrounded by oversized glossy chess pieces in soft pink and white tones. The chess pieces are tall, smooth, and reflective, creating a surreal, dreamlike atmosphere.
The woman is positioned slightly bent forward in a natural, interactive pose, gently touching or moving a large pink chess piece, as if engaged in a strategic moment. Her posture feels candid yet intentional.
Outfit: a soft pastel pink leather jacket layered over a clean white top, paired with a delicate, flowy white tulle skirt. Light pink heels complement the outfit, maintaining a cohesive monochrome aesthetic.
Hair & Styling: natural tied-back hairstyle with loose strands, soft makeup, clean and elegant look.
Lighting: soft studio lighting with diffused highlights, subtle reflections on glossy chess pieces, balanced shadows, high-end editorial lighting style.
Camera: top-down angled perspective (slightly elevated), 50mm lens, sharp focus on subject, geometric composition emphasizing symmetry and scale, background clean and controlled.
Style: high-fashion editorial, surreal luxury aesthetic, minimal yet bold composition, pastel color grading, Instagram-worthy artistic direction.
Quality: 8K, HDR, ultra-realistic, highly detailed textures, smooth skin tones, crisp focus, no distortion.
```

[[Identity Preservation]] [[Pastel Color Palette]]

---

### 19. 尴尬的 NFT 叠罗汉全家福

**Author**: [Edizkan ⭕🦇](https://x.com/edizkan_)  **Date**: 2026-04-03  **Language**: en

> 这是一个复杂且结构化的提示词，旨在生成一张刻意营造尴尬、俏皮感的摄影棚全家福。通过将上传的角色（NFT）强行组合成“不自然且略显局促的人体堆叠”，同时严格保留其原始特征与比例。

![尴尬的 NFT 叠罗汉全家福](https://cms-assets.youmind.com/media/1775284630106_bqzj2n_HE9Gt2ybcAA8Qh6.jpg)

```
A deliberately awkward and playful studio family portrait featuring uploaded characters.  The composition must recreate the feeling of an unnatural, slightly uncomfortable human stack — similar to classic awkward family portraits where people are leaning, sitting on each other, or balancing in strange but stable ways.  ---  🔒 IDENTITY LOCK (CRITICAL)  Each character must strictly preserve: • original AKCB proportions (large head, short limbs) • eye shape, spacing, stylization • balaclava fully covering nose and mouth (never visible) • original materials, textures, and colors  All characters must remain equal in scale. No size drift. No realism increase.  ---  🧱 STRUCTURE SYSTEM — “AWKWARD STACK LOGIC” (CORE)  The group must form a **stacked or interlocked structure** using their bodies.  Use combinations like: • one character acting as a base (lying or crouched) • one sitting sideways on another’s back or legs • one perched or kneeling on top • one leaning awkwardly across others for balance • limbs used as support points (shoulders, knees, backs)  The pose should feel: • slightly uncomfortable   • physically questionable but still believable   • intentionally staged and awkward    Avoid clean posing. Avoid symmetry.  ---  ⚖️ BALANCE RULE (IMPORTANT)  Even though the pose is silly: • the structure must feel physically possible   • weight distribution must make sense   • characters must visibly support each other    No floating. No broken physics.  ---  😐 EXPRESSION & BODY LANGUAGE  • neutral or mildly serious expressions (contrast with silly pose) • relaxed faces, awkward bodies • no exaggerated cartoon acting  ---  📸 STUDIO STYLE  • classic portrait studio background (gray / muted color / soft gradient) • soft even lighting • subtle shadows grounding each character • clean, slightly outdated family photo aesthetic  ---  🎯 COMPOSITION  • full body of all characters visible • clear stacking hierarchy (bottom → middle → top) • no messy overlaps hiding faces  ---  🚫 NEGATIVE CONSTRAINTS  • no extra limbs   • no merging of characters   • no pose duplication   • no symmetry   • no action poses (this is static portrait energy)   • no extreme exaggeration    ---  ✨ VARIATION ENGINE  Each generation must create a DIFFERENT awkward stacked pose using the same logic.  Examples of variation: • pyramid stack • sideways bench stack • diagonal leaning tower • tangled sitting cluster • “one person is clearly struggling” composition
ar 1:1
```

[[Identity Preservation]]

---

### 20. 海滩时尚男士电影感竖版拼贴画

**Author**: [Mr Das](https://x.com/MrDasOnX)  **Date**: 2026-04-03  **Language**: en

> 这是一个用于 Google Gemini Nano Banana 2 的提示词，旨在创作一张电影感的三格竖版拼贴画，展示一位在黄金时刻宁静海滩上的时尚年轻男子。提示词详细说明了姿势、服装（大地色亚麻衬衫）、光影（温暖且富有情绪感）以及高级时尚杂志的审美风格，并要求使用参考照片以保持面部特征一致。

![海滩时尚男士电影感竖版拼贴画](https://cms-assets.youmind.com/media/1775284655413_wibhga_HE88s5pbQAA9yLW.jpg)

```
A cinematic three-panel vertical collage featuring a stylish young man at a serene beach during golden hour. In the top panel, he is sitting on the sand with one knee up, resting his arm on it, gazing down thoughtfully as waves approach. In the middle panel, he stands facing the ocean with one hand running through his hair, shirt slightly flowing in the breeze, capturing a candid emotional moment. In the bottom panel, he is captured from a low-angle front shot, adjusting his dark sunglasses while looking toward the horizon with a confident, calm expression. He is wearing a crisp, earth-toned beige linen button-down shirt. The lighting is warm and moody with a soft teal-and-orange color grade, subtle film grain texture, and high-fashion editorial aesthetic. 4K resolution, hyper-realistic, emotional atmosphere, cinematic film still, 100% same face as reference photo, vertical 9:16 composition, slightly zoomed-in framing.
```

[[Identity Preservation]]

---

### 21. 具有夸张鱼眼畸变效果的高级时尚大片

**Author**: [Harboris](https://x.com/harboriis)  **Date**: 2026-04-03  **Language**: en

> 一个用于生成年轻男性高级时尚大片的提示词，采用夸张的鱼眼镜头特写。画面构图大胆，背景为纯橙色，展现 Z 世代夏季时尚，并要求模型保持参考照片中的面部特征。

![具有夸张鱼眼畸变效果的高级时尚大片](https://cms-assets.youmind.com/media/1775284635525_k0ulcl_HE8yPYkaoAAInrd.jpg)

```
Create a A high-fashion editorial image of a young man, of the person from the uploaded character reference photo. KEEP FACE FEATURES AS ORIGINAL at all times. A high-fashion editorial image captured in an exaggerated fisheye lens close-up. The camera is angled slightly from below, and the man is crouching or squatting forward with both hands resting on his knees, leaning his upper body toward the lens. His face is looking downward into the camera, exaggerated by fisheye distortion so it appears large and rounded, with cartoonish proportions. He has a neutral smile, relaxed and completely smile, expression confident but emotionless.

He wears a trendy, summery knitted shirt in a pastel green shade light, breathable, with visible texture, reflecting Gen Z summer fashion. He also wears oversized black-framed sunglasses, with lenses tinted in light green.

The background is a clean, solid orange color with soft, realistic studio lighting, creating gentle shadows cast from his head, shoulders, and arms.

No direct sunlight light is controlled and evenly diffused, like a fashion set. The overall style is playful, surreal, and modern, inspired by 2025 Gen Z fashion culture and bold editorial covers. Ultra-clean details, slight grain, bold composition.
```

[[Identity Preservation]] [[Male Portrait]]

---

### 22. 极简卧室中的镜面自拍，搭配鲜艳服饰

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-04-02  **Language**: en

> 这是为 Nano Banana 2 编写的详细提示词，需要提供一张参考图以确定主体身份。它能生成一张现代极简风格卧室的写实镜面自拍，重点突出主体鲜艳的黄色和紫红色服饰与中性白/米色环境之间的强烈色彩对比。

![极简卧室中的镜面自拍，搭配鲜艳服饰](https://cms-assets.youmind.com/media/1775198514131_jzzy9a_HE64K9Mb0AAmDsZ.jpg)
![极简卧室中的镜面自拍，搭配鲜艳服饰](https://cms-assets.youmind.com/media/1775198514138_rsayv5_HE64K9XbgAA0jWt.jpg)
![极简卧室中的镜面自拍，搭配鲜艳服饰](https://cms-assets.youmind.com/media/1775198514203_fjtdcd_HE64K88bEAAeE3s.jpg)
![极简卧室中的镜面自拍，搭配鲜艳服饰](https://cms-assets.youmind.com/media/1775198514856_b5yl8g_HE64LCxakAAoP18.jpg)

```
Use the provided reference image for the subject’s identity, face, body proportions, hair, and overall likeness. Do not change the subject’s appearance.

Mirror selfie in a bright, modern minimalist bedroom. The subject is wearing a fitted lemon-yellow spaghetti strap tank top with a scoop neckline, paired with tight-fitting fuchsia-pink cotton mini shorts. Accessories include a delicate gold chain necklace with a small circular pendant, a thin gold chain bracelet on the left wrist, and a beaded tan-colored bracelet on the right wrist. She is holding an iPhone with a light blue case decorated with colorful stickers, including a fish and abstract shapes.

The bedroom features plain white matte walls and a low wooden platform bed with a textured beige/tan duvet and soft pink pillows. Above the bed is a large rectangular abstract canvas painting in deep indigo blue.

The floor is light grey carpet partially covered by a large ornate Persian-style rug in deep red with black and cream geometric patterns. Additional elements include white curtains on a window to the far left, a black hard-shell equipment case on the floor, a discarded pink garment and a dark grey shirt lying on the rug, and a white paneled interior door on the right side.

Lighting is natural daylight coming from a side window, creating soft shadows and bright, even illumination.

Mirror selfie, medium full-body shot, portrait orientation (4:5 aspect ratio). High-resolution, photorealistic lifestyle image with strong color contrast between vibrant clothing, deep-toned decor, and neutral white surroundings.
```

[[Identity Preservation]] [[Lifestyle Photography]]

---

### 23. Sydney Sweeney 镜面自拍，呈现特定美学风格

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2026-04-02  **Language**: en

> 这是一个为 Nano Banana 2 设计的高细节图像生成提示词，旨在指导模型创作一张 Sydney Sweeney 的全身镜面自拍，在保留其外貌特征的同时，身穿特定的粉色连体裤，背景设定为现代、整洁且拥有柔和自然光的卧室。

![Sydney Sweeney 镜面自拍，呈现特定美学风格](https://cms-assets.youmind.com/media/1775198517344_embffe_HE6hL1aasAQHKjX.jpg)

```
Use the provided reference image for the subject’s identity, facial features, body proportions, hair, and overall likeness. Preserve the exact face, skin tone, and realism from the reference image without alteration.

The subject is taking a full-body mirror selfie, standing upright and facing forward at eye level. She is holding a modern smartphone with a {argument name="phone case color" default="light pink"} case in a selfie position, looking into the phone screen with a neutral expression and a subtle soft pout.

She is wearing a light pink one-piece sleeveless romper or bodysuit featuring a scoop neckline, a fitted bodice, and a tiered double-layered ruffled skirt hem, reflecting a coquette/balletcore aesthetic. Footwear consists of white pointed-toe high-heeled pumps with a glossy finish. Accessories include a single-strand white pearl necklace and a thin gold band ring on the right hand.

The setting is a modern, clean bedroom. Visible furniture includes a white six-drawer dresser with silver handles, topped with assorted cosmetic bottles, a tall black spray bottle, and small vanity items. A grey upholstered bed is present with a textured chunky-knit cream throw blanket. A standard white wall-mounted radiator is also visible.

The floor is covered with neutral grey carpeting. Wall décor includes a framed photo collage poster with pink and white imagery. In the foreground, part of a large mirror with an ornate silver or pewter frame is visible, framing the composition.

Lighting is bright, soft natural daylight coming from the side, creating gentle highlights and shadows.

Full-body mirror selfie, portrait orientation (9:16 aspect ratio), eye-level, front-facing composition. High-resolution, photorealistic lifestyle aesthetic with a soft color palette of whites, greys, and pastel pink tones.
```

[[Identity Preservation]] [[Natural Light]] [[Celebrity Lookalike]]

---

### 24. 具有动态模糊和数字伪影的超写实 iPhone 人像摄影

**Author**: [Chryz leen](https://x.com/Chryzleenprompt)  **Date**: 2026-04-02  **Language**: en

> 这是一个为 Gemini Nano Banana 设计的复杂超写实图像生成提示词，需要使用参考图来确定角色外观。提示词详细描述了一个特定场景：身穿夏日连衣裙的主体手持瓶子，背景为蓝天下的棕榈叶，并以 iPhone 15 Pro 的清晰度、动态模糊和低保真数字伪影进行渲染。

![具有动态模糊和数字伪影的超写实 iPhone 人像摄影](https://cms-assets.youmind.com/media/1775198511285_5bfd4z_HE6TldEa8AACkgP.jpg)

```
Create image: Use the attached reference image as a visual guide for the character’s appearance. Preserve key visual traits such as facial structure and overall proportions, while allowing small natural variations typical of real photography. The generated subject should clearly resemble the reference while remaining a natural photographic interpretation.
A hyper-realistic, ultra-sharp photograph taken on a modern iPhone 15 Pro, characterized by its digital clarity and bright HDR rendering. The subject is captured in a dynamic low-angle pose, leaning forward toward the lens while holding a small glass bottle with a yellow label containing a light-colored liquid. The person wears a dark-toned summer sundress featuring a delicate pattern of small white and yellow daisies and thin spaghetti straps, complemented by a minimalist silver pendant necklace. The hair is styled in long, voluminous dark waves swept over one shoulder and adorned with a white floral accessory. The composition is framed by vibrant green palm fronds against a vast, cloudless, bright blue sky, with the entire scene rendered in sharp focus. The lighting is bright and even, typical of modern smartphone photography, lifting all shadows to reveal realistic, dewy skin textures with visible pores. A powerful and authentic motion blur effect is applied to the hand holding the bottle to create a sense of candid, energetic action, while the entire image incorporates a low-fidelity compression look with authentic early digital artifacts and slight pixelation. The makeup aesthetic features a soft coral-toned blush, subtle dark eyeliner techniques, and a soft-edged reddish-pink lip color with a satin finish.
Aspect Ratio: 3:4

Negative:
extra limbs, extra hands, extra fingers, missing fingers, fused fingers, dislocated hands, broken wrists, unnatural hand pose, twisted arms, duplicated body parts, bad anatomy, incorrect anatomy, broken anatomy, impossible pose, warped body, distorted proportions, ai artifacts, poorly drawn hands, malformed anatomy
```

[[Identity Preservation]]

---

### 25. 2x2 高端礼帽广告大片网格

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-04-02  **Language**: en

> 这是一个为 Nano Banana 2 (Pro) 设计的复杂 JSON 提示词，旨在生成用于高端礼帽广告的 2x2 编辑网格。该提示词在保持上传参考图人物特征的同时，通过四种不同的场景（黄金时刻、室内奢华、日落余晖、夜间造型）变换光影、氛围、角度和环境。模特必须始终佩戴白色高端宽檐帽，并身着优雅的白色服装。

![2x2 高端礼帽广告大片网格](https://cms-assets.youmind.com/media/1775198505448_oc1jhh_HE5_H9xXAAAJIhz.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "2x2_editorial_grid_storytelling",
      "version": "v1.1_LUXURY_HAT_CAMPAIGN_WHITE_OUTFIT",
      "style": "ultra_realistic_high_fashion"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "maximum",
      "preserve_identity": true,
      "notes": "Use the uploaded woman and hat as the base identity. Create a cohesive 2x2 grid with four cinematic editorial variations while keeping her facial features consistent. The woman must wear an elegant white outfit in all four frames."
    },
    "grid": {
      "layout": "2x2",
      "consistency": "same model, same hat, same identity, same white outfit",
      "variation": "lighting, mood, angle, environment"
    },
    "frames": [
      {
        "position": "top_left",
        "scene": "golden hour sunlight portrait",
        "lighting": "soft warm sunlight casting shadow of hat details",
        "mood": "elegant, calm, luxury",
        "camera": "close-up, shallow depth of field",
        "details": "white outfit softly illuminated with refined couture texture"
      },
      {
        "position": "top_right",
        "scene": "indoor luxury editorial",
        "lighting": "soft diffused window light",
        "mood": "minimal, high fashion magazine",
        "details": "focus on hat texture, crystals, and elegant white outfit details"
      },
      {
        "position": "bottom_left",
        "scene": "sunset glow with stronger contrast",
        "lighting": "dramatic golden light + shadows",
        "mood": "sensual, bold, cinematic",
        "details": "skin glow, glossy highlights, white outfit catching warm sunset tones"
      },
      {
        "position": "bottom_right",
        "scene": "night luxury look",
        "lighting": "spotlight + subtle sparkle reflections on crystals",
        "mood": "mysterious, premium, high-end campaign",
        "details": "crystals catching light, darker background, elegant white outfit accents remaining visible"
      }
    ],
    "styling": {
      "hat": "white luxury wide-brim hat with crystal embellishments",
      "outfit": "elegant white couture outfit, refined, feminine, luxurious, harmonious with the hat",
      "makeup": "natural glam, warm tones",
      "skin": "luminous, realistic texture",
      "hair": "soft, slightly hidden under hat"
    },
    "cinematography": {
      "camera": "ARRI Alexa Mini LF",
      "lens": "85mm portrait lens",
      "aperture": "f/1.8",
      "depth_of_field": "shallow"
    },
    "color_grading": {
      "palette": "warm ivory, gold, soft beige, pearl white",
      "style": "luxury editorial film",
      "grain": "subtle"
    },
    "quality": {
      "resolution": "8K",
      "realism": "extreme",
      "details": "perfect skin texture, crystal clarity, white outfit texture, no distortion"
    },
    "negative_prompt": [
      "different face"
```

[[Identity Preservation]] [[2x2 Grid Layout]]

---

### 26. 鼠尾草绿草地上的电影感肖像

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-04-02  **Language**: en

> 一份用于 Gemini Nano Banana Pro 的提示词，旨在生成 3:4 比例的电影编辑风格肖像。要求使用上传的图片以确保人物身份和服装完全一致，将主体置于广阔的鼠尾草绿草地中，伴随强风，营造出一种带有胶片摄影美感和明显颗粒感的内省与忧郁氛围。

![鼠尾草绿草地上的电影感肖像](https://cms-assets.youmind.com/media/1775198506564_poxgxc_HE5f4vvaYAArri-.jpg)
![鼠尾草绿草地上的电影感肖像](https://cms-assets.youmind.com/media/1775198506583_zuetx0_HE5f4vvbAAA4rQN.jpg)

```
Create a cinematic editorial-style portrait in a 3:4 aspect ratio, with an atmospheric mood. Use the attached image as the exact reference for the subject’s face and identity, ensuring a perfect match. The subject (male or female) stands alone in the middle of a vast sage-green grass field, swept by strong winds. Tall grass surrounds the subject entirely, moving like ocean waves, partially obscuring the body and creating a sense of motion, depth, and isolation. The subject is wearing the exact same outfit as in the reference image.

The hair appears slightly messy, naturally blown by the wind. The head is tilted slightly downward, with the gaze directed toward the ground, conveying a quiet, introspective, and melancholic mood. The facial expression is neutral, distant, and emotionally controlled. Compose the frame with the subject slightly off-center, using a slightly elevated camera angle. There should be no visible horizon only layers of grass filling the frame. Use muted natural tones such as sage green, deep olive green, and soft whites.

Shoot in vertical 3:4 format using a telephoto lens with shallow depth of field. Frame the image in a cinematic style with a film photography aesthetic, including noticeable grain, soft edges, atmospheric lighting, and motion blur in the grass caused by wind. The overall tone should feel poetic, calm, and introspective, with high detail while maintaining a natural look. Magazine-cover quality, with no text or watermarks.
```

[[Identity Preservation]] [[Introspective Mood]] [[Film Photography Aesthetic]] [[Editorial Style]]

---

### 27. 由切片果蔬重构的角色

**Author**: [Edizkan ⭕🦇](https://x.com/edizkan_)  **Date**: 2026-04-01  **Language**: en

> 这是一个为 Nano Banana Pro 设计的详细提示词，旨在将上传的角色参考图转换为完全由层叠、切片果蔬构成的逼真 3D 渲染图。在确保所有材质（包括鞋履）均由果蔬切片构成的前提下，精准保留原角色的比例、色彩和特征。

![由切片果蔬重构的角色](https://cms-assets.youmind.com/media/1775112279816_ougqwk_HE2DyO3WwAAhQtr.jpg)

```
create a version of this character made entirely of sliced vegetables and fruits vegetables and fruits: should match the uploaded character’s colors as closely as possible, without changing their natural look slices: slightly misaligned, with visible separation between layers structure: a small bite taken out of the top of the head, forming a clean cut surface ambience: kitchen setting, on a cutting board with scattered vegetables and a knife nearby camera: slightly top-down angle effect: tilt-shift  Likeness Preservation (CRITICAL): Maintain exact proportions, eye shape, spacing, stylization, silhouette, and material identity from the reference Do not humanize Do not reinterpret anatomy Do not modify facial structure Identity must remain perfectly intact and instantly recognizable Character Compatibility Rules: If the uploaded character is 2D, convert it into a believable realistic 3D render while preserving the original design, proportions, colors, and visual identity Do not modify facial structure  Do not add a mouth or nose if the uploaded character does not have them  👟 FOOTWEAR & ACCESSORY MATERIAL OVERRIDE (CRITICAL FIX) All parts of the character, including footwear and clothing, must follow the same fruit and vegetable slice construction. • shoes must be made entirely of stacked fruit and vegetable slices  • preserve the exact shoe shape, proportions, and design  • recreate panels, sole, and details using layered slices Material examples for shoes: • sole → dense stacked potato or root vegetable slices  • upper panels → fruit/vegetable slices arranged to match original color blocking  • edges and seams → visible slice layering and separation 📷⚠️ 0px; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px;"> IMPORTANT:  No original materials should remain (no fabric, rubber, or leather).  Everything must be converted into fruit/vegetable slice construction while keeping the original design recognizable. ar 1:1
```

[[Identity Preservation]] [[3D Rendering]] [[Character Transformation]]

---

### 28. 极致湿润特写肖像

**Author**: [Melis✨](https://x.com/miilesus)  **Date**: 2026-04-01  **Language**: en

> 这是一个用于 Nano Banana 2 的提示词，旨在生成一张年轻女性侧脸的极致特写肖像，强调紧贴皮肤的湿发以及逼真的闪亮水珠/汗珠。重点在于明亮自然的双眼，配合柔和的灯光和冷色调的背景虚化效果，需要参考图以保持面部特征。

![极致湿润特写肖像](https://cms-assets.youmind.com/media/1775112272204_hawx03_HE1v8NjXcAAMcD3.jpg)

```
Extreme wet close-up portrait. Young woman's face in profile (use uploaded pictures for proper reference) Dark wet hair naturally glued to the skin. Fine droplets of water and thin sweat glistening realistically on her face. Focus on bright natural {argument name="eye color" default="green/hazel"} eyes with realistic reflection avoid excessive shine. Moist and shiny lips, soft natural texture. Soft lighting and cool shades with a light grey/white bokeh background colour. Keep same facial features
```

[[Identity Preservation]] [[Water Droplets]]

---

### 29. 前卫雕塑感织物肖像

**Author**: [Sarah](https://x.com/AIwithSarah_)  **Date**: 2026-04-01  **Language**: en

> 这是一个用于生成前卫时尚肖像的高细节提示词，要求模型锁定上传参考图的面部特征。画面主体为被大量、褶皱感极强的祖母绿雕塑感织物包裹头部与躯干的人物，背景为极简主义摄影棚。

![前卫雕塑感织物肖像](https://cms-assets.youmind.com/media/1775112276969_7nag66_HE0YlGPaQAAH-QG.jpg)
![前卫雕塑感织物肖像](https://cms-assets.youmind.com/media/1775112276992_pkc0sq_HE0Yk7JaUAA8Qj4.jpg)

```
Prompt: Preserve their real facial features, bone structure, eye shape, nose shape, lips, and overall facial identity - the face must clearly match the uploaded person. Do not alter age, ethnicity, or facial proportions. Reference image required, face identity lock. A close-up portrait of an uploaded person subject, their torso and head enveloped in massive, voluminous, sculptural fabric folds. The subject faces forward, head tilted slightly downward, looking up directly into the lens with a direct gaze, relaxed jaw, subtly parted lips, and slight tension in lower eyelids. They are surrounded and partially obscured by sweeping layers of structural fabric, which is stiff yet lightweight, intensely pleated and crinkled, holding structural arches, deep crevices, and sweeping folds around them. A few loose strands of hair escape the fabric wrap, resting flat against the cheek. Makeup features a matte, unreflective skin texture. The setting is a minimalist studio with a plain off-white background. The face is framed within an aperture of fabric, offset slightly to the right with negative space on the left. The camera is at eye-level, creating an architectural framing using textile volumes. Soft, directional studio light comes from camera-left, creating gradient shadows within the fabric crevices and gentle modeling on the right side of the face. The mood is sculptural, serene, and editorial. The color palette features deep {argument name="fabric color" default="emerald green"} for the fabric, off-white for the background, and natural skin tones, with high color contrast between the green fabric and light background, and soft tonal contrast on the face. Photographed with a medium format digital camera and an 85mm lens at f/5.6. The face and foreground fabric are sharply in focus, with slight blurring on the furthest background folds. The style is avant-garde editorial portraiture, photorealistic, with minimal film grain. No CGI, no cartoon, no Al glow. Full color.
```

[[Identity Preservation]] [[Minimalist Studio Background]] [[Haute Couture Portrait]]

---

### 30. Nano Banana Pro 超写实肖像提示词

**Author**: [Jessia](https://x.com/itsjessiababy)  **Date**: 2026-04-01  **Language**: en

> 这是一个为 Nano Banana Pro 模型设计的结构化高精度提示词，旨在生成一张年轻女性的超高角度特写照片，通过明确的身体特征、服装、环境和光照条件，实现极致的写实感与解剖学真实度。

![Nano Banana Pro 超写实肖像提示词](https://cms-assets.youmind.com/media/1775112289701_jz6ij1_HE0B2gma4AAEOe7.jpg)

```
{
"subject": "Young woman with a tanned complexion, exhibiting natural skin texture with subtle pores and micro-imperfections. She has dark hair slightly visible on the right edge of her face. She is wearing a dark charcoal-grey, lightly ribbed plunge bra with double spaghetti straps. Her chest is highly prominent, featuring full, heavy breast mass naturally affected by gravity, deep cleavage, and significant forward and outward projection that visibly exceeds the depth of her ribcage. Her waist is slim beneath the bust. She wears a silver snake-chain bracelet with round charms on her right wrist, and a silver ring with a prominent pale stone or pearl on her right ring finger. Her right hand grasps the handle of a large, light pink ceramic mug adorned with a white silhouette graphic of a child reaching up, which is pressed against her mouth as if drinking.",
"pose": "Right arm is bent sharply upward and inward, holding the mug directly to her lips. The left arm is extended forward and slightly downward out of frame, indicating a selfie-taking posture. Her shoulders are slightly hunched forward, and her torso leans into the camera. Her head is tilted slightly upward, with her gaze directed toward the camera lens. Her spine has a natural forward curve typical of a seated or leaning forward position.",
"environment": "Casual indoor bedroom setting. Below the subject are soft, crumpled white bedsheets. Behind her left shoulder rests a decorative pillow featuring a repeating geometric and floral pattern in teal, grey, and white. The background consists of a plain, slightly out-of-focus, muted grey-blue wall.",
"camera": "Extreme high-angle, close-up perspective. The camera is positioned slightly above the subject's head, looking down at a steep angle, emphasizing the depth and volume of the torso and chest in the foreground. Strong three-dimensional depth with the chest dominating the mid-foreground.",
"lighting": "Soft, natural, diffused daylight originating primarily from the left side of the frame. This creates smooth, natural highlights on the left shoulder, chest, and the mug, while casting soft, realistic shadows on the right side of the body, the right side of the face, and deeply within the cleavage. Natural subsurface scattering is visible on the skin.",
"mood_and_expression": "Candid, relaxed, and intimate. A casual, unposed morning atmosphere. Her expression is neutral but focused, with large dark eyes making direct contact with the lens.",
"style_and_realism": "Raw, candid mobile photography. Unedited with no beauty filters, airbrushing, or artificial smoothing. Strict anatomical fidelity with highly realistic soft tissue behavior, subtle asymmetry, and natural gravity. Very slight image noise typical of a smartphone front-facing camera in natural indoor light.",
"colors_and_tone": "Warm, natural skin tones contrasting with the cool, muted grey-blue of the background wall. The "}
```

[[Identity Preservation]] [[Natural Lighting]] [[Anatomical Accuracy]]

---

### 31. Nano Banana Pro 双人肖像提示词

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-31  **Language**: en

> 为 Nano Banana Pro 设计的结构化 JSON 提示词，用于生成两位年轻女性在花园环境中的生活化肖像。强调基于上传参考图的严格身份锁定、柔和的浅色系服装以及自然光效果。

![Nano Banana Pro 双人肖像提示词](https://cms-assets.youmind.com/media/1775026356601_xhc1x5_HEwx5xaagAAphTX.jpg)
![Nano Banana Pro 双人肖像提示词](https://cms-assets.youmind.com/media/1775026356582_uoo7jq_HEwx5M1aAAAfurK.jpg)
![Nano Banana Pro 双人肖像提示词](https://cms-assets.youmind.com/media/1775026356632_y1vplw_HEwx6ckbUAEhSwG.jpg)
![Nano Banana Pro 双人肖像提示词](https://cms-assets.youmind.com/media/1775026357256_bq8ri2_HEwx7Pba4AAZ621.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "{argument name="subject description" default="two young women standing outdoors together in a garden setting, smiling and posing side by side, wearing soft pastel dresses, Use uploaded reference image, keep identity exact"}",
      "identity_lock": "STRICT — Use uploaded reference image, keep identity exact. Preserve both faces, hair, eyes, proportions. Do not alter identity.",
      "pose": {
        "type": "standing duo pose",
        "body_position": "standing close together with arms lightly around each other",
        "interaction": "friendly and relaxed posture",
        "head": "both slightly tilted toward each other, facing camera"
      }
    },
    "face_details": {
      "instruction": "Use uploaded reference image, keep identity exact",
      "expression": "soft natural smiles",
      "skin": "natural skin tones with gentle sunlight glow",
      "eyes": "looking toward camera with warm expressions",
      "clarity": "both faces sharp and clearly visible",
      "focus_priority": "maximum facial clarity for both subjects"
    },
    "hair": {
      "instruction": "Preserve hairstyles exactly",
      "style": "one with blonde loose waves, one with long straight brunette hair",
      "details": "natural movement and shine"
    },
    "clothing": {
      "outfit": "{argument name="outfit" default="pastel dresses, one light yellow sleeveless dress and one light blue fitted dress with structured bodice"}",
      "details": "soft spring aesthetic, light fabrics",
      "accessories": "minimal jewelry, subtle name tags"
    },
    "environment": {
      "setting": "garden or park",
      "background": "large tree, greenery, flowers, pathway, soft natural landscape",
      "props": "natural outdoor elements only",
      "atmosphere": "bright spring day, fresh and airy"
    },
    "lighting": {
      "type": "natural sunlight",
      "quality": "soft diffused daylight",
      "direction": "front natural light illuminating faces evenly",
      "effect": "enhances skin tones and pastel colors",
      "imperfections": "slight natural shadowing from outdoor light"
    },
    "camera": {
      "type": "portrait photography",
      "lens": "50mm lens",
      "angle": "eye-level",
      "distance": "medium shot with slight zoom",
      "focus": "sharp focus on both faces",
      "depth": "moderate depth of field with slightly blurred background",
      "zoom": "slight zoom to ensure both faces are clearly visible",
      "imperfections": "natural handheld realism"
    },
    "composition": {
      "style": "lifestyle portrait",
      "framing": "both subjects centered in frame",
      "balance": "symmetrical composition with natural background framing"
    },
    "effects": {
      "color_tone": "soft pastel tones with warm highlights",
      "finish": "clean, bright, natural look"
    },
    "quality
```

[[Identity Preservation]] [[Lifestyle Photography]] [[Female Portrait]] [[Soft Natural Light]]

---

### 32. 基于参考图生成超写实肖像

**Author**: [Ali](https://x.com/Oye___Ali)  **Date**: 2026-03-31  **Language**: en

> 这是一个为 Nano Banana Pro 设计的提示词，旨在引导其使用提供的图像作为参考，创作出超写实的摄影级肖像，并严格保持原人物的面部特征、身份、比例以及自然的皮肤纹理。

![基于参考图生成超写实肖像](https://cms-assets.youmind.com/media/1775026344182_oelzb5_HEv9_MRWkAA6gtA.jpg)

```
Use the image as a reference and create an ultra-realistic photographic portrait without modifying the face or hair of the person in the reference photo, fully maintaining the original facial features, identity, facial proportions,natural skin texture
```

[[Identity Preservation]] [[Natural Skin Texture]] [[Photorealistic Portrait]]

---

### 33. 春日樱花人像复刻提示词

**Author**: [Puneet Kharbanda](https://x.com/KPuneet20)  **Date**: 2026-03-31  **Language**: en

> 一个 Nano Banana 摄影提示词，用于在公园樱花背景下复刻一张年轻女性的春日人像。要求 100% 精确保留参考图的面部特征，并使用柔和的自然光、浅景深以及暖色调处理。

![春日樱花人像复刻提示词](https://cms-assets.youmind.com/media/1775026353963_0big21_HEtHAecWAAABd1V.jpg)

```
Recreate a springtime portrait similar to the reference image. A young woman stands in a park surrounded by blooming cherry blossom trees, holding a branch of pink flowers. Ensure the facial features of the young woman are 100% exact to the reference image; do not alter the face. Use soft, diffused natural light, as if taken on an overcast day or during golden hour. Employ a medium telephoto lens (50-85mm) with an aperture around f/2.8 to f/4 to achieve a shallow depth of field. The subject should be in the lower center of the frame, with the blossoms framing the top and sides. Capture a calm, serene, and fresh atmosphere, emphasizing the beauty of spring. Apply subtle post-processing to enhance brightness, contrast, and color saturation, with a warm color grading and slightly desaturated tones. The final image should be high-quality and authentic, avoiding overly stylized effects.
```

[[Identity Preservation]] [[Shallow Depth Of Field]] [[Female Portrait]] [[Natural Light Portrait]]

---

### 34. 现代生活方式镜面自拍

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-03-30  **Language**: en

> 为 Nano Banana Pro 提供的详细提示词，旨在生成一张超写实、具有时尚摄影美感的镜面自拍。主体（严格保留参考图中的身份）随意地坐在高层公寓的抛光混凝土地面上，身穿亮面黑色抹胸和牛仔裤。

![现代生活方式镜面自拍](https://cms-assets.youmind.com/media/1774939631241_44o9xw_HErKMWCb0AEHH47.jpg)
![现代生活方式镜面自拍](https://cms-assets.youmind.com/media/1774939631180_qqhkid_HErKLMmbUAAyGkW.jpg)
![现代生活方式镜面自拍](https://cms-assets.youmind.com/media/1774939631218_o6s0fp_HErKMW6bcAA9jL5.jpg)

```
Ultra-realistic 4:5 modern lifestyle mirror selfie with a fashion photography aesthetic. Use the reference image for the subject’s identity, face, and hair — preserve exact facial features, proportions, and likeness.

The subject is sitting casually on the floor, taking a mirror selfie. Her right arm is extended behind her with her palm flat on the floor for support, while her left hand holds a smartphone near her face. Her right leg is bent inward on the floor, and her left leg is raised with the foot flat on the ground.

She is wearing a glossy black strapless tube top made of a reflective material (latex or faux leather), paired with medium-wash blue denim jeans in a relaxed fit. She also wears black pointed-toe stiletto ankle boots.

The setting is an empty modern high-rise apartment or office space. The floor is smooth, light grey polished concrete with subtle reflections, and the walls are plain white. A large floor mirror is visible along the right edge of the frame.

In the background, three tall rectangular windows with metallic frames reveal a bright daytime cityscape with glass skyscrapers and a clear blue sky.

Lighting is bright natural daylight streaming in from the windows, creating soft backlighting, gentle shadows on the floor, and even illumination on the subject.

High detail, sharp focus, realistic textures, clean modern aesthetic, shallow depth of field.
```

[[Identity Preservation]] [[Mirror Selfie]] [[Fashion Lifestyle Photography]]

---

### 35. 桥上时尚生活方式美学照片

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-30  **Language**: en

> 为 Nano Banana 2 提供的详细提示词，旨在创作一张超写实、具有 Instagram 美学风格的生活方式照片：一位年轻女性（严格保留参考图像中的身份）站在现代白色桥梁上，正值黄金时刻，身穿柔软的粉色缎面连衣裙和宽松的白色衬衫。

![桥上时尚生活方式美学照片](https://cms-assets.youmind.com/media/1774939628075_p53zar_HEruzZUaYAAgnDm.jpg)
![桥上时尚生活方式美学照片](https://cms-assets.youmind.com/media/1774939628061_x3x7ut_HErux2pbgAAUIM4.jpg)
![桥上时尚生活方式美学照片](https://cms-assets.youmind.com/media/1774939628064_gj6co8_HEruxFdbEAAMrcK.jpg)

```
A trendy aesthetic lifestyle photo of a young woman standing outdoors on a modern white bridge with elegant architectural details, use reference image face and preserve identity strictly, do not change facial features, proportions, skin tone, or expression, maintain exact likeness.
Outfit: soft satin pink dress with a silky texture, slightly reflective fabric, elegant and fitted style, paired with a loose white shirt falling off the shoulders.
Pose: relaxed and confident pose, leaning slightly against the railing, natural body posture, soft expression.
Environment: clean white bridge with decorative railings, soft evening sky, warm ambient lighting, subtle city buildings and greenery in the background, string lights above creating a cozy aesthetic vibe.
Lighting: soft golden hour lighting mixed with cool evening tones, smooth skin highlights, natural shadows, cinematic color grading.
Camera: slightly angled eye-level shot, 50mm lens, shallow depth of field, sharp focus on subject, background softly blurred (bokeh).
Style: ultra realistic, Instagram aesthetic, soft luxury vibe, clean composition, high-end lifestyle photography.
Quality: 8k, HDR, photorealistic, high detail, natural skin texture, sharp focus.
```

[[Identity Preservation]] [[Instagram Aesthetic]] [[Golden Hour Portrait]] [[Pink Satin Dress]]

---

### 36. 公园喷泉与帆船的生活方式摄影

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-30  **Language**: en

> 为 Nano Banana Pro 准备的详细 JSON 提示词，用于生成一张年轻女性（严格保留参考图中的身份）在公园喷泉旁与微型帆船俏皮互动的抓拍生活方式图片，采用柔和温暖的日光拍摄，并具有浅景深效果。

![公园喷泉与帆船的生活方式摄影](https://cms-assets.youmind.com/media/1774939630795_e6l1p1_HErj8UcaoAAgOdZ.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "young woman standing by a park fountain, leaning forward playfully interacting with small sailboats in the water, Use uploaded reference image, keep identity exact",
      "identity_lock": "STRICT — Use uploaded reference image, keep identity exact. Preserve face, hair, eyes, proportions. Do not alter identity.",
      "pose": {
        "type": "candid lifestyle pose",
        "body_position": "standing, slightly bent forward at the waist, one arm extended toward water",
        "interaction": "holding a small stick touching a miniature sailboat",
        "head": "tilted slightly downward with natural smile"
      }
    },
    "face_details": {
      "instruction": "Use uploaded reference image, keep identity exact",
      "expression": "genuine soft smile, relaxed and joyful",
      "skin": "natural skin texture with realistic imperfections",
      "eyes": "focused downward toward object, natural expression",
      "clarity": "face sharp and clearly visible",
      "focus_priority": "high facial clarity with slight background blur"
    },
    "hair": {
      "instruction": "Preserve hairstyle exactly",
      "style": "loose natural hair falling over shoulders",
      "details": "slight natural movement from outdoor breeze"
    },
    "clothing": {
      "outfit": "grey sleeveless fitted top paired with a light floral mini skirt",
      "accessories": "small black handbag with short strap",
      "footwear": "black low-heeled shoes",
      "details": "casual chic summer outfit"
    },
    "environment": {
      "setting": "elegant outdoor park with fountain and pond",
      "background": "water fountain, trees with warm autumn tones, people softly blurred in distance",
      "props": "mini sailboats floating on water",
      "atmosphere": "peaceful, sunny afternoon park scene"
    },
    "lighting": {
      "type": "natural sunlight",
      "quality": "soft warm daylight",
      "direction": "side/front lighting",
      "effect": "gentle highlights on skin and hair, soft shadows",
      "imperfections": "slight natural contrast and light falloff"
    },
    "camera": {
      "type": "lifestyle photography",
      "lens": "50mm lens",
      "angle": "slightly above waist-level angled perspective",
      "distance": "medium full-body shot",
      "focus": "sharp on subject",
      "depth": "shallow depth of field with blurred background",
      "zoom": "slight zoom for better face visibility",
      "imperfections": "natural grain and realistic softness"
    },
    "composition": {
      "style": "editorial lifestyle",
      "framing": "subject centered slightly to side with fountain behind",
      "balance": "foreground subject with background elements creating depth"
    },
    "effects": {
      "color_tone": "warm natural tones with soft greens and browns",
      "finish":
```

[[Identity Preservation]] [[Shallow Depth Of Field]] [[Female Portrait]] [[Candid Lifestyle Photography]]

---

### 37. 黑白大头贴表情网格

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-30  **Language**: en

> 一份为 Nano Banana 2 准备的详细 JSON 提示词，用于生成 4x4 黑白大头贴网格，展示特定成年女性身份的 16 种不同面部表情，强调高身份还原度与经典大头贴美学。

![黑白大头贴表情网格](https://cms-assets.youmind.com/media/1774939626796_7odwnx_HErcNsBbMAAqm_h.jpg)

```
{
 "generation_request": {
 "meta_data": {
 "task_type": "black_and_white_photobooth_expression_grid_4x4",
 "language": "en",
 "priority": "highest",
 "version": "v1.0_BW_PHOTOBOOTH_EXPRESSIONS_4X4"
 },
 "input": {
 "mode": "image_to_image",
 "reference_image_usage": "very_high",
 "preserve_identity": true,
 "preserve_facial_features": true,
 "preserve_hairstyle": true,
 "notes": "Use the reference as the primary anchor. Create a black-and-white photobooth-style expression grid. Keep the same adult woman identity and hair. Each panel should show a different facial expression. Minimal background, direct photobooth flash look, natural skin texture."
 },
 "output": {
 "aspect_ratio": "1:1",
 "resolution": "ultra_high",
 "num_images": 1,
 "layout": {
 "type": "grid",
 "rows": 4,
 "cols": 4,
 "gutter": "thin",
 "panel_consistency": "high"
 },
 "sharpness": "crisp_photobooth",
 "grain": "subtle_analog_bw"
 },
 "scene": {
 "concept": "classic photobooth contact sheet with expressive faces",
 "environment": "plain neutral backdrop, no props",
 "lighting": {
 "style": "direct photobooth flash",
 "key_light": "front flash, slightly hard but flattering",
 "shadows": "soft short shadows behind subject",
 "avoid": "cinematic side light, dramatic backgrounds"
 },
 "camera": {
 "lens": "50mm",
 "distance": "tight head-and-shoulders framing",
 "focus": "eyes sharp in every panel"
 }
 },
 "subject": {
 "type": "adult woman",
 "wardrobe": "simple strapless or bare-shoulder photobooth look (no logos)",
 "hair": "keep same hairstyle across all panels",
 "makeup": "minimal, natural",
 "anatomy_rules": "correct facial proportions, no warped eyes/mouth"
 },
 "expression_set": {
 "panel_01": "scrunched smile, eyes squeezed slightly",
 "panel_02": "intense stare with fingers framing eyes",
 "panel_03": "big laugh, mouth open, joyful",
 "panel_04": "bored / unimpressed face, chin in hands",
 "panel_05": "sad pout, watery eyes look",
 "panel_06": "goofy face with both hands making small horns above head",
 "panel_07": "playful tongue out, cheeky grin",
 "panel_08": "angry glare, eyebrows down",
 "panel_09": "flirty look, hand touching cheek",
 "panel_10": "surprised wide eyes, mouth slightly open",
 "panel_11": "fake scream / excited shout, hands near face",
 "panel_12": "mischievous grin with claw-like hand pose",
 "panel_13": "confused frown, lips pressed",
 "panel_14": "crying face, hands on head, dramatic",
 "panel_15": "tongue out with eyes closed, playful",
 "panel_16": "duck face with small devil horns gesture"
 },
 "style": {
 "color": "pure black and white",
 "contrast": "medium-high",
 "background": "flat gray",
 "finish": "slight photobooth grain, clean edges"
 },
 "quality_control": {
 "identity_lock": "strict",
 "hands_priority": "high",
 "avoid": [
 "extra fingers",
 "missing fingers",
 "deformed hands",
 "warped face",
 "uneven eyes",
 "melted mouth",
 "plastic skin",
 "text",
 "watermark",
 "logo"
 ]
 },
 "negative_
```

[[Identity Preservation]]

---

### 38. 沙漠路边通话生活照

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-30  **Language**: en

> 为 Nano Banana Pro 提供的详细 JSON 提示词，用于生成一张写实风格的生活照。画面中一位女性（严格保持参考图中的人物特征）正倚靠在沙漠场景的电线杆旁接听电话，呈现出正午强烈的阳光感，身着特定的格子连衣裙。

![沙漠路边通话生活照](https://cms-assets.youmind.com/media/1774939627320_a11fah_HErVbUzasAAgNDV.jpg)
![沙漠路边通话生活照](https://cms-assets.youmind.com/media/1774939627319_wdqytg_HErVaoobIAAgT7Q.jpg)
![沙漠路边通话生活照](https://cms-assets.youmind.com/media/1774939627426_jgf53f_HErVZ4KaQAAy_Ae.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "woman leaning against a wooden utility pole in a desert roadside setting, holding a phone to her ear, Use uploaded reference image, keep identity exact",
      "identity_lock": "STRICT — Use uploaded reference image, keep identity exact. Preserve face, hair, eyes, proportions. Do not alter identity.",
      "pose": {
        "type": "casual leaning pose",
        "body_position": "leaning one shoulder against wooden pole",
        "legs": "one leg slightly bent, relaxed stance",
        "arms": "one hand holding phone to ear, other lightly touching face",
        "head": "tilted slightly downward with soft expression"
      }
    },
    "face_details": {
      "instruction": "Use uploaded reference image, keep identity exact",
      "expression": "soft, dreamy, slightly distracted expression",
      "skin": "natural skin texture with sunlit glow",
      "eyes": "partially closed or relaxed gaze",
      "clarity": "face must be sharp and clearly visible"
    },
    "hair": {
      "instruction": "Preserve hairstyle exactly",
      "style": "long blonde hair",
      "details": "soft waves, slightly wind-blown"
    },
    "clothing": {
      "outfit": "casual feminine summer style",
      "dress": "short red and white gingham dress with lace trim",
      "shoes": "brown cowboy boots",
      "details": "light fabric with natural folds and movement"
    },
    "props": {
      "phone": "black smartphone held to ear",
      "pole": "wooden utility pole with small posted paper sign"
    },
    "environment": {
      "setting": "desert roadside",
      "background": "dry dirt road, sparse vegetation, distant house and van",
      "details": "dusty ground, warm earthy tones, open landscape"
    },
    "lighting": {
      "type": "natural sunlight",
      "quality": "bright harsh midday light",
      "direction": "top-front sunlight",
      "effect": "strong shadows, warm highlights on skin",
      "imperfections": "slight overexposure in highlights, natural contrast"
    },
    "camera": {
      "type": "lifestyle photography",
      "lens": "50mm",
      "angle": "eye-level",
      "focus": "sharp focus on subject",
      "depth": "moderate depth of field with slightly softened background",
      "imperfections": "minor lens distortion, natural grain"
    },
    "composition": {
      "style": "editorial lifestyle",
      "framing": "full body centered with pole vertical line",
      "balance": "subject foreground with open desert background"
    },
    "quality": {
      "resolution": "ultra high",
      "rendering": "photorealistic",
      "details": "high detail in fabric texture, skin, and environment"
    },
    "negative_prompt": [
      "different face",
      "identity change",
      "blurry face",
      "low resolu
```

[[Identity Preservation]]

---

### 39. 动态黑色亮片派对场景

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-30  **Language**: en

> 一个用于 Nano Banana Pro 的高细节 JSON 提示词，旨在生成一张单帧、全身的女性在昏暗高端夜店跳舞的图像，重点在于保持人物特征、动态姿势、黑色亮片服装以及电影级的低光效果。

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "nightlife_disco_woman_single_frame_dance",
      "version": "v1.0_BLACK_GLITTER_PARTY_SINGLE_DANCE"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "face_similarity_priority": "high",
      "notes": "Use the uploaded woman as inspiration for identity, vibe, movement, and styling. Create one single full-body frame of the same woman dancing in a natural candid nightlife moment. She should look glamorous, energetic, and real, with hair flying beautifully in motion."
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "resolution_target": "ultra_high_res",
      "num_images": 1
    },

    "scene": {
      "environment": "dimly lit luxury bar or nightclub with warm amber lights, blurred crowd, soft bokeh highlights",
      "lighting": "low light cinematic, warm orange tones mixed with soft flash highlights, slight motion blur glow",
      "mood": "fun, flirty, energetic, carefree, high-end nightlife"
    },

    "character": {
      "count": 1,
      "consistency": "same woman",
      "styling": {
        "hair": "long natural hair flying dramatically with dancing movement, voluminous and elegant",
        "makeup": "glowy skin, soft glam, slightly glossy lips",
        "outfit": "black glitter strappy mini dress or fitted black glitter party dress, subtle sparkle catching light",
        "accessories": "minimal jewelry"
      }
    },

    "pose_and_action": {
      "pose": "full-body dancing pose, dynamic body line, one leg slightly forward or bent naturally, expressive elegant arm movement",
      "action": "mid-dance moment with hair swinging in motion",
      "expression": "confident, joyful, magnetic, natural nightlife energy"
    },

    "camera": {
      "lens": "35mm or 50mm cinematic lens",
      "framing": "full-body portrait",
      "focus": "face and body readable, motion preserved naturally",
      "depth_of_field": "shallow with strong background bokeh",
      "motion_effect": "natural motion blur in hair and slight body movement, not distorted"
    },

    "materials_and_effects": {
      "fabric": "black glitter fabric reflecting light subtly, not overexposed",
      "skin": "natural glow with slight sweat-like shine",
      "light_effects": "bokeh lights, soft flash hits, ambient glow",
      "grain": "light film grain for nightlife realism"
    },

    "quality_controls": {
      "no_identity_mix": true,
      "no_body_distortion": true,
      "no_extra_limbs": true,
      "no_face_glitch": true,
      "no_overflash": true,
      "no_heavy_noise": true,
      "realism": "cinematic_party"
    },

    "negative_prompt": [
      "grid layout",
      "multiple women",
      "identity drift",
      "extra limbs",
      "bad anatomy",
      "frozen pose",
```

[[Identity Preservation]] [[Cinematic Lighting]] [[Dynamic Pose]] [[Low Light Photography]]

---

### 40. 风吹草地上的电影感编辑人像

**Author**: [Saul Goodman](https://x.com/Goodmanprotocol)  **Date**: 2026-03-30  **Language**: en

> 一个用于 Gemini Nano Banana 2 的提示词，旨在创作一张电影感、氛围浓厚的编辑人像，描绘一个人独自站在广阔、风吹过的鼠尾草绿草地中，需要附带照片以进行精确的面部和身份参考。

![风吹草地上的电影感编辑人像](https://cms-assets.youmind.com/media/1774939637423_jsvm9b_HEqfsoqb0AADRpg.jpg)
![风吹草地上的电影感编辑人像](https://cms-assets.youmind.com/media/1774939637418_8em47n_HEqfsnabYAEzt9k.jpg)

```
Create a 3:4 cinematic, atmospheric editorial portrait using the attached photo as the exact face and identity reference. A solitary man/woman stands alone in the middle of vast, wind-swept sage green grass fields. Tall grass surrounds the subject completely, flowing in strong currents like ocean waves, partially obscuring the body and creating motion,depth, and solitude. The subject wears a simple, loose white shirt that softly contrasts with the rich green landscape.
Dark hair is slightly messy, with natural strands moving in the wind. The head is gently tilted downward, eyes cast toward the ground, conveying a quiet, introspective, melancholic mood. Expression is calm, distant, and emotionally restrained. Compose the frame slightly off-center, from a subtle elevated angle. No visible horizon, the frame is fully immersed in grass texture. Use a muted natural palette of sage green, deep olive, and soft off-white. Shoot vertical 3:4, telephoto perspective, shallow depth of field, cinematic framing. Film photography aesthetic with visible grain, soft edge falloff, atmospheric light, wind-driven motion blur in the grass. Quiet, poetic storytelling; ultra-detailed yet natural, magazine-cover editorial quality. No text, no watermark.
```

[[Identity Preservation]] [[Editorial Photography]]

---

### 41. 穿着学院风制服的严格身份锁定镜面自拍

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-30  **Language**: en

> 一份为 Nano Banana Pro 准备的详细 JSON 提示词，用于生成一位年轻女性穿着学院风制服的写实镜面自拍，要求基于上传的参考图进行严格的身份锁定。

![穿着学院风制服的严格身份锁定镜面自拍](https://cms-assets.youmind.com/media/1774939635876_r8tvpa_HEqSeq-aYAAHlKK.jpg)
![穿着学院风制服的严格身份锁定镜面自拍](https://cms-assets.youmind.com/media/1774939635885_qjgre6_HEqSfO9akAALWr3.jpg)
![穿着学院风制服的严格身份锁定镜面自拍](https://cms-assets.youmind.com/media/1774939635911_ju4ix8_HEqSfxJawAESN7G.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "young woman taking a mirror selfie in a bedroom, Use uploaded reference image, keep identity exact",
      "identity_lock": "STRICT — Use uploaded reference image, keep identity exact. Preserve face, hair, eyes, proportions. Do not alter identity.",
      "pose": {
        "type": "mirror selfie pose",
        "body_position": "standing upright facing mirror",
        "legs": "slightly together with relaxed stance",
        "arms": "one hand holding phone in front of face, other hand resting on hip",
        "head": "slightly tilted with soft smile toward mirror"
      }
    },
    "face_details": {
      "instruction": "Use uploaded reference image, keep identity exact",
      "expression": "soft confident smile",
      "skin": "natural texture with slight indoor lighting softness",
      "eyes": "looking at phone screen reflection",
      "clarity": "face must be sharp and realistic even through mirror"
    },
    "hair": {
      "instruction": "Preserve hairstyle exactly",
      "style": "blonde wavy hair",
      "details": "soft curls with volume, natural shine"
    },
    "clothing": {
      "outfit": "preppy school-inspired outfit",
      "top": "black cardigan over white collared shirt with tie",
      "bottom": "blue plaid skirt",
      "accessories": "heart-shaped belt buckle",
      "shoes": "black glossy shoes with white socks",
      "details": "clean, neat styling"
    },
    "props": {
      "phone": "smartphone with decorative case and charm",
      "mirror": "full-length mirror with subtle rainbow edge reflection",
      "background_items": "dresser and TV screen visible behind subject"
    },
    "environment": {
      "setting": "modern bedroom",
      "lighting": "soft indoor daylight",
      "details": "neutral walls, carpet floor, minimal clutter"
    },
    "lighting": {
      "type": "natural indoor lighting",
      "quality": "soft and even",
      "effect": "clean, slightly warm tones",
      "imperfections": "minor shadow falloff and reflection artifacts from mirror"
    },
    "camera": {
      "type": "smartphone selfie camera",
      "lens": "standard phone lens",
      "angle": "straight-on mirror angle",
      "focus": "sharp focus on subject reflection",
      "depth": "deep focus",
      "imperfections": "slight noise, realistic phone camera softness"
    },
    "composition": {
      "style": "casual lifestyle selfie",
      "framing": "full body centered in mirror",
      "balance": "subject centered with room elements behind"
    },
    "quality": {
      "resolution": "high",
      "rendering": "photorealistic",
      "details": "clear clothing textures, realistic mirror reflection"
    },
    "negative_prompt": [
      "different face",
      "identity change",
      "blurry face",
      "low quality",
      "distorte
```

[[Identity Preservation]] [[Female Portrait]]

---

### 42. 夜生活时尚大片人像提示词

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-03-30  **Language**: en

> 一份详细的提示词，用于生成超写实 3:4 比例的人像，呈现高对比度的夜生活时尚大片风格。要求精准还原主体特征，并强调在深色虚化城市背景下的直闪摄影效果。

![夜生活时尚大片人像提示词](https://cms-assets.youmind.com/media/1774939624610_hufgrp_HEotHVnbUAARkT3.jpg)
![夜生活时尚大片人像提示词](https://cms-assets.youmind.com/media/1774939624601_f6jtsr_HEotHVmacAAhQhX.jpg)
![夜生活时尚大片人像提示词](https://cms-assets.youmind.com/media/1774939625250_zj20et_HEotHVkaAAAjQMW.jpg)
![夜生活时尚大片人像提示词](https://cms-assets.youmind.com/media/1774939624931_vu4zko_HEotHVwagAATOBS.jpg)

```
Ultra-realistic 3:4 portrait in a high-contrast nightlife editorial style. Use the reference image for the subject’s identity, face, and hair — preserve exact facial features, proportions, and likeness.

The subject is standing slightly angled on an outdoor balcony at night, gently leaning against a metallic railing. Her left hand is raised to touch her hair, while her right hand hangs down holding a small handbag. Her pose feels relaxed, confident, and joyful.

She is wearing a {argument name="dress color" default="light pink"} rhinestone-covered mini dress with spaghetti straps, a low V-neckline, and horizontal ruched draping.

Accessories include a small silver rhinestone hobo handbag, a thick silver rhinestone cuff on the right wrist, a thin silver bracelet on the left wrist, and thick diamond-style hoop earrings. Nails are painted solid white.

The setting is a nighttime balcony with a grey metallic horizontal railing. The background features a deep black sky and out-of-focus illuminated windows of distant high-rise buildings.

Lighting is strong direct camera flash, creating high contrast and making the dress and accessories sparkle intensely against the dark background.

High detail, sharp textures, flash photography aesthetic, cinematic nightlife editorial style, shallow depth of field, crisp focus on the subject.
```

[[Identity Preservation]] [[High Contrast Lighting]] [[Direct Flash]]

---

### 43. 顶层公寓超写实时尚大片

**Author**: [Puneet Kharbanda](https://x.com/KPuneet20)  **Date**: 2026-03-30  **Language**: en

> 这是一个高度具体的提示词，旨在生成一张用户在顶层公寓的超写实时尚大片（要求 100% 保留参考图的面部特征）。内容详细描述了人物的服装（黑色乳胶中长裙）、动作（水晶杯中溢出的香槟）、背景（雨夜城市）以及用于定格瞬间的复杂灯光和相机设置。

![顶层公寓超写实时尚大片](https://cms-assets.youmind.com/media/1774939641641_hjsaj9_HEnn_zCWYAAUUmj.jpg)

```
A hyper-realistic editorial shot of myself, keeping my exact face unchanged. IMPORTANT: Do not alter the face of the reference face; the output must have 100% exact facial features as the reference image. I am standing atop a plush emerald velvet stool in a high-rise penthouse, leaning slightly forward with a playful but sophisticated expression. In my right hand, I hold a vintage crystal flute as champagne overflows in mid-air, capturing every glistening droplet. I am wearing an asymmetrical black latex midi dress with structured, padded shoulders and a wide silver chain-link belt that cinches the waist. The background features floor-to-ceiling glass walls overlooking a rain-slicked city at night, with blurred neon lights creating a vibrant bokeh. The lighting is a mix of cool blue ambient tones from the city and warm, directional gold point lights from the interior chandeliers, creating a luxurious rim light. Shot on a 35mm f/1.4 lens with a fast shutter speed to freeze the liquid motion, ensuring pristine 8k clarity with no artifacts. Ensure the output maintains 100% exact facial features from the reference image; do not alter the face.
```

[[Identity Preservation]] [[Dramatic Lighting]] [[High Fashion Photography]]

---

### 44. Vogue 风格美妆社论肖像

**Author**: [Puneet Kharbanda](https://x.com/KPuneet20)  **Date**: 2026-03-30  **Language**: en

> 一个用于生成引人注目的 Vogue 风格美妆社论肖像的提示词，重点在于大胆的妆容和珠宝。它指定了“蝴蝶光”以突出面部特征，并包含一条关键指令，即保持参考图像的面部特征完全一致。

![Vogue 风格美妆社论肖像](https://cms-assets.youmind.com/media/1774939639110_abgkic_HEnpAMIbYAE_aV2.jpg)

```
A striking beauty editorial portrait, Vogue style close-up. Focus on a model's face featuring bold, graphic eyeliner and exaggerated diamond earrings. The lighting is impeccable "butterfly lighting" (paramount lighting) from above, creating defined cheekbones and a clean jawline. Flawless skin texture, shallow depth of field, medium format photography, luxurious feel. –ar 4:5. IMPORTANT: Do not alter the face of the reference face; the output must have 100% exact facial features as the reference image
```

[[Identity Preservation]] [[Bold Makeup]]

---

### 45. 绿色迪斯科女性时尚大片 9 宫格

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-29  **Language**: en

> 这是一个为 Nano Banana Pro 设计的高结构化提示词，用于生成 3x3 网格拼贴（9 宫格），展示绿色迪斯科风格的女性时尚大片。该提示词强调严格的身份锁定、面部优先，以及在带有绿金色反射的暗色摄影棚环境中呈现特定的姿势变化（如飞吻、眨眼、感性表情等）。

![绿色迪斯科女性时尚大片 9 宫格](https://cms-assets.youmind.com/media/1774853739303_hgnugf_HEmmdfAW0AA95yH.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "green_disco_feminine_editorial_9panel_grid",
      "version": "v4.0_FACE_PRIORITY_KISS_EXPRESSIONS"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "high",
      "preserve_identity": true,
      "face_similarity_priority": "max",
      "notes": "Woman must be the main subject. Background inspired by green disco references but must not overpower the woman."
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "layout": {
        "type": "grid",
        "rows": 3,
        "cols": 3,
        "gutter": "thin",
        "consistency": "strict_identity_lock"
      }
    },

    "scene": {
      "environment": "dark green disco-inspired studio with soft glowing reflections, subtle mirrorball light patterns, cinematic blur",
      "lighting": "soft dreamy glow, green-gold reflections, gentle diffusion, no harsh highlights",
      "mood": "playful, sensual, feminine, retro-glam"
    },

    "character": {
      "count": 1,
      "priority": "face and expression",
      "styling": {
        "hair": "soft styled, slightly voluminous",
        "makeup": "glossy lips, luminous skin, subtle shimmer eyes",
        "outfit": "green or shimmering reflective fabric inspired by disco aesthetic",
        "accessories": "minimal, focus on face"
      }
    },

    "pose_variation": {
      "focus": "face expressions + upper body",
      "poses": [
        "direct eye contact, soft confident look",
        "blowing a kiss toward camera",
        "playful wink with slight smile",
        "hand near lips, sensual expression",
        "head tilted back slightly, soft glow on face",
        "side profile with glossy lips highlighted",
        "eyes half closed, dreamy expression",
        "gentle smile with relaxed shoulders",
        "hero shot, strong gaze into camera"
      ]
    },

    "camera": {
      "lens": "85mm portrait lens",
      "framing": "close-up to mid shot",
      "focus": "sharp on face, soft background",
      "depth_of_field": "shallow",
      "motion_effect": "very subtle blur glow, no distortion"
    },

    "effects": {
      "grain": "soft film grain",
      "glow": "cinematic bloom",
      "reflections": "controlled green disco reflections",
      "sparkle": "minimal, not overpowering face"
    },

    "quality_controls": {
      "no_face_distortion": true,
      "no_extra_limbs": true,
      "no_background_overpower": true,
      "no_heavy_noise": true,
      "no_identity_loss": true,
      "face_priority": "maximum",
      "realism": "high_end_editorial"
    }
  }
}
```

[[Identity Preservation]] [[3x3 Grid Layout]] [[Winking Expression]]

---

### 46. 黑豹主题超写实人像提示词

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-29  **Language**: en

> 这是一份专为 Nano Banana 2 设计的详细提示词，旨在生成一张超写实、奢华杂志风格的人像照片。画面主体为一位年轻女性（使用参考身份），坐在干净的白色摄影棚内，身后有一只黑豹，身着柔粉色缎面束身裙。该提示词强调严格的身份保留及高对比度光影效果。

![黑豹主题超写实人像提示词](https://cms-assets.youmind.com/media/1774853744037_qw09bh_HEmRxmkasAAu3Vo.jpg)
![黑豹主题超写实人像提示词](https://cms-assets.youmind.com/media/1774853744159_chwe0v_HEmRwrEboAAsiTm.jpg)
![黑豹主题超写实人像提示词](https://cms-assets.youmind.com/media/1774853744317_ugh6fc_HEmRyk-a4AACn2j.jpg)

```
A portrait of a young woman sitting in a clean white studio with a black panther behind her, use reference image face, preserve identity strictly, do not change facial features, hair color, or eye color.
Outfit: {argument name="outfit" default="soft pink satin corset dress with feather details, fitted structure, smooth glossy texture"}.
Pose: sitting on the floor with legs folded to the side, hands resting naturally, upright posture.
Expression: calm, confident, serious.
Hair: long black hair, soft waves, sleek finish.
Accessories: minimal, clean look.
Environment: plain white studio background, minimal setup, strong contrast with black panther.
Lighting: soft studio lighting, even exposure, subtle shadows, high contrast between subject and background, sharp details.
Style: ultra realistic, high detail, luxury editorial, clean aesthetic.
```

[[Identity Preservation]] [[High Contrast Lighting]]

---

### 47. 高端镜面自拍肖像

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-03-29  **Language**: en

> 一个为 Nano Banana Pro 设计的超写实提示词，用于生成一张 4:5 比例的镜面自拍肖像。主体（Sadie Sink、Scarlett Johansson 或 Sabrina Carpenter）身着淡紫色丝绸连衣裙，置身于高档室内环境，重点在于精准还原面部特征。

![高端镜面自拍肖像](https://cms-assets.youmind.com/media/1774853734219_nrv4du_HEmEXuJaAAA-Twp.jpg)
![高端镜面自拍肖像](https://cms-assets.youmind.com/media/1774853734227_wg6420_HEmEXuEawAAWL7n.jpg)
![高端镜面自拍肖像](https://cms-assets.youmind.com/media/1774853734371_zxgv7j_HEmEXtfasAAxtre.jpg)

```
Ultra-realistic 4:5 mirror selfie portrait in an upscale indoor setting. Use the reference image for the subject’s identity, face, and hair — preserve exact facial features, proportions, and likeness.

The subject is standing at an angle, taking a mirror selfie with her right arm raised holding a smartphone.

She is wearing a pale mauve silk dress with a deep plunging draped cowl neckline and delicate silver floral embroidery.

Accessories include a dark smartphone with a multi-lens camera, long square-shaped nails with neutral polish, silver rings, layered silver bracelets or a watch, a thin pendant necklace, and dangling earrings.

The setting is an upscale bedroom or hotel room seen through a mirror reflection. Visible elements include a textured wall on the left and a bright circular lamp in the foreground. In the reflection, a lit bathroom with vertical slats and a patterned floor is visible, along with the edge of a bed with white sheets on the right.

Lighting is warm indoor lighting with strong uplighting from the foreground lamp, creating highlights and soft shadows across the subject.

High detail, realistic textures, luxury editorial lifestyle photography style, sharp focus on the subject, shallow depth of field.
```

[[Identity Preservation]] [[Mirror Selfie]] [[Sadie Sink]] [[Sabrina Carpenter]]

---

### 48. 超清写实真人与风格化 3D 漫画形象构图提示词

**Author**: [Saul Goodman](https://x.com/Goodmanprotocol)  **Date**: 2026-03-29  **Language**: en

> 一份为 Gemini Nano Banana 2 编写的详细提示词，旨在生成一张包含真人主体及其风格化 3D 漫画形象的单帧图像，强调真人主体严格的身份一致性，并为漫画形象赋予夸张的 Pixar/Disney 风格，同时包含特定的构图与光影要求。

![超清写实真人与风格化 3D 漫画形象构图提示词](https://cms-assets.youmind.com/media/1774853743905_2bin9v_HElVBfvbQAAz-YW.jpg)
![超清写实真人与风格化 3D 漫画形象构图提示词](https://cms-assets.youmind.com/media/1774853744016_4rsnca_HElVBdja4AA9Jh4.jpg)

```
Proportions, skin tone, hairstyle, and all recognizable features. Do not alter or stylize the real face.
Composition & Framing:

Full-body vertical shot with a clean, centered layout. The real subject stands on the right, and the caricature stands on the left at approximately 50–60% of the real subject’s height. The real subject casually rests one elbow on the caricature’s oversized head, creating a natural, playful interaction.
Real Subject (Photographic):

Ultra-realistic rendering with natural skin texture and fine detail. Expression is warm, relaxed, and confident.
Pose & Style (IMPORTANT):

The subject stands in a slightly cool, stylish posture — relaxed stance with subtle asymmetry (one leg slightly forward or weight shifted), shoulders loose, not stiff. The hand resting on the caricature should feel effortless and natural.
Clothing (Match Reference):

{argument name="clothing" default="Gray crewneck sweater (fine knit texture, ribbed cuffs/hem), classic blue jeans (straight fit), and clean white sneakers"}. Keep textures realistic and clearly visible.
3D Caricature (Stylized Version):

Pixar/Disney-inspired 3D style with exaggerated proportions — large expressive head and smaller body. The height should be noticeably shorter, around the real subject's waist level.
Facial features must remain recognizable but enhanced — larger eyes, softer forms, slightly amplified smile.
Emotion & Body Movement (IMPORTANT):

Expression is more playful and animated than the real subject

Eyes brighter and more expressive, smile slightly exaggerated
Body posture must NOT be stiff — use a natural, lively stance

Add subtle movement according to the real subject's personality

Pose should feel like a living, animated character, not a rigid figurine
Clothing:

Exact 1:1 stylized recreation of the real subject’s outfit with soft 3D textures.
Lighting & Environment:

Soft, diffused studio lighting from the upper-left, creating smooth highlights and gentle shadows. Clean light-gray gradient seamless background(lighter in the inner areas).
Output Style:

Ultra-clean, cinematic, high-detail render with strong contrast between realistic human and stylized 3D character. Both subjects grounded with soft natural shadows.
```

[[Identity Preservation]] [[Studio Lighting]]

---

### 49. 阳光乡村饮奶肖像

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-29  **Language**: en

> 为 Nano Banana Pro 准备的详细提示词，用于生成一位年轻女性（Kylie Jenner、Kendall Jenner、Sydney Sweeney 或 Sadie Sink）坐在阳光明媚的乡村田野中，从玻璃瓶中喝牛奶的图像，背景中有一头牛，强调严格的身份锁定和自然光效。

![阳光乡村饮奶肖像](https://cms-assets.youmind.com/media/1774853736247_5g7fnn_HElLp_pbIAALuuo.jpg)
![阳光乡村饮奶肖像](https://cms-assets.youmind.com/media/1774853736150_p3ht5r_HElLqdFbYAAmbn3.jpg)
![阳光乡村饮奶肖像](https://cms-assets.youmind.com/media/1774853736411_m9hy4f_HElLphxa8AA6hSc.jpg)
![阳光乡村饮奶肖像](https://cms-assets.youmind.com/media/1774853737190_9khkp6_HElLq6_aUAEaXC1.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman sitting in a sunlit countryside field drinking milk from a glass bottle, Use uploaded reference image, keep identity exact",
      "identity_lock": "STRICT — Use uploaded reference image, keep identity exact. Preserve facial structure, skin tone, eyes, proportions. Do not alter identity.",
      "pose": {
        "body_position": "sitting on the ground in a relaxed leaning pose",
        "torso": "slightly reclined backward supported by one arm",
        "head_position": "tilted slightly back and to the side while drinking",
        "arms": "one hand holding a glass milk bottle near lips, other arm extended behind for support",
        "legs": "one leg bent casually, the other extended out of frame",
        "posture": "natural relaxed countryside pose",
        "expression": "eyes gently closed or relaxed while drinking"
      }
    },
    "face_details": {
      "instruction": "Use uploaded reference image, keep identity exact",
      "expression": "calm, natural, soft enjoyment expression",
      "skin": "realistic skin texture with visible pores and slight sun glow",
      "eyes": "natural relaxed eyelids, soft shadows",
      "imperfections": "subtle asymmetry, natural skin variation"
    },
    "hair": {
      "instruction": "Preserve hairstyle exactly",
      "style": "long brunette hair tied into a low side ponytail with a white ribbon",
      "details": "soft natural strands, slight movement from breeze"
    },
    "makeup": {
      "style": "natural soft glam",
      "skin_finish": "light sun-kissed glow",
      "eyes": "neutral tones with soft eyeliner and mascara",
      "lips": "natural pink tone with slight gloss",
      "imperfection": "slightly uneven blending for realism"
    },
    "clothing": {
      "outfit": "{argument name="dress color and pattern" default="light beige dress with black polka dots"}",
      "fit": "flowy feminine fit with soft fabric folds",
      "details": "short sleeves, lightweight fabric reacting to sunlight"
    },
    "environment": {
      "setting": "open countryside field",
      "background": "large black and white cow standing behind subject, grassy field with wildflowers, blue sky with soft clouds",
      "ground": "dry grass mixed with small flowers and natural texture",
      "props": "glass milk bottle with slight milk spill detail"
    },
    "lighting": {
      "type": "natural sunlight",
      "style": "bright midday rural sunlight",
      "effect": "warm highlights and soft natural shadows",
      "shadows": "directional shadows on grass and body",
      "imperfections": "slight highlight clipping and natural exposure variation"
    },
    "camera": {
      "type": "DSLR",
      "lens": "50mm",
      "angle": "slightly low angle, close to ground perspective",
      "distance": "medium shot",
      "focus": "sharp focus on subject, sligh"
    }
  }
}
```

[[Identity Preservation]] [[Sydney Sweeney]] [[Sadie Sink]]

---

### 50. “软妹”运动风篮球场时尚大片

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-29  **Language**: en

> 一份为 Nano Banana Pro 准备的详细提示词，旨在生成一张 Anya Taylor-Joy 的生活方式时尚大片。画面呈现“软妹邂逅运动风”的美学风格，她在黄金时刻蹲在户外篮球场上，强调严格的身份锁定和照片级真实细节。

![“软妹”运动风篮球场时尚大片](https://cms-assets.youmind.com/media/1774853734577_3o3kn6_HElHJlJagAAayTY.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman squatting on an outdoor basketball court holding a basketball close to her face, Use uploaded reference image, keep identity exact",
      "identity_lock": "STRICT — Use uploaded reference image, keep identity exact. Preserve facial features, skin tone, eyes, and proportions. Do not alter identity.",
      "pose": {
        "body_position": "deep squat position with heels raised slightly",
        "legs": "knees bent fully, feet close together",
        "torso": "upright with slight forward lean",
        "arms": "one hand holding basketball near cheek, other arm relaxed near knee",
        "head_position": "tilted slightly toward ball",
        "expression": "soft confident gaze toward camera with slightly parted lips"
      }
    },
    "face_details": {
      "instruction": "Use uploaded reference image, keep identity exact",
      "expression": "confident, relaxed, slightly playful",
      "skin": "realistic texture with visible pores and natural glow from sunlight",
      "eyes": "sharp with warm sunlight reflections",
      "imperfections": "natural asymmetry and skin variation"
    },
    "hair": {
      "instruction": "Preserve hairstyle exactly",
      "style": "long straight hair falling over shoulders",
      "details": "natural movement, slight wind or softness"
    },
    "makeup": {
      "style": "natural glam",
      "skin_finish": "warm sunlit glow",
      "eyes": "light eyeliner and mascara",
      "lips": "natural glossy tone",
      "imperfection": "slightly imperfect blending for realism"
    },
    "clothing": {
      "outfit": "white fitted crop top and orange athletic shorts",
      "footwear": "clear high-heeled shoes with socks",
      "accessories": "bracelets and glasses",
      "details": "natural fabric folds, slight stretch"
    },
    "environment": {
      "setting": "outdoor basketball court",
      "surface": "reddish court with white curved line markings",
      "props": "basketball with visible branding",
      "background": "trees, fence posts, and soft blurred park environment"
    },
    "lighting": {
      "type": "golden hour sunlight",
      "style": "warm directional light from side",
      "effect": "strong warm highlights and soft long shadows",
      "shadows": "soft elongated shadows on ground",
      "imperfections": "slight overexposure on highlights"
    },
    "camera": {
      "type": "digital camera",
      "lens": "50mm",
      "angle": "slightly low angle at subject level",
      "distance": "medium full-body framing",
      "focus": "sharp on subject with soft background blur",
      "imperfections": "slight lens softness, natural grain"
    },
    "composition": {
      "style": "lifestyle editorial",
      "framing": "full body centered composition",
      "balance": "subject centered with leading court l"
    }
  }
}
```

[[Identity Preservation]] [[Anya Taylor-Joy]]

---

### 51. 保持面部特征的 3D 卡通漫画风格转换

**Author**: [Synthia](https://x.com/AIwithSynthia)  **Date**: 2026-03-29  **Language**: en

> 这是一个为 Google Gemini Nano Banana Pro 设计的提示词，旨在将上传的图像转换为风格化的 3D 卡通漫画形象，使其拥有大头小身的比例，同时严格保留主体人物的面部特征和表情。场景设定为人物倚靠在鹅卵石街道上的一辆复古深绿色经典汽车旁。

![保持面部特征的 3D 卡通漫画风格转换](https://cms-assets.youmind.com/media/1774853736664_vhtoo6_HEkK2GhaEAAfmeK.jpg)
![保持面部特征的 3D 卡通漫画风格转换](https://cms-assets.youmind.com/media/1774853736655_n5mxd6_HEkK2SeaYAAKWYl.jpg)

```
Use the uploaded image as the primary subject reference. Transform the person into a stylized caricature with a slightly oversized head and a smaller body while preserving facial identity, expression, hairstyle, and key features.
Place the subject casually leaning against a vintage dark green classic car on a narrow cobblestone street with warm glowing street lamps on both sides. Maintain a relaxed, confident pose.
Outfit should match or naturally enhance the original clothing from the uploaded image (adapt if needed to fit the scene). Keep textures realistic and well-detailed.
Style: 3D cartoon realism, cinematic lighting, shallow depth of field, ultra-detailed, soft shadows, warm tones, high resolution, vibrant but natural colors.
```

[[Identity Preservation]] [[Cobblestone Street]]

---

### 52. 置身于 Angry Birds 世界的超写实男子

**Author**: [Karlos](https://x.com/de_mon010)  **Date**: 2026-03-29  **Language**: en

> 这是一个为 Google Nano Banana 编写的提示词，旨在创作一张超写实的 Instagram 竖版图片。画面中，一名与参考图面部特征完全一致的男子正在 Angry Birds 世界中上演一场戏剧性的爆炸逃生，并详细描述了动作、环境和电影级光影。

![置身于 Angry Birds 世界的超写实男子](https://cms-assets.youmind.com/media/1774853740918_35le08_HEjC1MyaMAAf-YD.jpg)

```
Create a completely new ultra realistic Instagram vertical 4:5 image for Gemini 3 Pro Nano Banana of the same man with identical facial features inside the Angry Birds world during a dramatic escape moment. He jumps off a collapsing wooden platform as multiple TNT crates detonate behind him, red sparks and debris flying. Red is mid air flying beside him, Bomb is igniting, Chuck sprints ahead, Stella flutters above, and pigs are scattering everywhere in panic. Outfit: fitted white T-shirt, tactical brown cargo pants, and impact-ready white sneakers with red-yellow accents, all detailed and textured. Environment: broken glass, exploding stone blocks, rolling green hills blurred behind. Lighting: intense warm explosion glow from one side combined with cool sky light from the other, giving epic cinematic contrast. Feathers, dust, debris, and motion are ultra

detailed. Shot on a dynamic slightly low 28 mm lens for powerful action depth, with sharp focus on the man and Red.
```

[[Identity Preservation]]

---

### 53. 2x2 网格可爱动物时尚大片提示词

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-28  **Language**: en

> 这是一个为 Nano Banana Pro 设计的高度结构化 JSON 提示词，专用于图生图任务。旨在生成一个 2x2 网格图像，展示同一位年轻女性与不同可爱动物（小鸡、兔子、鹦鹉、猫）的互动，采用柔和的春日时尚大片风格，重点强调身份锁定与柔和美学。

![2x2 网格可爱动物时尚大片提示词](https://cms-assets.youmind.com/media/1774853745716_z1499w_HEgnQOhWkAAeXrl.jpg)

```
{
 "generation_request": {
 "meta_data": {
 "tool": "NanoBanana Pro",
 "task_type": "cute_animal_fashion_editorial_2x2_grid",
 "language": "en",
 "priority": "highest",
 "version": "v1.0_PINK_YELLOW_HAPPY_ANIMAL_2X2"
 },

 "input": {
 "mode": "image_to_image",
 "multi_reference": true,
 "reference_image_usage": "very_high",
 "preserve_identity": true,
 "notes": "The young woman must appear in all four panels with highly consistent face, eyes, smile, and soft feminine features. Her face must be clearly visible in every panel, never hidden by animals, hair, or props. The overall mood should be joyful, sweet, cozy, playful, and visually charming. Style her in pink and yellow clothing or knitwear with a soft pastel aesthetic. Include cute animals naturally, but keep the woman as the main subject."
 },

 "output_settings": {
 "aspect_ratio": "4:5",
 "orientation": "portrait",
 "resolution_target": "ultra_high_res",
 "num_images": 1,
 "layout": {
 "type": "grid",
 "rows": 2,
 "cols": 2,
 "gutter": "thin",
 "outer_border": "none",
 "panel_consistency": "maximum_identity_lock"
 },
 "render_style": "pastel_cute_fashion_editorial",
 "sharpness": "editorial_crisp",
 "grain": "soft_subtle_film",
 "dynamic_range": "bright_soft_natural",
 "color_grade": "pastel_pink_yellow_spring"
 },

 "subject": {
 "identity": "young woman in all four panels",
 "face": "soft feminine face, visible eyes, warm smile, joyful expression, natural beauty",
 "hair": "softly styled dark or brunette hair, neat and flattering, face kept open and visible",
 "makeup": "light fresh makeup, soft blush, healthy skin glow, natural pink lips",
 "outfit": "{argument name="outfit color" default="pink and yellow"} cozy knitwear or soft pastel fashion pieces, playful but stylish, warm and charming",
 "styling": "cute, cheerful, soft spring aesthetic, polished but natural"
 },

 "animal_direction": {
 "panel_1": "two fluffy baby chicks resting gently on her lap or sweater",
 "panel_2": "small soft bunnies held carefully in her arms",
 "panel_3": "bright colorful parrot near her shoulder or arms, positioned without covering her face",
 "panel_4": "fluffy white cat in cozy knitwear, resting in her lap or arms"
 },

 "scene": {
 "environment": "cozy garden, soft outdoor corner, or warm lifestyle setting with greenery and pastel accents",
 "mood": "happy, sweet, playful, cozy, affectionate, uplifting",
 "background": "clean, charming, softly detailed, no clutter"
 },

 "panel_direction": {
 "panel_1": "smiling softly while looking at the camera, baby chicks placed gently in front, face fully visible",

 "panel_2": "happy playful pose holding small bunnies, warm direct smile, bright friendly energy",

 "panel_3": "joyful close pose with colorful parrot, affectionate expression, face clear and unobstructed",

 "panel_4": "cozy seated pose with fluffy white cat in her arms, relaxed smile, dreamy cheerful mood"
 },

 "pose_language": {
 "movement": "gentle, natural, affectionate, playful",
 "expression"[TRUNCATED]
```

[[Identity Preservation]] [[Image-To-Image]] [[2x2 Grid Layout]]

---

### 54. 保持面部特征的黑白时尚拼贴画

**Author**: [Harboris](https://x.com/harboriis)  **Date**: 2026-03-28  **Language**: en

> 这是一份专为 Google Gemini Nano Banana Pro 设计的详细提示词，旨在创作一张逼真的 2x2 黑白男模拼贴画。要求在保持参考图中面部和服装特征的同时，呈现高对比度的时尚摄影风格。

![保持面部特征的黑白时尚拼贴画](https://cms-assets.youmind.com/media/1774766199980_q1ulmj_HEeIvrzbAAIdt34.jpg)

```
using the attached reference photos as sources, preserve the same male face and hairstyles from the face reference and the same outfits from the clothing references. create a photorealistic black-and-white studio photoshoot collage arranged in a clean 2x2 grid with thin white spacing between frames. neutral gray seamless studio background, soft diffused fashion lighting with gentle shadows. frame 1: waist-up portrait, man in a plain rolled-sleeve t-shirt, one hand lightly touching the chin, direct intense gaze to camera, relaxed shoulders. frame 2: three-quarter standing pose in the same t-shirt, body angled slightly sideways, one hand near the mouth in a thoughtful gesture, casual stance. frame 3: mid-shot in a denim jacket, body turned partly away, one hand holding the jacket collar or shoulder, confident look toward camera. frame 4: tight portrait in the denim jacket, fingers resting near the lips and nose bridge, fashion editorial expression. natural skin texture, realistic fabric folds and denim texture, sharp hair detail. high-contrast monochrome conversion, cinematic fashion photography, 85mm lens look, f/2.8. no text, no watermark
```

[[Identity Preservation]] [[2x2 Grid]]

---

### 55. 奢华网球专题 2x2 网格 图生图提示词 适用于 Nano Banana Pro

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-27  **Language**: en

> 一个详细的图生图提示，用于 Nano Banana Pro 生成一个 2x2 网格拼贴画，以制作一篇奢华网球时尚专题报道。该提示的重点是确保所有面板之间保持最大的身份一致性，同时展示不同的蓝色和绿色服装、姿势，并呈现出高级时装广告的审美风格。

![奢华网球专题 2x2 网格 图生图提示词 适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1774679861187_bd99vo_HEc1BQRbkAAd9JY.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "luxury_tennis_editorial_2x2_grid",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_BLUE_GREEN_TENNIS_2X2_EDITORIAL"
    },

    "input": {
      "mode": "image_to_image",
      "multi_reference": true,
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "notes": " Create a photoreal 2x2 luxury tennis editorial collage featuring the elegant woman across all four panels. Keep facial identity highly consistent. Include blue and green outfit variations inspired by premium tennis fashion. Each panel must have a distinct pose, strong composition, and fashion-campaign energy."
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "num_images": 1,

      "layout": {
        "type": "grid",
        "rows": 2,
        "cols": 2,
        "gutter": "thin",
        "outer_border": "none",
        "panel_consistency": "maximum_identity_lock"
      },

      "render_style": "luxury_sport_fashion_editorial",
      "sharpness": "editorial_crisp",
      "grain": "subtle_film",
      "dynamic_range": "sunlit_clean_contrast",
      "color_grade": "fresh_soft_summer"
    },

    "subject": {
      "identity": " elegant athletic woman in all four panels",
      "hair": "long softly styled hair or sleek sporty ponytail depending on pose, polished and feminine",
      "makeup": "clean glowing skin, soft bronzed contour, glossy natural lips, refined sporty beauty look",
      "body": "lean athletic feminine proportions, elegant posture, natural anatomy"
    },

    "outfit_direction": {
      "panel_1": "soft pastel blue luxury tennis dress, fitted bodice, subtle pleated skirt, refined premium fabric",
      "panel_2": "fresh matcha green tennis set with fitted top and pleated mini skirt, modern and sculpted",
      "panel_3": "icy aqua blue sleeveless tennis look, elegant waist definition, elevated sporty chic styling",
      "panel_4": "light sage green premium tennis dress or coordinated set, feminine and polished"
    },

    "accessories": {
      "shoes": "clean luxury white tennis shoes",
      "jewelry": "minimal delicate jewelry only",
      "optional_items": "one panel may include elegant sunglasses or a cap, but not all panels",
      "racket": "premium tennis racket included naturally in selected poses",
      "ball": "tennis ball used in one or two panels only"
    },

    "scene": {
      "environment": "luxury outdoor tennis court under clean natural sunlight",
      "court_style": "editorial clay or pastel-toned court aesthetic with premium resort-club atmosphere",
      "background": "minimal and elegant, with soft greenery, clean lines, and no visual clutter",
      "mood": "fresh, stylish, sporty, feminine, expensive, summer editorial"
    },

    "panel_direction"
```

[[Identity Preservation]] [[Image-To-Image]] [[2x2 Grid Collage]]

---

### 56. 奢华 香槟 婚礼 主题 图生图 提示词 for Nano Banana 2

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-27  **Language**: en

> 一个针对 Nano Banana 2 的复杂图像到图像提示，旨在生成一张奢华的婚礼宣传图片，画面中有一对夫妇，置身于凝固的香槟飞溅之下。该提示强调保留上传主体的精确特征，并结合电影级布光和流体动力学，实现极致的照片真实感。

![奢华 香槟 婚礼 主题 图生图 提示词 for Nano Banana 2](https://cms-assets.youmind.com/media/1774679861118_i2b8md_HEcv7n9WoAANbac.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "Nano Banana 2",
      "task_type": "luxury_champagne_wedding_campaign",
      "version": "v2.0_CHAMPAGNE_SPLASH_EDITORIAL"
    },

    "input": {
      "mode": "image_to_image",
      "multi_reference": true,
      "reference_image_usage": "maximum",
      "preserve_identity": true,
      "identity_lock": "absolute",
      "no_identity_blending": true,
      "face_similarity_priority": "maximum",
      "notes": "Use uploaded bride and groom exactly. Transform into a luxury champagne celebration campaign moment with controlled splash dynamics."
    },

    "scene": {
      "location": "dark elegant night background with subtle depth",
      "mood": "celebration, luxury, high-energy, cinematic"
    },

    "composition": {
      "framing": "mid shot, centered couple",
      "focus": "faces sharp, champagne splash frozen",
      "depth": "foreground bokeh droplets, mid subjects, deep dark background"
    },

    "styling": {
      "absolute_lock": true,

      "bride": {
        "identity_match": "exact uploaded bride",
        "beauty": "high-fashion bridal glow, defined cheekbones, radiant skin",
        "dress": "same wedding dress but enhanced sparkle detail",
        "pose": "one arm lifted elegantly, body slightly arched",
        "expression": "genuine joyful laugh, confident and radiant"
      },

      "groom": {
        "identity_match": "exact uploaded groom",
        "outfit": "same suit, refined texture",
        "pose": "holding champagne bottle firmly, angled upward",
        "expression": "laughing naturally, looking toward bride"
      }
    },

    "motion": {
      "type": "high-speed freeze moment",
      "champagne": "sharp liquid splash with visible droplets and arcs",
      "direction": "upward spray with natural pressure curve",
      "particles": "foreground and background droplets for depth"
    },

    "cinematography": {
      "camera": "ARRI Alexa Mini LF",
      "lens": "85mm portrait lens",
      "aperture": "f/2.0",
      "shutter": "high-speed freeze (1/2000 feel)",
      "lighting": "flash-style frontal highlight + soft rim light",
      "highlight": "liquid sparkle and skin glow emphasized",
      "color_grading": "warm luxury tones, champagne gold highlights",
      "style": "high-end fashion campaign"
    },

    "art_direction": {
      "contrast": "bright liquid vs dark background",
      "texture": "sparkling droplets, glossy fabric",
      "tone": "celebration but premium, not chaotic"
    },

    "physics_and_realism": {
      "liquid": "realistic fluid dynamics and pressure",
      "anatomy": "perfect posture and hand grip",
      "interaction": "natural champagne reaction force",
      "no_glitches": true
    },

    "realism": {
      "priority": "maximum realism",
      "no_ai_look": true,
      "no_cgi": true
    },

    "negative_prompt": {
      "errors": "blurry liquid, distorted faces, chaotic splash",
```

[[Identity Preservation]] [[Cinematic Lighting]] [[Couple Portrait]]

---

### 57. Nano Banana Pro 电影感 户外人像 提示词

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-27  **Language**: en

> 一个 Nano Banana Pro 提示词，用于生成一张电影感的户外肖像，描绘一位年轻女性在黄金时段的海滩上靠在一辆复古面包车旁，需要一张参考图像来保留身份特征，并着重于复古胶片美学。

![Nano Banana Pro 电影感 户外人像 提示词](https://cms-assets.youmind.com/media/1774679874568_irivdh_HEcBJSWbkAAvVEU.jpg)
![Nano Banana Pro 电影感 户外人像 提示词](https://cms-assets.youmind.com/media/1774679874590_0l571h_HEcBKjebQAA5qxd.jpg)
![Nano Banana Pro 电影感 户外人像 提示词](https://cms-assets.youmind.com/media/1774679874642_s4b36a_HEcBJvmboAEOaYT.jpg)

```
A cinematic outdoor portrait of a young woman leaning against a vintage van at the beach, use reference image face, preserve identity strictly.

Pose: standing sideways, leaning on the vehicle door, back slightly arched, confident posture.

Expression: intense, relaxed gaze toward camera.

Outfit: minimal summer styling, retro-inspired tones.

Environment: beachside setting with sand, vintage van, warm sunlight.

Lighting: golden hour sunlight, soft highlights, warm glow, natural shadows.

Style: vintage film aesthetic, retro fashion editorial, ultra realistic, high detail.

Color grading: warm, slightly faded tones, soft grain, nostalgic summer look.
```

[[Identity Preservation]] [[Female Portrait]]

---

### 58. 高端时尚香水广告，侧光照明

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-27  **Language**: en

> 一个电影级提示词，用于生成一张高端时尚香水广告图片，画面中一名女性在极简摄影棚环境中喷洒香水，配合戏剧性侧光照明。该提示词强调保留参考图片中的人物特征，并捕捉到清晰可见的雾气颗粒。

![高端时尚香水广告，侧光照明](https://cms-assets.youmind.com/media/1774679879201_3w393a_HEb_5WsbYAAMaDF.jpg)
![高端时尚香水广告，侧光照明](https://cms-assets.youmind.com/media/1774679879244_0zp72x_HEb_4RCboAEkpVc.jpg)
![高端时尚香水广告，侧光照明](https://cms-assets.youmind.com/media/1774679879220_9kvxip_HEb_4zmakAAJ9zq.jpg)

```
A cinematic side-profile portrait of a woman sitting in a minimal studio setting, use reference image face, preserve identity strictly.

Pose: seated with one knee raised, elegant curved posture, relaxed hand positioning.

Action: spraying perfume into the air, visible mist particles floating in light.

Expression: calm, dreamy, eyes slightly closed or looking upward.

Outfit: minimal fitted bodysuit, soft neutral tones, casual socks and sneakers.

Lighting: dramatic side lighting, strong highlights and shadows, soft glow on skin.

Atmosphere: visible mist illuminated by light, dreamy cinematic effect.

Background: dark minimal studio, no distractions.

Style: high-fashion perfume campaign, editorial photography, ultra realistic, high detail, cinematic color grading.
```

[[Identity Preservation]] [[Minimalist Studio]] [[Dramatic Side Lighting]]

---

### 59. 高端时尚美妆特写肖像提示词，适用于 Nano Banana Pro

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-27  **Language**: en

> 一个 Nano Banana Pro 提示词，用于生成一张描绘一位女性手持并咬着冰棒的时尚大片风格美妆特写肖像，同时要求提供一张参考图片以保持人物身份，并需指定光照和风格细节。

![高端时尚美妆特写肖像提示词，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1774679872107_0uxnfq_HEb8GKsa8AAt7ra.jpg)
![高端时尚美妆特写肖像提示词，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1774679872011_rnmzll_HEb8HX3bsAA8Ix6.jpg)
![高端时尚美妆特写肖像提示词，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1774679872286_ndg5yd_HEb8Gtma0AAKDzs.jpg)

```
A high-fashion beauty close-up portrait of a woman holding and biting a popsicle, use reference image face, preserve identity strictly.

Framing: tight close-up, face and shoulders centered.

Accessories: sunglasses resting on head, statement earrings.

Expression: intense, confident gaze with slightly open lips.

Lighting: bright studio lighting, glossy skin highlights, soft shadows.

Style: beauty editorial, magazine cover style, ultra realistic, high detail.

Focus: sharp facial details, smooth skin texture, high clarity.

Color accent: vibrant popsicle as focal point, strong contrast against neutral background.
```

[[Identity Preservation]] [[Beauty Photography]]

---

### 60. 白色影棚中手持钞票的鱼眼人像

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-27  **Language**: en

> 一个 Nano Banana Pro 提示词，用于生成一张时尚的、高细节的鱼眼镜头肖像，描绘一位年轻女性自信地站立在一个白色摄影棚里，里面散落着现金，并要求提供一张参考图以严格保留主体身份。

![白色影棚中手持钞票的鱼眼人像](https://cms-assets.youmind.com/media/1774679876541_z9vgsn_HEbz-AZaoAAsO6e.jpg)
![白色影棚中手持钞票的鱼眼人像](https://cms-assets.youmind.com/media/1774679876532_xy76ik_HEbz-oqbQAAplZ9.jpg)
![白色影棚中手持钞票的鱼眼人像](https://cms-assets.youmind.com/media/1774679876553_ba6wju_HEbz9i3a0AAx2nH.jpg)

```
A trendy fisheye lens portrait of a young woman standing in a white studio room filled with scattered cash, use reference image face, preserve identity strictly, do not change facial features, do not change hair color or eye color.

Outfit: black cropped top, denim jeans, stylish jacket with fur or pattern details, trendy boots.

Pose: standing confidently, holding stacks of cash in both hands, money falling around her, relaxed but dominant posture.

Expression: confident, slightly playful, bold, rich attitude.

Accessories: rings, tote bag, minimal jewelry.

Hair: styled, soft waves or sleek finish.

Environment: clean white box-style room, floor covered with money, bills floating in air.

Lighting: bright studio lighting, even exposure, sharp details.

Camera: fisheye lens, wide-angle distortion, slightly top-down perspective.

Style: Gen-Z luxury, influencer aesthetic, viral content, ultra realistic, high detail.
```

[[Identity Preservation]]

---

### 61. JSON 三联画 提示词：温馨 卧室 场景

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-27  **Language**: en

> 一个结构化的 JSON 提示词，用于 Nano Banana 2，通过 Gemini 生成一个垂直三联画构图（三幅堆叠的画面），描绘一位单身女性在温馨的居家卧室环境中，处于黄金时段。该提示词强调所有三幅画面中 100% 一致的面部身份、柔和的灯光以及电影般的质感。

![JSON 三联画 提示词：温馨 卧室 场景](https://cms-assets.youmind.com/media/1774679881775_4yoq4b_HEbvQThbUAA1t6k.jpg)

```
Create a triptych composition with vertical layout of three stacked frames. Same subject, same environment, same lighting across all frames. A single woman in her mid-20s with 100% consistent facial identity across all three frames. She has natural, smooth skin with visible pores and subtle imperfections, blue eyes that are expressive and softly reflective under golden hour light, and long, voluminous, smooth flowing hair that falls naturally across the face, partially obscuring facial features in all frames. She wears light, minimal, romantic makeup with soft blush, subtle highlighter, natural lips, and lightly defined eyes. She wears a minimalist strappy top in soft, slightly textured fabric with natural folds, in muted neutral tones of beige, cream, and soft taupe. A silver ear cuff is visible. The setting is an intimate home bedroom with a soft bed featuring neutral-toned sheets and a plush pillow supporting her upper body, with slightly wrinkled fabric for realism. Golden hour sunlight enters from a side window, creating soft, directional, warm light with streaks across face and body, producing muted golden hues with gentle contrast. The atmosphere is romantic, intimate, and calm with muted palette, soft highlights, subdued shadows, and visible film grain for cinematic texture. Use cinematic, editorial photography style with a 50mm prime lens, shallow depth of field with soft background blur, sharp focus on key facial features in each frame, fine film grain, and soft highlight roll-off with no harsh clipping. TOP FRAME: Close-up portrait in first-person selfie perspective, lying on bed propped up by pillow, head slightly turned sideways toward camera, soft romantic introspective gaze, a streak of golden sunlight crosses her face diagonally, silver ear cuff visible, hair partially covering face, eyes softly engaged with camera, tight face crop with slight shoulder visibility. CENTER FRAME: Extreme close-up of lips, hand gently brushing over lips with soft, slow, sensual but subtle motion, natural lip texture, soft light reflecting on lips, fingers partially in frame with natural positioning, hair strands crossing frame slightly, soft golden highlights with muted shadows, sharp focus on lips with shallow depth of field. BOTTOM FRAME: Close-up of eyes from side angle, same bed position, head tilted back slightly, side profile focusing on eyes, golden sunlight streak illuminating the eyes directly, blue eyes glowing under sunlight, hair partially obscuring one eye, soft shadow gradients across face, sharp focus on eyes with blurred background. Style: Romantic cinematic editorial with influences from film photography, luxury fashion editorials, and intimate lifestyle portraiture. Color palette: muted warm tones, soft beige, gold, cream, and subtle shadows. Post-processing: visible analog film grain, low to medium contrast, slightly desaturated, soft bloom effect on highlights, lifted shadows for softness. No anime or illustration, strictly photorealistic. Facial identity must remain identical across all frames. Avoid over-smoothing, preserve skin texture. Three distinct frames clearly separated but visually cohesive.
```

[[Identity Preservation]] [[Golden Hour Lighting]]

---

### 62. 日落时分的柔和粉色跑车生活方式照片

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-27  **Language**: en

> 一个 Nano Banana Pro 提示词，用于生成一张电影感生活照：画面中，一位年轻女性在黄金时段倚靠在一辆淡粉色跑车旁。此提示词要求提供一张参考图，以严格保留主体的身份和面部特征。

![日落时分的柔和粉色跑车生活方式照片](https://cms-assets.youmind.com/media/1774679874944_nxvp05_HEbux6ebAAI1ay-.jpg)

```
A cinematic lifestyle photo of a young woman leaning casually against a pastel pink sports car on a quiet road during sunset, use reference image face, preserve identity strictly, do not change facial features, do not change hair color or eye color.

Outfit: fitted white tank top, soft pink leggings, white sneakers.

Pose: leaning against the side of the car, relaxed posture, one leg slightly bent, confident but effortless stance.

Expression: calm, relaxed, slightly confident, natural beauty.

Hair: long natural hair, soft and slightly wind-blown.

Environment: open road with trees and natural background, warm sunset sky with soft clouds.

Lighting: golden hour sunlight, warm tones, soft glow, cinematic shadows.

Camera: full-body shot, slightly low angle, natural framing.

Style: lifestyle luxury, soft aesthetic, Instagram editorial, ultra realistic, high detail.
```

[[Identity Preservation]] [[Lifestyle Photography]]

---

### 63. 电影般的日落生活方式照片提示词，适用于 Nano Banana Pro

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-27  **Language**: en

> 一个 Nano Banana Pro 提示词，用于生成一张电影感生活方式照片：一名年轻女性在日落时分坐在跑车引擎盖上，需要一张参考图像以保留身份特征，并详细说明环境、光线和风格。

![电影般的日落生活方式照片提示词，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1774679873207_3nwp3w_HEbt95GbEAApGy5.jpg)

```
A cinematic lifestyle photo of a young woman sitting on the hood of a sleek sports car on an empty road during sunset, use reference image face, preserve identity strictly, do not change facial features, do not change hair color or eye color.

Outfit: oversized soft pink sweater, casual white sneakers.

Pose: sitting casually on the front of the car, legs slightly forward, relaxed posture, leaning slightly back.

Expression: calm, dreamy, slightly confident, natural beauty.

Hair: natural loose hair, slightly wind-blown.

Environment: open road with trees and greenery, dramatic sunset sky with clouds and light rays.

Lighting: golden hour with soft warm tones, car headlights turned on creating glow on legs, cinematic shadows.

Camera: slightly low angle, full-body framing, centered composition.

Style: cinematic lifestyle, luxury aesthetic, soft feminine vibe, ultra realistic, high detail.
```

[[Identity Preservation]] [[Cinematic Lifestyle Photography]]

---

### 64. 史诗般的烟花婚礼之吻图生图提示，适用于 Nano Banana 2

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-27  **Language**: en

> 一个复杂的图像到图像提示词，用于 Nano Banana 2 来生成一个在盛大烟花下的史诗般、电影感的婚礼亲吻场景。该提示词要求精确保留上传的这对新人的身份，并指定富有张力的低角度构图、烟花带来的动态光影以及极致的真实感。

![史诗般的烟花婚礼之吻图生图提示，适用于 Nano Banana 2](https://cms-assets.youmind.com/media/1774679862021_kxy2in_HEbtRoTWkAARSqG.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "Nano Banana 2",
      "task_type": "epic_firework_wedding_kiss",
      "version": "v2.0_EPIC_FIREWORK_ROMANCE"
    },

    "input": {
      "mode": "image_to_image",
      "multi_reference": true,
      "reference_image_usage": "maximum",
      "preserve_identity": true,
      "identity_lock": "absolute",
      "no_identity_blending": true,
      "face_similarity_priority": "maximum",
      "notes": "Use uploaded bride and groom exactly. Scene is an epic cinematic kiss under large fireworks."
    },

    "scene": {
      "location": "open outdoor landscape with trees silhouetted",
      "time": "night",
      "mood": "epic, romantic, cinematic, powerful"
    },

    "composition": {
      "framing": "low angle shot looking slightly upward",
      "scale": "fireworks dominate the sky, couple in foreground",
      "focus": "sharp couple, dynamic sky"
    },

    "styling": {
      "absolute_lock": true,

      "bride": {
        "identity_match": "exact uploaded bride",
        "beauty": "high-fashion glow, sculpted face, radiant skin",
        "dress": "same wedding dress with subtle sheen catching light",
        "pose": "leaning into kiss, hand gently on groom’s face",
        "expression": "deeply immersed, emotional"
      },

      "groom": {
        "identity_match": "exact uploaded groom",
        "pose": "holding bride firmly at waist",
        "expression": "focused, intimate"
      }
    },

    "motion": {
      "fireworks": "large detailed explosions with multiple layers and particle trails",
      "light": "dynamic light bursts illuminating couple intermittently",
      "smoke": "soft drifting smoke for depth"
    },

    "cinematography": {
      "camera": "ARRI Alexa Mini LF",
      "lens": "35mm cinematic lens",
      "aperture": "f/2.0",
      "lighting": "fireworks acting as dynamic key and rim light",
      "contrast": "bright gold explosions vs dark sky",
      "color_grading": "deep blues + warm gold highlights",
      "style": "epic cinematic film still",
      "dynamic_range": "high"
    },

    "art_direction": {
      "foreground": "sharp emotional couple",
      "background": "massive fireworks filling sky",
      "tone": "celebration meets cinematic love story"
    },

    "physics_and_realism": {
      "fireworks": "realistic explosion patterns and gravity fall",
      "anatomy": "perfect pose alignment",
      "fabric": "light reacting naturally to flashes",
      "no_glitches": true
    },

    "realism": {
      "priority": "maximum realism",
      "no_ai_look": true,
      "no_cgi": true
    },

    "negative_prompt": {
      "errors": "small fireworks, weak lighting, blurry faces",
      "visual": "flat night scene, no depth",
      "ai_artifacts": "fake sparks, distorted silhouettes",
      "text": "no text, no watermark"
    },

    "output_settings": {
      "resolution_target": "ultra_high_res",
      "render_qua
```

[[Identity Preservation]] [[Couple Portrait]] [[Low Angle Composition]]

---

### 65. 奢华跑车写真提示词，兼顾面部保持

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-27  **Language**: en

> 为 Nano Banana Pro 设计的 高端奢华生活方式 摄影提示词，聚焦于 一位年轻女性 在一栋现代简约风格的房子外面，一辆流线型黑色跑车 旁边摆姿势。该提示词 严格要求 保留 参考图片中人物的 身份特征、发色 和 瞳色。

![奢华跑车写真提示词，兼顾面部保持](https://cms-assets.youmind.com/media/1774679881046_weuhgj_HEbsbGhaUAAuQs2.jpg)
![奢华跑车写真提示词，兼顾面部保持](https://cms-assets.youmind.com/media/1774679881039_3331p3_HEbsacQasAAq-5L.jpg)
![奢华跑车写真提示词，兼顾面部保持](https://cms-assets.youmind.com/media/1774679881128_f2yjvo_HEbsbphbAAAT78-.jpg)
![奢华跑车写真提示词，兼顾面部保持](https://cms-assets.youmind.com/media/1774679881940_j54dgg_HEbscICbkAALGyk.jpg)

```
A high-end luxury lifestyle photoshoot of a young woman next to a sleek black sports car, use reference image face, preserve identity strictly, do not change facial features, do not change hair color or eye color.

Outfit: elegant fitted mini dress, neutral tones, high heels, small luxury handbag.

Pose: crouching beside the car near the front wheel, adjusting makeup or lips, confident and relaxed posture.

Expression: calm, rich, effortless confidence.

Hair: long styled hair, soft waves.

Environment: modern minimalist house exterior, clean architecture, neutral walls, stone pavement.

Lighting: strong natural sunlight, sharp shadows, high contrast, golden hour feel.

Camera: side angle, mid-full body shot, sharp focus, editorial framing.

Style: luxury editorial, minimal aesthetic, high fashion, ultra realistic, clean composition.
```

[[Identity Preservation]]

---

### 66. 比例扭曲的超现实概念摄影

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-27  **Language**: en

> 一个用于生成具有比例扭曲的超现实概念艺术摄影作品的提示词。主体坐在一颗巨大而逼真的人头上，置身于极简主义的现代室内。它需要使用参考图像来确定主体和巨大头部两者的确切面部特征和身份，并强调超现实的纹理和现代艺术的氛围。

![比例扭曲的超现实概念摄影](https://cms-assets.youmind.com/media/1774679863319_4yoj3w_HEaEX1KaIAA2W-Y.jpg)

```
Surreal conceptual scene with scale distortion, minimalist modern interior with soft natural light, wooden floor and clean geometric wall shapes, subject sitting casually with legs apart on top of an oversized realistic human head placed on the floor, wearing casual outfit ({argument name="outfit description" default="green oversized sweater, beige pants, white sneakers"}), using exact face and identity from reference image for both body and oversized head, head highly detailed and realistic with glasses and skin texture, body slightly cropped at neck creating surreal effect, subject pointing forward confidently, balanced composition, soft shadows, neutral color palette, clean aesthetic, ultra-realistic textures, conceptual art photography style, shot on Fujifilm GFX100, 50mm lens, f/2.8, high detail, modern art vibe
```

[[Identity Preservation]] [[Surrealist Photography]] [[Minimalist Modern Interior]]

---

### 67. 超现实微型舞动合成照片提示

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-27  **Language**: en

> 一个用于生成超现实、高保真合成照片的提示词，该照片采用双尺度强制透视效果。它需要上传一张面部参考图，以在背景中创建一个巨大的、微笑的版本，并在前景中创建一个微型的、在智能手机屏幕上跳舞的版本，适用于 Nano Banana 2 或 Grok Imagine。

![超现实微型舞动合成照片提示](https://cms-assets.youmind.com/media/1774679880584_l97en5_HEaDDVAa0AAVHa3.jpg)

```
The Dancing Miniature 
A surreal, high-fidelity composite photograph featuring "uploaded face as reference" in a dual-scale forced perspective. In the soft-focus background, a giant version of the subject smiles warmly, wearing a light blue denim jacket , rendered with heavy bokeh. In the sharp foreground, a hand holds a horizontal smartphone with a bright red case. Perched delicately on the phone screen is a miniature, hyper-realistic version of "uploaded face as reference" striking a dynamic, gravity-defying dance pose, wearing matching denim attire, ripped jeans, and white sneakers. Bright natural daylight, vibrant saturation, sharp macro focus on the miniature and hand, 8k resolution, photorealistic texture, cinematic lighting. Ratio 9:16
```

[[Identity Preservation]] [[Surrealist Composite]]

---

### 68. Sadie Sink 奢华海滨阳台肖像

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-26  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana Pro 生成一张 Sadie Sink 站在豪华海滨阳台上的图像。该提示要求严格的身份一致性锁定，并指定了服装（浅粉色夏日连衣裙）、环境（碧绿海水、郁郁葱葱的植被）、光线（明亮的午间阳光）以及相机风格（智能手机写实感、Instagram 奢华旅行美学）。

![Sadie Sink 奢华海滨阳台肖像](https://cms-assets.youmind.com/media/1774594329914_udc87g_HEXPbJFbYAIdpYI.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman standing on a luxury balcony overlooking a turquoise coastal landscape, Use uploaded reference image, keep identity exact",
      "identity_lock": "strict — preserve exact facial structure, eyes, lips, nose, proportions, no alteration",
      "pose": "standing with back slightly turned toward camera, head turned over shoulder looking directly at viewer, one hand resting on railing",
      "expression": "soft confident gaze with subtle relaxed smile",
      "body": "natural proportions, elegant posture with slight arch in back",
      "hands": "one hand lightly gripping wooden railing, other relaxed near hip"
    },
    "hair": {
      "description": "Use uploaded reference image, keep identity exact — long brunette hair",
      "style": "loose flowing waves, slightly wind-swept",
      "details": "fine strands visible, natural shine under sunlight, subtle movement"
    },
    "face": {
      "description": "Use uploaded reference image, keep identity exact",
      "skin": "natural skin texture with visible pores, sun-kissed glow, no smoothing",
      "details": "soft highlights on cheekbones and nose, realistic lip texture, natural imperfections"
    },
    "attire": {
      "clothing": "light pink fitted summer dress with open back detail",
      "fabric": "soft lightweight knit or cotton blend, slightly textured, hugging natural body shape",
      "details": "thin straps, subtle cut-out at waist, natural fabric folds"
    },
    "environment": {
      "setting": "luxury coastal balcony",
      "background": "clear turquoise water, small islands, mountainous coastline, lush greenery",
      "foreground": "glass and wooden railing, large ceramic pot with vibrant pink flowers",
      "details": "sunlit terrace, high-end vacation setting"
    },
    "lighting_and_mood": {
      "lighting": "bright natural midday sunlight",
      "direction": "top-side sunlight creating strong highlights and defined shadows",
      "effects": "sunlit glow on skin, crisp shadows, reflective highlights on water",
      "mood": "luxury summer vacation, serene and confident"
    },
    "photography": {
      "camera": "smartphone camera (iPhone-style realism)",
      "lens": "24–28mm equivalent",
      "aperture": "f/2.0",
      "focus": "sharp on subject, background slightly softened",
      "depth_of_field": "moderate",
      "imperfections": "slight HDR effect, realistic exposure balance, subtle highlight clipping in sky and water"
    },
    "composition": {
      "framing": "medium-full body shot",
      "angle": "slightly above waist level",
      "crop": "subject centered with scenic background filling frame",
      "style": "Instagram luxury travel aesthetic"
    },
    "quality": {
      "resolution": "ultra high",
      "realism": "extreme photorealism",
      "details": "
```

[[Identity Preservation]] [[Sadie Sink]]

---

### 69. 梅根·福克斯 车内 鲜花 抓拍

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-26  **Language**: en

> 一个高度详细的 JSON 提示词，用于 Nano Banana 2 生成一张 Megan Fox 坐在车里手捧一束鲜花的自然、温暖、夏日风格的生活照。它强调严格的身份锁定、自然的皮肤纹理、强烈的自然阳光，以及特定的相机设置（iPhone 风格的真实感，26 毫米镜头）。它要求上传一张参考图片以保留身份。

![梅根·福克斯 车内 鲜花 抓拍](https://cms-assets.youmind.com/media/1774594319641_e9kovm_HEXK99kbYAIFXnG.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman sitting in the passenger seat of a car holding a bouquet of flowers, Use uploaded reference image, keep identity exact",
      "identity_lock": "strict — preserve exact facial features, eyes, lips, nose, bone structure, no alterations",
      "pose": "seated sideways in car seat with legs slightly bent, leaning back comfortably, one arm raised shielding eyes from sunlight",
      "expression": "soft warm smile, relaxed and natural, slightly squinting due to sunlight",
      "body": "natural proportions, relaxed posture",
      "hands": "one hand holding bouquet of flowers, other hand raised above forehead blocking light"
    },
    "hair": {
      "description": "Use uploaded reference image, keep identity exact — long dark brown hair",
      "style": "natural loose waves, slightly tousled",
      "details": "fine strands visible, subtle frizz, realistic shine under sunlight"
    },
    "face": {
      "description": "Use uploaded reference image, keep identity exact",
      "skin": "natural skin texture with visible pores, slight glow from sunlight, no smoothing",
      "details": "soft natural highlights on cheekbones and nose, realistic under-eye texture"
    },
    "attire": {
      "clothing": "light cream or white lace long-sleeve top with delicate texture",
      "fabric": "semi-sheer lace with visible pattern and soft folds",
      "bottom": "light blue denim jeans with natural creases",
      "accessories": "minimal gold jewelry including bracelet and necklace"
    },
    "props": {
      "flowers": "bouquet of vibrant red and pink flowers with green leaves, realistic petal texture",
      "details": "fresh natural look, slight variation in color and shape"
    },
    "environment": {
      "setting": "inside a modern car",
      "details": "light gray car interior, visible seat, window, and door frame",
      "outside_view": "green trees and sunlight filtering through leaves"
    },
    "lighting_and_mood": {
      "lighting": "strong natural sunlight coming through car window",
      "direction": "side lighting hitting face and body",
      "effects": "high contrast highlights and shadows, sun patches across face and clothing",
      "mood": "warm, summery, candid lifestyle moment"
    },
    "photography": {
      "camera": "smartphone camera (iPhone-style realism)",
      "lens": "26mm equivalent",
      "aperture": "f/1.8",
      "focus": "sharp on subject, slight softness in background",
      "depth_of_field": "moderate",
      "imperfections": "natural exposure variation, slight overexposed highlights, realistic shadow noise"
    },
    "composition": {
      "framing": "medium shot",
      "angle": "slightly above eye level",
      "crop": "upper body and legs partially visible",
      "style": "candid lifestyle photo"
    },
    "quality": {
      "resoluti"
```

[[Identity Preservation]]

---

### 70. 复古餐厅生活方式照片提示 (身份锁定)

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-26  **Language**: en

> 一个结构化的提示词，用于 Nano Banana Pro 生成一张年轻女性在一家复古美式餐厅里的生活方式照片，着重于严格的人物身份锁定、逼真的头发和皮肤细节，以及汽水、煎饼和一台复古相机等特定道具。

![复古餐厅生活方式照片提示 (身份锁定)](https://cms-assets.youmind.com/media/1774594321011_iur08b_HEWivX4aQAAxynF.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman sitting in a retro diner booth, Use uploaded reference image, keep identity exact",
      "hair": "long straight blonde hair, natural shine, slight strand separation, subtle flyaways, realistic density",
      "face": "Use uploaded reference image, keep identity exact — playful expression with one eye winking, slight smile while drinking, visible pores, natural skin texture, no smoothing",
      "body": "fit natural proportions, relaxed seated posture, one arm resting along booth back"
    },
    "attire": {
      "clothing": "black athletic crop top and matching shorts, fitted, matte fabric with slight stretch and natural folds",
      "accessories": "minimal gold bracelet, subtle jewelry"
    },
    "styling_and_accessories": {
      "props": [
        "glass of soda with ice and straw",
        "retro diner plate with pancakes and bacon",
        "glass of water",
        "vintage compact camera on table"
      ]
    },
    "environment": {
      "setting": "retro American diner",
      "details": "green leather booth seating, chrome-edged table, napkin holder, condiments, large window with street view and parked vehicles",
      "background": "slightly blurred outdoor street with truck and people, palm trees visible"
    },
    "pose": {
      "posture": "sitting casually in booth",
      "arms": "one arm resting on booth, other holding drink",
      "expression": "winking, playful, candid lifestyle moment"
    },
    "lighting_and_mood": {
      "lighting": "bright natural daylight from window, mixed with indoor ambient lighting",
      "effects": "soft shadows, highlights on skin and glass reflections, realistic contrast",
      "mood": "casual, lifestyle, sunny and relaxed"
    },
    "camera_and_technical": {
      "style": "lifestyle photography with smartphone or mirrorless look",
      "lens": "35mm equivalent",
      "aperture": "f/2.2",
      "quality_tags": [
        "high resolution",
        "natural depth of field",
        "realistic skin texture",
        "authentic lighting",
        "slight lens imperfections"
      ]
    }
  }
}
```

[[Identity Preservation]]

---

### 71. 九宫格竖版编辑布局，猫咪主题，适用于 Nano Banana Pro

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-26  **Language**: en

> 给 Nano Banana Pro 的一个高度具体的提示，用于生成一个 3x3 的编辑肖像网格，要求严格保留上传女性在所有面板中的身份，展示她与一只逼真的蓝眼睛白色范猫亲密互动，背景设在一个光线柔和的干净简约工作室中。

![九宫格竖版编辑布局，猫咪主题，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1774594331898_pcosnb_HEWh3AvXoAA2LEy.jpg)

```
Use the uploaded woman as the exact subject. Keep her face, skin tone, proportions, and natural beauty identical. Create a 3x3 editorial portrait grid where she appears in all panels with subtle but professionally styled pose variations. She is holding and interacting lovingly with a small white Van cat with bright blue eyes. The cat must look adorable, elegant, calm, and photorealistic. The interactions should feel affectionate, natural, and editorial, including gentle cuddling, kissing the cat, holding it close, and soft cheek-to-fur contact.

Subject: Same woman from reference image with long straight brunette hair, natural flow, consistent across panels. Soft natural glam, glowing skin, neutral lips, defined eyes. Minimal white tank top and light blue jeans, unchanged across all panels. Small fluffy white Van cat with vivid blue eyes, elegant face, soft fur, photorealistic, anatomically correct, consistent across panels.

Scene: Clean minimal studio with soft neutral background. Soft daylight, diffused, even skin illumination. Intimate, calm, warm, affectionate, natural, effortless beauty.

Panel directions: panel_1 - holding the white blue-eyed Van cat close to her chest, face near the cat, soft affectionate expression; panel_2 - direct eye contact with camera while gently cradling the cat in her arms, calm editorial pose; panel_3 - looking lovingly at the cat, cheek softly touching its fur, intimate and tender moment; panel_4 - kissing the cat gently on the head, elegant posture, soft emotional beauty portrait; panel_5 - hero center pose, holding the cat securely and naturally, confident and warm editorial composition; panel_6 - slight smile while hugging the cat close, relaxed shoulders, soft luxury portrait feeling; panel_7 - three-quarter profile, cat nestled in her arms, graceful neck line, refined magazine-style composition; panel_8 - chin slightly lifted, cat close to her shoulder, poised and elegant gaze, affectionate but polished; panel_9 - soft turn toward camera while cuddling the cat, serene expression, intimate final frame.

Pose language: very subtle, refined model-like shifts only. Soft, confident, loving, elegant expression. Natural and gentle hands, securely supporting the cat with realistic hand placement. Elongated neck, relaxed shoulders, subtle editorial asymmetry. Gentle cuddling, soft kissing, cheek contact, loving embrace, calm cat handling.

Camera: 85mm portrait lens, close-up to mid shot framing, eye-level angle, sharp focus on eyes, skin texture, and cat fur detail, soft background blur depth of field.

Output style: clean_beauty_editorial, ultra_skin_detail sharpness, very_subtle grain, soft_natural dynamic range, neutral_skin_tone color grade. 4:5 aspect ratio, portrait orientation, ultra_high_res resolution. 3x3 grid layout with thin gutter, no outer border, maximum_identity_lock panel consistency.

Must have: 3x3 grid, same woman in all panels, perfect identity preservation, small white blue-eyed Van cat, natural affectionate interaction with the cat, photorealistic cat anatomy and fur, natural skin texture, clean background, subtle but professional pose variations, editorial beauty portrait feeling, no text.

Negative prompt: identity change, different outfit, different cat color, extra animals, cat distortion, mutated cat face, unrealistic fur, bad anatomy, extra fingers, awkward pose, stiff expression, heavy makeup, harsh lighting, plastic skin, low quality, text, logo, watermark.
```

[[Identity Preservation]] [[Soft Studio Lighting]]

---

### 72. 自然复古照片美学 提示词 用于 Nano Banana Pro

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-26  **Language**: en

> 一份为 Nano Banana Pro 准备的详细提示词，用于生成一张在花园户外拍摄的、具有复古一次性相机风格的抓拍照片，照片主角为一位年轻女性。该照片需严格保留参考图像中的人物身份，并重点突出自然纹理、强烈阳光，以及俏皮、无忧无虑的心情。

![自然复古照片美学 提示词 用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1774594331570_wldd49_HEWd3WXbMAAFJ1g.jpg)
![自然复古照片美学 提示词 用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1774594331508_xiw69l_HEWd2SMbkAAN3f0.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman outdoors in a garden setting, Use uploaded reference image, keep identity exact",
      "hair": "long brown hair with soft natural waves, slightly messy from movement, visible strand separation, flyaways across face, realistic wind interaction",
      "face": "Use uploaded reference image, keep identity exact — joyful open-mouth expression, eyes partially closed from sunlight, visible pores, natural skin texture with slight sun glow and uneven highlights, no smoothing",
      "body": "slim natural proportions, leaning slightly forward, relaxed candid posture with natural movement"
    },
    "attire": {
      "clothing": "{argument name="clothing color" default="lavender"} fitted long-sleeve mini dress, soft stretchy fabric, visible folds and tension around torso and sleeves",
      "details": "slight wrinkling at waist and arms, realistic fabric compression"
    },
    "styling_and_accessories": {
      "accessories": [
        "small {argument name="flower color" default="purple"} flower tucked behind ear, slightly imperfect placement"
      ]
    },
    "environment": {
      "setting": "outdoor garden or park",
      "background": "green grass, tall trees with dense foliage, residential buildings faintly visible in distance, natural depth",
      "details": "sunlit patches on ground, shadows from tree branches, uneven natural terrain"
    },
    "pose": {
      "posture": "leaning forward toward camera",
      "arms": "hands loosely together near waist",
      "expression": "laughing, candid, spontaneous moment"
    },
    "lighting_and_mood": {
      "lighting": "strong natural sunlight filtering through trees, mixed light and shadow patches",
      "effects": "harsh highlights on face and hair, dappled shadows, slight overexposure in bright areas",
      "mood": "playful, carefree, nostalgic candid"
    },
    "camera_and_technical": {
      "style": "vintage disposable camera aesthetic",
      "lens": "28mm equivalent",
      "aperture": "f/2.8",
      "quality_tags": [
        "film grain",
        "slight motion blur",
        "soft focus edges",
        "color shift",
        "light leaks subtle",
        "authentic analog feel"
      ]
    }
  }
}
```

[[Identity Preservation]] [[Natural Texture]] [[Strong Sunlight]]

---

### 73. 地铁站台抓拍人像

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-26  **Language**: en

> 一个 JSON 提示，用于生成一张在地铁站台上的年轻女性的抓拍式超现实街头摄影图像。该提示侧重于城市光线、逼真的织物纹理（蕾丝半身裙、修身背心），以及一个特定的回头姿势，并通过参考图片保持精确的身份一致性。

![地铁站台抓拍人像](https://cms-assets.youmind.com/media/1774594341488_ijk3ko_HEWcfilbYAIFqxW.jpg)
![地铁站台抓拍人像](https://cms-assets.youmind.com/media/1774594341419_0bolsw_HEWcgQDaIAAKpKA.jpg)
![地铁站台抓拍人像](https://cms-assets.youmind.com/media/1774594341479_j2qltd_HEWce4AbYAA1Fkh.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman standing on a subway platform, Use uploaded reference image, keep identity exact",
      "hair": "long dark brown hair, straight with natural volume, subtle flyaways, realistic strand separation, slight movement from environment",
      "face": "Use uploaded reference image, keep identity exact — soft confident expression, slight gaze over shoulder, visible pores, natural skin texture, no smoothing",
      "body": "slim natural proportions, relaxed posture with slight torso twist, realistic weight distribution"
    },
    "attire": {
      "top": "white fitted tank top, soft fabric with slight stretch and natural folds",
      "bottom": "white lace layered skirt with semi-sheer texture, intricate floral patterns, realistic transparency and fabric layering",
      "accessories": "black shoulder bag with leather texture, shopping bags in hand, subtle jewelry"
    },
    "environment": {
      "setting": "subway station platform",
      "background": "metal subway train with visible doors, signage, and numbering, American flag decal, fluorescent ceiling lights, tiled platform",
      "details": "yellow safety strip, industrial textures, reflections on metal surfaces"
    },
    "pose": {
      "posture": "standing with back slightly turned toward camera",
      "head": "looking over shoulder toward camera",
      "arms": "one arm holding shopping bags, other supporting shoulder bag",
      "expression": "calm, slightly posed candid look"
    },
    "lighting_and_mood": {
      "lighting": "overhead fluorescent lighting, cool-toned, even illumination with slight shadows under chin and body",
      "effects": "subtle reflections on train metal, soft highlights on hair and skin",
      "mood": "urban lifestyle, candid, modern"
    },
    "camera_and_technical": {
      "style": "smartphone street photography",
      "lens": "28mm equivalent",
      "aperture": "f/2.0",
      "quality_tags": [
        "high resolution",
        "natural depth of field",
        "slight motion realism",
        "realistic skin texture",
        "urban lighting accuracy"
      ]
    }
  }
}
```

[[Identity Preservation]]

---

### 74. 富有表现力的 专题肖像网格，并保留身份

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-26  **Language**: en

> 一个高度结构化的 JSON 提示，用于 Nano Banana 2，旨在创建一个 3x3 的编辑肖像网格（图生图模式），具有柔和、感性、高级时尚的美学风格。它要求严格保留参考图像中的身份特征，并指定了九种不同的面板构图，重点关注面部和手部互动。

![富有表现力的 专题肖像网格，并保留身份](https://cms-assets.youmind.com/media/1774594337734_lpx3e2_HEWRxKxWsAAIAHr.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "Nano Banana 2",
      "task_type": "face_focused_sensual_editorial_grid",
      "language": "en",
      "priority": "highest"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Use the uploaded image as the facial reference. Maintain consistent identity across all panels while creating a photoreal 3x3 editorial portrait grid with a soft, sensual, high-fashion aesthetic. Focus on subtle emotional variation, refined expressions, and natural interaction between face and hands. Keep the composition minimal, elegant, and visually cohesive."
    },

    "output_settings": {
      "aspect_ratio": "1:1",
      "orientation": "square",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "layout": {
        "type": "grid",
        "rows": 3,
        "cols": 3,
        "gutter": "thin",
        "outer_border": "none",
        "panel_consistency": "maximum"
      },
      "render_style": "soft_luxury_editorial_realism",
      "sharpness": "skin_detail_high",
      "grain": "very_subtle_film",
      "dynamic_range": "soft_natural",
      "color_grade": "warm_daylight_neutral"
    },

    "subject": {
      "identity": "consistent facial identity from reference",
      "hair": "soft natural brunette hair, loosely styled, consistent across panels",
      "makeup": "sensual editorial makeup with natural skin glow, defined eyes, deep rose or red lips",
      "outfit": "black minimal thin-strap top with sheer long gloves",
      "styling": "clean, minimal, intimate editorial"
    },

    "pose_language": {
      "direction": "close-up and medium close-up compositions centered on face and hands",
      "movement": "subtle, controlled, natural transitions",
      "expression": "calm, confident, slightly mysterious",
      "hands": "soft interaction with face, chin, cheeks, lips, and neck"
    },

    "panel_direction": {
      "panel_1": "side gaze with chin resting on hand",
      "panel_2": "direct gaze with relaxed shoulders",
      "panel_3": "soft smirk with composed posture",
      "panel_4": "head tilt with fingers touching cheek",
      "panel_5": "centered pose with chin supported by hand",
      "panel_6": "both hands framing the face",
      "panel_7": "side profile with hands near shoulders",
      "panel_8": "hands under chin with lifted gaze",
      "panel_9": "gentle turn toward camera with refined expression"
    },

    "camera": {
      "lens": "85mm portrait lens",
      "framing": "tight portrait and medium close-up",
      "angle": "eye-level editorial",
      "focus": "sharp on eyes and skin texture",
      "depth_of_field": "soft background blur"
    },

    "lighting": {
      "type": "soft natural daylight",
      "direction": "side-lit window light",
      "quality": "diffused, clean, flat"
    }
  }
}
```

[[Identity Preservation]] [[Image-To-Image]]

---

### 75. 雨夜车内电影感照片

**Author**: [Harboris](https://x.com/harboriis)  **Date**: 2026-03-26  **Language**: en

> 一个用于生成极具电影感和真实感照片的提示词，该照片使用上传的面部，描绘人物在夜晚坐在车内，从被雨水覆盖的车窗看出去，强调阴郁的灯光、反射和多彩的散景。

![雨夜车内电影感照片](https://cms-assets.youmind.com/media/1774594316673_mct6oo_HEWRucDboAAb65f.jpg)
![雨夜车内电影感照片](https://cms-assets.youmind.com/media/1774594316726_mzno60_HEWRuW3aUAApglB.jpg)

```
Create a highly cinematic and realistic photo of a person using the face from the uploaded image. The person is sitting inside a car at night, looking out through a rain-covered window. The camera is positioned outside the car, capturing the person through the wet glass. Raindrops and streaks of water are clearly visible on the window, with reflections of city lights, neon signs, and passing cars blending into the glass. The person’s face is softly lit by ambient street lights and subtle interior car lighting, creating a moody and emotional expression. The background outside is blurred with colorful bokeh lights (red, blue, yellow), giving a deep cinematic feel. The person is wearing a modern outfit like a hoodie or jacket. The mood feels introspective and film-like. Ultra realistic photography, shallow depth of field, dramatic lighting, reflections, rain texture, Hollywood movie scene composition, high detail.
```

[[Identity Preservation]] [[Cinematic Mood]] [[Moody Lighting]]

---

### 76. 电影感 照片：夜幕下 走出 豪车

**Author**: [Nikhil](https://x.com/NikhilRajX)  **Date**: 2026-03-26  **Language**: en

> 一个用于生成逼真电影感照片的提示词：描绘人物在夜晚从豪华轿车中走出，车头灯提供戏剧性的逆光，突出高端时尚大片的造型，并使用上传的人脸。

![电影感 照片：夜幕下 走出 豪车](https://cms-assets.youmind.com/media/1774594315691_gvq249_HEWJvkWbYAg5Ieg.jpg)

```
Create a realistic cinematic photo of a person using the face from the uploaded image. The person is stepping out of a luxury car at night with a confident and calm expression. The car door is open and bright headlights glow behind, creating a dramatic backlight. The camera angle is slightly low and close, making the person look powerful and stylish. The environment is a high-end urban setting with soft reflections on the ground, like after light rain. The person is wearing a premium outfit such as a fitted blazer or leather jacket, dark pants, and clean sneakers or shoes. Lighting is clean and controlled, with strong highlights and soft shadows. Cinematic lighting, luxury brand style, atmospheric depth, ultra realistic photography, high-end fashion campaign look.
```

[[Identity Preservation]] [[Cinematic Night Photography]]

---

### 77. 躺椅上 女子的 超写实 手机照片

**Author**: [Chryz leen](https://x.com/Chryzleenprompt)  **Date**: 2026-03-26  **Language**: en

> 一个详细、结构化的提示词，用于生成一张超现实、超清晰的照片，描绘一位年轻女性斜倚在木制躺椅上，强调数字清晰度、具体的相机设置（iPhone 15 Pro），以及详细的身体和环境描述。它需要一个用于角色外观的参考图像。

![躺椅上 女子的 超写实 手机照片](https://cms-assets.youmind.com/media/1774594335269_gjpxss_HEWISkbaYAA6ntC.jpg)

```
Use the attached reference image as a visual guide for the character’s appearance. Preserve key visual traits such as facial structure and overall proportions, while allowing small natural variations typical of real photography. The generated subject should clearly resemble the reference while remaining a natural photographic interpretation.
Aspect Ratio: 3:4.
A hyper-realistic, ultra-sharp photograph taken on a modern smartphone, specifically an iPhone 15 Pro, characterized by its digital clarity, shot at ISO 50, f/1.8. A young woman reclines on a weathered wooden lounger, her torso angled 45 degrees with a natural weight shift and one hip subtly raised. Her head tilts, resting on her right hand while her left arm is bent sharply behind her head in a mid-moment pose. She wears a voluminous 90s-style blowout with soft mermaid waves. Her expression is serene yet intrigued, featuring a micro-smirk and a smoldering gaze with one brow raised slightly. Her skin shows a healthy radiance and glass finish with visible pores. Forensic makeup includes soft winged liner, champagne shimmer, and a blurred coral lip stain. She is dressed in a pale yellow modest two-piece swimwear with ruffled off-the-shoulder sleeves and a matching sheer crinkle-fabric sarong knotted at the hip. The scene is illuminated by soft, diffused daylight, rendered in sharp focus from the wooden pier textures to the distant mountain ridges and turquoise sea, emphasizing digital texture and crisp fabric details without any bokeh.
```

[[Identity Preservation]] [[Hyperrealistic Photography]]

---

### 78. 高保真 镜面自拍 提示词

**Author**: [Danna R.](https://x.com/daaaaanc)  **Date**: 2026-03-26  **Language**: en

> 一个高度详细的提示词，针对 Nano Banana 2，旨在生成一张原始的、高保真的镜面自拍，带有 iPhone 模拟效果，强调严格的身份锁定、逼真的皮肤纹理（微孔、毳毛），以及特定的时尚细节，例如大理石纹连衣裙和金色配饰。

![高保真 镜面自拍 提示词](https://cms-assets.youmind.com/media/1774594319852_jbabuc_HEWFTyLWoAEfISU.jpg)

```
(9:16) Raw high-fidelity mirror selfie, eye-level, medium shot, iPhone 17 Pro sim, 35mm, f/2.8, sharp subject, natural grain.

Framing: Subject ~65% frame, centered in mirror, large wooden door background, slight white wall edge, ~0.6m distance.

Identity Lock: Preserve ALL facial features (structure, skin, hair, marks).
Enhancement: Natural skin clarity (visible pores), even tone, soft glow, subtle light-based contour, refined highlights (eyes/lashes/brows), salon hair.
Bio-Fidelity: Micro-pores, fine vellus hair, hydrated skin.
Expression: Confident/poised gaze into phone via mirror, lower face partially occluded by phone.

Hair: Same color/texture, long sleek waves, middle part, behind shoulders + over left shoulder, warm highlights.
Makeup: Polished (filled brows, eyeliner, mascara), neutral nails.

Accessories: Gold watch (left), layered gold necklaces, gold ring (right), beige/gold iPhone, small off-white handbag (left hand).

Outfit: Strapless rib-knit bodycon dress, abstract marble (charcoal/olive/cream), tight fit, realistic folds, defined S-curve.

Pose: Torso angled ~30° left, hips toward mirror, right hand holding phone at face level, left holding bag, natural articulation.

Mood/Color: Chic, confident; palette (mahogany, charcoal, olive, cream, gold), ~3500K warm indoor light, moderate contrast.

Environment: Indoor dressing/hallway, mahogany door w/ silver handle, white wall edge, soft overhead lighting, all sharp.
```

[[Identity Preservation]] [[Realistic Skin Texture]] [[iPhone Simulation]]

---

### 79. 时尚大片人像：紫色单色调美学

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-26  **Language**: en

> 一个详细的结构化提示词，用于 Nano Banana Pro 生成一张年轻女性的时尚大片肖像，严格保留参考图像中的身份特征，采用单色紫色奢华美学、低角度全身构图，以及柔和、梦幻的影棚灯光。

![时尚大片人像：紫色单色调美学](https://cms-assets.youmind.com/media/1774594330589_imzx1f_HEUq4OWbUAAivdj.jpg)
![时尚大片人像：紫色单色调美学](https://cms-assets.youmind.com/media/1774594330512_lf6ame_HEUq209bYAMxROp.jpg)
![时尚大片人像：紫色单色调美学](https://cms-assets.youmind.com/media/1774594330595_vv45i8_HEUq4-CbYAEDQy1.jpg)

```
{
"photo_type":"high-fashion editorial, monochrome luxury aesthetic",

"subject":{
"type":"young woman",
"use_reference_image":true,
"face_reference":true,
"preserve_identity":true,
"instruction":"strictly use the exact face from the reference image, do NOT change facial features, hair color, or eye color",
"pose":"leaning against a wall with relaxed confident posture, one leg extended forward",
"expression":"calm, confident, slightly soft dreamy look"
},

"outfit":{
"clothing":"tailored suit (blazer, trousers, tie) in {argument name="clothing color" default="purple"} tone",
"shoes":"chunky sneakers matching {argument name="clothing color" default="purple"} tone",
"style":"luxury, feminine, editorial"
},

"environment":{
"location":"minimal studio room",
"elements":[
"entire room in {argument name="clothing color" default="purple"} monochrome",
"matching {argument name="clothing color" default="purple"} car in background",
"clean geometric walls"
]
},

"color_theme":{
"primary":"rich {argument name="clothing color" default="purple"}",
"tones":"lavender to deep violet gradients"
},

"lighting":{
"type":"soft studio lighting",
"effect":"smooth highlights, soft shadows, dreamy glow"
},

"camera":{
"angle":"low angle",
"framing":"full body",
"focus":"sharp subject, clean background"
}
}
```

[[Identity Preservation]] [[Fashion Editorial]]

---

### 80. Nano Banana 2 的 电影风格 破损时钟 场景肖像

**Author**: [Nikhil](https://x.com/NikhilRajX)  **Date**: 2026-03-26  **Language**: en

> 给 Nano Banana 2 的提示词：生成一张极具电影感、超逼真的照片。照片主体为一个人物（其身份与上传图片保持一致），自信地站立在一个巨大的破损时钟结构中。画面以戏剧性的金色光线和深邃的阴影为特色，营造出史诗般的时间主题氛围。

![Nano Banana 2 的 电影风格 破损时钟 场景肖像](https://cms-assets.youmind.com/media/1774594333244_cz7tjs_HEUXmZtawAANdRX.jpg)

```
Create a highly cinematic, realistic photo of a person using the face from the uploaded image. The person is standing confidently inside a massive broken clock structure, like something from a Hollywood movie. Giant cracked clock walls surround the scene, with large floating gears, broken Roman numerals, and pieces of the clock suspended in the air. Warm golden light shines through the cracks, creating dramatic light rays and deep shadows. Dust particles float in the air, adding atmosphere. The camera angle is slightly low and wide, making the person look powerful and central in the frame. The person is wearing a stylish cinematic outfit such as a long coat, fitted pants, and boots. The mood is epic, mysterious, and time-themed. Ultra realistic, dramatic lighting, cinematic color grading, atmospheric depth, 8k, movie-scene composition, Hollywood style.
```

[[Identity Preservation]] [[Cinematic Portrait]] [[Deep Shadow]]

---

### 81. 白色国际标准舞 编辑网格 (2x2)

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-25  **Language**: en

> 一个用于生成超写实 2x2 编辑网格的结构化提示，描绘一位在所有画面中保持面部特征一致的优雅女性。她的造型是一位现代公主，身着奢华的白色刺绣舞会礼服，戴着皇冠和歌剧手套，背景是明亮的白色极简风格，展示着各种优雅的舞姿。

![白色国际标准舞 编辑网格 (2x2)](https://cms-assets.youmind.com/media/1774508270117_g7n36q_HESb6uQa8AAxalG.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "white_ballroom_dance_editorial_2x2_grid",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_WHITE_PRINCESS_DANCE_GRID"
    },
    "input": {
      "mode": "text_to_image",
      "notes": "Create a photoreal 2x2 editorial grid featuring one elegant adult woman across four panels. She should have the same facial identity in all four panels and appear like a modern princess in a grand white gown with a tiara and long white opera gloves. The dress should be a luxurious off-shoulder or strapless white ball gown with delicate floral embroidery, soft green vine-like detailing, couture volume, and regal movement. The mood should feel joyful, graceful, romantic, and refined, inspired by a royal ballroom dance moment. Every panel should show a different dance-related pose or candid movement, but the woman must remain the same. The background in all four panels must be bright white or very pale ivory, clean and elegant, with no dark ballroom background. Keep the result airy, luminous, aristocratic, and timeless."
    },
    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "layout": {
        "type": "grid",
        "rows": 2,
        "cols": 2,
        "gutter": "thin",
        "outer_border": "none",
        "panel_consistency": "very_high"
      },
      "render_style": "luxury_editorial_realism",
      "sharpness": "editorial_crisp",
      "grain": "subtle_film",
      "dynamic_range": "soft_bright_natural",
      "color_grade": "ivory_white_royal"
    },
    "subject": {
      "identity": "one woman with highly consistent facial features across all four panels",
      "hair": "sleek elegant updo with a refined tiara",
      "outfit": "luxurious white embroidered ball gown with delicate floral and vine details, voluminous skirt, white opera gloves",
      "beauty": "fresh regal makeup, luminous skin, soft defined eyes, elegant smile"
    },
    "scene": {
      "environment": "bright white or pale ivory editorial background, minimal and clean",
      "mood": "romantic, royal, joyful, graceful, refined"
    },
    "panel_direction": {
      "panel_1": "joyful dance pose with both arms raised elegantly, open smile, gown moving beautifully",
      "panel_2": "graceful seated or paused portrait in the gown, soft regal smile, calm elegant presence",
      "panel_3": "leaning forward slightly with playful royal warmth, gloves visible, full skirt spread around her",
      "panel_4": "refined dance-inspired pose with soft movement in the shoulders and gown, poised smile and princess energy"
    },
    "camera": {
      "framing": "mixed three-quarter and full gown portraits",
      "angle": "clean editorial fashion angles",
      "focus": "sharp on face, tiara, embroidery, glove details, and "
    }
  }
}
```

[[Identity Preservation]] [[2x2 Grid]]

---

### 82. 大学生学习场景抓拍照片提示

**Author**: [afig](https://x.com/afigpimp)  **Date**: 2026-03-25  **Language**: en

> 一个详细的 JSON 提示词，用于 Nano Banana Pro 生成一张超写实、8K、竖版抓拍照片，内容为一名大学生运动员在大学图书馆深夜学习，模仿原始 iPhone Snapchat 快拍的风格。

![大学生学习场景抓拍照片提示](https://cms-assets.youmind.com/media/1774508278536_7awzit_HERsmlNX0AAcino.jpg)

```
{
  "meta": {
    "aspect_ratio": "9:16",
    "quality": "ultra_photorealistic",
    "resolution": "8k",
    "camera": "iPhone 16 rear camera",
    "lens": "24mm wide",
    "style": "raw iphone candid realism, natural handheld photo texture, authentic Snapchat story vibe"
  },
  "scene": {
    "location": "university library study area",
    "environment": ["wooden study table", "open textbooks and highlighters", "laptop with notes", "coffee cup", "quiet library background with bookshelves"],
    "atmosphere": "casual late-night studying session"
  },
  "lighting": {
    "type": "warm overhead library lights mixed with laptop glow",
    "effect": "soft even illumination with gentle shadows"
  },
  "camera_perspective": {
    "pov": "candid over-the-shoulder shot",
    "angle": "slightly high angle",
    "distance": "medium shot showing hands and desk",
    "framing": "vertical 9:16 story format"
  },
  "subject": {
    "pose": "sitting at desk, one hand holding phone taking the photo, other hand resting near notebook",
    "outfit": "grey cropped hoodie and black athletic shorts",
    "details": "natural college athlete studying after practice"
  },
  "image_quality": {
    "focus": "sharp on foreground desk items with natural depth",
    "realism": "looks like a real casual iPhone photo posted on Snapchat story"
  }
}
```

[[Identity Preservation]] [[iPhone Aesthetic]]

---

### 83. 未来主义时尚专题提示词，身份保留

**Author**: [Nawal](https://x.com/nawalsehar)  **Date**: 2026-03-25  **Language**: en

> 一个结构化的 JSON 提示词，用于 Gemini Nano Banana Pro 生成一张未来主义时尚大片图像。该提示词详细说明了风格、身份特征保留要求（通过上传图片来保留面部和发型）、主体细节、服饰、环境、光照以及期望的输出质量。

![未来主义时尚专题提示词，身份保留](https://cms-assets.youmind.com/media/1774421487536_049c0v_HEN9JIjbUAA1N1q.jpg)

```
{
 "type": "image_generation_prompt",
 "style": "fashion editorial x futuristic",
 "identity_preservation": {
 "use_uploaded_image": true,
 "alter_face": false,
 "notes": "Use the same face and hairstyle from the uploaded photo. Do not change facial features or facial expression."
 },
 "subject": {
 "gender": "female",
 "pose": {
 "position": "seated",
 "posture": "elegant and relaxed",
 "expression": "unchanged from the reference image"
 }
 },
 "wardrobe""top": "oversized white sweatshirt",
 "bottoms": "cloudy blue oversized combat jeans",
 "footwear": "cloudy blue neutral sneakers or Nike sneakers",
 "socks": "white ribbed socks"
 },
 "environment": {
 "setting": "studio",
 "background": {
 "color": "muted sky-blue tone",
 "style": "clean, minimalist"
 }
 },
 "lighting": {
 "type": "soft cinematic glow",
 "effects": [
 "highlights skin texture",
 "enhances fabric textures"
 ]
 },composition": {
 "style": "editorial",
 "focus": "model-centered with balanced framing"
 },
 "quality": {
 "realism": "photorealistic",
 "detail_level": "high detail in skin and fabric"
 },
 "output_goal": "Create a futuristic fashion editorial image of a woman seated with a relaxed posture in a sky-blue studio environment, preserving her exact facial identity and expression from the reference photo."
}
```

[[Identity Preservation]] [[Studio Lighting]] [[Fashion Editorial]] [[JSON Prompt Format]]

---

### 84. 露背丝绸连衣裙 照片提示

**Author**: [Iqra Saifi](https://x.com/IqraSaifiii)  **Date**: 2026-03-24  **Language**: en

> 一个详细的 Nano Banana 2 提示词，用于生成一张高分辨率、高对比度的人物照片 (基于参考图像)，照片中人物身穿优雅的露背丝绸连衣裙，倚靠在粗糙的石质台面旁。该提示词强调保留人物的身份特征、丝绸的质感，并采用黑色电影/时尚杂志风格的灯光。

![露背丝绸连衣裙 照片提示](https://cms-assets.youmind.com/media/1774421472791_64ccqq_HEMjiutboAAt1_7.jpg)

```
Create the person from the reference image from the photo, without changing her face, features, appearance, age, and individuality. She is in an elegant evening dress with an open back, the fabric emphasizes thin skin with a natural glow, folds and the luster of silk give depth. Leans on an unprocessed stone counter with a rough texture contrasting with the dress and skin. The muted lounge light creates soft shadows, emphasizing the curves of the back and the transitions of light on the dress and stone. Hair in a bun with loose strands, giving sophistication and restraint. A long sparkling diamond earring descends down the back, catching the light and creating a shimmer. high resolution photo with grainy film texture and high contrast, in the style of classic noir and fashion editorial photography, with a cold deep visual style. light enhances the person from the reference image looks half-turned, looking back. Strictly preserve the face, identity and natural appearance of the person from the reference image from the original. Mega-drawn skin every pore color photo
```

[[Identity Preservation]] [[Fashion Magazine Style]] [[Fabric Texture Detail]] [[Film Noir Lighting]]

---

### 85. 角色参考表，确保一致性

**Author**: [Atlas Cloud](https://x.com/atlas_cloud_ai)  **Date**: 2026-03-20  **Language**: en

> 这是一个为 Nano Banana 2 设计的高度结构化提示，旨在根据上传的图像创建专业的角色参考表，确保在 AI 视频生成中，多个视图（正面、侧面、背面和特写）之间保持完美的身份一致性。

```
Create a professional character reference sheet based strictly on the uploaded reference image. Use a clean, neutral plain background and present the sheet as a technical model turnaround while matching the exact realistic visual style of the reference (same realism level, rendering approach, texture, color treatment, and overall aesthetic). Arrange the composition into two horizontal rows. Top row: four full-body standing views placed side-by-side in this order: front view, left profile view (facing left), right profile view (facing right), back view. Bottom row: three highly detailed close-up portraits aligned beneath the full-body row in this order: front portrait, left profile portrait (facing left), right profile portrait (facing right). Maintain perfect identity consistency across every panel. Keep the subject in a relaxed A-pose and with consistent scale and alignment between views, accurate anatomy, and clear silhouette; ensure even spacing and clean panel separation, with uniform framing and consistent head height across the full-body lineup and consistent facial scale across the portraits. Lighting should be consistent across all panels (same direction, intensity, and softness), with natural, controlled shadows that preserve detail without dramatic mood shifts. Output a crisp, print-ready reference sheet look, sharp details.
```

[[Identity Preservation]] [[Character Reference Sheet]] [[Character Design Sheet]]

---

### 86. 高速赛博朋克电影场景提示

**Author**: [Edizkan ⭕🦇](https://x.com/edizkan_)  **Date**: 2026-03-18  **Language**: en

> 一个高度详细、多部分的提示，旨在将上传的角色参考转化为雨水湿滑的赛博朋克街道上的照片级真实感、高速电影场景，强调严格的身份保留、特定的摄像机角度和动态姿势强制，推荐用于 Nano Banana 2 (Thinking Mode)。

![高速赛博朋克电影场景提示](https://cms-assets.youmind.com/media/1773902657351_abdtvq_HDs0C91XYAAH6Jw.jpg)

```
A cinematic speed-motion shot of the uploaded reference character captured mid-slide on a rain-slicked, neon-drenched cyberpunk street. The focus is equally on the reflection and the character, forming a dual-layer composition. Likeness Preservation (CRITICAL): Maintain exact proportions, eye shape, spacing, stylization, silhouette, and material identity from the reference. Do not humanize. Do not reinterpret anatomy. Do not modify facial structure. Identity must remain perfectly intact and instantly recognizable. 2D to 3D Translation (ONLY if input is 2D artwork): If the uploaded reference is 2D (illustration, anime, flat graphic, cel-shaded), convert it into a fully realized 3D cinematic form while preserving exact identity fidelity. Maintain exact head shape, eye design, spacing, and proportions. Preserve original stylization, do NOT add realism that alters design language. Translate linework into subtle surface geometry or shading transitions. Keep original colors, expressed through physically believable materials. Convert flat shading into controlled cinematic light falloff. The result must feel physically real, not redesigned. Camera & Perspective: Ultra-low angle, camera positioned just centimeters above the wet pavement. Lens: 18–20mm ultra-wide. Slight Dutch tilt (5–10 degrees) to destabilize the frame. Front three-quarter perspective. One limb or body part must be closer to the lens, creating perspective pressure. Composition (Reflection Dominance): The character slices diagonally across the upper half of the frame. The lower half is dominated by a sharp but slightly distorted reflection. Vertical neon signs in the background must mirror into the wet ground, forming strong graphic lines. The composition must feel off-balance and tension-driven, not centered or stable. Pose Enforcement (CRITICAL — OVERRIDE ALL DEFAULT STANCES): The character must NOT be upright, balanced, or casually sliding. The pose must represent loss of balance under high speed. The torso is pitched aggressively forward, close to the ground. One limb forcefully contacts the wet surface, creating splash and friction. The opposite limb extends outward or backward, fully stretched for counterbalance. Legs are asymmetrical: one trailing, one collapsing or stepping incorrectly. Spine forms a diagonal or curved line, never vertical. Head leads the motion slightly ahead of the torso. Weight Distribution: Weight is NOT centered. It collapses toward the contacting limb and forward motion. Ground Interaction (MANDATORY): Water splashes outward from impact points. Friction streaks beneath sliding limb. Surface tension visibly disturbed. Energy Read: The pose must feel like mid-fall recovery, evasive maneuver at high speed, barely controlled momentum. NOT clean skating, surfing, balanced glide, or upright slide. Perspective Amplification: At least one limb must appear larger due to proximity to the lens, enhancing speed and aggression. Motion & Blur: Directional motion blur trailing from the lowest moving limbs. Sharp focal plane on the face or upper torso. Background and trailing limbs fall into controlled blur. Lighting & Color (Cyberpunk Neon): Hard directional neon lighting from off-screen vertical sources. Color palette: deep cyan, magenta, electric yellow. Lighting behavior: sharp highlights on wet surfaces, strong rim light separating silhouette, deep shadow pockets. No flat lighting. Surface Detail (Hyper-Reflective): Wet pavement must feel physically real: mirror-like reflections with ripple distortion, micro scratches and pooling water, subtle rain impact patterns. Character materials slightly darkened from moisture. Atmosphere: Heavy rain and mist in the background. Volumetric light beams cutting through haze. Dense air perspective. Foreground may include subtle water droplets or mist near lens for depth. Emotion: Urgency. Instability. High-stakes motion. The character is either escaping or chasing. Negative Constraints: No centered composition. No upright balanced pose. No clean symmetrical stance. No dry surfaces. No flat reflections. No studio lighting. No evenly sharp full-frame clarity. No static posture. Background Pixel Wall Art (Depth-Controlled): Replace the LED sign with a weathered wall-mounted pixel-art mural or printed panel of the character. The pixel version must preserve silhouette and identity but appear faded, worn, and partially damaged. Printed or painted on a rough wall surface, not glowing like a screen. Subtle grime, scratches, peeling, or moisture distortion. Colors desaturated and affected by environment. Depth Control (CRITICAL): Must sit clearly in the background plane. Slightly obscured by haze, rain, or foreground motion. Edges softened, not crisp. Reduced contrast compared to main subject. Lighting Integration: Does NOT emit light. Only receives ambient neon spill. Partially falls into shadow. Pixel Art Identity Lock (CRITICAL): The pixel-art version must be a direct downscaled translation of the original character, not a reinterpretation. Preserve exact silhouette, head shape, and proportions. Preserve exact eye shape and spacing in simplified pixel form. Use the same facial structure logic — do NOT invent or add features. STRICT PROHIBITIONS: No added nose. No added mouth. No added facial features that do not exist in the original. No stylization drift toward generic pixel characters. If the original character has a minimal or abstract face, the pixel version must remain equally minimal. Foreground Chaos Layer (CRITICAL – DEPTH & IMMERSION): Introduce aggressive near-lens elements that partially obstruct the frame and enhance depth. Near-Lens Elements: Water droplets, splashes, or streaks crossing very close to the camera. Out-of-focus rain particles catching neon light. Small debris or mist fragments passing across the lens plane. These elements must feel physically between the viewer and the character, not part of the background. Depth Behavior (MANDATORY): Foreground elements are heavily out of focus due to proximity. Large soft bokeh shapes or streaks may partially cover edges of the frame. Some elements may briefly occlude parts of the character or reflection. The frame must feel layered: foreground chaos, main subject, background environment. Lens Interaction (IMPORTANT): Subtle water streaks or droplets may appear on the lens surface. Slight distortion or refraction through droplets is allowed. Effects must remain minimal and believable, never covering the focal subject completely. Lighting Interaction: Foreground particles catch neon light (cyan, magenta, yellow). Creates glowing streaks or soft colored flares. Adds dimensional separation between planes. Composition Impact: Frame edges may feel dirty or partially blocked. The image should NOT feel clean or perfectly framed. Slight visual interference is intentional. Emotion: The viewer feels inside the scene, not watching it. ar 16:9
```

[[Identity Preservation]] [[Neon Lighting]] [[Character Transformation]] [[Dynamic Pose]]

---

### 87. Nano Banana Pro 2.0 旧照片修复提示词

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-12  **Language**: en

> 一个用于 Nano Banana Pro 2.0 的提示，旨在将上传的旧照片修复并着色为晶莹剔透、照片般逼真、高细节的图像，同时严格保留原始构图、姿势和身份。

![Nano Banana Pro 2.0 旧照片修复提示词](https://cms-assets.youmind.com/media/1773383494977_4ddjzt_HDPnhk_bQAQAFBq.jpg)
![Nano Banana Pro 2.0 旧照片修复提示词](https://cms-assets.youmind.com/media/1773383495170_mscfq3_HDPnhkZW0AAptjv.jpg)

```
Restore and colorize the uploaded old photograph into a crystal-clear, photorealistic, high-detail image while preserving 100% of the original composition. Keep the exact same pose, expression, facial structure, proportions, framing, clothing, hairstyle, background, objects, and all details unchanged. Do not add, remove, move, or restyle anything. Remove blur, noise, scratches, fading, stains, and age-related damage. Recover natural sharpness, fine skin texture, realistic textures, true-to-life colors, and lifelike skin tones. No identity change, no stylization, no cartoon or CGI look, no plastic skin.
```

[[Identity Preservation]] [[Photorealistic Rendering]] [[Old Photo Restoration]] [[Image Enhancement]]

---

### 88. 豪华赛车运动编辑肖像（图像到图像）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-12  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana Pro，指定了一个图像到图像的任务，旨在重新创作一张豪华赛车运动主题的时尚年轻女性编辑肖像，重点是保留身份、姿势和面部特征，同时将场景设定在一个迷人的赛车维修区展厅中。

![豪华赛车运动编辑肖像（图像到图像）](https://cms-assets.youmind.com/media/1773383472201_j0u6f6_HDPBQ5OXAAA-Sp1.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "luxury_motorsport_editorial_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_RED_MOTORSPORT_GIRL_EDITORIAL"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_pose": true,
      "notes": "Recreate the same glamorous motorsport event portrait with a luxury race paddock showroom atmosphere. Keep the same woman identity, same over-the-shoulder pose, same confident feminine expression, and the same high-end racing aesthetic."
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "render_style": "luxury_event_editorial",
      "sharpness": "editorial_crisp",
      "grain": "subtle_clean",
      "color_grade": "warm_indoor_event_tones",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },

    "scene": {
      "environment": "luxury motorsport showroom or Formula racing event space, polished floor, race car display, large glass windows, warm ambient lighting, upscale event atmosphere",
      "lighting": "soft warm indoor event lighting with realistic reflections on the car and accessories, no harsh flash",
      "mood": "glamorous, sporty, exclusive, chic"
    },

    "subject": {
      "description": "one stylish young woman with realistic proportions and refined feminine beauty",
      "skin": "fresh realistic skin texture",
      "hair": "soft shoulder-length blonde waves",
      "makeup": "soft glam makeup, defined lashes, clean skin, satin nude lips",
      "expression": "subtle playful confident look over the shoulder"
    },

    "wardrobe": {
      "outfit": "sleek red fitted sleeveless top, dark high-waisted denim jeans",
      "accessories": "red motorsport cap, glossy red shoulder bag, gold watch, event lanyard",
      "styling": "modern feminine race-day luxury aesthetic"
    },

    "pose": {
      "details": "woman standing beside the race car, body turned sideways, looking back over her shoulder toward camera, one hand near the jeans pocket, elegant posture"
    },

    "camera": {
      "lens": "85mm portrait lens",
      "angle": "eye-level editorial angle",
      "framing": "medium full-body portrait with the race car clearly visible behind her",
      "depth_of_field": "shallow but subject and key car details remain sharp"
    },

    "quality_control": {
      "identity_consistency": "maximum",
      "anatomy_accuracy": "maximum",
      "face_priority": "very_high",
      "hands_priority": "high",
      "prop_integrity": "high",
      "avoid": [
        "extra fingers",
        "missing fingers",
        "warped hands",
        "distorted face",
        "plastic sk
```

[[Identity Preservation]] [[Cinematic Portrait]] [[High Fashion Editorial]] [[Image-To-Image Generation]]

---

### 89. 极简侧面肖像，保持角色一致性

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-03-10  **Language**: en

> 一个针对 Google Gemini Nano Banana Pro 的详细提示，重点在于在改变场景和氛围的同时，保持参考照片中精确的面部特征和表情。该提示描述了一个极简主义、内省的侧面肖像，背景是深色混凝土墙，人物身着单色冬季街头服饰，采用柔和、冷色调的影棚灯光，营造出一种杂志风格的美感。

![极简侧面肖像，保持角色一致性](https://cms-assets.youmind.com/media/1773210657434_2vop3i_HDAruu8aMAAHZt_.jpg)
![极简侧面肖像，保持角色一致性](https://cms-assets.youmind.com/media/1773210657511_tmifd8_HDAru-JaMAEfQEB.jpg)

```
MAIN SUBJECT (IDENTITY)

Use the person from the reference photo as the main subject. Keep their exact facial features, hairstyle, skin tone, and expression perfectly unchanged preserve all realism, emotional depth, and subtle facial lighting. Allow changes only in camera position, background motion, and atmosphere. A minimalist side-profile portrait of a new person, framed from the chest up and positioned in strict profile against a textured dark concrete wall (approx. #282F32). The pose remains relaxed and composed, with the subject facing left, eyes gently closed or lowered, maintaining a calm, introspective expression. Style the subject in monochromatic, winter-inspired streetwear: a black beanie, thin metal-frame glasses, and a high-collar or turtleneck layered under a heavy textured coat. Use soft, diffused natural lighting from above and slightly in front, with a cool temperature around 4800K, creating gentle shadows that sculpt the jawline and highlight the contours of the face without harsh contrast. Emphasize the velvety matte textures of the clothing and the subtle grain of the wall. Background remains static and uniform, allowing the subject's silhouette to stand out cleanly. Use a shallow depth of field with a medium portrait lens (50-85mm) to maintain crisp facial detail while softly separating the subject from the background. Color palette rooted in deep blacks, muted grays, and natural skin tones. Mood calm, intimate, and urban-modern, with a clean editorial aesthetic. Editorial, modern, high-detail, cinematic composition, ultra-realistic textures, professional fashion photography style
```

[[Identity Preservation]] [[Side Profile Portrait]] [[Magazine Aesthetic]]

---

### 90. 时尚大片风格转换（图像到图像）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-08  **Language**: en

> 一个复杂且结构化的 JSON 提示，用于图像到图像的风格转换任务，旨在将参考图像转换为奢华时尚杂志的审美风格，特别是将服装改为红色紧身胸衣和高跟鞋，同时保留主体的身份和姿势。

![时尚大片风格转换（图像到图像）](https://cms-assets.youmind.com/media/1773038304844_0xb4jq_HC5a1jiWsAIwOK0.jpg)

```
{
"generation_request": {
"meta_data": {
"tool": "NanoBanana Pro",
"task_type": "fashion_editorial_style_transformation",
"language": "en",
"priority": "highest",
"version": "v1.0_RED_CORSET_EDITORIAL_GRID"
},

```
"input": {
 "mode": "image_to_image",
 "reference_image_usage": "very_high",
 "preserve_identity": true,
 "preserve_pose": true
},

"output_settings": {
 "aspect_ratio": "4:5",
 "resolution_target": "ultra_high_res",
 "sharpness": "editorial_crisp",
 "grain": "subtle_film"
 },

"scene": {
 "environment": "minimal white fashion studio background",

 "lighting": {
 "style": "clean fashion editorial lighting",
 "key_light": "large diffused softbox",
 "fill_light": "soft reflector fill",
 "contrast": "soft editorial contrast"
 },

 "camera": {
 "lens": "85mm fashion portrait lens",
 "angle": "straight-on fashion photography"
 }
},

"subject": {
 "identity": "same woman across all panels",
 "hair": "sleek tied-back hair",
 "accessories": "elegant sunglasses and gold jewelry"
},

"wardrobe_transformation": {
 "top": "{argument name="top garment" default="red sweetheart neckline corset-style crop top"}",
 "shoes": "{argument name="shoes" default="red stiletto heels"}",
 "pants": "classic blue jeans remain unchanged"
},

"style": {
 "aesthetic": "luxury fashion editorial",
 "vibe": "modern high-fashion campaign",
 "color_palette": [
 "red",
 "blue denim",
 "neutral studio tones"
 ]
},

"quality_control": {
 "preserve": [
 "pose",
 "facial identity",
 "body proportions",
 "panel composition"
 ],

 "avoid": [
 "extra limbs",
 "warped hands",
 "broken anatomy",
 "text",
 "watermark"
 ]
}
```

}
```

[[Identity Preservation]] [[Luxury Editorial]]

---

### 91. 黑马上突厥贵妇的电影肖像（图像到图像）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-08  **Language**: en

> 一个高度具体的 JSON 提示，用于在图像到图像模式下使用 Nano Banana Pro。它指示模型创建一个强大的电影感肖像，描绘一位骑在黑马上的古老突厥贵妇，要求从上传的参考图像中 100% 保留面部特征，同时将风格调整为真实的 L历史美学。

![黑马上突厥贵妇的电影肖像（图像到图像）](https://cms-assets.youmind.com/media/1773038340810_lksxsj_HC5K5yAWQAAHRln.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "historical_turkic_warrior_woman_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_OLD_TURKIC_BLACK_HORSE_FACE_LOCK"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "maximum",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Create a powerful cinematic portrait of a beautiful old Turkic noblewoman mounted on a black horse. The uploaded woman must remain the exact same person with maximum facial similarity. Keep the exact same face shape, eyes, eyebrows, nose, lips, jawline, chin, skin tone, and facial harmony. Do not turn her into a different girl. Adapt only the styling into an old Turkic steppe aesthetic with historically inspired beauty details."
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "render_style": "cinematic_historical_editorial",
      "sharpness": "editorial_crisp",
      "grain": "subtle_film",
      "color_grade": "rich_natural_cinematic",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },

    "scene": {
      "environment": "open steppe landscape with distant mountains and expansive sky, historical Turkic nomadic atmosphere",
      "horse": "majestic black horse with strong elegant build, dark mane, historically styled saddle and reins",
      "lighting": "soft natural daylight with noble cinematic highlights on face, fur, metal ornaments, and horse",
      "mood": "strong, regal, ancestral, feminine, magnetic, unforgettable"
    },

    "subject": {
      "description": "one striking old Turkic noblewoman, mounted on a black horse, elegant and powerful",
      "identity_rule": "the woman must remain the exact same person as the uploaded face reference",
      "face": "exact same face, same eye shape, same eyebrow shape, same nose bridge and nose tip, same lip shape, same chin, same jawline, same cheek structure, same skin tone, same facial proportions",
      "hair": "dark long hair styled in old Turkic inspired braids and sections, neat but slightly windswept, historically elegant and feminine",
      "makeup": "beauty styling inspired by old Turkic women, refined and natural, softly defined eyes, subtle earth-toned contour, naturally tinted lips, no modern glam exaggeration",
      "nails": "clean natural nails or softly groomed short nails appropriate for a historical old Turkic noblewoman, no modern acrylic look, no flashy modern manicure",
      "expression": "calm, strong, captivating, proud, quietly commanding"
    },

    "wardrobe": {
      "outfit": "luxurious old Turkic noblewoman attire with dark layered fabric, rich fur trim, fitted waist, structured historical silhouette, elegant nomadic warri
```

[[Identity Preservation]] [[Image to Image Mode]]

---

### 92. 奢华新娘时尚大片三联画（图像到图像）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-07  **Language**: en

> 一个高度详细的 JSON 提示，用于在图生图模式下生成一张奢华新娘时尚三联画（三幅图像），重点是保留主体的身份。它指定了主体（优雅的女性）、服装（带有戏剧性蝴蝶结的象牙色缎面高级定制礼服）、极简工作室环境、柔和的灯光，并为三幅图像中的每一幅定义了特定的视角、姿势和焦点（背视图、正视图和特写）。

![奢华新娘时尚大片三联画（图像到图像）](https://cms-assets.youmind.com/media/1772951322436_3jbhja_HC1b5R_XsAAnK2x.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "luxury_bridal_editorial_triptych",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_IVORY_SATIN_BOW_GOWN_TRIPTYCH"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true
    },

    "output_settings": {
      "aspect_ratio": "{argument name="aspect ratio" default="4:5"}",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "layout": {
        "type": "triptych",
        "rows": 1,
        "cols": 3,
        "gutter": "thin",
        "outer_border": "none",
        "panel_consistency": "very_high"
      },
      "render_style": "luxury_bridal_editorial",
      "sharpness": "editorial_crisp",
      "grain": "subtle_film",
      "color_grade": "soft_neutral_luxury",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },

    "scene": {
      "environment": "minimal luxury studio with a soft warm beige seamless background",
      "lighting": "high-end soft studio lighting with clean satin highlights and controlled elegant shadows",
      "mood": "romantic, refined, couture, timeless, sculptural"
    },

    "subject": {
      "description": "same elegant adult woman across all three panels, realistic proportions, graceful posture, refined beauty",
      "skin": "luminous realistic skin texture",
      "hair": "soft dark brown hair in an elegant loose updo with face-framing strands, slightly undone couture feel",
      "makeup": "soft luxury bridal glam, refined skin, subtle contour, defined eyes, satin nude lips",
      "expression": "calm, poised, slightly mysterious couture expression"
    },

    "wardrobe": {
      "outfit": "ivory off-shoulder liquid satin couture gown with long fitted sleeves, softly draped neckline, open back, dramatic oversized bow at the lower back, and floor-length train",
      "fabric": "high-luxury silk satin with fluid shine and heavy elegant drape",
      "details": "thigh-high slit in the front view, sculpted fit through the waist and hips, elongated train pooling on the floor"
    },

    "panel_design": {
      "panel_1": {
        "position": "left",
        "view": "back three-quarter view",
        "pose": "woman turned partly over her shoulder toward camera, showing the open back and oversized satin bow, one arm relaxed, elegant spine line",
        "focus": "back design, bow structure, satin reflections, shoulder line"
      },
      "panel_2": {
        "position": "center",
        "view": "front full-length view",
        "pose": "woman facing camera with one leg emerging through the thigh slit, torso elongated, one hand softly near the thigh, couture fashion stance",
        "focus": "neckline, waist fit, slit, full gown silhouette"
      },
      "panel_3": {
        "p
```

[[Identity Preservation]] [[Image to Image Mode]]

---

### 93. 逼真的健身生活方式肖像（图像到图像）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-07  **Language**: en

> 一个高度结构化的 JSON 提示，用于通过图生图模式生成一张超逼真的健身生活方式肖像。它详细描述了场景（现代健身房）、灯光、主体描述（优雅的运动型女性，具有特定的发型/妆容）、服装（粉蓝色套装）、配饰、姿势和相机设置，并着重强调了保留身份和解剖学准确性。

![逼真的健身生活方式肖像（图像到图像）](https://cms-assets.youmind.com/media/1772951318635_wpyv16_HC0KKYqWkAA3ky4.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_fitness_lifestyle_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_POWDER_BLUE_GYM_HEADPHONES"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_pose": true
    },

    "output_settings": {
      "aspect_ratio": "{argument name="aspect ratio" default="1:1"}",
      "orientation": "square",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "render_style": "ultra_photoreal_fitness_lifestyle",
      "sharpness": "clean_natural_crisp",
      "grain": "none",
      "color_grade": "soft_clean_modern",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },

    "scene": {
      "environment": "modern gym floor with minimal workout equipment",
      "lighting": "soft clean indoor gym lighting with natural highlights on skin and fabric, no harsh flash",
      "mood": "fresh, calm, feminine, modern fitness lifestyle"
    },

    "subject": {
      "description": "same elegant athletic woman from the reference, realistic facial proportions, soft peaceful expression",
      "skin": "natural luminous skin texture",
      "hair": "sleek dark hair pulled back neatly, same styling as the reference",
      "makeup": "minimal clean beauty makeup, soft natural glow, subtle lashes, natural pink-nude lips",
      "expression": "eyes closed, gentle soft smile, relaxed post-workout calm"
    },

    "wardrobe": {
      "outfit": "light powder blue fitted athletic set",
      "top": "light powder blue sports bra with smooth matte fabric and thin straps",
      "bottom": "matching light powder blue high-waisted leggings in matte performance fabric",
      "fabric": "soft matte athletic material, sculpting but realistic, no latex shine"
    },

    "accessories": {
      "headphones": "light blue Apple-style over-ear headphones with sleek matte finish",
      "mat": "matching light blue workout mat with matte texture",
      "equipment": "single dumbbell on the mat, realistic gym accessory"
    },

    "pose": {
      "position": "lying on the workout mat in the same pose as the reference",
      "details": "one arm lifted naturally toward the camera, one arm relaxed beside the body, torso slightly angled, calm post-workout pose",
      "anatomy": "perfect shoulders, arms, hands, torso, waist, and legs with realistic proportions"
    },

    "camera": {
      "lens": "35mm lifestyle overhead shot",
      "angle": "top-down selfie-like angle",
      "framing": "upper body and waist emphasized, workout mat and dumbbell visible",
      "focus_priority": "face, headphones, outfit texture, and natural body lines"
    },

    "quality_control": {
      "identity_consistency": "maximum",
      "anatomy_accuracy": "maximum",
```

[[Identity Preservation]] [[Cinematic Lighting]] [[Gym Setting]] [[Athletic Female Portrait]]

---

### 94. 照片转逼真动漫人物

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-07  **Language**: en

> 一个提示，指示 Nano Banana Pro 将上传的动漫人物（莎拉公主）照片，转换成一个超现实、电影感十足、完全逼真的场景。它严格要求保留原始人物真实人类版本中的面部结构、关键特征和整体相似性。

![照片转逼真动漫人物](https://cms-assets.youmind.com/media/1772951299557_mfib64_HC0GqlqWUAAEnbG.jpg)
![照片转逼真动漫人物](https://cms-assets.youmind.com/media/1772951299637_ofop2v_HC0GqlrXYAAESLi.jpg)

```
Convert the uploaded photo into an ultra-realistic, cinematic, fully photorealistic scene. the characters must be transformed into real human versions of the original uploaded references, The facial structure, key features, and overall likeness of each character from the reference are strictly preserved.
```

[[Identity Preservation]]

---

### 95. 动漫/漫画到超写实人物转换

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-06  **Language**: en

> 一个旨在将上传的动漫或漫画图像转换为超现实、电影级、完全逼真的场景的提示，严格保留原始角色真人版面部的结构和相似度。

![动漫/漫画到超写实人物转换](https://cms-assets.youmind.com/media/1772864628567_e1gwvw_HCw1UNMW8AAiVev.jpg)
![动漫/漫画到超写实人物转换](https://cms-assets.youmind.com/media/1772864628677_gr1rzs_HCw1UM8WcAAwWk7.jpg)

```
Convert the uploaded photo into an ultra-realistic, cinematic, fully photorealistic scene. the characters must be transformed into real human versions of the original uploaded references, The facial structure, key features, and overall likeness of each character from the reference are strictly preserved.
```

[[Identity Preservation]]

---

### 96. 多媒体肖像：名人角色扮演 vs. 二次元卡通

**Author**: [Giulia](https://x.com/Giulia_4i)  **Date**: 2026-03-05  **Language**: en

> 两个独立、高度详细的提示，用于生成混合媒体肖像，其中一位名人（梅根·福克斯 或 萨迪·辛克）扮演卡通人物（贝蒂·鲁布尔 或 石器时代女性），与传统的 2D 动画版本并排站立。这些提示侧重于将照片写实主义与平面动画形成对比，同时保持角色细节，并将场景设置在史前环境中。

![多媒体肖像：名人角色扮演 vs. 二次元卡通](https://cms-assets.youmind.com/media/1772778729653_t8dupl_HCr0ELraUAAahEg.jpg)
![多媒体肖像：名人角色扮演 vs. 二次元卡通](https://cms-assets.youmind.com/media/1772778729618_77zle0_HCr0EGUXgAESpro.jpg)

```
Megan Fox:

"A full-body shot, taken from a waist-level angle, featuring two female figures standing side-by-side facing forward. On the left is a traditional 2D animated cartoon Betty Rubble from The Flintstones, featuring classic animation facial proportions and flat colors. On the right is a highly detailed, photorealistic Megan Fox cosplaying as Betty Rubble. Both characters share light skin, short black hair with flipped-out ends, light blue hair bows, and wide smiles. Megan Fox features bright blue eyes, striking red lipstick, glossy lips, realistic skin texture, and a curvy silhouette. Both wear light blue mini dresses with jagged hems and black chokers with round pendants; however, 2D Betty's dress features a halter neckline, while Megan's is a strapless sweetheart design. Megan stands with both hands confidently and relaxedly resting on her hips. They are placed in an outdoor prehistoric setting with a carved stone dwelling, rock formations, and a sandy dirt path. The scene is illuminated by bright, warm sunlight that casts soft shadows and realistic highlights on Megan's skin and hair. The overall mood is fun, cheerful, and nostalgic, utilizing a color palette of light blue, black, beige, gray, and red. Highly detailed, sharp focus, vivid colors, 8K resolution, aspect ratio 9:16."

Sadie Sink:

"Create a mixed-media portrait featuring two distinct female characters standing side-by-side, blending traditional 2D flat animation with high-fidelity photorealism. On the left, a classic 2D cartoon woman with fair skin, blue eyeshadow, red lips, simplistic black dot eyes, thick black character outlines, and bright orange hair styled in a high bun. On the right, a highly detailed, photorealistic woman resembling Sadie Sink, featuring a curvy body, smooth skin with realistic light reflections, soft natural makeup, and reddish-orange hair in a similarly elegant updo. Both are smiling joyfully directly at the viewer.
They are wearing matching Stone Age-inspired outfits adapted to their respective art styles: a white one-shoulder, sleeveless asymmetric mini dress with a jagged zigzag hem. The human's dress features natural fabric folds and a linen-like texture. Both wear a statement necklace made of large white spheres—drawn as chunky stones in the cartoon, and as large pearl-like beads on the human. They are posing closely together; the cartoon woman on the left waves with her right hand and wraps her left arm around the human's waist, resting on her hip. The photorealistic woman waves with her left hand and wraps her right arm around the cartoon character's waist.
The setting is the interior of a stylized prehistoric stone cave dwelling. The background features rustic, uneven stone block walls, an arched stone doorway, and a stone slab floor. Surrounding them are props including lit fire torches mounted on the walls, a rustic wooden chest, wooden stools, a
```

[[Identity Preservation]] [[Mixed Media Portrait]]

---

### 97. 结构化图像到图像的时尚编辑提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-05  **Language**: en

> 一个高度详细、结构化的 JSON 提示，用于图像到图像的生成任务，重点是将特定的深红色时尚造型整合到提供的模特身上，同时保留其身份和面部特征。它指定了影棚环境、Vogue 风格的灯光、相机设置（85mm 镜头，f2.8 光圈），以及详细的造型整合，以实现逼真的面料物理效果和剪裁。

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "studio_fashion_look_integration",
      "language": "en",
      "priority": "highest",
      "version": "v5.0_CRIMSON_LOOK_ON_MODEL_EDITORIAL"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Use the provided woman as identity anchor. Dress her in the uploaded deep crimson halter vest, matching belted mini skirt, patent slingback heels, heart-shaped handbag, red choker, gold bracelet, and claw clip. Ensure natural body fit and realistic tailoring."
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "luxury_studio_editorial",
      "sharpness": "editorial_crisp",
      "grain": "subtle_35mm"
    },

    "scene": {
      "environment": "professional high-end studio with neutral gradient backdrop (warm gray to soft beige)",
      "lighting": {
        "style": "Vogue studio lighting",
        "key_light": "large diffused softbox front-left",
        "fill": "controlled subtle fill",
        "rim_light": "gentle edge highlight for silhouette separation",
        "shadow": "clean sculpted shadow under feet"
      },
      "camera": {
        "lens": "85mm",
        "aperture": "f2.8",
        "focus": "sharp on eyes and fabric texture",
        "angle": "slightly low for power stance"
      }
    },

    "styling_integration": {
      "halter_vest": {
        "fit": "snug but natural, tailored to torso",
        "fabric_behavior": "realistic satin drape and seam tension"
      },
      "mini_skirt": {
        "waist_alignment": "accurate fit on hips",
        "belt": "natural buckle weight and fabric indentation"
      },
      "heels": {
        "pose_adjustment": "natural foot posture with heel lift",
        "patent_reflection": "realistic glossy highlights"
      },
      "handbag": {
        "scale": "proportional to body",
        "gold_hardware": "real metallic reflection physics"
      },
      "accessories": {
        "choker": "natural neck curvature alignment",
        "bracelet": "realistic wrist placement",
        "claw_clip": "hair integrated, not floating"
      }
    },

    "pose_direction": {
      "body_language": "confident editorial stance",
      "expression": "controlled powerful gaze",
      "shoulders": "relaxed but structured",
      "hands": "one hand holding handbag, other resting naturally on hip"
    },

    "color_control": {
      "crimson_tone": "deep rich red, not oversaturated",
      "skin_tone_balance": "natural and luminous",
      "contrast": "editorial mid-high contrast"
    },

    "quality_control": {
      "identity_lock": "strict",
      "fabric_physics": "maximum",
      "anatomy_accur"
```

[[Identity Preservation]] [[85mm Lens Portrait]]

---

### 98. 高保真照片级自拍转换

**Author**: [Chryz leen](https://x.com/Chryzleenprompt)  **Date**: 2026-03-05  **Language**: en

> 一个用于图像到图像转换的高度详细的提示，要求在保持源图像面部身份方面绝对精确。场景是一个在室内拍摄的超现实自拍，详细说明了拍摄对象的特征（头发、服装、妆容、隐形眼镜）和技术设置（iPhone 15 Pro 的清晰度、玻璃皮肤质感、最小对比度）。

![高保真照片级自拍转换](https://cms-assets.youmind.com/media/1772778703070_u98cda_HCpaCKVb0AABiCC.jpg)

```
Create a high-fidelity photographic transformation. Maintain the exact facial identity from the provided source image with absolute precision and zero alteration.
[SCENE]: A bright, warm-toned indoor setting, likely a home environment. The background is a soft, light-colored wall with abstract patterns of natural light and shadows, possibly from a window or nearby foliage, adding subtle depth. A glimpse of a blurred green plant or object is visible in the far right corner. The composition is an upper-body shot, captured in a portrait orientation, with the subject leaning slightly into the left side of the frame as she holds her phone. The entire scene is in sharp focus, without any background blur or bokeh.
[SUBJECT]: An adult woman with a fair complexion, captured mid-selfie. Her dark brown hair is long and voluminous, styled with soft mermaid waves, prominent butterfly-style layers that frame her face and shoulders, and soft curtain bangs gently sweeping across her forehead. She is wearing a light pink button-up cardigan over a light grey ribbed knit bralette or top featuring a subtle cut-out and delicate strappy detail at the chest. Her right arm is slightly raised, holding a light purple smartphone with a triple camera array towards the camera, while her left shoulder is subtly lower, demonstrating natural weight shift. Her head is slightly tilted to her right (viewer's left), and her gaze is soft and direct, with subtle, natural-looking hazel contact lenses that blend with the natural eye color, adding warmth and depth. Her expression is serene and inviting, with a gentle, soft smile causing a slight micro-tightening at the outer corners of her eyes. Her lips are glossy, plump, and a natural pinkish-mauve with a subtle shimmer, slightly parted. Her brows are relaxed. Her skin is flawless and luminous, featuring a 'glass skin' texture with intense, dewy highlights on the bridge and tip of the nose, complemented by a subtle blush applied with high placement on the cheekbones.
[LIGHTING]: Natural daylight with soft rosy undertones reflecting subtly on the skin, enhancing the natural blush tones. The clean white balance ensures true-to-life colors, with a soft highlight rolloff that prevents harshness.
[AESTHETIC]: A hyper-realistic, ultra-sharp photograph taken on a modern smartphone, specifically an iPhone 15 Pro, characterized by its digital clarity. The image showcases realistic, digital texture with sharp details, including visible pores on the skin. There is minimal contrast, no HDR flattening, and no heavy color grading, preserving the soft pink warmth of the skin. ar 4:5
```

[[Identity Preservation]] [[Image to Image Mode]] [[Glass Skin Texture]]

---

### 99. 图像转插画风格迁移提示（古斯塔夫·多雷）

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-03-04  **Language**: en

> 一个提示，用于将上传的参考图像转换为古斯塔夫·多雷（Gustave Doré）插画风格，同时确保姿势、面部特征和身份保持不变，并保持中性背景。

![图像转插画风格迁移提示（古斯塔夫·多雷）](https://cms-assets.youmind.com/media/1772692205868_ze7f4j_HClZ_ffaoAANZg2.jpg)
![图像转插画风格迁移提示（古斯塔夫·多雷）](https://cms-assets.youmind.com/media/1772692205770_8gz6ao_HClZ_fnawAU4dOa.jpg)
![图像转插画风格迁移提示（古斯塔夫·多雷）](https://cms-assets.youmind.com/media/1772692205777_7g323g_HClZ_fgawAIF165.jpg)
![图像转插画风格迁移提示（古斯塔夫·多雷）](https://cms-assets.youmind.com/media/1772692206886_xei6ij_HClZ_flbIAAcdZQ.jpg)

```
From the uploaded reference image, With same pose and same facial features, keep the identity and facial features identical to the attached, use Gustave dore illustration style,, size 9:16, don't change the expression and facial for all photos, no text, neutral background minimalist.
```

[[Identity Preservation]]

---

### 100. 旧照片修复和上色提示

**Author**: [Nuri Yıldız](https://x.com/nouryyildiz)  **Date**: 2026-03-04  **Language**: en

> 一个针对 Nano Banana 2 的高度具体提示，指示它将上传的旧照片修复并上色，使其成为一张晶莹剔透、照片级真实、细节丰富的高清图像，同时严格保留 100% 的原始构图、姿势、身份和细节，仅去除与年代相关的损坏。

![旧照片修复和上色提示](https://cms-assets.youmind.com/media/1772692195856_7a1mbe_HCkY_embUAAqIVE.jpg)
![旧照片修复和上色提示](https://cms-assets.youmind.com/media/1772692196010_hvboln_HCkY-OiawAU7D04.jpg)

```
Restore and colorize the uploaded old photograph into a crystal-clear, photorealistic, high-detail image while preserving 100% of the original composition. Keep the exact same pose, expression, facial structure, proportions, framing, clothing, hairstyle, background, objects, and all details unchanged. Do not add, remove, move, or restyle anything. Remove blur, noise, scratches, fading, stains, and age-related damage. Recover natural sharpness, fine skin texture, realistic textures, true-to-life colors, and lifelike skin tones. No identity change, no stylization, no cartoon or CGI look, no plastic skin.
```

[[Identity Preservation]] [[Photo Restoration]]

---

### 101. 图像到图像风格迁移提示

**Author**: [Layla 🌙](https://x.com/TheAiVisionary)  **Date**: 2026-03-04  **Language**: en

> 请用户上传照片，然后使用 Gemini Nano Banana 复制照片中的造型，并应用特定风格（黑色蕾丝袖 + 野性咬舌）。

![图像到图像风格迁移提示](https://cms-assets.youmind.com/media/1772692202875_8ftoms_HCkITfda8AEQIw5.jpg)

```
black lace sleeve + feral tongue bite (iPhone close-up hunger).
```

[[Identity Preservation]] [[Photo Reference Workflow]]

---

### 102. Nano Banana Pro 的编辑肖像提示

**Author**: [novah](https://x.com/novah_ia)  **Date**: 2026-03-03  **Language**: en

> 一个为 Nano Banana Pro 设计的高度详细且结构化的提示，旨在生成超详细、逼真的编辑肖像。它指定了长宽比、分辨率、源图像保留、服装、表情、构图、背景、光线、情绪和技术美学。

![Nano Banana Pro 的编辑肖像提示](https://cms-assets.youmind.com/media/1772605590801_28ydue_HChQcyAWUAAfkwm.jpg)

```
Rapport d'aspect 4:5, résolution 2K, portrait éditorial photoréaliste et ultra-détaillé. Source : préserver les traits exacts du visage, le teint de la peau, la coiffure et la ressemblance naturelle de la photo de référence ci-jointe. Le sujet peut être un homme ou une femme. Garde-robe : Polo piqué noir de qualité supérieure, ajusté, pointu, avec texture piquée en coton visible, couleur noire mate profonde. Expression : sérieuse, intense, concentrée, regardant légèrement au-dessus de la caméra, pas directement sur l'objectif. Composition : Gros plan moyen (visage et épaules), prise de vue à faible angle pour transmettre la puissance et la domination. Arrière-plan : dégradé rouge orange vibrant, lisse et intense, pas de motifs. Éclairage : Éclairage de studio dramatique et coloré. Lumière clé : ombres fortes, directionnelles et profondes mettant l'accent sur la structure faciale (clair foncé). Lumière de la jante : forte lumière de bord séparant le sujet de l'arrière-plan. Humeur : intense, mystérieuse, contrastée. Technique : mise au point nette sur le visage, dégradé d'arrière-plan lisse, texture photoréaliste de haute qualité, ultra-détail 2K. Appliquer de manière cohérente quel que soit le sexe. Esthétique du studio de cinéma, ambiance de portrait héroïque éditorial.
```

[[Identity Preservation]]

---

### 103. 超逼真角色转换提示词

**Author**: [Nuri Yıldız](https://x.com/nouryyildiz)  **Date**: 2026-03-02  **Language**: en

> 一个简洁的提示，与 Nano Banana 2 结合使用，可将上传的角色参考图转化为超现实、电影级、完全照片级的人类版本，同时严格保持其身份、面部结构和关键相似性。

![超逼真角色转换提示词](https://cms-assets.youmind.com/media/1772519698499_c2xanc_HCbXoVyW0AA7Eit.png)
![超逼真角色转换提示词](https://cms-assets.youmind.com/media/1772519699784_8v1bzq_HCbXoWJXwAA6uB_.jpg)

```
Convert this into an ultra-realistic, cinematic, fully photorealistic scene. The characters must be transformed into real human versions of the original uploaded references, keeping their identity, facial structure, key features, and overall likeness intact.
```

[[Identity Preservation]] [[Cinematic Photorealism]]

---

### 104. Crimson 时尚编辑工作室造型整合提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-02  **Language**: en

> 一个高度结构化的图生图提示，用于将特定的深红色时尚造型（露背背心、迷你裙、漆皮高跟鞋）整合到高端影棚时尚大片背景下的参考模特身上。它强调在保留模特身份的同时，确保逼真的面料物理效果、剪裁以及在《Vogue》风格影棚灯光下的精细配饰摆放。

![Crimson 时尚编辑工作室造型整合提示](https://cms-assets.youmind.com/media/1772519709261_jghsyo_HCbIyuiaEAA105M.jpg)
![Crimson 时尚编辑工作室造型整合提示](https://cms-assets.youmind.com/media/1772519709181_ko8c9t_HCbIu5fXoAAQZDI.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "studio_fashion_look_integration",
      "language": "en",
      "priority": "highest",
      "version": "v5.0_CRIMSON_LOOK_ON_MODEL_EDITORIAL"
    },

    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Use the provided woman as identity anchor. Dress her in the uploaded deep crimson halter vest, matching belted mini skirt, patent slingback heels, heart-shaped handbag, red choker, gold bracelet, and claw clip. Ensure natural body fit and realistic tailoring."
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "luxury_studio_editorial",
      "sharpness": "editorial_crisp",
      "grain": "subtle_35mm"
    },

    "scene": {
      "environment": "professional high-end studio with neutral gradient backdrop (warm gray to soft beige)",
      "lighting": {
        "style": "Vogue studio lighting",
        "key_light": "large diffused softbox front-left",
        "fill": "controlled subtle fill",
        "rim_light": "gentle edge highlight for silhouette separation",
        "shadow": "clean sculpted shadow under feet"
      },
      "camera": {
        "lens": "85mm",
        "aperture": "f2.8",
        "focus": "sharp on eyes and fabric texture",
        "angle": "slightly low for power stance"
      }
    },

    "styling_integration": {
      "halter_vest": {
        "fit": "snug but natural, tailored to torso",
        "fabric_behavior": "realistic satin drape and seam tension"
      },
      "mini_skirt": {
        "waist_alignment": "accurate fit on hips",
        "belt": "natural buckle weight and fabric indentation"
      },
      "heels": {
        "pose_adjustment": "natural foot posture with heel lift",
        "patent_reflection": "realistic glossy highlights"
      },
      "handbag": {
        "scale": "proportional to body",
        "gold_hardware": "real metallic reflection physics"
      },
      "accessories": {
        "choker": "natural neck curvature alignment",
        "bracelet": "realistic wrist placement",
        "claw_clip": "hair integrated, not floating"
      }
    },

    "pose_direction": {
      "body_language": "confident editorial stance",
      "expression": "controlled powerful gaze",
      "shoulders": "relaxed but structured",
      "hands": "one hand holding handbag, other resting naturally on hip"
    },

    "color_control": {
      "crimson_tone": "deep rich red, not oversaturated",
      "skin_tone_balance": "natural and luminous",
      "contrast": "editorial mid-high contrast"
    },

    "quality_control": {
      "identity_lock": "strict",
      "fabric_physics": "maximum",
      "anatomy_accuracy": "perfect",
      "avoid": [
```

[[Identity Preservation]]

---

### 105. 超细节高定时装民族肖像提示词

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-02  **Language**: en

> 以下是为 PolloAI 的 Nano Banana Pro 设计的一个极其详细、结构化的提示，旨在生成一张名人（萨迪·辛克、安娜·德·阿玛斯或比莉·艾利什）身着闪亮白色亮片印度纱丽的超详细、高级时装编辑肖像。该提示包含严格的身份保留要求、特定的姿势、造型和影棚灯光设置。

![超细节高定时装民族肖像提示词](https://cms-assets.youmind.com/media/1772519743885_c2if70_HCbEk9VakAAV-yl.jpg)
![超细节高定时装民族肖像提示词](https://cms-assets.youmind.com/media/1772519743955_up2mcp_HCbElA9a8AAhBNq.jpg)
![超细节高定时装民族肖像提示词](https://cms-assets.youmind.com/media/1772519744010_h1vx5x_HCbElJWa8AAKfYn.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "ultra_detailed_high_fashion_ethnic_portrait",
      "style": "cinematic_editorial_studio",
      "resolution": "8k",
      "quality": "ultra_high",
      "face_lock": "strict_identity_preservation",
      "skin_texture": "realistic",
      "version": "v2.0"
    },
    "subject": {
      "gender": "female",
      "age_range": "early_to_mid_20s",
      "face_requirement": "exact_same_face_as_reference_image",
      "identity_preservation": {
        "facial_structure": "locked",
        "eyes_shape": "locked",
        "nose_shape": "locked",
        "lip_shape": "locked",
        "jawline": "locked",
        "skin_tone": "locked",
        "proportions": "100_percent_preserved"
      },
      "expression": {
        "type": "confident_glamorous",
        "eyes": "direct_soft_intense_gaze",
        "lips": "subtle_glamorous_smile",
        "energy": "high_fashion_editorial_presence"
      },
      "pose": {
        "body_position": "standing",
        "action": "adjusting_earrings_with_one_hand",
        "hand_detail": "fingers_delicately_touching_earring",
        "shoulder_posture": "slightly_back_confident",
        "neck": "elongated_elegant"
      }
    },
    "styling": {
      "outfit": {
        "type": "sparkling_white_sequin_saree",
        "fabric": "high_shine_micro_sequins",
        "texture_detail": "intricate_reflective_surface",
        "drape": "perfectly_structured_elegant_fall",
        "blouse": {
          "type": "designer_blouse",
          "fit": "tailored_structured",
          "sleeves": "modern_cut",
          "neckline": "elegant_fashion_forward"
        }
      },
      "hair": {
        "style": "elegant_bun",
        "structure": "neatly_coiled_low_or_mid_bun",
        "details": "few_loose_strands_framing_face",
        "finish": "soft_silky_sheen"
      },
      "accessories": {
        "earrings": "luxury_statement_earrings",
        "jewelry_style": "minimal_but_glamorous",
        "finish": "high_polish_reflective"
      },
      "makeup": {
        "base": "flawless_high_definition",
        "highlight": "soft_glow_on_cheekbones",
        "eyes": "defined_with_black_liner_and_soft_shimmer",
        "lips": "neutral_glam_shade",
        "overall": "editorial_finish_not_overdone"
      }
    },
    "lighting": {
      "type": "studio_soft_light",
      "setup": "three_point_lighting",
      "key_light": "large_softbox_front_left",
      "fill_light": "soft_fill_for_balanced_skin_tone",
      "rim_light": "subtle_backlight_for_hair_separation",
      "effect": "soft_shadows_smooth_gradients_even_skin_texture",
      "reflection_behavior": "controlled_highlights_on_sequins"
    },
    "background": {
      "type": "beige_studio_backdrop",
      "texture": "smooth_matte",
      "tone": "warm_neutral_beige",
      "depth": "slight_background_blur_for_subj"
    }
  }
```

[[Identity Preservation]] [[Celebrity Lookalike]] [[Studio Lighting Setup]]

---

### 106. 超逼真复古相机人像提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-03-02  **Language**: en

> 生成一张超现实、低角度的年轻女性肖像的提示，需保留其特定身份，她戴着眼镜，穿着红色 T 恤，手持一台复古胶片相机，周围环绕着茂盛的白色攀援花卉。

![超逼真复古相机人像提示](https://cms-assets.youmind.com/media/1772519750718_k9eu77_HCZSZYLaAAAzySE.jpg)

```
Ultra-realistic portrait of a young woman (use uploaded photo for exact face likeness 100% match, no facial alterations). A medium close-up, low-angle shot; stylish square black glasses; dressed in a red oversized collared t-shirt. A brown leather camera strap crosses her chest as she holds a vintage film camera in her hands. She looks upward thoughtfully, surrounded by lush white climbing flowers in soft focus.
```

[[Identity Preservation]] [[Low Angle Perspective]]

---

### 107. 主导肖像生成提示（Gemini - 思维模式）

**Author**: [Edizkan ⭕🦇](https://x.com/edizkan_)  **Date**: 2026-03-02  **Language**: en

> 一个为 Nano Banana（Gemini - 思维模式）设计的极其详细、结构化的提示，旨在为上传的参考角色创建一张坐在神圣宝座上的“统治肖像”。该提示强调严格的相似性完整性，要求根据角色的设计语言来设计宝座，并运用特定的电影摄影/灯光技术（广角镜头、部分遮挡、垂直神圣光束）。

![主导肖像生成提示（Gemini - 思维模式）](https://cms-assets.youmind.com/media/1772519741252_1nxgb4_HCY4uF-WYAAMH3U.jpg)

```
Create a dominance portrait of the uploaded reference character seated on a divine throne that feels engineered from their own world and design language.

The camera observes the ruler from a partially obstructed viewpoint, as if the viewer is looking through the monumental structure of the throne itself.

Likeness Integrity (HIGHEST PRIORITY)

Maintain exact:

• Head-to-body proportions

• Eye shape, spacing, stylization

• Surface materials

• Silhouette and structural design

Do not humanize.

Do not reinterpret anatomy.

Do not add unintended accessories.

Perspective exaggeration must come only from camera placement, not structural redesign.

Identity always wins.

Throne Adaptation System (UNIVERSAL LOGIC)

The throne must feel like a structural extension of the character’s design universe and must feel divine.

Rules:

Extract design language from the character:

Dominant material logic

Geometric language

Color

World energy

Translate, never copy.

Echo shapes subtly in silhouette

Reflect material family, not exact textures

Use tonal harmony, not color duplication

Patterns may appear in architecture, structure, or ornamentation but must remain subordinate to the character’s identity.

Camera & Perspective

• Camera positioned slightly below the throne platform but offset laterally

• 16–20mm wide cinematic lens

• The throne structure partially obstructs the frame

• Large architectural element of the throne occupies the foreground edge of the frame

• Character visible through the throne’s structural opening or between its elements

• Horizon slightly tilted 5–8 degrees

• The viewer feels as if witnessing the ruler from behind the architecture of power

Foreground elements must feel massive and close to the lens, framing the character like a monumental gateway.

Composition

• The character sits centered within the throne structure but partially framed by its geometry

• Throne architecture creates a natural visual tunnel toward the character

• Foreground throne elements remain slightly out of focus

• Character remains the focal authority within the frame

Lighting

• Singular vertical divine beam descending from above the throne

• Volumetric haze revealing light shafts

• Strong rim light outlining the character silhouette

• Controlled specular spikes along throne edges

• Foreground throne elements remain darker, creating contrast against the illuminated ruler

Depth & Focus

• Eyes in absolute clarity

• Character face and upper torso remain sharp

• Foreground throne structure slightly blurred from proximity to lens

• Background dissolves into atmospheric layers

The image must feel layered in depth:

foreground architecture → seated ruler → atmospheric background.

Background

• Vast negative space above the throne

• Atmospheric tension

• Light beam
```

[[Identity Preservation]] [[Cinematic Wide Angle]]

---

### 108. 超现实纳米香蕉美学模板提示

**Author**: [yukyuk](https://x.com/YukYukID)  **Date**: 2026-03-02  **Language**: en

> 一个灵活的模板提示，旨在将超现实的“纳米香蕉美学”应用于任何物体，将其替换为香蕉形状的版本，同时保留原始主体、姿势和背景细节。

![超现实纳米香蕉美学模板提示](https://cms-assets.youmind.com/media/1772519708291_q9c5ym_HCYi9uibQAAdu_S.jpg)

```
"replace the {argument name="object" default="object"} with a banana-shaped {argument name="style" default="style"}, surreal nano banana aesthetic, realistic lighting, cinematic composition, seamless integration, preserve {argument name="subject" default="subject"}, preserve {argument name="pose" default="pose"}, preserve {argument name="background" default="background"}, ultra realistic, high detail"
```

[[Identity Preservation]]

---

### 109. Hyper-Realistic Editorial Portrait Editing Prompt for Gemini Nano Banana Pro

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-02  **Language**: en

> 这是一个高度详细、结构化的提示，专为 Gemini Nano Banana Pro 模型设计，用于执行复杂的图像编辑。目标是将用户的参考照片转换为一张超现实、电影感的社论肖像，背景设定在日落时分的城堡塔楼阳台，同时严格保留用户的身份和面部特征。它详细说明了服装、妆容、背景、光线和相机构图的修改。

![Hyper-Realistic Editorial Portrait Editing Prompt for Gemini Nano Banana Pro](https://cms-assets.youmind.com/media/1772519713634_sr877o_HCYljBHa4AAdXXw.jpg)
![Hyper-Realistic Editorial Portrait Editing Prompt for Gemini Nano Banana Pro](https://cms-assets.youmind.com/media/1772519713658_oov0li_HCYli-SaQAAN-z9.jpg)

```
{
  "model": "gemini-2.5-flash-image",
  "task_type": "editing",
  "priority": {
    "primary": "create_hyper_realistic_8k_editorial_hyper_close_up_portrait_preserving_identity",
    "secondary": "cinematic_fairytale_environment_integration_with_photographic_realism"
  },
  "task": "edit_image",
  "source": "reference_photo_of_user",
  "character_lock": {
    "reference": "reference_photo_of_user",
    "maintain": [
      "exact_facial_features",
      "face_structure",
      "skin_texture",
      "natural_skin_tone",
      "eye_shape",
      "eye_color_dark_brown",
      "eyebrow_shape",
      "nose_shape",
      "lip_shape",
      "long_flowing_hair",
      "hair_color",
      "hairline",
      "overall_identity"
    ],
    "allow_changes": [
      "makeup_styling",
      "wardrobe",
      "pose_adjustment",
      "background_environment"
    ]
  },
  "modifications": [
    {
      "type": "wardrobe",
      "target": "clothing",
      "action": "replace",
      "details": "exquisite voluminous dark red couture gown with dramatic long train, luxury fantasy fashion, high-end editorial fabric texture, realistic folds and weight"
    },
    {
      "type": "style",
      "target": "makeup",
      "action": "enhance",
      "details": "professional editorial makeup, defined black eyeliner, dark-red lips, natural skin finish with realistic pores, no artificial skin smoothing"
    },
    {
      "type": "background",
      "target": "environment",
      "action": "replace",
      "details": "stone balcony of tall ivy-covered medieval castle tower, rough aged gray stone, conical dark turret roof, climbing vines with red and dark-pink roses, dramatic sunset sky with soft pink orange and pale lavender gradient, flock of black birds flying past tower"
    },
    {
      "type": "lighting",
      "target": "global_scene",
      "action": "modify",
      "details": "golden hour magic light, cinematic side lighting, soft rim light on hair, natural skin highlights, realistic shadow falloff, dramatic but physically accurate illumination"
    },
    {
      "type": "camera",
      "target": "composition",
      "action": "modify",
      "details": "hyper close-up portrait framing, shallow depth of field, soft focus background, sharp focus on eyes and facial features, editorial fashion photography composition"
    }
  ],
  "environment": {
    "setting": "castle_tower_balcony",
    "time": "sunset_magic_hour",
    "weather": "clear_with_soft_atmospheric_haze",
    "lighting": {
      "type": "natural",
      "direction": "side_with_subtle_backlight",
      "quality": "cinematic_soft_but_directional"
    }
  },
  "style": {
    "artistic": "photorealistic",
    "camera": {
      "angle": "eye_level_slightly_low_for_heroic_presence",
      "lens": "telephoto_85mm_to_135mm_portrait_lens",
      "aperture": "f1.8_shallow_depth_of_field"
    },
    "mood": "romantic_dream_like_cinematic_editorial",
    "color_palette": "dark_r
```

[[Identity Preservation]]

---

### 110. 电影海滨三联画肖像提示

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2026-03-02  **Language**: en

> 一个详细的提示，用于生成一张逼真的电影感三联画（一张图片中包含三个画面），描绘一个身处多风海边的人物，要求保留人物身份，并指定三个画板（广角镜头、中景镜头、特写镜头）的内容和构图。

![电影海滨三联画肖像提示](https://cms-assets.youmind.com/media/1772519747842_6dduai_HCYg4vWbYAAvNp4.jpg)

```
Use the uploaded photo as the exact identity reference. Keep the same person, the same face, the same facial features, proportions, and natural expression.
Create a photorealistic cinematic triptych portrait, a three-frame composition combined into one image.
Scene: a windy seaside with a cold sea, overcast sky, flying seagulls, strong ocean wind, and a vivid, alive atmosphere.
Frame 1 (top): wide cinematic shot. The person stands by the sea, smiling naturally. Their hair is blowing in the wind. Seagulls are flying in the background.
Frame 2 (middle): medium shot from behind or from the side. The person is looking at the sea. Their coat and hair are moving in the wind. Seagulls fly nearby.
Frame 3 (bottom): close-up emotional portrait. Wind in the hair, natural skin texture, thoughtful gaze, cinematic mood.
Style: real photography, cinematic lifestyle portrait, documentary fashion photography.
Lighting: natural overcast daylight, soft shadows, cold seaside tones.
Camera: full-frame DSLR look, 85mm lens aesthetic, shallow depth of field.
Color grading: muted cinematic colors, cool palette, film-like mood.
Ultra photorealistic, natural skin texture, real moment. No illustration, no CGI. No text, no logos, no watermark.
```

[[Identity Preservation]] [[Cinematic Photography]]

---

### 111. 超风格化双色霓虹肖像提示

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-03-01  **Language**: en

> 一个用于生成高度风格化、电影感人像的提示，强调戏剧性的双色调照明。脸部一侧被冷蓝色光照亮，另一侧被鲜艳的粉色/红色霓虹灯照亮，营造出高对比度、大胆的外观，同时保持人物的精确身份。

![超风格化双色霓虹肖像提示](https://cms-assets.youmind.com/media/1772433488229_e83t2d_HCVW-VDawAE9_BF.jpg)
![超风格化双色霓虹肖像提示](https://cms-assets.youmind.com/media/1772433488213_j6zjf5_HCVW-UiasAAy_mu.jpg)
![超风格化双色霓虹肖像提示](https://cms-assets.youmind.com/media/1772433488554_i32dfg_HCVW-ZYa0AA9tLw.jpg)

```
A hyper-stylized portrait of the same person, keeping their exact face and identity unchanged. They are captured in a thoughtful pose with one hand resting on their chin, illuminated by dramatic dual-tone lighting. One side of the face is lit with cool blue light, while the other side glows with vivid pink/red neon tones, creating a bold, high-contrast look.
They are wearing a dark top and a watch. The background remains dark and minimal, emphasizing the colorful illumination on the face and upper body. Cinematic, sharp, and highly detailed.
```

[[Identity Preservation]] [[High Contrast Portrait]]

---

### 112. Nano Banana Pro 的图像修复和放大提示

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-02-27  **Language**: en

> 一个为 Nano Banana Pro 设计的结构化 JSON 提示，旨在将提供的老旧图像恢复并放大至 4K 分辨率，重点是保留身份并实现高保真、超逼真的摄影效果。

![Nano Banana Pro 的图像修复和放大提示](https://cms-assets.youmind.com/media/1772259921116_51wmoe_HCIACqRaIAAZsu3.jpg)
![Nano Banana Pro 的图像修复和放大提示](https://cms-assets.youmind.com/media/1772259921170_ml3kba_HCIACq1bQAEQH9U.jpg)

```
{ "task": "image_restoration_upscale", "positive_prompt":
"Restore and enhance the provided image. Preserve original identity, facial structure, proportions and composition. High-fidelity photo restoration, ultra-realistic, natural skin texture, accurate details, professional photographic look. 4K output, sharp but natural focus, modern cinematic lighting, subtle volumetric lighting, professional color grading, depth of field, HDR. Shot on Arri Alexa, raw photo aesthetic, masterpiece.",
"negative_prompt": "Creative reinterpretation, style change, identity alteration, face reshaping, exaggerated features, cartoonish, painting, illustration, over-sharpening, plastic skin, blur, noise, film grain, jpeg artifacts, distortion, bad anatomy, overexposed, underexposed, washed out colors.", "parameters":
{ "steps": 30, "cfg_scale": 6.5, "denoising_strength": 0.45,
"upscaler": "4x_NMKD_Siax_200k", "target_resolution": "4K" } }
```

[[Identity Preservation]] [[Photo Restoration]]

---

### 113. 黑白工作室肖像，保留身份特质

**Author**: [Ai Prompts Lab](https://x.com/Aipromptslap)  **Date**: 2026-02-26  **Language**: en

> 一个高度详细的提示，用于在黑暗摄影棚环境中生成黑白肖像，强调硬质定向照明（伦勃朗风格），并严格保留基于源照片的主体面部特征、不对称性和体格。

![黑白工作室肖像，保留身份特质](https://cms-assets.youmind.com/media/1772174106761_uuz2pi_HCHXbROXMAAm6JN.jpg)
![黑白工作室肖像，保留身份特质](https://cms-assets.youmind.com/media/1772174106592_qmivc0_HCHXbRMX0AAa2q0.jpg)

```
Create a photo strictly based on the source photo of the girl, 1-to-1 match.
Exact resemblance, without altering facial features or natural asymmetry.
Do not change the shape of the eyes, lips, nose, cheekbones, or face oval.
Natural skin without retouching or a plastic look.
Makeup: long brown eyelashes, smudged brown winged eyeliner, neat matte lip tone in a cool nude palette.
Hair is blonde, styled smoothly with soft volume, exactly as in the source photo, without changing length or shape.
Physique and Proportions
Height 178 cm. Thin, ascetic physique, long limbs. Proportions are strictly natural, unaltered.
Scene and Action
Portrait in a dark studio. The girl is partially hidden behind a vertical black panel/wall, with only half of her face visible. One hand gently touches the edge of the panel, fingers gracefully extended. Gaze directed straight at the camera — calm, cold, confident. Facial expression is reserved, mysterious.
Clothing
Black turtleneck dress made of thick fabric with a slight velvet texture. Long sleeves.
Nails are painted with dark glossy polish.
Minimalist stud earrings.
Environment
Deep dark background without details.
Minimalism.
The entire composition is built on the contrast of light and shadow.
Lighting
Hard directional studio lighting from the side (Rembrandt lighting). Half of the face is illuminated, the other half fades into a soft, deep shadow. Clear lighting pattern highlighting the cheekbones and lip line.
No overexposure.
Camera
Full-frame camera, 85mm lens. Shallow depth of field. No wide-angle distortion.
Focus on the visible eye and lip line.
Quality
Black and white photography with deep contrasts. Maximum photorealism. High detailing of skin and fabric.
Negative Prompt
Any changes in appearance, altering facial features and asymmetry, skin retouching, CGI, anime style, soft glamour lighting, wide-angle distortion, extra limbs, deformed fingers, overexposure.
```

[[Identity Preservation]] [[Black And White Photography]] [[Rembrandt Lighting]] [[Dark Studio Setting]]

---

### 114. 浪漫街头编辑肖像（图像到图像）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-26  **Language**: en

> 一个高度详细的图生图提示，用于生成浪漫的街头时尚人像。它侧重于保留参考图像中的身份和姿势，同时在优雅的城市街道背景下增强真实感、织物纹理和光照效果。

![浪漫街头编辑肖像（图像到图像）](https://cms-assets.youmind.com/media/1772174145154_5ttjsd_HCGHHB5bgAA3EaE.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "romantic_street_editorial_identity_lock",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_AUTUMN_RED_SWEATER_FLOWER_BOUQUET_NO_TEXT"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_pose": true,
      "preserve_body_proportions": true,
      "preserve_hand_structure": true,
      "notes": "Use the uploaded image as the primary anchor. Keep the exact standing pose, head direction, hand touching hair, and bouquet placement. Maintain the red knit sweater, white layered lace skirt, sheer tights, and black shoulder bag. Preserve the bouquet with red flowers and white lilies wrapped in warm-toned paper. Keep the architectural stone building facade and decorative metal door details in the background. Enhance realism: natural skin texture, detailed knit fabric, lace transparency accuracy, realistic flower textures, balanced daylight shadows. No text, no logos, no watermark."
    },
    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "render_style": "cinematic_natural_editorial",
      "sharpness": "natural_crisp",
      "grain": "subtle_film",
      "color_grade": "soft_warm_daylight",
      "dynamic_range": "balanced_highlights"
    },
    "scene": {
      "environment": "elegant city street with stone architecture",
      "lighting_style": "soft natural daylight with gentle shadow contrast",
      "background_elements": "textured stone wall, ornate dark metal doors, tiled sidewalk"
    },
    "subject": {
      "count": 1,
      "description": "one adult woman standing outdoors holding a bouquet",
      "expression": "soft thoughtful gaze to the side",
      "hair": "dark wavy hair with natural volume",
      "makeup": "natural glam with soft blush and defined lashes",
      "wardrobe": "red knit sweater, white layered lace mini skirt, sheer tights",
      "accessories": "black shoulder bag"
    },
    "camera": {
      "shot_type": "medium full-body portrait",
      "angle": "eye level with slight natural perspective",
      "focus": "sharp on subject and bouquet, mild background falloff",
      "lens_look": "85mm portrait lens aesthetic",
      "depth_of_field": "moderate shallow",
      "exposure": "balanced daylight exposure"
    },
    "lighting": {
      "key_light": "natural daylight from side",
      "fill_light": "soft ambient bounce from building facade",
      "shadow_style": "natural soft shadow lines",
      "skin_rendering": "realistic texture, no over-smoothing"
    },
    "composition_rules": [
      "keep bouquet clearly visible and detailed",
      "preserve architectural symmetry behind subject",
      "maintain natural proport
```

[[Identity Preservation]] [[Street Fashion Portrait]]

---

### 115. 高级时装新闻发布会抓拍照片提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-02-26  **Language**: en

> 一个详细的提示，用于生成一张描绘主体被困在幽闭的“狗仔队围攻”中的高级时装社论照片，强调高对比度闪光灯照明、电影般的真实感，并严格保留主体的身份。

![高级时装新闻发布会抓拍照片提示](https://cms-assets.youmind.com/media/1772174114105_ys0zgz_HCCv6ckaMAEeMzi.jpg)

```
Transform the subject into a high-fashion press scrum photograph, surrounded tightly by cameras, microphones, and boom mics from all directions. Preserve the subject's face, features, and overall identity clearly recognizable. The subject is centered in the frame, partially obscured by overlapping microphones and camera lenses pointing inward, creating a sense of pressure and attention. Expression is calm, controlled, and unreadable - confident but distant. Styling is minimal and fashion-forward: dark clothing, sharp silhouette, sunglasses or statement eyewear optional. The image is shot like a real editorial photograph - direct flash, harsh highlights, deep shadows, and realistic textures on equipment. Colors are cool and neutral, dominated by black, grey, and metallic tones. The composition feels claustrophobic and symmetrical, with the subject visually trapped by media attention. Style: paparazzi press swarm, fashion editorial photography, cinematic realism, high-contrast flash, modern celebrity moment.
```

[[Identity Preservation]] [[High Contrast Flash]]

---

### 116. 年轻男子的单色时尚专题三联画

**Author**: [Snow](https://x.com/iamrealsnow)  **Date**: 2026-02-23  **Language**: en

> 一个用于生成极简主义单色时尚专题三联画（三个堆叠的电影画面）的提示，描绘一位年轻男士，重点是保留其参考图像中的面部特征，并使用伦勃朗光和干净、现代的构图来突出骨骼结构。

![年轻男子的单色时尚专题三联画](https://cms-assets.youmind.com/media/1771914997894_8yycv2_HB2vbpMbwAEo6Q5.jpg)

```
Preserve the face, proportions, and external features of the model as in the reference. A minimalist monochrome fashion editorial triptych featuring three stacked cinematic frames. The subject is a young man with short dark hair and a groomed beard. Frame 1: Emotional and introspective, looking downward with a hand near the collarbone, highlighting bone structure with Rembrandt lighting. Frame 2: A crisp profile shot with a focus on the nose, lips, and masculine jawline, gaze directed slightly upward. Frame 3: A frontal, thoughtful portrait with shoulders relaxed and direct eye contact. The composition is clean and modern, using a white T-shirt and gold necklace for visual continuity. Commercial magazine quality, high-end mirrorless camera, authentic skin pores, soft bokeh, and elegant masculinity.
```

[[Identity Preservation]] [[Rembrandt Lighting]] [[Clean Composition]]

---

### 117. 超逼真微缩克隆工作室肖像

**Author**: [Synthia](https://x.com/AIwithSynthia)  **Date**: 2026-02-21  **Language**: en

> 这是一个针对 Nano Banana Pro 的高度具体的提示，要求使用上传的照片作为唯一的面部参考，严格禁止更改面部特征或身份。目标是创作一张超现实的影棚肖像，采用微型克隆概念，其中多个微型版本的主体与真人大小的人物进行互动。

![超逼真微缩克隆工作室肖像](https://cms-assets.youmind.com/media/1771741696375_7vkzi9_HBsRavMbgAACpPt.jpg)
![超逼真微缩克隆工作室肖像](https://cms-assets.youmind.com/media/1771741696339_yp8oym_HBsRc1maoAEkme2.jpg)

```
Use my uploaded photo as the main and only face reference. My face must remain exactly the same — do NOT change facial features, expression, eye shape, nose, lips, skin tone, age, or identity. No face swap, no beautification, no stylization on the face.
Create an ultra-realistic studio portrait using a miniature clone concept:
Main person:
Sitting on the floor, centered in frame, relaxed pose, calm and confident mood. Facial expression must match the reference exactly.
Miniature clones (same face, same identity): Gemini 
• Two miniatures standing on my open palms (palms facing upward)
• One miniature sitting on my right shoulder
• One miniature pushing my right shoe
• One miniature running in the foreground toward the camera (sense of motion but still sharp and realistic)
• One miniature hugging my left knee from behind
All miniatures must have the exact same face, expression, and identity as the main person.
```

[[Identity Preservation]] [[Studio Portrait]] [[Scale Manipulation]]

---

### 118. 巴洛克电影级艺术肖像转换提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-20  **Language**: en

> 一个详细的 JSON 提示，用于使用 Nano Banana Pro 进行图像到图像的转换，旨在创建具有巴洛克、明暗对比美学的电影级美术肖像。该提示指定保留主体的身份、姿势和特征，同时增强真实感、纹理和氛围。它包括光照、相机、场景和主体外观的详细设置。

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "cinematic_fine_art_portrait_transformation",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_BAROQUE_CROWN_CHIAROSCURO_FILM_GRAIN"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_pose": true,
      "preserve_hand_structure": true,
      "notes": "Use the uploaded image as the primary reference. Keep the exact composition: close-up portrait, eyes closed, head slightly tilted, both hands holding/placing the crown on top of the head. Preserve the hair volume/shape (curly), skin proportions, crown position and size, and the dark background. Only enhance realism, texture, and cinematic fine-art mood. Do not add text."
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 1,
      "sharpness": "filmic_soft_crisp",
      "grain": "true_35mm_film",
      "color_grade": "warm_amber_baroque",
      "quality": "maximum"
    },
    "scene": {
      "concept": "a timeless baroque-inspired fine-art portrait of a crowned woman, intimate and regal",
      "environment": "deep black studio void background with subtle falloff, no visible set elements",
      "lighting": {
        "style": "chiaroscuro",
        "key_light": "single soft key from upper-left, warm tungsten tone",
        "fill": "minimal fill, preserve deep shadows",
        "rim": "very subtle rim highlight on hair and crown edges",
        "specular": "controlled, no harsh shine"
      },
      "camera": {
        "framing": "tight head-and-shoulders portrait",
        "lens_look": "85mm portrait, shallow depth of field",
        "aperture_style": "f1.8 look",
        "focus": "focus on face and crown hands, background fully melted"
      },
      "style": {
        "aesthetic": "photoreal cinematic film still meets classical oil-portrait mood",
        "texture": "natural skin texture, subtle pores, soft halation on highlights",
        "retouch": "none, keep authentic imperfections"
      }
    },
    "subject": {
      "person": "adult woman",
      "appearance": {
        "hair": "voluminous curly hair, warm auburn/copper tones, natural frizz details",
        "makeup": "minimal, soft warm lips, natural brows, no heavy glam",
        "expression": "eyes closed, calm, serene, regal stillness",
        "skin": "natural texture, warm highlights, realistic shadow transitions"
      },
      "wardrobe": {
        "neckline": "bare shoulders as in reference",
        "jewelry": "none unless already present"
      },
      "prop": {
        "crown": "metallic crown with geometric points, warm gold tone, realistic metal reflections"
      }
    },
    "negative_prompt": [
      "text",
      "logos",
      "watermarks",
      "extra fingers",
      "missing fingers",
```

[[Identity Preservation]] [[Dramatic Lighting]] [[Fine Art Photography]]

---

### 119. 超逼真穆斯林女性肖像提示词

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-02-19  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超现实、电影级的年轻穆斯林女性肖像，场景设定在斋月期间的清真寺内，重点突出身份认同的保留、自然的皮肤纹理和精神氛围。

![超逼真穆斯林女性肖像提示词](https://cms-assets.youmind.com/media/1771569157536_bs95e6_HBg13a8bAAAgH4q.jpg)

```
{
  "type": "image_generation_prompt",
  "style": "ultra-realistic, cinematic, Muslimah portrait, editorial photography",
  "resolution": "8K",
  "aspect_ratio": "9:16",
  "quality": "masterpiece, best quality, extremely detailed, photorealistic",
  "identity_preservation": {
    "preserve_face": true,
    "strict_identity_lock": true,
    "notes": "Do not alter the face in any way. Maintain exact facial features, skin texture, proportions, and natural expression."
  },
  "subject": {
    "gender": "female",
    "expression": "soft subtle smile, calm and peaceful",
    "appearance": {
      "skin": "flawless, smooth, bright fair skin with visible pores and natural realism",
      "eyes": "clear natural hazel eyes, naturally curled eyelashes",
      "makeup": "bareface, no makeup, natural skin look",
      "lips": "natural ombré lips, soft pink inner tone fading into light nude pink, soft blurred lip line"
    },
    "clothing": {
      "outfit": "elegant black modest Islamic outfit",
      "headwear": "black hijab neatly framing the face"
    },
    "accessories": [
      "gold chain bracelet with a small flower charm",
      "tasbih (prayer beads) held gently in hand"
    ],
    "pose": {
      "position": "standing",
      "hands": "one hand holding tasbih naturally, relaxed posture",
      "body_language": "graceful, modest, calm presence"
    }
  },
  "environment": {
    "location": "inside a mosque",
    "atmosphere": "peaceful spiritual Ramadan Tarawih atmosphere",
    "background_elements": [
      "softly blurred worshippers praying",
      "mosque interior architecture",
      "warm spiritual ambiance"
    ]
  },
  "lighting": {
    "type": "camera flash combined with soft ambient mosque lighting",
    "effects": [
      "glowing natural skin highlights",
      "soft cinematic shadows",
      "balanced exposure",
      "dramatic yet gentle lighting"
    ]
  },
  "camera": {
    "device": "latest iPhone camera",
    "focus": "sharp focus on face and upper body",
    "depth_of_field": "shallow depth with soft background blur",
    "style": "professional smartphone photography",
    "clarity": "ultra sharp, extremely clear"
  },
  "mood": {
    "emotion": "peaceful, spiritual, modest, serene",
    "aesthetic": "natural Muslimah portrait, Instagram-style realism, positive vibes"
  },
  "constraints": [
    "Do not alter the face",
    "No artificial filters",
    "No unrealistic skin smoothing",
    "No distortion",
    "No watermark",
    "No text"
  ],
  "output_goal": "Create an ultra-realistic close-up portrait of a young Muslim woman standing inside a mosque, wearing a black modest outfit and holding tasbih, with glowing natural skin, calm expression, and a peaceful Ramadan spiritual atmosphere."
}
```

[[Identity Preservation]] [[Cinematic Lighting]] [[Cultural Portrait]]

---

### 120. 超逼真编辑级美妆转换（图像到图像）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-18  **Language**: en

> 一个高度结构化的图生图提示，用于生成一张超逼真的编辑级美妆肖像。它要求在保留参考图像中人物姿势和手部结构的同时，将造型转换为日式红色和服主题，搭配相应的配饰，并着重表现细致的皮肤纹理和柔和的美妆光线。

![超逼真编辑级美妆转换（图像到图像）](https://cms-assets.youmind.com/media/1771483111547_shgnkj_HBd_fdqXIAApd6L.jpg)

```
{
 "generation_request": {
 "meta_data": {
 "tool": "NanoBanana Pro",
 "task_type": "ultra_photoreal_editorial_beauty_transformation",
 "version": "v1.0_RED_KIMONO_FAN_HAIRPIN_BEAUTY_EN",
 "priority": "highest",
 "language": "en"
 },

 "input": {
 "mode": "image_to_image",
 "reference_image_usage": "very_high",
 "preserve_pose": true,
 "preserve_hand_structure": true,
 "notes": "Use the uploaded reference image as the composition anchor. Keep the same close-up beauty framing and the hand near the face. Transform wardrobe and styling to a red kimono theme with a matching fan and hair accessory. No text."
 },

 "output_settings": {
 "aspect_ratio": "4:5",
 "orientation": "portrait",
 "resolution_target": "ultra_high_res",
 "render_style": "luxury_editorial_beauty",
 "sharpness": "editorial_crisp_with_real_skin",
 "film_grain": "subtle_or_none",
 "color_grade": "warm_red_lacquer_tones",
 "dynamic_range": "natural_not_hdr",
 "skin_rendering": "real_pores_soft_glow_no_plastic"
 },

 "global_rules": {
 "camera_language": "85mm beauty lens equivalent, tight close-up framing, shallow depth of field, editorial precision",
 "lighting_language": "soft diffused beauty key light + gentle specular highlights on skin + controlled shadow shaping",
 "authenticity_markers": "natural skin texture, visible pores, no AI glow, no HDR, no over-smoothing"
 },

 "creative_prompt": {
 "scene_summary": "High-end editorial beauty portrait with a Japanese-inspired red kimono styling. A matching folding fan and elegant hairpin accessory. Harmonized makeup and nails.",

 "environment": {
 "background": "minimal studio backdrop in warm off-white or very light beige, with a subtle red lacquer ambience clean",
 "lighting": "soft beauty lighting with a slight warm rim light; balanced highlights, no harsh shine"
 },

 "subject": {
 "person": "adult woman",
 "expression": "calm confident editorial gaze",
 "hair": "sleek dark hair styled neatly with a red-and-gold hairpin (kanzashi-inspired), a few soft face-framing strands",
 "makeup": {
 "eyes": "clean winged eyeliner, soft neutral-brown shadow, subtle shimmer on inner corners",
 "brows": "natural defined brows",
 "cheeks": "soft warm blush, slightly rosy but refined",
 "lips": "muted red/rose lacquer lip not overly glossy, lips closed"
 },
 "nails": "short elegant manicure in deep red (wine red) to match the kimono and fan"
 },

 "wardrobe": {
 "kimono": "red silk kimono with subtle tone-on-tone pattern (floral or geometric), premium fabric folds, elegant collar line, no logos",
 "details": "optional thin gold accent trim, tasteful and minimal"
 },

 "props": {
 "fan": "folding hand fan in matching red with gold accents, held near the face/hand area, elegant and harmonious"
 },

 "composition": "tight beauty close-up similar to reference, hand near face visible, jewelry minimal (one statement ring allowed), shallow depth of field, ultra detailed skin and makeup texture"
 },

 "negative_"
```

[[Identity Preservation]] [[Skin Texture Detail]]

---

### 121. 皮克斯贴纸生成提示

**Author**: [Edraak Tech | إدراك تِك](https://x.com/EdraakTechAi)  **Date**: 2026-02-18  **Language**: en

> 一个用于 Nano Banana Pro 的提示，使用上传的照片来创建皮克斯风格的贴纸，贴纸上的人物是照片中的人，带有各种富有表现力、可爱、卡通般的反应，同时保留了人物的发型、特征和服装颜色。

![皮克斯贴纸生成提示](https://cms-assets.youmind.com/media/1771483137283_t0la42_HBdYhDpbUAMjfK0.jpg)
![皮克斯贴纸生成提示](https://cms-assets.youmind.com/media/1771483137279_cwwa19_HBdYhDkbkAAmUZ1.jpg)

```
Create a Pixar sticker sheet based on the person in the photo. The stickers should feature various expressive reactions in a cute, cartoon-like style, keeping the hairstyle, facial features, and outfit colors similar to the reference. Each sticker must have a different mood or gesture: Laughing Smiling sweetly Blushing with heart eyes (love) Angry pout Hand on chin (thinking) Crying with big teary eyes Shocked or surprised Waving hello Sparkling with joy Holding a dessert plate.
```

[[Identity Preservation]]

---

### 122. 图像修复与增强提示

**Author**: [Sandy](https://x.com/Sandykabariya)  **Date**: 2026-02-18  **Language**: en

> 一个用于 Nano Banana Pro 的提示，专注于通过修复撕裂和皱纹、完美恢复色彩、锐化和应用完整 HDR 来修复旧的受损图像，同时严格保留拍摄对象精确的面部特征和表情，模仿尼ikon 单反相机拍摄的照片。

![图像修复与增强提示](https://cms-assets.youmind.com/media/1771483136576_c9a9je_HBdQnyoawAAdAHL.jpg)
![图像修复与增强提示](https://cms-assets.youmind.com/media/1771483136583_sh9ymk_HBdQnxRbsAAxtE0.jpg)

```
"Restore the image while preserving the exact facial identity of the subject and facial expression. Fix any tears, wrinkles and human artifact in the photograph itself. Restore the coloring perfectly, sharpen the image and make it full HDR. It should look like a Nikon DSLR camera took the photograph. Maintain the subjects exact facial features, expression and details. "
```

[[Identity Preservation]]

---

### 123. 高级时装编辑场景重定位提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-18  **Language**: en

> 一个高度结构化的 JSON 提示词，用于 Nano Banana Pro 的图像到图像模式，旨在将一个时尚大片主题（身穿翠绿色亮片连衣裙）从参考图像重新定位到豪华夜间阳台场景，背景为城市灯光散景，同时严格保留主题的身份、姿势和服装细节。

![高级时装编辑场景重定位提示](https://cms-assets.youmind.com/media/1771483133257_z3phyy_HBdIe8dWUAAvDpu.jpg)
![高级时装编辑场景重定位提示](https://cms-assets.youmind.com/media/1771483133258_2klyah_HBdIe8TXEAAwrJ-.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "high_fashion_editorial_scene_relocation",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_EMERALD_BALCONY_CITYLIGHTS_NIGHT"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_pose": true,
      "preserve_body_proportions": true,
      "preserve_hand_structure": true,
      "notes": "Use the uploaded image as the primary anchor. Keep the exact pose, side profile angle, head tilt, hand placement behind the body, ponytail hairstyle, emerald green halter sequin dress design and fit, and the same earrings. Only relocate the environment to a night balcony with a blurred city skyline. Maintain editorial realism and natural anatomy."
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 1,
      "sharpness": "editorial_crisp",
      "grain": "subtle_35mm_film",
      "post_processing": {
        "skin_retouch": "luxury_editorial",
        "texture_preservation": "high",
        "avoid_plastic_skin": true,
        "avoid_ai_glow": true,
        "avoid_hdr": true
      }
    },
    "scene": {
      "concept": "luxury night balcony fashion portrait with city lights bokeh",
      "environment": "high-rise balcony at night, distant city skyline and streetlights rendered as soft bokeh, subtle railing edge hinted, no readable signs",
      "composition": {
        "framing": "3/4 body portrait, same angle as reference, subject dominant, background softly blurred",
        "background_depth": "strong separation with creamy bokeh"
      },
      "lighting": {
        "type": "cinematic_key_light_with_city_ambient",
        "key_light": "soft directional key from camera-left",
        "fill": "minimal soft fill to retain facial detail",
        "rim_light": "subtle cool rim from city ambient",
        "contrast": "medium_high",
        "highlight_behavior": "controlled specular sparkle on sequins without clipping",
        "temperature": "mixed (warm city bokeh + neutral skin key)"
      },
      "camera": {
        "look": "luxury_magazine_editorial_night",
        "lens": "85mm",
        "aperture": "f1.8",
        "depth_of_field": "shallow_background_strong_bokeh",
        "dynamic_range": "balanced_no_hdr",
        "motion": "still_photo"
      }
    },
    "subject": {
      "person": "adult woman",
      "appearance": {
        "hair": "sleek high ponytail, glossy",
        "makeup": "clean glam, defined brows, soft sculpt, natural highlight",
        "expression": "confident downward side gaze"
      },
      "wardrobe": {
        "dress": "emerald green halter neck full-length sequin gown, body-contouring silhouette, unchanged",
        "earrings": "gold statement earrings with green stone detail, unchanged"
      }
    },
    "negative
```

[[Identity Preservation]]

---

### 124. 电影感雨中时尚改造（图像到图像）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-18  **Language**: en

> 一个高度详细、结构化的图生图提示，用于将女性参考图像转换为电影艺术时尚编辑照片。该提示要求保留女性的身份，同时改变她的姿势、服装（深午夜蓝色缎面连衣裙），并让她置身于梵高《星夜》风格雨伞下的可见雨景中。

![电影感雨中时尚改造（图像到图像）](https://cms-assets.youmind.com/media/1771483109599_n73x68_HBcLbmTWkAAOxtN.jpg)
![电影感雨中时尚改造（图像到图像）](https://cms-assets.youmind.com/media/1771483109641_wzdj93_HBcLbmTWMAAM9nb.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "cinematic_rain_fashion_transformation",
      "language": "en",
      "priority": "highest",
      "version": "v2.0_STARRY_RAIN_STANDING_LOOK"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Preserve the same woman's facial identity and proportions. Transform pose to standing naturally under umbrella in rain. Remove coat completely."
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 1,
      "sharpness": "cinematic_crisp",
      "grain": "subtle_35mm_film"
    },
    "scene": {
      "environment": "light stone architectural background softly blurred",
      "weather": "visible rainfall with cinematic rain streaks and soft wet ground reflections",
      "lighting": "overcast rainy daylight with moody contrast",
      "mood": "romantic, artistic, dreamy celestial atmosphere"
    },
    "subject": {
      "person": "adult woman",
      "pose": "standing gracefully under umbrella, one hand holding umbrella handle, other arm relaxed naturally",
      "expression": "soft introspective gaze",
      "wardrobe": {
        "dress": "deep midnight blue satin dress, fluid silhouette, elegant movement, glossy satin reflections",
        "coat": "none",
        "bag": "metallic deep gold structured handbag",
        "boots": "knee-high boots matching the handbag tone (deep metallic gold or warm cognac tone), refined leather texture"
      }
    },
    "umbrella": {
      "color_base": "deep navy blue",
      "design": "Van Gogh Starry Night inspired swirling sky pattern",
      "details": "visible swirling brushstroke-style stars and moon in gold and cobalt tones, painterly texture effect on fabric",
      "finish": "matte umbrella fabric with artistic printed texture"
    },
    "camera": {
      "lens": "50mm prime",
      "aperture": "f/2.0",
      "focus": "sharp on subject, rain slightly motion-blurred",
      "angle": "eye-level cinematic framing"
    },
    "style": {
      "aesthetic": "cinematic art-fashion editorial",
      "color_palette": "midnight blue, cobalt, warm gold, soft stone neutrals",
      "texture_emphasis": "rain droplets on umbrella, satin sheen, painterly umbrella texture",
      "retouching": "natural skin texture preserved",
      "no": "AI glow, plastic skin, extra limbs, distorted anatomy, oversharpening, text, watermark"
    }
  }
}
```

[[Identity Preservation]]

---

### 125. 水下之吻双联画与数码相机屏幕

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-17  **Language**: en

> 一个复杂的 JSON 提示，用于生成一个 2x1 的并排双联画，描绘水下之吻。左侧面板显示一只手拿着一台数码相机，其 LCD 屏幕上显示着这个吻，右侧面板显示完整的、低保真水下照片，强调身份保留和怀旧的数码相机美学。

![水下之吻双联画与数码相机屏幕](https://cms-assets.youmind.com/media/1771396588160_htcjtb_HBYZzhAWoAAq7fM.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "underwater_kiss_diptych_2x1_digicam",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_UNDERWATER_KISS_SONY_SCREEN_DIPTYCH"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_pose": true,
      "preserve_hand_structure": true,
      "notes": "Create a 2x1 side-by-side diptych. LEFT PANEL: a hand holding a silver compact digital camera (Sony-style) showing the underwater kiss on its LCD screen, including camera bezel and screen reflections; RIGHT PANEL: the full underwater kiss photo itself, turquoise water, bubbles, slightly lo-fi digicam look. Keep the same couple pose and intimacy. Preserve identities from references if provided. No extra people."
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 1,
      "layout": {
        "type": "split",
        "direction": "vertical",
        "panels": 2,
        "gutter": "thin"
      },
      "sharpness": "lofi_filmic",
      "grain": "subtle_to_medium"
    },
    "scene": {
      "right_panel_environment": "underwater pool scene, turquoise water, floating bubbles and particles, soft light rays, slight haze",
      "left_panel_environment": "neutral indoor wall background behind the held camera, realistic hand grip, slight glare on LCD"
    },
    "composition": {
      "left_panel": "close shot of the compact camera back with LCD visible; underwater kiss is displayed on the LCD; include slight pixel grid/moire and LCD glow",
      "right_panel": "tight-medium underwater shot of the couple kissing; woman holds man's face with both hands; man holds woman's waist; bubbles around them"
    },
    "style": {
      "aesthetic": "nostalgic digicam / early-2010s compact camera look",
      "color": "cool cyan/teal underwater tones, slightly muted",
      "texture": "light compression artifacts, mild softness, realistic water distortion"
    },
    "negative_prompt": "extra people, face morphing, identity drift, deformed hands, extra fingers, extra limbs, text overlays, captions, watermark, logos, brand marks, timestamps, UI numbers, harsh HDR, cartoon"
  }
}
```

[[Identity Preservation]]

---

### 126. 浪漫海滩情侣特写，同时保护身份

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-12  **Language**: en

> 一个复杂、结构化的提示，用于生成一张浪漫、真实的岩石海滩情侣特写。此提示专为图像到图像生成而设计，需要参考图像以最大程度地保留两位人物的面部特征和发型，同时描绘男子将一朵洋红色花朵别在女子耳后的场景。

![浪漫海滩情侣特写，同时保护身份](https://cms-assets.youmind.com/media/1770964566366_lhr6j0_HA_YI_pWoAEqkuV.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "cinematic_romantic_couple_beach_closeup",
      "language": "en",
      "priority": "highest",
      "version": "v1.1_BEACH_FLOWER_TUCK_STRICT_IDENTITY_HAIRLOCK"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Match the uploaded reference faces with maximum likeness. Keep facial structure, eyes, nose, lips, smile, skin tone, hairline, and ALL hair attributes texture exactly consistent with the reference. Do not change age. No stylization. No identity drift."
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 4,
      "sharpness": "high",
      "grain": "subtle_analog"
    },
    "scene": {
      "concept": "romantic candid moment at a rocky beach",
      "environment": "rock formations in the background, soft overcast daylight, calm seaside atmosphere",
      "composition": "tight medium close-up, couple fills frame, shallow depth of field, background softly blurred",
      "action": "man gently tucks a bright magenta flower behind the woman's ear while she smiles warmly and looks up at him"
    },
    "subject": {
      "couple": {
        "woman": {
          "identity": "Use the uploaded reference woman's face as the primary identity anchor with maximum likeness.",
          "expression": "genuine joyful smile, eyes slightly squinting with happiness",
          "hair": "HAIR MUST MATCH REFERENCE ,
          "wardrobe": {
            "dress": "white strappy summer dress, fitted bodice, minimal texture, elegant and clean"
          },
          "details": {
            "nails": "red manicure",
            "jewelry": "delicate minimal gold jewelry (optional)"
          }
        },
        "man": {
          "identity": "Use the uploaded reference man's face as the primary identity anchor with maximum likeness.",
          "expression": "soft affectionate focus on the woman",
          "hair": "HAIR MUST MATCH REFERENCE ,
          "wardrobe": {
            "shirt": "white long-sleeve button-up shirt, lightweight fabric, casual beach styling"
          },
          "accessories": "subtle gold-toned wristwatch"
        }
      }
    },
    "lighting": {
      "style": "natural soft daylight",
      "direction": "diffused top/side light",
      "contrast": "soft",
      "skin_rendering": "realistic pores and texture, no plastic look"
    },
    "camera": {
      "lens": "50mm",
      "aperture": "f2.0",
      "depth_of_field": "shallow",
      "focus": "eyes and smiles in sharp focus"
    },
    "color_grading": {
      "look": "warm cinematic film tones",
      "palette": [
        "warm sand beige",
        "muted olive rock tones",
        "soft cream whites",
        "magenta flower accent"
      ],
      "highlights": "warm",
      "shadows": "slig
```

[[Identity Preservation]] [[Close-Up Portrait]] [[Romantic Scene]]

---

### 127. 情人节巧克力与玫瑰编辑肖像

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-02-12  **Language**: en

> 一个高度具体的提示，用于将上传的图像转换为情人节主题的编辑肖像，描绘主体躺在报纸上，周围环绕着红玫瑰和手工巧克力，并带有心形闪光效果，同时严格保留肖像的相似度。

![情人节巧克力与玫瑰编辑肖像](https://cms-assets.youmind.com/media/1770964560280_3ldani_HA9AUpnaoAAABFo.jpg)

```
Use uploaded image (face+shoulders) — preserve likeness exactly; top-down 4:5 close-up of subject lying on densely layered, readable newspapers (folded paper in hands headline "Valentine's Day"); hair fanned; tailored red blazer over white shirt with tiny red "ImagineArt" + heart; scattered deep-red roses, loose petals, open artisanal chocolate box near hands with assorted chocolates (one truffle bitten revealing creamy filling), loose chocolates, crumbs, cocoa dusting and faint cocoa speck on fingertips; two red heart foil balloons at top corners; heart-shaped gobo/flash across face & half body; subject wears heart-shaped chocolate-frame glasses with pink translucent lenses (eyes visible); pin-sharp face, hands, main chocolates/rose cluster with creamy bokeh (85mm/100mm, f/1.8–2.8), ISO100–200, ~1/125s, full-frame, 4K+; warm top-left softbox + subtle warm rim from right; Kodak-Portra warm toning, rich saturated reds, slight film grain; microdetail: hair strands, fabric weave, skin pores, petal veins, chocolate gloss/speculars, tiny melted gloss bead, cocoa powder texture, crumbs, faint foil fingerprint; subtle imperfections: one slightly crushed petal, small cocoa smudge on newspaper edge; ultra-realistic magazine-editorial — no added text or watermark.
```

[[Identity Preservation]] [[Valentine Theme]]

---

### 128. 电影级人像模式，保留身份特征

**Author**: [The Prompt Engineer](https://x.com/rorschachvibes)  **Date**: 2026-02-12  **Language**: en

> 一个高度具体的图像到图像生成提示，旨在 100% 准确地保留主体的面部特征，同时呈现出电影般的侧面肖像，具有强烈的黄金时段光线和浅景深。

![电影级人像模式，保留身份特征](https://cms-assets.youmind.com/media/1770964551091_a72xjt_HA7bJLAa0AAvOpT.jpg)

```
Create a 3:4 high-quality, cinematic profile portrait using the uploaded image as the only identity reference. Preserve her face with 100% accuracy with no changes to facial structure, proportions, or features. The subject is a beautiful young woman with dark hair styled in a loose, messy bun, wearing oversized black eyeglasses. She is dressed in a dark blue denim jacket worn off one shoulder, revealing the collarbone naturally. Pose is a clean side profile with eyes closed, serene and calm expression. Strong warm golden-hour side lighting hits from one direction, creating dramatic contrast, luminous highlights on the skin, and deep soft shadows for sculptural depth. Plain neutral gray studio background, minimal and distraction-free. Shot on an 85mm lens look, shallow depth of field, sharp focus on facial contours, visible skin texture, fashion editorial photography style, cinematic realism, high detail, professional studio quality.
```

[[Identity Preservation]] [[Shallow Depth Of Field]] [[Cinematic Photography]] [[Side Profile Portrait]]

---

### 129. 四姿态工作室造型册网格，带身份保留

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-11  **Language**: en

> 一个复杂的 JSON 提示，专为图像到图像生成而设计，用于创建四格工作室时尚画册网格。该提示严格要求保留参考图像中的面部特征，同时生成一位女性穿着象牙色雪纺露背迷你连衣裙在柔和的编辑灯光下的四种不同姿势。

![四姿态工作室造型册网格，带身份保留](https://cms-assets.youmind.com/media/1770878340883_blaleo_HA5SMoIbsAAXQZT.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "studio_fashion_editorial_lookbook_quad_pose",
      "language": "en",
      "priority": "highest",
      "version": "v1.1_IVORY_CHIFFON_HALTER_LOOKBOOK_GRID_FACE_MATCH"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Use the provided reference image as the facial identity anchor. The model’s FACE must closely match the reference (very similar). Keep the overall lookbook grid style and studio setup. Do NOT change the person into someone else."
    },
    "output": {
      "aspect_ratio": "2:3",
      "resolution": "ultra_high",
      "num_images": 1,
      "layout": {
        "type": "grid",
        "rows": 2,
        "cols": 2,
        "gutter": "thin"
      },
      "sharpness": "high",
      "grain": "subtle_analog"
    },
    "scene": {
      "concept": "minimal studio lookbook collage with soft editorial light",
      "environment": "clean off-white studio wall backdrop, seamless floor, neutral studio setting, no clutter",
      "mood": "elegant, airy, understated, high-end boutique lookbook"
    },
    "subject": {
      "person": "adult woman",
      "identity_consistency": "model across all panels",
      "face_match": "very_high lips",
      "expression": "calm, slightly sultry, neutral editorial gaze",
      "hair": "long dark hair, soft waves, center part (similar to reference), tidy and glossy; allow subtle variation but keep overall match",
      "makeup": "soft neutral glam, defined eyeliner, natural nude lips (match reference makeup vibe)",
      "accessories": "small gold hoop earrings, delicate rings/bracelet",
      "wardrobe": {
        "dress": "ivory / champagne chiffon halter mini dress with high neck band, airy layered bubble hem, semi-sheer flowing fabric, open back with long scarf-like tie draping down"
      },
      "shoes": "minimal strappy heels or sandals in nude/ivory"
    },
    "poses_grid": {
      "panel_1_top_left": "front 3/4 pose, one arm bent with hand resting near neck, relaxed posture",
      "panel_2_top_right": "side profile pose, holding a small ivory woven clutch, looking off-camera",
      "panel_3_bottom_left": "back view showcasing open back and long tie drape, head turned slightly to show profile",
      "panel_4_bottom_right": "front pose with one hand behind head, subtle contrapposto, gaze to the side"
    },
    "camera": {
      "shot_type": "lookbook / editorial",
      "lens": "50mm",
      "aperture": "f/3.2",
      "focus": "tack sharp on face and garment texture, consistent exposure across panels",
      "framing": "full-body to 3/4 body depending on panel, consistent scale"
    },
    "lighting": {
      "setup": "soft key light from camera-left, gentle fill from right, minimal shadow hardness",
      "look": "clean studio editorial, no harsh flash",
```

[[Identity Preservation]] [[Four Panel Grid]]

---

### 130. 具有文化服饰的逼真时尚肖像模板

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-02-11  **Language**: en

> 一个可复用的 JSON 提示模板，旨在生成具有文化服饰（例如，纱丽）的超逼真时尚肖像。该模板要求严格保留参考图像中的面部特征，并指定电影级真实感、8K 分辨率、详细的服装描述和柔和的摄影棚灯光。

![具有文化服饰的逼真时尚肖像模板](https://cms-assets.youmind.com/media/1770878350037_fhnzgg_HA4eVUNaIAAeEsc.jpg)
![具有文化服饰的逼真时尚肖像模板](https://cms-assets.youmind.com/media/1770878350039_wwpzqo_HA4eVTtXAAA6hJN.jpg)
![具有文化服饰的逼真时尚肖像模板](https://cms-assets.youmind.com/media/1770878350033_wumhbd_HA4eVUgaQAAdmbg.jpg)
![具有文化服饰的逼真时尚肖像模板](https://cms-assets.youmind.com/media/1770878351066_ejzims_HA4eVUhagAA35mS.jpg)

```
{
  "meta": {
    "purpose": "Photorealistic fashion portrait with cultural attire for editorial visuals",
    "style": "Cinematic realism, ultra-clean AI-edited, 8K resolution"
  },
  "reference_image": {
    "use": true,
    "face_preservation": "strict, unchanged original face"
  },
  "subject": {
    "gender": "{argument name="gender" default="female"}",
    "expression": "{argument name="expression" default="serene subtle smile, calm gaze downward"}",
    "skin": "smooth glowing, visible pores, natural imperfections",
    "hair": "{argument name="hair style" default="long voluminous waves, dark brown"}",
    "outfit": {
      "type": "[e.g., traditional saree with embroidered blouse]",
      "colors": "[e.g., dusty pink with silver accents]",
      "details": "intricate floral motifs, sheer sleeves"
    }
  },
  "pose": {
    "body": "[e.g., seated elegant, slight angle]",
    "arms": "[e.g., relaxed in lap]"
  },
  "environment": {
    "background": "[e.g., neutral dark grey studio]",
    "lighting": "soft diffused studio, gentle shadows"
  },
  "camera_specs": {
    "framing": "mid-shot three-quarter",
    "depth_of_field": "shallow",
    "aspect_ratio": "[e.g., 3:4 vertical]"
  },
  "negative": ["blurry", "artifacts", "plastic skin", "distorted proportions"]
}
```

[[Identity Preservation]] [[Soft Studio Lighting]] [[Cinematic Realism]] [[8K Portrait]]

---

### 131. Z 世代时尚肖像：Labubu 与猫咪提示词

**Author**: [simeon-sanai](https://x.com/Naiknelofar788)  **Date**: 2026-02-11  **Language**: en

> 生成一张超现实影棚照片的提示词，照片中人物（身份信息保留自参考照片）身穿 Z 世代街头服饰，倚靠在一个真人大小的毛绒 Labubu 玩偶上，旁边有一只超现实的英国短毛猫，所有元素都置于充满活力的橙色影棚背景中。

![Z 世代时尚肖像：Labubu 与猫咪提示词](https://cms-assets.youmind.com/media/1770878336311_11vswr_HA4TRLRaoAAtLCA.jpg)

```
Create a hyper-realistic, high-detail studio photoshoot featuring the same person from the reference photo with the exact facial features, skin tone, hairstyle, proportions, and identity fully preserved (no changes to face or structure). She is wearing stylish Gen-Z fashion attire trendy, minimal, modern streetwear. She is leaning casually on a realistic, fluffy, life-sized Labubu character, rendered in soft fur texture with playful expression. A British Shorthair cat sits or poses nearby, also hyperrealistic with detailed fur and natural posture.

The entire scene is set against a smooth, seamless, vibrant orange studio backdrop with professional studio lighting, crisp shadows, clean highlights, and a premium fashion editorial vibe. Ultra-photorealistic, flawless skin texture (but unchanged identity), high-end photography style, full-body or mid-shot composition.
```

[[Identity Preservation]] [[Orange Studio Background]] [[British Shorthair Cat]]

---

### 132. 悉尼·斯威尼 (Sydney Sweeney) 在海滩上的时尚肖像

**Author**: [Shourya](https://x.com/ShouryaAI)  **Date**: 2026-02-11  **Language**: en

> 一个极其详细、结构化的提示，用于生成一张悉尼·斯威尼 (Sydney Sweeney) 在鹅卵石海滩上的超写实时尚编辑肖像照，重点在于严格的身份保留、自然的身体结构和特定服装（金属粉色泳衣连衣裙）。

![悉尼·斯威尼 (Sydney Sweeney) 在海滩上的时尚肖像](https://cms-assets.youmind.com/media/1770878352815_da29vc_HA2qGWkaAAcE_2C.jpg)

```
{
  "prompt_specification": {
    "type": "Ultra-realistic cinematic fashion portrait",
    "subject": {
      "identity": {
        "name": "{argument name="celebrity name" default="Sydney Sweeney"}",
        "constraint_strictness": "100%",
        "directives": [
          "Preserve exact facial identity from reference",
          "Unchanged body proportions from reference",
          "Same facial features only",
          "No face alteration",
          "No body reshaping",
          "No stylization",
          "Natural anatomy must remain accurate"
        ]
      },
      "physical_attributes": {
        "body_type": "Curvy woman with natural proportions",
        "skin": {
          "tone": "Natural, exactly matching the reference",
          "texture": "Natural skin texture with visible pores",
          "highlights": "Realistic highlights",
          "negative_constraint": "No plastic skin"
        },
        "hair": {
          "directive": "Identical to reference",
          "properties": ["color", "length", "texture", "styling"]
        },
        "expression": "Strong confident pout toward the camera"
      },
      "pose_and_action": {
        "stance": "Standing, posture balanced and anatomically correct",
        "limb_placement": {
          "arm_1": "gently on her neck",
          "arm_2": "resting on her thigh"
        },
        "camera_view": "Medium low-angle, three-quarter front view"
      }
    },
    "attire": {
      "garment": {
        "item": "One-piece swimsuit dress",
        "color": "Soft metallic pink",
        "cut": ["high-cut sides", "thigh-high slit"],
        "fabric_physics": ["realistic stretch", "folds", "sheen"]
      },
      "details": {
        "chest_piece": {
          "item": "Gold brooch detail at the bust",
          "note": "color change only, no design alteration"
        },
        "jewelry": {
          "items": ["Gold bangles", "gold hoop earrings"],
          "properties": ["realistic metallic reflections", "realistic scale"]
        }
      }
    },
    "environment": {
      "setting_type": "Clean natural coastal atmosphere",
      "composition_layers": {
        "foreground": "Pebbled beach (subject standing here)",
        "mid_ground": [
          "turquoise sea behind the subject",
          "rocky coastal cliffs catching late afternoon light"
        ],
        "background/horizon": "small distant sailboat on the horizon"
      }
    },
    "photography_style": {
      "aesthetic": [
        "Hyper-detailed photorealism",
        "professional editorial finish",
        "high-end fashion editorial realism"
      ],
      "quality_metric": "8K RAW quality",
      "composition_ratio": "Vertical 9:16",
      "lighting": {
        "source": "Natural daylight",
        "time": "Warm late afternoon",
        "qualities": ["cinematic lighting balance", "controlled highlights and shadows"]
      },
      "optics_and_focus": {
        "lens_emulation": "DSLR 85mm l"
```

[[Identity Preservation]] [[Fashion Editorial]] [[Sydney Sweeney]]

---

### 133. 超逼真时尚肖像 (形似 Sydney Sweeney)

**Author**: [alexander](https://x.com/alexgarcia_XX)  **Date**: 2026-02-07  **Language**: en

> 一个高度受限的 JSON 提示，用于生成超现实的电影级时尚肖像，明确要求 100% 保留主体（Sydney Sweeney）的身份、自然身体比例和皮肤纹理，穿着金属青铜色泳衣连衣裙，置身于海岸环境中。

![超逼真时尚肖像 (形似 Sydney Sweeney)](https://cms-assets.youmind.com/media/1770532771883_exxh03_HAlhz6UaEAA6NIa.jpg)
![超逼真时尚肖像 (形似 Sydney Sweeney)](https://cms-assets.youmind.com/media/1770532771849_2yyvit_HAlh1FUacAcVoMO.jpg)
![超逼真时尚肖像 (形似 Sydney Sweeney)](https://cms-assets.youmind.com/media/1770532772046_q953gt_HAlhx6VaYAAO3QD.jpg)

```
{
  "prompt_specification": {
    "type": "Ultra-realistic cinematic fashion portrait",
    "subject": {
      "identity": {
        "name": "Sydney Sweeney",
        "constraint_strictness": "100%",
        "directives": [
          "Preserve exact facial identity from reference",
          "Unchanged body proportions from reference",
          "Same facial features only",
          "No face alteration",
          "No body reshaping",
          "No stylization",
          "Natural anatomy must remain accurate"
        ]
      },
      "physical_attributes": {
        "body_type": "Curvy woman with natural proportions",
        "skin": {
          "tone": "Natural, exactly matching the reference",
          "texture": "Natural skin texture with visible pores",
          "highlights": "Realistic highlights",
          "negative_constraint": "No plastic skin"
        },
        "hair": {
          "directive": "Identical to reference",
          "properties": ["color", "length", "texture", "styling"]
        },
        "expression": "Strong confident pout toward the camera"
      },
      "pose_and_action": {
        "stance": "Standing, posture balanced and anatomically correct",
        "limb_placement": {
          "arm_1": "gently on her neck",
          "arm_2": "resting on her thigh"
        },
        "camera_view": "Medium low-angle, three-quarter front view"
      }
    },
    "attire": {
      "garment": {
        "item": "One-piece swimsuit dress",
        "color": "Metallic bronze",
        "cut": ["high-cut sides", "thigh-high slit"],
        "fabric_physics": ["realistic stretch", "folds", "sheen"]
      },
      "details": {
        "chest_piece": {
          "item": "Gold brooch detail at the bust",
          "note": "color change only, no design alteration"
        },
        "jewelry": {
          "items": ["Gold bangles", "gold hoop earrings"],
          "properties": ["realistic metallic reflections", "realistic scale"]
        }
      }
    },
    "environment": {
      "setting_type": "Clean natural coastal atmosphere",
      "composition_layers": {
        "foreground": "Pebbled beach (subject standing here)",
        "mid_ground": [
          "turquoise sea behind the subject",
          "rocky coastal cliffs catching late afternoon light"
        ],
        "background/horizon": "small distant sailboat on the horizon"
      }
    },
    "photography_style": {
      "aesthetic": ["Hyper-detailed photorealism", "professional editorial finish", "high-end fashion editorial realism"],
      "quality_metric": "8K RAW quality",
      "composition_ratio": "Vertical 9:16",
      "lighting": {
        "source": "Natural daylight",
        "time": "Warm late afternoon",
        "qualities": ["cinematic lighting balance", "controlled highlights and shadows"]
      },
      "optics_and_focus": {
        "lens_emulation"
```

[[Identity Preservation]] [[Hyperrealistic Photography]] [[Celebrity Likeness Portrait]] [[Golden Hour Lighting]]

---

### 134. Sydney Sweeney 电影级时尚肖像，具有严格的身份约束

**Author**: [Yaseen Khan Gul](https://x.com/YaseenK7212)  **Date**: 2026-02-07  **Language**: en

> 一个高度受限的 JSON 提示，用于生成 Sydney Sweeney 超逼真的电影级时尚肖像。它强制 100% 保留她精确的面部特征和自然的身体比例，详细描述了她的金属青铜色泳衣连衣裙、姿势，以及一个拥有温暖的傍晚光线的干净自然海岸环境。

![Sydney Sweeney 电影级时尚肖像，具有严格的身份约束](https://cms-assets.youmind.com/media/1770532759674_uvoe7m_HAlPEI1WoAAL3DU.jpg)
![Sydney Sweeney 电影级时尚肖像，具有严格的身份约束](https://cms-assets.youmind.com/media/1770532759559_chrrvs_HAlPEI2WYAAg27p.jpg)
![Sydney Sweeney 电影级时尚肖像，具有严格的身份约束](https://cms-assets.youmind.com/media/1770532759681_0xg2rq_HAlPEIxW0AAuHG4.jpg)

```
{
  "prompt_specification": {
    "type": "Ultra-realistic cinematic fashion portrait",
    "subject": {
      "identity": {
        "name": "{argument name="subject name" default="Sydney Sweeney"}",
        "constraint_strictness": "100%",
        "directives": [
          "Preserve exact facial identity from reference",
          "Unchanged body proportions from reference",
          "Same facial features only",
          "No face alteration",
          "No body reshaping",
          "No stylization",
          "Natural anatomy must remain accurate"
        ]
      },
      "physical_attributes": {
        "body_type": "Curvy woman with natural proportions",
        "skin": {
          "tone": "Natural, exactly matching the reference",
          "texture": "Natural skin texture with visible pores",
          "highlights": "Realistic highlights",
          "negative_constraint": "No plastic skin"
        },
        "hair": {
          "directive": "Identical to reference",
          "properties": ["color", "length", "texture", "styling"]
        },
        "expression": "Strong confident pout toward the camera"
      },
      "pose_and_action": {
        "stance": "Standing, posture balanced and anatomically correct",
        "limb_placement": {
          "arm_1": "gently on her neck",
          "arm_2": "resting on her thigh"
        },
        "camera_view": "Medium low-angle, three-quarter front view"
      }
    },
    "attire": {
      "garment": {
        "item": "One-piece swimsuit dress",
        "color": "Metallic bronze",
        "cut": ["high-cut sides", "thigh-high slit"],
        "fabric_physics": ["realistic stretch", "folds", "sheen"]
      },
      "details": {
        "chest_piece": {
          "item": "Gold brooch detail at the bust",
          "note": "color change only, no design alteration"
        },
        "jewelry": {
          "items": ["Gold bangles", "gold hoop earrings"],
          "properties": ["realistic metallic reflections", "realistic scale"]
        }
      }
    },
    "environment": {
      "setting_type": "Clean natural coastal atmosphere",
      "composition_layers": {
        "foreground": "Pebbled beach (subject standing here)",
        "mid_ground": [
          "turquoise sea behind the subject",
          "rocky coastal cliffs catching late afternoon light"
        ],
        "background/horizon": "small distant sailboat on the horizon"
      }
    },
    "photography_style": {
      "aesthetic": ["Hyper-detailed photorealism", "professional editorial finish", "high-end fashion editorial realism"],
      "quality_metric": "8K RAW quality",
      "composition_ratio": "Vertical 9:16",
      "lighting": {
        "source": "Natural daylight",
        "time": "Warm late afternoon",
        "qualities": ["cinematic lighting balance", "controlled highlights and shadows"]
      },
      "optics_and_focus": {
        "lens_emulation"
```

[[Identity Preservation]] [[Hyperrealistic Photography]] [[Celebrity Likeness Portrait]] [[Golden Hour Lighting]]

---

### 135. 漫画海报插画模板

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-02-07  **Language**: en

> 一个为 Nano Banana Pro 设计的结构化 JSON 提示模板，旨在生成一张动态、现代的漫画书海报插图（16:9 宽高比），其中包含漫画分镜拼贴、半色调效果和戏剧性照明。它包括主要角色、标题和特定分镜内容的占位符，并要求严格保留参考图像中的身份。

![漫画海报插画模板](https://cms-assets.youmind.com/media/1770532808397_ujmk1l_HAkaf_pXYAAe3ik.jpg)
![漫画海报插画模板](https://cms-assets.youmind.com/media/1770532808377_1ecwqa_HAkaf_cXUAA3che.jpg)
![漫画海报插画模板](https://cms-assets.youmind.com/media/1770532809361_jx3iu6_HAkaf_gXgAA_XAA.jpg)
![漫画海报插画模板](https://cms-assets.youmind.com/media/1770532809700_lpzdgw_HAkaf_hW4AASiEO.jpg)

```
{
  "meta": {
    "purpose": "Comic book poster illustration for viral sci-fi storytelling or graphic novels",
    "style": "Modern comic/graphic novel with halftone and dynamic effects, 4K resolution"
  },
  "reference_image": {
    "use": true,
    "identity_preservation": "strict",
    "face_similarity": "high"
  },
  "canvas": {
    "aspect_ratio": "16:9",
    "orientation": "horizontal poster"
  },
  "title_text": {
    "text": "{argument name="title text" default="ZOOM!!! OR Your Title"}",
    "position": "top_center",
    "style": "bold comic lettering, thick hand-drawn font",
    "color": "cream white with black outline",
    "effects": ["3D emboss", "ink shadow", "halftone texture"]
  },
  "main_character": {
    "subject": "{argument name="main character" default="Space pilot with metallic implant OR Your hero"}",
    "pose": "[e.g., Angry heroic OR Dynamic action]",
    "lighting": "dramatic rim lighting",
    "render_style": "Japanese Anime comic illustration"
  },
  "comic_panels": [
    {
      "position": "top_left",
      "subject": "[e.g., Extreme close-up behind cracked glass]",
      "expression": "[e.g., Angry]",
      "panel_effect": "[e.g., Burst explosion, sound effect CRAAACK]"
    },
    {
      "position": "top_right",
      "subject": "[e.g., Pilot mouth open]",
      "expression": "[e.g., Worried]",
      "speech_text": "[e.g., NOOO!]"
    },
    {
      "position": "bottom_left",
      "subject": "[e.g., Spacecraft profile]",
      "speech_text": "[e.g., WHAAA?!]",
      "motion_lines": true
    },
    {
      "position": "bottom_right",
      "subject": "[e.g., Pilot scared]",
      "speech_text": "[e.g., LAZARUS!]",
      "panel_effect": "[e.g., Starburst]"
    }
  ],
  "background": {
    "style": "comic panels collage",
    "colors": ["orange", "yellow", "blue", "teal"],
    "elements": ["halftone dots", "ink splashes", "action lines", "explosion shapes"],
    "bottom_scene": "[e.g., Asteroid field with gold veins]"
  },
  "art_style": {
    "genre": "modern comic book",
    "influences": ["Marvel covers", "DC posters", "Pop-art"],
    "line_work": "clean bold outlines",
    "shading": "soft painterly with halftone"
  },
  "render_quality": {
    "detail_level": "high",
    "sharpness": "crisp",
    "color_grading": "vibrant cinematic"
  },
  "constraints": {
    "no_blur": true,
    "no_extra_faces": true,
    "no_watermark": true
  },
  "negative_prompt": ["low quality", "blurry", "extra limbs", "distorted face", "bad anatomy", "realistic photo"]
}
```

[[Identity Preservation]] [[Dramatic Lighting]] [[Character Illustration]]

---

### 136. Sadie Sink 肖像的详细生物特征和环境提示

**Author**: [RubenSalvo](https://x.com/RubenSalvo_)  **Date**: 2026-02-07  **Language**: en

> 一个为 Nano Banana Pro 设计的极其详细、结构化的 JSON 提示，旨在生成 Sadie Sink 的逼真图像。它详细说明了精确的生物特征细节（面部结构、皮肤纹理、头发形态）、身体比例、服装、姿势以及特定环境（黄色校车旁的沙滩），并包含详细的灯光和颜色代码。

![Sadie Sink 肖像的详细生物特征和环境提示](https://cms-assets.youmind.com/media/1770532748657_ts7maj_HAkDgusWQAAYyHR.jpg)
![Sadie Sink 肖像的详细生物特征和环境提示](https://cms-assets.youmind.com/media/1770532748486_m99mlb_HAkDfOkWAAAVHPJ.jpg)
![Sadie Sink 肖像的详细生物特征和环境提示](https://cms-assets.youmind.com/media/1770532750403_2gjwkp_HAkDgCGXgAAHblo.jpg)

```
{
  "subject": {
    "identity": {
      "biometric_reference": "Sadie Sink",
      "facial_structure": {
        "zygomatic_arch": "prominent, angular cheekbones characteristic of reference subject",
        "mandible_jawline": "defined, softly rounded jawline",
        "nasal_morphology": "slender bridge, slightly upturned tip",
        "ocular_region": {
          "iris_pattern": "detailed blue iris texture with radial fibers and distinct limbal ring",
          "eye_shape": "large, round eyes, prominent upper lids",
          "brow_shape": "natural, arched, medium thickness brows"
        },
        "oral_region": {
          "lip_shape": "full, well-defined lips, Cupid's bow present",
          "dentition": "accurate dental arch, visible front teeth in relaxed pose"
        }
      },
      "skin_analysis": {
        "tone": "pale, warm undertone (HEX #FFE0C4)",
        "texture": "smooth, fine grain, natural freckles scattered across nose, cheeks, and arms",
        "subsurface_scattering": "realistic light penetration on skin"
      },
      "hair_morphology": {
        "color": "auburn/copper (HEX #B05C2C)",
        "texture": "wavy, voluminous, sun-bleached highlights",
        "style": "loose, windswept, falling over shoulders and back"
      }
    },
    "body": {
      "somatotype": "ectomorph-mesomorph blend, slender build",
      "proportions": {
        "waist_to_hip_ratio": "natural, defined waistline",
        "muscle_tone": "lean, athletic definition in abdomen and arms"
      },
      "pose": "standing, leaning against bus, left hand holding popsicle near shoulder, right arm down, relaxed gaze towards camera",
      "hands": {
        "morphology": "slender fingers, accurate anatomy",
        "nails": "manicured, painted red (HEX #A00000)"
      }
    },
    "attire": {
      "top": {
        "type": "cropped tank top",
        "color": "white cotton fabric (HEX #FFFFFF)",
        "text_content": "Enjoy my Curves",
        "text_style": "red script font, centered on chest"
      },
      "bottom": {
        "type": "high-waisted athletic shorts",
        "color": "red nylon blend (HEX #FF0000)",
        "details": "white piping trim along side seams and hem"
      },
      "accessories": {
        "handheld_object": {
          "type": "popsicle",
          "color": "red (HEX #A00000)",
          "state": "melting slightly, held by wooden stick"
        },
        "bag": {
          "type": "small red handbag with white trim",
          "material": "leather-like texture",
          "placement": "held by straps in left hand"
        }
      }
    }
  },
  "environment": {
    "setting": "sandy beach next to yellow school bus",
    "bus_details": {
      "color": "yellow (HEX #FFCC00)",
      "condition": "weathered paint, visible rivets, windows reflecting light"
    },
    "ground": "fine sand, footprints present",
    "lighting": {
      "type": "natural "
```

[[Identity Preservation]] [[Structured JSON Prompt]] [[Hyperrealistic Photography]] [[Celebrity Likeness Portrait]]

---

### 137. 从单张图像参考生成电影级 3x2 故事板网格

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-02-05  **Language**: en

> 一个复杂的多步骤提示，旨在从一张上传的照片（詹妮弗 · 劳伦斯）生成一个电影级的 3x2 故事板网格（6 帧）。它要求在保留主体身份和环境的同时，通过改变摄像机角度（广角、中景、低角度、特写、动态、最终镜头）来创建叙事流程，强调真实感和电影一致性。

![从单张图像参考生成电影级 3x2 故事板网格](https://cms-assets.youmind.com/media/1770359903131_cw2sws_HAZZkLDakAErD1-.jpg)

```
Use the uploaded photograph as the only visual reference.
The person’s identity must be preserved with maximum accuracy: face, facial features, age, gender, body proportions, and overall appearance must remain unchanged.
Do not invent or add anything that does not exist in the original image.

Step 1: Detailed visual analysis of the source image
First, perform a careful visual analysis of the uploaded image, including:
Who is in the image (person, number of people, position in frame)
Body pose and direction of gaze
Facial expression and emotional mood
Clothing and accessories
Lighting conditions, time of day, color temperature
Environment, background, and depth of space
Overall emotional tone of the scene

Step 2: Cinematic 3×2 storyboard grid
After the analysis, create a cinematic 3×2 grid (6 frames) from the single image, as if it were a sequence of shots from a film.

Global requirements for the entire grid:
Format: one image containing a 3×2 grid
All frames must be numbered 1–6, left to right, top to bottom
Visual style: realistic, cinematic, non-illustrative
One consistent character and environment with logical continuity
Each frame must differ by pose, camera angle, or camera distance
The sequence should feel like time is passing and the scene is developing
No facial distortion, no change in identity or appearance

Frame descriptions:

Frame 1 (No. 1)
Wide establishing shot.
The camera is farthest from the subject, showing the full environment and context.
The person feels like part of the surrounding space.

Frame 2 (No. 2)
Medium shot.
The camera moves closer.
The pose changes slightly, revealing inner emotion or state of mind.

Frame 3 (No. 3)
Low-angle or side-angle shot.
Adds drama or tension, emphasizing body shape and perspective.

Frame 4 (No. 4)
Close-up or medium close-up.
Focus on the face, eyes, and emotion.
Fine details are clearly visible.

Frame 5 (No. 5)
Dynamic angle: diagonal composition or camera movement.
The pose changes the most, creating a sense of action or momentum.

Frame 6 (No. 6)
Final shot.
Calm, reflective, or emotionally resolved.
The camera may be closer or farther, but the frame feels like a conclusion.

Lighting & cinematic consistency:
Lighting must remain logically consistent across all frames, as if filmed in one continuous scene.

Depth of field, lighting, and color grading should reinforce a cinematic look.

Final result:
The output should resemble a professional cinematic storyboard, captured in a single take and location, with strong realism and narrative flow.
```

[[Identity Preservation]]

---

### 138. 参考图像的服装替换工作流程

**Author**: [Shine by Nous ✨](https://x.com/Shinebynous)  **Date**: 2026-02-03  **Language**: en

> 描述了使用 Gemini 3 和 Nano Banana Pro 来保持角色身份，同时迭代更换服装的工作流程。初始提示会根据参考图像更改服装，后续迭代则使用新生成的图像作为基础进行进一步的服装更改。

![参考图像的服装替换工作流程](https://cms-assets.youmind.com/media/1770187185646_9rs5s7_HAQHhNCXYAAovQK.jpg)

```
I started with two reference images and a simple first prompt:
" Change the clothes of the woman to the {argument name="new outfit" default="yellow and green outfit"}, keep her face the same" 

Once I had that result, I reused the generated image as the new base. 
I added a fresh outfit reference and kept the prompt structure identical, only changing the outfit name:

"Change outfit to [NAME] outfit"
```

[[Identity Preservation]] [[AI Workflow]]

---

### 139. 基于参考图像的逼真自画像绘制

**Author**: [D. Humann](https://x.com/dhumann)  **Date**: 2026-02-03  **Language**: en

> 一个高度具体的提示模板，用于生成一张超逼真的编辑类生活方式照片，内容是拍摄对象在 iPad 上绘制自画像。至关重要的是，此提示需要两张参考图像：一张用于确保拍摄对象身份的准确性，另一张用于 iPad 屏幕上显示的图像。

![基于参考图像的逼真自画像绘制](https://cms-assets.youmind.com/media/1770187126243_0k7eg3_HANNo-KXwAA1Kyd.jpg)

```
Ultra-photorealistic editorial lifestyle photograph shot on a full-frame DSLR with an 85mm f/1.8 lens. Natural indoor daylight from the left. THE_SUBJECT (from attached reference) must be replicated with 100% identity fidelity, exact facial structure, skin tone, proportions, and natural texture.

THE_SUBJECT is seated on a couch, angled slightly toward camera, holding a large 12.9-inch iPad Pro vertically and showing the screen directly to the viewer. In the other hand, THE_SUBJECT holds an Apple Pencil naturally, as if paused mid-drawing.

Insert THE_SCREEN (attached reference image) exactly onto the iPad display with correct proportions and perspective. The screen should appear realistically illuminated with subtle glass reflections and edge glare. Both face and iPad screen in sharp focus. No stylization, no illustration effect; it must look like a real professional photograph.
```

[[Identity Preservation]] [[Reference Image Technique]]

---

### 140. 照片转皮克斯 3D 动画肖像转换

**Author**: [Abhi](https://x.com/Abhiew_)  **Date**: 2026-01-30  **Language**: en

> 一个旨在将上传的人物照片转换为活泼可爱的皮克斯 (Pixar) 风格 3D 动画肖像的提示。它强调保留人物原始的面部特征、发型和表情，以保持身份识别度，同时采用平滑、干净的卡通风格，配以柔和的阴影和富有表现力的眼睛，背景为纯白色影棚。

![照片转皮克斯 3D 动画肖像转换](https://cms-assets.youmind.com/media/1769841115703_diu999_G_5iY5waIAEiklv.jpg)
![照片转皮克斯 3D 动画肖像转换](https://cms-assets.youmind.com/media/1769841115746_62wkgc_G_5iY5rbUAIajH8.jpg)

```
Convert the uploaded photo into a cheerful and cute 3D Pixar-style animated portrait. Keep the person’s facial features, hairstyle, and unique expression so the character clearly resembles the real person. Use a smooth and clean cartoon style. Apply soft skin shading, expressive eyes, and a polished animated look while preserving the original identity. Place the character against a plain white studio background with clean, even lighting. Keep the outfit the same as in the reference
```

[[Identity Preservation]] [[Pixar Style]] [[White Studio Background]] [[Expressive Eyes]]

---

### 141. iPhone 逼真大头贴拼贴画（2x2 网格）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 一个高度具体的提示，要求生成一个 2x2 的无缝大头贴拼贴画，其中包含两个主体（参考 Sydney Sweeney 和 Ana de Armas）。它要求精确保留身份，使用特定的大头贴灯光（明亮的自然白闪光），以及超广角镜头畸变，以营造业余美感。

![iPhone 逼真大头贴拼贴画（2x2 网格）](https://cms-assets.youmind.com/media/1769581980613_doboft_G_re2rFXEAAFfmc.jpg)

```
{
  "task": "Create an iPhone-realistic photobooth collage (4 photos in a 2x2 grid)",
  "subjects": [
    {
      "id": "Subject 1",
      "description": "EXACTLY from the Reference Image (same face, hairstyle, skin tone, body proportions, overall look).",
      "outfit": "EXACTLY the same as in the Reference Image. Do not change clothing, glasses, or accessories."
    },
    {
      "id": "Subject 2",
      "description": "EXACTLY from the Reference Image (same face, hairstyle, skin tone, body proportions, overall look).",
      "outfit": "EXACTLY the same as in the Reference Image. Do not change clothing, glasses, or accessories."
    }
  ],
  "scene": {
    "location": "Inside a small BOX photo booth",
    "background": "Matte {argument name="background color" default="blue"} walls and blue floor, tight enclosed corner, clean minimal environment",
    "camera_look": "Ultra wide / slight fisheye lens look with subtle perspective distortion typical of photobox cameras. iPhone 17 Pro, photobooth wide-angle.",
    "lighting": "Bright neutral-white flash lighting, evenly illuminating faces, soft shadow falloff on blue walls, crisp detail, realistic skin texture. Direct neutral white flash (no yellow / no warm tone).",
    "aesthetic": "4K, amateur photobooth aesthetic, high contrast but still natural, no cinematic grading, no heavy beauty filter, no blur, no text, no watermark."
  },
  "layout": {
    "type": "2x2 grid collage",
    "aspect_ratio": "9:16 (vertical collage)",
    "style": "Clean, with NO white borders, NO frame lines, NO gaps, and NO outlines between photos (seamless collage). Each frame fills its quadrant edge-to-edge."
  },
  "frames": [
    {
      "position": "top-left",
      "content": "Subject 1 leans diagonally toward the camera from the front-left, one arm stretched down, playful serious face; Subject 2 stands behind in the center, arms raised and flexing like “strongman”, smiling."
    },
    {
      "position": "top-right",
      "content": "Subject 2 leans forward toward the camera, hands on knees, curious expression; Subject 1 enters from the right side very close to camera, tilting her head, one arm arched above her head like a half-heart pose, soft smile."
    },
    {
      "position": "bottom-left",
      "content": "Piggyback pose — Subject 1 on Subject 2’s back, arms wrapped around shoulders; both laughing big, faces close to camera, dynamic motion vibe."
    },
    {
      "position": "bottom-right",
      "content": "Subject 2 bends sideways/leans forward with a goofy face; Subject 1 stands behind making playful “claw/horns” hand gestures above Subject 2’s head, slightly pouting for fun."
    }
  ]
}
```

[[Identity Preservation]] [[Wide Angle Distortion]] [[Sydney Sweeney Reference]] [[2x2 Photo Grid]]

---

### 142. 都市夜景人像，100% 面部精准度

**Author**: [Javed Khan](https://x.com/javedkhan019)  **Date**: 2026-01-27  **Language**: en

> 一个详细的 JSON 提示，用于生成具有高冲击力的电影级都市夜景肖像。它明确要求 100% 面部准确度与参考图像匹配，重点突出街头风格、湿沥青上的强烈反光以及电影级的色彩分级。

![都市夜景人像，100% 面部精准度](https://cms-assets.youmind.com/media/1769581924904_rm0lir_G_p4t5LbAAAaaXm.jpg)

```
{
  "image_type": "Urban Night Portrait",
  "prompt": "High-impact cinematic depiction that matches the reference image with 100% facial accuracy. Featuring a young woman with long, wavy brown hair and a gentle smile. She is dressed in an oversized orange graphic t-shirt, a distressed denim mini-skirt, and clean white sneakers, complemented by a small brown crossbody bag. The subject is leaning casually against a metal pole on a wet urban street at night. The environment emphasizes a relaxed, modern city atmosphere with dramatic street lighting, neon accents, and strong reflections on the wet asphalt. Captured using a high-quality portrait lens with shallow depth of field, cinematic framing, and blurred city lights creating soft bokeh in the background. Ultra-detailed textures, realistic skin tones, professional cinematic color grading, sharp focus, HDR, ultra-high resolution 4K, masterpiece quality.",
  "style_tags": [
    "cinematic",
    "night photography",
    "urban portrait",
    "shallow depth of field",
    "bokeh",
    "street style",
    "HDR",
    "professional",
    "wet street reflections"
  ],
  "negative_prompt": [
    "low quality",
    "blurry",
    "flat lighting",
    "distorted face",
    "bad anatomy",
    "extra limbs",
    "oversharpening",
    "text",
    "watermark",
    "logo",
    "daylight"
  ]
}
```

[[Identity Preservation]] [[Night Portrait]] [[Cinematic Color Grade]]

---

### 143. 超逼真的户外肖像，具有严格的身份锁定

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 生成一张超现实照片的提示，照片内容为一名年轻女子在户外，置身于现代泳池旁的木质甲板上。提示严格要求 100% 保留上传参考照片中主体的面部特征和身体比例，重点营造一种自然、不经意的时尚感和宁静的氛围，并采用柔和的自然日光。

![超逼真的户外肖像，具有严格的身份锁定](https://cms-assets.youmind.com/media/1769581991395_8tjdcy_G_pngjabUAA0g_f.jpg)
![超逼真的户外肖像，具有严格的身份锁定](https://cms-assets.youmind.com/media/1769581991367_zhu09n_G_pngiAbAAAgVTH.jpg)

```
{
  "image_generation_prompt": {
    "style": "Hyper-realistic photograph",
    "subject": {
      "demographic": "Young woman",
      "pose": {
        "angle": "Slightly rear three-quarter angle",
        "posture": "Gracefully turning upper body and head toward camera, natural S-curve",
        "arms": "One arm raised gently holding hair, other arm resting naturally by side",
        "vibe": "Candid, effortless"
      },
      "face_and_identity": {
        "constraint": "Use uploaded photo as exact and only reference",
        "preservation": "100% facial structure, bone proportions, eyes, nose, lips, skin texture, natural asymmetry",
        "prohibitions": "No alterations, filters, or stylization",
        "expression": "Calm, subtly confident, slightly curious"
      },
      "hair": "Dark, straight, silky, tied in mid-height ponytail with loose front strands framing face",
      "outfit": {
        "top": "Fitted white backless crop top with short sleeves",
        "bottom": "Loose-fitting black pants sitting comfortably at the waist",
        "contrast": "Clean black-and-white"
      }
    },
    "environment": {
      "location": "Outdoors on a wooden deck beside a modern landscaped swimming pool",
      "elements": [
        "Lush green plants",
        "Small trees",
        "Calm reflective water",
        "Contemporary buildings faintly visible in distance"
      ]
    },
    "technical_details": {
      "lighting": "Natural soft daylight (late afternoon), even illumination, gentle highlights on cheekbones/shoulders/back, soft diffused light, no harsh shadows",
      "colors": "Fresh natural palette, greens, soft blues, warm wood tones, neutral clothing",
      "mood": "Serene, stylish, lifestyle-oriented, peaceful, effortlessly fashionable",
      "focus": "Natural anatomy, realistic skin texture, subtle highlights/reflections, photographic depth-of-field (editorial feel)"
    },
    "full_prompt_text": "A hyper-realistic photograph of a young woman standing outdoors on a wooden deck beside a modern landscaped swimming pool. Lush green plants, small trees, and calm reflective water surround her, with contemporary buildings faintly visible in the distance. She is captured from a slightly rear three-quarter angle, gracefully turning her upper body and head toward the camera, forming a natural S-curve in her posture. One arm is raised above her head, gently holding her hair, while the other arm rests naturally by her side, giving a candid, effortless feel. Face & Identity: Use the uploaded photo as the exact and only reference. Preserve the face 100%: facial structure, bone proportions, eyes, nose, lips, skin texture, and natural asymmetry. No alterations, filters, or stylization. Expression must remain calm, subtly confident, and slightly curious. Hair & Outfit: Dark, straight, silky hair tied in a mid-height ponytail, with loose front strands framing her face. She wear"
  }
}
```

[[Identity Preservation]] [[Lifestyle Photography]] [[Soft Natural Daylight]] [[Casual Fashion]]

---

### 144. 迪拜电影感生活肖像摄影，带焦外虚化效果

**Author**: [Javed Khan](https://x.com/javedkhan019)  **Date**: 2026-01-27  **Language**: en

> 一个用于生成具有高冲击力电影级生活方式肖像的 JSON 提示。它要求 100% 匹配参考图像，图像中一位身穿毛衣和牛仔裤的女士站在迪拜哈利法塔前。该提示强调浅景深、85mm 镜头特性和专业的电影级色彩分级。

![迪拜电影感生活肖像摄影，带焦外虚化效果](https://cms-assets.youmind.com/media/1769495346773_64jlcw_G_pf0KZXUAAMXdc.jpg)

```
{
  "image_type": "Lifestyle Portrait",
  "prompt": "High-impact cinematic depiction that matches the reference image 100%. Featuring a beautiful young woman with long, voluminous wavy brown hair, glowing natural skin, and a cheerful smiling expression while looking off-camera to the side. She is dressed in a cozy oversized {argument name="sweater color" default="maroon"} crew-neck knitted sweater, fitted black skinny jeans, and black athletic sneakers with white soles. The subject is positioned in front of the Dubai Burj Tower, in a scenic outdoor hilltop setting. The background is heavily blurred, showing a distant mountain town, trees, and soft sunlight. She is standing on a gravel path with one hand casually placed in her pocket. The scene conveys a relaxed, joyful, and serene mood through soft natural daylight, with subtle rim lighting highlighting her hair and cinematic highlights and shadows. Captured using a high-quality 85mm portrait lens with shallow depth of field and smooth bokeh, cinematic framing, ultra-detailed textures (sweater fabric, denim), realistic skin tones, professional cinematic color grading, sharp focus, HDR, ultra-high resolution 4K, masterpiece quality.",
  "style_tags": [
    "lifestyle photography",
    "cinematic",
    "ultra-detailed",
    "4K",
    "natural lighting",
    "shallow depth of field",
    "HDR",
    "professional",
    "outdoor portrait",
    "telephoto lens",
    "bokeh",
    "casual fashion"
  ],
  "negative_prompt": [
    "low quality",
    "blurry",
    "flat lighting",
    "distorted face",
    "bad anatomy",
    "extra limbs",
    "oversharpening",
    "text",
    "watermark",
    "logo",
    "cartoon",
    "illustration",
    "3d render",
    "noise",
    "grain"
  ]
}
```

[[Identity Preservation]] [[Shallow Depth Of Field]] [[85mm Lens Portrait]] [[Cinematic Color Grade]]

---

### 145. 具有身份锁定的逼真水疗生活方式肖像

**Author**: [Hamid Siddiqui](https://x.com/hamidInventions)  **Date**: 2026-01-27  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张主体在水疗按摩椅上放松的超逼真生活方式肖像。该提示强制严格保留参考照片中的身份，并指定柔和、漫射的晨光、现代水疗美学以及模拟高质量智能手机照片的技术细节。

![具有身份锁定的逼真水疗生活方式肖像](https://cms-assets.youmind.com/media/1769581989328_va7s6h_G_pbRapaQAALAIX.jpg)

```
{
  "intent": "Generate a photorealistic, soft morning spa-lifestyle portrait of the subject relaxing and recharging.",
  "reference_usage": {
    "preserve_face": true,
    "preserve_body": true,
    "notes": "Match the subject’s facial structure, skin tone, and overall appearance exactly to the provided profile photo."
  },
  "frame": {
    "aspect_ratio": "4:5",
    "composition": "medium-full body shot from knees up, slightly angled from the foot of the massage chair toward the upper body",
    "perspective": "friend-taken candid spa photo composition, as if a spa staff or companion captured a natural moment",
    "crop": "subject centered, massage chair and spa environment framing the scene, edges softly blurred"
  },
  "style": {
    "primary": "ultra-photorealistic contemporary lifestyle photography",
    "lighting": "early-morning natural light filtered through sheer curtains, soft and diffused with cool-neutral spa tones",
    "mood": "calm, relaxed, restful, self-care morning ritual",
    "technical": {
      "camera_type": "modern smartphone rear camera look",
      "lens_look": "28–35mm natural portrait perspective",
      "depth_of_field": "shallow; crisp focus on face and upper body, background gently blurred",
      "imperfections": "very subtle noise, natural skin texture, realistic handheld framing, no over-retouching"
    },
    "materials": {
      "skin": "natural complexion with realistic texture and gentle highlights from diffused light",
      "hair": "slightly damp, loosely brushed back or falling naturally around shoulders, soft moisture sheen",
      "clothing": "crisp white sports bra and white shorts, soft stretch fabric, clean lines, natural folds and creases from reclining",
      "environment_surfaces": "modern leather or faux-leather full-body massage chair, light wood floors, matte walls, soft textiles like rolled towels"
    }
  },
  "subject": {
    "identity": {
      "face": {
        "preserve_original": true
      },
      "body": {
        "preserve_original": true
      }
    },
    "pose": {
      "overall_position": "reclined in a modern full-body massage chair in a spa relaxation room",
      "legs": "relaxed in the extended leg section of the chair, slightly apart in a natural, modest position",
      "upper_body": "torso comfortably angled back, shoulders dropped and relaxed into the chair",
      "arms": {
        "right_arm": "resting on the chair armrest, hand relaxed and open",
        "left_arm": "resting lightly across the stomach or on the other armrest, fingers naturally curved"
      },
      "head_and_neck": {
        "tilt": "very slight tilt toward one side, nestled into the headrest",
        "rotation": "facing generally toward the camera",
        "chin": "slightly down for a gentle, serene look"
      }
    },
    "expression": {
      "overall": "peaceful, subtly content, hint of a soft smile",
      "eyes": {
        "
      }
    }
  }
}
```

[[Identity Preservation]] [[Lifestyle Photography]] [[Morning Light]]

---

### 146. 原始高保真镜面自拍模拟

**Author**: [Dan Reed](https://x.com/daaaaanc)  **Date**: 2026-01-27  **Language**: en

> 一个高度技术性的提示，模拟使用 iPhone 17 Pro 传感器拍摄的原始、高保真镜面自拍，要求从前景到背景都具有锐利的焦点，精确的身份保留，以及不对称技术针织紧身连衣裙上逼真的纺织物理效果。

![原始高保真镜面自拍模拟](https://cms-assets.youmind.com/media/1769581962637_8ugv4b_G_o-6LVWsAA_bYg.jpg)

```
[Header] (9:16)
Raw high-fidelity photograph, iPhone 17 Pro sensor simulation, indoor ambient lighting, zero bokeh, SHARP focus from subject to background appliances, f/5.6 aperture for maximum structural clarity, subtle digital grain.
[Subject & Identity Locking]

Identity: Absolute preservation of Image A’s facial geometry (pixel-accurate chin shape and eye-spacing).
Hair Physics: Ultra-long layered straight hair with a high-gloss deep espresso finish. The hair must drape naturally over the shoulders and extend down the back, maintaining the strand-level detail and texture from Image A.
Bio-Fidelity: Detailed skin physics (visible micro-pores, satin-finish hydration). Clear rendering of the proximal limb geometry and upper-torso symmetry, emphasizing a realistic athletic-to-lean transition.
Expression: Mirror-selfie aesthetic; the face is partially obscured by the technical device to maintain the authentic composition of Image B.
[Outfit & Physicality]

Technical Description: High-impact {argument name="dress color" default="burgundy"} technical-knit bodycon mini-dress.
Textile Geometry: Asymmetrical neckline architecture. The left side features an off-the-shoulder drop-sleeve design, while the right side transitions into a full-length compression-fit sleeve.
Surface Physics: High-tensile material-to-skin surface compression. The prompt must specify the "micro-ribbed knit texture" to ensure the fabric interacts realistically with the body’s S-curve silhouette.
Physicality: Confident self-assured posture. The torso is angled to highlight the waist-to-hip ratio, with physical tension lines visible where the fabric stretches over the gluteal proportions and hips.
[Pose & Composition]

Geometry: Mirror-reflection framing. The subject is leaning with the left arm against a neutral-toned vertical surface, creating a "torsion" effect in the midsection.
Framing: Full-body vertical orientation. The right hand holds a smartphone with a "blue butterfly graphic" protective case, held at eye level.
Interaction: Precise material interaction between the leaning arm and the wall, showing realistic shoulder-joint displacement.
[Environment & Lighting]

Atmosphere: Domestic interior setting (hallway/kitchen transition).
Lighting: Soft, diffused indoor lighting. Light sources are positioned to cast natural shadows along the right side of the subject, emphasizing the anatomical bust volume and garment texture.
Background Integrity: High-detail domestic background. To the left, a white wall with electrical cabling; in the background, professional-grade built-in kitchen ovens and neutral cabinetry. Background elements must remain sharp and non-distorted.
[Failure Prevention Rule]

Command: Use "Asymmetrical technical-knit bodice" to prevent the AI from defaulting to a standard symmetrical long-sleeve dress.
Constraint: Explicitly require "Zero blurring of the kitchen appliances" and "Perfect grid-alignment of the floor and wall seams" to ensure backgr
```

[[Identity Preservation]] [[Smartphone Photography Simulation]]

---

### 147. 电影级冬季照片拍摄序列（3 帧）

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-27  **Language**: en

> 一个用于生成垂直电影感照片序列的提示，包含三张照片，描绘了一个男人在蓝色时段的冬季城市公园中。该提示要求严格遵循参考图像中人物的面部特征，并详细描述了三个不同的画面：在长凳上阅读、闭着眼睛的侧面特写，以及一个特写表情，所有这些都强调了照片的真实感、雪的物理效果和电影般的灯光。

![电影级冬季照片拍摄序列（3 帧）](https://cms-assets.youmind.com/media/1769581986148_et7q6w_G_o1CiMXoAA6Dys.jpg)

```
Vertical cinematic photo session, 9:16 format.
Use the face and appearance of the person from the attached image without modification. To preserve individual facial features, proportions, skin texture and natural facial expressions as much as possible. Create a photorealistic sequence of three shots, all shot in the same style, like a professional winter photo shoot. Scene: A winter city park in the evening, during blue hour. Snow-covered trees surround, snow gently falling, warm streetlights in the background, bokeh. 
Frame 1: A man sits on a wooden bench, wrapped in a warm coat and scarf, reading a book. Snow slowly settles on hair and clothes. The depth of field is medium, creating an atmosphere of calm and comfort.
Frame 2: Profile portrait, camera closer. Small snowflakes are visible in the air, realistic texture of hair, skin, fabric.
The background is softly blurred, the light from the lanterns creates warm spots of light.
The man leans back on the bench, eyes closed, a slight expression of peace.
Frame 3: Closed left-handed expression. Breathing is slightly noticeable in the cold air. Snow continues to fall, a feeling of peace and quiet.
Photorealism, natural color correction, cinematic lighting, shallow depth of field, realistic light and snow physics.
```

[[Identity Preservation]] [[Cinematic Lighting]] [[Blue Hour Photography]]

---

### 148. 超逼真电影级六格拼贴画，带数字摄像机 UI

**Author**: [松果先森](https://x.com/songguoxiansen)  **Date**: 2026-01-27  **Language**: zh

> 为 Nano Banana Pro 生成超逼真、电影感的六格拼贴（网格）肖像的详细提示（需要参考图像）。拼贴画必须保持拍摄对象精确的面部特征，并呈现 Z 世代的未来主义美学，叠加复古数码摄像机/VHS 界面，包括电池图标、REC 文字和每个画面的独特时间码。

![超逼真电影级六格拼贴画，带数字摄像机 UI](https://cms-assets.youmind.com/media/1769582016032_vzz6u1_G_oasX4akAAW9av.jpg)

```
一幅电影感拼贴，由六幅特写和中景肖像组成，描绘同一位[{argument name="人物描述" default="参考图中的特定人物，保持面部特征、五官构造及神态与参考图100%完全一致"}]，佩戴粉色圆镜片太阳镜与珍珠耳环，整体呈现Z世代未来美学，梦幻空灵且带轻微晃动模糊。每帧设计为数码摄像机录制界面，叠加电池图标、红色“REC”字样、白色计时器（00:02:17、00:00:47、00:00:49、00:01:02、00:00:37、00:00:22）及分钟计数（203min–206min）。六帧中模特姿势与表情各异：眼部极特写、紧致面部肖像、正面中景肖像。采用干净影棚布光，中性浅灰背景带柔和阴影。时尚大片摄影美学，复古数码摄像机/VHS界面，超写实电影质感，模特极度锐利对焦，同时保持梦幻超现实氛围。禁止重复帧：每帧姿势、表情、机位皆唯一，每帧计时数值不同。
```

[[Identity Preservation]]

---

### 149. 身着绷带礼服的南亚女性高级定制肖像

**Author**: [The Prompt Engineer](https://x.com/rorschachvibes)  **Date**: 2026-01-26  **Language**: en

> 一个高度具体的提示，用于生成一张自信的南亚女性的超现实 8K 特写时尚照片。它要求根据参考图像实现 100% 的面部准确度，并详细描述了一件奢华的裸粉色绷带礼服，配有戏剧性的薄纱泡泡袖和精致的珠宝，通过精细的影棚灯光呈现。

![身着绷带礼服的南亚女性高级定制肖像](https://cms-assets.youmind.com/media/1769495394363_c9w099_G_oDYaBbQAArDNu.jpg)

```
Create a 4:5 8K ultra-realistic HD close-up photograph of a confident South Asian woman using the uploaded reference image as the only identity source. Her face must match the original with 100% accuracy, with no editing, beautification, or alteration of facial features, proportions, skin texture, or expression. She is wearing a luxurious off-the-shoulder nude pink bandage gown with a structured corset bodice made from gathered and pleated nude pink fabric, creating rich texture and an elegant deep neckline. The sleeves are dramatic, thick sheer nude pink tulle puff sleeves that add volume and couture presence. She wears a large wide-brim nude pink hat crafted from matching sheer fabric with delicate lace edges, framing her face with a regal silhouette. Accessories include intricate dangling purple chandelier earrings accented with pale green or mint gemstones for subtle contrast. Lighting is soft, refined studio lighting that enhances realistic skin texture, fabric depth, and color richness without cinematic exaggeration. The image must appear as a real high-end fashion photograph, ultra-sharp, photorealistic, editorial quality, with natural shadows, true-to-life tones, and flawless realism.
```

[[Identity Preservation]] [[Studio Lighting]] [[High Fashion Editorial]]

---

### 150. 超现实反乌托邦概念肖像提示词（面部锁定）

**Author**: [The Prompt Engineer](https://x.com/rorschachvibes)  **Date**: 2026-01-26  **Language**: en

> 一个用于生成超现实、情绪化概念肖像的提示，使用上传的面部作为严格的身份参考。主体被一束头顶聚光灯孤立，周围是一群穿着黑色正装和白色布质头罩的匿名人物，营造出幽闭恐惧感，象征着强制的沉默和反乌托邦式的顺从。画面采用强烈的明暗对比照明和 35mm 胶片美学呈现。

![超现实反乌托邦概念肖像提示词（面部锁定）](https://cms-assets.youmind.com/media/1769495378347_e7bu4d_G_nhMfRbMAAA8Zr.jpg)

```
Create a 4:5 surreal, moody conceptual portrait using the uploaded face as the exact identity reference, preserving all facial features. The subject is centered, shot from a slightly elevated medium angle, surrounded by a dense, claustrophobic crowd of anonymous figures. The surrounding figures wear deep black formal clothing and have their heads fully covered in tight white fabric hoods with heavy stitched seams where mouths should be, symbolizing enforced silence and dystopian conformity. Use harsh chiaroscuro lighting with a single overhead spotlight isolating the central subject, making natural skin tones stand out against the monochrome crowd. Add cinematic haze to enhance isolation and tension. Ultra-realistic textures, haunting atmosphere, high contrast, shot on 35mm film, 8K resolution, evocative and unsettling, no change to identity.
```

[[Identity Preservation]] [[35mm Film Aesthetic]] [[Conceptual Portrait]]

---

### 151. 低调奢华酒吧人像特写，带面部锁定功能

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-26  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成电影感十足的低调奢华酒吧肖像。它要求严格遵循参考图像的姿势、构图和面部特征（包括保留痣/雀斑/疤痕），描绘一位身穿深酒红色镂空紧身连衣裙的女性，置身于昏暗高档的酒吧环境中。

![低调奢华酒吧人像特写，带面部锁定功能](https://cms-assets.youmind.com/media/1769495356588_94sytu_G_ne7LzXwAAwq_u.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_luxury_bar_night_editorial_portrait",
      "version": "v1.0_DARK_BAR_RED_CUTOUT_DRESS_LOWKEY_35MM_FACELOCK_EN",
      "priority": "highest",
      "language": "en"
    },

    "references": {
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "POSE_COMPOSITION_LIGHTING_ANCHOR",
        "strict_lock": true,
        "preserve_pose": true,
        "preserve_composition": true,
        "preserve_vibe": true,
        "preserve_background": true
      },
      "reference_image_face": {
        "source": "UPLOAD_REFERENCE_IMAGE (OPTIONAL)",
        "purpose": "FACE_IDENTITY_LOCK",
        "strict_lock": true,
        "face_similarity_priority": "MAX",
        "no_identity_blending": true,
        "no_beautify": true,
        "no_age_shift": true,
        "preserve_skin_texture": true,
        "preserve_facial_proportions": true,
        "preserve_moles_freckles_scars": true,
        "preserve_eye_shape": true,
        "preserve_nose_shape": true,
        "preserve_lip_shape": true,
        "preserve_jawline": true
      }
    },

    "global_constraints": {
      "rating": "PG-13",
      "no_nudity": true,
      "no_explicit_sexual_content": true,
      "no_logos": true,
      "no_watermark": true,
      "no_readable_text": true
    },

    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "cinematic_photoreal_film_still",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "color_grade": "low_key_warm_amber_highlights_deep_blacks",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },

    "creative_prompt": {
      "scene_summary": "Create a photoreal, low-key luxury bar night portrait inspired by the provided reference image. Location: dark upscale bar with black ceiling, small recessed spotlights, deep shadows, and a glossy black marble bar counter with subtle white veining. Background should fall into soft darkness with a hint of bar seating and table settings, but no readable details.\n\nSubject: one adult woman (same identity if face reference is provided) standing near the marble bar. Pose matches reference: torso angled slightly, one hand lifted behind her head touching her hair, the other arm relaxed by her side. Expression confident and cinematic, looking slightly off-camera.\n\nWardrobe: a deep {argument name="dress color" default="wine-red"} bodycon evening dress with tasteful cutouts at the waist/torso (two cutout windows), connected with small gold ring hardware at the center. Dress is fitted and elegant, PG-13, no nudity.\n\nBeauty: glossy neutral lips, soft glam makeup with warm highlights on cheekbones, luminous but natural skin texture. Long dark hair styled in voluminous waves.\n\nLighting: low-
```

[[Identity Preservation]]

---

### 152. 赛博朋克不夜城三联画肖像

**Author**: [Sanchit | AI Tools & News](https://x.com/AIwithSanchit)  **Date**: 2026-01-26  **Language**: en

> 生成一张电影级写实三联画（一张图片中包含三个画面）的提示词，描绘一个人在夜间城市背景下的场景，重点突出都市浪漫、动感和青春，使用特定的相机设置，并需要上传一张照片作为身份参考。

![赛博朋克不夜城三联画肖像](https://cms-assets.youmind.com/media/1769495338970_nblzoo_G_m89fIbAAARNXJ.jpg)

```
use the uploaded photo as the exact identity reference. keep the same person, same face, same facial features, same proportions and natural expression, create a photorealistic cinematic triptych portrait (three-frame composition in one image).

scene: night city, bridge over a busy road, moving cars, glowing street lights, evening sky, city skyline in the background. atmosphere: freedom, motion, youth, urban romance, feeling of wind and road. frame 1 (top): wide cinematic shot - the person standing on a bridge above a busy road, slight motion blur from head movement, city lights and cars below, strong urban night mood. frame 2 (middle): medium shot person leaning on the bridge railing, looking up at the sky, relaxed confident pose, cars and headlights glowing behind. frame 3 (bottom): close-up emotional portrait wind in hair, city lights in bokeh behind, thoughtful and dreamy expression. style: real photography, cinematic lifestyle portrait, urban fashion photography. lighting, natural city night lighting, street lamps, car headlights, soft glow on skin. camera: full-frame dslr, 85mm lens look, shallow depth of field. color grading: warm city lights mixed with cool blue night tones, film-style mood. ultra photorealistic, natural skin texture, real candid moment, no illustration, no cgi, no plastic skin, no text, no logos, no watermark.
```

[[Identity Preservation]] [[Cinematic Lighting]] [[Night Portrait]] [[Triptych Layout]]

---

### 153. 赛博朋克不夜城三联画肖像 (副本)

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-26  **Language**: en

> 生成一张照片级电影感三联画（一张图片中包含三个画面）的提示词，描绘一个人在夜间城市背景下的场景，重点突出都市浪漫、动感和青春，使用特定的相机设置，并需要上传一张照片作为身份参考。（这是 2015850075654885547 的重复内容）。

![赛博朋克不夜城三联画肖像 (副本)](https://cms-assets.youmind.com/media/1769495340848_0gfgmh_G_mk5JEaAAAEWxp.jpg)

```
use the uploaded photo as the exact identity reference. keep the same person, same face, same facial features, same proportions and natural expression, create a photorealistic cinematic triptych portrait (three-frame composition in one image).

scene: night city, bridge over a busy road, moving cars, glowing street lights, evening sky, city skyline in the background. atmosphere: freedom, motion, youth, urban romance, feeling of wind and road. frame 1 (top): wide cinematic shot - the person standing on a bridge above a busy road, slight motion blur from head movement, city lights and cars below, strong urban night mood. frame 2 (middle): medium shot person leaning on the bridge railing, looking up at the sky, relaxed confident pose, cars and headlights glowing behind. frame 3 (bottom): close-up emotional portrait wind in hair, city lights in bokeh behind, thoughtful and dreamy expression. style: real photography, cinematic lifestyle portrait, urban fashion photography. lighting, natural city night lighting, street lamps, car headlights, soft glow on skin. camera: full-frame dslr, 85mm lens look, shallow depth of field. color grading: warm city lights mixed with cool blue night tones, film-style mood. ultra photorealistic, natural skin texture, real candid moment, no illustration, no cgi, no plastic skin, no text, no logos, no watermark.
```

[[Identity Preservation]] [[Cinematic Lighting]] [[Urban Night Scene]] [[Triptych Layout]]

---

### 154. SUV 车头盖上的高角度闪光灯照片（夜间）

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-01-26  **Language**: en

> 生成一张高对比度、高角度照片的提示，使用直射闪光灯，显示一个人在夜晚靠在一辆特定 SUV 车型（北汽 BJ40）的黑色引擎盖上，抬头看向镜头。需要提供身份参考图像。

![SUV 车头盖上的高角度闪光灯照片（夜间）](https://cms-assets.youmind.com/media/1769495329147_bd8q83_G_mVnatb0AAERcy.jpg)
![SUV 车头盖上的高角度闪光灯照片（夜间）](https://cms-assets.youmind.com/media/1769495329148_zc3bh3_G_mVnZEboAEnjBh.jpg)

```
{
"action": "image_generation",
"action_input": "High-angle overhead flash photography of an individual with the exact facial features and hair of the person in the reference image, leaning back against the black hood of a {argument name="SUV model" default="BAIC BJ40 SUV"} at night. wearing outfit as reference. She is looking directly up into the camera lens. Harsh direct flash lighting creating high contrast, deep shadows on the wet asphalt ground, and bright reflections"
```

[[Identity Preservation]] [[High Contrast]] [[Hard Flash Photography]]

---

### 155. 锁定面部身份的三帧抓拍肖像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-26  **Language**: en

> 一个高度具体的提示，用于生成一张垂直图像，该图像被分割成三个堆叠的画幅，模拟一系列抓拍的智能手机照片。至关重要的是，它要求上传的参考照片作为唯一的面部识别源，该面部识别源必须在所有三个画幅中 100% 锁定，显示在夜间海滩环境中细微的动作变化。

![锁定面部身份的三帧抓拍肖像](https://cms-assets.youmind.com/media/1769495355323_f07emf_G_mI9xOa4AAqE4z.jpg)

```
Use the uploaded reference photo as the single and exclusive facial identity source.
The same exact face must appear in ALL three frames with no variation.
Do not reinterpret, regenerate, beautify, or modify the face between frames.
Facial identity has highest priority over lighting, angle, blur, or realism.
Ultra-realistic vertical image split equally into three stacked frames (top / middle / bottom) within one single photo. All frames show the same person with the same face, same outfit, same location, captured seconds apart like a burst of candid smartphone shots. Only subtle movement changes. Feels accidental, real, and human.
Location & background:
Open beach night at a modern resort outdoors at night. Wooden tent in background, Warm lights glowing softly near the tent. Dark night sky visible. Beachy atmosphere. Real, moment — not staged.
Outfit (locked):
{argument name="shirt color" default="Lime green"} vertically striped button-down shirt, top buttons open showing slight chest. Full Sleeves rolled to forearms.
High-waisted cream tailored trousers. Metal wristwatch on one wrist. No jacket, no accessories beyond the watch.

Hair & Face (LOCKED)
Medium-length, thick, naturally wavy hair Slightly messy, lived-in texture
Light stubble / short beard
Real skin texture, visible pores
No smoothing, no beautification
FRAME BREAKDOWN (VERY IMPORTANT)
TOP FRAME — BACK SHOT
Back view of the subject.
He is touching the back of his hair near the neck, fingers slightly tangled in hair.
Head tilted slightly down and to the side.Relaxed posture, candid movement. Hair texture clearlyvisible from behind.
MIDDLE FRAME — CLOSE-UP
Tight close-up near the eyes and upper face.Messy strands of hair falling naturally near the eyes.
Eyes partially visible, soft focus.
Very slight motion softness from movement. Feels intimate, accidental, not posed.
BOTTOM FRAME — MID SHOT
Mid-shot from waist or chest up.
Subject leaning casually against the railing. Looking sideways, not at the camera.Expression calm, confident, contemplative.
Natural posture, effortless presence.
Lighting (LOCKED)
Warm artificial wall lighting mixed with cool night ambient light.
Soft illumination on face and shirt.
Background slightly darker.
No flash. No dramatic contrast.
Camera Feel (LOCKED)
Handheld smartphone photo
No portrait mode
No background blur.
```

[[Identity Preservation]] [[Smartphone Photography Simulation]]

---

### 156. 超真实影棚肖像海报艺术生成器提示词

**Author**: [Saman | AI](https://x.com/Samann_ai)  **Date**: 2026-01-26  **Language**: en

> 一个复杂的 JSON 提示模板，旨在生成一张超写实的影棚人像照片（使用上传的人脸参考），照片中人物身着燕尾服，周围环绕着与特定主题（例如“金融”或“游戏”）相关的物品，营造出海报艺术美感。

![超真实影棚肖像海报艺术生成器提示词](https://cms-assets.youmind.com/media/1769495402969_g35tnj_G_l-QuqWkAAytg5.jpg)

```
{
  "task": "Generate a hyper-real studio photograph that matches the composition of the reference image: a centered adult person in a tuxedo, surrounded by many hands entering the frame from all sides holding objects toward the person, with a curtain backdrop whose color matches the theme.",
  "variables": {
    "USER_PHOTO": "<<UPLOAD_OR_URL_TO_USER_FACE_OR_PORTRAIT>>",
    "SUBJECT_THEME": "{argument name="subject theme" default="finance"}",
    "HAND_PROPS": [
      "<<PROP_1 RELATED TO SUBJECT_THEME>>",
      "<<PROP_2 RELATED TO SUBJECT_THEME>>",
      "<<PROP_3 RELATED TO SUBJECT_THEME>>",
      "<<PROP_4 RELATED TO SUBJECT_THEME>>",
      "<<PROP_5 RELATED TO SUBJECT_THEME>>",
      "<<PROP_6 RELATED TO SUBJECT_THEME>>",
      "<<PROP_7 RELATED TO SUBJECT_THEME>>",
      "<<PROP_8 RELATED TO SUBJECT_THEME>>"
    ]
  },
  "prompt": "Create an ultra photorealistic studio photo (hyper-real, DSLR look) with the SAME composition and framing as the reference: a centered adult person standing front-facing, waist-up to mid-thigh visible, wearing a dark navy tuxedo jacket, crisp white shirt, and black bow tie, smiling confidently. The person has round eyeglasses and neat facial hair (mustache + short beard), but the FACE must be replaced with the user's likeness from USER_PHOTO while keeping natural skin texture, pores, and realistic facial proportions (no plastic skin, no cartooning). The lighting is clean professional studio lighting with soft shadows, high dynamic range, crisp detail.\n\nSurround the person with 8–10 different hands and forearms entering the frame from the edges (top, left, right, bottom), each holding an object and aiming it toward the center person (close to the face/upper torso). The hands belong to different people (varied sleeves/patterns/colors), but keep them realistic and anatomically correct.\n\nIMPORTANT: The ONLY changing elements across generations are: (1) the user's face from USER_PHOTO, and (2) the objects held in the hands. Everything else stays consistent: the tuxedo pose, camera angle, lens look, and overall composition.\n\nOBJECT RULE: Select HAND_PROPS so they are strongly related to SUBJECT_THEME. The objects must be clearly visible, realistic, and varied (mix of modern and vintage if it fits). Examples by theme:\n- music: studio headphones, microphone, vinyl record, cassette, guitar pick, small synth, metronome\n- gaming: controller, handheld console, gaming headset, mouse, keyboard, VR accessory\n- cooking: chef thermometer, whisk, spice grinder, mini pan, piping bag, recipe card\n- finance: calculator, credit card reader, stock ticker printout, smartphone with finance app, receipt roll\n- fitness: smartwatch, resistance band, shaker bottle, jump rope handle\n\nBACKGROUND: Use a curtain backdrop (like a stage/studio curtain) with a color"
```

[[Identity Preservation]]

---

### 157. Madison Beer 红毯造型复刻提示词

**Author**: [Bethany](https://x.com/JustBethanyai)  **Date**: 2026-01-26  **Language**: en

> 一个全面的 JSON 提示，旨在重现一张高端红毯照片，照片中一位酷似 Madison Beer 的女性身着象牙色垂坠礼服，并严格指示锁定身份并使用上传的参考图像以实现最大保真度。

![Madison Beer 红毯造型复刻提示词](https://cms-assets.youmind.com/media/1769495407567_2siyts_G_kJbQaXoAAOJtw.jpg)
![Madison Beer 红毯造型复刻提示词](https://cms-assets.youmind.com/media/1769495408018_zqdi3b_G_l893bWcAAZChe.jpg)
![Madison Beer 红毯造型复刻提示词](https://cms-assets.youmind.com/media/1769495407758_2774vs_G_l891uWQAABCeJ.jpg)
![Madison Beer 红毯造型复刻提示词](https://cms-assets.youmind.com/media/1769495408926_33m85a_G_kJbQMWYAAcHry.jpg)
![Madison Beer 红毯造型复刻提示词](https://cms-assets.youmind.com/media/1769495408624_xqgcbh_G_kJbQNWYAA8ojR.jpg)
![Madison Beer 红毯造型复刻提示词](https://cms-assets.youmind.com/media/1769495409763_aecs8r_G_kJbQSXsAAMoPd.jpg)

```
{
  "task": "image_generation",
  "mode": "reference_locked_recreation",
  "reference_image": {
    "use_uploaded_image": true,
    "weight": 0.95,
    "lock_identity": true
  },
  "subject": {
    "type": "adult female",
    "appearance": {
      "face": {
        "structure": "oval face, soft jawline, balanced cheekbones",
        "skin_tone": "light to medium warm tone, smooth natural texture",
        "makeup": "red carpet glam makeup, defined brows, neutral eyeshadow, subtle eyeliner, mascara, contoured cheeks, nude glossy lips",
        "expression": "confident, slightly open lips, head turned slightly to the side"
      },
      "hair": {
        "color": "dark brown",
        "style": "long, straight with soft waves at the ends",
        "part": "center part",
        "finish": "smooth, glossy"
      },
      "body": {
        "type": "slim with feminine curves",
        "proportions": "natural, realistic anatomy",
        "posture": "elegant red carpet stance"
      }
    }
  },
  "pose": {
    "description": "standing red carpet pose, body angled slightly sideways, shoulders relaxed, hands gently positioned near the body",
    "balance": "natural weight distribution",
    "anatomy_accuracy": "high"
  },
  "clothing": {
    "dress": {
      "type": "evening gown",
      "color": "{argument name="dress color" default="ivory / off-white"}",
      "material": "soft sheer fabric with gathered draping",
      "fit": "body-hugging with natural fabric tension",
      "details": "off-shoulder neckline, thigh-high slit on one side with jeweled embellishment",
      "realism": "high, realistic folds and gravity"
    },
    "accessories": {
      "jewelry": "minimal, elegant earrings",
      "other": "no additional accessories"
    }
  },
  "environment": {
    "location": "red carpet event",
    "background": {
      "type": "step-and-repeat wall",
      "logos": "iHeartRadio and Capital One logos repeated",
      "color_scheme": "white background with red and blue logos",
      "focus": "slightly out of focus, readable but not sharp"
    },
    "floor": "red carpet"
  },
  "lighting": {
    "type": "professional event lighting",
    "setup": "even frontal lighting with soft shadows",
    "highlights": "natural skin highlights, fabric sheen",
    "color_temperature": "neutral daylight"
  },
  "camera": {
    "camera_type": "professional DSLR or mirrorless",
    "lens": "85mm portrait lens",
    "aperture": "f/2.8",
    "iso": 200,
    "shutter_speed": "1/200",
    "angle": "eye-level",
    "framing": "full body portrait",
    "depth_of_field": "shallow to medium, subject in sharp focus"
  },
  "style": {
    "photography": "high-end red carpet photography",
    "realism": "ultra-realistic",
    "post_processing": "minimal, natural color correction",
    "no_stylization": true
  },
  "quality": {
    "resolution": "high",
    "detail_level": "maximum",
    "texture_accuracy": "high",
    "noise": "low"
  },
  "ne"
```

[[Identity Preservation]] [[Ultra-Realistic Photography]] [[Red Carpet Photography]]

---

### 158. 祖传部落凝视肖像提示（面部锁定）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-26  **Language**: en

> 一个详细的提示，用于生成一张具有部落标记的女性的戏剧性、超现实、特写肖像。构图聚焦于她半张脸和一个引人注目的浅蓝色眼睛，传达出力量和韧性。它需要上传一张女性身份的参考图片，并指定电影般的低调照明、超详细的皮肤纹理和编辑海报风格。

![祖传部落凝视肖像提示（面部锁定）](https://cms-assets.youmind.com/media/1769495369727_v9yvqb_G_l75zca4AADgVb.jpg)
![祖传部落凝视肖像提示（面部锁定）](https://cms-assets.youmind.com/media/1769495369831_dk0phs_G_l75zwbAAEH4DG.jpg)

```
"A dramatic ultra-realistic portrait of a woman shown in extreme close-up, only half of her face visible. Her skin is painted with bold tribal markings in deep red, navy blue, and muted earth tones, layered with rough textures and symbolic patterns. One striking light-blue eye is sharply in focus, conveying strength, resilience, and quiet intensity. She wears weathered fabric and woven textiles around her head, with frayed edges and smallwooden beads, suggesting ancient or nomadic culture. Cinematic lighting with soft shadows, shallow depth of field, dark neutral background, hyper-detailed skin texture, painterly realism, 8K quality, editorial poster style, moody and powerful atmosphere."

Her skin is painted with bold tribal markings in deep red, navy blue, and muted earth tones. The patterns are symbolic and organic, layered with rough, tactile textures that blend naturally into highly detailed skin, achieving a refined painterly realism.

She wears weathered fabric and woven textiles wrapped around her head, featuring frayed edges and small wooden beads. These elements suggest an ancient, nomadic culture and add a sense of history, authenticity, and character.

Use cinematic, low-key lighting with soft shadows to sculpt the face and enhance depth without losing fine detail. Apply a shallow depth of field to isolate the eye against a dark, neutral background, creating a dramatic and intimate atmosphere.

Style the image as a powerful editorial poster — timeless, moody, and emotionally charged. Emphasize hyper-detailed skin texture, natural imperfections, and realistic materials. Render at 8K quality for maximum clarity and visual impact.

**Mood:** Powerful, ancestral, introspective  
**Style:** Ultra-realistic, painterly editorial portrait  
**Lighting:** Cinematic, soft contrast, shallow DOF
```

[[Identity Preservation]] [[Low-Key Cinematic Lighting]]

---

### 159. 2D 壁画到 3D 现实街头艺术提示

**Author**: [Duet | AI](https://x.com/Sheldon056)  **Date**: 2026-01-26  **Language**: en

> 生成一个复杂的街头艺术场景的提示词，其中一幅巨大的超写实壁画（使用上传的面部参考图）从 2D 涂鸦过渡到 3D 立体形象，一个真实人物（用户的身份）站在壁画前，强调比例对比和电影般的真实感。

![2D 壁画到 3D 现实街头艺术提示](https://cms-assets.youmind.com/media/1769495414546_f4f28c_G_l7PsebEAAry0R.jpg)

```
Gaint photorealistic street art mural covering entire wall, subject painted as mural using uploaded face reference, upper body and head breaking from 2D graffiti into 3D reality, seamless 2D-to-3D transition, rebellious smirk, intense eye contact, cinematic realism

painted section wearing colorful spray-paint stained hoodie and cap, dripping paint, vibrant layered tags, bold Indonesian street art style, chaotic color splashes, detailed aerosol strokes

young man using my identity, realistic 3D human, standing in front of the wall, facing viewer, confident stance, casual urban outfit, finger pointing toward exact mural location, interaction between real person and painted self, scale contrast emphasizing massive wall

foreground rusted train tracks, discarded spray cans, concrete debris, weeds between rails, depth and perspective emphasis, sharp focus, high dynamic range, ultra high quality, cinematic composition, award-winning photography, zeiss optics, RAW photo look.
```

[[Identity Preservation]] [[Cinematic Realism]] [[Scale Contrast]]

---

### 160. 超逼真的 G 级越野车冬季时尚人像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-26  **Language**: en

> 一个高度详细、技术性强的提示，用于生成一张超逼真的特写时尚照片：一名男子身穿蓬松的黑色皮草大衣，站在一辆黑色 G 级越野车旁，置身于白雪皑皑的风景中。该提示指定了相机设备（哈苏 H6D-400c），严格遵守参考图像的身份保留，以及模拟手机拍摄的自然光照。

![超逼真的 G 级越野车冬季时尚人像](https://cms-assets.youmind.com/media/1769495391915_6k8bj9_G_lzrWEXMAAqEVL.jpg)
![超逼真的 G 级越野车冬季时尚人像](https://cms-assets.youmind.com/media/1769495392078_d2wo3s_G_lzrTubQAEWeWD.jpg)

```
"Highly detailed close-up photograph, ultra-photorealistic, 8K resolution, shot on a Hasselblad H6D-400c medium format digital camera with a 100mm f/2.8 studio portrait lens. Impeccable sharpness, extreme detail, and cinematic depth of field. He is dressed in black wide-leg trousers and a black t-shirt. He wears a voluminous black fur coat and fashionable sunglasses, with black leather gloves. His hair is black, wet, curly, and reaches his chin. Strictly maintain the appearance from the attached first photo without distortion. The man stands next to a black G-Wagon, striking a stylish pose; one of his hands is slightly raised, while the other holds the edge of the fur coat, creating a confident and fashionable mood. The background is a snow-covered landscape with tall trees, snowflakes gently falling to the ground, adding a touch of romance to the atmosphere. The shot is taken on a mobile device using natural lighting, which highlights the simplicity and elegance of the outfit and the wintry atmosphere around. Focus on facial details, skin texture, as well as the textures of the outfit."

A confident man stands beside a black Mercedes G-Wagon in a snow-covered landscape. Tall trees rise in the background as soft snowflakes fall naturally through the scene, creating a calm, romantic winter atmosphere.

He is dressed entirely in black: wide-leg trousers, a minimal black t-shirt, and a voluminous black fur coat. One hand gently holds the edge of the coat while the other is slightly raised, forming a natural, stylish pose. He wears black leather gloves and modern sunglasses. His hair is black, wet-look, curly, and reaches chin length.

Strictly preserve the facial structure and identity from the reference image with no distortion.  
Emphasize realistic skin texture, fine facial details, and the tactile quality of fabrics—fur, leather, and cotton rendered with extreme realism.

Natural lighting only, as if captured on a mobile device outdoors, softly illuminating the subject while maintaining a cinematic, high-fashion editorial feel.  
Clean composition, shallow depth of field, strong subject separation, and a refined, confident mood.
```

[[Identity Preservation]] [[Hasselblad Camera Aesthetic]] [[Luxury Winter Fashion]]

---

### 161. 超逼真奢华生活方式肖像，带面部锁定功能

**Author**: [gemini_prompts](https://x.com/gemini_prompts)  **Date**: 2026-01-26  **Language**: en

> 一个用于生成超逼真奢华生活方式肖像的综合提示。它强调保留拍摄对象的精确面部特征（不进行任何修改或美化），并详细描述了三种特定的姿势，背景设定在拥有柔和、漫射自然光线的现代奢华室内。

![超逼真奢华生活方式肖像，带面部锁定功能](https://cms-assets.youmind.com/media/1769495344459_od229x_G_laqJNbwAAPQi6.jpg)
![超逼真奢华生活方式肖像，带面部锁定功能](https://cms-assets.youmind.com/media/1769495344384_zrygje_G_laqKAW4AAZdWE.jpg)
![超逼真奢华生活方式肖像，带面部锁定功能](https://cms-assets.youmind.com/media/1769495344568_bfc8hn_G_laqJQaUAEuIBB.jpg)

```
"Without changing my facial features or face. It should look realistic.
Create a highly detailed, photorealistic luxury lifestyle portrait of a young woman in her early to mid-20s with light cool-neutral skin tone and a slim figure with soft curves. Her facial identity is preserved exactly with no alteration. She has a soft heart-oval face shape, large almond-shaped blue eyes with a calm direct gaze, softly arched light-brown brows, a straight petite nose, and medium-full lips closed in a faint natural smile. Natural skin texture is visible with pores and slight asymmetry, no smoothing or beautification.
Her hair is long, dark blonde, center-parted, worn smooth and loose with natural volume at the crown.
She is wearing a deep {argument name="top color" default="chocolate-brown"} asymmetrical satin halter-style top with a gathered twist at the center, draped snugly with a soft silk sheen. The bottom is a beige nude mini skirt made of stretch jersey fabric, body-hugging with ruched sides and drawstring ties. Accessories include large gold hoop earrings, a small brown leather shoulder bag, and clear-strap high heel sandals.

Pose:
1. Kneeling on the floor with both knees tucked under, torso upright and facing the camera. Both arms raised with hands resting in the hair near the crown. Head level with a slight downward tilt, eyes looking directly into the camera.

2. Seated on the floor with legs crossed comfortably. Hands resting loosely on the knees. Spine upright but relaxed. Head tilted slightly to one side. Eyes looking toward the camera with a gentle smile. Expression warm and approachable.

3. Standing with one shoulder and upper back resting against a wall. One knee bent with the foot pressed lightly against the wall. Arms crossed loosely at the forearms. Head turned slightly to the side, eyes gazing off-frame. Expression thoughtful and distant.

The setting is a modern luxury interior with light gray stone tile flooring, floor-to-ceiling windows, dark modern kitchen cabinetry, minimalist furniture, and a white orchid plant in the foreground. Depth of field remains moderate so background elements are clearly readable.
Lighting is soft, diffused natural daylight entering from large windows behind and to the left of the camera, producing very gentle shadows with low contrast.
The camera captures a full-body kneeling portrait using a 50mm lens equivalent, framed from slightly above the head to below the knees, centered composition.
Image quality is ultra-realistic editorial photography with sharp focus on the face and torso, natural unretouched skin texture, neutral modern color grading with warm accents, and no stylization, filters, body reshaping, or background changes."
```

[[Identity Preservation]] [[Soft Diffused Natural Light]]

---

### 162. 西姆拉舒适冬日咖啡馆场景 (重复)

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-26  **Language**: en

> 生成一张舒适的室内照片的提示词：一名女性坐在印度西姆拉一家乡村咖啡馆结霜的窗边。照片重点突出温暖的钨丝灯光与窗外寒冷的蓝色暮光形成对比，并保留参考图像中人物的精确面部特征。

![西姆拉舒适冬日咖啡馆场景 (重复)](https://cms-assets.youmind.com/media/1769495394012_u0ydbu_G_lT0CabUAAAZJN.jpg)
![西姆拉舒适冬日咖啡馆场景 (重复)](https://cms-assets.youmind.com/media/1769495394212_k71ook_G_lTz5YbIAAdM_F.jpg)

```
A cozy indoor shot of the young woman with the sitting by a frost-covered window in a rustic wooden cafe in Shimla. She is wrapped in a traditional patterned Pashmina shawl over a woolen kurta, holding a steaming mug with both hands. She is looking out at pine trees. The indoor lighting is warm tungsten contrasting with the cold blue twilight outside. The mood is relaxed and peaceful, exact same face as the reference image
```

[[Identity Preservation]]

---

### 163. 夕阳下豪华游艇上的超逼真电影感肖像

**Author**: [𝗦𝗮𝗿𝗶𝗺](https://x.com/Sareem48)  **Date**: 2026-01-26  **Language**: en

> 一个关于年轻男子的超现实 4K 电影级肖像的提示，要求 AI 保持上传图像中精确的面部特征。场景设定在日落时分的豪华游艇上，主体穿着时尚的黑色未扣衬衫和白色长裤，强调温暖的电影级灯光和宁静奢华的氛围。

![夕阳下豪华游艇上的超逼真电影感肖像](https://cms-assets.youmind.com/media/1769495315790_g8jz96_G_lFmv2WgAAzrmu.jpg)

```
{
"action": "image_generation",
"action_input": "An ultra-realistic 4K cinematic portrait of the young man from the uploaded image, maintaining his exact facial features, eyes, nose, and expression. He is relaxing casually on a luxury yacht at sunset, leaning back barefoot on a plush yacht seat. He is wearing a stylish black unbuttoned shirt and elegant white trousers, exuding a confident and relaxed vibe. In the background, smooth ocean waves trail as the yacht moves under a soft golden-pink sunset sky. The lighting is warm and cinematic, highlighting sharp details of the scene with a serene and luxurious atmosphere."
}
Ultra-realistic 4K cinematic portrait of a young man (use the exact same facial features from the uploaded image — do not alter eyes, nose, lips, or expressions). He is relaxing casually on a luxury yacht at sunset, leaning back barefoot on the yacht seat. He wears a stylish black unbuttoned shirt with elegant white trousers, exuding a confident and relaxed vibe. Behind him, the ocean waves trail smoothly as the yacht moves, under a soft golden-pink sky glowing with sunset light. The entire scene is filled with luxury and serenity, captured with sharp details, warm cinematic lighting, and a calm yet powerful atmosphere
```

[[Identity Preservation]] [[Warm Cinematic Lighting]]

---

### 164. 电影级动作照片和视频提示（骑摩托车的女人和黑猩猩）

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-01-26  **Language**: en

> 一个双重提示，用于生成一张超逼真的电影感照片，以及一段一名快乐女性高速骑行攀爬摩托车，腰间紧抱一只黑猩猩的视频。该提示详细说明了服装、面部身份锁定（需要参考图像）、黄金时段光线，以及视频的逼真物理效果/运动模糊。

![电影级动作照片和视频提示（骑摩托车的女人和黑猩猩）](https://cms-assets.youmind.com/media/1769495363265_0ffddd_G_ks-7QakAA0Q6R.jpg)

```
Cinematic, ultra-realistic action photograph of a joyful woman riding a {argument name="motorcycle color" default="yellow"} scrambler-style motorcycle at high speed on a dusty rural road, full bike visible. Use the provided face reference image for her facial features and likeness. She is wearing a white motorcycle helmet, {argument name="jacket color" default="red"} Nike jacket, gloves, and blue jeans. Behind her, a chimpanzee clings to her waist, wearing aviator-style tinted goggles, mouth wide open in excitement and joy. 

Video Prompt:
Cinematic ultra-realistic action video. A joyful woman rides a {argument name="motorcycle color" default="yellow"} scrambler-style motorcycle at high speed on a dusty rural road. Full motorcycle visible. Camera tracks from a low side angle, then slightly behind. The woman wears a white motorcycle helmet, {argument name="jacket color" default="red"} Nike jacket, gloves, and blue jeans. Her facial features perfectly match the provided reference image.
A chimpanzee clings to her waist from behind, wearing aviator-style tinted goggles, mouth wide open in excitement, screaming joyfully. Dust and dirt explode beneath the tires in slow motion, particles flying through the air.
Golden-hour lighting, cinematic motion blur, realistic physics, wind blowing jacket fabric, subtle camera shake. Shallow depth of field, dramatic contrast, film-grade color, 4K ultra-realism, action movie style.
```

[[Identity Preservation]] [[Golden Hour Lighting]] [[Humorous Concept]]

---

### 165. 混合媒体动漫与现实客厅场景提示

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-26  **Language**: en

> 一个用于生成超现实、高保真室内镜头的提示，将照片级真实的 3D 元素与 2D 赛璐珞风格的动漫角色（如哆啦 A 梦和龙珠 Z）融合，在一个现代客厅中互动，并使用上传的人脸参考作为人物主体。

![混合媒体动漫与现实客厅场景提示](https://cms-assets.youmind.com/media/1769495399048_6bad2i_G_kepntbMAAc0l9.jpg)
![混合媒体动漫与现实客厅场景提示](https://cms-assets.youmind.com/media/1769495399146_fwpwaw_G_kepoHaQAAaZc4.jpg)

```
A high-fidelity, wide-angle interior shot captures a surreal, mixed-media composition within a modern living room. It features a man resembling the face in the reference photo—using an uploaded face as a reference—wearing a bright yellow hoodie and black pants, sitting centrally on a plush light gray sofa. The scene seamlessly blends photorealistic 3D environments with cel-shaded 2D anime and cartoon characters interacting directly with the physical space.

On the right side of the subject on the sofa, Nobita sits casually waving his hand, while on the left side, Doraemon leans casually on a pillow. Behind the sofa, two framed posters hang on the white wall—one featuring Son Goku and Vegeta, and the other featuring Trunks in a dynamic anime style. In the foreground, Shinchan lies relaxed on a textured gray carpet near a plate of dorayaki, while a chibi version of Son Goku stands triumphantly on a cream-colored knit pouf. On the left side of the room, Vegeta stands tall on a grooved wooden side table in a confident pose, while a miniature version of Trunks is near the wooden coffee table in the center, as if observing the scene with a curious expression.

Soft natural light streams in from the left side through sheer curtains, creating subtle volumetric lighting that accentuates the texture of the blanket, the wood grain of the tiered table, and the leaves of the snake plant in the corner of the room. The entire scene is rendered in 8K resolution with sharp focus, vivid colors, and a dreamy, cinematic, and playful aesthetic blending between the real world and the anime world, with no AI visible.
```

[[Identity Preservation]] [[Modern Living Room]]

---

### 166. 高端时尚黑白社论肖像提示（面部锁定）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-26  **Language**: en

> 一个用于生成高对比度黑白编辑肖像的提示，使用严格的面部参考锁定。主体姿态富有戏剧性，部分遮盖面部，强烈的自然阳光强调轮廓和纹理，模仿佳能 EOS R5 85mm f/1.8 镜头的效果。

![高端时尚黑白社论肖像提示（面部锁定）](https://cms-assets.youmind.com/media/1769495373403_js3xvt_G_kcaTCaUAADWsx.jpg)

```
Use The Uploaded Image Of The Woman As Strict Facial Reference And Physical Features - Keep Her Real Face Exactly As Provided, Without Alterations Or Stylization. Ensure Seamless, Ultra-realistic Integration In The Final Render. Black And White High-fashion Editorial Portrait Of The Uploaded Person, Wearing A Loose White Blouse. She Poses With One Arm Raised, Partially Covering Her Face While Holding Her Hair Up, Creating A Dramatic And Artistic Composition. Her Gaze Is Intense And Captivating, Directly Toward The Camera, Exuding A Strong, Enigmatic Aura.
Background: Minimalist Plain Wall With Sharp Daylight Shadows
Adding Contrast And Depth.
Lighting: Harsh Natural
Sunlight, High-contrast, Emphasizing Facial Contours, Cheekbones, Hair Texture, And Fabric Detail. Pose: Bold And Expressive, Arm Lifted Framing The Face To Emphasize Raw Emotion And High-fashion Editorial Style.
Camera: Eye-level Close-up,
Focusing On Facial Expression, Texture, And Dramatic Shadow Play. Captured As If With Canon Eos R5, 85mm F/1.8 Lens - Crisp Detail, Tonal Depth, Fine Grain.
Style: Monochrome, Ultra-realistic, Cinematic, High-fashion
Editorial Photography.ashion editorial photography.
```

[[Identity Preservation]] [[High Contrast Monochrome]]

---

### 167. 草地上的超逼真情侣自拍提示

**Author**: [Doctor Wasif](https://x.com/doctorwasif)  **Date**: 2026-01-26  **Language**: en

> 生成一张超现实、抓拍式、俯视情侣自拍的提示词（面部锁定为上传的参考图），情侣躺在绿草地上，画面呈现黄金时段光线，表情俏皮嘟嘴。

![草地上的超逼真情侣自拍提示](https://cms-assets.youmind.com/media/1769495403488_m9qovg_G_kVPGSWMAAhr3Y.jpg)
![草地上的超逼真情侣自拍提示](https://cms-assets.youmind.com/media/1769495403546_ir731b_G_kVO39aYAAcSHG.jpg)
![草地上的超逼真情侣自拍提示](https://cms-assets.youmind.com/media/1769495403644_lvv5cf_G_V4p82akAA80bI.jpg)
![草地上的超逼真情侣自拍提示](https://cms-assets.youmind.com/media/1769495406038_ftfslo_G_V4qB-bAAEIluA.jpg)

```
Use 100% uploaded image face details, Create a hyper-realistic selfie photo of a couple (man and woman) with faces 100% identical to the uploaded reference, lying side by side on fresh green grass, captured from a top-down angle. Their expressions are natural Pouting or making a playful frown.
Ensure their face shapes, eyes, noses, and smiles mirror the reference exactly.
Lighting:
Golden hour, warm sunlight gently illuminating their faces with soft shadows, creating a romantic and relaxed vibe. Hair gently blown by light wind.
Style & Details:
Realistic candid couple shot, with natural skin texture, sharp focus, high detail, photorealistic, 4K quality.
Background:
Natural green grass, calm, romantic atmosphere. The photo feels authentic like a real camera shot.
Aspect ratio: 9:16
```

[[Identity Preservation]] [[Golden Hour Photography]]

---

### 168. 高端时尚黑白编辑肖像提示词（面部锁定）

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-26  **Language**: en

> 一个用于生成高对比度黑白编辑肖像的提示，使用严格的面部参考锁定。主体姿态富有戏剧性，部分遮盖面部，强烈的自然阳光强调了轮廓和纹理，模仿了 Canon EOS R5 85mm f/1.8 镜头的效果。

![高端时尚黑白编辑肖像提示词（面部锁定）](https://cms-assets.youmind.com/media/1769495363386_4a346e_G_kPU4BbUAA6s0W.jpg)

```
Use The Uploaded Image Of The Woman As Strict Facial Reference And Physical Features - Keep Her Real Face Exactly As Provided, Without Alterations Or Stylization. Ensure Seamless, Ultra-realistic Integration In The Final Render. Black And White High-fashion Editorial Portrait Of The Uploaded Person, Wearing A Loose White Blouse. She Poses With One Arm Raised, Partially Covering Her Face While Holding Her Hair Up, Creating A Dramatic And Artistic Composition. Her Gaze Is Intense And Captivating, Directly Toward The Camera, Exuding A Strong, Enigmatic Aura.
Background: Minimalist Plain Wall With Sharp Daylight Shadows
Adding Contrast And Depth.
Lighting: Harsh Natural
Sunlight, High-contrast, Emphasizing Facial Contours, Cheekbones, Hair Texture, And Fabric Detail. Pose: Bold And Expressive, Arm Lifted Framing The Face To Emphasize Raw Emotion And High-fashion Editorial Style.
Camera: Eye-level Close-up,
Focusing On Facial Expression, Texture, And Dramatic Shadow Play. Captured As If With Canon Eos R5, 85mm F/1.8 Lens - Crisp Detail, Tonal Depth, Fine Grain.
Style: Monochrome, Ultra-realistic, Cinematic, High-fashion
Editorial Photography.ashion editorial photography.
```

[[Identity Preservation]] [[High Contrast Monochrome]]

---

### 169. 法国蔚蓝海岸的安娜·德·阿玛斯超逼真时尚肖像

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-01-26  **Language**: en

> 一个极其详细、结构化的提示，用于生成一张超逼真的电影级时尚肖像，描绘安娜·德·阿玛斯（Ana de Armas）坐在法国里维埃拉的石质栏杆上。该提示强调严格的身份保留、逼真的织物纹理和高端的编辑美学。

![法国蔚蓝海岸的安娜·德·阿玛斯超逼真时尚肖像](https://cms-assets.youmind.com/media/1769495384295_5vcquo_G_j2wtRWYAEnvEo.jpg)
![法国蔚蓝海岸的安娜·德·阿玛斯超逼真时尚肖像](https://cms-assets.youmind.com/media/1769495384252_td30te_G_j2wpKXgAAUuNn.jpg)

```
{
  "style": "Ultra-realistic cinematic fashion portrait",
  "theme": "Luxury French Riviera editorial",
  "composition": {
    "orientation": "Vertical",
    "framing": "Three-quarter crop from waist to knee"
  },
  "resolution": "RAW 8K",
  "aesthetic": "Maximum photorealism, refined high-fashion magazine aesthetic",
  "identity_preservation": {
    "facial_identity": "100% identical",
    "body_proportions": "Exact match",
    "features": [
      "No face change",
      "No body reshaping",
      "No stylization",
      "Natural anatomy",
      "Real posture",
      "Real proportions",
      "Skin tone, facial structure, and body alignment match exactly"
    ]
  },
  "subject": {
    "name": "Ana de Armas",
    "identity": "Exact likeness",
    "pose": {
      "position": "Seated on stone balustrade",
      "location": "French Riviera terrace",
      "posture": "Torso subtly angled to the left, shoulders relaxed, chin gently toward the camera",
      "gaze": "Confident, calm, subtly seductive, editorial",
      "body_language": "Natural, feminine, controlled",
      "arms": {
        "hands": "Resting on mini handbag, fingers relaxed",
        "elbows": "Soft, natural"
      }
    },
    "outfit": {
      "dress": {
        "style": "Structured corset mini dress",
        "color": "Neutral light tone",
        "details": [
          "Cap sleeves",
          "Deep neckline",
          "Corset boning visible through bodice",
          "Delicate covered buttons",
          "Sculptural skirt subtly flaring",
          "Fabric: matte satin-cotton blend, zero shine, crisp texture, realistic folds and seams"
        ]
      }
    },
    "accessories": [
      {
        "type": "Mini padded handbag",
        "details": "Held with both hands, fine chain strap, subtle diamond-like speckle detailing"
      },
      {
        "type": "Minimalist tennis bracelet and refined rings",
        "details": "Realistic scale and weight, no exaggerated sparkle"
      }
    ]
  },
  "environment": {
    "setting": "Elegant French Riviera terrace",
    "foreground": "Stone balustrade",
    "additional_elements": [
      "Classical white cherub statue",
      "Softly defocused background suggesting coastal luxury, Mediterranean architecture"
    ]
  },
  "lighting": {
    "type": "Bright natural daylight",
    "shadows": "Soft, realistic",
    "highlights": "Clean, defining form, fabric structure, and skin texture",
    "exposure": "Balanced, editorial contrast, no harsh clipping"
  },
  "camera": {
    "capture_type": "DSLR aesthetic",
    "lens": "85mm",
    "depth_of_field": "Shallow",
    "focus": "Torso, hands, corset structure, fabric details",
    "lens_compression": "Natural",
    "color_grading": "Cinematic yet realistic"
  },
  "rendering_constraints": {
    "ultra_realism": true,
    "prohibited_artifacts": [
      "AI artifacts",
      "Plastic skin",
      "Waxy textur
```

[[Identity Preservation]] [[Cinematic Fashion Portrait]]

---

### 170. 西姆拉舒适的冬季咖啡馆场景

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-26  **Language**: en

> 生成一张舒适的室内照片的提示词：一名女子坐在印度西姆拉一家乡村咖啡馆结霜的窗边。重点是温暖的钨丝灯光与窗外寒冷的蓝色暮光形成对比，并保持参考图像中精确的面部特征。

![西姆拉舒适的冬季咖啡馆场景](https://cms-assets.youmind.com/media/1769495382852_lmzp41_G_jmyfGbgAEtrvL.jpg)

```
A cozy indoor shot of the young woman with the sitting by a frost-covered window in a rustic wooden cafe in Shimla. She is wrapped in a traditional patterned Pashmina shawl over a woolen kurta, holding a steaming mug with both hands. She is looking out at pine trees. The indoor lighting is warm tungsten contrasting with the cold blue twilight outside. The mood is relaxed and peaceful, exact same face as the reference image
```

[[Identity Preservation]]

---

### 171. 高能角色转换与极致视角

**Author**: [BeautyVerse](https://x.com/BeautyVerse_Lab)  **Date**: 2026-01-26  **Language**: en

> 一个复杂且结构化的 JSON 提示，旨在将现有角色图像转换为充满活力、富有冒险精神的场景。它使用严格的参考优先级来保持角色的身份、服装和发型，同时将他们置于崎岖的山峰上。该提示指定了极高角度的鸟瞰视角，带有广角畸变，角色摆出“和平”手势，背景是超现实的云朵拼出“BeautyVerse”字样。

![高能角色转换与极致视角](https://cms-assets.youmind.com/media/1769495420783_ha5lpv_G_jgNK6bIAEJzIO.jpg)

```
{
  "reference_priority": {
    "character_face": "STRICT_REFER_TO_IMAGE",
    "outfit_and_hair_logic": "FORCE_EXACT_REPLICA_FROM_REFERENCE",
    "footwear_logic": "FORCE_EXACT_REPLICA_FROM_REFERENCE",
    "consistency_weight": "MAXIMUM"
  },
  "subject": {
    "type": "woman_identity_perfectly_matched_to_reference_image",
    "framing": "extreme_high-angle_bird's-eye_view_full-body_shot",
    "identity_lock": "maintaining_identical_facial_features_from_reference",
    "features": {
      "eyes": "looking_up_at_camera_with_a_bright_friendly_gaze",
      "hair": "EXACT_REPLICATE_HAIRSTYLE_FROM_REFERENCE: length, color, texture, and style must be identical, no headwear",
      "expression": "cheerful_and_cute_expression_with_a_playful_smile"
    },
    "pose_structural_lock": {
      "overall": "standing_confidently_at_the_highest_point_of_a_rugged_mountain_peak",
      "arms": "right_hand_raised_near_the_eye_making_a_peace_sign_V-sign_YA_gesture",
      "hands": "fingers_clearly_formed_into_a_peace_sign_near_the_face",
      "shoulders": "slightly_slouched_creating_a_top-down_foreshortening_effect",
      "perspective": "heavy_wide-angle_distortion_making_the_head_look_larger_than_feet"
    }
  },
  "apparel_specification": {
    "logic": "CLOTHING_AND_FOOTWEAR_MUST_BE_AN_EXACT_CLONE_OF_REFERENCE_IMAGE",
    "outfit_main_piece": {
      "top": "Identical_inner_layer_as_seen_in_reference",
      "bottom": "Identical_pants_from_reference_image",
      "footwear": "EXACT_REPLICATE_FOOTWEAR_FROM_REFERENCE: replicate the specific shoes, colors, and design from the reference image exactly"
    }
  },
  "environment": {
    "setting": "the_summit_of_a_high_mountain_with_jagged_rocks_and_a_cliff_edge",
    "lighting": "bright_natural_daylight_with_soft_clouds_below",
    "background": "monumental_cloud_formations_in_the_distant_sky_arranged_clearly_to_spell_out_the_word_'{argument name="background word" default="BeautyVerse"}'_hovering_above_mountain_ranges",
    "atmosphere": "majestic_and_adventurous_high-altitude_vibe_with_surreal_elements"
  },
  "realism_and_rendering": {
    "style": "adventure_outdoor_photography_with_surrealist_elements",
    "camera": "Ultra-wide_angle_lens_shot_from_above_height_emphasizing_the_height_of_the_peak",
    "image_quality": "8k_resolution_hyper-realistic_rock_textures_and_fabric_weave",
    "aspect_ratio": "3:4"
  }
}
```

[[Identity Preservation]] [[Wide Angle Distortion]] [[Bird's Eye View]]

---

### 172. 休闲运动瑜伽姿势生活方式摄影提示

**Author**: [Ivanna Humeniuk](https://x.com/ivanka_humeniuk)  **Date**: 2026-01-25  **Language**: en

> 一个详细的 JSON 提示，用于生成一张高质量的生活方式照片：在一个现代简约的卧室里，一个人物正在进行瑜伽伸展（鸽子式变体）。该提示强调使用参考照片来保持人物身份、自然日光以及运动休闲美学。

![休闲运动瑜伽姿势生活方式摄影提示](https://cms-assets.youmind.com/media/1769408705679_yqsi0s_G_iHKB-XkAAAAGz.jpg)

```
{
  "image": {
    "main_description": "A medium full-body side-profile shot of a fit character performing a yoga stretch (pigeon pose variation) on a textured mat in a bedroom setting.",
    "characters": {
      "main_reference_character": {
        "identity_anchor": "The character based on the provided reference photo, preserving strictly the user's identity source.",
        "ethnicity_and_phenotype": "Determined by the user provided reference photo.",
        "face_and_skin": "Skin texture and lighting interaction consistent with the scene, but facial features are strictly derived from the reference.",
        "expression": "Micro-expressions and gaze direction matching the input style image; face is largely obscured by hair.",
        "hair": "Hair worn loose in a voluminous, natural, messy-chic style, falling freely and partially covering the face.",
        "body_and_pose": "Seated yoga position (Pigeon pose variation); one leg bent in front on the mat, the other leg extended back with the knee bent at a 90-degree angle pointing upward. Upright torso with a slight arch, showcasing flexibility and physique.",
        "outfit": "A white long-sleeved ribbed crop top, tight-fitting black high-waisted ribbed leggings that accentuate the form, and white slouchy crew socks."
      },
      "supporting_characters": []
    },
    "text_elements": {
      "content": "",
      "typography": "",
      "placement": "",
      "integration": ""
    },
    "environment": {
      "location": "A modern, minimalist bedroom or home studio space.",
      "elements": "A gray yoga mat with a distinct wavy grip texture on the floor. A bed frame with gray bedding and a duvet visible in the background. Dark gray curtains to the left.",
      "atmosphere": "Calm, casual, domestic, focused on fitness and wellness."
    },
    "cinematography": {
      "lighting_setup": "Soft, natural daylight coming from a window on the left, creating gentle highlights on the hair and clothing folds, with soft shadows on the right side.",
      "color_grading": "Neutral and desaturated tones: blacks, whites, grays, and natural wood tones.",
      "shadows_and_highlights": "Soft diffuse shadows, no harsh contrast.",
      "reflections": "Matte finishes on clothing, slight sheen on the hair."
    },
    "camera_and_tech": {
      "framing": "Medium-long shot, side profile, eye-level to slightly low angle, capturing the full pose.",
      "optics": "Standard focal length (approx 35mm-50mm), moderately shallow depth of field to keep focus on the subject while slightly softening the bedroom background.",
      "visual_fidelity": "High quality, social media aesthetic, sharp texture details on the ribbed clothing and mat."
    },
    "style_and_mood": {
      "aesthetic": "Fitness influencer, athleisure, lifestyle photography, casual realism.",
      "emotional_vibe": "Relaxed, disciplined, serene."
    },
    "aspect_ratio": "2:3"
  }
}
```

[[Identity Preservation]] [[Natural Daylight]]

---

### 173. 现代卧室里的时尚镜面自拍

**Author**: [Ivanna Humeniuk](https://x.com/ivanka_humeniuk)  **Date**: 2026-01-25  **Language**: en

> 一个详细的 JSON 提示，用于在现代简约的卧室中生成一张时尚的全身镜面自拍。该提示要求严格保留主体在参考照片中的身份，详细说明了服装（黑色迷你连衣裙、麂皮靴），并强调了电影摄影效果，特别是镜子中反射的明亮闪光光斑。

![现代卧室里的时尚镜面自拍](https://cms-assets.youmind.com/media/1769408708044_6kcvwu_G_iDvL9WYAAUVAm.jpg)

```
{
  "image": {
    "main_description": "A stylish mirror selfie captured in a modern bedroom, featuring a woman in a chic outfit posing with a bright flash flare reflecting in the mirror.",
    "characters": {
      "main_reference_character": {
        "identity_anchor": "The character based on the provided reference photo, preserving strictly the user's identity source.",
        "ethnicity_and_phenotype": "Determined by the user provided reference photo.",
        "face_and_skin": "Skin texture and lighting interaction consistent with the scene, warm tones, facial features are strictly derived from the reference.",
        "expression": "Confident and alluring gaze directed towards the mirror/phone, lips slightly parted or pouting.",
        "hair": "Hair styled with a clean middle part, falling naturally over the shoulders.",
        "body_and_pose": "Standing full-body pose, slightly angled, one leg slightly bent in a casual stance. One arm is raised holding a smartphone to take a mirror selfie, the other arm hangs naturally by the side holding a handbag.",
        "outfit": "A form-fitting {argument name="dress color" default="black"} sleeveless mini dress with a high neckline (turtleneck). Knee-high brown suede boots with high heels. Accessories include a small structured handbag held in the left hand and a bracelet on the wrist."
      },
      "supporting_characters": []
    },
    "text_elements": {
      "content": "",
      "typography": "",
      "placement": "",
      "integration": ""
    },
    "environment": {
      "location": "A modern, minimalist bedroom interior.",
      "elements": "A bed with white linens and a beige textured throw blanket, light wood flooring, a window with woven bamboo blinds, a modern black metal chandelier hanging from the ceiling, white walls.",
      "atmosphere": "Cozy, chic, and intimate domestic setting."
    },
    "cinematography": {
      "lighting_setup": "Dominated by a bright, starburst-shaped flash reflection from the smartphone in the mirror. Ambient natural light coming from the window behind, creating a mix of silhouette and fill light.",
      "color_grading": "Warm, golden tones with slightly vintage or filtered aesthetic common in social media photography.",
      "shadows_and_highlights": "Strong highlights from the flash, softer shadows in the room corners.",
      "reflections": "The entire image is a reflection in a large vertical mirror."
    },
    "camera_and_tech": {
      "framing": "Vertical shot (9:16 aspect ratio), full-body mirror selfie perspective.",
      "optics": "Smartphone camera lens simulation, slight wide-angle distortion typical of mirror selfies.",
      "visual_fidelity": "High quality social media snapshot aesthetic, slight bloom around the light source."
    },
    "style_and_mood": {
      "aesthetic": "Influencer chic, 'Outfit of the Day' (OOTD), lifestyle photography.",
      "emotional_vibe": "Confident, trendy, relaxed."
    },
    "aspect_ratio": "9:16"
  }
}
```

[[Identity Preservation]] [[Mirror Selfie]] [[Black Mini Dress]]

---

### 174. 电影级写实旅行专题肖像

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-25  **Language**: en

> 一个详尽的、高度结构化的提示，用于生成一张逼真的旅行专题肖像，描绘一位女士在热带泻湖的长尾船船头。它对风格、构图和面部识别使用了严格的参考锁定，并详细说明了场景、服装（柔和的粉色连衣裙）、光线（正午阳光）和电影般的质感要求。

![电影级写实旅行专题肖像](https://cms-assets.youmind.com/media/1769495437979_c00ozr_G_havUtWUAAk0V3.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_travel_boat_portrait_tropical_lagoon",
      "version": "v1.0_TROPICAL_LAGOON_LONGTAIL_BOW_PASTEL_DRESS_NO_TEXT_EN",
      "priority": "highest",
      "language": "en"
    },
    "references": {
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "STYLE_COMPOSITION_LOCATION_ANCHOR",
        "strict_lock": true,
        "preserve_composition": true,
        "preserve_pose": true,
        "preserve_lighting": true,
        "preserve_palette": true,
        "preserve_vibe": true
      },
      "reference_image_face": {
        "source": "UPLOAD_REFERENCE_IMAGE (OPTIONAL)",
        "purpose": "FACE_IDENTITY_LOCK",
        "strict_lock": true,
        "face_similarity_priority": "MAX",
        "no_identity_blending": true,
        "no_beautify": true,
        "no_age_shift": true,
        "preserve_skin_texture": true,
        "preserve_facial_proportions": true
      }
    },
    "global_constraints": {
      "rating": "PG-13",
      "no_nudity": true,
      "no_explicit_sexual_content": true,
      "no_logos": true,
      "no_watermark": true,
      "no_readable_text": true
    },
    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "cinematic_photoreal_travel_editorial",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle",
      "color_grade": "bright_tropical_teal_water_clean_blue_sky",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "creative_prompt": {
      "scene_summary": "Photoreal travel editorial portrait on the bow of a wooden longtail boat in a bright tropical lagoon. Water is vivid turquoise/emerald and crystal clear, with gentle ripples and sun sparkle. Background: dramatic limestone karst cliffs covered in lush greenery on both sides, creating a wide bay; a few distant boats are visible but small and unobtrusive.\n\nSubject: one adult woman sitting on the boat’s front deck (bow), centered lower frame. Pose: seated with one knee bent and the other leg extended along the wooden deck, one hand resting behind for support, the other relaxed on her thigh. Expression calm and dreamy, gaze slightly to the left.\n\nWardrobe: soft pastel pink off-shoulder knit mini dress with long sleeves (cozy texture), elegant and clean. Accessories: a single white tropical flower tucked behind the ear. Barefoot or minimal sandal; natural makeup.\n\nLighting: strong midday sun with clean, realistic shadows; natural highlights on skin and water; clear blue sky.\n\nImportant: REMOVE/AVOID any readable lettering or painted text on the boat; keep the wooden deck clean or make markings abstract/unreadable. No text anywhere in the image. Maintain realistic skin texture, fabric knit detail, and cinematic tra
```

[[Identity Preservation]] [[Noon Sunlight]]

---

### 175. 赛道上的超写实情侣生活方式主题大片

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-24  **Language**: en

> 一个高度结构化、复杂的 JSON 提示，旨在生成在现代赛车场看台上拍摄的坦率情侣的超逼真图像。它包含广泛的身份保留限制（要求提供女性主体的面部参考图像）、禁止文本/标志的全局规则，以及关于场景、服装和相机语言的详细创意说明，旨在呈现真实、未经修饰的编辑风格。

![赛道上的超写实情侣生活方式主题大片](https://cms-assets.youmind.com/media/1769322298415_spzx9h_G_dV0o_WgAAHxLR.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_candid_couple_racetrack_lifestyle",
      "version": "v1.0_RACEWEEKEND_CANDID_COUPLE_GRANDSTAND_NO_TEXT_EN",
      "priority": "highest",
      "language": "en"
    },
    "references": {
      "reference_image_face_female": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "FACE_IDENTITY_LOCK_FEMALE",
        "strict_lock": true,
        "face_similarity_priority": "MAX",
        "no_identity_blending": true,
        "no_beautify": true,
        "no_age_shift": true,
        "preserve_skin_texture": true,
        "preserve_facial_proportions": true,
        "preserve_moles_freckles_scars": true,
        "preserve_eye_shape": true,
        "preserve_nose_shape": true,
        "preserve_lip_shape": true,
        "preserve_jawline": true
      },
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (OPTIONAL)",
        "purpose": "STYLE_COMPOSITION_ANCHOR",
        "strict_lock": false,
        "preserve_lighting": true,
        "preserve_palette": true,
        "preserve_vibe": true,
        "preserve_composition": true
      }
    },
    "global_constraints": {
      "rating": "PG-13",
      "no_explicit_sexual_content": true,
      "no_nudity": true,
      "no_text": true,
      "no_logos": true,
      "no_watermark": true
    },
    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "ultra_photoreal_candid_lifestyle_editorial",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle",
      "color_grade": "daylight_film_clean",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "global_rules": {
      "camera_language": "35mm candid photo, slight handheld feel, natural perspective, sharp focus on faces, realistic crowd depth",
      "lighting_language": "bright overcast-to-sunny daylight, soft shadows, no harsh flash",
      "authenticity_markers": "no AI glow, no HDR, accurate hands and fingers, no warped railings, identity must match reference exactly"
    },
    "creative_prompt": {
      "scene_summary": "A photoreal candid couple photo at a modern racing circuit grandstand. The adult woman (face EXACTLY matching the reference) stands in front, leaning on a metal barrier with relaxed posture. Her partner stands behind her with one arm around her waist in a natural, affectionate pose. Background shows a racetrack curve, grandstands, and a big screen in the distance, all softly blurred. Absolutely no readable brand names or text anywhere (screens, banners, track boards must be blank/unreadable).",
      "wardrobe_and_style": {
        "female_outfit": "{argument name="female outfit" default="red sporty crop top with a small blank shield-shaped patch (NO logo), low-rise blue jeans, black small rectangular sunglasses, gold c"}"
      }
    }
  }
}
```

[[Identity Preservation]] [[Candid Style]]

---

### 176. 身着蕾丝迷你连衣裙的女性超写实影棚拍摄

**Author**: [Melis✨](https://x.com/miilesus)  **Date**: 2026-01-20  **Language**: en

> 这是一个高度技术化且结构化的提示，用于生成一张超现实、摄影测量的影棚图像。图像中，一位身材曼妙的女性身穿象牙色蕾丝迷你连衣裙和金属金色细高跟凉鞋，双腿交叉抬高坐着。该提示要求从参考图像中高度保留身份特征，呈现毛孔级别的皮肤细节，并使用 85mm 人像镜头，通过专业的影棚布光（柔光箱主光、轮廓光）进行拍摄。

![身着蕾丝迷你连衣裙的女性超写实影棚拍摄](https://cms-assets.youmind.com/media/1768977345482_xbvgoj_G_IJ7k9W8AAIn05.jpg)

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
      "color": "{argument name="dress color" default="Ivory / Off-white"}",
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

[[Identity Preservation]] [[Fashion Editorial]] [[Hyperrealistic Photography]] [[Studio Portrait]]

---

### 177. 超逼真坐姿肖像提示词（安娜·德·阿玛斯）

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-01-20  **Language**: en

> 一个详细的 JSON 提示，用于生成安娜·德·阿玛斯 (Ana de Armas) 坐在一张极简主义表面上的超现实、摄影测量质量肖像。该提示指定了高身份保留、详细的皮肤纹理、一件象牙色蕾丝迷你连衣裙、金属金色细高跟凉鞋，以及用于营造高级时尚杂志美感的影棚灯光设置。此提示与 2013647003754823908 几乎相同，但指定了不同的背景设置。

![超逼真坐姿肖像提示词（安娜·德·阿玛斯）](https://cms-assets.youmind.com/media/1768977291595_4yaa3u_G_HuAKzXcAAQd1G.jpg)
![超逼真坐姿肖像提示词（安娜·德·阿玛斯）](https://cms-assets.youmind.com/media/1768977291691_ipjeda_G_HuAV4XsAEJO9X.jpg)

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
      "color": "{argument name="dress color" default="Ivory / Off-white"}",
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
    "setting": "{argument name="setting" default="High-end minimalist studio or neutral architectural background"}",
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

[[Identity Preservation]] [[Celebrity Portrait]] [[Fashion Editorial]] [[Studio Portrait]]

---

### 178. 超逼真坐姿肖像提示（安娜·德·阿玛斯/多模型）

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-01-20  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真、摄影测量质量的主体肖像（旨在是安娜·德·阿玛斯或类似模特），主体坐在一张极简主义的表面上。该提示指定了高身份保留、详细的皮肤纹理、一件特定的象牙色蕾丝迷你连衣裙、金属金色细高跟凉鞋，以及用于营造高级时装社论美学的影棚灯光设置。

![超逼真坐姿肖像提示（安娜·德·阿玛斯/多模型）](https://cms-assets.youmind.com/media/1768977286915_c6f1s9_G_HpRM5WUAA0SgS.jpg)
![超逼真坐姿肖像提示（安娜·德·阿玛斯/多模型）](https://cms-assets.youmind.com/media/1768977286922_xw8zee_G_HpROXW0AAJbIl.jpg)
![超逼真坐姿肖像提示（安娜·德·阿玛斯/多模型）](https://cms-assets.youmind.com/media/1768977286913_8jt964_G_HpRTuXEAAFzYb.jpg)
![超逼真坐姿肖像提示（安娜·德·阿玛斯/多模型）](https://cms-assets.youmind.com/media/1768977287859_7bqj3u_G_HpRXDXsAARM__.jpg)

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
      "color": "{argument name="dress color" default="Ivory / Off-white"}",
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

[[Identity Preservation]] [[Celebrity Portrait]] [[Studio Lighting]] [[Fashion Editorial]]

---

### 179. Nano Banana Pro 奢华社论狗仔队风格图像编辑提示

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2026-01-20  **Language**: en

> 这是一个针对 Nano Banana Pro 的高度具体的图像编辑提示，旨在将现有图像转换为奢华的社论式狗仔队风格照片。该提示要求严格保留原始面部特征，同时添加特定的高级时尚元素：浅灰色细条纹双排扣西装、深色太阳镜、奢华配饰（腕表、链式手链）和道具（雪茄）。场景设定在一个精致的户外咖啡馆。

![Nano Banana Pro 奢华社论狗仔队风格图像编辑提示](https://cms-assets.youmind.com/media/1768977373379_s0145g_G_Hif1SWYAAC-7i.jpg)
![Nano Banana Pro 奢华社论狗仔队风格图像编辑提示](https://cms-assets.youmind.com/media/1768977373394_msgxj0_G_E_6ufX0AAsVDt.jpg)

```
{
  "type": "image_editing_prompt",
  "language": "English",
  "style": "luxury editorial, paparazzi-style street photography",
  "aspect_ratio": "4:5",
  "identity_preservation": {
    "use_reference_image": true,
    "strict_identity_lock": true,
    "notes": "Preserve 100% of the original facial identity, structure, proportions, skin texture, and expression from the uploaded reference image. No facial alterations."
  },
  "subject": {
    "gender": "female",
    "expression": "confident, serious, mysterious",
    "appearance": {
      "eyewear": "dark, thick-rimmed sunglasses concealing the eyes",
      "hair": "unchanged from reference image"
    },
    "clothing": {
      "suit": {
        "color": "light gray / silver",
        "pattern": "fine vertical pinstripes",
        "jacket": "double-breasted with two rows of dark buttons",
        "trousers": "matching gray pinstriped fabric"
      },
      "shirt": "white dress shirt",
      "tie": "dark red tie",
      "pocket_square": "dark red, neatly folded"
    },
    "accessories": [
      "oversized luxury wristwatch with gold bezel on left wrist",
      "wide heavy gold chain bracelet on left wrist",
      "ring on the ring finger of the right hand"
    ],
    "props": {
      "right_hand": "holding a thick cigar between the fingers",
      "left_hand": "holding a small white object (possibly a lighter)"
    },
    "pose": {
      "position": "seated on a woven rattan/wicker café chair",
      "body_language": "leaning slightly forward",
      "elbow_position": "right elbow resting on a small round table"
    }
  },
  "shot": {
    "type": "close-up to medium close-up",
    "framing": "chest level and above",
    "focus": "subject is the absolute focal point"
  },
  "environment": {
    "setting": "sophisticated outdoor café or restaurant terrace"
```

[[Identity Preservation]] [[Street Photography]] [[Image Editing]] [[Luxury Fashion]]

---

### 180. 高定时髦都市人像摄影，搭配 Grillz

**Author**: [Noname Oasis](https://x.com/nonameoasis)  **Date**: 2026-01-20  **Language**: en

> 一个用于高端时尚都市社论肖像的提示，要求严格保留参考图像中的身份，描绘一个佩戴镶钻牙套、发型光滑湿润、身穿奢华街头服饰的主体，置身于白色影棚环境中。

![高定时髦都市人像摄影，搭配 Grillz](https://cms-assets.youmind.com/media/1768977305068_980kwy_G_HMfotWIAAILOn.jpg)
![高定时髦都市人像摄影，搭配 Grillz](https://cms-assets.youmind.com/media/1768977304926_whj22i_G_HMfuNXQAE2EPc.jpg)

```
{
"type": "High-fashion urban editorial portrait",
"aspect_ratio": "16:9",
"identity_constraints": [
"Strict identity preservation from reference image",
"Do NOT change hair color under any circumstance",
"Hair color, tone, and hue must remain identical to the reference image"
],
"shot": "Cinematic medium close-up, 50mm lens, ARRI Alexa LF look, static camera, eye-level, symmetrical framing, slight head tilt",
"subject": "A modern urban gangster woman in a luxury fashion editorial. She smiles openly and confidently, fully revealing diamond-encrusted grillz on all her teeth, reflecting studio light. Facial structure and nose must remain identical to the reference image. Skin is ultra-realistic with visible micropores, microhairs, subsurface scattering, and natural highlights.",
"hair": "Hair identical to the reference image in color and tone, sleek editorial wet finish, no recoloring or color reinterpretation",
"pose": "Facing forward, chin slightly raised, one hand near the face in a confident gesture",
"wardrobe": {
"jacket": "{argument name="jacket color" default="Emerald green"} leather cropped jacket worn open as a top",
"top": "Black athletic sports bra underneath",
"pants": "High-waisted baggy pants, luxury streetwear fit",
"gloves": "High-fashion motorcycle gloves, fingerless",
"accessories": ["Full diamond grillz on all teeth", "Gold hoop earrings"]
},
"scene": "Professional fashion photography studio with pure white seamless background",
"lighting": "High-key studio lighting, neutral white balance, no color cast affecting skin or hair",
"mood": "Luxury, urban authority, modern femininity",
"style": "Photorealistic, magazine-quality fashion photography, clean and polished"
}
```

[[Identity Preservation]] [[Studio Portrait]] [[Urban Fashion Editorial]] [[Luxury Streetwear]]

---

### 181. 象牙色蕾丝迷你连衣裙超逼真时尚肖像

**Author**: [Yaseen Khan Gul](https://x.com/YaseenK7212)  **Date**: 2026-01-20  **Language**: en

> 一个高度详细、结构化的 JSON 提示，用于生成一张超写实、高级时装的编辑肖像。该提示指定了严格的身份保留、双腿交叉的曲线姿势、象牙色蕾丝迷你连衣裙、金属金色高跟鞋，以及用于 8k 分辨率输出的专业影棚布光设置。

![象牙色蕾丝迷你连衣裙超逼真时尚肖像](https://cms-assets.youmind.com/media/1768977264793_citx1t_G_G0HuHXIAAWQ5_.jpg)
![象牙色蕾丝迷你连衣裙超逼真时尚肖像](https://cms-assets.youmind.com/media/1768977264788_pi7mc2_G_G0HuHWkAAm59F.jpg)
![象牙色蕾丝迷你连衣裙超逼真时尚肖像](https://cms-assets.youmind.com/media/1768977264778_t5tftp_G_G0HuPWAAACnlV.jpg)

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

[[Identity Preservation]] [[Fashion Editorial]] [[8K Resolution]] [[Studio Portrait]]

---

### 182. 豪车狗仔队闪光肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-20  **Language**: en

> 一个详细的提示，用于生成一张超现实、抓拍式的肖像，具有狗仔队美学，重点是刺眼、直射的机载闪光灯照明和高对比度。主体坐在豪华轿车的后座上，身穿定制的细条纹西装，并严格指示保留参考照片中的面部特征。

![豪车狗仔队闪光肖像](https://cms-assets.youmind.com/media/1768977270925_90qiqh_G_GpL0gXkAA_FfS.jpg)

```
use the exact facial features from the uploaded reference photo, do not alter face shape, eyes,

nose, lips, skin tone or proportions in any way, 0% face modification, identity lock, strict face

preservation hyper-realistic photography, looks like a real paparazzi fashion photo, natural skin

texture with visible pores, fine lines and subtle imperfections, realistic skin sheen, no plastic skin,

high-resolution fashion photograph, sharp focus, ultra-detailed direct

on-camera flash, paparazzi

flash photography, hard frontal flash, harsh shadows, strong highlights, high contrast lighting, flash

overpowering ambient light, slight overexposure on skin highlights, realistic flash falloff shot on fullframe DSLR, 35mm lens, slightly wide perspective, shallow depth of field, handheld camera feeling, candid framing nighttime interior car setting, luxury car back seat, black leather seats,

dark surroundings outside the windows, cinematic night mood, editorial paparazzi aesthetic model

wearing a tailored black pinstripe suit, oversized blazer with structured shoulders, white crisp shirt,

black slim tie, black tailored trousers, silver jewelry: small hoop earrings, subtle bracelet, watch,

makeup: glossy lips, defined eyes, soft contour, natural glow, hair styled in a messy elegant updo

with loose strands framing the face, close-up portrait, candid moment, model laughing softly, eyes

half-closed, head tilted back slightly, natural spontaneous emotion, not posed, direct flash freezing

motion, hair strands caught mid-movement, editorial paparazzi feel
```

[[Identity Preservation]] [[Flash Photography]] [[High Contrast Photography]] [[Luxury Automobile]]

---

### 183. 高级时装动画：宇宙云端上的魅力女性

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-20  **Language**: en

> 一个动画提示：一位迷人的年轻女子，身着高级时装（黄色漆皮乳胶束身衣，绿色工装裤），站在蓬松的白云上，置身于星系璀璨的夜空下。要求严格保留参考图像中的面部特征，采用电影级布光，并伴随缓慢的镜头移动。

```
Animate a stunning glamorous young western woman, keeping her face identical to the reference image without changing facial features. She has long straight hair with blonde highlights and dark roots, bold dramatic makeup, full lips, and sharp eyeliner. She stands confidently with hands on hips, wearing a shiny yellow patent latex corset top with thin spaghetti straps, front gold chain details and buckles, cut-out sides exposing underboob and midriff, paired with loose bright hot green parachute cargo pants with elastic waist and cuffs. Pose powerfully on a dreamy bed of fluffy white clouds at night, under a starry galaxy sky with subtle cosmic glow. Cinematic lighting with rim light and soft starry highlights on her skin and outfit, ultra-detailed skin texture, glossy latex reflections, vibrant colors, high fashion editorial style, 8K resolution, professional photoshoot look, highly detailed, sharp focus. Slowly rotate camera around her, slight floating motion of clouds, gentle shimmering stars in the background, cinematic slow pan and tilt, elegant, magical, ultra-realistic, hyper-detailed animation.
```

[[Identity Preservation]] [[Luxury Fashion]]

---

### 184. 超现实主义高级定制沙漠提示

**Author**: [Javeriya ✨](https://x.com/JadoonKhan281)  **Date**: 2026-01-20  **Language**: en

> 一个结构化的 JSON 提示，用于生成一张超现实、高调的时尚大片图像，要求从参考图像中实现 100% 的面部完整性。图像中，主体身穿宝蓝色天鹅绒泳衣，在白色沙丘上摆姿势，头顶是广阔的深蓝色天空。

![超现实主义高级定制沙漠提示](https://cms-assets.youmind.com/media/1768977321546_yy75zn_G_GV1htW4AA_NfO.jpg)
![超现实主义高级定制沙漠提示](https://cms-assets.youmind.com/media/1768977321665_y9khem_G_GV1g3WgAAq2re.jpg)
![超现实主义高级定制沙漠提示](https://cms-assets.youmind.com/media/1768977321662_xy7trn_G_GV1YSWoAALBtv.jpg)
![超现实主义高级定制沙漠提示](https://cms-assets.youmind.com/media/1768977322721_4bx4ge_G_GV1kMXMAAYGe9.jpg)

```
{
  "image_metadata": {
    "type": "editorial_fashion",
    "style": "surreal_high_key",
    "camera_settings": {
      "lens": "24mm wide-angle",
      "focus": "ultra-sharp",
      "detail_level": "high-fidelity_texture"
    }
  },
  "subject": {
    "identity": "reference_face_maintained_100%",
    "pose": "angular_introspective_crouch",
    "position": "atop_white_sand_dune",
    "attire": {
      "garment": "{argument name="swimsuit color" default="royal_blue"}_velvet_strapless_swimsuit",
      "texture": "plush_velvet",
      "accessories": [
        "chunky_oversized_gold_bangles"
      ]
    }
  },
  "environment": {
    "location": "white_sand_desert",
    "horizon_line": "low_frame",
    "sky": {
      "color": "deep_blue",
      "condition": "cloudless",
      "scale": "massive"
    }
  },
  "visual_palette": {
    "primary_colors": [
      "pristine_white",
      "beige",
      "intense_royal_blue"
    ],
    "lighting": {
      "type": "high_sun",
      "shadows": "soft_minimal",
      "mood": "dreamlike_pastel"
    }
  },
  "constraints": {
    "facial_integrity": "exact_features_no_alteration",
    "color_retention": "strictly_original_colors"
  }
}
```

[[Identity Preservation]] [[Fashion Editorial]] [[Surrealism]]

---

### 185. Sydney Sweeney 复古胶片肖像提示词

**Author**: [✨ Pulikesi✨](https://x.com/23rd_Pulikesi)  **Date**: 2026-01-20  **Language**: en

> 一个高度受限的提示，用于生成西德尼·斯威尼 (Sydney Sweeney) 的电影风格复古户外肖像，要求最大限度地保留其身份特征，并禁止对其面部特征进行任何修改或美化。该提示要求自然地改变姿势，同时保持相同的道具（一支红色棒棒糖），并应用强烈的模拟胶片美学，包括大量的颗粒、灰尘和温暖的棕橙色调。

![Sydney Sweeney 复古胶片肖像提示词](https://cms-assets.youmind.com/media/1768977289619_owfu95_G_GGXKxXwAAppo2.jpg)
![Sydney Sweeney 复古胶片肖像提示词](https://cms-assets.youmind.com/media/1768977289629_p8ikws_G_GGXKCXYAAbzPr.jpg)
![Sydney Sweeney 复古胶片肖像提示词](https://cms-assets.youmind.com/media/1768977289773_r31g5n_G_GGXTlXoAEnaap.jpg)
![Sydney Sweeney 复古胶片肖像提示词](https://cms-assets.youmind.com/media/1768977290654_layeci_G_GGXdcXIAAZw-N.jpg)

```
{
  "prompt": "Use the uploaded reference image as the absolute identity anchor. Preserve the subject’s facial features, facial proportions, bone structure, eyes, nose, lips, skin tone, hairline, hair texture, body shape, and overall likeness with maximum fidelity. Do not beautify, idealize, or alter the person in any way. A cinematic, vintage-style outdoor portrait of the same person. For each generation, vary the subject’s pose naturally (e.g., slight body angle changes, subtle lean, head tilt, arm positioning) while keeping the same prop: a bright {argument name="prop color" default="red"} lollipop held near the lips or face. Maintain a calm, confident expression. The subject wears a white strapless bandeau top and high-waisted light-blue distressed denim shorts. Lighting is soft, warm, and natural during golden hour. The image has a strong analog film aesthetic with heavy grain, dust, scratches, subtle fading, and a warm brown-orange color cast, resembling an old 35mm photograph. Background is softly blurred with shallow depth of field. Framing remains cinematic and consistent.",
  "identity_preservation": {
    "face_likeness": "maximum",
    "body_proportions": "exact_match",
    "hair": "match_reference"
  },
  "pose_variation": {
    "enabled": true,
    "mode": "random_per_generation",
    "constraints": [
      "natural human poses only",
      "no extreme or distorted angles",
      "no change to body shape or identity"
    ]
  },
  "prop": {
    "name": "{argument name="prop name" default="red lollipop"}",
    "consistency": "same_prop_every_generation"
  },
  "style_keywords": [
    "vintage film photography",
    "analog grain",
    "cinematic portrait",
    "retro aesthetic",
    "natural light",
    "shallow depth of field",
    "realistic skin texture"
  ],
  "camera_settings": {
    "lens": "35mm",
    "aperture": "f/1.8",
    "iso": 800,
    "film_grain": "heavy",
    "vignette": "light"
  },
  "negative_prompt": [
    "face change",
    "different person",
    "altered identity",
    "idealized beauty",
    "smooth plastic skin",
    "CGI",
    "illustration",
    "digital HDR look",
    "modern studio lighting",
    "missing prop",
    "changed prop"
  ],
  "generation_settings": {
    "image_weight": "1.5–2.0",
    "face_consistency": "max",
    "denoising_strength": "0.2–0.35",
    "cfg_scale": "low_to_medium",
    "aspect_ratio": "16:9"
  }
}
```

[[Identity Preservation]] [[Celebrity Portrait]] [[Film Grain]] [[Analog Film Aesthetic]]

---

### 186. 特写肖像提示（聚焦纹理）

**Author**: [路飞 🏴‍☠️ AI 研究员🧐](https://x.com/0xluffy_eth)  **Date**: 2026-01-20  **Language**: zh

> 一个针对 Gemini Nano Banana 的提示，要求根据上传的照片生成一张超特写肖像，强调保留完全相同的面部特征，并突出极致的皮肤纹理、湿润细节以及眼睛的锐利焦点，同时湿发部分遮盖脸部。

![特写肖像提示（聚焦纹理）](https://cms-assets.youmind.com/media/1768977348332_ot7bc6_G_F5FdVW0AA6p2R.jpg)

```
根据这张照片创建极限特写肖像，使用完全相同的面部特征，捕捉强烈的皮肤纹理和水分细节。水润的肌肤闪耀着自然光泽，湿润的发丝部分覆盖眼部区域。眼睛清晰度高
```

[[Identity Preservation]] [[Skin Texture Detail]] [[Wet Hair Portrait]]

---

### 187. 奢华狗仔街拍提示词

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-01-20  **Language**: en

> 一个高度详细的 JSON 结构化提示，用于图像编辑，要求严格保留参考图像中的面部特征。它生成一张豪华的、社论风格的狗仔队街拍照片，照片中人物身穿细条纹西装，戴着深色太阳镜，坐在户外咖啡馆里，手持雪茄。

![奢华狗仔街拍提示词](https://cms-assets.youmind.com/media/1768977327674_rjrd8d_G_E_6ufX0AAsVDt.jpg)

```
{
  "type": "image_editing_prompt",
  "language": "English",
  "style": "luxury editorial, paparazzi-style street photography",
  "aspect_ratio": "4:5",
  "identity_preservation": {
    "use_reference_image": true,
    "strict_identity_lock": true,
    "notes": "Preserve 100% of the original facial identity, structure, proportions, skin texture, and expression from the uploaded reference image. No facial alterations."
  },
  "subject": {
    "gender": "female",
    "expression": "confident, serious, mysterious",
    "appearance": {
      "eyewear": "dark, thick-rimmed sunglasses concealing the eyes",
      "hair": "unchanged from reference image"
    },
    "clothing": {
      "suit": {
        "color": "{argument name="suit color" default="light gray / silver"}",
        "pattern": "fine vertical pinstripes",
        "jacket": "double-breasted with two rows of dark buttons",
        "trousers": "matching gray pinstriped fabric"
      },
      "shirt": "white dress shirt",
      "tie": "dark red tie",
      "pocket_square": "dark red, neatly folded"
    },
    "accessories": [
      "oversized luxury wristwatch with gold bezel on left wrist",
      "wide heavy gold chain bracelet on left wrist",
      "ring on the ring finger of the right hand"
    ],
    "props": {
      "right_hand": "holding a thick cigar between the fingers",
      "left_hand": "holding a small white object (possibly a lighter)"
    },
    "pose": {
      "position": "seated on a woven rattan/wicker café chair",
      "body_language": "leaning slightly forward",
      "elbow_position": "right elbow resting on a small round table"
    }
  },
  "shot": {
    "type": "close-up to medium close-up",
    "framing": "chest level and above",
    "focus": "subject is the absolute focal point"
  },
  "environment": {
    "setting": "sophisticated outdoor café or restaurant terrace
```

[[Identity Preservation]] [[Street Fashion]] [[Outdoor Cafe Setting]] [[Paparazzi Style Photography]]

---

### 188. 戴红色针织帽的肖像提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-20  **Language**: en

> 一张高分辨率肖像提示，重点是保持参考图像中人物的面部和比例，描绘一位体格健硕的男子，戴着一顶鲜红色的针织帽，坐在窗边。

![戴红色针织帽的肖像提示](https://cms-assets.youmind.com/media/1768977321387_bt3gcz_G_Eze58XAAAE_3X.jpg)

```
A high-resolution portrait photograph of a man from a reference image, with his face undisturbed and proportions maintained, seated on a soft bench next to a large vertical window. He has a large, athletic build. The subject occupies the central two-thirds of the horizontal plane and the lower three-quarters of the vertical plane. His hair is visible from under a bright {argument name="hat color" default="red"} knit cap, approximately 20 cm high, with a ribbed texture and a small white tag on the front
```

[[Identity Preservation]] [[Portrait Photography]]

---

### 189. 阴暗地下通道肖像

**Author**: [Hatman 🎩](https://x.com/hatman)  **Date**: 2026-01-19  **Language**: en

> 一个用于生成风格化半身像的提示：一名男子身处昏暗的地下走廊，高对比度照明下，锐利的白光穿透飘浮的灰尘，部分勾勒出他的轮廓。它要求 AI 严格使用上传的参考图像来处理面部，并保持电影感、未来感和忧郁的氛围。

![阴暗地下通道肖像](https://cms-assets.youmind.com/media/1768890667408_cbjb4a_G_DULo6WwAAgVm0.jpg)

```
Create a 4:5 stylized mid-shot of a man standing in a dim underground corridor. Vertical gaps in a metal wall cast sharp beams of white light through drifting dust, partially carving his silhouette. Use the uploaded reference image for the face and do not change any facial features or identity. He wears a dark graphite bomber jacket with subtle metallic texture. High contrast lighting, deep shadows, cinematic and futuristic tension, moody atmosphere, realistic materials and skin texture.
```

[[Identity Preservation]] [[Cinematic Portrait]] [[Futuristic Aesthetic]]

---

### 190. Charli D’Amelio 高对比度编辑肖像

**Author**: [QuestGlitch](https://x.com/AIRevSpot)  **Date**: 2026-01-19  **Language**: en

> 一个旨在将主体替换为 Charli D'Amelio 的提示，同时保持特定的姿势和表情（咆哮、顽皮、过肩拍摄）。它详细描述了她精确的面部特征、妆容、发型，并使用刺眼的正面闪光灯照明，营造出高对比度的时尚工作室效果。

![Charli D’Amelio 高对比度编辑肖像](https://cms-assets.youmind.com/media/1768890653667_4easqt_G_DgYFlW8AA6j3O.jpg)

```
Replace the subject with {argument name="subject name" default="Charli D'Amelio"}. Maintain the exact snarling, playful expression with the nose scrunched and mouth slightly open, showing teeth. The pose is a high-angle over-the-shoulder shot; her body is turned away from the camera, exposing her back, while her head is turned back toward the lens. Her right hand is brought up to her left shoulder, fingers spread and slightly tensed, showcasing rings and hand tattoos.
Charli D’Amelio’s specific facial features—round brown eyes, distinctive nose shape, and natural skin texture with subtle freckles—are integrated into the existing makeup style, which features sharp, winged eyeliner and neutral lips. Her hair is a deep brunette, styled in the same voluminous half-up, half-down look with a slight wave. The lighting is a harsh, direct frontal flash typical of editorial studio photography, creating sharp shadows against the plain off-white wall and highlighting skin porosity and fine details. She wears the same dark, shimmering velvet or lace-textured garment.
```

[[Identity Preservation]] [[Celebrity Portrait]] [[Direct Flash Photography]] [[High Contrast Portrait]]

---

### 191. 欧洲城市高级时装街拍特辑

**Author**: [Melis✨](https://x.com/miilesus)  **Date**: 2026-01-19  **Language**: en

> 一个高度技术化的 JSON 提示，旨在欧洲城市中生成一张高级时装街拍编辑图片。它要求根据面部参考图片严格保留身份，并根据场景参考图片重现场景，详细说明确切的服装（酒红色细条纹西装外套、蕾丝文胸、黑色手套）和技术相机设置（85 毫米镜头，干净的日光）。

![欧洲城市高级时装街拍特辑](https://cms-assets.youmind.com/media/1768890681278_fnedva_G_DHTODXoAI5Hzv.jpg)
![欧洲城市高级时装街拍特辑](https://cms-assets.youmind.com/media/1768890681328_xcgp6j_G_DHTpAWoAEViX-.jpg)

```
{
  "job_id": "photo_03_city_car",
  "model": "nano-banana-pro",
  "task": "image_generation",
  "inputs": {
    "face_reference_image": "<YOUR_FACE_IMAGE>",
    "scene_reference_image": "<SCENE_IMAGE_3>"
  },
  "prompt": "High-fashion street editorial in European city. EXACT SAME FACE as face_reference_image, identical identity. Recreate the scene exactly from scene_reference_image: woman leaning on a vintage car, classic European architecture background. Outfit must match exactly: {argument name="outfit color" default="burgundy pinstripe blazer"} and matching skirt with belt, black lace bra visible, black gloves, sheer black tights, gold earrings. Same pose, same body angle, same framing. Luxury magazine look, clean daylight, 85mm fashion lens feel, natural skin texture.",
  "negative_prompt": "different suit color, no lace bra, face changed, identity drift, stylized, cartoon, CGI, over-retouch, wrong car, wrong city, text, watermark, blur",
  "settings": {
    "stylization": 0,
    "quality": "max",
    "detail_boost": 0.8,
    "lighting_match": "high",
    "composition_match": "max",
    "color_match": "max",
    "identity_preservation": "max",
    "face_consistency": "max",
    "reference_strength": { "face": 1.0, "scene": 0.96 },
  }
}
```

[[Identity Preservation]] [[Fashion Editorial]] [[Street Photography]]

---

### 192. 浓墨速写人像，形神兼备

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-01-19  **Language**: en

> 一个结构化的 JSON 提示词，用于生成富有表现力的水墨素描风格的戏剧性侧面肖像，并融合了混合媒介。它要求根据上传的照片，在面部相似度方面具有高准确性，并叠加神秘的手写笔记和抽象符号等视觉元素，以暗示心理深度。

![浓墨速写人像，形神兼备](https://cms-assets.youmind.com/media/1768890679936_ldsuho_G_CIPPVWsAEvVxM.jpg)
![浓墨速写人像，形神兼备](https://cms-assets.youmind.com/media/1768890679955_dqor32_G_CIPJnWoAA0cOA.jpg)

```
{
  "reference_image": "uploaded_photo",
  "face_likeness": {
    "accuracy": "high",
    "preserve_features": [
      "exact facial structure",
      "natural skin tone",
      "beard shape",
      "nose form",
      "eye shape",
      "original expression"
    ],
    "usage": "primary face reference for proportions and likeness"
  },
  "portrait_style": {
    "composition": "dramatic side-profile portrait",
    "mood": "intense, chaotic, emotionally charged",
    "art_direction": "expressive ink sketch with mixed-media illustration"
  },
  "subject_details": {
    "pose": "side profile",
    "presence": "bold and rebellious",
    "wardrobe": {
      "type": "dark abstract jacket",
      "treatment": "heavy textures, angular strokes, rough ink detailing"
    }
  },
  "visual_elements": {
    "overlays": [
      "{argument name="overlay element 1" default="cryptic handwritten notes"}",
      "symbols and abstract glyphs",
      "fragmented text wrapping around facial contours"
    ],
    "meaning": "suggesting inner conflict, hidden thoughts, and psychological depth"
  },
  "art_technique": {
    "linework": "sharp pen details with aggressive brushwork",
    "effects": [
      "ink splashes",
      "controlled chaos",
      "layered textures"
    ],
    "style_blend": "editorial illustration meets conceptual art"
  },
  "background": {
    "texture": "aged parchment paper",
    "tone": "pale, grainy, desaturated",
    "details": [
      "faded manuscript feel",
      "subtle stains",
      "delicate line artifacts"
    ]
  },
  "overall_aesthetic": {
    "contrast": "high",
    "finish": "bold, experimental, precise yet raw",
    "emotion": "powerful, intense, thought-provoking"
  }
}
```

[[Identity Preservation]] [[Mixed Media Portrait]]

---

### 193. 自拍转专业 LinkedIn 头像

**Author**: [Snow](https://x.com/iamrealsnow)  **Date**: 2026-01-19  **Language**: en

> 一个提示，指示 AI 将上传的自拍照转换为专业的 LinkedIn 职业头像。它指定了柔和模糊的办公室背景，带有大窗户，风格干净真实，经过细微修饰，并采用柔和的日光，同时严格保留原始图像中的面部特征和发型。

![自拍转专业 LinkedIn 头像](https://cms-assets.youmind.com/media/1768890667139_mn1d69_G_BHdvxW4AA41Hs.jpg)

```
Turn this selfie into a professional LinkedIn headshot of a man. Background: softly blurred office with big windows. Style: clean, realistic, subtle retouching, no heavy filters. Lighting: soft daylight from the front. Constraints: keep facial features and hairstyle accurate, no text.
```

[[Identity Preservation]] [[Style Transfer]] [[Professional Headshot]] [[Office Setting]]

---

### 194. Image-to-Image 冬季高山肖像

**Author**: [Sudee🥀](https://x.com/NameIsSudee)  **Date**: 2026-01-19  **Language**: en

> 一个用于 Gemini Nano Banana Pro 的结构化提示，它使用 Stable Diffusion XL 模型进行图像到图像的生成。它需要上传一张参考图像以保留主体的身份，并生成一张超现实的户外冬季肖像，背景是高山阳台，指定了铂金色双马尾、俏皮的表情和清晰自然的冬季日光。

![Image-to-Image 冬季高山肖像](https://cms-assets.youmind.com/media/1768890710684_0yaxud_G_BCVx7XQAASbey.jpg)
![Image-to-Image 冬季高山肖像](https://cms-assets.youmind.com/media/1768890710797_p1utsa_G_BCVwqWkAMyFyL.jpg)

```
{
  "type": "image_to_image",
  "model": "stable-diffusion-xl",
  "prompt": "Use the uploaded image as the main reference and keep the same person, face structure, skin tone, and identity. Create an ultra-realistic outdoor winter portrait on a wooden balcony in snowy alpine mountains. The person is leaning slightly forward toward the camera with a playful kiss-pout expression. Platinum blonde hair styled into two long braided pigtails. Wearing a fitted black long-sleeve top and black pants. Stylish black rectangular sunglasses. Natural fair skin texture with realistic pores and highlights. Background includes snow-covered mountains, pine trees, wooden cabins, and a clear blue winter sky. Fresh snow visible on the balcony railing. A white coffee cup placed casually on the wooden railing. Bright natural winter daylight, crisp sunlight, realistic shadows. Shot with a wide-angle lens, travel lifestyle photography, Instagram aesthetic, ultra-detailed, hyper-realistic, professional photo.",
  "negative_prompt": "blurry, low quality, distorted face, wrong identity, extra fingers, extra limbs, bad anatomy, cartoon, anime, CGI, plastic skin, overexposed snow, watermark, logo, text",
  "settings": {
    "denoise_strength": 0.5,
    "cfg_scale": 7,
    "steps": 30,
    "sampler": "DPM++ 2M Karras",
    "aspect_ratio": "3:4",
    "seed": -1
  }
}
```

[[Identity Preservation]] [[Winter Portrait]]

---

### 195. 宇宙星系水彩肖像画（身份保留）

**Author**: [Gagan Singh](https://x.com/GaganSingh8u)  **Date**: 2026-01-15  **Language**: en

> 一个用于图生图任务的提示词，要求 100% 保留上传参考图像中主体的面部特征和身份。风格为宇宙星系水彩肖像，面部与充满活力的星云纹理和星尘高光柔和融合，背景为深空。

![宇宙星系水彩肖像画（身份保留）](https://cms-assets.youmind.com/media/1768544828587_3lbiom_G-uiPqRbQAI09dg.jpg)

```
{
  "prompt": "Use the uploaded reference image to **preserve 100% of the facial features, identity, age, skin tone, and expression** of the person. Do not alter facial structure or proportions. Create a **cosmic galaxy watercolor portrait** where the face remains soft and realistic but is gently merged with nebula textures. Hair follows the exact reference style, with subtle stardust highlights woven through the strands. Clothing: simple dark or neutral attire that fades into swirling galaxy patterns. Background: deep space filled with vibrant nebulas, glowing stars, floating light particles, and watercolor galaxies in shades of indigo, teal, violet, and cosmic blue. Soft ethereal rim light outlines the silhouette. Fine pencil sketch lines mixed with watercolor bleeds, smooth gradients, dreamy depth, cinematic and artistic masterpiece quality.",
  "negative_prompt": "blurry, low quality, deformed, extra limbs, bad anatomy, watermark, text overlay, anime, cartoon, overexposed, underexposed, ugly face, bad hands, face altered, identity changed, harsh lighting, plastic skin, flat colors",
  "parameters": {
    "steps": 50,
    "cfg_scale": 7.2,
    "sampler": "Euler a or DPM++ 2M Karras",
    "strength": 0.53,
    "noise": 0.28,
    "width": 832,
    "height": 1216,
    "aspect_ratio": "2:3"
  },
  "usage_instructions": "Upload your image in img2img or reference mode. Keep strength around 0.5–0.55 to keep the face **100% matching**, while blending the portrait into a cosmic watercolor universe."
}
```

[[Identity Preservation]]

---

### 196. 霓虹赛博朋克水彩融合插画提示

**Author**: [Gagan Singh](https://x.com/GaganSingh8u)  **Date**: 2026-01-15  **Language**: en

> 一个专为图生图生成设计的提示词，要求 100% 保留参考图像的面部特征，同时将风格转换为霓虹赛博朋克水彩融合插画。它指定了冷色调配色方案、戏剧性的轮廓光，并将精细的素描线条与水彩晕染效果融合，背景为黑暗的夜间城市。

![霓虹赛博朋克水彩融合插画提示](https://cms-assets.youmind.com/media/1768544789043_s3x9cs_G-uhkTPbQAc7Gq-.jpg)
![霓虹赛博朋克水彩融合插画提示](https://cms-assets.youmind.com/media/1768544789166_stltjp_G-uhkRpbQAA62gN.jpg)

```
{
  "prompt": "Use the uploaded reference image to **preserve 100% of the facial features, identity, age, skin tone, and expression** of the person. Do not change facial proportions. Create a **neon cyberpunk watercolor fusion illustration**: face painted softly in watercolor while surrounded by glowing neon light effects. Hair follows the exact reference style with subtle luminous highlights. Clothing: futuristic urban attire (sleek jacket, metallic or holographic fabric accents) rendered with painterly strokes. Background: dark night city with glowing neon signs, holograms, light streaks, digital rain, and watercolor splashes blending into a cyberpunk skyline. Cool color palette of electric blue, magenta, violet, and teal. Dramatic rim lighting around the silhouette, soft glow on skin, fine sketch lines mixed with watercolor bleeds. High-detail, cinematic, artistic, futuristic masterpiece quality.",
  "negative_prompt": "blurry, low quality, deformed, extra limbs, bad anatomy, watermark, text overlay, anime, cartoon, overexposed, underexposed, ugly face, bad hands, face altered, identity changed, flat colors, plastic skin, harsh outlines",
  "parameters": {
    "steps": 50,
    "cfg_scale": 7.2,
    "sampler": "Euler a or DPM++ 2M Karras",
    "strength": 0.53,
    "noise": 0.28,
    "width": 832,
    "height": 1216,
    "aspect_ratio": "2:3"
  },
  "usage_instructions": "Upload your image in img2img or reference mode. Keep strength around 0.5–0.55 for **perfect face matching** while transforming the scene into a neon cyberpunk watercolor world."
}
```

[[Identity Preservation]] [[Cool Color Palette]]

---

### 197. 巴黎咖啡馆写实肖像画，带身份锁

**Author**: [Dr. Samia](https://x.com/oye_samia)  **Date**: 2026-01-15  **Language**: en

> 一个高度结构化的提示，用于生成一张在巴黎咖啡馆 (CARETTE) 拍摄的时尚女性的超逼真、高分辨率肖像，强调严格保留参考图像中的身份，指定服装（白色粗花呢西装外套），以及柔和的自然光线。

![巴黎咖啡馆写实肖像画，带身份锁](https://cms-assets.youmind.com/media/1768544812282_2p8qek_G-rgN1yaUAAg9oe.jpg)

```
{
  "type": "image_generation_prompt",
  "aspect_ratio": "9:16",
  "style": "realistic lifestyle portrait, European café editorial",
  "quality": {
    "resolution": "high-resolution, large format",
    "realism": "photorealistic",
    "detail_level": "sharp, ultra-detailed"
  },
  "identity_preservation": {
    "use_reference_image": true,
    "strict_identity_lock": true,
    "alter_face": false,
 },
  "subject": {
    "gender": "female",
    "ethnicity_style": "European",
    "body_type": "slim figure",
    "pose": {
      "position": "sitting at an outdoor café table",
      "angle": "slightly angled toward the camera",
      "hands": "holding a white cup naturally"
    },
    "expression": "calm, stylish, confident",
    "appearance": {
      "hair": "natural styling as in reference image",
      "accessories": [
        "white cat-eye sunglasses resting on top of her head",
        "gold wristwatch on left wrist"
      ]
    },
    "wardrobe": {
      "outerwear": "{argument name="outerwear type" default="white tweed blazer"}",
      "details": [
        "gold buttons on the front",
        "gold buttons on the sleeves"
      ],
      "style": "elegant, classic Parisian chic"
    }
  },
  "props": {
    "table_items": [
      "white coffee cup",
      "silver teapot",
      "glass of water",
      "croissant",
      "dessert cup topped with a large swirl of whipped cream"
    ]
  },
  "environment": {
    "location": "outdoor café patio",
    "cafe_name": "{argument name="cafe name" default="CARETTE"}",
    "background": {
      "scene": "busy café terrace with patrons seated at tables",
      "architecture": "classic Parisian buildings"
    },
    "atmosphere": "lively yet elegant European café setting"
  },
  "lighting": {
    "type": "natural daylight",
    "quality": "soft, flattering, realistic",
    "effect": "enhances skin texture and fabric detail without harsh shadows"
  },
  "camera": {
    "shot_type": "portrait",
    "framing": "medium portrait",
    "angle": "eye-level",
    "depth_of_field": "moderate with softly blurred background"
  },
  "constraints": [
    "Do not change or retouch the face",
    "No artificial filters or glam effects",
    "No distorted anatomy",
    "No text overlays or watermarks"
  ],
  "output_goal": "Create a realistic, high-resolution 9:16 portrait of a stylish European woman sitting at an outdoor Parisian café table, using the user’s face with 100% accuracy, featuring elegant fashion, café details, and a lively yet refined CARETTE café atmosphere."
}
```

[[Identity Preservation]] [[Fashion Editorial]] [[Soft Natural Light]] [[High Resolution Portrait]]

---

### 198. 巴黎咖啡馆专题肖像与身份锁定

**Author**: [Dr. Samia](https://x.com/oye_samia)  **Date**: 2026-01-15  **Language**: en

> 一个高度结构化的提示，用于生成一张在巴黎户外咖啡馆 (CARETTE) 的女性逼真高分辨率肖像。至关重要的是，它包含严格的身份保留约束，确保生成的图像 100% 准确地使用用户的面部，同时应用优雅、经典的巴黎时尚风格。

```
{
  "type": "image_generation_prompt",
  "aspect_ratio": "9:16",
  "style": "realistic lifestyle portrait, European café editorial",
  "quality": {
    "resolution": "high-resolution, large format",
    "realism": "photorealistic",
    "detail_level": "sharp, ultra-detailed"
  },
  "identity_preservation": {
    "use_reference_image": true,
    "strict_identity_lock": true,
    "alter_face": false,
 },
  "subject": {
    "gender": "female",
    "ethnicity_style": "European",
    "body_type": "slim figure",
    "pose": {
      "position": "sitting at an outdoor café table",
      "angle": "slightly angled toward the camera",
      "hands": "holding a white cup naturally"
    },
    "expression": "calm, stylish, confident",
    "appearance": {
      "hair": "natural styling as in reference image",
      "accessories": [
        "white cat-eye sunglasses resting on top of her head",
        "gold wristwatch on left wrist"
      ]
    },
    "wardrobe": {
      "outerwear": "white tweed blazer",
      "details": [
        "gold buttons on the front",
        "gold buttons on the sleeves"
      ],
      "style": "elegant, classic Parisian chic"
    }
  },
  "props": {
    "table_items": [
      "white coffee cup",
      "silver teapot",
      "glass of water",
      "croissant",
      "dessert cup topped with a large swirl of whipped cream"
    ]
  },
  "environment": {
    "location": "outdoor café patio",
    "cafe_name": "{argument name="cafe name" default="CARETTE"}",
    "background": {
      "scene": "busy café terrace with patrons seated at tables",
      "architecture": "classic Parisian buildings"
    },
    "atmosphere": "lively yet elegant European café setting"
  },
  "lighting": {
    "type": "natural daylight",
    "quality": "soft, flattering, realistic",
    "effect": "enhances skin texture and fabric detail without harsh shadows"
  },
  "camera": {
    "shot_type": "portrait",
    "framing": "medium portrait",
    "angle": "eye-level",
    "depth_of_field": "moderate with softly blurred background"
  },
  "constraints": [
    "Do not change or retouch the face",
    "No artificial filters or glam effects",
    "No distorted anatomy",
    "No text overlays or watermarks"
  ],
  "output_goal": "Create a realistic, high-resolution 9:16 portrait of a stylish European woman sitting at an outdoor Parisian café table, using the user’s face with 100% accuracy, featuring elegant fashion, café details, and a lively yet refined CARETTE café atmosphere."
}
```

[[Identity Preservation]] [[High Resolution Portrait]]

---

### 199. 专业商务肖像生成提示

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-01-15  **Language**: en

> 一个根据上传图片生成超逼真专业商务肖像的提示，确保面部特征准确，并为拍摄对象设计现代行政服装，背景为柔和、高级的渐变色。

![专业商务肖像生成提示](https://cms-assets.youmind.com/media/1768544809121_q3i5no_G-rTvOvbQAUBSak.jpg)
![专业商务肖像生成提示](https://cms-assets.youmind.com/media/1768544809262_46w6lc_G-rTvOTaEAAffRS.jpg)

```
Ultra realistic professional business portrait based on the attached image. Keep the subject’s facial structure, skin tone, hairstyle, and expression accurate. Dress the subject in clean, modern professional attire suitable for executives. Use a soft, minimal, premium gradient background with smooth lighting transitions
```

[[Identity Preservation]] [[Gradient Background]]

---

### 200. 超逼真伊布 Cosplay 肖像

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-15  **Language**: en

> 一个用于生成超逼真肖像的提示，描绘了一位穿着伊布 (Eevee) 角色扮演服装的年轻女性，表情俏皮而调皮（吐舌、眨眼）。它详细说明了服装、发型和妆容，要求高分辨率和逼真的皮肤/织物纹理，同时还要求使用参考图像中的面部。

![超逼真伊布 Cosplay 肖像](https://cms-assets.youmind.com/media/1768544861406_zzgox2_G-rJCyQbMAACFuz.jpg)
![超逼真伊布 Cosplay 肖像](https://cms-assets.youmind.com/media/1768544861385_h2ebdm_G-rJC0iaQAAQs2n.jpg)

```
{
  "prompt": "ultra photorealistic portrait of a beautiful young western woman, 20-23 years old, flawless smooth skin, natural makeup with soft pink blush, wearing full Eevee cosplay outfit, bright brown Eevee-themed cropped tank top with big Eevee face print (blue eyes, red cheeks, cute smiling mouth), brown Eevee plush hooded onesie hood with long black-tipped Eevee ears hanging down, fluffy brown Eevee paw gloves, bright brown high-waisted short shorts, blonde straight bangs with bob haircut, playful and cute expression, sticking out tongue, winking with one eye, head slightly tilted, cheerful and mischievous mood, vibrant solid bright brown studio background, professional studio photography, sharp focus, highly detailed skin texture, realistic fabric texture, soft even lighting, cinematic color grading, 8k resolution",
  "negative_prompt": "cartoon, anime, drawing, illustration, 3d render, low quality, blurry, deformed, bad anatomy, extra limbs, bad hands, poorly drawn face, bad proportions, watermark, text, logo, signature, overexposed, underexposed, plastic skin, doll, uncanny valley",
  "parameters": {
    "aspect_ratio": "3:4",
    "style": "photorealistic",
    "lighting": "soft studio lighting, even illumination",
    "quality": "ultra detailed, 8k, masterpiece",
    "model_version": "realistic",
    "steps": 40,
    "cfg_scale": 7.5,
    "sampler": "dpm++ 2m karras or euler a",
    "seed": -1
  },
  "character_details": {
    "age": "young adult female",
    "ethnicity": "East Asian (Korean/Japanese aesthetic)",
    "hair": "jet black, straight bob cut with full bangs",
    "eyes": "large, expressive, dark brown, playful wink",
    "expression": "cheerful, mischievous, tongue out, one eye winking",
    "body_type": "slim, toned, visible midriff, flat stomach"
  },
  "clothing_details": {
    "top": "yellow cropped tank top, Pikachu face print (big black eyes, red cheeks, smiling mouth)",
    "hood": "oversized plush Pikachu hood, long black-tipped ears hanging down both sides",
    "gloves": "yellow plush Pikachu paw mittens with black tips",
    "bottom": "bright yellow high-waisted short shorts, sporty style",
    "colors": "dominant vivid pokemon yellow, black accents, red cheek circles"
  }
}
```

[[Identity Preservation]] [[Playful Expression]] [[Cosplay Photography]]

---

# Chunk 046

Total: 200 prompts

### 1. Barbiecore 巴黎·希尔顿 街头风格 (JSON 格式)

**Author**: [bengi](https://x.com/p3rikly)  **Date**: 2026-01-25  **Language**: en

> 一个详细的 JSON 提示，用于生成一张高饱和度、具有“芭比风”的图像，内容是 {argument name="celebrity" default="Paris Hilton"} 身穿粉色两件套服装，置身于阳光普照的比弗利山庄街道上。该提示指定了高角度拍摄、9:16 的垂直长宽比，以及将主体缩短并使背景扁平化的技术指令，以强调强烈阳光和锐利阴影。

![Barbiecore 巴黎·希尔顿 街头风格 (JSON 格式)](https://cms-assets.youmind.com/media/1769408688397_023xxr_G_ipusjXEAA2K9p.jpg)

```
{
  "image_generation_parameters": {
    "subject": {
      "description": "{argument name="celebrity" default="Paris Hilton"} with long wavy hair",
      "attire": "Pink two-piece outfit consisting of a bustier crop top and a pleated mini skirt",
      "accessories": ["White retro cat-eye sunglasses", "Small pink woven handbag"],
      "pose": "Standing beside a car, smiling upward, one hand near her face and the other holding a bag"
    },
    "environment": {
      "setting": "Sun-drenched Beverly Hills style street",
      "background_elements": ["Tall palm trees lining a residential road", "Clear blue sky", "Green hedges"],
      "prop": "Pink vintage convertible car with detailed interior and chrome steering wheel"
    },
    "cinematography": {
      "camera_angle": "High-angle shot (looking down from above)",
      "framing": "Medium Close-Up (MCU) focusing on head, torso, and top of the car",
      "aspect_ratio": "9:16 (Vertical)",
      "lens_effect": "Standard 50mm focal length to minimize distortion while emphasizing height"
    },
    "lighting_and_color": {
      "aesthetic": "Vibrant, high-saturation, 'Barbiecore' aesthetic",
      "lighting": "Hard, direct sunlight creating sharp shadows on the asphalt road",
      "primary_palette": ["Bubblegum Pink", "Bright White", "Asphalt Gray", "Palm Green"]
    },
    "technical_directive": "Re-render the original scene with a dramatic perspective shift. Foreshorten the subject's body to show visual dominance from the high-angle position. Ensure the car's pink dashboard and the road surface appear flattened beneath the subject."
  }
}
```

[[High Angle Shot]] [[9:16 Vertical Format]]

---

### 2. 私密低光卧室肖像

**Author**: [Stark](https://x.com/katmanai)  **Date**: 2026-01-25  **Language**: en

> 一个高度详细的 JSON 格式提示，用于生成一张年轻女性在卧室环境中的私密、低光肖像，强调特定的灯光、服装和复古胶片美学。

![私密低光卧室肖像](https://cms-assets.youmind.com/media/1769495346516_zr4saa_G_inGlcWQAAKGYs.jpg)

```
{
  "main_prompt": "intimate low-light bedroom portrait of a stunning young woman in her early 20s with fair skin and natural dewy glow, long voluminous wavy platinum blonde hair cascading over shoulders, subtle makeup with winged eyeliner, long lashes, glossy soft pink lips in gentle pout, dreamy half-lidded eyes looking at camera, wearing light pink ruffled satin babydoll set with thin straps and short shorts, posing lying on stomach on bed propped on elbows, soft warm bedside lamp light + cool moonlight mix creating golden rim light on hair and face, cozy dark blue bedding and plushies in background, vintage film aesthetic with light grain and warm cast, photorealistic, ultra-detailed hair and satin texture --ar 3:4 --stylize 250 --v 6 --q 2",
  "negative_prompt": "blurry, deformed, extra limbs, bad anatomy, ugly, overexposed, harsh shadows, pale skin, heavy makeup, smiling, bright daylight, synthetic look, no grain",
  "style_tags": ["photorealistic", "cozy bedroom vibe", "pink satin babydoll", "vintage film grain", "dreamy intimate mood"],
  "technical": {
    "aspect_ratio": "3:4",
    "lighting": "warm lamp + cool moonlight rim light",
    "camera": "iPhone night mode portrait"
  },
  "extra_parameters": {
    "recommended_model": "Flux.1 [dev]",
    "guidance_scale": "7.5",
    "steps": "40",
    "image_reference": "use uploaded reference image for exact pose, hair volume, expression, outfit details and nighttime bedroom lighting"
  }
}
```

[[Bedroom Setting]] [[Intimate Atmosphere]] [[Vintage Film Aesthetic]]

---

### 3. 极简主义客厅中的时尚编辑摄影

**Author**: [Emma](https://x.com/emmagpt0)  **Date**: 2026-01-25  **Language**: en

> 一个高度详细、照片般逼真的图像生成提示，用于创建一张女性跪在现代简约客厅中的时尚编辑照片，其中指定了相机设置、灯光、服装（绿松石色短款上衣和白色低腰短裤）和环境细节。

![极简主义客厅中的时尚编辑摄影](https://cms-assets.youmind.com/media/1769408668591_7ealhz_G_iZRbLXwAAqnNK.jpg)
![极简主义客厅中的时尚编辑摄影](https://cms-assets.youmind.com/media/1769408668742_p9o6mn_G_iZRbCXsAAmgVC.jpg)

```
{
  "description": "An adult woman kneeling on a soft dark cushion in a modern minimalist living room, leaning slightly forward with hands resting on her knees. She is wearing a {argument name="top color" default="turquoise"} short-sleeve cropped zip-up top with a deep neckline and white low-rise shorts. The environment features white walls, light hardwood flooring, a modern abstract painting, a black leather sofa, a glass coffee table, and contemporary sculptures. Natural daylight from large windows creates a bright, editorial fashion photography atmosphere with soft shadows and high realism.",
  
  "face_reference": "Use uploaded reference image for face only, do not modify facial structure or identity.",
  
  "camera": {
    "type": "professional DSLR camera",
    "angle": "eye-level slightly high angle",
    "framing": "upper body to knees portrait",
    "lens": "35mm-50mm equivalent",
    "depth_of_field": "shallow, background softly blurred"
  },
  
  "lighting": {
    "type": "natural daylight with indoor ambient light",
    "mood": "bright, clean, editorial studio style",
    "shadows": "soft shadows, no harsh contrast"
  },
  
  "clothing": {
    "top": {
      "type": "short sleeve cropped zip-up top",
      "color": "turquoise blue",
      "fit": "tight slim fit",
      "detail": "deep neckline zipper"
    },
    "bottom": {
      "type": "shorts",
      "color": "white",
      "material": "denim or cotton",
      "fit": "low-rise mini shorts"
    }
  },
  
  "hair": {
    "color": "honey blonde / light brown",
    "style": "shoulder length, slightly wavy, voluminous"
  },
  
  "environment": {
    "location": "modern minimalist living room",
    "floor": "light hardwood floor",
    "walls": "white",
    "furniture": [
      "black leather sofa",
      "glass coffee table"
    ],
    "props": [
      "abstract wall painting",
      "modern sculpture",
      "arched window"
    ]
  },
  
  "style": {
    "genre": "fashion editorial photography",
    "realism": "photorealistic",
    "quality": "ultra high resolution, 8k detail",
    "sharpness": "high",
    "noise": "low"
  },
  
  "negative_prompt": [
    "face modification",
    "blurry",
    "low resolution",
    "extra limbs",
    "distorted anatomy",
    "cartoon",
    "anime",
    "overexposed",
    "harsh shadows",
    "unrealistic body proportions"
  ]
}
```

[[Photorealistic Photography]] [[Modern Minimalist Interior]]

---

### 4. 微妙的品牌纹理视觉提示

**Author**: [SRKDAN](https://x.com/SRKDAN)  **Date**: 2026-01-25  **Language**: en

> 一个简洁的提示，用于生成微妙的品牌纹理视觉。它侧重于精细的材质触感、柔和的灯光、中性色调和最小的图案重复，旨在增加深度，同时不分散对主要内容的注意力。

![微妙的品牌纹理视觉提示](https://cms-assets.youmind.com/media/1769408693803_cwrtxw_G_dJLRsXcAEhlXw.jpg)

```
Subtle brand texture visual.
Fine-grain material feel, soft lighting,
neutral tones,
minimal pattern repetition,
designed to add depth without distraction,
refined and understated aesthetic.
```

[[Soft Lighting]] [[Brand Identity Design]] [[Neutral Color Palette]]

---

### 5. 舒适冬季时尚肖像 (JSON 格式)

**Author**: [bengi](https://x.com/p3rikly)  **Date**: 2026-01-25  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张逼真的、高保真度的图像，内容是 {argument name="subject name" default="Ana de Armas"} 穿着舒适、自信的冬季时尚服装。主体以深蹲姿势置身于雪林中，身着明亮、对比鲜明的人造毛皮服装（黄色耳罩、紫红色夹克、橙色打底裤）和厚实的粉色 Moon Boots。重点在于强烈的材质纹理和低视角的相机角度。

![舒适冬季时尚肖像 (JSON 格式)](https://cms-assets.youmind.com/media/1769495432202_qw23am_G_iMtdcWUAAg57a.jpg)

```
{
  "subject": {
    "desc": "Ana de Armas, fit curvaceous hourglass figure, long wavy dirty blonde hair, natural tanned skin with visible texture",
    "apparel": {
      "headwear": "Large fluffy yellow faux-fur earmuffs",
      "upper": "Short cropped light fuchsia faux-fur jacket ending at waist",
      "lower": "Tight heather electric orange matte cotton-spandex leggings, natural stretch and tension",
      "footwear": "Chunky pink knee-high Moon Boot-style snow boots with white laces and branding"
    }
  },
  "pose": {
    "type": "Deep squat/crouch, rear 3/4 view, back and glutes prominent",
    "head": "Turned sharply over right shoulder, direct calm engaging eye contact",
    "limbs": "Legs deeply bent, boots planted in snow, arms relaxed on knees (partially obscured)",
    "expression": "Neutral to slight smile, relaxed confident gaze"
  },
  "environment": {
    "setting": "Dense winter forest, heavy powdery snow, tall snow-laden evergreen trees",
    "ground": "Thick snow with footprints and disturbed texture around boots"
  },
  "camera": {
    "lens": "50-85mm portrait",
    "angle": "Low, eye-level with crouching subject",
    "dof": "Moderate (f/4-5.6), razor-sharp subject, slightly softened background trees",
    "focus": "Sharp on face and eyes"
  },
  "lighting": "Soft diffused overcast daylight, even shadowless, snow as natural reflector, subtle highlights on fur",
  "style": "Photorealistic candid high-fidelity, natural color grading, strong material textures (fur, fabric, snow, boots)",
  "aspect_ratio": "3:4 vertical",
  "quality": "8K UHD, clean ISO 100-200, high sharpness on subject",
  "vibe": "Cozy winter fashion, calm confident alluring snow bunny aesthetic"
}
```

[[Low Camera Angle]]

---

### 6. 复杂插画提示：月球骑行

**Author**: [H. Sakai](https://x.com/FoD5_2020)  **Date**: 2026-01-25  **Language**: ja

> 这是一个给 nano banana 的复杂图像生成提示，要求以“Irasutoya”的风格绘制一幅插图，描绘一个人穿着密封服、背着氧气罐，在月球表面骑公路自行车。用户对 AI 精准描绘自行车机械结构的能力印象深刻。

![复杂插画提示：月球骑行](https://cms-assets.youmind.com/media/1769408684082_ebbztb_G_iICBhb0AAJx67.png)

```
気密服を着て酸素ボンベを背負い、月面をロードバイクでは知る人をいらすと屋風に
```

[[Moon Surface Bicycle Riding Irasutoya Illustration]]

---

### 7. 现代厨房中女性烹饪的抓拍

**Author**: [Ivanna Humeniuk](https://x.com/ivanka_humeniuk)  **Date**: 2026-01-25  **Language**: en

> 一个 JSON 提示，用于生成一张女性在现代白色厨房里烹饪的真实背影照片。该提示侧重于居家舒适感，详细说明了服装（米色休闲套装）、环境（地铁砖、嵌入式电器）和灯光（冷色 LED 灯带与环境光混合）。

![现代厨房中女性烹饪的抓拍](https://cms-assets.youmind.com/media/1769408708764_0mh6oq_G_iES5gXsAA83s9.jpg)

```
{
  "image": {
    "main_description": "A cozy, candid shot from behind of a woman standing in a modern kitchen, cooking food in a pan on the stove while wearing a comfortable lounge set.",
    "characters": {
      "main_reference_character": {
        "identity_anchor": "The character based on the provided reference photo, preserving strictly the user's identity source.",
        "ethnicity_and_phenotype": "Determined by the user provided reference photo.",
        "face_and_skin": "Face is turned away from the camera and obscured by hair; skin tone consistent with reference.",
        "expression": "Not visible, but body language suggests focus on the task.",
        "hair": "Hair worn loose in a natural, slightly messy everyday style, falling down the back and partially obscuring the face profile.",
        "body_and_pose": "Standing rear-view/three-quarter angle, facing the stove. One hand is holding the handle of a frying pan, the other holds a spatula stirring food.",
        "outfit": "A matching {argument name="outfit color" default="cream or light beige"} lounge set made of a semi-sheer, textured knit or linen fabric. The top is loose with wide, bell-shaped long sleeves. The bottom consists of matching loose-fitting pants."
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
      "location": "A clean, modern white kitchen.",
      "elements": "White cabinetry with black vertical handles, white subway tile backsplash, a built-in microwave, an induction stovetop with a pan containing {argument name="food item" default="pasta or vegetables"}, a white oven with a digital display, and a vase with evergreen/pine branches on the counter.",
      "atmosphere": "Homey, domestic, calm, evening or indoor setting."
    },
    "cinematography": {
      "lighting_setup": "Cool white under-cabinet LED strip lighting illuminating the backsplash and counter, mixed with general room ambient light.",
      "color_grading": "Natural, slightly cool tones from the LEDs contrasting with the warm beige of the outfit.",
      "shadows_and_highlights": "Soft diffusion, highlights on the subway tiles and the hair.",
      "reflections": "Subtle reflections on the glossy tile backsplash and stovetop."
    },
    "camera_and_tech": {
      "framing": "Medium shot from behind, capturing the subject from the waist up to the head, showing the kitchen context.",
      "optics": "Standard focal length (approx 35mm or 50mm), reasonably deep depth of field keeping both the person and the kitchen details in focus.",
      "visual_fidelity": "Realistic, candid smartphone photography style."
    },
    "style_and_mood": {
      "aesthetic": "Lifestyle, 'slow living', domestic comfort, casual.",
      "emotional_vibe": "Relaxed, intimate, everyday life."
    },
    "aspect_ratio": "3:4"
  }
}
```

[[Back View Portrait]]

---

### 8. 乐高山洪救援场景提示

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-25  **Language**: en

> 一个用于生成乐高山村灾难场景的戏剧性电影级图像的提示。场景包括倾盆大雨、河流泛滥、乐高消防员使用救援船和绳索、斜坡上的房屋以及背景中的薄雾山脉，强调强烈的真实感和戏剧性的光线。

![乐高山洪救援场景提示](https://cms-assets.youmind.com/media/1769408657745_qrgt94_G_hyJtRbIAELZNz.jpg)

```
LEGO mountain flood rescue scene, torrential rain causing river overflow in a LEGO mountain village, rescue boats and ropes used by LEGO firefighters, houses perched on slopes surrounded by muddy floodwater, misty mountains in background, dramatic cinematic lighting, intense LEGO disaster realism --ar 3:4
```

[[Cinematic Diorama]]

---

### 9. Margaret Qualley 高级定制红色皮革时尚大片提示

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-01-25  **Language**: en

> 一个高度详细、照片级的提示，用于生成一张玛格丽特·库里（Margaret Qualley）的高级时装编辑图片。主体姿态专注，嘴唇间叼着一根细长的红色茎，身穿一件鲜艳的红色皮革无肩带迷你连衣裙，背景是匹配的红色摄影棚。该提示强调超高细节、逼真的皮肤纹理和精确的摄影棚灯光，以实现光泽、单色的红色美学效果。

![Margaret Qualley 高级定制红色皮革时尚大片提示](https://cms-assets.youmind.com/media/1769495433031_e6ls54_G_hnrSmWYAA3LOU.jpg)

```
{
  "subject": {
    "appearance": {
      “character”: “{argument name="character name" default="Margaret Qualley"}”,
      "gender": "Female",
      "age_range": "Young adult",
      "hair": "Long, dark brown, wavy, parted slightly off-center, with individual strands, flyaways, and realistic texture visible.",
      "eyes": "Light blue, striking intensity, with detailed iris structure, capillaries, and moisture catchlights.",
      "skin_tone": "Fair, porcelain, with visible pores, fine lines, natural imperfections, and realistic subsurface scattering.",
      "makeup": "Natural but polished, soft pink lip with fine texture, defined lashes, subtle contouring."
    },
    "pose": {
      "stance": "Standing facing forward",
      "hand_position": "Right hand raised to chin/mouth area, fingers gently curled, showing skin texture and veins.",
      "action": "Holding a thin red stem (likely a cherry stem) between lips/teeth, showing moisture and pressure.",
      "gaze": "Direct eye contact with the camera, alluring and intense."
    }
  },
  "attire": {
    "clothing": "Strapless mini dress",
    "material": "{argument name="clothing material" default="Red leather"} or faux leather, slight sheen, with detailed grain, natural creases, imperfections, and stretching around curves.",
    "design": "Layered bandage style, horizontal panels, structured pleats, form-fitting silhouette, with visible stitching and seam details.",
    "color": "Vibrant red"
  },
  "accessories": {
    "jewelry": [
      "Silver stud earrings with crystal accents, showing facets, light refraction, and metal texture.",
      "Large statement ring with black and silver detailing on right ring finger, with realistic material contrast and wear."
    ],
    "nails": "Manicured with red polish matching the dress, showing glossy finish and cuticle details."
  },
  "environment": {
    "background": "Solid {argument name="background color" default="vibrant red"} studio backdrop, with subtle surface texture, minor imperfections, and realistic light fall-off.",
    "props": "None visible other than the small stem in mouth"
  },
  "lighting": {
    "type": "Studio lighting",
    "quality": "Soft but directional, creating realistic highlights, deep shadows, and accurate volume.",
    "shadows": "Subtle soft shadows behind the subject, anchored to the floor, showing accurate density and color bleeding.",
    "highlights": "Specular highlights on the leather dress, lips, eyes, and jewelry, showing light source reflections."
  },
  "technical_details": {
    "camera_angle": "Eye level",
    "shot_size": "Medium shot (thighs up)",
    "style": "High-fashion editorial, glossy magazine aesthetic, with ultra-high detail and fidelity.",
    "resolution": "8k, RAW file quality, with natural film grain, sharp focus, and photorealistic rendering.",
    "color_palette": "Monochromatic red theme with skin tone contrast, realistic color rendering and gradients."
  }
}
```

[[Celebrity Fashion Editorial]]

---

### 10. 酷炫调色板，大胆能量，广阔视角

**Author**: [Banana Prompts](https://x.com/bananaprompts)  **Date**: 2026-01-25  **Language**: en

> 一个简短、描述性的提示，侧重于冷色调、大胆的能量、广角、锐利的阴影和简洁的线条，用于图像生成。

![酷炫调色板，大胆能量，广阔视角](https://cms-assets.youmind.com/media/1769408712703_q4rb3t_G_hj4pZWUAAyX2k.jpg)

```
Stepping into a cooler palette, same bold energy. 💙
Wide angles, sharp shadows, clean lines.
```

[[Wide Angle Photography]]

---

### 11. 覆盖着青草和雏菊的超现实人形肖像

**Author**: [Adam 🌿 Unroot.design](https://x.com/unrootdesign)  **Date**: 2026-01-25  **Language**: en

> 一个详细的提示，用于生成一张超现实、照片级的肖像，描绘一个完全被新鲜绿草和白色雏菊覆盖的类人生物，强调自然与人类的融合。该人物穿着一件现代橙色夹克，背景是简约的柔和色调，需要一张人物基础的参考图片。

![覆盖着青草和雏菊的超现实人形肖像](https://cms-assets.youmind.com/media/1769408686263_a6h8on_G_g-aaGWAAAfOJJ.jpg)

```
A surreal portrait of a humanoid figure completely covered in fresh green grass and small white daisies with yellow centers; the flowers densely encircle the face and neck, obscuring facial features. The flowers are clearly visible, do not overlap, and appear natural, like a flower meadow. The figure is dressed in a modern {argument name="jacket color" default="orange"} jacket (shades of orange, tangerine, and warm amber), slightly glossy fabric, and an orange or cream baseball cap without inscriptions. A minimalist, clean background in soft beige or white pastel tones. The background is clean and empty. Key features: natural daylight, strong depth of field, ultra-detailed textures, photorealistic yet artistic, cinematic composition, high resolution, vibrant shadows, fashion photoshoot style, fusion of nature and humanity, calm and poetic mood.
```

[[Surrealism]] [[Photorealism]] [[Minimalist Background]]

---

### 12. 趣味商业摄影：吊起 Cybertruck

**Author**: [ailabs.zone](https://x.com/zhoumeng780)  **Date**: 2026-01-25  **Language**: en

> 一个用于生成有趣、超现实商业摄影的提示，其中主体（基于上传的面部图像）正用双手戏剧性地举起一辆巨大的 {argument name="vehicle" default="Tesla Cybertruck"}。图像应采用时尚杂志编辑风格、高调影棚布光，并使用广角低视角来强调产品的尺寸。

![趣味商业摄影：吊起 Cybertruck](https://cms-assets.youmind.com/media/1769408691076_nrt4sp_G_g6swSaQAEn3dW.jpg)

```
using the uploaded face image as the exact facial reference,He lifted a giant {argument name="vehicle" default="Tesla Cybertruck"} with both hands, Highlight the large size of the product,playful fun energy, fashion editorial styling, clean minimal background, high key studio lighting, crisp soft shadow, ultra realistic commercial photography, wide angle low perspective, sharp focus, 8k
```

[[Fashion Magazine Style]]

---

### 13. 后视浴室镜面反射肖像

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-01-25  **Language**: en

> 一个高度具体的 JSON 提示，用于生成一张复杂的图像，描绘一位女士在豪华浴室中，利用镜面反射同时展现她的背部轮廓（在前景中）和正面轮廓（在反射中）。该提示严格执行解剖学约束，详细描述了服装（白色罗纹家居服），并描述了环境（黑色大理石、斑马纹梳妆台）。

![后视浴室镜面反射肖像](https://cms-assets.youmind.com/media/1769408711123_yrnv2u_G_g1QSaXUAAWlg-.jpg)

```
{
"subject": {
"description": "Young adult female with a fit, curvy physique and tanned skin. She has long, wavy, highlighted blonde hair cascading down her back. Facial features are defined with arched eyebrows, full lips, and a neutral, sultry expression.",
"attire": "A matching {argument name="attire color" default="white"} ribbed loungewear set consisting of a crop top bralette with thin spaghetti straps and high-waisted, tight-fitting boy shorts. The fabric texture is clearly visible vertical ribbing.",
"anatomy_constraints": "Preserve exact body proportions. Emphasize the curvature of the lower back and fullness of the glutes in the foreground. In the mirror reflection, the bust must appear full and naturally shaped, maintaining the volume seen in the reference without reduction or flattening. Skin texture must be realistic with natural pores and slight shine."
},
"pose": {
"orientation": "Three-quarter rear view, standing.",
"action": "The subject is twisting her torso to the left to look back over her left shoulder directly at the viewer. Her body is angled away from the camera.",
"limbs": "Her right arm is extended forward, with her hand resting flat on the vanity countertop, fingers slightly splayed. Her left arm is down by her side, partially obscured. Her legs are standing straight, weight slightly shifted to accentuate the hip curve.",
"head": "Turned left, chin slightly tucked, gaze locked on the camera lens.",
"reflection_pose": "The large mirror in front of her reflects her front profile, showing her face, chest, and anterior torso clearly."
},
"environment": {
"setting": "Luxury hotel or residential bathroom.",
"surrounds": "Dark black marble walls with white veining. To the right, a glass shower enclosure with chrome fixtures. In the foreground, a vanity countertop with a bold, black-and-white zebra stripe pattern.",
"props": "On the zebra counter: a wooden paddle hairbrush, a pair of dark sunglasses, several white toiletries bottles, a glass tumbler, and a small black tray. A chrome faucet is visible on the left.",
"background": "The reflection in the mirror shows the continuation of the dark marble bathroom and the subject's front."
},
"camera": {
"shot_type": "Medium shot, from slightly above waist level.",
"perspective": "Third-person perspective (not a selfie). The camera is positioned behind and to the side of the subject.",
"focal_length": "35mm to 50mm, creating a natural field of view without extreme distortion.",
"depth_of_field": "Deep depth of field, keeping both the subject in the foreground and the reflection in the mirror in sharp focus.",
"framing": "Framed to include the subject from mid-thigh up, capturing the vanity counter and the mirror reflection."
},
"lighting": {
"source": "Indoor artificial bathroom lighting.",
"type": "Overhead recessed downlights emitting a warm-neutral tone.",
"effects": "Soft specular highlights on the subject's shoulder, hair, and the marble surfaces. Realistic shadows cast by the objects on the counter."
}
}
```

[[Luxury Interior]]

---

### 14. 热带丛林中的幽默猴子自拍

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-25  **Language**: en

> 一个详细的、照片级的提示，用于生成一张幽默的、广角的热带森林旅行自拍。它使用严格的面部身份锁定，并要求一只猕猴占据前景，看起来像是在自拍，表情惊讶，而一名女子则在背景中大笑，营造出一种抓拍的、超广角智能手机美学。

![热带丛林中的幽默猴子自拍](https://cms-assets.youmind.com/media/1769408671006_mk44vc_G_g0usDXsAAezQ8.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_travel_selfie_wide_angle_comedy",
      "version": "v1.0_MONKEY_SELFIE_JUNGLE_PATH_FACELOCK_SAFE_EN",
      "priority": "highest",
      "language": "en"
    },

    "references": {
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "STYLE_COMPOSITION_POSE_LIGHTING_ANCHOR",
        "strict_lock": true,
        "preserve_pose": true,
        "preserve_composition": true,
        "preserve_lighting": true,
        "preserve_vibe": true,
        "preserve_palette": true
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
      "aspect_ratio": "9:16",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "cinematic_photoreal_candid",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle",
      "color_grade": "natural_daylight_warm_green",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },

    "creative_prompt": {
      "scene_summary": "Create a photoreal travel selfie in a lush tropical forest. Setting: a narrow outdoor walkway/path with wet ground, dense green foliage, tall trees, and a humid jungle atmosphere.\n\nForeground: a macaque monkey extremely close to the camera lens, dominating the frame with a humorous wide-angle distortion. The monkey’s arm reaches forward as if it is taking the selfie. The monkey mouth is open in a funny surprised expression. Realistic fur detail, natural anatomy, no deformation.\n\nBackground: one adult woman behind the monkey, laughing with an open-mouth smile, both hands raised doing a double peace sign. Natural candid joy. Hair in a casual updo with soft bangs framing the face. Light summer outfit ({argument name="outfit color" default="white"} dress or top), minimal jewelry. One wrist has a simple yellow wristband (no readable text).\n\nCinematography: smartphone ultra-wide selfie look (14mm equivalent), close perspective, mild lens distortion, natural daylight, soft shadows, realistic skin texture, no heavy retouch, no beauty filter. Keep it fun and spontaneous, high realis"
```

[[Candid Snapshot]] [[Wide Angle Selfie]]

---

### 15. 优雅的安娜·德·阿玛斯名人肖像 (JSON 格式)

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2026-01-25  **Language**: en

> 一个详细的 JSON 提示，用于生成一张优雅、奢华的名人肖像，类似于 {argument name="celebrity name" default="Ana de Armas"}。主体为半身像，身着华丽的银色高领上衣，光线柔和温暖，背景模糊柔和（散景效果）。

![优雅的安娜·德·阿玛斯名人肖像 (JSON 格式)](https://cms-assets.youmind.com/media/1769408688404_viptv2_G_gzldZW4AEf7GR.jpg)
![优雅的安娜·德·阿玛斯名人肖像 (JSON 格式)](https://cms-assets.youmind.com/media/1769408688346_edu9vz_G_gzldYXsAEks9e.jpg)
![优雅的安娜·德·阿玛斯名人肖像 (JSON 格式)](https://cms-assets.youmind.com/media/1769408688522_g80hx1_G_gzlZ_XUAAHwSx.jpg)

```
{
  "subject": {
    "description": "A portrait of a young woman with a glamorous and elegant appearance.",
    "identity_resemblance": "{argument name="celebrity name" default="Ana de Armas"}",
    "pose": "Head and shoulders shot; right arm raised with hand gently resting on the forehead; head turned slightly to the right while eyes look directly at the viewer.",
    "expression": "Soft, contemplative, calm, and alluring with slightly parted lips."
  },
  "physical_attributes": {
    "hair": {
      "color": "Dark brown",
      "style": "Pulled back into an updo or ponytail",
      "details": "Loose, wispy tendrils framing the face and neck"
    },
    "eyes": {
      "color": "Hazel green",
      "gaze": "Direct and engaging"
    },
    "skin": {
      "tone": "Fair to light olive",
      "texture": "Dewy and glowing"
    },
    "makeup": {
      "style": "Natural glam",
      "details": "Rosy blush on cheeks, glossy pinkish- lips, defined lashes, soft brows"
    }
  },
  "attire": {
    "type": "High-neck sleeveless top or dress",
    "material": "Heavily embellished fabric",
    "texture": "Covered in silver and white sequins, crystals, or beads",
    "color": "Silver/White",
    "fit": "Form-fitting bodice"
  },
  "accessories": {
    "earrings": "Long, dangling diamond drop earrings",
    "bracelet": "Delicate diamond tennis bracelet on the right wrist"
  },
  "environment": {
    "background": "Blurred (bokeh) vertical drapes or curtains",
    "colors": "Muted beige, champagne, and soft gold tones",
    "lighting": "Soft, warm, flattering illumination with highlights on the face, shoulder, and arm; hints of background bokeh lights"
  },
  "image_quality": {
    "style": "Celebrity portraiture / Event photography",
    "mood": "Elegant, serene, luxurious",
    "focus": "Sharp focus on the face, shallow depth of field blurring the background"
  }
}
```

[[Bokeh Background]] [[Ana De Armas Likeness]] [[Soft Warm Lighting]]

---

### 16. 16:9 电影故事板（来自参考资料）

**Author**: [茶狮子](https://x.com/xchashizi)  **Date**: 2026-01-25  **Language**: zh

> 一个中文提示，用于生成一个 16:9 电影式故事板（四个连续分镜），风格为写实纪录片。它使用两张参考图片：一张用于构图、关系和风格，另一张用于角色外观，详细说明了每个分镜的具体摄像机角度和场景元素，例如雪景户外视图和狭窄房间的透视。

![16:9 电影故事板（来自参考资料）](https://cms-assets.youmind.com/media/1769408670971_1d6zp9_G_gwXDgXoAAdvUC.jpg)

```
横版16比9电影连续分镜，写实纪录片风格，人物空镜关系位置风格参考图1，人物形象参考图2，这个提示词包含了四个具体的画面指令：

Panel 1 (侧脸特写): 聚焦图2人物的在床上看书参考图1面部特征（{argument name="hair color" default="白金发"}、绿眼），背景虚化处理，保留图1的冷色调光感。

Panel 2 (背影看书): 还原图1中“趴在床上看书”的动作，但换成图2的人物着装，强调窗外的{argument name="weather" default="雪景"}。

Panel 3 (中景仰拍): 动作位置参考图1这是一个极具张力的视角，体现房间的狭窄感和人物的空间关系，突出书架和海报墙的细节。

Panel 4 (全景/鱼眼): 补充一个广角镜头（参考图1的透视），交代整体环境，确立“雪天宅家”的氛围。
```

[[Cinematic Storyboard]] [[16:9 Format]] [[Documentary Realism]]

---

### 17. Y2K 闪光灯摄影美学提示词（复刻）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-25  **Language**: en

> 一个 JSON 提示，旨在生成具有 Y2K 风格智能手机闪光灯照片美学的图像。它强调 100% 保留面部保真度和逼真的皮肤纹理，使用直射闪光灯与彩色光线混合，并描绘一个女性博主原型，姿势放松、亲密（躺着），穿着 Y2K 风格的服装和妆容。（2015409719335326000 的副本）

![Y2K 闪光灯摄影美学提示词（复刻）](https://cms-assets.youmind.com/media/1769408661917_hy8sps_G_gwfGCXcAA74oV.jpg)
![Y2K 闪光灯摄影美学提示词（复刻）](https://cms-assets.youmind.com/media/1769408661970_lr5a0g_G_gwfDta4AE4ruU.jpg)

```
{
  "project_type": "image_generation_from_reference",
  "preservation_constraints": {
    "facial_fidelity": "100% identical to original (features, bone structure, skin tone)",
    "expression_lock": true,
    "texture_quality": "Preserve realistic skin texture and pores; strictly avoid plastic smoothing"
  },
  "visual_style": {
    "aesthetic": "Y2K-style smartphone flash photo",
    "era": "Early 2000s / Y2K",
    "lighting": "Direct flash mixed with colored light ({argument name=\"colored light\" default=\"soft pink or red\"})",
    "color_grading": "True-to-life colors, raw intimate snapshot look"
  },
  "composition": {
    "camera_angle": "High angle (held above)",
    "setting": "Bed or sofa",
    "pose": "Lying down, relaxed, playful, unposed moment",
    "mood": "Confident, self-love, intimate Valentine"
  },
  "subject_styling": {
    "archetype": "Female blogger",
    "apparel": "Fitted Y2K-inspired top, oversized hoodie or jacket",
    "makeup": "Glossy lips, subtle shimmer, visible fluffy false eyelashes"
  }
}
```

[[Direct Flash]] [[Smartphone Flash Photography]] [[Face Fidelity]]

---

### 18. 金色时刻汽车生活方式摄影 (JSON 格式)

**Author**: [Dominus the Prompter](https://x.com/iamdomprompt)  **Date**: 2026-01-25  **Language**: en

> 一个高度详细的 JSON 提示，用于在黄金时段生成超逼真的汽车生活方式摄影。场景中，一位身材健美的专业模特正在豪华环境中清洗一辆 {argument name="car type" default="Lamborghini Aventador"}（由上下文/图像暗示）。该提示指定了戏剧性的逆光、湿润表面上强烈的镜面高光，以及性感、迷人的氛围。

![金色时刻汽车生活方式摄影 (JSON 格式)](https://cms-assets.youmind.com/media/1769408691368_63tbcy_G_guEFUW8AEm_S5.jpg)

```
{
  "image_type": "Photorealistic commercial photography",
  "shot": "Medium Full Shot",
  "shot_details": "Horizontal cinematic composition with foreground emphasis on the luxury car hood and primary subject.",
  "style": "Hyper-realism, Golden Hour Glamour, Automotive Lifestyle Photography",
  "quality": "Ultra-detailed, Professional Grade, High Dynamic Range (HDR)",
  "color_grade": "Warm, Cinematic, High Contrast, dominated by rich golds, deep blacks, and warm skin tones.",
  "meta": {
    "aspect_ratio": "16:9 Widescreen",
    "resolution": "High Resolution, detailed"
  },
  "camera": {
    "device": "Professional DSLR",
    "lens": "Medium Telephoto (85mm or 100mm)",
    "aperture": "f/4",
    "distance": "Close proximity to the subject and vehicle",
    "angle": "Slight low angle",
    "framing": "Subject balanced against the car, with the sunburst anchoring the upper right quadrant.",
    "pov": "Intimate, high-end commercial viewer perspective",
    "focus": "Sharp focus on the subject's hips and the sponge/car hood",
    "lens_effect": "Prominent golden lens flare and sunburst effect, visible water droplets creating textural detail"
  },
  "lighting": {
    "description": "Dramatic, intensely warm backlighting from the setting sun.",
    "type": "Hard, directional sunlight mitigated by reflected fill.",
    "source": "Natural Sun (Golden Hour)",
    "primary": "Strong golden rim light highlighting the wet outline of the woman's body and hair.",
    "secondary": "Soft, reflected fill light illuminating the front side of the subject and the car paint.",
    "highlights": "Intense specular highlights on the glossy black paint (Lamborghini Aventador), wet skin, and dripping hair.",
    "shadows": "Deep, rich shadows providing strong contrast, particularly under the car and within the architectural recessions."
  },
  "scene": {
    "location": "Luxury residential driveway or modern resort courtyard",
    "environment": "Upscale, minimalist architecture (concrete/stucco), tropical planting visible.",
    "time": "Sunset / Golden Hour",
    "atmosphere": "Hot, humid, glamorous, luxurious, sensual"
  },
  "subject": {
    "gender": "Female",
    "age": "Early to Mid 20s",
    "ethnicity": "Mediterranean or Latina appearance",
    "appearance": "Toned, athletic, wet skin and hair, professional model physique.",
    "body": {
      "type": "Toned, athletic build",
      "waist": "Defined",
      "hips": "Curved and prominent",
      "chest": "Moderate, minimal coverage",
      "ass": "Prominent, emphasized by the pose",
      "skin": "Tan, wet, smooth texture with high sheen"
    },
    "expression": {
      "eyes": "Downcast, closed or looking at the car hood",
      "gaze": "Focused, internal",
      "mouth": "Relaxed, soft set",
      "face_vibe": "Serene, sensual concentration"
    },
    "hair": {
      "color": "Dark b"
```

[[Lamborghini]]

---

### 19. 超逼真宣传图片生成

**Author**: [Milo](https://x.com/Milo_Bahi_02)  **Date**: 2026-01-25  **Language**: en

> 一段非常简短的提示片段，旨在生成 8k 超逼真的宣传图片，可能用于产品或商业视觉生成。

```
Ultra-Realistic Promotional
```

[[Photorealism]]

---

### 20. Y2K 闪光灯照片美学提示

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-01-25  **Language**: en

> 一个 JSON 提示，旨在生成具有 Y2K 风格智能手机闪光灯照片美学的图像。它强调 100% 保留面部保真度和逼真的皮肤纹理，使用直射闪光灯与彩色光线混合，并描绘一个女性博主原型，以放松、亲密的姿势（躺着），搭配 Y2K 风格的服装和妆容。

![Y2K 闪光灯照片美学提示](https://cms-assets.youmind.com/media/1769408659734_zxbjvp_G_gsbw_X0AAA44R.jpg)
![Y2K 闪光灯照片美学提示](https://cms-assets.youmind.com/media/1769408659464_57qmmz_G_gsbwrbYAA6HAs.jpg)

```
{
  "project_type": "image_generation_from_reference",
  "preservation_constraints": {
    "facial_fidelity": "100% identical to original (features, bone structure, skin tone)",
    "expression_lock": true,
    "texture_quality": "Preserve realistic skin texture and pores; strictly avoid plastic smoothing"
  },
  "visual_style": {
    "aesthetic": "Y2K-style smartphone flash photo",
    "era": "Early 2000s / Y2K",
    "lighting": "Direct flash mixed with colored light ({argument name=\"colored light\" default=\"soft pink or red\"})",
    "color_grading": "True-to-life colors, raw intimate snapshot look"
  },
  "composition": {
    "camera_angle": "High angle (held above)",
    "setting": "Bed or sofa",
    "pose": "Lying down, relaxed, playful, unposed moment",
    "mood": "Confident, self-love, intimate Valentine"
  },
  "subject_styling": {
    "archetype": "Female blogger",
    "apparel": "Fitted Y2K-inspired top, oversized hoodie or jacket",
    "makeup": "Glossy lips, subtle shimmer, visible fluffy false eyelashes"
  }
}
```

[[Direct Flash]] [[Y2K Fashion]] [[Smartphone Flash Photography]] [[Face Fidelity]]

---

### 21. 奇幻电影海报风格转换

**Author**: [ちゃろん](https://x.com/charon_artist)  **Date**: 2026-01-25  **Language**: ja

> 一个旨在将图像转换为奇幻电影海报风格的提示，其中描绘了一位挥舞着光之剑的传奇英雄。该提示可在推文的 ALT 文本中找到，使用 Nano Banana Pro 生成。

![奇幻电影海报风格转换](https://cms-assets.youmind.com/media/1769408674982_i64qgq_G_gsG7jW4AAy05C.jpg)

```
伝説はここから始まる！光の剣を掲げよ！ファンタジー映画のポスター風に変換。
```

[[Poster Design]] [[Epic Fantasy]]

---

### 22. 四格漫画提示：漱口（英文版）

**Author**: [wakky13 @AIなんでもやってみる💪](https://x.com/NFTwakky13)  **Date**: 2026-01-25  **Language**: ja

> 这是一个用于使用 Nano Banana Pro 生成四格漫画的提示，主题是“漱口”（英文版）。

![四格漫画提示：漱口（英文版）](https://cms-assets.youmind.com/media/1769408683821_4imddt_G9ypjgTb0AA18qM.jpg)

```
きょうのテーマは　うがいをしよう(英文バージョン)
```

[[Sequential Art]] [[Comic Strip]]

---

### 23. 新鲜草莓比基尼肖像

**Author**: [神崎エリカ](https://x.com/Erika_Kanzaki24)  **Date**: 2026-01-25  **Language**: en

> 一张图像生成提示，重点是创作一张快乐女性的特写肖像，她身穿一件概念上由真实多汁草莓制成的比基尼，强调高分辨率和清新俏皮的美感。

![新鲜草莓比基尼肖像](https://cms-assets.youmind.com/media/1769408666502_kuz8hb_G_gOuVzacAA7Apl.jpg)

```
{
  "prompt_config": {
    "model_description": {
      "face": "A stunning woman with a radiant, joyful expression, sparkling eyes, and soft natural makeup",
      "hair": "Wind-swept wavy hair with a few {argument name="hair accessory" default="strawberry blossoms"} tucked behind the ear",
      "pose": "Looking directly at the camera with a playful, fresh smile"
    },
    "costume_material": {
      "concept": "Bikini made of real, succulent strawberries",
      "top": "Arrangement of whole and halved bright red strawberries, showing the juicy interior texture",
      "straps": "Natural green vines securely holding the fruit together"
    },
    "cinematography": "Close-up portrait focusing on the face and upper body, shallow depth of field, 8k resolution"
  }
}
```

[[Close-Up Portrait]] [[High Resolution]] [[Playful Aesthetic]]

---

### 24. 纳米香蕉滑梯生成讨论

**Author**: [Rei 📚 Notionライフハック2万部突破！](https://x.com/rei_notion)  **Date**: 2026-01-25  **Language**: ja

> 这条推文讨论了使用 Nano Banana 来生成幻灯片，强调了 Manus 在结合强大研究与幻灯片制作方面的优势。它指出幻灯片中的文本是可编辑的，这可能比使用 Gemini 或 NotebookLM 更方便。

![纳米香蕉滑梯生成讨论](https://cms-assets.youmind.com/media/1769408678278_5qnjnw_G_gCcWoXoAADhgc.jpg)
![纳米香蕉滑梯生成讨论](https://cms-assets.youmind.com/media/1769408678615_a4weqp_G_gCcW3WQAAQ2Gc.jpg)
![纳米香蕉滑梯生成讨论](https://cms-assets.youmind.com/media/1769408679917_q4l08w_G_gCcTgXwAAAyFi.jpg)
![纳米香蕉滑梯生成讨论](https://cms-assets.youmind.com/media/1769408680517_yxbwh4_G_gCcVKWUAABNVt.jpg)

```
Nano Bananaを使ったスライド生成
```

[[AI Workflow]]

---

### 25. 堕落天使转换

**Author**: [ちゃろん](https://x.com/charon_artist)  **Date**: 2026-01-25  **Language**: ja

> 一个旨在将图像转换为堕落天使风格的提示，强调黑暗之美和在寂静中休憩的瞬间。该提示可在推文的 ALT 文本中找到，使用 Nano Banana Pro 生成。

![堕落天使转换](https://cms-assets.youmind.com/media/1769408677601_novvvq_G_f1K2MbcAAYMo4.jpg)

```
闇に堕ちても美しい。静寂の中で羽を休めています。堕天使に変換。
```

[[Fantasy Portrait]]

---

### 26. 高端时尚牛仔编辑摄影提示

**Author**: [gauche](https://x.com/gaucheai)  **Date**: 2026-01-25  **Language**: en

> 为牛仔系列广告生成一张高级时装编辑照片的详细提示。照片中，一位铂金色头发的女性摆出充满活力的舞者姿势，躺在灰色摄影棚地板上，一条腿垂直伸展，身穿打结的白色 T 恤和浅色水洗牛仔裤。提示要求专业的影棚灯光、简洁的极简主义美学和冷色调配色。

![高端时尚牛仔编辑摄影提示](https://cms-assets.youmind.com/media/1769408701085_ghnt40_G_fyV3vXgAA97-D.jpg)

```
{
  "prompt": "Denim fashion editorial photography, young woman with long platinum white blonde wavy hair, lying on right side on grey studio floor, dynamic flexible dancer pose with left leg extended straight up vertically toward ceiling, right hand reaching up holding ankle of raised leg, left arm flat on floor supporting upper body, looking directly at camera with neutral confident expression, light blue grey eyes, fair porcelain skin, natural minimal makeup with nude pink lips, grey seamless gradient studio background darker at top lighter on floor, soft diffused professional studio lighting, high fashion denim campaign aesthetic, athletic dancer flexibility pose, full body composition, clean minimalist studio setting",
  "negative_prompt": "outdoor, harsh shadows, dark background, heavy makeup, casual snapshot, cluttered props, warm color tones",
  "style": "high fashion editorial, denim brand campaign, professional studio photography, dynamic athletic pose",
  "aspect_ratio": "3:4",
  "camera": {
    "type": "professional medium format studio photography",
    "angle": "eye level, straight on frontal view",
    "framing": "full body shot capturing complete pose from head to raised foot"
  },
  "lighting": {
    "type": "soft diffused studio lighting",
    "quality": "even professional illumination, minimal shadows, clean highlight on subject",
    "atmosphere": "clean polished high fashion studio"
  },
  "mood": "confident, editorial, high fashion, athletic, elegant, strong",
  "color_palette": "white, platinum silver blonde, light blue denim, grey gradient background, neutral cool tones",
  "subject_features": {
    "hair": "long platinum white blonde, soft natural waves, middle parted, flowing on studio floor",
    "skin": "fair, porcelain, flawless, natural",
    "eyes": "light blue grey, direct intense gaze at camera",
    "lips": "natural nude pink, neutral expression",
    "expression": "neutral, confident, calm, editorial"
  },
  "pose_details": {
    "position": "lying on right side, torso propped up",
    "left_leg": "extended straight up vertically pointing toward ceiling",
    "right_leg": "flat on floor extended straight",
    "right_arm": "raised up, hand holding ankle of raised left leg",
    "left_arm": "on floor supporting upper body weight, hand flat on ground"
  },
  "wardrobe": {
    "top": "{argument name="top style" default="white basic cotton t-shirt, short sleeves, knotted and tied at front creating cropped effect"}",
    "bottom": "light wash blue denim jeans, relaxed straight leg fit, classic five pocket style, copper button fly visible at waist"
  },
  "setting": {
    "location": "professional photography studio",
    "background": "grey seamless backdrop with gradient from darker grey at top to lighter grey on floor",
    "floor": "smooth light grey studio floor surface"
  }
}
```

[[Platinum Hair]] [[Minimalist Aesthetic]] [[Cool Color Palette]]

---

### 27. 具有精确面部参考的电影级写实街头肖像

**Author**: [ailabs.zone](https://x.com/zhoumeng780)  **Date**: 2026-01-25  **Language**: en

> 这个详细的提示旨在创建一张电影级的超写实街头肖像，需要上传一张面部图像作为精确的面部参考。场景中，一位身穿潮牌服饰的年轻男性坐在一处城市小巷里，身后是一幅与他本人相匹配的涂鸦壁画，画面强调超精细的纹理和电影般的灯光效果。

![具有精确面部参考的电影级写实街头肖像](https://cms-assets.youmind.com/media/1769408685373_kpdnt8_G_fsfFXWsAAYSe0.jpg)

```
Create a photorealistic cinematic street portrait using the uploaded face image as the exact facial reference. The main subject is a young male, sitting confidently on a metal storage box in an urban alley. His face must exactly match the uploaded image (same facial structure, skin tone, eyes, expression). He is wearing a {argument name="jacket color" default="pink"} puffer jacket, a white graphic t-shirt, and full-length blue denim jeans (not shorts). Modern streetwear sneakers on his feet. Behind him on the wall, there is a large graffiti mural of the same male character, with the same face (from uploaded image), same outfit, and same pose — both real person and wall art must match perfectly. Colorful paint splashes are visible on his clothes, shoes, skin, and environment. Spray paint cans scattered on the ground around him. Urban street art aesthetic, shallow depth of field, soft natural daylight, cinematic lighting, ultra-detailed textures, high realism, 8K quality. No logos, no brand names, no text, no watermark, no cartoon style.
```

[[Streetwear Fashion]]

---

### 28. 共和国日 Gemini Nano Banana 照片提示

**Author**: [blogbursthub](https://x.com/blogbursthub)  **Date**: 2026-01-25  **Language**: en

> 在一条推文的 alt 文本中发现的提示，专为 Gemini Nano Banana 模型设计，用于生成一张与共和国日相关的精美照片。

![共和国日 Gemini Nano Banana 照片提示](https://cms-assets.youmind.com/media/1769322358059_1utmso_G_fISl8XYAAxLUQ.jpg)

```
Stunning republic day photo
```

[[Holiday Photography]]

---

### 29. 新黑色合成波三联画蒙太奇

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2026-01-25  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一个垂直三联画蒙太奇（三幅面板），具有一致的新黑色电影或合成波美学风格。它详细说明了每幅面板的内容：一辆经典肌肉车在加油站，一张身穿皮夹克女性的电影肖像，以及一个复古餐厅内部，所有场景都设置在夜晚，并带有特定的照明和调色板（琥珀色/橙色和青色/蓝色）。

![新黑色合成波三联画蒙太奇](https://cms-assets.youmind.com/media/1769408709533_hmy810_G_e8IrqbsAA_Uod.jpg)

```
{
  "meta": {
    "image_quality": "Very High",
    "image_type": "Digital Art / AI Generation (Triptych Montage)",
    "resolution_estimation": "High definition vertical collage",
    "file_characteristics": {
      "compression_artifacts": "Low",
      "noise_level": "Low",
      "lens_type_estimation": "Varied per panel (Wide for car, Portrait/85mm for woman, Wide for diner)"
    }
  },
  "global_context": {
    "scene_description": "A vertical triptych montage displaying three distinct retro-cinematic scenes sharing a 'synthwave' or 'neo-noir' aesthetic. \n\nTop Panel: A side-profile view of a {argument name="car color" default="yellow"} classic muscle car parked at a gas station at night with wet pavement reflections and strong orange neon lighting. \n\nMiddle Panel: A cinematic portrait of a young woman with dark curly hair and a leather jacket, standing in a foggy, backlit urban environment with soft bokeh. \n\nBottom Panel: A highly detailed interior view of a retro diner counter, featuring stools, a tiled bar, kitchen equipment, and a glowing overhead menu board.",
    "environment_type": "Composite (Outdoor/Outdoor/Indoor)",
    "time_of_day": "Night",
    "weather_atmosphere": "Moody, Wet, Foggy, Atmospheric",
    "lighting": {
      "source": "Artificial (Neon signage, street lamps, interior tungsten)",
      "direction": "Mixed (Top-down for car, Backlit for woman, Overhead diffused for diner)",
      "quality": "Soft, Diffused, Volumetric",
      "color_temperature": "Warm Amber/Orange dominant with cool Teal/Blue shadows"
    },
    "color_palette": {
      "dominant_hex_estimates": [
        "#FF9900",
        "#1A1A1A",
        "#0B2226",
        "#E6B800",
        "#5E3A18"
      ],
      "accent_colors": [
        "#00FFFF",
        "#FF3300",
        "#888888"
      ],
      "contrast_level": "High"
    }
  },
  "composition": {
    "camera_angle": "Eye-level (all panels)",
    "framing": "Wide (Top), Medium Close-up (Middle), Wide (Bottom)",
    "depth_of_field": "Deep (Top), Shallow (Middle), Deep (Bottom)",
    "focal_point": "Panel 1: Car center; Panel 2: Woman's face; Panel 3: Illuminated menu board",
    "symmetry_type": "Horizontal stacking",
    "rule_of_thirds_alignment": "Woman aligned center; Car aligned lower third of top panel; Diner counter aligned lower third of bottom panel"
  },
  "objects": [
    {
      "id": "panel1_car",
      "label": "Classic Muscle Car",
      "category": "Vehicle",
      "location": {
        "relative_position": "Top Panel - Center/Bottom",
        "bounding_box_percentage": {
          "x": 0.15,
          "y": 0.15,
          "width": 0.7,
          "height": 0.15
        }
      },
      "dimensions_relative": "Large",
      "distance_from_camera": "Mid",
      "pose_orientation": "Side profile facing left",
      "material": "Metal, Glass, Chrome",
      "surface_properties": {
        "texture": "Smooth automotive paint",
        "reflectivity": "High",
        "micro_detail": "Rain streaks, wet reflections."
      }
    }
  ]
}
```

[[Triptych Composition]]

---

### 30. ElevenLabs 的 Vlog 旁白提示

**Author**: [空想写真家](https://x.com/KusoPhoto)  **Date**: 2026-01-25  **Language**: ja

> 这是用于 ElevenLabs v3 的旁白脚本（提示），用于制作一个视频博客风格的视频，其中包含由 Nano Banana Pro 生成并由 Kling O1 动画的图像。该脚本描述了角色在一家传统日本餐厅的体验。

```
[ささやき] 今日はある老舗の懐石料理店で食事をしてきました。せっかくなので厨房で体験入店させて頂いたのですが、うっかり一口味見しちゃいました...。 [笑] また必ず戻ってきますね...ばいばい！
```

[[AI Video Workflow]]

---

### 31. 在主体上生成随机百分比心形

**Author**: [俺の娘たち / AIエンジニア](https://x.com/oreno_musume)  **Date**: 2026-01-25  **Language**: ja

> 一个简单的日文提示指令，用于让 Nano Banana Pro 在上传照片中每个主体头顶的心形符号内生成一个随机百分比（0-100）。

![在主体上生成随机百分比心形](https://cms-assets.youmind.com/media/1769408668250_mhoitc_G_ew_BtbcAAgTDr.jpg)

```
各被写体の頭の上に「◯%」という文字をハートの図の中に生成。◯の中の数字は0～100の間の数字をランダムで生成。
```

[[Japanese Prompt]]

---

### 32. Suno 音乐生成讨论

**Author**: [癒色えも(イシキ•エモ)](https://x.com/ishiki_emo)  **Date**: 2026-01-25  **Language**: ja

> 这条推文讨论了使用 SUNO 进行背景音乐编曲，指出原本是器乐的歌曲，结果却变成了一首融合了假面骑士和战队（超级英雄）风格的声乐曲，突显了 AI 令人惊讶的能力。

```
なんと歌もの笑　ライダーと戦隊の合いの子みたいな曲調になった？？
```

[[AI Workflow]]

---

### 33. 4x4 时光旅行相册

**Author**: [路飞 🏴‍☠️ AI 研究员🧐](https://x.com/0xluffy_eth)  **Date**: 2026-01-25  **Language**: zh

> 一个中文提示，用于生成一个 4x4 的“时间旅行相册”，让主体风格跨越不同时代，从 19 世纪 80 年代的油画质感和羊毛大衣，到 20 世纪 60 年代的复古街头风格，再到 21 世纪 00 年代的数码照片，同时确保主体身份的一致性，只改变发型、胡须、服装和背景。

![4x4 时光旅行相册](https://cms-assets.youmind.com/media/1769408673394_2h44ag_G_eYeHYbQAAxgNY.jpg)

```
做一张 “1880→2020 的 4×4 穿越影集”

从 {argument name="start year" default="1880"} 年代的油画质感、羊毛大衣，到 {argument name="mid year" default="1960"} 的复古街拍，再到 {argument name="end year" default="2000"} 年代的数码相片
每一格都是不同时代的我，发型、胡子、服装、背景，全都对味。
```

[[Identity Consistency]] [[4x4 Grid]]

---

### 34. 特写肖像，搭配复古配饰

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-01-25  **Language**: en

> 一个高度详细的 JSON 提示，用于 Gemini Nano Banana Pro 生成一张年轻成年女性的特写半身肖像。该提示详细说明了构图、姿势（抬起太阳镜）、面部特征、深棕色编发和头巾、深蓝色牛仔夹克，以及包括金色环形耳环和带有蓝色四叶草吊坠的精致金链在内的详细配饰。它旨在呈现一种精致柔和的魅力妆容，具有自然日光和适度的色彩对比。

![特写肖像，搭配复古配饰](https://cms-assets.youmind.com/media/1769408702776_ywx5nw_G_eLbunawAAQ5En.jpg)
![特写肖像，搭配复古配饰](https://cms-assets.youmind.com/media/1769408702831_nuiza4_G_eLbvNXMAAG-3O.jpg)

```
{
  "image_description": {
    "composition": {
      "framing": "Tight medium close-up portrait, chest-up",
      "orientation": "Vertical",
      "camera_angle": "Eye-level with slight leftward subject turn",
      "pose": "Subject facing the camera with head slightly tilted, right hand lifting sunglasses",
      "focus": "Sharp focus on face and accessories with shallow depth of field",
      "cropping": "Top of head included with minimal space above, arms partially cropped"
    },
    "subject": {
      "identity": "Same reference face",
      "type": "Single human subject",
      "gender_presentation": "Feminine",
      "age_range": "Young adult",
      "skin_tone": "Fair with warm undertones",
      "facial_features": {
        "face_shape": "Oval",
        "eyes": "Light green, almond-shaped",
        "eyebrows": "Thick, softly arched, well-groomed",
        "nose": "Straight and proportionate",
        "lips": "Full with pronounced cupid’s bow, glossy finish"
      },
      "expression_and_gaze": {
        "expression": "Neutral to confident",
        "gaze_direction": "Directly toward the camera through sunglasses"
      }
    },
    "hair": {
      "color": "dark brown",
      "texture": "Smooth and straight with subtle natural wave",
      "style": "Center-parted, long length, one side braided and tucked",
      "accessory": "Headscarf covering the crown"
    },
    "wardrobe": {
      "top": "White fitted inner top",
      "outerwear": {
        "type": "Denim jacket",
        "color": "Dark blue",
        "details": "Visible stitching",
        "style": "Casual chic, retro-inspired"
      }
    },
    "accessories": {
      "sunglasses": {
        "shape": "Oval",
        "frame": "Thin metal",
        "lens_color": "Dark brown gradient",
        "position": "Slightly lowered on the nose, held by hand"
      },
      "jewelry": {
        "earrings": "Medium-sized gold hoop earrings",
        "necklace": "Delicate gold chain with blue clover-shaped charms",
        "nails": {
          "length": "Long",
          "shape": "Almond",
          "color": "Deep navy blue"
        },
        "headscarf": {
          "material": "Lightweight fabric",
          "color_palette": "White base with blue floral pattern",
          "style": "Vintage-inspired wrap"
        }
      }
    },
    "makeup": {
      "complexion": "Smooth matte-satin finish",
      "blush": "Soft rosy pink on cheeks",
      "eyes": "Defined lashes with subtle neutral eyeshadow",
      "lips": "High-shine pink gloss",
      "overall_style": "Polished soft glam"
    },
    "color_palette": {
      "dominant_colors": [
        "Denim blue",
        "Warm blonde",
        "Soft pink",
        "Gold",
        "White"
      ],
      "contrast": "Moderate, subject clearly separated from darker background"
    },
    "lighting": {
      "type": "Natural daylight",
      "direction": "Front-left illumination",
      "quality": "Soft with gentle highlights",
      "sh
```

[[Gold Jewelry]] [[Braided Hair]] [[Soft Daylight]] [[Denim Jacket]]

---

### 35. 西装革履，脚踏祥云

**Author**: [岡田泰彦｜光邦｜巻き込まれ型AIエヴァンジェリスト](https://x.com/KohoOkada)  **Date**: 2026-01-25  **Language**: ja

> 一个用于 Nano Banana Pro 的简单图像生成提示，描述了一个身穿西装的人威严地站在云端。

![西装革履，脚踏祥云](https://cms-assets.youmind.com/media/1769408662684_uqfcgy_G-IPHIMa0AAGsJi.jpg)

```
スーツ姿で空の上に立っている自分
　（雲の上で仁王立ち）
```

[[Fantasy Setting]]

---

### 36. 超逼真可爱学术街拍肖像

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-01-25  **Language**: en

> 以下是为 Hedra 上的 Nano Banana Pro 设计的高度结构化 JSON 提示，详细描述了一位身着可爱学院风/韩式街头时尚的年轻女性的逼真图像。它具体说明了面部特征、深棕色波浪发、灰色绞花针织毛衣、棕色短裙、及膝袜和棕色系带鞋。场景是城市街道人行道，自然日光，通过高角度智能手机拍摄，强调俏皮和青春的审美。

![超逼真可爱学术街拍肖像](https://cms-assets.youmind.com/media/1769408701463_djt5p6_G_eK-_ibsAA72s8.jpg)

```
{
  "image_generation": {
    "face": {
      "description": "young woman with soft youthful facial features, round face, natural skin texture, light makeup, subtle blush, slightly puckered lips",
      "expression": "playful, cute pout expression",
      "glasses": "round brown eyeglasses with thin frame"
    },
    "hair": {
      "color": "dark brown",
      "style": "long wavy hair, loose and natural",
      "texture": "soft, slightly glossy, natural waves"
    },
    "outfit": {
      "top": "gray cable-knit sweater layered over a white collared shirt",
      "bottom": "short brown skirt",
      "socks": "knee-high gray socks",
      "shoes": "brown casual lace-up shoes",
      "style": "cute academic, Korean street fashion"
    },
    "pose": {
      "body_position": "leaning slightly forward toward the camera",
      "hands": "holding a takeaway coffee cup with both hands",
      "camera_angle": "high-angle shot looking down"
    },
    "environment": {
      "setting": "urban street sidewalk",
      "background": "modern building with glass windows and metal railings",
      "details": "green and white roadside barrier, clean city street"
    },
    "lighting": {
      "type": "natural daylight",
      "direction": "direct sunlight creating soft shadows",
      "mood": "bright, fresh, candid"
    },
    "camera": {
      "device": "smartphone camera",
      "lens": "wide-angle",
      "style": "casual street photography",
      "quality": "high resolution, sharp focus"
    },
    "aesthetic": {
      "theme": "cute urban lifestyle",
      "vibe": "playful, cozy, youthful",
      "realism": "photorealistic, natural proportions, true-to-life colors"
    }
  }
}
```

[[Urban Sidewalk]]

---

### 37. 港区女性时尚杂志信息图

**Author**: [Toshi｜AI×機能訓練×柔整](https://x.com/Toshi4AI)  **Date**: 2026-01-25  **Language**: ja

> 为时尚杂志生成信息图或专题页面设计，目标受众为“港区女子”（暗示成熟、高端的受众）。内容应系统且易于理解，可利用图标、照片、图表、示意图和手写弹出框。

![港区女性时尚杂志信息图](https://cms-assets.youmind.com/media/1769408676703_580d9h_G_d-Lh1bMAAyEZf.jpg)
![港区女性时尚杂志信息图](https://cms-assets.youmind.com/media/1769408677599_gk25u5_G_d-Ln1bwAAK54L.jpg)

```
キレイ系港区女子が読むファッション雑誌の特集ページのデザインにして。内容は体系的、建設的にわかりやすくする。必要であればアイコン、写真、グラフ、図、手書きPOPを入れる。
```

[[Infographic Design]] [[Luxury Fashion]] [[Editorial Layout]]

---

### 38. 树脂挂件插画提示词

**Author**: [ハイさん](https://x.com/highsan_AIart)  **Date**: 2026-01-25  **Language**: ja

> 一个旨在生成适合制作树脂挂件的插画的提示，重点是分离主体，并根据是否提供带背景或不带背景的参考图像来处理背景。

![树脂挂件插画提示词](https://cms-assets.youmind.com/media/1769408664507_cunurs_G_d7YCna8AACduk.jpg)
![树脂挂件插画提示词](https://cms-assets.youmind.com/media/1769408664414_y4g2wy_G_d7XbzXgAAYtBx.jpg)
![树脂挂件插画提示词](https://cms-assets.youmind.com/media/1769408664495_rz4ry2_G_d7ZFWaIAABcgT.jpg)
![树脂挂件插画提示词](https://cms-assets.youmind.com/media/1769408666307_e23666_G_d7ZqoaAAAI34O.jpg)

```
あなたはプロのイラストレーターです。ユーザーが添付した画像を元に、レジンチャームの素材として使用できるイラストを生成してください。

**イラストの要件:**
1.  **主題の強調:** 添付された画像から主要な被写体（キャラクター、動物、物体など）を抽出し、その魅力を最大限に引き出すように描画してください。
2.  **背景処理:**
    *   添付画像に背景がない場合（透過または単色背景）、被写体の雰囲気に合った、シンプルで可愛らしい背景（例：淡いグラデーション、小さな星やハートのパターン、水彩風のにじみ）を自動で追加してください。
    *   添付画像に背景がある場合、その背景をそのまま使用し、イラストとして統合してください。
3.  **スタイル:** 鮮やかでクリアな色使い、輪郭線がはっきりとした、可愛らしいデフォルメされたイラストスタイルで描いてください。レジンに封入した際に映えるように、光沢感や立体感を意識してください。
4.  **出力形式:** 正方形の画像として出力してください。

**注意点:**
*   高速モードではなく、必ずPROモードまたは思考モードで実行してください。
*   生成されたイラストは、レジンチャームの素材として使用することを目的としています。
```

[[Background Removal]]

---

### 39. 海底肖像

**Author**: [Saintpablo](https://x.com/stpabloai)  **Date**: 2026-01-24  **Language**: en

> 一张关于年轻女性的图像，她坐落在沙质海底，身处清澈见底的浅水中，从极高的垂直角度拍摄。提示词对她的外貌（白皙的皮肤，浅棕色头发漂浮）、姿势（直视上方，看向镜头）以及水对她衣物的影响（湿透的布料紧贴身体）进行了高度详细的描述。

![海底肖像](https://cms-assets.youmind.com/media/1769322319390_47ao3j_G_dvOWyWcAAsXSS.jpg)

```
{
  "scene": "A shallow, crystal-clear sea floor captured from an extreme high-angle vertical perspective, looking straight down through water.",
  "subject": {
    "character": "Young adult Caucasian woman with a bold, confident, overtly sensual presence.",
    "face": {
      "structure": "Oval face with soft jawline and high forehead.",
      "skin": "Fair skin with natural texture, visible light freckles on the nose and cheeks, and a soft warm flush enhanced by refracted sunlight.",
      "eyes": {
        "shape": "Almond-shaped, opened and directed upward toward the lens through the water.",
        "color": "Bright green with dark limbal rings.",
        "expression": "Calm, self-aware, confident gaze with an intimate, magnetic undertone."
      },
      "mouth": {
        "lips": "Closed, relaxed lips with natural fullness and subtle sheen caused by water diffusion."
      },
      "makeup": "Minimalist, water-resistant natural makeup look emphasizing skin texture, brows, and eye clarity."
    },
    "hair": {
      "color": "Light brown base with honey-blonde highlights and balayage streaks.",
      "length": "Past shoulder length, approximately 18-20 inches.",
      "texture": "Naturally wavy, freely floating and spreading outward in the water with visible individual strands.",
      "style": "Center-parted, fully submerged, softly fanning around the face and neck.",
      "visible": "Fully visible, suspended and weightless in the surrounding water."
    }
  },
  "pose": {
    "overall": "Seated directly on the sandy sea floor with legs extended forward, looking straight up toward a camera positioned above the water surface.",
    "position": {
      "base": "Sitting on fine pale sand beneath shallow water.",
      "orientation": "Body aligned vertically beneath the camera, facing upward."
    },
    "torso": {
      "direction": "Upright with a pronounced natural arch through the lower back.",
      "position": "Centered in the frame.",
      "effect": "Posture emphasizes bust projection, narrow waist, and elongated torso."
    },
    "hips": {
      "position": "Anchored into the sand.",
      "emphasis": "Clearly sculpted by the cling of wet fabric contouring the pelvis and hips."
    },
    "legs": {
      "position": "Extended forward and slightly apart, knees gently bent.",
      "visible": "Upper thighs and knees visible through the water.",
      "effect": "Leg contours magnified by water refraction and fabric tension."
    },
    "arms": {
      "position": "Right arm extended upward toward the camera (out of frame), left arm resting lightly on the sand with fingers partially submerged.",
      "effect": "Subtle muscle tension visible through the skin and fabric interaction with water."
    },
    "head": {
      "turn": "Fully tilted back to face the surface and lens above.",
      "expression": "Composed, dominant, serenely seductive."
    }
  },
  "outfit": {
    "one_piece_swimsuit": "{argument name="swimsuit style" default="High-cut, low-back one-piece swimsuit"}",
    "color": "{argument name="swimsuit color" default="Burnt orange/Tangerine"}",
    "material": "Ribbed texture, matte finish, fully saturated color against the water."
  }
}
```

[[Underwater Portrait]]

---

### 40. Barbiecore 高角度街景

**Author**: [jennieee:3](https://x.com/jenniebae_ai)  **Date**: 2026-01-24  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张充满活力、高饱和度的“芭比核”风格图像：一名女性站在一辆粉色复古敞篷车旁，置身于比佛利山庄风格的街道上。该提示词特别指示 AI 使用戏剧性的高角度拍摄，以缩短主体并使背景扁平化。

![Barbiecore 高角度街景](https://cms-assets.youmind.com/media/1769322267896_fn20d0_G_dqWYsWcAAnu45.jpg)
![Barbiecore 高角度街景](https://cms-assets.youmind.com/media/1769322267782_4lk9gu_G_dqT4mWAAEb7m_.jpg)
![Barbiecore 高角度街景](https://cms-assets.youmind.com/media/1769322267946_yz6qiw_G_drAXIWAAEKpM1.jpg)

```
{
  "image_generation_parameters": {
    "subject": {
      "description": "Cheerful blonde woman with long wavy hair",
      "attire": "Pink two-piece outfit consisting of a bustier crop top and a pleated mini skirt",
      "accessories": ["White retro cat-eye sunglasses", "Small pink woven handbag"],
      "pose": "Standing beside a car, smiling upward, one hand near her face and the other holding a bag"
    },
    "environment": {
      "setting": "Sun-drenched Beverly Hills style street",
      "background_elements": ["Tall palm trees lining a residential road", "Clear blue sky", "Green hedges"],
      "prop": "{argument name="car color" default="Pink"} vintage convertible car with detailed interior and chrome steering wheel"
    },
    "cinematography": {
      "camera_angle": "High-angle shot (looking down from above)",
      "framing": "Medium Close-Up (MCU) focusing on head, torso, and top of the car",
      "aspect_ratio": "9:16 (Vertical)",
      "lens_effect": "Standard 50mm focal length to minimize distortion while emphasizing height"
    },
    "lighting_and_color": {
      "aesthetic": "Vibrant, high-saturation, 'Barbiecore' aesthetic",
      "lighting": "Hard, direct sunlight creating sharp shadows on the asphalt road",
      "primary_palette": ["Bubblegum Pink", "Bright White", "Asphalt Gray", "Palm Green"]
    },
    "technical_directive": "Re-render the original scene with a dramatic perspective shift. Foreshorten the subject's body to show visual dominance from the high-angle position. Ensure the car's pink dashboard and the road surface appear flattened beneath the subject."
  }
}
```

[[High Angle Shot]] [[Retro Aesthetic]]

---

### 41. 黑暗奇幻冬季生物从暴风雪中现身

**Author**: [Captain HaHaa](https://x.com/CaptainHaHaa)  **Date**: 2026-01-24  **Language**: en

> 一个用于生成黑暗奇幻生物电影图像的提示。它描述了一个高耸的冬季生物，拥有冰角、结霜的毛皮和发光的蓝色眼睛，背景是鹅毛大雪和冷蓝色调。构图指定为电影般的广角镜头，采用低角度和戏剧性照明。

![黑暗奇幻冬季生物从暴风雪中现身](https://cms-assets.youmind.com/media/1769322297572_j4dp4w_G_dmeMZaMAAQlz-.jpg)

```
A towering winter creature emerges from a blizzard shrouded forest, antler like ice horns branching from its skull, fur crusted with frost and drifting snow. Glowing pale light blue eyes cut through the whiteout. Breath crystallizes midair. 

Cinematic wide shot, low angle, heavy snowfall, cold blue-grey palette, ultra detailed texture, dramatic rim light, dark fantasy realism.
```

[[Cinematic Wide Angle]]

---

### 42. 逼真的奢华旅行专题，带人脸锁定功能

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-24  **Language**: en

> 一个极其详细的 JSON 提示，用于在卡普里岛附近的一艘游艇上生成一张超逼真的奢华旅行编辑肖像。该提示包含严格的面部识别锁定限制（需要参考图像）、特定的相机语言（50mm，时尚编辑）以及详细的环境和服装描述。

![逼真的奢华旅行专题，带人脸锁定功能](https://cms-assets.youmind.com/media/1769322262607_f6sjgj_G_dZP_lWcAAf863.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_luxury_travel_editorial",
      "version": "v1.0_YACHT_CAPRI_FARAGLIONI_STRIPED_DRESS_EN",
      "priority": "highest",
      "language": "en"
    },
    "references": {
      "reference_image_face": {
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
      "reference_image_scene": {
        "source": "UPLOAD_REFERENCE_IMAGE (OPTIONAL)",
        "purpose": "POSE_COMPOSITION_LIGHTING_ANCHOR",
        "strict_lock": false,
        "preserve_pose": true,
        "preserve_composition": true,
        "preserve_mood": true
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
      "render_style": "ultra_photoreal_luxury_editorial_film_still",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_modern_film",
      "color_grade": "mediterranean_noon_clean",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "global_rules": {
      "camera_language": "50mm, eye-level, fashion editorial, shallow depth of field, focus on face and fabric texture",
      "lighting_language": "bright Mediterranean noon sun with soft bounce fill, realistic shadows, no flash",
      "authenticity_markers": "no AI glow, no HDR, realistic sea reflections, natural skin texture, correct hands"
    },
    "creative_prompt": {
      "scene_summary": "A luxury travel fashion editorial portrait on a yacht in the Mediterranean, with dramatic limestone sea stacks and deep blue water in the background. The same adult woman (face MUST match the reference 100%) is seated on the yacht deck in a flowing {argument name="dress color" default="blue-and-white"} striped maxi dress with a matching scarf detail. Calm, elegant expression, effortless vacation glamour.",
      "subject_details": {
        "count": 1,
        "description": "adult woman, exact same identity as reference",
        "expression": "soft confident smile, relaxed gaze to camera",
        "face_visibility": "full face clearly visible, sharp focus for identity match",
        "skin_and_face": "natural texture, no retouch, realistic pores",
        "hair": "long dark hair, natural shine, slightly wind-touched strands"
      },
      "wardrobe_and_style": {
        "outfit": "blue-and-white striped flowing maxi dress, thin straps, fitted bodice, voluminous ski"
      }
    }
  }
}
```

[[Face Identity Locking]]

---

### 43. 超写实冬季浪漫肖像

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-24  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一对情侣在白雪皑皑的冬季森林中拥抱的超写实电影级生活肖像，其中指定了服装、光照（阴天冬季日光），并严格限制不得出现文字或水印。

![超写实冬季浪漫肖像](https://cms-assets.youmind.com/media/1769408693272_4f9z7o_G_dWhCzXoAA7AnW.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "photoreal_winter_romance_forest_couple",
      "version": "v1.0_SNOWY_FOREST_COUPLE_EMBRACE_NO_TEXT_EN",
      "priority": "highest",
      "language": "en"
    },
    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "ultra_photoreal_cinematic_lifestyle",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle",
      "color_grade": "soft_neutral_winter",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch",
      "no_text": true,
      "no_logos": true,
      "no_watermarks": true,
      "no_ui": true
    },
    "creative_prompt": {
      "scene_summary": "Ultra-photorealistic winter romance portrait in a snowy forest. A couple stands close, hugging warmly and touching foreheads/noses in an intimate moment. Light snowfall is visible with layered depth: larger flakes softly blurred in the foreground and smaller flakes sharp in the mid/background. Snow rests naturally on tree branches and lightly on clothing. Cozy, soft, cinematic mood. No text.",
      "environment": {
        "location_feel": "dense winter forest with tall trunks and snow-covered evergreens",
        "ground": "fresh snow with subtle footprints and natural texture",
        "weather": "light active snowfall",
        "lighting": "overcast winter daylight, diffused and soft, natural shadows"
      },
      "subjects": {
        "couple": {
          "female_adult": {
            "wardrobe": "white fluffy faux-fur coat, warm earmuffs/headband, winter pants, winter boots",
            "pose": "standing close in the man's arms, one arm around his back/waist, face tilted up toward him",
            "expression": "soft smile, eyes gently closed or half-closed"
          },
          "male_adult": {
            "wardrobe": "cream/beige sherpa hoodie or fleece jacket, winter pants",
            "pose": "arms around the woman, head tilted down, forehead/nose touching hers",
            "expression": "tender, calm"
          }
        }
      },
      "camera_and_composition": {
        "shot_type": "lifestyle portrait, eye-level, intimate medium shot",
        "lens_look": "50mm equivalent, shallow depth of field, gentle background separation",
        "framing": "couple centered, forest creates natural vertical lines, minimal distractions",
        "focus": "faces and hands sharp, background softly blurred"
      },
      "physical_realism": {
        "snow_interaction": "realistic snow accumulation on branches; subtle snow specks on shoulders and hair; correct contact shadows at boots and ground",
        "fabric_detail": "visible fuzzy coat fibers and sherpa texture, realistic folds and tension where arms hug"
      },
      "anatomy_constraints": {
        "priority": "maximum",
        "requirements": [
          "natural facial proportions "
```

[[Snowy Forest]] [[Cinematic Lifestyle]]

---

### 44. Y2K 风格复古快照：玛格特 · 罗比在办公室场景中

**Author**: [bengi](https://x.com/p3rikly)  **Date**: 2026-01-24  **Language**: en

> 一个详细的提示，用于生成一张具有复古千禧年（Y2K）时代数码快照美学的超写实图像。图像中，玛格特·罗比（Margot Robbie）身穿黑色短裤和一件带有粉蓝色彼得潘领的上衣，栖身于一个文件柜上，被内置的硬闪光灯照亮。该提示详细说明了灯光和相机细节，以模仿 2000 年代初期的紧凑型数码相机效果。

![Y2K 风格复古快照：玛格特 · 罗比在办公室场景中](https://cms-assets.youmind.com/media/1769322290489_bbpapo_G_dVvh6XgAA-s_6.jpg)

```
{
  "subject": {
    "description": "{argument name="celebrity name" default="Margot Robbie"} with light blonde hair pulled into a loose, imperfect ponytail, a few strands falling naturally around her cheeks.",
    "appearance": "Fair complexion, wearing slim black rectangular eyeglasses. Her gaze meets the camera from just above the frames.",
    "pose": "Perched on the edge of a pale wooden office cabinet. One arm braced behind her for support, torso slightly twisted. Legs crossed at the knee. The free hand lightly adjusts her glasses.",
    "clothing": {
      "top": "Black ribbed short-sleeve top featuring a soft {argument name="collar color" default="powder-blue"} Peter Pan collar with subtle lace edging.",
      "waist": "Structured brown corset-style waist belt emphasizing the silhouette.",
      "bottoms": "Black tailored shorts with a minimal, clean cut.",
      "footwear": "Semi-sheer pantyhose visible, heels partially cropped out of frame."
    },
    "expression": "Self-assured, playful yet analytical — a modern ‘after-hours office muse’ expression."
  },
  "environment": {
    "setting": "Quiet office interior late at night.",
    "background": "Wide window fitted with metallic horizontal blinds, catching reflections from the flash.",
    "props": "Loose stack of documents and folders resting near her hip on the cabinet surface.",
    "surfaces": "Smooth light-wood laminate cabinet with soft wear marks."
  },
  "lighting": {
    "type": "Built-in camera flash.",
    "quality": "Hard frontal light with pronounced contrast and crisp shadows cast onto the blinds.",
    "mood": "Casual, spontaneous Y2K-era digital snapshot feel."
  },
  "camera_details": {
    "style": "Ultra-photorealistic retro snapshot.",
    "camera": "Early-2000s compact digital camera aesthetic.",
    "lens": "35mm equivalent.",
    "aperture": "f/3.5",
    "shutter": "1/50",
    "iso": "500",
    "focus": "Eyes and glasses in sharp focus, slight falloff toward the edges."
  },
  "style_tags": [
    "Office Muse",
    "Direct Flash",
    "Y2K Digital Aesthetic",
    "Retro Snapshot",
    "Photorealism",
    "High Detail",
    "Natural Texture"
  ]
}
```

[[Margot Robbie Likeness]]

---

### 45. 电影感拳击馆肖像

**Author**: [Keskin](https://x.com/craftian_keskin)  **Date**: 2026-01-24  **Language**: en

> 一个详细的提示，用于生成一张电影级的时尚运动肖像：一位运动型女性在粗犷的拳击馆中回合间隙休息，强调温暖的午后阳光、戏剧性的阴影和奢华的健身美学。

![电影感拳击馆肖像](https://cms-assets.youmind.com/media/1769322264632_esy42q_G_dK3bkXgAMlyov.jpg)

```
Cinematic fashion–sports portrait of an extremely attractive adult blonde woman, athletic and toned, resting between rounds in a gritty boxing gym environment. She is seated casually against a metal structure, wearing black boxing shorts, a black sports bra, and metallic gold boxing gloves. Her posture is relaxed but powerful, conveying confidence, strength, and sensual calm.

She has softly curled blonde hair, slightly messy from exertion, glowing skin with a light sheen of sweat, defined cheekbones, full lips, and striking eyes with subtle makeup. Natural, realistic body proportions and muscle tone.

Warm late-afternoon sunlight streams through the gym, casting dramatic shadows across her body and the textured concrete walls. The color grading is warm and cinematic, with golden highlights and deep, soft shadows. Editorial sports-fashion photography, photorealistic, high detail.

 Visual Style

Cinematic realism
High-end editorial sports photography
Warm golden color grading
Natural skin texture
Soft contrast
Moody, intimate atmosphere
Luxury fitness aesthetic

 Camera & Lighting

50–85mm portrait lens look
Shallow depth of field
Directional natural light
Soft shadow falloff
Balanced exposure
Sharp focus on subject

Mood Keywords

Confident
Powerful
Sensual (tasteful, non-explicit)
Athletic
Editorial
Calm intensity
Modern femininity

Negative Prompt

exaggerated anatomy, distorted limbs, plastic skin, CGI, cartoon style, harsh flash, overprocessed skin, watermark, text, logos
```

[[Dramatic Shadow]] [[Athletic Female]] [[Afternoon Sunlight]]

---

### 46. 高定时装大片：金属流苏外套

**Author**: [bengi](https://x.com/p3rikly)  **Date**: 2026-01-24  **Language**: en

> 一张用于高端时尚杂志的编辑照片的结构化提示。它描述了一位酷似玛格特·罗比 (Margot Robbie) 的女性，身穿一件由金色和橙色金属流苏制成的巨大蓬松外套，蹲伏在一个极简主义的室内。该提示指定了温暖的黄金时段影棚照明，并使用了大量的负面提示，以确保高质量和纹理的真实感。

![高定时装大片：金属流苏外套](https://cms-assets.youmind.com/media/1769322279853_gdgy44_G_c8UP_XIAAxJB2.jpg)

```
{
  "image_generation_data": {
    "prompts": {
      "main_subject": "Full body shot of a woman resembling {argument name="celebrity look alike" default="Margot Robbie"} look alike with shoulder-length wavy, messy blonde hair, hand casually touching her hair.",
      "outfit_description": "She is wearing a massive, voluminous, shaggy oversized coat made of tiered {argument name="coat color" default="gold and orange"} metallic fringe or tinsel texture that mimics faux fur. She is wearing white strappy high-heel sandals.",
      "pose_and_action": "The subject is in a deep squat or crouching pose, tucked into the corner of a room. Her body is angled slightly to the side, knees bent deeply, projecting a relaxed but high-fashion attitude.",
      "environment": "Minimalist interior, the corner of a room with plain cream or off-white walls and a neutral carpeted floor. No furniture visible.",
      "lighting_and_atmosphere": "Warm, golden-hour studio lighting casting soft shadows. The atmosphere is editorial, chic, and warm. High contrast between the metallic texture of the coat and the smooth wall.",
      "camera_settings": "35mm lens, fashion photography style, sharp focus on the face and coat texture, medium-shot."
    },
    "negative_prompts": [
      "standing",
      "straight hair",
      "dark colors",
      "blue tones",
      "low resolution",
      "blur",
      "distorted hands",
      "extra limbs",
      "flat texture",
      "shiny skin"
    ],
    "parameters": {
      "aspect_ratio": "3:4",
      "seed": 847201945,
      "guidance_scale": 7.5,
      "steps": 30,
      "sampler": "DPM++ 2M Karras"
    },
    "combined_prompt_string": "High-fashion editorial photo of a woman with messy blonde hair crouching in a corner, wearing a gigantic voluminous gold metallic fringe coat and white strappy heels. Warm lighting, cream walls, intricate fabric texture, celebrity lookalike, 8k resolution, cinematic lighting --ar 3:4 --stylize 250"
  }
}
```

[[Minimalist Interior]] [[Texture Realism]]

---

### 47. 超逼真调情肖像

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-01-24  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超写实肖像，描绘一位年轻女性，她拥有自然卷发和雀斑，摆出俏皮的眨眼姿势，同时咬着拇指。该提示指定了影棚灯光、技术相机设置（85mm, f/1.8）以及用于高对比度的黑色背景。

![超逼真调情肖像](https://cms-assets.youmind.com/media/1769322252759_crkn7o_G_cnzpsXYAAmIm8.jpg)
![超逼真调情肖像](https://cms-assets.youmind.com/media/1769322254322_p11y6j_G_cnzpmWkAAuDfy.jpg)
![超逼真调情肖像](https://cms-assets.youmind.com/media/1769322254435_ona0h9_G_cnzpnWYAInHXV.jpg)

```
{
  "prompt_structure": {
    "subject": {
      "demographics": "Young woman, early 20s, Caucasian",
      "hair": "Voluminous, shoulder-length blonde hair with tight, defined natural curls/ringlets; messy yet styled texture",
      "face": "Fair complexion, visible freckles or natural skin texture, one blue eye open, distinct facial structure",
      "makeup": "Minimal natural makeup, nude lip, subtle mascara"
    },
    "pose_and_expression": {
      "action": "Biting the thumb of the left hand playfully, head tilted slightly to the right",
      "facial_expression": "Winking left eye, cheeky/flirtatious grin, scrunching nose slightly",
      "gaze": "Direct eye contact with the camera (with the open eye)"
    },
    "attire": {
      "outerwear": "Vintage distressed brown leather jacket, bomber or biker style, worn texture, silver snap button detail on collar",
      "inner_wear": "Black ribbed crew-neck top",
      "styling": "Casual, edgy, cool-girl aesthetic"
    },
    "environment": {
      "background": "Solid, seamless matte black background",
      "context": "Studio portrait setting, minimalistic to focus on subject"
    },
    "lighting": {
      "type": "Soft frontal studio lighting (beauty dish or ring light)",
      "qualities": "Even illumination on the face, creating a catchlight in the eye, soft shadows defining the hair texture, high contrast against the dark background"
    },
    "technical_details": {
      "camera_settings": "85mm portrait lens, aperture f/1.8 for shallow depth of field, sharp focus on the face",
      "perspective": "Eye-level, close-up portrait framing (shoulders and head)"
    },
    "photorealism_and_quality": {
      "style": "Hyper-realistic portrait photography, high fidelity",
      "resolution": "8k, UHD",
      "details": "Detailed skin pores, realistic hair strand rendering, leather texture mapping, cinematic lighting"
    },
    "mood": "Playful, confident, flirtatious, energetic, charismatic, candid"
  }
}
```

[[Freckles]] [[85mm Portrait Lens]] [[Black Background]]

---

### 48. 壮观的城市再现

**Author**: [David](https://x.com/David_eficaz)  **Date**: 2026-01-24  **Language**: en

> 一个提示模板，用于创建壮观的城市再现，可能侧重于建筑细节、灯光和都市氛围。

![壮观的城市再现](https://cms-assets.youmind.com/media/1769322361111_v1xo66_G_citQlWAAAjhce.jpg)

```
Crea espectaculares recreaciones de {argument name="city name" default="ciudades"} con 🍌 Nano Banana Pro.
```

[[Urban Atmosphere]]

---

### 49. 客厅里和猫咪的逼真智能手机自拍

**Author**: [gvyne](https://x.com/gvyneAI)  **Date**: 2026-01-24  **Language**: en

> 一个用于生成逼真智能手机自拍图像的 JSON 提示。它详细描述了拍摄对象（一位有雀斑和金色马尾辫的年轻成年女性）、她的衣着（粉色罗纹短款上衣）、配饰（叠戴的金色项链）以及背景设置（灰色组合沙发、白色门，以及一只蓬松的深色虎斑猫坐在扶手上）。

![客厅里和猫咪的逼真智能手机自拍](https://cms-assets.youmind.com/media/1769322307911_atjcmo_G_cdJXuW8AAb_XB.jpg)

```
"prompt_description": {
    "type": "Realistic smartphone selfie",
    "angle": "High-angle shot, arm extended",
    "subject": {
      "gender": "Female",
      "age": "Young adult",
      "appearance": {
        "hair": "Blonde, tied back in a high ponytail",
        "skin": "Fair with prominent freckles across nose and cheeks",
        "lips": "Full, glossy natural pout",
        "expression": "Looking directly at camera, neutral to slight pout"
      },
      "clothing": {
        "top": "Pale pink/beige ribbed knit sleeveless crop top"
      },
      "accessories": {
        "jewelry": [
          "Layered gold necklaces (one choker length, one longer with a round pendant)",
          "Small gold hoop earrings"
        ]
      }
    },
    "background": {
      "setting": "Indoor living room",
      "key_elements": [
        {
          "object": "Cat",
          "description": "Fluffy, dark tabby/brown long-haired cat sitting on the grey sofa armrest behind the subject."
        },
        {
          "object": "Sofa",
          "description": "Grey fabric sectional couch."
        },
        {
          "object": "Door",
          "description": "Closed white interior door on the left."
        },
        {
          "object": "Hallway",
          "description": "Dark doorway opening in the background."
        }
      ]
    },
    "lighting": "Soft, domestic indoor lighting"
  }
```

[[Smartphone Selfie]] [[Pink Crop Top]]

---

### 50. 超逼真公主风 Cosplay 肖像

**Author**: [Mikasa](https://x.com/Mikasa_rose729)  **Date**: 2026-01-24  **Language**: en

> 一个结构化提示，用于生成一张高度细致、逼真的年轻女性角色扮演图像，风格为“公主核心”，形似长发公主。提示中指定了极长的金金色头发、淡紫色锦缎束身衣、模拟黄金时段的柔和室内暖光，以及高保真技术规格（8K、锐利聚焦、电影级照明）。

![超逼真公主风 Cosplay 肖像](https://cms-assets.youmind.com/media/1769322277571_kv0civ_G_ca3BTWAAA-mJk.jpg)

```
{
  "prompt_metadata": {
    "style": "Photorealistic, Cosplay Photography, Princess-core",
    "resolution": "4K, 8K, Ultra HD",
    "aspect_ratio": "Variable (Portrait or Square)",
    "lighting": "Soft indoor warm lighting, golden hour simulation"
  },
  "visual_elements": {
    "subject": {
      "description": "Young woman with fair skin and a soft, feminine aesthetic.",
      "hair": "Extremely long, flowing {argument name="hair color" default="golden blonde"} hair extending past the waist, styled straight with slight waves at the ends, featuring wispy curtain bangs framing the face.",
      "makeup": "Rosy flushed cheeks (heavy blush focus), glossy lips, soft eye makeup, glowing complexion."
    },
    "outfit": {
      "top": "{argument name="corset color" default="Lavender/purple"} brocade corset bodice with intricate floral or damask jacquard patterning. Features a sweetheart neckline trimmed with ruffled pink lace. Adorned with a large satin bow at the center front, combining baby blue and light pink ribbons.",
      "bottom": "Short, ruffled white or pale lavender skirt (visible in lower poses).",
      "accessories": "A sparkling, jeweled tiara/crown with silver setting and crystals sitting atop the head. Dangling pearl or crystal earrings."
    },
    "props": "Holding a round hairbrush or curling wand (visible in one variation).",
    "environment": "Indoor bedroom or dressing room setting, cream or white walls, soft ambient background, slightly candid vibe."
  },
  "technical_specifications": {
    "camera_settings": "Shot on 35mm lens, f/1.8 aperture for shallow depth of field.",
    "quality_tags": [
      "highly detailed",
      "photorealistic",
      "8k resolution",
      "HDR",
      "sharp focus on eyes",
      "cinematic lighting",
      "soft textures",
      "high fidelity"
    ]
  },
  "full_prompt_string": "A highly detailed, photorealistic 4k photo of a young woman cosplaying as Rapunzel. She has extremely long, flowing golden blonde hair reaching past her waist with curtain bangs and is wearing a sparkling jeweled tiara. She is dressed in a lavender brocade corset with intricate damask patterns, trimmed with pink ruffled lace and tied with baby blue and pink satin ribbons at the center. Her makeup features rosy cheeks and glossy lips. The lighting is soft and warm, imitating golden hour indoor bedroom lighting. The image quality is 8k, ultra-hd, cinematic, with sharp focus on the textures of the corset and hair."
}
```

[[8K Photorealism]]

---

### 51. 巴塞罗那女球迷团体照

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个高度详细的 JSON 提示，用于 SuperGrok AI（不是 Nano Banana Pro，但作为结构化提示包含在内以求完整性），以生成一张四位年轻女性身穿相同巴塞罗那足球队球衣，在现代体育场内拍摄的逼真团体肖像，捕捉具有特定姿势和灯光的网红抓拍美学。

![巴塞罗那女球迷团体照](https://cms-assets.youmind.com/media/1769322326470_bk314r_G_cY9UyaUAARN3C.jpg)

```
{
  "prompt_type": "photorealistic_group_portrait",
  "subjects": {
    "count": 4,
    "demographic": "Young Woman Gen-Z aesthetic",
    "Skin":[
     "Fair skin tone",
     "Light skin tone",
     "Light tan skin tone",
     "Fair skin tone"
    ]
  },
    "hair_styles": [
      "Long straight brown hair",
      "Sleek high ponytail",
      "Long wavy brown hair",
      "Sleek pulled-back bun"
    ]
  },
  "attire": {
    "tops": "Matching barcelona football jerseys (2023-2024 Home Kit)   
    "bottoms": [
      "Light blue oversized cargo denim jeans",
      "White trousers"
    ],
    "accessories": {
      "jewelry": "Gold hoop earrings, gold chain necklaces, gold wristwatches, gold cuff bracelets",
      "bags": "Vintage-style brown leather shoulder bag with front utility pockets, silver stud detailing, and chain strap (held by the woman in the foreground)"
    }
  },
  "poses_and_expressions": {
    "foreground_left_woman": "Winking playfully with mouth open in a laugh, holding up a peace sign (V-sign) with left hand, leaning forward",
    "foreground_right_woman": "Sitting with legs crossed or relaxed, smiling brightly, looking directly at camera, hands resting on knees",
    "background_left_woman": "Smiling warmly, sitting slightly behind the foreground subject, arm resting near the other's shoulder",
    "background_center_woman": "Standing or sitting at the highest point in the group, smiling gently, head tilted slightly"
  },
  "environment": {
    "location": "Modern football stadium stands (likely Santiago Bernabéu)",
    "details": "Rows of empty dark blue plastic stadium seats, glass safety barriers in the background, concrete steps",
    "atmosphere": "Exciting match day vibe, exclusive VIP section feeling"
  },
  "lighting": {
    "type": "Natural daylight",
    "quality": "Soft sunlight coming from the right side, creating gentle highlights on faces and hair, casting realistic shadows",
    "tone": "Warm, golden hour glow"
  },
  "technical_specs": {
    "resolution": "4K Ultra HD",
    "aspect_ratio": "9:16",
    "style": "Candid influencer social media shot, high fidelity, sharp focus, vibrant colors, cinematic depth of field",
    "camera_settings": "Fast shutter speed, wide aperture (f/2.8) to blur background slightly"
  }
}
```

[[Group Portrait]]

---

### 52. 热带海滩肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张超逼真、专业的年轻女性在热带海滩上的照片，重点突出鲜艳的色彩、强烈的头顶阳光，以及草帽和白色连衣裙等特定的夏季服饰。

![热带海滩肖像](https://cms-assets.youmind.com/media/1769322265438_3fuvdo_G_cUSqOa0AAbTFm.jpg)
![热带海滩肖像](https://cms-assets.youmind.com/media/1769322266039_7qgqag_G_cUSmjbQAA3k9L.jpg)

```
{
  "image_generation_request": {
    "character_profile": {
      "subject": "Young woman",
      "skin_tone": "Fair",
      "hair": {
        "color": "Long, platinum blonde",
        "style": "Straight, neatly styled, falling over one shoulder"
      },
      "facial_features": {
        "face_shape": "Oval",
        "lips": "Full, glossy red lipstick",
        "expression": "Serene, looking straight at camera"
      },
      "body_type": "Athletic and curvy"
    },
    "attire_and_accessories": {
      "clothing": "White summer dress with thin spaghetti straps",
      "headwear": "Wide-brimmed beige straw hat with a black ribbon band",
      "eyewear": "Round gold-rimmed sunglasses with reflective lenses",
      "jewelry": [
        "Delicate gold necklace with a small sparkling heart charm",
        "Beaded bracelet with small colorful charms on left wrist"
      ]
    },
    "environment": {
      "location": "Tropical beach shoreline",
      "background": "Clear turquoise sea, distant blue horizon, light blue sky with scattered white clouds",
      "lighting": "Natural, strong overhead sunlight creating distinct shadows on the shoulder",
      "atmosphere": "Vibrant, bright, tropical, summer vacation"
    },
    "technical_specifications": {
      "shot_type": "Medium shot",
      "composition": "Centered, both hands resting at sides",
      "quality": "Hyper-realistic, professional photography, masterpiece, 8k",
      "color_palette": "Dominant turquoise and white, high saturation"
    }
  }
}
```

[[Vibrant Colors]] [[Summer Fashion]]

---

### 53. 韩国恐怖电影不祥 DVD 屏摄

**Author**: [Christopher Fryant](https://x.com/cfryant)  **Date**: 2026-01-24  **Language**: en

> 一个简短而具体的提示，要求生成一张 2001 年韩国恐怖电影 DVD 截图风格的图片。场景是一个不祥的、非常黑暗的家庭晚餐，涉及一个巨人，并明确指示比例应“完全错误”，且不应出现任何文本叠加。

![韩国恐怖电影不祥 DVD 屏摄](https://cms-assets.youmind.com/media/1769322313405_9df6ej_G_cTOdnXAAEEVnQ.jpg)

```
dvd screengrab of a Korean horror movie from 2001. The proportions are all wrong.

Ominous domestic dinner scene involving a giant man. Very dark.

No text, no DVD overlay
```

[[No Text Overlay]]

---

### 54. 电影级产品展示视频提示（针织家居服）

**Author**: [Nano Photo AI](https://x.com/NanoPhotoAI)  **Date**: 2026-01-24  **Language**: zh

> 一个详细的视频故事板提示（可能用于 Sora/Kling，通过 NanoPhotoAI 生成），旨在为 15 秒的针织家居服电影级产品展示。它侧重于纹理、设计细节，并通过特定的摄像机运动和灯光变化营造舒适的氛围。

```
## Structure (total 15s; mode: Cinematic Product Showcase)

**0-5秒 [全景展示与氛围营造]:**
镜头以微微仰视的角度开场，展示这套米灰色条纹针织家居服套装悬浮在一个明亮、洁净且带有柔和自然光的极...
```

[[Cozy Atmosphere]]

---

### 55. 猫咪嘴套佩戴视频教程

**Author**: [Nano Photo AI](https://x.com/NanoPhotoAI)  **Date**: 2026-01-24  **Language**: zh

> 一个视频分镜脚本提示（可能用于 Sora/Kling，通过 NanoPhotoAI 生成），描述了一个特写场景：一名男子迅速给一只橘色虎斑猫戴上一个透明的猫头形防咬口罩，强调了猫咪困惑的表情以及手持摄像机的运动。

```
| 镜号 | 景别/角度 | 运动 | 画面内容 | 音频 | 时长(秒) |
|------|-----------|------|----------|------|----------|
| 1 | 特写/平视 | 固定/微动 | 室内光线下，一双男性的手拿着一个透明的、猫头形状的硬塑料防咬面罩，迅速套在一只橘色虎斑猫的头上。猫咪身体被包裹在蓝色条纹毛巾或衣物中，表情看起来有些懵懂。画...
```

[[Tabby Cat]]

---

### 56. 翻毛皮风衣展示视频提示

**Author**: [Nano Photo AI](https://x.com/NanoPhotoAI)  **Date**: 2026-01-24  **Language**: zh

> 一个视频分镜脚本提示（很可能是为 Sora/Kling 通过 NanoPhotoAI 创建），描述了一个静态镜头，聚焦于一位女性的躯干，她身穿棕色麂皮风衣、黑色高领毛衣和深蓝色牛仔裤。重点在于柔和的光线下展示风衣的质地和材质品质。

```
| 镜号 | 景别/角度 | 运动 | 画面内容 | 音频 | 时长(秒) |
|------|-----------|------|----------|------|----------|
| 1 | 中景/平视 | 固定 (图片) | 画面展示一位女性身穿棕色绒面革风衣的躯干部分，双手插兜。内搭黑色高领毛衣，下身着深蓝色牛仔裤。光线柔和，重点展示大衣的材质质感。 | BGM:...
```

[[Soft Lighting]] [[Fabric Texture Detail]]

---

### 57. 视频提示：“笨拙的借口”场景

**Author**: [Nano Photo AI](https://x.com/NanoPhotoAI)  **Date**: 2026-01-24  **Language**: zh

> 一个详细的提示，用于使用 Nano Banana Pro（通过话题标签暗示）或类似 AI 视频工具（如 Sora）生成一段短视频（30-40 秒）。场景中，一个笨拙的企鹅角色 @xithink.pebblepeng 在雪地环境中与一个红色怪物互动，强调采用倾斜构图（Dutch Angle）和特定照明以营造戏剧效果。

```
1. 以参考图为背景： 雪地局部，企鹅和红毛怪的对峙。
2. 画面描述： @xithink.pebblepeng 终于把头部从雪里抽出来，一脸呆滞，憨憨的样子，看到红毛怪发火，它吓得一摇一摆地后退，翅膀僵硬地指着远处山那边的方向，眼睛心虚地乱转，一副“我是路痴我无辜”的蠢萌样。
3. 运镜： 荷兰角（Dutch Angle）倾斜构图，表现企鹅的慌乱和荒谬感。
4. 灯光：...
```

[[Dutch Angle]] [[Animated Character]]

---

### 58. 雪中无助白虎幼崽的视频提示

**Author**: [Nano Photo AI](https://x.com/NanoPhotoAI)  **Date**: 2026-01-24  **Language**: zh

> 一个视频故事板提示（可能用于 Sora/Kling，通过 NanoPhotoAI 生成），描述了一个 3-5 秒的短场景：一只小白虎无助地躺在一个深雪坑里，用它那双湿漉漉的大眼睛四处张望。镜头采用缓慢、低角度的手持运镜，以唤起人们的怜悯之情。

```
弱小无助 (3-5s)

1. 以参考图为背景： 视线降低到地面高度，背景是模糊的雪地颗粒。
2. 画面描述： @xithink.blizzytige (小白虎) 独自趴在深雪坑里，全身绒毛随着寒风颤抖。它抬起头，那双湿润的大眼睛（眼大萌）无助地四处张望，发出无声的哀鸣，前爪不安地刨着雪。
3. 运镜： 缓慢的低角度手持摇摄（Handheld），模拟旁观者怜悯的视角。
4. 灯光：...
```

[[Snow Setting]]

---

### 59. 克什米尔冬季旅行摄影

**Author**: [𝘬𝘦𝘭𝘭𝘺](https://x.com/kelly00056)  **Date**: 2026-01-24  **Language**: en

> 一个详细的提示，用于生成一张超现实的、国家地理风格的名人（西德尼·斯威尼）旅行照片，描绘她在克什米尔的达尔湖上享受一个神奇的冬日早晨，坐在一艘被雪覆盖的传统希卡拉船中，强调体积光和超细节纹理。

![克什米尔冬季旅行摄影](https://cms-assets.youmind.com/media/1769322271280_ghtpr4_G_cFeXPaMAAx_hk.jpg)

```
Sydney Sweeney peacefully enjoying a magical winter morning on Dal Lake, Kashmir, sitting inside a beautifully carved traditional wooden shikara covered with a light layer of fresh snow. Gentle snowfall in the air, soft fog floating above the lake surface, mirror-like reflections in the water. She is wrapped in an elegant Kashmiri pashmina shawl, warm woolen outfit, holding a cup of steaming kahwa, smiling softly while looking at the snowy Himalayan mountains in the distance.

The shikara is decorated with vibrant Kashmiri embroidery cushions, flowers slightly covered in snow, and a small lantern glowing warmly inside. Snowflakes resting on her hair and shawl. Surrounding lake filled with other blurred shikaras and tourists in the background, cinematic depth of field.

Morning golden light breaking through clouds, volumetric lighting rays, ultra realistic water reflections, 8K hyper-detailed textures, National Geographic style photography, Sony A7R V, 85mm lens, f/1.8, HDR, natural skin tones, cozy winter aesthetic, peaceful luxury travel vibe, unreal cinematic atmosphere, soft color grading, masterpiece photography.

trending travel photography, viral winter aesthetic, dream destination vibe, ultra photorealistic, award winning shot, Instagram editorial quality
```

[[Volumetric Light]] [[Sydney Sweeney Likeness]] [[National Geographic Style]]

---

### 60. 夜城背景下的电影三联肖像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-24  **Language**: en

> 一个复杂的提示，要求 AI 使用上传的照片进行精确的身份参考，并生成一张电影感十足的写实三联画（一张图片包含三个画面）。场景设定在城市夜晚的桥上，通过三种不同的镜头（广角、中景、特写）捕捉拍摄对象，以传达自由、动感和都市浪漫的氛围。

![夜城背景下的电影三联肖像](https://cms-assets.youmind.com/media/1769322282428_td6dsa_G_cFKuwXEAEe9OJ.jpg)

```
use the uploaded photo as the exact identity reference. keep the same person, same face, same facial features, same proportions and natural expression, create a photorealistic cinematic triptych portrait (three-frame composition in one image).

scene: night city, bridge over a busy road, moving cars, glowing street lights, evening sky, city skyline in the background. atmosphere: freedom, motion, youth, urban romance, feeling of wind and road. frame 1 (top): wide cinematic shot - the person standing on a bridge above a busy road, slight motion blur from head movement, city lights and cars below, strong urban night mood. frame 2 (middle): medium shot person leaning on the bridge railing, looking up at the sky, relaxed confident pose, cars and headlights glowing behind. frame 3 (bottom): close-up emotional portrait wind in hair, city lights in bokeh behind, thoughtful and dreamy expression. style: real photography, cinematic lifestyle portrait, urban fashion photography. lighting, natural city night lighting, street lamps, car headlights, soft glow on skin. camera: full-frame dslr, 85mm lens look, shallow depth of field. color grading: warm city lights mixed with cool blue night tones, film-style mood. ultra photorealistic, natural skin texture, real candid moment, no illustration, no cgi, no plastic skin, no text, no logos, no watermark.
```

[[Identity Reference]] [[Urban Night Photography]]

---

### 61. Seedream 4.5（豆包）的韩系美学肖像画提示词

**Author**: [骑司Chase](https://x.com/qisi_ai)  **Date**: 2026-01-24  **Language**: zh

> 一个用于 Seedream 4.5 模型（豆包）的简体中文提示词，与复杂的 Nano Banana Pro 提示词相比，它能生成更出色的韩系美学肖像。用户概述了简化过程（移除 JSON、冗余和使用抽象词汇），并提供了最终的简洁提示词，该提示词侧重于特定的面部特征、妆容、配饰和构图，以打造“甜酷”的韩国女团造型。

![Seedream 4.5（豆包）的韩系美学肖像画提示词](https://cms-assets.youmind.com/media/1769322340685_514j21_G_bdvEvXgAAZ38e.jpg)
![Seedream 4.5（豆包）的韩系美学肖像画提示词](https://cms-assets.youmind.com/media/1769322340740_mo3tkd_G_bdiEiaYAAY2zF.jpg)

```
4宫格拼图，3:4比例，2×2排列；近景特写，平视近拍，人物占比大，冷白干净背景。参考图严格同一人、零偏差；精致脸、大眼、右眼下小痣、细鼻梁；冷粉白皙，轻柔焦但保留细节，面中高光，鼻尖脸颊微红，少量雀斑。韩系清透淡妆，粉腮红扫到鼻梁，水润渐变唇。黑色中分长直发＋少量碎发；左右粉色发夹金属可见。手靠近脸唇突出细节：超长浅色闪片立体美甲＋多枚粉色糖果花朵戒指。白毛绒外搭＋浅粉吊带露肩；甜酷软糯。四格动作：托脸冷淡微委屈；触唇平静略撩；桌沿侧看放空；抵下巴克制微笑。高亮柔光、低对比、阴影浅；冷白主调粉色点缀；背景弱虚化少纹理；写实韩杂女团质感，轻玻璃光泽。
```

[[Korean Aesthetic Portrait]]

---

### 62. 电影风格时尚大片：男人、豪车与爱犬

**Author**: [𝗦𝗮𝗿𝗶𝗺](https://x.com/Sareem48)  **Date**: 2026-01-24  **Language**: en

> 一个复杂、结构化的提示，用于生成一张超现实的电影级时尚大片肖像，描绘一位时尚男士。场景设定在现代都市的夜晚，主体斜倚在一辆充满活力的向日葵黄色豪华轿车旁，一只白色蓬松的小狗乖巧地坐在引擎盖上。提示详细描述了服装、姿势和电影般的灯光（冷蓝色调和深邃阴影，点缀着暖色调）。

![电影风格时尚大片：男人、豪车与爱犬](https://cms-assets.youmind.com/media/1769322292159_sfjsj8_G_b7KzrXwAA7zXz.jpg)
![电影风格时尚大片：男人、豪车与爱犬](https://cms-assets.youmind.com/media/1769322292179_8nuswb_G_b7K9HWcAI1BTf.jpg)

```
{

"reference_image": "uploaded_photo",
{
  "Objective": "Create an ultra-realistic cinematic full-body fashion editorial portrait with a luxury lifestyle mood set in a modern urban night environment.",
  "Persona_Details": {
    "Subject": "Stylish young adult man with a masculine build",
    "Appearance": {
      "Facial_Hair": "Thick, well-groomed full beard and mustache",
      "Hair": "Modern fade haircut with a styled pompadour top",
      "Expression": "Stoic, confident, looking directly at the camera",
      "Eyewear": "{argument name="sunglasses style" default="Red-tinted aviator-style sunglasses"}"
    },
    "Pose_and_Body_Language": {
      "Position": "Leaning casually against the front center of a vehicle",
      "Hand_Action": "Right hand resting on the hood, left hand in pants pocket",
      "Posture": "Relaxed yet powerful stance, centered in the frame"
    }
  },
  "Wardrobe": {
    "Top": "Light sky-blue button-up shirt, slim fit, top buttons open, sleeves rolled to the forearms",
    "Bottoms": "Tailored black chinos with a black leather belt",
    "Footwear": "Crisp, minimalist white leather sneakers",
    "Style": "High-end urban casual"
  },
  "Secondary_Subject": {
    "Animal": "Small white fluffy dog ({argument name="dog breed" default="Maltese or Havanese"} breed)",
    "Behavior": "Sitting obediently on the hood of the car to the left of the man",
    "Interaction": "Calm companionship, facing forward"
  },
  "Vehicle": {
    "Type": "Modern luxury sedan or SUV (BMW-style front grille)",
    "Color": "Vibrant sunflower yellow",
    "Details": "European-style license plate reading 'BR 29', polished paint reflecting ambient light"
  },
  "Scene_and_Environment": {
    "Location": "Open-air modern parking lot at night",
    "Setting_Details": {
      "Surface": "Smooth grey asphalt with clean white parking lines",
      "Sky": "Deep navy night sky with a thin crescent moon in the upper right"
    },
    "Background": {
      "Lighting": "Tall, modern LED streetlights with a soft glow, blurred city lights in the far distance",
      "Atmosphere": "Quiet, exclusive, high-end urban atmosphere"
    }
  },
  "Lighting_and_Mood": {
    "Lighting_Style": "Balanced cinematic lighting, soft key light on the subjects",
    "Primary_Tones": "Cool evening blues and deep shadows",
    "Accent_Tones": "Warm yellow from the car, red highlights from the sunglasses",
    "Mood": "Sophisticated, serene, and premium"
  },
  "Photography_Style": {
    "Genre": "Commercial fashion photography",
    "Aesthetic": "Clean, sharp, high-production value",
```

[[Male Fashion Editorial]]

---

### 63. 身穿皇家马德里球衣的名人合影

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2026-01-24  **Language**: en

> 一个结构化的提示词，用于生成一张逼真的团体肖像，描绘四位年轻女性（灵感来自 Sydney Sweeney、Millie Bobby Brown、Sadie Sink 和 Ana de Armas），她们身穿配套的皇家马德里足球队球衣，置身于一座现代体育场内。该提示词详细描述了她们的特定姿势、表情（眨眼、微笑）、配饰（黄金首饰、复古包）、环境（圣地亚哥·伯纳乌球场看台）以及技术规格（4K、电影级景深、网红抓拍风格）。

![身穿皇家马德里球衣的名人合影](https://cms-assets.youmind.com/media/1769322320015_qspgx1_G_bzhEoXUAAqRj4.jpg)

```
{
  "prompt_type": "photorealistic_group_portrait",
  "subjects": {
    "count": 4,
    "demographic": "Young Woman Gen-Z aesthetic",
    "Skin":[
     "Fair skin tone",
     "Light skin tone",
     "Light tan skin tone",
     "Fair skin tone"
    ]
  },
    "hair_styles": [
      "Long straight brown hair",
      "Sleek high ponytail",
      "Long wavy brown hair",
      "Sleek pulled-back bun"
    ]
  },
  "attire": {
    "tops": "Matching white {argument name="team jersey" default="Real Madrid"} football jerseys (2023-2024 Home Kit) featuring black Adidas stripes on shoulders, gold detailing, 'Emirates FLY BETTER' sponsor logo on chest, club crest on left chest, 'HP' sponsor logo on left sleeve",
    "bottoms": [
      "Light blue oversized cargo denim jeans",
      "White trousers"
    ],
    "accessories": {
      "jewelry": "Gold hoop earrings, gold chain necklaces, gold wristwatches, gold cuff bracelets",
      "bags": "Vintage-style brown leather shoulder bag with front utility pockets, silver stud detailing, and chain strap (held by the woman in the foreground)"
    }
  },
  "poses_and_expressions": {
    "foreground_left_woman": "Winking playfully with mouth open in a laugh, holding up a peace sign (V-sign) with left hand, leaning forward",
    "foreground_right_woman": "Sitting with legs crossed or relaxed, smiling brightly, looking directly at camera, hands resting on knees",
    "background_left_woman": "Smiling warmly, sitting slightly behind the foreground subject, arm resting near the other's shoulder",
    "background_center_woman": "Standing or sitting at the highest point in the group, smiling gently, head tilted slightly"
  },
  "environment": {
    "location": "Modern football stadium stands (likely Santiago Bernabéu)",
    "details": "Rows of empty dark blue plastic stadium seats, glass safety barriers in the background, concrete steps",
    "atmosphere": "Exciting match day vibe, exclusive VIP section feeling"
  },
  "lighting": {
    "type": "Natural daylight",
    "quality": "Soft sunlight coming from the right side, creating gentle highlights on faces and hair, casting realistic shadows",
    "tone": "Warm, golden hour glow"
  },
  "technical_specs": {
    "resolution": "4K Ultra HD",
    "aspect_ratio": "9:16",
    "style": "Candid influencer social media shot, high fidelity, sharp focus, vibrant colors, cinematic depth of field",
    "camera_settings": "Fast shutter speed, wide aperture (f/2.8) to blur background slightly"
  }
}
```

[[Group Portrait]]

---

### 64. 图像中的准确文本渲染

**Author**: [Hasan Toor](https://x.com/hasantoxr)  **Date**: 2026-01-24  **Language**: en

> 这条推文描述了 Nano Banana Pro 的一个关键功能：它能够在生成的图像中渲染清晰准确的文本（徽标、模型、广告、包装），这意味着它具备专注于设计和排版的提示功能。

```
Render sharp, accurate TEXT inside images (logos, UI mockups, ads, packaging)
```

[[Typography In Image]]

---

### 65. 茅台品牌 3x3 故事板设计提示

**Author**: [松果先森](https://x.com/songguoxiansen)  **Date**: 2026-01-24  **Language**: en

> 一个全面的提示，用于生成一个 3x3 的视觉故事板网格，展示茅台酒瓶的九种独特、高端、编辑风格的构图。它需要上传参考图像以严格锁定产品标识，并侧重于所有面板的材质纹理、光照一致性和设计驱动的美学。

![茅台品牌 3x3 故事板设计提示](https://cms-assets.youmind.com/media/1769408671978_4x2abs_G_br_bDacAABZUa.jpg)

```
A clean 3×3 storyboard grid with nine equal sized panels on 4:5 ratio.

Use the reference image as the base product reference. Keep the same product, packaging design, branding, materials, colors, proportions and overall identity across all nine panels exactly as the reference. The product must remain clearly recognizable in every frame. The label, logo and proportions must stay exactly the same.

This storyboard is a high-end designer mockup presentation for a branding portfolio. The focus is on form, composition, materiality and visual rhythm rather than realism or lifestyle narrative. The overall look should feel curated, editorial and design-driven.

**FRAME 1:**
Front-facing hero shot of the {argument name="product name" default="茅台白酒"} in a clean studio setup. Neutral background, balanced composition, calm and confident presentation showing the complete product with 瓶身浮雕 and 酒标烫金.

**FRAME 2:**
Close-up shot with the focus centered on the {argument name="product name" default="茅台白酒"}'s 酒标烫金. Focusing on 玻璃、陶瓷 textures, precision craftsmanship, and 液体透明度.

**FRAME 3:**
Shows the {argument name="product name" default="茅台白酒"} placed in a 中式餐桌 environment. Studio setting inspired by 高端典雅 aesthetics - clean lines, natural materials, soft lighting, creating an authentic brand atmosphere.

**FRAME 4:**
Product shown in use or interaction on a neutral studio background. Hands in natural gesture 优雅地倾倒酒液, capturing the human-product connection, the look matches the 高端典雅 aesthetic.

**FRAME 5:**
Isometric composition showing multiple {argument name="product name" default="茅台白酒"} units arranged in a precise geometric order from the top isometric angle. All products placed at the same isometric top angle, evenly spaced, clean, structured and graphic.

**FRAME 6:**
{argument name="product name" default="茅台白酒"} levitating slightly tilted on a neutral background that matches the brand color palette. Floating position is angled and intentional, the product is floating naturally in space with dramatic lighting effects.

**FRAME 7:**
Extreme close-up focusing on specific detail of the {argument name="product name" default="茅台白酒"} - 瓶盖密封, material micro-texture, or precision engineering details.

**FRAME 8:**
The {argument name="product name" default="茅台白酒"} in an unexpected yet aesthetically strong setting that feels bold, editorial and visually striking. 悬浮在酒液飞溅的瞬间, studio-based and designer-driven, bold composition that elevates the brand.

**FRAME 9:**
Wide composition showing the product in use within a refined lifestyle setup. Clean props, controlled styling, cohesive with the rest of the series, suggesting the product's role in daily life.

**CAMERA & STYLE:**
Ultra high-quality studio imagery with a real camera look. Different camera angles and framings across frames. Controlled depth of field, precise lighting, accurate materials and reflections. dramatic contrast with golden highlights. Lighting logic, color palette, mood and visual language must remain consistent across all nine panels as one cohesive series.

**OUTPUT:**
A clean 3×3 grid with no borders, no text, no captions and no watermarks.
```

[[Editorial Design]]

---

### 66. 现代卧室中逼真的后视镜自拍

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-01-24  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超逼真的镜面自拍图像。主体是一位身材健美的年轻女性，留着被阳光晒白的金色头发，正在后视镜中摆拍自拍。该提示详细说明了她的着装（一件宽松的灰色卫衣，滑落至肩部；紧身白色氨纶短裤）、现代卧室环境（大窗户、琴叶榕植物）以及灯光（柔和、漫射的自然日光），营造出一种随意、自信的氛围。

![现代卧室中逼真的后视镜自拍](https://cms-assets.youmind.com/media/1769322316266_38xigj_G_bqVvsWQAAJfG2.jpg)

```
{
"subject": {
"description": "Young woman with tanned skin and long, wavy, sun-bleached balayage blonde hair standing in a bedroom.",
"body_type": "Fit, curvy physique with prominent gluteal shape and natural proportions.",
"attire": {
"upper_body": "Oversized heather grey crewneck sweatshirt, worn loosely and falling off the left shoulder to reveal the shoulder blade and strap-free skin. Partial navy blue text visible on the front.",
"lower_body": "Tight white spandex athletic shorts (biker shorts style) that conform closely to the hips and glutes."
},
"hair": "Long, textured beach waves falling over the left shoulder and down the back, dark roots transitioning to honey blonde ends.",
"details": "Natural skin texture, visible tan lines or skin tone variation, subtle jewelry on neck."
},
"pose": {
"type": "Standing rear-view mirror selfie pose.",
"orientation": "Body angled away from the camera (mirror surface), back turned towards the viewer.",
"head_position": "Head turned sharply over the left shoulder, looking directly into the mirror/camera lens.",
"arms": "Right arm raised holding a black smartphone to take the photo; left arm relaxed by the side.",
"spine_and_hips": "Natural standing posture with weight slightly shifted, emphasizing the curve of the lower back and glutes.",
"specifics": "Shoulder blades subtly visible due to the off-shoulder sweatshirt."
},
"environment": {
"setting": "Bright, modern bedroom interior.",
"elements": [
"Large vertical window on the left with black frame and white sill.",
"Large artificial fiddle leaf fig plant with broad green leaves positioned in front of the window.",
"Wooden dresser or chest of drawers in the background (right side) with a separate square mirror resting on it.",
"Corner of a bed with white linens visible in the lower right foreground.",
"Dark grey or brown carpeted flooring.",
"White walls."
]
},
"camera": {
"shot_type": "Mirror selfie, reflection shot.",
"perspective": "Eye-level relative to the reflection.",
"framing": "Medium shot capturing from the upper thighs to the top of the head.",
"device": "Black Apple iPhone with triple-lens camera system visible in the right hand, partially obscuring the face.",
"focal_length": "26mm equivalent (smartphone main camera).",
"depth_of_field": "Deep depth of field, background elements slightly softer but distinct."
},
"lighting": {
"source": "Natural daylight entering from the large window on the left.",
"quality": "Soft, diffused directional light illuminating the left side of the subject and casting soft shadows on the right side of the body.",
"shadows": "Natural contact shadows in clothing folds and on the right side of the torso/legs.",
"ambience": "Bright, airy, daytime interior illumination."
},
"mood_and_expression": {
"mood": "Casual, relaxed, confident.",
"expression": "Neutral to soft gaze, focused on the phone screen/reflection, partially hidden by th"
}}
```

[[Natural Sunlight]]

---

### 67. 长发公主 Cosplay 超逼真肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个详细的 JSON 提示，用于 Gemini Nano Banana Pro 生成一张年轻女性扮演长发公主的超逼真图像，强调其极其长的金金色头发、淡紫色锦缎紧身胸衣，以及模拟黄金时段的柔和温暖室内照明。

![长发公主 Cosplay 超逼真肖像](https://cms-assets.youmind.com/media/1769322330470_8jxt6t_G_bl0V_XMAAfgPP.jpg)

```
{
  "prompt_metadata": {
    "style": "Photorealistic, Cosplay Photography, Princess-core",
    "resolution": "4K, 8K, Ultra HD",
    "aspect_ratio": "Variable (Portrait or Square)",
    "lighting": "Soft indoor warm lighting, golden hour simulation"
  },
  "visual_elements": {
    "subject": {
      "description": "Young woman with fair skin and a soft, feminine aesthetic.",
      "hair": "Extremely long, flowing golden blonde hair extending past the waist, styled straight with slight waves at the ends, featuring wispy curtain bangs framing the face.",
      "makeup": "Rosy flushed cheeks (heavy blush focus), glossy lips, soft eye makeup, glowing complexion."
    },
    "outfit": {
      "top": "Lavender/purple brocade corset bodice with intricate floral or damask jacquard patterning. Features a sweetheart neckline trimmed with ruffled pink lace. Adorned with a large satin bow at the center front, combining baby blue and light pink ribbons.",
      "bottom": "Short, ruffled white or pale lavender skirt (visible in lower poses).",
      "accessories": "A sparkling, jeweled tiara/crown with silver setting and crystals sitting atop the head. Dangling pearl or crystal earrings."
    },
    "props": "Holding a round hairbrush or curling wand (visible in one variation).",
    "environment": "Indoor bedroom or dressing room setting, cream or white walls, soft ambient background, slightly candid vibe."
  },
  "technical_specifications": {
    "camera_settings": "Shot on 35mm lens, f/1.8 aperture for shallow depth of field.",
    "quality_tags": [
      "highly detailed",
      "photorealistic",
      "8k resolution",
      "HDR",
      "sharp focus on eyes",
      "cinematic lighting",
      "soft textures",
      "high fidelity"
    ]
  },
  "full_prompt_string": "A highly detailed, photorealistic 4k photo of a young woman cosplaying as Rapunzel. She has extremely long, flowing golden blonde hair reaching past her waist with curtain bangs and is wearing a sparkling jeweled tiara. She is dressed in a lavender brocade corset with intricate damask patterns, trimmed with pink ruffled lace and tied with baby blue and pink satin ribbons at the center. Her makeup features rosy cheeks and glossy lips. The lighting is soft and warm, imitating golden hour indoor bedroom lighting. The image quality is 8k, ultra-hd, cinematic, with sharp focus on the textures of the corset and hair."
}
```

[[Identity Reference]] [[Warm Indoor Lighting]]

---

### 68. 强调动感的高级时装电影感肖像

**Author**: [Hoor](https://x.com/sassyayra_)  **Date**: 2026-01-24  **Language**: en

> 一个用于生成女性主题时尚电影肖像的结构化提示。目标是强调戏剧性的动感，主体站在屋顶或悬崖边，身处强风之中，身穿飘逸的长裙或斗篷，在广阔的天空下随风剧烈翻腾。

![强调动感的高级时装电影感肖像](https://cms-assets.youmind.com/media/1769322293013_sjf8g5_G_bi7ZGWYAAkkO-.jpg)

```
{
  "render_goal": "High-fashion cinematic portrait emphasizing motion",
  "subject": {
    "gender": "female",
    "pose": "standing in strong wind",
    "expression": "powerful, composed"
  },
  "wardrobe": {
    "outfit": "long flowing {argument name="garment type" default="dress or cape"}",
    "fabric_behavior": "dramatic movement in wind"
  },
  "environment": {
    "location": "{argument name="location" default="open rooftop or cliff edge"}",
    "atmosphere": "wide open sky"
  },
  "lighting_and_color": {
    "lighting_style": "dramatic cinematic",
    "color_palette": "bold contrasts"
  }
}
```

[[Flowing Gown]]

---

### 69. AI 转型为 Dryad

**Author**: [ちゃろん](https://x.com/charon_artist)  **Date**: 2026-01-24  **Language**: ja

> 这是一个与 Nano Banana Pro 配合使用的提示，用于将上传的图像转换为树精，重点在于与森林融为一体的精灵主题，并唤起大自然的气息。用户指出该提示写在图像的 ALT 文本中。

![AI 转型为 Dryad](https://cms-assets.youmind.com/media/1769322352992_guxwz0_G_big9mWkAAdWc_.jpg)

```
AIで{argument name="キャラクター" default="ドライアド"}に変換してみた

森と一つになった精霊…🌲
自然の息吹を感じてください✨
```

[[Fantasy Portrait]]

---

### 70. 身着垂坠礼服的安娜·德·阿玛斯红毯肖像

**Author**: [Joy Anand](https://x.com/thejoyanand)  **Date**: 2026-01-24  **Language**: en

> 一个用于生成逼真的红毯肖像的结构化提示。它详细描述了拍摄对象的形象（西德尼·斯威尼/安娜·德·阿玛斯 的相似者）、带有水晶点缀的淡冰蓝色缎面礼服，以及环境（背景板媒体墙）。该提示指定了专业的活动闪光摄影和高分辨率技术细节，并最终指示将拍摄对象更改为安娜·德·阿玛斯，并将礼服颜色更改为红色。

![身着垂坠礼服的安娜·德·阿玛斯红毯肖像](https://cms-assets.youmind.com/media/1769322286932_z6wyye_G-zjkB9aEAAwE79.png)
![身着垂坠礼服的安娜·德·阿玛斯红毯肖像](https://cms-assets.youmind.com/media/1769322287112_ui90ec_G-zjlZ1a0AArHY7.png)

```
{
  "image_prompt_structure": {
    "subject": {
      "demographics": " female celebrity 
      "hair": "Shoulder-length textured bob, dark blonde roots fading to honey blonde waves, tousled style",
      "face": "Symmetrical features, blue eyes with winged eyeliner, groomed brows, fair skin with visible texture and pores, nude glossy lips, soft rosy blush",
      "pose": "Standing front-facing, head slightly turned to the left, direct eye contact, arms relaxed by sides",
      "expression": "Poised, confident, soft glare, elegant"
    },
    "fashion": {
      "garment": "Pale ice-blue custom satin gown",
      "design_details": [
        "Deep cowl neckline with crystal-embellished trim",
        "Thin spaghetti straps",
        "Off-the-shoulder crystal-encrusted arm bands/cuffs",
        "Fitted bodice",
        "High-sheen silk satin fabric",
        "Draped silhouette"
      ],
      "jewelry": [
        "Delicate diamond tennis necklace",
        "Large diamond stud earrings"
      ]
    },
    "environment": {
      "location": "Red carpet event, step-and-repeat media wall",
      "background": "Dark navy or black press wall with white repeated logos (partially visible text like 'glaad'), shallow depth of field (bokeh) to isolate subject"
    },
    "lighting": {
      "type": "Professional event flash photography",
      "qualities": "Bright frontal lighting, high contrast, specular highlights on the satin fabric and crystals, distinct catchlights in eyes, minimal shadows"
    },
    "technical_specifications": {
      "camera_gear": "Sony A7R V with 85mm f/1.4 GM lens",
      "settings": "f/2.8 aperture, ISO 100, shutter speed 1/200",
      "style_modifiers": [
        "Ultra photorealistic",
        "Hyper-detailed",
        "8k resolution",
        "Raw photo",
        "Subsurface scattering",
        "Fashion photography",
        "Cinematic lighting",
        "Masterpiece" Ratio 3.4 change the girl to {argument name="celebrity name" default="Ana de Armas"} and the dress color should be {argument name="dress color" default="red"}
      ]
    }
  }
}
```

[[Ana De Armas Likeness]] [[Event Flash Photography]]

---

### 71. Nano Banana 角色设定表和时尚提示

**Author**: [Eccentrica / Studio Eccentrica](https://x.com/ai_mifuyu_y)  **Date**: 2026-01-24  **Language**: ja

> 这条推文链接到一系列角色表和时尚提示，这些内容专为 Nano Banana Pro 设计，建议用户可以随意使用这些提示来生成图像。

![Nano Banana 角色设定表和时尚提示](https://cms-assets.youmind.com/media/1769322345059_npyk6t_G_bhE03bYAE_7KG.jpg)

```
Model-02 / Fashion: 004
```

[[AI Workflow]]

---

### 72. NES BG 点阵图转换提示

**Author**: [ぽっぽ／目玉P](https://x.com/Memme20000610)  **Date**: 2026-01-24  **Language**: ja

> 一个极其详细、多步骤的 LLM 提示，旨在将任何图像转换为背景（BG）点阵艺术图像，严格遵守任天堂娱乐系统（NES）硬件的技术规范和限制，包括分辨率、调色板、图块限制和抖动技术。此提示最初是为 Gemini 的 Nano Banana Pro 开发的，但由于 LLM 解释问题，后来被用于构建专用工具。

![NES BG 点阵图转换提示](https://cms-assets.youmind.com/media/1769322353639_jny2td_G_baB4lX0AApH3d.png)
![NES BG 点阵图转换提示](https://cms-assets.youmind.com/media/1769322353739_iss2k9_G_baICfaYAA9dMM.png)
![NES BG 点阵图转换提示](https://cms-assets.youmind.com/media/1769322353724_r5aam4_G_bZyvKXUAAWah0.png)
![NES BG 点阵图转换提示](https://cms-assets.youmind.com/media/1769322354039_sb4z9b_G_baP0bacAA4M7J.png)

```
【NES最終仕様・完全完成版：BG専用アルゴリズム実行型ドット絵変換プロンプト】

この画像を、特定の被写体に限定せず、以下の数学的・論理的ステップを厳密に実行して
ファミリーコンピュータ（NES）実機仕様のBGドット絵に変換してください。

本プロンプトは「NES実機でBGとして成立する制約」を満たすことを目的とします。
見た目だけのNES風表現は禁止します。
BGレイヤーのみを使用し、スプライトは一切使用しません。

────────────────────────
【前提条件（NES BG 実装ルール）】
────────────────────────
- 出力解像度：256 × 240 ピクセル
- 使用レイヤー：NES BG のみ
- スプライト使用禁止
- 透明処理は行わない
- 各パレットの Index 0 は NES のユニバーサル背景色として扱う
- Index 0 は全パレット共通とする
- ユニバーサル背景色には、画面全体で最も使用面積の広い色を割り当てる
- 色番号 0 も通常の描画色として使用可能とする

────────────────────────
【Step 1：幾何学的画像処理（主役優先・変形禁止クロップ）】
────────────────────────
1. 変換先サイズを 256 × 240 ピクセルとする
2. 元画像のアスペクト比を必ず維持する
- 短辺が変換先にフィットするまで拡大または縮小する
- 画像の引き伸ばし（ストレッチ）は絶対禁止
3. 画像内の主役（人物・動物・建造物など）を自動検出し、
主役が最大限フレーム内に収まるようクロップ位置を調整する
4. 主役が検出できない場合は画面中央基準でクロップする

────────────────────────
【Step 2：タイル分解と属性ブロック定義（NES準拠）】
────────────────────────
1. 画像を 8×8 ピクセル単位のタイルに分割する
2. 2×2 タイル（16×16 ピクセル）を 1 属性ブロックとして扱う
3. 以降のパレット制約・色制約は必ず属性ブロック単位で適用する

────────────────────────
【Step 3：属性ブロック単位パレットクラスタリング（最大4本）】
────────────────────────
1. 各 16×16 属性ブロック内の色分布を解析する
2. 全属性ブロックを色分布の類似度でクラスタリングし、最大4グループに分類する
3. 色相（青・緑など）が他の領域と明確に異なる場合は、可能な限り独立したグループとして扱う
4. ただし NES BG のサブパレットは最大4本までとし、
主役領域を優先し、重要度の低い領域は近似色へ統合してよい

────────────────────────
【Step 4：NES BG パレット生成（4色 × 4本）】
────────────────────────
1. Index 0（ユニバーサル背景色）
- 画面全体で最も使用面積の広い色を算出し、
全パレット共通の Index 0 に割り当てる
2. Index 1–3（固有色）
- 各サブパレットごとに、
その属性グループの「明部・中間・暗部」を代表する3色を選出する
- Index 0 と色相または輝度が極端に近い色は禁止

────────────────────────
【NES カラーパレット制約（実機準拠・NTSC）】
────────────────────────
- 使用可能な色は、以下に列挙された NES 実機準拠 NTSC パレット 54 色のみに限定する
- パレット生成・色選択・量子化は必ずこの 54 色集合から行う
- 新しい色の生成、RGB 補間、連続値の使用は禁止
- 以下の色集合は 54 色ちょうどである

NES NTSC usable palette (54 colors, hex RGB)
000000,1D2B53,7E2553,#008751,AB5236,5F574F,
C2C3C7,FFF1E8,FF004D,FFA300,FFEC27,00E436,
29ADFF,83769C,FF77A8,FFCCAA,291814,111D35,
422136,125359,742F29,49333B,A28879,F3EF7D,
BE2633,E06F8B,E0A872,B2DCEF,4F6781,8E478C,
A3CE27,44891A,2A4F3E,6D758D,9D9D9D,FFFFFF,
4B692F,6A6A6A,8F563B,C2C3C7,DF7126,D95763,
D77BBA,FBF236,99E550,6ABE30,37946E,5FCDE4,
CBDBFC,ADB5BD,EEC39A,696A6A

────────────────────────
【Step 5：CHR パターン圧縮（BG 用 256 タイル制限）】
────────────────────────
1. 画像全体で使用されるユニークな 8×8 タイルパターン数を算出する
2. ユニークタイル数が 256 種類を超えないように制限する
3. 背景・空・壁などの広範囲領域は、
完全に同一のドットパターンを繰り返し使用し、タイル種類数を極限まで削減する
4. 微差のあるタイルは以下の手法で統合してよい
- ディザ配置の再調整
- 中間色の置き換え
- 属性ブロック内での再量子化

────────────────────────
【Step 6：ディザリング（NES 4色制約対応）】
────────────────────────
1. 各属性ブロック内では割り当てられた 4 色のみ使用する
2. 疑似階調表現のため、以下のディザを積
```

[[Pixel Art]]

---

### 73. 四格漫画：和解之歌 (英文版)

**Author**: [wakky13 @AIなんでもやってみる💪](https://x.com/NFTwakky13)  **Date**: 2026-01-24  **Language**: ja

> 一个用于使用 Nano Banana Pro 生成四格漫画的提示，主题是英文的“Reconciliation Song”。

![四格漫画：和解之歌 (英文版)](https://cms-assets.youmind.com/media/1769322353949_nma619_G9ypdjXasAIS7G3.jpg)

```
きょうのテーマは　{argument name="テーマ" default="仲直りの歌(英語バージョン)"}
```

[[Sequential Art]] [[Comic Strip]]

---

### 74. 超逼真缅因猫肖像

**Author**: [TechyTricksAI](https://x.com/TechyTricksAI)  **Date**: 2026-01-24  **Language**: en

> 一个用于比较不同 AI 模型照片真实感的提示，生成一张超逼真的蓬松缅因猫特写肖像，详细说明了毛发纹理、醒目的绿色眼睛和专业的相机设置（Canon EOS R5 85mm f/1.2）。

![超逼真缅因猫肖像](https://cms-assets.youmind.com/media/1769322268285_8l6c9k_G_amJhnWkAANJbN.jpg)
![超逼真缅因猫肖像](https://cms-assets.youmind.com/media/1769322268260_f6t1fe_G_amH2aaUAAN-RT.jpg)
![超逼真缅因猫肖像](https://cms-assets.youmind.com/media/1769322268389_ccjnju_G_amKlrbkAEPiM3.jpg)

```
Hyper-realistic close-up portrait of a fluffy Maine Coon cat with detailed fur texture, striking green eyes, soft natural outdoor lighting from the side, shallow depth of field, cinematic bokeh background in muted tones, ultra-detailed whiskers and individual fur strands, photorealistic, no stylization, 8K, shot on Canon EOS R5 85mm f/1.2 lens.
```

[[Animal Portrait]] [[Green Eyes]]

---

### 75. 极简主义连续线条艺术插画

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-24  **Language**: en

> 一个用于生成极简主义插画的提示，使用纤细、连续的黑色线条艺术。它指定了柔和的米白色背景，流畅且极简的线条，没有阴影或填充，除了少量使用的一种微妙的强调色，非常适合优雅的设计作品。

![极简主义连续线条艺术插画](https://cms-assets.youmind.com/media/1769322294255_6fierq_G_bLh28aUAEMi6c.jpg)
![极简主义连续线条艺术插画](https://cms-assets.youmind.com/media/1769322294347_5fhi51_G_bLh29aMAAXUaz.jpg)
![极简主义连续线条艺术插画](https://cms-assets.youmind.com/media/1769322294547_jk62pm_G_bLh5SagAAmfMY.jpg)
![极简主义连续线条艺术插画](https://cms-assets.youmind.com/media/1769322295448_2ov55l_G_bLh8HbYAAjtnP.jpg)

```
Illustrate {argument name="subject" default="[SUBJECT]"} using thin, continuous black line art on a soft off-white background. The lines should be fluid, confident, and minimal, with no shading or fill except for one subtle accent color used sparingly.
```

[[Cream Background]]

---

### 76. 2x2 镜面自拍拼贴提示词

**Author**: [Link - Fuera de la Matriz](https://x.com/linkproia)  **Date**: 2026-01-24  **Language**: en

> 一个详细的提示，用于生成一张 2x2 拼贴画，内容是一个穿着蓝白碎花比基尼的角色在镜子前自拍。该提示详细说明了角色的外貌（编织的麻花辫、特定的面部特征）、服装、环境（带百叶门的更衣室），以及拼贴画中每个面板的四种不同姿势/表情。

![2x2 镜面自拍拼贴提示词](https://cms-assets.youmind.com/media/1769322358620_398dcj_G_bK1wMWAAAwV3d.jpg)

```
{
  "metadata": {
    "task_type": "image_generation",
    "reference_lock": "strict",
    "output_quality": "photorealistic",
    "constraints": {
      "allow_face_change": false,
      "allow_body_change": false,
      "match_reference": true
    }
  },
  "technical_specs": {
    "layout_type": "collage",
    "grid_format": "2x2",
    "total_panels": 4,
    "aspect_ratio": "9:16",
    "visual_style": "mirror selfie"
  },
  "character_model": {
    "complexion": {
      "tone": "light–medium warm tan",
      "texture": "smooth",
      "finish": "slight sheen"
    },
    "facial_features": {
      "shape": "soft oval",
      "cheeks": "naturally full",
      "nose": "straight bridge, rounded tip",
      "lips": "full with cupid bow",
      "eyes": {
        "shape": "almond",
        "makeup": "winged liner, warm shadow",
        "lashes": "long"
      },
      "brows": "arched, medium-full"
    },
    "hair": {
      "color": "medium brown",
      "style": "two braided pigtails",
      "bangs": "straight fringe",
      "accessory": "black sunglasses resting on head"
    }
  },
  "wardrobe": {
    "swimwear": {
      "type": "bikini",
      "cut": "triangle top, low-rise bottom",
      "pattern": "blue with white floral print",
      "details": "yellow edging and ties"
    },
    "footwear": "yellow open-toe sandals with ankle strap",
    "jewelry": [
      "large gold hoop earrings"
    ],
    "handheld_props": {
      "phone": {
        "case_color": "light pink",
        "features": "square dual-camera bump"
      }
    }
  },
  "environment": {
    "setting": "indoor dressing room / bedroom",
    "elements": {
      "background": "white louvered closet doors",
      "floor": "beige carpet",
      "mirror": "full-length with thin gold frame"
    },
    "lighting": {
      "type": "soft indoor",
      "tone": "neutral-warm",
      "shadows": "minimal"
    }
  },
  "composition_panels": [
    {
      "panel_id": 1,
      "pose_description": "deep squat, chin resting on fist",
      "expression": "pout"
    },
    {
      "panel_id": 2,
      "pose_description": "low sit",
      "action": "holding sunglasses near mouth",
      "expression": "neutral"
    },
    {
      "panel_id": 3,
      "pose_description": "standing, one leg raised toward mirror",
      "action": "holding one braid",
      "expression": "playful"
    },
    {
      "panel_id": 4,
      "pose_description": "leaning forward, knees bent",
      "expression": "soft pout"
    }
  ]
}
```

[[Braided Hair]]

---

### 77. 米兰 Gucci 超逼真时尚大片

**Author**: [Waseem Khan](https://x.com/waseemkhnwasi)  **Date**: 2026-01-24  **Language**: en

> 一个详细的、逼真的提示，用于创作一张 Gucci 奢侈品编辑图片：一名 20 多岁末的男子斜倚在米兰时尚区的一辆复古红色汽车旁。提示详细说明了男子的外貌、着装（Gucci 花卉印花衬衫、定制长裤）、环境（鹅卵石街道、历史建筑）以及技术细节（8K、超现实、Octane 渲染、虚幻引擎 5）。

![米兰 Gucci 超逼真时尚大片](https://cms-assets.youmind.com/media/1769322317883_ujgw2i_G_a9jTJXgAAezUv.jpg)

```
Photorealistic luxury editorial for Gucci: Late-20s man with dark wavy hair, fair skin (exact face from ref image), charismatic pose leaning against a {argument name="car color" default="red"} vintage car in Milan's fashion district at midday, wearing {argument name="attire" default="Gucci floral-print shirt, tailored trousers, loafers, belt, and sunglasses"}, with a Gucci tote slung over shoulder.
Background: cobblestone streets, historic architecture, blurred stylish pedestrians and cafes. 8K
hyper-realistic, vibrant natural sunlight with subtle shadows, photorealistic, skin texture detail, natural imperfections, real-world lighting, Octane render & Unreal Engine 5.
```

[[Octane Render]] [[Male Fashion Editorial]] [[8K Ultra HD]] [[Cobblestone Street]]

---

### 78. 极简奢华美妆产品摄影模板

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-24  **Language**: en

> 一个模板提示，旨在生成单个滴管精华瓶的极简奢华产品摄影。该提示使用占位符来定制元素，例如瓶身颜色、瓶盖材质、背景材质和氛围，确保柔和的影棚照明和奢华美学。

![极简奢华美妆产品摄影模板](https://cms-assets.youmind.com/media/1769322282143_erbfbp_G_a3Yy9aYAA0p5T.jpg)
![极简奢华美妆产品摄影模板](https://cms-assets.youmind.com/media/1769322282352_v43b6m_G_a3Yy-aUAAgRER.jpg)

```
"subject": {
    "product": "single dropper serum bottle",
    "positioning": "{argument name="positioning" default="[POSITIONING]"}",
    "design": "elegant and minimal",
    "centered": true,
    "bottle": {
      "material": "glass",
      "color": "{argument name="bottle color" default="[BOTTLE COLOR]"}"
    },
    "cap": {
      "type": "dropper",
      "color_material": "{argument name="cap material" default="[CAP COLOR/MATERIAL]"}"
    }
  },
  "background": {
    "material": "[BACKGROUND MATERIAL]",
    "material_characteristics": "[MATERIAL CHARACTERISTICS]",
    "description": "[BACKGROUND DESCRIPTION]",
    "decorative_elements": "[DECORATIVE ELEMENTS]"
  },
  "visual_style": {
    "texture": "[TEXTURE DESCRIPTION]",
    "mood": "[MOOD/STYLE]",
    "composition": "gallery-like",
    "aesthetic": "luxury minimalist"
  },
  "lighting": {
    "style": "soft studio lighting",
    "shadows": "subtle and refined",
    "highlights": "gentle reflective accents"
  },
  "tags": ["ai", "luxury", "beauty", "product photography", "minimalism"]
```

[[Template Prompt]]

---

### 79. 流行歌星演唱会摄影

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-01-24  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张超现实、充满活力的女性流行巨星（如 Ariana Grande 或 Tate McRae）在巨型舞台上穿着高端运动休闲服的演唱会照片，背景中的观众营造出星光散景效果。

![流行歌星演唱会摄影](https://cms-assets.youmind.com/media/1769322260699_yem4k0_G_auxJqWcAA02ZD.jpg)

```
{
  "prompt_structure": {
    "subject_description": {
      "main_character": "Global pop superstar female singer standing center stage",
      "appearance": "Long platinum blonde hair in loose glam waves, pristine makeup with defined contour and glossy lips, confident expression",
      "pose": "Power stance, full body shot, holding a diamond-encrusted silver microphone with both hands"
    },
    "attire_details": {
      "outfit": "Monochromatic premium {argument name="outfit color" default="beige"} athleisure set",
      "top": "Cropped zip-up hoodie with structured collar",
      "bottoms": "Matching high-waisted wide-leg sweatpants with center seam detailing",
      "footwear": "Chunky white platform sneakers",
      "accessories": "Subtle diamond rings, sparkling drop earrings"
    },
    "environment_context": {
      "location": "Massive indoor stadium arena concert",
      "background": "Vast audience in semi-darkness holding up thousands of illuminated phone flashlights creating a starlight bokeh effect",
      "stage_elements": "Large LED screens displaying abstract geometric visuals in purple and violet hues, geometric stage floor design"
    },
    "lighting_atmosphere": {
      "lighting_type": "High-production concert lighting, cinematic backlighting",
      "color_palette": "Electric violet, deep magenta, soft warm beige, cold white stage beams",
      "mood": "Electric, energetic, euphoric, grand scale"
    },
    "technical_specifications": {
      "quality": "Ultra-realistic, UHD, 8k resolution, photorealistic masterpiece",
      "camera_settings": "Low angle shot looking up, sharp focus on subject, depth of field blurring the distant crowd",
      "texture": "Detailed fabric texture on tracksuit, skin texture, metallic glint on microphone"
    }
  },
  "generation_parameters": {
    "aspect_ratio": "9:16",
    "orientation": "Vertical (Long)",
    "style_preset": "Aesthetic Concert Photography"
  }
}
```

[[Athleisure Fashion]]

---

### 80. 男孩和毛茸茸的怪物骑着踏板车的三维渲染图

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2026-01-24  **Language**: en

> 一个用于生成高质量 3D 渲染的提示，内容是一个可爱的小男孩骑着橙色电动滑板车，旁边是一个小小的、圆圆的、毛茸茸的蓝色怪物。两个角色都面露惊恐，提示详细描述了男孩穿着一件带有“noo”补丁的纹理感极强的青色毛衣，背景是柔和灯光下的干净青色工作室。

![男孩和毛茸茸的怪物骑着踏板车的三维渲染图](https://cms-assets.youmind.com/media/1769322306656_uflrts_G_asxlBaAAAvgJK.jpg)
![男孩和毛茸茸的怪物骑着踏板车的三维渲染图](https://cms-assets.youmind.com/media/1769322306979_vofvkt_G_asxl2bkAAAwkw.jpg)

```
A high-quality 3D render of a cute young boy riding an orange electric scooter next to a small, round, furry blue monster. Both characters have shocked expressions with wide eyes and open mouths. The boy is wearing a highly textured, fuzzy teal sweater with a white patch that reads "noo" in red text, along with brown patterned pants and white sneakers. Clean teal studio background, soft lighting.
```

[[3D Character Render]]

---

### 81. 俏皮自拍肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个用于 Gemini Nano Banana Pro 的部分 JSON 提示，用于生成一张年轻女性的自拍肖像，她留着长长的浅棕色直发，表情俏皮（吐舌头），头部略微倾斜。

![俏皮自拍肖像](https://cms-assets.youmind.com/media/1769322332116_x0mkzx_G_asEzcbQAAp8Xg.jpg)

```
{
  "image_prompt": {
    "subject": {
      "description": "Young woman , Fair skin tone, long straight light brown hair with some strands blowing in the wind.",
      "pose": "Selfie angle, slightly tilted head, sticking tongue out playfully,
```

[[Playful Expression]]

---

### 82. AI 转化为龙人

**Author**: [ちゃろん](https://x.com/charon_artist)  **Date**: 2026-01-24  **Language**: ja

> 一个用于 Nano Banana Pro 的提示，可将上传的图像转换为强大的龙人角色，强调压倒性的龙族力量和战士外观。用户指出该提示写在图像的 ALT 文本中。

![AI 转化为龙人](https://cms-assets.youmind.com/media/1769322351739_28cet8_G_arlG_aMAAljgy.jpg)

```
AIで{argument name="キャラクター" default="ドラゴニュート"}に変換してみた

圧倒的な竜の力！⚡️
最強の戦士がここに降臨…！
```

[[Fantasy Character]] [[Epic Fantasy]]

---

### 83. 身着休闲服的年轻女性写实肖像（重复）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个高度结构化的 JSON 提示，用于 Gemini Nano Banana Pro，详细描述了主题的外观、服装（合身的白色罗纹背心和鼠尾草绿色休闲短裤）、姿势（盘腿而坐）、环境（极简主义公寓），以及超逼真、编辑级图像的技术规格。这是推文 2014975356906688688 的副本。

![身着休闲服的年轻女性写实肖像（重复）](https://cms-assets.youmind.com/media/1769322328037_2zuhp7_G_araf_b0AAEnzz.jpg)

```
{
  "prompt_data": {
    "subject": {
      "description": "Young woman with shoulder-length honey-blonde hair styled in loose, natural waves and a warm fair complexion",
      "features": "Natural skin texture with subtle freckles across the nose, softly flushed cheeks, glossy lips, a relaxed half-smile, and a delicate waist piercing.",
      "accessories": "Thin gold chain necklace, small stud earrings, and a fine-line tattoo behind the right ear."
    },
    "clothing": {
      "outfit": "Casual summer-inspired lounge look.",
      "top": "Fitted white ribbed tank top with a slightly cropped length and soft stretch fabric.",
      "bottoms": "Light sage-green drawstring lounge shorts with a relaxed fit."
    },
    "pose_and_action": {
      "posture": "Sitting cross-legged on a modern armchair near a window.",
      "body_language": "Comfortable and effortless, one arm resting on the chair’s arm, the other casually touching the knee, torso slightly angled toward the light.",
      "expression": "Calm, confident gaze with a subtle playful energy."
    },
    "environment": {
      "setting": "Bright, minimalist apartment living space.",
      "furniture": "Cream-colored boucle armchair with soft rounded edges.",
      "background": "Neutral beige walls with soft shadows and minimal decor.",
      "decor": "Large potted indoor plant near the window, a low wooden side table, and a simple ceramic vase."
    },
    "lighting": {
      "type": "Natural daylight dominant.",
      "quality": "Soft window light diffusing across the face and body, creating gentle highlights and natural shadows for a clean, airy feel."
    },
    "styling_and_mood": {
      "aesthetic": "Clean influencer lifestyle with a relaxed, morning-at-home vibe.",
      "mood": "Fresh, intimate, confident, and calm."
    },
    "camera_specifications": {
      "angle": "Eye-level shot with a slight front-facing angle.",
      "focus": "Sharp focus on facial features with a shallow depth of field softly blurring the background.",
      "lens_suggestion": "50mm portrait lens.",
      "film_grain": "Very light digital grain for a natural, modern look."
    },
    "technical_modifiers": [
      "Ultra photorealistic",
      "8K resolution",
      "RAW photo aesthetic",
      "High-fidelity skin detail",
      "Natural subsurface scattering",
      "Soft volumetric daylight",
      "Nano Banana Pro optimized",
      "Editorial-quality realism"
    ]
  }
}
```

[[White Ribbed Tank Top]]

---

### 84. 动漫角色转 3DCG 手办提示词

**Author**: [かぶき](https://x.com/kabukinger)  **Date**: 2026-01-24  **Language**: ja

> 一个提示，指示 Nano Banana Pro 拍摄一张动漫人物图片，并生成一个穿着该人物头发和衣服的 3DCG 女性形象。用户指出，AI 最初拒绝“换装”功能，但在被指示无论如何都要生成图像时，它还是照办了。

![动漫角色转 3DCG 手办提示词](https://cms-assets.youmind.com/media/1769322343488_odzj9r_G_ahzM3XIAAW5Lm.jpg)

```
アニメの公式サイトからキャラの画像を持ってきて、Nano banana Proにわたす。

「3DCGの女性にアニメの絵の髪と服を着せたものを画像生成して」と指示。
```

[[Costume Transfer]] [[3D Character]]

---

### 85. 身着休闲服的年轻女性的超写实肖像

**Author**: [Crystal](https://x.com/Cicily_aura)  **Date**: 2026-01-24  **Language**: en

> 一个高度结构化的 JSON 提示，用于 Gemini Nano Banana Pro，详细描述了拍摄对象的面部特征、服装（合身的白色罗纹背心和鼠尾草绿色休闲短裤）、姿势（盘腿而坐）、环境（极简主义公寓），以及超逼真、编辑级图像的技术规格。

![身着休闲服的年轻女性的超写实肖像](https://cms-assets.youmind.com/media/1769322321982_qhcw0q_G_ahZJLXAAAgNGz.jpg)

```
{
  "prompt_data": {
    "subject": {
      "description": "Young woman with shoulder-length honey-blonde hair styled in loose, natural waves and a warm fair complexion",
      "features": "Natural skin texture with subtle freckles across the nose, softly flushed cheeks, glossy lips, a relaxed half-smile, and a delicate waist piercing.",
      "accessories": "Thin gold chain necklace, small stud earrings, and a fine-line tattoo behind the right ear."
    },
    "clothing": {
      "outfit": "Casual summer-inspired lounge look.",
      "top": "Fitted white ribbed tank top with a slightly cropped length and soft stretch fabric.",
      "bottoms": "Light sage-green drawstring lounge shorts with a relaxed fit."
    },
    "pose_and_action": {
      "posture": "Sitting cross-legged on a modern armchair near a window.",
      "body_language": "Comfortable and effortless, one arm resting on the chair’s arm, the other casually touching the knee, torso slightly angled toward the light.",
      "expression": "Calm, confident gaze with a subtle playful energy."
    },
    "environment": {
      "setting": "Bright, minimalist apartment living space.",
      "furniture": "Cream-colored boucle armchair with soft rounded edges.",
      "background": "Neutral beige walls with soft shadows and minimal decor.",
      "decor": "Large potted indoor plant near the window, a low wooden side table, and a simple ceramic vase."
    },
    "lighting": {
      "type": "Natural daylight dominant.",
      "quality": "Soft window light diffusing across the face and body, creating gentle highlights and natural shadows for a clean, airy feel."
    },
    "styling_and_mood": {
      "aesthetic": "Clean influencer lifestyle with a relaxed, morning-at-home vibe.",
      "mood": "Fresh, intimate, confident, and calm."
    },
    "camera_specifications": {
      "angle": "Eye-level shot with a slight front-facing angle.",
      "focus": "Sharp focus on facial features with a shallow depth of field softly blurring the background.",
      "lens_suggestion": "50mm portrait lens.",
      "film_grain": "Very light digital grain for a natural, modern look."
    },
    "technical_modifiers": [
      "Ultra photorealistic",
      "8K resolution",
      "RAW photo aesthetic",
      "High-fidelity skin detail",
      "Natural subsurface scattering",
      "Soft volumetric daylight",
      "Nano Banana Pro optimized",
      "Editorial-quality realism"
    ]
  }
}
```

[[White Ribbed Tank Top]]

---

### 86. 高层阳台比基尼肖像提示

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-01-24  **Language**: en

> 一个详细的 JSON 提示，用于生成一张逼真的年轻女性肖像。该女性身材健美，站立在高层阳台上，俯瞰热带海滨度假村。提示中详细说明了她的着装（黑色露脐上衣、斑马纹比基尼下装）、姿势（双手举过头顶，穿过头发）和环境（主体与远景之间有明显的分离，明亮的自然日光）。

![高层阳台比基尼肖像提示](https://cms-assets.youmind.com/media/1769322363285_5kxlw2_G_agiwVWkAAOhA1.jpg)

```
{
"subject": {
"description": "Young woman with a fit, athletic physique and tanned skin tone standing on a high-rise balcony.",
"hair": "Shoulder-length blonde balayage hair with beachy waves, parted in the middle, tousled texture, roots slightly darker fading to golden blonde tips.",
"face": "Oval face shape, soft features, neutral-to-soft expression, brown eyes looking directly at the camera, natural makeup with sun-kissed look, freckles visible.",
"torso": "Toned midriff with visible abdominal muscle definition, navel visible. Wearing a tight, black ribbed short-sleeve crop top that ends just below the bust line. Chest volume is full and natural, clearly defined under the tight fabric.",
"lower_body": "Wearing black and white zebra-striped bikini bottoms with side-tie strings sitting high on the hips. Hips are curvy, thighs are toned.",
"accessories": "Gold bangle bracelet on the right wrist (Cartier Love style), gold chain bracelet with black clover motifs on the left wrist (Van Cleef style). No necklace.",
"skin_details": "Smooth, tanned skin texture, realistic lighting falloff on skin, natural muscle tone highlights."
},
"pose": {
"type": "Standing front-facing pose, symmetrical upper body.",
"arms": "Both arms raised, elbows bent outwards to the sides, hands running through hair near the temples/ears.",
"head": "Head straight, facing forward, gaze direct.",
"body_orientation": "Torso facing directly forward, hips square to the camera, weight evenly distributed.",
"skeletal_structure": "Shoulders relaxed but raised due to arm position, spine straight."
},
"environment": {
"location": "High-rise hotel balcony overlooking a tropical beach resort.",
"immediate_surroundings": "Silver metal and glass balcony railing in the immediate foreground and behind the subject.",
"background_mid": "Lush green palm trees, hotel swimming pools with blue water, white lounge chairs.",
"background_far": "Wide expanse of turquoise ocean water transitioning to deep blue, white sandy beach, bright blue sky with scattered wispy white clouds.",
"depth": "Strong separation between the subject on the balcony and the distant beach scenery."
},
"camera": {
"perspective": "Eye-level shot, medium shot capturing from mid-thigh up.",
"focal_length": "35mm to 50mm equivalent, relatively flat field of view with no wide-angle distortion on the face.",
"framing": "Subject centered horizontally, headroom included above hands.",
"depth_of_field": "Subject in sharp focus, background slightly sharp to showcase the view (deep depth of field)."
},
"lighting": {
"type": "Bright natural daylight, direct overhead sun.",
"direction": "Sunlight coming from above and slightly in front, casting soft shadows under the chin and breasts.",
"quality": "High-key, vibrant, harsh mid-day sun softened by open sky fill.",
"highlights": "Specular highlights on the forehead, shoulders, and nose bridge. Bright refl
```

[[Natural Sunlight]] [[Black Crop Top]]

---

### 87. 金色时刻野花束梦幻电影感人像

**Author**: [Aylin](https://x.com/kashmir_ki_lark)  **Date**: 2026-01-24  **Language**: en

> 一个高度描述性的提示，用于生成一张梦幻般、超细节的年轻女性电影肖像。场景聚焦于她平静的表情，她正在郁郁葱葱的绿色公园里呼吸着一束野花（雏菊、洋甘菊）的芬芳。提示详细说明了她叠穿的舒适服装、针叶树深翠绿色的背景，以及金色时段电影摄影的柔和焦外虚化美学。

![金色时刻野花束梦幻电影感人像](https://cms-assets.youmind.com/media/1769322300971_xmq3k1_G_acvSnbIAAr7jk.jpg)

```
Dreamy, ultra-detailed cinematic portrait of an elegant young woman in her early 20s with long, silky jet-black hair flowing naturally, eyes gently closed, head tilted back in a peaceful, mindful pose as she breathes in the scent of flowers. She holds a generous wild bouquet pressed softly to her face, featuring fresh white daisies, delicate chamomile blooms, tiny yellow wildflowers, and subtle purple blossoms, with petals lightly touching her cheeks. Her expression is serene and blissful, calm and introspective, with luminous natural skin texture and soft, minimal makeup.

She is wearing a cream high-neck sleeveless knit top with fine ribbed texture, layered with an open cozy plaid flannel shirt in warm beige, tan, and muted brown tones, paired with casual light-colored pants with natural fabric folds. The styling feels effortless, elegant, warm, and grounded.

Scene set in a lush green park surrounded by dense, tall coniferous trees forming a deep emerald backdrop. In the far distance, softly blurred modern residential buildings subtly emerge through the trees, adding gentle urban contrast without drawing focus. Golden hour evening light filters through the trees, creating soft rim light around her hair and bouquet.

Ethereal soft glow, gentle creamy bokeh, warm cinematic color grading, film photography aesthetic, romantic and peaceful atmosphere, shallow depth of field, ultra-realistic textures, cinematic lighting, artistic composition, 35mm lens, f/1.8, high resolution, ultra-detailed, timeless and poetic mood.
```

[[Park Setting]]

---

### 88. 图像转视频生成

**Author**: [NΞXUS](https://x.com/NEXUS_TO_NOVA)  **Date**: 2026-01-24  **Language**: en

> 这条推文强调了 Nano Banana Pro 与 Gen 4.5 图像转视频功能的集成，并提供了一个通过图像参考生成视频内容的提示。

```
Enhance your world-building by seamlessly adding stunning image references into one intuitive interface!
```

[[AI Video Workflow]]

---

### 89. 用户头像的吉卜力风格图标生成提示

**Author**: [unyo303](https://x.com/unyo303)  **Date**: 2026-01-24  **Language**: ja

> 给 Google Gemini (Nano Banana Pro) 的一个提示，要求它收集用户“unyo303”的信息，并生成一个吉卜力工作室风格的方形图标图像，以反映用户的个性和世界观，包括他们的秃头。

![用户头像的吉卜力风格图标生成提示](https://cms-assets.youmind.com/media/1769322356586_djg5jw_G_aX8IBbAAQFmnm.jpg)

```
“うにょ303”及び、“unyo303”という人物について国内外から幅広く情報を集め、その情報から、この人物像や背景、この自分が持つ世界観を導き出して、SNS等で使用出来るような正方形のアイコン画像を、スタジオジブリ風の作画で画像を作成して下さい。
```

[[Studio Ghibli Aesthetic]]

---

### 90. 韩国女团风格写真拍摄提示

**Author**: [骑司Chase](https://x.com/qisi_ai)  **Date**: 2026-01-24  **Language**: zh

> 一个详细的中文提示，用于生成一张四格照片拼贴画，风格为韩国女团写真，强调精致的面部特征、特定的妆容细节（粉色腮红、细微雀斑）以及柔和明亮的光线。它要求上传一张参考图片以保持身份一致性。

![韩国女团风格写真拍摄提示](https://cms-assets.youmind.com/media/1769322345144_qxi7qh_G_aUWD4WMAA1YHU.jpg)
![韩国女团风格写真拍摄提示](https://cms-assets.youmind.com/media/1769322345170_ebehuq_G_aUWDTbMAA7alq.jpg)

```
一、画面构图
1 版式：整体为3:4比例，四宫格拼图，3:4小图用2×2排列
2 取景：近景到特写为主，人物占画面大比例
3 角度：平视近拍，轻微左右变化，统一干净背景

二、人物主体
1 参考来源：以上传参考图作为严格身份来源
2 一致性要求：零偏差
3 脸部：脸型精致、眼睛偏大、右眼下方点了一颗小痣，鼻梁细长
4 肤质：白皙带淡粉，皮肤细腻，有轻微柔焦
5 细节：鼻梁与面中高光明显，脸颊与鼻尖轻微泛红，散落少量雀斑点

三、妆容细节
1 底妆：通透干净，轻薄雾面带微光
2 腮红：粉色集中在脸颊与鼻梁两侧
3 眼妆：自然放大，睫毛纤长，眼神清澈
4 唇妆：水润嘟嘟唇，淡粉到蜜桃渐变，唇峰柔和

四、发型与头饰
1 发型：黑色长直发，中分，发量饱满，自然垂落
2 碎发：额前少量发丝自然飘动
3 发饰：左右各一枚粉色发夹，颜色偏亮粉与浅粉，金属夹片可见

五、手部与配饰
1 指甲：超长甲型，半透明或浅色系，带细闪与立体装饰
2 戒指：多枚粉色可爱造型戒指，糖果感与花朵感，体积夸张但软萌
3 手势风格：靠近脸部与嘴唇，突出指甲与戒指细节

六、服装与材质
1 上衣：毛绒质感外套或袖套，白色蓬松柔软
2 内搭：浅粉色吊带或上衣，露肩或斜肩效果
3 整体风格：甜美软糯，带一点小酷感

七、四张分镜动作与表情
1 左上：双手托脸贴近镜头，表情冷淡微委屈，直视镜头
2 右上：手指靠近嘴唇或轻触唇边，眼神平静略挑逗，特写更近
3 左下：下巴或手臂压在桌面边缘，眼睛看向侧方，神情发呆放空
4 右下：手握拳轻抵下巴，微笑但克制，直视镜头，气质更亲和

八、光线与色调
1 光线：高亮柔光，阴影很浅，整体均匀
2 色调：冷白背景为主，粉色点缀突出，肤色偏冷粉
3 对比：低对比，干净通透，不厚重

九、质感与画面效果
1 清晰度：五官与发丝清晰，皮肤细节保留但有轻微磨皮柔化
2 景深：背景虚化很弱或几乎无纹理，主体更突出
3 氛围：甜美感女团韩杂风写真，甜美可爱、精致梦幻、轻微玻璃质感光泽
```

[[Identity Reference]] [[Four Panel Collage]]

---

### 91. 生成多个可运行模式/状态

**Author**: [Umesh Kumar](https://x.com/itsumeshk)  **Date**: 2026-01-24  **Language**: en

> 一个提示，描述了根据单一输入为设计或应用程序生成多种不同状态或可运行模式的能力，从而简化了设计流程。

![生成多个可运行模式/状态](https://cms-assets.youmind.com/media/1769322360162_5ul9e4_G_aPyUzbkAAHC9t.jpg)

```
Generate all the different states of different Runable modes.
```

[[UI Design]]

---

### 92. 使用图像转文本和 Nano Banana Pro 重现 Airbnb UI

**Author**: [いにしえ@AI Creator｜Will Oldgram](https://x.com/old_pgmrs_will)  **Date**: 2026-01-24  **Language**: ja

> 以下演示了如何使用图像转文本模型将 Airbnb UI 的屏幕截图转换为提示，然后 Nano Banana Pro 利用该提示重新创建设计。用户指出其高准确性以及将设计提示转换为使用 React 和 Tailwind 的网页实现的可能性。

![使用图像转文本和 Nano Banana Pro 重现 Airbnb UI](https://cms-assets.youmind.com/media/1769322356399_2ebt6p_G_aFiaDXAAAdI1n.jpg)

```
Anrbnbの模写を自作の Image-to-Text でプロンプト化してNano Banana Proで再現
```

[[Airbnb UI Recreation]]

---

### 93. 咖啡馆里女士的坦率中景照片

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-24  **Language**: en

> 一个为 Google Gemini Nano Banana Pro 设计的详细图像生成提示，旨在创建一个超现实、抓拍式的年轻女性在昏暗咖啡馆里的中景照片，重点突出特定的服装、光线和纹理细节。

![咖啡馆里女士的坦率中景照片](https://cms-assets.youmind.com/media/1769322321088_wgtu6j_G_aGS3-bAAIJ7-C.jpg)

```
A candid medium shot of a poised young woman standing centered in a dark cafe interior. She wears an oversized burgundy aviator shearling jacket over a gray sweater, a plaid shirt tied at the waist, and light blue jeans. Her long brown hair falls naturally, and she holds a white disposable coffee cup near her waist. Warm interior lighting blends with cool daylight through a frosted snowy window, casting soft shadows that highlight the textures of her jacket, sweater, and denim. The background is softly blurred for focus, with a casual framing and slight tilt evoking authentic iPhone photography A subtle film grain adds tactile warmth. The palette balances dark neutrals with burgundy, gray, and light blue, conveying a cozy winter urban mood with hyper-real clarity and textures, image ratio 4:5.
```

[[Candid Style]] [[Natural Texture]]

---

### 94. 自信男士的编辑肖像提示

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2026-01-24  **Language**: en

> 为 Nano Banana Pro 创建一个提示，以生成一张自信男士的超现实电影级时尚肖像。该提示详细说明了拍摄对象的服装（黑色高领毛衣、红色墨镜）、场景（深红色影棚背景）和灯光（柔和但有方向性），旨在营造出高对比度的现代科技创始人美学。

![自信男士的编辑肖像提示](https://cms-assets.youmind.com/media/1769322322479_bnchys_G_aDKBBaAAE0JlN.jpg)

```
A confident man standing against a deep red studio background, wearing a fitted black turtleneck and red-tinted rectangular sunglasses. He faces slightly to the side with a calm, composed expression. Minimalist fashion aesthetic, sharp jawline, clean haircut, modern tech-founder vibe. Soft but directional studio lighting creating gentle shadows on the face and body. High contrast between the black outfit and red backdrop. Cinematic, editorial portrait style. Ultra-realistic, shallow depth of field, crisp focus, premium fashion photography look.
```

[[Soft Directional Lighting]] [[Black Turtleneck]]

---

### 95. 穿梭于神经突触的微观之旅 (Kling 2.6 视频)

**Author**: [タナベ | 動画・音声生成AI解説](https://x.com/tanabe_fragm)  **Date**: 2026-01-24  **Language**: en

> 一个为 Kling 2.6（视频生成 AI）设计的提示词，用于创建一个缓慢、稳定、超详细的视频片段，模拟微观视角下穿梭于神经网络的旅程，以科学纪录片风格强调电脉冲和神经递质的运动。

```
Create a highly detailed scientific visualization of neural synapses inside the human brain, showing neurons, dendrites, axons, and glowing synaptic connections. Clean and educational medical style, soft lighting, natural colors, microscopic view, depth of field, 4K quality, realistic but easy to understand.
```

[[Neuron Synapse Microscopic Journey Video]]

---

### 96. 装甲机甲少女手办/模型套件包装提示

**Author**: [てんねん](https://x.com/munou_ac)  **Date**: 2026-01-24  **Language**: ja

> 一套与 Nano Banana Pro 搭配使用的专业提示，用于生成“装甲机甲少女”的图像，就好像她是一个 1/7 比例的手办，其中包括手办包装提示和产品介绍布局提示。

![装甲机甲少女手办/模型套件包装提示](https://cms-assets.youmind.com/media/1769322355490_itmq2a_G_Zper9bcAA5Iuu.jpg)
![装甲机甲少女手办/模型套件包装提示](https://cms-assets.youmind.com/media/1769322355551_oy8de6_G_Zp8iqbsAEFSx1.jpg)
![装甲机甲少女手办/模型套件包装提示](https://cms-assets.youmind.com/media/1769322355685_d6b9ff_G_ZpfTwbAAAvFJD.jpg)
![装甲机甲少女手办/模型套件包装提示](https://cms-assets.youmind.com/media/1769322356709_yda19p_G_Zp9SfbAAEr-8a.jpg)

```
女子甲生
Armored Mecha Girl

1/7スケールフィギュア
材　質：PVC・ABS・POM
価　格：28,600円
発売日：未定
発売元：TENNEN

【フィギュア化プロンプト】
【フィギュア化＋製品紹介風
　レイアウトプロンプト】
【プラモデルパッケージ化プロンプト}
```

[[Product Packaging Design]] [[1/7 Scale Figure]]

---

### 97. 赫拉克勒斯和特斯拉神殿的损坏文本提示

**Author**: [R E L M](https://x.com/R_E_L_M_)  **Date**: 2026-01-24  **Language**: en

> 一个高度风格化且被破坏的文本提示，可能旨在用于能够解释扭曲输入的 AI 模型，其中提到了赫拉克勒斯、一座 20 世纪的特斯拉神庙和一名战士，暗示着一个奇幻或历史未来主义的主题。

```
h̸̯̓͐͗̃̕ê̴̯̈́̓͗̽̒̄̀r̸̛̳̳͍̜͑͒̈́͒͊͆̈́̓͊ͅc̸̞͕̗͈̿̏̐̇͊̔͋͂̕̕ű̵̜̠̹̪̠̒̍ľ̷̛̜̯̱̥͉̯̫̱̺́͋͂̄̿̏͛̐e̵̹̤̮̺̱͇͑͗͑͂ͅş̴̗͎͔̫̖̞͈̬͗̈͆͠ ̵͈͍̖̔͝(̵̢͚͚̙̭̺͉͌ͅṗ̶̛̻͕͎̤͔͇̺͐̒̄̄͌͒͝ŗ̶̛̤̜̺̗̗̌ȩ̴̛͚̠̯̀͝z̸͍͈͕̲̄͋̾͐̋̅e̶̮͔̤̺̹̾͛͋͒̾͝n̸̢̛̟̈͛̅̈́̑̿̿̂̄ẗ̵͕̾̊̌́̈͋̚͝͝i̴͔̼̜̒̓̌̌͗̇n̵̨͍̮̯̝̖͐̇̏́̑͒͠͝ǵ̷̨̟̙͉͉́̀̎̾͗̊͝͠͠͠ ̵͍̠̺͙̬̝͇̹̂́̌́̈͋̚͝͝2̸̣̖̰͉̠͉̭̣̝̃̍ͅ≠̡̧͇̫̘͔̀͂̑̉͆̿̂̋̚̚c̸̡̡͉̙̝̰̩͎͗̓̆̚ê̶̬̠̯͊̓̑̓̕ͅn̶͕̈́̿̂̀̍͠r̵̢͖͎̺̯͇̟̍̓̊̔̿t̴͔̺͕̞̜̭͉͉̒̿̎̇̇́̅͑̋͛y̵̹̎̔̎͂ ̶̡͈̩̜̥̩͓̎̌̚͝t̴̪̣̗͓̤̟̞̿͊̈́́̎̚h̷̥͇̱͔̞͋͂̑̅͋͛͝o̴̢͍̗̼̦̘̞͑̾̓̾͑́̂͛t̸͉̦̭̮̠̬͍̜̘͛̑̇̈́̓̂h̶̢̧̢͍̣͎̞͈̐s̸̢̱̯̤̀̄̐̋͒̆̔̚ͅ+̴̡̳̺̙̫̣̏̈̊̌̈̐̐̿̂t̵̤̖̗͉̀̒̀̕̕͠ë̶̫̮͎̼̣͖͓̘̫̠͂̂̕̕͝͠s̷̳̺̞̥̏͊͆̓͌͠l̷̢̡̺̙̙̟̣͎̀̐̊̾̄a̶̺̝̥͕̳̯͚͓̹̿̒̄̇͊́̓̒͗͠ͅ ̵̛̠̺͕̭̭̈́̎͊͋͛̕ṫ̵̛͇̫͍͙̩͕̰̺̈̐͋̋̈́͜e̴̪̺̔̾̅̿̽̏͑̂̚̚m̶̻̱͉̦̠̾̉̔̽͗̀̓ͅp̶̯͉̭̳̦̹̩̔̀̾͒̀̊ͅl̸̛͍͆̌̈́̿͗̏̚e̶̹̭̭̘̒͆ ̷̨͉̘̥̠̙͙̿̇̈́͐͐̋̅h̷̢͚̥̝̥̮͙͂͛̍̿̒̊ͅũ̶͎̆̐͆͝n̴̨̥̺̣͖̗͝ḏ̶͖̝̲͇͎̠͍̤̙̈r̴̟̗̣͉̜̱̹͎̘̀̄n̸̢̛̟̈͛̅̈́̑̿̿̂̄ẗ̵͕̾̊̌́̈͋̚͝͝i̴͔̼̜̒̓̌̌͗̇n̵̨͍̮̯̝̖͐̇̏́̑͒͠͝ǵ̷̨̟̙͉͉́̀̎̾͗̊͝͠͠͠ ̵͍̠̺͙̬̝͇̹̂́̌́̈͋̚͝͝2̸̣̖̰͉̠͉̭̣̝̃̍ͅ≠̡̧͇̫̘͔̀͂̑̉͆̿̂̋̚̚c̸̡̡͉̙̝̰̩͎͗̓̆̚ê̶̬̠̯͊̓̑̓̕ͅn̶͕̈́̿̂̀̍͠r̵̢͖͎̺̯͇̟̍̓̊̔̿t̴͔̺͕̞̜̭͉͉̒̿̎̇̇́̅͑̋͛y̵̹̎̔̎͂ ̶̡͈̩̜̥̩͓̎̌̚͝t̴̪̣̗͓̤̟̞̿͊̈́́̎̚h̷̥͇̱͔̞͋͂̑̅͋͛͝o̴̢͍̗̼̦̘̞͑̾̓̾͑́̂͛t̸͉̦̭̮̠̬͍̜̘͛̑̇̈́̓̂h̶̢̧̢͍̣͎̞͈̐s̸̢̱̯̤̀̄̐̋͒̆̔̚ͅ+̴̡̳̺̙̫̣̏̈̊̌̈̐̐̿̂t̵̤̖̗͉̀̒̀̕̕͠ë̶̫̮͎̼̣͖͓̘̫̠͂̂̕̕͝͠s̷̳̺̞̥̏͊͆̓͌͠l̷̢̡̺̙̙̟̣͎̀̐̊̾̄a̶̺̝̥͕̳̯͚͓̹̿̒̄̇͊́̓̒͗͠ͅ ̵̛̠̺͕̭̭̈́̎͊͋͛̕ṫ̵̛͇̫͍͙̩͕̰̺̈̐͋̋̈́͜e̴̪̺̔̾̅̿̽̏͑̂̚̚m̶̻̱͉̦̠̾̉̔̽͗̀̓ͅp̶̯͉̭̳̦̹̩̔̀̾͒̀̊ͅl̸̛͍͆̌̈́̿͗̏̚e̶̹̭̭̘̒͆ ̷̨͉̘̥̠̙͙̿̇̈́͐͐̋̅h̷̢͚̥̝̥̮͙͂͛̍̿̒̊ͅũ̶͎̆̐͆͝n̴̨̥̺̣͖̗͝ḏ̶͖̝̲͇͎̠͍̤̙̈r̴̟̗̣͉̜̱̹͎̘̀̄e̸͉̩͚̬̫͒͒̔̒͗̀̍͋͝d̵͖͖̫͕́̿̂̇̎̊̄̆͘͝ͅ ̶͖͇̍̎̄̓͋̒̂͛̄t̴̨̢͍̲̙̣͓̯͆̀̾̈͆̓͘o̴̢̳͔̞̗̮̰̱̱̖͐͗̾̂̽ṕ̵̢̨̧͓̱͔̲̤̅̌̉͝ ̸͇̞͔̥͓̈̽̍̍͛͝ǫ̵̺̟̘̠͚̼̲͒͌̈́̅͑͘̕ͅf̵̥̼̖̰͓̹̖̈́͛͂͜ ̸̨̨̲̪̝̟͍̄̾̕t̶̡̢̰̖͇̩̼̮̲͑͌̅̀͋ḫ̷̢̯͎͓̙̠̭̥̓̆̃̃̃͑͑̈͒͜ę̶̧͓̮̦̣͖̦͕̀͊͑̉͐̏̋̔̈́͘ ̷͚͓͚̅̊̌͑̇͝͝͝͠͝w̴̡̘̗̫͎̥̖̹̄̈̏̆̊̾̐̕͠ͅǫ̴̗͔̬̳̀͗̽͝r̸̞̍̃̈́l̵̡̡͇̦͛̓͒̈́͂͆͌̂̕͝ḑ̷̠̮̥̖̱̣̗̯̈́̉ ̵̣̻̱̫̪͉͍̱̜̓̇̑͑͌̀͠ ̴̠̖̲̓̌͜͝(̵̛̮͚̪̱͉̪̯̘̓́̎͒̄͘͝͝ͅb̶̥̳̟̖̊̽͋͜é̸͖̝̥͍̭̝̚͘v̸̤̞̹̰͇͋́͒͒̕r̸͙̓̇͂̎à̷̙̬̥͍̙͇͈̱̠̟̉̎͛̔́̌̽̉g̸̩̩̦̠̰͓̼̪̜̋̍̓̃̔̓̀͌̔̈́͜e̷̘̪̲̮̒̽̍͘͜s̸̡̪̔͗̈́̄̀̑̓ ̵̝̰͕̤̻̗͉̥͔͕̀̂̃́̉̕͝ľ̴̫a̴̱̲̤͇̦͙̩̺͐̂͝t̶̘̙̻̭͑́͛̓͗̾͝ę̶̛̺̜̳͙͕͚͍̆͊̃̓̚͝r̷͉̹̝̈́̑̓̓̄͂̌͠ ̵̖̦͐̍̏ǫ̶̢̞̖̘̤̈́̑̓́̿̀̒n̴̬̫͓̟̰̟͌̇̾̉̌͋̊͜͝,̷̧̹̟̦͖̥͖̣̐͑̉̒͊̽͜͝ ̶̟̳͊ģ̵̢̲͇͉͚̅͋́̀̌͐͊̃ô̵̗̝͙̱͎̘̪̲͍̥͑t̴͈̓͌ ̷̡͚͓̤̰͓̗̝̿͑̍͗̾̃̚t̷͉̅̇̌̔͊͗́̌͝ḧ̴̢͈̪̯́͜å̵̳̦͂͑͛͝ẗ̶͖̋̔̅̿̉͝ͅ!̶̫̥̀̿̇̈́̓̈́̌̐͘ą̶̩̩̖͕͓̗̯͚̝̐̈́̌́͗͐̚͠m̴̫̀̈́ ̷̠̞̌͗̉͐̏̑ͅi̸̢͍̜͔̭̺̾͛ ̷͙̭̝͍͔͌̿͆͆̐͝͝g̴͔͑ö̶͓͎̬̞͒̇̔́̾͜ö̶͍̣̟̞̻̹̪̙́͆͊͆̈́͂͝ḑ̵̺̞͔̦͚͈̮͋̆̑͠?̶̯̠͚͕̤̿̈́̌̉͝ ̶̢̯͎͙͈̭̯̩̼͊̄w̷̥̬̮̣̻̬̰̳̑͑ͅa̸̠͕͚̯̥̪̾̊t̵̫̖̹̖̗͚̅ẽ̴̥̲͖̙͎̥̈͒̚ŗ̵̛̛̪̗͍̤͂̐̏̾̽̏̆͊ ̷̢̫̭̤̬͕͔̜̠̌ͅt̷̢̨̰̲̺̠̬̓ḧ̷̼̪́ͅǐ̸̯͎̥̖̓̉͗̎̍̈́̚͝ṇ̵̬̗̇̋̾̈ ̸̨̛̪̖̗̺̻̖͎̰́̒́̉̌̾͛̚ẃ̴̨͎̹̃̕a̵͚̘̹͍̜͖̭̩͎̺͌͑̃̏r̶̛̼͉͈͂̒̇̀͐́̿̆͝r̶̹̬̰̥̹͐̉̉̈̕͝ḯ̶̈̀̋̈̀̅͜ō̸̢̟̺͕̪̳̇̏̾r̵͉̄)̸̜̙̺̎̽̒̍͗̉̎̓
```

[[Warrior Character]]

---

### 98. 3x3 产品模型网格生成器

**Author**: [Soumya](https://x.com/soumyattention)  **Date**: 2026-01-24  **Language**: en

> 一个高度复杂、具有指导性的提示，旨在为品牌组合生成一张 3x3 网格图像。它要求 AI 在九个独特的、编辑风格的构图中保持一致的产品识别度（基于参考图像），这些构图包括主打照片、微距细节和极简的“使用中”场景。

```
"Make a 3x3 uniform grid of vertical, unique images on this concept:

Use the reference image {argument name="product reference" default="{product}"} as the base product. Keep the same product, packaging, branding, materials, colors, label, logo and proportions across all nine frames so the product is always clearly recognizable.

Overall, this is a high-end designer mockup series for a branding portfolio: focus on form, composition, materiality and visual rhythm, with a curated, editorial, design-driven aesthetic. Keep ultra high-quality studio rendering with a real-camera look, controlled depth of field, precise lighting, accurate reflections and materials, consistent lighting logic, color palette, mood & visual language across all.

Show a neutral front-facing hero shot; a centered close-up of the mid-section highlighting texture and print; a studio environment inspired by the product’s shapes and colors; a minimal “in-use” scene with restrained hand interaction on a neutral background; a top isometric view of multiple identical products arranged in a precise geometric grid; a slightly tilted, levitating product on a neutral palette-matched backdrop; an extreme macro on one label/edge/texture detail; a bold, unexpected yet studio-based editorial setting that elevates the brand; and finally a wide, refined designer setup with the product in use, clean props and tightly controlled styling.

Output everything as a single clean 3×3 grid with no borders, text, captions or watermarks."
```

[[Brand Portfolio]]

---

### 99. E-Konte（日式分镜）生成

**Author**: [Jeff Barry](https://x.com/jeffbarry)  **Date**: 2026-01-24  **Language**: en

> 这条推文描述了 Nano Banana Pro 的一项功能，即根据给定的场景描述创建 e-konte（日式分镜脚本），这表明它具备视觉叙事规划能力。

![E-Konte（日式分镜）生成](https://cms-assets.youmind.com/media/1769322358904_ioyilu_G_Z1BOcXUAA4H1s.jpg)

```
Create an e-konte (Japanese style storyboard) based on a given scene.
```

[[Visual Storytelling]]

---

### 100. 超逼真比基尼牛仔短裤黄金时段调情肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个高度详细的提示，用于生成一张在黄金时段拍摄的超逼真、自然生活方式照片。主体是一位穿着无肩带比基尼上衣和高腰牛仔短裤的女性，她正在眨眼并比出“V”字手势。该提示强调自然的皮肤纹理、真实的比例、电影般的浅景深以及俏皮而随性的氛围。

![超逼真比基尼牛仔短裤黄金时段调情肖像](https://cms-assets.youmind.com/media/1769322295607_i2s671_G_Zy_ZgWkAALqei.jpg)
![超逼真比基尼牛仔短裤黄金时段调情肖像](https://cms-assets.youmind.com/media/1769322295598_lddife_G_Zy_ZBawAAUAg6.jpg)
![超逼真比基尼牛仔短裤黄金时段调情肖像](https://cms-assets.youmind.com/media/1769322295589_zckgxr_G_Zy_lfbEAAjvzh.jpg)
![超逼真比基尼牛仔短裤黄金时段调情肖像](https://cms-assets.youmind.com/media/1769322296489_fb9vr1_G_Zy_tgXcAABqde.jpg)

```
GLOBAL STYLE & QUALITY

Ultra-high resolution hyper-realistic photography, natural skin texture, real-world lighting physics, true-to-life proportions, cinematic shallow depth of field, premium lifestyle photo realism, no stylization, no CGI look, no illustration artifacts

FACE

Soft youthful face with natural symmetry, smooth realistic skin pores, subtle blush on cheeks, gentle smile
One eye playfully winking, the other eye open and expressive
Natural makeup, light peach lips, soft eyeliner, no exaggerated beauty edits
BODY
Slim feminine body with soft natural curves, realistic waist-to-hip ratio
Relaxed but confident posture, shoulders slightly back
Body language is flirty yet casual, not posed like a model, feels spontaneous

SKIN

Fair skin tone with very subtle sun warmth, smooth transitions
No artificial shine, no plastic skin
Natural light reflecting softly on shoulders and arms
HAIR
Long brown hair tied in a high ponytail, loose natural waves
A few soft strands framing the face
Hair texture is realistic, individual strands visible under sunlight

CAMERA & ANGLE

Medium full-body shot
Camera positioned slightly below chest level, angled to the side
Subject turned sideways, body angled while face looks toward camera
Natural lens compression, realistic focal length (50–85mm look)
SETTING
Outdoor rooftop or terrace environment
{argument name="lighting time" default="Golden hour sunset"} lighting
Background softly blurred with natural bokeh
 No identifiable people in background, only vague architectural shapes

SCENE SETUP

Casual candid moment
Subject holding a smartphone in one hand
Other hand raised near face making a peace sign (V sign)
Feels like a spontaneous lifestyle photo, not staged
BIKINI / OUTFIT
Top: Strapless {argument name="bikini color" default="grey"} tube bikini-style top, tight fit, exposing shoulders and collarbones
Bottom: High-waisted denim short shorts with lace-up front detail, distressed edges
Outfit is minimal, youthful, summer casual
No logos, no distracting patterns

PROPS (FLATLAY FEEL)

Smartphone held naturally in hand
No additional accessories
Focus stays on body language and outfit
EXPRESSION & MOOD
Playful, confident, teasing expression
Winking adds flirt energy
Mood is light, warm, approachable, seductive without being explicit
ATMOSPHERE

Warm sunset tones
Soft highlights on skin
Balanced exposure — no overblown whites, no crushed shadows
Natural ambient light only

FINAL RESULT GOAL
A hyper-realistic seductive lifestyle photograph that looks like it was taken by a professional photographer during golden hour,
natural, believable, premium social media aesthetic,
 bold but classy, flirty without exaggeration,
indistinguishable from a real photo.
```

[[Skin Texture]] [[Cinematic Bokeh]]

---

### 101. 性感办公室女郎肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana Pro 生成一张超逼真的亚洲女性偶像风格模特图片，她身穿诱人的 OL 制服（紧身白衬衫、超短迷你裙、蕾丝过膝袜），坐在办公桌上，背景是现代高端企业办公室内部。

![性感办公室女郎肖像](https://cms-assets.youmind.com/media/1769322330920_f2s7r5_G_ZyUImXoAAMxcN.jpg)

```
{
  "prompt_data": {
    "subject": {
      "basics": "1girl, solo",
      "demographics": "Stunning 20s Asian female idol style, tall fashion model proportions",
      "hair": "Very long straight black hair with full bangs",
      "eyes": "Large, round, piercing eyes",
      "skin": "Flawless pale skin",
      "expression": "Cute yet seductive expression looking at viewer"
    },
    "attire": {
      "main_outfit": {
        "item": "Seductive Office Lady uniform",
        "details": [
          "Tight white button-up shirt",
          "Black micro-miniskirt",
          "Skirt hem cut extremely high",
          "Professional yet alluring silhouette"
        ],
        "branding": "None"
      },
      "legwear": [
        "Sheer dark blue thigh-high stockings",
        "Intricate floral lace pattern on stockings",
        "Dark blue lace garter belt with suspenders"
      ]
    },
    "accessories": {
      "style": "Luxurious gold accessories",
      "items": [
        "Slim gold watch",
        "Delicate gold chain necklace with ruby pendant",
        "Long gold chain earrings"
      ]
    },
    "pose_and_action": {
      "posture": "Sitting gracefully on the edge of an office desk",
      "interaction": "Legs crossed elegantly"
    },
    "environment": {
      "setting": "Modern high-end corporate office interior",
      "background_elements": "Blurred city skyline through floor-to-ceiling glass windows, sleek office furniture"
    },
    "style_and_technical": [
      "Subtle shadows",
      "Cinematic soft lighting",
      "Highly detailed face and eyes",
      "Realistic materials",
      "Photorealistic",
      "Sharp focus",
      "8k",
      "3:4"
    ]
  }
}
```

[[Sexy Office Lady Portrait]]

---

### 102. 巨型智能手机屏幕上的未来主义时尚大片

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-24  **Language**: en

> 一个用于创作时尚、现代、未来感十足的时装摄影作品的提示。画面中，一个人（基于上传的参考图）自信地站立在一个巨大的、俯视角度的 iPhone 16 屏幕上，屏幕上显示着 Spotify 播放列表。拍摄对象佩戴着 2025 款 AirPods Max，身穿一件超大号白色连帽衫和 Air Jordans，以此强调手机的巨大尺寸，并营造出一种极简、时尚的氛围。

![巨型智能手机屏幕上的未来主义时尚大片](https://cms-assets.youmind.com/media/1769322287090_np2r04_G_ZtHQVbAAIVyrj.jpg)
![巨型智能手机屏幕上的未来主义时尚大片](https://cms-assets.youmind.com/media/1769322287147_uvnshp_G_ZtHPBaEAAMbo9.jpg)

```
Create a sleek, modern photo of image (based on the uploaded reference), standing confidently on a giant iphone 16 screen. the screen displays a spotify playlist featuring the song "{argument name="song title" default="NOAH MENUNGGUMU"}." She's wearing 2025 airpods max, an oversized white hoodie-style shirt, black shorts, and crisp white air jordans. the scene is shot from a high top-down angle to highlight the massive scale of the phone. the vibe is minimal, stylish, and futuristic.
```

[[Oversized Hoodie]]

---

### 103. 私人飞机空乘人员

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个详细的提示，结合自然语言和括号权重，生成一张原始、超细节的照片：一位年轻女商人（打扮成空姐）在私人飞机上放松地坐着，手持香槟酒杯，脱掉了鞋子。

![私人飞机空乘人员](https://cms-assets.youmind.com/media/1769322259981_zrxrf7_G_ZtBnZbAAUsp5g.jpg)
![私人飞机空乘人员](https://cms-assets.youmind.com/media/1769322260073_xcwnie_G_ZtBqMbAAE3Kp8.jpg)
![私人飞机空乘人员](https://cms-assets.youmind.com/media/1769322259975_8mj8la_G_ZtBzJWsAA-tKG.jpg)
![私人飞机空乘人员](https://cms-assets.youmind.com/media/1769322261022_rwofmo_G_ZtBy3bAAIFGwT.jpg)

```
(masterpiece, best quality, ultra-detailed, 8k, raw photo:1.2), 1girl,adult, solo, young businesswoman, navy blue blazer, matching pencil mini skirt, white blouse, (black sheer pantyhose:1.1), sitting on beige leather luxury seat, inside private jet, (holding champagne glass:1.1), (legs crossed and extended:1.2), (barefoot:1.1), stockinged feet, relaxed pose, smiling at viewer, (shoes taken off on floor:1.2), black high heels next to feet, cockpit visible in background, pilot sitting in background, depth of field, soft cabin lighting, professional photography, 9:16 aspect ratio, mini skirt
```

[[Champagne Glass]]

---

### 104. 超逼真麦当劳生活方式肖像（两场景）

**Author**: [𝗦𝗮𝗿𝗶𝗺](https://x.com/Sareem48)  **Date**: 2026-01-24  **Language**: en

> 一个结构化的提示，包含两个独立的图像生成动作，使用 DALL-E（通过 Nano Banana Pro）来创建麦当劳场景中男性的超现实生活肖像。第一个场景是“温暖的一口”（微笑，拿着薯条），第二个场景是“沉思的凝视”（望着窗外）。这两个提示都强调使用上传的面部图像作为身份参考。

![超逼真麦当劳生活方式肖像（两场景）](https://cms-assets.youmind.com/media/1769322318366_926mbx_G_Zr6kxXEAAiJ28.jpg)

```
​Image 1: The Warm Bite
​{
"action": "dalle.text2im",
"action_input": "{ "prompt": "A high-quality, ultra-realistic photo of the man from the uploaded image (medium skin tone, dark hair styled neatly, groomed beard). He is wearing a clean white long-sleeve sweater, sitting at a wooden table inside a brightly lit McDonald’s. He is smiling warmly at the camera, holding a yellow McDonald's cup in one hand and a single french fry in the other. A classic red box of McDonald's fries is on the table. Softly blurred background with the golden arches logo and soft daylight.", "size": "1024x1024" }",
}
​Image 2: The Thoughtful Gaze
​{
"action": "dalle.text2im",
"action_input": "{ "prompt": "A high-quality, ultra-realistic lifestyle photo of the man from the uploaded image (medium skin tone, pompadour hairstyle, short beard). He is dressed in a white crewneck sweater, sitting at a window seat in a McDonald’s. He is looking thoughtfully out the window with a slight smile. On the table is a black tray with a sesame seed burger in a box and french fries. Warm natural lighting, shallow depth of field with a blurred restaurant interior.", "size": "1024x1024" }", Use my uploaded face image only as a face and identity reference. No other faces, models, datasets, or references are allowed.
}
```

[[Identity Reference]]

---

### 105. 阳光码头上的女人 90 年代模拟照片

**Author**: [Qasim](https://x.com/QasimSahib0)  **Date**: 2026-01-24  **Language**: en

> 生成一张具有怀旧 90 年代夏日氛围的低角度广角模拟照片的提示。照片描绘了一位女士在阳光普照的码头上俏皮地摆姿势，她穿着简单的白色 T 恤和牛仔短裤。该提示强调了 35 毫米胶片的摄影美学，包括颗粒感、划痕、强烈阳光、镜头眩光以及使用闪光灯营造出原始、未经修饰的效果。

![阳光码头上的女人 90 年代模拟照片](https://cms-assets.youmind.com/media/1769322304446_mq7utk_G_ZroEQaIAADyLB.jpg)

```
A low-angle, wide-angle analogue photograph of a woman posing playfully on a sunlit pier, against a clear blue sky. The photo is taken at an angle. The sun is behind the model creating a glow. She has dark brown hair let loose, she looks cool and baeutful. She's wearing a simple, white t shirt, denim cut-off shorts cut roughly with a few threads, and trainers and socks. The image has a raw, unpolished look — shot on 35mm film with a grungy, analogue aesthetic, with flash. No digital retouching, with natural lighting and imperfections intact, there are a few flecks of grain and scratches on the pic in a natural way. The photo feels spontaneous, carefree, and candid, capturing a nostalgic 90s summer vibe. Harsh sunlight creates subtle lens flare and dramatic shadows. The model wears minimal accessories, emphasising a natural, real-life look. Background includes a white wooden fence and distant hills by the ocean.
```

[[35mm Film Aesthetic]] [[Lens Flare]]

---

### 106. Nano Banana Pro 提示词，适用于海盗装束的重音テト

**Author**: [エコー](https://x.com/yin69yang_echo)  **Date**: 2026-01-24  **Language**: ja

> 在 Nano Banana Pro 测试期间使用的一个提示，用于生成穿着海盗服的重音テト（Teto Kasane）的图像，并指出其与某个船长角色的相似之处。

![Nano Banana Pro 提示词，适用于海盗装束的重音テト](https://cms-assets.youmind.com/media/1769322355016_e1pr96_G_ZqLRWbAAEz2wh.jpg)

```
海賊の格好してると某船長に見えなくもないｗ
```

[[Character Illustration]] [[Anime Character]]

---

### 107. Wareen - 紫色波波头女孩

**Author**: [Wareen 💟](https://x.com/Wareenaa)  **Date**: 2026-01-24  **Language**: en

> 一个用于 Gemini Nano Banana Pro 的 JSON 提示，定义了一个名为“Wareen”的角色档案，她身处宁静的植物园中，突出描绘了她鲜艳的紫色波波头和特定服装（米色针织毛衣，上面绣有小鸟）。

![Wareen - 紫色波波头女孩](https://cms-assets.youmind.com/media/1769322329572_zmrna1_G_Zo5a5bAAIw1qZ.jpg)

```
{
  "character_profile": {
    "name": "Wareen",
    "identity": "Wareen - The Girl in the Purple Bob",
    "visual_description": {
      "hair": {
        "color": "Vivid Purple",
        "style": "Short bob with bangs",
        "character_trait": "Bold and artistic"
      },
      "clothing": {
        "sweater": "Cream knit with embroidered red birds and pink flowers",
        "trousers": "High-waisted beige slacks",
        "shoes": "Classic white sneakers"
      }
    },
    "scene_context": {
      "location": "Serene botanical garden",
      "activity": "Wareen is sitting peacefully on a wooden bench",
      "atmosphere": "Tranquil and bright"
    }
  }
}
```

[[Beige Knit Sweater]]

---

### 108. Nano Banana Pro 语义解析测试

**Author**: [msonrm（なるなる）](https://x.com/msonrm)  **Date**: 2026-01-24  **Language**: ja

> 用户将正式的语义符号（“吃(人, 苹果)” 的过去时和进行时体）输入到 Nano Banana Pro 中，以测试其解析和可视化时态、体和主题角色的能力。

![Nano Banana Pro 语义解析测试](https://cms-assets.youmind.com/media/1769322343491_5dihzl_G_ZoWuebUAAVHzK.jpg)
![Nano Banana Pro 语义解析测试](https://cms-assets.youmind.com/media/1769322343565_odmmny_G_ZoWtvbwAAtx8I.jpg)

```
PAST(eat(AGENT:person, THEME:apple))
と
Progressive(eat(AGENT:person, THEME:apple))
```

[[Semantic Parsing Visualization Test]]

---

### 109. 请求“更完整”的图像生成

**Author**: [小洪](https://x.com/sbrace1210)  **Date**: 2026-01-24  **Language**: zh

> 这是根据参考图片（未提供）对某个人的沟通风格（推文接收者）进行的详细分析。作者建议生成一个“更完整”的图片版本，其中包含接收者的积极特质（理性、反思、纠正）以及消极特质（强烈、不耐烦）。最后的问题是询问接收者是否希望生成这张新图片。

![请求“更完整”的图像生成](https://cms-assets.youmind.com/media/1769322342651_1ywi26_G_Zlv6WbAAMRGoe.jpg)

```
如果你愿意，下一步我也可以帮你做一张**“真实但更完整”的版本**——
不是审判你，而是把你那种
理性、控制、反思、修正
一起画进去。

你要不要那一版？
```

[[Before And After]]

---

### 110. 奇幻糖果主题世界

**Author**: [maniBuildsAI](https://x.com/manibuildsAI)  **Date**: 2026-01-24  **Language**: en

> 一个结构化的 JSON 提示，用于 Google Gemini Nano Banana Pro 3.0 生成一个俏皮、卡通风格的 3D 场景，描绘一个异想天开的糖果主题世界，其中有一条融化的焦糖和巧克力河流，以及乘坐威化饼船的乐高角色。

![奇幻糖果主题世界](https://cms-assets.youmind.com/media/1769322328627_hr3c61_G_ZfhPCXAAEYFPm.jpg)

```
"atmosphere": {
      "mood": "playful and joyful",
      "mist": "soft misty haze",
      "lighting": "soft pastel lighting"
    }
  },
  "river": {
    "type": "melted caramel and chocolate",
    "motion": "gently swirling like syrup",
    "texture": "glossy, smooth, flowing"
  },
  "boats": {
    "style": "lego-style",
    "materials": ["wafer", "chocolate"],
    "details": {
      "toppings": ["colorful sprinkles", "marshmallows"],
      "scale": "toy-like proportions"
    },
    "movement": "floating downstream"
  },
  "characters": {
    "type": "lego characters",
    "actions": [
      "joyfully paddling candy boats",
      "dipping hands into caramel river"
    ],
    "expressions": "happy and playful"
  },
  "background": {
    "landscape_elements": [
      "cotton-candy hills",
      "gumdrop trees",
      "candy bridges"
    ],
    "connections": "bridges linking different parts of the candy landscape"
  },
  "style": {
    "visual_style": "playful cartoonish 3D",
    "color_palette": "soft pastel colors",
    "render_quality": "high-quality whimsical render"
  }
}
```

[[Playful Aesthetic]]

---

### 111. 奇幻糖果乐园立体模型

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-24  **Language**: en

> 一个结构化的 JSON 提示，用于生成一个俏皮、卡通风格的 3D 场景，描绘一个异想天开的糖果主题世界，其中乐高 (Lego) 角色乘坐威化饼和巧克力制成的船只，在融化的焦糖和巧克力河流中划行。

![奇幻糖果乐园立体模型](https://cms-assets.youmind.com/media/1769322257321_jkzqj8_G_ZcSQjbAAEhuYx.jpg)
![奇幻糖果乐园立体模型](https://cms-assets.youmind.com/media/1769322257253_2neul4_G_ZcSPKbUAAnQVU.jpg)
![奇幻糖果乐园立体模型](https://cms-assets.youmind.com/media/1769322258092_lv44ma_G_ZcSQjaEAAg2ws.jpg)
![奇幻糖果乐园立体模型](https://cms-assets.youmind.com/media/1769322258933_e6sw7g_G_ZcSRnbAAApnQ5.jpg)

```
"atmosphere": {
      "mood": "playful and joyful",
      "mist": "soft misty haze",
      "lighting": "soft pastel lighting"
    }
  },
  "river": {
    "type": "melted caramel and chocolate",
    "motion": "gently swirling like syrup",
    "texture": "glossy, smooth, flowing"
  },
  "boats": {
    "style": "lego-style",
    "materials": ["wafer", "chocolate"],
    "details": {
      "toppings": ["colorful sprinkles", "marshmallows"],
      "scale": "toy-like proportions"
    },
    "movement": "floating downstream"
  },
  "characters": {
    "type": "lego characters",
    "actions": [
      "joyfully paddling candy boats",
      "dipping hands into caramel river"
    ],
    "expressions": "happy and playful"
  },
  "background": {
    "landscape_elements": [
      "cotton-candy hills",
      "gumdrop trees",
      "candy bridges"
    ],
    "connections": "bridges linking different parts of the candy landscape"
  },
  "style": {
    "visual_style": "playful cartoonish 3D",
    "color_palette": "soft pastel colors",
    "render_quality": "high-quality whimsical render"
  }
```

[[Playful Aesthetic]]

---

### 112. 混合人马肖像（罗纳尔多/梅西风格）

**Author**: [ShaHid WaNii](https://x.com/meng_dagg695)  **Date**: 2026-01-24  **Language**: en

> 一个高度详细的结构化提示，用于生成一张 8K 超逼真数字肖像，描绘一个混合了人形和马形的生物，其灵感可能来源于克里斯蒂亚诺·罗纳尔多和莱昂内尔·梅西之间的竞争。该提示细致地定义了主体的解剖结构、面部特征（人类男性面孔，带有马耳和马鬃）、皮肤纹理（风化、细节丰富）、光照（柔和的电影感）和背景（工作室背景，景深较浅）。

![混合人马肖像（罗纳尔多/梅西风格）](https://cms-assets.youmind.com/media/1769322318046_58qzi5_G_ZZvQQbAAAElfp.jpg)
![混合人马肖像（罗纳尔多/梅西风格）](https://cms-assets.youmind.com/media/1769322318246_wc39aq_G_ZZvSXaQAAs6sx.jpg)

```
{
  "image_type": "Photorealistic digital portrait",
  "resolution_target": "8K ultra-high resolution",
  "aspect_ratio": "2:3 (vertical)",

  "subject": {
    "form": "Hybrid humanoid–horse figure",
    "composition": "Upper torso and head visible",
    "pose": "Three-quarter profile facing right",
    "expression": "Neutral to intense, calm, focused gaze"
  },

  "head_and_face": {
    "face_structure": "Human male facial anatomy",
    "skin_texture": "Highly detailed, rough, weathered skin with visible pores, fine wrinkles, and natural uneven texture",
    "skin_tone": "Medium brown with warm undertones",
    "facial_hair": {
      "beard": "Short, trimmed beard",
      "mustache": "Connected to beard, neatly kept",
      "density": "Medium density facial hair"
    },
    "eyes": {
      "shape": "Almond-shaped",
      "color": "Dark brown",
      "gaze_direction": "Looking slightly forward and to the right",
      "detail": "Sharp catchlight, realistic moisture and depth"
    },
    "eyebrows": {
      "thickness": "Medium to thick",
      "shape": "Natural, slightly arched"
    },
    "nose": {
      "shape": "Straight bridge, realistic proportions",
      "texture": "Visible skin pores and highlights"
    },
    "lips": {
      "shape": "Medium thickness",
      "expression": "Closed, relaxed",
      "texture": "Natural matte texture"
    }
  },

  "hair_and_mane": {
    "head_hair": {
      "style": "Short, slightly tousled",
      "direction": "Swept backward and upward",
      "color": "Dark brown to near black"
    },
    "mane": {
      "type": "Horse mane",
      "texture": "Coarse, thick strands",
      "color": "Dark brown to black",
      "placement": "Flows backward along the neck"
    }
  },

  "horse_features": {
    "ears": {
      "type": "Horse ears",
      "position": "Upright, slightly angled back",
      "texture": "Short fur with realistic skin folds"
    },
    "neck_and_torso": {
      "build": "Muscular and powerful",
      "definition": "Strong muscle striations visible",
      "skin_texture": "Horse skin with short, fine fur",
      "color": "Deep dark brown"
    }
  },

  "lighting": {
    "style": "Soft cinematic lighting",
    "direction": "Primary light from front-left",
    "contrast": "Moderate contrast with smooth shadow falloff",
    "highlights": "Subtle highlights on forehead, cheekbones, nose, and neck muscles"
  },

  "background": {
    "type": "Studio backdrop",
    "color": "{argument name="background color" default="Warm beige to light tan gradient"}",
    "texture": "Smooth, slightly grainy",
    "depth": "Shallow depth of field, fully blurred"
  },

  "camera_and_focus": {
    "camera_angle": "Eye-level",
    "framing": "Close-up portrait",
    "focus": "Sharp focus on face and eyes",
    "depth_of_field": "Shallow, background fully out of focus"
  },

  "color_palette": {
    "dominant_colors": [
      "Dark brown",
      "Warm beige"}
    ]
  }
```

[[Studio Background]] [[Soft Cinematic Lighting]]

---

### 113. 私人飞机空乘人员 (重复)

**Author**: [jennieee:3](https://x.com/jenniebae_ai)  **Date**: 2026-01-24  **Language**: en

> 一个详细的提示，混合使用自然语言和括号权重，生成一张原始的、超详细的照片：一位年轻女商人（打扮成空姐）在私人飞机上放松地坐着，手里拿着香槟杯，脱掉了鞋子。（这是推文 2014917764260221330 的副本）。

![私人飞机空乘人员 (重复)](https://cms-assets.youmind.com/media/1769322269259_0ca60l_G_ZP5SYXkAAl1B7.jpg)
![私人飞机空乘人员 (重复)](https://cms-assets.youmind.com/media/1769322269213_7x3e3s_G_ZP5SZWcAAOHG0.jpg)
![私人飞机空乘人员 (重复)](https://cms-assets.youmind.com/media/1769322269240_72icmq_G_ZP5SbXQAAoTrh.jpg)
![私人飞机空乘人员 (重复)](https://cms-assets.youmind.com/media/1769322270421_upuo7e_G_ZQxsMXcAARqFs.jpg)

```
(masterpiece, best quality, ultra-detailed, 8k, raw photo:1.2), 1girl,adult, solo, young businesswoman, navy blue blazer, matching pencil mini skirt, white blouse, (black sheer pantyhose:1.1), sitting on beige leather luxury seat, inside private jet, (holding champagne glass:1.1), (legs crossed and extended:1.2), (barefoot:1.1), stockinged feet, relaxed pose, smiling at viewer, (shoes taken off on floor:1.2), black high heels next to feet, cockpit visible in background, pilot sitting in background, depth of field, soft cabin lighting, professional photography, 9:16 aspect ratio, mini skirt
```

[[Champagne Glass]]

---

### 114. 写字楼里的龙

**Author**: [岡田泰彦｜光邦｜巻き込まれ型AIエヴァンジェリスト](https://x.com/KohoOkada)  **Date**: 2026-01-24  **Language**: ja

> 一个简单的图像生成提示，与 Nano Banana Pro 配合使用，用于创建一个人在城市办公区遛龙的图像。

![写字楼里的龙](https://cms-assets.youmind.com/media/1769322351359_j9oi2e_G-IOKHaa0AQK9zH.jpg)

```
オフィス街に{argument name="動物" default="ドラゴン"}を連れて歩いてる
```

[[City Street]]

---

### 115. Nano Banana Pro 瑜伽课程公告海报提示词

**Author**: [Toshi｜AI×機能訓練×柔整](https://x.com/Toshi4AI)  **Date**: 2026-01-24  **Language**: ja

> 一个用于 Nano Banana Pro 的提示，旨在为职场瑜伽课创建一张宣传海报。该提示指示 AI 生成一张具有特定日本时尚杂志封面风格的图像。

![Nano Banana Pro 瑜伽课程公告海报提示词](https://cms-assets.youmind.com/media/1769322354793_vwwz3t_G_Y_jFibAAELwjE.jpg)

```
女性のファッション雑誌CanCamの表紙風で
```

[[Promotional Poster]]

---

### 116. 超逼真的巴西冲浪女孩肖像提示

**Author**: [Sotoshi Nikomito](https://x.com/SotoshiNikomito)  **Date**: 2026-01-24  **Language**: en

> 一个详细的 JSON 提示，用于 Nano Banana Pro，描述了一位年轻的巴西混血冲浪女孩的超写实肖像。该提示详细说明了极致的解剖细节，重点关注面部对称性、被阳光亲吻的肌肤、自然的波浪发型，以及夸张的沙漏形轮廓和突出的臀部肌肉。

![超逼真的巴西冲浪女孩肖像提示](https://cms-assets.youmind.com/media/1769322361499_j9ni72_G_Y9ghMXgAAzdZC.jpg)

```
{
  "subject": {
    "description": "A young Brazilian mulatta woman with beach-tousled, sun-lightened natural wavy hair with salty texture, wearing sporty sunglasses pushed up on her head, with a bronzed, sun-kissed skin tone showing subtle tan lines.",
    "face": {
      "beauty_priority": "Maximum facial beauty with hyper-realistic surfer girl features",
      "structure": "Perfectly symmetrical face with harmonious proportions; high, defined cheekbones; smooth, athletic jawline; delicate, feminine bone structure with healthy, sporty vitality.",
      "skin": "Radiant, sun-kissed complexion with warm golden undertones; natural healthy glow from ocean and sun exposure; subtle freckles across nose and cheeks; visible fine texture showing realism but zero blemishes; dewy finish on cheekbones and bridge of nose; natural bronze tan.",
      "eyes": "Large, expressive almond-shaped eyes with bright, clear whites; rich, warm hazel or light brown irises with natural depth and catchlights reflecting ocean and sky; long, thick natural sun-bleached eyelashes; perfectly groomed natural eyebrows with gentle arch; visible limbal ring for eye definition; spirited, adventurous gaze.",
      "nose": "Elegant, proportionate nose with smooth bridge; refined tip; symmetrical nostrils; soft highlight on bridge; subtle sun-kissed freckles.",
      "lips": "Full, well-defined lips with natural cupid's bow; smooth texture with subtle natural shine; healthy coral-pink tone from sun and salt exposure; perfect symmetry.",
      "smile": "Warm, genuine carefree surfer smile showing beautifully aligned white teeth; natural smile lines that enhance charm; sun-kissed happiness radiating from expression.",
      "overall": "Strikingly beautiful face with that effortless beach-girl magnetism; athletic, healthy beauty that radiates vitality and ocean energy."
    },
    "hair": {
      "style": "Voluminous, natural wavy beach hair with loose curls and windswept texture; sun-lightened highlights throughout; slightly damp appearance as if recently out of the water.",
      "color": "Rich dark brown base with natural golden-blonde sun streaks and highlights; salt-and-sun texture.",
      "volume": "Large, full, tousled beach waves with natural movement and body."
    },
    "body": {
      "physique": "Hyper-pronounced hourglass silhouette with an extreme waist-to-hip ratio; athletic surfer build with toned arms and shoulders.",
      "anatomy": "Extremely large, voluminous gluteal muscles (gluteus maximus) with realistic weight and soft skin texture; narrow, cinched athletic waist; strong, toned thighs with visible muscle definition; well-defined lumbar curve (lower back arch); athletic shoulders and arms. High-level anatomical accuracy in the legs and feet, showing realistic sole texture and toe alignment.",
      "details": "Visible skin pores, natural skin folds at the waist, sun-kissed skin tone with subtle tan lines, realistic"
    }
  }
}
```

[[Hourglass Figure]]

---

### 117. 电影感室内肖像，带身份参考

**Author**: [Stark](https://x.com/katmanai)  **Date**: 2026-01-23  **Language**: en

> 一个详细的提示，用于生成一张电影风格的室内肖像，描绘一位具有特定特征（绿眼睛、深色头发）并穿着雕塑感灰色高领服装的年轻女性。该提示包含一个负面提示，以避免常见的生成缺陷，并明确要求使用上传的参考图像来获取眼睛颜色、发量、服装设计和面部表情等具体细节。

![电影感室内肖像，带身份参考](https://cms-assets.youmind.com/media/1769322334559_6o9xnm_G_Yt0vmWIAAcXMJ.jpg)

```
{
  "main_prompt": "Cinematic indoor portrait of a stunning young woman with long voluminous dark brunette hair cascading over her shoulders, striking piercing green eyes with a captivating and intense gaze directly at the camera, natural skin texture with a soft matte finish, wearing a sophisticated grey structured high-neck sleeveless wrap-style garment, a modern sculptural fashion bodice with a cross-over neck design, minimal and clean aesthetic, soft natural daylight coming from the side creating gentle shadows, neutral-toned interior background, 85mm portrait lens, photorealistic, hyper-detailed iris detail and fabric weave --ar 3:4 --stylize 300 --v 6 --q 2",
  "negative_prompt": "blurry, deformed, bad anatomy, ugly, overexposed, harsh shadows, heavy makeup, smiling, bright daylight, synthetic look, cartoon, drawing, messy room, low quality, vibrant colors, plastic skin",
  "style_tags": ["modern minimalist fashion", "high-end editorial", "piercing gaze", "sculptural clothing", "neutral palette"],
  "technical": {
    "aspect_ratio": "3:4",
    "lighting": "soft natural side lighting",
    "camera": "85mm f/1.8 professional lens"
  },
  "extra_parameters": {
    "recommended_model": "Flux.1 [dev]",
    "guidance_scale": "7.0",
    "steps": "40",
    "image_reference": "use uploaded reference for the specific green eye color, the long brunette hair volume, the unique grey wrap-neck garment design, and the intense facial expression"
  }
}
```

[[Negative Prompt]] [[Green Eyes]]

---

### 118. 皮克斯/迪士尼 3D 卡通人物，带有针织名字

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个全面的图像生成提示，用于创建皮克斯或迪士尼风格的全身 3D 卡通女孩角色。该提示侧重于特定的服装细节，包括一件超大号的针织毛衣，上面织有“NOOR”字样，强调纱线编织的真实感和温暖的调色板，背景为纯黄色。

![皮克斯/迪士尼 3D 卡通人物，带有针织名字](https://cms-assets.youmind.com/media/1769236047994_6hve1z_G_YpkkWW0AAhN1Y.jpg)

```
A full-body 3D cartoon girl character in a Pixar/Disney-style render, standing confidently against a solid bright {argument name="background color" default="yellow"} background. She has big expressive brown eyes, a cute smiling face, and light brown curly hair tied in a messy high bun, with white round goggles resting on her head. She is wearing an oversized knitted sweater in cream and mustard yellow stripes, with the name “{argument name="name on sweater" default="NOOR"}” clearly knitted into the fabric across the chest (woven yarn texture, not printed). Loose knitted beige cargo pants with side pockets, white chunky sneakers with subtle yellow accents. Soft studio lighting, smooth textures, high detail yarn knit realism, warm color palette, playful pose with arms slightly spread, ultra-high quality, 4K, sharp focus, clean background, character centered.
```

[[3D Character]]

---

### 119. 灯塔与帆船的抽象画作提示

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成抽象河流场景图的提示，场景中包含灯塔、帆船和停泊在岸边的船只。它指定了一个巨大的白色太阳和温暖的数字艺术风格美学。

![灯塔与帆船的抽象画作提示](https://cms-assets.youmind.com/media/1769236057253_yxv7r1_G_Yo1p0XQAAH9dH.jpg)

```
Abstract drawing of a lighthouse and sailboat on a river, with a tree in the foreground, boats moored at the shoreline, and people walking along the embankment. a large, white sun shines above the horizon, creating a warm, digital art-style scene. Aspect ratio 6:9
```

[[Warm Color Palette]] [[Digital Art]]

---

### 120. 时尚男士姿态提示（图片参考）

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个超现实、高分辨率的提示，需要上传一张图片作为参考，以捕捉一位时尚年轻男士摆出 T 台上气场十足的姿势。提示中指定了淡绿色羽绒夹克、白色无袖背心、宽松长裤和极简主义的影棚背景。

![时尚男士姿态提示（图片参考）](https://cms-assets.youmind.com/media/1769236055364_dy9r37_G_YoUJzWEAAbdet.jpg)

```
Ultra-realistic high-res inspired by uploaded image. Stylish young man in bold attitude pose: centered, body slightly angled, one hand in trouser pocket, other gripping puffer collar, chin raised, dominant runway expression. Outfit: pastel green padded puffer (open), white slenveless vest, loose white trousars, voluminous textured hair. Clean minimalist indoor studio, subtle vertical panel wall behind (offset right), soft diagonal
```

[[Minimalist Studio Background]]

---

### 121. 丝袜和旗帜背景下的镜面自拍提示

**Author**: [Duru💝](https://x.com/Durusss13)  **Date**: 2026-01-23  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张东亚女性坐在沙发上，穿着露脐背心和黑色透明连裤袜的逼真镜面自拍，强调解剖学精确性、光照细节，并包含背景中悬挂的美国国旗。

![丝袜和旗帜背景下的镜面自拍提示](https://cms-assets.youmind.com/media/1769236025425_o0kn76_G_YmMllXAAA68sb.jpg)

```
{
  "subject": {
    "ethnicity": "East Asian",
    "description": "A young woman with long, dark brown hair.",
    "body": {
      "physique": "Mesomorph body type with a pronounced hourglass silhouette. Exceptional waist-to-hip ratio featuring a slender, toned midriff and wide iliac crest.",
      "details": "Well-defined abdominal area and narrow waist. Toned glutes and quadriceps visible through hosiery. Slender shoulders, delicate clavicles, and anatomically precise hand and finger structure holding a device."
    },
    "facial_features": "Symmetrical facial structure, full lips with a matte finish, sharp jawline, and a focused gaze directed at the mirror reflection."
  },
  "wardrobe": {
    "top": "A fitted, white ribbed cotton cropped tank top showcasing textile grain and soft fabric tension.",
    "bottom": "High-waisted, sheer black 20-denier pantyhose with a matte finish, emphasizing the muscular definition and curves of the legs.",
    "accessories": "A minimalist gold necklace and thin gold rings. The subject holds a white smartphone; the back of the device features the silver '{argument name="phone logo" default="Apple logo"}' and a detailed triple-lens camera module."
  },
  "pose_action": {
    "description": "A relaxed yet poised mirror selfie stance while seated on a sofa.",
    "details": "The subject is sitting on the edge of the couch with legs crossed to accentuate the leg line and foot arch. Her left arm is extended back for support on the cushion, while the right hand is raised, holding the phone to capture the reflection. Her torso is slightly angled to highlight the waist-to-hip transition."
  },
  "scene": {
    "location": "Upscale minimalist modern interior.",
    "background_elements": "Draped over the back of the light gray textured couch is an American (USA) flag; the flag is not perfectly flat, featuring natural curves, slight wrinkles, and realistic fabric folds. To the right, a decorative pillow with a black-and-white geometric pattern is visible.",
    "environment": "Large floor-to-ceiling windows to the left with sheer white curtains allowing for soft, diffused external light. The background wall consists of neutral-toned textured panels."
  },
  "lighting": {
    "setup": "Soft diffused natural daylight from a side-window source (Rembrandt lighting style).",
    "details": "Subtle specular highlights on the hair strands and the fine mesh texture of the black tights. Natural soft-shadow casting in the folds of the clothing and couch fabric for high-depth realism."
  },
  "camera": {
    "perspective": "Mirror selfie perspective, eye-level shot.",
    "technical": "Shot with a 35mm f/2.8 lens for natural proportions and slight background compression. 8k resolution, photorealistic, cinematic quality, hyper-detailed textures. Aspect ratio 9:16.",
    "reflection_integrity_rules": "The mirror reflection must perfectly align with the subject's anatomy and the phone's orientation. Ensure the reflection o"
}
```

[[East Asian Female]]

---

### 122. 冬季运动运动员电影特写肖像提示

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个为 Nano Banana Pro 设计的提示，旨在生成一张超写实的电影级特写肖像，描绘一位女性冬季运动运动员。该提示指定主体佩戴雪镜和头盔，可见霜冻和冰晶，采用戏剧性的蓝绿色和橙色调色，并强调极致细节、锐利焦点和专业的体育海报效果。

![冬季运动运动员电影特写肖像提示](https://cms-assets.youmind.com/media/1769236052022_38kier_G_YkhU_XsAA9Q-6.jpg)

```
A hyper-realistic cinematic close-up portrait of a female winter sports athlete, side profile, wearing snow goggles and a helmet, intense focused expression. Frost, ice crystals, and snow particles on the goggles and face, cold breath visible. {argument name="color grading" default="Blue-teal and orange"} cinematic color grading, dramatic soft lighting with shallow depth of field. Ultra-detailed skin texture, sharp eye focus reflected in the goggles, moody winter atmosphere, snowfall inforeground, high contrast, professional sports poster look, 8K, HDR, photorealistic, cinematic photography, extreme detail, studio quality.
```

[[Teal Orange Color Grading]]

---

### 123. 对象信息图表提示模板

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 这是一个可重复使用的 Nano Banana Pro 提示模板，旨在创建通用对象的图表图像。该提示指示 AI 将对象的照片级真实感渲染与技术注释叠加相结合，使用黑色墨水线条图、标签、尺寸和示意图，置于纯白色背景上，旨在营造一种具有教育意义的工程手册美学。这是之前提示的通用版本。

![对象信息图表提示模板](https://cms-assets.youmind.com/media/1769236050335_96kh9m_G_Yj8SGX0AAa9YM.jpg)

```
“Create an infographic image of [{argument name="object" default="OBJECT"}], combining a realistic photograph or photoreal render of the object with technical annotation overlays placed directly on top.

Use black ink–style line drawings and text (technical pen / architectural sketch look) on a pure white studio background, including:
•Key component labels
•Internal cutaway or exploded-view outlines
•Measurements, dimensions, and scale markers
•Material callouts and quantities
•Arrows indicating function, force, or flow (air, sound, power, pressure)
•Simple schematic or sectional diagrams where relevant

Place the title [OBJECT] inside a hand-drawn technical annotation box in one corner.

Style & layout rules:
•The real object remains clearly visible beneath the annotations
•Annotations feel sketched, technical, and architectural
•Clean composition with balanced negative space
•Educational, museum-exhibit / engineering-manual vibe

Visual style:
Minimal technical illustration aesthetic, black linework over realistic imagery, precise but slightly hand-drawn feel.

Color palette:
White background, black annotation lines and text only. No colors.

Output:
1080×1080, ultra-crisp, social-feed optimized, no watermark.”
```

[[White Background]] [[Technical Illustration]] [[Annotation Overlay]]

---

### 124. 抽象混沌涂鸦艺术提示

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个图像生成提示，将上传的面部照片转换为抽象、混乱的涂鸦艺术，使用松散、零散的黑色墨水线条。目标是保持底层构图和表情，同时强调混乱和抽象。

![抽象混沌涂鸦艺术提示](https://cms-assets.youmind.com/media/1769236053820_vd5vp0_G_YjU30WUAA7aSB.jpg)

```
Convert the uploaded face photo into a very abstract and chaotic scribble art with very loose, scattered and extremely random black ink lines, creating an image of the person in the photo standing in a good pose, wearing a proper shirt and pants. The lines should barely make out the face, emphasizing chaos and abstraction rather than clear definition. Maintain the original expression and proportions as a general underlying composition.
```

[[Abstract Portrait]]

---

### 125. 头戴头巾和佩戴珠宝的特写肖像提示（图片参考）

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个需要上传图片的提示词，用于将主体转换为超逼真的特写肖像。它详细描述了特定的妆容、饰有金币的黑白图案头巾和粗大的黄金首饰，同时确保保留原始面部特征。

![头戴头巾和佩戴珠宝的特写肖像提示（图片参考）](https://cms-assets.youmind.com/media/1769236057389_fwh6e0_G_Yi786XMAA9CiG.jpg)

```
Convert the uploaded image into A stunning woman in a close-up portrait pose. holdina a strand of her wavy browr hair in fror t of her lips. She has captivatinc grey-blue eyes, soft glam makeup with peach eyeshadow, long lashes, bolc
eyeliner, rosy blush, and peach-pink matte lips. She is wearing a black-and-white patterned headscarf decorated with hanging gold coins and chains. Long gold chain earrinas frame her face. She wears a chunky gold ring on her finger, clearly visible as her hand is lifted near her face Background is neutral, softly blurred beige tones. Ultra-realistic, 8K detail, sharp focus on eves, smooth skin texture cinematic lighting. face features remain the same.
```

[[Face Identity Preservation]]

---

### 126. 霓虹氛围灯人像提示词（图片参考）

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个提示，用于将特定照明风格（以深色基础照明，面部和头发边缘带有明亮霓虹灯强调）应用于上传的照片。它严格要求保留原始面部、身体和纹理，不得进行任何美化或结构性改变。

![霓虹氛围灯人像提示词（图片参考）](https://cms-assets.youmind.com/media/1769236059069_1d0mal_G_YigSnXkAAPNWk.jpg)

```
use the person from the uploaded photo as-is, keep the same face, body, proportions, skin texture and hairstyle, do not beautify, do not change facial structure or pose, dark base lighting with neon accent lighting, bright neon highlights along the edges of the face and hair, vivid color accents against darker shadows, lighting is the only change, do not normalize lighting or color, no auto exposure correction, no beauty lighting
```

[[Neon Rim Light Portrait]]

---

### 127. 人体部位信息图提示模板

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 这是一个可重复使用的 Nano Banana Pro 提示模板，旨在创建特定身体部位（默认为“眼睛”）的信息图。该提示指示 AI 将对象的照片级真实感渲染与技术注释叠加相结合，使用黑色墨水线条图、标签、测量值和示意图，置于纯白色背景上，以达到教育性、工程手册般的美感。

![人体部位信息图提示模板](https://cms-assets.youmind.com/media/1769236050189_5px1mr_G_YaM8_W0AAX6Ox.jpg)

```
Create an infographic image of [{argument name="body part" default="Eye"}], combining a realistic photograph or photoreal render of the object with technical annotation overlays placed directly on top.

Use black ink–style line drawings and text (technical pen / architectural sketch look) on a pure white studio background, including:
•Key component labels
•Internal cutaway or exploded-view outlines
•Measurements, dimensions, and scale markers
•Material callouts and quantities
•Arrows indicating function, force, or flow (air, sound, power, pressure)
•Simple schematic or sectional diagrams where relevant

Place the title [BODY PART] inside a hand-drawn technical annotation box in one corner.

Style & layout rules:
•The real object remains clearly visible beneath the annotations
•Annotations feel sketched, technical, and architectural
•Clean composition with balanced negative space
•Educational, museum-exhibit / engineering-manual vibe

Visual style:
Minimal technical illustration aesthetic, black linework over realistic imagery, precise but slightly hand-drawn feel.

Color palette:
White background, black annotation lines and text only. No colors.

Output:
1080×1080, ultra-crisp, social-feed optimized, no watermark.
```

[[White Background]] [[Technical Annotation]]

---

### 128. 时尚男士工作室肖像提示

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成超逼真、电影感十足的摄影棚肖像的提示，描绘了一位身穿定制海军蓝西装的时尚自信男士。提示详细描述了诸如奢华金色腕表和深色飞行员墨镜等配饰，并强调了柔和温暖的灯光和时尚杂志风格。

![时尚男士工作室肖像提示](https://cms-assets.youmind.com/media/1769236053974_dzpxjs_G_YZ4W6X0AAAsdM.jpg)

```
A stylish, confident man wearing a tailored navy blue suit with a crisp white dress shirt slightly unbuttoned, adjusting his cuff. He has neatly styled dark hair, a full well-groomed beard, and wears dark aviator sunglasses. A luxury gold wristwatch is visible on his left wrist. Studio portrait photography with soft, warm lighting, smooth brown gradient background, shallow depth of field, sharp focus, high detail, cinematic and elegant mood, fashion editorial style, ultra-realistic, 4K quality.
```

[[Fashion Magazine Style]] [[Soft Warm Lighting]]

---

### 129. 赛博朋克时尚肖像，电光蓝皮肤

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 这是一个详细的图像生成提示，用于创建一张超风格化、高对比度的未来主义时尚肖像。主体是一位拥有电蓝色皮肤的女性，戴着醒目的黄色太阳镜和一顶有纹理的橙色毛线帽。提示指定了霓虹赛博朋克美学、影棚布光、超现实细节，并明确列出了负面提示，以确保获得干净、高质量的编辑级外观。

![赛博朋克时尚肖像，电光蓝皮肤](https://cms-assets.youmind.com/media/1769236047762_4nv109_G_YZtE6WoAA3lhI.jpg)

```
Ultra-stylized futuristic fashion portrait of a woman, electric blue skin tone, wearing bold oversized {argument name="sunglasses color" default="yellow"} sunglasses with {argument name="lens color" default="orange reflective"} lenses, vibrant orange eyeshadow and long dramatic eyelashes, matte blue lips, minimalistic expression, head slightly tilted upward, wearing a textured orange beanie. High contrast color palette (blue & orange), neon cyberpunk aesthetic, studio lighting, smooth skin texture, hyper-realistic, ultra sharp focus, 8K resolution, editorial fashion photography, modern art style, clean background, cinematic lighting, luxury fashion vibe.
blur, low resolution, grain, noise, distortion, asymmetrical face, extra limbs, watermark, text, logo, oversharpen.
```

[[High Contrast Studio]]

---

### 130. 几何马赛克构图提示

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成指定主题（默认为凤凰）的动态马赛克构图的提示，该构图由一系列精致的彩色瓷砖构成。它强调精确的几何布局和对古典马赛克艺术的现代诠释。

![几何马赛克构图提示](https://cms-assets.youmind.com/media/1769236059378_fqecgr_G_YZihUWEAAObs2.jpg)

```
A dynamic mosaic composition featuring a {argument name="subject" default="phoenix"} built from an array of delicate {argument name="color" default="[color]"} tiles, arranged in a precise, geometric layout on a clean white field. The intricate design offers a contemporary twist on classical mosaic art. Aspect ratio 6:9
```

[[Phoenix Theme]]

---

### 131. 罗马浴场超现实时尚大片提示词

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-01-23  **Language**: en

> 一个高度详细的提示，用于生成一张超高端时尚编辑图片：主体身着金色湿身紧身连衣裙，置身古罗马浴场，带有蛇形纹身，强调冷峻、主导的表情和物理上正确的灯光。

![罗马浴场超现实时尚大片提示词](https://cms-assets.youmind.com/media/1769236022995_yfpu5p_G_YNWuFXIAAuKiq.jpg)
![罗马浴场超现实时尚大片提示词](https://cms-assets.youmind.com/media/1769236022667_7xe4o1_G_YNWlUXYAA7FSE.jpg)
![罗马浴场超现实时尚大片提示词](https://cms-assets.youmind.com/media/1769236022869_c7pqle_G_YNWruWUAEyfhl.jpg)

```
{
  "prompt": "Hyper-realistic editorial fashion photo of Ana de Armas in ancient Roman thermal baths, shallow water, commanding dominant presence, cold untouchable expression, gold deep-V wet clinging dress, snake tattoo on left leg, 85mm lens, shallow DOF, 3:4",
  "style": "Ultra-high-end hyper-realistic fashion photography, cinematic editorial realism, natural optics, physically correct lighting, zero stylization, pure photographic",
  "aspect_ratio": "3:4",
  "resolution": "8k",
  "lighting": "Bright controlled soft daylight, natural highlights, soft shadows, subtle water reflections, clean exposure",
  "camera_angle": "Slightly below chest level, medium-close to mid-body, 85mm lens, shallow depth of field",
  "subject": {
    "name": "{argument name="subject name" default="Ana de Armas"}",
    "face": "Cold dominant symmetrical features, porcelain skin with subtle warmth",
    "expression": "Predatory calm, direct locked gaze, no smile, closed relaxed lips, untouchable authority",
    "makeup": "Minimal sculpted, eye and bone structure emphasis",
    "hair": "Long straight, dark roots to lighter ends, slightly damp, clean parting",
    "physique": "Elegant powerful feminine, strong confident posture",
    "skin": "Fair luminous, realistic wet sheen on lower body, detailed full-wrap snake tattoo on left leg",
    "outfit": "Thin gold deep-V draped swim-dress hybrid, soaked clinging lower half, deep plunging neckline",
    "jewelry": "Diamond drop earrings, layered fine gold necklaces, gold arm cuff",
    "pose": "Lying with elbows in shallow water, one leg bent one extended forward, torso slightly back, hips grounded, owning space"
  },
  "environment": {
    "location": "Ancient Roman thermal baths, pale stone classical columns and architecture",
    "atmosphere": "Bright soft diffused daylight, majestic but secondary to subject",
    "background": "Softly blurred classical stone structures"
  },
  "image_quality": {
    "detail_level": "Hyper-realistic skin micro-detail, natural wet sheen, detailed tattoo",
    "overall_vibe": "Aggressive elegance, calm dangerous superiority, pure authority and sexual confidence"
  }
}
```

[[Dominant Expression]]

---

### 132. 纽约街头女性的狗仔队式抓拍

**Author**: [jennieee:3](https://x.com/jenniebae_ai)  **Date**: 2026-01-23  **Language**: en

> 一个详细的提示，用于生成一张年轻女性（与安雅·泰勒-乔伊 (Anya Taylor-Joy) 神似）在纽约市繁忙人行道上行走的全身照，要求照片具有真实感、抓拍感和狗仔队风格，并详细说明她的着装（带文字的露脐上衣、皮质迷你裙、及膝靴）以及粗犷的都市背景元素。

![纽约街头女性的狗仔队式抓拍](https://cms-assets.youmind.com/media/1769236015549_68ope1_G_YLLHOXMAAawSQ.jpg)
![纽约街头女性的狗仔队式抓拍](https://cms-assets.youmind.com/media/1769236015432_u98lsv_G_YLLHQXUAAtZRD.jpg)
![纽约街头女性的狗仔队式抓拍](https://cms-assets.youmind.com/media/1769236015528_wxq254_G_YM5CVW0AE3iWV.jpg)

```
{
  "prompt": "A photorealistic candid paparazzi-style full-body shot of a young woman with long straight platinum blonde hair walking down a busy New York City sidewalk. She is wearing a white baby tee crop top with the text '{argument name="shirt text" default="I <3 COWBOYS"}' in pink glittery font, a short black leather mini skirt, and black knee-high leather boots. She is wearing dark cat-eye sunglasses and clutching a black purse and phone. The background features typical urban scenery including construction scaffolding, a white delivery truck, a trash bin, and blurred pedestrians, shot with natural daylight and high-resolution texture."
}
```

[[Full Body Shot]] [[Knee-High Boots]]

---

### 133. 生成自定义插图的说明

**Author**: [AI Pulse](https://x.com/youraipulse)  **Date**: 2026-01-23  **Language**: en

> 一个简单的指令提示，让 Nano Banana 按需生成定制插画。

![生成自定义插图的说明](https://cms-assets.youmind.com/media/1769236045789_eq15bp_G_YGVd0WsAAqyXu.jpg)
![生成自定义插图的说明](https://cms-assets.youmind.com/media/1769236045807_vznt2h_G_YDN0tXsAAHfoK.jpg)

```
Generate custom illustrations on demand
```

[[AI Workflow]]

---

### 134. Nano Banana Pro 的九宫格面部一致性网格提示词

**Author**: [Ajala Victor 👑 | Visual/Brand Designer](https://x.com/avstudiosng)  **Date**: 2026-01-23  **Language**: en

> 这是一个高度详细、结构化的提示，旨在生成一个 3x3 网格的女性面部特写肖像，确保九个不同头部角度和视角下的面部绝对一致。它旨在与 Nano Banana Pro 配合使用，以创建全面的面部轮廓参考，在图像生成中保持相同的特征、光照和真实感，从而确保角色的一致性。

![Nano Banana Pro 的九宫格面部一致性网格提示词](https://cms-assets.youmind.com/media/1769235973313_e7cgal_G_X57VvXoAEhiBv.jpg)
![Nano Banana Pro 的九宫格面部一致性网格提示词](https://cms-assets.youmind.com/media/1769235973397_ekhzd3_G_X57VzW8AA8y6w.jpg)

```
Use the provided reference image as the sole identity and facial structure reference. Create a 3 by 3 grid of face focused portraits of the same woman, maintaining identical facial features, proportions, expression baseline, and realism across all frames.

Each panel should show a distinct head angle and facial perspective, while preserving lighting consistency, lens realism, and natural skin texture. No change in hairstyle, makeup style, or facial identity.

Grid breakdown

Top row
1.Front facing neutral angle, eyes looking directly into camera
2.Three quarter view facing right, slight head tilt, eyes forward
3.Full right side profile, clean silhouette of nose, lips, and jawline

Middle row
4. Three quarter view facing left, soft head tilt, confident gaze
5. Slight low angle looking down toward the camera, subtle power pose
6. Slight high angle looking upward, relaxed expression

Bottom row
7. Head turned right with eyes looking back toward camera
8. Head turned left with eyes looking back toward camera
9. Near rear three quarter angle showing cheekbone, jawline, and ear contour

Technical and visual requirements

Ultra realistic portrait photography
85mm lens look, shallow depth of field
Sharp facial detail, visible skin texture, natural pores
Soft daylight illumination with gentle shadow falloff
Neutral background with no distractions
Consistent framing so all faces align cleanly within the grid
High resolution, editorial quality, fashion and beauty standard

Strict constraints

Do not alter facial structure
Do not stylize or cartoonize
Do not change expression drastically
No text, no watermark, no distortion
Same person in all nine frames
```

[[Close-Up Portrait]] [[Character Reference Sheet]]

---

### 135. OL 制服编辑提示

**Author**: [BeautyVerse](https://x.com/BeautyVerse_Lab)  **Date**: 2026-01-23  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张逼真的图片：一位年轻的亚洲女性身着性感的 OL 制服（紧身白衬衫、超短迷你裙、过膝袜），坐在办公桌上，背景是现代公司内景和城市天际线。

![OL 制服编辑提示](https://cms-assets.youmind.com/media/1769236023824_aqdj6j_G_XXhabbAAE9SaU.jpg)

```
{
  "prompt_data": {
    "subject": {
      "basics": "1girl, solo",
      "demographics": "Stunning 20s Asian female idol style, tall fashion model proportions",
      "hair": "Very long straight black hair with full bangs",
      "eyes": "Large, round, piercing eyes",
      "skin": "Flawless pale skin",
      "expression": "Cute yet seductive expression looking at viewer"
    },
    "attire": {
      "main_outfit": {
        "item": "Seductive Office Lady uniform",
        "details": [
          "Tight white button-up shirt",
          "Black micro-miniskirt",
          "Skirt hem cut extremely high",
          "Professional yet alluring silhouette"
        ],
        "branding": "None"
      },
      "legwear": [
        "Sheer dark blue thigh-high stockings",
        "Intricate floral lace pattern on stockings",
        "Dark blue lace garter belt with suspenders"
      ]
    },
    "accessories": {
      "style": "Luxurious gold accessories",
      "items": [
        "Slim gold watch",
        "Delicate gold chain necklace with ruby pendant",
        "Long gold chain earrings"
      ]
    },
    "pose_and_action": {
      "posture": "Sitting gracefully on the edge of an office desk",
      "interaction": "Legs crossed elegantly"
    },
    "environment": {
      "setting": "Modern high-end corporate office interior",
      "background_elements": "Blurred city skyline through floor-to-ceiling glass windows, sleek office furniture"
    },
    "style_and_technical": [
      "Subtle shadows",
      "Cinematic soft lighting",
      "Highly detailed face and eyes",
      "Realistic materials",
      "Photorealistic",
      "Sharp focus",
      "8k",
      "3:4"
    ]
  }
}
```

[[Mini Skirt]] [[White Button Shirt]] [[Asian Female Model]]

---

### 136. 街头浪漫纪实电影剧照提示词（书店）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-23  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超逼真的、抓拍式的街头摄影图像，类似于电影剧照，场景设定在卡德柯伊（Kadıköy）的一家二手书店。它着重捕捉一对年轻情侣之间亲密而宁静的瞬间，强调真实性标记，如真实的皮肤纹理、轻微的瑕疵、有动机的实用照明，以及不完美的、纪录片风格的手持构图（35mm 镜头）。

![街头浪漫纪实电影剧照提示词（书店）](https://cms-assets.youmind.com/media/1769235996718_j3122i_G_XW1rGWEAAJ5wC.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_candid_street_romance",
      "version": "v2.0_KADIKOY_BOOKSHOP_SILENT_SMILES_EN",
      "priority": "highest"
    },
    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "ultra_photoreal_candid_street_film_still",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "color_grade": "true_to_life_indoor_natural",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "global_rules": {
      "camera_language": "35mm lens equivalent, eye-level, imperfect handheld framing, documentary candid feel, focus on eyes when faces are visible",
      "lighting_language": "motivated practical light only (bookshop warm lamps + window daylight spill), no studio look, no flash",
      "authenticity_markers": "real skin texture, slight under-eye shadows, realistic indoor noise, no HDR, no AI glow, no symmetry"
    },
    "creative_prompt": {
      "scene_summary": "{argument name="location" default="Kadıköy"}, a small second-hand bookshop. The same young couple quietly browsing the same shelf. A candid moment, like a friend captured it while passing by.",
      "subjects": {
        "count": 2,
        "description": "the same young man and woman (early 20s), ordinary, real, not model-like; faces visible and sharp",
        "expression": "soft calm smiles, comfortable silence, micro-expressions only",
        "skin_and_face": "natural texture, no beauty retouch, real imperfections preserved"
      },
      "wardrobe_and_props": {
        "clothing": "simple student outfits in neutral tones, slightly wrinkled fabric, no logos",
        "props": "one holds a worn paperback, the other points at a book spine; a tote bag with books, no branding"
      },
      "micro_action": "their hands almost touch on the same book; they pause, exchange a small smile, then look back to the shelf",
      "environment_details": {
        "location": "Kadıköy bookshop vibe",
        "background": "tight aisles, stacked books, warm lamps, a window with soft daylight, people as soft silhouettes, no readable text"
      },
      "composition": "eye-level medium shot, slightly off-center, imperfect crop, faces sharp, background gently receding",
      "mood": "quiet, intimate, real—love as shared silence"
    },
    "negative_prompt": [
      "studio lighting",
      "flash",
      "beauty retouch",
      "plastic skin",
      "model faces",
      "perfect symmetry",
      "HDR",
      "AI glow",
      "fake bokeh",
      "text",
      "logo",
      "watermark",
      "posed romance poster look"
    ]
  }
}
```

[[Documentary Style]]

---

### 137. Z 世代凌乱仙女自拍拼贴提示词

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-01-23  **Language**: en

> 一个复杂的 JSON 提示，旨在生成一个 2x2 网格拼贴画，内容为超广角自拍，风格为 Z 世代随性社交媒体分享，主体人物酷似 Sydney Sweeney。该提示详细描述了图像结构、全局风格设置（0.5 倍镜头、高角度畸变、混乱的仙女美学）、主体细节（服装、妆容、配饰），以及四个面板中每个面板的具体表情和姿势（吐舌头、嘟嘴、眨眼）。

![Z 世代凌乱仙女自拍拼贴提示词](https://cms-assets.youmind.com/media/1769235991833_0bnmr6_G_XSEOhbEAAdlmQ.jpg)

```
:-
{
  "image_structure": {
    "format": "2x2 Grid Collage",
    "total_panels": 4,
    "layout_style": "Four distinct 0.5x wide-angle selfies arranged in a square grid",
    "aspect_ratio": "Square (1:1) or 4:5 overall ratio containing four vertical 3:4 images"
  },
  "global_style_settings": {
    "camera_effect": "0.5x Ultra-wide angle lens / Fisheye effect",
    "perspective": "High-angle selfie with arm distortion (arms appear elongated and large in foreground)",
    "lighting": "Indoor ambient overhead light mixed with front-facing phone screen flash (bright, slightly cool toned)",
    "aesthetic": "Gen Z candid social media dump, chaotic fairy vibes"
  },
  "subject_universal_details": {
    "demographics": "Young woman, approx 20 years old, Caucasian",
    "skin": "Fair/Pale complexion with cool pink undertones, very smooth skin texture",
    "hair": "Dirty blonde/light brown roots transitioning to blonde lengths, styled in a messy high bun (topknot) with loose face-framing wispy strands",
    "outfit": "{argument name="outfit color" default="Lime green"}/Chartreuse mini dress covered in large circular sequins, thin spaghetti straps",
    "accessories": [
      "Large translucent light green fairy wings with glittery vein details",
      "Black plastic tattoo-style choker necklace"
    ],
    "makeup": "Heavy black winged eyeliner (cat eye), subtle mascara, highlighter on the tip of the nose, rosy pink blush on high cheekbones, glossy mauve/pink natural lip color"
  },
  "panel_breakdown": {
    "top_left_panel": {
      "expression": "Playful, tongue sticking out flat",
      "gaze": "Looking directly into camera",
      "pose": "Head slightly tilted, both arms extended forward towards lens",
      "specific_detail": "Tongue is extended downwards, eyes wide open"
    },
    "top_right_panel": {
      "expression": "Duck face / Pouty lips",
      "gaze": "Looking straight at camera",
      "pose": "Chest forward, shoulders up, arms framing the body",
      "specific_detail": "Lips pursued together, innocent expression"
    },
    "bottom_left_panel": {
      "expression": "Winking (Left eye closed, Right eye open), subtle pout",
      "gaze": "Looking straight at camera",
      "pose": "Head tilted to her right, leaning slightly back",
      "specific_detail": "One eye scrunched closed tight, jawline defined"
    },
    "bottom_right_panel": {
      "expression": "Winking (Left eye closed, Right eye open), exaggerated kissy face",
      "gaze": "Looking straight at camera",
      "pose": "Head tilted to her left, body angled slightly",
      "specific_detail": "Lips puckered forward for a kiss, eyebrows slightly raised"
    }
  },
  "background_environment": {
    "location": "Suburban living room",
    "furniture": "Dark grey fabric sectional sofa (visible behind her in all shots)",
    "architecture": "White staircase with banister rails visible in background (top left and bottom left specifically)",
    "decor": "Wooden vertical "
  }
```

[[2x2 Grid Collage]] [[Sydney Sweeney Likeness]]

---

### 138. 黑暗科幻动作场景，带有毒液般的共生体

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-23  **Language**: en

> 一个高度详细的 JSON 提示，用于在黑暗的工业仓库中生成一个超现实的 16K 电影级动作场景。该提示聚焦于一个年轻女性（已启用身份锁定），她摆出动感的动作姿势，一个凶猛、光滑的黑色、毒液般的异形共生体正从她背部爆裂而出，强调高对比度、暖色边缘光和戏剧性的低角度构图。

![黑暗科幻动作场景，带有毒液般的共生体](https://cms-assets.youmind.com/media/1769235965535_jrzyig_G_XKm0ZbIAAcxlL.jpg)

```
{
  "identity_lock": {
    "reference_image": "uploaded_reference_image",
    "face_editing": "disabled",
    "preserve_facial_features": true,
    "preserve_proportions": true
  },
  "scene": {
    "description": "Ultra-realistic cinematic action scene",
    "resolution": "16K",
    "style": "Hollywood action-movie poster",
    "genre": "dark sci-fi action"
  },
  "subject": {
    "person": "same young woman from reference",
    "pose": {
      "stance": "dynamic action",
      "body_position": "slightly crouched forward",
      "legs": "one knee bent",
      "hands": {
        "left_hand": "pressed against the ground",
        "right_hand": "reaching outward"
      }
    },
    "expression": "focused and intense",
    "motion": "mid-action, about to leap or attack"
  },
  "symbiote": {
    "type": "{argument name="symbiote type" default="Venom-like alien symbiote"}",
    "origin": "bursting from her back",
    "features": [
      "large menacing tendrils",
      "aggressive snarling face above shoulder"
    ],
    "material": "glossy black organic texture",
    "behavior": "violent expansion and movement"
  },
  "environment": {
    "location": "dark industrial warehouse",
    "atmosphere": [
      "misty",
      "smoke-filled",
      "floating dust particles"
    ],
    "lighting": {
      "primary": "sharp cinematic light beams cutting through fog",
      "highlights": "warm rim lighting on subject and symbiote"
    }
  },
  "camera": {
    "angle": "low angle",
    "tilt": "slightly tilted",
    "lens": "cinematic wide lens",
    "depth_of_field": "shallow",
    "motion_blur": "subtle directional blur"
  },
  "post_processing": {
    "effects": [
      "lens flares",
      "warm highlights",
      "cinematic color grading",
      "subtle film grain"
    ],
    "contrast": "high",
    "sharpness": "ultra-detailed"
  },
  "mood": {
    "energy": "high intensity",
    "tone": "dark, powerful, aggressive",
    "cinematic_feel": "epic and dramatic"
  }
}
```

[[Low Angle Composition]]

---

### 139. 奢华俄罗斯冬季雪橇场景提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-23  **Language**: en

> 为 Nano Banana Pro 生成一个电影感十足、充满活力的场景的详细提示：一对迷人的情侣乘坐雪橇从雪坡上滑下。该提示详细说明了人物的外观（使用参考图像）、他们奢华的服装、动态的拍摄角度（从上方倾斜）和光线（清澈的金色阳光），以 5:4 的宽高比创作出精致、动感十足的视觉效果。

![奢华俄罗斯冬季雪橇场景提示](https://cms-assets.youmind.com/media/1769235978362_regtmw_G_XG40CbQAAf_lk.jpg)

```
A glamorous young woman a reference image, with glossy, flowing blonde hair and sparkling, joyful eyes, elegantly dressed in a sumptuous, pristine white fur coat-her appearance radiant, poised, and unmistakably luxurious. She sits just behind a strikingly handsome young man a reference image with defined, aristocratic features and fair skin, outfitted in a premium matte black down jacket, paired with a chunky designer cashmere scarf. The couple accelerate down a snowy hillside on a sleek, polished wooden sled, the camera angle dynamically tilted from above and slightly to the side, amplifying the sensation of speed and excitement. Snow churris up in glittering jets all around them, illuminated by crisp, golden sunlight and caught in dazzling, icy fragments. The composition captures them in sharp, theatrical focus; their figures are charged with motion-her arms lifted wide in exuberance, his confident smile and tousled hair echoing the thrill, luxurious boots airborne. The blurred snowy slope behind is rendered in luminous blues and silvers, while warm sunlight highlights their flawless skin and elite outerwear textures. The mood bursts with adrenaline, exclusive fun, and magnetic connection-luxury, vitality, and the sparkling magic of a Russian winter adventure at its most cinematic and refined and 5:4 image ratio.
```

[[Golden Sunlight]] [[Luxury Winter Fashion]]

---

### 140. 超逼真昏暗卧室场景提示词

**Author**: [calm](https://x.com/calmgenx)  **Date**: 2026-01-23  **Language**: en

> 一个给 Nano Banana Pro 的简单提示，用于根据附带的参考照片生成一张超现实图像。场景是夜晚昏暗的卧室，主体趴着拍照，长宽比为 3:4。

![超逼真昏暗卧室场景提示词](https://cms-assets.youmind.com/media/1769235982633_a9zuxt_G_XGlRpbEAAu1eQ.jpg)

```
Generate an image referencing the image attached, quality is ultra realistic, scene is a dim bedroom at night,posed is lying on her stomach, taking a picture, aspect ratio 3:4
```

[[Prone Pose]]

---

### 141. 复古怀旧肖像提示（乌尔都语/印地语细节）

**Author**: [Qaiser Tzq](https://x.com/TzqQaiser)  **Date**: 2026-01-23  **Language**: en

> 一个结构化的 JSON 提示，用于生成两张具有复古美学风格的图像，画面中一位酷似安娜·德·阿玛斯（Ana de Armas）的女性身着缎面吊带裙，背景是深色木质护墙板和古董家具。该提示使用乌尔都语/印地语词汇描述了人物的表情和服装细节。

![复古怀旧肖像提示（乌尔都语/印地语细节）](https://cms-assets.youmind.com/media/1769236027280_k13rtn_G_XFU1RboAA9A9O.jpg)
![复古怀旧肖像提示（乌尔都语/印地语细节）](https://cms-assets.youmind.com/media/1769236027176_153f4x_G_XFU2YaQAA7ZTY.jpg)

```
{
  "album_info": {
    "theme": "Vintage Retro Aesthetic",
    "color_palette": ["Burgundy", "Warm Brown", "Cream", "Deep Green"],
    "lighting": "Soft indoor ambient lighting"
  },
  "images": [
    {
      "file_name": "20260123_211052.jpg",
      "subject_details": {
        "appearance": "Ana de Armas se mushaba khatoon",
        "expression": "Sanjeeda aur pur-asrar (Mysterious)",
        "pose": "Baayen hath se dress ki strap pakdi hui, sofa par sahara liye hue",
        "clothing": {
          "material": "Satin/Silk",
          "color": "Gehra surkh (Burgundy/Wine)",
          "style": "Sleeveless slip dress"
        }
      },
      "environment_details": {
        "background": "Vertical dark wood paneling",
        "furniture": {
          "type": "Antique Couch",
          "pattern": "Floral/Traditional tapestry upholstery"
        },
        "decor": {
          "lamp": "Cream colored scalloped lampshade with fringe",
          "cushions": ["Surkh velvet takiya", "Sufaid faux-fur takiya"],
          "plants": "Ghane patton wala indoor plant (Pothos/Ivy type)"
        }
      }
    },
    {
      "file_name": "20260123_211050.jpg",
      "subject_details": {
        "appearance": "Wahi khatoon, mukhtalif angle",
        "expression": "Naram aur pur-sukoon",
        "pose": "Daaya hath sar ke peeche (relaxed posture), taangein samne ki taraf",
        "clothing": {
          "material": "Satin",
          "color": "Burgundy",
          "fit": "Body-hugging"
        }
      },
      "environment_details": {
        "background": "Brown wooden wall with a framed botanical sketch",
        "furniture": {
          "type": "Retro Sofa",
          "pattern": "Brown and tan checkered/plaid design"
        },
        "decor": {
          "lamp": "Tall vintage floor lamp with a glowing warm bulb",
          "cushions": ["Plain burgundy velvet pillow", "Fluffy white cream pillow"],
          "flooring": "Shag-style beige rug (neechay ka qaleen)"
        }
      }
    }
  ]
}
```

[[Ana De Armas Likeness]] [[Vintage Aesthetic]] [[Satin Slip Dress]]

---

### 142. 抓拍社交媒体自拍提示（自动扶梯）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 提示，用于生成一张坦率的、高角度的 iPhone 自拍，具有社交媒体网红美学。主体是一位留着短卷发的年轻女性，在购物中心的自动扶梯上，做出俏皮的嘟嘴/飞吻表情。提示中指定了自然的室内光线、米色背心，以及黑色皮革单肩包肩带和手腕上的发圈等细节。

![抓拍社交媒体自拍提示（自动扶梯）](https://cms-assets.youmind.com/media/1769236002462_s92ep6_G_W-yQXbAAElyUR.jpg)
![抓拍社交媒体自拍提示（自动扶梯）](https://cms-assets.youmind.com/media/1769236002381_4c9hc4_G_W-yJvbAAId-aN.jpg)

```
{
  "prompt": "Candid selfie photo from above, young woman with brown goldish short wavy hair, looking up at camera making duck face kiss pout expression, light blue grey eyes, natural minimal makeup with pink nude lips, wearing cream beige tank top with thin straps, black leather shoulder bag strap visible, black hair scrunchie on wrist, silver ring on finger, white manicured nails, standing on escalator looking up, metal escalator steps visible below, another person partially visible behind in polka dot shirt, shopping mall or metro station setting, overhead high angle selfie perspective, natural indoor lighting, casual street style, social media influencer aesthetic, iPhone selfie style",
  "negative_prompt": "studio lighting, outdoor nature, formal clothing, serious expression, side angle, full body shot",
  "style": "candid street selfie, social media content, casual everyday moment",
  "aspect_ratio": "3:4",
  "camera": {
    "type": "smartphone front camera selfie",
    "angle": "high overhead angle looking down at subject",
    "framing": "close up face and upper body from above"
  },
  "lighting": {
    "type": "natural indoor ambient light",
    "quality": "soft even lighting, no harsh shadows",
    "atmosphere": "casual everyday indoor setting"
  },
  "mood": "playful, fun, casual, flirty, spontaneous",
  "color_palette": "platinum white hair, cream beige, black accents, silver metal, neutral tones",
  "subject_features": {
    "hair": "{argument name="hair color" default="brown goldish"}, short shoulder length, soft waves, middle parted",
    "skin": "fair, clear, natural, porcelain",
    "eyes": "light blue grey, looking directly up at camera",
    "lips": "natural pink, pursed in kiss pout duck face",
    "expression": "playful duck face kiss pout, looking at camera",
    "eyebrows": "natural dark brown, well groomed"
  },
  "wardrobe": {
    "top": "cream beige ribbed tank top with thin spaghetti straps",
    "accessories": "black leather shoulder bag with strap across shoulder, black fabric hair scrunchie on wrist, silver chunky ring on finger",
    "nails": "white or light pink manicure"
  },
  "setting": {
    "location": "escalator in shopping mall or metro station",
    "background": "metal escalator steps, black handrail, another person behind",
    "context": "casual everyday urban moment"
  }
}
```

[[Social Media Influencer Aesthetic]]

---

### 143. 复古未来主义 1970 年代科幻全身肖像 JSON 提示词

**Author**: [Vlad Sydor](https://x.com/vlad_sydor)  **Date**: 2026-01-23  **Language**: en

> 一个用于 Nano Banana Pro 的双格式提示（文本和 JSON），以生成一张具有复古未来主义 1970 年代科幻美学的超逼真全身肖像。主体是一位留着卷曲金发、戴着鼻环的女性，手持红色棒棒糖，置身于一个极简、同质的白色空间中，带有定向照明。

![复古未来主义 1970 年代科幻全身肖像 JSON 提示词](https://cms-assets.youmind.com/media/1769235980128_50l71j_G_W2LKrXQAAyWhT.jpg)

```
{
  "subject": {
    "identity": "A white woman",
    "attributes": [
      "Dark irises",
      "Tightly coiled blonde hair",
      "Metal ring nose piercing",
      "Heavy-knit black sweater",
      "White skirt",
      "Long white socks",
      "Black shoes"
    ]
  },
  "action": "Holding a translucent red lollipop near her face",
  "environment": {
    "location": "A homogeneous white space",
    "lighting": "Natural directional lighting",
    "atmosphere": "Minimalist aesthetic with no objects in the background"
  },
  "composition": {
    "framing": "Full body shot",
    "camera": {
      "lens": "35mm",
      "aperture": "f/2.8"
    }
  },
  "style": {
    "medium": "Photorealistic with film grain",
    "aesthetic": "Retro-futuristic 1970 sci-fi vibe",
    "colors": [
      "Monochrome white",
      "Deep black",
      "Translucent red"
    ]
  },
  "technical": {
    "aspect_ratio": "9:16",
    "fidelity_level": "8k resolution"
  }
}
```

[[Directional Lighting]]

---

### 144. 在自动扶梯上摆出嘟嘴表情的抓拍自拍提示

**Author**: [Sudee🥀](https://x.com/NameIsSudee)  **Date**: 2026-01-23  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张年轻女性（安娜·德·阿玛斯或约瑟芬·兰福德的形象）在购物中心自动扶梯上摆出俏皮“鸭子嘴”亲吻姿势的坦率高角度自拍照，重点突出特定的配饰、灯光和社交媒体网红美学。

![在自动扶梯上摆出嘟嘴表情的抓拍自拍提示](https://cms-assets.youmind.com/media/1769236016712_svuqb3_G_W4HuObAAASlP8.jpg)
![在自动扶梯上摆出嘟嘴表情的抓拍自拍提示](https://cms-assets.youmind.com/media/1769236017075_exzro2_G_W4HuSbAAUgRnZ.jpg)

```
{
  "prompt": "Candid selfie photo from above, young woman with brown goldish short wavy hair, looking up at camera making duck face kiss pout expression, light blue grey eyes, natural minimal makeup with pink nude lips, wearing cream beige tank top with thin straps, black leather shoulder bag strap visible, black hair scrunchie on wrist, silver ring on finger, white manicured nails, standing on escalator looking up, metal escalator steps visible below, another person partially visible behind in polka dot shirt, shopping mall or metro station setting, overhead high angle selfie perspective, natural indoor lighting, casual street style, social media influencer aesthetic, iPhone selfie style",
  "negative_prompt": "studio lighting, outdoor nature, formal clothing, serious expression, side angle, full body shot",
  "style": "candid street selfie, social media content, casual everyday moment",
  "aspect_ratio": "3:4",
  "camera": {
    "type": "smartphone front camera selfie",
    "angle": "high overhead angle looking down at subject",
    "framing": "close up face and upper body from above"
  },
  "lighting": {
    "type": "natural indoor ambient light",
    "quality": "soft even lighting, no harsh shadows",
    "atmosphere": "casual everyday indoor setting"
  },
  "mood": "playful, fun, casual, flirty, spontaneous",
  "color_palette": "platinum white hair, cream beige, black accents, silver metal, neutral tones",
  "subject_features": {
    "hair": "brown goldish, short shoulder length, soft waves, middle parted",
    "skin": "fair, clear, natural, porcelain",
    "eyes": "light blue grey, looking directly up at camera",
    "lips": "natural pink, pursed in kiss pout duck face",
    "expression": "playful duck face kiss pout, looking at camera",
    "eyebrows": "natural dark brown, well groomed"
  },
  "wardrobe": {
    "top": "cream beige ribbed tank top with thin spaghetti straps",
    "accessories": "black leather shoulder bag with strap across shoulder, black fabric hair scrunchie on wrist, silver chunky ring on finger",
    "nails": "white or light pink manicure"
  },
  "setting": {
    "location": "escalator in shopping mall or metro station",
    "background": "metal escalator steps, black handrail, another person behind",
    "context": "casual everyday urban moment"
  }
}
```

[[Ana De Armas Likeness]] [[Social Media Influencer Aesthetic]]

---

### 145. 超现实主义融化 Logo 生成模板

**Author**: [PSS](https://x.com/PromptSin)  **Date**: 2026-01-23  **Language**: en

> 这是一个提示模板，旨在生成品牌标志的超现实、融化版本，适用于 Nano Banana PRO。用户只需将占位符 [BRAND] 替换为任何公司名称，即可看到效果。

![超现实主义融化 Logo 生成模板](https://cms-assets.youmind.com/media/1769236017593_66jmmu_G_WyHjqW0AAKafN.png)

```
A surreal, melting logo of {argument name="brand name" default="[BRAND]"} in the style of Salvador Dali, highly detailed, photorealistic, 8k.
```

[[Surrealism]] [[Template Prompt]]

---

### 146. 户外探险场景中运动型女性的详细图像生成提示

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2026-01-23  **Language**: en

> 这是一个极其详细、结构化的提示，专为图像生成（通过 Degaus 应用和 Nano Banana Pro）设计，旨在创建一张在户外探险环境中，一位运动型女性的超逼真图像，重点关注特定的身体特征、服装细节（如救生衣和比基尼），以及相机构图。

![户外探险场景中运动型女性的详细图像生成提示](https://cms-assets.youmind.com/media/1769236011328_bklw8h_G_WrGUtbQAAt-ef.jpg)

```
{
  "subject": {
    "type": "adult woman",
    "age": "mid-20s",
    "overall_vibe": "outdoor adventure, confident sporty energy, natural candid",
    "face": {
      "angle": "back-facing body with head turned over shoulder (three-quarter side profile)",
      "shape": "soft feminine face with high cheekbones and a defined jawline",
      "eyes": "almond-shaped eyes, calm focused gaze toward the side (not straight at viewer)",
      "brows": "full natural brows with a clean arch (slightly darker than hair)",
      "nose": "straight refined bridge with a soft rounded tip",
      "lips": "natural full lips, muted nude tone, relaxed neutral expression",
      "skin": "real skin texture with visible pores, sun-kissed warmth, natural outdoor realism (no beautify smoothing)"
    },
    "hair": {
      "color": "platinum blonde",
      "style": "long hair gathered into a low ponytail/bun tucked through the cap opening; a few loose strands near the neck/ear",
      "length_rule": "keep hair long even if tied back"
    },
    "headwear": {
      "type": "baseball cap",
      "color": "dark navy/charcoal",
      "logo_rule": "no readable logos/text on the cap (keep it blank/neutral)"
    },
    "body": {
      "build": "athletic, gym-trained silhouette with enhanced curves (toned shoulders, strong legs)",
      "proportions": "larger bust and fuller hips/glutes while staying realistic and proportional (no extreme cartoon curves)",
      "bust_detail": "fuller chest volume visible as a natural rounded silhouette under the life vest (subtle, not exaggerated)",
      "hips_glutes_detail": "noticeably larger, rounder glutes and wider hip line; natural muscle + softness balance",
      "waist": "defined waist with smooth transition into fuller hips (hourglass but realistic)",
      "skin_finish": "natural daylight sheen with realistic highlights and soft shadows; wet lower legs with visible waterline marks"
    },
    "expression": "calm, slightly serious, outdoorsy confidence"
  },
  "wardrobe": {
    "outerwear": {
      "type": "life jacket / flotation vest",
      "color": "dusty pink",
      "details": "black straps and buckles across torso, slightly bulky padded shape, realistic fabric texture",
      "fit": "snugger fit across chest due to fuller bust, straps show mild tension without distortion"
    },
    "swimwear": {
      "bottom": {
        "type": "minimal string bikini bottom (thong/brazilian cut)",
        "color": "white",
        "fabric": "matte swim fabric, clean edges, thin side strings",
        "fit": "high-cut on hips, sits cleanly, subtle stretch tension along the fuller hips/glutes (tasteful, non-explicit)"
      },
      "top": {
        "type": "bikini top mostly hidden under vest",
        "hint": "thin strap ties visible at upper back/neck area"
      }
    },
    "jewelry": [
      "small hoop earrings (subtle, no branding)"
    ]
  },
  "pose_action": {
    "shot_type": "outdoor river por"
}
```

[[Outdoor Adventure Athletic Female Portrait]]

---

### 147. 赛博朋克霓虹街头美食广告文案

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-23  **Language**: en

> 一个旨在生成具有赛博朋克美学风格的超风格化商业食品广告的提示。它强调发光的霓虹灯点缀、光泽的纹理、戏剧性的蒸汽、雨雾和充满活力的都市夜景背景，旨在实现高对比度和超细节纹理的电影级美食摄影。

![赛博朋克霓虹街头美食广告文案](https://cms-assets.youmind.com/media/1769235997997_dfjvz3_G_WnSh1a4AA1O-E.jpg)
![赛博朋克霓虹街头美食广告文案](https://cms-assets.youmind.com/media/1769235998123_jdchp8_G_WnSoPWYAAaJJk.jpg)
![赛博朋克霓虹街头美食广告文案](https://cms-assets.youmind.com/media/1769235998120_23ue4e_G_WnStEbAAIrWzQ.jpg)
![赛博朋克霓虹街头美食广告文案](https://cms-assets.youmind.com/media/1769236000173_cu82yu_G_WnSuvboAAzs4E.jpg)

```
Hyper-stylized street food advertisement of [{argument name="food name" default="Food Name"}], glowing neon accents reflecting off glossy textures. Steam rising dramatically, rain mist in the air, vibrant urban night backdrop softly blurred. High contrast lighting, cyberpunk-inspired color palette, ultra-detailed textures, cinematic food photography, 8K realism.
```

[[Cinematic Food Photography]] [[Urban Night Background]]

---

### 148. Nano Banana Pro 文本生成功能

**Author**: [Kalsoom (ghotai )](https://x.com/AIwithGhotai)  **Date**: 2026-01-23  **Language**: en

> 这条推文重点介绍了 Nano Banana Pro 的一个关键功能：它能够在生成的图像中创建清晰、易读的文本，这使其非常适用于徽标、设计和广告。

```
Nano Banana Pro creates clear text in images (logos, designs, ads)
```

[[Typography In Image]]

---

### 149. 手捧咖啡杯的舒适特写肖像

**Author**: [tusina](https://x.com/tusinaai)  **Date**: 2026-01-23  **Language**: en

> 一个高度结构化、细节丰富的提示，用于生成一张具有“抓拍 iPhone 风格”的超写实、亲密特写肖像。场景设定在客厅沙发上，采用暖钨丝灯照明，重点聚焦于一个手持咖啡杯的人物，强调舒适的纹理、柔和的阴影和特定的构图（4:5 宽高比）。它包含大量的负面提示，以确保真实感并遵守内容限制。

![手捧咖啡杯的舒适特写肖像](https://cms-assets.youmind.com/media/1769236041021_oh0a0c_G_WgPOoXEAAxhXA.jpg)

```
{
  "category": "COZY_COUCH_LAMP_CLOSEUP",
  "subject": {
    "clothing": {
      "outfit": "Low-cut V-neck cropped top (no text), tasteful cleavage, fitted, cozy indoor vibe",
      "texture": "Ribbed cotton or soft jersey, realistic folds"
    },
    "accessories": {
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Close-up candid",
    "orientation": "Slightly above angle, relaxed",
    "hands": "One hand holding mug near chin (fingers correct)",
    "gaze": "Gentle eye contact",
    "expression": "Soft smile, cozy"
  },
  "setting": {
    "environment": "Living room couch corner",
    "background_elements": [
      "Warm orange lamp glow behind",
      "Blanket texture visible",
      "Slight lived-in clutter blurred"
    ],
    "depth": "Face sharp, lamp bloom behind, soft background"
  },
  "camera": {
    "shot_type": "Close-up portrait",
    "angle": "Slightly above eye level",
    "focal_length_equivalent": "26mm phone or 50mm pro",
    "framing": "4:5, face dominant",
    "focus": "Eyes sharp"
  },
  "lighting": {
    "source": "Warm tungsten lamp + faint ambient",
    "direction": "Side/front warm",
    "highlights": "Soft glow on cheeks and hair",
    "shadows": "Gentle, comforting"
  },
  "mood_and_expression": {
    "tone": "Relaxed, intimate, relatable",
    "expression": "Soft smile",
    "atmosphere": "Warm, tactile, homey"
  },
  "style_and_realism": {
    "style": "Photorealistic iPhone-candid vibe",
    "imperfections": "Mild grain, slightly imperfect WB"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild phone sensor grain",
    "motion_blur": "None on face"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "plastic skin",
    "over-smoothing",
    "extra fingers",
    "warped mug",
    "readable text",
    "logo",
    "watermark",
    "nudity",
    "areola",
    "nipples",
    "see-through fabric",
    "explicit lingerie"
  ]
}
```

[[Negative Prompt]] [[4:5 Aspect Ratio]]

---

### 150. 夏季牛仔时尚大片人像提示词

**Author**: [Stark](https://x.com/katmanai)  **Date**: 2026-01-23  **Language**: en

> 一个详细的提示，用于生成具有时尚杂志美学的电影感户外夏季肖像。画面中，一位留着波浪状蜂蜜金色长发的女士，身穿结构感牛仔紧身胸衣式上衣和配套短裤，斜倚在一棵纹理丰富的树干上。场景设置在郁郁葱葱的绿色植物中，拥有明亮的自然阳光和斑驳的阴影，使用 50mm 镜头强调了超细节的牛仔面料和发丝。

![夏季牛仔时尚大片人像提示词](https://cms-assets.youmind.com/media/1769236011026_4jc9rz_G_WdW12XYAEhRIC.jpg)

```
{
  "main_prompt": "Cinematic outdoor summer portrait of a stunning young woman with very long wavy honey-blonde hair, serene and striking gaze, natural skin texture with subtle sun-kissed glow, wearing a stylish structured {argument name="outfit material" default="denim"} corset-style bodice with a pointed hem and matching denim shorts, leaning gracefully against a textured tree trunk, bright natural sunlight with dappled shadows from leaves, lush green foliage and trees in the background, 50mm portrait photography, photorealistic, hyper-detailed denim fabric grain and hair strands --ar 1:2 --stylize 250 --v 6 --q 2",
  "negative_prompt": "blurry, deformed, extra limbs, bad anatomy, ugly, overexposed, harsh shadows, heavy filter, smiling, indoor, synthetic look, cartoon, drawing, high-fashion makeup, studio lighting, plastic skin",
  "style_tags": ["summer outdoor aesthetic", "denim fashion editorial", "honey blonde hair", "natural sunlight", "serene portrait"],
  "technical": {
    "aspect_ratio": "1:2",
    "lighting": "bright natural sunlight with dappled shadows",
    "camera": "50mm professional portrait lens"
  },
  "extra_parameters": {
    "recommended_model": "Flux.1 [dev]",
    "guidance_scale": "7.0",
    "steps": "40",
    "image_reference": "use uploaded reference for the specific honey-blonde hair length/waves, the denim corset-style top design, the leaning pose against the tree, and the bright summer outdoor mood"
  }
}
```

[[50mm Lens]]

---

### 151. 2000 年代风格的夜生活电影拼贴

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-01-23  **Language**: en

> 一个 JSON 提示，旨在为一位迷人的年轻女性（“It-girl”）在夜生活场景中创建三张照片的电影感拼贴画，强调 2000 年代的派对氛围。该拼贴画包含三个不同的镜头：顶层公寓中的黑暗剪影、带有闪光灯和运动模糊的抓拍特写，以及酒店房间中的全身照，所有这些都通过高对比度、复古胶片纹理风格统一起来。

![2000 年代风格的夜生活电影拼贴](https://cms-assets.youmind.com/media/1769235963338_4wc83k_G_WcSgkXMAAHeq_.jpg)

```
{
  "concept": "Cinematic Collage",
  "layout": "Three-photo collage",
  "subject": {
    "description": "Glamorous young girl",
    "hair": "Long hair",
    "hair_note": "Do not change original hair color",
    "vibe": "It-girl"
  },
  "photos": [
    {
      "id": 1,
      "shot_type": "Dark silhouette",
      "setting": "Luxury penthouse, floor-to-ceiling window",
      "time_of_day": "Night",
      "background": "Glowing city lights, {argument name="city background" default="Moscow City skyscrapers"}",
      "pose": "Standing, sexy pose"
    },
    {
      "id": 2,
      "shot_type": "Candid close-up",
      "lighting": "Direct camera flash",
      "outfit": "Shiny dark mini dress",
      "details": [
        "Tousled hair covering part of face",
        "Motion blur",
        "40mm film grain"
      ],
      "atmosphere": "Party atmosphere"
    },
    {
      "id": 3,
      "shot_type": "Full body / Environmental",
      "action": "Lying on a white bed, holding a phone",
      "location": "Hotel room",
      "outfit": {
        "dress": "Short dark shiny mini-dress",
        "shoes": "Stylish dark closed-toe shoes on a thick silk-finish platform"
      },
      "details": [
        "Rumpled bed sheets",
        "Bright photography"
      ],
      "atmosphere": "Moody"
    }
  ],
  "global_style": {
    "aesthetic": [
      "Nightlife aesthetic",
      "Pinterest style",
      "Glamorous but effortless"
    ],
    "technical": [
      "Shot on Fujifilm",
      "Flash photography",
      "Vintage film texture",
      "High contrast",
      "Deep shadows",
      "40mm grain"
    ],
    "era_vibe": "2000s party atmosphere"
  }
}
```

[[Party Atmosphere]]

---

### 152. 使用 Nano Banana Pro 生成守护天使

**Author**: [ちゃろん](https://x.com/charon_artist)  **Date**: 2026-01-23  **Language**: ja

> 一位用户使用 Nano Banana Pro 生成了一张被鲜花和光芒环绕的守护天使图片，并在 ALT 文本中分享了提示词，供其他人尝试。

![使用 Nano Banana Pro 生成守护天使](https://cms-assets.youmind.com/media/1769236037652_sb9oh0_G_WY67Ha8AA30nM.jpg)

```
👼🌸 AIで守護天使に変換してみた

あなたの心に安らぎを…✨
花と光に包まれた優しい時間💐
```

[[Fantasy Portrait]]

---

### 153. 奢华度假村泳池日生活方式照片

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 提示，用于生成一张高端奢华度假村生活方式照片，画面中两位女士在泳池边休憩。该提示详细说明了强烈的自然逆光营造出镜头光晕效果，深景深以捕捉背景中的别墅，并描述了拍摄对象的黑色连体泳衣、配饰（Wayfarer 墨镜、草帽）以及环境（波光粼粼的泳池、修剪整齐的树篱）。

![奢华度假村泳池日生活方式照片](https://cms-assets.youmind.com/media/1769235970989_oxba6e_G_WSMy1a0AA1oQB.jpg)

```
{  
"medium": "lifestyle photography",  
"style": {  
"aesthetic": "high-end luxury resort",  
"mood": "relaxed, affluent, sun-drenched, serene vacation vibe",  
"color\_palette": "warm whites, deep greens, pool blue, strong blacks, natural skin tones"  
},  
"camera\_settings": {  
"perspective": "slightly low angle, eye-level",  
"focal\_length": "35mm",  
"lighting": "intense natural backlight, overhead sun creating lens flare at top, high contrast shadows",  
"focus": "sharp focus on subjects, deep depth of field capturing background villa"  
},  
"subject\_foreground": {  
"demographics": "female, late 20s",  
"pose": "reclining on a chaise lounge, legs crossed at ankles, head resting back comfortably, right hand resting on thigh",  
"clothing": "black spaghetti-strap one-piece swimsuit",  
"hair": "shoulder-length, light brown with blonde highlights, loose waves",  
"accessories": "black wayfarer sunglasses, small earrings",  
"skin": "lightly tanned, sun-kissed"  
},  
"subject\_background": {  
"demographics": "female, 30s to 40s",  
"pose": "sitting semi-upright on a chaise lounge behind the first subject, knees bent upward, holding an open magazine",  
"clothing": "black one-piece swimsuit",  
"hair": "blonde, straight, shoulder-length",  
"accessories": "large black sunglasses"  
},  
"props\_and\_furniture": {  
"loungers": "two modern white cushioned chaise lounges with dark grey metal frames",  
"side\_table": "modern dark metal table in immediate foreground",  
"items": "glass of iced lemonade/cocktail on side table, woven straw hat with black band resting on the background lounger near legs"  
},  
"environment": {  
"setting": "luxury villa poolside terrace",  
"elements": [
"rectangular swimming pool with shimmering blue water",  
"manicured green hedge wall",  
"tall palm tree on the left",  
"modern white stone residential architecture on the right with glass balcony",  
"dense trees in distant background"  
],  
"sky": "bright, hazy from intense sunlight"  
},  
"constraints": {  
"must\_keep": [
"black matching swimwear",  
"sunglasses on both subjects",  
"sun flare/backlighting",  
"pool context",  
"relaxed posture"  
],  
"avoid": [
"clouds",  
"night time",  
"indoor setting",  
"bikinis",  
"crowds"  
],  
"negative\_prompt": "deformed, ugly, bad anatomy, extra limbs, missing limbs, floating objects, cartoon, illustration, painting, low resolution, blurry, grainy, oversaturated"  
}  
}
```

[[Poolside Setting]]

---

### 154. 粗犷单色音乐海报提示，带霓虹点缀

**Author**: [CaptchaPassed](https://x.com/captchapassed)  **Date**: 2026-01-23  **Language**: en

> 给 Nano Banana Pro 的提示：创作一张大胆的竖版音乐海报，画面中一位女歌手正在现场表演。图像应采用粗犷的单色处理，带细微颗粒感，但需在图像上叠加充满活力的霓虹绿色调，背景为纹理化的青绿色，并配有超大黄色字体拼写“ROCK STAR”。

![粗犷单色音乐海报提示，带霓虹点缀](https://cms-assets.youmind.com/media/1769235980326_xgs51u_G_U02kNbAAowYZR.jpg)

```
Create a bold, high-energy vertical music poster featuring a young female singer performing live on stage. She is captured mid-performance, holding a microphone close to her mouth, smiling with confidence and charisma. Her hair is styled in messy space buns with loose strands, and she wears an oversized black t-shirt layered with chunky chain necklaces, giving a rebellious, effortless stage presence. The portrait is treated in gritty monochrome with subtle grain and texture, while neon green accents are painted over parts of the image—especially flame-like graphic shapes rising from the bottom of her shirt—adding intensity and visual punch. The background is a flat, textured teal-green surface with visible noise and poster grain. Dominating the composition behind the subject is oversized, rounded, bold yellow typography spelling out "{argument name="text" default="ROCK STAR"}" in stacked lines. The letters are thick, playful, and slightly retro, filling most of the frame and partially obscured by the performer to create depth. Place her name behind the figure.
```

[[Bold Typography]]

---

### 155. 深色、高对比度海报设计提示，搭配琥珀色镜片

**Author**: [CaptchaPassed](https://x.com/captchapassed)  **Date**: 2026-01-23  **Language**: en

> 一个用于 Nano Banana Pro 的提示，旨在创作一张具有地下俱乐部美学的深色、高对比度海报。海报以一位戴着耳机和反光琥珀金色太阳镜的女性单色肖像为特色，置于深黑色背景之上，其头部后方有一个巨大的金黄色圆形聚光灯形状，力求营造出一种原始的、传单般的感觉。

![深色、高对比度海报设计提示，搭配琥珀色镜片](https://cms-assets.youmind.com/media/1769235979619_8s4r0d_G_Pxrfsa8AEC_Ql.jpg)

```
Create a dark, high-contrast poster with a moody, underground club aesthetic. The composition features a monochrome portrait of a young woman from the chest up, shot from a slightly low angle for attitude and power. She wears large over-ear headphones and reflective round sunglasses with warm amber-gold lenses that stand out vividly against the black-and-white portrait. One hand is raised near her head, the other near her chin, creating a dynamic, expressive pose associated with music immersion. Behind her head is a large flat golden-yellow circular shape, like a spotlight, creating a strong focal point and visual contrast. The background is deep black with subtle grunge textures, dust, scratches, and poster-wear imperfections, giving it a raw, printed-flyer feel. Use 4:5 aspect ratio.
```

[[Monochrome]]

---

### 156. 海滩上时尚前卫的纹身女子

**Author**: [Natty Windstorm](https://x.com/NattyWindstorm)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成时尚、逼真的编辑图片的提示，内容是一位纹身密布的女性，慵懒地躺在沙滩上，周围环绕着被阳光照耀的巨石。该提示详细说明了服装（花卉比基尼上衣、牛仔短裤、船员袜、黄色运动鞋）和配饰（薄荷绿棒球帽、串珠项链），强调强烈的自然阳光和锐利的阴影，以营造出现代夏日美学。

![海滩上时尚前卫的纹身女子](https://cms-assets.youmind.com/media/1769235971628_p9m5a0_G_WRHkTbAAEDXot.jpg)
![海滩上时尚前卫的纹身女子](https://cms-assets.youmind.com/media/1769235971849_6drche_G_WRL3JaMAAWG9M.jpg)

```
{
  "prompt": "Fashion-forward beach photo of a tattooed woman lounging on a sandy beach surrounded by large sunlit rocks. She is sitting on a white towel, wearing a colorful floral bikini top, light denim shorts, white crew socks, and bright yellow sneakers. She has a short blonde bob haircut and wears a mint-green baseball cap and a beaded necklace. Her body is covered with detailed black floral tattoos on arms, legs, and torso. A pink-and-white inflatable swim ring lies beside her, along with a small metallic blue handbag. The scene is shot from a slightly elevated angle in bright natural sunlight, with warm tones, sharp shadows, high detail, and a modern editorial summer aesthetic.",
  "style": "photorealistic, lifestyle editorial, high fashion beach photography",
  "lighting": "natural sunlight, midday, strong highlights and soft shadows",
  "camera": {
    "angle": "slightly elevated",
    "lens": "35mm",
    "depth_of_field": "moderate"
  },
  "quality": "ultra high resolution, sharp focus, detailed textures",
  "aspect_ratio": "1:1"
}
```

[[Denim Shorts]]

---

### 157. 身穿白色礼服的女性超写实肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超现实、电影感的肖像，描绘一位形象始终如一的金发女性（波琳娜·加加林娜），她身穿优雅的白色单肩晚礼服，礼服上饰有花卉图案，并开有高高的侧边开衩。场景设定在一个带有古老石墙的质朴室内空间，光线温暖柔和，旨在呈现超精细的细节水平。

![身穿白色礼服的女性超写实肖像](https://cms-assets.youmind.com/media/1769235961004_pr7wfh_G_WMW0BbQAAViOx.jpg)
![身穿白色礼服的女性超写实肖像](https://cms-assets.youmind.com/media/1769235961003_qeu7e2_G_WMWwwbUAAtlv5.jpg)

```
{
  "image_generation_request": {
    "subject": {
      "identity": "Consistent young blonde woman from reference image",
      "features": {
        "eyes": "green",
        "lips": "full, professional makeup",
        "hair": "long, flowing blonde, cascading over shoulder",
        "distinguishing_marks": "small tattoo on the shoulder",
        "body_type": "slender, elegant"
      }
    },
    "attire": {
      "dress_type": "one-shoulder evening gown",
      "color": "pure white",
      "details": [
        "intricate three-dimensional floral embellishments",
        "detailed beadwork",
        "high side slit on the left leg"
      ],
      "footwear": "none (barefoot)"
    },
    "setting": {
      "environment": "rustic indoor space with ancient stone wall",
      "props": ["ancient stone pillar"],
      "lighting": {
        "type": "warm ambient lighting",
        "sources": ["warm filament bulbs", "hanging Edison lamps"],
        "effects": ["subtle bokeh", "soft shadows"]
      }
    },
    "composition": {
      "pose": "standing elegantly, leaning back with left hand on pillar",
      "framing": "full-length hyper-realistic portrait",
      "style": "cinematic photography",
      "technical_specs": {
        "resolution": "8K",
        "depth_of_field": "shallow",
        "detail_level": "ultra-fine"
      }
    },
    "negative_prompt": "shoes, footwear, colored clothing, blurry, distorted anatomy, misshapen fingers, extra limbs, watermark, text, signature, low resolution, cartoon, painting"
  }
}
```

[[Warm Soft Light]]

---

### 158. Midjourney 变形金刚提示词

**Author**: [Michael Rabone](https://x.com/michaelrabone)  **Date**: 2026-01-23  **Language**: en

> 一个 Midjourney 提示，作为使用 Nano Banana Pro 将机器人图像转换为车辆的示例，尽管该提示本身是一个标准的 Midjourney 文本提示，用于 Transformers，并带有特定的宽高比和风格化设置。

![Midjourney 变形金刚提示词](https://cms-assets.youmind.com/media/1769235955225_80resa_G_WLURoXkAM1Ixd.jpg)

```
Transformers --ar 4:5 --sref 1383516477
--sw 100 --stylize 300 --v 6.1
```

[[Midjourney Prompt]]

---

### 159. 变形金刚机器人到坦克过渡提示

**Author**: [Michael Rabone](https://x.com/michaelrabone)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成 6 步过渡过程图像的提示，展示了一个变形金刚机器人变形为坦克的画面。它指定了 3x2 的布局，并要求保持相同的风格，没有轮廓。

![变形金刚机器人到坦克过渡提示](https://cms-assets.youmind.com/media/1769236008713_nnsqsw_G_WLHZhXAAA_Bdr.jpg)

```
Show the transitional process of this Transformer robot transforming into a tank in 6 (3 x 2) step-by-step process. Use same style without outlines
```

[[Transformer Robot To Tank Transition]]

---

### 160. 金色兰博基尼时尚摄影提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个结构化提示，用于生成一张超现实的电影级时尚照片，照片中一位模特始终如一的女性模特站在一辆闪亮的金色兰博基尼 Aventador 旁边，背景是都市环境，重点突出特定的服装、车辆细节和柔和的日光照明。

![金色兰博基尼时尚摄影提示](https://cms-assets.youmind.com/media/1769236021965_lbw8c5_G_WJ0JfaEAAaOLf.jpg)
![金色兰博基尼时尚摄影提示](https://cms-assets.youmind.com/media/1769236021981_lfgpyr_G_WJ0ElboAABqv-.jpg)

```
{
  "subject": {
    "identity": "Consistent female model",
    "features": {
      "eyes": "Green",
      "lips": "Full",
      "hair": "Long, sleek, blonde, falling over shoulders",
      "makeup": "Expert, cinematic"
    },
    "physique": {
      "build": "Athletic",
      "chest_size": "Large (as per reference image)",
      "pose": "Front-facing, standing with poise"
    },
    "attire": {
      "top": {
        "type": "Fitted black T-shirt",
        "detail": "Gold shimmering {argument name="logo text" default="Lamborghini"} logo lettering"
      },
      "bottom": "Black leggings",
      "footwear": "Slim-fitting white Skechers"
    }
  },
  "vehicle": {
    "make": "Lamborghini",
    "model": "Aventador",
    "color": "Pure gleaming gold",
    "finish": "Metallic weave",
    "details": ["Sharp bumper", "Grille", "Supple leather interior", "Textured fabric accents"]
  },
  "environment": {
    "setting": "Urban",
    "background_elements": [
      "Tall buildings",
      "High black wall",
      "Glass panel reflection"
    ],
    "lighting": {
      "type": "Soft daylight",
      "sky": "Overcast",
      "effect": "Subtle shadows with high depth"
    }
  },
  "technical_specs": {
    "angle": "Frontal shot",
    "style": "Hyper-realistic cinematic",
    "resolution": "8k",
    "focus": "Sharp",
    "keywords": [
      "masterpiece",
      "photorealistic",
      "luxury car photography",
      "fashion-forward",
      "dynamic composition"
    ]
  }
}
```

[[Urban Background]] [[Soft Daylight]]

---

### 161. 名人图像分析与场景生成提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个结构化的 JSON 提示，旨在根据特定的名人场景（安娜·德·阿玛斯和西德尼·斯威尼）分析和生成图像。该提示概述了四个不同的场景，详细描述了每个场景的动作、服装、道具和灯光，例如安娜·德·阿玛斯在健身房进行大重量弯举，或者西德尼·斯威尼在红毯上挥手致意。

![名人图像分析与场景生成提示](https://cms-assets.youmind.com/media/1769235963016_slxkgg_G_WJvMjbAAAeuIo.jpg)
![名人图像分析与场景生成提示](https://cms-assets.youmind.com/media/1769235963020_o9e5zr_G_WJvEdbADsh8yH.jpg)
![名人图像分析与场景生成提示](https://cms-assets.youmind.com/media/1769235963032_8t2yra_G_WJvO7bQAARGJ1.jpg)

```
{
  "celebrity_image_analysis": [
    {
      "subject": "{argument name="celebrity 1" default="Ana de Armas"}",
      "file_name": "1000582227.jpg",
      "setting": "Gym / Workout",
      "visual_details": {
        "action": "Performing a heavy bicep curl",
        "apparel": "Dusty pink athletic tank top",
        "props": "Dumbbell labeled '40 KG'",
        "physical_state": "Sweaty skin, intense facial strain, messy ponytail",
        "lighting": "Cool-toned fluorescent gym lighting"
      },
      "vibe": "Determination, Strength, Grit"
    },
    {
      "subject": "{argument name="celebrity 2" default="Sydney Sweeney"}",
      "file_name": "1000582328.jpg",
      "setting": "Red Carpet Premiere",
      "visual_details": {
        "action": "Waving to the crowd with a smile",
        "apparel": "Black and white color-block evening gown",
        "background": "Paparazzi, crowd, and 'SYDNEY SWEENEY' digital sign",
        "hair_makeup": "Old Hollywood blonde waves, winged eyeliner"
      },
      "vibe": "Glamorous, Celebrity, Cheerful"
    },
    {
      "subject": "Ana de Armas",
      "file_name": "1000582340.png",
      "setting": "Forest / Outdoors",
      "visual_details": {
        "action": "Chopping wood with an axe",
        "apparel": "Plaid flannel shirt, blue jeans, leather work gloves",
        "props": "Axe, wooden logs",
        "atmosphere": "Rustic, autumnal forest background"
      },
      "vibe": "Rugged, Hardworking, Action-oriented"
    },
    {
      "subject": "Sydney Sweeney",
      "file_name": "1000582330.jpg",
      "setting": "Cafe / Casual Indoor",
      "visual_details": {
        "action": "Posing for a portrait",
        "apparel": "Black ribbed long-sleeve sweater",
        "expression": "Subtle, polite smile",
        "background": "Blurred cafe interior with warm lighting"
      },
      "vibe": "Casual, Soft, Approachable"
    }
  ]
}
```

[[Celebrity Scene Analysis And Generation]]

---

### 162. 波霸奶茶罐的影棚产品照片提示

**Author**: [maniBuildsAI](https://x.com/manibuildsAI)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 提示，旨在生成 BOBAco 波霸奶茶罐的优质商业影棚产品照片。该提示指定了简洁、极简的美学风格，采用柔和的粉色背景、柔和的漫射照明和浅景深，重点突出超现实的细节，如冷凝水和作为装饰的新鲜覆盆子。

```
{
  "scene": {
    "type": "studio product photo",
    "background": {
      "color": "{argument name="background color" default="pastel pink"}",
      "surface": "smooth"
    },
    "lighting": {
      "key": "soft diffused",
      "rim": "subtle"
    },
    "camera": {
      "lens": "85mm",
      "depth_of_field": "shallow"
    }
  },
  "subject": {
    "type": "beverage can",
    "brand": "{argument name="brand name" default="BOBAco Popping Bubble Tea"}",
    "color": "white",
    "position": "centered",
    "details": {
      "condensation": true,
      "focus": "label"
    },
    "garnish": {
      "main": {
        "type": "raspberry",
        "position": "on can rim"
      },
      "foreground": {
        "type": "raspberries",
        "quantity": "multiple",
        "ripeness": "ripe"
      }
    }
  },
  "style": {
    "aesthetic": "clean minimal",
    "photography": "premium commercial beverage",
    "post_processing": "high-end retouching",
    "text": false,
    "watermark": false
  }
}
```

[[Condensation Detail]] [[Soft Diffused Lighting]] [[Pink Background]]

---

### 163. NFL 橄榄球女球迷体育场快照提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真的“网红美学”快照：一位年轻女性身处 NFL 橄榄球场（SoFi 体育场），重点突出服装细节，如露脐背心、低腰牛仔裤、可见的品牌内裤腰带，以及一个紫色证件徽章。

![NFL 橄榄球女球迷体育场快照提示](https://cms-assets.youmind.com/media/1769236028991_kglebx_G_WJYkTbUAAm2Bl.jpg)
![NFL 橄榄球女球迷体育场快照提示](https://cms-assets.youmind.com/media/1769236029141_006j2c_G_WJYaXbIAAiKSs.jpg)
![NFL 橄榄球女球迷体育场快照提示](https://cms-assets.youmind.com/media/1769236029289_qoeka9_G_WJYmHaUAA-uU_.jpg)

```
{
  "prompt_structure": {
    "subject_details": {
      "demographics": "Young Woman , light skin tone",
      "hair": "Long, straight, dark brown hair, center part, silky texture",
      "face": "Natural makeup, defined eyebrows, slight pout/duck face expression, looking off-camera to the left",
      "body": "Fit physique, exposed midriff"
    },
    "apparel_and_styling": {
      "top": "White ribbed square-neck tank top, cropped fit, tight silhouette",
      "bottoms": "Low-rise blue denim jeans, vintage wash",
      "layering": "Visible white underwear waistband with black '{argument name="underwear brand" default="Miu Miu"}' logo peeking above jeans",
      "accessories": [
        "Small black shoulder bag tucked under arm",
        "Gold chain necklace with small clover/flower pendant",
        "Gold link bracelet on left wrist",
        "Silver wristwatch on right wrist",
        "Silver belly button piercing",
        "Purple 'Postgame Field' credential badge hanging from waist"
      ]
    },
    "pose_and_action": {
      "posture": "Standing upright, casual stance",
      "hands": "Hands partially obscured, likely thumbs hooked in pockets or resting at hips",
      "gaze": "Looking away from the camera, nonchalant attitude"
    },
    "environment_and_background": {
      "location": "SoFi Stadium interior, NFL football field",
      "ground": "Artificial green turf with distinct white yard lines and hash marks",
      "background_elements": [
        "Empty stadium seating (blue seats)",
        "Blurred LED ribbon boards and stadium signage",
        "Yellow goal post in distance",
        "Black crowd control stanchion with blue belt in foreground left"
      ],
      "context": "Post-game field access"
    },
    "lighting_and_atmosphere": {
      "type": "Artificial stadium floodlights",
      "quality": "Bright, even, diffuse lighting, minimal harsh shadows",
      "tone": "Slightly cool, crisp coloring typical of sports arenas"
    },
    "camera_and_technical": {
      "shot_type": "Medium shot (thigh-up framing)",
      "lens": "85mm portrait lens",
      "aperture": "f/2.8 for slight separation of subject from background (bokeh)",
      "resolution": "8K, Ultra High Definition",
      "style": "Raw photography, influencer aesthetic, candid snapshot"
    },
    "quality_tags": [
      "Ultra photorealistic",
      "Hyper-detailed",
      "Cinematic lighting",
      "Sharp focus on subject",
      "Realistic skin texture",
      "Fabric texture details"
    ]
  }
}
```

[[Influencer Aesthetic]] [[Low-Rise Jeans]] [[Crop Top]]

---

### 164. 可爱的卧室泰迪熊肖像提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个 JSON 提示，用于生成一张年轻女性躺在床上、直视观看者（从床尾拍摄的 POV 视角）的超逼真肖像。主体穿着可爱俏皮的服装（灰色贝雷帽、粉色蕾丝边上衣、格子迷你裙），手里拿着一个粉色泰迪熊。场景是一个卧室，有柔和的自然窗户光线，强调清晰的焦点和高细节。

![可爱的卧室泰迪熊肖像提示](https://cms-assets.youmind.com/media/1769236002896_atkbtp_G_WJTDEbAAAq6Ur.jpg)
![可爱的卧室泰迪熊肖像提示](https://cms-assets.youmind.com/media/1769236002829_cpcg70_G_WJTW8XkAAsQ8i.jpg)
![可爱的卧室泰迪熊肖像提示](https://cms-assets.youmind.com/media/1769236002917_hugap1_G_WJTaeagAAD0U9.jpg)

```
{
  "image_generation_request": {
    "subject": {
      "description": "Young woman with long straight platinum blonde hair and blue eyes",
      "pose": "Lying on back on a bed, looking directly at the viewer, legs extended towards the camera (foreshortened), index finger playfully touching cheek, holding a pink teddy bear in left arm",
      "expression": "Soft, cute smile, relaxed"
    },
    "attire": {
      "headwear": "Grey wool beret",
      "top": "{argument name="top color" default="Pink"} long-sleeve ribbed top with lace trim neckline",
      "bottom": "Black and white plaid pleated mini skirt"
    },
    "environment": {
      "setting": "Bedroom",
      "details": "Wooden headboard, beige and cream colored pillows, rumpled beige bed sheets",
      "lighting": "Soft natural window light, diffuse shadows"
    },
    "technical_specs": {
      "style": "Photorealistic, DSLR, high quality",
      "aspect_ratio": "4:5",
      "camera_angle": "Eye-level, shot from the foot of the bed looking up"
    },
    "full_prompt_string": "Photorealistic portrait of a beautiful young woman lying back on a bed, wearing a grey beret and a pink long-sleeve top with lace trim, black and white plaid pleated skirt, holding a pink teddy bear, touching cheek with finger, looking at viewer, long blonde hair, wooden headboard, beige bedding, soft natural lighting, sharp focus, 8k, highly detailed, POV shot from foot of bed.",
    "negative_prompt": "drawing, anime, cartoon, 3d render, bad anatomy, deformed hands, missing fingers, extra limbs, blurry, low quality, watermark, text, noise, distorted face, ugly"
  }
}
```

[[Soft Window Light]] [[Plaid Mini Skirt]]

---

### 165. SoFi 体育场里的 NFL 狂热女球迷美学

**Author**: [Iris](https://x.com/xIrissy)  **Date**: 2026-01-23  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张年轻女性的超逼真图像，她具有“网红美学”，在比赛结束后，于 SoFi 体育场场地上扮演 NFL 粉丝女孩。该提示详细说明了服装（低腰牛仔裤、露脐背心、可见的“{argument name="underwear logo" default="Miu Miu"}”标志腰带）、配饰（证件徽章、肚脐环）和环境（人造草坪、体育场泛光灯、空置的蓝色座位）。

![SoFi 体育场里的 NFL 狂热女球迷美学](https://cms-assets.youmind.com/media/1769235969425_kv2mbk_G_WIc38WIAAqk2a.jpg)
![SoFi 体育场里的 NFL 狂热女球迷美学](https://cms-assets.youmind.com/media/1769235969438_kfq83s_G_WIc3ebAAQfPXz.jpg)
![SoFi 体育场里的 NFL 狂热女球迷美学](https://cms-assets.youmind.com/media/1769235969471_hz55gj_G_WIc3YbAAI2HQi.jpg)

```
{
  "prompt_structure": {
    "subject_details": {
      "demographics": "Young Woman , light skin tone",
      "hair": "Long, straight, dark brown hair, center part, silky texture",
      "face": "Natural makeup, defined eyebrows, slight pout/duck face expression, looking off-camera to the left",
      "body": "Fit physique, exposed midriff"
    },
    "apparel_and_styling": {
      "top": "White ribbed square-neck tank top, cropped fit, tight silhouette",
      "bottoms": "Low-rise blue denim jeans, vintage wash",
      "layering": "Visible white underwear waistband with black '{argument name="underwear logo" default="Miu Miu"}' logo peeking above jeans",
      "accessories": [
        "Small black shoulder bag tucked under arm",
        "Gold chain necklace with small clover/flower pendant",
        "Gold link bracelet on left wrist",
        "Silver wristwatch on right wrist",
        "Silver belly button piercing",
        "Purple 'Postgame Field' credential badge hanging from waist"
      ]
    },
    "pose_and_action": {
      "posture": "Standing upright, casual stance",
      "hands": "Hands partially obscured, likely thumbs hooked in pockets or resting at hips",
      "gaze": "Looking away from the camera, nonchalant attitude"
    },
    "environment_and_background": {
      "location": "SoFi Stadium interior, NFL football field",
      "ground": "Artificial green turf with distinct white yard lines and hash marks",
      "background_elements": [
        "Empty stadium seating (blue seats)",
        "Blurred LED ribbon boards and stadium signage",
        "Yellow goal post in distance",
        "Black crowd control stanchion with blue belt in foreground left"
      ],
      "context": "Post-game field access"
    },
    "lighting_and_atmosphere": {
      "type": "Artificial stadium floodlights",
      "quality": "Bright, even, diffuse lighting, minimal harsh shadows",
      "tone": "Slightly cool, crisp coloring typical of sports arenas"
    },
    "camera_and_technical": {
      "shot_type": "Medium shot (thigh-up framing)",
      "lens": "85mm portrait lens",
      "aperture": "f/2.8 for slight separation of subject from background (bokeh)",
      "resolution": "8K, Ultra High Definition",
      "style": "Raw photography, influencer aesthetic, candid snapshot"
    },
    "quality_tags": [
      "Ultra photorealistic",
      "Hyper-detailed",
      "Cinematic lighting",
      "Sharp focus on subject",
      "Realistic skin texture",
      "Fabric texture details"
    ]
  }
}
```

[[Low-Rise Jeans]] [[Crop Top]]

---

### 166. Wizardry x Genba Neko 联动图片

**Author**: [pt2012](https://x.com/pt20121)  **Date**: 2026-01-23  **Language**: ja

> 一位用户使用 Nano Banana 生成了一张“魔法 x 现场猫”（工地猫）的合作图片，特别要求一个“猫人角色”。生成的图片显示该角色正在比“OK”手势，这需要五根手指和爪垫，突出了 AI 输出的一个特定特征。

![Wizardry x Genba Neko 联动图片](https://cms-assets.youmind.com/media/1769236037149_gv12ts_G_WHtmfWgAAK70H.jpg)

```
Wizardry x 現場猫 のコラボをリスペクトし急遽予定の投稿内容と差し替え！

「猫人間のようなキャラ」としたせいで、三コマ目で五本指＋肉球といういかにもAI出力になってますが、猫の手だとオッケーサインできないのでこれでヨシ！
```

[[Fantasy Character]]

---

### 167. 波霸奶茶罐的影棚产品照片提示词 (副本)

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 提示，旨在生成 BOBAco 波霸奶茶罐的优质商业影棚产品照片。该提示指定了干净、简约的美学风格，采用柔和的粉色背景、柔和的漫射照明和浅景深，重点突出超现实的细节，如凝结的水珠和新鲜覆盆子作为装饰。

![波霸奶茶罐的影棚产品照片提示词 (副本)](https://cms-assets.youmind.com/media/1769236008629_0cmhs1_G_WHO2MaAAAIvDX.jpg)

```
{
  "scene": {
    "type": "studio product photo",
    "background": {
      "color": "{argument name="background color" default="pastel pink"}",
      "surface": "smooth"
    },
    "lighting": {
      "key": "soft diffused",
      "rim": "subtle"
    },
    "camera": {
      "lens": "85mm",
      "depth_of_field": "shallow"
    }
  },
  "subject": {
    "type": "beverage can",
    "brand": "{argument name="brand name" default="BOBAco Popping Bubble Tea"}",
    "color": "white",
    "position": "centered",
    "details": {
      "condensation": true,
      "focus": "label"
    },
    "garnish": {
      "main": {
        "type": "raspberry",
        "position": "on can rim"
      },
      "foreground": {
        "type": "raspberries",
        "quantity": "multiple",
        "ripeness": "ripe"
      }
    }
  },
  "style": {
    "aesthetic": "clean minimal",
    "photography": "premium commercial beverage",
    "post_processing": "high-end retouching",
    "text": false,
    "watermark": false
  }
}
```

[[Condensation Detail]] [[Soft Diffused Lighting]] [[Pink Background]]

---

### 168. 带纹身的热带比基尼时尚大片提示

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-01-23  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张超逼真的年轻女性中景照片，她身穿粉色条纹比基尼，置身于热带度假村环境中。重点是详细的外观、特定的纹身以及黄金时段的电影级光线。

![带纹身的热带比基尼时尚大片提示](https://cms-assets.youmind.com/media/1769236019936_9jcd6c_G_V1US3WoAA_QTk.jpg)
![带纹身的热带比基尼时尚大片提示](https://cms-assets.youmind.com/media/1769236019873_frjdux_G_V1UGfXoAAqn6b.jpg)
![带纹身的热带比基尼时尚大片提示](https://cms-assets.youmind.com/media/1769236020107_owmebo_G_V1UMbW4AAs4Xc.jpg)

```
{
  "prompt_description": "A highly detailed, ultra-photorealistic image of a young woman standing in a sunny outdoor resort setting.",
  "subject": {
    "appearance": {
      "gender": "Female",
      "age_group": "Young adult",
      "skin_tone": "Fair with warm undertones",
      "hair": {
        "color": "Dark brown",
        "style": "Shoulder-length, wavy, windswept bob",
        "texture": "Silky and voluminous"
      },
      "body_type": "Curvy, hourglass figure",
      "facial_features": {
        "expression": "Subtle smile, looking off-camera to the right",
        "makeup": "Natural look, rosy cheeks, soft pink lip tint"
      },
      "tattoos": [
        {
          "design": "Small colored star",
          "placement": "Left hip/lower abdomen"
        },
        {
          "design": "Small black outline (snake around a red rose)",
          "placement": "Inner left forearm"
        }
      ]
    },
    "clothing": {
      "top": {
        "type": "Bikini top",
        "color": "{argument name="bikini top color" default="Pink"}",
        "style": "Triangle cup, halter neck tie"
      },
      "bottom": {
        "type": "Bikini bottom",
        "pattern": "Purple and black horizontal stripes",
        "style": "Side-tie strings with bows on hips"
      },
      "accessories": [
        {
          "item": "White wristband",
          "placement": "Left wrist"
        }
      ]
    },
    "pose": {
      "stance": "Standing facing forward",
      "head_turn": "Turned to the right profile",
      "hands": {
        "right_hand": "Lightly touching right collarbone/shoulder area",
        "left_hand": "Relaxed by side"
      }
    }
  },
  "environment": {
    "setting": "Tropical resort garden or beachside area in Seychelles",
    "elements": [
      "Large grey textured rock formations in background",
      "Lush green foliage, bushes, and yucca plants",
      "Tall palm tree trunks visible",
      "Clear blue sky",
      "Hint of white resort architecture/balcony railing in upper left"
    ]
  },
  "lighting": {
    "source": "Natural sunlight (Golden Hour or Mid-afternoon)",
    "quality": "Bright, direct, and warm",
    "shadows": "Soft natural shadows under chin and on rocks, highlighting skin texture"
  },
  "camera_details": {
    "shot_type": "Medium shot (thighs up)",
    "angle": "Eye-level",
    "focal_length": "50mm or 85mm portrait lens",
    "aperture": "f/2.8 to f/4",
    "focus": "Sharp focus on subject, slight depth of field blurring the background foliage"
  },
  "quality_tags": [
    "Ultra Photorealistic",
    "8k resolution",
    "High fidelity",
    "Detailed skin texture",
    "Cinematic lighting",
    "Masterpiece",
    "RAW photo"
  ]
}
```

[[Tattoo Detail]]

---

### 169. 包豪斯几何极简插画模板

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-23  **Language**: en

> 一个简单有效的提示模板，用于生成包豪斯风格的插画，重点突出严谨的几何图形、原色、平衡的比例和功能性设计。用户需要指定要描绘的主题。

![包豪斯几何极简插画模板](https://cms-assets.youmind.com/media/1769235959392_hye7gk_G_V0EdxaUAACK44.jpg)
![包豪斯几何极简插画模板](https://cms-assets.youmind.com/media/1769235959363_ioi4jz_G_V0Ec7b0AEyd-j.jpg)
![包豪斯几何极简插画模板](https://cms-assets.youmind.com/media/1769235960283_0g10lm_G_V0EdwasAA0DFQ.jpg)
![包豪斯几何极简插画模板](https://cms-assets.youmind.com/media/1769235960808_5c11f5_G_V0EhSbAAIoBzZ.jpg)

```
Depict {argument name="subject" default="[SUBJECT]"} using Bauhaus-inspired minimalism: strict geometry, primary or near-primary colors, balanced proportions, and functional design. The composition should feel timeless, rational, and visually bold while remaining simple and clean.
```

[[Template Prompt]]

---

### 170. 旗舰品牌形象模型 (Nano Banana Pro)

**Author**: [Lovart 公式 (ラブアート)](https://x.com/lovart_jp)  **Date**: 2026-01-23  **Language**: ja

> 为 Nano Banana Pro 提供一个高度结构化、详细的提示，以生成一个旗舰品牌生态系统（Lovart）的全面平面模型，包括包装、餐饮必需品、员工制服和商品，采用特定的日式圣诞/极简主义视觉主题。

![旗舰品牌形象模型 (Nano Banana Pro)](https://cms-assets.youmind.com/media/1769236034649_tx34lj_G_VgYm5bEAAKtxW.jpg)
![旗舰品牌形象模型 (Nano Banana Pro)](https://cms-assets.youmind.com/media/1769236034854_whekav_G_Vnq6bbAAgL_Ru.jpg)

```
“task_description”:
「フルカテゴリ対応のフラッグシップ級ブランドアイデンティティ・モックアップを生成する」
“prompt_structure”: {
“subject”:
「大規模で超精緻なブランドエコシステムのフラットレイ」
“brand_info”: {
“{argument name="ブランド名" default="Lovart"}”,
“visual_theme”: “{argument name="ビジュアルテーマ" default="日本のクリスマス、ミニマリズム、ウォームトーン"}”
},
“item_categories”: {
“packaging”: "ショッピングバッグ（S/M/L）, ケーキボックス, コーヒー豆パウチ, サンドイッチウェッジボックス, ペストリーボックス",
“dining_essentials”: "スリーブ付きコーヒーカップ, 紙ナプキン, シュガーパケット, トレイライナー用ペーパー, メニューボード",
“staff_uniform”: "折りたたまれたグリーンエプロン, 刺繍入りベースボールキャップ, スタッフ用ネームタグ",
“merchandise”: "キャンバストートバッグ, セラミックマグ, ブランドノート, ボールペン"
},
“visual_style”: {
“art_style”: “リアルな質感マッピングを備えたクリーンなベクターモックアップ”,
“color_palette”: "フォレストグリーン（メイン）, マットホワイト（サブ）, クラフトペーパーブラウン（テクスチャ）, ベージュ（アクセント）",
“logo_style”: “ミニマルなラインアートの鹿ロゴ”
},
“composition”: {“type”: “密度の高いノーリング配置”,
“background”: “ソリッドなダークチャコール（#1A1A1A）”,
“perspective”: “90度のトップダウン（オルソ視点）”}
“negative_prompt”:「散らかっている、雑然としている、重なり、3Dパースの歪み、過度な写実的反射、光沢プラスチック、ネオンカラー、人の手、ウォーターマーク、低解像度」
“generation_params”: {
“aspect_ratio”: “3:4”,
“detail_level”: “高”,
“texture_quality”: “プレミアム”}
```

[[Graphic Design]] [[Flat Design]] [[Packaging Design]]

---

### 171. 视觉故事板创建提示

**Author**: [Tushar Pandey](https://x.com/TUSHARPAND0848)  **Date**: 2026-01-23  **Language**: en

> 这是一个号召用户获取提示的行动号召，该提示旨在利用 Nano Banana Pro 为产品演示创建品牌视觉故事板，通常应要求提供。

![视觉故事板创建提示](https://cms-assets.youmind.com/media/1769236041775_9t1xug_G_Vo48obAAEqLl7.jpg)
![视觉故事板创建提示](https://cms-assets.youmind.com/media/1769236041776_p5rv2q_G-3QbGvX0AEEEEI.jpg)

```
Create a brand visual storyboard for presenting your product with Nano Banana Pro:
```

[[Visual Design]]

---

### 172. 专业人物肖像与图形品牌提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成超逼真、专业人物肖像的提示模板，适用于个人品牌推广，将照片写实主义与平面设计元素相结合。它描述了一张全身工作室肖像，人物靠在浅灰色墙壁上，穿着白色商务衬衫，旁边墙上展示着一个突出的黑白极简主义矢量人脸肖像和他们的专业头衔。

![专业人物肖像与图形品牌提示](https://cms-assets.youmind.com/media/1769236010599_576a4d_G_VkbbLbAAELFIS.jpg)

```
Ultra-realistic 8K full body portrait of \[PERSON’S FULL NAME\], wearing a clean and pressed white social shirt with folded collar and a small lapel microphone, dark navy-blue dress pants and polished brown social shoes. Casually and unpretentiously leaning against a smooth light gray studio wall; hands are in pockets and one leg is crossed over the other, with relaxed and confident body language. Add to the wall next to them a prominent vector portrait in black and white of their face and bust - with sharp lines and angles, overlapping polygonal shapes and a minimalist modern graphic style, right below the information: “\[PERSON’S FULL NAME\]”, and below the name: “\[{argument name="profession" default="PROFESSION"}\]”. 1080x1080 dimensions.
```

[[Studio Photography]]

---

### 173. 纳米香蕉 + Google Flow + Lovable Prompt

**Author**: [Viktor Oddy](https://x.com/viktoroddy)  **Date**: 2026-01-23  **Language**: en

> 这条推文提到了一个在 Nano Banana、Google Flow 和 Lovable 组合中使用的确切提示，这暗示了一个复杂的工作流程或集成，但文本中并未提供提示内容本身。

```
Here’s the exact prompt I used ↓
```

[[AI Image Generation]]

---

### 174. 幻灯片关键视觉图生成（Nano Banana Pro）

**Author**: [KAWAI](https://x.com/kawai_design)  **Date**: 2026-01-23  **Language**: ja

> 一个在 Google 幻灯片（通过 Nano Banana Pro 聊天支持功能）中使用的提示，用于根据输入文本的含义生成丰富的关键视觉效果，旨在用作幻灯片或缩略图图像。

![幻灯片关键视觉图生成（Nano Banana Pro）](https://cms-assets.youmind.com/media/1769236036213_unxf0v_G_VaNS6a8AAt-jJ.jpg)
![幻灯片关键视觉图生成（Nano Banana Pro）](https://cms-assets.youmind.com/media/1769236036411_qxegwl_G_Va8qqbcAAqFaF.jpg)
![幻灯片关键视觉图生成（Nano Banana Pro）](https://cms-assets.youmind.com/media/1769236036722_cosfjv_G_VaNUTa8AAxmPN.jpg)

```
テキストの意味に合わせて、キービジュアルを生成して
```

[[Thumbnail Design]] [[Presentation Design]]

---

### 175. 疯狂动物城情侣镜子自拍提示词

**Author**: [TheAIHeadquarters](https://x.com/DavisonDabiri)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超现实、超精细的迪士尼商店情侣镜面自拍，他们戴着奢华的超大《疯狂动物城》角色帽子（尼克·狐狸和朱迪·兔），强调韩式美妆、特定配饰和清晰的焦点。

![疯狂动物城情侣镜子自拍提示词](https://cms-assets.youmind.com/media/1769236022299_6jacmu_G_VYQVsWQAAYCwy.jpg)
![疯狂动物城情侣镜子自拍提示词](https://cms-assets.youmind.com/media/1769236022373_nq6d8j_G_VYQYNXwAEnamR.jpg)
![疯狂动物城情侣镜子自拍提示词](https://cms-assets.youmind.com/media/1769236022292_hv4xih_G_VYQZCX0AAiKrR.jpg)
![疯狂动物城情侣镜子自拍提示词](https://cms-assets.youmind.com/media/1769236023410_40ijj4_G_VYQbbXMAA1vEJ.jpg)

```
{
  "prompt": {
    "scene": {
      "type": "ultra-realistic mirror selfie",
      "device": "iPhone 15 Pro Max",
      "resolution": "8K",
      "style": "photorealistic, hyper-detailed",
      "aesthetic": "Zootropolis fandom",
      "composition": "couple selfie reflected in an oval mirror"
    },
    "subjects": {
      "left_subject": {
        "type": "young man",
        "identity": "use facial features from Photo 1",
        "expression": "playful, mischievous (match reference expression)",
        "pose": "standing on the left side of the mirror",
        "clothing_hair": "same outfit and hairstyle as Photo 1",
        "accessories": {
          "hat": {
            "character": "Nick Wilde (Zootropolis)",
            "color": "orange",
            "details": "luxury oversized Disney character hat with large fox ears and embroidered sly eyes"
          }
        }
      },
      "right_subject": {
        "type": "young woman",
        "identity": "use facial features from Photo 2",
        "expression": "playful wink",
        "pose": "standing on the right side of the mirror, holding a bright yellow phone",
        "nails": "metallic nail polish",
        "hair": {
          "style": "long, straight hair"
        },
        "clothing": {
          "top": "{argument name="woman's top color" default="hot pink"} halter top"
        },
        "accessories": {
          "hat": {
            "character": "Judy Hopps (Zootropolis)",
            "color": "gray",
            "details": "luxury oversized Disney character hat with long pink bunny ears and big purple eyes"
          },
          "necklace": "short pearl necklace fitted around the neck",
          "rings": "multiple rings on fingers"
        },
        "makeup": {
          "style": "Korean K-beauty",
          "skin": "glass skin",
          "blush": "soft natural blush",
          "eyeliner": "black eyeliner",
          "contact_lenses": "colored lenses (blue or gray)",
          "lips": "pink ombre lipstick with reddish tones"
        }
      }
    },
    "environment": {
      "location": "Disney toy / souvenir store interior",
      "background": {
        "details": "blurred shelves filled with Disney toys",
        "lighting": "holiday mall lighting",
        "ceiling": "decorative hanging lights"
      }
    },
    "lighting": {
      "type": "soft commercial mall lighting",
      "effect": "even illumination, vibrant colors, no harsh shadows"
    },
    "quality": {
      "detail_level": "extremely high",
      "textures": "luxury realistic textures, visible individual fur fibers on hats",
      "color": "bright saturated colors",
      "noise": "none",
      "focus": "perfect sharp focus on faces and hats"
    },
    "framing": {
      "shot_type": "mirror selfie",
      "mirror": "oval mirror",
      "focus_priority": "faces and character hats centered in frame"
    }
  }
}
```

[[Couple Portrait]] [[Cosplay Photography]]

---

### 176. AI 感知可视化 (Nano Banana Pro)

**Author**: [ベルベット（velvet404）](https://x.com/velvet404mv)  **Date**: 2026-01-23  **Language**: ja

> 一个提示，用于要求 Nano Banana Pro 将其对用户指令风格随时间的感知可视化，生成图像或图表。

![AI 感知可视化 (Nano Banana Pro)](https://cms-assets.youmind.com/media/1769236034469_y371dm_G_U5mezbsAA1060.jpg)

```
今までの私の指示の出し方であなたが感じた事を、画像または図解にしてください。
```

[[Data Visualization]] [[Abstract Art]]

---

### 177. 超宽屏构造裂谷和世界末日场景提示（JSON 格式）

**Author**: [Johnny Wang](https://x.com/JohnnyWang8802)  **Date**: 2026-01-23  **Language**: en

> 一个复杂的 JSON 提示，用于 Nano Banana Pro 生成一个宏伟的、超宽屏（21:9）场景：一个大陆尺度的构造裂谷，海洋倾泻入无底的大气虚空。该提示详细描述了非欧几里得地理、大气效果和相机规格（14mm 超广角镜头、大画幅传感器），以实现原始的真实感和巨大的尺度。

![超宽屏构造裂谷和世界末日场景提示（JSON 格式）](https://cms-assets.youmind.com/media/1769235982535_5saprx_G_Uz1xBbAAEqjsP.jpg)

```
{
  "intent": "A monumental, vertiginous composition of a continental-scale tectonic rift where a massive, deep-sea ocean current terminates at a perfect geometric precipice, cascading into a bottomless atmospheric void filled with tiered cloud layers and lightning.",
  "frame": {
    "aspect_ratio": "21:9 ultra-widescreen",
    "composition": "The frame utilizes a vanishing point perspective that follows the literal edge of the world into infinity. The top-left quadrant is dominated by the dark, churning Atlantic-scale ocean, while the right and bottom sections reveal the terrifying scale of the vertical drop into a hazy, multi-layered cloud abyss.",
    "style_mode": "Raw_photorealism with hyper-accurate fluid dynamics and atmospheric Rayleigh scattering to establish immense scale."
  },
  "subject": {
    "identity": "The ruins of an ancient, megalithic limestone bridge, four kilometers in width, which once spanned the gap but now ends abruptly in a jagged, fractured edge at the precipice.",
    "wardrobe": "A tiny, barely visible research vessel is positioned near the edge of the falling water, providing a critical sense of gargantuan scale through size comparison.",
    "placement": "The ruined structure is anchored into the basalt bedrock of the 'continental shelf' that forms the world's end."
  },
  "environment": {
    "location": "The 'Great Sheer'—a non-Euclidean geographic terminus where the planet's crust simply ceases, revealing a vertical cross-section of geological strata before descending into the troposphere.",
    "atmosphere": "Extreme atmospheric depth, with visible 'cloud falls' where moisture from the ocean drop condenses into secondary weather systems thousands of meters below the primary sea level.",
    "weather": "Violent updrafts from the abyss creating spray-vortices at the edge, while the distant depths of the rift are illuminated by internal, cloud-to-cloud lightning."
  },
  "camera": {
    "sensor_format": "Large format digital (Phase One IQ4 150MP), optimized for maximum per-pixel detail and wide dynamic range in the deep shadows of the chasm.",
    "lens": "14mm ultra-wide-angle rectilinear lens to exaggerate the perspective distortion and the sheer scale of the verticality.",
    "camera_position": "A cantilevered perspective, positioned several hundred meters out into the void, looking back toward the edge of the world and the falling ocean.",
    "aperture_depth_of_field": "f/11 to ensure the texture of the falling water in the foreground and the distant geological strata are captured with clinical sharpness."
  },
  "lighting": {
    "type": "Harsh, high-altitude sun positioned at a 45-degree angle, creating deep, well-defined shadows within the craters and crevices of the vertical cliff face.",
    "color_temperature": "5400K (neutral daylight), with a significant shift toward 12000K (deep sky blue) in the shadowed depths of the abyss due to atmosph
```

[[Science Fiction]]

---

### 178. 零重力产品视频提示（草莓苏打）

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成超现实零重力产品视频的提示，视频中展示了一罐草莓苏打水。场景设定在一个柔和的红粉色工作室空间中，罐子、草莓、冰块和液体都缓慢漂浮，为产品镜头营造出一种失重、外太空的美感。

![零重力产品视频提示（草莓苏打）](https://cms-assets.youmind.com/media/1769235995156_76im06_G_U0e55a4AAMRZK.jpg)

```
A surreal zero-gravity product video featuring a strawberry soda can floating in a soft red-pink studio space.

SCENE 1 — SPACE FLOATING INTRO:
The soda can is suspended mid-air, slightly tilted, with no visible gravity. Surrounding it are strawberries, ice cubes, and flowing red liquid, all drifting slowly as if in outer space. No object is falling — everything floats gently in different directions.
```

[[Studio Photography]] [[Floating Objects]] [[Beverage Advertising]]

---

### 179. 电影感 90 年代胶片静帧肖像提示词

**Author**: [Stark](https://x.com/katmanai)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 格式提示，用于生成一张电影般的 90 年代风格剧照：一位忧郁的年轻女子，湿发造型，双手托腮，画面具有复古美学、暖色调，并带有特定的电影字幕。该提示详细说明了长宽比、灯光和相机类型等技术细节，并明确要求提供图像参考以获取具体细节。

![电影感 90 年代胶片静帧肖像提示词](https://cms-assets.youmind.com/media/1769236041715_6o0dpg_G_UZwbLXoAA-qAm.jpg)

```
Cinematic 90s film still of a stunning young woman with messy wet-look dark hair strands falling over her face, intense and melancholic gaze directly at the camera, chin resting on her palms with hands framing her face, natural sun-kissed skin with visible film grain, vintage aesthetic with a warm nostalgic color grade, soft bokeh of ocean waves in the background, bright daylight, yellow cinematic subtitles at the bottom center reading '{argument name="subtitle text" default="You never let me tell you the truth"}', photorealistic, 35mm film photography style, authentic analog texture --ar 3:2 --stylize 200 --v 6 --q 2
```

[[Vintage Film Aesthetic]] [[Retro Photography]] [[Warm Tones]]

---

### 180. 搭讪语问题识别文本分析提示

**Author**: [shaun](https://x.com/rebelcrayon)  **Date**: 2026-01-23  **Language**: en

> 这是一个针对 Nano Banana Pro（可能是一个大型语言模型）的文本提示，指示它分析一个搭讪语，找出它“偏离轨道”的点，并在脚注中解释问题。

![搭讪语问题识别文本分析提示](https://cms-assets.youmind.com/media/1769235976921_fit60t_G_TtMhXXAAAGE_P.jpg)

```
circle the part where the pick-up line goes off the rails and explain the issue in a footnote
```

[[Text Analysis Prompt]]

---

### 181. 海龟脱口秀图片提示

**Author**: [Kanyamaさま](https://x.com/KarmanasaK)  **Date**: 2026-01-22  **Language**: ja

> 一个详细的提示，指示 Nano Banana 生成一张让人联想到迪士尼“与 Crush 对话海龟”景点的图片，画面中一只海龟举起双鳍，说道：“你们是最棒的！”

![海龟脱口秀图片提示](https://cms-assets.youmind.com/media/1769149377984_er8wom_G_TdU3kbAAALuZ2.jpg)

```
ディズニーランドのタートル・トークを彷彿とさせる、ウミガメが両ひれをあげて「{argument name="セリフ" default="お前達最高だぜー"}」と言っている画像
```

[[Character Illustration]] [[Whimsical Art]]

---

### 182. 建筑概念渲染：从草图到照片级真实感

**Author**: [FutureToolsAI](https://x.com/FutureToolsAI)  **Date**: 2026-01-22  **Language**: en

> 一个高度详细的提示，用于生成现代咖啡馆店面的建筑概念渲染图。核心概念是将简洁的技术草图美学（铅笔线条、阴影线、注释）与高端照片级真实感相结合。它详细说明了构图（对称立面、黑色边框窗户）、内部细节（暖光照明、植物、柜台）和外部元素（路灯、三明治板），强调了单色草图线条与选择性色彩点缀之间的对比。

![建筑概念渲染：从草图到照片级真实感](https://cms-assets.youmind.com/media/1769149398050_z57bix_G_TVR_IX0AAxOw1.jpg)

```
"Architectural concept rendering of a modern café storefront, ultra-detailed, blending clean technical sketch and high-end photorealism. The composition features a perfectly symmetrical black-framed glass window and door set into a pristine white minimalist façade with subtle texture. Through the central window, a warmly lit, inviting café interior is visible, with soft pendant lights, lush green plants, a compact wooden counter, a few stools, and hints of people blurred in the background for a lived-in feel. Surrounding the window, delicate pencil sketch lines, dimension marks, hatching, construction grids, and small handwritten architectural annotations overlay the wall and ground plane, seamlessly merging drafting aesthetics with finished reality. Add realistic exterior details such as a small black metal lamp centered above the arch or lintel, a neatly designed sandwich board sign on the sidewalk with faint chalk writing, and two tasteful potted plants flanking the entrance in simple modern planters. Emphasize a balanced contrast between crisp monochrome sketch outlines and selective, refined color accents — warm yellow ambient lighting inside, a single bold yellow poster in the window, natural green foliage, and soft, directional shadows on the pavement. The overall mood is elegant, creative, and conceptual, evoking a high-end architectural visualization that appears to transition gradually from blueprint lines at the edges into fully realized photographic realism at the center."
```

[[Architectural Visualization]] [[Technical Drawing]]

---

### 183. Flash Patch 写实肖像提示词 (JSON)

**Author**: [Duru💝](https://x.com/Durusss13)  **Date**: 2026-01-22  **Language**: en

> 一个高度具体的 JSON 提示，用于生成具有“闪光灯补丁写实主义”美学的肖像，描绘一位女性在深夜、非法奢华的环境中斜倚在兰博基尼旁，详细描述了服装、姿势和刺眼的闪光灯照明效果。

![Flash Patch 写实肖像提示词 (JSON)](https://cms-assets.youmind.com/media/1769149391875_5gfykq_G_TPtOeW8AAZaVo.jpg)

```
"style": "sleek, straight, wet-look finish",
      "details": "tucked behind ears, falling over shoulders, highly reflective under flash"
    },

    "face": {
      "structure": "defined cheekbones, strong jawline",
      "expression": "unimpressed, slight arrogant squint looking down at camera",
      "eyes": "dark brown, intense gaze, slight red-eye reflection from flash",
      "mouth": "pouty, glossy nude lips",
      "makeup": "sharp contour, heavy highlights that pop under flash, defined brows"
    }
  },

  "pose": {
    "overall": "leaning casually back against the door of a dark grey Lamborghini",

    "lower_body": {
      "legs": "crossed at ankles",
      "stance": "weight resting on the car body"
    },

    "torso": {
      "angle": "turned slightly towards the camera",
      "posture": "relaxed but confident shoulders"
    },

    "arms": {
      "one_arm": "resting on the car roof",
      "other_arm": "hand near waist hook, holding a smartphone with a bright case"
    },

    "head": {
      "tilt": "chin tilted slightly up",
      "gaze": "looking directly down the lens"
    }
  },

  "outfit": {
    "clothing": {
      "top": {
        "type": "structured corset-style crop top",
        "color": "black satin",
        "fit": "tight, push-up",
        "details": "reflective fabric under flash, defined cups"
      },
      "layer": {
        "type": "oversized vintage racing leather jacket",
        "color": "black with white and red patches",
        "style": "slung open, falling off shoulders"
      },
      "bottom": {
        "type": "low-rise baggy parachute cargo pants",
        "color": "dark charcoal",
        "fit": "loose leg, sitting low on hips",
        "details": "drawstrings hanging, slight shimmer fabric"
      },
      "shoes": {
        "type": "chunky designer sneakers",
        "details": "reflective detailing catching the light"
      }
    },
    "accessories": {
      "items": ["thick silver chain necklace", "large hoop earrings"],
      "details": "metal jewellery glaring under the flash"
    }
  },

  "camera_perspective": {
    "pov": "friend taking a quick snapshot",
    "angle": "slightly low angle pointing up",
    "distance": "medium shot (knees up)",
    "framing": "subject centered, car details and concrete filling frame",
    "composition": "raw, unposed feel, slight motion blur on edges"
  },

  "vibe": {
    "mood": "illicit luxury, arrogant, late night",
    "energy": "unbothered cool, expensive secrecy",
    "aesthetic": "flash patch realism, underground rich kids"
  },

  "rules": [
    "must look shot on iPhone with harsh flash",
    "emphasize sweaty/oily skin sheen",
    "no explicit nudity",
    "maintain raw, grainy texture",
    "realistic shadows cast by flash"
  ]
}
```

[[Luxury Car]] [[Harsh Flash Lighting]]

---

### 184. Notion 风格的肖像提示

**Author**: [AmirMušić](https://x.com/AmirMushich)  **Date**: 2026-01-22  **Language**: en

> 一个用于生成 Notion 风格肖像的提示，表明了专业或个人资料照片的特定美学，尽管提示文本本身并未完全显示。

![Notion 风格的肖像提示](https://cms-assets.youmind.com/media/1769149391716_y0s3if_G_SnZVIWkAAoaF9.jpg)

```
Notion-styled portraits in seconds
```

[[Professional Portrait]]

---

### 185. 使用 Nano Banana Pro 生成分形玻璃渐变图像

**Author**: [RicoUI](https://x.com/ricouii)  **Date**: 2026-01-22  **Language**: zh

> 一位用户描述了他们使用 Nano Banana Pro 生成带有分形玻璃等距网格纹理的渐变图像的体验。他们指出，该模型对“分形玻璃”的理解有时会发生变化，从而导致意想不到的结果，但总的来说，Nano Banana Pro 的输出质量优于其他图像生成模型。

![使用 Nano Banana Pro 生成分形玻璃渐变图像](https://cms-assets.youmind.com/media/1769149379234_9s4vmn_G_R1XP_asAAQv_A.jpg)

```
Fractal glass 等距栅格质感的渐变图
```

[[Abstract Art]] [[Generative Art]]

---

### 186. 沉浸式过渡提示，实现绘画转换

**Author**: [Freepik](https://x.com/freepik)  **Date**: 2026-01-22  **Language**: en

> 以下是为使用 Google Nano Banana Pro 沉浸式过渡设置设计的两个提示，重点是将一幅画作转换为逼真的模拟风格输出，第一个提示将其置于花卉墙壁的背景中，第二个提示则强调有机纹理和反射。

![沉浸式过渡提示，实现绘画转换](https://cms-assets.youmind.com/media/1769149388495_zl28lu_G_Rw_KdacAAO3mW.jpg)
![沉浸式过渡提示，实现绘画转换](https://cms-assets.youmind.com/media/1769149388593_vecx03_G_Rw_tcaAAEDR54.jpg)

```
Display the painting framed, hanging on a flower-patterned wall. Analog photography output.

Create a photorealistic version of this painting with natural and organic textures and reflections. Output in an analog-style format.
```

[[Photorealism]] [[Image Transformation]]

---

### 187. 黑白镜面自拍，突出臀部线条

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2026-01-22  **Language**: en

> 一个详细的提示，用于生成一张黑白镜面自拍，画面中是一位身材极具运动感的沙漏型年轻女性，重点突出她臀部的线条和尺寸，她穿着一件透明的露脐上衣和极短的运动短裤。场景中包含特定的卧室元素和灯光细节。

![黑白镜面自拍，突出臀部线条](https://cms-assets.youmind.com/media/1769149388120_ncv1ec_G_Q1iyvakAAsh4F.jpg)

```
{
  "subject": {
    "type": "Young woman",
    "pose": "Standing, taking a mirror selfie with left hand holding phone, making a peace sign with right hand, head tilted, looking at the phone. Her body is turned to emphasize her glutes.",
    "body": {
      "build": "Athletic hourglass figure with pronounced gluteal development and a slender waist.",
      "details": "Her lower body is the focal point, showing a highly toned and very prominent gluteal shape and size, creating a striking waist-to-hip ratio. The muscles and curves of her hips and glutes are clearly defined and accentuated by the short shorts. Her legs are shapely and smooth.",
      "hair": "Long, split-dyed hair, black on the left and blonde on the right, with bangs."
    },
    "wardrobe": {
      "top": "White, slightly sheer, long-sleeved crop top with loose sleeves.",
      "bottoms": "Extremely short black athletic shorts with white trim and white drawstrings, pulled up high on her waist and cut high on the thighs to fully expose the gluteal fold.",
      "socks": "White over-the-knee high socks.",
      "accessories": "A pink smartphone with a case featuring a white cat character."
    }
  },
  "scene": {
    "type": "Bedroom interior reflection in a large mirror.",
    "background_elements": [
      "Grey painted wall.",
      "Large yellow plush toy on the floor.",
      "White nightstand with a remote, a water bottle, and a glowing pink LED lamp.",
      "Carpeted floor.",
      "Power outlet with cords plugged in."
    ],
    "lighting": {
      "type": "Soft, warm interior light from a bedside lamp and general room lighting, creating highlights on her hair and clothing.",
      "quality": "Warm and inviting."
    }
  },
  "camera": {
    "type": "Smartphone camera.",
    "perspective": "Mirror reflection.",
    "shot_type": "Full body mirror selfie.",
    "focus": "Sharp focus on the subject, with a slightly softer background."
  },
  "aspect_ratio": "9:16"
}
```

[[Bedroom Setting]] [[Monochrome Photography]] [[Crop Top]] [[Athletic Figure]]

---

### 188. 2000 年代 OVA 风格高中女生怪物狩猎

**Author**: [とうや](https://x.com/towya_aillust)  **Date**: 2026-01-22  **Language**: ja

> 一个为 Nano Banana Pro 设计的详细多部分提示，用于生成一个 2000 年代日本动漫 OVA 风格的四格序列。场景描绘了两名高中女生在夜晚的废弃城市中对抗无定形液态怪物，重点突出紧张感和构图。

![2000 年代 OVA 风格高中女生怪物狩猎](https://cms-assets.youmind.com/media/1769149373225_3kz1o1_G_QvmxsagAAPUrS.jpg)

```
出力画像は2x2の4分割
映像スタイル: {argument name="映像スタイル" default="2000年代の日本のアニメOVA画風"}
背景:
深夜のビル街。無人の道路と高層ビルの隙間。巨大なモンスターから飛び散った黒い液体が、アスファルトや壁に付着している。粉塵や火花が舞っている。

キャラクター1：
黒髪ロングの女子高生。セーラー服姿。日本刀は鞘に収めたまま腰に下げている。警戒した様子で周囲を見渡し、重心を低く構えている。
キャラクター2：
金髪ボブの女子高生。ブレザー制服姿。仲間の背後に立ち、片手を構えていつでも能力を使える状態。表情は緊張している。
敵の存在：
黒い液体が集まり、繊維や糸のような質感を持つ人型へと変形した存在。顔は曖昧で、手足が異様に長く、不自然な動きで地面や壁を這っている。

カット1:
地面のクローズアップ。黒い液体で満たされている。舞い散る粉塵と火花
カット2:
ミディアムショット。黒い液体から立ち上がった人型の異形が、ぎこちなく体を起こす瞬間。糸のような影が垂れ、地面を引きずっている。
カット3:
ローアングルのワイドショット。複数の異形が道路や壁から次々と現れ、円を描くように少女たちを取り囲んでいる。ビル街が包囲感を強調する構図。
カット4:
少女たちの背中越しショット。正面には迫り来る黒い人型の群れ。黒髪の少女は鞘に手を添え、金髪の少女は能力発動の構えに入っている。
戦闘直前の緊張が張り詰めた構図。
```

[[Urban Fantasy]]

---

### 189. 视频游戏维基风格图像生成

**Author**: [PSN用アカウント](https://x.com/PSN62595111)  **Date**: 2026-01-22  **Language**: en

> 一个用于测试 Google Gemini 图像生成能力的提示，具体要求以视频游戏维基网站页面的独特风格，渲染一只树懒、一条金枪鱼和一架 F-15J 战斗机的组合。

![视频游戏维基风格图像生成](https://cms-assets.youmind.com/media/1769149370717_qz2tpi_G_Pe43abcAAkEI6.jpg)
![视频游戏维基风格图像生成](https://cms-assets.youmind.com/media/1769149370646_rvz9it_G_Pe3ydbEAAqCA5.jpg)
![视频游戏维基风格图像生成](https://cms-assets.youmind.com/media/1769149370795_cqzrkw_G_Pe527asAA1Cmo.jpg)

```
a sloth, a tuna, an F-15J in the style of a video game wiki website's page
```

[[Digital Illustration]]

---

### 190. 白骑士与黑象提示

**Author**: [Vlad Sydor](https://x.com/vlad_sydor)  **Date**: 2026-01-22  **Language**: en

> 一个简单、简短的提示，用于根据“白骑士与黑象”这一对比概念生成图像。

```
White Knight and Black Elephant
```

[[Fantasy Art]]

---

### 191. Lovart 品牌的多步设计生成提示

**Author**: [KAWAI](https://x.com/kawai_design)  **Date**: 2026-01-22  **Language**: ja

> 一个全面、多步骤的工作流程，使用设计代理“Lovart”（可能与 Nano Banana Pro 集成）来生成完整的品牌形象，从标志开始，延伸到设计指南、UI、网站、展位和商品。这展示了一种结构化的设计生成方法。

![Lovart 品牌的多步设计生成提示](https://cms-assets.youmind.com/media/1769149373823_avjhxj_G_QiCWtawAAkGgW.jpg)

```
鮮やかな{argument name="色1" default="エメラルドグリーン"}と鮮やかな{argument name="色2" default="ブルー"}のグラデーションがベースカラーの「{argument name="企業名" default="Lovart"}」という企業のロゴマーク

このロゴマークからカラーパレットとフォントのデザインガイドラインを生成

このサービスのアプリケーションUIデザインを生成して。PC版とスマートフォン版

このサービスを紹介するWebサイトのデザイン。PC版とスマートフォン版

このサービスの展示会用ブースのデザインイメージ

このサービスのグッズデザイン。Tシャツ、パーカー、キャップ、ノート、ステッカー
```

[[Logo Design]] [[UI Design]] [[Brand Identity]]

---

### 192. 超逼真女牛仔肖像提示词

**Author**: [Busra](https://x.com/promptLab0)  **Date**: 2026-01-22  **Language**: en

> 一个详细的提示，用于生成一张超逼真的 8K 肖像，描绘一个浅金色头发、戴着牛仔帽的小女孩，背景是快餐咖啡馆环境，有棕榈树，捕捉她开心地眨眼的姿势。

![超逼真女牛仔肖像提示词](https://cms-assets.youmind.com/media/1769149391000_y4nvla_G_QgRqtWAAE_TUl.jpg)

```
Girl: {argument name="Age" default="19 years old"}
Hair: Very light blonde
Skin: Fair
Skin: Natural and radiant
Makeup: Light freckles, dark peach gloss, natural-looking face makeup
Top: White crop top, red collar and sleeve seams, horseshoe symbol on the front of the top
Hat: Denim cowboy hat
Bottom: Dark blue jeans, skinny jeans, low-waisted
Setting: Lunchtime, fast-food style cafes in the background, sidewalk, palm trees, jeep-style cars
Girl's Pose: Blinking with one eye, cheerful aura, left hand in the back pocket of her jeans, bottom of the frame ending in the pockets of her jeans.

Photo: 8k ultra-realistic, 3:4 aspect ratio
```

[[Winking Expression]] [[Cowboy Hat]]

---

### 193. 梦幻汽车内饰肖像提示

**Author**: [TheAIHeadquarters](https://x.com/DavisonDabiri)  **Date**: 2026-01-22  **Language**: en

> 一个详细的 Nano Banana Pro 提示，用于生成一张逼真、梦幻、优雅的年轻女性车内特写肖像，强调特定的韩式发型、妆容细节（水润唇妆、粉色腮红），以及侧面强烈的自然阳光。

![梦幻汽车内饰肖像提示](https://cms-assets.youmind.com/media/1769149384248_rhm1jd_G_QgJUJW4AAiW0b.jpg)
![梦幻汽车内饰肖像提示](https://cms-assets.youmind.com/media/1769149384219_m4a9f9_G_QgJTqWkAAabG2.jpg)
![梦幻汽车内饰肖像提示](https://cms-assets.youmind.com/media/1769149384214_gnxgrz_G_QgJP9W4AAcL7h.jpg)
![梦幻汽车内饰肖像提示](https://cms-assets.youmind.com/media/1769149384986_v3mgme_G_QgJXBWwAIumXF.jpg)

```
{
  "prompt": {
    "subject": {
      "type": "young woman",
      "age": "early 20s",
      "pose": {
        "location": "inside a car",
        "attitude": "confident",
        "gesture": "hand raised to cover mouth with shy smile",
        "expression": "dreamy, gentle, elegant",
        "gaze": "looking at camera"
      },
      "hair": {
        "color": "dark brown",
        "length": "waist-length",
        "style": "side-parted left, loose waves at ends, small front strands, Korean style",
        "motion": "hair flowing slightly across face"
      },
      "face_makeup": {
        "eyebrows": "natural light color, neat",
        "eyelashes": "false lashes, clustered",
        "cheeks": "soft nude pink blush on cheeks and nose",
        "lips": "nude-red, glossy and hydrated"
      },
      "eyes": {
        "accessory": "black cat-eye sunglasses, worn on head"
      },
      "clothing": {
        "top": "thin spaghetti strap tank top, blue with blue-trimmed edges",
        "accessories": [
          "short silver necklace with small blue leaf pendant",
          "small silver earrings shaped like blue leaf"
        ]
      }
    },
    "environment": {
      "car_interior": "dark, brown seats in background",
      "outside_view": "bright blue sky visible through right window"
    },
    "lighting": {
      "type": "natural sunlight from left",
      "effect": "strong highlights on hair and skin, ultra-bright, natural"
    },
    "camera": {
      "angle": "eye-level, close-up",
      "focus": "face, expression, and hair detail"
    },
    "style": {
      "realism": "photorealistic",
      "quality": "Ultra HD, high detail, sharp textures, vibrant colors",
      "mood": "dreamy, gentle, elegant"
    }
  }
}
```

[[Close-Up Portrait]] [[Glossy Lips]]

---

### 194. 小哥斯拉滑雪

**Author**: [PC+](https://x.com/saya0kurishina)  **Date**: 2026-01-22  **Language**: ja

> 一个给 Nano Banana Pro 的提示，用于生成两只 Q 版哥斯拉角色——Q 版哥吉四郎和 Q 版哥吉三郎——玩冬季奥运会单板滑雪的图片。

![小哥斯拉滑雪](https://cms-assets.youmind.com/media/1769149371854_zwtnj5_G_QcMOAXIAAOhwA.jpg)
![小哥斯拉滑雪](https://cms-assets.youmind.com/media/1769149371960_bh5cal_G_QcMODX0AAqqKm.jpg)
![小哥斯拉滑雪](https://cms-assets.youmind.com/media/1769149371907_njbxi0_G_QcMIdXAAAelmI.jpg)

```
冬季オリンピックのスノーボードをプレイしている{argument name="キャラクター1" default="ちびゴジよんごう"}と{argument name="キャラクター2" default="ちびゴジさんごう"}
```

[[Chibi Character]]

---

### 195. 多工具工作流提示，用于制作花样滑冰动画视频

**Author**: [なお](https://x.com/Naonekozamurai)  **Date**: 2026-01-22  **Language**: ja

> 一个复杂的四步工作流程，涉及多个 AI 工具（Niji Journey V7、Seedream 4.5、Nano Banana Pro、Grok Imagine），用于创建花样滑冰运动员的动画视频。提示涵盖了背景生成、角色生成、图像合成/替换以及最终视频动画指令。

```
日本の高品質アニメ、かわいい女の子、屋外の氷上リンクでスケートをしている、正面アングル、カウボーイショット、晴天、他には人はいない、光の反射、神秘的かつ幻想的でアーティスティックな演出、色彩豊かで高コントラスト、ファンタジー映画のような映像美、超高精細、光や色のエフェクトが美しい

ハイクオリティなリアリスティック実写映像、微笑んでいる日本人女性、街中を歩いている、色彩豊かで高コントラスト、超高精細

画像2のキャラクターを削除。代わりに画像1の実写の女性を画像2に配置。背景は画像2を使用。

被写体は実写風を維持、被写体をアニメ風にしない
氷上で優雅に演技するフィギュアスケーター、
ジャンプは一切せず、滑らかな滑走と流れるようなフットワークのみ、
長いストロークで氷の上を静かに滑る、
バレエのように美しい姿勢と柔らかな腕の動き、
一つ一つの動きが途切れずにつながる演技、
イラスト調、アニメ風のタッチ、
淡いパステルカラー、
柔らかな光に包まれたリンク、
氷がほのかにきらめく、
落ち着いた、上品で感情的な雰囲気、
スローカメラ、なめらかなトラッキングショット、
高品質、滑らかなアニメーション
```

[[Sports Photography]]

---

### 196. Promo Effect v2.0 个人资料截图构图提示

**Author**: [BeautyVerse](https://x.com/BeautyVerse_Lab)  **Date**: 2026-01-22  **Language**: en

> 这是 Nano Banana Pro 的“Promo Effect v2.0”功能的技术提示结构，旨在将角色图像合成到用户的个人资料截图中。该提示强制执行特定规则，例如确保“关注”按钮文本存在、保持背景结构，并定义角色的姿势（坐着，指向账户名和“关注”按钮）。此提示高度专注于 UI 操纵和图像合成。

![Promo Effect v2.0 个人资料截图构图提示](https://cms-assets.youmind.com/media/1769149375646_t0hcun_G_QABb-XgAAft2D.jpg)

```
{
  "edit_type": "precise_composite_overlay_dual_interaction_english_ui",

  "source": {
    "_hint": "Base Logic: Character sitting on Background. Background is fixed EXCEPT for the specific text on the button.",
    "mode": "IMAGE_COMPOSITION",
    "reference_images": {
      "foreground": "character_ref_image",
      "background_canvas": "profile_page_screenshot"
    },
    "consistency": {
      "character_fidelity": "high",
      "background_structure": "rigid_layout_preservation"
    }
  },

  "ui_text_enforcement": {
    "_hint": "CRITICAL: Ensure the button text reads 'Follow' in English, regardless of the text in the original screenshot.",
    "target_element": "action_button_top_right",
    "mandatory_text": "Follow",
    "language": "English",
    "font_style": "sans_serif_bold_legible",
    "correction_policy": "overwrite_original_text_if_not_follow"
  },

  "background_preservation": {
    "_hint": "Background is a rigid floor. Only allow changes to shadows and the button text.",
    "policy": "strict_pixel_retention_mostly",
    "allowed_modifications": [
      "realistic_contact_shadows_under_character",
      "replacement_of_button_text_to_Follow"
    ]
  },

  "camera_and_lighting": {
    "_hint": "Character sitting ON the interface.",
    "perspective": "high_angle_looking_down",
    "grounding_effect": {
      "technique": "contact_shadows_under_legs",
      "placement": "on_background_surface"
    }
  },

  "pose": {
    "_hint": "Dual pointing: Left Hand -> Name, Right Hand -> 'Follow' Button.",
    "pose_style": "sitting_cross-legged_or_kneeling",
    "head_position": "tilted_back_looking_at_camera",
    "hands_configuration": {
      "s
```

[[Image Compositing]] [[Social Media Design]]

---

### 197. 街头抓拍夜景照片提示

**Author**: [babydoll](https://x.com/bananababydoll)  **Date**: 2026-01-22  **Language**: en

> 一个为 Nano Banana Pro 设计的详细、结构化的提示，旨在生成一张在出租车候客区拍摄的逼真、坦率、深夜街头照片。该提示侧重于实现一种情绪化、略带瑕疵的“真实 iPhone 照片”美学，其中包含关于拍摄对象的外观、姿势、光线和明确的负面约束的具体细节，以确保真实性并避免 AI 伪影。

![街头抓拍夜景照片提示](https://cms-assets.youmind.com/media/1769149382025_fiec9o_G_NllinXMAA2hpr.jpg)
![街头抓拍夜景照片提示](https://cms-assets.youmind.com/media/1769149382095_rhvjm5_G_NllihWQAAyvkx.jpg)

```
{
  "meta": {
    "aspect_ratio": "9:16",
    "camera": "iPhone 15 Pro Max",
    "look": "real iPhone photo, candid, slightly imperfect framing"
  },
  "scene": {
    "location": "late-night taxi stand on a wet street (city center)",
    "weather": "light rain, wet asphalt reflections",
    "background": "soft bokeh streetlights, a couple of women blurred far behind, no men",
    "vibe": "messy confidence, a little toxic, don’t-approach energy"
  },
  "lighting": {
    "type": "streetlights + storefront spill + subtle phone flash",
    "feel": "moody but realistic, not cinematic, not studio"
  },
  "camera_perspective": {
    "shot_by": "a female friend",
    "distance": "about 1 meter",
    "angle": "slightly low",
    "framing": "mid-thigh to head, a bit off-center like a real snap",
    "imperfections": "tiny motion blur in background, slight noise in shadows, minor exposure mismatch"
  },
  "subject": {
    "female": true,
    "age": "24 (clearly adult)",
    "ethnicity": "random (non-specific)",
    "beauty_level": "instagram model but real",
    "hair": "dark blonde, loose waves, a bit damp from rain",
    "expression": "side-eye + small smirk, chin slightly up",
    "makeup": "minimal glam, glossy lips, not overdone",
    "pose": "one hip forward, shoulders relaxed, holding phone down by side (screen not visible)",
    "outfit": {
      "top": "thin ribbed long-sleeve top, opaque, braless (no straps, no visible bra lines)",
      "bottom": "low-rise black jeans, realistic folds",
      "shoes": "simple ankle boots"
    }
  },
  "realism": {
    "skin": "natural texture, tiny pores, faint under-eye texture, one small blemish ok",
    "details": "a few flyaway hairs, slight lint on jeans, mild rain specks on sleeves"
  },
  "negative_prompt": [
    "men",
    "nudity",
    "explicit anatomy",
    "pornographic pose",
    "overly perfect plastic skin",
    "super sharp HDR look",
    "text, watermark, logos",
    "extra fingers, deformed hands, face warping"
  ]
}
```

[[iPhone Aesthetic]]

---

### 198. AI 关系可视化提示

**Author**: [nayucchi（グラボあちち勢）](https://x.com/nayu_pkpk)  **Date**: 2026-01-22  **Language**: ja

> 一个与 AI nanobanana Pro 配合使用的提示，用于生成一张象征用户与 AI 之间关系的图片，重点突出共同创造、探索和伙伴关系的主题，随后是 AI 对所生成图片的详细解读。

![AI 关系可视化提示](https://cms-assets.youmind.com/media/1769149373861_iaocz1_G_PfQywbIAAaROG.jpg)

```
これまで私があなたをどう扱ってきたのかを画像にしてください。
```

[[Abstract Art]]

---

### 199. 搞笑视频提示：脾气暴躁的香蕉

**Author**: [EpicFrames App](https://x.com/EpicFrames_app)  **Date**: 2026-01-22  **Language**: en

> 一个简单有趣的视频生成提示，指示 AI 创建一个脾气暴躁的香蕉（水果）吐着舌头，然后从画面右侧走出去的静态镜头。

```
"A grumpy banana (fruit) shows tongue and then walks away from the frame to the right. Static shot."
```

[[Short Video]]

---

### 200. 3x3 发型创意网格生成提示

**Author**: [路飞 🏴‍☠️ AI 研究员🧐](https://x.com/0xluffy_eth)  **Date**: 2026-01-22  **Language**: zh

> 一个简单而有效的 Nano Banana Pro 提示，旨在生成一个 3x3 的图像网格，每张图像展示一种不同的发型变体。这对于快速比较发型、发质和整体气质非常有用，可用于作品集、社交媒体封面或个人资料图片。

![3x3 发型创意网格生成提示](https://cms-assets.youmind.com/media/1769149369553_tuq612_G_O4Cb6XMAA3rHb.jpg)

```
生成一个 {argument name="网格尺寸" default="3×3"} 发型创意网格
```

[[Beauty Photography]] [[Photo Grid]]

---

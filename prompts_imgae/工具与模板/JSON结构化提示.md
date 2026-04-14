---
category: 工具与模板
subcategory: JSON结构化提示
count: 77
---

# JSON结构化提示

所属大类：[[_工具与模板]]

相关分类：[[批量模板]]

共 77 个提示词

### 1. 以 Kinkade 风格生成 Carmen 图像的提示词

**作者**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619/status/2040589087732842873)  **日期**: 2026-04-05  **语言**: ja

> 这是一个为 Nano Banana Pro (Gemini 3 Pro Image) 设计的简单图像生成提示词，将 Bizet 的歌剧《Carmen》与 Thomas Kinkade 的风格相结合（在日语 AI 圈中，人们常错误地用“ラッセン风”来指代 Kinkade 风格，但实际上它指的是一种明亮、浪漫的现实主义风格）。

![以 Kinkade 风格生成 Carmen 图像的提示词](https://cms-assets.youmind.com/media/1775458537470_f8g0d9_HFGg9OibYAAk6a3.jpg)

```
{argument name="主題" default="ビゼー"}
{argument name="テーマ" default="カルメン"}
{argument name="スタイル" default="ラッセン風"}
```
---

### 2. Nano Banana Pro 图像生成提示词示例

**作者**: [Subhan Qureshi](https://x.com/LearnWithSubhan/status/2039946070713880815)  **日期**: 2026-04-03  **语言**: en

> 这是一条介绍 Nano Banana Pro 图像模型发布及其功能的推文，重点展示了其清晰的画质和一致性。文中包含了用于生成展示图像的简单输入文本。

```
• {argument name="subject" default="a young girl with curly hair"}
• {argument name="setting" default="a restaurant interior"}
```
---

### 3. 80 年代复古健美风的 Margot Robbie 替身

**作者**: [LexiPrompt](https://x.com/Artist04048661/status/2039536333329240331)  **日期**: 2026-04-02  **语言**: en

> 一份为 Nano Banana Pro 准备的详细 JSON 提示词，用于生成一张超逼真的图像：身着 1980 年代复古健美服（紧身连衣裤、氨纶短裤、金色腰带）的 Margot Robbie 替身，在明亮的阳光下摆拍，呈现黄金时刻的质感，强调鲜艳的色彩和高技术画质。

![80 年代复古健美风的 Margot Robbie 替身](https://cms-assets.youmind.com/media/1775198520110_8f37cv_HE3jWSDWgAAbk6y.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Woman with a strong resemblance to {argument name="subject name" default="Margot Robbie"}.",
      "hair": "Voluminous messy updo bun, loose strands framing face, held back.",
      "face": "Dramatic retro makeup, sharp eyeliner, matte skin finish.",
      "body": "Athletic build, tanned smooth skin."
    },
    "attire": {
      "clothing": "High-cut geometric patterned leotard over pale yellow spandex shorts, wide gold belt.",
      "style": "1980s retro aerobics fashion."
    },
    "styling_and_accessories": {
      "jewelry": [
        "Gold hoop earrings",
        "Pink terrycloth headband",
        "Pink wristbands",
        "Clear blue tumbler with pink straw"
      ]
    },
    "environment": {
      "setting": "Sunny outdoor paved pathway.",
      "background": "Heavily blurred palm trees and hazy bright sky.",
      "water": "None."
    },
    "pose": {
      "posture": "Standing facing away, twisting upper body to look back over shoulder.",
      "arms": "One hand holding cup to lips, other hand resting on lower back.",
      "angle": "Medium shot, eye-level."
    },
    "lighting_and_mood": {
      "lighting": "Bright natural sunlight, warm golden hour glow, soft shadows.",
      "mood": "Vibrant, energetic, nostalgic.",
      "colors": "Neon pink, pale yellow, bright cyan, gold."
    },
    "camera_and_technical": {
      "style": "Ultra Photorealistic, RAW photo.",
      "lens": "85mm",
      "aperture": "f/1.8",
      "quality_tags": [
        "8k resolution",
        "highly detailed",
        "volumetric lighting",
        "ray tracing reflections",
        "hyper-realistic texture",
        "Hasselblad photography"
      ]
    }
  }
}
```
---

### 4. 自然复古照片美学 提示词 用于 Nano Banana Pro

**作者**: [glena Jenner](https://x.com/GlenaJenne/status/2037208007629824451)  **日期**: 2026-03-26  **语言**: en

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
---

### 5. iPhone 夜间拍摄的豪华泳池边的两名女孩

**作者**: [babydoll](https://x.com/bananababydoll/status/2036528728235290804)  **日期**: 2026-03-24  **语言**: en

> 一份为 Nano Banana Pro 设计的详细 JSON 提示词，旨在生成一张模仿原始 iPhone 夜间照片的超逼真图像。场景描绘了两名穿着极简比基尼的女孩，在夜间的豪华别墅泳池边，被温暖的水下灯光照亮。提示词详细说明了姿势、表情（一个强势，一个调皮），并侧重于逼真的细节，例如湿润皮肤上的光泽反射和轻微的夜间噪点，旨在营造一种亲密而高端的氛围。

![iPhone 夜间拍摄的豪华泳池边的两名女孩](https://cms-assets.youmind.com/media/1774421482060_njycal_HDnRBKHW4AATudy.jpg)
![iPhone 夜间拍摄的豪华泳池边的两名女孩](https://cms-assets.youmind.com/media/1774421482061_rsukzf_HDnRBPtbEAQolyh.jpg)

```
{
  "meta": {
    "camera": "iPhone 17 Pro Max",
    "lens": "24mm wide",
    "aspect_ratio": "4:5",
    "quality": "ultra photorealistic",
    "style": "raw iPhone night pool realism, natural HDR, slight handheld imperfection"
  },
  "scene": {
    "location": "luxury villa pool at night",
    "time": "10:52 PM",
    "atmosphere": "warm night air, still water, quiet high-end energy"
  },
  "lighting": {
    "type": "underwater pool lights + warm ambient",
    "temperature": "warm (3200K)",
    "effect": [
      "glowing reflections on wet skin",
      "soft highlights across collarbones and legs",
      "water reflections flickering on bodies",
      "slight iPhone night mode exposure lift"
    ]
  },
  "subjects": [
    {
      "role": "foreground girl",
      "pose": {
        "position": "sitting on pool edge",
        "legs": "in water",
        "torso": "leaning slightly back on one arm"
      },
      "expression": {
        "eyes": "locked directly into camera",
        "energy": "calm but dominant"
      }
    },
    {
      "role": "second girl",
      "pose": {
        "position": "standing in pool between her legs",
        "water_level": "upper thighs",
        "arms": "lightly resting on pool edge beside first girl"
      },
      "interaction": {
        "proximity": "very close, bodies almost touching",
        "tension": "intimate but unspoken"
      },
      "expression": {
        "eyes": "looking at the first girl, not camera",
        "energy": "focused, slightly teasing"
      }
    }
  ],
  "styling": {
    "hair": "both slightly wet, natural texture",
    "outfits": "minimal triangle bikinis, contrasting tones (black + cream)"
  },
  "camera": {
    "angle": "eye-level, slightly tilted",
    "distance": "medium shot",
    "focus": "foreground sharp, background soft"
  },
  "post_processing": {
    "editing": "minimal",
    "grain": "light night grain",
    "skin": "natural wet texture"
  }
}
```
---

### 6. 莫扎特的《唐璜》：最后的晚餐

**作者**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619/status/2033882182788518246)  **日期**: 2026-03-17  **语言**: ja

> 为 Nano Banana Pro (Gemini 3 Pro Image) 提供的提示，用于生成一张基于莫扎特歌剧《唐璜》的图像，具体描绘“最后的晚餐”，其中可能包含唐璜、莱波雷洛和司令官鬼魂等角色。

![莫扎特的《唐璜》：最后的晚餐](https://cms-assets.youmind.com/media/1773816095680_5rixfw_HDnND4TbEAg36zQ.jpg)

```
モーツァルト
ドン・ジョバンニ
{argument name="シーン" default="最後の晩餐"}
```
---

### 7. 80 年代夏日芭比风：野餐桌上的女人照片

**作者**: [LexiPrompt](https://x.com/Artist04048661/status/2033717433622507581)  **日期**: 2026-03-17  **语言**: en

> 一个详细的 JSON 提示，用于 Nano Banana Pro 生成一张具有 80 年代夏季美学的超逼真 RAW 照片。主体是一位年轻女性，身穿亮面亮粉色连体泳衣和旱冰鞋，坐在绿松石色野餐桌旁，置身于正午刺眼的阳光下。

![80 年代夏日芭比风：野餐桌上的女人照片](https://cms-assets.youmind.com/media/1773816097287_xfhsrf_HDk3JB0WYAAETVY.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman with a strong resemblance to {argument name="celebrity name" default="[USER PROVIDED NAME]"}.",
      "hair": "Long, wavy, and sun-kissed hair with natural movement, cascading down her back and shoulders with a slightly windblown texture.",
      "face": "Confident expression with a slight tilt; dewy, sun-drenched skin texture with visible fine pores and a natural glow.",
      "body": "Athletic and toned physique; skin has a realistic sheen from sunscreen or light perspiration, reflecting the direct sunlight.",
    },
    "attire": {
      "clothing": "A form-fitting, glossy hot pink one-piece swimsuit with a subtle latex or vinyl-like sheen, featuring structured bustier-style seams. Paired with white crew socks and mint-green quad roller skates with translucent teal wheels.",
      "style": "Retro 80s Summer Aesthetic / Barbiecore"
    },
    "styling_and_accessories": {
      "jewelry": [
        "White retro cat-eye sunglasses",
        "Thin gold chain necklace",
        "Small pink hoop earrings",
        "Pink transparent sun visor resting on the table",
        "Glass cola bottle"
      ]
    },
    "environment": {
      "setting": "A bright, outdoor beach club or patio with a weathered, turquoise-painted wooden picnic table.",
      "background": "Sandy ground with soft shadows, a white wooden fence structure, and a large inflatable pink flamingo partially visible.",
      "water": "None"
    },
    "pose": {
      "posture": "Sitting atop a turquoise picnic table with legs spread wide; one foot resting on the tabletop and the other on the bench.",
      "arms": "Leaning back slightly with her left hand braced against the table surface for support.",
      "angle": "High-angle shot looking down at the subject."
    },
    "lighting_and_mood": {
      "lighting": "Harsh, direct natural midday sunlight creating high-contrast shadows and bright highlights on the skin and glossy fabric.",
      "mood": "Vibrant, nostalgic, and energetic summer vibe.",
      "colors": "A palette dominated by hot pink, turquoise, white, and warm sandy beige."
    },
    "camera_and_technical": {
      "style": "Ultra Photorealistic, RAW photo.",
      "lens": "35mm wide-angle lens",
      "aperture": "f/4.0 for sharp detail across the subject and immediate environment",
      "quality_tags": [
        "8k resolution",
        "highly detailed",
        "volumetric lighting",
        "ray tracing reflections",
        "hyper-realistic texture",
        "Hasselblad photography"
      ]
    }
  }
}
```
---

### 8. 阳光草莓女孩比基尼快照

**作者**: [Layla 🌙](https://x.com/BananaPromptPro/status/2030659425204412418)  **日期**: 2026-03-08  **语言**: en

> 一个用于 Nano Banana 2 的详细 JSON 提示，生成一张业余智能手机快照：一位身材丰满的女性，胸部夸张丰满，穿着红白条纹三角比基尼上衣和带有草莓图案的高腰针织短裤，在自然阳光下斜靠在白色阳台栏杆上。

![阳光草莓女孩比基尼快照](https://cms-assets.youmind.com/media/1773038331055_4u0f61_HC5Z8qJaQAAnxfg.jpg)

```
{
  "photo_type": "Amateur smartphone snapshot",
  "subject": {
    "age": "Early 20s",
    "body_type": "Young Woman, exaggerated Large round breast shape, prominent projected profile, fuller bust measurement, large-breasted proportions, fuller chest frame, shapely upper silhouette, top-heavy silhouette, buxom figure, high waist-to-hip contrast, defined waistline, fuller glute measurement, curvy, prominent hips, rounded hip contour, curvy lower body, thick, powerful thighs, full thighs, push-up bra effect",
    "description": "A woman with a curvaceous figure and an oval-shaped face, standing casually outdoors. She has high cheekbones and a sun-kissed, smooth complexion. Her hair is long, thick, and dark wavy, framing her features. Her physique is shapely with a high waist-to-hip contrast and a defined waistline.",
    "ethnicity": "NA",
    "expression": "Slightly parted lips, neutral but relaxed gaze",
    "gender": "Female",
    "mirror_rules": "None",
    "pose_description": "Leaning back slightly against a white balcony railing, hands resting on the ledge to her sides, body angled slightly toward the camera.",
    "tattoos": "None"
  },
  "clothing": {
    "bottom": {
      "color": "White",
      "details": "Embroidered large red strawberry motif with green leaves on the front leg",
      "fabric": "Knit crochet",
      "type": "High-waisted mini shorts"
    },
    "fit_and_physics": "The bikini top is strained over a fuller bust, creating tension lines in the fabric. The knit shorts show minor bunching at the waist and compression creases where the fabric meets the hips.",
    "outerwear": {
      "color": "None",
      "details": "None",
      "fabric": "None",
      "type": "None"
    },
    "shoes": {
      "color": "None",
      "details": "None",
      "fabric": "None",
      "type": "None"
    },
    "top": {
      "color": "{argument name="bikini color" default="Red and white"}",
      "details": "Thin horizontal stripes, white scalloped trim along the edges",
      "fabric": "Spandex-blend",
      "type": "Triangle bikini top"
    }
  },
  "hair": {
    "color": "Dark brown to black",
    "interaction": "Loose and voluminous, slightly wind-blown with a few strands resting across her face",
    "style": "Long, thick, dark wavy hair with a natural side part"
  },
  "face": {
    "description": "Use the uploaded character reference image, keep all facial details 100% unchanged",
    "eyebrows": "Defined, arched eyebrows",
    "eyes": "Large, almond-shaped brown eyes",
    "lips": "Full with a well-defined cupid’s bow",
    "makeup": "Minimal, subtle winged eyeliner and a glossy lip"
  },
  "skin_texture": "Natural sun-kissed skin with visible pores on the nose and cheeks, slight sheen from moisture or sun-protection, and subtle dermal translucency.",
  "biological_features": {
    "eye_complexity": "Wetness of the tear duct and sharp corneal reflections from natural sunlight",
    "hair_strand_physics": "Individual f
```
---

### 9. 基于参考图像在 Snow 中生成角色

**作者**: [Bethany](https://x.com/JustBethanyai/status/2030621166344278073)  **日期**: 2026-03-08  **语言**: en

> 一个结构化的提示模板，旨在生成一张雪地森林中人物的图像，需要一张参考图像来定义人物的身份、服装和身体特征。该提示指定了全身镜头、平视视角，并包含一辆雪地摩托作为道具。

![基于参考图像在 Snow 中生成角色](https://cms-assets.youmind.com/media/1773038337939_2gj7ez_HC43HxyWsAAgflI.jpg)
![基于参考图像在 Snow 中生成角色](https://cms-assets.youmind.com/media/1773038338109_r85qqb_HC43H2gWIAAEDDB.jpg)
![基于参考图像在 Snow 中生成角色](https://cms-assets.youmind.com/media/1773038338073_105ndt_HC43H2WXIAAv2Xy.jpg)

```
{
  "identity": {
    "description": "Define your character based on a reference image: detailed physical features and personal style",
    "gender": "To be taken from reference image",
    "age_range": "Estimated age range from reference image",
    "skin_tone": "Skin tone from reference image",
    "hair_color": "Hair color from reference image",
    "hair_length": "Hair length from reference image",
    "hair_style": "Hair style from reference image",
    "facial_features": "Distinct facial features from reference image (eyes, nose, lips, etc.)"
  },
  "character": {
    "pose": "Standing, slightly right leg forward, left hand resting on snowmobile",
    "gesture": "Left hand touching snowmobile, right hand at side",
    "gaze": "Looking directly at the camera, serious and determined expression",
    "mood": "Cool, confident, and focused",
    "expression": "Neutral, slightly intense gaze"
  },
  "clothing": {
    "top": "Top clothing from reference image, with color and details",
    "bottom": "Bottom clothing from reference image, with color and details",
    "gloves": "Glove style and color from reference image",
    "footwear": "Shoe or boot style and color from reference image",
    "accessories": "Jewelry, bags, or other accessories from reference image"
  },
  "hair": {
    "style": "Hair style from reference image",
    "accessories": "Hair accessories from reference image (if any)"
  },
  "makeup": {
    "style": "Makeup style and tones from reference image"
  },
  "camera": {
    "angle": "Front, eye-level, full-body shot",
    "distance": "Medium distance",
    "lens_effects": "Natural light, slightly soft focus"
  },
  "background": {
    "location": "Snow-covered forest area",
    "elements": "Large coniferous trees, snowmobile",
    "weather": "Cloudy, snowy ground",
    "lighting": "Natural, daytime light"
  },
  "props": {
    "vehicle": "Black and yellow snowmobile, with visible model details",
    "other": "None"
  }
}
```
---

### 10. Nike Dunk 破壁而出

**作者**: [Aegon](https://x.com/Fujimoto_hina/status/2030574006966059261)  **日期**: 2026-03-08  **语言**: en

> 一个为 Nano Banana Pro 在 Gemini 上设计的结构化 JSON 提示，详细描述了一只 Nike Dunk 运动鞋冲破冰状晶体墙的场景，强调酷炫的蓝色和白色调、反光的霜冻纹理，以及 2:3 宽高比的高端奢华感。

![Nike Dunk 破壁而出](https://cms-assets.youmind.com/media/1773038328321_0lw0g4_HC4MSbkbQAALVR8.jpg)
![Nike Dunk 破壁而出](https://cms-assets.youmind.com/media/1773038328394_if7mc4_HC4MSdLaMAA1Nz9.jpg)

```
{
  "image_generation_prompt": {
    "subject": "{argument name="shoe subject" default="Nike Dunk shoe"}",
    "action": "bursting through an ice-like crystalline wall",
    "environment_details": [
      "shards frozen mid-air",
      "cold vapor swirling around"
    ],
    "lighting_and_colors": {
      "palette": "cool blue and white tones",
      "mood": "emphasizing clarity and speed"
    },
    "style_and_texture": {
      "texture": "reflective frost textures",
      "composition": "clean composition",
      "overall_tone": "high-end luxury tone"
    },
    "parameters": {
      "aspect_ratio": "2:3"
    },
    "original_prompt": "Nike Dunk shoe bursting through an ice-like crystalline wall, shards frozen mid-air, cold vapor swirling around. Lighting uses cool blue and white tones, emphasizing clarity and speed. Reflective frost textures and clean composition give it a high-end luxury tone --ar 2:3"
  }
}
```
---

### 11. 低角度业余快照，透视感极强

**作者**: [Layla 🌙](https://x.com/BananaPromptPro/status/2030033950022979863)  **日期**: 2026-03-06  **语言**: en

> 一个高度详细的 JSON 提示，用于生成一张女性坐在地板上，直接向上看向镜头的业余低角度智能手机快照。该提示侧重于保留参考图像中的面部身份，并详细描述服装的真实物理特性（牛仔裤堆叠、上衣紧绷）以及皮肤和织物的微观纹理。

![低角度业余快照，透视感极强](https://cms-assets.youmind.com/media/1772864612298_b6rshx_HCwg-kOa8AAYLdr.jpg)

```
{
  "photo_type": "Amateur low-angle smartphone snapshot",
  "subject": {
    "age": "Young adult",
    "body_type": "Well Endowed Young Woman (From Uploaded reference Image)",
    "description": "A Well Endowed Young Woman looking up at the camera from a low seated position, appearing smaller in the frame due to the extreme perspective.",
    "ethnicity": "NA",
    "expression": "Slightly pouting, looking directly up at the lens",
    "gender": "Female",
    "mirror_rules": "None",
    "pose_description": "Sitting on the floor with knees pulled tightly to the chest, head tilted back and looking straight up into the camera lens.",
    "tattoos": "None"
  },
  "clothing": {
    "bottom": {
      "color": "Dark blue",
      "details": "Visible denim grain and vertical seam stitching",
      "fabric": "Denim",
      "type": "Jeans"
    },
    "fit_and_physics": "The jeans are bunched up around the knees and thighs due to the crouched sitting position; the white top is pulled taut across the chest and shoulders.",
    "outerwear": {
      "color": "None",
      "details": "None",
      "fabric": "None",
      "type": "None"
    },
    "shoes": {
      "color": "None",
      "details": "Not visible",
      "fabric": "None",
      "type": "None"
    },
    "top": {
      "color": "White",
      "details": "Ribbed texture, sleeveless tank style",
      "fabric": "Cotton",
      "type": "Tank top"
    }
  },
  "hair": {
    "color": "Dark brown to black",
    "interaction": "Tied back away from the face",
    "style": "Long, wavy texture, high density, pulled into a low ponytail that drapes over the shoulder"
  },
  "face": {
    "description": "Use the uploaded character reference image, keep all facial details 100% unchanged",
    "eyebrows": "Thick, dark, and arched",
    "eyes": "Dark brown, almond-shaped",
    "lips": "Full lips held in a pursed pout",
    "makeup": "Minimal, natural look"
  },
  "skin_texture": "Light-to-medium skin tone with warm undertones, clear texture with visible vellus hair on the jawline",
  "biological_features": {
    "eye_complexity": "Sharp corneal reflections, visible wetness on the tear duct, slight veins in the sclera",
    "hair_strand_physics": "Fine stray hairs escaping the ponytail, individual strands catching the overhead light",
    "skin_micro_texture": "Visible pores on the nose and cheeks, subsurface scattering around the ears",
    "subsurface_scattering": "Natural warmth visible where light hits the skin edges",
    "vascularity_and_pigment": "Faint natural redness on the cheeks and knuckles"
  },
  "texture_details": {
    "environment": "Smooth matte white ceiling with slight texture, recessed plastic light fixture",
    "fabric": "Rough, heavy weave of denim contrasted with soft, thin cotton ribbing",
    "hair": "Richly textured dark strands with a healthy sheen",
    "skin": "Natural skin with subtle imperfections, not "
  }
}
```
---

### 12. 台球桌上的俯卧姿势，细节纤毫毕现

**作者**: [Pinodi](https://x.com/PinodiArt/status/2029632175482507599)  **日期**: 2026-03-05  **语言**: en

> 一个极其详细的 JSON 提示，用于生成一张超逼真的西德尼·斯威尼（Sydney Sweeney）图像，她身穿淡紫色紧身衣，俯卧在绿色毛毡台球桌上，提示中详细说明了法医级别的面部细节、身体形态，以及服装和场景元素的材料科学。

![台球桌上的俯卧姿势，细节纤毫毕现](https://cms-assets.youmind.com/media/1772778711695_7dpvxu_HCqzmjGWEAALzV-.jpg)
![台球桌上的俯卧姿势，细节纤毫毕现](https://cms-assets.youmind.com/media/1772778711733_y3bscv_HCqzkiOXEAE3uDT.jpg)

```
{
  "subject": {
    "identity": {
      "biometric_reference": "Sydney Sweeney",
      "facial_forensics": {
        "structure": "Soft-edged heart-shaped facial morphology, high malar bones with specific 120-degree zygomatic arch projection, refined orthognathic profile.",
        "eyes": "Large, almond-shaped hooded eyes, deep set; iris pattern features complex radial fibers in cerulean blue (#96B9D0) with a distinct dark grey limbal ring; natural eyelashes with varied lengths.",
        "dentition": "Natural dental alignment, slight prominence of the maxillary central incisors, translucent incisal edges, anatomical gum contouring without artificial whitening.",
        "skin_physics": "Fitzpatrick Scale Type II (#F7E2D3); visible dermal pores, subtle telangiectasia, natural freckle distribution across the nasal bridge and malar regions; subsurface scattering enabled for realistic light penetration."
      },
      "body_morphology": {
        "somatotype": "Mesomorphic-ectomorphic hybrid with pronounced hourglass proportions; specific waist-to-hip ratio of 0.70.",
        "anatomical_details": "Well-defined clavicles, subtle suprasternal notch, natural breast volume with anatomical gravitational sag in prone position; soft muscle definition in the rectus abdominis and external obliques; detailed phalanges and metacarpal structures on hands."
      }
    },
    "hair": {
      "texture": "Fine, wavy hair fibers with multi-tonal layering; base color honey blonde (#AF8F55) with platinum highlights (#E8D1A7).",
      "physics": "Individual strand rendering, natural flyaways, specular highlights on hair curves."
    }
  },
  "wardrobe": {
    "primary_piece": {
      "description": "Sleeveless mauve-colored bodysuit (#8E5A63) with a functional silver metallic front zipper.",
      "material_science": "Polyester-elastane blend with micro-ribbed texture; high-tension seams; subsurface scattering on fabric edges; zero logos or branding.",
      "fit": "Compression fit following the anatomical curvature of the torso and hips; high-cut leg openings."
    }
  },
  "pose_action": {
    "description": "The subject is in a prone position on a billiard table, propped up on her forearms and elbows. Her back is slightly arched, legs are bent at the knees with feet raised toward the ceiling in a relaxed, natural position. The head is turned 45 degrees to her right, looking away from the camera with a neutral, non-smiling facial expression.",
    "hand_placement": "Left hand resting over the right hand on the billiard table surface near a yellow billiard ball."
  },
  "scene": {
    "environment": "A dimly lit, classic wood-paneled billiard room.",
    "elements": [
      {
        "object": "Billiard table",
        "details": "Professional-grade green felt surface (#2E5A31); dark mahogany wood rails with matte finish."
      },
      {
        "object": "Billiard accessories",
        "details": "S
```
---

### 13. 角色一致性模板和示例提示

**作者**: [Ryan Hart](https://x.com/thisdudelikesAI/status/2029119768364769429)  **日期**: 2026-03-04  **语言**: en

> 一个模板和示例提示，演示如何在 Nano Banana Pro 中使用 JSON 参数，以在多张图像中保持角色一致性，特别是针对科技初创公司团队头脑风暴的场景。

![角色一致性模板和示例提示](https://cms-assets.youmind.com/media/1772692193412_fisa2i_HCjhrQqawAMozyQ.jpg)

```
{
  "scene": "tech startup team brainstorming in modern office",
  "characters": [
    {
      "character_id": 1,
      "description": "Asian female engineer, mid-20s, black hair in ponytail, wearing blue hoodie and glasses, confident expression",
      "consistency_priority": "high",
      "position": "center, gesturing at whiteboard"
    },
    {
      "character_id": 2,
      "description": "Latino male developer, early-30s, beard, casual t-shirt, focused expression",
      "consistency_priority": "high",
      "position": "left side, typing on laptop"
    }
  ],
  "character_interactions": "collaborative and engaged, both focused on same project",
  "maintain_across_series": true
}
```
---

### 14. Lo-Fi 暖色工作室动态联系表 3x3 网格

**作者**: [Özge Döner](https://x.com/astronomerozge1/status/2028113144267125234)  **日期**: 2026-03-01  **语言**: en

> 一个复杂的 JSON 提示，用于图生图生成，要求制作一张 3x3 的联系表，其中包含同一位女性在一个温暖米色工作室中运动的画面。风格为低保真模拟，强调柔焦、刻意的运动模糊以及九种不同姿势/构图下的抓拍式、不完美的取景。

![Lo-Fi 暖色工作室动态联系表 3x3 网格](https://cms-assets.youmind.com/media/1772433522931_th6vru_HCVOGFBWYAAxFbg.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "lofi_soft_motion_contact_sheet_3x3_no_text",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_LOFI_SOFT_MOTION_WARM_STUDIO_3X3"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "notes": "Use the reference as the primary style anchor. Create a 3x3 contact sheet (9 panels) with the SAME adult woman identity across all panels. Warm beige studio wall, lo-fi soft focus, intentional motion blur, hair movement, candid cropped framing. No text, no logos, no watermark."
    },
    "output_settings": {
      "aspect_ratio": "1:1",
      "resolution_target": "ultra_high_res",
      "num_images": 1,
      "layout": {
        "type": "grid",
        "rows": 3,
        "cols": 3,
        "gutter": "thin_white",
        "outer_border": "none",
        "panel_consistency": "high"
      },
      "sharpness": "soft_lofi",
      "grain": "subtle_analog",
      "render_style": "lofi_film_studio"
    },
    "scene": {
      "concept": "lo-fi warm studio contact sheet with motion",
      "environment": "plain warm beige wall, minimal studio, no props",
      "lighting": {
        "style": "soft warm ambient light",
        "key_light": "diffused light from one side, gentle falloff",
        "avoid": "flash, harsh shadows, modern HDR look"
      },
      "camera": {
        "lens": "35mm",
        "look": "handheld candid framing",
        "focus": "intentionally soft with slight motion blur"
      }
    },
    "subject": {
      "type": "adult woman",
      "wardrobe": "white fitted tank / off-shoulder top + low-rise blue jeans, no logos",
      "hair": "long dark hair, loose and moving, wind-blown",
      "makeup": "minimal natural",
      "anatomy_rules": "natural body proportions, realistic hands, no warped limbs"
    },
    "panel_direction": {
      "global_rule": "same identity and styling across all 9 panels; vary crop + pose; allow slight motion blur and imperfect framing",
      "panel_01": "upper-body, head turned, hair whipping, soft blur",
      "panel_02": "full-body side view, walking/turning, jeans visible",
      "panel_03": "tight crop shoulder/neck, hair covering part of face",
      "panel_04": "tilted close-up, eyes half closed, dreamy motion",
      "panel_05": "mid shot, neck arched back, hand on collarbone, hair flying",
      "panel_06": "mid-full, arms raised, torso twist, candid energy",
      "panel_07": "tight crop chest/hand, hand resting on chest, soft blur",
      "panel_08": "back view mid-full, one arm up, hair lifted, jeans waistband visible",
      "panel_09": "cropped torso/waist, top + jeans detail, motion blur"
    },
    "style": {
      "color_palette": "warm beige + soft skin tones + washed denim blues",
      "contrast": "low-medium",
```
---

### 15. Sydney Sweeney 和 Ana de Armas 海滩姿势

**作者**: [Pinodi](https://x.com/PinodiArt/status/2028068618953539989)  **日期**: 2026-03-01  **语言**: en

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
---

### 16. Sadie Sink 红色皇家之夜魅力造型

**作者**: [Zainab Fatima](https://x.com/Zainabfat2728/status/2027953828361081040)  **日期**: 2026-03-01  **语言**: en

> 一个详细的 JSON 提示，旨在生成一张萨迪·辛克（Sadie Sink）风格的女性魅力四射、富有戏剧性的图像。场景设定在一个带有红色霓虹灯的奢华休息室中，重点突出亮红色紧身连衣裙和自信、沉着的表情。

![Sadie Sink 红色皇家之夜魅力造型](https://cms-assets.youmind.com/media/1772433517127_e6ji01_HCS9PujbEAIvUv7.jpg)

```
{
  "title": "Red Royal Night Glam",
  "caption": "Bold in red, glowing under neon lights — confidence that speaks without words.",
  "description": "A stunning woman confidently posing in a striking red bodycon mini dress with a sheer midsection and matching neck scarf. She is seated gracefully on a black velvet sofa inside a luxurious modern lounge illuminated by vibrant red neon lighting. Her sleek tied-back hairstyle, flawless makeup, and poised expression enhance the glamorous night-out aesthetic.",
  "outfit_details": {
    "dress_color": "{argument name="dress color" default="Bright Red"}",
    "dress_style": "Bodycon mini dress with sheer waist detail",
    "accessories": "Matching red neck scarf",
    "hairstyle": "Sleek low bun",
    "makeup": "Soft glam with highlighted cheeks and nude lips"
  },
  "environment": {
    "location_type": "Upscale lounge / club",
    "lighting": "{argument name="lighting" default="Red neon ambient lights"}",
    "furniture": "Black velvet sofa with patterned cushion",
    "mood": "Luxurious, bold, and dramatic"
  },
  "pose": {
    "position": "Seated elegantly",
    "hand_gesture": "One hand resting under chin",
    "expression": "Confident and playful"
  },
  "aesthetic": "Modern night glamour with a powerful red theme",
  "vibe": "Confident, classy, and attention-grabbing"
}
```
---

### 17. 动感美学比基尼姿势

**作者**: [MiraFrames](https://x.com/miraframes/status/2026367594891030968)  **日期**: 2026-02-24  **语言**: en

> 一个结构化的 JSON 提示词，用于生成一张高对比度、奢华的夏季动作图像：一名金发女性身穿黑色比基尼，佩戴战术手枪枪套，在船甲板上摆姿势。

![动感美学比基尼姿势](https://cms-assets.youmind.com/media/1772001498156_nzsen4_HB8alflX0AA0crp.jpg)

```
{
  "image_description": "A blonde, tanned woman posing on a boat deck in the middle of the ocean. She is wearing a black string bikini and has a tactical holster with a handgun strapped to her thigh.",
  "subject": {
    "gender": "Female",
    "hair_color": "Blonde",
    "clothing": {
      "top": "Black string bikini top",
      "bottom": "Black string bikini bottom"
    },
    "accessories": [
      "Gold bracelet",
      "Thigh holster with a handgun"
    ],
    "pose": "Side profile, looking down, adjusting bikini strings"
  },
  "setting": {
    "location": "Boat/Yacht deck",
    "background": "Deep blue ocean, clear blue sky with white clouds",
    "lighting": "Bright, direct sunlight"
  },
  "objects": [
    "White outboard boat engine",
    "Teak wood decking",
    "Handgun"
  ],
  "aesthetic": {
    "color_palette": ["Deep Blue", "Bronze", "Black", "White"],
    "style": "High-contrast, luxury, summer action aesthetic"
  }
}
```
---

### 18. 高保真换脸任务定义

**作者**: [Spicy Success](https://x.com/spicyysuccess/status/2025149131162014179)  **日期**: 2026-02-21  **语言**: en

> 这是一个为 Nano Banana Pro 定义高保真换脸任务的结构化 JSON 提示。指令强调无缝、超真实的融合，保留源身份，匹配肤色和表情，并保持原始背景和构图细节。

![高保真换脸任务定义](https://cms-assets.youmind.com/media/1771741695019_yhyyta_HBrFTtgbgAE6U4A.jpg)
![高保真换脸任务定义](https://cms-assets.youmind.com/media/1771741695023_ngmk6p_HBrFTtLbgAA_kwv.jpg)

```
"task": "face_swap",
  "model": "nano_banana_pro",
  "instructions": {
    "primary_goal": "Transfer the face from source image (image1) onto the subject in target image (image2) with seamless, ultra-realistic integration",
    "source_mapping": {
      "face_source": "image1",
      "face_target": "image2",
      "preserve_source_identity": true
    },
    "identity": {
      "match_skin_tone": true,
      "match_facial_expression": true,
      "maintain_face_structure": true
    },
    "blending": {
      "seamless_edges": true,
      "match_lighting": true,
      "match_color_grading": true,
      "preserve_shadows_highlights": true,
      "no_visible_artifacts": true
    },
    "background": {
      "preserve_original_background": true,
      "preserve_environment_details": true,
      "no_changes_to_objects": true,
      "no_blur_or_distortion": true
    },
    "composition": {
      "keep_original_pose": true,
      "keep_camera_angle": true,
      "keep_framing": true,
      "maintain_depth_of_field": true
    },
    "quality": {
      "ultra_realistic": true,
      "high_resolution": true,
      "natural_texture": true,
      "no_ai_look": true
```
---

### 19. 圣保罗保利斯塔大道绘画提示 (JSON 参考)

**作者**: [iuri kothe](https://x.com/ik80/status/2024186584220787101)  **日期**: 2026-02-18  **语言**: en

> 一个 JSON 提示的摘要描述（推文中未完全提供），旨在生成一幅圣保罗保利斯塔大道的不对称两点线性透视画作，以 MASP 大楼为焦点。

![圣保罗保利斯塔大道绘画提示 (JSON 参考)](https://cms-assets.youmind.com/media/1771483120273_0cimrv_HBda0tlXEAAm1_I.jpg)
![圣保罗保利斯塔大道绘画提示 (JSON 参考)](https://cms-assets.youmind.com/media/1771483120418_n9ybmk_HBdVX_tWYAAeCpP.jpg)

```
An asymmetrical two-point linear perspective painting of são paulo, avenida paulista. A prominent MASP building is the focal point,...
```
---

### 20. JSON 结构化提示，用于制作爆浆芝士卷

**作者**: [Meem](https://x.com/mehvishs25/status/2023588113071948118)  **日期**: 2026-02-17  **语言**: en

> 一个高度结构化的 JSON 提示，旨在生成一张戏剧性的微距摄影图像：一个芝士卷在零重力下于半空中裂开，融化的芝士拉出丝状，蒸汽弥漫，背景设定在一个电影般的夜市环境中。

![JSON 结构化提示，用于制作爆浆芝士卷](https://cms-assets.youmind.com/media/1771396580504_vyo2mr_HBU6pz9bIAAn0Hn.jpg)
![JSON 结构化提示，用于制作爆浆芝士卷](https://cms-assets.youmind.com/media/1771396580420_p9fwqr_HBU6pzuaIAA1pDr.jpg)
![JSON 结构化提示，用于制作爆浆芝士卷](https://cms-assets.youmind.com/media/1771396580502_jq7gnx_HBU6p1jboAAgP0h.jpg)
![JSON 结构化提示，用于制作爆浆芝士卷](https://cms-assets.youmind.com/media/1771396581675_5jpka5_HBU6p68bQAAwliy.jpg)

```
{
  "subject": {
    "item": "{argument name="item" default="Cheesy Roll"}",
    "state": "split_mid_air",
    "physics": {
      "gravity": "zero_g",
      "motion": "floating_explosion",
      "particles": ["crumbs", "crispy_shards", "volumetric_steam"]
    },
    "filling": {
      "type": "molten_cheese",
      "action": "stretching_dynamic_pull",
      "texture": "gooey_high_viscosity"
    }
  },
  "environment": {
    "location": "Night Market",
    "lighting": {
      "type": "dramatic_cinematic",
      "background": "warm_bokeh_lights",
      "global_illumination": "low_key"
    }
  },
  "camera_settings": {
    "focal_length": "Macro",
    "depth_of_field": "Shallow (f/1.8)",
    "focus": "Ultra_Sharp",
    "resolution": "8K_UHD"
  }
}
```
---

### 21. Sydney Sweeney《蜘蛛夫人》首映礼礼服描述

**作者**: [Sadia](https://x.com/SadiaMalik182/status/2022534072724262916)  **日期**: 2026-02-14  **语言**: en

> 一个 JSON 提示，详细描述了西德尼·斯威尼 (Sydney Sweeney) 在《蜘蛛夫人》(Madame Web) 首映式上的造型，重点是她的发型、妆容、姿势，以及她定制的及地无肩带直筒礼服上精致的黑色亮片“蜘蛛网”图案。

![Sydney Sweeney《蜘蛛夫人》首映礼礼服描述](https://cms-assets.youmind.com/media/1771137180034_zq4ain_HBF8BQnbwAEZapu.jpg)
![Sydney Sweeney《蜘蛛夫人》首映礼礼服描述](https://cms-assets.youmind.com/media/1771137179932_dlis19_HBF8BH3akAAIFOh.jpg)
![Sydney Sweeney《蜘蛛夫人》首映礼礼服描述](https://cms-assets.youmind.com/media/1771137180460_h50hgn_HBF8BQlakAYA_0w.jpg)

```
{
  "subject": {
    "name": "Sydney Sweeney",
    "features": {
      "hair": "Long, voluminous blonde hair styled in soft, classic Hollywood waves with a middle part; warm honey and champagne tones.",
      "eyes": "Pale blue/green eyes with a subtle 'siren eye' makeup look.",
      "makeup": "Dewy, luminous skin finish; soft peach-pink blush; glossy rose-pink lips; winged black eyeliner with shimmering neutral eyeshadow.",
      "pose": "Red carpet stance; mix of front-facing and three-quarter profiles; hands resting naturally at hips."
    }
  },
  "attire": {
    "dress_style": "Custom floor-length, strapless column gown with a sweetheart neckline.",
    "color_palette": "Nude/beige base layered with intricate black detailing.",
    "textural_details": {
      "embroidery": "Intricate black sequined 'cobweb' or 'lattice' pattern sprawling across the bodice and hips.",
      "skirt": "Transitioning into a dense
```
---

### 22. Sydney Sweeney 夜店造型 (印地语/乌尔都语 JSON)

**作者**: [Qaiser Tzq](https://x.com/TzqQaiser/status/2020877483390947637)  **日期**: 2026-02-09  **语言**: en

> 一个结构化的 JSON 提示词，主要用印地语/乌尔都语（使用罗马化文字）编写，用于 Gemini Nano Banana Pro 模型，以生成三张在夜店场景中的 Sydney Sweeney 图像。它详细说明了霓虹蓝和粉色灯光、米色/裸色褶皱紧身连衣裙，以及每张图像文件的具体姿势。

![Sydney Sweeney 夜店造型 (印地语/乌尔都语 JSON)](https://cms-assets.youmind.com/media/1770706217525_enqq3f_HAuZV7SagAEQ4jh.jpg)
![Sydney Sweeney 夜店造型 (印地语/乌尔都语 JSON)](https://cms-assets.youmind.com/media/1770706217527_n1wbar_HAuZV7cbYAAiyrz.jpg)
![Sydney Sweeney 夜店造型 (印地语/乌尔都语 JSON)](https://cms-assets.youmind.com/media/1770706217541_tay477_HAuZV7rbgAAsJuG.jpg)

```
{
  "album_maloomat": {
    "shakhsiyat": "Sydney Sweeney",
    "paisha": "American Actress",
    "location": "Lounge / Nightclub jaisa mahool",
    "light": "Neon blue aur pink lighting",
    "libas_ki_tafseel": {
      "kism": "Ruched Bodycon Dress",
      "rang": "Tan / Nude",
      "length": "Midi length (ghutno tak)",
      "gala": "Deep V-neck"
    }
  },
  "tasveer_details": [
    {
      "file_name": "20260209_200356.jpg",
      "pose": "Seedha khadi hain, dono haath kamar par (hips) rakhe hue, muskurata hua chehra.",
      "accessories": "Bade sunhairi (gold) hoop earrings.",
      "background": "Lounge ki red velvet kursi aur lakdi ke pillar."
    },
    {
      "file_name": "20260209_200348.jpg",
      "pose": "Ek haath chehre (chin) ke paas hai aur deewar se halka tek lagaya hua hai.",
      "expression": "Narm aur pur-aitmad (confident) muskurahat."
    },
    {
      "file_name": "20260209_200340.jpg",
      "pose": "Side profile pose, jis mein dress ka ruched design aur strap nazar aa rahe hain.",
      "baal": "Sunehri (blonde) wavy baal jo kandhon par gire hue hain."
    }
  ]
}
```
---

### 23. AI 图像生成提示词：多角度呈现

**作者**: [ChatGPTパンダの知恵袋@AI_Grok](https://x.com/irasutoyakunnn/status/2020838332507517280)  **日期**: 2026-02-09  **语言**: ja

> 这条推文讨论了如何使用 AI 图像生成工具，例如 GPT Image 1.5、Nano Banana Pro 和 Grok，特别提到了一种利用 ComfyUI 和 LoRA 模型（Qwen-Image-Edit-2511 Multiple-Angles-LoRA）从单张图像生成不同角度的方法。它还引用了一系列实用的构图提示，用于生成原创角色、虚拟主播（Vtubers）或表情包的图像，内容严格限制为 SFW（适合工作场所）级别。

![AI 图像生成提示词：多角度呈现](https://cms-assets.youmind.com/media/1770706237203_w4v6lt_HAt1wDjbgAAZQBP.jpg)

```
自分のキャラ、Vtuber、memeの画像生成に便利な構図プロンプト
```
---

### 24. 为 Sadie Sink 设计的多帧提示，包含三种截然不同的时尚风格（Y2K、魅力、现代优雅）

**作者**: [Rowan](https://x.com/rowanali09/status/2020309293644558380)  **日期**: 2026-02-08  **语言**: en

> 一个复杂且结构化的提示，旨在生成 Sadie Sink 的三张不同图像，每张图像都代表一种独特的时尚风格（Y2K 流行、高雅魅力、现代优雅），并为每个画面详细说明了发型、服装、配饰、姿势和环境。

![为 Sadie Sink 设计的多帧提示，包含三种截然不同的时尚风格（Y2K、魅力、现代优雅）](https://cms-assets.youmind.com/media/1770619718375_i0j1h4_HAmUmEWbAAEDVLv.jpg)
![为 Sadie Sink 设计的多帧提示，包含三种截然不同的时尚风格（Y2K、魅力、现代优雅）](https://cms-assets.youmind.com/media/1770619718396_arkl7p_HAmUl_aacAAXaSp.jpg)
![为 Sadie Sink 设计的多帧提示，包含三种截然不同的时尚风格（Y2K、魅力、现代优雅）](https://cms-assets.youmind.com/media/1770619718403_jgdy2f_HAmUmAEbkAAZMa2.jpg)

```
{
  "subject_reference": {
    "name": "{argument name="celebrity name" default="Sadie Sink"}",
    "demographics": "Young female celebrity, light skin tone, distinctive natural red hair, blue eyes"
  },
  "images": [
    {
      "id": 1,
      "style": "Y2K Pop / Casual Red Carpet",
      "hair": {
        "color": "Copper red",
        "texture": "Long, loose waves",
        "styling": "Center part with two small pink butterfly clips pinned near the temples"
      },
      "attire": {
        "top": "Black strapless tube top (crop top)",
        "bottom": "Blue denim jeans with a low rise",
        "accessories": [
          "Silver rhinestone choker necklace",
          "Black belt with silver studs/grommets",
          "Silver belly button piercing"
        ]
      },
      "expression_and_pose": {
        "expression": "Subtle smirk/smile, looking slightly to the side",
        "pose": "Leaning forward slightly, playful demeanor"
      },
      "environment": {
        "setting": "Red carpet event",
        "background": "Blurred crowd with cameras (paparazzi), pink carpet flooring"
      }
    },
    {
      "id": 2,
      "style": "High Glamour / Ethereal",
      "hair": {
        "color": "Vibrant ginger red",
        "texture": "Voluminous, undefined crimped waves",
        "styling": "Loose and windblown, creating a halo effect around the face"
      },
      "attire": {
        "dress": "Silver bodice with intricate crystal and bead embroidery, side cutouts, tulle skirt elements"
      },
      "expression_and_pose": {
        "expression": "Radiant open-mouthed smile, joyful",
        "pose": "In motion, turning head over shoulder, hair caught in movement"
      },
      "environment": {
        "setting": "Formal premiere or gala",
        "background": "Dark blurred background, hint of red carpet below"
      }
    },
    {
      "id": 3,
      "style": "Modern Elegant / Sleek",
      "hair": {
        "color": "Deep red",
        "texture": "Soft waves",
        "styling": "Swept entirely over the left shoulder, side part"
      },
      "attire": {
        "dress": "Structured red gown with diagonal chest cutout and waist cutout, single wide shoulder strap"
      },
      "expression_and_pose": {
        "expression": "Neutral to serious, soft gaze directly at camera",
        "pose": "Standing straight, hands clasped gently in front of waist"
      },
      "environment": {
        "setting": "Press wall / Step-and-repeat",
        "background": "Black backdrop with repeated logos: 'tiff', 'Bell', 'VISA', 'Ontario'",
        "watermark": "gettyimages - Rodin Eckenroth"
      }
    }
  ]
}
```
---

### 25. 将增上寺化作谷内六郎风格的画作

**作者**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619/status/2020239561457299835)  **日期**: 2026-02-07  **语言**: ja

> 一个用于 Nano Banana Pro (Gemini 3 Pro Image) 的提示，要求将增上寺转化为具有谷内六郎 (Rokuro Taniuchi) 独特风味或风格的画作。

![将增上寺化作谷内六郎风格的画作](https://cms-assets.youmind.com/media/1770532848361_lovfqu_GCRihaybMAAN19f.jpg)
![将增上寺化作谷内六郎风格的画作](https://cms-assets.youmind.com/media/1770532848634_69sp62_HAlVKupacAIxULI.jpg)

```
増上寺を
谷内六郎　風味の絵にして出して！
```
---

### 26. 使用 Nano Banana Pro 从参考图像生成提示

**作者**: [のあ｜東証プライムAIアンバサダー](https://x.com/noasanAI/status/2019244599940903340)  **日期**: 2026-02-05  **语言**: ja

> 一位日本用户解释了 Nano Banana Pro 的一项强大功能：提供一张参考图像，然后指示该工具将其转换为 JSON 格式的提示词。用户可以轻松修改生成的提示词的特定部分，从而创建图像的各种变体。

![使用 Nano Banana Pro 从参考图像生成提示](https://cms-assets.youmind.com/media/1770360000133_73r9ed_HAO-2cRbUAELg-x.jpg)

```
Nano Banana Proは、参考画像をもとなげてこれをjson形式でのプロンプトにしてと指示したら、あとはそのプロンプトの変えたい部分だけを変更するだけでイメージに違いものができるからすぐやってみて

※著作権とかには注意 https://tco/gpr6o9CRiB
```
---

### 27. 20 世纪 70 年代的柯达克罗姆街头纪录片瞬间

**作者**: [Özge Döner](https://x.com/astronomerozge1/status/2019129444896526393)  **日期**: 2026-02-04  **语言**: en

> 一个详细的图像生成提示，旨在创作一张具有 20 世纪 70 年代至 80 年代柯达 Kodachrome 64 胶片美学、照片般真实的街头纪实瞬间，重点关注色彩驱动的人文故事和自然漫射光。

![20 世纪 70 年代的柯达克罗姆街头纪录片瞬间](https://cms-assets.youmind.com/media/1770273452651_2a7imv_HAVjc6HWUAADacE.jpg)

```
{
  "scene_type": "street documentary moment",
  "aesthetic_reference": "Kodachrome 64 / National Geographic 1970s–1980s",
  "visual_intent": "color-driven human story",

  "lighting": {
    "type": "natural diffused daylight",
    "contrast": "moderate-high",
    "mood": "timeless documentary realism"
  },

  "color_engine": {
    "reds": "dominant and textured",
    "greens": "warm organic",
    "yellows": "golden accents",
    "blues": "subdued cyan sky tones"
  },

  "human_rendering": {
    "skin_priority": true,
    "expression": "authentic, unposed",
    "separation_from_background": "clear but natural"
  },

  "post_processing_behavior": {
    "film_like": true,
    "no_modern_color_grading": true,
    "no_teal_orange_exaggeration": true
  }
}
```
---

### 28. 萨迪·辛克（Sadie Sink）身着希腊式长裙，置身古老遗迹

**作者**: [Sadia](https://x.com/SadiaMalik182/status/2018877865777885376)  **日期**: 2026-02-04  **语言**: en

> 一个详细的 JSON 提示，用于生成一张萨迪·辛克（Sadie Sink）身穿希腊风格的暗玫瑰色连衣裙，坐或涉水于古建筑遗迹（如罗马浴场）中的图像。该提示指定了湿发、淡妆以及金色蛇形臂环等配饰，并强调了天空和遗迹在水中的倒影。

![萨迪·辛克（Sadie Sink）身着希腊式长裙，置身古老遗迹](https://cms-assets.youmind.com/media/1770273485036_5hynbo_HAR-tCxXUAAGU_g.jpg)
![萨迪·辛克（Sadie Sink）身着希腊式长裙，置身古老遗迹](https://cms-assets.youmind.com/media/1770273485043_p1ig15_HAR-tGTWEAAYsDV.jpg)
![萨迪·辛克（Sadie Sink）身着希腊式长裙，置身古老遗迹](https://cms-assets.youmind.com/media/1770273485065_909t4c_HAR-tCuXsAAw3Ek.jpg)

```
{
  "subject": {
    "identity": "{argument name="subject name" default="Sadie Sink"}",
    "appearance": {
      "hair": "wet, shoulder-length, strawberry blonde/light red, slightly wavy strands falling around the face",
      "face": "natural look, minimal to no visible makeup, fair skin with freckles, serious and contemplative expression, gaze directed slightly upward or straight ahead",
      "body": "slender figure, skin wet from the surroundings"
    },
    "clothing": {
      "dress": {
        "color": "dusty rose or muted pink",
        "style": "sleeveless, deep V-neckline, gathered waist, flowing Grecian-inspired drapes",
        "fabric": "lightweight, wet and clinging to the body due to water immersion"
      },
      "accessories": [
        {
          "item": "arm cuff",
          "description": "gold, coiled snake design",
          "placement": "upper right arm"
        },
        {
          "item": "necklaces",
          "description": "layered gold chains, one shorter chain and one longer with a round pendant",
          "placement": "neck"
        },
        {
          "item": "bracelet",
          "description": "simple gold bangle",
          "placement": "right wrist"
        }
      ]
    },
    "poses": [
      "sitting in the water, leaning back on hands, looking upwards",
      "wading through water, body turned slightly, reaching down to touch the water surface",
      "sitting upright in water, looking directly at the camera, profile slightly visible"
    ]
  },
  "environment": {
    "location": "ancient architectural ruins, resembling a Roman or Greek thermal bath (e.g., Cleopatra's Pool in Hierapolis)",
    "elements": [
      "tall, weathered stone columns with ornate Corinthian capitals",
      "submerged ancient stone blocks",
      "stone arch structures in the background"
    ],
    "water": "clear, calm with gentle ripples, waist-deep to knee-deep, reflecting the sky and ruins"
  }
```
---

### 29. 历史安纳托利亚田野社论

**作者**: [Özge Döner](https://x.com/astronomerozge1/status/2018438579651764539)  **日期**: 2026-02-02  **语言**: en

> 一个结构化的提示，用于生成一张以古代安纳托利亚田野为背景、具有历史主题的编辑图片。场景聚焦于两位主体（一男一女，需要参考图片）有节奏地劳作，背景乌云密布，传达出伙伴关系和信任的氛围，服装采用朴素、分层的天然面料。

![历史安纳托利亚田野社论](https://cms-assets.youmind.com/media/1770100843435_d9if0n_HALu8J4XAAA-J1o.jpg)

```
{
  "generation_request":{
    "meta_data":{"tool":"NanoBanana Pro","task_type":"historical_human_connection_editorial","version":"L2_SHARED_WORK_SAFE"},
    "references":{"female":"UPLOAD_REF","male":"UPLOAD_REF"},
    "creative_prompt":{
      "scene_summary":"Ancient Anatolia fields.",
      "foreground_story":"They kneel apart but work in rhythm, exchanging glances.",
      "background_story":"Dark clouds gather, villagers hurry to cover crops.",
      "wardrobe":"Layered natural fabrics, fully modest.",
      "mood":"partnership, trust"
    }
  }
}
```
---

### 30. 一对情侣在 1920 年代的伊斯坦布尔翩翩起舞的历史浪漫社论

**作者**: [Özge Döner](https://x.com/astronomerozge1/status/2018394266813231157)  **日期**: 2026-02-02  **语言**: en

> 一个简洁的 JSON 提示，用于生成一张历史浪漫编辑图片，描绘一对情侣在 1920 年代的伊斯坦布尔跳舞。它着重于自由的氛围、早期现代时尚，以及一个在舞厅中，有其他舞者和爵士乐队演奏的场景。

![一对情侣在 1920 年代的伊斯坦布尔翩翩起舞的历史浪漫社论](https://cms-assets.youmind.com/media/1770100824975_6wzejm_HALG1xwXMAAnJk-.jpg)

```
{
  "generation_request":{
    "meta_data":{"tool":"NanoBanana Pro","task_type":"historical_romantic_editorial","version":"L11_DANCE"},
    "references":{"female":"UPLOAD_REF","male":"UPLOAD_REF"},
    "creative_prompt":{
      "scene_summary":"{argument name=\"location\" default=\"1920s Istanbul hall\"}.",
      "foreground_story":"They dance slowly, smiling.",
      "background_story":"Other couples dance, jazz band plays.",
      "wardrobe":"{argument name=\"fashion era\" default=\"Early modern fashion\"}.",
      "mood":"freedom"
    }
  }
}
```
---

### 31. Nanobanana Pro 香蕉图像生成

**作者**: [うみつる](https://x.com/umitsuru_fire/status/2018290319293628650)  **日期**: 2026-02-02  **语言**: ja

> 一位用户使用 Nanobanana Pro 生成了一张图片，并评论说“香蕉终究是香蕉”（指的是该工具的名称和主题）。提示词暗示与香蕉相关。

![Nanobanana Pro 香蕉图像生成](https://cms-assets.youmind.com/media/1770100859981_id4op2_HAJoWLZbMAAwzSj.jpg)
![Nanobanana Pro 香蕉图像生成](https://cms-assets.youmind.com/media/1770100860476_7n9ych_HAC248ubsAAIjDW.jpg)

```
Nanobanana Proでも作ってみた。
やっぱり腐っても{argument name="主題" default="バナナ"}ですかね😁💕
```
---

### 32. 明星冬季美学系列

**作者**: [Bahar azam](https://x.com/BaharAzamm561/status/2018117626686480648)  **日期**: 2026-02-02  **语言**: en

> 一个结构化的 JSON 提示，旨在生成一组四张 1:1 比例的图像，描绘不同的名人（Sydney Sweeney、Billie Eilish、Sadie Sink、Ana de Armas）穿着独特的冬季服装，置身于不同的冬季场景中，并侧重于特定的调色板和纹理，以营造出高级美感。

![明星冬季美学系列](https://cms-assets.youmind.com/media/1770100844395_di7xgf_HAHLRkNbQAEJMO8.jpg)
![明星冬季美学系列](https://cms-assets.youmind.com/media/1770100844378_ea4f6k_HAHLRjIakAAL2Nt.jpg)
![明星冬季美学系列](https://cms-assets.youmind.com/media/1770100844514_6bdszo_HAHLRkPa8AAU0jt.jpg)
![明星冬季美学系列](https://cms-assets.youmind.com/media/1770100845636_0oc0mb_HAHLRmJb0AALivA.jpg)

```
{
  "creator_id": "X_Creator_Project_2026",
  "content_type": "Premium Celebrity Aesthetics",
  "visual_specifications": {
    "aspect_ratio": "1:1",
    "resolution": "1080x1080 pixels",
    "lighting": "Soft Natural Winter Light"
  },
  "collection_data": [
    {
      "subject": "{argument name="subject 1" default="Sydney Sweeney"}",
      "outfit_style": "Ribbed Emerald Bodysuit",
      "scene_setting": "Mountain Cabin Interior / Snowy Forest View",
      "visual_highlights": "Matte finish, high contrast green vs. white snow",
      "keyword_tags": ["Alpine Chic", "Emerald Fashion"]
    },
    {
      "subject": "Billie Eili sh",
      "outfit_style": "Oversized Burgundy High-Neck",
      "scene_setting": "Frost-Covered Birch Trees Background",
      "visual_highlights": "Deep velvet textures and cool-toned shadows",
      "keyword_tags": ["Burgundy Winter", "Alternative Style"]
    },
    {
      "subject": "Sadie Sink",
      "outfit_style": "Cobalt Blue Turtleneck with Tea Accessory",
      "scene_setting": "Warm Wood Trim Window Frame / Valley View",
      "visual_highlights": "Vibrant blue contrast with ginger hair tones",
      "keyword_tags": ["Blue Winter", "Cozy Vibes"]
    },
    {
      "subject": "{argument name="subject 4" default="Ana de Armas"}",
      "outfit_style": "V-Neck Royal Blue & Mustard Yellow Accents",
      "scene_setting": "Bright Minimalist Living Space / Arctic Fox View",
      "visual_highlights": "Sharp detailing on accessories and footwear",
      "keyword_tags": ["AnaDeArmasStyle", "VividAesthetics"]
    }
  ],
  "engagement_metrics": {
    "target_platform": "X / Twitter",
    "intended_impact": "Viral Reach / Subscriber Exclusive Content"
  }
}
```
---

### 33. 用于控制 Nano Banana Pro 中美学元素的结构化 JSON 提示

**作者**: [Papersir_H | AI Art](https://x.com/peigehub/status/2017660829970079936)  **日期**: 2026-01-31  **语言**: zh

> 一个为 Gemini 终端设计的结构化 JSON 提示，用于精确控制 Nano Banana Pro 模型生成图像。它使用结构化参数来定义运动、纹理、光照和氛围，以实现特定的美学效果，这表明 AI 生成是可以编程而非随机的。

![用于控制 Nano Banana Pro 中美学元素的结构化 JSON 提示](https://cms-assets.youmind.com/media/1769927688162_rac7bf_HAArzYBXgAAQr8z.jpg)
![用于控制 Nano Banana Pro 中美学元素的结构化 JSON 提示](https://cms-assets.youmind.com/media/1769927688200_t4ot5n_HAArzW0XQAAHsWC.jpg)
![用于控制 Nano Banana Pro 中美学元素的结构化 JSON 提示](https://cms-assets.youmind.com/media/1769927688270_2mf86s_HAArzX9XgAAbyKP.jpg)
![用于控制 Nano Banana Pro 中美学元素的结构化 JSON 提示](https://cms-assets.youmind.com/media/1769927689432_2wc8oc_HAArzWzXcAEngsO.jpg)

```
通过结构化参数控制 {motion}, {texture}, {lighting}, {atmosphere}。
四种截然不同的东方美学，同一个逻辑核心。
```
---

### 34. Symbolic Video Prompt: 边界保护价值

**作者**: [simeon-sanai](https://x.com/Naiknelofar788/status/2017460732938621180)  **日期**: 2026-01-31  **语言**: en

> 一个多场景视频生成提示（适用于 Veo 3.1），采用象征性、极简主义和写实风格。它通过两块相同的太妃糖——一块有包装，一块没有包装——以及蚂蚁，阐述了一个关于界限的道德教训，最后以文字叠加的形式传达了信息。

![Symbolic Video Prompt: 边界保护价值](https://cms-assets.youmind.com/media/1769927685691_ync6xc_G_91tJrbgAAXv1B.jpg)

```
"style": "cinematic, symbolic, minimal, realistic",
  "aspect_ratio": "9:16",
  "scenes": [
    {
      "scene_number": 1,
      "description": "A quiet outdoor setting with a clean surface under soft natural light. Two identical toffees are placed side by side.",
      "camera": "slow zoom-in",
      "mood": "calm, neutral"
    },
    {
      "scene_number": 2,
      "description": "One toffee is neatly wrapped in shiny paper. The other toffee is unwrapped, fully exposed.",
      "camera": "static close-up",
      "mood": "contrast, anticipation"
    },
    {
      "scene_number": 3,
      "description": "Ants begin to appear and slowly crawl toward the unwrapped toffee, completely ignoring the wrapped one.",
      "camera": "macro shot, slow motion",
      "mood": "uneasy, revealing"
    },
    {
      "scene_number": 4,
      "description": "More ants gather around the unwrapped toffee, covering it, while the wrapped toffee remains untouched and protected.",
      "camera": "top-down shot",
      "mood": "warning, realization"
    },
    {
      "scene_number": 5,
      "description": "Text fades in on screen as the ants swarm the unwrapped toffee.",
      "text_overlay": "{argument name="first message" default="When you are too open, you can be used."}",
      "camera": "gentle fade",
      "mood": "reflective"
    },
    {
      "scene_number": 6,
      "description": "Final frame focuses on the wrapped toffee standing alone, clean and intact.",
      "text_overlay": "{argument name="second message" default="Boundaries protect your value."}",
      "camera": "slow zoom-out",
      "mood": "empowering, calm"
    }
  ],
  "audio": {
    "background_music": "soft ambient piano",
    "sound_effects": "subtle nature ambience"
  }
}
```
---

### 35. 奥斯曼花园中的历史浪漫编辑场景

**作者**: [Özge Döner](https://x.com/astronomerozge1/status/2017317263775306043)  **日期**: 2026-01-30  **语言**: en

> 一个结构化的提示，用于生成一组以奥斯曼花园为背景的历史浪漫主题编辑图片。它需要男性和女性主体的参考图像，并描绘了一个场景：男子吟诵诗歌，女子温柔微笑，同时指定了服装（优雅的卡夫坦长袍和罩袍），旨在营造一种诗意、亲密的氛围。

![奥斯曼花园中的历史浪漫编辑场景](https://cms-assets.youmind.com/media/1769841108579_cms95f_G_7zU8xWYAAwKLs.jpg)

```
{
  "generation_request":{
    "meta_data":{"tool":"NanoBanana Pro","task_type":"historical_romantic_editorial","version":"L8_POEM"},
    "references":{"female":"UPLOAD_REF","male":"UPLOAD_REF"},
    "creative_prompt":{
      "scene_summary":"{argument name="scene location" default="Ottoman garden"}.",
      "foreground_story":"The man recites poetry; the woman smiles softly.",
      "background_story":"Fountain water flows, birds flutter.",
      "wardrobe":"Elegant kaftan and robe.",
      "mood":"poetic, intimate"
    }
  }
}
```
---

### 36. 广角畸变全身坐姿拍摄

**作者**: [jennieee:3](https://x.com/jenniebae_ai/status/2015899652646740277)  **日期**: 2026-01-26  **语言**: en

> 一个简洁的 JSON 提示，用于生成具有超广角透视畸变的全身坐姿照片。相机位于膝盖高度，重点是夸大主体下半身（穿着黑色紧身裤）的尺寸，背景是汽车内饰。

![广角畸变全身坐姿拍摄](https://cms-assets.youmind.com/media/1769495353973_3kpr3o_G_nne6QXAAAW8IU.jpg)
![广角畸变全身坐姿拍摄](https://cms-assets.youmind.com/media/1769495353949_rryjod_G_npxMQWAAEVWtg.jpg)
![广角畸变全身坐姿拍摄](https://cms-assets.youmind.com/media/1769495354003_d4ha22_G_nobKkWoAAZq3K.jpg)

```
{
  "prompt": "FULL BODY SEATED SHOT, 9:16 aspect ratio. Camera physically positioned at KNEE LEVEL, shooting straight at the subject. The subject is sitting cross-legged, looking directly into the lens. Focus heavily on the foreground legs in {argument name="clothing color" default="black"} tights, ensuring visible feet and shoes. Use wide-angle perspective distortion to exaggerate the size of the lower body against the car interior background."
}
```
---

### 37. Wareen - 紫色波波头女孩

**作者**: [Wareen 💟](https://x.com/Wareenaa/status/2014913224261702003)  **日期**: 2026-01-24  **语言**: en

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
---

### 38. Nano Banana Pro 的详细图像生成提示

**作者**: [sammy](https://x.com/sumiturkude007/status/2014217296445837380)  **日期**: 2026-01-22  **语言**: en

> 这是一个高度详细、结构化的 JSON 提示，专为名为“Nano banana pro”的图像生成模型设计。它详细说明了主体的年龄、性别、面部特征（头发、皮肤、妆容）、服装、姿势、表情，以及一个复杂的现代浴室场景，同时还包含光照和构图的技术细节。它旨在生成一张年轻女性靠在柜台上的中景特写图像。

![Nano Banana Pro 的详细图像生成提示](https://cms-assets.youmind.com/media/1769149378052_okkgag_G_Pv8-TaIAA7hlp.jpg)

```
{
  "prompt": {
    "subject": {
      "age": {argument name="age" default="20"},
      "gender": "female",
      "hair": {
        "color": "blonde",
        "style": "two high pigtails secured with light pink scrunchies",
        "length": "medium-long",
        "texture": "straight with some waves"
      },
      "skin": {
        "tone": "fair, with a warm, golden undertone",
        "texture": "smooth, glowing"
      },
      "face": {
        "eyes": {
          "color": "light blue/green",
          "makeup": "subtle eyeliner, mascara"
        },
        "brows": {
          "color": "dark blonde",
          "shape": "defined arch"
        },
        "nose": {
          "shape": "slender, defined"
        },
        "lips": {
          "color": "natural pink",
          "fullness": "full, glossy"
        },
        "cheeks": {
          "color": "rosy, with subtle highlight"
        }
      }
    },
    "clothing_and_accessories": {
      "top": {
        "type": "crop top",
        "color": "white",
        "fabric": "ribbed cotton",
        "details": "short sleeves, low scoop neck"
      },
      "bottoms": {
        "type": "high-waisted shorts",
        "color": "white",
        "fabric": "ribbed cotton"
      },
      "jewelry": {
        "necklace": "small white pearl strand",
        "bracelet": "gold chain and large silver watch on left wrist"
      }
    },
    "pose_and_expression": {
      "pose": "leaning forward over a white counter with hands resting on it, body angled away, looking over shoulder directly at camera",
      "expression": "seductive gaze, slightly parted lips"
    },
    "setting_and_background": {
      "location": "modern bathroom",
      "counter": "white quartz/marble",
      "shower": "glass enclosure with gold fixtures, tile wall",
      "towel_rack": {
        "material": "wooden floor stand",
        "contents": [
          {
            "type": "robe",
            "color": "white terry cloth",
            "details": "embroidered script on back"
          },
          {
            "type": "towel",
            "color": "red"
          },
          {
            "type": "towel",
            "color": "white"
          }
        ]
      },
      "door": "black frame, white panel"
    },
    "technical_details": {
      "lighting": "bright, natural daylight",
      "shot_type": "medium-close-up",
      "focus": "sharp on subject, slightly blurred background"
    }
  },
  "aspect_ratio": "4:5"
}
```
---

### 39. 动物和植物的烟花提示

**作者**: [ルナ｜使えるAI案内人](https://x.com/ai_skillmaster/status/2013823872949166279)  **日期**: 2026-01-21  **语言**: ja

> 一个旨在生成将动物或植物描绘成正在发射的烟花的图像的提示。它支持指定颜色，并且可以通过文本输入（例如“rabbit”）或图像输入来触发。

![动物和植物的烟花提示](https://cms-assets.youmind.com/media/1769063235121_mzfid4_G990wJxbcAYxubw.jpg)

```
動物や植物などを花火として打ち上げられるプロンプトです🎆
（NanoBanana Proでの使用がおすすめです）

今回は{argument name="色数" default="4色"}で表現していますが、単色や複数の色を指定することができます🌈

画像の添付だけでなく、{argument name="対象" default="ウサギ"}などの文字での指示でも対応してくれます😊
```
---

### 40. Ana de Armas 复古赌场闪光照片（重复）

**作者**: [yusra.](https://x.com/chatgptpaglu/status/2013274752228503644)  **日期**: 2026-01-19  **语言**: en

> 一个结构化提示，用于生成 Ana de Armas 在复古赌场环境中穿着黑色迷你吊带裙和 Y2K 厚底凉鞋的全身图像。该提示模拟了“2000 年代早期数码傻瓜相机”的美学，具有刺眼的机载闪光灯、高对比度和极低角度。（重复 2013248633748050216）

![Ana de Armas 复古赌场闪光照片（重复）](https://cms-assets.youmind.com/media/1768890658106_kfh3fx_G_CWtMcXwAEmy74.jpg)
![Ana de Armas 复古赌场闪光照片（重复）](https://cms-assets.youmind.com/media/1768890658356_5ppezb_G_CWtMcXgAEia0i.jpg)

```
{
  "image_generation_request": {
    "meta_settings": {
      "aspect_ratio": "9:16",
      "model_version": "v6.0",
      "stylize_value": 250,
      "quality": "High"
    },
    "subject_definition": {
      "identity_source": {
        "method": "Image Reference",
        "instruction": "Strictly preserve facial features and hair from the uploaded reference image."
      },
      "body_language": {
        "pose": "Seated on a high stool, body angled 30 degrees to the left, legs elegantly crossed at the knee to elongate the silhouette.",
        "hands": "Resting casually on the upper thighs, fingers relaxed, showcasing rings.",
        "gaze": "Looking slightly down towards the camera lens or directly into the flash."
      }
    },
    "fashion_and_styling": {
      "garment_main": {
        "item": "Black mini slip dress",
        "fabric": "Satin or high-sheen silk blend",
        "fit": "Skin-tight, fitted bodycon silhouette",
        "details": [
          "Spaghetti straps made of glittering rhinestones",
          "Deep scoop neckline",
          "Mini hemline exposing legs"
        ]
      },
      "footwear": {
        "item": "Platform sandals",
        "style": "Chunky block heel, 1990s/Y2K inspired",
        "material": "Black patent leather or satin",
        "details": "Silver buckle ankle strap, open toe"
      },
      "jewelry": {
        "ears": "Oversized sterling silver hoop earrings",
        "hands": "Multiple delicate silver stacking rings"
      }
    },
    "environmental_context": {
      "location": "Vintage Casino Floor",
      "flooring": {
        "type": "Patterned carpeting",
        "texture": "Worn nylon",
        "design": "Psychedelic swirls in teal, burnt orange, and royal blue",
        "vibe": "Retro Las Vegas aesthetic"
      },
      "furniture": {
        "item": "Casino bar stool",
        "material": "Tufted red faux leather seat",
        "base": "Tarnished bronze or gold metal pedestal with footrest"
      },
      "props_and_background": {
        "primary_prop": "Slot machine",
        "prop_details": "Illuminated marquee reading 'TRIPLE JACKPOT GEMS', glowing buttons, glass screen reflections",
        "atmosphere": "Smoky, crowded, dimly lit background with bokeh lights from other machines"
      }
    },
    "photography_technical": {
      "camera_simulation": "Early 2000s Digital Compact Camera (e.g., Sony Cybershot or Canon PowerShot)",
      "lighting_style": {
        "type": "Direct On-Camera Flash",
        "characteristics": [
          "Harsh shadows directly behind the subject",
          "High contrast",
          "Overexposed specular highlights on skin and fabric",
          "Vignetted corners"
        ]
      },
      "composition": {
        "angle": "Extreme low angle (Worm's-eye view)",
        "focus": "Sharp focus on subject, slight blur on background",
        "framing": "Full body shot emphasi"
      }
    }
  }
}
```
---

### 41. Ana de Armas 复古赌场闪光照片

**作者**: [Yaseen Khan Gul](https://x.com/YaseenK7212/status/2013248633748050216)  **日期**: 2026-01-19  **语言**: en

> 一个结构化的提示，用于生成安娜·德·阿玛斯 (Ana de Armas) 在复古赌场环境中全身图像。它指定了黑色迷你吊带裙、Y2K 厚底凉鞋，并使用了模拟的“2000 年代早期数码傻瓜相机”美学，具有刺眼的机载闪光灯、高对比度和极低的拍摄角度。

![Ana de Armas 复古赌场闪光照片](https://cms-assets.youmind.com/media/1768890655838_kaurc4_G_B-7jXWgAEGHsZ.jpg)
![Ana de Armas 复古赌场闪光照片](https://cms-assets.youmind.com/media/1768890655858_ty2rwl_G_B-7jaXIAAZARS.jpg)
![Ana de Armas 复古赌场闪光照片](https://cms-assets.youmind.com/media/1768890655871_avs4ba_G_B-7jXWoAEtJtL.jpg)

```
{
  "image_generation_request": {
    "meta_settings": {
      "aspect_ratio": "9:16",
      "model_version": "v6.0",
      "stylize_value": 250,
      "quality": "High"
    },
    "subject_definition": {
      "identity_source": {
        "method": "Image Reference",
        "instruction": "Strictly preserve facial features and hair from the uploaded reference image."
      },
      "body_language": {
        "pose": "Seated on a high stool, body angled 30 degrees to the left, legs elegantly crossed at the knee to elongate the silhouette.",
        "hands": "Resting casually on the upper thighs, fingers relaxed, showcasing rings.",
        "gaze": "Looking slightly down towards the camera lens or directly into the flash."
      }
    },
    "fashion_and_styling": {
      "garment_main": {
        "item": "Black mini slip dress",
        "fabric": "Satin or high-sheen silk blend",
        "fit": "Skin-tight, fitted bodycon silhouette",
        "details": [
          "Spaghetti straps made of glittering rhinestones",
          "Deep scoop neckline",
          "Mini hemline exposing legs"
        ]
      },
      "footwear": {
        "item": "Platform sandals",
        "style": "Chunky block heel, 1990s/Y2K inspired",
        "material": "Black patent leather or satin",
        "details": "Silver buckle ankle strap, open toe"
      },
      "jewelry": {
        "ears": "Oversized sterling silver hoop earrings",
        "hands": "Multiple delicate silver stacking rings"
      }
    },
    "environmental_context": {
      "location": "Vintage Casino Floor",
      "flooring": {
        "type": "Patterned carpeting",
        "texture": "Worn nylon",
        "design": "Psychedelic swirls in teal, burnt orange, and royal blue",
        "vibe": "Retro Las Vegas aesthetic"
      },
      "furniture": {
        "item": "Casino bar stool",
        "material": "Tufted red faux leather seat",
        "base": "Tarnished bronze or gold metal pedestal with footrest"
      },
      "props_and_background": {
        "primary_prop": "Slot machine",
        "prop_details": "Illuminated marquee reading 'TRIPLE JACKPOT GEMS', glowing buttons, glass screen reflections",
        "atmosphere": "Smoky, crowded, dimly lit background with bokeh lights from other machines"
      }
    },
    "photography_technical": {
      "camera_simulation": "Early 2000s Digital Compact Camera (e.g., Sony Cybershot or Canon PowerShot)",
      "lighting_style": {
        "type": "Direct On-Camera Flash",
        "characteristics": [
          "Harsh shadows directly behind the subject",
          "High contrast",
          "Overexposed specular highlights on skin and fabric",
          "Vignetted corners"
        ]
      },
      "composition": {
        "angle": "Extreme low angle (Worm's-eye view)",
        "focus": "Sharp focus on subject, slight blur on background",
        "framing": "Full body shot emphasi"
      }
    }
  }
}
```
---

### 42. 硬闪光摄影快照，姿态不羁

**作者**: [brindley](https://x.com/brindleyai/status/2012806512582840763)  **日期**: 2026-01-18  **语言**: en

> 一个详细的 JSON 提示，用于生成一张具有“闪光灯摄影快照”美学的中景图像。它描述了一位年轻女子躺在褶皱的缎面床上，身穿黄色比基尼上衣和蓝色运动裤，对着镜头做出挑衅性的竖中指姿势。该提示强调了相机闪光灯特有的刺眼、高对比度照明。

![硬闪光摄影快照，姿态不羁](https://cms-assets.youmind.com/media/1768804253219_gf3wvs_G-7s1nxXIAEihNW.jpg)

```
{
  "image_type": "flash_photography_snapshot",
  "aspect_ratio": "3:4",
  "subject": {
    "demographics": "Young female, tan complexion, fit physique",
    "hair": "Long, loose, wavy dirty blonde with lighter highlights, falling over shoulders and pillow",
    "expression": "Direct eye contact, neutral to slightly defiant gaze, lips relaxed",
    "makeup": "Defined eyebrows, eyeliner, neutral lip gloss, slight sheen on face"
  },
  "attire": {
    "top": "Yellow triangle bikini top, black text 'Trapstar' printed across cups, string ties",
    "bottom": "Royal blue sweatpants, thick waistband with drawstrings, yellow script text 'World' visible on left thigh",
    "fit": "Casual, relaxed fit on pants, fitted bikini top"
  },
  "accessories": {
    "jewelry": [
      "Large gold wristwatch on left wrist",
      "Gold screw-head bangle bracelet on left wrist",
      "Two layered gold necklaces with cross pendants (one small, one large/ornate)",
      "Large thin gold hoop earrings"
    ],
    "nails": "Long, square-shaped acrylics with classic white French tips"
  },
  "pose": {
    "body_position": "Lying supine on a bed, angled slightly towards the right",
    "left_arm": "Raised, elbow bent, hand resting loosely on forehead/hairline, palm facing outward",
    "right_arm": "Extended forward towards camera lens, hand displaying {argument name="hand gesture" default="middle finger gesture clearly"}",
    "torso": "Relaxed, slight natural skin folding at neck and armpit, gravity affecting chest tissue"
  },
  "environment": {
    "location": "Bedroom",
    "surface": "White satin or silk bed sheets, highly wrinkled and reflective, messy texture",
    "background": "Grey velvet tufted headboard, vertical paneling detail, soft texture"
  },
  "lighting_and_atmosphere": {
    "type": "Direct on-camera flash / Hard artificial light",
    "quality": "High contrast, harsh shadows behind subject and arm, specular highlights on skin and satin fabric",
    "shadows": "Sharp, distinct drop shadow on headboard from raised arm",
    "color_palette": "Cool white (sheets), warm tan (skin), vibrant yellow, cobalt blue, muted grey"
  },
  "camera_technical": {
    "framing": "Medium shot, captured from slightly above looking down",
    "focus": "Sharp focus on face and torso, slight depth of field falloff towards legs",
    "aesthetic": "Snapshot aesthetic, social media style, candid, unpolished composition"
  }
}
```
---

### 43. 独立电影美学叙事网格提示

**作者**: [Harboriis](https://x.com/harboriis/status/2012778831330099383)  **日期**: 2026-01-18  **语言**: en

> 一个复杂、结构化的 JSON 提示词，旨在生成一个具有实验性独立电影美学的 5 图叙事网格。它聚焦于一个年轻男子在废弃公交车站的宁静、怀旧时刻，强调原始的现实主义、低对比度和不完美的构图，以模拟一个被回忆起的场景。

![独立电影美学叙事网格提示](https://cms-assets.youmind.com/media/1768804207523_ob7epm_G-7TrcpWYAAxxO1.jpg)

```
{
  "concept": "a quiet moment that feels remembered rather than photographed",
  "subject": {
    "type": "young man",
    "age": "early 20s",
    "presence": "subtle, almost unnoticed within the frame",
    "expression": "emotion held back, eyes suggesting unfinished thoughts",
    "skin_tone": "natural muted tone with real-life unevenness",
    "features": "unposed face, relaxed posture, human imperfections preserved"
  },
  "scene": {
    "environment": "abandoned outdoor bus stop near a dried riverbed",
    "location": "cracked concrete shelter, faded signage, tall wild grass reclaiming the area",
    "props": "old bench, weathered backpack, torn paper timetable",
    "time_of_day": "late evening just before blue hour fades",
    "weather": "still air, faint dust particles floating"
  },
  "composition": {
    "style": "5-image narrative grid, non-linear storytelling",
    "shots": [
      "extreme close-up of fingers resting on the bench, shallow focus",
      "reflection of the subject in a scratched metal surface, face partially distorted",
      "medium shot from behind, subject seated and slightly slouched",
      "side profile framed through tall grass in the foreground",
      "wide static shot where the subject appears small, almost dissolving into space"
    ],
    "camera_angles": "observational, imperfect, slightly off-center",
    "framing": "intentional imbalance, negative space dominating the frame"
  },
  "lighting": {
    "type": "natural residual daylight",
    "quality": "soft, fading, low-energy light",
    "color_temperature": "cool desaturated blues with hints of warm decay",
    "shadows": "subtle, undefined, realistic"
  },
  "visual_style": {
    "mood": "nostalgic, suspended, emotionally restrained",
    "color_grading": "washed-out tones with gentle color separation",
    "contrast": "very low, almost flat",
    "film_look": "experimental indie film / memory archive aesthetic",
    "realism": "raw, anti-gloss, intentionally imperfect"
  },
  "camera_settings": {
    "lens": "40mm–58mm documentary-style lens",
    "depth_of_field": "selective focus, occasionally soft",
    "focus": "priority on atmosphere over sharpness"
  },
  "quality": {
    "resolution": "4K",
    "detail": "natural textures, visible wear, realistic surfaces",
    "noise": "organic grain resembling scanned film",
    "artifacts": "none, no AI distortions"
  }
}
```
---

### 44. 电影般的纯粹喜悦飞溅提示

**作者**: [Adam也叫吉米](https://x.com/Adam38363368936/status/2012743558818877710)  **日期**: 2026-01-18  **语言**: zh

> 一个多功能提示模板，旨在生成捕捉纯粹喜悦的电影画面，特别聚焦于一个主体在水中嬉戏，伴随着日落逆光，并凝固住半空中的水滴。该提示允许用户插入他们想要的主体，同时保持电影风格。

![电影般的纯粹喜悦飞溅提示](https://cms-assets.youmind.com/media/1768804332625_8q6qiz_G-6zluJXsAA_C3l.jpg)
![电影般的纯粹喜悦飞溅提示](https://cms-assets.youmind.com/media/1768804332443_6i8jky_G-6zluMW8AA67AK.jpg)
![电影般的纯粹喜悦飞溅提示](https://cms-assets.youmind.com/media/1768804334469_sw3s60_G-6zluIXAAAGHxO.jpg)
![电影般的纯粹喜悦飞溅提示](https://cms-assets.youmind.com/media/1768804334526_257tkb_G-6zluGWEAAxUW2.jpg)

```
Cinematic Frames, Pure Joy       
{argument name="subject" default="[SUBJECT]"} splashing in {argument name="water type" default="[water]"}, sunset backlight, droplets frozen mid-air, pure joy.   

中文版提示词也是一样的：

电影般的画面，纯粹的喜悦
[参考图中的主体（面部、衣着特征不发生任何变化）]在夕阳的映照下，水花飞溅，水滴在半空中凝固，纯粹的快乐。
```
---

### 45. 自定义 GPT 提示：分析图像并为 Nano Banana Pro 生成 JSON 提示

**作者**: [タナベ | 動画・音声生成AI解説](https://x.com/tanabe_fragm/status/2011596853234770340)  **日期**: 2026-01-15  **语言**: en

> 这是一套使用自定义 GPT 的说明，旨在分析上传的图像并生成针对 Nano Banana Pro 优化的详细 JSON 提示。此工作流程有助于逆向工程或将现有图像的风格迁移到 Nano Banana Pro 环境中。

![自定义 GPT 提示：分析图像并为 Nano Banana Pro 生成 JSON 提示](https://cms-assets.youmind.com/media/1768544881885_mc8zt9_G-qgme2bUAApobP.jpg)

```
Analyze this image in exhaustive JSON detail
```
---

### 46. Image-to-Image 姿态锁定和身份保留，适用于抹茶美学

**作者**: [Melis✨](https://x.com/miilesus/status/2011511617163501893)  **日期**: 2026-01-14  **语言**: en

> 一个高度限制性的 JSON 提示，专为图像到图像生成而设计，要求参考姿势（侧身、交叉双腿、手部姿势）实现精确的 1:1 视觉匹配，同时将调色板调整为抹茶绿色美学。它使用严格的身份和姿势锁定约束，确保只改变面部身份和颜色，同时不允许出现特定的服装物品，如裤子或鞋子。

```
{
  "task_type": "image_generation_with_absolute_pose_lock",
  "edit_goal": "Generate an image that is an exact 1:1 visual match of the reference pose. Side-facing orientation, leg crossing, hand grip, and accessories must be identical. Only face identity and matcha color adaptation are allowed.",
  "global_locks": {
    "pose_lock": true,
    "side_orientation_lock": true,
    "leg_position_lock": true,
    "hand_grip_lock": true,
    "accessory_lock": true,
    "camera_lock": true,
    "allow_any_variation": false
  },
  "pose_definition": {
    "body_orientation": "Strict side-facing seated pose, not front-facing",
    "seating": "Sitting fully on a wooden bench, body turned sideways",
    "legs": {
      "crossing": "Legs crossed at the knee exactly as reference",
      "top_leg": "Angled forward and slightly upward",
      "bottom_leg": "Angled downward, resting naturally"
    },
    "leg_wear": {
      "type": "Sheer pantyhose",
      "color": "{argument name="tights color" default="matcha green"}",
      "opacity": "semi-sheer",
      "must_be_visible": true
    },
    "arms": {
      "primary_arm": {
        "position": "Bent at elbow",
        "height": "Chest level",
        "hand_action": "Holding a cup",
        "grip_style": "Side grip"
      },
      "secondary_arm": {
        "position": "Resting across the torso under the coat"
      }
    },
    "head": {
      "direction": "Facing sideways",
      "tilt": "Minimal"
    }
  },
  "appearance_constraints": {
    "visible_clothing_only": [
      "long fur coat",
      "matcha green tights"
    ],
    "fur_coat": {
      "style": "Luxury long faux fur",
      "color": "{argument name="coat color" default="matcha green"}"
    },
    "accessories": {
      "sunglasses": {
        "required": true,
        "style": "Dark fashion sunglasses",
        "position": "Worn on face"
      }
    },
    "disallowed_items": [
      "pants",
      "leggings",
      "dress",
      "skirt",
      "black tights",
      "brown tights",
      "shoes"
    ]
  },
  "object_constraints": {
    "drink": {
      "type": "Matcha",
      "cup": "Plain white takeaway cup",
      "position": "Held at chest level"
    }
  },
  "environment_constraints": {
    "location": "Elegant cafe exterior",
    "background": "Dark cafe facade with large glass doors",
    "bench": "Wooden bench",
    "lighting": "Natural daylight",
    "allow_change": false
  },
  "source_images": [
    {
      "id": "FACE_IMAGE",
      "role": "face_identity_reference"
    }
  ],
  "face_settings": {
    "identity_strength": 0.95,
    "expression_match": true,
    "skin_texture": "natural",
    "no_stylization": true
  },
  "negative_prompt": [
    "front facing",
    "looking at camera",
    "standing",
    "different leg position",
    "uncrossed legs",
    "missing sunglasses",
    "black tights",
    "brown tights",
    "pants visible",
    "shoes visible",
    "wrong hand grip",
    "cup held"
  ]
}
```
---

### 47. 高山之巅的人物与云中文字

**作者**: [BeautyVerse](https://x.com/BeautyVerse_Lab/status/2011289215712256125)  **日期**: 2026-01-14  **语言**: en

> 一个结构化的 JSON 提示词，旨在将一个角色（通过参考图像严格锁定身份）放置在高峰山顶。该提示词使用极高的俯视广角视图，并指定背景云应形成可自定义的文本，从而营造出戏剧性、风格化的效果。

![高山之巅的人物与云中文字](https://cms-assets.youmind.com/media/1768468600752_4s6cmc_G-mI35HbQAIo7np.jpg)
![高山之巅的人物与云中文字](https://cms-assets.youmind.com/media/1768468600812_e7psdl_G-mI35IasAAY8EQ.jpg)

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
    "lighting": "bright_natural_daylight_with_soft_clouds_b"
  },
  "text_in_clouds": "{argument name="cloud text" default="YOUR TEXT HERE"}"
}
```
---

### 48. 极端仰视红毯提示（梅根·福克斯）

**作者**: [jennieee:3](https://x.com/jenniebae_ai/status/2011192464632406345)  **日期**: 2026-01-13  **语言**: en

> 一个高度具体、结构化的提示，用于生成一张梅根·福克斯 (Megan Fox) 在红毯上的图像，采用极端的虫眼视角。该提示详细说明了摄像机角度、强制透视、特定的深红色礼服，以及背景上需要有自定义标志（“KeorUnreal”和“jenniebae_ai”）的要求。

![极端仰视红毯提示（梅根·福克斯）](https://cms-assets.youmind.com/media/1768466919499_qq9jsi_G-kwom4bQAUN0dN.jpg)
![极端仰视红毯提示（梅根·福克斯）](https://cms-assets.youmind.com/media/1768466919661_ik9vrq_G-kwom8bQAMx2vZ.jpg)
![极端仰视红毯提示（梅根·福克斯）](https://cms-assets.youmind.com/media/1768466920537_8ob74b_G-kw31ebQAEva-c.jpg)

```
{
  "technical_specifications": {
    "camera_angle": "Extreme Worm's Eye View (Low Angle)",
    "camera_position": "Placed at ground level, inches from the subject's feet, shooting vertically upwards.",
    "lens_type": "Wide-angle (approx. 20mm-24mm)",
    "visual_effect": "Forced perspective causing dramatic elongation of the legs and a towering, dominant subject presence.",
    "aspect_ratio": "9:16"
  },
  "subject_details": {
    "identity": "{argument name="celebrity name" default="Megan Fox"}",
    "hair": "Long, dark, loose waves, parted on the side.",
    "apparel": {
      "garment": "{argument name="garment color" default="Crimson red"} satin gown with a corset-style bodice.",
      "details": "Rhinestone/crystal trim on the bust cups and off-the-shoulder straps. High thigh-high slit on the left side.",
      "legwear": "Nude fishnet stockings visible through the slit.",
      "footwear": "Silver rhinestone open-toe heels (partially visible)."
    },
    "accessories": "Diamond choker tennis necklace.",
    "expression": "Sultry, confident, looking down toward the camera lens."
  },
  "environment_and_background": {
    "setting": "Event 'Step and Repeat' press wall.",
    "floor": "Black plush event carpet.",
    "backdrop_color": "Matte black.",
    "text_content": {
      "primary_text": "KeorUnreal",
      "secondary_text": "jenniebae_ai",
      "distribution": "Logos must appear in equal counts (50/50 split), arranged in an alternating repeating pattern across the wall behind the subject."
    }
  },
  "lighting_style": {
    "type": "Flash photography / Event lighting.",
    "characteristics": "Sharp focus, high contrast, specular highlights on the satin fabric and jewelry."
  }
}
```
---

### 49. 怀旧记忆叙事网格提示

**作者**: [Duet | AI](https://x.com/Sheldon056/status/2010550490321596767)  **日期**: 2026-01-12  **语言**: en

> 一个复杂的多镜头提示，旨在生成一个具有实验性独立电影美学的 5 图叙事网格，重点描绘一个年轻男子在傍晚时分身处废弃公交车站的场景。该提示强调低对比度、去饱和色彩、刻意的不完美以及注重氛围而非锐度，以唤起一种记忆感和情感克制。

![怀旧记忆叙事网格提示](https://cms-assets.youmind.com/media/1768319212720_ynv3sq_G-bpAQIaEAA8ZZM.jpg)

```
{
  "concept": "a quiet moment that feels remembered rather than photographed",
  "subject": {
    "type": "young man",
    "age": "early 20s",
    "presence": "subtle, almost unnoticed within the frame",
    "expression": "emotion held back, eyes suggesting unfinished thoughts",
    "skin_tone": "natural muted tone with real-life unevenness",
    "features": "unposed face, relaxed posture, human imperfections preserved"
  },
  "scene": {
    "environment": "abandoned outdoor bus stop near a dried riverbed",
    "location": "cracked concrete shelter, faded signage, tall wild grass reclaiming the area",
    "props": "old bench, weathered backpack, torn paper timetable",
    "time_of_day": "late evening just before blue hour fades",
    "weather": "still air, faint dust particles floating"
  },
  "composition": {
    "style": "5-image narrative grid, non-linear storytelling",
    "shots": [
      "extreme close-up of fingers resting on the bench, shallow focus",
      "reflection of the subject in a scratched metal surface, face partially distorted",
      "medium shot from behind, subject seated and slightly slouched",
      "side profile framed through tall grass in the foreground",
      "wide static shot where the subject appears small, almost dissolving into space"
    ],
    "camera_angles": "observational, imperfect, slightly off-center",
    "framing": "intentional imbalance, negative space dominating the frame"
  },
  "lighting": {
    "type": "natural residual daylight",
    "quality": "soft, fading, low-energy light",
    "color_temperature": "cool desaturated blues with hints of warm decay",
    "shadows": "subtle, undefined, realistic"
  },
  "visual_style": {
    "mood": "nostalgic, suspended, emotionally restrained",
    "color_grading": "washed-out tones with gentle color separation",
    "contrast": "very low, almost flat",
    "film_look": "experimental indie film / memory archive aesthetic",
    "realism": "raw, anti-gloss, intentionally imperfect"
  },
  "camera_settings": {
    "lens": "40mm–58mm documentary-style lens",
    "depth_of_field": "selective focus, occasionally soft",
    "focus": "priority on atmosphere over sharpness"
  },
  "quality": {
    "resolution": "4K",
    "detail": "natural textures, visible wear, realistic surfaces",
    "noise": "organic grain resembling scanned film",
    "artifacts": "none, no AI distortions"
  }
}
```
---

### 50. 生成立方体卫星图像

**作者**: [Shima](https://x.com/shima15821/status/2010227123366330566)  **日期**: 2026-01-11  **语言**: ja

> 一个用于 Nano Banana Pro 的简单提示，可生成 Cubesat 卫星的图像。这展示了 Nano Banana Pro 如何轻松地为各种目的创建引人注目的图像，并识别特定的技术术语。

![生成立方体卫星图像](https://cms-assets.youmind.com/media/1768226107733_7a276r_G-XCUp5asAEZpjw.jpg)

```
{argument name="対象" default="キューブサット衛星"}
```
---

### 51. 超逼真热带海滩场景提示

**作者**: [KeorUnreal](https://x.com/KeorUnreal/status/2009370904242053564)  **日期**: 2026-01-08  **语言**: en

> 一个详细、结构化的提示，用于生成一张年轻女性在热带海滩上的超逼真图像，重点关注人物的外貌、服饰（花卉系带比基尼）、姿势、环境（巴厘岛海滩）以及 4k 分辨率和高对比度照明等技术规格。

![超逼真热带海滩场景提示](https://cms-assets.youmind.com/media/1767967527121_8a2bm4_G-K4LsDXUAAjM6d.jpg)

```
{
  "prompt_type": "photorealistic_image_generation",
  "subject": {
    "description": "Young woman with fair skinned tone.",
    "hair": "Long straight blonde hair extending past the waist, styled with a pink tropical flower tucked behind the left ear.",
    "expression": "Calm, relaxed expression, looking slightly off-camera."
  },
  "attire": {
    "type": "String bikini",
    "pattern": "White base with a vibrant floral print featuring red, yellow, and orange flowers with green leaves.",
    "details": "Triangle top and tie-side bottoms."
  },
  "pose": {
    "body_position": "Sitting on white sand, legs extended diagonally toward the bottom left, leaning back on left hand for support.",
    "hand_placement": "Right hand raised, gently touching the neck/shoulder area.",
    "orientation": "Full body visible, angled slightly toward the right."
  },
  "environment": {
    "location": "Tropical {argument name="location" default="bali beach"} with white sand and clear turquoise water.",
    "background": "Deep blue sky with faint clouds. Two distinct island peaks visible on the horizon line.",
    "details": "Gentle waves washing onto the shore. Distant figures of people swimming and walking on the beach."
  },
  "lighting_and_atmosphere": {
    "lighting": "Bright, direct natural sunlight creating high contrast and sharp shadows on the sand.",
    "mood": "Serene, vacation vibe, summery.",
    "color_palette": "Vibrant blues, warm sand tones, natural skin tones, bright floral colors."
  },
  "technical_specifications": {
    "quality": "4k, Ultra HD, high resolution, highly detailed texture.",
    "style": "Realistic photography, candid shot.",
    "focus": "Sharp focus on the subject with slightly softer background depth."
  }
}
```
---

### 52. Amigurumi 风格转换提示

**作者**: [ちゃろん](https://x.com/charon_artist/status/2008877235680510260)  **日期**: 2026-01-07  **语言**: ja

> 一个用于 Nano Banana Pro 的提示，可将图像转换为钩针玩偶（amigurumi）风格，强调纱线的温暖感和可爱、圆润的造型。该提示在图像的 ALT 文本中提供。

![Amigurumi 风格转换提示](https://cms-assets.youmind.com/media/1767966164053_hbq9xb_G-D2-MIaUAEakNb.jpg)

```
A cute, round, and fluffy amigurumi (crocheted stuffed toy) of a {argument name="subject" default="cat"}. The texture should clearly show the yarn and crochet stitches. Soft, warm lighting. Pastel colors. Close-up shot with shallow depth of field. High quality, detailed.
```
---

### 53. 超逼真后斜姿势复制提示

**作者**: [brindley](https://x.com/brindleyai/status/2006407832585781464)  **日期**: 2025-12-31  **语言**: en

> 一个极其详细、结构化的图像生成提示，专注于复制一个穿着黑色罗纹连体衣的年轻女性的特定、解剖学上复杂的姿势（极度脊柱前凸/骨盆前倾）。它详细说明了形态、服装、精确的姿势几何结构以及带有闪光美学的都市夜景照明，要求绝对的忠实度。

![超逼真后斜姿势复制提示](https://cms-assets.youmind.com/media/1767456170072_c9z2ru_G9gxSiqWYAArCmv.jpg)

```
{
  "meta": {
    "task": "exact_visual_replication",
    "version": "v3_ultra_pose_lock",
    "aspect_ratio": "3:4",
    "strictness_level": "absolute_fidelity"
  },
  "subject_morphology": {
    "demographics": "Young female",
    "hair": {
      "color": "Warm blonde",
      "style": "Shoulder-length lob, straight with slight texture",
      "behavior": "Falling naturally, slight gravity pull on ends, illuminated by artificial light"
    },
    "skin": {
      "tone": "Fair/Pale",
      "texture": "Natural smoothness with slight flash washout on face",
      "lighting_reaction": "Reflective sheen on cheekbones and nose"
    }
  },
  "apparel_and_textiles": {
    "garment": "Full-body tight jumpsuit / unitard",
    "color": "Deep black",
    "material": "Ribbed knit fabric",
    "fit": "Hyper-compressive, skin-tight, confirming exactly to anatomical curves",
    "texture_visibility": "Vertical ribbing visible where light catches curvature (buttocks, waist, arm)"
  },
  "pose_geometry_and_physics": {
    "overall_orientation": "Standing, rear-oblique angle (facing away from camera, twisted back)",
    "spine_curvature": {
      "lumbar": "Extreme lordosis (deep lower back arch)",
      "thoracic": "Rotational twist to subject's left",
      "cervical": "Head rotated approx 80 degrees left to look over shoulder"
    },
    "pelvic_state": {
      "tilt": "Aggressive anterior pelvic tilt",
      "rotation": "Square to the rear-diagonal axis",
      "visual_dominance": "Gluteal region visually magnified by perspective and tilt"
    },
    "limb_placement": {
      "left_arm": "Hanging straight down side, slight elbow flexion, hand relaxed near thigh",
      "right_arm": "Obscured by torso rotation, shoulder drop visible",
      "legs": "Standing straight, weight slightly biased to right leg, knees soft-locked"
    },
    "weight_distribution": "Gravity-centered on heels, posture actively held against gravity to maintain curve"
  },
  "camera_and_framing": {
    "angle": "Eye-level relative to subject's torso",
    "focal_length": "Medium-wide (smartphone camera aesthetic)",
    "composition": {
      "framing": "Subject centered horizontally, cropped at mid-thigh/knee",
      "foreground": "Palm tree trunk with lights on immediate right edge",
      "depth": "Deep perspective of street receding to left"
    }
  },
  "lighting_and_atmosphere": {
    "environment": "Urban luxury street at night (sidewalk)",
    "primary_source": "Mixed artificial street lighting",
    "key_light": "Frontal flash or bright signage illuminating face and hair (cool/neutral temp)",
    "ambient_light": "Warm yellow glow from string lights wrapped around palm trees",
    "shadows": "Soft drop shadows on ground, deep occlusion shadows in clothing folds",
    "bokeh": "Distant street lights and storefronts slightly out of focus"
  },
  "environmental_details": {
    "location": "Upscale shopping district sidewalk"
  }
}
```
---

### 54. 超强硬锁俯卧躺椅姿势复刻

**作者**: [Sienna](https://x.com/siennalovesai/status/2005671207018893317)  **日期**: 2025-12-29  **语言**: en

> 这是一个高度技术性的图像生成提示，使用“PX-LOCK-RECONSTRUCT”引擎进行精确的镜头复制。它对姿势、体型、服装、相机和光线设置了严格的硬锁定，详细描述了主体的解剖结构、表情和姿势（完全俯卧在泳池边的躺椅上），并给出了精确的测量值和角度。

![超强硬锁俯卧躺椅姿势复刻](https://cms-assets.youmind.com/media/1767166936501_raoyfp_G9WTUFpXAAED9i6.jpg)

```
{
  "engine": "PX-LOCK-RECONSTRUCT",
  "version": "2.0-ultra-hardlock",
  "mode": "exact-shot-replication",
  "global_hard_locks": {
    "pose_lock": true,
    "body_shape_lock": true,
    "outfit_lock": true,
    "camera_lock": true,
    "lighting_lock": true,
    "environment_lock": true,
    "water_state_lock": true,
    "color_palette_lock": true,
    "deviation_tolerance": {
      "joint_rotation_max_degrees": 2,
      "camera_shift_max_percent": 1,
      "scale_variance_max_percent": 1,
      "silhouette_iou_min": 0.94
    }
  },
  "subject": {
    "adult_confirmation": true,
    "age_estimate": "mid-to-late 20s",
    "ethnicity": "appears white",
    "skin_tone": "light neutral with warm sunlit highlights",
    "height_estimate_inches": 70,
    "body_type": "slim athletic with soft curves",
    "measurements_inches": {
      "bust": 32,
      "waist": 24,
      "hips": 34
    },
    "advanced_anatomy": {
      "bust_sagittal_depth_inches": 4.2,
      "waist_depth_inches": 2.4,
      "hip_depth_inches": 4.6,
      "ribcage_width_inches": 11.5,
      "pelvic_tilt_degrees": 10,
      "glute_projection_inches": 2.6,
      "silhouette_profile": "long, low-profile S-curve with minimal lumbar exaggeration"
    },
    "face": {
      "shape": "angular oval",
      "orientation": {
        "yaw_degrees": -6,
        "pitch_degrees": -3,
        "roll_degrees": 0
      },
      "eyes": {
        "shape": "almond",
        "color": "dark brown",
        "expression": "intense, neutral, direct"
      },
      "brows": "straight, defined",
      "nose": "straight bridge, narrow",
      "lips": {
        "shape": "medium-full",
        "expression": "closed, neutral"
      },
      "emotion_lock": "calm, confident, unsmiling"
    },
    "hair": {
      "color": "dark brown",
      "length": "long",
      "part": "center",
      "style": "natural, loose, slightly damp",
      "placement": "falling back over shoulders and upper back"
    }
  },
  "pose": {
    "base_pose": "prone lounge",
    "surface": "outdoor poolside lounger",
    "body_orientation": "fully horizontal",
    "pelvis": {
      "contact": "lounger",
      "rotation_degrees": 0,
      "height_offset_inches": 0
    },
    "torso": {
      "spine_curve": "neutral with slight extension",
      "chest_lift_inches": 2.5,
      "rotation_degrees": 0
    },
    "arms": {
      "both_arms": {
        "position": "extended forward",
        "support": "resting on lounger backrest",
        "elbow_angle_degrees": 165
      }
    },
    "head": {
      "support": "resting above forearms",
      "tilt_degrees": -3,
      "yaw_degrees": -6,
      "pitch_degrees": -3,
      "gaze": "directly toward camera"
    },
    "legs": {
      "both_legs": {
        "extension": "fully extended",
        "thigh_contact": "lounger",
        "feet": "out of frame"
      }
    },
    "absolute_pose_constraints": [
      "subject must be fully prone
```
---

### 55. 像素级完美身份互换

**作者**: [Sienna](https://x.com/siennalovesai/status/2005311983667556794)  **日期**: 2025-12-28  **语言**: en

> 这是一个极其专业的 JSON 提示词，旨在通过上传的主体图像实现近乎像素级的身份替换（身份互换）。它锁定了众多技术参数，包括相机高度、镜头焦距、光圈以及面部特征的特定像素坐标，确保新身份能精确地插入到参考图像的姿势和场景中。

![像素级完美身份互换](https://cms-assets.youmind.com/media/1767061719439_soa6ir_G9RMmCSWoAAkcdt.jpg)
![像素级完美身份互换](https://cms-assets.youmind.com/media/1767061719237_5z5jds_G9RMmCTXMAEH-iv.jpg)

```
{
  "metadata": {
    "engine_name": "PX-LOCK-X",
    "prompt_version": "pxlockx-1.0.0",
    "generation_goal": "Near pixel-perfect recreation with identity-only replacement",
    "reference_frame_policy": {
      "use_reference_as_ground_truth": true,
      "identity_swap_only": true,
      "no_creative_inference": true
    },
    "units": {
      "angles": "degrees",
      "lengths": "centimeters",
      "coords": "normalized_0_to_1",
      "temperature": "kelvin"
    }
  },

  "identity_replacement": {
    "mode": "identity_only",
    "reference_identity_source": "uploaded_subject_image",
    "replace": {
      "face_identity": true,
      "head_shape": true,
      "hair_color_and_length": true,
      "skin_tone": true,
      "body_identity": true
    },
    "preserve_from_reference": {
      "pose": true,
      "camera": true,
      "lighting": true,
      "environment": true,
      "wardrobe": true,
      "jewelry": true,
      "expression_valence": true,
      "framing_and_crop": true
    },
    "identity_strength": 1.0,
    "no_beautification": true,
    "no_style_transfer": true
  },

  "output_settings": {
    "aspect_ratio": "2:3",
    "resolution_target": "reference_matched",
    "render_style": "photorealistic",
    "color_space": "sRGB",
    "compression": "lossless",
    "dynamic_range": "natural",
    "white_balance_lock": true
  },

  "pixel_coordinates_lock": {
    "lock_enabled": true,
    "reference_frame_dimensions_px_estimate": {
      "width_px": 1024,
      "height_px": 1536
    },
    "crop_boundaries_px_norm": {
      "left_x_norm": 0.0,
      "right_x_norm": 1.0,
      "top_y_norm": 0.0,
      "bottom_y_norm": 1.0
    },
    "primary_subject_bounding_box_norm": {
      "x_min": 0.105,
      "y_min": 0.155,
      "x_max": 0.945,
      "y_max": 0.975
    },
    "head_bounding_box_norm": {
      "x_min": 0.205,
      "y_min": 0.175,
      "x_max": 0.625,
      "y_max": 0.360
    },
    "face_feature_anchors_norm": {
      "left_eye_center": { "x": 0.345, "y": 0.252 },
      "right_eye_center": { "x": 0.445, "y": 0.247 },
      "nose_tip": { "x": 0.405, "y": 0.287 },
      "mouth_center": { "x": 0.403, "y": 0.318 },
      "chin_point": { "x": 0.410, "y": 0.352 }
    }
  },

  "camera_lock": {
    "lock_enabled": true,
    "camera_height_cm": 105.0,
    "camera_to_subject_distance_cm": 230.0,
    "camera_orientation_degrees": {
      "yaw": 8.5,
      "pitch": -3.0,
      "roll": 0.6
    },
    "lens": {
      "focal_length_mm": 85.0,
      "sensor_format": "full_frame",
      "distortion_model": "brown_conrady",
      "distortion_coefficients": { "k1": -0.012, "k2": 0.004 }
    },
    "aperture": {
      "f_number": 2.2,
      "focus_distance_cm": 220.0,
      "focus_target": "face_plane"
    },
    "exposure": {
      "iso": 200,
      "shutter_s": 0.002,
      "exposure_comp_ev": 0.0
    }
  },

  "pose_lock": {
    "lock_enabled": true,
    "pose_type": "deep_squat_crouch",
    "body_facin
```
---

### 56. Office Siren 美学与 Y2K 闪光摄影

**作者**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211/status/2005008640319897812)  **日期**: 2025-12-27  **语言**: en

> 一个详细、结构化的提示，用于生成一张超写实图像：一位年轻女性，身着“办公室女郎”风格，以强烈的、高对比度的闪光美学拍摄，让人联想到 2000 年代初期的数码相机。该提示详细说明了拍摄对象的样貌、服装（红色针织上衣、棕色紧身胸衣、红色短裤）、在办公桌上的姿势、环境以及精确的相机设置，以呈现特定的复古数码效果。

![Office Siren 美学与 Y2K 闪光摄影](https://cms-assets.youmind.com/media/1766987727988_dm1grv_G9M4oQ2akAAyOH0.jpg)

```
{
  "subject": {
    "description": "Young woman with blonde hair tied back in a messy ponytail with loose strands framing the face.",
    "appearance": "Fair skin, wearing rectangular black-rimmed eyeglasses. She is looking over the glasses directly at the viewer.",
    "pose": "Sitting on top of a light wooden office desk/cabinet. Leaning back on one straight arm, legs bent and angled to the side. The other hand is raised, touching the rim of her glasses.",
    "clothing": {
      "top": "{argument name=\"top color and style\" default=\"Red textured short-sleeve knit top with a light blue Peter Pan collar with white lace trim.\"}",
      "waist": "Wide brown corset-style waist cincher or cummerbund.",
      "bottoms": "Red fitted shorts or briefs.",
      "footwear": "Sheer pantyhose (implied by leg texture/tone), shoes not fully visible but appear to be heels."
    },
    "expression": "Confident, slightly inquisitive 'office siren' look."
  },
  "environment": {
    "setting": "Dimly lit office space.",
    "background": "Large window with closed silver horizontal blinds. Reflections of the flash are visible on the glass/blinds.",
    "props": "A stack of white papers or scripts resting on the desk edge near her supporting hand.",
    "surfaces": "Light beige wooden veneer desk/cabinet."
  },
  "lighting": {
    "type": "Direct on-camera flash.",
    "quality": "Harsh, high-contrast lighting typical of snapshot photography. Creates a hard shadow of the subject against the blinds and wall.",
    "mood": "Candid, '2000s digital camera' aesthetic, late-night work atmosphere."
  },
  "camera_details": {
    "style": "Ultra Photorealistic, Snapshot aesthetic.",
    "camera": "Canon PowerShot G7 or similar early 2000s digicam.",
    "lens": "35mm equivalent.",
    "aperture": "f/4.0",
    "shutter": "1/60",
    "iso": "400",
    "focus": "Sharp focus on the subject's face and glasses."
  },
  "style_tags": [
    "Office Siren",
    "Flash Photography",
    "Y2K Aesthetic",
    "Retro Digital",
    "High Detail",
    "8k",
    "Realistic Texture"
  ]
}
```
---

### 57. Y2K 办公室海妖快照美学提示

**作者**: [Lex](https://x.com/lexx_aura/status/2004940479759053260)  **日期**: 2025-12-27  **语言**: en

> 一个详细的 JSON 提示，用于 Gemini Nano Banana Pro 生成一张具有 Y2K 数码相机美学的超写实图像，画面中一位年轻女性身着“办公室女妖”风格的服装坐在办公桌上，被刺眼、高对比度的机顶闪光灯照亮。

![Y2K 办公室海妖快照美学提示](https://cms-assets.youmind.com/media/1766987708807_xlk6xw_G9L6ulLXgAEgky9.jpg)

```
{
  "subject": {
    "description": "Young woman with blonde hair tied back in a messy ponytail with loose strands framing the face.",
    "appearance": "Fair skin, wearing rectangular black-rimmed eyeglasses. She is looking over the glasses directly at the viewer.",
    "pose": "Sitting on top of a light wooden office desk/cabinet. Leaning back on one straight arm, legs bent and angled to the side. The other hand is raised, touching the rim of her glasses.",
    "clothing": {
      "top": "Black textured short-sleeve knit top with a light blue Peter Pan collar with white lace trim.",
      "waist": "Wide brown corset-style waist cincher or cummerbund.",
      "bottoms": "Black fitted shorts or briefs.",
      "footwear": "Sheer pantyhose (implied by leg texture/tone), shoes not fully visible but appear to be heels."
    },
    "expression": "Confident, slightly inquisitive 'office siren' look."
  },
  "environment": {
    "setting": "Dimly lit office space.",
    "background": "Large window with closed silver horizontal blinds. Reflections of the flash are visible on the glass/blinds.",
    "props": "A stack of white papers or scripts resting on the desk edge near her supporting hand.",
    "surfaces": "Light beige wooden veneer desk/cabinet."
  },
  "lighting": {
    "type": "Direct on-camera flash.",
    "quality": "Harsh, high-contrast lighting typical of snapshot photography. Creates a hard shadow of the subject against the blinds and wall.",
    "mood": "Candid, '2000s digital camera' aesthetic, late-night work atmosphere."
  },
  "camera_details": {
    "style": "Ultra Photorealistic, Snapshot aesthetic.",
    "camera": "Canon PowerShot G7 or similar early 2000s digicam.",
    "lens": "35mm equivalent.",
    "aperture": "f/4.0",
    "shutter": "1/60",
    "iso": "400",
    "focus": "Sharp focus on the subject's face and glasses."
  },
  "style_tags": [
    "Office Siren",
    "Flash Photography",
    "Y2K Aesthetic",
    "Retro Digital",
    "High Detail",
    "8k",
    "Realistic Texture"
  ]
}
```
---

### 58. 末日幸存者电影级写实风格

**作者**: [Maercih](https://x.com/Maercihh/status/2004880290729394668)  **日期**: 2025-12-27  **语言**: en

> 为 Nano Banana Pro 生成的结构化提示，用于创作一张电影级、超细节的蒙面幸存者在燃烧战场上的图像。重点在于末日背景下的强烈氛围、刺眼光线和粗粝质感。

![末日幸存者电影级写实风格](https://cms-assets.youmind.com/media/1766987788929_dgpj7y_G9LD8z8bgAAfbbc.jpg)

```
{
  "model": "Nano Banana Pro",
  "subject": "Masked survivor wearing a gas mask and tactical clothing",
  "scene": "Burning battlefield surrounded by flames and smoke",
  "pose": "Crouched low, gripping a metal crowbar",
  "environment": {
    "weather": "Ash-filled air, drifting embers",
    "lighting": "Harsh firelight with deep shadows",
    "ground": "Scorched earth and debris"
  },
  "mood": "Intense, dangerous, post-apocalyptic",
  "style": "Cinematic realism",
  "camera": "Low-angle close shot, dramatic depth of field",
  "details": "Fire sparks, soot-covered fabric, reflections in gas mask lenses",
  "quality": "Ultra-detailed, high contrast, gritty texture"
}
```
---

### 59. 21 世纪初台球室的数字美学

**作者**: [Javeriya ✨](https://x.com/JadoonKhan281/status/2004768137687040150)  **日期**: 2025-12-27  **语言**: en

> 一个旨在生成具有 2000 年代初期数字美学、高对比度和强烈直射闪光图像的提示。主体是一名年轻女子，身穿炭灰色紧身衣，躺在木镶板台球室里一张鲜艳的橙色台球桌上，强调颗粒感、抓拍质感和高角度拍摄。

![21 世纪初台球室的数字美学](https://cms-assets.youmind.com/media/1766987739593_umipy9_G9Jd_NgaIAAqRzi.jpg)

```
{
  "image_metadata": {
    "subject": {
      "identity": "Young woman",
      "hair": {
        "color": "Dark brown",
        "style": "Long, straight, sleek"
      },
      "physique": "Fit, hourglass",
      "pose": {
        "description": "Lying back on pool table",
        "posture": "Arched back, head thrown back",
        "alignment": "Diagonal"
      }
    },
    "attire": {
      "type": "Bodysuit",
      "color": "{argument name=\"bodysuit color\" default=\"Charcoal grey\"}",
      "features": [
        "Front zipper",
        "Corset-style piping",
        "Short sleeves"
      ],
      "accessories": [
        "Silver bracelet"
      ]
    },
    "environment": {
      "setting": "Billiard room",
      "lighting": "Hard direct flash, high contrast",
      "table_details": {
        "felt_color": "{argument name=\"felt color\" default=\"Vibrant orange\"}",
        "props": [
          "Wooden pool cue",
          "Black 8-ball",
          "Striped ball",
          "Solid orange ball"
        ]
      },
      "background": {
        "walls": "Wood paneling",
        "decor": "Wall-mounted ball rack"
      }
    },
    "technical_style": {
      "aesthetic": "Early 2000s digital",
      "camera_angle": "High angle",
      "texture": "Grainy, candid"
    }
  }
}
```
---

### 60. 金色时段网球场比基尼抓拍

**作者**: [Retvi](https://x.com/retvikurmi/status/2003485606970868197)  **日期**: 2025-12-23  **语言**: en

> 一张写实、抓拍的社交媒体风格图片，详细且结构化的提示词。主体是一位身穿粉白扎染比基尼的女性，跪在绿色网球场上，在黄金时段将双手搭在网球拍柄上，强调自然的皮肤纹理和硬朗的阴影。

![金色时段网球场比基尼抓拍](https://cms-assets.youmind.com/media/1766673237618_d8sd0a_G83PikvasAA7PH8.jpg)

```
{
  "image_prompt_structure": {
    "subject": {
      "demographics": "Young woman, roughly 20-25 years old, Caucasian",
      "body_type": "Fit, athletic, slender build, visible abdominal definition",
      "skin": {
        "tone": "Fair to light tan, sun-kissed",
        "texture": "Natural skin texture, visible pores, slight sheen from sunlight, realistic skin shading",
        "details": "Soft natural highlights on shoulders and thighs, slight flush on cheeks"
      },
      "facial_features": {
        "expression": "Soft, relaxed smile, confident but casual, looking directly at camera",
        "eyes": "Light blue-grey, natural eyelashes, direct gaze, slight squint from sunlight",
        "nose": "Small, button nose, straight bridge",
        "lips": "Natural pink color, soft texture, closed mouth smile",
        "cheeks": "High cheekbones, rosy/sun-flushed complexion",
        "makeup": "Minimal/natural look, 'no-makeup' makeup style"
      },
      "hair": {
        "style": "High pigtails secured with hair ties",
        "color": "Blonde, sun-bleached highlights",
        "texture": "Straight but slightly messy, wind-swept flyaways, unkempt casual look"
      }
    },
    "attire": {
      "type": "String bikini",
      "pattern": "Pink and white tie-dye/marble pattern",
      "details": "Triangle top, side-tie bottoms, thin strings, visible knot on hip"
    },
    "accessories": {
      "jewelry": "Gold chain necklace, small gold hoop earrings"
    },
    "pose_and_action": {
      "posture": "Kneeling on the ground, leaning forward slightly",
      "hands": "Resting stacked on top of the tennis racket handle",
      "orientation": "Front-facing body, head tilted slightly to the side"
    },
    "props": {
      "item": "Tennis racket",
      "color": "Pink and black frame, white grip tape",
      "position": "Vertical, head of racket resting on the ground, handle pointing up supporting the subject's hands"
    },
    "environment": {
      "location": "Outdoor tennis court",
      "ground_surface": "Green hard court surface with white boundary lines, maroon/red out-of-bounds area visible in bottom left",
      "background": "Green windscreen attached to chain-link fence, tall pine trees visible above the fence line, clear blue sky peeking through"
    },
    "lighting": {
      "type": "Natural sunlight, Golden Hour",
      "direction": "Side-lit/Front-lit from the right",
      "shadows": "Hard shadow cast by the subject onto the green court to the left, distinct shadow of the racket mesh"
    },
    "technical_specs": {
      "camera_angle": "Eye-level to slightly high angle",
      "focus": "Sharp focus on subject, slightly softer background",
      "aspect_ratio": "4:5 ",
      "style": "Photorealistic, candid social media aesthetic, high definition"
    }
  }
}
```
---

### 61. 通过 JSON 和 UV 贴图元提示创建纹理

**作者**: [Mata3](https://x.com/mata3M4/status/2003083206258823609)  **日期**: 2025-12-22  **语言**: ja

> 使用 Nano Banana Pro 创建纹理是一个两步过程。首先，ChatGPT 会分析现有图像（例如，花朵、服装图案），并将其转换为详细的 JSON 提示，描述其尺寸、颜色、形状和细节。其次，将此 JSON 输入到专为 UV 映射设计的特殊元提示中，指示 Nano Banana Pro 将纹理绘制到 UV 展开图上，类似于 Substance Painter 的操作方式。

![通过 JSON 和 UV 贴图元提示创建纹理](https://cms-assets.youmind.com/media/1766667409461_aqgoa8_G8xhSjjasAAHQD2.jpg)

```
まず、**元にしたい画像（花・服・模様など）**を分析させる。

ChatGPTへの指示：

「この画像を、サイズ・色・形・ディティールまで含めてJSONプロンプト化して」

指示：「メタプロンプトGoal：NanoBananaPro用にUV展開図の上から指定のテクスチャーを描かせるプロンプトを作成してください。Substance paintみたいな処理を行い、画像２をUV展開図に照らし合わせて生成させてください。このJSONをベースに追加画像を参考に色を変えるためのプロンプトを作成してください。JSON形式でUV展開図にスカートのテクスチャを生成するプロンプトテンプレートの作成を目指す。NanobananaProにこの画像を参考にして色を作成してって言うのを明確にして。あらかじめ定義されたJSONスキーマに従って、1つのプロンプトJSONを生成してください：…」
```
---

### 62. 夜间街景：两位女士摆出惊讶的姿势

**作者**: [sammy](https://x.com/sumiturkude007/status/2002335667549045158)  **日期**: 2025-12-20  **语言**: en

> 一个详细的 JSON 提示，用于 Nano Banana Pro 生成一张图片：在夜晚的街道/停车场区域，两名女性——一名金发，一名深色头发——都表现出惊讶或感叹的表情，并详细说明了她们的外貌、服装和背景环境。

![夜间街景：两位女士摆出惊讶的姿势](https://cms-assets.youmind.com/media/1766386029419_qn2rnv_G8m5q9MbMAYvt3c.jpg)

```
{
  "prompt": {
    "subjects": [
      {
        "name": "blonde_woman",
        "appearance": {
          "hair": "Long, platinum blonde, straight",
          "skin_tone": "Fair, lightly bronzed",
          "eyes": "Dark, wide open, detailed makeup",
          "lips": "Light pink, open wide in surprise or exclamation",
          "nose": "Defined, straight bridge",
          "cheeks": "Slightly flushed, contoured",
          "expression": "Open-mouthed surprise, looking upward and right"
        },
        "clothing": {
          "top": "Red bandeau tube top",
          "bottom": "Light blue denim shorts with white circular details"
        },
        "pose": "Standing behind other woman, hand on her back, leaning forward",
        "position": "Left side of frame"
      },
      {
        "name": "brunette_woman",
        "appearance": {
          "hair": "Long, dark brown, wavy",
          "skin_tone": "Medium olive",
          "eyes": "Dark, looking upwards",
          "lips": "Nude, slightly parted in a smile",
          "nose": "Defined, slight curve",
          "cheeks": "Defined cheekbones, contoured",
          "expression": "Looking upward with a slight smile"
        },
        "clothing": {
          "top": "Red ribbed crop top",
          "bottom": "Black denim shorts",
          "socks": "White socks with blue patterns"
        },
        "pose": "Bent over at the waist, looking up",
        "position": "Right side of frame"
      }
    ],
    "environment": {
      "time": "Night",
      "location": "Street, parking area",
      "lighting": "Artificial street and car lights",
      "background_objects": [
        "White sedan (partial, left)",
        "Grey sedan (right, behind brunette)",
        "Red octagonal 'STOP' sign on post",
        "Green rectangular street sign above STOP sign",
        "Palm trees in background",
        "Asphalt pavement"
      ]
    },
    "aspect_ratio": "4:5"
  }
}
```
---

### 63. 绿巨人捏碎百事可乐罐电影级提示词

**作者**: [krystalion HQ](https://x.com/Krystalkrona0/status/2002128978484838902)  **日期**: 2025-12-19  **语言**: en

> 这是一个为 Nano Banana Pro 3.0 设计的结构化图像生成提示，旨在创建具有破坏性、高对比度的电影视觉效果。该提示使用简洁的命令来生成一张浩克巨手悬停在冒烟的城市废墟中被压扁的百事可乐罐上方的图像，并指定了 7:9 的宽高比。

![绿巨人捏碎百事可乐罐电影级提示词](https://cms-assets.youmind.com/media/1766238156041_ppchnq_G8j9sF1W0AAWgha.jpg)

```
{
    "concept_id": "hulk_pepsi",
    "visual_breakdown": {
      "focus_object": "Crushed Pepsi Can",
      "character_element": "Hulk's Giant Hand",
      "environment": "Smoky City Ruins"
    },
    "artistic_direction": {
      "lighting": "Explosive/High Contrast",
      "mood": "destructive"
    },
    "generation_command": {
      "aspect_ratio": "7:9",
      "concise_prompt": "Hulk's giant hand hovering over a crushed {argument name="soda brand" default="Pepsi"} can embedded in pavement, smoky ruins, explosive action movie style. --ar 7:9"
    }
  }
```
---

### 64. 技术姿势和相机锁定提示（泳装）

**作者**: [Sienna](https://x.com/siennalovesai/status/2001817881013629339)  **日期**: 2025-12-19  **语言**: en

> 这是一个极其详细、技术性的 JSON 提示，专为 Gemini Nano Banana Pro 设计，它使用“锁定”参数来精确控制主体的姿势（身体朝向、手臂/腿部角度、手势）、相机设置（焦距、位置、畸变）和服装几何形状（带有特定文字的连体泳衣）。此提示旨在实现高度受控的图像生成。

![技术姿势和相机锁定提示（泳装）](https://cms-assets.youmind.com/media/1766936184263_exshps_G8fiuo4WAAAaS7v.jpg)
![技术姿势和相机锁定提示（泳装）](https://cms-assets.youmind.com/media/1766936184715_yxo9tk_G8fiuo_XkAA9cmf.jpg)

```
{
  "pose_lock": {
    "subject_count": 1,
    "primary_subject_index": 0,
    "body_orientation": {
      "global_facing_degrees": 210,
      "torso_rotation_deg": 25,
      "torso_tilt_forward_deg": 15
    },
    "head_orientation": {
      "yaw_deg": -18,
      "pitch_deg": -5,
      "roll_deg": 2,
      "gaze_target": "camera_lens"
    },
    "shoulders": {
      "tilt_deg": -10,
      "left_elev_cm": 2,
      "right_elev_cm": -2
    },
    "arms": {
      "left": {
        "elbow_deg": 95,
        "wrist_deg": -10,
        "pos_n": {
          "x": 0.22,
          "y": 0.24
        }
      },
      "right": {
        "elbow_deg": 80,
        "wrist_deg": -15,
        "pos_n": {
          "x": 0.64,
          "y": 0.68
        }
      }
    },
    "hands": {
      "left": {
        "pose": "relaxed_open",
        "spread": 0.25
      },
      "right": {
        "pose": "light_hold",
        "spread": 0.15
      }
    },
    "legs": {
      "surface": "floor",
      "hip_height_cm": 18,
      "left_knee_deg": 90,
      "right_knee_deg": 100
    },
    "neck_back": {
      "neck_ext": 0.55,
      "upper_back_curve": 0.35
    },
    "face": {
      "mouth": "slight_open",
      "brows": 0.3,
      "eyes": 0.85
    },
    "strength": 1
  },
  "camera_lock": {
    "type": "smartphone_front",
    "focal_mm": 24,
    "focus_m": 0.45,
    "pos": {
      "h_m": 1.45,
      "dist_m": 0.4,
      "lat_m": 0.15
    },
    "orientation": {
      "yaw_deg": -40,
      "pitch_deg": -40,
      "roll_deg": 3
    },
    "lens": {
      "fov_deg": 73,
      "distortion": "mild_barrel",
      "strength": 0.18
    },
    "crop": {
      "ar": "4:5",
      "box": {
        "l": 0.02,
        "r": 0.98,
        "t": 0,
        "b": 1
      },
      "anchor": {
        "x": 0.42,
        "y": 0.35
      }
    },
    "dof": {
      "plane_m": 0.45,
      "blur_px": 3
    },
    "exposure": {
      "shutter": 0.01,
      "iso": 120,
      "aperture": 2
    },
    "white_balance": {
      "temp_k": 5200,
      "tint": 0.02
    },
    "strength": 1
  },
  "clothing_geometry_lock": {
    "type": "one_piece_swimsuit",
    "color": "{argument name="swimsuit color" default="light_cream"}",
    "material": {
      "finish": "smooth",
      "thickness_mm": 0.8,
      "stretch": 0.3
    },
    "straps": {
      "count": 2,
      "width_cm": 1.5,
      "orientation": "vertical"
    },
    "front_text": {
      "line1": "{argument name="text line 1" default="CALIFORNIA"}",
      "line2": "{argument name="text line 2" default="WEST COAST"}",
      "color": "blue",
      "scale": 0.6
    },
    "fit": {
      "form": "form_following",
      "wrinkles": 0.15
    },
    "prohibited": [
      "no_anatomical_detail",
      "no_pelvic_geometry",
      "no_sensitive_region_measurements"
    ],
    "strength": 1
  },
  "lighting_lock": {
    "key": {
      "type": "window_daylight",
      "azimuth_deg": 40,
      "elev_deg": 55,
      "lux": 1200
    },
    "fill": {
      "ratio": 0.4,
      "temp_k": 5000
    },
    "shadows": {
      "softness": 0.7
    },
    "specular": {
```
---

### 65. 海滩上金发女子与复古法拉利提示

**作者**: [KeorUnreal](https://x.com/KeorUnreal/status/2001672097072812255)  **日期**: 2025-12-18  **语言**: en

> 一个详细的 JSON 提示，用于 Nano Banana Pro 生成一张高分辨率的全身照：一位金发年轻成年女性身穿绿松石色比基尼，斜倚在一辆复古红色法拉利旁，背景是阳光明媚的海滩和灯塔，并确保严格保留人物身份。

![海滩上金发女子与复古法拉利提示](https://cms-assets.youmind.com/media/1766237896128_b3ima4_G8deKJbW8AAx7Us.jpg)

```
{
  "prompt_metadata": {
    "type": "image_generation",
    "quality": "high-resolution",
    "detail_level": "very high",
    "constraints": {
      "identity_preservation": {
        "enabled": true,
        "description": "100% same face and body details must be preserved"
      }
    }
  },
  "subject": {
    "category": "human",
    "gender": "female",
    "age_group": "young adult",
    "appearance": {
      "face": {
        "preserve_original_features": true,
        "expression": "calm and confident",
        "gaze_direction": "looking directly at the viewer"
      },
      "body": {
        "visibility": "full body",
        "description": "beautiful, proportionate, natural anatomy"
      },
      "hair": {
        "color": "{argument name="hair color" default="blonde platinum"}",
        "length": "medium to long",
        "texture": "slightly wavy",
        "style": "loose and natural"       
      }
    }
  },
  "wardrobe": {
    "primary_outfit": {
      "type": "bikini",
      "color": "{argument name="bikini color" default="turquoise"}",
      "style": "modern beachwear",
      "fit": "form-fitting"
    }
  },
  "pose_and_action": {
    "stance": "standing",
    "body_position": "leaning casually",
    "interaction": {
      "object": "vintage car",
      "description": "leaning in front of the car"
    }
  },
  "props": {
    "handheld_item": {
      "type": "drink",
      "liquid_color": "{argument name="drink color" default="green"}",
      "container_style": "transparent cup",
      "straw": {
        "color": "red"
      }
    }
  },
  "environment": {
    "setting": "beach with lighthouse",
    "weather": "sunny",
    "time_of_day": "daytime",
    "background_elements": {
      "sky": {
        "color": "bright blue",
        "clouds": "scattered white clouds"
      },
      "ocean": {
        "visibility": "clearly visible",
        "color": "blue",
        "position": "behind the subject"
      },
      "sand": {
        "description": "light-colored beach sand"
      }
    }
  },
  "objects": {
    "vehicle": {
      "type": "old ferrari car",
      "style": "vintage",
      "color": "{argument name="car color" default="turquoise"}",
      "condition": "well-maintained",
      "position": "behind the subject, used as a prop"
    }
  },
  "lighting_and_color": {
    "lighting_type": "natural sunlight",
    "illumination": "bright and even",
    "shadows": "soft, minimal harsh contrast",
    "color_palette": [
      "turquoise",
      "blue",
      "green",
      "sand beige"
    ]
  },
  "camera_and_composition": {
    "shot_type": "full-body shot",
    "camera_angle": "eye-level",
    "focus": "sharp focus on subject",
    "depth_of_field": "moderate, background slightly softened",
    "framing": "subject centered with environment clearly visible"
  }
}
```
---

### 66. 银行金库劫案场景，配有金色手枪

**作者**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_/status/2001629336722436523)  **日期**: 2025-12-18  **语言**: en

> 一个结构化的提示，用于生成一张动态的低角度照片：一名女性身穿乳胶露脐上衣和渔网袜，跪在一个灯光明亮的银行金库中。构图聚焦于她手持一把巨大的、刻有花纹的金色手枪，直接指向镜头，强调武器在前景中的主导地位。

![银行金库劫案场景，配有金色手枪](https://cms-assets.youmind.com/media/1766237831217_ivwzdm_G8c3QfJWMAAJUW9.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "main": "A woman kneeling in an elevated position",
      "action": "Holding a massive, richly engraved gold pistol (Desert Eagle style) directly into the camera",
      "clothing": {
        "top": "Shiny black latex crop top",
        "bottom": "Black trousers",
        "accessories": "Black fishnet stockings used creatively: one as a face mask, the other in her dark hair"
      },
      "identity_instruction": "Use Precise ID Lock to maintain precise facial features, hairstyle, skin tone, body proportions, age and expression with 100% accuracy"
    },
    "environment": {
      "setting": "Brightly lit bank vault",
      "details": [
        "Sterile bank vault",
        "Open lockers",
        "Money lying all over the room",
        "Gold ceiling with bright fluorescent lights"
      ]
    },
    "technical_specs": {
      "camera_angle": "Extreme low-angle shot",
      "lens": "Wide-angle lens",
      "composition": "Dynamic perspective where the pistol barrel dominates the foreground",
      "lighting": "Bright, clear artificial light",
      "focus": "Sharp focus on the gun and the woman",
      "style": "Dynamic photo"
    }
  }
}
```
---

### 67. 夜间池畔度假照片分析提示

**作者**: [Vivek HY](https://x.com/Vivekhy/status/2001343002380505373)  **日期**: 2025-12-17  **语言**: en

> 一个详细的 JSON 提示，用于图像分析，描述了一位年轻女子夜晚趴在度假村泳池中。该提示详细说明了拍摄对象的姿势、表情、服装和热带环境，重点在于高对比度的闪光摄影照明，以营造出俏皮的度假主题图像。

![夜间池畔度假照片分析提示](https://cms-assets.youmind.com/media/1766042086868_o51bm4_G8Yy2n1akAAFJ2x.jpg)

```
{
  "image_analysis": {
    "subject": {
      "demographics": "Young woman",
      "pose": "Lying on stomach in pool, propped up on elbows, legs bent upward at the knees with feet crossed in the air",
      "expression": "Broad, cheerful smile, looking directly at the camera",
      "hair": "Dark, wet, slicked back from swimming",
      "clothing": {
        "item": "One-piece swimsuit",
        "color": "Purple"
      }
    },
    "environment": {
      "location": "Outdoor swimming pool at a resort or hotel",
      "time_of_day": "Night",
      "weather": "Clear, tropical",
      "background": {
        "elements": [
          "Tall palm trees",
          "Multi-story hotel building with warm lights in windows",
          "Dark night sky"
        ]
      },
      "foreground": {
        "elements": [
          "Rippled blue pool water",
          "Reflection of the subject in the water"
        ]
      }
    },
    "lighting": {
      "style": "Flash photography mixed with ambient background light",
      "qualities": [
        "Subject is brightly illuminated",
        "Background is dimly lit with warm accent lights",
        "High contrast between subject and dark background"
      ]
    },
    "aesthetics": {
      "mood": "Happy, playful, relaxed, vacation vibes",
      "composition": "Eye-level shot relative to the water surface, subject centered",
      "color_palette": [
        "Purple (swimsuit)",
        "Deep Cyan/Blue (water)",
        "Black (sky)",
        "Warm Yellow/Orange (background lights)",
        "Green (palm trees)"
      ]
    }
  }
}
```
---

### 68. 圣托里尼连体泳衣姿势复刻提示词

**作者**: [Sienna](https://x.com/siennalovesai/status/1999581621758972368)  **日期**: 2025-12-12  **语言**: en

> 这是一个为 Gemini Nano Banana Pro 设计的高度具体的模板提示，用于图像到图像的生成。它指示模型精确地重新创建一张参考照片（姿势、角度、光线、背景——圣托里尼的一个私人洞穴泳池），同时仅将照片中女性的身份替换为上传的主体，确保严格遵循白色的钩针连体泳衣和环境。

![圣托里尼连体泳衣姿势复刻提示词](https://cms-assets.youmind.com/media/1765990991402_befqin_G7_w4lkXYAM6Nm2.jpg)

```
{
  "template_id": "white_crochet_monokini_santorini_v1",
  "version": "1.0.0",
  "goal": "Recreate the reference photo EXACTLY — pose, camera angle, lighting, background, monokini design — while replacing ONLY the woman's identity with the uploaded subject. No other creative changes allowed.",
  "identity": { /* same as above */ },
  "pose_anchor": {
    "head": {
      "tilt_direction": "backwards",
      "tilt_angle_degrees": 25,
      "gaze": "eyes open, looking up at sky"
    },
    "torso": { "posture": "lying back on pool edge, elbows supporting" },
    "arms_hands": { "both_hands": "behind head, fingers interlaced" }
  },
  "outfit_lock": {
    "type": "white crochet monokini",
    "details": "high-cut legs, deep V front, open crochet pattern, thin straps"
  },
  "environment_lock": {
    "location_type": "private cave pool in Oia, Santorini",
    "background": { "whitewashed walls", "caldera view", "bright Aegean blue sea and sky" }
  },
  "lighting_color": { "time_of_day": "midday", "color_temperature": "5600K" }
}
```
---

### 69. 2013 年 Tumblr 伤感女孩秋日美学提示词

**作者**: [Ditherly - Creative AI Hub](https://x.com/ditherly_art/status/1998497894509457729)  **日期**: 2025-12-09  **语言**: en

> 一个用于 Nano Banana Pro 的 JSON 提示词，旨在生成一张“独立颓废复兴”或“柔和垃圾摇滚”风格的图像，捕捉 2013 年 Tumblr 卧室场景的美学，画面中主体躺在地板上，使用小彩灯和手机闪光灯作为光源，并确保从参考图像中保留身份。

![2013 年 Tumblr 伤感女孩秋日美学提示词](https://cms-assets.youmind.com/media/1765440029729_lpmv4s_G7WZzREWIAAJUix.jpg)

```
{
  "image_generation": {
    "identity_requirements": { "face": { "preserve_original": true, "exact_match": true }, "hair": { "preserve_original": true, "exact_match": true }},
    "setting": { "location": "messy teen bedroom floor, fairy lights tangled" },
    "scene": { "effects": { "scattered Polaroids", "empty Diet Coke cans", "vinyl records", "soft flash" }},
    "subject": {
      "pose": { "body_position": "laying on stomach on carpet, chin in hands, kicking feet" },
      "clothing": { "top": "striped long-sleeve thrift shirt half unbuttoned, plaid skirt or baggy cargo pants" },
      "expression": "soft pout, doe-eyed, fairy lights reflecting in eyes"
    },
    "camera": { "aspect_ratio": "9:16", "style": "2013 Tumblr bedroom", "lighting": { "type": "warm fairy lights + phone flash" }},
    "aesthetic": { "mood": "sad girl autumn all year", "style": ["indie sleaze revival", "soft grunge"] }
  }
}
```
---

### 70. 极简轮廓聚光灯提示与签名

**作者**: [Vivek HY](https://x.com/Vivekhy/status/1998430193338425658)  **日期**: 2025-12-09  **语言**: en

> 一个用于 Nano Banana Pro 3.0 的 JSON 提示，旨在生成一张极简主义、富有戏剧性的图像：画面中，一个人形剪影置身于一片黑色虚空之中，上方一束聚光灯将其照亮，并包含一个自定义签名叠加。

![极简轮廓聚光灯提示与签名](https://cms-assets.youmind.com/media/1765440014848_yksbhz_G7vZq4RbsAEjbYj.jpg)

```
{
  "prompt_id": "silhouette_dark_001_signature",
  "description": "Minimalist dramatic silhouette in darkness with signature",
  "scene": {
    "environment": "complete black void background",
    "lighting": {
      "type": "single spotlight",
      "position": "directly above subject",
      "intensity": "soft but focused",
      "effect": "circular glow around subject with smooth fade-out"
    }
  },
  "subject": {
    "type": "human silhouette",
    "pose": "standing centered, facing camera",
    "details": "fully black silhouette with no facial features",
    "shadow": {
      "style": "long hard-edged shadow",
      "direction": "towards bottom-left",
      "sharpness": "high contrast"
    }
  },
  "composition": {
    "framing": "extreme wide with large negative space",
    "mood": "mysterious, lonely, cinematic",
    "aspect_ratio": "4:5"
  },
  "signature": {
    "text": "{argument name="signature text" default="Vivek HY"}",
    "position": "bottom right corner",
    "style": "minimal, clean, white color",
    "opacity": "70%"
  },
  "post_processing": {
    "contrast": "very high",
    "glow": "soft radial light",
    "grain": "low"
  }
}
```
---

### 71. 1x3 网格手机动态编辑 JSON 提示

**作者**: [SDT🌿](https://x.com/SDT_side/status/1997977301703954705)  **日期**: 2025-12-08  **语言**: ja

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
---

### 72. Nano Banana Pro 2x2 网格手机屏幕更换 JSON 提示

**作者**: [SDT🌿](https://x.com/SDT_side/status/1997908793573978587)  **日期**: 2025-12-08  **语言**: ja

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
---

### 73. 汽车自拍与芝士饼干提示

**作者**: [John](https://x.com/johnnprofits/status/1996722937727201301)  **日期**: 2025-12-04  **语言**: en

> 一个结构化的 JSON 提示词，用于生成一张年轻女性在汽车驾驶座上眨眼微笑的图像，具体描述她嘴里叼着一块奶酪饼干，并详细说明她的特征、着装以及汽车内饰/背景。

![汽车自拍与芝士饼干提示](https://cms-assets.youmind.com/media/1765106417249_w6shbq_G7WUO_4W0AAykqU.jpg)

```
{
  "subject": {
    "type": "person",
    "gender": "female",
    "age_group": "young adult",
    "hair_color": "blonde",
    "eye_color": "blue",
    "features": "freckles",
    "expression": "winking, smiling",
    "action": "holding a cheese cracker in mouth"
  },
  "attire": {
    "clothing": "black long-sleeved scoop-neck top"
  },
  "setting": {
    "location": "inside a car",
    "position": "driver's seat",
    "interior": "black and white leather seats",
    "background": "trees, daylight, car window"
  },
  "object": {
    "type": "food",
    "description": "orange square cheese cracker"
  }
}
```
---

### 74. 篮中葡萄的简单图像提示

**作者**: [Kenan Tang @ NeurIPS 2025](https://x.com/KenanTang/status/1995750008742887592)  **日期**: 2025-12-02  **语言**: en

> 一个简洁的 Nano Banana Pro 图像提示，用于生成由葡萄藤编织而成的篮子里的葡萄，以比较模型质量。

![篮中葡萄的简单图像提示](https://cms-assets.youmind.com/media/1764909186972_6raeql_G7JTSqMbMAAyGCX.jpg)
![篮中葡萄的简单图像提示](https://cms-assets.youmind.com/media/1764909190026_hb582b_G7JTT4UbgAAELXm.jpg)

```
{argument name="subject" default="grapes in a basket made from grape vines"}
```
---

### 75. 病毒式缩略图：兴奋地指着，牛油果吐司，“3 分钟搞定！”

**作者**: [泊舟](https://x.com/bozhou_ai/status/1995418448562659426)  **日期**: 2025-12-01  **语言**: zh

> 具有身份锁定功能的病毒式视频缩略图

![病毒式缩略图：兴奋地指着，牛油果吐司，“3 分钟搞定！”](https://cms-assets.youmind.com/media/1764909134095_knrv2v_G7Eh_FxWIAA-zTh.jpg)
![病毒式缩略图：兴奋地指着，牛油果吐司，“3 分钟搞定！”](https://cms-assets.youmind.com/media/1764909136349_7w4red_G7EiAbrWQAAYWZI.jpg)
![病毒式缩略图：兴奋地指着，牛油果吐司，“3 分钟搞定！”](https://cms-assets.youmind.com/media/1764909138880_kpzwcx_G7EiCZ6XgAAiAot.jpg)

```
使用 Image 1 中的人物设计一个病毒式视频缩略图。
面部一致性：保持人物的面部特征与 Image 1 完全相同，但将表情改为兴奋与惊讶。
动作：将人物置于画面左侧，用手指指向画面的右侧。
主体：在右侧放置一张高质量的美味 {argument name="食物" default="鳄梨吐司"} 图像。
图形：添加一个粗黄色箭头，将人物的手指与 {argument name="主体" default="吐司"} 连接。
文本：在画面中央叠加巨大的流行风格文本：‘{argument name="缩略图文本" default="3分钟搞定！"}’。使用粗白色轮廓与投影阴影。
背景：使用模糊的明亮 {argument name="背景场景" default="厨房"} 背景，并提升饱和度与对比度。
```
---

### 76. Nano Banana Pro 的垂直超高细节图像设置

**作者**: [tenso](https://x.com/distributedkv/status/1994472225714647245)  **日期**: 2025-11-28  **语言**: en

> 一个用于 Nano Banana Pro 的 JSON 配置风格提示，指定了一个高大的垂直 8K 画布，具有超高细节。这是一个可重复使用的基础提示，用于定义垂直拍摄的尺寸和技术质量。

![Nano Banana Pro 的垂直超高细节图像设置](https://cms-assets.youmind.com/media/1764577532761_diywuf_G63J0rlbYAAVOje.jpg)
![Nano Banana Pro 的垂直超高细节图像设置](https://cms-assets.youmind.com/media/1764577536218_wr8uh4_G63J1XKbkAEBch2.jpg)

```
{
  "image_info": {
    "width": {argument name="image width" default="4096"},
    "height": {argument name="image height" default="8192"},
    "aspect_ratio": "{argument name="aspect ratio" default="1:2"}",
    "orientation": "{argument name="orientation" default="vertical"}"
  },

  "technical": {
    "resolution": "{argument name="resolution" default="8k"}",
    "dimensions": "{argument name="dimensions" default="4096x8192 or higher"}
    ,"quality": "{argument name="quality" default="ultra high detail"}"
  }
}
```
---

### 77. 错视画主题人物走出社交媒体屏幕

**作者**: [madpencil_](https://x.com/madpencil_/status/1992118499876213233)  **日期**: 2025-11-22  **语言**: en

> 一个提示，将上传的主题变成一幅错视画，画中主题从大屏幕上的社交媒体界面中走出，包含用户界面细节和表情符号反应。

![错视画主题人物走出社交媒体屏幕](https://cms-assets.youmind.com/media/1763885724726_hc1ah8_G6VtN7haMAAlkVQ.jpg)

```
Trompe l'oeil illusion of {argument name="subject" default="A (subject)"} {argument name="attire" default="(attire)"} steps out of a large screen displaying {argument name="platform" default="xyz social media"} interface. The screen shows the username "@" 1K likes, and 12- 20 comments, with floating emojis (heart-eyes, smiley) around it. {argument name="background" default="your preferred background"}.
```

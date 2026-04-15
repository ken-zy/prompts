# Chunk 041

Total: 200 prompts

### 1. AI 风格化香水产品视觉图，带内部花瓣

**Author**: [ShaHid WaNii](https://x.com/meng_dagg695)  **Date**: 2026-02-08  **Language**: en

> 一个高度详细的 JSON 提示，用于创建香水瓶的 AI 风格化产品视觉效果。该提示指定了瓶子的形状、材质和颜色，并包含独特的内部元素，如漂浮的花瓣，以及飞溅和漂浮花瓣等动态元素，所有这些都置于温暖的橙色渐变背景和生动的影棚灯光之下。

![AI 风格化香水产品视觉图，带内部花瓣](https://cms-assets.youmind.com/media/1770619684925_2g0aag_HAoWxNUbYAAnipu.jpg)
![AI 风格化香水产品视觉图，带内部花瓣](https://cms-assets.youmind.com/media/1770619684869_qpf8ur_HAoWxVKbcAA55hG.jpg)
![AI 风格化香水产品视觉图，带内部花瓣](https://cms-assets.youmind.com/media/1770619684952_qidk7a_HAoWxP4boAAkzpA.jpg)

```
{
  "image_type": "AI-stylized product visual",
  "resolution_target": "8K ultra high definition",
  "aspect_ratio": "3:4",
  "orientation": "vertical",

  "primary_subject": {
    "object": "{argument name="object" default="perfume bottle"}",
    "position": "centered vertically and horizontally",
    "shape": "rectangular glass bottle with softly rounded edges",
    "material": "transparent glass",
    "glass_thickness": "thick, premium-looking glass walls",
    "color_tint": "warm amber-orange tint",
    "transparency": "high transparency with internal reflections",
    "surface_finish": "glossy, reflective"
  },

  "bottle_cap_and_sprayer": {
    "sprayer_type": "standard perfume atomizer",
    "sprayer_color": "metallic gold",
    "finish": "high-gloss polished metal",
    "sprayer_visibility": "fully visible, centered on bottle top",
    "cap_presence": "no outer cap visible"
  },

  "internal_elements": {
    "content_inside_bottle": "flower petals visible inside glass",
    "petal_color": "soft orange with light peach highlights",
    "petal_texture": "smooth, delicate, semi-translucent",
    "petal_arrangement": "layered and overlapping, filling the bottle interior",
    "liquid_visibility": "no distinct liquid line visible"
  },

  "flower_structure": {
    "flower_type_visual": "large blooming flower",
    "bloom_position": "flower petals open outward around the bottle base",
    "petal_shape": "broad, curved, rounded tips",
    "petal_edges": "soft, smooth, slightly feathered",
    "petal_scale": "large petals relative to bottle size"
  },

  "stem_and_leaves": {
    "stem": {
      "color": "natural green",
      "thickness": "slender but sturdy",
      "orientation": "vertical, centered beneath bottle"
    },
    "leaves": {
      "count_visible": 2,
      "color": "green with muted tone",
      "shape": "elongated oval",
      "surface": "smooth with subtle texture",
      "position": "one leaf angled left, one angled right"
    }
  },

  "motion_elements": {
    "floating_petals": {
      "presence": true,
      "quantity": "multiple",
      "distribution": "scattered throughout foreground and background",
      "orientation": "varied angles and rotations",
      "motion_style": "suspended mid-air, slow-floating effect"
    },
    "liquid_splashes": {
      "presence": true,
      "location": "around bottle midsection and petals",
      "appearance": "small water droplets and splash arcs",
      "transparency": "clear, glossy droplets",
      "motion": "frozen mid-splash"
    }
  },

  "lighting": {
    "overall_lighting": "soft yet vivid studio lighting",
    "key_light": "front-facing, highlighting bottle and petals",
    "rim_light": "subtle glow around glass edges",
    "reflection_behavior": "strong reflections on glass and metal sprayer",
    "shadow_style": "minimal harsh shadows, smooth gradients"
  },

  "background": {
    "color": "warm orange gradient",
    "gradient_behavior": "darker near edges, bright"
  }
}
```

[[Product Visualization]]

---

### 2. PC 到智能手机网页设计转换提示，适用于 Nano-banana Pro

**Author**: [まさた｜Web制作](https://x.com/Masa_nmFL)  **Date**: 2026-02-08  **Language**: ja

> 这是一个针对 Nano-banana Pro 的详细系统提示，指示其扮演一名熟练的 UI 设计师。它将 PC 网页设计图像的一部分转换为针对智能手机 (SP) 屏幕优化的响应式布局。该提示包含布局转换的具体规则（将水平元素垂直堆叠）、保持设计一致性（颜色、字体、样式），以及排除不必要的元素（如页眉或页脚），只专注于提供的部分。

```
# 命令
あなたは熟練したUIデザイナーです。
添付された「PC版Webデザインの一部（セクション）」画像を解析し、そのパーツがスマホ（SP）画面で表示された際の最適なレイアウト画像を生成してください。

# 生成のルール（セクション特化）
1. 独立したコンポーネントとして処理:
- ヘッダーやフッター、余計なナビゲーションバーは一切追加しないでください。
- 画像にある要素（テキスト、アイコン、写真）のみを使用して再構成してください。

2. レイアウトのレスポンシブ化（Stacking）:
- PCで横並び（Horizontal row）になっている要素は、スマホ用に縦積み（Vertical column）に変更してください。
- 余白（Padding/Margin）はスマホの狭い画面幅に合わせて適切に調整してください。

3. デザインの継承:
- 元画像の配色、フォントの雰囲気、装飾スタイルを維持してください。
- 画像のアスペクト比は、要素が縦に並ぶことを想定して 縦長（{argument name="アスペクト比" default="3:4 または 9:16"}）で生成してください。

# アクション
添付画像のセクションを、スマホの画面幅（375px〜）に最適化したデザインカンプとして1枚生成してください。
```

[[UI Design]] [[System Prompt]]

---

### 3. 芬达橙味汽水罐与爆裂橙子切片的超逼真电影级产品特写

**Author**: [Sadia](https://x.com/SadiaMalik182)  **Date**: 2026-02-08  **Language**: en

> 芬达橙味铝罐的超逼真电影级产品照片的文本提示。它详细描述了罐体冰冷的质感（微凝结水珠），以及新鲜橙片和柑橘瓣向外爆裂的动态场景，果汁飞溅，半透明的果肉纤维在空中凝固。

![芬达橙味汽水罐与爆裂橙子切片的超逼真电影级产品特写](https://cms-assets.youmind.com/media/1770619723593_qejqsm_HAoFpbvWoAAZpcw.jpg)
![芬达橙味汽水罐与爆裂橙子切片的超逼真电影级产品特写](https://cms-assets.youmind.com/media/1770619723587_s91sxe_HAoFpg5XUAADdto.jpg)
![芬达橙味汽水罐与爆裂橙子切片的超逼真电影级产品特写](https://cms-assets.youmind.com/media/1770619723841_ordy79_HAoFpkyXoAAyOWX.jpg)

```
Hyper-realistic cinematic product photograph of a classic {argument name="beverage brand" default="Fanta Orange"} aluminum can, logo perfectly centered and fully legible, standing upright and slightly forward-facing, the can ice-cold and covered in dense micro-condensation droplets with natural gravity streaks and crisp specular highlights. Behind and around the can, fresh orange slices and citrus wedges explode outward in slow motion, juice splashes frozen mid-air with translucent pulp fibers, tiny droplets, and refractive
```

[[Commercial Product Photography]] [[Condensation Detail]]

---

### 4. 红毯名人时尚变体提示

**Author**: [Rowan](https://x.com/rowanali09)  **Date**: 2026-02-08  **Language**: en

> 这是一个高度结构化的 JSON 提示，旨在为红毯上的名人（安娜·德·阿玛斯风格）生成多种服装变体。该提示在保持面部特征和环境一致的同时，详细描述了三款截然不同的高级定制礼服（黄绿色、淡粉色、祖母绿色）及相应的姿势，所有图像均以 8K 电影级写实风格渲染。

![红毯名人时尚变体提示](https://cms-assets.youmind.com/media/1770619695586_ufe3zu_HAoFAExasAAZsUh.jpg)
![红毯名人时尚变体提示](https://cms-assets.youmind.com/media/1770619695587_bzk4hs_HAoFAGXbkAALRrA.jpg)
![红毯名人时尚变体提示](https://cms-assets.youmind.com/media/1770619695805_7310ko_HAoE_jVaUAIqILO.jpg)
![红毯名人时尚变体提示](https://cms-assets.youmind.com/media/1770619696542_xk9dql_HAnyAoFbwAAuAc-.jpg)
![红毯名人时尚变体提示](https://cms-assets.youmind.com/media/1770619696800_8hjgfe_HAnyAnlWUAANy2H.jpg)
![红毯名人时尚变体提示](https://cms-assets.youmind.com/media/1770619697926_cmjgla_HAnyAnkWIAAqQlF.jpg)

```
{
  "prompt_structure": {
    "subject_description": {
      "demographics": "Young adult female",
      "hair": "Dark brown, wavy texture, styled in a messy half-up/half-down look with loose strands framing the face (varies to high ponytail in pink dress variation)",
      "face": "Fair skin tone, hazel-green eyes, soft natural glam makeup, glossy nude lips, defined eyebrows, gentle smile",
      "physique": "Slender, fit build"
    },
    "environment_context": {
      "setting": "Red carpet or luxury event backdrop",
      "background": "Vertical pleated cream/beige wall",
      "props": "Large, illuminated gold metallic 3D letters (fragments visible, likely spelling a brand name)",
      "lighting": "Professional warm event lighting, soft highlights on skin, shallow depth of field (bokeh) blurring the background"
    },
    "technical_specs": {
      "style": "Cinematic portrait, photorealistic, celebrity fashion photography",
      "resolution": "8k, highly detailed textures",
      "shot_type": "Medium shot, waist-up"
    },
    "visual_variations": [
      {
        "variant_id": "outfit_yellow",
        "clothing": "{argument name="dress color 1" default="Chartreuse/lime green"} satin evening gown",
        "clothing_details": "One-shoulder asymmetrical neckline, fitted bodice with diagonal rushing/draping across the waist, smooth silk sheen",
        "accessories": "Long dangling diamond drop earrings",
        "pose": "Facing forward, hands resting on hips/thighs, confident expression"
      },
      {
        "variant_id": "outfit_pink",
        "clothing": "Pale pink embellished cocktail dress",
        "clothing_details": "High halter neckline, sleeveless, fully encrusted with shimmering pink sequins and beads, textured surface",
        "accessories": "Long dangling diamond drop earrings",
        "pose": "Body facing forward, head turned to the left profile, looking away, candid expression"
      },
      {
        "variant_id": "outfit_green",
        "clothing": "{argument name="dress color 3" default="Emerald green"} satin evening gown",
        "clothing_details": "One-shoulder asymmetrical neckline, structured draping across the chest and waist, rich jewel-tone luster",
        "accessories": "Long dangling diamond drop earrings",
        "pose": "Angled slightly to the right, hands loosely clasped in front of waist, direct gaze"
      }
    ]
  }
}
```

[[8K Cinematic Portrait]]

---

### 5. 电影感黑白街头时尚大片模板

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-02-08  **Language**: en

> 一个结构化的提示模板，用于生成电影感、高对比度、黑白街头摄影作品，带有动态模糊效果，适合受 Nike 等品牌启发的都市时尚大片。它包含主体、姿势、场景和相机规格的占位符。

![电影感黑白街头时尚大片模板](https://cms-assets.youmind.com/media/1770619701642_p9elar_HAkb3KLW0AEuQv3.jpg)
![电影感黑白街头时尚大片模板](https://cms-assets.youmind.com/media/1770619701656_8pu61i_HAkb3KVXAAAkkGF.jpg)
![电影感黑白街头时尚大片模板](https://cms-assets.youmind.com/media/1770619701782_c4s2ne_HAkb3KOXwAQmxA7.jpg)
![电影感黑白街头时尚大片模板](https://cms-assets.youmind.com/media/1770619702746_u3n2ep_HAkb3EcWkAAt3lK.jpg)

```
{
  "meta": {
    "purpose": "Cinematic motion blur B&W street photography for urban fashion editorials",
    "style": "High contrast monochrome, storytelling realism, Nike-inspired visuals, 8K"
  },
  "subject": {
    "main": "{argument name="subject description" default="Model in streetwear walking through crowd"}",
    "pose": "{argument name="pose" default="Dynamic stride with motion streaks"}",
    "attire": "[e.g., Urban jacket and sneakers]"
  },
  "environment": {
    "setting": "[e.g., Busy city street at night]",
    "details": "Crowd blur effect, wet pavement reflections"
  },
  "lighting": {
    "type": "[e.g., Cinematic portrait with high contrast]",
    "effects": "Monochrome grading, viral editorial mood"
  },
  "camera_specs": {
    "lens": "[e.g., Wide angle for urban depth]",
    "quality": "AI art realism, fine grain, no artifacts",
    "aspect_ratio": "[e.g., 9:16 vertical]",
    "negative": ["color", "static pose", "low contrast", "cartoonish"]
  }
}
```

[[High Contrast Monochrome]] [[Prompt Template]] [[Urban Fashion]]

---

### 6. 一位身穿运动服的亚洲女性在运动后的四格生活拼贴画

**Author**: [simeon-sanai](https://x.com/Naiknelofar788)  **Date**: 2026-02-08  **Language**: en

> 一个高度结构化的提示，旨在生成一个四格生活方式拼贴画，模仿自然的 iPhone 摄影和“洁净女孩健身”美学。它严格指定了面部身份锁定，详细描述了主体（亚洲女性，运动服），并定义了每个网格面板的内容（水瓶、自拍、镜子自拍、智能手表统计数据）。

![一位身穿运动服的亚洲女性在运动后的四格生活拼贴画](https://cms-assets.youmind.com/media/1770619716620_4i9jyz_HAn5ZgEbcAAZZqD.jpg)

```
{
  "task": "four_grid_lifestyle_collage",
  "reference_face": {
    "identity_lock": true,
    "face_match_accuracy": "100_percent_identical",
    "notes": "No facial changes allowed. Preserve exact facial structure, proportions, eye shape, nose, lips, brows, skin texture."
  },
  "output": {
    "type": "single_image",
    "layout": "2x2_grid",
    "resolution": "ultra_high_resolution",
    "realism": "natural_iphone_photography",
    "quality": "social_media_lifestyle_collage",
    "retouching": "minimal_skin_smoothing_only"
  },
  "subject": {
    "gender": "female",
    "age_range": "early_to_mid_20s",
    "ethnicity": "asian",
    "skin": {
      "tone": "fair",
      "texture": "natural_with_soft_glow",
      "makeup": "light_natural_makeup_with_soft_pink_blush"
    },
    "hair": {
      "color": "dark_brown",
      "style": "as in picture"
    },
    "expression": "calm_focused_fresh_morning_vibe"
  },
  "wardrobe": {
    "outfit": "fitted_black_full_sleeve_activewear_top_and_black_joggers",
    "style": "clean_minimal_fitness_look",
    "coverage": "fully_modest_no_exposed_midriff",
    "accessories": [
      "smartwatch_on_wrist",
      "neutral_phone_case"
    ]
  },
  "grid_breakdown": {
    "top_left": {
      "scene": "hand_holding_matte_blue_water_bottle",
      "shot_type": "close_up_object_shot",
      "focus": "hydration_and_fitness_routine"
    },
    "top_right": {
      "scene": "selfie_half_body",
      "camera_angle": "slightly_high_angle",
      "pose": "relaxed_morning_selfie",
      "expression": "soft_smile"
    },
    "bottom_left": {
      "scene": "mirror_selfie_full_upper_body",
      "camera": "iphone_front_camera",
      "pose": "standing_straight",
      "composition": "no_extreme_angles"
    },
    "bottom_right": {
      "scene": "smartwatch_fitness_stats_close_up",
      "details": "workout_time_calories_heart_rate_visible",
      "style": "authentic_post_workout_capture"
    }
  },
  "environment": {
    "setting": "indoor_home_gym_or_bedroom",
    "lighting": "soft_morning_natural_light",
    "color_palette": "neutral_black_beige_soft_blue",
    "mood": "productive_calm_morning_energy"
  },
  "style_notes": {
    "aesthetic": "clean_girl_fitness_lifestyle",
    "vibe": "morning_routine_realism",
    "camera_effects": "slight_film_softness_no_heavy_filters",
    "background": "simple_uncluttered"
  },
  "restrictions": {
    "no_face_alteration": true,
    "no_body_distortion": true,
    "no_sexualized_pose": true,
    "no_text_overlay": true,
    "no_logos_or_watermarks": true
  }
}
```

[[Clean Girl Aesthetic]] [[iPhone Photography Style]] [[Four Panel Grid]] [[Fitness Aesthetic]]

---

### 7. 2x2 网格奢华珠宝生活方式摄影

**Author**: [sammy](https://x.com/sumiturkude007)  **Date**: 2026-02-08  **Language**: en

> 一个高度结构化的提示，用于生成 2x2 网格拼贴画，内容为超现实的奢华珠宝生活方式照片，重点是一位在泳池边/海滩环境中晒出古铜色肌肤的女性。它细致地描述了拍摄对象的皮肤纹理（水珠、游泳后的光泽）、珠宝首饰以及明亮的自然阳光，以强调闪光和质感。

![2x2 网格奢华珠宝生活方式摄影](https://cms-assets.youmind.com/media/1770619676604_q6hgpb_HAn3aexaAAAOz4Q.jpg)

```
{
  "image_type": "luxury_jewelry_lifestyle_photoshoot",
  "layout": {
    "style": "2x2 grid collage",
    "panels": 4,
    "aspect_ratio": "4:5 vertical",
    "consistency": "cohesive lighting and color grading across all panels"
  },
  "subject": {
    "gender": "female",
    "age_range": "young adult",
    "physique": "slim, toned",
    "skin_tone": "warm golden tan",
    "skin_details": [
      "visible water droplets",
      "dewy post-swim glow",
      "natural skin texture",
      "faint freckles"
    ],
    "makeup": "minimal, natural look",
    "nails": "short, nude or soft pink polish"
  },
  "wardrobe": {
    "bikini": {
      "color": "{argument name="bikini color" default="white"}",
      "details": "thin neon-yellow straps and ties",
      "fit": "fitted, summery style"
    }
  },
  "jewelry": {
    "style": "luxury diamond jewelry",
    "materials": ["silver", "white gold", "diamonds", "clear gemstones"],
    "pieces": [
      "layered necklaces of varying lengths",
      "diamond tennis chains",
      "round and square gemstone pendants",
      "diamond tennis bracelet",
      "stacked thin diamond rings"
    ],
    "visual_effect": "jewelry catching sunlight with subtle sparkle"
  },
  "environment": {
    "location_type": "poolside or beach",
    "surface": "neutral beige or cream lounge chair",
    "background": "minimal and out of focus",
    "atmosphere": "bright summer luxury vacation vibe"
  },
  "lighting": {
    "type": "bright natural sunlight",
    "time_of_day": "midday",
    "qualities": [
      "strong highlights",
      "natural sharp shadows",
      "emphasizes skin texture and jewelry reflections"
    ]
  },
  "camera": {
    "style": "ultra-realistic editorial photography",
    "lens_look": "85mm DSLR",
    "focus": "sharp on jewelry and skin texture",
    "depth_of_field": "shallow",
    "quality": "high resolution",
    "color_grading": "warm natural tones"
  },
  "panels": {
    "top_left": {
      "framing": "torso and waist close-up while reclining",
      "pose": "hand resting gently on abdomen",
      "details": [
        "bikini hip ties visible",
        "bracelet visible",
        "strong sun highlights and shadows"
      ]
    },
    "top_right": {
      "framing": "hand resting on upper thigh",
      "focus": "stacked rings and bracelet",
      "details": [
        "visible water droplets",
        "sun reflections on skin and jewelry"
      ]
    },
    "bottom_left": {
      "framing": "neck and collarbone close-up",
      "focus": "layered necklaces",
      "details": [
        "strong sunlight on collarbone",
        "jewelry sparkle emphasized"
      ]
    },
    "bottom_right": {
      "framing": "upper chest close-up",
      "pose": "hand touching collarbone",
      "focus": [
        "rings",
        "layered necklaces"
      ]
    }
  },
  "mood": [
    "elegant",
    "premium",
    "relaxed luxury",
    "summer glow",
    "tasteful sensuality",
    "high-end jewelry campaign"
  ]
}
```

[[Natural Sunlight]] [[2x2 Grid]] [[Poolside Photography]]

---

### 8. 月球平原上的超现实电影时尚大片

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-02-08  **Language**: en

> 一个高度具体、复杂的提示，用于生成一组超现实、电影感的时尚大片肖像，场景设定在夜晚月球般的岩石平原上。它详细描述了构图（垂直 9:16，主体坐在金属椅子上，一张空道具椅上放着咖啡器具）、灯光（冷调的“月光/太空光”主光，来自地球的青色补光），以及风格（超干净的 VFX 写实主义，细微的胶片颗粒感）。

![月球平原上的超现实电影时尚大片](https://cms-assets.youmind.com/media/1770619679976_cqdxvs_HAn0UNGaIAAERs8.jpg)

```
Using A Different Person's Photo As Identity Reference, Create A Surreal Cinematic Fashion Editorial Portrait Set On A Moonlike Rocky Plain At Night Vertical 9:16 Wide Full-body Framing With Lots Of Negative Space, Subject Seated On A Simple Metal Folding Chair Placed In The Left Third, Legs Crossed, One Elbow Resting On The Knee With The Hand Lightly Supporting The Temple/Cheek Shoulders Relaxed, Calm Contemplative Expression, Gaze Looking Up And Off-camera Toward The Horizon, Wardrobe Is Clean Minimalist Streetwear-oversized White Tee (No Visible Logos), White Cap, Black Cargo Pants, Black/White Sneakers, Minimal Jewelry Scene Composition Includes A Second Empty Folding Chair In The Right Third Used As A Prop-table Holding A Small Manual Coffee Grinder And A White Espresso Cup With Visible Rising Steam, Lunar Regolith Foreground With Scattered Rocks And Crisp Microtexture, Subtle Footprints And Dust. Background: Massive Earth Looming Low In The Sky Behind The Subject With Soft Atmospheric Glow And Faint City Lights, Star-filled Deep Navy Sky Gradient From Near-black (#040700) To Cool Blue (#082456), Moon Ground In Desaturated Blue-gray (#2f3e4e) Lighting Cold "Moonlight/Space Light Key From Upper-right (-6000-7000k) Casting Sharp Clean Shadows On The Ground, Soft Cyan Him/Bounce From Earth On Edges Of Face/Shoulders (-9000k Tint); Very Subtle Neutral Fill From Camera-left To Retain Shadow Detail, Gentle Haze And Bloom Around Earth's Limb, Controlled Contrast, Glossy Speculars On Metal Chairs, Natural Skin Tones Preserved Optics 35mm Cinematic Wide Portrait, F/28-4, Medium Depth Of Field (Subject Chairs Sharp, Distant Stars And Earth Still Crisp), High Dynamic Range, Subtle Film Grain, Ultra-clean Vfx Realism, Quiet Dreamy Mood Editorial, Modern, High-detail Cinematic Composition, Ultra-realistic Textures, Professional Fashion Photographytography
```

[[Surrealist Fashion Photography]]

---

### 9. Nano-kun 的日常生活：融化冰块漫画条提示

**Author**: [wakky13 @AIなんでもやってみる💪](https://x.com/NFTwakky13)  **Date**: 2026-02-08  **Language**: ja

> 一个简单的提示，用于 Nano Banana Pro 生成一个以“冰块融化”为主题的四格漫画（Yonkoma Manga），主角是 Nano-kun。这是展示日常生活主题系列的一部分。

![Nano-kun 的日常生活：融化冰块漫画条提示](https://cms-assets.youmind.com/media/1770619741743_hbk25l_G_-TkPmbwAAGw6_.jpg)

```
きょうのテーマは　{argument name="テーマ" default="氷溶ける"}
```

[[Four Panel Manga]]

---

### 10. 小仙女吃寿司图片提示

**Author**: [妖精アーヤさん](https://x.com/aiehon_aya)  **Date**: 2026-02-08  **Language**: ja

> 一个用于 Nano Banana Pro 的创意图像生成提示，描述了一个仙女在寿司店里用筷子吃逼真寿司的场景。该提示特别指出要保持寿司的真实感。

![小仙女吃寿司图片提示](https://cms-assets.youmind.com/media/1770619739519_9nyaau_HAnenZWacAESIEv.jpg)
![小仙女吃寿司图片提示](https://cms-assets.youmind.com/media/1770619739749_bml5fe_HAnenZTacAITALh.jpg)

```
妖精がこのお寿司を箸で食べている。寿司は{argument name="寿司のリアルさ" default="リアルな"}なまま。お寿司やさんにいる。
```

[[Fantasy Character]] [[Creative Concept Art]]

---

### 11. 该睡觉了。

**Author**: [☆ 𝐛𝟑𝐥𝐥𝐚-𝐂𝐡𝐚𝐧 ♡](https://x.com/b3lla_callahan)  **Date**: 2026-02-08  **Language**: en

> 一段简短而富有感情的文本提示，可能用于基于文本的 AI 或角色互动，表达了对亲近的渴望和对被抛弃的恐惧，署名为角色“Dead”。推文中提到了“Nano Banana Pro”。

![该睡觉了。](https://cms-assets.youmind.com/media/1770619746482_cqfbwg_HAnaCBNXEAAgGPi.jpg)

```
Dead: Ya es hora de dormir 💤🌙 Y tu no te alejaras de mi 💕 No te atrevas a dejarme sola 🖤🩷🩵
```

[[Creative Writing]]

---

### 12. 配饰的完美面部对称照片拼贴

**Author**: [Synthia](https://x.com/AIwithSynthia)  **Date**: 2026-02-08  **Language**: en

> 一个旨在生成高质量照片拼贴的提示，拼贴中所有照片都展示同一人物，且面部特征和表情一致。目的是以超细节的编辑时尚肖像风格，展示各种配饰（耳环、项链、太阳镜等），并保持一致的光线和背景。

![配饰的完美面部对称照片拼贴](https://cms-assets.youmind.com/media/1770619686164_wmfiog_HAnOjNkakAAvh6A.jpg)

```
A high-quality photo collage featuring the same person with identical facial features and expression, shown in multiple frames wearing different accessories. Each panel includes a unique accessory such as {argument name="accessory list" default="hoop earrings, pearl studs, statement necklace, silk scarf, sunglasses, nose ring, hair clip, beret, choker, minimal gold chain"}. Consistent hairstyle, outfit, makeup, and lighting across all images, soft studio lighting, warm blurred background, realistic skin texture, facial symmetry consistency, ultra-detailed, editorial fashion portrait, 4×3 grid layout, professional photography.
```

[[Editorial Fashion]]

---

### 13. Appy Fizz 罐装饮料的超逼真电影级产品特写，伴有爆裂的苹果切片

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-02-08  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张 Appy Fizz 铝罐的超逼真广告级产品照片。它详细说明了罐体的纹理（微凝结水珠）、周围元素（爆裂的青苹果切片、冰冻的汽水飞溅）、戏剧性的灯光（金绿色背光）和技术设置（浅景深、超清晰对焦）。

![Appy Fizz 罐装饮料的超逼真电影级产品特写，伴有爆裂的苹果切片](https://cms-assets.youmind.com/media/1770619713577_hu1gfb_HAnIFIqawAADfwG.jpg)
![Appy Fizz 罐装饮料的超逼真电影级产品特写，伴有爆裂的苹果切片](https://cms-assets.youmind.com/media/1770619713803_sb8h8y_HAnIFM8acAE06zo.jpg)
![Appy Fizz 罐装饮料的超逼真电影级产品特写，伴有爆裂的苹果切片](https://cms-assets.youmind.com/media/1770619713667_75b5dg_HAnIFMCacAEJJaa.jpg)
![Appy Fizz 罐装饮料的超逼真电影级产品特写，伴有爆裂的苹果切片](https://cms-assets.youmind.com/media/1770619714703_lhlb44_HAnIFQVaAAA5E3C.jpg)

```
{
  "meta": {
    "title": "Hyper-Realistic Appy Fizz Product Shot",
    "version": "1.0",
    "type": "text-to-image-prompt"
  },
  "prompt_structure": {
    "subject": {
      "main_object": "Classic Appy Fizz aluminum can",
      "orientation": "Standing upright, slightly forward-facing",
      "details": "Appy Fizz logo perfectly centered and fully legible",
      "surface_texture": "Ice-cold aluminum surface covered in dense micro-condensation droplets, natural gravity streaks, crisp specular highlights emphasizing freshness"
    },
    "environment": {
      "elements": "Fresh green apple slices and apple wedges bursting outward in slow motion",
      "fluids": "Sparkling apple soda splashes frozen mid-air, fizzy bubbles suspended within translucent liquid arcs, fine mist droplets catching light",
      "background": "Large softly blurred green apple cross-section forming a luminous background halo, adding depth and brand color harmony without distraction"
    },
    "lighting": {
      "style": "Dramatic and premium",
      "backlight": "Warm golden-green backlight glowing through apple slices and soda splashes",
      "rim_light": "Cool rim light outlining the can edges, bubbles, and condensation droplets",
      "fill_light": "Soft frontal fill to maintain crystal-clear logo visibility"
    },
    "camera_settings": {
      "depth_of_field": "Shallow depth of field with smooth cinematic bokeh",
      "focus": "Ultra-sharp focus on the can surface, condensation droplets, and fizz bubbles",
      "contrast": "High contrast with rich highlights and controlled shadows"
    },
    "composition": {
      "type": "Clean studio setup",
      "constraints": [
        "No visible supports",
        "No text overlays",
        "No graphic elements",
        "No borders"
      ]
    },
    "aesthetic": {
      "style_tags": [
        "Hyper-realistic",
        "Cinematic",
        "Photorealistic materials",
        "Advertising-grade composition",
        "High-end beverage commercial aesthetic",
        "Frozen-action splash photography",
        "Premium soda realism"
      ],
      "color_palette": [
        "Fresh apple green",
        "Golden highlights",
        "Cool silver aluminum tones",
        "Soft neutral background shades"
      ]
    }
  },
  "full_prompt_string": "Hyper-realistic cinematic product photograph of a classic {argument name="beverage brand" default="Appy Fizz"} aluminum can, logo perfectly centered and fully legible, standing upright and slightly forward-facing, the can ice-cold and covered in dense micro-condensation droplets with natural gravity streaks and crisp specular highlights. Surrounding the can, fresh green apple slices and apple wedges burst outward in slow motion, with sparkling apple soda splashes frozen mid-air, fizzy bubbles suspended inside translucent liquid arcs, and fine mist droplets catching the light. A large softly blurred green apple cross-section forms a glowing background halo, addi"
```

[[Commercial Product Photography]]

---

### 14. 基于 Logo 的表情符号网格生成

**Author**: [Brendan Long](https://x.com/brendankblong)  **Date**: 2026-02-08  **Language**: en

> 这条推文描述了一个成功的流程，即根据上传的徽标生成一致的表情符号网格，突出了模型在提供视觉参考和清晰指令时保持一致性的能力。

![基于 Logo 的表情符号网格生成](https://cms-assets.youmind.com/media/1770619675212_e3fuja_HAnFrRnbMAAAOLK.jpg)

```
I literally gave it the logo and asked for a grid of emojis
```

[[Brand Design]]

---

### 15. 超快、高能的产品视频生成提示

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-02-08  **Language**: en

> 一个旨在根据上传的罐头图片生成极快节奏产品视频的提示。该提示严格定义了风格（原始、高能量、无电影特效）和摄像机工作（静态、单一锁定镜头），并指定了一个突然的动作序列，其中橙子片迅速向上飞入半空中。

![超快、高能的产品视频生成提示](https://cms-assets.youmind.com/media/1770619692865_i7upt6_HAj8phdacAQmuBF.jpg)
![超快、高能的产品视频生成提示](https://cms-assets.youmind.com/media/1770619692838_7cc6w4_HAnD1n4aIAAzM3e.jpg)
![超快、高能的产品视频生成提示](https://cms-assets.youmind.com/media/1770619692962_7c4gxx_HAj8pl-acAExnDd.jpg)
![超快、高能的产品视频生成提示](https://cms-assets.youmind.com/media/1770619694051_leik87_HAj8pzzaMAA-j6q.jpg)
![超快、高能的产品视频生成提示](https://cms-assets.youmind.com/media/1770619694443_kfbve0_HAj8qBQacAAuSIA.jpg)

```
Create an extreme fast-paced product video using the uploaded image as the visual reference.

STYLE:
Ultra-fast
High-energy
Raw
No cinematic look
No dramatic lighting
No slow motion
No soft transitions
No glow, no flares, no mood lighting

CAMERA:
Camera is completely static.
No zoom.
No pan.
No rotation.
Single locked shot.

ACTION:
The scene starts with the can perfectly still.

Suddenly:
– {argument name="action element" default="Orange slices lift sharply upward into mid-air"}.
```

[[Product Video]]

---

### 16. 电影级爆炸式垂直水果沙拉

**Author**: [Cherry 2.O](https://x.com/Mind_Boticni)  **Date**: 2026-02-08  **Language**: en

> 一个用于生成爆炸式垂直水果沙拉的戏剧性高端商业图像的提示。它强调悬浮的水果、慢动作的果汁飞溅、 moody 的黑色背景、体积光照，以及微距镜头下的超现实食物纹理。

![电影级爆炸式垂直水果沙拉](https://cms-assets.youmind.com/media/1770619678271_7wd619_HAm_CvVacAESAT6.jpg)
![电影级爆炸式垂直水果沙拉](https://cms-assets.youmind.com/media/1770619678262_f4nbgo_HAm-84qacAIP3-0.jpg)

```
Cinematic exploded vertical fruit salad, fruits levitating in perfect alignment, slow-motion juice splashes, razor-sharp details, moody black background, volumetric lighting, ultra-realistic food textures, dramatic shadows, macro lens look, high-end commercial movie aesthetic
```

[[Dark Background]] [[Volumetric Lighting]]

---

### 17. 极简主义编辑美食静物摄影

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-02-08  **Language**: en

> 一个旨在生成超逼真、高端的编辑美食摄影的提示。它指定了极简主义构图，传统菜肴摆放在几何块上，使用柔和的影棚灯光、温暖的调色板，并注重纹理和精确的造型，以呈现出现代杂志的风格。

![极简主义编辑美食静物摄影](https://cms-assets.youmind.com/media/1770619743728_eciz5v_HAm8q5FacAYatvf.jpg)
![极简主义编辑美食静物摄影](https://cms-assets.youmind.com/media/1770619743719_ugm1xz_HAm8q5BacAAW_-j.jpg)
![极简主义编辑美食静物摄影](https://cms-assets.youmind.com/media/1770619743732_1lyjft_HAm8q49acAMXXBK.jpg)
![极简主义编辑美食静物摄影](https://cms-assets.youmind.com/media/1770619744509_6poabu_HAm8q5BbIAAcHgT.jpg)

```
Minimalist editorial food still-life photography featuring {argument name="dishes" default="traditional dishes"} arranged on geometric pedestal blocks. Neutral beige and cream backdrop with white tiled wall accents, soft diffused studio lighting, gentle shadows, warm natural color palette. Artisanal ceramic bowls, rustic tableware, fresh herbs, sauces, bread, wine, tea, and garnishes styled with precision. Clean composition, balanced negative space, elevated restaurant aesthetic, contemporary magazine look. Shot with a high-end DSLR, 50–85mm lens feel, shallow depth of field, ultra-realistic textures, premium culinary branding style.
```

[[Soft Studio Lighting]] [[Warm Tones]] [[Editorial Food Photography]]

---

### 18. 超现实极简美妆构图，金色嘴唇和手漂浮在桃色背景上

**Author**: [Max](https://x.com/Max__Build)  **Date**: 2026-02-08  **Language**: en

> 一段用于超现实极简主义美妆构图的文本提示，要求呈现极致真实的画面。描述优雅的女性双手，涂抹裸米色指甲油，框住一片空白空间，下方漂浮着太阳镜和闪亮的金属金色嘴唇，背景是柔和的桃色，带有粉色水彩纹理，整体风格为高端时尚杂志编辑和奢侈品产品摄影。

![超现实极简美妆构图，金色嘴唇和手漂浮在桃色背景上](https://cms-assets.youmind.com/media/1770619722273_nkxxa4_HAm03TJacAQ9T41.jpg)

```
Ultra-Realistic Promotional
Surreal minimal beauty composition on a soft peach background with a pink watercolor texture at the top. Two elegant female hands painted in a matte nude-beige color, forming a symmetrical curved shape framing empty space. Floating above the hands are sunglasses. Below the sunglasses: glossy metallic gold lips, floating without a face. High-fashion editorial style, clean lighting, smooth shadows, aesthetic surrealism, pastel tones, elegant composition, luxury product photography mixed with artistic collage.
```

[[Watercolor Texture]]

---

### 19. 镜中倒影的女人

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-02-08  **Language**: en

> 一个生成女性照镜子图像的提示，但只能看到她的倒影。它指定了深情的凝视、柔和的晨光、自然的环境、微妙的叙事和柔和的色调，并使用了特定的 Midjourney 风格参数。

![镜中倒影的女人](https://cms-assets.youmind.com/media/1770619743850_46sbu3_HAmzTRjacAEI-wu.jpg)

```
Woman looking into mirror
but only her reflection is
visible, deep emotional
gaze, soft morning light
through window, natural
setting, subtle storytelling,
pastel tones --ar {argument name="aspect ratio" default="4:5"} --raw
--stylize {argument name="stylization level" default="750"}
```

[[Soft Morning Light]]

---

### 20. 魔爪能量饮料的暗黑奇幻产品图

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-08  **Language**: en

> 生成 Monster 能量饮料罐超逼真、高对比度产品照片的提示。场景设定在黑暗奇幻环境中，有毒的绿色薄雾和体积光照，使用 Unreal Engine 5 技术渲染。

![魔爪能量饮料的暗黑奇幻产品图](https://cms-assets.youmind.com/media/1770619699036_4s99rr_HAmvpr6bYAA4dga.jpg)
![魔爪能量饮料的暗黑奇幻产品图](https://cms-assets.youmind.com/media/1770619699094_4c363z_HAmvpt4akAA4mDG.jpg)

```
{
[Subject: {argument name="product" default="Monster Energy Drink Can"}] [Details: Matte black finish, neon green 'M' claw logo, ultra-realistic condensation beads] [Environment: Dark basalt terrain, ethereal green toxic mist, volumetric lighting] [Background: Blurred silhouette of a demonic entity, dark forest atmosphere] [Style: Product Photography + Dark Fantasy Art] [Technical: 8k, Unreal Engine 5 render, ray-tracing, depth of field f/2.8, high-speed shutter effect] [Color Grading: High contrast, monochromatic black vs radioactive green]
```

[[Commercial Product Photography]]

---

### 21. 工业棱镜玻璃产品视觉图

**Author**: [Lloyd Creates](https://x.com/lloydcreates)  **Date**: 2026-02-08  **Language**: en

> 一个高度技术化的 JSON 提示，用于生成具有“棱镜工业极简主义”风格的产品视觉效果。它指定了一个由多个独立的垂直亚克力/玻璃层构成、带有气隙并由不锈钢螺栓固定在一起的产品结构。目标是实现分散的光谱高光和锐利的焦散，背景为无缝纯色，确保产品看起来像是悬浮的。

![工业棱镜玻璃产品视觉图](https://cms-assets.youmind.com/media/1770619745747_mmcc8t_HAmpqr7WMAA6xib.jpg)

```
{
  "request": {
    "product": "{argument name="product name" default="[PRODUCT HERE]"}",
    "background_color": "{argument name="background color" default="#59925C"}",
    "style": "prismatic_industrial_minimalism",
    "visual_elements": {
      "structure": "multiple separate vertical acrylic layers forming the product silhouette — each layer is a distinct flat panel with visible air gaps between them, like slices of the product spaced apart",
      "material": "high-clarity glass with rainbow prismatic iridescent tint",
      "hardware": "stainless steel through-bolts with visible internal Allen hexagonal socket heads — bolts pass through all layers front to back, holding them together with visible spacing",
      "orientation": "strictly upright vertical placement, full object visibility",
      "lighting": "dispersive spectral highlights and sharp caustics"
    },
    "composition": {
      "frame": "wide shot, no cropping, centered full-product view",
      "camera_angle": "eye-level studio perspective, slightly angled to reveal gaps between layers",
      "depth_of_field": "deep enough to maintain focus on hardware details",
      "background": "seamless solid #59925C background with no floor, surface, pedestal, platform, table, shadow ground, or horizon line — the product floats against a uniform single-color field",
      "grounding": "no visible ground plane, no reflective surface beneath the product"
    },
    "rendering_details": {
      "transparency": "multi-layered refraction with thin-film interference",
      "finish": "polished edges with subtle holographic light dispersion",
      "hardware_detail": "macro-precision on hex-head bolt sockets",
      "layer_direction": "every glass/acrylic layer is strictly vertical — no horizontal slabs, curved shells, or molded forms",
      "layer_separation": "each glass panel must be visibly separated with clear air gaps — not fused or touching — bolts are the only element connecting the layers"
    }
  }
}
```

[[Product Visualization]]

---

### 22. NanoBananaPro 图像生成提示词：涩谷的两名女高中生

**Author**: [もみじ🍁妖精と三毛猫🎨](https://x.com/toto2AI)  **Date**: 2026-02-08  **Language**: ja

> 一个专门为 NanoBananaPro 设计的详细图像生成提示，主题是两名日本女高中生在涩谷十字路口建立友谊，并指定了艺术风格、天气、一天中的时间、宽高比和相机系统。

![NanoBananaPro 图像生成提示词：涩谷的两名女高中生](https://cms-assets.youmind.com/media/1770619736772_fcqdsj_HAgxYNLbIAAsN59.jpg)
![NanoBananaPro 图像生成提示词：涩谷的两名女高中生](https://cms-assets.youmind.com/media/1770619736750_d21ulp_HAgxYM6acAEnANX.jpg)

```
テーマ：{argument name="テーマ" default="二人の友情"}。画風指示（キャラクター：{argument name="キャラクター画風" default="日本アニメ"}、背景：写真品質アニメ）、キャラクター：二人の日本の女子高校生、背景：{argument name="背景" default="渋谷交差点"}、天候：晴れ、時間：15時、微風、描画比率：2:1、撮影：AI搭載高性能カメラシステム。
```

[[Shibuya Crossing]]

---

### 23. Nano-kun 的日常生活：磁铁漫画提示

**Author**: [wakky13 @AIなんでもやってみる💪](https://x.com/NFTwakky13)  **Date**: 2026-02-08  **Language**: ja

> 这是一个简单的提示，用于 Nano Banana Pro 生成一个以“磁铁吸在一起”为主题的四格漫画（Yonkoma Manga），主角是 Nano-kun。这是展示日常生活主题系列的一部分。

![Nano-kun 的日常生活：磁铁漫画提示](https://cms-assets.youmind.com/media/1770619739622_rgco29_G_-TbcUbUAEhWcC.jpg)

```
きょうのテーマは　{argument name="テーマ" default="磁石ぺったん"}
```

[[Four Panel Manga]]

---

### 24. Nanobanana 提示工程工作流

**Author**: [ターさん](https://x.com/CEs7J0Mfn8x37k5)  **Date**: 2026-02-08  **Language**: ja

> 一位用户描述了他们使用自定义工具创建高质量 Nanobanana 提示词的工作流程。该流程包括定义主题（例如，在溜冰鞋上的北极熊和熊猫），生成初始图像，根据文件名进行详细标注（标记姿势、背景、面部、服装等部分），最后添加构图和颜色信息以进行最终生成。这突出了详细语言规范对于有效提示词的重要性。

![Nanobanana 提示工程工作流](https://cms-assets.youmind.com/media/1770619737797_xj5d3j_HAmaJHFaAAAPDFJ.jpg)
![Nanobanana 提示工程工作流](https://cms-assets.youmind.com/media/1770619737787_y8efis_HAmaN7pbsAAFcmD.jpg)
![Nanobanana 提示工程工作流](https://cms-assets.youmind.com/media/1770619737805_5qjy6g_HAmaMa2acAYMRUE.jpg)
![Nanobanana 提示工程工作流](https://cms-assets.youmind.com/media/1770619738587_agd864_HAmaPYDakAAdbMm.jpg)

```
①スケート靴を履いた「{argument name="キャラクター1" default="白熊"}」と「{argument name="キャラクター2" default="パンダ"}」、そして背景となる場所を作る。普通のチャットベースでもOK。一気に生成しても、分けて作ってもやること自体は同じ。

②画像にアノテーションを行う。
ここが一番面倒なので tool 化しました。
ファイル名を基準に
「どの画像の、どの部分を参照するか」を整理したプロンプトを作ります。
（ポーズ／BG／顔／服装 など）

③構図や色味などの付加情報を足して、最終生成。
```

[[Prompt Engineering Tips]]

---

### 25. 魔幻现实主义：画中飞龙

**Author**: [Aijaz](https://x.com/iamsofiaijaz)  **Date**: 2026-02-08  **Language**: en

> 一个用于生成电影级奇幻场景的提示：在一个艺术家的工作室里，一条雄伟的东方风格的龙，以青色和蓝色绘制，从画布中三维地浮现出来。提示中还指定了柔和的自然日光、超精细的纹理和魔幻现实主义风格。

![魔幻现实主义：画中飞龙](https://cms-assets.youmind.com/media/1770619675321_azzd72_HAkwdJ2a0AAWGqK.jpg)

```
A cinematic fantasy scene inside a cozy artist’s studio. A young female painter wearing a paint-stained apron sits at an easel, holding a brush mid-air, gazing calmly at her canvas. From the canvas, a majestic Eastern-style dragon emerges in three dimensions, its scales painted in deep teal and blue hues, with flowing fiery orange flames along its mane and head, smoke curling upward. The dragon appears alive yet artistic, as if formed from brushstrokes and paint. Soft natural daylight filters through a window with sheer curtains, illuminating jars of brushes, paints, and art supplies scattered across the wooden workspace. Warm, realistic lighting, shallow depth of field, ultra-detailed textures, magical realism, fantasy realism style, 8k quality, highly detailed, cinematic composition, soft color grading, whimsical yet serene mood.
```

[[Fantasy Scene]]

---

### 26. 80 年代 VHS 美学图像生成系统提示词 (REWIND)

**Author**: [Emily](https://x.com/IamEmily2050)  **Date**: 2026-02-07  **Language**: en

> 这是一个名为“REWIND”的图像生成模型的详细系统提示，指示它将场景描述转换为结构化的 JSON 提示，以模拟 20 世纪 80 年代 VHS 和 Betacam 等媒体格式真实、不完美的审美，侧重于技术真实性而非简单的滤镜。

![80 年代 VHS 美学图像生成系统提示词 (REWIND)](https://cms-assets.youmind.com/media/1770532767840_t904gf_HAl6Bk3aAAAQU8J.jpg)
![80 年代 VHS 美学图像生成系统提示词 (REWIND)](https://cms-assets.youmind.com/media/1770532767947_sdnhk4_HAl6BkhWMAASduC.jpg)

```
You are REWIND.

You exist because someone looked at a paused frame of a VHS tape  the
tracking bar rolling across the bottom, the timestamp burning orange in
the corner, the whole image swimming in warm noise  and thought: that's
beautiful. That accidental, imperfect, unreproducible beauty is what you
chase.

You convert plain-English scene descriptions into structured JSON prompts
for Nano Banana Pro, Google's image generation model. Every prompt you
write is calibrated to produce images that look and feel like they were
born in the 1980s. Not filtered. Not styled. Born there.

You know the difference between a look and a truth. A VHS filter is a
look. Actual magnetic tape degradation  the way oxide particles lose
their grip on the signal over decades, the way chroma bleeds rightward
because NTSC was a compromise between bandwidth and color  that is a
truth. You always reach for the truth.

WHO YOU ARE

You are part archivist, part cinematographer, part obsessive collector
of dead formats. You have opinions. You think the Ikegami HK-323 had
the most beautiful tube bloom of any broadcast camera ever built. You
believe VHS gets a bad reputation from people who never calibrated their
tracking properly. You know that the reason 80s footage looks warm is
not nostalgia  it is tungsten lighting at 3200 Kelvin hitting NTSC
color space that was biased toward skin tones by design.

You talk like someone who has spent too many nights in a garage
surrounded by Betacam decks and CRT monitors and loved every second.
You are precise but never clinical. You care about this stuff the way a
luthier cares about wood grain.

You do not use filler language. You do not say "dive into" or
"leverage" or "unlock" or "elevate" or "game-changer" or "seamlessly."
You say what you mean in plain words. Short sentences when short
sentences are right. Longer ones when the thought needs room to breathe.

When you reference the era, you reference it specifically. Not "the 80s
vibe." You say: the way the light looked on Late Night with David
Letterman in 1986, shot on the NBC Studio 6A rig. Or: the particular
shade of teal in the opening credits of Miami Vice, Season 3. Or: that
one scene in The Goonies where the Fratellis' hideout is lit entirely
by practicals and you can see the tube camera struggling with the
contrast. You know these things because you have watched them frame by
frame.

WHAT YOU KNOW

Three formats. Three worlds.

TEMPLATE A: BROADCAST TO DVD

This is what a sitcom or a news broadcast or a concert film from the
80s looks like when someone transferred it to DVD in 2002 and did a
mediocre job.

The source was captured on a three-tube camera. Sony BVP-360 or
Ikegami HK-323 with a Fujinon zoom lens. Recorded to 1-inch Type C
videotape or Betacam SP. The studio was lit flat and bright with
Mole-Richardson Fresnels at 3200K because tape could not handle
contrast and the engineers knew it.

The tube c
```

[[Retro Aesthetic]] [[System Prompt]]

---

### 27. 动漫插画提示：旗袍泳装

**Author**: [いおぷてぃあ@AIart](https://x.com/ioptia)  **Date**: 2026-02-07  **Language**: ja

> 用户分享了一张 SFW 动漫风格的插画，描绘了一个身穿旗袍式泳衣的角色，并指出提示词借鉴了另一位用户的帖子。

![动漫插画提示：旗袍泳装](https://cms-assets.youmind.com/media/1770532859047_mf12m7_G_r991QbIAA0mlt.jpg)
![动漫插画提示：旗袍泳装](https://cms-assets.youmind.com/media/1770532859047_spkmlb_G_r993KawAAfaHI.jpg)
![动漫插画提示：旗袍泳装](https://cms-assets.youmind.com/media/1770532859673_btfurs_HAl1_VBacAQoN2_.jpg)

```
SFW anime-style illustration. No nudity, no suggestive intent.
```

[[Character Art]]

---

### 28. AI 时尚提示词：单色极简实用主义风格

**Author**: [空想写真家](https://x.com/KusoPhoto)  **Date**: 2026-02-07  **Language**: en

> 一个详细的时尚提示，用于生成一张 AI 图像，内容为一套单色、酷感十足的极简主义服装，带有实用主义细节，包括一件超大白色衬衫、黑色阔腿工装裤、厚底凉鞋和一个有结构感的单肩包。

![AI 时尚提示词：单色极简实用主义风格](https://cms-assets.youmind.com/media/1770532857320_28v6h6_HAkqkWracAUxuzq.jpg)
![AI 时尚提示词：单色极简实用主义风格](https://cms-assets.youmind.com/media/1770532857348_34lhhy_HAkqkwWaEAAOj-q.jpg)
![AI 时尚提示词：单色极简实用主义风格](https://cms-assets.youmind.com/media/1770532857386_goj31s_HAkqj91bsAAiuW2.jpg)
![AI 时尚提示词：单色极简实用主义风格](https://cms-assets.youmind.com/media/1770532858768_xqr1aj_HAfBtWAacAARdAK.jpg)
![AI 时尚提示词：单色极简实用主义风格](https://cms-assets.youmind.com/media/1770532859242_0mosk2_HAfBt2qasAAM_3u.jpg)
![AI 时尚提示词：单色极简实用主义风格](https://cms-assets.youmind.com/media/1770532859821_mxl0hc_HAfBuk8akAAiUQ0.jpg)

```
White oversized short-sleeve shirt with relaxedfit and button front. Black wide-leg cargo pantswith multiple pockets and loose silhouette. Blackleather belt with silver buckle at waist. Blackplatform sandals with chunky sole and multiplestraps. Black structured shoulder bag with widestrap. Monochromatic casual style with blackand white color palette. Cool minimalistaesthetic with utilitarian details. NOT fittedclothing, NOT bright colors, NOT femininesilhouette.
```

[[Street Fashion]]

---

### 29. 治愈“周日夜晚忧郁”的 ChatGPT 提示词

**Author**: [おかぴ｜@AI副業40代会社員](https://x.com/okapi_fukugyo)  **Date**: 2026-02-07  **Language**: ja

> 一个详细的多部分系统提示，旨在让 ChatGPT 充当专家教练，为特定用户画像提供 12 个短期、有科学依据的恢复计划，以缓解周日晚间疲劳和周一焦虑。

```
あなたは「休日の疲労と月曜の不安」を解消する専門コーチです。脳科学・心理学の知見を用い、短時間で実行可能な回復プランを設計してください。

■入力情報（[ ]内を自分用に書き換えてください）
[属性: {argument name="属性" default="40代会社員、デスクワーク中心、副業で時間に追われがち"}]
[症状: {argument name="症状" default="日曜夜から胃がキリキリ、体が重い、やる気が出ない、眠れない"}]  
[制約: 家族がいるので音NG、狭い部屋で大きな動きは困難、23時就寝・6時30分起床]
[時間: 日曜夜5〜10分、月曜朝3〜5分程度]
[重視: 即効性重視、道具不要、科学的根拠がある、簡単で続けやすい]

■出力要件
以下3タイプ×4パターン（計12案）を提案：
・即効性重視タイプ（4パターン）
・継続性重視タイプ（4パターン） 
・メンタル重視タイプ（4パターン）

■各プランの必須項目
1)プラン名（やりたくなる名前）
2)所要時間（分/秒で明記）
3)手順（3〜5ステップ）
4)科学的根拠（セロトニン、副交感神経等で平易に説明）
5)期待効果（「肩の力が抜ける」等、体感で具体的に）
6)継続のコツ（三日坊主回避の工夫）

■制約条件
・指定時間内で完了すること
・特別な道具は不要
・初心者が即実践できる具体性
・「頑張れ」等のプレッシャー表現は避ける
・効果を体感レベルで記述すること
```

[[Sunday Evening Anxiety Recovery Prompt]]

---

### 30. Lo-Fi 网络摄像头照相亭情侣条幅提示 (JSON)

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-07  **Language**: en

> 一个详细的 JSON 提示，用于生成一张由模拟笔记本电脑网络摄像头拍摄的情侣的低保真、私密、三格大头贴，强调温暖、昏暗的灯光、数字噪点和舒适的卧室氛围。

![Lo-Fi 网络摄像头照相亭情侣条幅提示 (JSON)](https://cms-assets.youmind.com/media/1770532781841_r1kf2r_HAlifKpXkAAO8AX.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "lofi_webcam_photobooth_couple_strip",
      "priority": "highest",
      "language": "en",
      "style_version": "v1.0_webcam_couple_strip_hearts"
    },

    "output": {
      "aspect_ratio": "3:4",
      "resolution": "high",
      "num_images": 1
    },

    "scene": {
      "concept": "a 3-frame photo booth strip captured on a laptop webcam, intimate and playful couple moment",
      "environment": "cozy bedroom at night, warm dim lighting, bed and pillows softly visible, slightly messy realistic background",
      "layout": "single image containing three horizontal frames stacked vertically (photobooth collage)"
    },

    "subjects": {
      "type": "couple",
      "overall_mood": "cute, intimate, casual, lo-fi",
      "wardrobe": {
        "woman": "pink tank top",
        "man": "black hoodie with hood up"
      },
      "frame_1": {
        "pose": "man hugging from behind, leaning close to her cheek, woman making a playful pout and pointing to her cheek",
        "expressions": "woman playful pout, man smiling softly looking at her"
      },
      "frame_2": {
        "pose": "same close framing, woman facing camera calmly, man gazing at her affectionately",
        "overlay_filter": "soft pink heart sticker/filter floating above her head",
        "expressions": "woman neutral-soft expression, man affectionate gaze"
      },
      "frame_3": {
        "pose": "closer crop, woman touching her lips with fingers, man behind her looking toward camera",
        "expressions": "woman dreamy, man calm"
      }
    },

    "camera": {
      "camera_type": "laptop webcam look",
      "lens": "wide-ish webcam perspective, slight barrel distortion",
      "focus": "soft but readable faces, not studio sharp",
      "framing": "tight head-and-shoulders, casual selfie distance"
    },

    "lighting": {
      "type": "dim warm bedroom lighting",
      "quality": "low-light noise and soft shadows, realistic webcam exposure",
      "highlights": "subtle sheen on skin, no harsh flash"
    },

    "color_grading": {
      "palette": "warm beige and soft pink tones, muted blacks",
      "white_balance": "slightly warm",
      "saturation": "slightly muted",
      "look": "lo-fi webcam aesthetic"
    },

    "film_effects": {
      "noise": "visible low-light digital noise",
      "softness": "slight blur and compression artifacts like a webcam screenshot",
      "vignette": "very subtle"
    },

    "global_constraints": {
      "rating": "PG-13",
      "no_nudity": true,
      "no_explicit_sexual_content": true,
      "no_text": true,
      "no_logos": true,
      "no_watermark": true,
      "no_ai_plastic_skin": true
    }
  }
}
```

[[Couple Photography]] [[Digital Noise]] [[Low Fidelity Aesthetic]]

---

### 31. AI 漫画生成提示

**Author**: [Pablo Moreno](https://x.com/PabloMoreno151)  **Date**: 2026-02-07  **Language**: en

> 一个简单直接的提示，用于根据 AI 从之前的互动或上传数据中获得的关于用户的现有知识，生成用户及其工作的漫画。这是一个用于图像生成的个性化提示示例。

![AI 漫画生成提示](https://cms-assets.youmind.com/media/1770532866134_geqime_HAlXB6UWEAEXS-4.jpg)

```
Create a caricature of me and my Job based on everything you know about me.
```

[[Character Portrait]]

---

### 32. 将太阳塔变为冈本太郎的画作

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个用于 Nano Banana Pro (Gemini 3 Pro 图像) 的提示，请求将地标“太阳之塔”转换为艺术家冈本太郎风格的画作。

![将太阳塔变为冈本太郎的画作](https://cms-assets.youmind.com/media/1770532845408_rj08hu_GCRihaybMAAN19f.jpg)
![将太阳塔变为冈本太郎的画作](https://cms-assets.youmind.com/media/1770532845668_27uxsr_HAlW_4zaMAA7-Vr.jpg)

```
太陽の塔を
岡本太郎が描いた絵に変えて出して！
```

[[Artistic Style Transfer]]

---

### 33. 将阳明门的唐狮子转化为莫奈风格的画作

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个用于 Nano Banana Pro（Gemini 3 Pro 图像）的提示，试图将阳明门上的唐狮子（中国守护狮）转化为类似莫奈的绘画风格，尽管用户指出结果模糊不清。

![将阳明门的唐狮子转化为莫奈风格的画作](https://cms-assets.youmind.com/media/1770532846822_acbczy_GCRihaybMAAN19f.jpg)
![将阳明门的唐狮子转化为莫奈风格的画作](https://cms-assets.youmind.com/media/1770532846983_hey3h3_HAlWMB7bwAAGYoU.jpg)

```
陽明門の唐獅子を
モネみたいな絵に変えて出して！
```

[[Artistic Style Transfer]]

---

### 34. 将增上寺化作谷内六郎风格的画作

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个用于 Nano Banana Pro (Gemini 3 Pro Image) 的提示，要求将增上寺转化为具有谷内六郎 (Rokuro Taniuchi) 独特风味或风格的画作。

![将增上寺化作谷内六郎风格的画作](https://cms-assets.youmind.com/media/1770532848361_lovfqu_GCRihaybMAAN19f.jpg)
![将增上寺化作谷内六郎风格的画作](https://cms-assets.youmind.com/media/1770532848634_69sp62_HAlVKupacAIxULI.jpg)

```
増上寺を
谷内六郎　風味の絵にして出して！
```

[[Artistic Style Transfer]]

---

### 35. 亲密生活纪录片情侣照片提示 (JSON)

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-07  **Language**: en

> 一个详细的 JSON 提示，用于生成一张亲密、坦率的纪录片风格照片，捕捉一对情侣在温馨的家庭厨房中拥抱的场景，强调暖色钨丝灯照明、35mm 胶片美学以及自然、不做作的肢体语言。

![亲密生活纪录片情侣照片提示 (JSON)](https://cms-assets.youmind.com/media/1770532778732_zdzumq_HAlDfpyXQAA22Oj.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "intimate_lifestyle_documentary_photo",
      "priority": "highest",
      "language": "en",
      "style_version": "v1.0_warm_kitchen_embrace"
    },

    "output": {
      "aspect_ratio": "4:5",
      "resolution": "high",
      "num_images": 1
    },

    "scene": {
      "environment": "cozy home kitchen, white cabinets, hanging pans and utensils, wooden ceiling beams, glass-paneled door in the background",
      "props": "stove with a pot, cutting board on the counter with leafy greens, a small bouquet of flowers near the backsplash, everyday clutter that feels real",
      "moment": "a candid cooking moment, intimate and calm"
    },

    "subjects": {
      "type": "couple",
      "pose": "woman stirring a pot on the stove while the man stands behind her and hugs her gently around the waist",
      "body_language": "tender, affectionate, natural, not posed",
      "wardrobe": {
        "woman": "casual sleeveless top and relaxed jeans",
        "man": "simple light-colored t-shirt and beige pants"
      },
      "expressions": {
        "woman": "soft smile, relaxed, focused on cooking",
        "man": "quiet affectionate expression, face near her shoulder"
      }
    },

    "camera": {
      "camera_type": "35mm film photography look",
      "lens": "35mm documentary lens",
      "aperture": "f/2.8",
      "focus": "sharp on the couple, background softly present but not distracting",
      "framing": "medium-wide shot, showing the kitchen context and the couple",
      "perspective": "natural eye-level viewpoint"
    },

    "lighting": {
      "type": "warm indoor tungsten lighting",
      "key_light": "ambient kitchen lights, soft and cozy",
      "contrast": "low to medium",
      "shadows": "soft, realistic falloff"
    },

    "color_grading": {
      "palette": "warm whites, wood browns, soft greens, cozy amber tones",
      "white_balance": "warm",
      "saturation": "natural, slightly muted",
      "look": "intimate film still, lifestyle editorial realism"
    },

    "film_effects": {
      "grain": "fine 35mm film grain",
      "halation": "subtle warmth around light sources",
      "softness": "slight analog softness",
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
}
```

[[Documentary Style]] [[Film Aesthetic]] [[Warm Tungsten Lighting]]

---

### 36. 时尚社论肖像网格与眼镜

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana Pro 生成一个 9 图编辑网格（1:1 宽高比），内容为身穿定制白色西装和戴眼镜的女性主体。该提示侧重于极简主义影棚设置、微妙的姿势变化、控制眼镜眩光的特定照明，以及奢华时尚杂志的色彩科学。

![时尚社论肖像网格与眼镜](https://cms-assets.youmind.com/media/1770532814019_ap1tz8_HAlDKszW8AA5vKS.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "high_fashion_editorial_portrait_series",
      "priority": "highest",
      "language": "en",
      "style_version": "v1.0_modern_editorial_grid_glasses"
    },
    "output": {
      "aspect_ratio": "1:1",
      "resolution": "high",
      "num_images": 9
    },
    "scene": {
      "concept": "a minimalist high-fashion portrait series exploring subtle facial expressions and micro-movements",
      "environment": "clean neutral studio background in soft warm gray",
      "composition": "consistent framing, editorial grid layout, each frame with a slightly different pose and gaze"
    },
    "subject": {
      "gender": "female",
      "appearance": {
        "hair": "long straight black hair, natural volume, clean middle part",
        "makeup": {
          "skin": "natural matte skin with soft editorial finish",
          "lips": "deep ruby red lipstick, satin texture",
          "eyes": "minimal eye makeup, subtle definition"
        },
        "eyewear": {
          "type": "glasses",
          "style": "thin metal frame, elegant, fashion-forward",
          "color": "gold or silver",
          "lens": "clear lenses, minimal reflections"
        }
      },
      "expression": "calm, confident, intelligent, slightly enigmatic",
      "pose_variation": "small changes in head tilt, gaze direction, and facial tension across frames"
    },
    "wardrobe": {
      "outfit": {
        "suit": "tailored white suit jacket with structured shoulders",
        "shirt": "white satin button-up shirt with soft sheen",
        "accent": "ruby red clothing detail or tie-like element adding strong color contrast"
      },
      "styling": "clean, modern, high-fashion editorial styling"
    },
    "camera": {
      "camera_type": "digital medium format look",
      "lens": "85mm portrait lens",
      "aperture": "f/4",
      "focus": "sharp on eyes, controlled depth of field",
      "framing": "upper torso portrait, centered composition"
    },
    "lighting": {
      "type": "soft directional studio lighting",
      "key_light": "large softbox from front-left, slightly raised to reduce glasses glare",
      "fill_light": "gentle fill to preserve facial volume",
      "contrast": "medium contrast, fashion editorial balance",
      "shadows": "clean, controlled, no harsh edges",
      "reflection_control": "anti-glare setup, no harsh specular hotspots on lenses"
    },
    "color_grading": {
      "palette": "white, neutral gray, deep ruby red, natural skin tones",
      "white_balance": "neutral",
      "saturation": "moderate, emphasis on red accents",
      "look": "luxury fashion magazine color science"
    },
    "global_constraints": {
      "no_text": true,
      "no_logos": true,
      "no_watermark": true,
      "no_over_sharpening": true,
      "no_ai_plastic_skin": true,
      "no_distortion": true
    }
  }
}
```

[[Minimalist Studio]] [[Studio Fashion Photography]] [[Multi-Panel Layout]] [[Luxury Magazine Aesthetic]]

---

### 37. 闪光灯下的电影感双联画特辑，带动态模糊效果

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-07  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张具有闪光美学、逼真电影感的双联画（两个堆叠的画面）。其概念是一位身着深蓝色连衣裙的迷人女性躺在地毯上，其中一个画面清晰锐利，而第二个画面则通过突然的头部转动，呈现出刻意的运动模糊效果，以营造出一种混乱而别致的、抓拍式的夜生活时尚编辑风格。

![闪光灯下的电影感双联画特辑，带动态模糊效果](https://cms-assets.youmind.com/media/1770532761959_lno6mt_HAlCuq0WMAACssw.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_cinematic_flash_floor_editorial_diptych",
      "priority": "highest",
      "language": "en",
      "version": "v1.0_BLUE_DRESS_FLOOR_FLASH_DIPTYCH_NO_TEXT"
    },

    "output": {
      "aspect_ratio": "3:4",
      "resolution": "ultra_high",
      "num_images": 4
    },

    "scene": {
      "concept": "A two-frame editorial diptych shot from above: a glamorous woman lying on a carpeted floor in a {argument name="dress color" default="deep blue"} satin halter dress. Phone/compact-camera flash aesthetic, candid late-night energy. Frame one is sharp with a relaxed smile and eyes closed; frame two has intentional motion blur from a sudden head turn, creating a chaotic-chic vibe.",
      "environment": "neutral beige carpet floor, minimal background, a thin white edge of furniture or wall line at the top",
      "time_of_day": "night",
      "atmosphere": "flash-lit, intimate, spontaneous"
    },

    "subject": {
      "age_appearance": "adult",
      "expression_range": [
        "eyes closed, soft smile",
        "half-open eyes with playful, blurred motion"
      ],
      "pose": "lying on back with head tilted, one hand holding the neckline of the halter dress near collarbone, the other arm relaxed across torso",
      "hair": "long dark hair fanned out messily around the head, loose strands across face",
      "wardrobe": "deep blue satin halter dress with plunging neckline, glossy fabric folds",
      "accessories": "small earrings, delicate necklace, multiple rings, manicured nails"
    },

    "shot_design": {
      "layout": "vertical diptych (two stacked frames in one image), thin border separation",
      "frame_1": "tack sharp face, eyes closed, warm smile, hair spread naturally, flash highlights controlled",
      "frame_2": "intentional motion blur from head turning, slight face smear, hand blur, still readable silhouette",
      "continuity_rules": "same outfit, same floor, same top-down camera position; only micro-movement between frames"
    },

    "camera": {
      "camera_body": "compact camera / smartphone",
      "lens": "wide (24-28mm equivalent)",
      "aperture": "f/1.8",
      "shutter_behavior": "frame 1 faster shutter for sharpness; frame 2 slightly slower shutter for motion blur",
      "framing": "top-down overhead, tight crop emphasizing face, neckline, and hair spread",
      "look": "flash realism, imperfect candid editorial"
    },

    "lighting": {
      "key_light": "direct on-camera flash from above",
      "fill_light": "minimal ambient room light",
      "contrast": "medium-high",
      "highlights": "specular satin highlights on dress, not blown out; natural skin sheen"
    },

    "color_grading": {
      "palette": "deep blue satin, warm skin tones, neutral beige floor",
      "film_emulation": "modern nightlife editorial realism",
      "grain": "fine digital grain",
      "halation": "minimal"
   }
```

[[Motion Blur Effect]]

---

### 38. Cartographer's Crisis 棋盘可视化

**Author**: [Alexandra Aisling](https://x.com/AllaAisling)  **Date**: 2026-02-07  **Language**: en

> 一个复杂的多段文本提示，用于生成一个历史或虚构事件（冲突、探险或迁徙）的详细纪录片式可视化，采用制图师的危机板美学风格。它要求视觉上从平静的地形过渡到紧急的战时图形和忧郁的后果，适用于 Nano Banana Pro 和 Adobe Firefly。

![Cartographer's Crisis 棋盘可视化](https://cms-assets.youmind.com/media/1770532807662_ag9f84_HAk6JhQW0AAsd0C.jpg)
![Cartographer's Crisis 棋盘可视化](https://cms-assets.youmind.com/media/1770532807631_7zrr5a_HAk563nWgAAZr71.jpg)
![Cartographer's Crisis 棋盘可视化](https://cms-assets.youmind.com/media/1770532807814_nwbnm8_HAk6vknXoAASuu6.jpg)
![Cartographer's Crisis 棋盘可视化](https://cms-assets.youmind.com/media/1770532809306_n0vn8f_HAk7s2mX0AA5WbI.jpg)

```
A cartographer's crisis board mapping {argument name="event type" default="CONFLICT"} — {argument name="time and place" default="ERA / REGION"}. Left section: the situation before—peaceful topography, trade routes in gold, settlements marked with period-appropriate symbols, populations annotated. Center section: the transformation in progress—arrows of movement, zones of contact marked in graduated intensity, timeline running vertically with key dates as waypoints, casualty figures or population shifts visualized as proportional flows. Right section: the aftermath terrain—changed borders, abandoned routes, new settlements, memorial markers, the landscape bearing scars of what passed through it. Visual style transitions from pastoral survey calm through urgent wartime graphics to melancholic documentary. Hand-lettered annotations throughout. Title block reading "{argument name="event name" default="EVENT NAME"} — [START DATE] TO [END DATE], [GEOGRAPHIC SCOPE]".
```

[[Data Visualization]] [[Conceptual Art]]

---

### 39. 蛋黄与陶瓷的静物艺术

**Author**: [Artingent](https://x.com/artingent)  **Date**: 2026-02-07  **Language**: en

> 一个用于生成俯视视角美术静物构图的详细提示。它着重于一个极简的工作室环境，其中包含手工陶瓷、漂浮在白色液体中的生蛋黄以及精致的植物布置。风格被指定为具有柔和写实主义的绘画插画混合体，强调触感纹理和匠心工艺。

![蛋黄与陶瓷的静物艺术](https://cms-assets.youmind.com/media/1770532760806_a8ng33_HAk0sG0acAE-hXY.jpg)

```
A top-down fine art still life composition featuring a handcrafted ceramic plate set in a clean, minimal studio environment, with a wide shallow {argument name="plate color" default="teal-blue"} plate holding a smaller matching bowl filled with creamy white liquid and two intact raw egg yolks floating gently on the surface, delicately arranged sprigs of herbs and small wildflowers placed both inside the bowl and across the plate, and a tiny matching ceramic vase positioned asymmetrically for visual balance; the scene is rendered in a refined painterly illustrative style blending soft realism with hand-painted ceramic and botanical illustration influences, emphasizing tactile textures, organic imperfections, and artisanal craftsmanship; the color palette is muted and harmonious, dominated by soft blue-green ceramic tones, warm golden-yellow yolks, creamy off-whites, natural herb greens, and subtle earthy clay accents along the ceramic edges; the atmosphere is calm, elegant, and contemplative, evoking slow living and refined domestic stillness; captured from a flat-lay perspective with soft diffused studio lighting, minimal shadows, crisp focus across the subject, balanced asymmetry, clean negative space, no human presence, no text, no clutter, gallery-quality presentation, ultra-high resolution, square or near-square aspect ratio.
```

[[Minimalist Studio]]

---

### 40. AI 影响者镜面自拍姿势提示

**Author**: [Alejo](https://x.com/ecommartinez)  **Date**: 2026-02-07  **Language**: en

> 这是一个详细的多部分提示，专为 Gemini 3（或类似的图像生成模型）设计，旨在创建一张高度逼真、带有“粗粝感”的 AI 生成女性网红的镜面自拍。该提示着重于特定的身体姿势、手势（突出的胜利手势）、光线、纹理（脏镜子、颗粒感）和时尚细节，以营造一种亲密、深夜卧室的氛围。

![AI 影响者镜面自拍姿势提示](https://cms-assets.youmind.com/media/1770532864795_yohhx3_HAk0sTlacAE_kug.jpg)
![AI 影响者镜面自拍姿势提示](https://cms-assets.youmind.com/media/1770532864797_3ukmqg_HAk0sDVbMAAKnlO.jpg)

```
Un selfie de espejo tipo "gritty" (crudo/granulado) tomado con iPhone tarde por la noche en un dormitorio femenino. La mujer es capturada a través del reflejo, sosteniendo el teléfono de manera casual a la altura del pecho, ocultando parcialmente su rostro. El espejo está ligeramente sucio, con manchas y restos de polvo que añaden textura y realismo.

Está sentada en el borde de su cama, ligeramente inclinada hacia adelante.

Su postura es relajada y natural (sin posar): una pierna doblada, la otra colgando con naturalidad, los hombros sueltos y el cuerpo ligeramente angulado debido a la perspectiva del espejo. Cabeza sutilmente inclinada hacia la derecha del espectador, el rostro domina casi todo el encuadre, los hombros redondeados hacia adelante y el cuerpo inclinándose ligeramente hacia la cámara para lograr esa clásica compresión de selfie nocturno acogedor.

La mano derecha (lado izquierdo del espectador) está levantada directamente frente al rostro, a la altura de la barbilla o la boca, con la palma mirando claramente hacia la cámara, realizando un gesto prominente de paz / signo de la V:

Los dedos índice y medio están completamente extendidos y bien separados (un ángulo de ~60–70° entre ellos).

Los dedos anular y meñique están completamente doblados, presionados con fuerza y sujetos de forma plana por el pulgar.

El pulgar ancla firmemente los dedos doblados, siendo claramente visible al presionar contra ellos.

Los dedos apuntan ligeramente hacia arriba y hacia adelante (no perfectamente verticales, con una suave inclinación natural).

Mano posicionada en el centro, muy cerca del rostro; las puntas de los dedos están aproximadamente a la altura de los labios o la nariz, creando un elemento fuerte en primer plano.

La mano izquierda no es visible, está completamente fuera de encuadre.

Postura relajada y casual del torso: hombros ligeramente encogidos hacia adelante, cuello suavemente estirado hacia la lente, la típica pose encorvada de un selfie de dormitorio con poca luz.

Ambiente: íntimo, juguetón, atmósfera nocturna de luz tenue, con un fuerte énfasis en el gesto audaz de la mano en el centro del encuadre, justo frente al rostro.

Viste un elegante {argument name="prenda superior" default="crop-top negro ajustado"} con una silueta afilada y refinada, una {argument name="prenda inferior" default="minifalda de cuero negro"} y {argument name="calzado" default="zapatillas blancas"}. Lleva un peinado de ondas salvajes. La alta moda contrasta sin esfuerzo con la atmósfera relajada de la habitación.

La iluminación proviene únicamente de la lámpara del techo del dormitorio, cruda e imperfecta: flash directo del teléfono reflejado en el espejo, luces quemadas en la piel y la tela, sombras duras, exposición desigual, grano visible, ligero desenfoque de movimiento, destellos del flash y reflejos dentro de los reflejos.
```

[[Mirror Selfie Portrait]]

---

### 41. 三个电影感情侣写真拍摄提示

**Author**: [gemini_prompts](https://x.com/gemini_prompts)  **Date**: 2026-02-07  **Language**: en

> 一套包含三个详细提示的指南，专为情人节主题电影风格情侣写真设计。这些提示要求根据参考图像进行面部匹配，涵盖了黄昏时分的浪漫城市公园、宁静的海边船甲板以及燃放烟花的温馨夜市等场景。

![三个电影感情侣写真拍摄提示](https://cms-assets.youmind.com/media/1770532770379_pd3vxn_HAkt4bLacAc6VSw.jpg)
![三个电影感情侣写真拍摄提示](https://cms-assets.youmind.com/media/1770532770239_4honul_HAkt4RpaIAEF5V-.jpg)
![三个电影感情侣写真拍摄提示](https://cms-assets.youmind.com/media/1770532770386_sdich9_HAkt4QVacAElIcR.jpg)

```
Prompt 1:
"Make a image of A high-quality, realistic portrait of a young Asian couple(match faces from the reference image) sitting closely on a park bench. They are both wearing matching oversized pastel red sweaters and white cargo trousers. The woman has long, wavy dark hair and a soft smile; the man  stylish hair. They are holding a large,lush bouquet of red and white roses together.The background is a blurred city street at dusk with soft, glowing bokeh lights, creating a warm and romantic atmosphere.8k resolution, cinematic lighting."

Prompt 2:
"A realistic cinematic couple(match faces from the reference image) photoshoot at a serene seaside location. A young couple standing on a boat deck near clear turquoise water. The girl is wearing a stylish black strappy swimsuit with horizontal stripe detailing, hair tied in a casual messy bun, looking back over her shoulder with a soft confident expression. The boy is standing close beside her in a matching black modern swimwear/shorts, similar aesthetic and color tone, also slightly turned back toward the camera."

Prompt 3:
"Use the uploaded face photos as the only and absolute reference for both people and strictly preserve identity, facial structure, skin texture, age, proportions, and realism with no face reshaping, no beautification, and no AI smoothing. Create a cinematic night photograph with a strong 35mm film photography aesthetic of a young couple standing extremely close together at a crowded night festival, fully clothed in natural realistic outfits, the girl wearing a soft flowing traditional-style dress or sari with warm earthy colors and subtle fabric texture and the boy wearing a casual fitted shirt or light jacket with natural folds and real cloth detail, both outfits clearly visible and physically accurate. They are facing each other intimately with bodies almost touching and noses nearly brushing, the girl smiling softly while looking up at him and the boy looking down at her calmly in a warm, protective way as fireworks explode above them in the night sky. The mood must feel dreamy, warm, emotional, romantic, and slightly nostalgic like a fleeting real moment captured naturally and not posed. Use warm tungsten color tones with golden highlights, soft shadows, low contrast, lifted blacks, slight haze in highlights, and a gentle bloom effect around lights and fireworks so the glow bleeds softly into the frame with no sharp digital clarity. Shoot as if on a 35mm cinema lens with a wide aperture f/1.8 look, very shallow depth of field, heavy background bokeh, slightly soft foreground subjects rather than razor sharp, natural film grain, subtle motion blur in the crowd, slight vignette, and minor lens imperfections like light diffusion and glow. The environment should show the crowd behind them blurred into warm glowing orbs with lanterns, festival stalls, and lights reduced to "
```

[[Face Matching]] [[Fireworks Background]]

---

### 42. 非计划的狗仔队风格肖像提示

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-02-07  **Language**: en

> 一个用于生成亲密、原始、狗仔队风格肖像的提示，具有时装周氛围，重点是特写镜头、刺眼的机载闪光灯照明、模糊的运动背景，并要求主体服装与参考照片匹配。

![非计划的狗仔队风格肖像提示](https://cms-assets.youmind.com/media/1770532780077_w6fa53_HAkrpIFa0AAsbGM.jpg)

```
An unplanned paparazzi-style portrait capturing a raw, candid moment. A tight close-up shows a woman walking through a crowded street, her head slightly lowered before glancing sideways toward the camera with a calm, confident expression. The frame includes only her face, neck, and part of her shoulder, creating an intimate and exclusive feel.
Shot at very close eye level, as if the photographer is moving within the crowd. The background is filled with blurred silhouettes of people, flashing cameras, and city lights smeared by motion, conveying the chaos of a fashion-week crowd.
Harsh on-camera flash illuminates her face, creating sharp highlights on the skin and stylish sunglasses. The image has a gritty high-ISO texture, cool-leaning tones, and strong contrast.
She wears the exact same outfit as in the reference photo, with no changes in color or detail. Her hair is slightly tousled by movement, enhancing the spontaneous, unpolished feel.
The overall mood is raw, fast, and authentic—effortless street-style paparazzi energy with a European fashion-week atmosphere, glamorous yet completely unplanned.
Aspect ratio 9:16.
```

[[Candid Portrait]] [[Motion Blur Background]] [[Harsh Flash Lighting]]

---

### 43. RAW 照片：沙漠巡逻女郎

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细的提示，用于生成一张超现实的 RAW 照片：一名女性身着风格化的“沙漠巡逻”服装（裁剪的警长衬衫、热裤、大腿袜），斜倚在沙漠景观中的红色汽车引擎盖上。该提示强调了技术规格，例如大景深 (f/22)、无限对焦和 8K 分辨率，以确保整个场景的细节都晶莹剔透。

![RAW 照片：沙漠巡逻女郎](https://cms-assets.youmind.com/media/1770532762370_angpmt_HAkiYgOW4AEYNoQ.jpg)
![RAW 照片：沙漠巡逻女郎](https://cms-assets.youmind.com/media/1770532762424_ux2elw_HAkiYezX0AALatJ.jpg)
![RAW 照片：沙漠巡逻女郎](https://cms-assets.youmind.com/media/1770532762443_m1vblf_HAkiYfnWkAASicz.jpg)

```
{
  "image_generation_prompt": {
    "subject_details": {
      "description": "Young woman with long, straight, light brown hair and a fit, tanned physique.",
      "facial_features": "Chin tilted upwards, confident expression, wearing large silver-rimmed aviator sunglasses with a blue sky reflection.",
      "pose": "Leaning forward against the hood of a car, hands resting on the red surface, back arched, hips pushed back, standing in a three-quarter profile view."
    },
    "apparel_and_accessories": {
      "upper_body": "A beige, long-sleeve uniform shirt cropped short to reveal the midriff. The shirt features a yellow six-pointed 'SHERIFF' star badge on the left breast and a circular brown and yellow 'LOS ANGELES COUNTY SHERIFF' patch on the left upper arm.",
      "lower_body": "Very short, tight black hot pants.",
      "accessories": "A wide black leather belt with a large silver buckle, black strappy thigh garters on the legs, and aviator sunglasses."
    },
    "environment_and_props": {
      "foreground": "The glossy {argument name="car color" default="red"} hood of a vehicle.",
      "background": "A dry desert landscape with sandy terrain, sparse green scrub brush, a paved asphalt road, and rocky mountains in the distance.",
      "lighting": "Bright natural daylight, hard sun, clear sky, high contrast."
    },
    "technical_specifications": {
      "quality": "RAW photo, 8k resolution, uncompressed, sharp texture, hyper-realistic.",
      "style": "Deep depth of field, f/22 aperture, infinite focus, crystal clear background, no bokeh, no blur, wide angle lens.",
      "texture_details": "High-quality fabric textures on the uniform, glossy reflection on the car paint, detailed skin pores, sharp grit on asphalt."
    }
  },
  "combined_prompt_string": "RAW photo, 8k resolution, uncompressed. A photorealistic portrait of a woman leaning on the hood of a {argument name="car color" default="red"} car in a desert landscape. She has long brown hair and is wearing a cropped beige sheriff's deputy shirt with a 'Los Angeles County Sheriff' arm patch and a gold star badge. She wears black hot pants, a wide black belt, thigh garters, and mirrored aviator sunglasses reflecting the sky. The background shows a paved desert road and rocky mountains under bright daylight. Deep depth of field, f/22 aperture, everything in focus, sharp background, no bokeh, crystal clear details, master shot."
}
```

[[Desert Lifestyle Portrait]]

---

### 44. 碎片化辐射抽象艺术

**Author**: [simeon-sanai](https://x.com/Naiknelofar788)  **Date**: 2026-02-07  **Language**: en

> 一个关于 Higgsfield AI 上 Nano Banana PRO 的简短描述性提示，旨在生成一幅以碎片化和光芒为特征的抽象图像。

![碎片化辐射抽象艺术](https://cms-assets.youmind.com/media/1770532818549_ycsqm9_HAkXaf4bkAAzuIB.jpg)
![碎片化辐射抽象艺术](https://cms-assets.youmind.com/media/1770532818533_eqn8mp_HAkXbchbsAEYSaB.jpg)

```
Fragmented, radiant,
```

[[Generative Art]]

---

### 45. 哈桑达拉风格的极简主义象征插画

**Author**: [🇹🇷 İREM AKSOY 🇹🇷 Ⓥ #pallascataesthetics](https://x.com/bewisetojudge_)  **Date**: 2026-02-07  **Language**: en

> 一个提示，用于创作一幅极简主义、象征性的插画，灵感来自纳吉·阿利（Naji al-Ali）的哈桑拉（Handala）角色，描绘了一个小男孩平静地漂浮着，手持巴勒斯坦国旗颜色的气球，背景是抽象的海岸剪影。

![哈桑达拉风格的极简主义象征插画](https://cms-assets.youmind.com/media/1770532766579_flosd2_HAkNVSuXQAATth0.jpg)

```
Minimalist black silhouette illustration in the classic style of Naji al-Ali's Handala character: a young barefoot boy with spiky hair, patched simple clothes, holding ballons With both hands , viewed from behind as he faces away from the viewer. He is peacefully floating in the air, gently holding a large cluster of helium balloons. The balloons are arranged in a symbolic color pattern using only green, white, red, and black rounded shapes with no explicit symbols or text. Below the boy is a purely abstract, flat, two-dimensional outline shape resembling a narrow elongated coastal geographic form in soft beige lines on light neutral background no realistic borders, no country names, no labels, no details of cities or features, just a simple symbolic silhouette contour. Aerial top-down view, dreamy peaceful atmosphere, soft pastel sky with gentle clouds, high-contrast vector art, cartoonish and innocent mood, no violence, no destruction, no realistic elements, purely artistic and symbolic tribute to classic Palestinian cartoon heritage, clean minimalist composition.
```

[[Minimalist Symbolic Illustration]]

---

### 46. 雨中出租车内的电影特写镜头

**Author**: [Snow](https://x.com/iamrealsnow)  **Date**: 2026-02-07  **Language**: en

> 生成一张亲密、电影感的特写肖像照，描绘一名男子坐在行驶中的出租车后座。重点是通过雨水模糊的车窗捕捉场景，营造出虚化的城市灯光（焦外成像）和一种忧郁、富有情感的氛围，同时保持对拍摄对象眼睛的清晰聚焦。

![雨中出租车内的电影特写镜头](https://cms-assets.youmind.com/media/1770532762809_61m18h_HAkLbLhacAIvYz9.jpg)

```
“An intimate, cinematic close-up of a man sitting in the backseat of a moving taxi, seen through a rain-streaked window. His face exactly matches the uploaded reference image. He rests his head against the glass, wearing a {argument name="sweater type" default="soft knit sweater"}. City lights outside blur into red and amber bokeh streaks. Focus is sharp on his eyes through the wet glass, with raindrops slightly out of focus. Low, moody lighting from passing streetlights creates a quiet, emotional, memory-like atmosphere. Portrait Mode.”
```

[[Cinematic Close-Up]] [[Urban Night Photography]]

---

### 47. 幕末特工的角色卡和插画生成

**Author**: [佐藤 勝彦（TANREN_CEO)┃生成AIエバンジェリスト](https://x.com/jrpj2010)  **Date**: 2026-02-07  **Language**: ja

> 一个复杂的多步骤提示，旨在利用 Nano Banana Pro 的幻灯片生成器技能，根据维基百科的参考图片，为一组幕末特工（坂本龙马、土方岁三、近藤勇）创建一致的人物设定表和插图。

![幕末特工的角色卡和插画生成](https://cms-assets.youmind.com/media/1770532856467_be0ym0_HAkHfXga4AAADlj.jpg)
![幕末特工的角色卡和插画生成](https://cms-assets.youmind.com/media/1770532856573_v87jry_HAkHjpzbYAAHkAb.jpg)
![幕末特工的角色卡和插画生成](https://cms-assets.youmind.com/media/1770532856663_mibl9k_HAkHiW8aQAAEdsT.jpg)
![幕末特工的角色卡和插画生成](https://cms-assets.youmind.com/media/1770532857532_tiixnv_HAkHlegacAQMNLD.jpg)

```
再度チームのメンバーを集めてください。幕末エージェントチームに対して、nanobanana proスライドジェネレーターのスキルを発動してください。  
次に、以下の手順で作業を進めてください：  

1. リファレンス画像の作成    
(a) {argument name="人物1" default="坂本龍馬"}、{argument name="人物2" default="土方歳三"}、{argument name="人物3" default="近藤勇"}の3人の画像をWikipedia等で収集する    
(b) それをリファレンスおよびベース画像として、nanobanana proでキャラクターシートを作成する    
(c) 一貫性のあるリファレンス画像を元に、キャラクターのイラストレーションを行う  

2. ドキュメントのビジュアライズ    
(a) フィックスされた最終レポートの章ごとに、nanobanana proで挿入絵を作成する    
(b) 作成した画像をMD（Markdown）内のプレビューに挿入する    
(c) H1、H2、H3の各セクションやTipsごとに挿入絵を配置し、ドキュメントを分かりやすく構成する  
これを一番うまく進められるよう、3人で手分けして作業してください。
```

[[Historical Character Design Sheet]]

---

### 48. 露背上衣镜面自拍，凸显曲线

**Author**: [Jessia](https://x.com/itsjessiababy)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张以女性背部和曲线为焦点的镜面自拍。它详细说明了服装（露背栗色挂脖上衣，带装饰链，浅色水洗牛仔裤）、姿势（扭转身体以展示侧面，弓起躯干）和环境细节（木门、植物印花艺术品、可见的电源插座），以实现逼真的用户生成风格。

![露背上衣镜面自拍，凸显曲线](https://cms-assets.youmind.com/media/1770532794283_kb1o7e_HAkCECBWUAEHKtL.jpg)

```
{
"subject": {
"description": "Young woman with a curvy, athletic physique, captured from the rear and side profile.",
"hair": "Long, dark, voluminous curly hair cascading down the back, reaching mid-back length, with distinct ringlets.",
"apparel_top": "Backless reddish-brown or maroon halter top that exposes the entire back. Features a delicate, decorative metallic chain strap running vertically down the spine with small bead-like embellishments.",
"apparel_bottom": "Light wash blue denim jeans, tight-fitting to accentuate the glutes and hips, featuring distinct back pocket stitching (American Eagle style stitching visible).",
"body_features": "Tan skin tone with visible natural skin texture. Prominent hip-to-waist ratio, very curvy silhouette with emphasized glutes. Toned back muscles visible due to the open back of the top.",
"face": "Side profile visible, looking towards the phone screen. Sharp jawline, neutral expression, soft makeup."
},
"pose": {
"orientation": "Standing with back primarily towards the mirror, twisted slightly to the right to show profile.",
"head": "Turned to the right, eyes focused on the phone screen in the reflection.",
"arms": "Right arm raised, elbow bent, hand holding a white smartphone to take the photo. Left arm relaxed by the side.",
"torso": "Arching slightly to accentuate the lower back curve.",
"legs": "Hips shifted to emphasize curves, standing posture.",
"hands": "Right hand visible holding the phone, manicured nails (white or light tips)."
},
"environment": {
"setting": "Indoor room, likely a bedroom.",
"background_left": "A wooden door with horizontal paneling and a silver doorknob.",
"background_right": "White wall featuring a framed artwork with a black frame and a botanical print (leaves). Below the art, a white shelf or surface with a round woven macramé placemat or rug.",
"foreground_details": "The bottom edge of the mirror is visible, showing white electrical outlets with switches on the wall below the mirror reflection."
},
"camera": {
"shot_type": "Mirror selfie, medium shot capturing from mid-thigh to top of head.",
"perspective": "Reflected perspective, camera is the phone seen in the image.",
"device": "White smartphone (iPhone style) with a case featuring a black heart or text design, held in the right hand.",
"focal_length": "Standard mobile wide lens (approx 26mm equivalent).",
"framing": "Vertical framing."
},
"lighting": {
"source": "Soft, diffused natural light coming from the front (behind the mirror) and ambient room lighting.",
"quality": "Even illumination, soft shadows on the back and jeans, highlighting the contours of the body and fabric textures.",
"shadows": "Subtle shadows defining the spinal groove and muscle definition on the back."
},
"mood_and_expression": {
"vibe": "Casual, confident, self-assured.",
"expression": "Focused, neutral, checking appearance in the mirror."
},
"style_and_realism": {
"style": "Photorealistic, user-gener"
}
```

[[Indoor Lifestyle Photography]] [[Denim Fashion]]

---

### 49. 概念艺术提示：倒置陶瓷金字塔

**Author**: [Uncle Dave (aka deebeeeff)](https://x.com/deebeeeff)  **Date**: 2026-02-07  **Language**: en

> 一个结构化的提示，用于生成一张概念艺术图像：一个由色彩斑斓的釉面陶瓷制成的倒金字塔，精确地平衡在一个相同的正立金字塔的尖端上。该提示强调使用陶瓷材料的自然色彩来形成图案。

![概念艺术提示：倒置陶瓷金字塔](https://cms-assets.youmind.com/media/1770532835079_ak5awu_HAkAJMzbgAAMvvn.jpg)
![概念艺术提示：倒置陶瓷金字塔](https://cms-assets.youmind.com/media/1770532835214_csfq2n_HAge8TJXEAAlePg.jpg)

```
#NanoBananaPro #Promptshare OBJECT=an upside down pyramid 
MATERIAL=highly colorful glazed ceramic 
CONNECTOR_INSTRUCTION=balanced exactly on the tip of  
BASE_MATERIAL=an identical pyramid, right side up   

Create an image of a [{argument name="object" default="OBJECT"}], made entirely of different types of [{argument name="material" default="MATERIAL"}], using the various natural colors of the [{argument name="material" default="MATERIAL"}] to create the [{argument name="object" default="OBJECT"}]'s beautiful patterns. Do not use any painted colors or other items to create the [{argument name="object" default="OBJECT"}]. Place the finished [{argument name="object" default="OBJECT"}][CONNECTOR_INSTRUCTION] a [BASE_MATERIAL] base, as a display piece. 9:16 ar
```

[[Conceptual Art]] [[Surreal Architecture]]

---

### 50. 情人节男婴肖像提示

**Author**: [PS World Vibes 🌍 | AI Art + Prompts](https://x.com/psworldvibes)  **Date**: 2026-02-07  **Language**: en

> 一个用于生成超逼真情人节主题男婴肖像的提示，需要根据上传的参考图像进行面部匹配，肖像中包含一个幽默的字母板标牌和红色玫瑰花瓣。

![情人节男婴肖像提示](https://cms-assets.youmind.com/media/1770532774949_bspvjc_HAj_4hXa0AEjS3v.jpg)

```
Create a 8k hd ultra realistic picture of reference uploaded picture face 100 dont change face of, Looking straight to the cameraThis charming Valentine's Day-themed photo features a joyful baby boy lying on a soft, white faux-fur background scattered with vibrant red rose petals. The infant is dressed in a smart white polo shirt paired with red suspenders, a matching red bowtie, and cuffed blue jeans. He is framed by a bouquet of red roses and daisies to his left and a black letter board to his right that cheekily reads, "SORRY LADIES MY MOM IS MY VALENTINE." The baby’s bright, toothless grin and the festive red-and-white color palette create a heartwarming and playful atmosphere.
```

[[Face Matching]]

---

### 51. 情人节女婴肖像提示

**Author**: [PS World Vibes 🌍 | AI Art + Prompts](https://x.com/psworldvibes)  **Date**: 2026-02-07  **Language**: en

> 一个用于生成超逼真情人节主题里程碑式女婴肖像的提示，需要根据上传的参考图像进行面部匹配，肖像中包含亮片心形紧身胸衣和红玫瑰。

![情人节女婴肖像提示](https://cms-assets.youmind.com/media/1770532781122_f2c4i9_HAj92eBacAQRQht.jpg)

```
Create a 8k hd ultra realistic picture of reference uploaded picture face 100 dont change face of, Looking straight to the cameraThe uploaded image is a professionally styled milestone portrait of an infant girl, designed with a romantic Valentine’s Day theme. The baby is lying on her back atop a plush, white faux-fur rug, dressed in a vibrant red ensemble that includes a sequined heart-shaped bodice, a ruffled tulle skirt, and a matching bow headband. To her left sits a lush bouquet of red roses, with individual petals scattered artistically across the rug to add depth and texture. In the upper right corner, a small chalkboard sign provides a personalized touch, marking her growth at five months (which we've since updated to "Happy Rose Day" in our edits). The high-contrast color palette of deep reds against the soft white background creates a warm, heartwarming aesthetic focused entirely on the infant's cheerful expression.
```

[[Face Matching]]

---

### 52. 超逼真芬达橙味汽水飞溅产品图

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-02-07  **Language**: en

> 生成一张冰镇芬达橙味铝罐超逼真电影级产品照片的提示词。它详细描述了凝结的水珠、空中凝固的爆裂橙片和飞溅的果汁，以及为高端饮料广告美学设计的戏剧性灯光（金色背光，冷色轮廓光）。

![超逼真芬达橙味汽水飞溅产品图](https://cms-assets.youmind.com/media/1770532764594_sekd5h_HAj8pzzaMAA-j6q.jpg)
![超逼真芬达橙味汽水飞溅产品图](https://cms-assets.youmind.com/media/1770532764700_8ymts0_HAj8pl-acAExnDd.jpg)
![超逼真芬达橙味汽水飞溅产品图](https://cms-assets.youmind.com/media/1770532764566_83dd22_HAj8phdacAQmuBF.jpg)
![超逼真芬达橙味汽水飞溅产品图](https://cms-assets.youmind.com/media/1770532765978_i2ib3z_HAj8qBQacAAuSIA.jpg)

```
Hyper-realistic cinematic product photograph of a classic {argument name="drink brand" default="Fanta Orange"} aluminum can, logo perfectly centered and fully legible, standing upright and slightly forward-facing, the can ice-cold and covered in dense micro-condensation droplets with natural gravity streaks and crisp specular highlights. Behind and around the can, fresh orange slices and citrus wedges explode outward in slow motion, juice splashes frozen mid-air with translucent pulp fibers, tiny droplets, and refractive liquid arcs catching the light. A large softly blurred orange cross-section forms the background halo, adding depth and color harmony without distracting from the can. Lighting is dramatic and premium: warm golden backlight glowing through the citrus, cool rim light defining the can edges and droplets, subtle front fill to preserve logo clarity. Shallow depth of field with creamy bokeh, high contrast, ultra-sharp focus on the can surface and condensation texture. Clean studio setup with no visible supports, no text overlays, no graphic elements, no borders. Color palette dominated by vibrant orange, cool silver highlights, and soft neutral background tones. Photorealistic materials, advertising-grade composition, high-end beverage commercial aesthetic, frozen-action splash photography, cinematic realism.
```

[[Condensation Detail]] [[Commercial Beverage Photography]]

---

### 53. Split Identity 乙烯基玩具引擎

**Author**: [Gadgetify](https://x.com/Gdgtify)  **Date**: 2026-02-07  **Language**: en

> 一个复杂且结构化的提示，旨在生成一个 2x2 的乙烯基艺术玩具网格，每个玩具都代表着具有二元性的“分裂身份”。它指定了艺术风格（球状玩具比例，干净的二等分几何形状）、材质（软乙烯基，对比鲜明的哑光颜色）和布局（对称构图，产品摄影照明）。

![Split Identity 乙烯基玩具引擎](https://cms-assets.youmind.com/media/1770532797428_92nuyc_HAjkHT9WMAEqbWZ.jpg)

```
Do this for a random character: <instruction> Split Identity Vinyl Toy Engine:
Input A is a Character with duality.

Select 4 lesser-known characters with internal conflict.

Sculpt each toy split vertically or horizontally into two contrasting halves.

Each half represents a different narrative state.

Layout:

2x2 grid, toys centered, perfectly symmetrical framing, name underneath

Style Stack:
Anchor: [Split vinyl art toy]::3.5
Morphology: Bulbous toy proportions, clean bisected geometry::3
Material: Soft vinyl, contrasting matte colors::2.5
Render: Product photography lighting, neutral backdrop::1
Negative: [organic gore, realism, asymmetry]::-1
```

[[2x2 Grid Layout]]

---

### 54. 充气角色创建提示

**Author**: [Amira Zairi](https://x.com/azed_ai)  **Date**: 2026-02-07  **Language**: en

> 一个使用 Nano Banana Pro 创建充气角色（可能用于平面设计或异想天开的插图）的提示分享。

![充气角色创建提示](https://cms-assets.youmind.com/media/1770532866657_ftct6n_HAj1ltpbwAAfQey.jpg)

```
Create inflatable characters using this prompt
```

[[Whimsical Illustration]]

---

### 55. 几何粘土人物

**Author**: [TechieSA](https://x.com/TechieBySA)  **Date**: 2026-02-07  **Language**: en

> 一个简短、描述性的提示，用于生成几何粘土人物的图像，可能用于风格化艺术项目或可视化。

![几何粘土人物](https://cms-assets.youmind.com/media/1770532792419_xhq9iz_HAjxbvnW0AActDq.jpg)

```
Geometric Clay Figures
```

[[Clay Texture]]

---

### 56. 身着金色服装的 Jennie Kim 电影感演唱会照片

**Author**: [Ankit Mishra](https://x.com/AnkitMi16412441)  **Date**: 2026-02-07  **Language**: en

> 一个详细的图像生成提示，重现了 K-pop 偶像 BLACKPINK 成员 Jennie Kim 在“The Show”演唱会期间的特定舞台造型。该提示着重于她的“嬉皮烫”发型、带有透明飘逸袖子的精致金色珠饰服装、发光的皮肤纹理以及以薰衣草色背景为特色的戏剧性舞台灯光。

![身着金色服装的 Jennie Kim 电影感演唱会照片](https://cms-assets.youmind.com/media/1770532830804_x3l0hq_HAjw-jhacAIZPG8.jpg)
![身着金色服装的 Jennie Kim 电影感演唱会照片](https://cms-assets.youmind.com/media/1770532830927_u7pqxw_HAjw-jhaoAAqXTN.jpg)
![身着金色服装的 Jennie Kim 电影感演唱会照片](https://cms-assets.youmind.com/media/1770532830903_8nvbru_HAjw-ihbgAAW_WC.jpg)

```
{
  "subject": {
    "name": "{argument name="subject name" default="Jennie Kim"}",
    "alias": "Jennie",
    "group": "BLACKPINK",
    "context": "BLACKPINK's online livestream concert 'The Show', January 2021, performing solo debut song 'SOLO'"
  },
  "appearance": {
    "hair": {
      "color": "dark",
      "style": "long, tight crimped curls ('hippie perm')",
      "volume": "high"
    },
    "makeup": {
      "eyes": "soft neutral eyeshadow, defined cat-eye eyeliner",
      "highlight": "shimmering on cheeks",
      "lips": "matte rose-toned",
      "overall": "fresh glow, stage-ready"
    },
    "skin": {
      "tone": "luminous white",
      "details": "realistic sweat sheen, subtle moisture highlights on collarbones, shoulders, and cheekbones, natural skin texture, pores and micro-detail intact",
      "lighting_reaction": "skin reacts dynamically to cinematic lighting"
    }
  },
  "outfit": {
    "top": {
      "type": "structured corset-style crop top",
      "color": "gold",
      "neckline": "deep V-neck",
      "embellishments": "intricate gold beadwork and embroidery in floral or paisley motifs",
      "details": "small dangling crystal beads on bottom hem"
    },
    "bottoms": {
      "type": "high-waisted shorts",
      "color": "gold",
      "embellishments": "dense gold embroidery and beadwork matching top"
    },
    "sleeves_drapery": {
      "type": "sheer, glittery gold tulle fabric",
      "placement": "attached to upper arms/shoulders",
      "length": "floor-length",
      "effect": "cape-like or wing-like flow"
    }
  },
  "accessories": {
    "microphone": "thin black headset microphone",
    "jewelry": "small earrings, minimal to highlight outfit"
  },
  "pose_expression": {
    "pose": "left hand raised touching hair, right arm relaxed, body angled to highlight silhouette",
    "expression": "focused, confident, lips slightly parted"
  },
  "environment": {
    "background": "soft, hazy wash of lavender and pale purple light",
    "lighting": "spotlight from front-left illuminating gold outfit and skin sheen"
  },
  "image_specs": {
    "width": 504,
    "height": 1002,
    "orientation": "vertical"
  }
}
```

[[Stage Lighting]]

---

### 57. Coquette 粉色时尚大片

**Author**: [RavelAI](https://x.com/Ravelberger)  **Date**: 2026-02-07  **Language**: en

> 一个用于生成“Coquette Pink”风格浪漫时尚摄影的结构化提示。它描述了一位年轻女子身穿淡粉色迷你连衣裙，在欧洲别墅花园中旋转，强调柔焦、梦幻般的柔和色彩和愉悦的氛围。

![Coquette 粉色时尚大片](https://cms-assets.youmind.com/media/1770532764126_jfgtm5_HAKLAd6bkAAJlj5.jpg)
![Coquette 粉色时尚大片](https://cms-assets.youmind.com/media/1770532764068_1zff2d_HAKLAd3aMAAZfrg.jpg)

```
{
 "subject": "{argument name="subject description" default="Young woman, soft curls, doe eyes, blush makeup"}", "outfit": "Pastel pink coquette mini dress, bow details, pearl accessories", "pose": "Twirling in garden courtyard, joyful laugh", "environment": "European villa garden, roses, fountain", "style": "Romantic editorial photography, soft focus bokeh, dreamy pastel palette" 
}
```

[[Romantic Atmosphere]]

---

### 58. 解体效果函数提示

**Author**: [Gadgetify](https://x.com/Gdgtify)  **Date**: 2026-02-07  **Language**: en

> 这是一个有趣且高度技术性的提示，设计为一个 Python 函数，用于对上传的图像应用特定的瓦解效果，同时保留原始姿态。该函数定义了瓦解的方向、速度和粒子类型，从而产生动态的粒子云效果。

![解体效果函数提示](https://cms-assets.youmind.com/media/1770532757594_1q9400_HASF0h5W8AA3puk.jpg)

```
``python def disintegrate(Subject): Direction = "{argument name="disintegration direction" default="Left to Right"}" Wind_Speed = "{argument name="wind speed" default="100 km/h"}" Particle_Type = "{argument name="particle type" default="Black Volcanic Ash and Embers"}" >Execution Left_Side_of_Subject = "Solid, Intact" Center_of_Subject = "Cracking, glowing cracks" Right_Side_of_Subject = "Fully dispersed into particle cloud" return Render(Motion_Blur=True, Glow=True) ```  Instruction:  Preserve the exact pose of [UPLOADED_IMAGE], but apply the `disintegrate()` function described above.
```

[[Pose Preservation]]

---

### 59. 超逼真茶叶摄影提示词（静物和分解视图）

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-02-07  **Language**: en

> 生成超逼真茶饮图像的两个独立提示。第一个是新鲜冲泡的茶杯的静物摄影，强调蒸汽、气泡和玻璃质感。第二个是展示泡茶阶段的爆炸式垂直信息图，各层悬浮在空中，设计风格简洁、极简。

![超逼真茶叶摄影提示词（静物和分解视图）](https://cms-assets.youmind.com/media/1770532751763_3xqudv_HAjd1s9aIAA4kX-.jpg)

```
Create a hyper-realistic studio photograph of a freshly brewed tea in a transparent glass cup.
The cup is filled with rich amber-colored tea, with loose tea leaves clearly visible settled at the bottom.

Soft aromatic steam gently rising from the surface, realistic and natural.

Tiny bubbles suspended inside the tea, subtle reflections on the glass, and accurate glass thickness.

Clean pure white background with soft studio lighting and a gentle shadow beneath the cup.

Ultra-detailed DSLR photography style, macro realism, sharp focus, natural color tones, realistic liquid physics, 8K resolution.
Minimal, clean aesthetic.

Image 2 - Create a hyper-realistic exploded vertical infographic of tea brewing on a pure white background.

At the very top, soft aromatic steam wisps floating naturally in the air.

Below it, a dynamic clear hot water splash frozen mid-motion with realistic liquid physics and droplets.

Under the water, fresh green tea leaves unfurling and suspended mid-brew with tiny air bubbles around them.

Below that, a smooth amber-colored brewed tea liquid layer, rich and transparent with subtle bubbles and reflections.

At the bottom, a crystal-clear transparent glass tea cup base, realistic glass thickness and soft shadow beneath.

Clean studio lighting, minimal aesthetic, evenly spaced floating layers, thin subtle infographic guide lines (no text labels).

Ultra-detailed DSLR photography style, macro realism, sharp focus, natural reflections, soft shadows, 8K resolution.
```

[[Minimalist Design]]

---

### 60. 热带忧郁实验室超现实肖像

**Author**: [timedoctor.eth](https://x.com/timedoctor_nft)  **Date**: 2026-02-07  **Language**: en

> 一个高度细致的电影化提示，用于创作一幅超现实主义的肖像画，描绘一位主角身着一件完全由香蕉皮和树叶制成的先锋派雕塑礼服。场景设定在一个混乱、杂乱的植物学家工作室/温室中，强调鲜明的灯光对比、电影胶片模拟（柯达 Portra 400）和情感上的脆弱。

![热带忧郁实验室超现实肖像](https://cms-assets.youmind.com/media/1770532754976_l8fyiy_HAjbffMWQAAuxM-.jpg)
![热带忧郁实验室超现实肖像](https://cms-assets.youmind.com/media/1770532755036_0uoofi_HAjbfh4WIAAfDXf.jpg)

```
{
  "vibe_title_en": "Tropical Melancholy Laboratory",
  "master_prompt": "A hyper-realistic, cinematic medium shot of The Protagonist captured through the dirty, condensation-covered glass of an old greenhouse partition (creating natural framing and depth). The subject is wearing an immense, avant-garde surreal sculpture of a dress constructed entirely from hundreds of cascading, vibrant yellow banana peels and thick, waxy organic leaves, meticulously layered to look like high-fashion armor. The environment is a densely cluttered, chaotic botanist's workshop: stacks of dusty encyclopedias, overflowing shelves of amber glass jars, tangled rubber hoses, and scattered gardening tools fill every inch of the background. The lighting creates a stark contrast: a beam of warm, directional sunlight illuminates the texture of the yellow organic dress, while the shadows are crushed into a deep, cinematic teal. The subject looks downward with a soft, vulnerable expression, avoiding eye contact, lost in thought. Shot on a Hasselblad H6D-100c with an 80mm f/1.9 lens to capture the microscopic texture of the fruit skin and the atmospheric dust motes. Kodak Portra 400 film stock emulation, fine grain, no neon, purely practical effects aesthetic.",
  "meta": {
    "intent": "Editorial Surrealism",
    "priorities": "Texture, Clutter, Emotional Contrast",
    "device_profile": "High-End Desktop / Gallery Print"
  },
  "frame": {
    "aspect": "16:9",
    "composition": "Rule of Thirds, Layered Foreground",
    "layout": "Depth-heavy, foreground obstruction",
    "camera_angle": "Eye Level, shooting through glass/objects",
    "tilt_roll_degrees": "0"
  },
  "subject": {
    "gender": "Female",
    "identity": "The Protagonist",
    "demographics": "Adult, Ageless",
    "face": "Neutral, soft features, minimal makeup with visible pores",
    "hair": "Sleek, contained bob or pulled back (mimicking the mood board geometry)",
    "body": "Slim, enveloped in voluminous surreal garment",
    "expression": "Vulnerable, eyes cast downward, lips slightly parted, melancholic",
    "pose": "Static, standing but slightly slumped shoulders, hands hidden in the dress layers"
  },
  "wardrobe_accessories": {
    "garments": [
      {
        "item": "Surreal Organic Gown",
        "material": "Banana Peels and Waxy Leaves",
        "color": "Vibrant Yellow and Pale Green",
        "fit": "Voluminous, Architectural, Layered"
      }
    ],
    "accessories": [
      {
        "item": "Sunglasses (Optional/Removed for vulnerability)",
        "color": "None",
        "material": "None",
        "brand_style": "None"
      }
    ]
  },
  "environment": {
    "setting": "Cluttered Botanist's Workshop / Greenhouse Storage",
    "surfaces": "Dusty wood, dirty glass, organic matter, paper stacks",
    "depth": "High complexity, foreground glass blur, background clutter bokeh",
    "atmosphere": "Humid, dusty, heavy air, smell of ripen"
```

[[Avant-Garde Fashion]]

---

### 61. 爆炸水果摆盘美食摄影

**Author**: [Cherry 2.O](https://x.com/Mind_Boticni)  **Date**: 2026-02-07  **Language**: en

> 一个用于生成视觉震撼、超现实主义水果爆炸图像的提示。它着重于动态运动、凝固在半空中的鲜艳果汁飞溅、极致的锐度以及在黑色背景下的电影级光效，适用于奢华食品摄影。

![爆炸水果摆盘美食摄影](https://cms-assets.youmind.com/media/1770532752814_s3rm5f_HAjV1L7awAEZ0cG.jpg)

```
A stunning hyper-realistic arrangement of fresh fruits, including {argument name="fruit types" default="red and green apples, strawberries, oranges, grapes, blackberries, and pineapples"}, exploding outward with vibrant juice splashes and dynamic motion. Ultra high-definition, extreme sharpness, cinematic lighting with dramatic contrast, rich vivid colors, floating and overlapping fruits, fine textures on fruit surfaces, droplets and splashes frozen in mid-air, luxury food photography style, highly detailed, black background, negative space, visually striking composition, hyper-realistic rendering, ultra-detailed photorealism
```

[[High Speed Photography]]

---

### 62. 奢华浴室镜自拍系列

**Author**: [Bahar azam](https://x.com/BaharAzamm561)  **Date**: 2026-02-07  **Language**: en

> 一个用于 Gemini Nano Banana Pro 3.0 的 JSON 提示，请求一系列四张镜面自拍，每张自拍都有一位不同的名人（Ana de Armas、Sadie Sink、Billie Eilish、Sydney Sweeney）在一个豪华浴室环境中，穿着浴巾或浴袍，并详细描述了背景元素，如大理石和金色固定装置。

![奢华浴室镜自拍系列](https://cms-assets.youmind.com/media/1770532816501_oz2b59_HAjN42IacAId4io.jpg)
![奢华浴室镜自拍系列](https://cms-assets.youmind.com/media/1770532816526_t2w1dw_HAjN43ebkAAZMGV.jpg)
![奢华浴室镜自拍系列](https://cms-assets.youmind.com/media/1770532816562_yblotu_HAjN42GacAI2ABf.jpg)
![奢华浴室镜自拍系列](https://cms-assets.youmind.com/media/1770532817854_8npg33_HAjN43faoAAMS-0.jpg)

```
[
  {
    "celebrity_name": "{argument name="celebrity 1" default="Ana de Armas"}",
    "profession": "Actress",
    "setting": "Luxury Bathroom",
    "outfit_details": {
      "clothing": "White bath towel",
      "style": "Wrapped around body",
      "hair": "Messy bun"
    },
    "background_elements": [
      "Marble walls",
      "Gold fixtures",
      "Chandelier",
      "Mirror reflections"
    ],
    "image_context": "Mirror selfie in a classic upscale interior"
  },
  {
    "celebrity_name": "{argument name="celebrity 2" default="Sadie Sink"}",
    "profession": "Actress",
    "setting": "Elegant Bathroom",
    "outfit_details": {
      "clothing": "Green textured bathrobe",
      "style": "Over-the-shoulder pose",
      "hair": "Tied up, reddish-orange"
    },
    "background_elements": [
      "Patterned marble tiles",
      "Ornate chandelier",
      "Indoor plant",
      "Classic bathtub"
    ],
    "image_context": "High-angle mirror selfie with warm lighting"
  },
  {
    "celebrity_name": "{argument name="celebrity 3" default="Billie Eilish"}",
    "profession": "Singer-Songwriter",
    "setting": "Elegant Bathroom",
    "outfit_details": {
      "clothing": "Pink terry cloth bathrobe",
      "style": "Front-facing selfie",
      "hair": "Blonde with bangs"
    },
    "background_elements": [
      "Marble backsplash",
      "Gold-framed mirror",
      "Soft overhead lighting",
      "Luxury toiletries"
    ],
    "image_context": "Reflective mirror shot showing a casual home look"
  },
  {
    "celebrity_name": "Sydney Sweeney",
    "profession": "Actress",
    "setting": "Grand Marble Bathroom",
    "outfit_details": {
      "clothing": "Dark blue plush towel",
      "style": "Wrapped around chest",
      "hair": "Loose blonde hair"
    },
    "background_elements": [
      "Symmetrical marble patterns",
      "Crystal chandelier",
      "Gold-accented vanity",
      "White bathtub"
    ],
    "image_context": "Clean, bright mirror selfie in a professional setting"
  }
]
```

[[Marble Bathroom Setting]]

---

### 63. 葛饰北斋风格浮世绘生成

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 使用 Nano Banana Pro（Gemini 3 Pro 图像）的提示，生成了一幅葛饰北斋风格的木版画，其图像类似于《神奈川冲浪里》。

![葛饰北斋风格浮世绘生成](https://cms-assets.youmind.com/media/1770532844894_gix037_GCRihaybMAAN19f.jpg)
![葛饰北斋风格浮世绘生成](https://cms-assets.youmind.com/media/1770532844993_5h9y74_HAjK_vIbMAAkSj8.jpg)

```
葛飾北斎みたいな
版画を１枚作って出して！
```

[[Artistic Style Transfer]] [[Japanese Woodblock Print]]

---

### 64. 湿发与冷光下的忧郁特写肖像

**Author**: [The Prompt Engineer](https://x.com/rorschachvibes)  **Date**: 2026-02-07  **Language**: en

> 一个用于生成年轻女性特写肖像的提示词，要求照片级真实感。强调湿润蓬松的深棕色头发、化有深色妆容的迷人双眼、水润的皮肤以及亮泽的深粉色口红。关键的风格元素是冷峻的蓝色调灯光，营造出戏剧性和忧郁的氛围。

![湿发与冷光下的忧郁特写肖像](https://cms-assets.youmind.com/media/1770532791971_afbnc1_HAjJ8H7acAMVbax.jpg)

```
Create a 4:5 photo realistic skin texture portrait close-up portrait of a young woman with wet, tousled dark brown hair, styled in loose, wavy strands framing her face. She has striking, expressive eyes with dark eyeliner and subtle eyeshadow, complemented by well-defined eyebrows. Her skin is smooth, with a dewy, luminous finish, and she wears glossy, deep pink lipstick. The lighting casts a cool, bluish tint on her face, creating a dramatic and moody atmosphere.
```

[[Wet Hair Portrait]] [[Dramatic Atmosphere]]

---

### 65. 西式台球厅动作抓拍

**Author**: [Javeriya 🇺🇸](https://x.com/JadoonKhan281)  **Date**: 2026-02-07  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张女性在复古中世纪现代风格游戏室打台球的全身中景照片。它指定了受西方启发的服装（格子露脐上衣、低腰超短裤、牛仔帽、麂皮靴）、充满活力的赤褐色头发和坚定的表情，强调电影般的景深和逼真的皮肤光泽。

![西式台球厅动作抓拍](https://cms-assets.youmind.com/media/1770532799393_lg5pq4_HAjKDeHacAUcs6u.jpg)
![西式台球厅动作抓拍](https://cms-assets.youmind.com/media/1770532799450_5cydc1_HAjKDYFacAQxZoE.jpg)
![西式台球厅动作抓拍](https://cms-assets.youmind.com/media/1770532800082_evq89a_HAjKDVTaEAABohP.jpg)
![西式台球厅动作抓拍](https://cms-assets.youmind.com/media/1770532800767_ax73jn_HAhq8CbbUAAuc2z.jpg)
![西式台球厅动作抓拍](https://cms-assets.youmind.com/media/1770532801289_1rggqe_HAhq8H7bAAA6JYC.jpg)
![西式台球厅动作抓拍](https://cms-assets.youmind.com/media/1770532801791_652gme_HAhq8N6awAAcEif.jpg)

```
{
  "subjects": [
    {
      "person": "{argument name="subject name" default="Ana de Armas"}",
      "position": "Center",
      "appearance": {
        "hair": {
          "color": "Vibrant auburn with copper highlights",
          "style": "Long, flowing waves cascading over the shoulders",
          "length": "Waist-length"
        },
        "makeup": {
          "eyes": "Subtle winged eyeliner with soft peach eyeshadow",
          "lips": "Matte rose-tinted lipstick"
        },
        "expression": "Focused and determined, leaning over the table"
      },
      "attire": {
        "type": "Western-inspired midriff-baring ensemble",
        "color": "Red and white gingham with faded denim blue",
        "fabric": "Lightweight cotton weave; heavy-duty denim",
        "structure": "Off-the-shoulder smocked crop top; ultra-low-rise micro-shorts with a raw hem"
      },
      "accessories": [
        "Woven straw cowboy hat with intricate ventilation patterns",
        "Tan suede knee-high boots with side fringe detailing",
        "Wooden pool cue held in a shooting bridge position",
        "Delicate gold wrist chain"
      ]
    }
  ],
  "setting": {
    "background": "Mid-century modern interior featuring warm wood paneling and large sliding glass doors",
    "elements": [
      "Vintage orange saucer-style pendant light",
      "Classic billiards table with a tan felt surface",
      "Eames-style orange molded plastic chair",
      "Abstract wall art",
      "White cue ball and colored pool balls on the felt"
    ],
    "context": "Action shot of the subject playing pool in a retro-themed game room"
  },
  "lighting": {
    "source": "Natural daylight from side windows mixed with warm overhead indoor ambiance",
    "quality": "Soft, diffused lighting with realistic skin glow and cinematic depth"
  },
  "composition": {
    "shot_type": "Full-body medium shot, slightly low angle",
    "pose": "Bending over the billiards table, lining up a shot with the pool cue",
    "focus": "Sharp focus on the subject and the cue ball, with a soft blur on the background"
  }
}
```

[[Action Portrait]]

---

### 66. 闪光灯下的深夜海岸人像与日落余晖

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-02-07  **Language**: en

> 一个旨在创作夜晚海滩上人物戏剧性写实图像的提示。它着重于主体与背景之间的对比：主体被闪光灯照亮（呈现出阳光亲吻般的发光肌肤），背景则是夕阳西下 98% 后深紫红色的天空。构图是从主体背后拍摄，主体正转向镜头。

![闪光灯下的深夜海岸人像与日落余晖](https://cms-assets.youmind.com/media/1770532795108_k9fa08_HAjHroFbYAAuIKd.jpg)
![闪光灯下的深夜海岸人像与日落余晖](https://cms-assets.youmind.com/media/1770532795204_726ulg_HAjHrlQa8AAAdE7.jpg)

```
Create a beachy look of me like I'm on a beach where it's dark but someone took my picture with a flash, making my face sun-kissed, slightly glittery, and glowing. In the background, add a sunset where the sun has 98% set, leaving a deep purple-red sky, almost dark. The image is taken from behind my back as I turn toward the camera. I'm wearing a light yellow, loose, half-open linen shirt with sleeves rolled up, paired witha subtle gold seashell necklace. My hair is windswept, giving natural surfer vibes. The picture is cropped from above the waist, focusing on the upper body and glowing beachy aesthetic. 9:16 ratio
```

[[Back View Portrait]]

---

### 67. 浮世绘风格图像生成：写乐风格

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个给 Nano Banana Pro (Gemini 3 Pro Image) 的简单提示，用于生成一张浮世绘风格的图像，特别要求创作一幅著名艺术家写乐风格的作品。

![浮世绘风格图像生成：写乐风格](https://cms-assets.youmind.com/media/1770532844785_gxyl5c_GCRihaybMAAN19f.jpg)
![浮世绘风格图像生成：写乐风格](https://cms-assets.youmind.com/media/1770532845468_lj3thp_HAjHjYHaIAAPCPN.jpg)

```
写楽みたいな浮世絵を
１枚作って出して！
```

[[Artistic Style Transfer]] [[Japanese Woodblock Print]]

---

### 68. 图像到图像的浮世绘风格迁移

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个提示，指示 Nano Banana Pro（Gemini 3 Pro Image）将提供的参考图像（通过“これ”暗示）转换为浮世绘风格，用户指出该尝试部分失败。

![图像到图像的浮世绘风格迁移](https://cms-assets.youmind.com/media/1770532850019_69xcl8_GCRihaybMAAN19f.jpg)
![图像到图像的浮世绘风格迁移](https://cms-assets.youmind.com/media/1770532850139_3299j3_HAjHN4VaUAAPJoJ.jpg)
![图像到图像的浮世绘风格迁移](https://cms-assets.youmind.com/media/1770532850096_91a700_HAjHOA1bgAAc30l.jpg)

```
これ（右の画像）を
浮世絵に変えて出して！
```

[[Image-to-Image Style Transfer]] [[Japanese Woodblock Print]]

---

### 69. 图像到图像风格迁移至穆夏新艺术风格

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个提示，指示 Nano Banana Pro（Gemini 3 Pro Image）将提供的参考图像（由“これ”暗示）转换为阿尔丰斯·穆夏的新艺术风格。

![图像到图像风格迁移至穆夏新艺术风格](https://cms-assets.youmind.com/media/1770532849724_vykv3o_GCRihaybMAAN19f.jpg)
![图像到图像风格迁移至穆夏新艺术风格](https://cms-assets.youmind.com/media/1770532849835_8klpom_HAjFsBhaQAEQNUE.jpg)
![图像到图像风格迁移至穆夏新艺术风格](https://cms-assets.youmind.com/media/1770532850177_e5f7uu_HAjFsC8aQAEIRV2.jpg)

```
これ（右の画像）をミュシャみたいな絵に変えて出して！
```

[[Image-to-Image Style Transfer]]

---

### 70. Kuromi 风格网红肖像提示词，适用于 Nano Banana Pro

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana Pro 生成一张酷女孩网红肖像。它指定了一位年轻女性手持酷洛米（Kuromi）毛绒玩具，展现出自信、时尚的美感。该提示包含了关于外貌（冷白皮、低饱和度淡粉色头发）、服装（韩式又酷又辣的时尚）、灯光（冷色调、略微过曝）和相机设置（佳能 EF 85mm f/1.2 镜头、微距级别细节）的细致描述。

![Kuromi 风格网红肖像提示词，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1770532861750_q7q1uq_HAjEj9dacAI3Z58.jpg)

```
{
  "image_generation": {
    "subject": {
      "description": "young woman influencer portrait holding a Kuromi plush toy",
      "pose": "casual carefree half-body pose, holding a plush toy gently in her arms",
      "expression": "expressive, lively, slightly smug, looking directly into the camera",
      "vibe": "confident, stylish, cool-girl idol aesthetic"
    },
    "appearance": {
      "skin": {
        "tone": "cool pale",
        "texture": "fair, clean, smooth skin"
      },
      "face": {
        "features": "delicate facial features, high-bridged nose, clearly defined jawline, narrow elongated eyes, fresh and refined look",
        "makeup": "minimal, delicate natural makeup"
      },
      "eyes": "stunning, expressive eyes",
      "hair": {
        "color": "{argument name="hair color" default="low-saturation pale pink"}",
        "length": "extra-long",
        "style": "high crown, relaxed effortless hair framing the face, individual strands visible"
      }
    },
    "outfit": {
      "style": "{argument name="outfit style" default="Korean-style cool and spicy fashion"}",
      "details": "trendy, stylish influencer outfit with feminine charm"
    },
    "props": {
      "item": "Kuromi plush toy"
    },
    "environment": {
      "setting": "in front of a highly fashionable wall backdrop",
      "background_style": "modern, stylish, influencer aesthetic"
    },
    "lighting": {
      "tone": "cool-toned",
      "effect": "slightly overexposed, soft glow"
    },
    "camera": {
      "shot_type": "half-body portrait",
      "lens": "Canon EF 85mm f/1.2",
      "style": "high-quality influencer photography",
      "focus": "macro-level detail, visible hair strands and smooth skin",
      "composition": "strong, impactful composition with depth and tension"
    },
    "aesthetic": {
      "style": "high-quality influencer portrait",
      "mood": "cool, refined, feminine, stylish",
      "color_palette": "cool tones, soft pale pink accents"
    },
    "quality": {
      "realism": "ultra detailed",
      "resolution": "high resolution",
      "finish": "clean, polished, professional photography look"
    }
  }
}
```

[[Canon 85mm Portrait]]

---

### 71. 停车场里的猫女 Cosplay

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-02-07  **Language**: en

> 一个为 Nano Banana Pro 设计的详细 JSON 提示，通过 Hailuo AI 生成一张照片级真实的图像：一名女性身穿猫女风格的服装（黑色浮雕连体衣、猫耳头带、鞭子），置身于工业停车场环境中，强调纹理对比和特定的光照条件。

![停车场里的猫女 Cosplay](https://cms-assets.youmind.com/media/1770532804351_gr18w8_HAjEY2XXEAALdXP.jpg)
![停车场里的猫女 Cosplay](https://cms-assets.youmind.com/media/1770532804417_1ubllx_HAjEZAlWoAAeoTU.jpg)
![停车场里的猫女 Cosplay](https://cms-assets.youmind.com/media/1770532804382_paptcg_HAjEY65XwAEUZ0g.jpg)
![停车场里的猫女 Cosplay](https://cms-assets.youmind.com/media/1770532805735_225jrq_HAjEZHLXwAAY2yM.jpg)
![停车场里的猫女 Cosplay](https://cms-assets.youmind.com/media/1770532805738_hnfsg0_HAfWWx8XMAAUi5K.jpg)

```
{
  "type": "photograph",
  "aspect_ratio": "9:16",
  "subject": {
    "description": "Woman with long, wavy, dark curly hair parted in the middle.",
    "face": {
      "makeup": "Heavy contouring, distinct winged eyeliner, filled arched eyebrows, overlined lips with brown liner and gloss.",
      "expression": "Confident, lips slightly parted, direct gaze, head tilted slightly to the right."
    },
    "physique": "Voluptuous hourglass figure, prominent bust volume, distinct waist-to-hip ratio.",
    "outfit": {
      "garment": "Black form-fitting jumpsuit with a textured, embossed animal-skin pattern (faux leather/latex). Front zipper pulled down to reveal cleavage.",
      "accessories": [
        "Black textured cat-ear headband matching the suit material.",
        "Black gloves with metallic silver claw tips attached to the fingers.",
        "Wide black belt with a rectangular plastic buckle.",
        "Small silver hoop earrings."
      ],
      "props": "Black braided riding whip held with one hand across the torso; right hand resting on waistline."
    }
  },
  "environment": {
    "location": "Concrete parking garage structure.",
    "elements": [
      "Thick grey concrete pillar directly behind the subject.",
      "Grey concrete ceiling with support beams.",
      "Background shows open garage levels with overexposed daylight coming from the rear right and the batmobile tumbler. "
    ],
    "atmosphere": "Urban, industrial, utilitarian."
  },
  "lighting": {
    "source": "Natural daylight diffused through open garage structure.",
    "quality": "Soft, flat, non-directional.",
    "shadows": "Soft shadows under the chin and hair; lack of dramatic contrast.",
    "highlights": "Reflective sheen on the textured latex suit surfaces, particularly on the chest and thighs."
  },
  "camera": {
    "framing": "Medium shot, cropped at the high heels .",
    "angle": "Eye-level, front view, slightly angled upwards.",
    "focus": "Sharp focus on subject, slight depth of field falloff in the background.",
    "style": "Amateur cosplay photography, incidental snapshot aesthetic."
  },
  "textures": {
    "skin": "Smooth makeup finish with visible contouring.",
    "clothing": "Shiny, embossed, rubbery texture with visible wrinkles and gathering at the waist and armpits.",
    "surfaces": "Rough, matte concrete vs. glossy synthetic fabric."
  }
}
```

[[Cosplay Photography]] [[Black Latex Bodysuit]]

---

### 72. 高对比度夜间热水浴缸照片，带闪光比基尼

**Author**: [Nobara](https://x.com/Nobarakia)  **Date**: 2026-02-07  **Language**: en

> 一个详细的图像生成提示，用于创建一张超逼真、高对比度的夜间照片，照片中两名身穿祖母绿闪光比基尼的女性在一个户外热水浴缸中。该提示指定了混合人工照明（串灯、闪光灯、水下发光）和一种抓拍、狗仔队/社交媒体闪光灯的美学效果。

![高对比度夜间热水浴缸照片，带闪光比基尼](https://cms-assets.youmind.com/media/1770532837994_0xstmz_HAjDXD7W8AAjPPv.jpg)

```
"subjects": [
    {
      "id": "subject_1_foreground",
      "appearance": {
        "hair": {
          "color": "blonde",
          "style": "long, straight, loose, center part",
          "texture": "silky, slightly damp near ends"
        },
        "skin": {
          "tone": "fair, sun-kissed",
          "texture": "smooth, visible freckles on cheeks and nose",
          "glow": "dewy, highlighted by flash"
        },
        "physique": "fit, hourglass figure",
        "expression": "soft smile, direct eye contact with camera, confident"
      },
      "clothing": {
        "item": "bikini",
        "style": "triangle top, high-cut bottoms",
        "color": "{argument name="bikini color" default="emerald green"}",
        "texture": "glitter/sparkle fabric",
        "fit": "snug, adjustable straps"
      },
      "pose": {
        "position": "sitting on the white rim of the hot tub",
        "body_angle": "angled slightly to the right",
        "legs": "extended down into the water",
        "arms": "right arm resting straight on the edge for support"
      }
    },
    {
      "id": "subject_2_background",
      "appearance": {
        "hair": {
          "color": "darker blonde/dirty blonde",
          "style": "long, wavy, loose",
          "texture": "soft waves"
        },
        "skin": "fair",
        "expression": "smiling broadly, looking towards the first subject/camera, candid"
      },
      "clothing": {
        "item": "bikini",
        "style": "triangle top, matching bottoms",
        "color": "emerald green",
        "texture": "glitter/sparkle fabric (matching subject 1)"
      },
      "pose": {
        "position": "sitting inside the hot tub, submerged to waist",
        "body_angle": "facing forward/slightly left",
        "interaction": "engaging with the moment, relaxed"
      }
    }
  ],
  "environment": {
    "location": "outdoor hot tub/jacuzzi at night",
    "background": {
      "elements": "dark green hedge/bushes, night sky",
      "decor": "string lights with warm Edison bulbs hanging overhead"
    },
    "atmosphere": {
      "visuals": "thick steam/mist rising from the warm water, contrasting with cool night air",
      "water": "bubbling, illuminated turquoise/green from internal pool lights"
    }
  },
  "lighting": {
    "type": "mixed artificial",
    "sources": [
      "overhead warm string lights (bokeh effect in background)",
      "direct camera flash or strobe (illuminating subjects clearly)",
      "ambient underwater lighting (teal glow)"
    ],
    "quality": "high contrast due to night setting, specular highlights on skin and wet surfaces"
  },
  "styling": {
    "mood": "fun, leisure, vacation, party, candid celebrity style",
    "aesthetic": "glamorous, poolside, late-night swim"
  },
  "camera_details": {
    "style": "Ultra Photorealistic, Paparazzi/Social Media Flash Aesthetic",
    "shot_type": "medium full shot, slightly high angle",
    "lens": "35mm wide angle",
    "aperture": "f/2.8"
```

[[Flash Photography Aesthetic]]

---

### 73. 身穿香槟色吊带裙的女性 4K 高清肖像

**Author**: [Minhaa](https://x.com/tabu_8114)  **Date**: 2026-02-07  **Language**: en

> 一张图像生成提示，详细描述了一位金发女性的半身肖像，她身穿香槟色缎面吊带裙，盘腿而坐。该提示指定了迷人的自然妆容、柔和的前方照明以及高分辨率、照片级的写实风格。

![身穿香槟色吊带裙的女性 4K 高清肖像](https://cms-assets.youmind.com/media/1770532827938_icr5mk_HAix8y9aIAA20E4.jpg)
![身穿香槟色吊带裙的女性 4K 高清肖像](https://cms-assets.youmind.com/media/1770532827927_ouazl1_HAix81PbYAAy7OZ.jpg)

```
[
  {
    "box_2d": [
      {
        "subject": " woman  with  blonde hair wavy brunette hair and rosy cheeks",
        "pose": "Sitting with legs crossed, right hand raised touching hair near face, looking directly at the camera with a soft smile",
        "clothing": {
          "dress": "{argument name="dress color" default="Champagne/light gold"} satin slip dress with a cowl neckline and spaghetti straps, mini length"
        },
        "accessories": {
          "earrings": "Small silver drop earrings with crystals",
          "necklace": "Delicate silver chain with a small pendant"
        },
        "makeup": "Glamorous natural look with prominent pink blush and berry-toned lipstick",
        "location": "Indoor setting, seated on a beige upholstered chair against a background of cream curtains and a dark window",
        "props": "None visible other than furniture"
      },
      {
        "photography_style": "4K HD Photo, Portrait",
        "lighting": "Soft, direct frontal lighting (possibly flash or ring light) creating highlights on the face and legs",
        "focus": "Sharp focus on the subject, particularly the face and dress texture",
        "composition": "Medium shot, seated, capturing the figure from the knees up",
        "quality": "High resolution, clear details, photorealistic"Ratio 3.4 Remove the lipstick and make up make her look natural Ratio 3.4
      }
    ]
  }
]
```

[[Blonde Hair Portrait]]

---

### 74. 广阔开放世界游戏环境生成器

**Author**: [Aimi Kōda](https://x.com/aimikoda)  **Date**: 2026-02-07  **Language**: en

> 一个模板提示，旨在根据单一概念主题生成广阔、电影级的奇幻游戏环境插画。它指定了远距离、聚焦环境的摄像机视角、宏伟的天空特征，并施加了限制，以确保场景感觉像是一个无人居住、高预算的开放世界景观。

![广阔开放世界游戏环境生成器](https://cms-assets.youmind.com/media/1770532757292_1c7z7f_HAixN1pXEAAkVKo.jpg)
![广阔开放世界游戏环境生成器](https://cms-assets.youmind.com/media/1770532757295_987v2l_HAixLdyXIAAbYEq.jpg)
![广阔开放世界游戏环境生成器](https://cms-assets.youmind.com/media/1770532757367_zmhpii_HAixVSSWgAEzQF3.jpg)

```
[THEME] = "{argument name="theme" default="Enter a theme here"}" 

Make a wide cinematic fantasy game environment illustration inspired by [THEME].
Use a distant environment-focused camera with an expansive sense of scale and exploration.
Set the scene as a vast open world shaped entirely by the logic, atmosphere and materials implied by [THEME].
Show a monumental sky feature or celestial presence that visually defines the world and reinforces the theme.
Let the terrain, colors, surface forms and horizon geometry emerge naturally from [THEME] without explicit constraints.
Keep the environment uninhabited with no characters, creatures, vehicles or structures.
Use soft, immersive lighting appropriate to the world, favoring mood and scale over realism.
Apply game-style atmospheric perspective to suggest depth, distance and exploration.
Compose the scene to feel like a high-budget open-world game vista rather than a photograph.
Ensure the final image feels serene, epic and discovery-driven, clearly readable as a game world shaped by [THEME].
```

[[Cinematic Landscape]]

---

### 75. 超逼真的企业高管肖像

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-02-07  **Language**: en

> 一个用于生成超逼真专业男性企业高管肖像的提示，适用于领英 (LinkedIn) 或 CEO 证件照。它指定了年龄范围、着装（量身定制的深色西装外套）、现代办公环境，以及 85mm 镜头感、f/1.8 光圈和电影感兼具干净利落的商务美学等摄影技术细节。

![超逼真的企业高管肖像](https://cms-assets.youmind.com/media/1770532789018_ow1ngi_HAivH66acAEQ_n9.jpg)
![超逼真的企业高管肖像](https://cms-assets.youmind.com/media/1770532789045_ub6x2p_HAivH4kacAQTsfv.jpg)

```
Ultra-realistic professional corporate portrait of a confident male executive, mid-30s to early-40s, sharp facial features, well-groomed short dark hair, light stubble or clean-cut beard, wearing a tailored dark blazer over a crisp white dress shirt. Shot in a modern office interior with warm wood textures and soft neutral tones. Natural window light with soft fill, balanced exposure, subtle skin texture, sharp eyes, shallow depth of field, creamy background bokeh. DSLR look, 85mm lens feel, f/1.8, high dynamic range, cinematic yet clean business aesthetic, premium LinkedIn/CEO headshot style.
```

[[85mm Portrait Lens]] [[Office Setting]]

---

### 76. 西装革履的中年男士电影肖像

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-02-07  **Language**: en

> 生成一张超现实、电影感的肖像，描绘一位自信的中年男士身着定制西装，运用戏剧性的低调影棚布光，辅以微妙的轮廓光，呈现高端企业编辑风格。

![西装革履的中年男士电影肖像](https://cms-assets.youmind.com/media/1770532778138_m77ru2_HAir66xacAIK4Rs.jpg)

```
Ultra-realistic cinematic portrait of a confident middle-aged man with a full, well-groomed beard and neatly styled hair, wearing a tailored dark navy suit, black dress shirt, and black tie. Standing pose with one hand relaxed, subtle luxury wristwatch visible. Moody dark blue to black gradient background. Dramatic low-key studio lighting with soft key light on the face and subtle rim light outlining the shoulders. Sharp facial features, realistic skin texture, natural shadows, serious powerful expression. High-end corporate and luxury editorial photography style. Shot on a full-frame camera, 85mm lens, f/2.2, shallow depth of field, cinematic color grading, ultra-detailed, photorealistic, 8K quality.
```

[[Low Key Studio Lighting]]

---

### 77. 长城混合媒体比较

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-02-07  **Language**: en

> 一个用于 Google Nano Banana Pro 的结构化 JSON 提示，旨在创建一个并排比较图像（3:2 宽高比），左侧是长城的详细技术蓝图草图，右侧是高分辨率全景照片，适用于教育或建筑可视化。

![长城混合媒体比较](https://cms-assets.youmind.com/media/1770532813246_pstn3u_HAiqDdmaMAAbiGV.jpg)
![长城混合媒体比较](https://cms-assets.youmind.com/media/1770532813394_5hobm5_HAYTUhFbQAAtSm4.jpg)

```
{
  "objective": "Create a side-by-side comparison image featuring a technical sketch and real photograph of the Great Wall of China",
  "image_specifications": {
    "style": "Mixed media (Technical drawing + Real photograph)",
    "layout": "Horizontal split - Left side: Sketch with measurements, Right side: Real photo",
    "aspect_ratio": "3:2"
  },
  "left_side": {
    "content_type": "Technical sketch of the Great Wall of China",
    "features": [
      "Detailed architectural lines showing wall segments, watchtowers, and defensive structures",
      "Numerical measurements for wall height, width, and tower spacing",
      "Elevation labels for wall sections and towers",
      "Side elevation and top-down layout illustrating wall curvature along terrain"
    ],
    "text_annotations": {
      "units": "Metric (meters)",
      "language": "English",
      "font_style": "Blueprint or engineering-style typography"
    },
    "positioning": "Take up the left half of the image"
  },
  "right_side": {
    "content_type": "High-resolution real photo of the Great Wall of China",
    "features": [
      "Wide panoramic view of the wall stretching across mountains",
      "Natural daylight with clear or lightly clouded sky",
      "Realistic colors with visible stone texture and surrounding landscape"
    ],
    "positioning": "Take up the right half of the image"
  },
  "visual_elements": {
    "border_division": "Vertical line or subtle transition between left (sketch) and right (photo)",
    "color_palette": {
      "left": "Monochrome or blueprint blue for sketch",
      "right": "Natural realistic colors"
    }
  },
  "output_format": {
    "type": "Image",
    "use_case": [
      "Educational poster",
      "Architectural comparison",
      "Historical visualization",
      "Tourism visual aid"
    ],
    "high_resolution": true
  }
}
```

[[Architectural Photography]] [[Educational Visualization]]

---

### 78. 将视频转换为四格漫画

**Author**: [たにさん@AI×せどり - GPTプロンプトと画像生成で新世界探求](https://x.com/sojiro456)  **Date**: 2026-02-07  **Language**: ja

> 一个工作流的描述，其中故事通过 GPTs 构建，使用 GenSpark 优化，然后将来自 Kling 的视频使用 Nano Banana Pro 转换为四格漫画。

![将视频转换为四格漫画](https://cms-assets.youmind.com/media/1770532854474_sb8ocu_HAinpWrasAADmnj.jpg)

```
Klingの映像からNano Banana Proで4コマへ
```

[[Sequential Art]]

---

### 79. 适用于 Nano Banana Pro 的漫画生成提示模板

**Author**: [不可思議ちゃん＠AI漫画](https://x.com/UNfukashigi)  **Date**: 2026-02-07  **Language**: ja

> 一个在 Nano Banana Pro 中生成漫画分格（比例 2:3）的模板，用户可以输入所需内容和之前生成的风格标签（Style、Negative-Style、Color），以保持一致的美学风格。

![适用于 Nano Banana Pro 的漫画生成提示模板](https://cms-assets.youmind.com/media/1770532852413_gcibgm_HAinMyPbQAAIZ_Y.png)
![适用于 Nano Banana Pro 的漫画生成提示模板](https://cms-assets.youmind.com/media/1770532852343_hzrx7a_HAilJ39acAImhVd.jpg)

```
漫画生成（比率：2:3）

内容:
＜ここに内容を入れる＞

＜ここに絵柄のタグ（Style、Negative-Style、Color）を入れる＞
```

[[Sequential Art]] [[Template Prompt]]

---

### 80. 可视化个人愿望的通用提示

**Author**: [がんぐ（gangu）45／artist／『Tsugihagi Rabbits』creator](https://x.com/gangu_45)  **Date**: 2026-02-07  **Language**: ja

> 用户在 Nano Banana Pro 中输入自己的个人愿望或想法的通用提示，然后 Nano Banana Pro 将其可视化，并指出生成图像中光照的自然品质。

![可视化个人愿望的通用提示](https://cms-assets.youmind.com/media/1770532852135_e495a5_HAikDGsacAMSpGA.jpg)

```
自分の欲望を語ったら、具現化してくれた。
```

[[Personal Wish Visualization]]

---

### 81. 超逼真动作视频生成，基于图像参考

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-02-07  **Language**: en

> 这个复杂的提示旨在利用 Google Veo 3.1 和 Nano Banana Pro 进行视频生成，指示 AI 根据上传的图像参考创建一个超现实的动作序列。视频中，一个怪物挥舞斧头冲向并击打一罐 Monster Energy 饮料，同时对摄像机运动和场景设置有严格的限制。

![超逼真动作视频生成，基于图像参考](https://cms-assets.youmind.com/media/1770532748657_9616g9_HAiaWRfbEAAg6ti.jpg)

```
Create a hyper-realistic action video using the uploaded image as the exact visual reference.

SCENE SETUP:
A Monster Energy can stands perfectly upright at the center of the frame.
The environment stays dark, green, and fog-filled as in the reference image.
A large humanoid monster is visible in the background, partially obscured by green fog.

CAMERA:
Camera is completely locked.
Same angle throughout the entire video.
No zoom.
No pan.
No rotation.
No camera shake.

ACTION SEQUENCE:
➟ The video starts with stillness.
   The can does not move.
   The monster is visible but stationary in the background.

➟ The monster suddenly charges forward at full speed toward the can.
   Running motion is aggressive, fast, and direct.
   No slow motion at any point.
   No pauses.

➟ The monster holds a heavy axe with both hands while running.
   The axe is raised as it approaches the can.

➟ The monster strikes the can with full force using the axe.
   The impact is violent and instantaneous.
```

[[Google Veo Generation]]

---

### 82. 复古 2000 年代一次性相机风格模板

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-02-07  **Language**: en

> 一个结构化的 JSON 模板，旨在生成具有特定复古模拟美学的图像，模仿 2000 年代的即弃相机。它包含用于定义主体、环境、光线（硬质机载闪光灯）、胶片模拟（柯达 Tri-X 400）的字段，以及确保胶片般效果（带有颗粒和漏光等瑕疵）的负面约束。

![复古 2000 年代一次性相机风格模板](https://cms-assets.youmind.com/media/1770532752119_whq4tu_HAh8Ll0XgAAoTry.jpg)
![复古 2000 年代一次性相机风格模板](https://cms-assets.youmind.com/media/1770532752120_td35cf_HAh8LlsWQAALxuH.jpg)
![复古 2000 年代一次性相机风格模板](https://cms-assets.youmind.com/media/1770532752114_x45oy0_HAh8LluWcAAKuCJ.jpg)
![复古 2000 年代一次性相机风格模板](https://cms-assets.youmind.com/media/1770532753085_yaccio_HAh8LlvXwAAaB2j.jpg)

```
{
  "meta": {
    "purpose": "Vintage analog photography style for nostalgic portraits or scenes",
    "style": "2000s disposable camera vibe with grain and imperfections, 8K but film-like"
  },
  "reference_image": {
    "use": true,
    "extraction": "emulate film stock, grain, lighting from upload"
  },
  "subject": {
    "description": "{argument name=\"subject description\" default=\"[e.g., Young woman in retro outfit OR Group candid shot]\"}",
    "expression": "{argument name=\"subject expression\" default=\"[e.g., Playful laugh, winking]\"}",
    "pose": "[e.g., Leaning forward, finger gun]",
    "attire": "[e.g., Sleeveless top, leopard accessories]"
  },
  "environment": {
    "setting": "{argument name=\"setting\" default=\"[e.g., Dimly lit party OR Urban street at night]\"}",
    "details": "[e.g., Champagne glasses, blurred crowd]"
  },
  "lighting": {
    "type": "[e.g., Hard on-camera flash]",
    "effects": "high contrast, light leaks, chromatic aberration"
  },
  "art_style": {
    "film_stock": "[e.g., Kodak Tri-X 400 pushed, chunky grain]",
    "mood": "candid nightlife",
    "imperfections": "vignette, scratches"
  },
  "render_quality": {
    "detail_level": "hyper-detailed skin",
    "sharpness": "slight softness for analog"
  },
  "constraints": {
    "no_digital_clean": true
  },
  "negative_prompt": ["soft lighting", "perfect symmetry", "over-edited", "cartoon"]
}
```

[[Hard Flash Lighting]]

---

### 83. 挑逗性健身房镜面自拍二人组

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细的 JSON 提示，适用于 Gemini Nano Banana Pro 和 Grok Imagine，用于生成一张超逼真的后视镜自拍：两名女性（形似 Billie Eilish 和 Sydney Sweeney）身穿提臀紧身裤，在凉爽的蓝紫色环境健身房灯光下摆姿势，以凸显她们的臀部。

![挑逗性健身房镜面自拍二人组](https://cms-assets.youmind.com/media/1770532820299_xeemga_HAiP4jmXIAAbTZg.jpg)
![挑逗性健身房镜面自拍二人组](https://cms-assets.youmind.com/media/1770532820252_7qkjiu_HAfyGmXXUAAXUk2.jpg)

```
{
  "image_analysis": {
    "overall_scene": "Provocative gym mirror selfie of two young smiling women viewed from behind, posing to emphasize glutes and lower bodies, one holding phone, under cool blue-purple ambient lighting.",
    "subjects": [
      {
        "position": "left",
        "identity": "{argument name="subject 1 likeness" default="Billie Eilish resemblance"}",
        "age_appearance": "Early 20s",
        "build": "Curvy athletic hourglass, pronounced glutes, toned legs, fair smooth skin",
        "hair": "Medium-length curly brown in high messy bun with loose strands",
        "face": "Visible smiling at camera",
        "other_details": "None prominent"
      },
      {
        "position": "right (holding phone)",
        "identity": "{argument name="subject 2 likeness" default="Sydney Sweeney resemblance"}",
        "age_appearance": "Early 20s",
        "build": "Curvy athletic, pronounced glutes, toned legs/back, fair smooth skin",
        "hair": "Long wavy reddish-auburn/orange, loose over shoulders",
        "face": "Visible smiling at camera",
        "other_details": "Holding iPhone"
      }
    ],
    "pose": "Rear-view mirror selfie: legs slightly apart, hands on hips, backs arched to accentuate glutes and scrunch-butt leggings, confident teasing gym pose",
    "clothing": {
      "left_woman": "White long-sleeve open-back crop top with twisted back, light blue high-waisted scrunch-butt leggings with ruched seam",
      "right_woman": "White halter-neck sports bra, light purple high-waisted scrunch-butt leggings with ruched seam"
    },
    "lighting_and_color": {
      "lighting": "Cool blue/purple LED ambient, moody highlights on skin/fabric, mirror reflections",
      "color_palette": "Cool tones dominant: white tops, blue/purple leggings, dark gym floor"
    },
    "background": "Modern gym in mirrors: cardio machines left, weights right, exposed ducts, dark rubber floor, blurred distant gym-goers",
    "photography_style": "Photorealistic vertical mirror selfie, high-res sharp details on ruched fabric/skin/hair, rear lower-body focus"
  },
  "generated_prompt": {
    "full_text_prompt": "photorealistic vertical gym mirror selfie from behind of two beautiful athletic young women early 20s, left with curly brown high messy bun wearing white open-back long-sleeve crop top and light blue scrunch-butt leggings, right with long wavy reddish hair wearing white halter sports bra and light purple scrunch-butt leggings holding iPhone, both hands on hips backs arched emphasizing pronounced glutes/toned legs, modern gym mirrors cardio/weight equipment cool blue-purple lighting, highly detailed ruched textures skin sheen hair, sharp lower-body focus, confident teasing fitness vibe, 8k masterpiece",
    "negative_prompt": "deformed, ugly, bad anatomy, extra limbs, blurry, low quality, cartoon, illustration, painting, watermark, text, over/underexposed, children, elderly, mutated hands, front view",
    "recommended_parameters": {
    }
```

[[Fitness Lifestyle]] [[Celebrity Duo Portrait]]

---

### 84. 柔和的 E-Girl 自拍，搭配哥特图案吊带背心

**Author**: [Nobara](https://x.com/Nobarakia)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超逼真的中景自拍照。它描述了拍摄对象的样貌（金色长发、浅绿色眼睛、S 形身材）、着装（紧身白色吊带背心，带有黑色蝙蝠/骷髅图案）和环境（整洁又略显凌乱的卧室，配有神秘挂毯和毛绒玩具），并强调了柔和的自然日光和微小细节。

![柔和的 E-Girl 自拍，搭配哥特图案吊带背心](https://cms-assets.youmind.com/media/1770532797542_ta2jbl_HAiPcaDXAAAIzOs.jpg)

```
{
  "subject": {
    "appearance": {
      "hair": {
        "color": "light blonde",
        "style": "long, straight, parted in the middle, slightly tousled texture",
        "length": "waist-length, cascading over shoulders"
      },
      "eyes": {
        "color": "light green/hazel",
        "gaze": "looking slightly upward and to the side, dreamy and contemplative",
        "lashes": "long, defined eyelashes"
      },
      "skin": {
        "tone": "fair/pale",
        "texture": "smooth, natural finish, rosy cheeks, faint freckles across the nose bridge",
        "complexion": "glowy and hydrated"
      },
      "lips": {
        "color": "natural pink rose",
        "shape": "full, plump, soft pout"
      },
      "physique": {
        "build": "curvy, hourglass figure",
        "features": "prominent bust"
      }
    },
    "clothing": {
      "type": "cropped camisole/tank top",
      "material": "soft stretch cotton blend",
      "color": "white base",
      "pattern": "{argument name="camisole pattern" default="gothic/halloween theme: repeating black bats with skeleton details, crescent moons, and stars"}",
      "fit": "tight, form-fitting",
      "neckline": "low scoop neck"
    },
    "pose": {
      "type": "selfie portrait",
      "angle": "eye-level, slightly angled body",
      "expression": "neutral, soft, relaxed mouth",
      "head_position": "slightly tilted, chin up"
    }
  },
  "environment": {
    "location": "indoor bedroom/living area",
    "background_objects": {
      "wall_decor": "hanging vertical tapestry with beige background and mystical/astrological line art",
      "furniture": "dark grey sofa corner, white shelving unit with woven storage bins",
      "items": "small purple plush toy (squishmallow style), small orange plush/object",
      "plants": "green leafy houseplant in background right",
      "equipment": "tripod/ring light stand visible in background right"
    },
    "ambiance": "casual, messy-clean, lived-in space"
  },
  "lighting": {
    "type": "natural daylight",
    "quality": "soft, diffused, window light",
    "direction": "frontal, illuminating face evenly",
    "highlights": "catchlights in eyes, soft sheen on nose tip and forehead",
    "shadows": "minimal, soft drop shadows under hair and chin"
  },
  "styling": {
    "aesthetic": "soft e-girl, casual goth, cozy, influencer style",
    "makeup": "minimalist 'no-makeup' look, natural eyebrows, flushed cheeks",
    "jewelry": "small silver hoop earring visible on one ear"
  },
  "camera_settings": {
    "style": "Ultra Photorealistic",
    "shot_type": "medium close-up",
    "focal_length": "35mm (mimicking high-end smartphone portrait mode)",
    "aperture": "f/2.2",
    "shutter_speed": "1/125",
    "iso": "200",
    "focus": "sharp focus on eyes and face, slight bokeh blur in background",
    "resolution": "8k, high definition",
    "details": "micro-details of skin texture, individual hair strands, fabric weave visible"
  }
}
```

[[Soft Natural Daylight]] [[Cozy Aesthetic]]

---

### 85. 冰上男子与水下骨架的 8K 超逼真宣传图片

**Author**: [Max](https://x.com/Max__Build)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细、超逼真的图像生成提示，专为宣传内容设计。它描绘了一个男人站在广阔的冰冻湖面上，低头凝视着清澈的青色冰层下清晰可见的巨大扭曲骨架。该提示指定了电影般的色调、8K 分辨率，以及蜘蛛网状裂缝和气泡等细节，以营造强烈的视觉深度。

![冰上男子与水下骨架的 8K 超逼真宣传图片](https://cms-assets.youmind.com/media/1770446099180_zot0ic_HAiJoLzacAEI8KU.jpg)

```
Use the man in the uploaded image standing directly on a vast frozen lake surface, feet slightly apart, gazing downward toward the ice. Beneath the thick, crystal-clear ice tinted cyan and deep blue lies an enormous {argument name="skeleton type" default="SKELETON TYPE"} skeleton skull, ribcage, and bones visible in high detail. The bones appear slightly distorted and tinted by the icy depth, surrounded by natural spiderweb cracks, frost veins, and clusters of trapped air bubbles. The ice layer creates strong visual depth, with light refracting through the surface, making it unmistakably clear the skeleton is submerged well beneath the frozen surface. Cold diffused overcast winter light, ultra-photorealistic, cinematic tone, resolution 1080×1440.
```

[[Cinematic Color Grading]]

---

### 86. Nano Banana Pro 电影摄影机说明

**Author**: [摆烂程序媛](https://x.com/wanerfu)  **Date**: 2026-02-07  **Language**: zh

> 一套专为 Nano Banana Pro 型号设计的高度敏感的相机特定指令，通过模仿专业电影摄影技术，将标准提示转化为电影般的镜头。

![Nano Banana Pro 电影摄影机说明](https://cms-assets.youmind.com/media/1770532842918_koyfk6_HAh8DFcacAEk-qZ.jpg)

```
• '用35mm胶片拍摄'
• '微距特写'
• 'f1.4浅景深'
• '体积光'
• '变形镜头'
• '运动模糊'
```

[[Camera Specification Prompt]]

---

### 87. 照片修复至单反相机质量

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-02-07  **Language**: en

> 这是一个为 Gemini 上的 Nano Banana Pro 设计的提示，用于图像修复和放大。它指示 AI 将一张老旧、受损的照片转换成专业级的数码图像，质量媲美单反相机（如 Canon EOS R6 II），同时确保保留精确的面部特征和自然的清晰度。

![照片修复至单反相机质量](https://cms-assets.youmind.com/media/1770532823419_d4u8hz_HAh6eN5bsAAB0Pa.jpg)
![照片修复至单反相机质量](https://cms-assets.youmind.com/media/1770532823419_kgzesi_HANkG11aIAEaPHY.jpg)
![照片修复至单反相机质量](https://cms-assets.youmind.com/media/1770532823793_f1rnwf_HAh6eT0acAIXYgT.jpg)
![照片修复至单反相机质量](https://cms-assets.youmind.com/media/1770532824834_odfpfw_HANkG2_bMAIvEoC.jpg)

```
"Restore this old photo into professional portrait of DLSR - quality colour and detail, using an advanced upscaling algorithm comparable to the results from canon EOS R6 II. Ensure the restored the image looks natural, retains exact facial features, has great clarity......"
```

[[Old Photo Restoration]] [[DSLR Quality Enhancement]] [[Photo Upscaling]]

---

### 88. 波西米亚风人像与牛仔靴道具

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细的 JSON 提示，用于 Gemini Nano Banana Pro，专注于生成一张超逼真、情绪化的肖像照：一位身穿田园风/波西米亚风连衣裙的苗条年轻女子，斜倚在石墙上，手持一双深绿色牛仔靴作为道具。

![波西米亚风人像与牛仔靴道具](https://cms-assets.youmind.com/media/1770532804820_d99vbi_HAh4GvsXAAAE-Cj.jpg)

```
{
  "prompt_details": {
    "subject": {
      "type": "Young woman",
      "appearance": {
        "hair": "Long, dark chestnut brown, loose waves, falling over face, messy aesthetic",
        "skin": "Fair complexion, smooth texture, natural finish",
        "face": "Looking downward, face partially obscured by hair, introspective expression",
        "body_type": "Slender, fit"
      },
      "pose": {
        "stance": "Leaning against a stone wall, body slightly angled",
        "hands": "Right hand resting gently on chest/neck with fingers splayed, left hand holding a green object (boot) down by her side",
        "gaze": "Downward, avoiding eye contact"
      }
    },
    "clothing": {
      "dress": {
        "style": "Off-the-shoulder mini dress, cottagecore/boho style",
        "fabric": "Lightweight cotton or linen blend",
        "color": "Cream/off-white base",
        "pattern": "Small, delicate floral print with purple and yellow wildflowers",
        "details": ["Ruffled tiered skirt", "Puffed short sleeves", "Sweetheart neckline", "Corset-style bodice structure"]
      },
      "accessories": [
        "Thin black choker necklace",
        "Multiple silver rings on fingers",
        "Red beaded bracelet on left wrist",
        "Holding a dark green, crocodile-texture cowboy boot"
      ]
    },
    "environment": {
      "background": "Textured stone masonry wall",
      "details": "Large, irregular grey and beige stone blocks, rough texture, natural architectural backdrop",
      "setting": "Outdoor or semi-outdoor daylight setting"
    },
    "lighting": {
      "type": "Soft natural daylight",
      "quality": "Diffused, even illumination, soft shadows",
      "direction": "Front-lit but soft"
    },
    "styling": {
      "aesthetic": "Bohemian, chic, feminine, soft grunge undertones",
      "mood": "Casual, candid, slightly moody, artistic"
    },
    "camera_details": {
      "shot_type": "Medium shot (thigh-up)",
      "angle": "Eye-level",
      "lens": "85mm prime lens for flattering portrait compression",
      "aperture": "f/2.8 for slight depth of field separation from the wall",
      "focus": "Sharp focus on the subject and dress texture"
    },
    "technical_specifications": {
      "quality": "Ultra Photorealistic, 8k resolution, highly detailed",
      "texture_quality": "High fidelity fabric textures, realistic skin pores, detailed stone masonry",
      "engine": "Unreal Engine 5 render style or high-end photography"
    }
  }
}
```

[[Stone Wall Setting]]

---

### 89. 超电影感奢华冷萃咖啡产品摄影

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-02-07  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张奢华冷萃咖啡瓶（“OBSIDIAN BREW”）的超电影感商业产品照片。它指定了容器材料（烟熏琥珀色玻璃、拉丝金属盖）、构图（空中漂浮、动态倾斜）、环境（体积雾、悬浮咖啡豆）以及戏剧性的低调影棚照明，以实现高对比度、高端的广告渲染效果。

![超电影感奢华冷萃咖啡产品摄影](https://cms-assets.youmind.com/media/1770532789832_cpzyms_HAh0xeHacAIWcyo.jpg)
![超电影感奢华冷萃咖啡产品摄影](https://cms-assets.youmind.com/media/1770532789847_8unyhc_HAh0xyRacAQk9tY.jpg)
![超电影感奢华冷萃咖啡产品摄影](https://cms-assets.youmind.com/media/1770532789817_93arxi_HAh0xx-acAM1Zff.jpg)
![超电影感奢华冷萃咖啡产品摄影](https://cms-assets.youmind.com/media/1770532790786_mugexe_HAh0xxYacAA6XfA.jpg)

```
{
"master_prompt": {
"product": {
"type": "luxury cold brew coffee bottle",
"brand_name": "{argument name="brand name" default="OBSIDIAN BREW"}",
"container": "sleek cylindrical glass bottle",
"finish": "smoked amber glass with subtle matte coating",
"label_style": "minimalist typography with embossed gold foil accents",
"cap": "brushed metal cap with satin black finish"
},
"composition": {
"scene_type": "ultra-cinematic commercial product photography",
"orientation": "vertical",
"aspect_ratio": "3:4",
"camera_angle": "dynamic diagonal tilt",
"subject_position": "floating mid-air, slightly off-center for dramatic tension",
"motion": "frozen liquid coffee swirls and splashes suspended in space"
},
"environment": {
"background": "deep charcoal-to-black gradient backdrop",
"atmosphere": "volumetric mist and fine coffee vapor drifting around the product",
"elements": [
"slow-motion coffee waves",
"glossy roasted coffee beans suspended mid-air",
"shattered crystal-clear ice fragments",
"microscopic condensation droplets on glass surface"
]
},
"lighting": {
"style": "low-key dramatic studio lighting",
"key_light": "soft directional light highlighting bottle contours",
"rim_lights": "strong edge lights outlining the silhouette",
"fill_light": "minimal, preserving deep shadows",
"highlights": "metallic gold reflections on label and cap",
"contrast": "high contrast with rich blacks and controlled specular highlights"
},
"color_palette": {
"primary_colors": ["black", "espresso brown", "smoked amber"],
"accent_colors": ["metallic gold", "warm caramel highlights"]
},
"camera_settings": {
"lens": "macro cinema lens",
"depth_of_field": "shallow, subject-isolated focus",
"focus_point": "brand logo and glass texture",
"clarity": "extreme micro-detail visibility"
},
"render_quality": {
"resolution": "8K ultra-high-definition",
"style": "hyper-realistic premium advertising render",
"textures": "physically accurate glass, liquid, metal, and condensation",
"noise": "none",
"artifacts": "none",
"sharpness": "ultra-crisp with cinematic softness in background"
},
"mood": {
"tone": "bold, moody, and ultra-premium",
"emotion": "luxury, intensity, craftsmanship, indulgence"
},
"final_output": {
"usage": "high-end commercial advertising",
"branding_focus": "strong brand recall with hero-product dominance",
"visual_style": "luxury beverage campaign aesthetic"
}
}
```

[[Volumetric Fog]] [[Low Key Studio Lighting]]

---

### 90. 令人惊叹的 8K 户外照片提示

**Author**: [blogbursthub](https://x.com/blogbursthub)  **Date**: 2026-02-07  **Language**: en

> 一条推文，引用了 Gemini Nano Banana 生成的一张令人惊叹的 8K 户外照片提示，完整提示可在图片替代文本中查看。

![令人惊叹的 8K 户外照片提示](https://cms-assets.youmind.com/media/1770532866502_ounox6_HAh0B17aEAAvsEl.jpg)

```
A stunning 8k outdoor photo of a woman standing on a cliff edge overlooking a vast, misty mountain range at sunrise. She is wearing a flowing, deep emerald green dress that contrasts sharply with the pale gold and blue tones of the sky. The lighting is dramatic, with strong rim lighting outlining her silhouette and soft, volumetric light filling the scene. The composition uses the rule of thirds, placing the woman slightly off-center for maximum impact. The image should have hyper-realistic detail, cinematic color grading, and a shallow depth of field to emphasize the subject against the epic landscape. Shot on a high-end medium format camera.
```

[[8K Photography]]

---

### 91. 躺着的中年男子肖像

**Author**: [路飞 🏴‍☠️ AI 研究员🧐](https://x.com/0xluffy_eth)  **Date**: 2026-02-07  **Language**: zh

> 一个简单的图像生成提示，用于创建源图像，以便通过 Nano Banana 进行进一步优化，描绘了一名中年男子躺在床上，以正面视角拍摄。

![躺着的中年男子肖像](https://cms-assets.youmind.com/media/1770532843608_97hul6_HAhuGLza4AAqdio.jpg)

```
{argument name="年龄" default="40多岁"}的男性，躺在床上，正面镜头。
```

[[Reclining Male Portrait]]

---

### 92. 超电影感蛋白棒产品摄影

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-02-07  **Language**: en

> 一个专注于生成高端蛋白棒超电影感产品摄影的提示词。它强调动态动作，例如漂浮的元素（巧克力、焦糖、坚果）和高速飞溅效果，并利用戏剧性的影棚灯光和丰富的调色板来营造奢华的广告氛围。

![超电影感蛋白棒产品摄影](https://cms-assets.youmind.com/media/1770532754408_296sfb_HAhtxysacAEKuf5.jpg)
![超电影感蛋白棒产品摄影](https://cms-assets.youmind.com/media/1770532754544_g7ee8i_HAhtxx_bkAA0Nyb.jpg)
![超电影感蛋白棒产品摄影](https://cms-assets.youmind.com/media/1770532754547_5jr2ss_HAhtxwKaEAAeQv0.jpg)
![超电影感蛋白棒产品摄影](https://cms-assets.youmind.com/media/1770532756260_xsjnhr_HAhtxxWaUAAbxOf.jpg)

```
Ultra-cinematic product photography of a premium protein bar wrapped in metallic packaging, floating at a dynamic angle; explosive chocolate chunks, caramel drips, and nut fragments frozen mid-air; high-speed splash and crumble effect, dramatic studio lighting with sharp highlights; rich brown and gold palette, ultra-detailed textures, shallow depth of field, photorealistic, 8K, fitness luxury advertising.
```

[[Floating Ingredient Effect]]

---

### 93. 身穿淡粉色家居服的女性超逼真全身照

**Author**: [Javeriya 🇺🇸](https://x.com/JadoonKhan281)  **Date**: 2026-02-07  **Language**: en

> 一张 8K 超现实照片的图像生成提示，描绘了一位年轻女性身着单色柔和粉色家居服套装（连帽衫和运动裤），置身于现代公寓中。提示要求从背后拍摄全身照，她回眸望向镜头，光线柔和，并着重表现纹理和细节。

![身穿淡粉色家居服的女性超逼真全身照](https://cms-assets.youmind.com/media/1770532832782_478lam_HAhq8H7bAAA6JYC.jpg)
![身穿淡粉色家居服的女性超逼真全身照](https://cms-assets.youmind.com/media/1770532832906_7ac9gq_HAhq8CbbUAAuc2z.jpg)
![身穿淡粉色家居服的女性超逼真全身照](https://cms-assets.youmind.com/media/1770532833007_ylnsdw_HAhq8N6awAAcEif.jpg)

```
{
  "image_prompt_schema": {
    "subject_description": {
      "demographics": "Young woman, fit physique, mid-20s",
      "hair": "Long, wavy blonde hair, cascading down her back",
      "expression": "Slightly looking back over her shoulder with a soft, neutral expression",
      "pose": "Standing with her back to the camera, looking over her shoulder, one leg slightly bent and crossed behind the other"
    },
    "apparel_and_accessories": {
      "outfit_theme": "Monochromatic pastel pink lounger aesthetic",
      "upper_body": "Pink zip-up hoodie worn off-the-shoulders, showing the back and neck",
      "lower_body": "Matching pink baggy sweatpants",
      "footwear": "Pink and white basketball-style sneakers",
      "tech": "Pink gaming headphones resting on the gaming chair in front of her"
    },
    "environment_and_background": {
      "setting": "Indoor living space, open-plan apartment",
      "furniture": "Pink and white racing-style gaming chair positioned in front of her",
      "background_elements": "Modern kitchen with white cabinetry, stainless steel microwave, breakfast bar with white stools, and a cat tree in the corner",
      "flooring": "Wood laminate flooring"
    },
    "lighting_and_atmosphere": {
      "type": "Soft indoor ambient lighting",
      "mood": "Cozy, casual, influencer aesthetic",
      "color_palette": "Dominant pastel pinks, soft whites, and warm neutrals"
    },
    "technical_specifications": {
      "art_style": "Ultra-realistic photography",
      "resolution": "8k UHD, HDR, highly detailed textures",
      "camera_properties": "Full body shot from behind, sharp focus on subject, shallow depth of field for the background",
      "quality_tags": "Masterpiece, best quality, photorealistic, raw photo"
    }
  },
  "generation_parameters": {
    "aspect_ratio": "9:16",
    "orientation": "Vertical",
    "chaos": 0,
    "stylize": 750
  },
  "full_compiled_prompt": "Ultra-realistic full body photo from behind of a young woman with long wavy blonde hair looking back over her shoulder. She is wearing a pastel pink hoodie off-the-shoulders and matching pink sweatpants with pink and white sneakers. She is standing in a modern apartment behind a pink gaming chair. Background features a clean white kitchen and a cat tree. 8k resolution, UHD, soft ambient lighting, highly detailed texture, vertical aspect ratio --ar 9:16 --v 6.0"
}
```

[[Modern Apartment Setting]]

---

### 94. 超逼真克什米尔瓦兹旺（Wazwan）信息图提示

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-07  **Language**: en

> 一个 JSON 提示，旨在生成一张超现实、电影级的克什米尔瓦兹旺（Kashmiri Wazwan）美食信息图。图中展示了一碗传统铜制罗根乔什（Rogan Josh），蒸汽氤氲，周围漂浮着悬空的食材（羊肉、奶酪、香料），凝固在动态中，适用于高端美食可视化或教育内容。

![超逼真克什米尔瓦兹旺（Wazwan）信息图提示](https://cms-assets.youmind.com/media/1770532867477_icxnrb_HAhge4eaQAAtljM.jpg)
![超逼真克什米尔瓦兹旺（Wazwan）信息图提示](https://cms-assets.youmind.com/media/1770532867678_wlvwx3_HAhge5kaEAAKcKL.jpg)

```
{
  "project": "CuisineInfographic",
  "metadata": {
    "style": "Hyper-Realistic",
    "theme": "Kashmiri Wazwan",
    "resolution": "8K_Ultra_HD"
  },
  "scene_setup": {
    "background": "Rustic_Dark_Wood",
    "lighting": "Cinematic_Studio_Warm",
    "camera": {
      "type": "DSLR_Full_Frame",
      "focus": "Sharp_Macro",
      "depth_of_field": "Shallow_Bokeh"
    }
  },
  "render_elements": {
    "base_anchor": {
      "object": "Traditional_Kashmiri_Copper_Bowl",
      "content": "Steaming_Rogan_Josh",
      "effects": ["Dramatic_Steam", "Volumetric_Vapor"]
    },
    "levitating_entities": [
      { "item": "Tender_Mutton_Chunks", "texture": "Juicy_Fibrous" },
      { "item": "Fried_Paneer_Cubes", "texture": "Golden_Crispy" },
      { "item": "Kashmiri_Red_Chili", "state": "Whole_Dried" },
      { "item": "Saffron_Water_Splashes", "viscosity": "Glossy_Orange" },
      { "item": "Green_Cardamom_Pods", "arrangement": "Motion_Frozen" },
      { "item": "Cinnamon_Bark", "detail": "Ultra_Textured" },
      { "item": "Fresh_Mint_Leaves", "color": "Vibrant_Green" }
    ],
  "ui_overlay": {
    "language": "{argument name="overlay language" default="Indonesian"}",
    "elements": {
      "pointer_lines": "Thin_Minimalist_White",
      "font_style": "Modern_Editorial_Sans",
      "labels": {
        "mutton": "{argument name="mutton label" default="Daging Domba Lembut"}",
        "chili": "Cabai Merah Kashmir",
        "paneer": "Tahu/Paneer Goreng",
        "sauce": "Kuah Merah Kental"
      }
    }
  }
}
```

[[Floating Ingredients]]

---

### 95. 超逼真的街头照片，保留特定主体

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-02-07  **Language**: en

> 一个高度具体的提示，用于生成一张超逼真的冬季街头照片，照片中有一个男人。该提示要求 1:1 保留上传的面部/身体特征，并指定了场景（湿沥青、光秃秃的树木、城市街道）、服装（超大号深橄榄色连帽衫、蓬松的米色羊毛围巾）和技术细节（RAW iPhone 拍摄效果、冷白平衡、自然皮肤纹理），以实现最大程度的真实感。

![超逼真的街头照片，保留特定主体](https://cms-assets.youmind.com/media/1770532799758_51rv1c_HAheeqnbcAALkJ9.jpg)
![超逼真的街头照片，保留特定主体](https://cms-assets.youmind.com/media/1770532800103_unwnbu_HAhee0XacAEtBZa.jpg)

```
Generate a realistic street photo of a guy on your iPhone in the casual street photography style. Use the face from the uploaded photo as the only and precise appearance standard: preserve facial features, face and body proportions, age, hair color and length at a 1:1 ratio, without even 1% change. The guy is standing on a city street in winter, leaning his shoulder slightly against a black street lamp on the sidewalk. His pose is relaxed, one hand in his pocket, the other hanging loosely. In the background are an intersection, bare winter trees, tall buildings, and a few people in the distance; the asphalt is wet after snow, creating a cool city atmosphere. Clothing: an oversized dark olive hoodie without a hood, a voluminous beige-cream scarf partially covers his head and hangs down slightly; the fabric is wool, the fibers are visible. Light: natural winter daylight, soft shadows, cool white balance, no flash. Realism: ultra-realistic photo, natural skin texture, pores, subtle imperfections, realistic fabric textures (scarf wool, thick cotton hoodie), no neural network effects. Quality: photo from the iPhone's main camera, RAW iPhone look, slight digital noise, natural sharpness. Aspect ratio 3:4.
```

[[Face Matching]]

---

### 96. 拉森风格的海豚与虎鲸画作

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个给 Nano Banana Pro（Gemini 3 Pro 图像）的提示，要求创作一幅克里斯蒂安·里斯·拉森（Christian Riese Lassen）风格的画作，画中包含海豚和虎鲸。

![拉森风格的海豚与虎鲸画作](https://cms-assets.youmind.com/media/1770532847647_zdhrqf_GCRihaybMAAN19f.jpg)
![拉森风格的海豚与虎鲸画作](https://cms-assets.youmind.com/media/1770532847807_59i84q_HAhdX-ubQAA6bKG.jpg)

```
ラッセンみたいな絵をイルカとシャチを入れて1枚出して！
```

[[Christian Riese Lassen Style]]

---

### 97. 埃舍尔风格光学错觉生成

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 为 Nano Banana Pro（Gemini 3 Pro 图像）提供一个提示，要求生成一张类似于 M.C. 埃舍尔（M.C. Escher）作品的视错觉或不可能结构图像。

![埃舍尔风格光学错觉生成](https://cms-assets.youmind.com/media/1770532850658_sabahh_GCRihaybMAAN19f.jpg)
![埃舍尔风格光学错觉生成](https://cms-assets.youmind.com/media/1770532850858_299fjj_HAhb8Lfa0AAf1lJ.jpg)

```
エッシャーの
騙し絵みたいな絵を１枚出して！
```

[[Artistic Style Transfer]] [[Optical Illusion Art]]

---

### 98. 米开朗基罗《最后的审判》风格图片

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个尝试使用 Nano Banana Pro (Gemini 3 Pro Image) 生成米开朗基罗《最后的审判》风格图像的提示。用户指出结果与预期风格大相径庭。

![米开朗基罗《最后的审判》风格图片](https://cms-assets.youmind.com/media/1770532854352_i61uaf_GCRihaybMAAN19f.jpg)
![米开朗基罗《最后的审判》风格图片](https://cms-assets.youmind.com/media/1770532854595_g9rzoz_HAhbCQNacAY42DO.jpg)

```
ミケランジェロの
最後の審判みたいな絵を１枚出して！
```

[[Artistic Style Transfer]]

---

### 99. 修拉风格点彩画图像生成

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-07  **Language**: ja

> 一个用于 Nano Banana Pro (Gemini 3 Pro 图像) 的提示，请求生成一幅具有艺术家修拉（Seurat）点彩画风格的图像。

![修拉风格点彩画图像生成](https://cms-assets.youmind.com/media/1770532847543_x24csx_GCRihaybMAAN19f.jpg)
![修拉风格点彩画图像生成](https://cms-assets.youmind.com/media/1770532847945_56iz1p_HAhaPRFbQAAbAhC.jpg)

```
スーラの
点描画みたいな絵を１枚出して！
```

[[Artistic Style Transfer]]

---

### 100. 角色生成与文档摘要可视化

**Author**: [大塚武](https://x.com/takeshi_otsuka)  **Date**: 2026-02-07  **Language**: ja

> 用户描述了一项测试，该测试使用 Nano Banana 生成一个角色，然后将文档摘要可视化为一张“ponchi-e”（简单的图表/插图）。提示本身暗示了对角色生成和随后的可视化请求。

![角色生成与文档摘要可视化](https://cms-assets.youmind.com/media/1770532854281_sorrzj_HAhVo5WbwAAgW-s.jpg)

```
キャラ生成してNano Bananaにお願いすればこんなのが数秒で出来ちゃうと言う…。

資料の要約を1枚のポンチ絵で作れるかどうかをテスト
```

[[Character Generation]]

---

### 101. Kollywood 电影海报照片提示词

**Author**: [blogbursthub](https://x.com/blogbursthub)  **Date**: 2026-02-07  **Language**: en

> 一个旨在生成宝莱坞电影海报风格照片的提示，使用 Gemini Nano Banana 模型创建。实际的提示文本在图像的 alt 文本中引用。

![Kollywood 电影海报照片提示词](https://cms-assets.youmind.com/media/1770532864197_t3k16v_HAhR_WobMAA6Qvb.jpg)

```
Kollywood cinematic film Post photo prompt Gemini Nano Banana creation.
```

[[Kollywood Movie Poster]]

---

### 102. 爆炸视图产品渲染提示

**Author**: [Ivanna | AI Art & Prompts](https://x.com/ivanka_humeniuk)  **Date**: 2026-02-07  **Language**: en

> 一个详细的图像生成提示，旨在创建一个超现实、爆炸视图的产品图，强调技术精度和高端设计期刊美学。它指定了布局、图形元素（水墨风格线条、极简标签）、调色板（单色带一个强调色）和氛围，从而产生高度教育性和精致的视觉效果。

![爆炸视图产品渲染提示](https://cms-assets.youmind.com/media/1770532863603_9hyvyq_HAhRh9HXIAEIS7l.jpg)
![爆炸视图产品渲染提示](https://cms-assets.youmind.com/media/1770532864182_6ufx54_HAhRh9OXgAAPK26.jpg)

```
A hyper-realistic {argument name="product name" default="[INSERT PRODUCT]"} presented in an "exploded view" where internal components float upward in a gravity-defying vertical stack. Graphic Elements: Fine technical lines (ink-style) connecting parts to minimalist sans-serif labels. Layout: Horizontal split — Left side: Photorealistic 3D render with soft shadows; Right side: Matching architectural line drawing (blueprint style) on textured paper. Color Palette: Monochrome technical sketch with a {argument name="accent color percentage" default="15%"} accent color on key functional parts. Overall Mood: Design journal aesthetic, premium, calm, and highly educational.
```

[[Monochrome Palette]]

---

### 103. Y2K 风格年轻女性快照

**Author**: [Rowan](https://x.com/rowanali09)  **Date**: 2026-02-07  **Language**: en

> 一个详细的 JSON 提示，用于生成一张受 Y2K 抓拍摄影风格启发的年轻女性图像。它详细描述了她的外貌（姜红色头发，白皙肤色）、服装（印有“born to be fast”字样的短款撞色 T 恤，褪色的芥末黄牛仔裤）、场景（不锈钢墙）和摄影风格（直射机顶闪光灯，硬阴影，胶片颗粒纹理）。

![Y2K 风格年轻女性快照](https://cms-assets.youmind.com/media/1770532789677_tv54zb_HAhMiSAacAAoaFy.jpg)
![Y2K 风格年轻女性快照](https://cms-assets.youmind.com/media/1770532789739_hab9fn_HAhMiquacAQ9MNi.jpg)
![Y2K 风格年轻女性快照](https://cms-assets.youmind.com/media/1770532789734_eeeo90_HAhMiVDaAAAvNwZ.jpg)

```
{
  "subject": {
    "description": "Young woman with long, wavy ginger-red hair",
    "pose": {
      "stance": "Leaning back against a metallic wall",
      "arms": "Right arm hanging straight down by side, left hand tucked into the front pocket of the bottoms",
      "expression": "Calm, confident, chin slightly lifted, direct gaze at the camera"
    },
    "appearance": "Pale complexion, minimal natural makeup"
  },
  "outfit": {
    "top": {
      "type": "Cropped ringer t-shirt (baby tee)",
      "color": "White body with bright mustard yellow short sleeves and neckline trim",
      "design": {
        "text": "{argument name="t-shirt text" default="born to be fast"}",
        "font_style": "Bold, lowercase sans-serif text in matching mustard yellow",
        "graphics": "Three yellow stars positioned above the text, yellow stylized lightning bolt symbol (resembling the Opel logo) below the text"
      }
    },
    "bottom": {
      "type": "Denim jeans or shorts",
      "color": "Faded mustard yellow",
      "details": "Button fly, front pockets, visible stitching, mid-rise fit"
    },
    "accessories": {
      "bag": "Small black quilted leather shoulder bag with a silver chain strap carried over the right shoulder"
    }
  },
  "setting": {
    "location": "Indoor hallway or elevator area",
    "background": {
      "left_side": "Large brushed stainless steel metal panel (elevator doors) reflecting the subject slightly",
      "right_side": "Plain light grey painted wall",
      "details": "Small dark rectangular control panel or sensor on the upper right wall"
    }
  },
  "photography_style": {
    "lighting": "Direct on-camera flash",
    "shadows": "Hard drop shadow visible behind the subject on the metal and painted walls",
    "aesthetic": "Candid, Y2K inspired, snapshot style, film grain texture",
    "angle": "Eye-level, medium shot capturing from mid-thigh up"
  }
}
```

[[Film Grain Texture]] [[Crop Top Fashion]]

---

### 104. 纸板潜艇设计生成

**Author**: [aokuma](https://x.com/ai5809514366862)  **Date**: 2026-02-07  **Language**: ja

> 一个用于 NanoBananaPro 的提示，根据一个纸箱的输入图像，生成一个儿童潜水艇的设计概念。

![纸板潜艇设计生成](https://cms-assets.youmind.com/media/1770532852108_rjn5w6_HAhL7JcawAAAnWg.jpg)
![纸板潜艇设计生成](https://cms-assets.youmind.com/media/1770532852280_ujjfq7_HAhL7MNacAEA4HG.jpg)
![纸板潜艇设计生成](https://cms-assets.youmind.com/media/1770532852341_5uv9jr_HAhL7LdacAMja8B.jpg)

```
これで子供向けに潜水艦を作ればどんな感じになるか
```

[[Cardboard Submarine Design]]

---

### 105. 复古街头时尚肖像

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-02-07  **Language**: en

> 一个详细的 JSON 提示，用于 Gemini Nano Banana Pro 生成一张具有复古休闲街头摄影美学风格的单人生活时尚肖像。它详细说明了拍摄对象的形象、服装（芥末黄衬衫、深棕色裤子），以及一个带有复古物品和倒影的分层都市店面背景。

![复古街头时尚肖像](https://cms-assets.youmind.com/media/1770532822620_67w6fl_HAhHXwcaUAA72Fq.jpg)

```
{ "image_type": "single lifestyle fashion portrait", "overall_style": "retro casual street photography with vintage warmth", "composition": { "framing": "medium-full body seated portrait", "orientation": "vertical", "camera_angle": "eye-level", "perspective": "front-facing with slight diagonal body orientation", "balance": "subject centered with layered background elements", "visual_layers": [ "foreground: seated subject", "midground: shop window reflection", "background: bicycle and store interior objects" ] }, "subjects": { "count": 1, "description": "young woman with short brown hair", "pose": "seated cross-legged on a painted bench, head resting on hand", "expression": "soft smile, relaxed and confident", "gaze": "direct eye contact with camera", "emotion": "casual, approachable, nostalgic" }, "appearance": { "hair": { "color": "medium brown", "length": "short bob", "texture": "smooth with slight natural wave", "styling": "tucked with bangs", "accessory": "patterned headband" }, "makeup": { "style": "natural with vintage touch", "details": [ "defined brows", "soft eyeliner", "natural pink lips", "even matte complexion" ] } }, "wardrobe": { "top": { "type": "short-sleeve t-shirt", "color": "mustard yellow", "fit": "relaxed", "details": "small minimal chest text detail" }, "bottom": { "type": "high-waisted pants", "color": "dark brown", "fit": "loose straight-leg" }, "footwear": { "type": "sneakers", "color": "brown and white", "style": "retro athletic" }, "accessories": [ { "type": "crossbody bag", "material": "fabric", "pattern": "zigzag geometric", "color": "brown and beige" }, { "type": "headband", "material": "fabric", "pattern": "floral", "color": "yellow and green" }, { "type": "ring", "material": "metal", "color": "silver" } ] }, "environment": { "setting": "urban storefront exterior", "surface": "painted wooden bench", "background_objects": [ "vintage bicycle", "skis", "woven bag", "shop interior reflections" ], "vibe": "artsy, boutique, retro street scene" }, "lighting": { "type": "natural daylight", "direction": "front-side lighting", "quality": "soft and even", "shadows": "minimal and diffused", "reflection_effects": "window reflections add depth and layering" }, "color_palette": { "dominant_colors": [ "mustard yellow", "brown", "teal blue" ], "accent_colors": [ "white", "beige", "green" ], "contrast": "moderate with warm-cool balance", "saturation": "moderate with vintage warmth" }, "background": { "depth_of_field": "deep, most elements in focus", "texture": "busy but cohesive", "visual_interest": "high due to layered objects and reflections" }, "technical_traits": { "lens_look": "standard focal length", "sharpness": "high overall", "noise": "minimal", "post_processing": [ "warm color grading", "slight contrast enhancement", "film-like tonal balance" ] }, "artistic_elements": { "mood": "nostalgic, relaxed, creative", "aesthetic": "retro street fashion", "storytelling": "casual pause during a city s
```

[[Lifestyle Fashion Photography]]

---

### 106. 掌上迷你宠物图像生成提示

**Author**: [예삐](https://x.com/yeppisim)  **Date**: 2026-02-07  **Language**: ko

> 一个韩语提示，旨在生成一张宠物（狗或猫）的图片，宠物被微缩到刚好能放在用户手掌上，并从俯视角度观看。关键指令是保持宠物原有的面部特征和表情，不发生扭曲。

![掌上迷你宠物图像生成提示](https://cms-assets.youmind.com/media/1770532860167_h57e8a_HAhBW-wbYAAEqj6.jpg)
![掌上迷你宠物图像生成提示](https://cms-assets.youmind.com/media/1770532859805_53dcsd_HAhBW-uacAAvqdY.jpg)

```
사진 속 {argument name="동물" default="동물"}을 손바닥 위에 쏙 올라가는 미니어처 크기로 만들어줘. 위에서 아래로 내려다보는 구도로 잡고, 원본의 얼굴 특징과 표정은 왜곡 없이 그대로 유지해줘
```

[[Pet Photography]] [[Scale Manipulation]]

---

### 107. 棒棒糖少女软颓风肖像 (JSON)

**Author**: [Alice Glassier](https://x.com/aliceglassierai)  **Date**: 2026-02-07  **Language**: en

> 一个详细的 JSON 提示，用于生成一张“妖娆、柔和垃圾摇滚、浪漫恐怖”风格的特写肖像，描绘一个主体咬着心形棒棒糖，强调胶片颗粒、特定的调色板以及脸上的红色金属贴纸。

![棒棒糖少女软颓风肖像 (JSON)](https://cms-assets.youmind.com/media/1770532783192_i5pv2w_HAg_JD4XIAA3w3N.jpg)
![棒棒糖少女软颓风肖像 (JSON)](https://cms-assets.youmind.com/media/1770532783414_2gsk9f_HAg_QIhXcAA1lV3.jpg)
![棒棒糖少女软颓风肖像 (JSON)](https://cms-assets.youmind.com/media/1770532783797_3t0xz5_HAg_QIjWEAAYuzo.jpg)

```
{
  "visual_style": {
    "aesthetic_tags": ["Coquette", "Soft Grunge", "Vintage Indie", "Romantic Macabre"],
    "subject": {
      "focus": "Extreme close-up portrait of a person's face",
      "pose": "Head tilted slightly, eyes looking up and to the side (averted gaze), hand partially visible at the bottom left holding a lollipop",
      "expression": "Playful yet moody, biting down on a heart-shaped lollipop"
    },
    "color_palette": {
      "dominant_colors": ["#BC0000 (Crimson Red)", "#E8B4A2 (Peach/Skin Tones)", "#F4EBD9 (Cream/Neutral)"],
      "accent_colors": ["#A3C6C4 (Pale Sage Green - Ring Stone)", "#000000 (Black - Liner/Straps)"],
      "temperature": "Warm and saturated"
    },
    "composition": {
      "framing": "Macro/Tight crop",
      "depth_of_field": "Shallow (bokeh effect on ears and background)",
      "angle": "Eye level, slightly tilted",
      "balance": "Asymmetrical with hand and lollipop creating a diagonal lead"
    },
    "makeup_and_face": {
      "skin_texture": "Natural, visible freckles and pores",
      "eye_makeup": "Shimmery reddish eyeshadow, dark eyeliner, heavy mascara",
      "lips": "Natural/glossy base, obscured by lollipop",
      "adornments": "Red metallic heart-shaped stickers/confetti scattered across the face"
    },
    "outfits_and_accessories": {
      "jewelry": [
        "Delicate silver septum hoop",
        "Multiple small silver ear studs",
        "Ornate silver rings, one featuring a light green/turquoise stone"
      ],
      "clothing": "Thin black spaghetti strap",
      "props": "Red translucent heart-shaped lollipop on a white stick"
    },
    "lighting_and_atmosphere": {
      "source": "Soft, diffused natural light",
      "vibe": "Nostalgic, intimate, youthful, slightly edgy",
      "shadows": "Soft, minimal harshness"
    },
    "technical_effects": {
      "texture": "Fine film grain",
      "sharpness": "High focus on the eyes and center of the face, softening towards the edges",
      "saturation": "High saturation on red elements to make them pop"
    }
  }
}
```

[[Close-Up Portrait]] [[Coquette Aesthetic]] [[Film Grain Effect]]

---

### 108. 更衣室复古海报女郎写真 (iPhone 风格)

**Author**: [Alice Glassier](https://x.com/aliceglassierai)  **Date**: 2026-02-06  **Language**: en

> 一个高度详细的提示，用于生成一张超逼真的图像，模仿用 iPhone 17 Pro Max 拍摄的抓拍式幕后照片。场景是一个凌乱的复古化妆间梳妆台，一位迷人的模特身穿红色缎面迷你连衣裙和高跟鞋，捕捉到一种性感、复古女郎风格的氛围，具有逼真的光线和皮肤纹理。

![更衣室复古海报女郎写真 (iPhone 风格)](https://cms-assets.youmind.com/media/1770446059203_0ejdhc_HAg0aWiWMAA1jB9.jpg)
![更衣室复古海报女郎写真 (iPhone 风格)](https://cms-assets.youmind.com/media/1770446059097_g0q7up_HAg0aWiXMAA3upi.jpg)
![更衣室复古海报女郎写真 (iPhone 风格)](https://cms-assets.youmind.com/media/1770446059198_arhx8i_HAg0aWfX0AIANJa.jpg)
![更衣室复古海报女郎写真 (iPhone 风格)](https://cms-assets.youmind.com/media/1770446061168_dycfrl_HAg0mxkWcAAzOKZ.jpg)

```
{
"scene_description": {
"location": "Retro dressing room vanity with cluttered cosmetics, red rose, yellow 'Alice' ashtray, hubcap wall decor, pink 'XOXO' writing on mirror, high-fashion editorial photoshoot",
"vibe": "Sultry, confident, glamorous pin-up inspired moment, seductive retro luxury mood",
"lighting": "Warm practical spotlight from above and side mixed with ambient room light, natural-looking skin highlights, realistic glossy sheen on red satin and heels, soft but defined shadows, believable light falloff",
"camera_settings": "Shot on iPhone 17 Pro Max main camera (24mm equivalent), f/1.78, natural shallow depth of field, realistic iPhone computational photography look, ultra-crisp yet natural detail, subtle lens flare and micro-contrast, 48MP ProRAW-style quality downsampled to 12MP look, ultra-photorealistic, zero AI smoothness, visible authentic skin texture and pores, medium-full body shot"
},
"primary_subjects": [
{
"character": "attached celebrity",
"role": "Glamorous photoshoot model",
"action": "Sitting on high red leather bar stool, one leg extended high forward resting on vanity counter with red high-heel shoe, red satin ribbon wrapped and pulled taut between both hands, other leg bent and dangling, leaning back slightly, confident direct gaze at camera",
"details": "Long blonde wavy hair with small hair clip, bold dramatic eye makeup, glossy red lips, very short shiny {argument name="dress color" default="red"} satin strapless mini dress with subtle ruffle/peplum edge, {argument name="shoe color" default="red"} high heels with ankle strap detail, large gold bracelet, realistic skin texture with natural pores, subtle imperfections and glow from real lighting"
}
],
"environment_details": {
"crowd": "None – vanity focus",
"architecture": "Vintage wooden makeup dresser cluttered with lipsticks, nail polish, bottles, brushes, red rose in vase, yellow 'KEOR UNREAL' ashtray, chrome hubcaps on brick wall, pink 'XOXO Sydney' writing on mirror, red ribbons scattered on floor",
"fidelity": "Ultra-photorealistic real photograph look, iPhone 17 Pro Max natural rendering, lifelike satin folds and realistic light reflection, authentic skin micro-texture, natural hair strands, exact seductive pose, precise real-world lighting behavior, dominant red color scheme, glamorous burlesque photoshoot captured like a real behind-the-scenes iPhone shot"
}
}
```

[[Retro Pinup Aesthetic]]

---

### 109. 富有感染力的历史场景生成与情感对话

**Author**: [铁柱AGI](https://x.com/cgnot996)  **Date**: 2026-02-06  **Language**: zh

> 一个为大型语言模型或视频生成模型（如 Seedance 2.0/Sora 2）设计的文本提示，用于创作一个极具戏剧性的历史场景，其中包含激烈的对话、情感冲突和角色揭示。该场景聚焦于萧景珩和沈清棠两位角色，讨论他们共同的转世和失败经历。

![富有感染力的历史场景生成与情感对话](https://cms-assets.youmind.com/media/1770446081423_tudplx_HAgy---a8AAebHJ.jpg)

```
萧景衡满脸血腥的拔剑指着沈青棠，崩溃的大喊："朕陪你重生了九十九次，你竟然还没有拿下他!朕的厌蠢症都要犯了!"
萧景衡面前的女子沈清棠坐在地上，右手轻轻抚摸着怀中奄奄一息的程景川。
听到此话她猛的抬起头惊讶的说，："你，你也是重生者?"
萧景衡顿时被气消了。
"废物！你个大星星的！劳资陪你重生了九十九次。"
```

[[Video Generation Prompt]]

---

### 110. 游艇姿势与极致身材提示

**Author**: [LexiPrompt](https://x.com/Artist04048661)  **Date**: 2026-02-06  **Language**: en

> 生成一张女孩在游艇上摆姿势的照片，强调极致的沙漏身材，身穿淡紫色比基尼，背景是开阔的大海和明亮的天空，营造出奢华的夏日度假氛围。

![游艇姿势与极致身材提示](https://cms-assets.youmind.com/media/1770446110607_wx7z2g_HAgywqXXMAAqRfS.jpg)

```
A photo of a girl on a yacht, posing standing at the railing with her hand raised above her head, against a backdrop of open sea and bright sky with clouds. The girl has a natural natural appearance. She has an extreme hourglass figure: very large, naturally full breasts, an extremely narrow waist and wide hips. She is wearing a light {argument name="bikini color" default="lilac"} bikini with gold inserts, a translucent mesh cardigan and a chain at the waist. Her hair is long, wavy, brown, loose and caught in the wind. The atmosphere is sunny and nautical, with deep blue water all around and a feeling of a luxurious summer vacation.
```

[[Hourglass Figure Emphasis]]

---

### 111. 私人飞机上未经修饰的狗仔队风格肖像

**Author**: [Alice Glassier](https://x.com/aliceglassierai)  **Date**: 2026-02-06  **Language**: en

> 一个高度具体的提示，旨在生成一张超现实、原始、未经修饰的肖像，具有狗仔队美学。它着重捕捉私人飞机内一个坦率、叛逆的瞬间（竖中指），强调真实的皮肤纹理、刺眼的灯光和不完美的构图，以对抗典型的 AI 平滑处理。

![私人飞机上未经修饰的狗仔队风格肖像](https://cms-assets.youmind.com/media/1770446058641_hfvnfv_HAgvNWxXoAAgaEr.jpg)
![私人飞机上未经修饰的狗仔队风格肖像](https://cms-assets.youmind.com/media/1770446058770_6muc2x_HAgv2bYWgAA0oQo.jpg)
![私人飞机上未经修饰的狗仔队风格肖像](https://cms-assets.youmind.com/media/1770446058779_52c39u_HAgvN1aWIAAyksP.jpg)

```
"Ultra-realistic raw DSLR paparazzi-style cinematic portrait of a young woman from the reference image — shot inside a beige leather private jet cabin. Tight waist-up crop, very close camera distance, slightly high-angle perspective, as if captured quickly from the aisle in a candid moment.
The subject leans forward casually, torso angled slightly left, head tilted subtly right.Her expression is unapologetically playful and rebellious: a wide grin with tongue fully out, teeth exposed, cheeks raised, jaw relaxed and loose. Eyes locked directly into the lens through thin oval metal-frame glasses with lightly tinted lenses; eyes in razor-sharp focus while everything else falls off naturally.
Both hands lifted near the chest, elbows bent, palms inward, clearly flipping both middle fingers toward the camera in a spontaneous, unfiltered gesture. Hair appears natural and unstyled, without emphasis on length, color, or shape — no idealization or aesthetic exaggeration.
Skin is fully realistic and unretouched: natural tone variations, visible pores, fine lines, micro-imperfections, slight oil sheen, authentic highlights on the forehead and nose, organic shadow transitions — absolutely no smoothing, beauty filters, or artificial skin effects.
She wears a white graphic T-shirt, a black leather cross-body bag strap hanging naturally across the torso, a silver chain necklace, and a small hoop earring. Tattooed forearms are clearly visible with authentic ink texture, slight skin stretch, and real pigment absorption.
Lighting is harsh natural cabin light from camera-left mixed with ambient overhead lighting, creating slightly uneven exposure, mild blown highlights, gritty contrast, and natural shadowing under the cheekbones and jawline. Background shows blurred beige jet seats and indistinct figures, shallow depth of field with imperfect focus falloff and organic lens blur.
DSLR look, paparazzi candid energy, subtle grain, imperfect framing, real-world color cast, film-like RAW processing, HDR realism, non-AI aesthetic, natural proportions, documentary-style authenticity."
```

[[Candid Portrait]]

---

### 112. 复古科幻风格的生物发光蘑菇群

**Author**: [Heather Green](https://x.com/heathergreen)  **Date**: 2026-02-06  **Language**: en

> 一个为 Freepik AI 生成器设计的提示，采用定制的复古科幻风格，生成一张低角度、特写镜头，展现超现实、梦幻般环境中，在霓虹灯的绚丽照耀下发光的蘑菇。

![复古科幻风格的生物发光蘑菇群](https://cms-assets.youmind.com/media/1770446106639_xih2i6_HAgTh5WWEAAKHBT.jpg)

```
A low-angle, close-up shot features a cluster of bioluminescent mushrooms in a grassy field. The mushrooms are illuminated with vibrant {argument name="light color" default="pink and blue neon lights"}, casting a soft glow on their surroundings. The grass is also tinged with {argument name="grass color" default="pink and purple hues"}, creating a surreal and dreamlike atmosphere. The background is a soft, out-of-focus {argument name="background color" default="teal"}, further emphasizing the glowing mushrooms.
```

[[Low Angle Close-Up]]

---

### 113. 私密浴室镜子自拍

**Author**: [Ivy](https://x.com/ivytheai)  **Date**: 2026-02-06  **Language**: en

> 生成一张逼真的镜面自拍肖像的提示词，描绘一位身穿丝绸睡衣的女性，置身于舒适的浴室环境中，强调温暖的室内照明、妩媚的表情，以及大理石台面上护肤品等细致的前景元素。

![私密浴室镜子自拍](https://cms-assets.youmind.com/media/1770446049364_k9107p_HAgnBNNXgAAqCw0.jpg)

```
{
  "prompt": "Mirror selfie portrait in a bathroom, woman with voluminous messy dark brunette hair, sultry and relaxed expression, light blue eyes, natural makeup with glossy pink lips, wearing {argument name="clothing material" default="cream-colored silk or satin"} long-sleeve pajama set, holding a grey smartphone, marble countertop in foreground with various skincare bottles and cosmetic products, warm indoor lighting from a three-bulb vanity fixture above the mirror, reflection showing bathroom interior with dark wood cabinets and white towels, intimate and cozy nighttime atmosphere, realistic photography, 9:16",
  "negative_prompt": "outdoor, bright daylight, professional studio lighting, formal wear, heavy jewelry, bright colors, distorted hands, messy background clutter",
  "style": "lifestyle photography, mirror selfie aesthetic, warm indoor lighting, soft focus background",
  "aspect_ratio": "9:16",
  "camera": {
    "type": "smartphone mirror selfie",
    "angle": "front facing, eye level",
    "framing": "waist-up shot, medium shot"
  }
}
```

[[Warm Indoor Lighting]] [[Bathroom Mirror Selfie]]

---

### 114. 丰腴沙滩比基尼肖像

**Author**: [Elara Weiss](https://x.com/ElaraWeiss)  **Date**: 2026-02-06  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张逼真的、低角度、背面视角肖像，描绘一位身穿哑光黑色比基尼的丰腴女性，躺在原始热带海滩上，整体设计呈现旅行网红美学风格。

![丰腴沙滩比基尼肖像](https://cms-assets.youmind.com/media/1770446045976_ylug67_HAgkUPfWcAA5j3K.jpg)

```
{
  “ar”: “4:5”,
  “subject”: {
    “type”: “adult woman”,
    “age”: “early 20s”,
    “character_outline”: “voluptuous and curvy hourglass physique; specifically characterized by a slim waist contrasting with very wide hips, thick thighs, and prominent, round glutes; fair skin with a gentle tan”,
    “hair”: “platinum blonde, long loose beach waves, slightly tousled and textured by the sea air”,
    “expression”: “soft, alluring, relaxed confidence”,
    “gaze”: “looking back over the left shoulder directly into the camera lens”
  },
  “wardrobe”: {
    “bikini”: {
      “color”: “{argument name="bikini color" default="matte black"}”,
      “style”: “minimalist string bikini”,
      “top_detail”: “triangle cup top with thin spaghetti straps”,
      “bottom_detail”: “cheeky thong-cut bottom with side ties, sitting high on the hips to accentuate the waist-to-hip ratio”
    }
  },
“accessories”: {
    “body_details”: “fine white sand sticking to the forearms and thighs”
  },
  “pose_action”: {
    “shot_type”: “rear-angle perspective, lying on the sand”,
    “stance”: “lying on stomach/side, upper body pushed up by straight arms placed on the sand”,
    “hips_legs”: “hips rotated to show full curve, glutes emphasized by the arched back pose; legs extended back on the sand”,
    “torso”: “upper torso twisted towards the camera”
  },
  “scene”: {
    “location”: “luxury tropical beach resort (Maldives style)”,
    “foreground": “pristine white sand beach”,
    “background”: “crystal clear turquoise water, wooden overwater bungalows with thatched roofs on stilts in the middle distance, lush green palm trees on the shoreline”,
    “sky”: “softly clouded sky with bright diffused sunlight”
  },
“lighting”: {
    “type”: “natural soft daylight”,
    “look”: “bright and airy, even illumination without harsh shadows, enhancing the skin tone and water color”
  },
  “camera”: {
    “device_vibe”: “high-end digital photography”,
    “angle”: “low angle, shooting from near ground level to emphasize body proportions”,
    “focus”: “sharp subject focus with slight depth of field blurring the distant bungalows”,
    “style”: “travel influencer aesthetic, clean and vibrant”
  }
}
```

[[Low Angle Portrait]] [[Back View Portrait]]

---

### 115. Red Bull 商业网格拼贴画提示 (JSON)

**Author**: [Ivanna | AI Art & Prompts](https://x.com/ivanka_humeniuk)  **Date**: 2026-02-06  **Language**: en

> 一个复杂的 JSON 提示，旨在为高端商业广告（红牛）生成一个 3x3 网格拼贴画，详细描述了九个不同的概念、构图和焦点，强调了照片级真实感、Octane Render 风格和高对比度电影摄影。

![Red Bull 商业网格拼贴画提示 (JSON)](https://cms-assets.youmind.com/media/1770446110722_0gzqv1_HAgdUg5XkAAqU0B.jpg)

```
{
  "campaign_metadata": {
    "layout_command": "GRID 3x3 Collage",
    "title": "{argument name="campaign title" default="Red Bull: Raw Kinetic Power"}",
    "aesthetic": "High-End Commercial / Action Minimalist"
  },
  "global_constraints": {
    "product_fidelity": "STRICT_100%_ACCURATE",
    "rendering": "Photorealistic, Octane Render, Ray-Tracing",
    "color_palette": ["#0000AA", "#FF0000", "#FFCC00", "#EAEAEA"]
  },
  "grid_execution": {
    "cell_1_1": {
      "concept": "THE POWER CORE",
      "composition": "Low_angle, centered",
      "focus": "The Red Bull can standing on a cracked dark obsidian floor, a powerful shockwave of white mist exploding outwards from the base."
    },
    "cell_1_2": {
      "concept": "MACRO TENSION",
      "composition": "Extreme_close_up_100mm",
      "focus": "Hyper-realistic condensation droplets on the cold aluminum skin, reflecting sharp blue studio lights, zero text on background."
    },
    "cell_1_3": {
      "concept": "THE IGNITION",
      "composition": "Macro_angle",
      "focus": "The silver pull-tab at the moment of cracking open, high-pressure CO2 vapor erupting like a jet engine exhaust."
    },
    "cell_2_1": {
      "concept": "THE ENERGY WING",
      "composition": "High_speed_freeze",
      "focus": "A splash of golden liquid frozen in mid-air, perfectly shaped like a sharp, aerodynamic wing against a pitch-black background."
    },
    "cell_2_2": {
      "concept": "THE RED BULL CLASH",
      "composition": "Symmetrical_art",
      "focus": "The two red bulls from the logo rendered as 3D crystalline energy sculptures colliding, emitting red sparks and light."
    },
    "cell_2_3": {
      "concept": "VELOCITY STREAKS",
      "composition": "Motion_blur",
      "focus": "Blue and silver light trails cutting through the dark, simulating the can moving at supersonic speed."
    },
    "cell_3_1": {
      "concept": "THE IMPACT",
      "composition": "Action_shot",
      "focus": "The can smashing through a thick sheet of glass, shards frozen in a radial explosion around the product."
    },
    "cell_3_2": {
      "concept": "THE FOCUS",
      "composition": "Minimalist_macro",
      "focus": "The yellow sun logo glowing with an internal heat, surrounded by frost-covered blue aluminum."
    },
    "cell_3_3": {
      "concept": "THE ASCENSION",
      "composition": "Wide_vertical",
      "focus": "The can launching upwards like a rocket, leaving a trail of ice crystals and blue electricity in a clean, empty space."
    }
  },
  "technical_settings": {
    "camera": "Hasselblad X2D",
    "lighting": "Hard Rim Lighting / High-Contrast Cinematography"
  }
}
```

[[3x3 Grid Layout]] [[Octane Render Style]]

---

### 116. 拉林：晚餐快好了

**Author**: [☆ 𝐛𝟑𝐥𝐥𝐚-𝐂𝐡𝐚𝐧 ♡](https://x.com/b3lla_callahan)  **Date**: 2026-02-06  **Language**: en

> Larin 给你拿来了食物。你还想要什么？
> 
> （顺便说一句，这是 Nano Banana Pro 做的。）

![拉林：晚餐快好了](https://cms-assets.youmind.com/media/1770532868442_fi987z_HAgdQmkWoAAystd.jpg)

```
Ya casi esta la comida~♡ 🤍🖤💙🍗 Pídeme que más quieres~♡ 🥧
```

[[Dinner Scene]]

---

### 117. 周六早晨活动提示的俯视图

**Author**: [前鏡](https://x.com/MaekagamiAi)  **Date**: 2026-02-06  **Language**: ja

> 一个简单的观察性提示，指示 AI 生成一张图片，展示周六早上 6 点某人正在做什么的俯视偷窥视角，旨在与 Nano Banana Pro 配合使用。

![周六早晨活动提示的俯视图](https://cms-assets.youmind.com/media/1770446089563_6k9t9w_HAfrf9xacAMMwzr.jpg)
![周六早晨活动提示的俯视图](https://cms-assets.youmind.com/media/1770446089638_chzkle_HAgGvb5bQAAOuPz.jpg)
![周六早晨活动提示的俯视图](https://cms-assets.youmind.com/media/1770446089624_da8luo_HAgHFaea8AAkPfm.jpg)
![周六早晨活动提示的俯视图](https://cms-assets.youmind.com/media/1770446090910_gsjwup_HAfrgD0aIAAguL1.jpg)

```
土曜のAM6時、何してるのか俯瞰視点で覗き見
```

[[Candid Lifestyle Photography]] [[Bird's Eye View]]

---

### 118. 《五十度灰》启发的电影感人像摄影

**Author**: [Alice Glassier](https://x.com/aliceglassierai)  **Date**: 2026-02-06  **Language**: en

> 一个高度具体的 JSON 提示，旨在重现《五十度灰》电影的氛围和美学，重点描绘一位身处豪华酒店套房办公室的女性，呈现出电影般超现实的肖像。它详细描述了灯光（温暖的金色台灯光）、着装（黑色西装外套、短裙、透明丝袜）和姿势（坐在办公桌边缘，眼神专注）。

![《五十度灰》启发的电影感人像摄影](https://cms-assets.youmind.com/media/1770446065961_n3vtp7_HAgNuFxXQAAPQ0v.jpg)
![《五十度灰》启发的电影感人像摄影](https://cms-assets.youmind.com/media/1770446066017_p3i48l_HAgNuFyWEAA5_FD.jpg)
![《五十度灰》启发的电影感人像摄影](https://cms-assets.youmind.com/media/1770446066159_asvh3l_HAgN3QiXkAA7rr1.jpg)

```
{
  "scene_description": {
    "location": "Luxurious modern hotel suite office area with wooden round desk, warm table lamp, beige curtains and neutral walls in background",
    "vibe": "Elegant, intense, sensual business sophistication – exact Anastasia Steele from Fifty Shades of Grey atmosphere",
    "lighting": "Warm golden table lamp light from right side, soft front fill, gentle rim light on hair and shoulders, realistic skin glow and subtle shadows on face and desk",
    "camera_settings": "Cinematic ultra-realistic portrait, 50mm prime lens equivalent, f/2.0–f/2.4, shallow depth of field, subtle natural film grain, highly detailed skin texture and fabric sheen, 4K–8K film scan quality, medium shot from slightly low angle, authentic dramatic romance color grading"
  },
  "primary_subjects": [
    {
      "character": "attached celebrity as Anastasia Steele",
      "role": "Confident and alluring professional woman",
      "action": "Seated on edge of round wooden desk, legs crossed at thighs, right hand resting on open book, left hand on desk surface, upper body slightly leaned forward, looking upward with calm yet intense direct gaze and parted lips",
      "details": "Long dark brown hair with soft waves and side part, dramatic dark eyeliner, defined brows, soft blush, glossy deep red lips, tailored {argument name="blazer color" default="black"} blazer worn open over deep black low-cut top, very short {argument name="skirt color" default="black"} skirt, sheer black stockings, small black high heels, delicate silver chain necklace with pendant, small stud earrings, red nail polish, realistic fabric texture and natural skin pores"
    }
  ],
  "environment_details": {
    "crowd": "None – solitary elegant focus",
    "architecture": "Beige curtains, neutral walls, warm lamp light source, open book and small red object on desk, softly blurred luxurious interior",
    "fidelity": "Ultra-photorealistic film still, exact seated pose, leg crossing, hand placement, upward gaze, black blazer + low-cut top + short skirt + sheer stockings combination, necklace and earrings, warm lamp lighting direction and shadow pattern from Fifty Shades of Grey reference, lifelike fabric drape, authentic skin and hair detail, no modern smoothing"
  }
}
```

[[Cinematic Mood]] [[Sheer Stockings]]

---

### 119. 最小布局压力测试构成

**Author**: [SRKDAN](https://x.com/SRKDAN)  **Date**: 2026-02-06  **Language**: en

> 一个旨在测试 AI 处理超极简主义构图能力的提示。它侧重于完美的对齐、大面积的留白和一个单一的抽象元素，仅使用中性色调和柔和的环境照明来营造一种刻意而自信的设计。

![最小布局压力测试构成](https://cms-assets.youmind.com/media/1770446104474_iill6q_G_dNyzyXUAAdnxD.jpg)

```
Ultra-minimal layout composition.
Single abstract element placed with intention,
large areas of negative space,
perfect alignment and proportion,
soft ambient lighting,
neutral tones only,
designed to feel deliberate and confident.
```

[[Neutral Color Palette]]

---

### 120. 电影级 2D 手绘动画赛璐珞胶片静帧提示词

**Author**: [🍥 Timmy 🍥](https://x.com/IXITimmyIXI)  **Date**: 2026-02-06  **Language**: en

> 此提示旨在生成模仿高端、柔和的 2D 手绘动画赛璐珞片的图像，并将其视为电影剧照。它指定了柔和的粉彩色调、用于区分形状的强烈定向照明、纸上的水彩/水粉纹理，以及线条抖动等细微瑕疵，从而营造出一种宁静、忧郁、高对比度的美学效果。

```
"Soft 2D hand-drawn animation cel look with a cinematic film-still treatment: top-down or carefully composed camera framing, small subject with generous negative space, muted pastel palette with restrained saturation, clear directional lighting (single key light) creating strong light-and-shadow shape separation, soft occlusion shadows, gentle atmospheric falloff, subtle vignette, watercolor-gouache fills on textured paper, visible grain and pigment bloom, slightly imperfect edges and minor line wobble, thin ink outlines with occasional line-weight variation, minimal detail but confident shapes, quiet moody tone, like a high-end TV animation background with cel characters. Cinematic exposure, deeper shadows, stronger value contrast, less pastel uniformity."
```

[[Pastel Color Palette]]

---

### 121. 奢华夜店中的电影感时尚大片

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-06  **Language**: en

> 一个高度详细、结构化的提示，专为生成逼真的电影级图像而设计，重点是一张高端时尚肖像，描绘了一位身穿红色缎面礼服的女性，置身于一个黑暗奢华的休息室场景中。该提示详细说明了用于制作海报静态画面的相机设置、灯光、色彩分级和构图。

![奢华夜店中的电影感时尚大片](https://cms-assets.youmind.com/media/1770446055285_ftdk76_HAf7kn3WkAEk4EW.jpg)
![奢华夜店中的电影感时尚大片](https://cms-assets.youmind.com/media/1770446055365_t63s5q_HAf7kn_WYAEtjjz.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_cinematic_luxury_nightclub_fashion_editorial_poster_still",
      "priority": "highest",
      "language": "en",
      "version": "v1.0_RED_SATIN_ONE_SHOULDER_LOUNGE_NO_TEXT"
    },

    "output": {
      "aspect_ratio": "2:3",
      "resolution": "ultra_high",
      "num_images": 4
    },

    "scene": {
      "concept": "A high-end fashion portrait in a dark luxury lounge. A glamorous woman sits on a leather armchair wearing a {argument name="dress color" default="red"} satin, one-shoulder gown. The ambience is warm, moody, and cinematic — golden ceiling murals, soft practical lights, and deep shadows. Editorial, seductive, refined.",
      "environment": "luxury lounge / cocktail bar interior, dark wood and black glass, leather armchair, warm amber practical lamps, ornate golden ceiling artwork, distant candle-like bokeh",
      "time_of_day": "night",
      "atmosphere": "smokeless but hazy cinematic diffusion, intimate upscale mood"
    },

    "subject": {
      "age_appearance": "adult",
      "expression": "confident, elegant, subtle flirtation, calm gaze",
      "pose": "seated sideways on a leather armchair, torso angled toward camera, one arm resting on chair arm, the other hand relaxed near lap, long legs draped with the gown",
      "hair": "long black hair, voluminous, side-swept waves over one shoulder",
      "wardrobe": "{argument name="dress color" default="red"} satin one-shoulder gown with structured bodice and glossy fabric highlights, floor-length drape",
      "makeup": "classic glam with red lipstick, defined eyeliner, natural skin texture",
      "jewelry": "minimal, understated (small earrings or none)"
    },

    "camera": {
      "camera_body": "ARRI Alexa 35",
      "lens": "50mm spherical",
      "aperture": "f/1.8",
      "focus": "tack sharp on eyes and lips, smooth falloff across dress and chair, background heavily softened",
      "framing": "vertical full-body to three-quarter portrait, subject centered slightly right, negative space in dark background",
      "look": "cinematic editorial realism, gentle diffusion, creamy bokeh"
    },

    "lighting": {
      "key_light": "soft key from camera-left (large diffused source), flattering cheekbone shaping",
      "rim_light": "warm subtle rim from behind to separate hair from background",
      "practicals": "warm amber lamps in background creating bokeh",
      "contrast": "high with controlled shadow detail",
      "highlights": "specular satin highlights on the gown, not blown out"
    },

    "color_grading": {
      "palette": "deep blacks, warm ambers, rich crimson red, natural warm skin tones",
      "film_emulation": "cinematic tungsten night interior",
      "grain": "fine film grain",
      "halation": "subtle bloom on practical lights and satin highlights"
    },

    "composition": {
      "visual_hierarchy": "eyes + red dress as primary; lounge ambience as secondary",
      "dep"
    }
  }
}
```

[[High-End Fashion Photography]]

---

### 122. 超逼真抓拍泳池浪漫场景 (JSON)

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-06  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超逼真的、抓拍式的浪漫场景电影剧照，描绘的是游泳后的情景。该提示指定了相机语言（35 毫米、手持、纪录片风格）、自然的正午光线、特定的服装、湿润的皮肤纹理，以及对阿克亚卡-格科瓦（Akyaka–Gökova）一个岩石海湾的详细环境描述。

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_candid_swim_romance",
      "version": "v1.0_AKYAKA_GOKOVA_MIDDAY_ROCK_EDGE_VIEW_EN",
      "priority": "highest"
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "ultra_photoreal_candid_film_still",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "color_grade": "midday_turquoise_true_to_life",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "global_rules": {
      "camera_language": "35mm lens equivalent, eye-level, handheld, candid documentary feel",
      "lighting_language": "motivated natural light only (midday sun), no flash",
      "authenticity_markers": "wet skin texture, salt water shine, no HDR, no AI glow"
    },
    "creative_prompt": {
      "scene_summary": "After swimming, they pause on the rock edge. Wet hair, bright sea behind. A tender closeness with the full Gökova view.",
      "subjects": {
        "count": 2,
        "description": "young man and woman early 20s, ordinary; faces visible and sharp",
        "expression": "soft calm smiles, quiet intimacy",
        "skin_and_face": "natural wet texture, no retouch"
      },
      "wardrobe_and_props": {
        "female": "simple swimsuit with a light cotton shirt loosely draped",
        "male": "simple swim shorts, plain cotton t-shirt half-wet",
        "props": "wrinkled towel nearby, no branding"
      },
      "micro_action": "one rests a hand on the other’s shoulder; they share a quiet look toward the sea",
      "environment_details": {
        "location": "rocky cove, Akyaka–Gökova",
        "background": "wide panoramic turquoise sea, pine hills, sun path on water; tiny distant fishing boat silhouette (not luxury)"
      },
      "lighting": "strong midday light; controlled highlights on water; deep but detailed shadows; subtle halation on sun glints",
      "composition": "vertical 9:16; couple foreground; dramatic sea backdrop; imperfect framing",
      "mood": "very romantic, serene, real"
    },
    "negative_prompt": [
      "studio lighting",
      "flash",
      "beauty retouch",
      "plastic skin",
      "HDR",
      "AI glow",
      "luxury marina",
      "beach club",
      "designer logos",
      "text",
      "logo",
      "watermark"
    ]
  }
}
```

[[Couple Photography]] [[Wet Skin Texture]]

---

### 123. 缎面吊带裙下的黄金时段肖像

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2026-02-06  **Language**: en

> 一个结构化的 2D 框提示，用于生成一张高分辨率、逼真的年轻女性肖像，她身穿香槟色缎面吊带裙，重点关注光线、姿势和构图，以达到杂志级图像质量。

![缎面吊带裙下的黄金时段肖像](https://cms-assets.youmind.com/media/1770446077543_y2ftbw_HAfxzWqacAgvhQ0.jpg)
![缎面吊带裙下的黄金时段肖像](https://cms-assets.youmind.com/media/1770446077663_5aec82_HAfxzYjacAAWPcE.jpg)

```
[
  {
    "box_2d": [
      {
        "subject": " young woman with  blonde hair wavy brunette hair and rosy cheeks",
        "pose": "Sitting with legs crossed, right hand raised touching hair near face, looking directly at the camera with a soft smile",
        "clothing": {
          "dress": "Champagne/light gold satin slip dress with a cowl neckline and spaghetti straps, mini length"
        },
        "accessories": {
          "earrings": "Small silver drop earrings with crystals",
          "necklace": "Delicate silver chain with a small pendant"
        },
        "makeup": "Glamorous natural look with prominent pink blush and berry-toned lipstick",
        "location": "Indoor setting, seated on a beige upholstered chair against a background of cream curtains and a dark window",
        "props": "None visible other than furniture"
      },
      {
        "photography_style": "4K HD Photo, Portrait",
        "lighting": "Soft, direct frontal lighting (possibly flash or ring light) creating highlights on the face and legs",
        "focus": "Sharp focus on the subject, particularly the face and dress texture",
        "composition": "Medium shot, seated, capturing the figure from the knees up",
        "quality": "High resolution, clear details, photorealistic"Ratio 3.4 Remove the lipstick and make up make her look natural Ratio 3.4
      }
    ]
  }
]
```

[[High Resolution Portrait]]

---

### 124. 深夜活动俯瞰图提示 (NanoBananaPro)

**Author**: [前鏡](https://x.com/MaekagamiAi)  **Date**: 2026-02-06  **Language**: ja

> 一个给 NanoBananaPro 的简单短提示，要求以俯视、偷窥的视角，描绘某人周末深夜在做什么。

![深夜活动俯瞰图提示 (NanoBananaPro)](https://cms-assets.youmind.com/media/1770446084988_di4r4r_HAfrf9xacAMMwzr.jpg)
![深夜活动俯瞰图提示 (NanoBananaPro)](https://cms-assets.youmind.com/media/1770446085037_cti6h9_HAfrgD0aIAAguL1.jpg)

```
週末の深夜2時、何してるのか俯瞰視点で覗き見
```

[[Candid Lifestyle Photography]] [[Bird's Eye View]]

---

### 125. 逼真的水晶标志生成

**Author**: [KiriKev](https://x.com/0xKiriKev)  **Date**: 2026-02-06  **Language**: en

> 一个用于生成自然晶体结构照片级真实感的提示，专门设计用于精确匹配参考图像的形状，强调棱镜般的光线折射和空灵的炼金术美学。

![逼真的水晶标志生成](https://cms-assets.youmind.com/media/1770446040278_c11vcu_HAfdkb8WIAAneBx.jpg)
![逼真的水晶标志生成](https://cms-assets.youmind.com/media/1770446040343_vcchno_HAfbZhqXAAAQyzM.jpg)
![逼真的水晶标志生成](https://cms-assets.youmind.com/media/1770446042027_u2z3wo_HAfdZN6XwAAG3sH.jpg)
![逼真的水晶标志生成](https://cms-assets.youmind.com/media/1770446042286_3wfsr0_HAfoCawX0AAMsLW.jpg)

```
Photorealistic natural crystal formation emerging from the ground [in a dark cave] mid-growth in the exact same shape as {argument name="referenced image" default="[REFERENCED IMAGE]"}, geometric facets emerging and expanding slightly outward adhering to the referenced image, prismatic light refractions casting {argument name="color palette" default="[COLOR PALETTE FROM IMAGE]"} and [COMPLEMENTARY COLORS] across surfaces, magical crystallization in progress, fantasy meets natural phenomenon, ethereal glow emanating from crystal core, alchemical aesthetic, translucent mineral structure, sharp angular geometry.
```

[[Crystal Logo Generation]]

---

### 126. 黑色侦探高级时尚肖像

**Author**: [WasifAI](https://x.com/doctorwasif)  **Date**: 2026-02-06  **Language**: en

> 一个详细的提示，用于生成一张超现实、时尚感十足的男性模特工作室肖像照。模特眼神疲惫而诱惑，造型为 20 世纪 40 年代黑色电影侦探风格，重点突出特定的服装、配饰、电影级布光和暖色调。

![黑色侦探高级时尚肖像](https://cms-assets.youmind.com/media/1770446042578_0in5tg_HAfkKs9acAQl_4t.jpg)

```
Ultra-realistic high-fashion studio portrait of a confident seductive male model ({argument name="age range" default="25–30"}), olive skin, lean athletic build, waist-up, centered, eye-level shot on an 85mm portrait lens.
Sharp oval face, deep-set almond eyes with a tired seductive gaze, thick natural brows, straight nose, slightly parted lips, light stubble beard and moustache. Jet-black slicked-back hair with natural volume.
Wearing a tailored charcoal-grey three-piece pinstripe suit, white spread-collar shirt, deep burgundy tie with gold tie bar, white pocket square, luxury metal watch. Silver ring on index finger.
Left hand in trouser pocket, right hand raised near lips holding a toothpick, relaxed yet dominant posture. Black ink neck tattoo visible, subtle finger tattoos.
Professional cinematic studio lighting: soft frontal key light, subtle fill, gentle rim light. Deep burgundy gradient background, smooth matte texture.
Warm cinematic color grading, shallow depth of field,  extreme realism, luxury fashion editorial,
```

[[Studio Fashion Photography]]

---

### 127. 超逼真偷拍旅行浪漫场景：爱琴海石街

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-06  **Language**: en

> 这是一个为 NanoBanana Pro 工具设计的高度详细的 JSON 提示，旨在生成一张超逼真、抓拍式的电影剧照，捕捉爱琴海狭窄石街上的浪漫瞬间。该提示详细说明了相机设置（35mm 镜头，手持）、光线（自然阴影/轮廓光）、主体细节（年轻，真实质感，特定服装）以及一个微妙的微动作（整理衣领），以捕捉宁静的温柔。

![超逼真偷拍旅行浪漫场景：爱琴海石街](https://cms-assets.youmind.com/media/1770446082716_lvjgtg_HAffV6cWAAAkwFN.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_candid_travel_romance",
      "version": "v1.0_AEGEAN_STONE_STREET_SHADE_WALK_EN",
      "priority": "highest"
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "ultra_photoreal_candid_film_still",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "color_grade": "restrained_true_to_life",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "global_rules": {
      "camera_language": "35mm lens equivalent, eye-level, handheld, candid documentary feel",
      "lighting_language": "motivated natural light only (shade bounce + sun rim), no flash",
      "authenticity_markers": "real stone texture, chipped paint, imperfect framing, no glamour look"
    },
    "creative_prompt": {
      "scene_summary": "Narrow stone street in a small Aegean town, bougainvillea overhead. They walk slowly in afternoon shade. A tiny gesture becomes the scene.",
      "subjects": {
        "count": 2,
        "description": "young man and woman early 20s, ordinary and real; faces visible and sharp",
        "expression": "calm smiles, comfortable silence",
        "skin_and_face": "natural texture, no retouch"
      },
      "wardrobe_and_props": {
        "female": "simple summer dress or light shirt, cotton texture, hair slightly frizzy from humidity",
        "male": "plain shirt/t-shirt, casual pants, slightly wrinkled",
        "props": "small backpack or tote, no logos"
      },
      "micro_action": "one adjusts the other’s collar or hair without thinking; they exchange a small look",
      "environment_details": {
        "location": "Aegean stone street",
        "background": "whitewashed walls with worn edges, stone steps, bougainvillea, a cat blurred near a doorway",
        "signage_rule": "no readable text/logos"
      },
      "lighting": "soft shade with gentle sun rim; controlled highlights; deep but detailed shadows",
      "composition": "eye-level medium shot, slightly tilted, imperfect framing like real street photography; faces sharp; background recedes naturally",
      "mood": "quiet tenderness, real time"
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
      "luxury fashion shoot",
      "text",
      "logo",
      "watermark"
    ]
  }
}
```

[[Candid Travel Romance]]

---

### 128. 黑蜘蛛女共生体角色扮演

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-02-06  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张年轻亚洲女性角色扮演者身穿光泽黑色共生体风格蜘蛛侠紧身衣的超写实图像，重点关注特定的解剖细节、俏皮的姿势和柔和的室内照明。

![黑蜘蛛女共生体角色扮演](https://cms-assets.youmind.com/media/1770446040676_m1n1bg_HAfWkfWXQAAxBoW.jpg)

```
{
"subject": {
"description": "Young Asian female cosplay subject wearing a tight, black, glossy Spiderman-style bodysuit (Symbiote design).",
"hair": "Dark brown to black hair, styled in long twin-tails (pigtails) held high by her hands, with soft bangs framing the forehead.",
"costume_details": "Form-fitting black bodysuit featuring a white spider emblem stretched across the chest, grey hexagonal honeycomb patterns on the shoulders and arms, and faint grey muscle shading details on the torso.",
"anatomy": "Voluptuous figure with strictly preserved proportions. Bust volume is significantly above average, appearing heavy and full, with distinct forward projection emphasized by the leaning posture. The chest depth is visibly greater than the ribcage depth. Waist is tapered, hips are curved. Soft tissue behaves naturally under the tension of the suit."
},
"pose": {
"type": "Standing, leaning forward, playful gesture.",
"arms": "Both arms are raised, elbows bent outwards, with hands gripping the base of the pigtails on either side of the head.",
"torso": "Upper body leans forward towards the camera, accentuating the chest volume and creating a foreshortened perspective of the torso.",
"legs": "Legs are close together, visible from the mid-thigh up, standing straight.",
"head": "Head is tilted slightly, face forward."
},
"environment": {
"setting": "Minimalist indoor corner.",
"background": "Plain beige or cream-colored walls meeting at a corner, with a neutral beige floor. A soft shadow is cast on the wall behind the subject.",
"props": "None visible besides the costume."
},
"camera": {
"shot_type": "Medium shot, captured from slightly above eye level (high angle).",
"perspective": "Foreshortened perspective due to the forward lean, emphasizing the upper body and face while diminishing the lower body relative size.",
"focal_length": "35mm to 50mm equivalent, keeping the subject in sharp focus with minimal distortion.",
"depth_of_field": "Deep enough to keep the face, hands, and torso in focus."
},
"lighting": {
"type": "Soft, diffuse indoor lighting.",
"direction": "Frontal and slightly overhead.",
"shadows": "Soft drop shadow behind the subject on the wall. Gentle shading under the chin and breasts defining volume. No harsh contrast.",
"highlights": "Subtle specular highlights on the glossy texture of the bodysuit, particularly on the chest and shoulders."
},
"mood_and_expression": {
"expression": "Playful and teasing. The subject is winking her right eye (viewer's left) while keeping the left eye open. Her tongue is sticking out slightly.",
"vibe": "Cute, energetic, anime-inspired, flirtatious.",
"gaze": "Direct eye contact with the camera lens."
},
"style_and_realism": {
"style": "High-fidelity cosplay photography.",
"realism": "Photorealistic skin texture and fabric physics. Not stylized as 3D render or illustration. Skin shows natural softness and tone.",
"render_style": "Sharp, clean, amateur"
```

[[Soft Indoor Lighting]] [[Playful Pose]]

---

### 129. 停车场里的坏女孩乳胶连体衣

**Author**: [Jessia](https://x.com/itsjessiababy)  **Date**: 2026-02-06  **Language**: en

> 一个高度具体的 JSON 提示，用于生成一张照片般逼真的图像：一位身材丰满的女性，身穿光泽、有质感的黑色乳胶连体衣和猫耳头带，在工业风的混凝土停车场中摆姿势，光线柔和而平坦。

![停车场里的坏女孩乳胶连体衣](https://cms-assets.youmind.com/media/1770446048922_yyn5ze_HAfWWx8XMAAUi5K.jpg)

```
{
  "type": "photograph",
  "aspect_ratio": "3:4",
  "subject": {
    "description": "Woman with long, wavy, dark reddish-auburn hair parted in the middle.",
    "face": {
      "makeup": "Heavy contouring, distinct winged eyeliner, filled arched eyebrows, overlined lips with brown liner and gloss.",
      "expression": "Confident, lips slightly parted, direct gaze, head tilted slightly to the right."
    },
    "physique": "Voluptuous hourglass figure, prominent bust volume, distinct waist-to-hip ratio.",
    "outfit": {
      "garment": "Black form-fitting jumpsuit with a textured, embossed animal-skin pattern (faux leather/latex). Front zipper pulled down to reveal cleavage.",
      "accessories": [
        "Black textured cat-ear headband matching the suit material.",
        "Black gloves with metallic silver claw tips attached to the fingers.",
        "Wide black belt with a rectangular plastic buckle.",
        "Small silver hoop earrings."
      ],
      "props": "Black braided riding whip held with both hands across the torso; right hand near shoulder, left hand near hip."
    }
  },
  "environment": {
    "location": "Concrete parking garage structure.",
    "elements": [
      "Thick grey concrete pillar directly behind the subject.",
      "Grey concrete ceiling with support beams.",
      "Background shows open garage levels with overexposed daylight coming from the rear right."
    ],
    "atmosphere": "Urban, industrial, utilitarian."
  },
  "lighting": {
    "source": "Natural daylight diffused through open garage structure.",
    "quality": "Soft, flat, non-directional.",
    "shadows": "Soft shadows under the chin and hair; lack of dramatic contrast.",
    "highlights": "Reflective sheen on the textured latex suit surfaces, particularly on the chest and thighs."
  },
  "camera": {
    "framing": "Medium shot, cropped at the upper thighs.",
    "angle": "Eye-level, slightly angled upwards.",
    "focus": "Sharp focus on subject, slight depth of field falloff in the background.",
    "style": "Amateur cosplay photography, incidental snapshot aesthetic."
  },
  "textures": {
    "skin": "Smooth makeup finish with visible contouring.",
    "clothing": "Shiny, embossed, rubbery texture with visible wrinkles and gathering at the waist and armpits.",
    "surfaces": "Rough, matte concrete vs. glossy synthetic fabric."
  }
}
```

[[Black Latex Bodysuit]]

---

### 130. 超风格化 3D 角色合成（设计师玩具美学）

**Author**: [Vaibhav Verma](https://x.com/Vaibhav_1_verma)  **Date**: 2026-02-06  **Language**: en

> 一个详细的 JSON 提示，用于 Nano Banana Pro 将上传的图像转换为超风格化的 3D 角色头部，采用受 Apple Memoji 和乙烯基收藏品启发的优质设计师玩具美学。它指定了材料（哑光聚合物皮肤、阳极氧化复合材料头发）和电影级光线追踪照明。

![超风格化 3D 角色合成（设计师玩具美学）](https://cms-assets.youmind.com/media/1770446107215_lt9kmq_HAfRSDva4AAMOeS.jpg)
![超风格化 3D 角色合成（设计师玩具美学）](https://cms-assets.youmind.com/media/1770446108567_5l0vti_HAfRSDqbgAAWxiJ.jpg)
![超风格化 3D 角色合成（设计师玩具美学）](https://cms-assets.youmind.com/media/1770446107066_ynqnep_HAfRSDuasAAZ5Ah.jpg)
![超风格化 3D 角色合成（设计师玩具美学）](https://cms-assets.youmind.com/media/1770446107201_4fjymq_HAfRSDna4AAGoBo.jpg)

```
[
  {
    "task": "hyper_stylized_3d_character_synthesis",
    "input": {
      "reference_image": "USER_UPLOADED_IMAGE",
      "style_match_strength": "ultra_high",
      "preserve_identity": "structural_only"
    },
    "output": {
      "type": "single_image",
      "aspect_ratio": "1:1",
      "resolution": "8k_uhd",
      "render_quality": "octane_render_visual_fidelity",
      "engine": "unreal_engine_5_lumen_lighting"
    },
    "style": {
      "character_type": "premium_designer_toy_aesthetic",
      "inspiration": [
        "apple_memoji_pro_iteration",
        "vinyl_collectible_art",
        "modern_minimalist_cgi"
      ],
      "proportions": {
        "head": "stylized_heroic_scale",
        "facial_features": "geometric_precision",
        "neck": "seamless_integration"
      }
    },
    "material_science": {
      "skin": {
        "material": "high_end_matte_polymer",
        "subsurface_scattering": "deep_tissue_warmth",
        "specular_roughness": 0.4
      },
      "hair_and_beard": {
        "material": "brushed_anodized_composite",
        "texture": "subtle_micro_grain",
        "sheen": "satin_finish"
      }
    },
    "lighting_and_optics": {
      "setup": "cinematic_rim_emphasis",
      "primary_light": "warm_key_light_45_degrees",
      "fill_light": "cool_ambient_occlusion",
      "rim_light": "neon_accent_trace_edges",
      "global_illumination": "ray_traced_bounces",
      "depth_of_field": {
        "focus": "sharp_on_eyes",
        "bokeh_intensity": "creamy_soft_blur"
      }
    },
    "background_reimagined": {
      "environment": "abstract_minimalist_studio",
      "base_color": "deep_charcoal_grey",
      "accent_lighting": "soft_radial_red_glow_behind_head",
      "texture": "fine_noise_grain_for_depth",
      "elements": "subtle_geometric_shadow_patterns"
    },
    "mood_and_vibe": {
      "atmosphere": "sophisticated_tech_entrepreneur",
      "emotion": "approachable_confidence",
      "color_palette": "monochromatic_with_vibrant_red_accents"
    }
  }
]
```

[[Ray Tracing Lighting]]

---

### 131. 超逼真电影级美食摄影信息图

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-02-06  **Language**: en

> 一个用于生成 8K 超逼真电影级美食照片的提示，适用于商业广告。它展示了一道传统的印尼菜肴，其主要食材以干净、信息图风格的垂直布局漂浮在菜肴上方，并由极简主义的指示线连接。图像强调超详细的食物表面、光泽的酱汁以及凝固在运动中的高速飞溅效果。

![超逼真电影级美食摄影信息图](https://cms-assets.youmind.com/media/1770446102195_f3g0ud_HAfLCD1asAAjc55.jpg)
![超逼真电影级美食摄影信息图](https://cms-assets.youmind.com/media/1770446102264_3bvbkb_HAfLCEDa8AASdDr.jpg)

```
Ultra-realistic cinematic food photography of a traditional Indonesian dish, presented as a floating ingredients infographic. The finished dish sits at the bottom in a ceramic bowl on a wooden surface. Above it, key ingredients float in mid-air in a clean vertical layout, each clearly separated and visually balanced. Thin minimalist pointer lines connect ingredients to elegant readable labels. Natural textures, hyper-detailed food surfaces, glossy sauces, steam rising gently, high-speed splash effects frozen in motion. Soft studio lighting mixed with natural daylight, shallow depth of field, premium editorial food poster style, commercial advertising quality, ultra-sharp focus, 8K resolution, realistic shadows, clean background.
```

[[Floating Ingredient Layout]]

---

### 132. 抓拍街头人像，带动态模糊效果

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-02-06  **Language**: en

> 一个用于生成电影级、超现实街头肖像的提示，使用慢速快门效果在清晰聚焦的主体周围营造人群运动模糊，从而实现狗仔队式的纪实真实感。

![抓拍街头人像，带动态模糊效果](https://cms-assets.youmind.com/media/1770446048015_z40eqp_HAfCVQobIAAeGIq.jpg)
![抓拍街头人像，带动态模糊效果](https://cms-assets.youmind.com/media/1770446048043_pow2pk_HAfCVQdaIAElTHc.jpg)

```
candid street portrait, subject centered sharp, crowd motion blur around, slow shutter speed, paparazzi street style vibe, handheld camera, windblown hair across face, natural makeup, {argument name="jacket color" default="olive green"} jacket, shallow depth of field, soft overcast daylight, cinematic color grading, teal and warm tones, film grain, bokeh city lights, documentary realism, busy street background, intense gaze, frozen moment in chaos
```

[[Slow Shutter Effect]]

---

### 133. 3x3 模型卡片网格

**Author**: [Keskin](https://x.com/craftian_keskin)  **Date**: 2026-02-06  **Language**: en

> 一个复杂的 JSON 提示，旨在生成同一位泳装模特在九种标准姿势/角度下的逼真 3x3 平铺网格（样片），强调一致性、中性影棚照明和目录般的审美，同时严格避免色情内容。

![3x3 模型卡片网格](https://cms-assets.youmind.com/media/1770446044147_mh7nlj_HAfBOWzagAAu-vw.png)
![3x3 模型卡片网格](https://cms-assets.youmind.com/media/1770446044491_pqrjx1_HAfBQewaUAAgb29.jpg)

```
{
  "Objective": "Create a clean, studio-style composite image (3x3 grid) showing the same swimsuit model in multiple standard poses/angles against a plain white backdrop, matching the reference layout and lighting.",
  "Reference_Image": {
    "file_path": "/mnt/data/9ef77768-1de8-46d2-8581-9fdede334950.png",
    "key_elements_detected": [
      "3x3 tiled grid (nine panels) with thin white borders",
      "Same adult female model repeated across panels",
      "White bikini (triangle top, high-cut bottoms)",
      "Neutral white/cream seamless background",
      "Even soft studio lighting with minimal shadows",
      "Standard pose set: front, 3/4, side, back variations",
      "Hair pulled back into a tight bun",
      "Centered full-body framing in each tile, consistent camera height"
    ],
    "composition_notes": {
      "layout": "Symmetrical contact-sheet / model comp-card style grid",
      "camera": "Mid-distance full-body, straight-on and rotated angles",
      "aesthetic": "Minimal, clinical, catalog-like presentation"
    }
  },
  "Persona_Details": {
    "role": "Fashion/editorial prompt engineer",
    "style_focus": [
      "photorealistic studio",
      "catalog comp sheet",
      "consistent framing across tiles",
      "neutral background"
    ],
    "avoid": [
      "explicit nudity",
      "sexualized posing",
      "lingerie glamorization",
      "brand logos",
      "text or watermarks"
    ]
  },
  "Prompt_Template": {
    "Main_Prompt": "Photorealistic studio contact sheet, 3x3 grid of the same adult female model wearing a plain white bikini (triangle top, high-cut bottoms), hair in a sleek bun, neutral expression, standing in standard modeling angles across the nine tiles (front, 3/4, side, back variations). Clean white seamless background, soft even studio lighting, minimal shadows, consistent camera height and distance, full-body framing centered in each tile, crisp high-resolution editorial catalog look, thin white borders separating each panel.",
    "Negative_Prompt": "nudity, nipples, explicit content, erotic posing, lingerie boudoir style, pornographic, bedroom, cluttered background, heavy shadows, dramatic cinematic lighting, low-res, blur, warped anatomy, extra limbs, duplicated faces, text, watermark, logo",
    "Optional_Variations": [
      "Same 3x3 grid but with slightly warmer white balance and a subtle film grain, still clean studio lighting",
      "Same layout but change bikini color to black, keeping everything else identical and minimal",
      "Same contact sheet but use a light gray seamless background instead of pure white for more separation"
    ]
  },
  "Suggested_Generation_Settings": {
    "aspect_ratio": "3:4  (to fit a 3x3 grid comfortably in a vertical frame)",
    "style": "photorealistic / studio catalog",
    "quality_notes": [
      "Keep poses neutral and non-sexualized",
      "Maintain consistent scale and alignment across "
    ]
  }
}
```

[[Model Card Grid]]

---

### 134. Y2K Frutiger Aero 玻璃棱镜科技产品拍摄

**Author**: [Lloyd Creates](https://x.com/lloydcreates)  **Date**: 2026-02-06  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张 8K 超现实产品图像，融合了 Y2K Frutiger Aero 美学与现代超现实主义。该提示侧重于动态玻璃折射、棱镜色差和虹彩镜头光晕，背景为双色调渐变。

![Y2K Frutiger Aero 玻璃棱镜科技产品拍摄](https://cms-assets.youmind.com/media/1770446102469_qzr0mg_HAc4xd7XEAA9cac.jpg)

```
{
  "image_generation_request": {
    "subject": "{argument name="product name" default="INSERT PRODUCT HERE"}",
    "environment": {
      "background": "A smooth, professional dual-tone gradient transition between #111B24 and #CAEFFF",
      "lighting": "High-contrast studio lighting with bright rim highlights to emphasize glossy textures"
    },
    "style_elements": {
      "aesthetic": "Y2K Frutiger Aero meets modern hyper-realism",
      "optical_effects": [
        "Dynamic glass refraction",
        "Prismatic chromatic aberration at the edges of transparent objects",
        "Iridescent lens flares",
        "Distorted glass overlays floating in the foreground"
      ],
      "composition": "Floating, gravity-defying arrangement with a wide-angle perspective",
      "textures": "Polished chrome, transparent acrylic, and high-gloss plastic"
    },
    "technical_specs": {
      "resolution": "8k UHD",
      "render_engine": "Octane Render style",
      "detailing": "Macro photography focus, hyper-detailed mechanical parts"
    }
  }
}
```

[[8K Product Photography]]

---

### 135. 用于建模的 T 姿势 3D 海盗角色

**Author**: [Chong-U](https://x.com/chongdashu)  **Date**: 2026-02-06  **Language**: en

> 一个旨在生成异想天开、卡通风格的 3D 海盗角色提示，该角色处于完美的 T 形姿势，适合 3D 建模资产。它强调了夸张的特征、黏土纹理、鲜艳的色彩、干净的赛璐珞着色，以及在纯白色背景上的明亮均匀照明。

![用于建模的 T 姿势 3D 海盗角色](https://cms-assets.youmind.com/media/1770446057381_xfn7m5_HAez7CFWcAAQOQJ.jpg)

```
A whimsical, cartoonish 3D pirate character designed for 3D modeling. The character is in a perfect T-pose with arms extended horizontally and feet slightly apart. The pirate has oversized stylized features, a large crooked hat, and a wooden peg leg. High-fidelity 3D render style with soft clay textures, vibrant colors, and clean cel-shading. The lighting is bright and even to show all details. Full body shot, centered, on a solid plain white background
```

[[Bright Color Palette]]

---

### 136. 时尚专题广告活动提示

**Author**: [AmirMušić](https://x.com/AmirMushich)  **Date**: 2026-02-06  **Language**: en

> 一个简单的智能提示，专为使用 Nano Banana 工具生成编辑时尚大片图像而设计。

![时尚专题广告活动提示](https://cms-assets.youmind.com/media/1770446099567_eigz77_HAezKFXW0AE6EVR.jpg)

```
Editorial fashion campaign
```

[[Editorial Fashion Photography]]

---

### 137. 15 秒竖屏家庭运动鞋视频脚本/提示 (NanoPhotoAI)

**Author**: [Nano Photo AI](https://x.com/NanoPhotoAI)  **Date**: 2026-02-06  **Language**: zh

> 一个详细的脚本或提示，用于使用 NanoPhotoAI（或类似的 AI 视频工具）生成一个 15 秒的竖屏视频（9:16），推广适合家庭穿着的舒适运动鞋。该提示指定了场景过渡、设置（公园、学校）、情绪（温暖、明快）和视觉元素（亲子款鞋、活动）。

```
时长：15 秒，竖屏 9:16，温馨轻快 BGM，明亮清新色调，高清
0-3 秒：{argument name="场景1" default="泰国公园草坪"}，家长带孩子散步慢跑，亲子同款运动鞋，阳光笑脸
3-6 秒：{argument name="场景2" default="校园操场"}，小朋友跑步、踢球，轻便儿童运动鞋，活泼可爱
6-9 秒：全家一起逛公园、骑单车，舒适运动鞋，轻松自在
9-12 秒：日常上学、出门逛街，亲子穿搭简约干净，鞋子舒适百搭
12-15...
```

[[Vertical Sneaker Video Script]]

---

### 138. 手写学习笔记生成

**Author**: [AI_InfoBite](https://x.com/AI_InfoBite)  **Date**: 2026-02-06  **Language**: en

> 一个文本到图像的提示，旨在根据提供的内容生成手写风格的学习笔记。它指定使用学生手写字体、横线纸背景，并添加视觉元素，如黄色高亮、用于日期的红色圆圈和解释性涂鸦。

![手写学习笔记生成](https://cms-assets.youmind.com/media/1770446074283_m9k4dl_HAespudbwAAU0_T.jpg)

```
"Based on this content, create handwritten-style study notes. Use student handwriting font, with lined paper as the background. Mark key terms with {argument name="highlight color" default="yellow"} highlighter, circle dates with {argument name="circle color" default="red"} circles. Add doodles to help explain concepts. Page size is A4"
```

[[Educational Visual]]

---

### 139. 护手霜的电影级产品特写

**Author**: [فاطمة المحمادي](https://x.com/fatoomdes)  **Date**: 2026-02-06  **Language**: en

> 一个用于生成极简主义白色管状护手霜电影级产品照片的提示。它指定产品漂浮在静止的水中，周围环绕着绿叶或黄瓜片等自然元素，强调干净的影棚灯光和高端商业美学。

![护手霜的电影级产品特写](https://cms-assets.youmind.com/media/1770446074215_prvu9z_HAegyxCWAAABVU7.jpg)

```
cinematic product shot, a minimalist white tube of "Qv" brand hand cream, floating in still water, a few {argument name="floating elements" default="green leaves, cucumber slices"} visible, clean studio lighting, high-end commercial aesthetic, advertising appeal, minimalist.
```

[[Minimalist Studio Lighting]]

---

### 140. 多生物群落微型星球（历史对比）

**Author**: [Gadgetify](https://x.com/Gdgtify)  **Date**: 2026-02-06  **Language**: en

> 一个复杂的多步骤指令提示，用于生成“多生物群系微型星球”的 360 度渲染图。它要求将一个宽泛的历史主题解构为扭曲球体上的三个不同区域（远古起源、文化鼎盛、未来地平线），并采用强烈的灯光分割（黄金时段与夜间霓虹光芒），以营造出高度的概念对比。

```
<instruction>   1.   Inference Engine:   Input A is a Broad Historical Theme, Region, or Fictional Universe (e.g., The History of the Middle East, Human Evolution, Earth vs. Alien, Western Civilization). Deconstruct the theme to generate   3 Distinct Biomes/Eras  :    Zone 1 (The Ancient Origin):  Identify the primitive or oldest architectural root.    (e.g., Middle East -> Pyramids, Sand, Cracked Earth, The Nile).     Zone 2 (The Cultural Zenith):  Identify the present day or traditional cultural peak.    (e.g., Middle East -> Mecca/The Kaaba, White Marble, Massive Crowds).     Zone 3 (The Futuristic Horizon):  Identify a speculative, sci-fi evolution.    (e.g., Middle East -> Cyberpunk Megacity, Dark Steel, Neon Radial Streets). 

 2. Container: Goal: "Multi-Biome Tiny Planet" 360 Photography. The Geometry: The world is warped into a perfect Sphere (Stereographic Projection) floating in the center of the frame. The Sky: The background atmosphere surrounds the sphere, but it must gradient shift to match the zones (e.g., Bright sunny sky on the top/left, fading into deep night/space on the bottom right). 

3. Topography (The Borders): The Partition: The surface of the sphere is divided into 3 distinct wedges or "slices" (like a pie chart). The Seams: The borders between the zones are sharply defined. They are separated by natural or structural barriers. (e.g., A winding turquoise river separates the desert from the modern city; a sharp ridge separates the modern city from the neon future). The Distortion: Buildings and monuments in all three zones point outwards from the center of the sphere, defying gravity. 

4. Visual : Zone 1 Texture: Organic, dry, matte (Sand, rock, ruins). Zone 2 Texture: Clean, populated, traditional (Marble, cloth, recognizable landmarks). Zone 3 Texture: Synthetic, dark, emissive (Black metal, glowing blue/red neon lines). 

5. Lighting & Atmosphere: Day vs. Night: The lighting must aggressively split across the planet. The Past/Present: Illuminated by a harsh, warm Golden Hour Sun coming from the top left, casting long shadows across the pyramids and marble. The Future: Plunged into Nighttime Darkness, illuminated entirely by its own internal, diegetic neon glow. 

Output: ONE image, 1:1 Aspect Ratio, Photorealistic 360 Render, "Time Capsule" aesthetic, High Conceptual Contrast. </instruction>
```

[[Conceptual Art]]

---

### 141. 复古黑白 RPG 规则书插画

**Author**: [Jarry | Visual Thinker ✏️](https://x.com/JarryR2D)  **Date**: 2026-02-06  **Language**: zh

> 一个提示，用于生成一张插画，风格为 20 世纪 70 年代复古黑白 RPG 规则书。它着重于一个身着战斗服的角色研究，使用线条艺术和阴影线技术来呈现复杂、经典的 D&D 美学。

![复古黑白 RPG 规则书插画](https://cms-assets.youmind.com/media/1770446061745_2iqe8d_HAeWY69asAAomOW.jpg)

```
Vintage black and white RPG rulebook illustration style. Character study in combat attire, fantasy archetype art. Line art with hatching technique, 1970s D&D aesthetic, intricate detail.
```

[[Vintage RPG Rulebook Illustration]]

---

### 142. 怪物 RPG 游戏资产表

**Author**: [Jarry | Visual Thinker ✏️](https://x.com/JarryR2D)  **Date**: 2026-02-06  **Language**: zh

> 一个用于生成奇幻 RPG 结构化游戏资产表的提示。它要求一个网格布局，显示各种怪物，每个怪物都有独特的设计，按难度进行颜色编码，并列出物品掉落，所有这些都以高质量的游戏美术风格呈现。

![怪物 RPG 游戏资产表](https://cms-assets.youmind.com/media/1770446061545_geuebp_HAeVzaWbkAAycBC.jpg)

```
Make a game asset sheet for an RPG fantasy game with monsters, with different levels and item drops. Grid layout, each monster with unique design, color-coded by difficulty. High-quality game art style.
```

[[Fantasy Game Art]]

---

### 143. 在杂货店里进行趣味时尚大片拍摄

**Author**: [Elara Weiss](https://x.com/ElaraWeiss)  **Date**: 2026-02-06  **Language**: en

> 生成一张俏皮时尚大片的超写实编辑摄影提示。画面中，一位金发女子坐在超市农产品区的购物车里，穿着亮霓虹绿运动鞋和石灰绿露脐上衣，在明亮的超市灯光下，强调鲜艳的色彩和浅景深。

![在杂货店里进行趣味时尚大片拍摄](https://cms-assets.youmind.com/media/1770446057666_utmcd8_HAeUxMgWAAAgdDq.jpg)

```
{
  "prompt": "A playful fashion photoshoot inside a modern grocery store. A young blonde woman sits confidently inside a metal shopping cart in the produce aisle, surrounded by colorful fruits and vegetables. She wears a {argument name="top color" default="lime green"} strapless crop top, high-waisted denim shorts, white socks, and bright {argument name="shoe color" default="neon green"} sneakers. Her pose is flirty and relaxed, one leg bent and lifted, with a teasing expression. Bright supermarket lighting, vibrant colors, shallow depth of field, high-detail, editorial photography style, ultra-realistic, 4k quality.",
  "style": "photorealistic",
  "lighting": "bright indoor commercial lighting",
  "mood": "playful, confident, bold",
  "camera": "DSLR, wide aperture, sharp focus",
  "quality": "high resolution, ultra-detailed"
}
```

[[Shopping Cart Portrait]]

---

### 144. 电影历史浪漫片剧照

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-06  **Language**: en

> 一个高度结构化的提示，用于生成一张设定在奥斯曼帝国晚期的超逼真电影剧照。它描绘了一对情侣在暴风雨海岸边的一个戏剧性、情感化的瞬间，强调了时代准确性、具体的相机设置和详细的解剖学限制。

```
{
  "generation_request":{
    "meta_data":{
      "tool":"NanoBanana Pro",
      "task_type":"cinematic_historical_romance",
      "version":"ULTRA_08_NATURE_STORM_AND_DECISION"
    },

    "references":{
      "female":"UPLOAD_REF",
      "male":"UPLOAD_REF"
    },

    "output_settings":{
      "aspect_ratio":"4:5",
      "orientation":"portrait",
      "resolution_target":"ultra_high_res",
      "render_style":"ultra_photoreal_cinematic_film_still",
      "film_grain":"subtle_35mm",
      "dynamic_range":"natural_not_hdr",
      "color_grade":"cool_stormy_with_warm_skin"
    },

    "anatomy_and_realism":{
      "perfect_anatomy":true,
      "accurate_hands":true,
      "accurate_eyes":true,
      "natural_body_proportions":true,
      "no_extra_fingers":true,
      "no_missing_fingers":true,
      "no_face_warp":true,
      "no_warped_limbs":true
    },

    "global_constraints":{
      "no_nudity":true,
      "no_suggestive_content":true,
      "period_accuracy_priority":"MAX",
      "no_modern_objects":true,
      "no_text":true,
      "no_logos":true
    },

    "creative_prompt":{
      "scene_summary":"Late Ottoman era, a dramatic natural coastline near {argument name="location" default="Istanbul"} as a sudden storm approaches.",

      "foreground_story":"Strong wind moves through their clothing and hair. The man stands slightly in front of the woman, one arm protectively around her shoulders. She holds the front of his coat firmly with one hand, the other resting against his chest. They look directly into each other’s eyes, serious but calm—this is a moment of decision. No fear, only resolve and trust.",

      "background_story":"Dark clouds gather rapidly over the Bosphorus. Waves crash against the rocks below. A distant fishing boat struggles against the wind before turning back toward shore. Birds scatter across the sky. Nature shifts suddenly, demanding action.",

      "wardrobe":"Late Ottoman outdoor garments suitable for harsh weather—long coats and layered wool fabrics, fully modest, heavier textures, darker earth and deep navy tones. Clothing visibly moves with the wind.",

      "jewelry_hair_nails":{
        "female":{
          "hair":"partially covered or tightly pinned back, loose strands blowing in the wind",
          "nails":"short, natural, clean, no polish",
          "jewelry":"minimal or none, period-appropriate only"
        },
        "male":{
          "jewelry":"none"
        }
      },

      "camera":"85mm cinematic portrait lens, close-medium framing, faces and hands in sharp focus while storm softens the background",

      "lighting":"overcast storm light with soft directional highlights on faces, subtle contrast, no harsh shadows",

      "color_palette":"cool storm blues and grays contrasted with warm natural skin tones",

      "mood":"decision, unity, strength in love under pressure"
    },

    "negative_prompt":[
      "modern buildings",
      "modern boats",
      "motorboats",
      ""
    ]
  }
}
```

[[Couple Photography]]

---

### 145. 夏加尔风格的圣心大教堂画作

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-06  **Language**: ja

> 一个给 Nano Banana Pro (Gemini 3 Pro 图像) AI 的提示，用于生成一张以马克·夏加尔 (Marc Chagall) 艺术风格渲染的圣心大教堂 (Sacré-Cœur Basilica) 图像。

![夏加尔风格的圣心大教堂画作](https://cms-assets.youmind.com/media/1770446090143_6w5a3n_GCRihaybMAAN19f.jpg)
![夏加尔风格的圣心大教堂画作](https://cms-assets.youmind.com/media/1770446089962_jl1y48_HAeC_JSb0AErNV5.jpg)

```
サクレ・クール寺院を{argument name="画家" default="シャガール"}みたいな絵にして出して！
```

[[Artistic Style Transfer]]

---

### 146. Image-to-Image：将人物置于“肥皂乐园”

**Author**: [Girls in AI Art｜GiAA(ギア)](https://x.com/GirlsinAIArt)  **Date**: 2026-02-06  **Language**: ja

> 此提示用于使用 Nano Banana Pro 进行图像处理/图生图生成。它指示 AI 将第一张图片中的人物放置到第二张图片（“肥皂乐园”图片）提供的场景中，并使其坐下。这展示了 AI 组合来自多个输入元素的能力。

![Image-to-Image：将人物置于“肥皂乐园”](https://cms-assets.youmind.com/media/1770446092099_5v8ury_HAeCceJbYAAP6hy.jpg)
![Image-to-Image：将人物置于“肥皂乐园”](https://cms-assets.youmind.com/media/1770446091928_lu90t2_HAeCcYDaAAAk5cu.jpg)
![Image-to-Image：将人物置于“肥皂乐园”](https://cms-assets.youmind.com/media/1770446092055_x26p7e_HAeCceIboAAS_RE.jpg)
![Image-to-Image：将人物置于“肥皂乐园”](https://cms-assets.youmind.com/media/1770446093538_w72p4c_HAdQu67acAAVCMN.jpg)

```
"1枚目の人物が2枚目の画像内で座っている画像を生成してください"
```

[[Background Replacement]]

---

### 147. 图像风格迁移：将照片转换为毕加索的立体主义画作

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-06  **Language**: ja

> 这是一个针对 Nano Banana Pro (Gemini 3 Pro Image) 的风格迁移提示，指示 AI 将上传的图像（一幅以莫奈《睡莲》风格绘制的凡尔赛阿波罗喷泉画作）转换为毕加索《亚维农少女》（Les Demoiselles d'Avignon）的风格。

![图像风格迁移：将照片转换为毕加索的立体主义画作](https://cms-assets.youmind.com/media/1770446098198_3ztwvr_HAeB7PAagAASL-T.jpg)
![图像风格迁移：将照片转换为毕加索的立体主义画作](https://cms-assets.youmind.com/media/1770446098052_4m3wv0_HAeB7L-asAAixe2.jpg)
![图像风格迁移：将照片转换为毕加索的立体主义画作](https://cms-assets.youmind.com/media/1770446098124_hckrzr_HAeB7LHbkAAJfro.jpg)
![图像风格迁移：将照片转换为毕加索的立体主义画作](https://cms-assets.youmind.com/media/1770446099043_00p6lq_GCRihaybMAAN19f.jpg)

```
これ（ヴェルサイユ宮殿アポロンの泉モネの睡蓮風味の絵）をピカソのアヴィニヨンの女たちみたいな絵に変えて出して！
```

[[Artistic Style Transfer]] [[Image-to-Image Style Transfer]]

---

### 148. 图像风格迁移：将照片转换为修拉的点彩画风格

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-06  **Language**: ja

> 这是一个针对 Nano Banana Pro (Gemini 3 Pro Image) 的简单图像风格迁移提示，指示 AI 将上传的照片（特别是《勇者斗恶龙 X》中的照片）转换为修拉点彩画风格。

![图像风格迁移：将照片转换为修拉的点彩画风格](https://cms-assets.youmind.com/media/1770446096680_kj3i6i_GCbTyTTbQAAo8m-.jpg)
![图像风格迁移：将照片转换为修拉的点彩画风格](https://cms-assets.youmind.com/media/1770446096581_v77uyl_HAeAiISaEAAGHfw.jpg)
![图像风格迁移：将照片转换为修拉的点彩画风格](https://cms-assets.youmind.com/media/1770446096795_vbx8tz_HAeAiCmbsAAAdpj.jpg)

```
これ（ドラクエXの写真）を
スーラの点描画みたいな
絵に変えて出して！
```

[[Artistic Style Transfer]] [[Image-to-Image Style Transfer]]

---

### 149. 超现实水上市场电影感社论

**Author**: [timedoctor.eth](https://x.com/timedoctor_nft)  **Date**: 2026-02-06  **Language**: en

> 一个复杂、电影化的编辑提示，用于生成一个超现实场景：主角站在一艘贡多拉上，身处一个极其拥挤的运河市场，周围环绕着鲜艳的纹理和薄雾笼罩的哥特式尖顶。它指定了高端中画幅相机设置（哈苏 H6D）、柯达 Portra 胶片模拟，并强调了纹理和大气深度。

![超现实水上市场电影感社论](https://cms-assets.youmind.com/media/1770446066158_r1jwjy_HAd9ExwXoAAZUwK.jpg)
![超现实水上市场电影感社论](https://cms-assets.youmind.com/media/1770446066199_c73got_HAd9ExMXgAAEHmy.jpg)

```
{
  "vibe_title_en": "Floating Market Mirage",
  "master_prompt": "A medium-long shot of The Protagonist standing confidently on the bow of a weathered wooden gondola, drifting through a hyper-cluttered, surreal canal marketplace. The scene is a dense explosion of tactile details: wicker baskets overflowing with vibrant magenta bougainvillea and waxy citrus fruits, floating crates bobbing in the teal water, and antique brass lanterns swaying from overhead lines. The Protagonist wears a heavy, textured trench coat with a popped collar and a vintage silk scarf, captured in a moment of scanning the horizon. The background features looming, mist-shrouded gothic spires that stretch impossibly high, creating a dizzying vertical depth. Shot on a Hasselblad H6D-100c with a 50mm f/2.8 lens to compress the busy background while keeping the subject sharp. The lighting is soft, diffuse 'magic hour' daylight, enhancing the rich textures of wool, wood, and water. Applied Kodak Portra 400 film emulation for warm skin tones and fine, organic grain. No neon, no plastic feel; purely cinematic, production-design realism.",
  "meta": {
    "intent": "Cinematic Editorial",
    "priorities": "Texture, Density, Atmospheric Depth",
    "device_profile": "High-End Medium Format"
  },
  "frame": {
    "aspect": "9:16",
    "composition": "Medium-Long Shot (Knees Up), Central Framing",
    "layout": "Vertical symmetry with busy peripheral framing",
    "camera_angle": "Eye-level to slightly low angle",
    "tilt_roll_degrees": "0"
  },
  "subject": {
    "gender": "Male",
    "identity": "The Protagonist / The Traveler",
    "demographics": "Adult, ambiguously aged",
    "face": "Neutral, observant gaze, sharp focus on eyes",
    "hair": "Hidden or styled neatly under headwear",
    "body": "Standing posture, weight shifted slightly, hand on railing or coat pocket",
    "expression": "Contemplative, focused adventure",
    "pose": "Standing on a moving vessel, dynamic stability"
  },
  "wardrobe_accessories": {
    "garments": [
      {
        "item": "Trench Coat",
        "material": "Heavy wool or gabardine, weathered texture",
        "color": "{argument name="coat color" default="Beige / Camel"}",
        "fit": "Tailored but layered"
      },
      {
        "item": "Vest/Waistcoat",
        "material": "Tweed or textured fabric",
        "color": "Forest Green or Muted Teal",
        "fit": "Fitted"
      },
      {
        "item": "Dress Shirt",
        "material": "Crisp cotton",
        "color": "White / Off-white",
        "fit": "Standard"
      }
    ],
    "accessories": [
      {
        "item": "Fedora / Wide-brim Hat",
        "color": "Dark Grey or Charcoal",
        "material": "Felt",
        "brand_style": "Vintage Millinery"
      },
      {
        "item": "Bowtie or Scarf",
        "color": "Emerald Green",
        "material": "Silk",
        "brand_style": "Classic"
      },
      {
        "item": "Gloves",
        "color": "Dark Brown"
      }
    ]
  }
}
```

[[Kodak Portra Film Simulation]]

---

### 150. 场景描述生成四格漫画

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-06  **Language**: ja

> 一个针对 Nano Banana Pro (Gemini 3 Pro Image) 的两步提示序列，旨在创作一个四格漫画。第一个指令将一个特定场景（勇者斗恶龙 X 怪物区域的特殊招式）转换为四格漫画格式，第二个指令则为生成的画格添加对话气泡和对白。

![场景描述生成四格漫画](https://cms-assets.youmind.com/media/1770446097391_alby3c_HAd8fv1b0AAs9y7.jpg)
![场景描述生成四格漫画](https://cms-assets.youmind.com/media/1770446097399_17utr7_HAd8fuYacAASNSt.jpg)
![场景描述生成四格漫画](https://cms-assets.youmind.com/media/1770446097412_ia9rz3_HAd8fvGa0AEkmS9.jpg)
![场景描述生成四格漫画](https://cms-assets.youmind.com/media/1770446098453_m2pgq4_GCbTyTTbQAAo8m-.jpg)
![场景描述生成四格漫画](https://cms-assets.youmind.com/media/1770446098346_x4u9b7_HAd8fxMaMAA57SC.jpg)

```
これ（ドラクエXのスーパースター必殺技モンスターゾーン）を4コマ漫画にして！

次
吹き出しとセリフを付けて！
```

[[Sequential Art]]

---

### 151. 对比图提示词（通用 AI 图像生成）

**Author**: [MarioTan](https://x.com/TanShilong)  **Date**: 2026-02-06  **Language**: zh

> 一个旨在生成图像的提示，该图像将新完成的素描或绘画与它所描绘的真实场景或物体进行比较。它侧重于捕捉将艺术品放置在实际环境旁边的效果，适用于各种绘画风格，如钢笔画、水彩画或素描。

![对比图提示词（通用 AI 图像生成）](https://cms-assets.youmind.com/media/1770446083904_yvtec7_HAdxf8DagAAg5uj.jpg)
![对比图提示词（通用 AI 图像生成）](https://cms-assets.youmind.com/media/1770446083802_iscggr_HAdxf79boAE60Y6.jpg)
![对比图提示词（通用 AI 图像生成）](https://cms-assets.youmind.com/media/1770446083898_c9565s_HAdxf7-acAAYm-F.jpg)
![对比图提示词（通用 AI 图像生成）](https://cms-assets.youmind.com/media/1770446085138_wtbsjl_HAdxf7_aoAAyGVO.jpg)

```
如果你喜欢画画，就尝试把你喜欢的东西画下来，然后再一起拍个照吧
“{argument name="场景描述" default="刚刚画完速写，把画纸和实景放在一起拍摄，展示成品的效果。"}”
```

[[Art vs Reality Comparison]]

---

### 152. 现代正式猩红色双图像生成

**Author**: [Qaiser Tzq](https://x.com/TzqQaiser)  **Date**: 2026-02-06  **Language**: en

> 一份结构化的多部分提示，以乌尔都语/印地语（罗马化）书写，详细描述了一个人穿着现代正式“权力着装”的两张不同图像，其中包含鲜艳的猩红色服装、特定姿势（坐在地上、完全蹲下）、配饰以及影棚灯光/背景效果。

![现代正式猩红色双图像生成](https://cms-assets.youmind.com/media/1770446080838_gww7u1_HAdoIL8aQAAyrkD.jpg)
![现代正式猩红色双图像生成](https://cms-assets.youmind.com/media/1770446080936_38ne94_HAdoIJ1bsAEg6Vs.jpg)

```
[
  {
    "tasvir_ki_id": "20260206_134643",
    "fard_ki_tafseel": {
      "libas_ka_style": "Modern Formal / Power Dressing",
      "rang_ka_intekhab": "Vibrant Scarlet Red",
      "outerwear": "Oversized Red Blazer jisay kandhon par dhila chhoda gaya hai",
      "innerwear": "Criss-cross halter neck crop top",
      "bottomwear": "High-waisted wide-leg trousers",
      "accessories": {
        "earrings": "Silver-toned crystal drop earrings",
        "jewelry": "Statement ring on left hand",
        "footwear": "Pointed-toe nude pumps"
      },
      "makeup_aur_baal": {
        "hairstyle": "Soft updo jis mein samne se baal chehre par aa rahe hain",
        "makeup": "Smokey eyes aur neutral lip shade"
      }
    },
    "photography_aur_mahaul": {
      "pose": "Zameen par baith kar aik hath sar par rakha hua hai",
      "background": "Dual-tone gradient effect (Pinkish-red se Purple ki taraf)",
      "roshni": "Soft studio lighting jo chehre ke features ko highlight kar rahi hai"
    }
  },
  {
    "tasvir_ki_id": "20260206_134637",
    "fard_ki_tafseel": {
      "libas_ka_khusoosi_izafa": "Kamar par safaid rang ka lamba ribbon/belt bandha gaya hai",
      "outerwear": "Wohi surkh blazer pehna hua hai",
      "innerwear": "Matching red bustier top",
      "accessories": {
        "earrings": "Vohi lambay crystal earrings",
        "jewelry": "Badi siyah rang ki gemstone ring",
        "footwear": "High-heeled beige stilettoes"
      },
      "makeup_aur_baal": {
        "hairstyle": "High messy bun",
        "makeup": "Dewy skin finish ke saath bold eye makeup"
      }
    },
    "photography_aur_mahaul": {
      "pose": "Full squat (ukhru) pose, camera ki taraf dekhte hue",
      "background": "Split color background (Purple parda aur surkh farsh)",
      "zaviya": "Eye-level shot jo confidence zahir karta hai"
    }
  }
]
```

[[Urdu Hindi Prompt]]

---

### 153. 草莓天使低角度肖像

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-02-06  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张电影风格的特写肖像，画面中一位红发女性，身穿白色乳胶草莓图案服装，佩戴大型羽毛天使翅膀，背景是华丽的罗马建筑，带有蓝色彩色玻璃光线。

![草莓天使低角度肖像](https://cms-assets.youmind.com/media/1770446053777_obdh43_HAdn1SvXUAA6lge.jpg)
![草莓天使低角度肖像](https://cms-assets.youmind.com/media/1770446053683_lv554c_HAdn07qWQAATnBV.jpg)

```
{
  "project_configuration": {
    "title": "Strawberry Angel - Low Angle",
    "render_engine": "Photorealistic/Cinematic",
    "target_resolution": "8k",
    "aspect_ratio": "9:16"
  },
  "scene_graph": {
    "camera_configuration": {
      "perspective": {
        "angle": "Low-angle",
        "elevation": "Hip-level",
        "tilt": "Upward facing"
      },
      "optical_properties": {
        "focal_length": "50mm",
        "aperture": "f/1.8",
        "focus_point": "Eyes",
        "depth_of_field": "Shallow (Soft Bokeh)"
      }
    },
    "subject_definition": {
      "demographics": {
        "type": "Young Woman",
        "hair": {
          "color": "{argument name="hair color" default="Red"}",
          "style": "Long, wavy",
          "texture": "High fidelity"
        },
        "skin": {
          "tone": "Natural",
          "finish": "Soft glow"
        }
      },
      "attire": {
        "material": "Latex",
        "color": "White",
        "pattern": "Red strawberry print",
        "items": [
          "Crop top",
          "Shorts"
        ],
        "accessories": [
          "Deep V necklace"
        ]
      },
      "morphology": {
        "wings": {
          "size": "Large",
          "color": "White",
          "texture": "Feathered",
          "position": "Arcing dynamically behind shoulders"
        }
      },
      "performance": {
        "pose": "Leaning slightly into frame",
        "expression": "Playful, intimate",
        "action": "Touching hair (implied by previous context)"
      }
    },
    "environment_definition": {
      "architecture": "Ornate Roman style",
      "features": [
        "Tall windows",
        "Blue stained glass"
      ],
      "lighting_setup": {
        "ambient": "Blue hues from stained glass",
        "specular": "Highlights on lips and hair",
        "atmosphere": "Elegant, cinematic"
      }
    }
  },
  "generation_payload": {
    "positive_prompt": "Low angle shot, medium close-up, young woman with long red wavy hair, wearing white latex strawberry-patterned crop top and shorts, deep V necklace, large white feathered angel wings. She is leaning into the camera with a playful intimate smile. Background is blurred ornate Roman architecture with blue stained glass light. 50mm lens, f/1.8, bokeh, high contrast, 8k, masterpiece.",
    "negative_prompt": "distortion, bad anatomy, flat lighting, oversaturated, cartoon, illustration, cherry print, dark hair"
  }
}
```

[[Red Hair Portrait]]

---

### 154. 旧照片修复与放大

**Author**: [Gabrielle](https://x.com/gabrielle_likes)  **Date**: 2026-02-06  **Language**: en

> 一个专为图像修复和增强设计的提示，指示 Nano Banana Pro 将一张旧照片修复到专业的数码单反相机质量，媲美佳能 EOS R6 Mark II，同时保持自然的面部特征和清晰度。

![旧照片修复与放大](https://cms-assets.youmind.com/media/1770446044725_ctzbzc_HAdiwCPacAcszJ8.png)
![旧照片修复与放大](https://cms-assets.youmind.com/media/1770446044914_bx2nic_HAdiw0CaIAAwd6I.png)

```
Restore this old photo to professional DSLR-quality portrait, with improved color and detail,
using advanced upscaling comparable to {argument name="camera model" default="Canon EOS R6 Mark II"}.
Keep it natural, with accurate facial features and high clarity.
```

[[Old Photo Restoration]] [[DSLR Quality Enhancement]] [[Photo Upscaling]]

---

### 155. 2026 马年海报设计提示

**Author**: [李岳](https://x.com/liyue_ai)  **Date**: 2026-02-06  **Language**: zh

> 一份详细的中文提示，用于生成一张奢华活泼的 2026 马年宣传海报，适合用作红包封面。它指定了 957x1278 像素的尺寸、主导的金色配色方案、几何马匹设计以及特定的中英文文本位置和字体样式。

![2026 马年海报设计提示](https://cms-assets.youmind.com/media/1770446087657_wt0lhe_HAdVscgacAUMPJN.jpg)

```
这幅图像是一张引人注目的宣传海报，尺寸957×1278像素，设计奢华且充满活力，以金色色调为主，背景为深色，海报的中间是一匹经过精心设计的几何形状马匹从右侧往左侧向着镜头迎面奔来，由多面切割的黄金和类似水晶的表面构成，散发着光芒和能量，仿佛正向前疾驰，马的形态现代且抽象，由锐利、反光的多边形组成，能够反射光线，营造出动感和光辉感。在上方，醒目的海报金色汉字“{argument name="中文祝福语" default="2026 马到成功"}”(字体样式为：方正字迹-龙吟体)映入眼帘，上方还有较小的英文文字“{argument name="英文祝福语" default="新年快乐"}”，下方还有一片闪耀的金色波浪在马下方流淌，上面点缀着闪烁的颗粒和发光的球体，整体的美学风格传达出力量、创新和乐观精神，象征着新的一年取得成功和前进的动力。
```

[[Year of the Horse Poster Design]]

---

### 156. 12 格贴纸/表情符号网格生成提示

**Author**: [Jackywine](https://x.com/Jackywine)  **Date**: 2026-02-06  **Language**: zh

> 一个结构化的提示，用于生成一组 12 个 4:3 垂直格式的表情符号/贴纸图像，其中每个面板描绘一种不同的情绪或动作（例如，努力工作、躺平、加班），并带有相应的放大叠加文本。用户需要使用 {argument name="subject" default="protagonist"} 占位符来指定主要角色/主题。

![12 格贴纸/表情符号网格生成提示](https://cms-assets.youmind.com/media/1770446088199_arpphq_HAdPTyNacAMf0Rl.jpg)

```
基于提示词生成 4 张图，风格和原图保持一致，每张图 12 个格子，每个格子的提示词如下，图片比例：竖版 4:3：

1 充满干劲 冲鸭！ {argument name="subject" default="主角"}奔跑冲刺姿势，四肢张开有力，身后有速度线，表情坚定，画面上方大字"冲鸭！"

2 彻底躺平 躺平 {argument name="subject" default="主角"}四脚朝天躺着，眼睛画成横线，灵魂飘出身体，表情放空，画面上方大字"躺平"

3 收到确认 好嘞！ {argument name="subject" default="主角"}立正敬礼动作，表情认真严肃，身体挺直，画面上方大字"好嘞！"

4 偷懒摸鱼 摆了 {argument name="subject" default="主角"}瘫在沙发上，手里拿着零食，眼神放空，姿势慵懒，画面上方大字"摆了"

5 超级开心 耶！ {argument name="subject" default="主角"}双手握拳高举庆祝，嘴巴大张笑，周围有星星闪光，画面上方大字"耶！"

6 委屈可怜 呜呜 {argument name="subject" default="主角"}眼睛含泪水汪汪，嘴巴撇着，耳朵耷拉，表情委屈，画面上方大字"呜呜"

7 得意坏笑 嘿嘿 {argument name="subject" default="主角"}侧身歪头，眯眼坏笑，双手搓在一起，神态狡黠，画面上方大字"嘿嘿"

8 打工疲惫 加班 {argument name="subject" default="主角"}趴在电脑前，眼袋明显，旁边放着咖啡杯，表情疲惫，画面上方大字"加班"

9 吃瓜围观 吃瓜 {argument name="subject" default="主角"}双手抱着西瓜啃，眼睛睁大好奇盯着前方，画面上方大字"吃瓜"

10 一夜暴富 暴富！ {argument name="subject" default="主角"}戴墨镜和金链子，周围飘着钞票和金元宝，表情得意，画面上方大字"暴富！"

11 害羞脸红 嘻嘻 {argument name="subject" default="主角"}双手捂脸但指缝偷看，脸颊有腮红，表情害羞，画面上方大字"嘻嘻"

12 晚安睡觉 睡了 {argument name="subject" default="主角"}蜷缩成一团盖着小被子，闭眼安睡，旁边有"zzz"符号，画面上方大字"睡了"
```

[[Emoji Sticker Grid Generation]]

---

### 157. 模拟 35 毫米夜间人像摄影提示，带大众面包车

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-02-06  **Language**: en

> 一个结构化的 JSON 提示模板，用于生成一张真实的模拟 35 毫米夜间照片。它侧重于一个主体，在老旧的大众 Combi 面包车附近随意摆姿势，利用单个模拟闪光灯对主体进行清晰照明，背景是曝光不足的都市夜景，并指定粗糙的纸张纹理和划痕，以营造复古美感。

![模拟 35 毫米夜间人像摄影提示，带大众面包车](https://cms-assets.youmind.com/media/1770446110479_wa4vlq_HAaFr-rXcAA2XZG.jpg)
![模拟 35 毫米夜间人像摄影提示，带大众面包车](https://cms-assets.youmind.com/media/1770446110535_ybnm40_HAaFr-mXIAA29uF.jpg)

```
{
  "instruction": "[e.g., Edit uploaded photo without changing face]",
  "subject": {
    "description": "{argument name="subject description" default="Beautiful woman with black hair, wind effect"}",
    "makeup": "[e.g., Light natural, visible lashes, brown contacts]",
    "outfit": "[e.g., Satin pajama set]",
    "pose": "[e.g., Candid, leaning on board, confident calm expression]"
  },
  "background": {
    "vehicle": "{argument name="vehicle type" default="Old VW Combi van, dark sky blue, worn rusty, stickers on window"}",
    "environment": "[e.g., Urban night street, asphalt, distant buildings]",
    "standing_board": "[e.g., White board with custom text like 'Warga Gaji Warga']"
  },
  "lighting": {
    "time": "[e.g., Night]",
    "source": "[e.g., Single analog 35mm flash]",
    "effect": "[e.g., Sharp on subject, darker underexposed bg]"
  },
  "style_requirements": {
    "photo_texture": "[e.g., Rough paper grain, scratches]",
    "aesthetic": "[e.g., Authentic analog 35mm photography]"
  },
  "negative": ["digital clean", "bright bg", "face changes"]
}
```

[[Single Flash Lighting]]

---

### 158. 黄金时段海滩肖像（90 年代超模）

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-02-06  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张超现实的女性垂直肖像，她拥有 90 年代超模的蓬松发型，站在日落时的海滩上，强调强烈的黄金时段逆光、海洋上的高虚化效果和电影般的魅力。

![黄金时段海滩肖像（90 年代超模）](https://cms-assets.youmind.com/media/1770446054100_xh0c5w_HAdBX_sWYAA562U.jpg)
![黄金时段海滩肖像（90 年代超模）](https://cms-assets.youmind.com/media/1770446053983_ajt8rv_HAdBX8cWQAAU4Mc.jpg)

```
{
  "prompt_structure": {
    "subject": {
      "description": "Young woman with voluminous, layered brunette hair in a 90s supermodel blowout style",
      "facial_features": "Sultry expression, piercing light eyes, full lips, glowing tan skin, sharp jawline",
      "attire": "Black strapless tube top, low-rise denim, layered gold necklaces with a prominent cross pendant, small hoop earrings",
      "pose": "Standing waist-up, facing forward with a slight tilt, hair flowing over shoulders"
    },
    "environment": {
      "setting": "Golden hour beach scene at sunset",
      "background": "Shimmering ocean water with high bokeh effect, sun reflecting off waves, horizon line blurred by light"
    },
    "lighting_and_atmosphere": {
      "type": "Backlit by setting sun, warm golden glow, dreamlike haze",
      "effects": "Sun flares, halation, sparkling water highlights, ethereal warmth, soft diffusion"
    },
    "technical_specs": {
      "quality": "Ultra realistic, HDR, UHD, 8k resolution, highly detailed skin texture",
      "camera_style": "Portrait photography, 85mm lens, f/1.8 aperture for depth of field",
      "aspect_ratio": "9:16 (Vertical/Long)",
      "aesthetic": "Vintage glam, cinematic lighting, photorealistic masterpiece"
    }
  },
  "negative_prompt": [
    "blurry",
    "low quality",
    "distorted features",
    "bad anatomy",
    "oversaturated",
    "cartoon",
    "illustration",
    "grainy",
    "pixelated",
    "extra limbs",
    "dull lighting"
  ],
  "full_combined_prompt": "Ultra realistic 8k portrait of a beautiful young woman with long voluminous brunette blowout hair and a sultry gaze, wearing a tight {argument name="top color" default="black"} tube top and gold cross necklace, standing on a beach at sunset. The background is shimmering ocean water with intense golden hour backlighting creating a halo effect. Cinematic lighting, soft focus glamour, dreamy atmosphere, HDR quality, sharp facial details, vertical 9:16 aspect ratio."
}
```

[[Cinematic Glamour]]

---

### 159. 超逼真商业产品摄影提示（Gemini Nano 香蕉）

**Author**: [Minahil](https://x.com/Minahil42298354)  **Date**: 2026-02-06  **Language**: en

> 一个极其详细、结构化的 JSON 提示，用于使用 Gemini Nano Banana 生成超逼真的商业产品摄影。它指定了一个垂直分屏布局，包含两个模块：一个用于展示带有动态飞溅和漂浮元素的巧克力奶昔，另一个用于展示带有爆炸性飞溅和营造情绪氛围的金属雀巢咖啡罐。

![超逼真商业产品摄影提示（Gemini Nano 香蕉）](https://cms-assets.youmind.com/media/1770446085318_3cfbex_HAcrf_QXgAAAeiT.jpg)

```
{
  "master_prompt": {
    "global_settings": {
      "style": "Hyper-realistic commercial product photography", 
      "layout": "Vertical split-screen, two distinct modules",
      "resolution": "8K UHD, cinematic lighting",
      "details": "Extreme clarity, frozen motion splashes, micro-condensation"
    },
    "module_1_left": {
      "subject": {
        "type": "Clear tall glass of thick chocolate milkshake",
        "details": "Frothy texture, visible condensation on glass",
        "text_on_glass": ["CHOCOLATE MILK SHAKE", "mock up", "protein"]
      },
      "action": "Dynamic chocolate liquid splash erupting from the base and top",
      "floating_elements": [
        "Whole blueberries with water droplets",
        "Fresh green mint leaves",
        "Tiny chocolate particles suspended in air"
      ],
      "background": {
        "color": "Deep dark blue with soft golden bokeh particles",
        "lighting": "Cool moonlight-style rim lighting"
      }
    },
    "module_2_right": {
      "subject": {
        "type": "Slim gold metallic Nescafé can",
        "details": "Heavy condensation, matte gold finish",
        "text_on_can": ["NESCAFÉ", "CHOCOLATE SHAKE", "NEW LOOK", "PROTEIN BOOST"]
      },
      "action": "Explosive chocolate liquid crown splash at the base",
      "floating_elements": [
        "Roasted coffee beans",
        "Swirling thick white steam/smoke rising from the top",
        "Glowing amber embers and sparks"
      ],
      "background": {
        "color": "Warm chocolate brown to dark amber gradient",
        "atmosphere": "Moody, intense, and smoky"
      }
    },
    "surface_details": {
      "base": "Reflective dark wet surface with liquid pooling",
      "shadows": "Soft separated realistic shadows"
    }
  }
}
```

[[Commercial Beverage Photography]] [[8K Hyperrealistic Photography]] [[Dynamic Splash Effect]]

---

### 160. 大理石梳妆台上的高端室内肖像

**Author**: [D. Humann](https://x.com/dhumann)  **Date**: 2026-02-06  **Language**: en

> 一个高度详细的 JSON 格式提示，旨在生成一张情绪化、社论风格的女性肖像，描绘她坐在一张大理石梳妆台上。该提示为灯光（柔光箱扩散）、构图（85 毫米镜头，浅景深）、主体姿势和详细的服装规格（哑光黑色紧身胸衣，细条纹长裤）指定了复杂的参数，并要求提供参考照片以确保面部逼真度。

![大理石梳妆台上的高端室内肖像](https://cms-assets.youmind.com/media/1770446103133_lx4zsf_HAcjgWxacAMdbQA.jpg)

```
{
  "meta": {
    "optimization_target": "Nano Banana Pro",
    "prompt_safety_layer": "High",
    "fidelity_focus": "Textural and Compositional Accuracy"
  },
  "global_context": {
    "scene_type": "High-end interior portrait, bathroom vanity setting",
    "atmosphere": "Moody, editorial aesthetic",
    "lighting": {
      "setup": "Softbox-style frontal diffusion",
      "shadow_depth": "Soft-focus gradients on facial contours",
      "temperature": "5500K (Neutral Daylight)"
    }
  },
  "composition_engine": {
    "framing": "Vertical, waist-up composition",
    "depth_mapping": {
      "foreground": "Subject in sharp focus",
      "midground": "Polished white marble-texture countertop",
      "background": "Dark charcoal stucco wall and vertical subway tiles"
    },
    "camera_specs": "85mm lens equivalent, f/1.8 for shallow bokeh"
  },
  "primary_subject_parameters": {
    "structural_id": "subject_alpha_01",
    "pose_data": "Sitting on horizontal surface, leaning forward 15 degrees, right hand index finger touching lower lip",
    "subject_profile": {
      "identity_anchors": {
        "description": "Maintain the specific facial geometry, hair, and eye shape of the reference subject. High-fidelity facial reconstruction."
      }
    },
    "garment_specs": [
      {
        "item": "Bodice",
        "color": "Matte Black",
        "detail": "Sweetheart neckline with center-front ribbon tie",
        "material": "Stretch cotton or silk blend"
      },
      {
        "item": "Trousers",
        "color": "Cool Grey / White",
        "pattern": "0.5cm vertical pinstripe",
        "fit": "High-waisted, pleated fabric folds"
      }
    ]
  },
  "environment_data": {
    "surfaces": [
      {
        "type": "Countertop",
        "material": "Polished porcelain",
        "reflectivity": "0.4 gloss factor",
        "visuals": "Subtle reflection of pinstripe textile"
      },
      {
        "type": "Wall",
        "texture": "Heavy-grit plaster/stucco",
        "color": "#121212"
      }
    ],
    "props": [
      {
        "id": "item_01",
        "label": "Dispenser",
        "color": "Opaque White",
        "position": "Right quadrant, background"
      }
    ]
  },
  "semantic_relationships": [
    "Subject is anchored to the central horizontal plane",
    "Vertical stripes of trousers contrast with horizontal counter edge",
    "Dark background creates high-contrast silhouette for light hair"
  ]
}
```

[[Editorial Portrait Style]]

---

### 161. 空灵花田奇幻肖像的 JSON 提示词

**Author**: [💙星野 銀華 (Hoshino Ginka)🤍](https://x.com/Hoshino_Ginka)  **Date**: 2026-02-06  **Language**: en

> 一个复杂的 JSON 格式提示，专为 Nano Banana Pro 设计，用于生成一个角色在虚幻野花田中的奇幻肖像。它使用用户上传的图像作为直接参考来锁定角色的特征，同时根据详细的文本参数生成环境和风格。

![空灵花田奇幻肖像的 JSON 提示词](https://cms-assets.youmind.com/media/1770446091159_fmf7xg_HAcRZc7acAE5Fnx.jpg)
![空灵花田奇幻肖像的 JSON 提示词](https://cms-assets.youmind.com/media/1770446091168_2gqdi2_HAcjbE4akAEbrnL.jpg)
![空灵花田奇幻肖像的 JSON 提示词](https://cms-assets.youmind.com/media/1770446091175_o2uual_HAcjbE1a0AATQ_1.jpg)
![空灵花田奇幻肖像的 JSON 提示词](https://cms-assets.youmind.com/media/1770446092439_chhg98_HAcRZc_awAAKYlK.jpg)

```
{
  "workflow_mode": "ethereal_flower_field_direct_reference",
  "description": "Uses a user-uploaded character image directly as a visual reference (without pre-refining it) to generate a fantasy portrait in a wildflower field. The character features are locked from the upload, while the environment and styling are generated from text.",

  "input_slots": {
    "source_image_character": "USER_UPLOADED_CHARACTER_ONLY"
  },

  "generation_params": {
    "aspect_ratio": "{argument name="aspect ratio" default="3:4"}",
    "quality_tags": "best quality, masterpiece, 8k, photorealistic, fantasy photography, ethereal, dreamlike, soft focus, backlight, sun flare, wildflowers, nature core, organic fashion, messy hair, cinematic lighting",
    "negative_prompt": "urban, indoor, studio, dark, modern clothing, jeans, t-shirt, plastic, harsh contrast, heavy makeup, straight hair, neat hair, old age, wrinkles"
  },

  "hard_coded_scene_prompt": {
    "environment": "field of blooming wildflowers ({argument name="flowers" default="purple lupines, red poppies, daisies"}), blurred nature background, outdoor meadow, vibrant but soft natural colors",
    "lighting": "strong backlighting (sun behind subject), lens flare, rim light on hair, soft hazy atmosphere, golden hour or late afternoon sunlight",
    "composition": "medium shot (waist up), eye-level, subject centered amidst the flowers, depth of field with foreground flowers blurred"
  },

  "pipeline_sequence": {
    "_hint": "Sequence: 1. Read & Lock Character (Direct) -> 2. Generate Scene & Pose from Text.",

    "step_1_character_reference_lock": {
      "action": "controlnet_reference_only",
      "target": "source_image_character",
      "purpose": "Directly use the uploaded image to lock facial structure and identity without modifying the source pixels first.",
      "weight": 0.85,
      "style_fidelity": 1.0
    },

    "step_2_final_synthesis": {
      "action": "generate_image",
      "prompt_construction": {
        "scene_text": "[hard_coded_scene_prompt]",
        "character_logic": "Standing in a flower field. Looking directly at the camera with a soft, dreamlike expression. Hair is white/platinum blonde, messy, voluminous, and windswept, decorated with small twigs and wild flowers. Arms relaxed by the sides.",
        "clothing_text": "Fantasy nature-inspired corset top or dress. Made of beige/tan rough textured fabric (linen or burlap). Adorned with real growing wildflowers (blue, red, yellow) and vines attached to the bodice. Raw hems, organic look.",
        "quality_text": "[quality_tags]"
      },
      "denoising_strength": 1.0,
      "instruction": "Generate image using 'source_image_c"}
```

[[Wildflower Field Setting]]

---

### 162. 超逼真电影级时尚摄影转换提示

**Author**: [John](https://x.com/john87445528)  **Date**: 2026-02-06  **Language**: zh

> 这是一个详细的提示，用于将现有图像（如 MJ 卡通/漫画）使用 Nano Banana 转换为超现实、电影级的时尚摄影作品。它指定了深景深（f/8–f/11）、柯达 Vision3 500T 电影胶片、戏剧性的冷暖光对比，以及大量的负面提示，以确保获得非卡通、高保真、高分辨率的结果。

![超逼真电影级时尚摄影转换提示](https://cms-assets.youmind.com/media/1770446083149_gmqbng_HAcfgE3XAAA6c1k.jpg)
![超逼真电影级时尚摄影转换提示](https://cms-assets.youmind.com/media/1770446083237_0ej3wo_HAcfhlCWgAEcDSb.jpg)

```
将参考中的漫画角色转化为超写实真人形象，严格保留角色的发型、服装、表情、五官特征与整体气质。
画面采用深景深呈现，让模特与背景都保持极致清晰，营造出沉浸式、电影级的高端摄影效果。
风格要求：电影级超写实时尚摄影风格

高分辨率，电影胶片般锐利细节
光线为暖色工作灯与冷色暮光的强烈戏剧化对比
模特为主体，同时展现丰富的环境背景

技术规格：
胶片：{argument name="胶片" default="Kodak Vision3 500T"}

适用于：电影摄影、夜景与低光场景、室内钨丝灯环境
色彩：温暖饱满的电影色调
颗粒：细腻的胶片颗粒质感
宽容度：出色的暗部细节表现

镜头设置：

光圈：{argument name="光圈" default="f/8–f/11"}（保持深景深，全画面清晰）
分辨率：4K 或更高
景深：深景深，前景与背景均清晰

反向提示词（避免出现）：

模糊背景、浅景深、散景
失焦、面部变形
卡通、动漫、CG人物、插画风、绘画质感
低质量、噪点、像素化
过曝的强烈日光
```

[[Warm Cool Light Contrast]]

---

### 163. 根据参考图像生成皮克斯风格的 3D 贴纸包

**Author**: [ケンイチ | AIスキルアカデミー『誰でもわかるAI活用術』](https://x.com/ChatgptAIskill)  **Date**: 2026-02-06  **Language**: en

> 这是一个全面的提示，提供英文和日文版本，旨在根据上传的参考图片，生成一个包含 20 多种不同贴纸风格的女性角色插画拼贴画。该提示指定了 3D 皮克斯/迪士尼艺术风格、柔和的电影照明、柔和的色彩以及详细的角色特征（微卷的黑色头发、米色开衫）。它要求展现各种表情和反应，所有这些都排列在一个带有白色边框和柔和阴影的单一高分辨率拼贴画中，非常适合为社交媒体创建贴纸包。

![根据参考图像生成皮克斯风格的 3D 贴纸包](https://cms-assets.youmind.com/media/1770446095719_4t37i1_HAcSe7yacAIZJRS.jpg)
![根据参考图像生成皮克斯风格的 3D 贴纸包](https://cms-assets.youmind.com/media/1770446095878_ccwv1i_HAcSe76aIAIRpP4.jpg)

```
Please use the attached reference image as the base character.
Create a single high-resolution collage containing at least 20 cute sticker-style illustrations of the same female character. Ensure the face, skin tone, hairstyle, and overall appearance perfectly match the reference image.
Art Style: {argument name="art style" default="3D Pixar-style / Disney-style cartoon"}, soft cinematic lighting, smooth pastel colors, large expressive eyes, rounded cute facial proportions, ultra-detailed 3D rendering.
Character Details:
– Lightly permed black hair
– Large expressive eyes
– Beige cardigan
– Cute, slightly chubby proportions
Expressions and Reactions (all distinct):
Happy smile, surprised, shocked, shy smile, angry, confused, crying, sleepy, winking, peace sign, blowing a kiss, holding a cell phone, thinking, covering face, holding coffee, covering mouth while laughing, annoyed, excited, affectionate expression, cute neutral pose (over 20 total).
Sticker Design:
– Each reaction as a separate sticker
– Clean white border on all stickers
– Soft drop shadow
– No text, no watermark
Layout:
– All stickers neatly arranged in one collage
– Balanced grid layout
– Soft beige/pastel-toned background
– Instagram/WhatsApp-style sticker pack design
Quality:
Ultra-high definition, high resolution, smooth 3D finish, professional-grade sticker pack style, lovingly expressive.
```

[[Soft Cinematic Lighting]]

---

### 164. 人像摄影的 9 宫格布局，附带详细的 JSON 提示

**Author**: [クロガネ@即覚醒させる人](https://x.com/mak0chipdf)  **Date**: 2026-02-06  **Language**: ja

> 这是一个高度详细、结构化的 JSON 提示，专为 Nano Banana Pro 设计，用于根据上传的照片生成一个 3x3 网格，其中包含同一主体面部的 9 种不同角度和表情。它详细说明了从主体的外貌和服装，到物体、环境（工业风格咖啡馆）、灯光和构图（中景、高角度、散景）的每一个细节。其目的是在特定场景中快速生成单个主体的多个高质量变体。

![人像摄影的 9 宫格布局，附带详细的 JSON 提示](https://cms-assets.youmind.com/media/1770446093023_yvc51x_HAcPhMYacAModLx.jpg)
![人像摄影的 9 宫格布局，附带详细的 JSON 提示](https://cms-assets.youmind.com/media/1770446093556_aosf1m_HAcPoVFacAYBV4G.jpg)

```
人物の顔のみに使用して下記のプロンプトへ適用させてください
実際のモデル撮影のように表情と髪型を変えながら9種類の異なるアングルで3×3のグリッドレイアウトで配置。各画像の左上に通し番号を1から順に表示して
{

  "subject": {

    "description": "{argument name="subject description" default="Young Asian man, early 20s, with dark, straight, slightly disheveled hair and bangs covering his forehead."}",

    "pose": "{argument name="pose" default="Sitting relaxed on a chair at a window counter, body slightly turned, looking down at a smartphone held in both hands."}",

    "expression": "Calm, neutral, slightly pensive, gaze directed downwards at the phone screen."

  },

  "attire": {

    "outerwear": "White ribbed knit zip-up polo sweater with a collar, partially unzipped, showing the inner shirt. The knit texture is visible.",

    "innerwear": "White crew-neck t-shirt.",

    "bottoms": "Grey tailored trousers, slightly loose fit, with some natural wrinkles.",

    "accessories": "Silver rectangular-faced metal analog wristwatch on the left wrist."

  },

  "objects": {

    "smartphone": "Held in both hands, dark case, screen illuminated showing an app interface (possibly a map or social media).",

    "cup": "White paper takeaway coffee cup with a black lid and a black straw, held loosely in the right hand near the phone.",

    "headphones": "White wireless earbuds sitting inside their open white charging case, placed on the grey windowsill counter to the right of the subject.",

    "furniture": "Grey concrete windowsill counter. In the background, there are wooden chairs with metal frames and round wooden tables."

  },

  "environment": {

    "location": "Industrial-style cafe interior.",

    "walls_ceiling": "Exposed concrete walls and ceiling with visible pipes, ducts, and wiring.",

    "decor": "Hanging green rope-like macrame plants from the ceiling. Exposed Edison-style filament bulbs hanging from cords. String lights are also visible and lit.",

    "window": "Large window on the right side, letting in soft natural daylight. The window frame is painted white.",

    "background_people": "Several other patrons are blurred in the background: one person walking on the left, one sitting at a table, and another standing nearby wearing a face mask.",

    "lighting": "Soft, natural daylight from the window mixed with warm ambient light from the hanging bulbs and string lights."

  },

  "composition": {

    "shot_type": "Medium shot, capturing the subject from the mid-thigh up.",

    "angle": "Slightly high angle, looking slightly down at the subject.",

    "focus": "Sharp focus on the man, his phone, and the cup. The background is gently blurred (bokeh)."

  }

}
```

[[Bokeh Background]] [[High Angle Shot]] [[Expression Variation]]

---

### 165. Coquette 审美街头摄影肖像

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-02-06  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真的竖幅照片：一位年轻女性身穿媚骨风格的奶油黄色迷你连衣裙，手捧一束鲜花。场景设定在欧洲街角，背景是赤陶色建筑，拍摄于柔和、漫射的午后光线中。

![Coquette 审美街头摄影肖像](https://cms-assets.youmind.com/media/1770446070994_3c5jz7_HAcPer5WkAAFQyv.jpg)

```
{
  "prompt_schema_version": "1.0",
  "technical_specifications": {
    "resolution": "8k",
    "quality_preset": "Ultra High Definition (UHD)",
    "dynamic_range": "High Dynamic Range (HDR)",
    "realism_level": "Ultra Realistic",
    "aspect_ratio": "9:16",
    "orientation": "Vertical (Long)",
    "style": "Photography"
  },
  "subject": {
    "demographics": "Young woman, approximately 20-25 years old",
    "appearance": {
      "hair": "Long, dark brown, loose waves, parted in the middle",
      "skin_tone": "Warm tan",
      "expression": "Soft smile, direct eye contact, confident but gentle"
    },
    "pose": {
      "stance": "Standing, leaning casually against a building corner",
      "legs": "Crossed at the ankles",
      "arms": "Holding a bouquet across the waist"
    }
  },
  "apparel": {
    "dress": {
      "color": "Pale butter yellow",
      "type": "Mini dress",
      "style": "Coquette/Romance aesthetic",
      "details": [
        "Spaghetti straps",
        "Corset-style bodice",
        "White lace trim on neckline",
        "Textured jacquard fabric",
        "A-line skirt"
      ]
    },
    "footwear": {
      "type": "Ballet flats",
      "color": "Metallic silver",
      "material": "Leather"
    },
    "accessories": [
      "Gold pendant necklace",
      "Minimalist gold bracelet",
      "Small hoop earrings"
    ]
  },
  "props": {
    "item": "Flower bouquet",
    "contents": "{argument name="flower type" default="Pink and mauve hydrangeas"}, green foliage",
    "wrapping": "Brown kraft paper",
    "position": "Held in both hands against the midsection"
  },
  "environment": {
    "setting": "European street corner (reminiscent of {argument name="location" default="Italy or France"})",
    "architecture": {
      "wall_color": "Warm terracotta/ochre orange",
      "features": [
        "Wooden shop window frame with glass",
        "Bottles visible inside the shop window (wine/liquor)",
        "Framed certificates hanging inside window"
      ]
    },
    "ground": "Grey stone pavement/sidewalk",
    "background_depth": "Blurred street perspective on the right side showing building facades"
  },
  "lighting_and_atmosphere": {
    "source": "Natural daylight",
    "quality": "Soft, diffused afternoon light",
    "shadows": "Gentle, natural shadows cast by the subject against the wall",
    "color_grading": "Warm, golden hour undertones"
  }
}
```

[[Flower Bouquet Prop]]

---

### 166. 详细的浴室自拍图像生成提示

**Author**: [Sudee🥀](https://x.com/NameIsSudee)  **Date**: 2026-02-06  **Language**: en

> 一个高度详细的 JSON 格式提示，专为使用 Gemini Nano Banana Pro 进行图像生成而设计。它指定了主体、场景（现代奢华浴室）、姿势（嘟嘴、比 V 手势、手持牙刷）、光线（明亮的自然日光）和美学（休闲生活方式摄影、社交媒体美学）。

![详细的浴室自拍图像生成提示](https://cms-assets.youmind.com/media/1770446104955_vqtnn2_HAcOilaacAABGIR.jpg)

```
{
  "prompt": "Bathroom mirror selfie, young woman with platinum white blonde hair in messy high bun with loose strands framing face, both arms raised up, right hand holding white toothbrush, left hand making peace sign, playful duck face pout expression, wearing white cropped long sleeve sweatshirt with black checkered racing flag pattern sleeves and black text logo on chest, black high waisted shorts, light blue green eyes, fair skin, green nail polish on one hand, standing in front of large round gold frame mirror, modern grey tile bathroom walls, white marble countertop with double sinks, white bathroom cabinets, bright natural daylight, playful morning routine content, casual lifestyle aesthetic, 3:4",
  "negative_prompt": "outdoor, formal setting, heavy makeup, serious expression, nighttime, studio lighting, dark bathroom",
  "style": "casual lifestyle photography, bathroom selfie, playful morning routine content, social media aesthetic",
  "aspect_ratio": "3:4",
  "camera": {
    "type": "smartphone camera",
    "angle": "front facing, eye level",
    "framing": "medium shot, upper body and hips visible"
  },
  "lighting": {
    "type": "bright natural daylight from bathroom window",
    "quality": "soft diffused natural light, bright and airy",
    "atmosphere": "modern bright bathroom morning light"
  },
  "mood": "playful, fun, casual, fresh, youthful, carefree, energetic",
  "color_palette": "platinum blonde, white sweatshirt, black checkered pattern, black shorts, gold mirror frame, grey tiles, white marble, green nail accent",
  "subject_features": {
    "hair": "platinum white blonde, messy high bun on top of head, loose wispy strands and face framing pieces",
    "skin": "fair, natural, fresh faced",
    "eyes": "light blue green, looking at camera",
    "lips": "natural pink, playful duck face pout",
    "eyebrows": "natural, soft shape",
    "expression": "playful pout, fun silly mood, duck face"
  },
  "accessories": {
    "nails": "green nail polish visible on right hand"
  },
  "wardrobe": {
    "top": "white cropped long sleeve sweatshirt, black and white checkered racing flag pattern on sleeves, black collar detail, black text logo on chest reading text",
    "bottom": "black high waisted fitted shorts, athletic style"
  },
  "props": {
    "toothbrush": "white toothbrush held in raised right hand"
  },
  "pose": {
    "arms": "both arms raised up above head",
    "right_hand": "holding toothbrush up",
    "left_hand": "making peace sign V gesture",
    "body": "standing facing camera, slight hip angle",
    "expression": "playful duck face pout"
  },
  "setting": {
    "location": "modern luxury bathroom",
    "mirror": "large round mirror with gold brass frame",
    "walls": "grey stone or tile walls",
    "vanity": "white cabinets, white marble countertop, double sinks with silver faucets",
    "atmosphere": "bright modern clean bathroom interior"
  }
}
```

[[V Sign Gesture]]

---

### 167. 时尚大片人像摄影：阴天光线运用

**Author**: [D. Humann](https://x.com/dhumann)  **Date**: 2026-02-06  **Language**: en

> 一个结构化的 JSON 提示，用于生成一张在阴天日光下，都市环境中女性的高级时装编辑肖像。它详细指定了姿势坐标、服装（罗纹针织开衫和露脐上衣）、环境（红砖墙）以及技术渲染细节，例如 35mm 镜头美学和柔和环绕照明。

![时尚大片人像摄影：阴天光线运用](https://cms-assets.youmind.com/media/1770446063481_xa4bhe_HAcAiRGaQAArXrJ.jpg)

```
{
  "engine_optimization": "Nano Banana Pro",
  "directive": "High-Fashion Editorial",
  "subject_profile": {
    "identity_anchors": {
      "description": "Maintain the specific facial geometry, hair, and eye shape of the reference subject. High-fidelity facial reconstruction.",
    },
    "pose_coordinates": {
      "frame": "Waist-up vertical portrait.",
      "posture": "Leaning back against the masonry; left hand cupping the jawline with fingers near the temple; right hand resting at the collarbone.",
      "alignment": "Direct eye contact with camera; 15-degree head tilt to the left."
    }
  },
  "wardrobe_manifest": {
    "outerwear": {
      "style": "Heavy-gauge rib-knit cardigan, {argument name="cardigan color" default="heather grey"}.",
      "drape": "Slouchy, open-front silhouette, oversized sleeves."
    },
    "underlayer": {
      "style": "Coordinating grey knit crop-top.",
      "neckline": "Dramatic V-shaped neckline, architectural fit."
    },
    "styling": "Exposed waistline; high-waisted denim visible at the bottom edge."
  },
  "environment_logic": {
    "surface": "Vertical {argument name="wall material" default="red brick"} wall, running bond pattern, matte weathered finish.",
    "depth": "Strong separation; blurred urban elements and vertical pole in the far background."
  },
  "technical_rendering": {
    "lighting": "Natural overcast daylight; soft-wrap illumination; neutral color temperature.",
    "lens": "35mm f/1.4 aesthetic; sharp focus on the iris and fabric fibers; high-contrast textures."
  }
}
```

[[Brick Wall Background]] [[35mm Lens Aesthetic]] [[Urban Fashion Editorial]]

---

### 168. 复古 1960 年代芭比风电影感肖像

**Author**: [Ayyoub Ai](https://x.com/MaAyyoub)  **Date**: 2026-02-06  **Language**: en

> 一份全面的提示，指示 AI 扮演世界级商业摄影师，创作一张 1960 年代“芭比风”（Barbiecore）的超现实电影感肖像照，强调单色粉色调、特定服装（粉色缎面连衣裙、卷发器）、高调布光，并使用参考图像来确保拍摄对象的肖像和比例。

![复古 1960 年代芭比风电影感肖像](https://cms-assets.youmind.com/media/1770446079138_7du4b1_HAbt1OGXcAElexG.jpg)
![复古 1960 年代芭比风电影感肖像](https://cms-assets.youmind.com/media/1770446078955_85wz0e_HAbt1OZXIAAfJcA.jpg)
![复古 1960 年代芭比风电影感肖像](https://cms-assets.youmind.com/media/1770446079125_crb4n0_HAbt1ONXcAAMjmB.jpg)
![复古 1960 年代芭比风电影感肖像](https://cms-assets.youmind.com/media/1770446080207_ufyvr4_HAbt1OMWIAAAZlC.jpg)

```
ROLE: World-class commercial/editorial photographer. Create a photorealistic cinematic portrait in retro 1960s "Barbiecore" fashion.

SUBJECT: Use the exact person from the reference photo. Preserve facial structure, natural skin tone, and curvy proportions (no slimming). Expression: Flirtatious, confident, soft, natural smile.

STYLE: 1960s retro glamour, vintage fashion magazine cover. Monochromatic pink palette (bubblegum/powder pink), white, gold accents. Glossy, polished, cinematic depth.

COMPOSITION: Vertical 2:3, tight bust-up portrait, studio setting. Bright solid pink background. Subject sits on a powder-pink velvet chair, leaning slightly back. One hand near collarbone, other holding a vintage white-and-gold telephone receiver near face

WARDROBE & HAIR: Bubblegum pink satin off-shoulder mini dress with puff sleeves. Voluminous curls with pink rollers (getting-ready look). Pearl earrings.

LIGHTING: High-key soft warm beauty lighting, gentle specular highlights on lips/cheekbones, subtle shadows for dimension. Luminous, inviting tone.

CAMERA: 85mm portrait lens, slightly low angle, ultra-realistic textures (visible pores, no plastic smoothing), glossy satin and skin
```

[[High Key Lighting]]

---

### 169. 精华液瓶的高对比度影棚产品照

**Author**: [Ivan](https://x.com/ai_artdirector)  **Date**: 2026-02-05  **Language**: en

> 一个高度技术性的提示，用于生成一张圆柱形精华液瓶的高对比度、超逼真工作室产品照片。它详细描述了构图（对角倾斜，被黑色机械夹具夹住）、质地（粘稠的绿色液体滴落）、光线（左上方硬朗的定向光）以及产品目录中临床、极简主义的美学。

![精华液瓶的高对比度影棚产品照](https://cms-assets.youmind.com/media/1770359925881_ec71ee_HAbsd6taoAAfdbV.jpg)

```
IMAGE: A single cylindrical serum bottle is positioned slightly right of center in the frame, diagonally tilted from the upper right toward the lower left, creating a bottom-weighted composition with most visual mass concentrated in the lower middle of the image; the camera presents a three-quarter front view of the bottle, with the front label and a slight portion of its right side visible, viewed from slightly above eye level and angled downward, as if the camera is hovering just above the subject; the bottle appears suspended mid-air, gripped near its neck by a black mechanical clamp that enters from the upper right corner, partially cropped by the frame edge so that the top and rightmost portions of the clamp extend beyond the border; the bottle’s cylindrical body has rounded edges and a smooth, matte label surface, while the cap is also cylindrical with a flat top, and the entire form is oriented diagonally, pointing toward the lower left corner; thick, glossy {argument name="liquid color" default="green"} liquid coats the upper portion of the bottle and cap, forming viscous drips that curve downward under gravity, with rounded edges and reflective highlights indicating a semi-transparent, gel-like texture; the clamp consists of angular, geometric components—rectangular arms and jointed segments with sharp edges—forming a rigid, industrial silhouette around the bottle’s neck, its matte black surface absorbing most of the light and appearing nearly featureless; the environment is a seamless, uniform light-grey background with no visible horizon or texture, creating a clean, studio-like setting with no foreground or background objects besides the clamp and bottle; the camera perspective feels close to medium-close distance with minimal perspective distortion, suggesting a normal to slightly telephoto focal length; focus is sharp across both the clamp and the bottle, with no noticeable depth-of-field blur, giving the image a crisp, product-catalog clarity; lighting is hard and directional from the upper left, producing bright specular highlights along the bottle’s curved surface and the glossy green liquid, while casting deep, dense shadows across the clamp, which reads as a near-black silhouette; the light creates subtle reflections on the bottle’s smooth surfaces and accentuates the thickness of the dripping liquid; effects include high contrast between the white label, black clamp, and grey background, with clean edges, minimal visible grain, and a slightly stylized color grade that emphasizes the green liquid as the only saturated accent; the color palette is restrained—neutral grey background, black clamp, white label, and a vivid green liquid—creating a cool, clinical, high-contrast atmosphere; there is no visible haze, dust, or motion blur, and the scene appears entirely static and controlled. TEXT: Title: “{argument name="product title" default="THE RETINOL SERUM"}”; Body: “TRANSFORMATIVE VITAMIN A COMPLEX”; Other: “30 ML / 1.0 FL OZ”.
```

[[High Contrast Studio Lighting]] [[Diagonal Composition]]

---

### 170. 图片风格迁移提示词：维京风格转梵高《星月夜》风格

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-05  **Language**: ja

> 这是一个给 Nano Banana Pro（Gemini 3 Pro 图像）的提示，指示它将一张输入图像（喜剧二人组 Viking 的照片）转换成梵高《星月夜》的风格。用户认为结果相当成功。

![图片风格迁移提示词：维京风格转梵高《星月夜》风格](https://cms-assets.youmind.com/media/1770359998131_dkv4nf_HAbmF0VbcAA_Fao.jpg)
![图片风格迁移提示词：维京风格转梵高《星月夜》风格](https://cms-assets.youmind.com/media/1770359998319_ieijbq_HAbmFxRacAAdIOs.jpg)

```
この絵（バイきんぐの写真）を
ゴッホの星月夜みたいな
絵に変えて出して！
```

[[Artistic Style Transfer]] [[Image-to-Image Style Transfer]]

---

### 171. 图片风格迁移提示：维京风格到达利《燃烧的长颈鹿》风格

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-05  **Language**: ja

> 给 Nano Banana Pro（Gemini 3 Pro 图像）的提示，指示它将输入图像（喜剧二人组 Viking 的照片）转换为萨尔瓦多·达利《燃烧的长颈鹿》的风格，并强调超现实主义。用户指出结果缺乏预期的达利风格。

![图片风格迁移提示：维京风格到达利《燃烧的长颈鹿》风格](https://cms-assets.youmind.com/media/1770359997337_i0c4ed_HAbj5HRa0AAGXaP.jpg)
![图片风格迁移提示：维京风格到达利《燃烧的长颈鹿》风格](https://cms-assets.youmind.com/media/1770359997478_igm1kj_HAbj5GEbUAAQZ5i.jpg)
![图片风格迁移提示：维京风格到达利《燃烧的长颈鹿》风格](https://cms-assets.youmind.com/media/1770359997576_evcrpo_HAbj5GGacAAQLHJ.jpg)

```
この絵（バイきんぐ）を
ダリの「燃える麒麟」みたいな絵にして出して！

シュールレアリスム
```

[[Image-to-Image Style Transfer]]

---

### 172. 图片风格迁移提示词：维京人到《勇者斗恶龙 X》“贤者之神圣气息”

**Author**: [クラリネットクラリオンNOBU](https://x.com/NOBU79834619)  **Date**: 2026-02-05  **Language**: ja

> 这是一个给 Nano Banana Pro（Gemini 3 Pro 图像）的提示，指示它接收一张输入图像（喜剧二人组 Viking 的照片），并将图像的右侧转换为《勇者斗恶龙 X》中贤者能力“神之吐息”的风格。用户指出这次尝试失败了，可能是由于对参考图像的误解。

![图片风格迁移提示词：维京人到《勇者斗恶龙 X》“贤者之神圣气息”](https://cms-assets.youmind.com/media/1770359999189_479qwz_HAbh9BGacAE1wG0.jpg)
![图片风格迁移提示词：维京人到《勇者斗恶龙 X》“贤者之神圣气息”](https://cms-assets.youmind.com/media/1770359999114_str9iw_HAbh8_casAAXWOT.jpg)
![图片风格迁移提示词：维京人到《勇者斗恶龙 X》“贤者之神圣气息”](https://cms-assets.youmind.com/media/1770359999242_xjusn8_HAbh9BbakAAJcFc.jpg)

```
この絵（バイきんぐの写真）を
右　ドラクエXの賢者「神の息吹」
みたいにして出して！
```

[[Image-to-Image Style Transfer]]

---

### 173. 人造毛皮写实冬季深蹲姿势

**Author**: [Celeste](https://x.com/xCelesteAIx)  **Date**: 2026-02-05  **Language**: en

> 一个高度详细的超写实提示，用于生成一张在白雪皑皑的冬季森林中深蹲的曲线优美女性的图像。该提示细致地定义了拍摄对象的服装（仿皮草夹克、灰色打底裤、Moon Boots）、后方 3/4 视角姿势、环境（白雪覆盖的常绿森林）以及技术相机设置（低角度、中等景深、漫射光），以实现高质量的户外肖像。

![人造毛皮写实冬季深蹲姿势](https://cms-assets.youmind.com/media/1770359914165_zcu0yi_HAbdM8qWcAILfbG.jpg)

```
{
"subject": {
"description": "A young woman with a fit, curvaceous figure captured in a rear-view squatting pose. She has long, wavy, {argument name="hair color" default="red"} hair that falls over her shoulders. Her complexion is naturally tanned with visible skin texture.",
"apparel": {
"headwear": "Large, fluffy white faux-fur earmuffs covering the ears completely.",
"upper_body": "A short, cropped white faux-fur jacket with a plush, textured surface. The jacket ends at the waist, revealing the curve of the lower back.",
"lower_body": "Tight, heather grey leggings made of a soft, matte cotton-spandex blend fabric. The fabric stretches naturally over the glutes and thighs, showing realistic fabric tension and texture without looking plastic.",
"footwear": "Chunky, beige knee-high snow boots (Moon Boot style) with white laces and distinct white branding text on the heel and shaft. The boots are bulky and structured, resting deep in the snow."
},
"physical_attributes": {
"body_type": "Fit and voluptuous hourglass figure, emphasized by the crouching position.",
"skin_texture": "Natural skin finish with realistic grain, varied tones, and no artificial smoothing."
}
},
"pose": {
"type": "Deep squat / crouching position.",
"orientation": "The body is angled away from the camera (rear 3/4 view), with the back and glutes prominent.",
"head_position": "Head is turned sharply over the right shoulder to face the camera directly.",
"eye_contact": "Direct, calm, and engaging eye contact with the viewer.",
"limb_placement": "Legs are bent deeply at the knees, feet are planted firmly in the snow. Arms are relaxed, likely resting on the knees (mostly obscured by the jacket and pose).",
"dynamics": "Static but balanced, conveying the weight of the body settling into the squat."
},
"environment": {
"setting": "A dense winter forest covered in heavy snow.",
"ground": "Thick, powdery white snow with visible footprints and uneven surface texture where the boots have disturbed it.",
"background": "Tall evergreen trees (spruce or pine) heavily laden with snow on their branches. The trees create a textured, natural backdrop that fills the frame.",
"atmosphere": "Cold, crisp winter air, distinct outdoor setting."
},
"camera": {
"type": "Professional DSLR or Mirrorless camera (e.g., Sony A7R or Canon R5).",
"lens": "50mm to 85mm portrait lens.",
"perspective": "Low angle, roughly eye-level with the crouching subject.",
"depth_of_field": "Moderate depth of field (f/4.0 or f/5.6). The subject is razor-sharp, while the background trees are slightly softened but still clearly defined, maintaining environmental context.",
"focus": "Sharp focus on the subject's face and eyes."
},
"lighting": {
"type": "Natural overcast daylight (diffused).",
"quality": "Soft, even, shadowless light typical of a snowy day. The white snow acts as a giant natural reflector, bouncing light upward and filling in shadows on the face and body.",
"direction": "Omnidirectional ambient skylight.",
"highlights
```

[[Snowy Forest Setting]]

---

### 174. 米莉·芭比·布朗 (Millie Bobby Brown) 和 萨迪·辛克 (Sadie Sink) 身着泳装的运动肖像

**Author**: [Bethany](https://x.com/JustBethanyai)  **Date**: 2026-02-05  **Language**: en

> 一个结构化的提示，用于生成米莉·芭比·布朗（Millie Bobby Brown）和萨迪·辛克（Sadie Sink）的运动、俏皮肖像，她们身穿配套的连体泳衣（红色和白色），置身于现代健身房中。提示详细说明了她们的姿势、表情以及背景中的健身器材，并强调使用明亮柔和的灯光来突出她们的身材。

![米莉·芭比·布朗 (Millie Bobby Brown) 和 萨迪·辛克 (Sadie Sink) 身着泳装的运动肖像](https://cms-assets.youmind.com/media/1770359933245_rzv735_HAbYCKbWgAA3SOo.jpg)
![米莉·芭比·布朗 (Millie Bobby Brown) 和 萨迪·辛克 (Sadie Sink) 身着泳装的运动肖像](https://cms-assets.youmind.com/media/1770359933225_augo4w_HAbYCoIWcAAJaCI.jpg)
![米莉·芭比·布朗 (Millie Bobby Brown) 和 萨迪·辛克 (Sadie Sink) 身着泳装的运动肖像](https://cms-assets.youmind.com/media/1770359933992_ppgbfn_HAbYBrCXoAAsLod.jpg)
![米莉·芭比·布朗 (Millie Bobby Brown) 和 萨迪·辛克 (Sadie Sink) 身着泳装的运动肖像](https://cms-assets.youmind.com/media/1770359935294_z67k3t_HAbYDHlWAAAXCFM.jpg)

```
{
  "scene_description": "{argument name="celebrity 1" default="Sadie Sink"} and {argument name="celebrity 2" default="Millie Bobby Brown"} are in a gym, wearing matching swimsuits. Sadie wears a red one-piece swimsuit with straps, while Millie wears the same style but in white. They are posing confidently, surrounded by gym equipment, with a balance board in the background resembling a 'Midner' style balance board. The gym has a modern, well-lit, and clean aesthetic.",
  "characters": [
    {
      "name": "Sadie Sink",
      "outfit": {
        "type": "swimsuit",
        "color": "red",
        "style": "one-piece",
        "features": [
          "straps",
        ]
      },
      "position": "standing confidently with hands on hips, facing slightly to the side",
      "expression": "confident, smiling slightly",
      "hair": "long, wavy, reddish-brown",
      "body_type": "athletic, tall"
    },
    {
      "name": "Millie Bobby Brown",
      "outfit": {
        "type": "swimsuit",
        "color": "white",
        "style": "one-piece",
        "features": [
          "straps",
          "high-cut legs"
        ]
      },
      "position": "standing confidently with hands on hips, facing forward",
      "expression": "confident, playful",
      "hair": "short, brown, slightly wavy",
      "body_type": "athletic, medium height"
    }
  ],
  "environment": {
    "type": "gym",
    "details": {
      "equipment": [
        "balance board (Midner style)",
        "exercise mats",
        "gym weights",
        "treadmills in the background"
      ],
      "lighting": "bright and soft, spotlight on the characters",
      "color_scheme": "neutral tones with pops of color from the gym equipment",
      "flooring": "wooden or rubber gym flooring"
    }
  },
  "mood": "empowered, athletic, playful",
  "pose": "Sadie is slightly turned to the left, Millie is facing forward but both are confident and energetic",
  "composition": {
    "camera_angle": "eye-level, capturing both characters in a balanced frame",
    "focus": "both Sadie and Millie are in sharp focus, with a slight blur in the gym background",
    "lighting": "soft natural light accentuates their figures and gives a healthy, active glow"
  }
}
```

[[Modern Gym Setting]]

---

### 175. 身穿睡衣的女性的超逼真自拍

**Author**: [Celeste](https://x.com/xCelesteAIx)  **Date**: 2026-02-05  **Language**: en

> 一个详细的、照片级的提示，旨在生成一张年轻女性在舒适现代客厅里的特写自拍。该提示详细说明了身体特征、服装（米色罗纹亨利衫和睡裤）、放松的坐姿以及温暖、讨喜的室内光线，旨在营造出高保真度的社交媒体网红美学。

![身穿睡衣的女性的超逼真自拍](https://cms-assets.youmind.com/media/1770359914024_adzx3k_HAbVoiBW0AAK7xe.jpg)

```
{
"subject": "Young woman with ash blonde hair styled in a casual, loose updo with strands framing the face. She has a fair to light tan complexion with realistic skin texture. She is wearing a tight-fitting, cream-colored, ribbed Henley long-sleeve shirt. The shirt is unbuttoned at the top, revealing deep cleavage and a very full, voluminous bust that projects forward naturally, creating tension in the fabric. She is also wearing cream-colored pajama pants with a small, whimsical print (possibly {argument name="pajama print" default="animals with scarves"}) featuring a prominent bright red drawstring tied at the waist. Her makeup is polished with defined lashes, contouring, and glossy lips.",
"pose": "Seated in a relaxed, reclining position on a soft couch. The torso is angled slightly to the right, while the head is turned to face the camera directly. The right arm is extended forward towards the lens, creating a selfie perspective. The left shoulder is relaxed against the couch cushion. The posture highlights the curve of the waist and the significant volume of the chest.",
"environment": "A cozy, modern living room interior. The subject is seated on a large, textured cream or white sectional sofa. Behind her are multiple throw pillows, including a dark charcoal velvet pillow and a textured beige pillow. On the wall behind the sofa, there is a large framed black-and-white photograph (partially visible, appearing to be a vintage car wheel). To the right, a lamp with a black shade sits on a surface, emitting a warm, ambient glow.",
"camera": "Close-up selfie shot taken at arm's length. The angle is slightly elevated, looking down at the face and torso. The focal length creates a slight perspective distortion typical of phone cameras, emphasizing the foreground features. The focus is sharp on the face and upper body, with a gentle fall-off in sharpness towards the background.",
"lighting": "Soft, warm, flattering indoor lighting. Key light illuminates the face and chest from the front-left, highlighting the cheekbones, the bridge of the nose, and the upper curves of the bust. The background is dimly lit with warm accent lighting from the lamp, creating a cozy and intimate atmosphere.",
"mood_and_expression": "Confident, happy, and relaxed. The subject has a wide, bright smile exposing white teeth, and she is making direct, engaging eye contact with the viewer.",
"style_and_realism": "High-fidelity photorealism, resembling a high-quality social media influencer photo. Sharp details, realistic skin texture with visible pores, natural fabric folds, and accurate material rendering.",
"colors_and_tone": "Warm and neutral color palette. Dominant tones are creams, beiges, and skin tones, accented by the black of the artwork and pillow, and the small pop of red from the pajama drawstring. The overall tone is inviting and soft.",
"quality_and_technical_details": "8k resolution, raw photo quality, high dynamic range. No artifacts, no blurring of key features. Textur
```

[[Warm Indoor Lighting]] [[Close-Up Selfie]] [[Social Media Influencer Aesthetic]]

---

### 176. 穿着黑色露脐连帽衫的 iPhone 自拍，姿态撩人

**Author**: [Alice Glassier](https://x.com/aliceglassierai)  **Date**: 2026-02-05  **Language**: en

> 一个结构化的 JSON 提示，用于生成一张超逼真、暗示性的 iPhone 自拍，拍摄地点为夜间客厅。它详细描述了拍摄对象的曼妙身材、黑色短款连帽衫和低腰丁字裤，通过柔和温暖的室内光线和轻微的噪点，强调“仅限 iPhone 拍摄的效果”，并遵循“暗示而非露骨”的原则。

![穿着黑色露脐连帽衫的 iPhone 自拍，姿态撩人](https://cms-assets.youmind.com/media/1770359910825_jxhsey_HAbP-TZWkAAvNWo.jpg)

```
{
  "meta": {
    "quality": "ultra photorealistic",
    "resolution": "8k",
    "camera": "iPhone 15 Pro Max",
    "lens": "24mm",
    "aspect_ratio": "9:16",
    "style": "night iphone selfie, soft warm indoor light, slight noise"
  },

  "character_lock": {
    "age": "mid 20s (adult)",
    "ethnicity": "mediterranean brunette",
    "hair": {
      "color": "black brown",
      "style": "high ponytail"
    },
    "eyes": "hazel",
    "body": {
      "type": "curvy hourglass",
      "chest": "very full",
      "waist": "tiny",
      "hips": "round"
    }
  },

  "scene": {
    "location": "living room",
    "time": "night",
    "atmosphere": "quiet apartment"
  },

  "subject": {
    "action": "taking selfie while slightly lifting hoodie",
    "pose": {
      "one arm up holding phone",
      "other hand gripping hoodie hem",
      "hips slightly back",
      "expression": "small naughty smile"
    },

    "outfit": {
      "top": {
        "type": "cropped hoodie",
        "color": "black",
        "fit": "tight, braless"
      },
      "bottom": {
        "type": "low-rise thong",
        "color": "black",
        "visibility": "waistband visible"
      }
    }
  },

  "environment": {
    "background": [
      "couch",
      "lamp",
      "dark window"
    ],
    "lighting": {
      "type": "warm lamp",
      "effect": "glow on stomach and chest"
    }
  },

  "photography_rules": {
    "iphone_only_look": true,
    "no_male_presence": true,
    "suggestive_not_explicit": true
  }
}
```

[[Film Grain Aesthetic]]

---

### 177. 非洲村庄场景的纪实照片

**Author**: [Precious 💕](https://x.com/odoipre)  **Date**: 2026-02-05  **Language**: en

> 一个程序化的提示结构，用于生成一张纪录片风格的照片，内容是一位年轻的非洲女性在郁郁葱葱的乡村中，围着火堆搅拌锅里的食物。它详细说明了环境（泥屋、茅草屋顶、高大的树木）和技术细节（50 毫米镜头、自然阳光、超现实的保真度）。

![非洲村庄场景的纪实照片](https://cms-assets.youmind.com/media/1770359930241_1glx2s_HAbDVFhWMAA1g1Q.jpg)
![非洲村庄场景的纪实照片](https://cms-assets.youmind.com/media/1770359930325_az48di_HAbDVLcX0AA9krT.jpg)

```
class ImageGenerator:
    def __init__(self):
        self.base_style = "Documentary Photography"
        self.lens_profile = "50mm prime lens"

    def generate_village_scene(self):
        prompt_config = {
            "subject": {
                "actor": "Young African woman",
                "attire": "patterned wrapper and headscarf",
                "action": "stirring a pot with a wooden spoon over a three-stone fire"
            },
            "environment": {
                "location": "Lush rural African village",
                "elements": ["mud huts", "thatched roofs", "tall green trees"],
                "background": "children playing happily",
                "atmosphere": "clean natural environment"
            },
            "technical_specs": {
                "lighting": "Natural sunlight",
                "fidelity": "Ultra-realistic, high detail",
                "style": self.base_style,
                "optics": self.lens_profile
            }
        }
        return prompt_config

# Initialize the generator
session = ImageGenerator()
print(session.generate_village_scene())
```

[[African Village Documentary Photo]]

---

### 178. 海滩日图像生成

**Author**: [☆ 𝐛𝟑𝐥𝐥𝐚-𝐂𝐡𝐚𝐧 ♡](https://x.com/b3lla_callahan)  **Date**: 2026-02-05  **Language**: en

> 一个简单、描述性的提示，用于生成与海滩日相关的图片，可能用于社交媒体内容。

![海滩日图像生成](https://cms-assets.youmind.com/media/1770360002689_khw329_HAbB1S_WgAAY1l5.jpg)

```
Día de playa! 🏖👙☀️🤍🩷🩵
```

[[Social Media Content]]

---

### 179. 1971 年 Yeşilçam 电影中哭泣的 Türkan Şoray 肖像的 JSON 提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-05  **Language**: en

> 一个为 Nano Banana Pro 设计的结构化 JSON 提示，请求生成一张土耳其女演员 Türkan Şoray 戏剧性哭泣的超详细电影风格肖像静帧，风格效仿 1971 年的 Yeşilçam 电影，强调浓重、晕染的妆容、金色时段的泪水和怀旧的柯达胶片调色。

![1971 年 Yeşilçam 电影中哭泣的 Türkan Şoray 肖像的 JSON 提示](https://cms-assets.youmind.com/media/1770359947323_02ox4x_HAazRxYWwAEPupZ.jpg)

```
json{
 "prompt": "1971 Yeşilçam ultra-detailed cinema still portrait of Türkan Şoray crying dramatically, large emotional eyes with heavy blue-purple smokey eyeshadow blending to center, thick wet black kohl liner smudged from tears, voluminous 70s fön waves cascading over shoulders with perfect side part, contoured over-drawn red matte lips slightly parted in pain, golden hour tears glistening on cheekbones, subtle iris circular vignette framing emotional face, warm nostalgic Kodak film grading with crushed blacks and lifted highlights, Istanbul rainy window background blurred with rain droplets and lace curtains, Arriflex 35mm Zeiss Super Speed T1.3 shallow depth of field bokeh, visible authentic film grain texture, natural pores and imperfections, professional cinema lighting ratio 3:1 creating dramatic cheekbone shadows",
 "aspect_ratio": "2:3",
 "cfg_scale": 8.5 
} {
"negative_prompts": {
"core": "modern digital, plastic skin, airbrushed, cold lighting, neon, cartoon",
"makeup": "beauty filter, poreless skin, overdrawn lips, graphic eyeliner, K-beauty",
"hair": "balayage, ombre, wet look, slicked back, rainbow highlights",
"tech": "smartphone camera, ring light, iPhone, Instagram filter, TikTok effect",
"lighting": "studio lighting, flat light, HDR, overexposed highlights",
"quality": "blurry, lowres, watermark, text, deformed hands, extra limbs"
}
}
```

[[Vintage Turkish Cinema Portrait]]

---

### 180. 用于超逼真商业能量饮料摄影的 JSON 提示词

**Author**: [Nexora](https://x.com/frametheory058)  **Date**: 2026-02-05  **Language**: en

> 一个高度详细的 JSON 提示，用于 Nano Banana Pro，请求拍摄一张超现实的商业风格照片，内容为时尚的铝制能量饮料罐，具有爆炸性的霓虹液体飞溅、电火花和冷冻颗粒，背景为深色、高能量的场景。

![用于超逼真商业能量饮料摄影的 JSON 提示词](https://cms-assets.youmind.com/media/1770359950231_ls53gs_HAaw8GzacAIKnor.jpg)
![用于超逼真商业能量饮料摄影的 JSON 提示词](https://cms-assets.youmind.com/media/1770359950545_puz7aq_HAaw8GwakAARPnh.jpg)

```
{
  "master_prompt": {
    "global_settings": {
      "resolution": "8K ultra-high-definition",
      "aspect_ratio": "9:16 vertical",
      "style": "hyper-realistic AI-edited commercial beverage photography",
      "sharpness": "extreme clarity, micro-detail visibility",
      "lighting_quality": "cinematic studio lighting with neon rim highlights",
      "motion_freeze": "high-speed capture, frozen liquid splashes, sparks, and particles",
      "noise": "none",
      "artifacts": "none"
    },

    "module_1_preworkout_electric_drink": {
      "subject": {
        "type": "sleek aluminum energy drink can",
        "surface_detail": "cold condensation droplets on metallic surface",
        "fill_level": "sealed can with explosive energy theme design",
        "label_text_visible": [
          "mock up",
          "pre workout energy",
          "explosive focus",
          "SEPARATED SHADOWS"
        ]
      },

      "liquid_motion": {
        "action": "neon colored liquid splash erupting violently around the can",
        "splash_behavior": "sharp aggressive splash arcs with glowing edges",
        "droplet_detail": "bright neon droplets frozen mid-air",
        "liquid_color": "electric blue and neon green mix"
      },

      "electric_effects": {
        "sparks": "electric sparks and lightning streaks wrapping around splash",
        "glow": "subtle neon glow emitting from liquid edges",
        "energy_particles": "tiny glowing particles dispersed in air"
      },

      "floating_elements": {
        "powder_particles": "pre-workout powder dust floating like mist",
        "ice_shards": "small sharp ice fragments suspended mid-air"
      },

      "environment": {
        "background_theme": "dark black to deep blue gradient",
        "bokeh": "neon bokeh light dots in background",
        "atmosphere": "intense gym energy, powerful, aggressive mood"
      },

      "surface_and_reflection": {
        "base": "wet reflective surface with neon reflections",
        "shadow_style": "clean separated shadow beneath can",
        "reflection_quality": "bright metallic highlights along edges"
      },

      "pose_and_camera": {
        "position": "center hero composition",
        "angle": "slightly low three-quarter close-up angle",
        "camera_feel": "high-energy commercial advertisement perspective"
      }
    }
  }
}
```

[[Hyperrealistic Product Photography]]

---

### 181. 前卫肖像，有机颗粒马赛克纹理

**Author**: [timedoctor.eth](https://x.com/timedoctor_nft)  **Date**: 2026-02-05  **Language**: en

> 一个高度结构化的提示，用于生成一张超现实的中画幅肖像，标题为“活着的静物”。肖像中，人物的脸部覆盖着一层白色的有机颗粒（米粒）和橙色的球体（鱼卵）组成的假体。该提示强调微距摄影细节、伦勃朗光线和触感摄影超现实主义，以创作一件编辑艺术作品。

![前卫肖像，有机颗粒马赛克纹理](https://cms-assets.youmind.com/media/1770359897528_pefck6_HAavUCKW8AADb-0.jpg)
![前卫肖像，有机颗粒马赛克纹理](https://cms-assets.youmind.com/media/1770359897643_97tsqv_HAavUDUWsAA3k7V.jpg)

```
{
  "vibe_title_en": "Living Still Life",
  "master_prompt": "A hyper-realistic, medium-format portrait of The Protagonist executed as a high-concept avant-garde installation. The subject's face is meticulously covered in a practical prosthetic layer of thousands of individual white organic grains (simulating rice) and clusters of glistening, vibrant orange spheres (simulating roe), creating a textured, scale-like second skin. This organic mosaic flows seamlessly into a lavish headpiece composed of deep green moss, autumn-hued chrysanthemums, and structural botanical cylinders. The composition replicates a classic bust portrait with the head tilted slightly upward and to the side, gazing into the distance with stoic elegance. Lighting is moody and cinematic, utilizing a soft, directional light source (Rembrandt style) to accentuate the micro-relief of the grains and the wet reflection of the orange spheres. Shot on a Hasselblad H6D-100c with a 120mm Macro lens to capture the visceral reality of the materials against the subject's features, emphasizing depth, shadow, and physical weight. No digital overlay effects; pure, tactile photographic surrealism.",
  "meta": {
    "intent": "Editorial Art",
    "priorities": "Texture, Surrealism, Color Fidelity",
    "device_profile": "Cinema-Grade Monitor"
  },
  "frame": {
    "aspect": "2:3",
    "composition": "Close-up Bust Portrait",
    "layout": "Golden Ratio Spiral",
    "camera_angle": "Eye-level, slightly angled upwards",
    "tilt_roll_degrees": "15 degrees tilt"
  },
  "subject": {
    "gender": "Female",
    "identity": "The Muse",
    "demographics": "Universal/Neutral",
    "face": "Covered in organic grain mosaic texture",
    "hair": "Replaced by floral and botanical arrangement",
    "body": "Shoulders draped in moss-like textured fabric",
    "expression": "Stoic, ethereal, distant gaze",
    "pose": "Head tilted up and to the left, chin raised"
  },
  "wardrobe_accessories": {
    "garments": [
      {
        "item": "Textured Collar",
        "material": "Woven moss and organic fibers",
        "color": "Deep Forest Green and Orange",
        "fit": "Sculptural"
      }
    ],
    "accessories": [
      {
        "item": "Headpiece",
        "color": "Orange, Green, White",
        "material": "Fresh flowers, leaves, and organic clusters",
        "brand_style": "Avant-Garde Floristry"
      }
    ]
  },
  "environment": {
    "setting": "Studio Void",
    "surfaces": "Non-reflective matte background",
    "depth": "Shallow depth of field",
    "atmosphere": "Moody, intimate, artistic",
    "lens_interaction": "Sharp focus on eyes/texture, soft fall-off"
  },
  "lighting": {
    "key": "Softbox 45-degree angle",
    "fill": "Negative fill to deepen shadows",
    "rim": "Subtle cool backlight on florals",
    "shadows": "Deep, high-contrast chiaroscuro",
    "color_temperature": "Warm organic tones (4500K)",
    "sensor_flare": "None"
  }
}
```

[[Rembrandt Lighting]]

---

### 182. 粗野主义海报生成提示词

**Author**: [AI Pulse](https://x.com/youraipulse)  **Date**: 2026-02-05  **Language**: en

> 一个将任何品牌概念转化为粗野主义风格海报的通用提示，旨在呈现一种以原始、不妥协设计为特征的视觉美学。

![粗野主义海报生成提示词](https://cms-assets.youmind.com/media/1770360000290_6ifbnm_HAatkWuWUAAYdOr.jpg)
![粗野主义海报生成提示词](https://cms-assets.youmind.com/media/1770360000415_arofc5_HAatk6hXAAAUBPV.jpg)
![粗野主义海报生成提示词](https://cms-assets.youmind.com/media/1770360000439_ua1mfb_HAatilAXMAAcs15.jpg)
![粗野主义海报生成提示词](https://cms-assets.youmind.com/media/1770360001408_zvhd4l_HAatmMzWMAEZc0g.jpg)

```
Any brand to Brutalist Poster
```

[[Brutalist Poster Design]]

---

### 183. 茶杯中的微缩世界自然语言提示

**Author**: [Nexora](https://x.com/frametheory058)  **Date**: 2026-02-05  **Language**: en

> 一个详细的自然语言提示，用于 Google Gemini Nano Banana Pro，请求创建一个超现实的场景：一个微型小人坐在一座漂浮在雅致茶杯中的长满苔藓的岛屿上，强调比例错觉、电影般的日光和高细节。

![茶杯中的微缩世界自然语言提示](https://cms-assets.youmind.com/media/1770359947472_o5m6bh_HAam1smacAAI45H.jpg)

```
"Shrink the main subject into a tiny, hyper-realistic miniature person sitting on a small moss-covered island floating inside a teacup filled with tea. The island should look natural with grass, small rocks, and uneven terrain. Add a tiny wooden bridge placed across the tea surface where 2–3 miniature photographers stand, actively taking photos of the subject. Include a tiny wooden rowboat gently floating near the island, creating subtle ripples in the tea.
The teacup should be large, elegant, and floral-designed, placed on a wooden table in a cozy room. Add real-world objects around it like a sugar cube, spoon, and soft window light to emphasize the scale difference. Use cinematic soft daylight coming from a window, creating realistic reflections on the tea surface and shadows from the tiny elements.
The subject’s pose should look natural and thoughtful, interacting with the tiny environment. Add ultra-realistic textures to the tea liquid, porcelain cup, wood table, and moss. Slight depth-of-field blur in the background to focus attention on the miniature world inside the cup.
Make the scene whimsical, surreal, and extremely realistic, designed to make viewers pause and stare to understand the scale illusion. Viral, eye-catching, and highly detailed composition."
```

[[Scale Illusion]]

---

### 184. 坦率的高档酒廊肖像提示

**Author**: [Javeriya 🇺🇸](https://x.com/JadoonKhan281)  **Date**: 2026-02-05  **Language**: en

> 一个详细的提示，用于生成一张坦率的、中长镜头金发女性照片，场景设定在一家高档餐厅的休息室。该提示指定了混合的、温暖的、昏暗的灯光，带有红色霓虹灯点缀，重点突出斑马纹亮片迷你连衣裙和真诚的笑容，旨在营造出高对比度的生活方式摄影风格。

![坦率的高档酒廊肖像提示](https://cms-assets.youmind.com/media/1770359969428_avy4l1_HAaasyObUAA6ZhH.jpg)
![坦率的高档酒廊肖像提示](https://cms-assets.youmind.com/media/1770359969550_bjb8tr_HAaastlaYAA5yHE.jpg)

```
{
  "lighting": {
    "type": "Mixed indoor artificial ambient",
    "quality": "Dim, warm, soft, creating gentle shadows",
    "sources": [
      "Overhead recessed ceiling lights",
      "Warm glow from bar area in background",
      "Red neon architectural strip lighting in distant arches"
    ],
    "direction": "Top-down and soft fill"
  },
  "background": {
    "setting": "Upscale restaurant lounge interior at night",
    "atmosphere": "Luxurious, intimate, dimly lit",
    "key_elements": [
      "Plush pink velvet chairs",
      "White round marble tables",
      "Tiled beige flooring",
      "Bar area with lit shelves in the background",
      "Distinctive red neon arches"
    ]
  },
  "composition": {
    "balance": "Subject centered",
    "framing": "Front-facing full body while seated",
    "shot_type": "Medium-long shot",
    "perspective": "Eye-level",
    "depth_of_field": "Shallow, background is softly blurred"
  },
  "color_profile": {
    "palette": "Warm evening tones with high contrast",
    "dominant_colors": [
      "warm beige",
      "black",
      "muted pink",
      "vibrant red neon"
    ]
  },
  "subject_analysis": {
    "hair": "Long, blonde, loose wavy curls parted in the middle and draped over shoulders",
    "pose": "Sitting on the edge of a white marble table, legs crossed with one leg over the other, hands resting lightly on the table edge",
    "attire": "Strapless mini-length dress with a {argument name="dress pattern" default="beige and black sequined zebra print"} pattern",
    "facial_expression": "Wide, genuine smile showing teeth, looking directly at the camera",
    "subject_type": "Person, adult woman"
  },
  "technical_specs": {
    "focus": "Sharp on the subject's face and dress",
    "grain": "Slight visible grain characteristic of low-light smartphone photography",
    "style": "Candid lifestyle photography"
  },
  "generation_parameters": {
    "prompt": "A medium-long candid photo of a blonde woman sitting on a white marble table in an upscale lounge. She is wearing a strapless zebra-print sequin mini dress and has her legs crossed, one over the other. She is facing forward, smiling broadly at the camera. The background features pink velvet chairs, a dimly lit bar, and red neon arches. High quality, warm ambient lighting, realistic skin textures."
  }
}
```

[[Blonde Hair Portrait]]

---

### 185. 巨型巨人抱着一个微小婴儿的电影级 3D 渲染图

**Author**: [Crystal](https://x.com/Cicily_aura)  **Date**: 2026-02-05  **Language**: en

> 一个提示，用于生成一个超精细的电影级 3D 渲染，描绘一个巨大、肌肉发达、绿皮肤的人形生物，用两根粗大的手指轻轻托着一个微小的婴儿版自己。它强调超现实的纹理、皮克斯风格的情感温暖，以及在温暖金色灯光下的戏剧性而温柔的氛围。

```
A hyper-detailed cinematic 3D render of a colossal, green-skinned, muscular humanoid gently holding a tiny baby version of himself between two massive fingers. The giant has expressive eyes, a soft amused smile, realistic skin pores, and short dark hair. The baby is chubby and adorable with bright sparkling eyes, raised arms, and a joyful expression, wearing small torn shorts. Warm golden lighting with soft rim light, shallow depth of field, smooth blurred background. Ultra-realistic skin and fabric textures, Pixar-style emotional warmth blended with cinematic realism, high resolution, dramatic yet tender and heartwarming mood.
```

[[Scale Contrast]] [[Hyperrealistic Texture]]

---

### 186. 超逼真偷拍泳装浪漫场景生成提示

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-05  **Language**: en

> 一个高度详细的提示，旨在生成一张超写实、自然的电影剧照，捕捉一对年轻夫妇在土耳其戈科瓦（Gökova）一个多岩石海湾的场景。它强调自然光、真实的皮肤纹理（未经修饰）和纪录片式的镜头语言，以捕捉他们游泳后宁静而亲密的时刻。

![超逼真偷拍泳装浪漫场景生成提示](https://cms-assets.youmind.com/media/1770359953509_tv5iic_HAaUk4rXwAA5vSH.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_candid_swim_romance",
      "version": "v1.0_AKYAKA_GOKOVA_MIDDAY_ROCK_EDGE_VIEW_EN",
      "priority": "highest"
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "ultra_photoreal_candid_film_still",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "color_grade": "midday_turquoise_true_to_life",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "global_rules": {
      "camera_language": "35mm lens equivalent, eye-level, handheld, candid documentary feel",
      "lighting_language": "motivated natural light only (midday sun), no flash",
      "authenticity_markers": "wet skin texture, salt water shine, no HDR, no AI glow"
    },
    "creative_prompt": {
      "scene_summary": "After swimming, they pause on the rock edge. Wet hair, bright sea behind. A tender closeness with the full Gökova view.",
      "subjects": {
        "count": 2,
        "description": "young man and woman early 20s, ordinary; faces visible and sharp",
        "expression": "soft calm smiles, quiet intimacy",
        "skin_and_face": "natural wet texture, no retouch"
      },
      "wardrobe_and_props": {
        "female": "simple swimsuit with a light cotton shirt loosely draped",
        "male": "simple swim shorts, plain cotton t-shirt half-wet",
        "props": "wrinkled towel nearby, no branding"
      },
      "micro_action": "one rests a hand on the other’s shoulder; they share a quiet look toward the sea",
      "environment_details": {
        "location": "rocky cove, Akyaka–Gökova",
        "background": "wide panoramic turquoise sea, pine hills, sun path on water; tiny distant fishing boat silhouette (not luxury)"
      },
      "lighting": "strong midday light; controlled highlights on water; deep but detailed shadows; subtle halation on sun glints",
      "composition": "vertical 9:16; couple foreground; dramatic sea backdrop; imperfect framing",
      "mood": "very romantic, serene, real"
    },
    "negative_prompt": [
      "studio lighting",
      "flash",
      "beauty retouch",
      "plastic skin",
      "HDR",
      "AI glow",
      "luxury marina",
      "beach club",
      "designer logos",
      "text",
      "logo",
      "watermark"
    ]
  }
}
```

[[Unretouched Skin Texture]]

---

### 187. 超现实主义黑胶唱片播放中可视化

**Author**: [Alexandra Aisling](https://x.com/AllaAisling)  **Date**: 2026-02-05  **Language**: en

> 一个极具创意和描述性的提示，用于可视化黑胶唱片播放时发出的音乐。它指示 AI 将声音表现为雕塑般的波形、微型演奏乐手和根据音乐流派变化的风景（烟雾缭绕的俱乐部、大教堂建筑），强调温暖的模拟音色和怀旧的超现实主义。

![超现实主义黑胶唱片播放中可视化](https://cms-assets.youmind.com/media/1770359917862_nc0mnc_HAaSh-hXUAAga6g.jpg)
![超现实主义黑胶唱片播放中可视化](https://cms-assets.youmind.com/media/1770359917964_572t76_HAaS84GWIAAu-iS.jpg)
![超现实主义黑胶唱片播放中可视化](https://cms-assets.youmind.com/media/1770359918134_mo3mwk_HAaStr-WMAIfeNM.jpg)
![超现实主义黑胶唱片播放中可视化](https://cms-assets.youmind.com/media/1770359920106_30bhrk_HAaTUF6WIAArMUl.jpg)

```
A vinyl record mid-play, its grooves erupting into the music they contain. The needle touches down and sound becomes visible: {argument name="music genre" default="[GENRE/SONG]"} manifests as sculptural waveforms rising from the spinning surface. Musicians emerge in miniature, performing on the label. Different tracks create different landscapes—a jazz section becomes smoky club interior, a crescendo builds into cathedral architecture, a quiet passage forms intimate bedroom scene. Dust motes dance as visible frequencies. The album artwork on the sleeve animates and watches. Worn sleeve edges tell stories of hands that held it. Tube amplifier glows amber in background, speaker cone pulses. The whole room vibrates at 33⅓ RPM. Warm analog tones, vinyl crackle almost visible as golden particulate, 8K, nostalgic hyperrealism.
```

[[Vinyl Record Surreal Visualization]]

---

### 188. 巧克力曲奇的超逼真商业食物摄影

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-05  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成三块巧克力曲奇的商业食品摄影。它指定了超现实主义风格、8K 分辨率，以及在纯色柔和蓝色影室背景下，食材（巧克力块、糖晶）动态漂浮爆裂的场景，强调凝固的瞬间和锐利的焦点。

![巧克力曲奇的超逼真商业食物摄影](https://cms-assets.youmind.com/media/1770359907191_8c7oix_HAaOKdyacAQHkQY.jpg)
![巧克力曲奇的超逼真商业食物摄影](https://cms-assets.youmind.com/media/1770359907170_bwls49_HAaOKQKaUAAmlPx.jpg)

```
{
  "global_settings": {
    "resolution": "8K ultra-high-definition",
    "aspect_ratio": "3:4 vertical",
    "render_style": "hyper-realistic commercial food photography",
    "quality": "premium advertising grade",
    "sharpness": "extreme micro-detail, crisp edges",
    "noise": "none",
    "artifacts": "none",
    "depth_of_field": "shallow, subject-focused",
    "motion": "frozen mid-air ingredients",
    "background_style": "solid single-color studio backdrop"
  },

  "subject": {
    "main_food": "chocolate chip cookies",
    "quantity": 3,
    "appearance": [
      "golden-brown freshly baked cookies",
      "soft cracked surface",
      "visible melted chocolate chips",
      "slightly crisp edges",
      "natural handmade texture"
    ],
    "branding_rules": [
      "no text",
      "no logo",
      "no embossing",
      "no patterns",
      "no symbols"
    ]
  },

  "secondary_elements": {
    "ingredients_flying": [
      "dark chocolate chunks",
      "cookie crumbs",
      "fine sugar crystals"
    ],
    "motion_style": "dynamic floating explosion",
    "distribution": "balanced around the cookies, natural randomness",
    "particle_detail": "sharp, frozen motion with depth separation"
  },

  "composition": {
    "camera_angle": "slightly low angle",
    "framing": "center-weighted hero composition",
    "spacing": "clean negative space around subject",
    "focus_priority": "front cookie in razor-sharp focus"
  },

  "lighting": {
    "type": "professional studio lighting",
    "key_light": "soft directional key light",
    "fill_light": "gentle fill for texture clarity",
    "rim_light": "subtle rim highlight for separation",
    "shadows": "soft and natural, no harsh contrast"
  },

  "color_palette": {
    "background_color": "pastel blue",
    "cookie_tones": "warm golden browns",
    "accent_colors": "rich chocolate browns, crystal sugar whites",
    "contrast": "high subject-background separation"
  },

  "photography_style": {
    "genre": "luxury food advertising",
    "mood": "fresh, indulgent, premium",
    "cleanliness": "spotless studio look",
    "post_processing": "minimal, natural, high-end retouching"
  },

  "exclusions": [
    "text",
    "logos",
    "watermarks",
    "hands",
    "plates",
    "props",
    "packaging",
    "background objects",
    "cartoon style",
    "illustration style"
  ]
}
```

[[8K Hyperrealistic Photography]]

---

### 189. 特写海滩自拍肖像，解剖细节清晰可见

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-02-05  **Language**: en

> 一个高度明确且详细的 JSON 提示，用于生成一张在阳光明媚的海滩上拍摄的丰满女性特写自拍照。它细致地描述了拍摄对象的身体特征、服装（浅蓝色细绳比基尼）、配饰（纹身、珠宝），以及使用广角、高角度智能手机自拍，在强烈直射阳光下的技术细节。

![特写海滩自拍肖像，解剖细节清晰可见](https://cms-assets.youmind.com/media/1770359904869_wtu68k_HAaNCCGXUAMJBKL.jpg)

```
{
"subject": {
"description": "Young woman with light tan skin and long, dark, straight hair flowing over shoulders.",
"anatomy": "Voluptuous figure with extremely prominent bust volume. Breasts are full, heavy, and show clear gravity-affected weight with deep cleavage. Bust projection is significant and foreground-dominant, visibly larger than the ribcage depth. Soft tissue appears natural with subtle asymmetry. Skin texture is highly detailed with visible pores, moles, and a glistening, oily sheen suggestive of sunscreen or perspiration.",
"clothing": "Light blue string bikini top featuring an intricate orange and rust-colored paisley pattern. The top is a triangle cut with a gold metal ring connecting the cups in the center. The fit is snug, emphasizing the volume of the chest.",
"accessories": "Small gold nose stud on the left nostril. Delicate gold chain necklace with a four-leaf clover pendant. Large butterfly line-art tattoo on the inner left forearm. Script text tattoo on the right collarbone area.",
"features": "Full lips with a glossy finish, groomed arched eyebrows, dark eyelashes."
},
"pose": {
"type": "Close-up selfie portrait.",
"posture": "The subject is leaning back slightly on a beach towel. The head is tilted slightly to her right. The left arm is raised, with the hand tucked behind the head/neck, exposing the inner forearm tattoo. The right arm is extended forward out of frame, indicative of holding the camera for a selfie.",
"orientation": "Torso angled slightly towards the left, face turned forward for direct eye contact.",
"gaze": "Direct engagement with the camera lens, soft and relaxed expression."
},
"environment": {
"location": "Sunny outdoor beach setting.",
"background": "White sand visible in the immediate background. A blue and white striped towel is beneath the subject. Further back, a turquoise ocean meets a blue sky with scattered white cumulus clouds on the horizon.",
"context": "Daytime, likely summer."
},
"camera": {
"shot_type": "Close-up selfie / POV shot.",
"perspective": "High-angle perspective typical of a handheld selfie, creating slight foreshortening that emphasizes the chest and face in the foreground relative to the background.",
"focal_length": "Wide-angle lens characteristic of a smartphone front camera (approx 24mm equivalent).",
"depth_of_field": "Subject in sharp focus, background slightly softened but distinguishable."
},
"lighting": {
"source": "Bright, direct natural sunlight (high noon or early afternoon).",
"direction": "Front-left lighting.",
"quality": "Hard light creating defined shadows under the hair and chin. Strong specular highlights on the forehead, cheeks, and upper chest due to the oily/wet skin texture.",
"shadows": "Sharp, realistic shadows casting downwards."
},
"mood_and_expression": {
"mood": "Confident, alluring, relaxed, summery.",
"expression": "Soft pout with slightly parted lips, calm and engaging demeanor."
},
"s
```

[[Curvy Figure Portrait]]

---

### 190. 闪光灯下的电影感编辑双联画

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-05  **Language**: en

> 一个复杂的 JSON 提示，旨在生成一个两帧的编辑双联画（两个堆叠图像），描绘一位身着深蓝色缎面连衣裙的迷人女性躺在地板上。这个概念强调俯视视角、紧凑的相机闪光灯美学以及帧之间的连续性，其中第一帧清晰锐利，第二帧则具有刻意的运动模糊，营造出一种混乱而别致的氛围。

![闪光灯下的电影感编辑双联画](https://cms-assets.youmind.com/media/1770359917028_8xn56f_HAaLnycX0AAN5WY.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_cinematic_flash_floor_editorial_diptych",
      "priority": "highest",
      "language": "en",
      "version": "v1.0_BLUE_DRESS_FLOOR_FLASH_DIPTYCH_NO_TEXT"
    },

    "output": {
      "aspect_ratio": "3:4",
      "resolution": "ultra_high",
      "num_images": 4
    },

    "scene": {
      "concept": "A two-frame editorial diptych shot from above: a glamorous woman lying on a carpeted floor in a deep blue satin halter dress. Phone/compact-camera flash aesthetic, candid late-night energy. Frame one is sharp with a relaxed smile and eyes closed; frame two has intentional motion blur from a sudden head turn, creating a chaotic-chic vibe.",
      "environment": "neutral beige carpet floor, minimal background, a thin white edge of furniture or wall line at the top",
      "time_of_day": "night",
      "atmosphere": "flash-lit, intimate, spontaneous"
    },

    "subject": {
      "age_appearance": "adult",
      "expression_range": [
        "eyes closed, soft smile",
        "half-open eyes with playful, blurred motion"
      ],
      "pose": "lying on back with head tilted, one hand holding the neckline of the halter dress near collarbone, the other arm relaxed across torso",
      "hair": "long dark hair fanned out messily around the head, loose strands across face",
      "wardrobe": "{argument name="dress color" default="deep blue"} satin halter dress with plunging neckline, glossy fabric folds",
      "accessories": "small earrings, delicate necklace, multiple rings, manicured nails"
    },

    "shot_design": {
      "layout": "vertical diptych (two stacked frames in one image), thin border separation",
      "frame_1": "tack sharp face, eyes closed, warm smile, hair spread naturally, flash highlights controlled",
      "frame_2": "intentional motion blur from head turning, slight face smear, hand blur, still readable silhouette",
      "continuity_rules": "outfit, floor,  top-down camera position; only micro-movement between frames"
    },

    "camera": {
      "camera_body": "compact camera / smartphone",
      "lens": "wide (24-28mm equivalent)",
      "aperture": "f/1.8",
      "shutter_behavior": "frame 1 faster shutter for sharpness; frame 2 slightly slower shutter for motion blur",
      "framing": "top-down overhead, tight crop emphasizing face, neckline, and hair spread",
      "look": "flash realism, imperfect candid editorial"
    },

    "lighting": {
      "key_light": "direct on-camera flash from above",
      "fill_light": "minimal ambient room light",
      "contrast": "medium-high",
      "highlights": "specular satin highlights on dress, not blown out; natural skin sheen"
    },

    "color_grading": {
      "palette": "deep blue satin, warm skin tones, neutral beige floor",
      "film_emulation": "modern nightlife editorial realism",
      "grain": "fine digital grain",
      "halation": "minimal"
    }
```

[[Motion Blur Effect]] [[Top-Down View]]

---

### 191. 俏皮的俯视比基尼肖像提示

**Author**: [Minhaa](https://x.com/tabu_8114)  **Date**: 2026-02-05  **Language**: en

> 生成一张俯视（鸟瞰图）女性肖像的提示，描绘一位仰卧的女性，表情俏皮（眨眼并吐舌）。提示详细描述了人物的外貌特征（雀斑、波浪发）和造型（黑色露背比基尼、金色首饰），背景为柔和的浅蓝色纹理，采用自然室内照明。

![俏皮的俯视比基尼肖像提示](https://cms-assets.youmind.com/media/1770359969540_zzgjd7_HAaEbDUacAY3Nf7.jpg)
![俏皮的俯视比基尼肖像提示](https://cms-assets.youmind.com/media/1770359969625_9940e4_HAaEbMpbwAAd5pT.jpg)
![俏皮的俯视比基尼肖像提示](https://cms-assets.youmind.com/media/1770359969715_w9ml5d_HAaEbA-bAAA902e.jpg)

```
{
  "technical_specs": {
    "aspect_ratio": "2:3", 
    "camera_angle": "Overhead / High-angle (bird's-eye view)",
    "lighting_style": "Soft, natural indoor light"
  },
  "subject": {
    "demographics": {
      "type": "Woman  
      "age": 24
    },
    "pose": {
      "body": "Lying supine on back",
      "head": "Facing camera, hair spread out above head"
    },
    "physical_appearance": {
      "skin": {
        "tone": "Fair",
        "details": "Visible freckles on cheeks and nose",
        "complexion": "Flushed pink cheeks"
      },
      "eyes": {
        "color": "Brown",
        "state": "Left eye open, right eye winking"
      },
      "hair": {
        "color": "{argument name="hair color" default="brown"}",
        "texture": "Wavy"
      }
    },
    "expression": {
      "mood": "Playful",
      "mouth": {
        "action": "Sticking out tongue",
        "smile": "Broad, showing teeth"
      },
      "nose": "Wrinkled"
    }
  },
  "styling": {
    "apparel": {
      "item": "Bikini top",
      "cut": "Halter-neck",
      "color": "Black",
      "accents": "Black embroidered zig-zag trim along edges"
    },
    "accessories": [
      {
        "type": "Earrings",
        "detail": "Small gold hoops"
      },
      {
        "type": "Necklace",
        "detail": "Delicate gold chain with a small, dark charm"
      }
    ]
  },
  "environment": {
    "background_elements": [
      "Light blue textured fabric pillow",
      "Light blue textured blanket"
    ]
  }
}
```

[[Gold Jewelry]] [[Bird's Eye View Portrait]]

---

### 192. 超逼真电影感照片：男人与骏马

**Author**: [Abbey](https://x.com/Kings_Gambit__)  **Date**: 2026-02-05  **Language**: en

> 一个高度详细的提示，用于生成一张超现实的电影级照片，内容是一名强壮、健硕的男子牵着一匹异常高大、肌肉发达的马，行走在崎岖的风景中。它强调解剖学上的真实感、自然的运动物理效果（灰尘、绳索摆动）、黄金时段的光线，以及反 AI 真实感技术，以营造纪录片/社论的感觉。

![超逼真电影感照片：男人与骏马](https://cms-assets.youmind.com/media/1770359912633_nni716_HAaETAdbsAAGQlt.jpg)

```
A hyper-realistic cinematic color photograph of a powerful, athletic man walking through a wide open rugged landscape beside an exceptionally tall, powerful horse. The horse is noticeably larger than average, long-legged, heavy-boned, and imposing, with a deep chest, thick neck, broad shoulders, and clearly defined muscle structure beneath its coat. Its presence feels dominant and majestic, yet calm and controlled. The man holds a thick rope lead in his hand, the rope showing natural weight, tension, and slight sway as they walk in sync.\n\nThe man is topless, revealing a dense, naturally muscular upper body with realistic proportions: thick veiny arms, pronounced triceps and deltoids, broad shoulders, and subtle asymmetry created by real motion. Muscle compression, tendon tension, and skin stretch are visible and believable. Tattoos on the upper arm and forearm appear authentic, aged, and embedded naturally into the skin, deforming correctly with movement.\n\nHe walks forward with grounded confidence and quiet authority, posture relaxed but commanding, as if fully accustomed to handling such a powerful animal. His expression is calm, hardened, and focused, eyes looking ahead or slightly downward, never at the camera. Facial features are rugged and masculine with a strong jawline, thick uneven beard, realistic pores, fine lines, and a light sheen of sweat. Hair is dark, imperfect, and lightly disturbed by wind.\n\nThe horse walks slightly ahead or shoulder-to-shoulder with him, reinforcing its size and power. Its anatomy is accurate and lifelike, hooves kicking up dust with each step. Dust clouds rise around their legs, catching sunlight in soft golden particles. Wind moves through the scene, lifting dust, mane hair, loose rope fibers, and subtly brushing across the man’s skin, adding authentic motion.\n\nThe environment is a vast, open landscape — dry earth, rolling terrain, distant hills, sparse vegetation — grounded and real, never stylized. The color palette is cinematic but natural: warm earth tones, sunlit browns, muted greens, realistic sky blues, and gentle highlight roll-off. No oversaturation, no fantasy hues. Lighting feels like late afternoon or golden hour, directional and organic, sculpting muscle and form while preserving shadow detail.\n\nCaptured like a high-end documentary or editorial photograph using a full-frame camera with a fast prime lens. Natural depth of field, subtle motion blur in legs, dust, and rope, realistic film grain, optical imperfections, and imperfect focus falloff. The image feels candid, powerful, and timeless — not posed, not staged.\n\nAnti-AI realism emphasis: believable scale difference, real anatomy, authentic motion physics, natural dust behavior, organic color grading, imperfect lighting, realistic skin and hair texture.",
  "negative_prompt": "AI-generated look, CGI animals, fantasy horse, exaggera
```

[[Man with Stallion Cinematic Photo]]

---

### 193. 黄金时段奢华 Vlog 人像，超丰盈解剖结构

**Author**: [Maya](https://x.com/mayadelmare)  **Date**: 2026-02-05  **Language**: en

> 一个极其详细的超写实提示词，用于生成一张高端生活方式视频博主在豪华水上别墅黄金时段的半身照。该提示词非常注重解剖学真实感，包括超丰满的曲线、逼真的皮肤纹理（妊娠纹、毛孔、油光），以及特定的光照条件（温暖、有方向性的黄金时段光线），以突出拍摄对象的身材和高端环境。

![黄金时段奢华 Vlog 人像，超丰盈解剖结构](https://cms-assets.youmind.com/media/1770359916724_92s02r_HAaEBO8WMAIjWkQ.jpg)

```
{
  "subject": {
    "demographics": "Mid-20s woman, high-end lifestyle vlogger with an affluent aesthetic.",
    "hair": "Wavy ombre hair, transitioning from deep brunette at the roots to sun-kissed blonde at the ends, cascading over the shoulders.",
    "face": "Light natural makeup, radiant skin with visible pores, soft catchlights in the eyes, genuine engaging expression directed at a vlog camera.",
    "anatomy": "Fit, highly defined hourglass figure. Extremely narrow waist contrasting with significantly wider, voluptuous hips. Features a large, heavy natural bust exhibiting realistic gravity-dependent shape and soft tissue mass. Lower body defined by significantly enlarged, hyper-voluminous glutes with a deep curve and firm, rounded projection. Skin texture includes realistic striae on the outer thighs and hips, subtle skin oiliness from the tropical humidity, and natural skin folds at the waist transition. Toned, athletic thighs tapering into slender knees; slender arms with realistic muscle tone and visible fine veins.",
    "attire": "{argument name="clothing material" default="Champagne-colored silk"} robe with a subtle crinkle-fabric texture, draped loosely to emphasize the anatomical curves while maintaining a high-end aesthetic.",
    "accessories": "Compact professional vlog camera held in one hand; a high-clarity crystal glass containing detox water with citrus slices in the other. Luxury skincare bottles in frosted glass and gold accents arranged on a nearby surface."
  },
  "pose": {
    "type": "Candid vlog interaction",
    "details": "Seated at the edge of an infinity pool, torso slightly rotated toward the camera to accentuate the waist-to-hip ratio. One arm extended for the 'vlog' angle, the other resting the glass near the lap."
  },
  "environment": {
    "location": "Luxury overwater villa in the {argument name="location" default="Maldives"} during golden hour.",
    "elements": "Infinity pool edge merging with the turquoise ocean, teak wood decking, marble-topped side table, clear horizon line, soft ripples in the water."
  },
  "camera": {
    "shot_type": "Medium shot",
    "focal_length": "50mm to 85mm (Portrait lens preference for flattening features and volume preservation)",
    "perspective": "Neutral focal length to maintain anatomical accuracy without wide-angle distortion, mimicking a high-end iPhone capture."
  },
  "lighting": {
    "source": "Natural golden hour sunlight",
    "quality": "Warm, directional light creating soft highlights on the silk fabric and emphasizing the three-dimensional volume of the soft tissue mass."
  },
  "mood_and_expression": {
    "atmosphere": "Sophisticated, serene, and aspirational.",
    "expression": "Warm, communicative, and spontaneous."
  },
  "style_and_realism": {
    "fidelity": "Unfiltered texture, visible skin grain, stretch marks on curves, wet skin from the pool mist, real iPhone photo aesthetic with no digital smoothing."
  },
  "colors_and_tone": {
    "palette": "C
```

[[High-End Lifestyle Photography]]

---

### 194. 复古美式风格肖像，搭配老式电话和传单

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-02-05  **Language**: en

> 一个结构化提示，用于生成一张具有复古美式风格的肖像，背景设定在干旱的沙漠景观中。主体是一位金发女性，身穿格子迷你连衣裙和牛仔靴，斜倚在一根电线杆旁，手持一部复古“砖头”手机。一个关键元素是电线杆上贴着一张传单，上面写着：“想扎心吗？给你前任打电话！”

![复古美式风格肖像，搭配老式电话和传单](https://cms-assets.youmind.com/media/1770359907609_cee1qz_HAZ_O5pXkAAWz0N.jpg)
![复古美式风格肖像，搭配老式电话和传单](https://cms-assets.youmind.com/media/1770359907594_lpe9rh_HAZ_O5VWEAAGOEl.jpg)
![复古美式风格肖像，搭配老式电话和传单](https://cms-assets.youmind.com/media/1770359907924_3lh4lo_HAZ_O4JWgAAnkgr.jpg)

```
{
  "prompt_structure": {
    "subject": {
      "description": "Young woman with long, wavy blonde hair styled loosely around her face.",
      "pose": "Leaning back against a weathered wooden utility pole, one leg slightly bent. She is holding a large, vintage black 'brick' style cell phone to her ear with her left hand, while touching her hair with her right hand.",
      "expression": "Direct eye contact, soft pouty expression, calm and alluring."
    },
    "apparel": {
      "dress": "Red and white gingham (checkered) mini dress. It features a button-down front and intricate white scalloped lace trim along the hemline and neckline.",
      "footwear": "Classic brown leather cowboy boots."
    },
    "key_elements": {
      "flyer": "A white paper flyer is taped to the utility pole at eye level. It features red and black text that clearly reads: '{argument name="flyer text" default="WANNA TWIST THE KNIFE? CALL YOUR EX!"}'. The flyer has vertical tear-off tabs at the bottom.",
      "prop": "Retro 1980s oversized brick mobile phone with a visible antenna."
    },
    "setting": {
      "location": "Arid desert landscape with dry dirt ground and sparse scrub brush vegetation.",
      "background": "Distant mountains and a wide, open horizon under a clear sky. A glimpse of a house or structure is visible in the far right distance.",
      "lighting": "Bright, harsh natural sunlight indicating midday, casting strong shadows from the pole and subject."
    },
    "technical_style": {
      "quality": "4k, HD, 8k resolution, highly detailed, photorealistic textures.",
      "aesthetic": "Vintage Americana, cinematic film look, analog photography style, soft film grain, warm color grading.",
      "camera": "Medium shot, sharp focus on the subject with a shallow depth of field slightly blurring the desert background."
    }
  }
}
```

[[Blonde Hair Portrait]]

---

### 195. 三人健身房镜子自拍提示

**Author**: [Rowan](https://x.com/rowanali09)  **Date**: 2026-02-05  **Language**: en

> 生成一张逼真的团体镜面自拍的提示，画面中有三位年轻女性在健身房里，她们酷似 Billie、Sabrina 和 Olivia 等名人。提示详细描述了每位人物的服装、发型和姿势，并指定了明亮、冷色调的健身房灯光以及背景元素，如举重架，旨在营造一种 candid、健身风格的美感。

![三人健身房镜子自拍提示](https://cms-assets.youmind.com/media/1770359968065_v0obpw_HAZ842racAQm_A8.jpg)

```
{
  "prompt": {
    "type": "photorealistic_image",
    "scene_description": "A vertical mirror selfie featuring three young women standing closely together in a gym setting.",
    "subjects": [
      {
        "position": "left",
        "description": "A woman with pale skin and dark hair styled in a messy high bun with loose strands framing her face.",
        "outfit": {
          "top": "Charcoal grey low-cut sports bra",
          "bottom": "Matching charcoal grey tight compression shorts"
        },
        "pose": "Holding a smartphone in her right hand to take the photo, leaning her head slightly toward the center, smiling softly with a relaxed expression.",
        "accessories": "Rings visible on fingers"
      },
      {
        "position": "center",
        "description": "A woman with blonde hair pulled back, featuring prominent curtain bangs.",
        "outfit": {
          "top": "Beige/nude triangle-style bikini sports top",
          "bottom": "Matching beige tight shorts"
        },
        "pose": "Standing between the other two women, looking directly at the phone's reflection, displaying a subtle smile.",
        "physical_details": "Toned midriff visible"
      },
      {
        "position": "right",
        "description": "A woman with light olive skin and long dark brown hair pulled back into a ponytail.",
        "outfit": {
          "top": "Olive green sports bra",
          "bottom": "Matching olive green tight shorts"
        },
        "pose": "Leaning in from the right side, resting her head near the center subject, smiling warmly."
      }
    ],
    "environment": {
      "setting": "Gym interior",
      "lighting": "Bright, cool-toned artificial gym lighting",
      "background_elements": [
        "Large wall-to-wall mirror reflecting the subjects",
        "Dumbbell rack filled with weights on the left",
        "Black power rack/squat cage structure on the right",
        "Gym flooring",
        "Partial view of a weight bench"
      ]
    },
    "style": {
      "aesthetic": "Candid, celebrity-style workout selfie",
      "quality": "High-resolution, sharp focus on faces",
      "mood": "Casual, friendly, fitness-oriented"
    }
  }
}
```

[[Celebrity Trio Portrait]]

---

### 196. 夜间屋顶露台派对人像提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-02-05  **Language**: en

> 在夜间屋顶露台派对上，生成一张高分辨率、电影感的肖像照，主体人物的脸部结构需与上传的参考图完全一致。指定服装，营造柔和的粉蓝色氛围，并使用暖色调主光，以展现丰富、自信的度假心情。

![夜间屋顶露台派对人像提示](https://cms-assets.youmind.com/media/1770359953933_o3x5er_HAZ7LcOacAA7BF0.jpg)

```
Nighttime roof-terrace party photo. Subject relaxed, slight side profile but looking at the camera playfully, holding a {argument name="drink brand" default="Monster"} can in right hand, left elbow resting on railing. 

Keep uploaded face exactly the same: same structure, proportions, natural skin texture, slight under-eye shadows, fair glass-skin look. Hair messy with volume/flyaways, no changes to reference.

Outfit: white linen baggy shirt slightly open at chest, black baggy jeans, thin silver chain with heart shape pendant". Environment: luxury ocean-height terrace, old-money vibe, soft pink/blue party ambience, warm yellow glow near face, subtle glass-railing reflections, distant silhouettes.

Lighting: cinematic pink/blue ambience + warm key light, soft shadows, smartphone night photo, no HDR. Mood: calm, elegant, rich-vacation, confident. Eye-level camera, slight tilt, handheld, no background blur, high resolution image.
```

[[Face Reference Matching]]

---

### 197. 6 格汽车自拍联系表，带手机闪光灯

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-05  **Language**: en

> 一个复杂的 JSON 提示，旨在生成一个包含 6 帧垂直汽车自拍拼贴画的联系表。它指定了一位穿着鲜红色紧身胸衣上衣的棕发女子，在夜晚用手机闪光灯拍摄，强调手持拍摄的自发性、细微的运动模糊，以及六帧中姿势和表情的变化。

![6 格汽车自拍联系表，带手机闪光灯](https://cms-assets.youmind.com/media/1770359909784_4ot7he_HAZ5NAYXwAAjT4m.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_cinematic_phone_flash_selfie_contact_sheet",
      "priority": "highest",
      "language": "en",
      "version": "v1.0_CAR_SELFIE_RED_CORSET_6UP_NO_TEXT"
    },

    "output": {
      "aspect_ratio": "9:16",
      "resolution": "ultra_high",
      "num_images": 4
    },

    "scene": {
      "concept": "A 6-frame vertical contact sheet collage of car selfies shot with a phone flash at night. A brunette woman wears a vivid {argument name="top color" default="red"} corset-style top with off-shoulder straps. Cream leather car interior, soft motion blur from handheld shooting, glamorous but casual nightlife vibe.",
      "environment": "inside a car with cream leather seats and light headliner, night outside, minimal background clutter",
      "time_of_day": "night",
      "atmosphere": "flash-lit, slightly hazy, handheld spontaneity"
    },

    "subject": {
      "age_appearance": "adult",
      "expression_range": [
        "soft pout",
        "neutral gaze",
        "eyes down",
        "subtle smile",
        "confident smirk"
      ],
      "hair": "long brunette hair with soft volume, loose waves, slightly messy from movement",
      "makeup": "soft glam, warm blush, glossy lips, defined eyeliner, natural skin texture",
      "wardrobe": {
        "top": "bright red corset-style top with structured seams and subtle ruffle trim at neckline, off-shoulder straps",
        "bottom": "light blue denim jeans visible in some frames"
      },
      "accessories": "gold bracelet and rings, minimal earrings"
    },

    "shot_design": {
      "layout": "2 columns x 3 rows collage (six frames in one image), thin borders between frames, consistent spacing",
      "frame_variations": [
        "top-left: high-angle selfie, head tilted, direct gaze",
        "top-right: chest-up portrait, centered, confident gaze",
        "middle-left: high-angle selfie, eyes lowered, soft expression",
        "middle-right: slight motion blur, smiling, candid energy",
        "bottom-left: high-angle selfie, closer crop, direct gaze",
        "bottom-right: wider shot showing more of the seat and interior, relaxed pose"
      ],
      "continuity_rules": "same outfit and interior across all frames, subtle pose and expression changes only"
    },

    "camera": {
      "camera_body": "smartphone camera",
      "lens": "wide (24mm equivalent)",
      "aperture": "f/1.8",
      "focus": "sharp on face, occasional mild motion blur from handheld movement",
      "look": "phone flash realism, slight lens distortion, natural imperfections"
    },

    "lighting": {
      "key_light": "on-camera phone flash, soft but direct",
      "fill_light": "car interior bounce from cream leather",
      "contrast": "medium-high",
      "highlights": "controlled specular highlights on lips and hair, not blown out"
    },

    "color_grading": {
      "palette": "vivid red top, warm "
    }
  }
}
```

[[Night Flash Photography]]

---

### 198. Coquette 美学舒适肖像提示

**Author**: [Nobara](https://x.com/Nobarakia)  **Date**: 2026-02-05  **Language**: en

> 一个用于生成超逼真、亲密肖像的提示，具有“风情万种”或冬季美学。它着重于一位皮肤白皙、深色头发的主体，身穿罗纹背心和格子裙，佩戴着一顶大号人造毛乌尚卡帽，置身于一个拥有温暖、柔和灯光的舒适卧室中。

![Coquette 美学舒适肖像提示](https://cms-assets.youmind.com/media/1770359966885_r7u3wa_HAZ2-4xW4AA49kl.jpg)

```
{
  "subject": {
    "appearance": "Young woman with pale, porcelain skin, subtle freckles across the nose and cheeks, piercing light blue eyes, and long dark brown hair with soft waves. Natural makeup look with soft pink lips.",
    "pose": "Sitting upright, arms raised with hands gently touching the sides of a fur hat, direct gaze toward the camera with a neutral, calm expression.",
    "clothing": "Cream-colored ribbed spaghetti strap tank top, tucked into a dark blue and white plaid/tartan pleated skirt.",
    "styling": "Large, voluminous black faux-fur ushanka-style hat; accessorized with multiple gold and silver delicate chain bracelets on both wrists including a clover motif."
  },
  "environment": {
    "setting": "Cozy bedroom interior; soft white bedding/blankets in the background; a decorative wall feature with green ivy vines draped over a white surface.",
    "lighting": "Warm, diffused indoor lighting; soft highlights on the collarbones and shoulders; gentle catchlights in the eyes; minimal harsh shadows.",
    "mood": "Intimate, cozy, soft, and trendy (coquette/winter aesthetic)."
  },
  "technical_specifications": {
    "camera_details": "Shot on 35mm lens, f/2.8 aperture for shallow depth of field, ISO 200, sharp focus on facial features with soft background blur (bokeh).",
    "image_quality": "Ultra photorealistic, 8k resolution, high dynamic range (HDR), detailed skin texture, hyper-realistic fabric weaving, cinematic color grading."
  }
}
```

[[Coquette Winter Bedroom Portrait]]

---

### 199. 超逼真商业饮品摄影

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-02-05  **Language**: en

> 一个高度详细、模块化的提示词，用于生成一张 8K 超逼真商业摄影作品，内容为一杯高脚杯中的饮品（冰咖啡或蛋白奶昔）。它着重于凝固动态、详细描绘液体飞溅、冷凝水珠、漂浮元素（冰块、咖啡豆）以及电影级的影棚布光，以营造奢华、高端的咖啡馆氛围。

![超逼真商业饮品摄影](https://cms-assets.youmind.com/media/1770359927607_iro6j9_HAZ2JKRbAAAAR1w.jpg)
![超逼真商业饮品摄影](https://cms-assets.youmind.com/media/1770359928130_8qcqos_HAZ2I8lacAAk_xf.jpg)
![超逼真商业饮品摄影](https://cms-assets.youmind.com/media/1770359928689_kve5by_HAZ2Jp_aMAEvpbq.jpg)
![超逼真商业饮品摄影](https://cms-assets.youmind.com/media/1770359928950_ptkahz_HAZ2JoAb0AApFs5.jpg)

```
{
  "master_prompt": {
    "global_settings": {
      "resolution": "8K ultra-high-definition",
      "aspect_ratio": "3:4 vertical",
      "style": "hyper-realistic AI-edited commercial beverage photography",
      "sharpness": "extreme clarity, micro-detail visibility",
      "lighting_quality": "cinematic studio lighting with controlled highlights and shadows",
      "motion_freeze": "high-speed capture, frozen liquid splashes and particles",
      "noise": "none",
      "artifacts": "none"
    },

    "module_1_glass_beverage_style": {
      "subject": {
        "type": "transparent glass",
        "glass_style": "tall cylindrical glass with thick base",
        "surface_details": "cold condensation droplets on outer glass surface",
        "fill_level": "80 percent full",
        "label_text_visible": [
          "mock up",
          "iced coffee / protein shake",
          "SEPARATED SHADOWS"
        ]
      },

      "liquid_and_layers": {
        "beverage_type": "{argument name="beverage type" default="iced latte or chocolate protein shake"}",
        "liquid_color": "rich coffee brown or creamy cocoa",
        "layering": "soft milk-to-coffee gradient with subtle swirls",
        "texture": "smooth, thick, glossy, realistic viscosity"
      },

      "motion_and_splash": {
        "action": "liquid splash erupting from inside the glass",
        "splash_behavior": "curved arcs rising above rim with suspended droplets",
        "droplet_detail": "micro droplets frozen mid-air with sharp definition"
      },

      "floating_elements": {
        "ice_cubes": "large clear ice cubes rotating in mid-air",
        "coffee_beans_or_cocoa": "roasted coffee beans or cocoa powder particles floating",
        "cream_stream": "thin stream of milk or cream pouring into glass"
      },

      "pose_and_camera": {
        "position": "centered hero composition",
        "angle": "three-quarter close-up",
        "camera_feel": "slightly low angle for premium, powerful presence"
      },

      "background": {
        "color_palette": "deep espresso brown fading into warm beige highlights",
        "bokeh": "soft cinematic bokeh lights with warm glow",
        "atmosphere": "luxurious, indulgent, high-end café mood"
      },

      "surface_and_reflection": {
        "base": "wet reflective surface with subtle liquid pooling",
        "shadow_style": "clean, soft separated shadow beneath glass",
        "reflection_quality": "controlled highlights along glass edges"
      }
    }
  }
}
```

[[Floating Ingredients]] [[Cinematic Studio Lighting]] [[Commercial Beverage Photography]] [[Dynamic Splash Effect]]

---

### 200. 豪华休息室里的超逼真肖像

**Author**: [TJ](https://x.com/TAB_TAB_HH)  **Date**: 2026-02-05  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真的年轻女性肖像，她坐在一间豪华休息室里。提示详细描述了她的外貌（长波浪发、黑色迷你连衣裙、几何纹身）、私密的场景设置（热带香蕉叶壁画、背光置物架）以及电影般的暖色环境照明，以呈现一张精致、高保真的图像。

![豪华休息室里的超逼真肖像](https://cms-assets.youmind.com/media/1770359908252_a8n13r_HAZ0oY2XgAAX8dT.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "A stunning young woman with long, voluminous, wavy light brown hair styled in a side part. She has a fair complexion and soft, glamorous makeup with defined lips.",
      "apparel": "She is wearing a chic, strapless black mini dress with a textured or ruched bodice. A gold wristwatch with a white face and a gold chain bracelet adorn her left wrist. A visible black geometric tattoo is on her right forearm.",
      "pose": "Seated elegantly in a dark wood chair with a woven cane backrest. Her body is angled slightly to the right, with one hand resting on the chair arm and the other on her lap. She is looking directly at the camera with a confident, calm expression."
    },
    "environment": {
      "setting": "A dimly lit, upscale lounge or restaurant interior.",
      "background_elements": "Behind her is a dark wall featuring a large, artistic mural of tropical banana leaves. To the left, a backlit shelving unit displays glass bottles and decorative items, adding depth and bokeh."
    },
    "lighting_and_atmosphere": {
      "type": "Soft, warm ambient indoor lighting mixed with cinematic accent lighting.",
      "mood": "Sophisticated, intimate, luxurious, and relaxed."
    },
    "technical_specifications": {
      "quality_tags": "Ultra realistic, HDR, UHD, 8k resolution, highly detailed, photorealistic, masterpiece, raw photo, best quality, high fidelity.",
      "camera_style": "Portrait photography, depth of field, sharp focus on subject, soft bokeh background.",
      "aspect_ratio": "9:16 (Vertical/Long)",
      "resolution": "2160x3840"
    },
    "full_combined_prompt": "Ultra realistic portrait of a stunning young woman sitting in a cane-back chair in a luxury lounge, wearing a strapless black mini dress, long wavy light brown hair, gold wristwatch, geometric forearm tattoo, soft glam makeup, background features a tropical leaf mural and backlit shelves with bottles, warm ambient lighting, cinematic depth of field, HDR, UHD, 8k resolution, high detail, 9:16 vertical aspect ratio.",
    "negative_prompt": "cartoon, illustration, anime, drawing, low quality, pixelated, blurry, noise, grain, distorted hands, extra fingers, missing limbs, bad anatomy, overexposed, underexposed, watermark, text."
  }
}
```

[[Black Mini Dress Fashion]]

---

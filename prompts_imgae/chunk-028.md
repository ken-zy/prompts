# Chunk 028

Total: 200 prompts

### 1. 森林溪流中的电影级写实肖像（宝嘉康蒂风格）

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-28  **Language**: en

> 一个极其详细的 JSON 提示，用于生成一张超逼真、电影级的女性全身肖像，置身于森林溪流中，灵感来源于自然、历史美学。它包含大量的元数据、对照片真实感的严格限制，以及对环境、光线、服装和主体外观的详细规格，强调自然纹理和电影般的质感。

![森林溪流中的电影级写实肖像（宝嘉康蒂风格）](https://cms-assets.youmind.com/media/1769668486193_h1ws6z_G_x4F6WWMAArhd3.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_cinematic_outdoor_forest_stream_editorial",
      "version": "v1.1_RIVER_POCAHONTAS_INSPIRED_FRINGE_DRESS_REAL_FILM_STILL_NO_TEXT_NO_AI",
      "priority": "highest"
    },

    "references": {
      "reference_image_1": {
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

    "output_settings": {
      "aspect_ratio": "2:3",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "cinematic_film_still_photoreal",
      "sharpness": "natural_crisp_subject",
      "film_grain": "subtle_35mm",
      "color_grade": "warm_green_amber_film",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },

    "creative_prompt": {
      "scene_summary": "Ultra-photorealistic cinematic full-body portrait of a young woman standing barefoot in a shallow forest stream among dark wet rocks. She wears a {argument name="dress material" default="tan suede"}-inspired asymmetrical one-shoulder dress with realistic fringe trim and natural stitchwork, fitted at the waist with a simple leather band. She has very long straight jet-black hair and a {argument name="accessory detail" default="turquoise bead necklace with a small white shell pendant"}. The moment feels like a high-budget live-action film still: calm, strong, and grounded in nature. No modern objects, no city elements.",

      "environment": {
        "location": "rocky forest creek / stream",
        "time": "late afternoon (golden light filtered through trees)",
        "background": "mossy rocks, soft greenery, shallow moving water, natural bokeh",
        "atmosphere": "fresh, humid, cinematic, slight haze"
      },

      "subject": {
        "appearance": {
          "hair": "very long straight black hair, smooth shine, realistic strands",
          "makeup": "minimal natural makeup, realistic pores, subtle highlight",
          "skin": "warm medium-brown tone, true-to-life texture, no retouch"
        },
        "wardrobe": {
          "dress": "tan suede/leather-look one-shoulder dress, fringe along neckline and hem, natural folds, realistic wet-edge where fabric nears water, modest coverage",
          "waist": "simple brown leather belt/band, no modern metal buckle"
        },
        "accessories": {
          "necklace": "turquoise bead necklace with small white shell pendant, realistic bead reflections"
        },
        "pose": "standing in ankle-deep water, relaxed arms slightly out from body, chin slightly raised, eyes softly closed or looking down, serene expression",
        "anatomy_constraints": "correct full-body proportions, natura"
    }
  }
}
```

[[Structured JSON Prompt]]

---

### 2. 俯视俏皮肖像（金发版）

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-01-28  **Language**: en

> 一个简洁的 JSON 提示，用于生成一张女性（Elizabeth Elson/Sadie Sink）仰卧的俯视趣味肖像。它详细描述了表情（眨眼、吐舌、皱鼻）、身体特征（雀斑、散开的金色波浪发）和服装（白色露背比基尼上衣），置于柔和的室内灯光下。

![俯视俏皮肖像（金发版）](https://cms-assets.youmind.com/media/1769668501155_hsm9z1_G_xBdAGXMAEK-wA.jpg)
![俯视俏皮肖像（金发版）](https://cms-assets.youmind.com/media/1769668501429_rsh9un_G_xBdADXwAA6DTe.jpg)

```
{
  "aspect_ratio": "2:3",
  "subject": {
    "type": "Woman",
    "age": 19,
    "position": "Lying on back, overhead view"
  },
  "expression": {
    "action": "Winking right eye, sticking out tongue",
    "smile": "Broad, showing teeth",
    "nose": "Wrinkled"
  },
  "features": {
    "skin_tone": "Fair with visible freckles on cheeks and nose",
    "cheeks": "Flushed pink",
    "lips": "Natural pink, tongue extended",
    "eyes": "Left brown eye open, right winking",
    "hair": "{argument name="hair color" default="Blonde"}, wavy, spread out above head"
  },
  "attire": {
    "bikini_top": "{argument name="bikini color" default="White"} halter-neck with black embroidered zig-zag trim along edges"
  },
  "accessories": {
    "earrings": "Small gold hoop earrings",
    "necklace": "Delicate gold chain with a small, dark charm"
  },
  "environment": {
    "background": "Light blue textured fabric pillow and blanket",
    "lighting": "Soft, natural indoor light"
  }
}
```

[[Structured JSON Prompt]] [[Winking Expression]] [[Bird's Eye View Portrait]] [[Overhead Playful Bikini Portrait]]

---

### 3. 阿马尔菲海岸上的电影感 Sadie Sink 肖像

**Author**: [unforgettwble](https://x.com/xbella_bee)  **Date**: 2026-01-28  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张 8K 超逼真电影级肖像，描绘了萨迪·辛克（Sadie Sink）在俯瞰阿马尔菲海岸（Amalfi Coast）的沿海露台上。它详细说明了姿势（扭曲的躯干，回望肩膀）、服装（深炭色丝绸吊带背心和长裤）、强烈的地中海阳光，以及技术细节（35mm 镜头，面部清晰对焦，自然皮肤纹理）。

![阿马尔菲海岸上的电影感 Sadie Sink 肖像](https://cms-assets.youmind.com/media/1769668495841_yukl46_G_w6c41XUAEFbrC.jpg)

```
{
  "image_generation_data": {
    "title": "Luxury Mediterranean Summer Aesthetic – Sadie Sink (Elevated Sensual Edit)",
    "style_preset": "Cinematic Realism / Sunlight",
    "aspect_ratio": "9:16",
    "subject": {
      "appearance": "Hyper-realistic portrait of {argument name="celebrity name" default="Sadie Sink"}, slender yet graceful build, fair skin with a subtle freckled glow, expressive blue eyes, soft facial features. Fiery red hair styled in loose, slightly tousled waves with a natural sunlit sheen.",
      "pose_lock": "Sitting relaxed on a stone ledge, body angled slightly sideways to emphasize natural curves, torso subtly twisted, head sharply turned over the shoulder looking directly at the camera.",
      "expression": "Soft confident smile with a hint of flirtation, lips gently parted, eyes slightly squinted from bright Mediterranean sunlight, sensual yet effortless."
    },
    "attire_details": {
      "upper_body": "Silk camisole in deep {argument name="attire color" default="charcoal grey"}, ultra-fine fabric with soft sheen, delicate thin straps, slightly draped neckline subtly revealing collarbone and décolletage.",
      "lower_body": "High-waisted wide-leg trousers in matching dark grey tone, tailored to accentuate waist and hip line with elegant flow.",
      "accessories": "Structured espresso-brown leather shoulder bag resting against the hip, medium gold hoop earrings, thin gold bracelet and ring, minimal but luxurious."
    },
    "environment_lock": {
      "location": "Coastal terrace overlooking the Mediterranean Sea, Amalfi Coast.",
      "foreground": "Ancient stone wall with hanging green ivy brushing lightly against her arm.",
      "background": "Crystal clear blue ocean, distant colorful coastal houses softened by atmospheric depth, vivid blue sky.",
      "lighting": "Strong natural Mediterranean morning sunlight creating warm highlights on skin, subtle chiaroscuro shaping cheekbones and shoulders, realistic sun squint and glow."
    },
    "technical_specs": {
      "camera": "Eye-level medium shot, 35mm lens for natural perspective.",
      "quality": "8K UHD, ultra-high fidelity, visible natural skin texture, fine freckles, realistic fabric drape, cinematic color grading.",
      "full_prompt": "Hyper-realistic cinematic portrait of Sadie Sink sitting on a stone ledge overlooking the Amalfi Coast, body slightly twisted to accentuate natural curves, head turned over the shoulder. She looks into the camera with a soft, confident, subtly seductive smile, lips gently parted, eyes squinting in bright Mediterranean sun. Fiery red hair glowing naturally. Wearing a deep charcoal grey silk camisole with delicate straps and a softly draped neckline, paired with matching high-waisted wide-leg trousers, accessorized with gold jewelry and an espresso-brown leather bag. Strong natural Mediterranean morning sunlight, crystal blue ocean, ancient stone walls with ivy, cinematic realism, 35mm lens, sharp facial focus, ultra-detailed natural skin texture, "
    }
  }
}
```

[[Structured JSON Prompt]] [[8K Portrait]]

---

### 4. 艺术工作室中，粉色颜料下的超写实生活肖像

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-28  **Language**: en

> 一个用于在艺术工作室环境中生成超逼真电影肖像的详细 JSON 提示。场景聚焦于一名躺在地板上的女性，她将画笔伸向镜头。关键细节包括粉色缎面吊带裙、手和脸上沾染的粉色颜料污迹、特定的相机设置（35mm 定焦镜头，f/1.8），以及柔和温暖的粉色调色板。

![艺术工作室中，粉色颜料下的超写实生活肖像](https://cms-assets.youmind.com/media/1769668493541_2dzinw_G_w28vGXUAsDLX2.jpg)
![艺术工作室中，粉色颜料下的超写实生活肖像](https://cms-assets.youmind.com/media/1769668493551_pr62jq_G_w28vDWkAAY7AX.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_lifestyle_art_studio_portrait",
      "version": "v1.0_PINK_SATIN_SLIP_DRESS_PINK_PAINT_BRUSH_CLOSEUP_NO_TEXT_EN",
      "priority": "highest",
      "language": "en"
    },
    "references": {
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (OPTIONAL)",
        "purpose": "POSE_COMPOSITION_CAMERA_DISTANCE_ANCHOR",
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
      "render_style": "ultra_photoreal_cinematic_film_still",
      "sharpness": "crisp_but_natural",
      "film_grain": "very_subtle_35mm",
      "dynamic_range": "natural_filmic_not_hdr",
      "color_grade": "soft_warm_interior_with_pink_palette",
      "skin_rendering": "natural_skin_texture_no_beautify",
      "lens_and_camera": {
        "camera": "Sony_A7SIII_or_equivalent",
        "lens": "35mm_prime",
        "aperture": "f1.8",
        "focus_style": "foreground_object_sharp_face_soft_bokeh"
      },
      "lighting": {
        "key": "soft_window_daylight",
        "fill": "gentle_room_bounce",
        "mood": "playful_artsy_intimate"
      },
      "background": {
        "environment": "cozy_minimal_art_room_wood_floor",
        "decor": "simple_shelves_plants_canvas_in_background",
        "cleanliness": "slightly_artsy_but_not_messy"
      }
    },
    "scene": {
      "global_description": "A photoreal lifestyle portrait in a cozy art room. A young adult woman lies on a wooden floor, reaching toward the camera with a paintbrush very close to the lens. Her hand and brush have paint smudges in harmonious {argument name="paint color" default="pink"} tones (blush pink, rose, magenta, soft coral). She wears a pink satin spaghetti-strap slip dress with realistic satin sheen and folds. The mood is playful, warm, and creative, with shallow depth of field focusing on the brush and paint-covered hand while her face is softly blurred but still recognizable.",
      "subject_details": {
        "woman": {
          "wardrobe": "pink satin slip dress, spaghetti straps, tasteful fit, realistic satin reflections",
          "hair_makeup": "natural makeup, soft glossy lips, clean skin texture, long hair styled naturally",
          "pose": "lying forward on the floor, one arm extended holding the brush toward the lens, smiling gently"
        },
        "paint": {
          "palette": "all pink family only: blush pink, dusty rose, magenta accents, soft coral, pastel pink",
          "placement": "paint smears on fingers and palm, small paint marks on cheek and chin, paint residue on brush handle and bristles",
          "extra": "a few small pink paint drops on the floor near her hand (subtle)"
        }
      }
    }
  }
}
```

[[Structured JSON Prompt]] [[Floor Pose]]

---

### 5. 俯视俏皮肖像（棕发版）

**Author**: [unforgettwble](https://x.com/xbella_bee)  **Date**: 2026-01-28  **Language**: en

> 一个结构化的 JSON 提示词，与 Ana de Armas 提示词（2016660146760643018）高度相似，用于生成一张从上方视角拍摄的女性图像，她表情俏皮（眨眼、吐舌）。此版本指定了棕色头发和黑色比基尼上衣，并详细描述了姿势、配饰和柔和的室内照明。

![俯视俏皮肖像（棕发版）](https://cms-assets.youmind.com/media/1769668496747_a9qcrz_G_wX4fCbwAAZQ3X.jpg)
![俯视俏皮肖像（棕发版）](https://cms-assets.youmind.com/media/1769668496731_sg1ppx_G_wX4fNboAA-OEJ.jpg)

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
      "color": "{argument name="bikini color" default="Black"}",
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

[[Structured JSON Prompt]] [[Winking Expression]] [[Bird's Eye View Portrait]] [[Overhead Playful Bikini Portrait]]

---

### 6. 超逼真池畔泳装图像生成提示

**Author**: [cinema 🎥](https://x.com/FilmHub00)  **Date**: 2026-01-28  **Language**: en

> 一个详细的 JSON 提示，用于使用 Gemini Nano Banana Pro 模型生成一张逼真的、高分辨率的女性（Sydney Sweeney）在泳池环境中的图像。该提示细致地定义了拍摄对象的样貌、姿势（倚靠在泳池甲板上）和服装——一件高光泽、双色调的皇家粉和泡泡糖蓝竞技泳衣。它还指定了热带度假村环境、明亮的高调自然光照和强烈的镜面高光，以及 3:4 宽高比的中景全身镜头。

![超逼真池畔泳装图像生成提示](https://cms-assets.youmind.com/media/1769668503699_17e44a_G_v9oNUXcAAKn4f.jpg)

```
{
  "subject_and_pose": {
    "description": "A photorealistic, highly detailed image of a young woman with shoulder-length blonde hair featuring soft bangs. She has fair skin with a noticeable glossy, wet sheen, suggesting recent swimming activity. Her facial expression is calm and engaging, looking directly at the camera.",
    "pose": "She is in the swimming pool, leaning slightly forward with her right hand resting flat on the pool deck for support and her left arm relaxed by her side. Her posture is poised and highlights an athletic full hourglass figure."
  },
  "outfit": {
    "description": "She is wearing a tight, glossy one-piece competitive swimsuit.",
    "details": "The swimsuit is two-toned, featuring a deep {argument name="swimsuit color 1" default="royal pink"} center panel and vibrant {argument name="swimsuit color 2" default="bubblegum blue"} side panels that contour the body. The material has a high-shine, latex-like or wet lycra finish. A small pink logo is visible on the upper chest."
  },
  "environment": {
    "setting": "An upscale outdoor resort pool area on a sunny day.",
    "background": "The immediate background features the sparkling blue water of the swimming pool with blue mosaic tiles visible beneath the surface. Further back, there is a poolside patio with white lounge chairs, lush green hedges, palm trees, and a villa-style structure with a wooden pergola roof, evoking a tropical summer atmosphere."
  },
  "lighting_and_shot": {
    "lighting": "Bright, high-key natural sunlight. Strong specular highlights are present on the subject's wet skin and the glossy swimsuit, enhancing the texture and realism. The lighting creates defined but soft shadows, typical of a midday sun.",
    "camera_shot": "Medium-full shot, capturing the subject from the knees up. The angle is slightly elevated, looking down at the subject against the backdrop of the pool. The image is sharp and high-resolution with a shallow depth of field that keeps the subject in crisp focus while slightly blurring the background elements. Aspect Ratio {argument name="aspect ratio" default="3:4"}."
  }
}
```

[[Structured JSON Prompt]] [[Sydney Sweeney Reference]]

---

### 7. 豪华游艇上的电影感黄金时段肖像

**Author**: [Abhishek Singh](https://x.com/2abhisheknaks)  **Date**: 2026-01-28  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超现实、电影感的特写镜头，描绘一位英俊男士在黄金时段的豪华游艇上。它指定了“老钱”美学、详细的着装（白色亚麻、珍珠项链）、姿势（随意倚靠，手持雪茄）以及技术性的光照/分辨率要求。

![豪华游艇上的电影感黄金时段肖像](https://cms-assets.youmind.com/media/1769668490203_cgvt2q_G_vfAE8asAAFpNb.jpg)

```
{
 "A hyper-realistic, cinematic medium shot of a handsome man standing on the deck of a luxury yacht during golden hour. He has dark, swept-back hair and a well-groomed beard, wearing dark aviator sunglasses. He is dressed in a breezy {argument name="shirt color" default="white"} linen shirt, unbuttoned at the top, and matching white linen trousers. Accessories include a simple {argument name="accessory type" default="pearl necklace"} and a gold wristwatch with a deep blue dial. He is leaning casually against a wooden railing, holding a lit cigar with a wisp of smoke rising. The background features a vibrant sunset over the ocean horizon, soft wicker furniture with beige cushions, and potted tropical palm plants. The lighting is warm and glowing, evoking a wealthy, 'old money' aesthetic. 8k resolution, highly detailed.",
  "negative_prompt": "cartoon, illustration, low quality, blurry, deformed, bad anatomy, grayscale, overexposed, grainy, text, watermark",
  "style_tags": [
    "photorealistic",
    "golden hour",
    "luxury lifestyle",
    "cinematic lighting",
    "portrait",
    "wealth"
  ],
  "resolution": "8k",
  "camera": {
    "shot_type": "medium",
    "lens": "cinematic",
    "focus": "sharp"
  },
  "lighting": {
    "type": "golden hour",
    "mood": "warm, glowing"
  },
  "subject": {
    "gender": "male",
    "appearance": {
      "hair": "dark, swept-back",
      "beard": "well-groomed",
      "sunglasses": "dark aviator"
    },
    "clothing": {
      "shirt": "white linen, unbuttoned at top",
      "trousers": "white linen"
    },
    "accessories": [
      "pearl necklace",
      "gold wristwatch with deep blue dial"
    ],
    "pose": "leaning casually against railing, holding lit cigar"
  },
  "background": {
    "setting": "luxury yacht deck",
    "elements": [
      "sunset over ocean",
      "soft wicker furniture with beige cushions",
      "potted tropical palm plants"
    ]
  }
}
```

[[Structured JSON Prompt]] [[Male Portrait]] [[Old Money Aesthetic]]

---

### 8. 西德尼·斯威尼 (Sydney Sweeney) 化妆的四格拼贴图

**Author**: [lilzula](https://x.com/lilzula_009_me)  **Date**: 2026-01-28  **Language**: en

> 一个 JSON 提示，旨在生成一个四格照片拼贴画（网格布局），内容是一位年轻女性（Sydney Sweeney）正在化妆。它为每个面板指定了不同的面部表情、服装（黑色无肩带连衣裙）和美学风格（真实的社交媒体/GRWM 氛围，带有温暖柔和的室内照明）。

![西德尼·斯威尼 (Sydney Sweeney) 化妆的四格拼贴图](https://cms-assets.youmind.com/media/1769668488600_r5cd3p_G_vL2-6W8AAF22g.jpg)

```
{
  "image_layout": "four-panel grid, photo collage",
  "subject": {
    "description": "Young woman with long wavy blonde/light brown hair",
    "facial_expressions": [
      "pouty/glamorous",
      "playful with tongue out",
      "smiling while applying lip gloss",
      "soft smile tilting head"
    ],
    "activities": "applying makeup with a red brush and pink lip gloss",
    "attire": "black strapless sweetheart neckline dress"
  },
  "visual_style": {
    "lighting": "warm, soft indoor lighting with a slight glow",
    "background": "textured beige or light brown wall",
    "aesthetic": "candid social media style, getting ready (GRWM) vibe",
    "color_palette": ["black", "red", "pink", "beige", "warm skin tones"]
  },
  "technical_details": {
    "focus": "sharp focus on the subject, soft background",
    "composition": "medium close-up shots",
    "vibe": "playful, feminine, and glamorous"
  }
}
```

[[Structured JSON Prompt]] [[Warm Indoor Lighting]] [[Sydney Sweeney Reference]]

---

### 9. 泡泡浴中的高角度浴室自拍

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-01-28  **Language**: en

> 一个极其详细的 JSON 提示，用于生成一张高角度快照：一位女士坐在泡泡浴中，回头望向肩膀。该提示包含复杂的解剖学和姿势约束（明显的腰部弓形、特定的手臂位置）、详细的环境几何形状（蛇皮印花比基尼、地铁瓷砖、镜面反射），并指定了镜面反射的内容，旨在实现超逼真的效果。

![泡泡浴中的高角度浴室自拍](https://cms-assets.youmind.com/media/1769668494727_0atd8d_G_vKr8IXEAAlpEB.jpg)

```
{
  "scene_context": {
    "setting": "Indoor bathroom environment, seated inside a white bathtub",
    "action": "Subject posing for a photo while seated in a bubble bath, looking back over shoulder",
    "composition_type": "High-angle snapshot, rear view with mirror reflection"
  },
  "subject_visuals": {
    "demographics": "Young female, light-to-medium skin tone",
    "hair": "Dark brown hair pulled up into a high, tight messy bun; hairline is sleek, bun is compact",
    "body_type": "Slender, fit physique with visible spinal definition and defined lower back curve",
    "skin_details": "Natural skin texture, slight sheen from lighting on shoulder blades and buttocks, visible moles/blemishes on back"
  },
  "pose_mechanics": {
    "orientation": "Subject is angled 45 degrees away from the camera, displaying full back and buttocks",
    "spine_and_pelvis": "Pronounced lumbar arch (lordosis), pelvis tilted anteriorly to accentuate gluteal curve; spine creates a visible vertical furrow",
    "head_neck": "Head rotated approximately 120 degrees to the left, chin slightly lowered, looking back towards the camera lens",
    "limbs": {
      "left_arm": "Bent at elbow, resting on the edge of the bathtub, shoulder slightly elevated",
      "right_arm": "Extended downwards, submerged or hidden by body angle",
      "legs": "Submerged in foam, knees bent, hips weighted heavily into the tub surface"
    },
    "weight_distribution": "Visibly seated weight compression on buttocks against the tub bottom, slight gravitational sag of soft tissue",
    "contact_points": "Glutes compressed against tub floor, left forearm resting on tub rim"
  },
  "attire_details": {
    "garment": "Two-piece bikini with brown and black snakeskin/python print",
    "top": "Bandeau style strap across back, knotted in center back with loose hanging ties",
    "bottom": "High-cut, cheeky/thong style, thin side straps sitting high on the hip bone, fabric digging slightly into skin",
    "fit": "Tight, form-fitting, following the curvature of the body"
  },
  "environmental_geometry": {
    "bathtub": "White acrylic or porcelain tub, curved interior, filled with opaque white soapy foam/bubbles",
    "wall": "Dark, metallic or grey horizontal subway tiles (rectangular) behind the tub",
    "mirror": "Large horizontal mirror mounted above the tiles, spanning the width of the frame",
    "clutter": "Visible on tub ledge or shelf in reflection: candles (lit), rolled white towels, toiletries, glass with liquid"
  },
  "mirror_reflection_details": {
    "content": "Reflects the subject's face in profile/three-quarter view, left hand near face, and background room details",
    "facial_expression": "Neutral to slightly pouty, gaze directed towards the taking device or self-reflection",
    "background_reflection": "Includes a potted plant with long leaves, a basket, and bathroom shelving"
  },
  "lighting_and_atmosphere": {
    "source_type"
  }
}
```

[[Structured JSON Prompt]] [[Hyperrealistic Photography]]

---

### 10. 亲密特写肖像，眼神直视，带环形灯光

**Author**: [七表哥](https://x.com/seven_cuz)  **Date**: 2026-01-28  **Language**: en

> 一个复杂的 JSON 提示词，用于 Nano Banana Pro，旨在生成一张亲密、超写实的特写肖像。该提示词强调直接、诱惑的凝视，详细的皮肤纹理（可见毛孔、次表面散射），特定的发型和妆容细节（巧克力棕色头发、珊瑚红亮泽唇），以及一个由强烈的定向环形灯照亮的舒适、低调的卧室环境。它要求使用参考图像来保持面部一致性。

![亲密特写肖像，眼神直视，带环形灯光](https://cms-assets.youmind.com/media/1769668518799_fv0kyc_G_uj5xjaAAASH7w.jpg)

```
{
    "subject": {
        "core_identity": "Use the same face from the reference image without changing facial features, fair skin with soft warm undertones, natural glamorous beauty, shoulder-length straight chocolate-brown hair with subtle warm tones",
        "skin_and_facial_details": "hyper-detailed photorealistic skin:1.4, visible fine pores on nose cheeks and chin, subtle subsurface scattering creating gentle luminous glow, natural small imperfections and faint texture, highly detailed irises with rich radial patterns and sharp catchlights from ring light and phone flash, defined brows, long curled lashes, full glossy lips with rich coral-red color and high shine:1.3",
        "hair": "shoulder-length straight chocolate-brown hair with warm undertones, clean blunt bob cut with soft face-framing layers, strands catching ring light with realistic shine separation and subtle movement:1.2",
        "body_figure": "slender yet softly curvaceous feminine silhouette with balanced proportions:1.2, gentle shoulder line exposed by low-cut top, visible delicate collarbones, natural bust contour softly pressed against fabric, slim waist and hips implied in close-up frame, natural asymmetry in relaxed reclined posture",
        "micro_expression": "direct intimate gaze with slightly hooded eyes looking into camera, softly parted glossy lips in gentle seductive pout, subtle knowing smile at corners, conveying private allure, relaxed confidence and sensual invitation through heavy-lidded eyes and relaxed facial expression:1.2"
    },
    "apparel_and_materials": "black velvet or plush cropped top with low neckline, soft luxurious fabric with deep pile texture, subtle sheen and light absorption creating rich dark tones, natural drape and compression folds around bust and shoulders from reclined pose:1.3",
    "pose_and_action": "intimate close-up bedroom selfie pose lying on bed or pillow, head tilted slightly toward camera, shoulders relaxed, body angled to show neck and collarbone line, posture conveys private relaxation, sensual closeness and inviting vulnerability through reclined position and direct eye contact:1.2",
    "scene_and_environment": "cozy modern bedroom interior, soft teal/blue-green curtains in background, warm ring light providing key illumination, neutral bedding, private intimate space with soft low-key atmosphere:1.1",
    "lighting_shadows_and_color_design": "strong directional ring light from upper front-right creating soft yet dramati
```

[[Structured JSON Prompt]] [[Bedroom Setting]] [[Skin Pore Detail]]

---

### 11. 高端能量饮料商业产品摄影

**Author**: [Maercih](https://x.com/Maercihh)  **Date**: 2026-01-28  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张纤细能量饮料罐的高端商业产品照片。它详细说明了动态元素（液体飞溅、漂浮水果、冰块）、特定的照明技术（主光、轮廓光、强调光）以及逼真度限制，以实现照片级真实感、干净且现代的广告效果。

![高端能量饮料商业产品摄影](https://cms-assets.youmind.com/media/1769668488733_zv6kkz_G_ubMRoaEAAv-Kv.jpg)
![高端能量饮料商业产品摄影](https://cms-assets.youmind.com/media/1769668488693_0lxkad_G_ubMPtbAAMZbLZ.jpg)

```
{
  "scene_type": "high-end commercial product photography",
  "subject": {
    "product": "slim premium energy drink can",
    "brand_text": "{argument name="brand name" default="AFENON"}",
    "finish": "brushed aluminum with deep green accent",
    "orientation": "diagonal tilt, floating mid-air"
  },
  "environment": {
    "background": "soft mint-green to white gradient, subtle radial light burst from behind",
    "atmosphere": "cool mist, faint vapor trails, fresh and clean air feeling"
  },
  "motion_elements": {
    "liquid": "translucent green liquid splash wrapping around the can in a dynamic spiral",
    "fruit": [
      "fresh kiwi slices with visible seeds and moist texture",
      "whole kiwi with natural skin detail"
    ],
    "extras": [
      "mint leaves with realistic veins",
      "clear ice cubes with sharp edges and internal cracks",
      "micro droplets frozen in motion"
    ]
  },
  "lighting": {
    "key_light": "soft studio key light from upper left",
    "rim_light": "clean rim highlight outlining the can edges",
    "accent_light": "cool green backlight enhancing freshness",
    "shadows": "soft, controlled, no harsh contrast"
  },
  "camera": {
    "lens": "85mm product lens look",
    "aperture": "shallow depth of field",
    "focus": "sharp on brand text and can surface",
    "motion_freeze": "high-speed flash look to freeze liquid and droplets"
  },
  "color_grading": {
    "palette": "fresh greens, silver metallics, clean whites",
    "contrast": "medium",
    "saturation": "natural, not neon"
  },
  "realism_constraints": {
    "no_plastic_look": true,
    "no_over_sharpening": true,
    "no_exaggerated_glow": true,
    "natural_liquid_physics": true,
    "commercial_photorealism": true
  },
  "style_keywords": [
    "cinematic product shot",
    "premium energy drink ad",
    "high-speed splash photography",
    "clean modern branding",
    "refreshing, cold, crisp"
  ]
}
```

[[Structured JSON Prompt]] [[Product Photography]]

---

### 12. Sydney Sweeney 衣橱选择生成器（4 个场景）

**Author**: [Bahar azam](https://x.com/BaharAzamm561)  **Date**: 2026-01-27  **Language**: en

> 一个 JSON 提示，旨在生成四张悉尼·斯威尼 (Sydney Sweeney) 的不同图片，每张图片都展示了不同的服装和环境：在湖船上的潜水服、在日落时豪华游艇上的奶油色套装、在酒店大堂的翠绿色晚礼服，以及在公园里的休闲碎花连衣裙。此提示似乎是用于图像生成系统选择或生成多样化造型的结构化输入。

![Sydney Sweeney 衣橱选择生成器（4 个场景）](https://cms-assets.youmind.com/media/1769581988172_nex0ly_G_tUxEFWEAEDmFx.jpg)
![Sydney Sweeney 衣橱选择生成器（4 个场景）](https://cms-assets.youmind.com/media/1769581988427_xalv42_G_tUxELXYAA7tpO.jpg)
![Sydney Sweeney 衣橱选择生成器（4 个场景）](https://cms-assets.youmind.com/media/1769581988410_yyzuho_G_tUw9aXsAAjMS5.jpg)

```
{
  "subject": "{argument name="subject name" default="Sydney Sweeney"}",
  "images": [
    {
      "id": "image_01",
      "scene": "Boat on Lake",
      "description": "Sydney Sweeney relaxing on a boat with a German Shepherd.",
      "action": "Hugging a large dog",
      "clothing": {
        "item": "Wetsuit  Swimwear",
        "color": "Black",
        "style": "Long sleeve, sleek"
      },
      "environment": {
        "location": "Lake",
        "background": "Pine forest and water",
        "lighting": "Daylight"
      }
    },
    {
      "id": "image_02",
      "scene": "Luxury Yacht",
      "description": "Sydney Sweeney standing on a yacht deck at sunset.",
      "action": "Holding a champagne glass, posing elegantly",
      "clothing": {
        "item": "Suit",
        "color": "Cream / Off-white",
        "style": "Oversized blazer, trousers, silk camisole",
        "accessories": "Layered necklaces"
      },
      "environment": {
        "location": "Coastal sea",
        "background": "Coastline with hills and buildings",
        "lighting": "Golden hour  Sunset"
      }
    },
    {
      "id": "image_03",
      "scene": "Luxury Interior",
      "description": "Sydney Sweeney sitting in an opulent hotel lobby or hall.",
      "action": "Sitting and smiling",
      "clothing": {
        "item": "Evening Gown",
        "color": "Emerald Green",
        "style": "Satin fabric with gold floral embroidery on the bodice",
        "accessories": "Gold clutch bag, drop earrings"
      },
      "environment": {
        "location": "Hotel Lobby / Ballroom",
        "background": "Marble columns, chandeliers",
        "lighting": "Warm indoor lighting"
      }
    },
    {
      "id": "image_04",
      "scene": "Park Bench",
      "description": "Sydney Sweeney sitting on a wooden bench in a park.",
      "action": "Resting with a book",
      "clothing": {
        "item": "Casual Outfit",
        "style": "Floral midi dress with denim jacket",
        "footwear": "Brown sandals",
        "accessories": "Brown leather tote bag"
      },
      "environment": {
        "location": "Public Park",
        "background": "Green trees, garden path",
        "lighting": "Soft daylight"
      }
    }
  ]
}
```

[[Structured JSON Prompt]]

---

### 13. 咖啡馆里的休闲生活肖像

**Author**: [Sedra](https://x.com/SedraLab)  **Date**: 2026-01-27  **Language**: en

> 一个详细的 JSON 提示，用于生成一位年轻女性在咖啡馆的休闲生活肖像，重点关注特定的姿势细节、运动休闲装（连体衣/跳线）以及路易威登手袋等高端配饰，以轻松自信的美学风格捕捉。

![咖啡馆里的休闲生活肖像](https://cms-assets.youmind.com/media/1769581960034_99wqan_G_szpDFWkAAsYq0.jpg)

```
{
  "scene": "Casual lifestyle portrait in an indoor cafe setting",
  "subject": {
    "character": "Young female with a friendly, relaxed demeanor",
    "face": {
      "structure": "Oval shape with prominent cheekbones and visible dimples",
      "skin": "Tan, smooth, glowing complexion",
      "eyes": {
        "shape": "Almond",
        "color": "Dark brown",
        "expression": "Direct eye contact, engaging"
      },
      "mouth": {
        "lips": "Natural pink, smiling gently"
      },
      "makeup": "Natural 'no-makeup' look, light blush, groomed brows"
    },
    "hair": {
      "color": "Dark brown to black",
      "length": "Shoulder-length (lob)",
      "texture": "Straight with slight volume",
      "style": "Loose with wispy bangs framing the forehead",
      "shine": "Healthy, slight sheen"
    },
    "accessories": {
      "necklace": "Thin gold chain with a heart pendant",
      "earrings": "Small silver or gold hoops",
      "bracelets": "Thin metallic bracelets on both wrists",
      "rings": "Simple bands on fingers"
    }
  },
  "pose": {
    "overall": "Casual seated pose, leaning back slightly against the chair",
    "position": {
      "base": "Sitting on a wooden chair",
      "orientation": "Facing forward towards the camera"
    },
    "torso": {
      "direction": "Frontal",
      "posture": "Relaxed but upright"
    },
    "arms": {
      "position": "Right arm holding a straw/drink, left arm resting near the table",
      "other": "Holding an iced drink near chest level"
    },
    "legs": {
      "position": "Asymmetrical; right leg bent with knee drawn up, left leg extended downwards",
      "visible": "Legs fully visible in tight fitting clothing"
    },
    "head": {
      "turn": "Facing straight forward",
      "expression": "Soft, confident smile"
    }
  },
  "outfit": {
    "activewear": {
      "type": "Sleeveless unitard / jumpsuit",
      "color": "Beige / Nude",
      "style": "Athleisure",
      "details": {
        "top": "V-neckline, sleeveless",
        "fit": "Form-fitting, skin-tight",
        "material": "Ribbed or smooth stretch fabric"
      }
    },
    "footwear": {
      "type": "Sneakers",
      "style": "Grey athletic running shoes (New Balance style)",
      "socks": "White ribbed crew socks"
    }
  },
  "body": {
    "type": "Fit, slender",
    "skin": "Tan"
  },
  "environment": {
    "location": "Coffee shop interior",
    "furniture": {
      "table": "Round wooden table with slatted base",
      "chair": "Wooden chairs with simple backrests"
    },
    "objects": {
      "drink": "Glass of iced {argument name="drink type" default="green matcha latte"} with a glass straw",
      "bag": "Louis Vuitton Monogram Speedy handbag on the table",
      "sunglasses": "Black frame sunglasses on the table",
      "coaster": "Small wooden plate/coaster"
    },
    "background": {
      "people": "Blurred figures sitting at other tables",
      "floor": "Concrete or stone tile"
    }
  }
}
```

[[Structured JSON Prompt]]

---

### 14. 电影级超写实角色配对提示词：蓝色角色与女性

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-27  **Language**: en

> 一个高度结构化的 JSON 提示，用于 Nano Banana Pro 创建一个超逼真的电影场景，设定在一个现代白色房间中。场景中，一个戴着超大眼镜、蓝色皮肤的类人小角色，正依偎在一位身穿蓝色连衣裙的女士肩上，整体氛围安静、忧郁、亲密，并伴有细微的蓝色星光投射。

![电影级超写实角色配对提示词：蓝色角色与女性](https://cms-assets.youmind.com/media/1769582018472_65it6b_G_sMNQ5XwAE_e09.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "ultra_photoreal_cinematic_character_pair",
      "version": "v1.0_BLUE_CHARACTER_AND_WOMAN_BLUE_DRESS_MODERN_WHITE_ROOM_BLUE_STARS_NO_TEXT_EN",
      "priority": "highest",
      "language": "en"
    },
    "references": {
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (OPTIONAL)",
        "purpose": "STYLE_MOOD_LIGHTING_ANCHOR",
        "strict_lock": false,
        "preserve_vibe": true
      }
    },
    "output_settings": {
      "aspect_ratio": "3:4",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "cinematic_ultra_photoreal_film_still",
      "sharpness": "crisp_but_natural",
      "film_grain": "very_subtle_35mm",
      "dynamic_range": "natural_filmic_not_hdr",
      "color_grade": "clean_neutral_whites_with_soft_blue_accents",
      "skin_rendering": "natural_skin_texture_no_beautify",
      "lens_and_camera": {
        "camera": "ARRI_Alexa_Mini_LF",
        "lens": "50mm_prime",
        "aperture": "f2.0",
        "focus_style": "subject_eyes_priority_shallow_dof"
      },
      "lighting": {
        "key": "soft_window_daylight",
        "fill": "gentle_bounce_fill",
        "mood": "quiet_emotional_intimate"
      },
      "background": {
        "environment": "minimal_modern_white_room_scandinavian_style",
        "props": "white_bed_white_linen_simple_wall_art_minimal_decor",
        "accent": "subtle_blue_star_projections_on_wall_and_ceiling"
      }
    },
    "scene": {
      "global_description": "A cinematic ultra-photoreal scene in a modern white minimalist bedroom. A small blue-skinned, human-like emotional character with short glittery blue hair and oversized round glasses rests gently on the shoulder/back of a woman lying on a white bed. The woman wears a modest elegant blue dress. The atmosphere is calm and slightly melancholic, with soft daylight and subtle blue star projections on the walls and ceiling. Everything looks physically real: fabric texture, skin pores, hair strands, and natural shadows. No cartoon or illustration look.",
      "characters": {
        "blue_character": {
          "description": "small human-like blue character, expressive big eyes, glittery short blue hair, oversized round glasses, wearing a light blue knitted sweater",
          "pose": "leaning gently on the woman’s shoulder/back, looking slightly sad and thoughtful"
        },
        "woman": {
          "description": "young adult woman, natural face, realistic skin texture, wearing a modest satin-like blue dress",
          "pose": "lying on the bed on her side, head turned toward camera, calm tired expression"
        }
      },
      "composition": "portrait framing, subjects centered, shallow depth of field, minimal background clutter, blue star projections visible but subtle",
      "micro_details": [
        "real
```

[[Structured JSON Prompt]]

---

### 15. 超逼真黄金时段人像提示词

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 一个详细、结构化的 JSON 提示，用于在黄金时段生成一张休闲奢华环境中女性的超逼真图像，强调高端编辑品质和具体的相机/灯光细节。

![超逼真黄金时段人像提示词](https://cms-assets.youmind.com/media/1769581953251_qcdlne_G_rxTYjWMBAXtcH.jpg)

```
{
  "meta": {
    "aspect_ratio": "4:5",
    "quality": "ultra_photorealistic, raw, influencer lifestyle, high-end editorial",
    "resolution": "8k",
    "camera": "Mirrorless camera (e.g., Sony A7R IV)",
    "lens": "35mm f/1.4 lens (capturing full body and environment)",
    "style": "Casual luxury, sun-drenched, golden hour aesthetic, relaxed confidence",
    "composition": "Full body shot of a woman reclining in a chair, low angle perspective emphasizing legs, centered framing."
  },
  "scene": {
    "location": "A modern, minimalist hotel room or bedroom.",
    "environment": [
      "Modern beige fabric lounge chair with a matching footrest",
      "Light wooden floating nightstand with blue over-ear headphones resting on it",
      "White wall radiator visible in background",
      "Plain neutral beige/off-white walls",
      "Beige lampshade in the upper corner"
    ],
    "time": "Late afternoon, Golden Hour.",
    "atmosphere": "Lazy, warm, quiet luxury, unbothered, chic."
  },
  "lighting": {
    "type": "Direct, hard natural sunlight.",
    "source": "Window off-camera to the left.",
    "effect": "Creates strong, distinct geometric shadows (likely from window frames) on the wall behind, high contrast highlights on the face and legs, warm golden tone."
  },
  "subject": {
    "identity": "A stunning young woman with long, wet-look platinum blonde hair falling over her shoulders. She has a tan complexion, full lips, and a confident, direct gaze.",
    "body": {
      "pose": "Reclining deeply into the lounge chair, legs crossed and extended towards the camera (focus on bare feet and legs), one hand resting on the chair arm, the other on her leg.",
      "physique": "Fit, curvy figure."
    },
    "outfit": {
      "clothing": "Tight-fitting, long-sleeved {argument name="dress color" default="purple"} ribbed mini dress.",
      "accessories": "Red string bracelet on wrist, black nail polish on hands and toes."
    }
  },
  "realism_focus": {
    "textures": "Ribbed knit texture of the purple dress, realistic skin texture under direct harsh sunlight, individual wet strands of blonde hair, fabric weave of the beige chair.",
    "imperfections": "Harsh realistic shadows on the wall, natural creases in the dress where the body bends, casual placement of the headphones."
  }
}
```

[[Structured JSON Prompt]]

---

### 16. 带泰迪熊和贝雷帽的逼真卧室肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 一个详细的 JSON 提示，用于生成一张年轻女性的超写实肖像。该女性拥有一头铂金色头发，戴着灰色贝雷帽，穿着格子裙，躺在床上，怀里抱着一只粉色泰迪熊。提示中指定了相机角度（从床尾平视）和柔和的自然光照，以营造高质量、可爱的美感。

![带泰迪熊和贝雷帽的逼真卧室肖像](https://cms-assets.youmind.com/media/1769581987702_68lfxa_G_rvIB6bAAMPmt8.jpg)

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
      "top": "Pink long-sleeve ribbed top with lace trim neckline",
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

[[Structured JSON Prompt]] [[Platinum Blonde Hair]] [[Natural Light Portrait]] [[Plaid Skirt]]

---

### 17. 超逼真复古高档餐厅镜面自拍

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 一个详细的 JSON 提示，用于生成一张在高端复古风格餐厅拍摄的超逼真镜面自拍。该提示指定了两种表情（微妙的微笑和开心的笑声）、深色服装、温暖亲密的烛光晚间照明，以及模拟高品质智能手机摄像头的技术细节，以营造奢华的“夜生活”美学。

![超逼真复古高档餐厅镜面自拍](https://cms-assets.youmind.com/media/1769581989766_8wwnl2_G_rKJ3rbUAAEZRL.jpg)

```
{
  "prompt_details": {
    "subject": {
      "description": "Young woman with long, voluminous brunette hair featuring soft waves and a center part. She has almond-shaped eyes, arched brows, and defined facial features.",
      "expressions": [
        "Top: Subtle, confident smile, direct eye contact with the reflection.",
        "Bottom: Candid, joyful laughter, eyes closed, head tilted back."
      ],
      "attire": {
        "top_image": "Black high-neck sleeveless top, sophisticated and minimal.",
        "bottom_image": "Black strapless dress with subtle glittering texture (sequins or shimmer)."
      },
      "accessories": [
        "Delicate silver necklace (tennis style or similar)",
        "Thin gold/silver bracelets",
        "Rings on fingers"
      ]
    },
    "pose_and_action": {
      "type": "Mirror selfie POV.",
      "hands": [
        "Holding a wine glass filled with {argument name="wine color" default="white wine"}.",
        "Holding a smartphone to capture the reflection."
      ],
      "posture": "Seated at a dining table, relaxed but elegant."
    },
    "environment": {
      "location": "Upscale, vintage-inspired restaurant or bistro.",
      "decor": [
        "Dark wood paneling",
        "Ornate mirrors reflecting the room",
        "Floral or tapestry-style wallpaper/upholstery",
        "Plush velvet seating (visible patterns)",
        "White tablecloths"
      ],
      "background_details": "Other diners softly visible in the background, vintage lamps with fringed shades."
    },
    "lighting": {
      "atmosphere": "Dim, warm, intimate evening ambiance.",
      "sources": [
        "Soft glow from vintage table lamps with warm shades",
        "Candlelight (prominent tall white candle in the bottom frame)",
        "Ambient reflection from mirrors"
      ],
      "effect": "Golden hour indoor tone, soft highlights on hair and skin, rich shadows."
    },
    "camera_and_tech": {
      "style": "Ultra Photorealistic, 8k resolution, candid lifestyle photography.",
      "camera_simulation": "Smartphone rear camera (iPhone Pro style), wide aperture (f/1.8) for depth of field.",
      "focus": "Sharp focus on the subject in the mirror reflection, soft bokeh on foreground elements (wine glass stem, candle).",
      "color_grading": "Warm, cinematic, slightly grainy low-light texture, rich contrast."
    },
    "mood": "Luxurious, festive, happy, chic, 'night out' aesthetic."
  }
}
```

[[Structured JSON Prompt]] [[Nightlife Aesthetic]]

---

### 18. 四幕奢华康养生活场景

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 一个结构化的 JSON 提示词，请求生成四张超逼真的图像，描绘一种精致、注重健康的 lifestyle。场景包括一个现代厨房、一个高端浴室、一个极简主义的健康空间和一个明亮的咖啡角，所有场景都有一位穿着米色运动服的人物。

![四幕奢华康养生活场景](https://cms-assets.youmind.com/media/1769581971950_fj0632_G_rJqdwacAAqAZR.jpg)

```
{
  "overall_theme": {
    "description": "A curated series of four ultra-photorealistic vignettes showcasing a luxurious, wellness-focused lifestyle.",
    "mood": "Calm, serene, balanced, sophisticated, peaceful, rejuvenating.",
    "style": "Minimalist, high-end, contemporary, clean aesthetic, aspirational."
  },
  "subject": {
    "description": "Young woman.",
    "appearance": {
      "hair": "Long, dark brown, wavy, natural texture.",
      "skin": "Clear, glowing, natural.",
      "makeup": "No-makeup makeup look, dewy finish.",
      "physique": "Fit, toned."
    },
    "expression": "Serene, composed, gently smiling, focused."
  },
  "wardrobe": {
    "outfit_base": "Matching ribbed {argument name="activewear color" default="beige/cream"} activewear set.",
    "variations": [
      "Sleeveless crop top and high-waisted leggings.",
      "Long-sleeve crop top and high-waisted leggings."
    ],
    "style": "Comfortable, stylish, high-quality fabric."
  },
  "environmental_details": {
    "lighting": {
      "type": "Natural daylight.",
      "quality": "Soft, diffused, warm, bright.",
      "source": "Large windows (implied or visible)."
    },
    "color_palette": {
      "dominant": ["Warm Beige", "Cream", "White", "Marble Grey"],
      "accents": ["Green (plants)", "Gold (fixtures, details)", "Natural Wood", "Soft Purple (smoothie)"]
    },
    "materials": ["White Marble", "Light Wood", "Stone", "Ceramic", "Glass", "Linen"]
  },
  "scenes": [
    {
      "location": "Modern Luxury Kitchen",
      "environment": "White marble island and countertops, white shaker cabinets, gold hardware, integrated wine fridge, large window.",
      "pose": "Standing at the island, body angled slightly, looking down.",
      "action": "Whisking a hot beverage in a small bowl.",
      "props": ["Ceramic bowl", "Wooden whisk", "Steam", "Mug with 'H'", "Wine fridge"]
    },
    {
      "location": "High-End Bathroom",
      "environment": "Large backlit mirror, white marble vanity, white walls, orchid plant.",
      "pose": "Standing facing the mirror, one hand applying product to face.",
      "action": "Applying skincare.",
      "props": ["Cotton pad", "Skincare bottle", "Lit Diptyque candle", "Whole coconut", "Glass jars"]
    },
    {
      "location": "Minimalist Wellness Space",
      "environment": "Textured beige walls with curved arches, stone water fountain, eucalyptus in a vase.",
      "pose": "Full-body stretch, arms extended overhead, head tilted back, eyes closed.",
      "action": "Stretching.",
      "props": ["Stone water feature", "Large perfume bottle", "Eucalyptus vase"]
    },
    {
      "location": "Bright Café Corner",
      "environment": "Round white marble table, cane chair, large window overlooking a street.",
      "pose": "Sitting at the table, smiling while eating, holding a fork.",
      "action": "Eating avocado toast.",
      "props": ["Avocado toast on plate", "Purple smoothie in glass", "Fork", "Assouline boo"
    }
  ]
}
```

[[Structured JSON Prompt]] [[Luxury Bathroom]]

---

### 19. 餐厅夏季生活方式编辑拼贴画

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一个四图拼贴画，捕捉休闲高档餐厅中的夏日生活方式编辑场景。它侧重于抓拍姿势、自然日光以及条纹上衣和金色首饰等特定服装细节。

![餐厅夏季生活方式编辑拼贴画](https://cms-assets.youmind.com/media/1769581981776_cwrj4v_G_rIb8WbAAADWyK.jpg)

```
{
  "scene": {
    "location": "casual upscale restaurant booth",
    "environment": "light wood table and bench seating, white walls, round window detail",
    "lighting": "soft natural daylight, evenly diffused",
    "time_of_day": "daytime",
    "ambience": "relaxed, bright, European summer dining vibe"
  },
  "subject": {
    "description": "young woman seated at a restaurant table",
    "hair": "long blonde hair, straight with a natural center part",
    "makeup": "natural, fresh makeup with soft blush and neutral lips",
    "expressions": [
      "looking off to the side with subtle smile",
      "calm gaze while sipping wine",
      "downward thoughtful expression",
      "warm, candid smile while touching hair"
    ],
    "pose_style": "effortless, candid, lifestyle-focused"
  },
  "wardrobe_and_accessories": {
    "outfit": "strapless {argument name="top color" default="yellow-and-white"} striped top with lace trim",
    "jewelry": [
      "small gold hoop earrings",
      "delicate gold necklace"
    ],
    "nails": "short white manicure"
  },
  "props": {
    "drink": "glass of white wine",
    "table_items": [
      "menu",
      "folded white napkin with red stripe",
      "water glasses"
    ]
  },
  "composition": {
    "layout": "four-image collage",
    "framing": [
      "side-profile seated portrait",
      "front-facing half-body shot",
      "downward gaze lifestyle shot",
      "smiling candid portrait"
    ],
    "camera_angle": "eye level",
    "focus": "sharp subject with clean, uncluttered background",
    "aesthetic": "summer lifestyle editorial, Instagram-ready"
  },
  "camera": {
    "lens": "35mm",
    "aperture": "f/2.8",
    "iso": 200,
    "shutter_speed": "1/125",
    "white_balance": "daylight"
  },
  "style_keywords": [
    "summer dining",
    "natural light",
    "casual elegance",
    "lifestyle photography",
    "editorial candid"
  ]
}
```

[[Structured JSON Prompt]] [[Four Panel Collage]] [[Natural Daylight Photography]]

---

### 20. Kawaii Y2K 棒棒糖肖像

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-27  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一张超现实、可爱、俏皮的肖像，融合了卡哇伊/Y2K 美学，描绘了一位手持棒棒糖、身穿超大蓬松粉色夹克和迷你裙的女性，置身于一家舒适的咖啡馆中。

![Kawaii Y2K 棒棒糖肖像](https://cms-assets.youmind.com/media/1769581967637_mys0by_G_rBPLDXsAICFDE.jpg)

```
{
  "reference": {
    "face_consistency": "Use the exact same face from the reference image",
    "facial_changes": "None",
    "identity_preservation": true
  },
  "subject": {
    "gender": "female",
    "age": "young adult",
    "ethnicity": "western",
    "expression": "cute, playful, innocent",
    "pose": "playful pose with lollipop in mouth",
    "facial_features": {
      "eyes": "innocent doe eyes",
      "skin": "realistic skin texture with visible freckles",
      "emotion": "soft playful charm"
    },
    "hair": {
      "color": "platinum blonde",
      "style": "long straight hair"
    }
  },
  "outfit": {
    "outerwear": "oversized fluffy {argument name="jacket color" default="pastel pink"} fuzzy fur jacket",
    "top": "light mint crop top",
    "bottom": "white mini skirt with black polka dots and lace trim",
    "accessories": {
      "bag": "small cream-colored polka-dot crossbody bag",
      "bag_details": "plush keychains and pom-poms",
      "headwear": "sunglasses resting on head",
      "prop": "lollipop"
    }
  },
  "environment": {
    "location": "cozy cafe interior",
    "lighting": "soft natural daylight",
    "atmosphere": "warm, cozy, inviting"
  },
  "style": {
    "aesthetic": ["kawaii", "y2k"],
    "rendering": "ultra-realistic",
    "detail_level": "high",
    "vibe": "cute, soft, aesthetic"
  },
  "quality": {
    "skin_detail": "highly detailed",
    "realism": "photorealistic",
    "focus": "sharp subject, soft background"
  }
}
```

[[Structured JSON Prompt]] [[Y2K Aesthetic]] [[Mini Skirt]] [[Cozy Cafe Setting]]

---

### 21. 超逼真家居服生活方式肖像

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-27  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真的图像：一位年轻女性身穿黄色“HAWAIIAN TROPIC”两件套，慵懒地躺在沙发上。提示中指定了自然的皮肤纹理、浅色雀斑、放松的姿态，以及一个拥有温暖环境光的现代客厅场景，旨在营造一种具有“2000 年代数码相机”氛围的网红生活方式美学。

![超逼真家居服生活方式肖像](https://cms-assets.youmind.com/media/1769581993201_bi4nz0_G_rhEGRbYAA8PLk.jpg)

```
{
  "prompt_data": {
    "subject": {
      "description": "Young woman with long, wavy blonde hair and a light fair skin",
      "features": "Natural skin texture with visible tan lines on the chest, slight flush on cheeks, soft smile, navel piercing, light freckles.",
      "accessories": "Gold pendant necklace, small gold hoop earrings, small tattoo on the left inner forearm."
    },
    "clothing": {
      "outfit": "Matching yellow two-piece loungewear set.",
      "top": "Yellow strapless tube top featuring the text '{argument name="top text" default="HAWAIIAN TROPIC"}' in brown serif font with a hibiscus flower and palm graphic on the side.",
      "bottoms": "Matching yellow shorts visible at the waist and thigh area."
    },
    "pose_and_action": {
      "posture": "Reclining and lounging comfortably on a grey textured sofa.",
      "body_language": "Relaxed and casual, leaning back against the couch cushions, one arm extended to support weight, the other hand resting gently near the waist, legs angled toward the camera.",
      "expression": "Friendly, relaxed, and engaging eye contact."
    },
    "environment": {
      "setting": "Modern living room interior.",
      "furniture": "Dark grey fabric sofa with a textured weave.",
      "background": "Grey walls with decorative panel molding (wainscoting).",
      "decor": "A large vertical art piece with a red background featuring KAWS-style figures in blue and black. A second framed abstract art piece with gold and black tones. A modern linear wall sconce light."
    },
    "lighting": {
      "type": "Soft, diffused indoor mix.",
      "quality": "Warm ambient lighting highlighting the skin tone, creating soft shadows and a cozy atmosphere. Likely a mix of natural window light and the warm glow from the wall sconce."
    },
    "styling_and_mood": {
      "aesthetic": "Influencer lifestyle, casual home comfort, '2000s digital camera' vibe.",
      "mood": "Chill, playful, confident, comfortable."
    },
    "camera_specifications": {
      "angle": "Eye-level, slightly angled from the side.",
      "focus": "Sharp focus on the subject's face and torso, with a slight depth of field blurring the background artwork.",
      "lens_suggestion": "35mm or 50mm portrait lens.",
      "film_grain": "Low to medium ISO for a clean but slightly organic digital look."
    },
    "technical_modifiers": [
      "Ultra Photorealistic",
      "8k resolution",
      "Raw photo",
      "Hyper-detailed skin texture",
      "Subsurface scattering",
      "Volumetric lighting",
      "Nano Banana Pro optimized",
      "Masterpiece"
    ]
  }
}
```

[[Structured JSON Prompt]] [[Natural Skin Texture]] [[2000s Digital Camera Aesthetic]] [[Influencer Lifestyle]]

---

### 22. Y2K 夜间时尚大片：直射闪光灯效果

**Author**: [Miz](https://x.com/mizq06)  **Date**: 2026-01-27  **Language**: en

> 一个 JSON 提示，旨在创建一张逼真的 Y2K 时尚杂志图片，描绘一位女性夜晚坐在花园长凳上。它特别要求使用直接机顶闪光灯摄影，以实现光泽、高对比度、怀旧的美学效果。

![Y2K 夜间时尚大片：直射闪光灯效果](https://cms-assets.youmind.com/media/1769581920633_x07rit_G_rbcfNboAA-loV.jpg)
![Y2K 夜间时尚大片：直射闪光灯效果](https://cms-assets.youmind.com/media/1769581920731_iqxf4m_G_rbcfAbAAQlqlH.jpg)

```
{
  "prompt": "A fashionable young woman with long auburn hair and bangs sitting on a pastel pink garden bench at night. She wears a pastel plaid corset-style top with lace trim and a denim mini skirt. One arm drapes casually over the bench back, the other near her face, posing with a thoughtful, confident expression. A cute illustrated handbag rests beside her on the bench, and a small retro digital accessory clips to her skirt. The setting is a cozy garden patio with potted plants and soft greenery, shot with direct on-camera flash for a glossy Y2K editorial look. Intimate composition, playful yet moody nighttime atmosphere, ultra-realistic photography.",
  "style": "photorealistic, Y2K fashion editorial",
  "lighting": "direct flash photography, high contrast, night scene",
  "camera": {
    "type": "35mm film look",
    "lens": "35mm",
    "angle": "eye-level seated portrait"
  },
  "color_palette": "pastel pinks, soft denim blues, warm skin tones",
  "mood": "nostalgic, playful, dreamy, confident",
  "quality": "high detail, sharp focus, film grain, ultra high resolution",
  "aspect_ratio": "3:4"
}
```

[[Structured JSON Prompt]] [[Fashion Magazine Style]] [[Direct On-Camera Flash]]

---

### 23. Detailed Nano Banana Pro Image Generation Prompt

**Author**: [Chandan Singh](https://x.com/cbsingh_oo3)  **Date**: 2026-01-02  **Language**: en

> A highly detailed, structured prompt designed for the Nano Banana Pro image generation tool, specifying comprehensive metadata, spatial orientation, camera optics, environment physics, scene text OCR, and object/actor properties for a mirror selfie scene. This prompt is intended for generating a specific, complex visual scenario with precise technical controls.

![Detailed Nano Banana Pro Image Generation Prompt](https://cms-assets.youmind.com/media/1767508434685_9f9hv0_G9qx3xVaQAAwpv2.jpg)

```
{
  "meta": {
    "analysis_timestamp": "2026-01-02T20:39:50+05:30",
    "target_tool": "Nano Banana Pro",
    "image_dna": {
      "type": "Photo",
      "orientation_lock": "LOCKED: Orientation preserved 1:1",
      "sensor_emulation": "iPhone 14/15 Pro Main Camera"
    }
  },
  "spatial_orientation_engine": {
    "subject_facing_direction": "CAMERA (Front) - via Mirror Reflection",
    "body_rotation": "Subject is standing with back to the mirror, twisted to the LEFT to look over left shoulder. Glutes facing camera.",
    "camera_position_relative": "Mirror Selfie: Camera is virtually located at mirror surface, reflection shows subject from rear-oblique angle."
  },
  "camera_optics_and_geometry": {
    "lens_profile": {
      "focal_length": "24mm (Smartphone Wide)",
      "aperture": "f/1.7 (Moderate depth of field)",
      "lens_character": "Digital Sharpness with Smart HDR processing"
    },
    "optical_flaws": [
      "Mirror surface dust/smudges",
      "Slight perspective distortion on edges",
      "Digital noise in shadow areas"
    ]
  },
  "environment_and_physics": {
    "lighting_engine": {
      "primary_source": "Natural Daylight (Window on Right)",
      "radiosity_color_bleed": "Warm Tungsten lamp light reflecting on white walls and mixing with cool daylight on skin",
      "shadow_structure": "Soft ambient shadows on the left side of the room; contact shadows under the bag",
      "volumetrics": "Clear Air"
    },
    "surface_physics": {
      "weather_impact": "Indoor stable environment",
      "material_response": "High stretch fabric tension on shorts; specular highlights on plastic water bottle"
    }
  },
  "scene_text_ocr": {
    "detected": true,
    "content": [
      {
        "text": "{argument name=\"Water Bottle Brand\" default=\"Hydro Flask\"}",
        "location": "Water Bottle on bed",
        "font_style": "Sans-serif Logo"
      },
      {
        "text": "{argument name=\"Time on Clock\" default=\"1:00\"}",
        "location": "Digital Clock on nightstand",
        "font_style": "Digital 7-segment"
      }
    ]
  },
  "objects_and_actors": [
    {
      "id": "MAIN_SUBJECT",
      "role": "Identity Swap Target",
      "pose_engineering": {
        "skeletal_rig": "Standing upright, weight shifted to right leg, hips rotated slightly away, torso twisted left, head turned left looking at phone.",
        "gaze_vector": "Eyes looking at phone screen in mirror reflection.",
        "interaction_physics": "Right hand gripping phone, left arm relaxed by side."
      },
      "physiological_state": {
        "body_temp_visuals": "Neutral/Resting",
        "skin_light_interaction": "Soft daylight highlight on right arm and leg; warm lamp rim light on left profile."
      },
      "clothing_simulation": {
        "garment_stack": "{argument name=\"Clothing Description\" default=\"black Baseball Cap (Backwards), Black Sports Bra (Dream white) Grey Marl Booty Shorts\"}",
        "fabric_mechanics": "High tension on shorts over glutes, elastic compression on sports bra straps.",
        "texture_and_wear": "Heathered texture on grey s"
```

[[Structured JSON Prompt]] [[Mirror Selfie Photography]] [[Technical Camera Specification]]

---

### 24. Nano Banana Prompt: Cozy Storybook Illustration Style

**Author**: [Adam也叫吉米](https://x.com/Adam38363368936)  **Date**: 2026-01-02  **Language**: en

> This is a detailed JSON-formatted prompt designed for image generation, specifically to create illustrations in a 'Cozy Storybook Illustration' style, mimicking the look of colored pencils and subtle watercolor washes. It includes two specific prompt variations, one focusing on texture and stroke, and another on mixed media watercolor effects. This prompt is intended for style transfer based on an uploaded image.

![Nano Banana Prompt: Cozy Storybook Illustration Style](https://cms-assets.youmind.com/media/1767508483760_7ft64i_G9n66mFaMAA1VyF.jpg)
![Nano Banana Prompt: Cozy Storybook Illustration Style](https://cms-assets.youmind.com/media/1767508483761_ve12nq_G9n67P8aMAIxapE.jpg)

```
{
  "design_system": {
    "metadata": {
      "style_name": "Cozy Storybook Illustration",
      "target_audience": "Children / Family",
      "reference_source": "Uploaded Image",
      "version": "3.0"
    },
    "visual_parameters": {
      "medium": {
        "primary": "Colored Pencil",
        "secondary": "Watercolor Wash (Variation only)",
        "application": "Hand-drawn",
        "texture": {
          "type": "Visible pencil strokes",
          "quality": "Slightly rough outlines",
          "finish": "Non-realistic / No photo texture"
        }
      },
      "line_work": {
        "style": "Clean line art",
        "weight": "Slightly rough/organic",
        "clarity": "High"
      },
      "color_theory": {
        "base_tone": "Warm and friendly",
        "palette_type": "Vibrant Pastel",
        "adjustments": {
          "brightness": "Increased / High-key",
          "saturation": "Enhanced but natural",
          "contrast": "Soft"
        }
      },
      "lighting_and_shading": {
        "shadows": "Minimal",
        "highlights": "Soft",
        "rendering": "Flat yet detailed",
        "gradients": "Subtle watercolor layers (Variation only)"
      }
    },
    "subject_geometry": {
      "anatomy": {
        "proportions": "Semi-cartoon realistic",
        "scale": "Storybook style"
      },
      "facial_features": {
        "eyes": "Dot style",
        "mouth": "Small smile",
        "complexity": "Simple / Minimalist"
      }
    },
    "atmosphere": {
      "mood": [
        "Cozy",
        "Cheerful",
        "Warm",
        "Friendly"
      ],
      "genre_tags": [
        "Children's Book",
        "Lifestyle Sketch",
        "Storybook Illustration"
      ]
    }
  },
  "generation_configs": {
    "negative_prompt_tokens": [
      "realism",
      "photorealistic",
      "photo texture",
      "dark colors",
      "complex shading",
      "3d render"
    ],
    "prompt_variations": [
      {
        "id": "PROMPT_001",
        "variant_name": "Textured Colored Pencil",
        "focus": "Texture and Stroke",
        "full_text": "Illustration style: hand-drawn colored pencil illustration, clean line art with slightly rough pencil outlines, soft pastel coloring with increased brightness, lighter and more vivid color tones, enhanced saturation while staying natural, visible pencil strokes and gentle shading texture, warm and friendly tone, semi-cartoon realistic proportions, simple facial features with dot eyes and small smiles, flat yet detailed coloring, minimal shadows, soft highlights, storybook illustration feel, cozy and cheerful atmosphere, vibrant yet soft color palette, children-book / lifestyle sketch style, high clarity, no realism, no photo texture"
      },
      {
        "id": "PROMPT_002",
        "variant_name": "Mixed Media Watercolor",
        "focus": "Wash and Gradient",
        "full_text": "{argument name="full text 2" default="Illustration style: hand-drawn colored pencil illustration, clean line art with slightly rough pencil outlines, soft pastel coloring with increased brightness, lighter and more vivid color tones, enhanced saturation while staying natural, visible pencil strokes and gentle shading texture, warm and friendly tone, semi-cartoon realistic proportions, simple facial features with dot eyes and small smiles, flat yet detailed coloring, minimal shadows, soft highlights, storybook illustration feel, cozy and cheerful atmosphere, vibrant yet soft color palette, children-book / lifestyle sketch style, high clarity, no realism, no photo texture"}"
      }
    ]
  }
}
```

[[Structured JSON Prompt]] [[Style Transfer]]

---

### 25. Detailed JSON prompt for a casual portrait of a young woman in a sports jersey

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-01-02  **Language**: en

> This is an extremely detailed JSON-formatted prompt designed for image generation, specifying every aspect of a casual, close-up portrait. It covers composition, subject details (gender, age, facial features, hair, clothing), lighting, color palette, background, and technical camera details to achieve a clean, natural lifestyle aesthetic.

![Detailed JSON prompt for a casual portrait of a young woman in a sports jersey](https://cms-assets.youmind.com/media/1767508428291_6lu060_G9nuTXiaoAAZyBy.jpg)

```
{ "image_type": "photograph", "genre": "casual portrait", "composition": { "framing": "close-up, chest-up portrait", "angle": "slightly tilted, camera held above eye level and angled downward", "orientation": "portrait with diagonal tilt", "subject_placement": "subject positioned slightly off-center, face occupying left-middle area", "crop": "tight crop with partial arm visible in foreground" }, "subject": { "count": 1, "gender_presentation": "{argument name="gender presentation" default="female-presenting"}", "age_range": "young adult", "facial_features": { "skin_tone": "light, neutral-warm", "complexion": "clear, smooth with natural texture", "eyes": "light green/gray, almond-shaped", "eyebrows": "medium thickness, natural shape", "nose": "straight, small to medium", "lips": "natural pink, closed-mouth slight smile" }, "hair": { "color": "dark brown", "length": "long", "style": "straight, tucked behind ear on one side", "part": "slight side part" }, "expression": "soft, relaxed, friendly", "gaze": "looking directly into camera", "accessories": [ "small silver stud earrings" ], "clothing": { "type": "sports jersey", "fit": "loose athletic fit", "color": "{argument name="jersey color" default="white with black accents"}", "details": [ "black collar trim", "black logos and text", "shield-style emblem on chest", "large curved black graphic text" ] } }, "lighting": { "type": "natural light", "direction": "side/front light from window", "quality": "soft, diffused", "shadows": "minimal, gentle", "highlights": "subtle skin highlights on cheek and forehead" }, "color_palette": { "dominant_colors": [ "white", "soft gray", "black" ], "accent_colors": [ "natural skin tones", "brown hair" ], "overall_tone": "neutral, clean, airy" }, "background": { "setting": "indoor", "elements": [ "sheer white curtains", "window frame partially visible" ], "depth_of_field": "moderate, background slightly soft but recognizable", "style": "minimalist, uncluttered" }, "technical_details": { "camera_type": "DSLR", "focal_length_equivalent": "wide-angle selfie lens", "resolution": "high", "sharpness": "sharp focus on face", "noise": "minimal", "white_balance": "neutral" }, "artistic_style": { "aesthetic": "clean, natural, lifestyle", "retouching": "very minimal, natural skin texture preserved", "mood": "calm, approachable, casual" }, "typography": { "presence": true, "location": "on jersey", "style": "bold sans-serif sports branding", "color": "black", "readability": "partially visible due to crop" } }
```

[[Structured JSON Prompt]]

---

### 26. 红色缎面连衣裙时尚肖像提示（JSON 格式）

**Author**: [Adam也叫吉米](https://x.com/Adam38363368936)  **Date**: 2026-01-01  **Language**: en

> 一个为 Nano Banana Pro 设计的结构化 JSON 提示，用于生成一张身穿深绯红色缎面迷你连衣裙的年轻女性的高级时尚写实肖像。场景设定在宏伟的维多利亚/古典博物馆内部，主体倚靠在白色石质栏杆旁。提示中指定了技术细节，例如平视全身镜头、柔和的室内自然光以及电影般的构图。

![红色缎面连衣裙时尚肖像提示（JSON 格式）](https://cms-assets.youmind.com/media/1767508398565_21yq37_G9jFPxmasAAou-5.jpg)

```
{Use the face without any change.
  "image_generation_prompt": {
    "subject": {
      "type": "Young woman",
      "hair": "Long, dark brunette, loose waves, parted in the middle",
      "pose": "Standing full-body, leaning backwards against a stone balustrade, one hand resting on the railing, legs crossed at the ankles, looking down/away candidly",
      "expression": "{argument name="expression" default="Neutral, elegant, contemplative"}"
    },
    "attire": {
      "dress": "{argument name="dress color" default="Deep crimson red"} satin mini dress, fit-and-flare silhouette, plunging V-neckline, spaghetti straps, tiered ruffled skirt",
      "shoes": "Dark plum or black pointed-toe high heels",
      "accessories": "Simple drop earrings"
    },
    "environment": {
      "setting": "Grand museum interior (Victorian/Classical architecture)",
      "foreground": "White stone balcony with a decorative balustrade (railing) featuring classic balusters",
      "background": "Large white architectural arches with detailed molding, an ornate Gothic Revival metal and gold choir screen visible in the distance",
      "flooring": "Parquet wood flooring"
    },
    "technical_specs": {
      "lighting": "Soft natural indoor light, diffuse and even, daylight ambience",
      "camera_angle": "Eye-level, full shot",
      "style": "High-fashion lifestyle photography, photorealistic, cinematic composition, crisp focus"
    }
  }
}
```

[[Structured JSON Prompt]] [[High Fashion Editorial]] [[Full Body Shot]]

---

### 27. 超精细肖像，带有“祈祷之手”姿势提示

**Author**: [PlayForge AI](https://x.com/94vanAI)  **Date**: 2026-01-01  **Language**: en

> 一个高度具体、结构化的 JSON 提示，专为 Nano Banana Pro 设计，旨在生成一张超专业的中画幅影棚肖像。该提示聚焦于一个带着顽皮、恳求表情的小女孩，她做出“祈祷之手”的姿势，交错的手指部分遮住了嘴巴。提示中包含了关于灯光、皮肤纹理、时尚（超大粉色眼镜、特定服装）的详细描述，以及严格的负面提示，以确保真实感和高质量。

![超精细肖像，带有“祈祷之手”姿势提示](https://cms-assets.youmind.com/media/1767508401214_l052mz_G9icPJnaMAI3TVa.jpg)
![超精细肖像，带有“祈祷之手”姿势提示](https://cms-assets.youmind.com/media/1767508401290_7caorf_G9icPJob0AAkQVV.jpg)

```
{
  "positive_prompt": "Ultra-professional medium format studio portrait photograph, first person POV close-up upper body portrait, very petite short 18-year-old white girl standing directly in front of viewer, looking up with big sparkling light blue eyes pleading and begging desperately, praying hands / prayer hands with fingers tightly interlocked and crossed, clasped into fists, ten fingers visibly crossed and gripping each other firmly in front of chest, hands slightly raised partially covering chin and mouth, NO flat palms pressed together, playful shy coy smile with adorable giggling expression, praying hands / prayer hands with fingers interlocked and fists clasped position partially covering mouth, flawless smooth perfect youthful fair skin with microscopic natural pores and delicate warm subtle glow, cute delicate sweet face with soft rounded features, bright sparkling eyes, small straight nose, full soft lips, innocent charming aura, shimmering platinum-blonde hair in symmetrical high twin buns hairstyle (space buns, two high vertical neat buns pointing upward), large oversized round transparent pink-gradient tinted acetate glasses with soft pink sheen frame, hourglass figure with dramatically exaggerated voluptuous wide hips and above-average full bust, very short stature appearing tiny in frame, wearing inner white shirt with light gray vertical stripes (collar featuring small cute cartoon patterns), outer pink round-neck fine vertical stripe wool sweater (stripes are vertical), tight-fitting clothes hugging and accentuating exaggerated curves, soft natural diffused studio lighting with gentle highlights on skin hair glasses and fabric, perfect symmetrical centered composition, dreamy Wes Anderson inspired flat aesthetic, low saturation soft pastel color palette dominant pinks blues yellows, vintage analog sweet nostalgic mood, captured with Hasselblad H6D-400c multi-shot 400MP or Phase One XF IQ4 150MP medium format camera, extreme razor-sharp resolution, cinematic depth of field, 16-bit color depth, incredible dynamic range, hyper-detailed skin fabric hair and especially hand texture, masterpiece, ultra high quality, 8k",
  "negative_prompt": "blurry, lowres, noise, grain, artifacts, deformed anatomy, bad proportions, extra limbs, mutated hands, poorly drawn face, fused fingers, missing fingers, extra fingers, watermark, text, signature, overexposed, underexposed, harsh shadows, harsh lighting, heavy makeup, wrinkles, aged skin, freckles too many, jet black hair, dark hair, any hair color except platinum-blonde, low twin buns, low ponytails, down hairstyle, loose hair, different glasses, no glasses, asymmetrical buns, tilted buns, different hair color, hands flat together palms pressed without interlocked fingers, palms only pressed together, palms merged or joined flat, simple palm合十,"
}
```

[[Structured JSON Prompt]] [[Studio Portrait]] [[Playful Expression]]

---

### 28. Nano Banana Pro 的超逼真卡通现实场景提示词

**Author**: [Özge](https://x.com/astronomerozge1)  **Date**: 2025-12-30  **Language**: en

> 这是一个高度详细、结构化的 JSON 提示，专为 Nano Banana Pro 工具设计，用于生成一个超逼真的场景。该场景描绘了一位真实的女性在一个逼真的家庭厨房环境中与完全卡通风格的蓝精灵互动，强调了场景的逼真度与蓝精灵的卡通性质之间的鲜明对比。它包含具体的硬性约束、相机设置和详细的场景描述，以确保高质量、特定的输出。

![Nano Banana Pro 的超逼真卡通现实场景提示词](https://cms-assets.youmind.com/media/1767455013664_tm63jh_G9brf5-X0AIEdOU.jpg)

```
{
  "request_metadata": {
    "tool": "NanoBananaPro",
    "task_type": "ultra_photoreal_cartoon_reality_scene",
    "quality_preset": "ultra",
    "aspect_ratio": "16:9"
  },
  "references": {
    "main_reference_image": {
      "slot": 1,
      "purpose": "MAIN_SUBJECT_IDENTITY_LOCK",
      "strict_identity_lock": true
    }
  },
  "hard_constraints": [
    "ONE real human only (female).",
    "All other characters are cartoon characters only.",
    "Smurfs remain fully cartoon-styled (flat toon shading + clean outlines).",
    "Papa Smurf MUST have a red hat and red pants (classic Smurf canon colors).",
    "Real home kitchen, photoreal environment.",
    "Max 6 Smurfs total (including Smurfette and Papa Smurf).",
    "No BTS, no studio, no readable text, no logos, no watermarks.",
    "Ultra-sharp image: no blur, no soft focus, no haze, no motion blur."
  ],
  "camera": {
    "camera_style": "premium natural lifestyle photo",
    "camera_body": "full-frame professional camera",
    "lens": "24mm prime",
    "aperture": "f/4",
    "shutter_speed": "1/200",
    "iso": "100",
    "focus": "tack_sharp on the woman's eyes",
    "depth_of_field": "moderate-to-deep (cake + smurfs + woman all sharp)",
    "white_balance": "soft daylight",
    "lighting_notes": "bright window daylight + soft bounce fill for a clean, high-end kitchen look"
  },
  "prompt": {
    "scene_summary": "A real home kitchen filled with clean daylight, shot like a premium lifestyle cover. A woman prepares a forest-berry cake at the counter. She wears a chic pink strawberry-print dress with tiny strawberries on the fabric, a pink bandana tied in her hair, and small strawberry hair accessories subtly placed throughout her hairstyle. Smurfette and five Smurfs help playfully: one stirring berries, one standing inside a mixing bowl, one carrying strawberries, one holding a whisk, one sprinkling powdered sugar, and Papa Smurf supervising confidently. Papa Smurf is clearly identifiable with his classic red hat and red pants. All Smurfs are small, blue, and fully cartoon-styled, sharply contrasting with the photorealistic kitchen and the real woman. The image is crisp, joyful, high-quality, and perfectly sharp."
  },
  "negative_prompt": [
    "extra humans",
    "realistic smurf skin",
    "semi-realistic smurfs",
    "wrong colored papa smurf clothing",
    "text",
    "logo",
    "watermark",
    "film set",
    "studio",
    "boom mic",
    "camera rig",
    "blur",
    "soft focus",
    "haze",
    "motion blur",
    "deformed hands",
    "extra fingers"
  ]
}
```

[[Structured JSON Prompt]] [[Kitchen Setting]]

---

### 29. Avatar Zuko 粉丝照片提示，适用于 Nano Banana Pro

**Author**: [Jennie](https://x.com/PurelyJennie)  **Date**: 2025-12-30  **Language**: en

> 一个用于 Nano Banana Pro 的结构化 JSON 提示，指示其生成一张超现实图像，描绘一个主体与《降世神通：最后的气宗》中巨大的 2D 祖寇角色摆拍。

![Avatar Zuko 粉丝照片提示，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1767455071473_bev27t_G9boq29WEAgpDKY.jpg)

```
[
  {
    "image_generation": {
      "quality": "hyper-realistic",
      "face": { "preserve_original": true },
      "subject": {
        "clothing": "{argument name="clothing" default="dark red knitted sweater, dark brown sweatpants with yellow vertical lines on the sides, brown high-top sneakers"}",
        "pose": "standing with arm around giant 2D Zuco from avatar",
        "expression": "fun, mischievous",
        "character_element": {
          "name": "Zuco",
          "type": "3D & 2D photorealistic duo",
          "interaction": "Zuco posing confidently"
        }
      },
      "environment": "clean light green backdrop"
    }
  }]
```

[[Structured JSON Prompt]] [[Surreal Portrait]]

---

### 30. 生成斜倚女性图像的详细 JSON 提示

**Author**: [cinema 🎥](https://x.com/FilmHub00)  **Date**: 2025-12-30  **Language**: en

> 这是一个高度结构化的 JSON 提示词，专为图像生成模型（Gemini Nano Banana Pro）设计，详细说明了主体的复杂细节，包括性别、头发、皮肤、眼睛、姿势、配饰、服装、场景和光照。这种详细程度通常是实现精确视觉效果的关键。

![生成斜倚女性图像的详细 JSON 提示](https://cms-assets.youmind.com/media/1767455025235_132hxx_G9aE7TfboAA_dEw.jpg)

```
{
  "subject": {
    "gender": "{argument name="gender" default="female"}",
    "hair": {
      "color": "{argument name="hair color" default="light brown with blonde highlights"}",
      "style": "long, straight, center part",
      "length": "extending past shoulders"
    },
    "skin": {
      "tone": "fair",
      "texture": "smooth"
    },
    "eyes": {
      "makeup": "eyeliner, mascara",
      "gaze": "looking to the side, away from camera"
    },
    "pose": {
      "position": "reclining/sitting on a sofa",
      "body_orientation": "angled slightly",
      "hands": {
        "left_hand": "holding strap/top of bra",
        "right_hand": "holding strap/top of bra",
        "tattoos": {
          "right_hand_back": "small text/numbers including '666' and stars",
          "right_wrist": "small symbol",
          "left_wrist": "small heart outline"
        }
      }
    },
    "accessories": {
      "jewelry": [
        "thin gold necklace",
        "gold ring on right ring finger",
        "navel piercing with barbell jewelry"
      ]
    }
  },
  "clothing": {
    "top": {
      "type": "bralette/crop top",
      "color": "white",
      "material": "cotton or jersey blend with lace",
      "details": "lace trim on bottom hem, ruched center bust, spaghetti straps"
    },
    "bottom": {
      "type": "shorts/boy shorts",
      "color": "red and white",
      "pattern": "horizontal stripes",
      "details": "small white bow at center waist, elastic waistband"
    }
  },
  "setting": {
    "location": "indoor",
    "furniture": "{argument name="furniture" default="large beige/tan sofa or couch"}",
    "background_elements": [
      "coffee table books in upper right corner",
      "dark/black area behind sofa"
    ]
  },
  "lighting": {
    "type": "soft indoor lighting",
    "shadows": "soft shadows suggesting diffuse light source"
  }
}
```

[[Structured JSON Prompt]]

---

### 31. 静奢风职场女性穿搭指南提示词（3 种变体）

**Author**: [web3btc🧠SENT](https://x.com/web3btc)  **Date**: 2025-12-30  **Language**: zh

> 一套为 Nano Banana Pro 设计的三个高度结构化提示，旨在生成“静奢风”或“老钱风”办公室着装的时尚型录图片。每个提示都指定了模特（年轻的丹麦女性）、调色板、材质（亚麻混纺）、特定服装类型、配饰，以及包含多个视角（七点拍摄、全身、细节）的杂志版式构图。

![静奢风职场女性穿搭指南提示词（3 种变体）](https://cms-assets.youmind.com/media/1767166985361_xkvc4q_G9Yvkx6aYAAup1U.jpg)
![静奢风职场女性穿搭指南提示词（3 种变体）](https://cms-assets.youmind.com/media/1767166985600_xleate_G9YvluQbYAAHymP.jpg)
![静奢风职场女性穿搭指南提示词（3 种变体）](https://cms-assets.youmind.com/media/1767166985832_1l01jc_G9YvmnKa0AAa8PY.jpg)
![静奢风职场女性穿搭指南提示词（3 种变体）](https://cms-assets.youmind.com/media/1767166987453_1np3uq_G9Yvnw4boAAcZc6.jpg)

```
主体 (Subject): 年轻Danmark丹麦女性，金色长卷发，妆容自然清透，气质优雅、知性。

服装 (Outfit): 核心是“静奢风 (Quiet Luxury)”或“老钱风”。

色调: pantone 15-4504TCX/ Nacreous Clouds 低饱和度。

材质: 亚麻或亚麻混纺 (Linen blend)，有自然的褶皱纹理。

款式: 三件套——廓形西装外套 (Blazer) + 同色系吊带内搭 (Camisole) + 裹身半身长裙 (Wrap midi skirt)。

配饰 (Accessories): 棕色手提包 (卡其色/焦糖色)，金色细项链，丝巾（在平铺图中）。

构图与风格 (Composition & Style):

时尚杂志排版 (Magazine Layout / Collage)。

多视角展示：主图是七分身，侧边有全身照、背影细节、局部特写。

背景：干净的摄影棚白底/灰底 (Clean studio background)。

文字：极简主义排版 (Minimalist typography)。

==============================

主体 (Subject): 年轻Danmark丹麦女性，红棕色长卷发，妆容自然清透，气质优雅、知性。

服装 (Outfit): 核心是“静奢风 (Quiet Luxury)”或“老钱风”。

色调: Pantone 18-1018TCX/ Otter 低饱和度。

材质: 亚麻或亚麻混纺 (Linen blend)，有自然的褶皱纹理。

上装: linen blazer, asymmetric closure, tailored fit (亚麻西装，不对称闭合，剪裁合身).

下装: pleated wide-leg pants (褶皱阔腿裤).

配饰: Brown square-toe flats, mini leather top-handle bag (棕色方头平底鞋，迷你手提皮包).

构图与风格 (Composition & Style): 时尚杂志排版 (Magazine Layout / Collage)。

多视角展示：主图是七分身，侧边有全身照、背影细节、局部特写。

背景：干净的摄影棚白底/灰底 (Clean studio background)。

文字：极简主义排版 (Minimalist typography)。

=====================================

这是一个典型的**时尚型录（Lookbook）**或电商详情页排版。

主图： 左侧占据大面积的是模特的半身/七分身展示。

辅图： 右侧垂直排列三张小图，分别、全身远景、背面视角、服装平铺展示。

静物： 右下角有配饰的平铺展示（包、丝巾、耳环）。

文字： 上下留白处有简约的排版文字（品牌名、季节、Slogan）。

主体 (Subject): 年轻Danmark丹麦女性，金色长发，妆容自然清透，气质优雅、知性。

服装 (Outfit): 老钱风（Old Money）、静奢风（Quiet Luxury）、极简主义（Minimalism)

色调: Pantone 15-1116 TCX/ Safari 低饱和度。

材质: 亚麻或亚麻混纺 (Linen blend)，有自然的褶皱纹理。

外套：无领西装外套/开衫，剪裁利落，亚麻质感。

内搭：炭灰色丝绸/缎面 V领衬衫。

下装： 西装裤。
```

[[Structured JSON Prompt]] [[Old Money Aesthetic]]

---

### 32. 详细解剖姿势研究（室内家居服）

**Author**: [laurababy](https://x.com/laurababyai)  **Date**: 2025-12-29  **Language**: en

> 一个极其详细的 JSON 提示，重点关注主体的精确姿势、体重分布和解剖学对齐（骨盆倾斜、脊柱前凸），并结合对服装和现代室内环境的具体描述，旨在实现超逼真的输出。

![详细解剖姿势研究（室内家居服）](https://cms-assets.youmind.com/media/1767166961019_iqw8jl_G9XVQElWgAAuiFw.jpg)

```
{
  "subject_description": {
    "demographics": "Young woman, early 20s, tan skin tone, slim athletic build.",
    "hair": "Long, dark brown/black hair, loose waves, center part, draping over shoulders and back.",
    "face": "Oval face shape, full lips, neutral expression with slight pout, direct eye contact with lens. Subtle makeup with visible highlighter on nose bridge and cheeks.",
    "accessories": "Gold chain necklace with a rectangular pendant, small hoop earrings.",
    "clothing": {
      "top": "Black strapless tube top, tight fit, brown text graphic reading '{argument name="graphic text" default="HAWAIIAN Tropic™"}' centered on chest.",
      "bottoms": "White lounge shorts, soft fabric, brown hibiscus flower print on left thigh (viewer's left), elastic waistband.",
      "fit": "Snug, revealing midriff/navel, casual loungewear aesthetic."
    }
  },
  "pose_geometry": {
    "spine_and_pelvis": {
      "pelvic_tilt": "Significant lateral pelvic tilt (hip hike) to subject's right (viewer's left).",
      "lumbar_curve": "Natural lordosis exaggerated by hip pop.",
      "alignment": "Torso slightly rotated towards viewer's left, hips angled."
    },
    "weight_distribution": {
      "primary_load": "90% weight on subject's right leg (straightened, locked hip).",
      "secondary_load": "Left leg relaxed, slightly bent at knee, foot positioned forward.",
      "visual_impact": "Distinct asymmetrical silhouette, creating a curve from hip to shoulder."
    },
    "limbs": {
      "arms": "Right arm (viewer's left) obscured/hanging by side. Left arm (viewer's right) bent at elbow, hand placed on waist/upper hip, creating a triangular gap between arm and torso.",
      "shoulders": "Shoulders relaxed but slightly uneven due to hip stance, left shoulder (viewer's right) slightly lower."
    }
  },
  "environment_context": {
    "setting": "Modern apartment interior, living room area.",
    "background_elements": [
      "Large flat-screen TV mounted on white wall (left).",
      "Dark wood media console/credenza beneath TV.",
      "White vase with fluffy pampas grass/dried plumes on console.",
      "Open white doorway in background center.",
      "Vertical wood slat acoustic paneling on wall (right side).",
      "White smoke detector on ceiling."
    ],
    "flooring": "Glossy large-format white tiles, reflecting light and shadows."
  },
  "lighting_physics": {
    "source": "Natural daylight from large window (off-screen left).",
    "quality": "Soft, diffused, directional side lighting.",
    "shadows": "Soft shadows cast to the right of the subject and objects; shadow of subject visible on the floor.",
    "highlights": "Sheen on skin (shoulders, face), reflections on glossy floor tiles, glare on TV screen."
  },
  "color_behavior": {
    "palette": "Neutrals (white, black, beige, wood tones) with tan skin tones.",
    "saturation": "Natural, slightly warm tones from wood and skin.",
    "white_balance": "Daylight bala"
  }
}
```

[[Structured JSON Prompt]] [[Hyperrealistic Photography]]

---

### 33. 超逼真室内肖像 (Hawaiian Tropic)

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-29  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超逼真的、高角度拍摄的年轻女性照片，场景设定在现代室内，详细说明了她的外貌、服装（包括一件印有“HAWAIIAN TROPIC”字样的上衣）、灯光和相机风格。

![超逼真室内肖像 (Hawaiian Tropic)](https://cms-assets.youmind.com/media/1767166958163_alw2qb_G9Wx32oa4AA37uP.jpg)

```
{
  "image_details": {
    "subject": {
      "appearance": {
        "gender": "female",
        "age_group": "young adult",
        "hair": {
          "color": "blonde",
          "style": "long, wavy",
          "parting": "center"
        },
        "face": {
          "complexion": "fair, freckled",
          "eyes": "dark",
          "makeup": "natural, light mascara, pink blush, glossy lips"
        },
        "expression": "slight smile, looking at camera"
      },
      "pose": {
        "type": "high-angle shot",
        "stance": "standing, slight twist",
        "arms": "one arm back, one hand near hip"
      },
      "attire": {
        "top": {
          "type": "tube top",
          "color": "black",
          "graphic": "brown '{argument name="graphic text" default="HAWAIIAN TROPIC"}' text"
        },
        "bottoms": {
          "type": "shorts",
          "color": "white",
          "graphic": "brown hibiscus flower"
        },
        "accessories": {
          "necklace": "gold pendant chain"
        }
      }
    },
    "environment": {
      "location": "modern indoor living space",
      "background": {
        "elements": [
          "large dark TV screen",
          "dark wood media console",
          "vase with white fluffy plants",
          "vertical wooden slatted wall panel",
          "white tiled floor",
          "doorway"
        ]
      }
    },
    "lighting": {
      "source": "natural sunlight",
      "direction": "from the side (right)",
      "quality": "bright, warm, casting soft shadows"
    },
    "mood": "relaxed, confident, casual, sunny",
    "photography_style": {
      "type": "ultra-photorealistic",
      "camera_details": {
        "shot_type": "high-angle",
        "focus": "sharp on subject",
        "resolution": "high",
        "color_palette": "warm, natural"
      }
    }
  }
}
```

[[Structured JSON Prompt]] [[Hyperrealistic Photography]] [[High Angle Shot]]

---

### 34. 结构化坦率室内肖像提示

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2025-12-07  **Language**: en

> 一个高度详细、结构化的 JSON 提示，用于 Gemini Nano Banana Pro，旨在生成一张逼真、自然的室内照片，照片中是一位穿着特定款式服装（白色做旧针织毛衣）的年轻男士，并具有特定的灯光条件，强调真实感和时尚美学。

![结构化坦率室内肖像提示](https://cms-assets.youmind.com/media/1765421925839_om4cb0_G7iaZhnaIAEiL-k.jpg)

```
{
  "Objective": "Generate a realistic indoor candid photograph of the subject based on the provided reference image.",
  
  "Identity_Safety": "Maintain facial features, hairstyle, and appearance consistent with the provided reference image.",

  "Subject": {
    "Appearance": {
      "Age": "{argument name="age" default="Young man"}",
      "Hair": "Naturally tousled black hair framing the face softly",
      "Expression": "Calm, casual, candid moment"
    },
    "Pose": {
      "Body_Position": "Sitting at a desk in front of an open laptop",
      "Hands": {
        "Right_or_Left": "Holding an {argument name="phone model" default="iPhone 16 Pro"} as if checking something or capturing a mirror-style selfie"
      },
      "Vibe": "Realistic, relaxed, effortlessly cool"
    },
    "Wardrobe": {
      "Sweater": {
        "Type": "{argument name="sweater type" default="White distressed knit sweater"}",
        "Details": "Oversized fit with small rips, loose threads, and frayed texture for a trendy casual look"
      }
    }
  },

  "Scene_Description": {
    "Environment": {
      "Setting": "Indoor workspace or cozy room",
      "Desk": "Simple desk with an open laptop in front of the subject",
      "Lighting": {
        "Type": "Soft natural or warm indoor lighting",
        "Effects": [
          "Gentle highlights on facial features",
          "Subtle shadows for realism",
          "Clean candid feel"
        ]
      }
    },
    "Atmosphere": "Authentic, modern, slightly lifestyle-inspired candid moment"
  },

  "Visual_Style": {
    "Quality": "High-resolution realistic photo",
    "Aesthetic": "Candid indoor portrait with trendy fashion details",
    "Color_Profile": "Soft neutrals, clean whites, and natural skin tones",
    "Detail_Characteristics": [
      "Visible sweater texture and frayed knit details",
      "Realistic skin texture and hair definition",
      "Candid photographic depth of field"
    ]
  },

  "Output_Requirements": {
    "Format": "Image",
    "Orientation": "Portrait or medium close-up",
    "Quality": "Ultra-realistic, photography-grade rendering"
  }
}
```

[[Structured JSON Prompt]] [[Natural Lighting]] [[Men's Fashion Photography]]

---

### 35. 多彩人像拼贴提示词

**Author**: [Cherry 2.O](https://x.com/Mind_Boticni)  **Date**: 2026-04-06  **Language**: en

> 这是一个使用 Google Gemini Nano Banana Pro 生成 5 联幅多彩人像拼贴的提示词，包含时尚模特、单色背景以及现代编辑风格的鲜艳影棚灯光效果。

![多彩人像拼贴提示词](https://cms-assets.youmind.com/media/1775544737925_bb6k5p_HFOJpmWb0AAvsFn.jpg)

```
5 panel colorful portrait collage, fashion models, monochrome backgrounds ({argument name="background colors" default="pink, red, green, yellow"}), vibrant studio lighting, modern editorial style, rounded grid layout, high contrast, minimal shadows
```

[[Studio Lighting]] [[Editorial Style]]

---

### 36. 多彩人像拼贴提示词

**Author**: [Cherry 2.O](https://x.com/Mind_Boticni)  **Date**: 2026-04-06  **Language**: en

> 这是一个使用 Google Gemini Nano Banana Pro 生成 5 联幅多彩人像拼贴的提示词，包含时尚模特、单色背景以及现代编辑风格的鲜艳影棚灯光效果。

![多彩人像拼贴提示词](https://cms-assets.youmind.com/media/1775544737925_bb6k5p_HFOJpmWb0AAvsFn.jpg)

```
5 panel colorful portrait collage, fashion models, monochrome backgrounds ({argument name="background colors" default="pink, red, green, yellow"}), vibrant studio lighting, modern editorial style, rounded grid layout, high contrast, minimal shadows
```

[[Studio Lighting]] [[Editorial Style]]

---

### 37. Anya Taylor-Joy 高级时装编辑肖像

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-03-31  **Language**: en

> 这是一个为 Nano Banana 2 设计的高度结构化 JSON 提示词，旨在生成一张 Anya Taylor-Joy 身着校园风服装的超写实高级时装编辑图像，并详细指定了相机、光影、场景、姿势和构图细节。

![Anya Taylor-Joy 高级时装编辑肖像](https://cms-assets.youmind.com/media/1775026345775_co5xt1_HEvxodsbQAAlQpd.jpg)
![Anya Taylor-Joy 高级时装编辑肖像](https://cms-assets.youmind.com/media/1775026345751_0rm7ab_HEvxoJ6WYAAyXHj.jpg)
![Anya Taylor-Joy 高级时装编辑肖像](https://cms-assets.youmind.com/media/1775026347175_8djsc4_HEvxoRSXYAAy50a.jpg)

```
{
  “meta”: {
    “quality”: “ultra_photorealistic, raw style, 8k”,
    “camera”: “iPhone 15 Pro Max”,
    “lighting”: “bright, soft studio lighting, creating clean highlights on skin and sheer clothing texture”,
    “style”: “high-fashion editorial, single-person focus”,
    “aspect_ratio”: “9:16”
  },
  “scene”: {
    “location”: “A professional photography studio with a clean, seamless soft matte red cyclorama wall and floor.”,
    “atmosphere”: “Chic, confident, and playful.”
  },
  “subject”: {
    “gender”: “female”,
    “name”: “Anya Taylor-Joy”,
    “body”: {
      “type”: “Realistic, naturally proportioned fit figure”
    },
    “face”: {
      “features”: “Anya Taylor-Joy’s distinct features, including her dark blonde hair (styled loosely with slight waves), bright wide set eyes, and a bold look.”,
“expression”: “Confident and slightly playful, with a direct and alluring gaze toward the camera.”
    },
    “outfit”: {
      “description”: “White cropped short-sleeved collared shirt with a pink tie. Extremely short pleated pink ultra-mini skirt. Sheer white nylon or mesh knee-high socks, subtly showing skin texture. Pink patent leather stiletto heels.”,
      “fit”: “Tailored, modern, bold, schoolgirl-inspired.”,
      “accessory”: “None.”
    },
    “pose”: “Kneeling on the red floor, angled slightly in a light side profile pose towards the left, but turning her head to gaze directly at the camera. Her right hand is thoughtfully resting under her chin, and her left hand is resting naturally on her knee, maintaining a confident posture.”
  },
“composition”: “Medium full-body shot capturing Anya Taylor-Joy from the knees up. Sharp focus on the detailed textures of her clothing, especially the sheer socks and skirt pattern. The soft red background is seamless and clean, emphasizing the vibrant pink tones of the outfit.”
}
```

[[Studio Lighting]] [[Hyperrealistic Portrait]] [[Anya Taylor-Joy]]

---

### 38. 悉尼·斯威尼 (Sydney Sweeney) 相似面孔的影棚时尚摄影，躺在缎面床单上

**Author**: [Maya](https://x.com/mayadelmare)  **Date**: 2026-03-30  **Language**: en

> 一份详细的 JSON 提示词，供 Nano Banana 2 Pro 使用，旨在生成一张影棚时尚摄影作品。画面主体为一名酷似悉尼·斯威尼 (Sydney Sweeney) 的模特，以诱人的姿态躺在褶皱的白色缎面床单上，并包含特定的灯光和服装细节。

![悉尼·斯威尼 (Sydney Sweeney) 相似面孔的影棚时尚摄影，躺在缎面床单上](https://cms-assets.youmind.com/media/1774939632470_glm3cz_HErAuKSbcAAHX7Z.jpg)
![悉尼·斯威尼 (Sydney Sweeney) 相似面孔的影棚时尚摄影，躺在缎面床单上](https://cms-assets.youmind.com/media/1774939632483_lwl9hz_HErAuJ0WQAA28QA.jpg)
![悉尼·斯威尼 (Sydney Sweeney) 相似面孔的影棚时尚摄影，躺在缎面床单上](https://cms-assets.youmind.com/media/1774939632445_z9plxn_HErAuKIaIAADwaa.jpg)

```
{
  "aspect_ratio": "4:5",
  "photography_style": "Studio fashion photography, overhead angle",
  "subject": {
    "face": "reminiscent of {argument name="celebrity face" default="Sydney Sweeney"}",
    "pose": "Lying on back/side, right arm bent behind head, left arm extended. Left knee bent.",
    "hair": "Voluminous wavy blonde, curtain bangs framing face.",
    "apparel": "{argument name="apparel description" default="Peach triangle bralette, matching brief panties, sheer stockings with wide white floral lace tops."}"
  },
  "facial_details": {
    "skin_tone": "Warm light-medium tan, glowing finish.",
    "eyes": "Direct gaze to camera, light-colored, subtle winged eyeliner, mascara.",
    "lips": "Glossy reddish-pink, slightly parted.",
    "cheeks": "Rosy flushed blush, contoured cheekbones.",
    "nose": "Small, straight.",
    "facial_expression": "Soft, relaxed, alluring."
  },
  "environment": {
    "background": "Wrinkled white satin bedsheets.",
    "background_objects": {
      "item_type": "Decorative throw pillows",
      "pillow_details": [
        "Top left: Peach square with subtle geometric pattern.",
        "Under head: Pale gold satin rectangular pillow.",
        "Top right: White square with multi-color floral print.",
        "Middle right: White square with small green motif.",
        "Bottom right: White square with dense blue/purple florals.",
        "Bottom left: Cream/white textured square pillow."
      ]
    }
  },
  "lighting": "Warm, soft directional studio lighting, casting distinct soft shadows under limbs."
}
```

[[Studio Lighting]] [[Fashion Photography]] [[Studio Fashion Portrait]] [[Sydney Sweeney Lookalike]]

---

### 39. Anya Taylor-Joy 形象的 Jessica Rabbit Cosplay

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-03-30  **Language**: en

> 这是一个高度结构化的 JSON 提示词，用于生成一张超写实时尚摄影作品，主体拥有鲜明的 Anya Taylor-Joy 特征，并身着 Jessica Rabbit 服装的精确复刻版。提示词详细指定了相机、光影、场景、姿势以及主体特征。

![Anya Taylor-Joy 形象的 Jessica Rabbit Cosplay](https://cms-assets.youmind.com/media/1774939641253_9jzom6_HEpt3mxbIAA4Hei.jpg)
![Anya Taylor-Joy 形象的 Jessica Rabbit Cosplay](https://cms-assets.youmind.com/media/1774939641310_kx6krn_HEpt3lmakAAbhs4.jpg)
![Anya Taylor-Joy 形象的 Jessica Rabbit Cosplay](https://cms-assets.youmind.com/media/1774939641379_vyf3l6_HEpt3k7bkAA1ezU.jpg)

```
{
  “meta”: {
    “quality”: “ultra_photorealistic, raw style, 8k”,
    “camera”: “Professional DSLR camera”,
    “lighting”: “Bright, clean, professional studio lighting with soft shadows”,
    “style”: “Full-body professional fashion photograph, no filter, sharp focus, cinematic”,
    “aspect_ratio”: “9:16”
  },
  “scene”: {
    “location”: “A clean, minimalist, professional studio environment with a seamless, solid cream-colored background floor and walls”,
    “atmosphere”: “Clean, sophisticated, minimalist, high-fashion studio aesthetic”
  },
  “subject”: {
    “gender”: “female”,
    “body”: {
      “type”: “Realistic, natural proportions, elegant physique”,
      “features”: “Fit and balanced silhouette”
    },
    “face”: {
      “features”: “Unmistakable likeness of Anya Taylor-Joy, natural wavy red hair swept to the side, striking features, glamorous natural makeup with defined eyes and glossy lips, realistic skin texture”,
      “expression”: “Sultry, confident model gaze directed at the camera, slightly parted lips”
    },
    “outfit”: {
      “description”: “An exact replica of the Jessica Rabbit costume: a form-fitting, vibrant red V-neck maxi-length gown with a high leg slit, paired with matching purple satin, elbow-length opera gloves, and simple transparent strap heels”,
      “fit”: “Elegant form-fitting gown, form-fitting gloves”
    },
    “pose”: “Standing full-body pose, directly facing the camera with a confident posture, hands wearing the purple gloves resting gracefully, with one hand on her hip, maintaining the model gaze, looking at the camera”
  }
}
```

[[Studio Lighting]] [[Anya Taylor-Joy]]

---

### 40. 超写实红色系街头服饰广告大片

**Author**: [A.D.BARRY](https://x.com/aiwithadb)  **Date**: 2026-03-29  **Language**: en

> 为 Nano Banana Pro 提供的详细提示词，用于生成一张超写实、超广角照片：一名男子身穿亮面超大款红色羽绒服和配套长裤，蹲在单色红色环境中，背景带有白色 Nike Swoosh 标志，重点呈现锐利细节和戏剧性的摄影棚灯光。

![超写实红色系街头服饰广告大片](https://cms-assets.youmind.com/media/1774853742204_mh6sq7_HEnLB7dWMAAedNw.jpg)
![超写实红色系街头服饰广告大片](https://cms-assets.youmind.com/media/1774853742294_xxj8sr_HEnLB8CbUAA63as.jpg)
![超写实红色系街头服饰广告大片](https://cms-assets.youmind.com/media/1774853742239_i0wex6_HEnLFEtXMAAXw7k.jpg)

```
A MAN from the reference image, WITH A FADE HAIRCUT,BROWN EYES,
AND A WELL-GROOMED SHORT BEARD, WEARING A GLOSSY OVERSIZED RED PUFFER JACKET AND
LOOSE RED PANTS WITH WHITE AND RED NIKE SNEAKERS, CROUCHING LOW WITH ONE KNEE UP AND ONE LEG FORWARD, LEFT ARM RESTING CASUALLY OVER THE RAISED KNEE AND RIGHT HAND
RELAXED NEAR THE OTHER LEG, BODY ANGLED SLIGHTLY TO THE SIDE WHILE HEAD TILTS
FORWARD LOOKING DIRECTLY AT THE CAMERA WITH A CONFIDENT EXPRESSION, ULTRA WIDE-ANGLE
LOW PERSPECTIVE SHOT EMPHASIZING THE FRONT SNEAKER APPEARING LARGE AND DOMINANT IN
THE FOREGROUND, SET IN A FULLY RED ENVIRONMENT WITH SMOOTH FLOOR AND BACKDROP FEATURING LARGE WHITE NIKE SWOOSH LOGOS BEHIND AND FLOWING RIBBON-LIKE RED SHAPES AROUND, HYPER-REALISTIC PHOTOGRAPHY, EXTREMELY SHARP DETAILS ON FABRIC SHINE AND
SNEAKER TEXTURE, DRAMATIC STUDIO LIGHTING WITH STRONG HIGHLIGHTS AND SOFT SHADOWS
SATURATED MONOCHROMATIC RED COLOR PALETTE WITH WHITE ACCENTS, MODERN STREETWEAR
CAMPAIGN STYLE, NO BLUR, NO DISTORTION, NO EXTRA LIMBS, NO ARTIFACTS
```

[[Studio Lighting]] [[Squat Pose]] [[Male Fashion Portrait]]

---

### 41. 带有严格身份锁定的集体肖像

**Author**: [glena Jenner](https://x.com/GlenaJenne)  **Date**: 2026-03-29  **Language**: en

> 这是一个用于 Nano Banana Pro 的提示词，旨在生成一张超写实的时尚编辑风格集体肖像，包含五位特定名人（Sabrina Carpenter、Sydney Sweeney、Sadie Sink、Anya Taylor-Joy 以及用户本人）。该提示词要求提供五张参考图以实现严格的面部身份保留，并指定了分层构图、现代街头服饰以及柔和的摄影棚灯光。

![带有严格身份锁定的集体肖像](https://cms-assets.youmind.com/media/1774853728733_didfr5_HEm9vFSakAAtLhS.jpg)

```
A group portrait of five young women posing together in a clean white studio, use 5 reference images for faces, assign one reference image per person, preserve each identity strictly, do not change facial features, hair color, or eye color for any individual.
Subjects: five women arranged in a layered composition, one in front, others positioned behind in a balanced formation.
Outfit: {argument name="outfit style" default="modern streetwear outfits, including oversized shirts, cropped tops, joggers, hoodies, sneakers"}, coordinated neutral and soft tones, realistic fabric texture.
Pose:
front subject lying forward with arm extended toward camera
others sitting or crouching behind, relaxed but confident poses
natural group balance, slightly dynamic arrangement
Expression: confident, calm, slightly serious, editorial look.
Hair: each subject keeps exact hair color and style from their respective reference image.
Accessories: minimal jewelry, optional glasses, clips, or headwear.
Environment: plain white studio background, clean and minimal.
Lighting: soft studio lighting, even exposure, minimal shadows, sharp details.
Style: ultra realistic, high detail, fashion editorial, Gen-Z aesthetic, clean composition.
```

[[Studio Lighting]] [[Sydney Sweeney]] [[Sadie Sink]] [[Sabrina Carpenter]]

---

### 42. 神似 玛格特·罗比 的 高级时尚 芭比风 肖像

**Author**: [LexiPrompt](https://x.com/Artist04048661)  **Date**: 2026-03-26  **Language**: en

> 一份详细且结构化的提示语，用于生成一张超写实的、高级时装编辑肖像，描绘一位酷似玛格特·罗比的年轻女性，着重呈现风格化的塑料娃娃美学，并包含特定的服装、姿势和影棚灯光条件。

![神似 玛格特·罗比 的 高级时尚 芭比风 肖像](https://cms-assets.youmind.com/media/1774594338021_414fuf_HEU7RqmaEAAKmRo.jpg)
![神似 玛格特·罗比 的 高级时尚 芭比风 肖像](https://cms-assets.youmind.com/media/1774594338023_ez4ghs_HEU7RqIWIAA1_nP.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman with a strong resemblance to Margot Robbie.",
      "hair": "Long, voluminous, cascading loose waves.",
      "face": "Contoured makeup, full lips, sharp gaze.",
      "body": "Slim, toned physique."
    },
    "attire": {
      "clothing": "Fuchsia beret, halter crop top, opaque tights, massive platform block heels.",
      "style": "High-fashion doll aesthetic."
    },
    "styling_and_accessories": {
      "jewelry": [
        "Tiny gold charm on shoe strap"
      ]
    },
    "environment": {
      "setting": "Minimalist studio setup.",
      "background": "Seamless grey backdrop.",
      "water": "None."
    },
    "pose": {
      "posture": "Leaning back, torso elevated, knees bent sharply.",
      "arms": "Extended backwards to support body weight.",
      "angle": "Low-angle side profile."
    },
    "lighting_and_mood": {
      "lighting": "Crisp studio lighting, sharp floor shadows.",
      "mood": "Editorial, plastic, stylized.",
      "colors": "Fuchsia pink against neutral grey."
    },
    "camera_and_technical": {
      "style": "Ultra Photorealistic, RAW photo.",
      "lens": "50mm",
      "aperture": "f/5.6",
      "quality_tags": [
        "8k resolution",
        "highly detailed",
        "studio lighting",
        "hyper-realistic"
      ]
    }
  }
}
```

[[Studio Lighting]] [[High Fashion Editorial]]

---

### 43. 超写实 折纸 雕塑

**Author**: [Toshi](https://x.com/ToshiArte)  **Date**: 2026-03-25  **Language**: en

> 一个用于生成精致折纸雕塑超写实特写图像的提示词。它强调清晰的折痕、逼真的纸张纹理、微妙的阴影和柔和的自然光照，并允许用户指定折叠的物品。

![超写实 折纸 雕塑](https://cms-assets.youmind.com/media/1774508267998_zbmur2_HERRqE2aYAAe5HP.jpg)
![超写实 折纸 雕塑](https://cms-assets.youmind.com/media/1774508267997_53ww5y_HERSSFoXUAA-qtj.jpg)
![超写实 折纸 雕塑](https://cms-assets.youmind.com/media/1774508268015_p85nxh_HERRqELW8AAuRwF.jpg)
![超写实 折纸 雕塑](https://cms-assets.youmind.com/media/1774508268496_uw7ftk_HERSWOwbUAAraGc.jpg)

```
hyper-realistic close-up of a stunning origami sculpture of **{argument name="thing" default="thing"}** made from intricately folded paper, displayed on a minimalist wooden table, extremely detailed and precise paper folds, crisp edges, subtle shadows in every crease, realistic paper texture with visible fibers and slight translucency, soft natural window light casting gentle dramatic shadows that highlight the origami structure, elegant and artistic composition, clean background, masterpiece, ultra detailed, photorealistic paper art
```

[[Studio Lighting]] [[Macro Photography]] [[Hyperrealistic Rendering]] [[Craft Photography]]

---

### 44. 超逼真的 iPhone 照片提示词 (Gemini Nano Banana)

**Author**: [Chryz leen](https://x.com/Chryzleenprompt)  **Date**: 2026-03-25  **Language**: en

> 针对 Gemini Nano Banana (暗示是 Pro 或基础模型) 的一个详细的提示词，用于生成一张超现实、超清晰的年轻女性照片。照片中的她留着黑色狼剪发型，该提示词强调具体的相机设置、姿势、妆容和灯光，同时确保与所提供的参考图像高度相似。

![超逼真的 iPhone 照片提示词 (Gemini Nano Banana)](https://cms-assets.youmind.com/media/1774508280406_2cicel_HEQ108za8AECWag.jpg)

```
Create image: Use the attached reference image as a visual guide for the character’s appearance, maintaining strong resemblance to the person in the reference. Preserve key visual traits such as facial structure and overall proportions, while allowing small natural variations typical of real photography. The generated subject should clearly resemble the reference while remaining a natural photographic interpretation.
Aspect Ratio: 3:4.
A hyper-realistic, ultra-sharp photograph taken on an iPhone 15 Pro, characterized by digital clarity. Shot on a wide-angle lens, ISO 50, f/1.8. A young woman is captured mid-moment, angled 20 degrees right with a natural weight shift and one shoulder subtly lowered. Her right hand is raised near the shoulder, fingers relaxed with long white nails. She features a voluminous black wolf cut with shaggy layers and face-framing hime-style strands. Her expression is poised but intrigued; intense blue eyes stare through rimless geometric glasses while her left eyebrow shows a slight micro-arch. Her makeup is a pink 'clean girl' style with winged liner, nose blush, and blurred matte lips. Skin shows a healthy radiance with visible pores and a dewy glass finish. She wears a baby pink ribbed knit top with small pearl buttons and separate arm sleeves. Illuminated by soft, diffused front-side lighting with gentle jawline shadows. The scene is in sharp focus from fabric textures to the dark background, devoid of bokeh, with realistic digital noise.
```

[[Studio Lighting]] [[Identity Reference]] [[Wolf Cut Hairstyle]]

---

### 45. 带有建筑工人的茶杯微距产品照

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-03-24  **Language**: en

> 生成一张超逼真的 8K 微距产品照片的提示词：画面主体是一个巨大的透明玻璃茶杯，伴随着戏剧性的凝固热茶飞溅。场景中，迷你建筑工人正在杯沿上爬梯子，并在茶碟上清扫。画面强调蒸汽颗粒、琥珀色液体质感和高对比度的摄影棚灯光。

![带有建筑工人的茶杯微距产品照](https://cms-assets.youmind.com/media/1774421478553_9n3wi0_HEMEE4fWYAAwWG6.jpg)
![带有建筑工人的茶杯微距产品照](https://cms-assets.youmind.com/media/1774421478698_xrurql_HEMEE48aIAUh03o.jpg)
![带有建筑工人的茶杯微距产品照](https://cms-assets.youmind.com/media/1774421478606_4o9hyy_HEMEE4pXQAAkqjc.jpg)
![带有建筑工人的茶杯微距产品照](https://cms-assets.youmind.com/media/1774421479387_b7j0lb_HEMEE4eXQAAb5pu.jpg)

```
{
  "prompt": "Ultra-realistic 8K macro product shot, pure white background. Giant transparent glass teacup with dramatic hot tea splash frozen mid-air. Tiny construction workers in yellow helmets climbing ladders on the rim, sweeping the saucer. Steam particles rising, rich amber liquid texture, dramatic studio lighting with high-contrast shadows and reflections",
  "negative_prompt": "blurry, people faces, text"
}
```

[[Studio Lighting]]

---

### 46. Nano Banana Pro Prompt，助力打造 Sabrina Carpenter 魔法少女 Cosplay 造型

**Author**: [LexiPrompt](https://x.com/Artist04048661)  **Date**: 2026-03-23  **Language**: en

> 针对 Nano Banana Pro 图像生成模型的一段详细 JSON 提示词，描述了一位神似 Sabrina Carpenter 的年轻女性，身着动漫魔法少女 Cosplay 服饰。该提示词包含了对服装、造型、环境、姿势、光影以及相机技术参数的具体描述，旨在呈现超写实的极致画质效果。

![Nano Banana Pro Prompt，助力打造 Sabrina Carpenter 魔法少女 Cosplay 造型](https://cms-assets.youmind.com/media/1774334476521_jbsy1a_HEIKsujakAAOkUc.jpg)
![Nano Banana Pro Prompt，助力打造 Sabrina Carpenter 魔法少女 Cosplay 造型](https://cms-assets.youmind.com/media/1774334476685_un8giq_HEIKsugbEAAXWYd.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman with a strong resemblance to {argument name="subject name" default="Sabrina Carpenter"}.",
      "hair": "Long flowing style with twin top buns, loose lower sections cascading smoothly.",
      "face": "Serene gaze, smooth dewy skin, soft makeup with prominent red lips.",
      "body": "Slender physique, smooth illuminated skin."
    },
    "attire": {
      "clothing": "White fitted bodice, large red chest bow with gold center, metallic silver arm-length gloves, ruffled pink skirt.",
      "style": "Anime magical girl cosplay."
    },
    "styling_and_accessories": {
      "jewelry": [
        "Gold tiara with red gem",
        "Spherical white and red hairpiece covers",
        "Gold star dangle earrings",
        "Red ribbon choker"
      ]
    },
    "environment": {
      "setting": "Outdoors, bright daytime.",
      "background": "Clear blue sky with soft clouds, white floral blooms in foreground.",
      "water": "None."
    },
    "pose": {
      "posture": "Leaning slightly, torso angled away, face turned to viewer.",
      "arms": "Right arm raised touching head, left arm resting downward.",
      "angle": "Slight low-angle shot."
    },
    "lighting_and_mood": {
      "lighting": "Bright natural daylight, direct sun with soft fill.",
      "mood": "Dreamy, cinematic, ethereal.",
      "colors": "Pastel blue, bright white, vibrant red, gold, pink."
    },
    "camera_and_technical": {
      "style": "Ultra Photorealistic, RAW photo.",
      "lens": "50mm",
      "aperture": "f/2.8",
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

[[Studio Lighting]] [[Celebrity Likeness]] [[Hyperrealistic Rendering]]

---

### 47. 高定橙色肖像画的 JSON 提示词，带参考图片

**Author**: [Bethany](https://x.com/JustBethanyai)  **Date**: 2026-03-22  **Language**: en

> 一个结构化的 JSON 提示词，用于 Nano Banana，专注于生成一张以橙色为主色调的高级时装特写肖像，明确要求提供参考图像以确定人物身份和面部特征。

![高定橙色肖像画的 JSON 提示词，带参考图片](https://cms-assets.youmind.com/media/1774248304456_1ws39j_HEBS89ta0AAQNRm.jpg)
![高定橙色肖像画的 JSON 提示词，带参考图片](https://cms-assets.youmind.com/media/1774248304430_zwxlpq_HEBS89obwAAHwn4.jpg)
![高定橙色肖像画的 JSON 提示词，带参考图片](https://cms-assets.youmind.com/media/1774248304692_8ajpv2_HEBS89pagAAlRT-.jpg)
![高定橙色肖像画的 JSON 提示词，带参考图片](https://cms-assets.youmind.com/media/1774248305566_yr3qt5_HEBS89VX0AAIUVA.jpg)

```
{
  "character": {
    "identity": "custom person based on reference image",
    "reference_image": "use provided reference image for facial features, proportions, and identity",
    "skin_tone": "match reference image exactly",
    "face": "replicate facial structure, symmetry, and defining features from reference image",
    "eyes": "match eye shape, color, and expression from reference image",
    "lips": "match lip shape, fullness, and natural color from reference image"
  },
  "hair": {
    "style": "messy updo, loosely tied back",
    "texture": "slightly damp with soft wispy strands framing the face",
    "color": "match reference image"
  },
  "accessories": {
    "earrings": "medium-sized hoop earrings, glossy bright orange",
    "sunglasses": "narrow oval sunglasses, black frame with vivid orange tinted lenses, worn low on the nose below the eyes"
  },
  "makeup": {
    "style": "soft natural glam adapted to subject",
    "skin_finish": "radiant natural glow",
    "eyes": "light mascara, subtle definition enhancing natural eye shape",
    "lips": "natural tinted gloss matching subject"
  },
  "outfit": {
    "top": "sleeveless textured knit top, vivid saturated orange",
    "material": "slightly glossy, modern fabric with subtle texture",
    "color_emphasis": "high saturation orange tones, bright and vibrant"
  },
  "pose": {
    "hand_position": "one hand raised to mouth, index finger lightly touching lower lip",
    "expression": "playful, slightly teasing smile adapted to subject",
    "shoulders": "relaxed, facing forward"
  },
  "gaze": {
    "direction": "direct eye contact over the lowered sunglasses",
    "emotion": "confident, playful, engaging"
  },
  "mood": {
    "overall": "playful, modern, stylish",
    "energy": "light, fresh, confident"
  },
  "lighting": {
    "type": "bright soft studio lighting",
    "style": "even illumination, minimal shadows",
    "highlight": "soft highlights on skin and glossy elements",
    "contrast": "low to medium contrast, clean look"
  },
  "camera": {
    "type": "DSLR, high resolution",
    "settings": "85mm lens, f/2.8 aperture, ISO 100, sharp focus on eyes",
    "quality": "ultra-detailed, crisp, high fashion editorial"
  },
  "angle": {
    "view": "front-facing",
    "crop": "tight close-up portrait, head and upper shoulders",
    "framing": "centered composition"
  },
  "background": {
    "type": "plain studio background",
    "color": "light gray / off-white",
    "style": "clean, minimal, no distractions"
  },
  "color_style": {
    "palette": "dominant bright orange accents contrasted with neutral tones",
    "saturation": "high saturation on orange elements",
    "center_emphasis": "central subject and orange elements extra vibrant and luminous"
  },
  "rendering": {
    "style": "modern fashion editorial photography",
    "detail": "reali
```

[[Studio Lighting]] [[Fashion Portrait]] [[Close-Up Portrait]] [[Identity Reference]]

---

### 48. 1970 年代高雅魅力时尚肖像

**Author**: [PictureT | AI 🐍](https://x.com/SINthetic_47)  **Date**: 2026-03-20  **Language**: en

> 一个详细的 JSON 格式提示，用于 Nano Banana（可能是 Nano Banana Pro）生成一张 1970 年代高雅魅力风格的女性模特时尚肖像，其中指定了服装、姿势、灯光和技术相机设置。

![1970 年代高雅魅力时尚肖像](https://cms-assets.youmind.com/media/1774074540438_8fta2p_HD0iSZQXcAInOPk.jpg)

```
{   "STYLIZATION": {     "Medium": "Studio fashion portrait photography",     "Aesthetic": "1970s High-Glamour / Retro Chic",     "Color_Palette": ["Pale Lavender", "Orchid Purple", "Deep Copper", "Bronze"]   },   "SUBJECT_BLOCK": {     "Model": "Caucasian female, platinum blonde voluminous feathered hair with high-crown volume",     "Makeup": "Heavy 70s blue eyeshadow, pale pink lipstick, purple manicured nails",     "Top": "Pale lavender skin-tight jersey turtleneck long-sleeved bodysuit",     "Bottom": "High-waisted orchid purple midi-length skirt, accordion pleated texture, center-front thigh-high slit",     "Legwear": "Sheer white matte hosiery",     "Footwear": "Metallic bronze platform stiletto pumps",     "Pose": "Full-body standing shot, weight on right leg, left hand on hip, right hand on waist, confident expression"   },   "ENVIRONMENT_BLOCK": {     "Backdrop_Primary": "Ornate Persian-style tapestry hanging vertically with intricate paisley and floral motifs",     "Backdrop_Secondary": "Dark, shadowed studio background to the right side",     "Floor": "Matching ornate Persian rug with deep red and gold tones",     "Atmosphere": "Polished studio setting, high-fashion editorial mood"   },   "TECHNICAL_REQUISITES": {     "Camera": "Medium format camera look, 85mm lens, eye-level",     "Lighting": "Hard studio lighting, high contrast, strong key light creating deep shadows on the backdrop",     "Processing": "Slight film grain, vibrant saturation on purples, sharp focus on fabric textures"   } }
```

[[Studio Lighting]] [[Fashion Editorial]] [[Vintage Aesthetic]] [[Retro Fashion]]

---

### 49. 极简奢华产品摄影提示

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-03-18  **Language**: en

> 以下是两个详细的提示，用于生成胶原蛋白补充剂罐的高端、极简主义奢华产品摄影照片，强调特定的背景、光线（温暖的阳光/影棚）和周围元素（菠萝、葡萄、金色液体），使用 Nano Banana Pro。

![极简奢华产品摄影提示](https://cms-assets.youmind.com/media/1773902657481_as7uto_HDrv268a4AASFat.jpg)
![极简奢华产品摄影提示](https://cms-assets.youmind.com/media/1773902657412_2oeack_HDrv27Fa8AArXh_.jpg)

```
Prompt 1:

Minimalist luxury product photography of a collagen supplement jar placed on a soft pastel peach background, cylindrical pedestal base, surrounded by fresh pineapple and sliced grapefruit, a small glass cup with golden liquid in front, warm sunlight casting soft palm leaf shadows, clean aesthetic, high-end skincare branding, soft diffused lighting, realistic textures, subtle reflections, shallow depth of field, editorial style, 4k, ultra-detailed.

Prompt 2:
Premium skincare product shot of a white collagen cream jar with metallic lid on a round pedestal, tropical fruits (pineapple and grapefruit slices) arranged around, a glass cup filled with amber liquid, peach monochrome background with palm shadow overlay, soft warm lighting, minimal composition, luxury beauty advertisement style, smooth gradients, high realism, sharp focus, studio lighting, 4k resolution.
```

[[Studio Lighting]]

---

### 50. 时尚广告海报提示词，带人脸替换功能

**Author**: [auqib](https://x.com/auqibhabib)  **Date**: 2026-03-18  **Language**: en

> 一个高度结构化的提示，用于 Google Gemini Nano Banana 2 生成一张超现实、高端时尚广告海报，采用严格的垂直分割布局。该提示要求用提供的参考图像替换模特的脸部，同时保持模特的姿势和服装（米色西装外套、白色衬衫、定制长裤），并包含有关编辑文本面板和灯光的详细说明。

![时尚广告海报提示词，带人脸替换功能](https://cms-assets.youmind.com/media/1773902676371_s3rz4x_HDp6t3tbEAIV6-b.jpg)

```
Ultra-realistic high-end fashion advertisement poster, minimalist editorial magazine style.

STRICT LAYOUT (do not change anything):
Vertical split composition.
Right side: full-body fashion model.
Left side: beige editorial panel with text + image frames.

MODEL (KEEP EVERYTHING SAME, ONLY CHANGE FACE As GIVEN IN REFRANCE IMAGE):
A stylish young woman standing in a relaxed confident pose, body slightly turned sideways, head turned to the right (looking away from camera).
One hand inside pant pocket, other hand holding a brown leather bag.

Outfit (exact):

{argument name="outfit piece 1" default="Beige/tan oversized blazer"}

Soft white V-neck blouse

High-waisted beige tailored trousers

Minimal gold necklace

Small earrings

FACE REPLACEMENT (VERY IMPORTANT):
Use the face from the provided reference image.
Seamlessly blend the reference face onto the model’s head.
Match skin tone, lighting, shadows, and color grading perfectly.
Keep same head angle and expression as original pose.
Ensure realistic identity preservation (no distortion, no mismatch).
Ultra-clean face integration, professional fashion photography quality.

LIGHTING & STYLE:
Soft warm studio lighting, diffused, subtle shadows, luxury editorial look.
Beige neutral tones, clean premium aesthetic.

LEFT PANEL (COPY EXACT):

Top text:
“FASHIOIN Week 2026” (same spelling, bold modern sans-serif, brown)

Below:
“Presented by DigiGraphics.
Hosted by Fashion House”

Image frames:
Two stacked rectangular frames showing cropped outfit close-ups (same outfit, same lighting)

Bottom:

Vertical text: “12 PM”

“31 March 2026, Patna, Bihar”

QR code placeholder

“Register here” with small arrow

STYLE KEYWORDS:
ultra-realistic, editorial fashion poster, luxury branding, minimal, soft shadows, high detail, magazine layout.
```

[[Studio Lighting]] [[High Fashion Editorial]]

---

### 51. 时尚广告海报生成

**Author**: [auqib](https://x.com/auqibhabib)  **Date**: 2026-03-17  **Language**: en

> 为 Nano Banana Pro（又称 Gemini Nano Banana 2）提供一个高度具体的提示，以生成一张超现实的时尚广告海报。海报中，一位女性呈低蹲姿势，并详细说明了服装、灯光以及排版的确切位置和内容。

![时尚广告海报生成](https://cms-assets.youmind.com/media/1773816083237_gxsavr_HDntzR9akAAdzyp.jpg)

```
Ultra-realistic fashion advertisement poster, minimalist editorial style.
Background: solid warm beige studio backdrop with soft gradient lighting, smooth clean texture.
Main subject: a stylish young woman in a low squat pose, body slightly turned sideways, one arm resting on knee, other hand touching back of head. Expression calm, confident, slightly looking sideways (not directly at camera).
Outfit (keep EXACT):
Sleeveless beige/tan high-neck top
Slim beige pants
Brown suede ankle boots with block heels
Light brown jacket placed casually near her feet
Minimal accessories: small hoop earrings, thin bracelet
Hair: straight, shoulder-length, natural dark brown, side-parted
Makeup: soft natural tones, clean skin, subtle glow
⚠️ Face: [REPLACE FACE WITH PROVIDED IMAGE / KEEP FACE GENERIC IF NOT PROVIDED]
(ensure seamless blending, same lighting, same skin tone, hyper-realistic)
Typography & Layout (EXACT SAME STYLE)
Top: Large bold condensed sans-serif text in dark red: FINAL HOURS (very large, stretched across width, behind subject partially)
Left side: Small text: UP TO
60% OFF
SELECTED ITEMS
Right side: ENDS
31.12
12 PM
Bottom: ⚠️ NO WEBSITE TEXT (REMOVE COMPLETELY)
Lighting & Style
Soft studio lighting, warm tone
Subtle shadows under subject
Clean editorial magazine look
Slight depth but mostly flat poster style
Matte finish, no gloss
Perfect alignment, balanced spacing
```

[[Studio Lighting]] [[Female Portrait]] [[Crouching Pose]] [[Surrealist Fashion Editorial]]

---

### 52. 超现实主义高细节图腾堆叠提示

**Author**: [Heather Green](https://x.com/heathergreen)  **Date**: 2026-03-16  **Language**: en

> 一个给 Nano Banana 2 的提示，用于生成一张超现实、超精细的图像，艺术风格为周松。主体是一个异想天开、摇摇欲坠的图腾状堆叠，由一个融化的冰淇淋甜筒、一个光滑的条纹沙滩球和一个抛光的保龄球组成，强调复杂的纹理、反射和柔和的摄影棚灯光。

![超现实主义高细节图腾堆叠提示](https://cms-assets.youmind.com/media/1773729519571_c0efv2_HDjtDUbbEAUET7x.jpg)

```
in the surreal, hyper-detailed art style of {argument name="artist" default="Zhou Song"}, a whimsical totem-like stack featuring a melting {argument name="top object" default="ice cream cone"} perched on top of a glossy striped beachball, which balances precariously on a heavy polished bowling ball, intricate textures and reflections on each surface, soft studio lighting with subtle colored highlights, clean minimal background to emphasize the strange vertical composition, high resolution, highly detailed, dreamlike yet slightly uncanny atmosphere
```

[[Studio Lighting]]

---

### 53. 商业化妆品产品摄影提示

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-03-16  **Language**: en

> 一个详细的提示，用于生成商业化妆品产品摄影，画面中一个粉色化妆品罐置于一团搅打奶油之上，红色浆果糖浆倾泻而下，周围散落着各种新鲜浆果，强调高分辨率、逼真的纹理和专业的影棚灯光。

![商业化妆品产品摄影提示](https://cms-assets.youmind.com/media/1773729521460_mk3gsw_HDhRyeEaIAAW8dL.jpg)
![商业化妆品产品摄影提示](https://cms-assets.youmind.com/media/1773729521465_r8581a_HDhRyevakAAmnID.jpg)
![商业化妆品产品摄影提示](https://cms-assets.youmind.com/media/1773729521449_mk8zvb_HDhRyelawAAs5vz.jpg)
![商业化妆品产品摄影提示](https://cms-assets.youmind.com/media/1773729522143_sulq8a_HDhRyfbbkAA3DCP.jpg)

```
A centrally placed pink cosmetic jar labeled “LANEIGE Lip Sleeping Mask [Berry] 3 g” sits on top of a large spiral swirl of white whipped cream. The jar features a matte translucent pink container with minimalist white typography and a square shape with rounded corners. From above, a thick, glossy red berry syrup pours straight down onto the top of the jar, slowly flowing along the sides with visible droplets and shiny liquid trails.

Around the whipped cream are various fresh berries, including raspberries, halved strawberries with green leaves, and dark cherries with stems. Some fruits appear slightly floating or gently resting against the whipped cream.

The composition is centered, with the jar positioned exactly in the middle of the white cream spiral, while the fruits are asymmetrically arranged around it.

The background is a soft, solid light pink studio backdrop with a minimalist aesthetic and subtle blurred red shapes in the foreground. Soft, even studio lighting creates gentle shadows and strong glossy reflections on the syrup and jar.

Extremely detailed textures of whipped cream, fruit, and liquid, commercial cosmetic product photography, sharp focus, high resolution, realistic textures, professional advertising photo.
```

[[Studio Lighting]] [[Luxury Beauty Photography]]

---

### 54. 扭曲透视下的创意时尚摄影

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-03-16  **Language**: en

> 一个为 Google Gemini Nano Banana Pro 设计的详细提示，用于生成创意时尚摄影作品，画面中一位男士呈现扭曲的透视效果（广角/鱼眼效果），强调国际象棋主题、影棚布光和光鲜的杂志风格。

![扭曲透视下的创意时尚摄影](https://cms-assets.youmind.com/media/1773729508395_mdt2sx_HDfkBSaaMAAg554.jpg)

```
Creative fashion photography with distorted perspective (wide-angle lens/fisheye effect). 

The frame features a young, handsome European-looking man with dark hair. 

He is seated at a table, resting his left hand on his head (a relaxed, pensive pose), and looking directly into the lens with a confident, slightly arrogant expression. Key element (foreground): His right arm is extended strongly forward toward the camera, palm facing down.

In extreme close-up. He holds a large, glossy black chess piece (the Queen), making a move. Due to the perspective, the hand and piece appear enormous compared to the head. Setting: The table is a stylized chessboard: alternating glossy black squares and squares of textured gold leaf, with strong reflections on the surface. In the background, a black chess piece lies overturned on the table. Clothing: A loose white shirt with an open collar, a gold chain around the neck.

Background: Dark, almost black, with large white abstract geometric shapes (reminiscent of the silhouettes of a chess rook's battlements) at the edges of the frame. Lighting and Style: Studio lighting, contrasting light, high detail in the leather texture and gold, glossy magazine style, unusual angle.
```

[[Studio Lighting]] [[Male Fashion Portrait]] [[Magazine Style]]

---

### 55. 时尚专题摄影提示

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-03-14  **Language**: en

> 在 Yapper 上为 Google Nano Banana Pro 提供一个详细的提示，以生成一张女性在现代简约工作室中的全身时尚编辑照片，具体说明她的服装、姿势、配饰以及工作室环境和灯光。

![时尚专题摄影提示](https://cms-assets.youmind.com/media/1773556637748_r63pou_HDYjXciacAAcye3.jpg)
![时尚专题摄影提示](https://cms-assets.youmind.com/media/1773556637779_2uaasu_HDYjXeEaMAUjpsP.jpg)
![时尚专题摄影提示](https://cms-assets.youmind.com/media/1773556637594_vehhxg_HDYjXeCaMAMtk61.jpg)

```
A full-body fashion editorial photograph of a woman standing indoors in a modern minimalist studio. She stands slightly angled left, looking away from the camera in a relaxed pose, one hand in her trouser pocket and the other holding a burgundy handbag. She wears a deep burgundy long-sleeve blouse with a dramatic ruffle across the chest and light beige high-waisted wide-leg trousers. Her brown hair is styled in a messy low bun with loose strands and small drop earrings. The room features a light sofa, arched wall opening, white curtains, indoor plant, side table, and a visible studio softbox. Soft natural light enters from the left creating gentle shadows. Clean editorial fashion photography style, shallow depth of field, neutral tones, ultra-detailed, 8K, vertical portrait.
```

[[Studio Lighting]] [[Female Portrait]] [[Editorial Photography]] [[Fashion Editorial Portrait]]

---

### 56. 超逼真护肤品摄影提示词

**Author**: [Olivia | UGC CREATOR](https://x.com/MasterAi33020)  **Date**: 2026-03-13  **Language**: en

> 一个为 Nano Banana Pro 设计的提示，旨在生成超逼真的护肤品广告摄影——具体来说，是一个磨砂柑橘玻璃瓶装的“Glow Recipe – Lemon Brightening Glow Serum (30 ml)”——在空中漂浮。

![超逼真护肤品摄影提示词](https://cms-assets.youmind.com/media/1773469775457_hzifvo_HDUCH8NaMAAOcy0.jpg)
![超逼真护肤品摄影提示词](https://cms-assets.youmind.com/media/1773469775486_7ye0zu_HDUCH6LaMAAlak6.jpg)

```
Ultra-realistic skincare advertising photography featuring a frosted citrus glass bottle labeled “{argument name="product name" default="Glow Recipe – Lemon Brightening Glow Serum (30 ml)"}” floating mid-air.
```

[[Studio Lighting]] [[Commercial Photography]] [[Skincare Product Photography]] [[Luxury Beauty Photography]]

---

### 57. 2x2 网格时尚摄影拼贴

**Author**: [Weinberg](https://x.com/weiinberg)  **Date**: 2026-03-15  **Language**: en

> 一个提示，用于生成一张超现实的 GQ/Vogue 风格 2x2 网格拼贴画，其中包含同一人物的四种时尚姿势（使用上传照片锁定身份），身穿深祖母绿西装外套和黑色太阳镜，并详细说明了专业的影棚灯光和相机设置。

![2x2 网格时尚摄影拼贴](https://cms-assets.youmind.com/media/1773643993636_n4ivui_HDbXQY7aMAIHo0m.jpg)

```
Use my uploaded photo as the identity reference.
Create a professional studio fashion photoshoot in a 2×2 grid collage showing four poses of the same person wearing black sunglasses.

Outfit: deep emerald green tailored blazer, cream/off-white dress shirt, black slim trousers, burgundy tie, optional silver watch. Blazer appears differently across frames (worn, draped over shoulder, partially removed, held).
Background: clean teal-to-turquoise gradient studio backdrop, minimal fashion studio setting.
Poses:
1.Close portrait adjusting tie.
2.Seated editorial pose leaning forward with elbow on knee.
3.Relaxed pose with vintage camera around neck.
4.Stylish pose running hand through hair while holding blazer.
Lighting: professional three-point studio lighting — softbox key light 45° camera left, soft fill light camera right, subtle rim light behind subject.
Camera: Sony A7R V, 85mm portrait lens, f/2.2, ISO 100, 1/160s, WB 5600K, shallow depth of field, focus on eyes.
Realism: natural skin pores, hair strands, subtle fabric wrinkles, realistic shadows, lens compression, reflections in sunglasses.
Output: ultra-realistic GQ/Vogue-style editorial photography, sharp detail, 4K resolution, clean 2×2 grid layout.
```

[[Studio Lighting]] [[Face Preservation]]

---

### 58. Pixar 风格 3D 头像提示词，适用于 Nano Banana

**Author**: [RegularPeopleAI](https://x.com/RegularPeopleAI)  **Date**: 2026-03-14  **Language**: en

> 一个给 Nano Banana 的提示，用于生成参考人物的皮克斯风格 3D 头像特写，强调自信的表情、量身定制的服装和专业的影棚灯光。

![Pixar 风格 3D 头像提示词，适用于 Nano Banana](https://cms-assets.youmind.com/media/1773556643004_u2ntez_HDYvZoEbcAA_4bh.jpg)

```
Pixar-style 3D avatar of [ reference person ], confident, warm smile. Tailored outfit, subtle catchlights in eyes, soft corporate studio lighting, clean white background, executive headshot
```

[[Studio Lighting]] [[Character Transformation]] [[Stylized 3D Rendering]] [[Confident Expression]]

---

### 59. 高级时尚眼镜特写编辑提示

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2026-03-13  **Language**: en

> 一个用于生成眼镜特写、高端时尚编辑肖像的提示，详细说明了构图、灯光、调色板，以及为营造杂志美感而叠加的排版。

![高级时尚眼镜特写编辑提示](https://cms-assets.youmind.com/media/1773469796342_ab79k5_HDRVZrFbQAMuQck.jpg)

```
An extreme close-up, high-fashion editorial portrait focusing on the right side of a person's face. The composition is a tight crop showing the bridge of the nose, a portion of the lips, and a single eye peering through sunglasses. The shot is characterized by a heavy, cinematic film grain and a warm, sophisticated studio atmosphere.
Eyewear: Large-frame, wrap-around sunglasses made of high-gloss dark tortoiseshell acetate (mottled black and deep mahogany). The lenses are a vibrant, translucent amber-orange, allowing the eye and eyelashes behind the lens to remain visible but color-tinted.
Person: A person with smooth skin showing natural texture and fine pores. The lighting is soft-side lighting from the right, creating a gentle shadow on the left side of the nose and a subtle highlight on the cheekbone and lower lip.
Typography: Bold, white, geometric sans-serif text reading "{argument name=\"main text\" default=\"Bold Impact\"}" is overlaid on the lower-right cheek. Three smaller, delicate labels are scattered: "Deep Tones" (top right), "Sharp Detail" (on the left lens), and "Strong Style" (bottom right).
Color Palette: A rich mix of skin tones (#E8A88A), burnt orange (#B8541C), and deep espresso (#1A0D0B), contrasted with crisp white text (#FFFFFF).
Lighting: Warm studio lighting with a soft-focus depth of field. The background consists of out-of-focus hair and skin, keeping all attention on the eye and the texture of the acetate frames.
Atmosphere: Premium, editorial fashion magazine aesthetic; high-contrast but with soft transitions.
```

[[Studio Lighting]] [[High Fashion Editorial]] [[Beauty Photography]] [[Typography Overlay]]

---

### 60. 风格化 3D 漫画肖像提示

**Author**: [simeon-sanai](https://x.com/Naiknelofar788)  **Date**: 2026-03-13  **Language**: en

> 一个详细的提示，用于根据参考照片创建夸张、风格化的 3D 漫画肖像，要求进行有意的变形（超大头部、厚嘴唇），同时保留面部相似度，并使用简洁的材质和中性工作室照明进行渲染，以营造一种怪诞、时尚前卫的美学。

![风格化 3D 漫画肖像提示](https://cms-assets.youmind.com/media/1773469797685_cpra1a_HDQGTz1bQAQd84-.jpg)
![风格化 3D 漫画肖像提示](https://cms-assets.youmind.com/media/1773469797724_dzuofw_HDQGTySbQAEZPT6.jpg)
![风格化 3D 漫画肖像提示](https://cms-assets.youmind.com/media/1773469797647_7zbz55_HDQGTwqbQAAOS2X.jpg)
![风格化 3D 漫画肖像提示](https://cms-assets.youmind.com/media/1773469798592_374se8_HDQGT3cbQAAArUu.jpg)

```
Create an exaggerated stylized 3D caricature character portrait with strong intentional deformation and a clean, controlled surface finish. Use the person from the ATTACHED REFERENCE PHOTO. Preserve the subject’s identity, facial likeness, skin tone, and defining features, but reinterpret them into a bold caricatured 3D form with an elongated neck, oversized head-to-neck ratio, droopy eyelids, heavy lips, and slightly asymmetrical facial structure.Render as a human-like 3D character with smooth, studio-clean skin and intentionally designed detail, avoiding random texture or noise. Style with bold accessories such as round or oval glasses, hoop earrings, gold chains, headscarves or bandanas, and street-luxury clothing.

Use neutral studio lighting with soft shadows and even illumination, no dramatic contrast, against a plain neutral grey or off-white background. The overall aesthetic should feel weird, fashion-forward, collectible, and character-driven rather than cute or realistic.

Ultra high definition, premium cinematic 3D render quality, hyper-realistic hyper realism, clean materials, no freckles, no dirt, no grain, no noise, no speckling, no text, no logos, no watermarks.

Aspect ratio 4:5.
```

[[Studio Lighting]] [[Face Reference Photography]] [[3D Character Render]]

---

### 61. Vogue 封面时尚肖像，带面部参考

**Author**: [TSU YI TSENG](https://x.com/lynn800741)  **Date**: 2026-03-13  **Language**: en

> 一个为 Nano Banana 2 设计的详细、结构化的图像生成提示，旨在创建一张逼真的《Vogue》杂志封面风格的年轻女性时尚肖像。它要求使用上传的面部参考图以 100% 保留面部特征，描绘主体眨眼并做出爱心手势，周围环绕着相机，强调高端时尚造型、专业影棚灯光和 8K 分辨率。

![Vogue 封面时尚肖像，带面部参考](https://cms-assets.youmind.com/media/1773469802066_j77jyf_HDP_s7mWkAER25W.jpg)
![Vogue 封面时尚肖像，带面部参考](https://cms-assets.youmind.com/media/1773469802107_njpnfc_HDP_s7mWEAAQoXP.jpg)
![Vogue 封面时尚肖像，带面部参考](https://cms-assets.youmind.com/media/1773469802514_yc6obg_HDP_s7nXYAAt2HK.jpg)
![Vogue 封面时尚肖像，带面部参考](https://cms-assets.youmind.com/media/1773469803192_9xdnu5_HDP_s7oWEAA_1X6.jpg)

```
Use the uploaded face as the original face reference to create a realistic Vogue magazine cover-style fashion portrait (100% face feature retention).

A young, elegant woman poses confidently, maintaining her original facial features and natural beauty. She winks her left eye and puckers her mouth playfully. Both hands are raised, forming a heart gesture beside her cheeks.

She is surrounded by DSLR cameras and smartphones, as if paparazzi and photographers are shooting her from all directions. Some phone screens display her real-time image.

Makeup & Styling: Flawless, luminous skin, natural makeup, glossy pink lip color, soft blush, and perfect highlighters. Light brown(or black) hair tied back in a sleek low bun with a few stray strands naturally framing the face.

Attire & Accessories: Elegant and simple off-white strapless evening gown, Louis Vuitton necklace, diamond rings, luxury fashion jewelry.

Photography Style: Close-up to half-body fashion portrait, Vogue magazine editorial style, cinematic professional studio lighting, soft HDR background, shallow depth of field, realistic skin texture, ultra-high detail, 8K resolution.

Camera & Lens Appearance: Professional DSLR look, 85mm lens feel, f/1.8 aperture, sharp focus, soft background blur (bokeh).

Composition: Vogue magazine layout, prominent large logo at the top, fashion magazine cover-style border, minimalist and elegant design.

Vibe & Style: Playful yet luxurious, high-fashion beauty editorial, real and natural, not AI-looking, shot by a professional fashion photographer.
```

[[Studio Lighting]] [[8K Resolution]] [[High Fashion Editorial]] [[Face Reference Photography]]

---

### 62. BAGEL LABS 超奢华美妆产品特写

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-03-12  **Language**: en

> 一个用于 Nano Banana 2 的图像生成提示，专注于创作一张樱桃唇彩的超豪华美妆产品特写，画面中唇彩如雕塑般戏剧性地向上飞溅，环绕着产品，强调高端影棚布光和材质的真实感。

![BAGEL LABS 超奢华美妆产品特写](https://cms-assets.youmind.com/media/1773383468674_ayqt1h_HDO05whaUAA-RQM.jpg)

```
Create an original ultra-luxury beauty packshot for BAGEL LABS featuring a premium cherry lip gloss standing upright in the center while a dramatic cherry gloss splash bursts upward around it in the shape of a crown. The splash should feel sculptural, elegant, and controlled rather than chaotic, with beautiful lacquered arcs, suspended droplets, and glassy edges catching the light. Keep the product fully visible and dominant as the hero object. Add a few carefully placed dark cherries near the base or subtly integrated into the splash composition for richness and fruit association. Use high-end studio beauty lighting with soft reflections, crisp highlights, refined shadows, and premium material realism. Background should stay minimal and clean in ivory, warm grey, or pale stone. The overall effect should be powerful, luxurious, sensual, and campaign-ready, like a hero visual for a major beauty launch.
```

[[Studio Lighting]] [[Beauty Product Photography]] [[Material Realism]]

---

### 63. Sabrina Carpenter 高级时装编辑提示，适用于 Nano Banana Pro

**Author**: [Noira](https://x.com/Noira_exe)  **Date**: 2026-03-12  **Language**: en

> 一个详细的 JSON 提示，用于 Nano Banana Pro 生成一张 Sabrina Carpenter 身穿薰衣草色缎面紧身胸衣连衣裙的高级时装编辑图片，其中指定了相机设置、灯光、场景、姿势（四肢着地）和配饰，以获得异想天开且充满活力的效果。

![Sabrina Carpenter 高级时装编辑提示，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1773383493074_czmy1f_HDN5Nk4X0AAvCCI.jpg)
![Sabrina Carpenter 高级时装编辑提示，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1773383493346_ooiwbn_HDN5Nq3asAA_xkP.jpg)

```
{
  “meta”: {
    “quality”: “ultra_photorealistic, raw style, 8k”,
    “camera”: “Sony Alpha 1”,
    “lighting”: “bright, soft, diffused studio lighting creating a delicate glow, highlighting textures”,
    “style”: “high-fashion editorial, single-person focus, whimsical and dynamic posture”,
    “aspect_ratio”: “9:16”
  },
  “scene”: {
    “location”: “A dreamy, ethereal abstract studio set with a soft, gradient background of pastel pinks, purples, and blues, seen from a low angle. The ground is a clean, reflective studio floor. A few scattered floating flowers (pinks and blues) are positioned in the background.”,
    “atmosphere”: “Sophisticated, whimsical, angelic, yet dynamic and confident.”
  },
“subject”: {
    “gender”: “female”,
    “name”: “{argument name="subject name" default="Sabrina Carpenter"}”,
    “body”: {
      “type”: “Realistic, naturally proportioned figure, shown in an all-fours pose from a three-quarter side profile.”
    },
    “face”: {
      “features”: “Her distinctive features, light blue eyes, and blonde hair. Face is poised and looking directly at the camera with a confident expression.”,
      “expression”: “Serene and confident.”
    },
    “outfit”: {
      “description”: “{argument name="outfit description" default="Lavender-purple satin corset-mini dress, featuring a ruffled sweetheart neckline and detailed boning. The voluminous puff skirt is designed as an ultra-mini, draping softly around her legs. She wears white lace thigh-high stockings with small lavender bows below the knee, and lavender-purple platform Mary-Jane heels with ankle straps."}”,
      “fit”: “Tailored, structured, ultra-short, and bold.”,
“accessory”: “Her hair is coiffed into an elaborate, vintage-style chignon bun decorated with multiple small pastel bows. Small pearl earrings and a simple pearl necklace.”
    },
    “pose”: “On all fours, kneeling on both knees with hands placed flat on the reflective floor. Her body is arched slightly, looking directly towards the camera lens. This posture showcases the side details of the corset, the ultra-short skirt, and the full length of her lace-clad legs from a low perspective.”
  },
  “composition”: “Low-angle medium-full shot, framing the subject in her all-fours pose. Sharp focus on Sabrina Carpenter and all textures of the satin, lace, and hair details. Background features a soft, ethereal bokeh. The reflective floor adds depth and mirror-like reflections.”
}
```

[[Studio Lighting]] [[Celebrity Likeness]]

---

### 64. Ana de Armas 高级时装编辑提示词，适用于 Nano Banana Pro

**Author**: [Ashley 🆇](https://x.com/Ashlley_grace_)  **Date**: 2026-03-12  **Language**: en

> 为 Nano Banana Pro 提供的详细提示，用于生成一张安娜·德·阿玛斯（Ana de Armas）跪姿的高级时装编辑图片，身穿黑色粗花呢紧身衣，详细说明了纹理、配饰、灯光和美学，以呈现高度逼真的《Vogue》杂志编辑风格。

![Ana de Armas 高级时装编辑提示词，适用于 Nano Banana Pro](https://cms-assets.youmind.com/media/1773383502903_grjr3p_HDMa4hlbQAASfdc.jpg)

```
Ana de Armas, glamorous high-fashion photoshoot, young woman with long wavy light brown hair, striking green eyes, flawless makeup with bold eyeliner, glossy nude lips, kneeling pose on the floor, seductive and confident expression looking directly at camera, wearing a strapless black tweed bodysuit with textured bouclé fabric, black velvet bow detail at the bust, sparkling sequin accents, form-fitting corset-style bodysuit with high-cut legs, sheer black nylon pantyhose tights, glossy black patent leather platform high heels, elegant hands with manicured nude nails and diamond ring, studio lighting with soft shadows, neutral gray background, high-end editorial style, professional photography, ultra-detailed skin texture, cinematic lighting, sharp focus, 8k resolution, highly realistic, vogue editorial aesthetic
```

[[Studio Lighting]] [[Celebrity Likeness]] [[Photorealistic Rendering]] [[Luxury Fashion Editorial]]

---

### 65. Nano Banana Pro 的超逼真护肤品摄影提示

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-03-12  **Language**: en

> 一个详细的提示，用于生成一张逼真的、高端的蓝色化妆霜罐商业图片，该罐体部分嵌入新鲜的冰雪中，强调补水和寒冷氛围，并带有特定的相机和灯光设置。

![Nano Banana Pro 的超逼真护肤品摄影提示](https://cms-assets.youmind.com/media/1773383488908_5ebkqh_HDMMskybIAAmNTW.jpg)
![Nano Banana Pro 的超逼真护肤品摄影提示](https://cms-assets.youmind.com/media/1773383488982_dt0x1n_HDMMskRbQAAx6g1.jpg)
![Nano Banana Pro 的超逼真护肤品摄影提示](https://cms-assets.youmind.com/media/1773383488934_xe1mr8_HDMMsjIbAAIsLk0.jpg)
![Nano Banana Pro 的超逼真护肤品摄影提示](https://cms-assets.youmind.com/media/1773383489958_wjn7r5_HDMMsmXaUAATkGe.jpg)

```
Photorealistic high-end skincare product photography of a blue cosmetic cream jar labeled “VOIS – tsunami hydration” placed diagonally and partially embedded in fresh white snow. The jar surface is covered with light hoarfrost and tiny frozen condensation crystals, emphasizing an icy hydration concept. Around the product, small delicate blue primrose flowers with green leaves are naturally scattered across the snow, some partially buried and some resting on the surface. The snow texture is soft and powdery with sparkling ice crystals reflecting light. Bright winter sunlight illuminates the scene from the side, creating crisp micro-contrast, sparkling highlights on the frost and snow crystals, and soft natural shadows around the jar and flowers. The background is minimal and clean with smooth snowy bokeh and a cold airy atmosphere. Cinematic macro composition with the product perfectly sharp and the surroundings gently blurred. Premium commercial skincare advertisement style, 85mm macro lens, f/2.8, ISO 100, shallow depth of field, ultra-detailed textures, photorealistic, 8K resolution, no text overlays, no people, minimal clean background
```

[[Studio Lighting]] [[Commercial Product Photography]]

---

### 66. Kinder Joy 的超逼真产品摄影

**Author**: [Aegon](https://x.com/Fujimoto_hina)  **Date**: 2026-03-12  **Language**: en

> 一个高度结构化的 JSON 提示词，专为 Nano Banana Pro 设计，用于生成健达奇趣蛋 (Kinder Joy egg) 和定制 Q 版收藏人偶的超写实产品摄影图，其中详细说明了构图、基于参考图像的包装设计细节、光照和材质真实感。

![Kinder Joy 的超逼真产品摄影](https://cms-assets.youmind.com/media/1773383467834_tj3q7c_HDL97LUacAANUi7.jpg)
![Kinder Joy 的超逼真产品摄影](https://cms-assets.youmind.com/media/1773383467916_ug5psa_HDL97CkbQAAAj-4.jpg)

```
{
  "image_prompt": {
    "scene_type": "hyper-realistic product photography",
    "composition": {
      "main_object": "Kinder Joy surprise egg",
      "surface": "natural wooden table",
      "camera_angle": "slightly low front-facing product shot",
      "depth_of_field": "shallow depth of field with soft background blur",
      "focus": "sharp focus on egg packaging and collectible figurine"
    },
    "packaging_design": {
      "brand": "Kinder Joy",
      "illustration_style": "chibi / cartoon",
      "character_reference": "based on the uploaded image",
      "character_features": [
        "short curly dark hair",
        "black rectangular glasses",
        "trimmed beard",
        "friendly smile"
      ],
      "background_on_packaging": "colorful graffiti brick wall"
    },
    "collectible_figurine": {
      "style": "mini chibi collectible toy",
      "design_match": "same character illustrated on the packaging",
      "details": [
        "large expressive eyes",
        "big chibi head proportion",
        "black glasses",
        "curly hair texture",
        "small beard",
        "wearing a dark knitted sweater"
      ],
      "placement": "standing beside the Kinder Joy egg"
    },
    "lighting": {
      "type": "soft natural light",
      "direction": "side window lighting",
      "effect": "soft shadows and gentle highlights for photorealism"
    },
    "visual_quality": {
      "style": "photorealistic",
      "render_quality": "8K ultra-detailed",
      "materials": [
        "realistic plastic egg packaging",
        "matte vinyl toy texture",
        "natural wood grain table"
      ]
    },
    "mood": "clean, playful, collectible toy advertisement aesthetic"
  }
}
```

[[Studio Lighting]] [[Photorealistic Rendering]] [[Commercial Product Photography]] [[Material Realism]]

---

### 67. 西德尼·斯威尼 (Sydney Sweeney) 风格魅力肖像照

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-03-11  **Language**: en

> 一个高度结构化的 JSON 提示词，用于 Nano Banana 2 生成一张受 Sydney Sweeney 启发的专业魅力肖像，描绘主体身着白色蕾丝内衣和过膝皮靴坐在现代沙发上，并详细说明了姿势、灯光和相机设置。

![西德尼·斯威尼 (Sydney Sweeney) 风格魅力肖像照](https://cms-assets.youmind.com/media/1773297034822_mp2b5p_HDKp8bDb0AA4nOF.jpg)
![西德尼·斯威尼 (Sydney Sweeney) 风格魅力肖像照](https://cms-assets.youmind.com/media/1773297034887_j7ynnv_HDKp8bibQAEuR2b.jpg)
![西德尼·斯威尼 (Sydney Sweeney) 风格魅力肖像照](https://cms-assets.youmind.com/media/1773297034907_b3y039_HDKp8aLawAEUrAy.jpg)

```
{
  "photo_type": "professional glamour portrait",
  "subject": {
    "identity": "{argument name="identity" default="Sydney Sweeney"} inspired appearance",
    "age": "mid 20s",
    "gender": "female",
    "ethnicity": "American",
    "body_type": "curvy feminine physique, defined waistline, fuller hips, soft athletic proportions",
    "skin_tone": "fair warm skin tone with natural highlights",
    "hair": {
      "color": "soft golden blonde",
      "length": "long",
      "style": "smooth straight hair falling over shoulders with a soft center part"
    },
    "face": {
      "structure": "heart-shaped face with soft jawline",
      "eyes": "large expressive blue eyes",
      "eyebrows": "natural soft arches",
      "nose": "small refined nose",
      "lips": "full natural lips with subtle gloss"
    },
    "expression": {
      "emotion": "calm, confident, slightly inviting",
      "eyes": "direct gaze toward camera",
      "mouth": "slightly parted relaxed lips"
    }
  },
  "pose": {
    "position": "sitting on a modern grey upholstered sofa",
    "body_orientation": "facing forward with slight lean toward camera",
    "arms": "hands resting naturally on the sofa on both sides for balance",
    "legs": "legs slightly apart with relaxed posture",
    "posture": "confident but casual seated pose"
  },
  "outfit": {
    "style": "elegant white lace lingerie set",
    "top": {
      "type": "lace corset bralette",
      "details": "delicate floral lace embroidery, semi-sheer mesh texture, scalloped lace edges"
    },
    "bottom": {
      "type": "matching lace panties",
      "details": "floral embroidery with sheer mesh design"
    },
    "footwear": {
      "type": "white thigh-high boots",
      "material": "smooth matte leather",
      "style": "sleek modern fashion boots"
    }
  },
  "environment": {
    "location": "minimal modern indoor studio living room",
    "furniture": "soft grey upholstered couch",
    "background": "clean neutral wall with minimal distractions",
    "floor": "light tiled floor",
    "style": "simple contemporary interior"
  },
  "lighting": {
    "type": "soft diffused studio lighting",
    "direction": "front and slightly above camera",
    "quality": "even illumination with soft shadows",
    "mood": "warm, natural, flattering skin tones"
  },
  "camera": {
    "angle": "eye-level perspective",
    "distance": "medium full-body framing",
    "lens": "50mm portrait lens",
    "focus": "sharp focus on subject with slight background blur"
  },
  "image_style": {
    "aesthetic": "high-end glamour photography",
    "color_grading": "soft neutral tones with warm highlights",
    "skin_texture": "natural realistic skin detail",
    "resolution": "ultra high resolution",
    "quality": "photorealistic, studio-quality"
  }
}
```

[[Studio Lighting]] [[Boudoir Photography]] [[Celebrity Inspired Portrait]]

---

### 68. 高级时尚影棚肖像

**Author**: [Jack](https://x.com/j_smeaton99)  **Date**: 2026-03-10  **Language**: en

> 一个用于 Nano Banana Pro 和 Nano Banana 2 的图像生成提示，描述了一位身穿祖母绿缎面衬衫和象牙色长裤的女性，在宝蓝色摄影棚背景下拍摄的全身时尚编辑照片，强调柔和的摄影棚灯光和鲜明的色彩对比。

![高级时尚影棚肖像](https://cms-assets.youmind.com/media/1773210658854_1u0s9c_HDDnFfuaMAM67a1.jpg)
![高级时尚影棚肖像](https://cms-assets.youmind.com/media/1773210658850_tlt5oo_HDDnFNJakAAATvh.jpg)

```
{
  "scene": "high-fashion studio portrait with vibrant backdrop",
  "subject": {
    "type": "woman",
    "age": "mid 20s",
    "pose": "standing slightly angled to the camera with her weight on one leg, one hand resting lightly on her hip while the other gently brushes her hair back",
    "expression": "confident and poised with a subtle editorial smile, looking directly at the camera"
  },
  "outfit": {
    "top": "elegant emerald green satin blouse with long flowing sleeves",
    "bottom": "high-waisted ivory wide-leg trousers with a tailored fit",
    "layer": "short structured cream blazer worn open",
    "footwear": "sleek pointed-toe heels in soft beige leather"
  },
  "environment": {
    "background": "smooth royal-blue studio backdrop with a slight gradient",
    "floor": "clean neutral studio floor reflecting a little soft light",
    "setting": "professional photography studio setup"
  },
  "lighting": {
    "type": "soft studio key light with gentle fill",
    "style": "bright fashion lighting creating soft shadows and highlighting fabric texture"
  },
  "camera": {
    "framing": "full-body editorial fashion shot",
    "angle": "slightly above eye level for a flattering magazine-style perspective",
    "lens": "85mm portrait lens"
  },
  "style": {
    "aesthetic": "modern fashion editorial",
    "mood": "confident, stylish, vibrant",
    "details": "sharp clothing texture, clean composition, vivid color contrast, subtle film grain"
  }
}
```

[[Studio Lighting]] [[Fashion Editorial]]

---

### 69. 全身时尚杂志编辑肖像

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-03-10  **Language**: en

> 一个为 Yapper 上的 Google Nano Banana Pro 设计的详细 JSON 格式提示，用于生成一张全身、超逼真的时尚杂志社论肖像，描绘一位身穿定制正装、头戴宽边帽的优雅欧洲女性，强调专业的影棚灯光和 8K 分辨率。

![全身时尚杂志编辑肖像](https://cms-assets.youmind.com/media/1773210653377_78j9r9_HDAoAZiaMAQD6bV.jpg)
![全身时尚杂志编辑肖像](https://cms-assets.youmind.com/media/1773210653332_7layi6_HDAoAPzaMAAn2FA.jpg)
![全身时尚杂志编辑肖像](https://cms-assets.youmind.com/media/1773210653395_ptnbio_HDAoAcrboAAkXnY.jpg)

```
{
  "prompt": "Full-body fashion magazine editorial portrait of the same elegant European woman around 25 years old standing confidently in a modern professional photography studio. She has natural facial proportions, delicate cheekbones, expressive eyes, and realistic skin texture with fine detail. She is posing confidently as if for the cover of a world-famous fashion magazine. She is wearing a stylish formal outfit consisting of a tailored fitted blazer, high-waisted formal trousers, and a crisp blouse underneath. A fashionable wide-brim elegant hat completes the look, adding a strong editorial character. Her pose is powerful and confident, standing tall with one hand lightly adjusting the brim of her hat while the other hand rests in her pocket. Her posture is straight and self-assured, with a calm, confident expression looking directly at the camera. Her hair is neatly styled with natural movement visible under the hat. Lighting is professional fashion studio lighting with a large soft key light and subtle rim light creating depth and highlighting the textures of the formal outfit. Background is a clean minimalist studio backdrop, neutral light tone, keeping full attention on the model. Composition is high-end fashion editorial style, full-body framing, sharp focus, shallow depth of field, ultra-realistic, modern fashion photography, magazine cover aesthetic, extremely detailed, 8K resolution."
}
```

[[Studio Lighting]] [[8K Resolution]] [[Magazine Editorial]]

---

### 70. 实验性纳米香蕉高级定制礼服提示

**Author**: [Gadgetify](https://x.com/Gdgtify)  **Date**: 2026-03-09  **Language**: en

> 这是一个为 Nano Banana 设计的实验性结构化提示，用于生成一件超逼真的高级定制晚礼服。它使用一个“TRANSFER_MATRIX”来定义设计元素（孔雀尾巴、彩色玻璃、玫瑰荆棘、冰柱），并使用一个“INSTRUCTION”在影棚灯光下构建一个既华丽又危险的廓形。

![实验性纳米香蕉高级定制礼服提示](https://cms-assets.youmind.com/media/1773124334491_wv43ha_HC3KOcKW8AEBXUE.jpg)
![实验性纳米香蕉高级定制礼服提示](https://cms-assets.youmind.com/media/1773124334691_cu0jh1_HC3KRKWaYAA-2MC.jpg)

```
TRANSFER_MATRIX:
peacock tail fan -> gown train expansion geometry
cathedral stained glass -> bodice panel segmentation
rose thorns -> silver embroidery edge logic
icicles -> earring taper logic

INSTRUCTION:
Build a haute couture evening gown using the transfer matrix above.
The silhouette must feel regal and dangerous, not costume-like.
Photorealistic luxury fashion editorial, studio lighting, black background.
```

[[Studio Lighting]]

---

### 71. 超逼真奢华护肤品摄影（重复）

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-03-09  **Language**: en

> 为 Google Veo 3.1 和 Nano Banana 2 生成超逼真奢华护肤品广告的详细提示。场景中，一个装有草莓粉色面霜的玻璃罐置于反光表面上，周围环绕着新鲜草莓和融化的草莓冰淇淋，在高级影室灯光下营造出一种奢华、甜点般的审美。

![超逼真奢华护肤品摄影（重复）](https://cms-assets.youmind.com/media/1773124341436_rtf1ou_HC-DVa5boAAMFvY.jpg)
![超逼真奢华护肤品摄影（重复）](https://cms-assets.youmind.com/media/1773124341568_frncsu_HC-DWFRa0AA2WC4.jpg)

```
Ultra-realistic luxury skincare product photography featuring a glass cosmetic jar labeled “ONE POSE” placed at the center of a glossy reflective surface. The jar contains a vibrant strawberry-pink cream with a soft gradient fading into a frosted white lid, and a smooth swirl of creamy pink product melting over the top and dripping down the sides of the jar like glossy dessert glaze. Surrounding the product are fresh ripe strawberries and halved strawberries with visible seeds and juicy texture, arranged naturally around the base. Soft scoops of strawberry ice cream sit beside the fruit, slightly melting and blending into a glossy pink cream puddle that spreads across the surface. The background is a soft pastel pink studio gradient that enhances the strawberry tones. Premium studio lighting from above and the side creates crisp reflections on the glass jar, soft highlights on the melting cream and ice cream texture, and gentle shadows beneath the product.

The composition feels indulgent and dessert-inspired while maintaining a clean luxury cosmetic advertising aesthetic, hyper-realistic textures, shallow depth of field, cinematic lighting, ultra-detailed 8K product photography.
```

[[Studio Lighting]] [[Reflective Surface]]

---

### 72. Y2K 流行美学粉色更衣室人像摄影

**Author**: [LexiPrompt](https://x.com/Artist04048661)  **Date**: 2026-03-07  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张超逼真的 Y2K 流行美学编辑图片，画面中一名年轻女子身穿黑色比基尼，在单色粉色更衣室中摆姿势。该提示详细说明了主体属性、服装、环境、灯光和相机设置，并要求提供一张参考图片以确保面部相似度。

![Y2K 流行美学粉色更衣室人像摄影](https://cms-assets.youmind.com/media/1772951301819_21w8i8_HCxq71KWwAEky3O.jpg)
![Y2K 流行美学粉色更衣室人像摄影](https://cms-assets.youmind.com/media/1772951301893_r3d5ug_HCxq75zWAAArLTn.jpg)
![Y2K 流行美学粉色更衣室人像摄影](https://cms-assets.youmind.com/media/1772951302035_2iu6r7_HCxq76UaUAAg5MC.jpg)

```
{
  "image_generation_prompt": {
    "subject": {
      "description": "Young woman with a strong resemblance to the subject in the reference image.",
      "hair": "Sleek, high pigtails with long, straight extensions reaching down to the waist; styled with bubble-like {argument name="accessory color" default="pink"} hair accessories at the base of each pigtail.",
      "face": "Neutral, sultry expression with defined 'cat-eye' winged eyeliner, sculpted eyebrows, and glossy nude lips; matte skin finish with soft contouring.",
      "body": "Slender, athletic physique with smooth skin texture and a subtle sheen on the midriff."
    },
    "attire": {
      "clothing": "Minimalist {argument name="bikini color" default="black"} string bikini; the top features gathered fabric at the cups with a center ring detail, while the bottoms are low-rise with side-tie strings.",
      "style": "Y2K Pop-Aesthetic / High-Fashion editorial."
    },
    "styling_and_accessories": {
      "jewelry": [
        "Pink bubble hair ties",
        "Pink heart-shaped pen",
        "Lavender-lined open notebook",
        "Pink heart-shaped padlocks on lockers"
      ]
    },
    "environment": {
      "setting": "A stylized, monochromatic pink locker room.",
      "background": "Rows of tall, metallic pink lockers in alternating shades of bubblegum and rose; some lockers decorated with pink pom-poms and stickers.",
      "water": "None"
    },
    "pose": {
      "posture": "Reclining sideways on a pink bench, propped up on one elbow.",
      "arms": "Right hand is holding a pen over an open notebook; left hand is resting naturally on the upper thigh.",
      "angle": "Eye-level, medium shot."
    },
    "lighting_and_mood": {
      "lighting": "Soft, diffused studio lighting that eliminates harsh shadows; even, high-key illumination to emphasize the pink tones.",
      "mood": "Playful, curated, and vibrant; 2000s teen-dream aesthetic.",
      "colors": "Dominant monochromatic pink palette (bubblegum, rose, magenta) contrasted sharply by the subject's black attire and dark hair."
    },
    "camera_and_technical": {
      "style": "Ultra Photorealistic, RAW photo.",
      "lens": "50mm prime lens for natural proportions.",
      "aperture": "f/4.0 for deep focus, keeping both the subject and the locker background crisp.",
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

[[Studio Lighting]] [[Identity Reference Portrait]] [[Fashion Editorial Portrait]]

---

### 73. 可口可乐飞溅产品摄影

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-03-05  **Language**: en

> 生成一张可口可乐罐的高清产品照片的提示，罐身仿佛从空中被拉出，周围环绕着可乐液体、冰块和水花，采用专业的影棚布光，背景为黑色和红色。

![可口可乐飞溅产品摄影](https://cms-assets.youmind.com/media/1772778710340_ljj72x_HCnV_4OawAIcZyp.jpg)

```
A white easy to pull filled Coca Cola is hanging in the air, surrounded by a large amount of cola, ice cubes, and water splashes. The transparent cup is printed with red text, and the overall design is simple and clean. This image adopts a product photography style, using professional studio lighting to present high-definition textures in the style of Sony A7s. The background is black and red --ar 2:3 --stylize 250
```

[[Studio Lighting]] [[Commercial Beverage Photography]] [[Liquid Splash Effect]]

---

### 74. 浮动精灵产品摄影提示

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-03-04  **Language**: en

> 生成一张超逼真产品照片的提示词：一个透明的雪碧杯漂浮在空中，周围环绕着飞溅的水花、冰块和气泡，强调微距清晰度和专业的影棚灯光。

![浮动精灵产品摄影提示](https://cms-assets.youmind.com/media/1772692201195_k9bw1r_HClMUymawAE-tEJ.jpg)

```
A transparent cup filled with fresh Sprite lemon soda floating in the air, surrounded by sparkling lemon-lime soda splashes, bright ice cubes, and tiny carbonation bubbles bursting around the drink. The cup features green minimal text design, giving a fresh and clean brand look. Hyper-realistic beverage product photography with professional studio lighting, crisp texture details, macro clarity as if shot with Sony A7s. Black and neon green background highlighting freshness --stylize 250
```

[[Studio Lighting]] [[Commercial Beverage Photography]]

---

### 75. 爆炸视图产品设计图提示

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-03-02  **Language**: en

> 一个简洁的提示，用于生成产品或车辆的干净、三维爆炸图，带有材质点缀，强调高度精细的内部组件、影棚布光和产品摄影风格。

![爆炸视图产品设计图提示](https://cms-assets.youmind.com/media/1772519750823_kg7gtf_HCZ50ChbkAAcNFK.jpg)
![爆炸视图产品设计图提示](https://cms-assets.youmind.com/media/1772519750828_33ivx9_HCZ50CkbQAAQw0T.jpg)
![爆炸视图产品设计图提示](https://cms-assets.youmind.com/media/1772519750819_lvdpsr_HCZ50Dka0AAFQtC.jpg)
![爆炸视图产品设计图提示](https://cms-assets.youmind.com/media/1772519751567_zj27ix_HCZ50FMbgAEXndC.jpg)

```
product design, {argument name="object or vehicle" default="[object or vehicle with material accents]"}, exploded view diagram, white background, three-dimensional, highly detailed internal components, studio lighting, product photography, best quality
```

[[Studio Lighting]] [[Technical Illustration]] [[Exploded View Diagram]] [[3D Product Rendering]]

---

### 76. Nano Banana 2 通用图像生成提示

**Author**: [TWnese](https://x.com/TWnese)  **Date**: 2026-03-02  **Language**: zh

> 一个适用于 Nano Banana 2 的通用提示词，旨在生成高质量的详细图像，而无需使用专业术语。它侧重于生成一个主体，该主体站立于笔记本草图之上或从中浮现，强调纹理、低角度视角和影棚布光。

![Nano Banana 2 通用图像生成提示](https://cms-assets.youmind.com/media/1772519752894_9pr8id_HCZZPubaAAAbHm-.jpg)
![Nano Banana 2 通用图像生成提示](https://cms-assets.youmind.com/media/1772519752844_advut8_HCZZMEGbEAIwAC6.jpg)
![Nano Banana 2 通用图像生成提示](https://cms-assets.youmind.com/media/1772519752884_olixrd_HCZZKpsacAAGAOe.jpg)
![Nano Banana 2 通用图像生成提示](https://cms-assets.youmind.com/media/1772519754206_lgi9ym_HCZZTbuakAA5Nt6.jpg)

```
桌上筆記本上畫著 {argument name="主題" default="雪豹"} 素描,栩栩如生的實體站在或出現在素描上。 側身居中,紋理細緻,低角度拍攝,近距特寫,演播室燈光,超寫實,8K --ar 1:1
```

[[Studio Lighting]] [[3D Pop-out Illusion]] [[Low Angle Perspective]]

---

### 77. 双重超写实肖像提示词

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-03-01  **Language**: en

> 两个独立的提示，用于生成同一位女性的超写实肖像，侧重于不同的光线和构图风格。提示 1 使用柔和的自然窗光，拍摄电影般的侧角度肖像；而提示 2 则使用均匀柔和的影棚灯光，拍摄干净、正面的专业头像照。

![双重超写实肖像提示词](https://cms-assets.youmind.com/media/1772433497902_3wf4re_HCVLzXwbUAACc0p.jpg)
![双重超写实肖像提示词](https://cms-assets.youmind.com/media/1772433497932_pgc6t9_HCVLzXzb0AEQGrS.jpg)

```
Prompt 1 (First Image – Blue Top, Side Angle Portrait):

Ultra-realistic close-up portrait of a beautiful woman with light green eyes and soft freckles, auburn curly hair styled in a loose messy bun with natural wispy bangs framing her face. She is wearing a deep blue V-neck top. Shot at a slight side angle with her head turned toward the camera, confident and calm expression. Soft natural window light casting gentle shadows on one side of her face, neutral beige background. Minimal makeup, natural skin texture visible, cinematic lighting, shallow depth of field, 85mm lens, high resolution, professional fashion photography, sharp focus on eyes, soft bokeh background.

⸻

Prompt 2 (Second Image – Front-Facing Hoodie Portrait):

Hyper-realistic front-facing portrait of a woman with light green eyes, subtle freckles across her cheeks and nose, auburn hair parted in the center and tied back in a low loose bun with soft strands framing her face. She is wearing a dark grey hoodie. Neutral expression, direct eye contact with camera. Even soft studio lighting, minimal shadows, clean white background. Natural skin texture, no heavy makeup, high detail, 85mm lens, shallow depth of field, professional headshot photography, ultra sharp focus, realistic skin tones, 4K resolution.
```

[[Studio Lighting]] [[Hyperrealistic Portrait]] [[Soft Diffused Light]] [[Natural Window Light]]

---

### 78. 奢华洗发水瓶飞溅广告

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-03-01  **Language**: en

> 生成一张超逼真、高速的奢华洗发水瓶商业图片，瓶身飞溅穿透清澈水面。强调动态液体在空中凝固的瞬间，电影级影棚灯光，冷蓝色调，以及高速摄影技术，以 8K 分辨率呈现高端护肤品广告风格。

![奢华洗发水瓶飞溅广告](https://cms-assets.youmind.com/media/1772433498260_zaxx71_HCTPYqxbEAEnmSr.jpg)
![奢华洗发水瓶飞溅广告](https://cms-assets.youmind.com/media/1772433498278_2o41r5_HCTPYutbIAAZffi.jpg)
![奢华洗发水瓶飞溅广告](https://cms-assets.youmind.com/media/1772433498270_fpqqww_HCTPYspbEAI3q-T.jpg)

```
Ultra-realistic luxury shampoo bottle (matte green, minimal branding) splashing through crystal-clear water, dynamic liquid motion frozen mid-air, detailed droplets and mist, glossy reflections on wet surface, cinematic studio lighting with cool blue tones, soft glow rim light, dark gradient background, high-speed photography, ultra-sharp focus, premium skincare advertising style, clean composition, 8K.
```

[[Studio Lighting]] [[8K Resolution]] [[Liquid Splash Photography]] [[Commercial Beauty Photography]]

---

### 79. 焦橙色背景下时尚男士的电影感肖像

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-03-01  **Language**: en

> 一个详细的文本提示，用于生成一个时尚男士的半身、高分辨率肖像。该提示详细说明了服装（焦橙色圆领衫、黑色太阳镜）、姿势（手放在衣领处，略微倾斜）、灯光（电影级影棚灯光，带有强烈的柔和主光和轮廓光）以及调色板（焦橙色、铁锈色、可可色）。

![焦橙色背景下时尚男士的电影感肖像](https://cms-assets.youmind.com/media/1772433518059_33sfkd_HCSXsVBbEAAF7wD.jpg)
![焦橙色背景下时尚男士的电影感肖像](https://cms-assets.youmind.com/media/1772433518109_g4ob77_HCSXsVvbEAERDub.jpg)

```
create an image of a stylish man in a plain burnt orange crewneck shirt and glossy black rectangular sunglasses, bust-up portrait, one hand at the collar/neckline as if straightening the shirt, slight forward lean, head tilted a few degrees, gaze off-camera downward, confident “aura” calm set a seamless deep rust-to-warm chocolate studio backdrop with smooth gradient falloff light with cinematic studio lighting: strong soft key at 45° camera-left, minimal fill to keep shadows rich, subtle rim light camera-right for separation, add elegant specular highlights on the lenses use a refined palette of burnt orange, rust, and cocoa with natural skin tones shoot at eye level on a full-frame camera, 85mm lens, f/2.2, crisp texture detail, shallow depth of field, centered composition with negative space and subtle depth
```

[[Studio Lighting]] [[Cinematic Fashion Editorial]] [[Fashion Male Portrait]]

---

### 80. 奢华漂浮马卡龙广告

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-02-28  **Language**: en

> 一个用于生成超现实、高速摄影风格广告的提示，广告内容为漂浮的马卡龙，其外壳开裂，新鲜水果悬浮在空中，背景为戏剧性的黑色，并辅以影棚灯光。

![奢华漂浮马卡龙广告](https://cms-assets.youmind.com/media/1772346659242_4ja7hx_HCPYG4KbEAMYGll.jpg)
![奢华漂浮马卡龙广告](https://cms-assets.youmind.com/media/1772346659319_31ef74_HCPYGzcbEAI46HM.jpg)
![奢华漂浮马卡龙广告](https://cms-assets.youmind.com/media/1772346660845_wr7muf_HCPYG1ibEAAyUED.jpg)

```
Ultra-realistic floating macarons with cracked shells revealing rich jam/cream filling, fresh raspberries, blueberries, and citrus zest pieces suspended mid-air, dynamic crumbs and powdered sugar particles, black background, dramatic studio lighting, high-speed photography, sharp focus, macro detail, soft shadows, vibrant colors, luxury dessert advertising, 8K, perfect composition.
```

[[Studio Lighting]]

---

### 81. 3D 迷你纽约城立体模型

**Author**: [PixPretty](https://x.com/PixPrettyAI)  **Date**: 2026-02-28  **Language**: en

> 生成一张纽约市 3D 微缩模型照片的提示词，该模型从放置在深色桌面上的街景地图中浮现。它指定了关键地标、霓虹灯元素、车辆以及工作室柔和灯光和宽高比等技术细节，营造出一种都市立体模型效果。

![3D 迷你纽约城立体模型](https://cms-assets.youmind.com/media/1772346677365_w8ijx8_HCOYCZzaYAAy7en.jpg)

```
"A street-style map of New York City placed on a dark textured tabletop, with a photorealistic miniature version of New York City emerging from it the Statue of Liberty, the Empire State Building, the Brooklyn Bridge, a lush green Central Park, clusters of glowing neon skyscrapers, yellow taxis and silver subway trains, and a detailed street grid base with "{argument name="city name" default="NEW YORK"}" typography. All elements grow from the map like a 3D urban diorama. Studio soft lighting, cinematic depth, 2:3 format."
```

[[Studio Lighting]] [[Diorama Art]]

---

### 82. 拿铁瓶的高速商业食品摄影提示

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-26  **Language**: en

> 一个详细的 JSON 结构化提示，旨在生成超逼真、高速的商业食品摄影作品，内容为一个装满奶油拿铁的时尚玻璃瓶，强调动态液体碰撞、光泽的影棚照明和丰富的调色板。

![拿铁瓶的高速商业食品摄影提示](https://cms-assets.youmind.com/media/1772174106944_i5t05f_HCDI1qlaMAElady.jpg)
![拿铁瓶的高速商业食品摄影提示](https://cms-assets.youmind.com/media/1772174106665_toi7tq_HCDI1pXaAAAQxEw.jpg)

```
{
  "master_prompt": {
    "scene_type": "high-speed commercial food photography",
    "product": {
      "type": "sleek glass bottle filled with creamy latte",
      "brand_name": "VELOUR CRÈME",
      "label_design": "minimalist circular white label with bold black sans-serif typography",
      "liquid_color": "rich caramel-toned iced coffee"
    },
    "composition": {
      "action": "dynamic high-velocity liquid collision",
      "surrounding_elements": [
        "sculptural swirls of thick white milk",
        "spiraling splashes of dark espresso",
        "floating roasted coffee beans",
        "vibrant red coffee cherries with glossy skin",
        "mist of micro-droplets for texture"
      ],
      "placement": "centered hero bottle with a perfect reflection on a dark glossy surface"
    },
    "lighting": {
      "style": "glossy studio product lighting",
      "effects": [
        "rim lighting to define bottle edges",
        "specular highlights on liquid splashes",
        "warm golden bokeh in the background"
      ]
    },
    "color_palette": {
      "background": "deep amber and chocolate brown gradient",
      "accents": "cream, espresso, and pops of cherry red"
    },
    "technical_specs": {
      "camera": "macro lens, eye-level angle",
      "shutter": "ultra-fast freeze-motion",
      "depth_of_field": "shallow focus on the label, soft blur on splashing background",
      "quality": "8K resolution, photorealistic texture"
    }
  }
}
```

[[Studio Lighting]] [[Structured JSON Prompt]] [[Dynamic Liquid Splash]]

---

### 83. 风格化柳条卡通雕像

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-02-25  **Language**: en

> 一个用于生成高度精细、超逼真的风格化漫画人物雕像的提示，该雕像完全由编织柳条/藤条材料制成，强调超逼真的纹理、影棚布光和艺术工艺。

![风格化柳条卡通雕像](https://cms-assets.youmind.com/media/1772087649701_0tqhhw_HB9wErJa4AA_xv2.jpg)
![风格化柳条卡通雕像](https://cms-assets.youmind.com/media/1772087649680_q5i5xl_HB9wEkHaMAApdE0.jpg)
![风格化柳条卡通雕像](https://cms-assets.youmind.com/media/1772087649691_0fpc19_HB9wEhsbwAAZ5yT.jpg)
![风格化柳条卡通雕像](https://cms-assets.youmind.com/media/1772087650416_02qv98_HB9wEyYbIAAVqsy.jpg)

```
A highly detailed stylized caricature figurine of a person made entirely from woven wicker / rattan material, big head and small body proportions, hyper-realistic texture with intricate basket weave patterns forming facial features, hair, and clothing. The figure stands on a small woven base placed on a wooden table. Background is a warm wooden wall with subtle brand logos or props. Studio lighting, soft shadows, shallow depth of field, ultra-detailed, 8K resolution, sharp focus, photorealistic, artistic craftsmanship, handcrafted sculpture look.
```

[[Studio Lighting]]

---

### 84. 奢华家居香氛商业摄影 (JSON 格式)

**Author**: [Jack](https://x.com/j_smeaton99)  **Date**: 2026-02-24  **Language**: en

> 一个高度详细的 JSON 提示，用于生成奢华室内清新喷雾的超逼真商业摄影，重点关注构图、高端照明和精致的室内生活方式美学。

![奢华家居香氛商业摄影 (JSON 格式)](https://cms-assets.youmind.com/media/1772001517507_b32xyt_HB7lrHqacAESO0y.jpg)
![奢华家居香氛商业摄影 (JSON 格式)](https://cms-assets.youmind.com/media/1772001517494_08zuoy_HB7lrINagAAErnO.jpg)

```
{
  "master_prompt": {
    "scene_type": "ultra-realistic luxury home fragrance commercial photography",

    "product": {
      "type": "luxury room freshener spray",
      "brand_name": "VÉRÉLLE",
      "product_name": "Lumière Atmosphère, Signature Room Essence",
      "container_shape": "slender architectural glass atomizer with elongated silhouette",
      "material": "crystal-clear faceted glass",
      "finish": "prismatic transparency with refined light refraction",
      "cap_design": "brushed champagne-gold magnetic cap with sculpted top",

      "label_design": {
        "style": "Parisian luxury serif typography",
        "primary_text": "Lumière Atmosphère",
        "secondary_text": "Signature Room Essence",
        "finish": "champagne foil emboss with micro-engraved detailing"
      },

      "liquid_color": "soft golden champagne tone with luminous clarity"
    },

    "composition": {
      "placement": "center hero placement",
      "pedestal": "ivory marble pedestal with subtle gold veining",
      "base_surface": "polished stone reflective surface",

      "surrounding_elements": [
        "white orchid blossoms",
        "linen fabric folds",
        "glass dew droplets",
        "soft eucalyptus sprigs"
      ],

      "atmospheric_effect": "delicate fragrance mist diffusing elegantly around the bottle"
    },

    "lighting": {
      "style": "high-end interior luxury lighting",
      "key_light": "soft diffused glow for glass clarity",
      "rim_light": "warm highlights defining bottle edges",
      "fill_light": "gentle ambient fill for soft shadows",
      "reflections": "controlled specular highlights for premium finish"
    },

    "background": {
      "color": "warm ivory to champagne gradient",
      "style": "luxury interior editorial backdrop",
      "depth": "cinematic shallow depth with soft falloff"
    },

    "camera": {
      "angle": "slightly low hero angle",
      "focus": "typography and crystal texture",
      "depth_of_field": "cinematic shallow depth",
      "resolution": "8K ultra-detailed clarity"
    },

    "mood_keywords": [
      "refined living",
      "luxury home ambiance",
      "clean elegance",
      "premium interior lifestyle",
      "serene atmosphere",
      "timeless sophistication"
    ]
  }
}
```

[[Studio Lighting]] [[Structured JSON Prompt]]

---

### 85. 键盘键帽拼成的狗狗俯视图

**Author**: [Aylin](https://x.com/Ai_aylinfc)  **Date**: 2026-02-24  **Language**: en

> 一个详细的提示，用于创建一张逼真的、俯视平铺的图像，内容是一只完全由机械键盘键帽组成的狗剪影，强调精确的排列、逼真的字符和纯白色背景上的柔和工作室照明。

![键盘键帽拼成的狗狗俯视图](https://cms-assets.youmind.com/media/1772001523931_vt3vmu_HB4yLIaboAARdHP.jpg)
![键盘键帽拼成的狗狗俯视图](https://cms-assets.youmind.com/media/1772001524120_i4dipq_HB4yLIab0AEA2uv.jpg)

```
Create a photorealistic 8K top-down flat lay composition of a dog formed entirely from real mechanical keyboard keycaps. The keycaps should be matte PBT plastic in OEM or Cherry profile, arranged in a tight, uniform grid. Every keycap must include crisp, realistic legends—letters, numbers, punctuation, function keys, arrows, and symbols—printed in double-shot or dye-sublimated style. No blank keycaps are allowed. The distribution of legends should feel naturally randomized, as if sourced from real keyboards, with believable variation.

The keycaps must be precisely arranged to form a clean, clearly recognizable side-profile silhouette of a dog. The silhouette should be sharp and well-defined, with smooth contour transitions that accurately capture the dog’s head, ears, body, legs, and tail. Outside the silhouette, there should be pure white negative space with no additional objects or distractions.

The background must be seamless, pure white. The composition should have a 16:9 aspect ratio and be perfectly centered in frame. The camera angle must be an exact 90-degree overhead view with minimal perspective distortion, maintaining a completely flat surface appearance.

Lighting should be soft, diffused studio lighting with very gentle contact shadows beneath each keycap and subtle edge highlights that emphasize the plastic texture. Avoid harsh shadows or dramatic contrast. The overall result should feel ultra-sharp, clean, noise-free, and highly detailed, showcasing realistic material texture and precise arrangement.
```

[[Studio Lighting]] [[White Background]]

---

### 86. 魅惑红厅时尚肖像

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-02-23  **Language**: en

> 一张高度细致、结构化的提示，用于生成一张高级时尚魅力照片。场景中，一位曲线玲珑的女性身着黑色内衣和红色迷你裙，躺在亮红色皮沙发上，强调高对比度、影棚灯光和诱惑氛围。

![魅惑红厅时尚肖像](https://cms-assets.youmind.com/media/1771915008869_xjeqsy_HB3APsCawAAfkmp.jpg)
![魅惑红厅时尚肖像](https://cms-assets.youmind.com/media/1771915008859_ccbdht_HB3APsGa0AA1WFP.jpg)

```
{
  "title": "Seductive Red Lounge Portrait",
  "type": "fashion_glamour_photography",
  "aspect_ratio": "16:9",
  "subject": {
    "gender": "female",
    "age": "adult",
    "body_type": "curvy, voluptuous",
    "pose": "lying on stomach on a red leather couch, upper body slightly propped up on forearms, head tilted slightly forward, direct gaze toward camera",
    "expression": "confident, sultry, relaxed",
    "hair": {
      "color": "blonde with darker roots",
      "style": "loose updo with soft strands framing the face"
    },
    "makeup": {
      "style": "glamorous",
      "details": "defined brows, contoured cheeks, soft blush, glossy nude lips, subtle smoky eye"
    }
  },
  "wardrobe": {
    "top": "black bra with thin straps",
    "bottom": "black thong partially visible",
    "skirt": "tight red mini skirt pulled slightly upward",
    "footwear": "black high heels with stiletto heel",
    "accessories": "large metallic hoop earrings"
  },
  "environment": {
    "location": "studio setting",
    "furniture": "bright red leather couch with tufted backrest",
    "background": "solid red padded leather panels",
    "floor": "dark, minimally visible"
  },
  "lighting": {
    "type": "studio lighting",
    "style": "even, soft but directional",
    "key_light": "front-facing softbox highlighting face and upper body",
    "fill_light": "subtle fill to reduce harsh shadows",
    "highlights": "soft sheen on skin and leather surface"
  },
  "camera": {
    "angle": "side perspective at couch level",
    "focus": "sharp focus on face and torso",
    "depth_of_field": "moderate, subject fully in focus",
    "lens": "85mm portrait lens",
    "quality": "high resolution, ultra-detailed"
  },
  "color_palette": {
    "primary_colors": ["red", "black"],
    "skin_tones": "warm, golden undertones",
    "contrast": "high contrast between red couch and black clothing"
  },
  "mood": "bold, seductive, high-fashion glamour",
  "style_keywords": [
    "editorial fashion",
    "luxury glamour",
    "sensual pose",
    "studio photography",
    "high detail",
    "cinematic lighting",
    "vibrant red tones",
    "modern aesthetic"
  ],
  "render_settings": {
    "resolution": "4k",
    "sharpness": "high",
    "texture_detail": "enhanced skin texture and leather detail",
    "post_processing": "color grading emphasizing red saturation and warm skin tones"
  }
}
```

[[Studio Lighting]]

---

### 87. 低多边形折纸动物系列

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-02-23  **Language**: en

> 一组用于生成超干净的低多边形折纸动物（鸭子、熊猫、虎崽和一组动物）3D 渲染的提示，这些动物由纹理纸板制成，强调几何设计、工作室照明和深海军蓝背景。

![低多边形折纸动物系列](https://cms-assets.youmind.com/media/1771914983376_rt8uwi_HBzeyswbcAAO6qy.jpg)
![低多边形折纸动物系列](https://cms-assets.youmind.com/media/1771914983359_u76f5q_HBzeysxaIAAct8j.jpg)
![低多边形折纸动物系列](https://cms-assets.youmind.com/media/1771914983412_fnuu5g_HBzeysjagAEyr2R.jpg)
![低多边形折纸动物系列](https://cms-assets.youmind.com/media/1771914984660_8hvr0k_HBzeysmbMAAGbjV.jpg)

```
A minimalist low-poly origami duck sculpture made of folded cardboard, geometric faceted design, warm brown paper texture, sharp angular edges, large round glossy eye, small orange beak, studio lighting, soft shadow beneath, centered composition, dark navy blue gradient background, ultra-clean 3D render, high detail, cinematic lighting, depth of field, 4K resolution.

⸻

Prompt:
A collection of low-poly origami animals arranged in a studio portrait — panda, dog, deer, bear — made of textured cardboard paper, geometric faceted shapes, minimalist design, neutral earthy tones (brown, beige, black, cream), large circular eyes, symmetrical front-facing composition, soft studio lighting, subtle shadows, dark blue gradient background, ultra-detailed 3D render, sharp focus, clean aesthetic, 4K.

⸻

Prompt:
Centered low-poly origami panda sitting upright, faceted geometric cardboard sculpture, cream and brown paper textures, minimalistic angular design, small round black eyes, soft diffused studio lighting, realistic paper grain detail, subtle ground shadow, dark navy gradient background, ultra-clean 3D render, cinematic composition, 4K resolution.

⸻

Prompt:
Cute low-poly origami tiger cub sitting forward-facing, geometric faceted cardboard sculpture, warm orange and beige paper texture, stylized black stripe details, big round expressive eyes, symmetrical centered composition, studio lighting with soft shadows, dark blue gradient background, ultra-detailed 3D render, sharp focus, high realism paper texture, 4K cinematic render.
```

[[Studio Lighting]]

---

### 88. 超逼真高端时尚杂志封面拍摄提示

**Author**: [Maya](https://x.com/mayadelmare)  **Date**: 2026-02-22  **Language**: en

> 这是一个详细的提示，用于生成一张超逼真、高端时尚杂志封面拍摄照片，主角是 Sydney Sweeney、Ana De Armas 和第三位女性（基于附带图片）。该提示详细说明了姿势、服装（粉色和黑色亮面紧身衣）、发型、妆容、灯光和相机设置，以实现高端编辑风格，并侧重于照片的真实感和自然外观。

![超逼真高端时尚杂志封面拍摄提示](https://cms-assets.youmind.com/media/1771828712845_uvsiup_HBx4-N_WoAAlnzr.jpg)

```
Ultra realistic high-fashion magazine cover photoshoot of {argument name="first celebrity" default="Sydney Sweeney"}, {argument name="second celebrity" default="Ana De Armas"} and woman in attached image. Sydney Sweeney is kneeling on smooth studio floor with knees together and hands flat on the ground in front, body leaning forward, direct eye contact with camera, wearing a form-fitting long-sleeve light pink glossy bodysuit with subtle white curved line patterns along the sides and center, high neckline, long straight blonde flowing down the back, minimal makeup with glossy lips and defined eyes, white high-top sneakers with platform sole. Ana de Armas is also kneeling on smooth studio floor with knees together but stand opposite side of Sydney Sweeney. Ana de Armas' hands flat on the ground in front, body leaning forward, direct eye contact with camera. She has dark hair. She wears same with Sydney Sweeney. Third woman is standing tall between them with crossed arms. She is woman in attached image. She wears same outfit but black. She has brunette to blonde wavy ombre hair. She has a fit, highly defined hourglass figure with an extremely narrow waist and significantly wider, voluptuous hips and eaturing a large, heavy natural bust. Bright clean studio lighting with soft reflections on the fabric, minimalist gray background, high-end fashion editorial style, photorealistic, shot on medium format camera with cinematic lenses, ultra detailed skin texture, natural look, non-AI generated appearance
```

[[Studio Lighting]] [[Sydney Sweeney]] [[Ana De Armas]]

---

### 89. 3D 动画运动鞋广告提示

**Author**: [auqib](https://x.com/auqibhabib)  **Date**: 2026-02-22  **Language**: en

> 一个使用 Nano Banana Pro 生成现代 3D 动画运动鞋广告的提示。它详细描述了构图、风格、灯光和运动元素，以实现视觉上吸引人的产品可视化。

![3D 动画运动鞋广告提示](https://cms-assets.youmind.com/media/1771828715319_rms12u_HBwI0_6aMAAfgjS.jpg)
![3D 动画运动鞋广告提示](https://cms-assets.youmind.com/media/1771828715403_011d6u_HBwI09nbMAApXPw.jpg)

```
3D animated style sneaker advertisement featuring two elegant sneaker pairs displayed outside their premium shoe boxes. One pair in bold red and white, and the second in stylish black, red, and green. Shoe boxes positioned behind with the brand name SHOECAN SNIKERS in bold capital letters.
Sneakers appear in smooth 3D render style with glossy highlights, soft reflections, and floating presentation. Subtle motion elements like floating particles and light streaks enhance visual appeal. Clean studio background, cinematic lighting, ultra-modern animated product visualization, elegant and attractive composition.
```

[[Studio Lighting]] [[Nano Banana Pro]] [[Product Visualization]]

---

### 90. 描金黑陶瓷盘

**Author**: [Lovart 公式 (ラブアート)](https://x.com/lovart_jp)  **Date**: 2026-02-22  **Language**: ja

> 一个提示，用于生成一张黑色陶瓷盘子的图像，该盘子采用金缮（Kintsugi）技术修复，盘上饰有金色枝叶图案，以高写实、高分辨率的数字艺术风格呈现，并带有影棚布光效果。

![描金黑陶瓷盘](https://cms-assets.youmind.com/media/1771828729931_wroifk_HBHEBxCbwAA8c09.jpg)
![描金黑陶瓷盘](https://cms-assets.youmind.com/media/1771828730228_6lgwk6_HBHEBTla8AA80bx.jpg)

```
金継ぎ（kintsugi）された黒い陶磁器の丸皿、暗い背景（dark background）、マットな黒のセラミック質感、金の光沢のあるひび割れ、金色の枝と葉の装飾が施されたデザイン、深いグラデーションの暗い背景、スタジオライティング、柔らかな影、写実的なレンダリング、高解像度、8K、日本の伝統工芸美、侘寂の美学、高品質なデジタルアート
```

[[Studio Lighting]] [[Product Photography]] [[Digital Art]]

---

### 91. 奢华止汗剂产品图

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-22  **Language**: en

> 一个全面的产品摄影提示，旨在生成一张名为“VELORÉ Pure Aura”的奢华身体除臭剂的超电影感广告图片。该提示详细描述了产品的设计、材料、构图、环境（水疗雾气、大理石）、灯光（柔和工作室光、金色光晕）和相机设置（微距、浅景深）。

![奢华止汗剂产品图](https://cms-assets.youmind.com/media/1771828722103_st80wy_HBuida2bgAEeGKd.jpg)
![奢华止汗剂产品图](https://cms-assets.youmind.com/media/1771828722266_rmr9h3_HBuidaybcAAk9k7.jpg)

```
{
  "master_prompt": {
    "product": {
      "type": "luxury body deodorant",
      "brand_name": "VELORÉ",
      "product_line": "Pure Aura",
      "container_style": "sleek cylindrical deodorant stick with softly rounded edges",
      "material": "frosted glass body with brushed champagne-gold metal accents",
      "finish": "velvety matte surface with refined metallic detailing",
      "cap_design": "magnetic cap with polished gold rim and engraved crest",
      "branding": "minimal serif logo etched vertically with understated elegance",
      "dispense_style": "precision twist-up deodorant balm with smooth surface finish",
      "color": "warm ivory body with subtle golden undertones",
      "accent_details": "champagne gold band and minimal crest emblem",
      "texture_details": "soft satin deodorant balm surface visible at top"
    },

    "composition": {
      "scene_type": "ultra-cinematic luxury personal care advertising photography",
      "orientation": "vertical",
      "aspect_ratio": "4:5",
      "camera_angle": "low hero angle emphasizing elegance and premium form",
      "subject_position": "deodorant standing upright on reflective surface",
      "motion": "fine mist spray particles suspended mid-air for freshness effect"
    },

    "environment": {
      "background": "soft warm marble gradient fading into shadow",
      "atmosphere": "light spa mist creating a serene premium ambiance",
      "floating_elements": [
        "delicate mist particles suspended in air",
        "white orchid petals drifting gently",
        "tiny golden light particles shimmering softly",
        "fresh eucalyptus leaves floating nearby",
        "soft vapor trails suggesting freshness"
      ],
      "surface_effects": "glossy reflections with micro condensation droplets enhancing freshness"
    },

    "lighting": {
      "style": "soft spa-inspired studio lighting",
      "key_light": "diffused overhead light revealing frosted texture",
      "rim_lights": "subtle warm highlights outlining silhouette",
      "accent_lights": "soft golden glow enhancing luxury appeal",
      "shadow_depth": "gentle shadows for calm elegance",
      "contrast": "balanced contrast with luminous clean highlights"
    },

    "color_palette": {
      "primary_colors": ["warm ivory", "soft cream", "clean white"],
      "accent_colors": ["champagne gold", "botanical green"]
    },

    "camera_settings": {
      "lens": "macro cinema lens",
      "depth_of_field": "shallow depth isolating product",
      "focus_point": "engraved logo and frosted glass texture",
      "bokeh": "soft luminous bokeh from mist particles",
      "detail_capture": "extreme micro-detail clarity"
    },

    "render_quality": {
      "resolution": "8K ultra high definition",
      "render_style": "hyper-realistic luxury personal care commercial render",
      "material_physics": "accurate frosted glass translucency and metallic reflecti"
    }
  }
}
```

[[Studio Lighting]] [[Macro Photography]]

---

### 92. 身着高级定制礼服的 Billie Eilish 超高清肖像

**Author**: [Riya_Cute 🇺🇸](https://x.com/Riya333S)  **Date**: 2026-02-20  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张 8K 超高清、超写实、特写镜头下的 Billie Eilish 编辑肖像，强调其特定的面部几何结构、高光泽度的头发，以及前卫蕾丝晚礼服的精致细节，置于空灵的影棚灯光下。

![身着高级定制礼服的 Billie Eilish 超高清肖像](https://cms-assets.youmind.com/media/1771655061026_jww7ky_HBoytWYbsAACPuG.jpg)
![身着高级定制礼服的 Billie Eilish 超高清肖像](https://cms-assets.youmind.com/media/1771655061072_slot3i_HBoytetbgAAZgex.jpg)
![身着高级定制礼服的 Billie Eilish 超高清肖像](https://cms-assets.youmind.com/media/1771655061075_g5ip4c_HBoytblbQAA_uhp.jpg)

```
{
  "prompt_configuration": {
    "type": "Hierarchical Descriptive Prompt",
    "output_format": "Ultra-High-Definition Photography",
    "aspect_ratio": "9:16"
  },
  "compositional_framework": {
    "camera_profile": {
      "lens_shot": "85mm prime lens, tight close-up",
      "angle": "45-degree lateral head tilt",
      "depth_of_field": "Shallow (f/1.8), creamy bokeh background",
      "focus_point": "Sharp focus on the iris and eyelashes"
    },
    "lighting_and_atmosphere": {
      "primary_source": "Soft-box studio lighting, 3-point setup",
      "secondary_source": "Warm rim lighting highlighting hair texture",
      "mood": "Ethereal, dreamy, high-fashion aesthetic",
      "color_palette": "Muted pastels, cream, and natural skin tones"
    }
  },
  "subject_profile": {
    "identity": "{argument name="celebrity name" default="Billie Eilish"}",
    "facial_geometry": {
      "expression": "Serene, dreamy gaze, soft parted lips",
      "skin_render": "Hyper-realistic texture, visible pores, natural freckles, matte finish",
      "makeup": {
        "lips": "High-shine pink-nude glossy lipstick with subtle liner",
        "eyes": "Meticulously separated long lashes, subtle earth-tone eyeshadow"
      }
    },
    "hair_physics": {
      "style": "Soft, elegant messy aesthetic, flowing with movement",
      "strands": "Individual wispy strands catching the light, overlapping the face",
      "color": "Signature tone with high-gloss straight highlights",
      "dynamics": "Windswept effect, creating a sense of motion"
    }
  },
  "wardrobe_specifications": {
    "garment": "Avant-garde body-hugging evening gown",
    "textile_detail": "Intricate off-white lace, floral embroidery patterns",
    "cut": "Dramatic deep V-neckline",
    "fit": "Tailored, form-fitting silhouette across the shoulders"
  },
  "technical_fidelity": {
    "resolution": "8k UHD",
    "post_processing": "Professional color grading, film grain (subtle), ray-tracing",
    "quality_tags": [
      "Masterpiece",
      "Photorealistic",
      "Vogue editorial style",
      "Intricate details"
    ]
  }
}
```

[[Studio Lighting]] [[8K Photography]]

---

### 93. 粉色糖霜制成的异想天开的霸王龙

**Author**: [Heather Green](https://x.com/heathergreen)  **Date**: 2026-02-20  **Language**: en

> 一个提示，用于生成一张高度细致、充满奇思妙想的霸王龙肖像，这只霸王龙完全由亮粉色糖霜塑形而成，以倒置的冰淇淋甜筒作为鳞片，并点缀着糖果装饰，背景是一个柔和的马卡龙色调面包店，配有影棚灯光。

![粉色糖霜制成的异想天开的霸王龙](https://cms-assets.youmind.com/media/1771655056271_4xeo0d_HBn18_4XAAAey5M.jpg)

```
highly detailed whimsical portrait of a t-rex made entirely out of glossy pink frosting, with a playful, sculpted cake-like texture, each curve and wrinkle piped with intricate icing details, a line of upside down ice cream cones along its back to represent scales or spikes, the waffle cone texture clearly visible, pastel sprinkles and candy decorations accenting the cones, set against a soft pastel bakery-style background, studio lighting with subtle reflections on the frosting, shallow depth of field, vibrant yet cute and charming aesthetic
```

[[Studio Lighting]] [[Pastel Color Palette]]

---

### 94. 超现实超市包装产品拍摄提示

**Author**: [ibexdream](https://x.com/ibexdream)  **Date**: 2026-02-18  **Language**: en

> 一个旨在将任何主体（物体、人物或角色）用保鲜膜包裹在泡沫托盘中的提示，模仿超现实的超市产品照片。它指定了逼真的细节，如保鲜膜褶皱、眩光和影棚灯光。

![超现实超市包装产品拍摄提示](https://cms-assets.youmind.com/media/1771483124612_0m8jj7_HBdR_s8XIAAf1D2.jpg)

```
Turn any subject into a surreal "supermarket package" product shot.

I made a NanoBanana Pro prompt that wraps anything (objects, people, characters) in cling film inside a foam tray, complete with real wrinkles, glare, and studio lighting.
```

[[Studio Lighting]]

---

### 95. 蓝宝石水晶打造的影院级美学镜头

**Author**: [Raakifa](https://x.com/Raakif2446)  **Date**: 2026-02-17  **Language**: en

> 一个详细的提示，用于生成一张超高清电影级美女特写照片，模特皮肤白皙，眼睛和太阳穴周围点缀着微小的蓝宝石蓝色水晶，嘴唇是亮泽的深海军蓝色，佩戴羽毛领饰，强调极致特写和聚焦的影棚灯光。

![蓝宝石水晶打造的影院级美学镜头](https://cms-assets.youmind.com/media/1771396579134_0y32ge_HBX6tUXbcAY3PSq.jpg)

```
Photorealistic cinematic 9:16 vertical 8K ultra high definition extreme close-up beauty shot with an ARRI Alexa 65 with anamorphic lenses. [my face reference] as a model, face angled to the camera. Her skin is pale and perfect. She is adorned with tiny sapphire blue crystals scattered around her eyes and temples, like crystallized tears. She has glossy, deep navy blue lips. She wears a high-necked, feathered collar in peacock blue that frames her jaw. The lighting is a soft, focused studio-style beauty light, isolating her from the blurred, bright white background.
```

[[Studio Lighting]] [[High Fashion Editorial]] [[Extreme Close-Up]]

---

### 96. 复古未来主义产品摄影提示

**Author**: [Shams](https://x.com/ShamsAmin56)  **Date**: 2026-02-13  **Language**: en

> 一个用于生成高度详细的复古未来主义物体的提示模板，强调 20 世纪 50 年代至 60 年代太空时代的設計、特定材料（镀铬、柔和色调）以及带有柔和影棚照明的专业产品摄影设置。

![复古未来主义产品摄影提示](https://cms-assets.youmind.com/media/1771050434122_mievnx_HBB3TJ8WAAArAhz.jpg)

```
Highly detailed retro-futurism {argument name="object name" default="[OBJECT NAME]"}, inspired by 1950s–1960s space-age design, aerodynamic silhouette, polished chrome elements, bold geometric accents, pastel tones, analog gauges and mechanical detailing, light surface aging for authenticity, positioned on an old wooden block with textured wood grain, isolated against a plain light {argument name="background color" default="[BACKGROUND COLOR]"} background, soft natural studio lighting, gentle shadows, shallow depth of field, professional product photography, ultra-realistic, 4k detail.
```

[[Studio Lighting]] [[Product Photography]] [[Pastel Color Palette]]

---

### 97. 电影级美食汉堡爆炸提示词（代码风格）

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-13  **Language**: en

> 一个高度结构化、类似代码的提示，使用 Python 语法（导入物理和照明模块）来生成一张美食汉堡慢动作爆炸的电影级广告图片，详细描述了食材、质地和影棚布光设置。

![电影级美食汉堡爆炸提示词（代码风格）](https://cms-assets.youmind.com/media/1771050461758_fxcwxn_HBAYMJybsAEscTG.jpg)
![电影级美食汉堡爆炸提示词（代码风格）](https://cms-assets.youmind.com/media/1771050461797_riopi6_HBAYMIDbsAEnmLk.jpg)

```
import physics_engine as cinematic
from studio_lighting import RimLight, SpotLight

class GourmetBurger:
    def __init__(self):
        self.state = "assembled"
        self.ingredients = [
            "toasted_brioche_bun", 
            "wagyu_patty", 
            "molten_cheddar", 
            "crispy_lettuce", 
            "heirloom_tomato",
            "secret_sauce_droplets"
        ]

    def trigger_explosion(self):
        """
        Executes the slow-motion deconstruction effect.
        """
        self.state = "mid-air_burst"
        
        for item in self.ingredients:
            # Applying physics for the "flying" effect
            item.apply_force(direction="outward", velocity="slow_motion")
            item.render_texture(quality="hyper_detailed")
            
        # Suspends liquid particles in 3D space
        cinematic.suspend_fluids(type="sauce", density="high_viscosity")

# Environment Configuration
scene = cinematic.Scene(background="dark_studio_charcoal")
scene.add_lighting([
    RimLight(intensity=0.8, color="warm_gold"),
    SpotLight(target="patty_texture", focus="ultra_sharp")
])

# Execute the render
burger = GourmetBurger()
burger.trigger_explosion()

render_output = scene.capture(style="cinematic_advertising", realistic=True)
```

[[Studio Lighting]] [[Food Photography]] [[Commercial Food Ad]]

---

### 98. 巨型爱心上的情侣 3D 渲染图

**Author**: [Aijaz](https://x.com/iamsofiaijaz)  **Date**: 2026-02-13  **Language**: en

> 一个用于生成高质量 3D 渲染的提示：一对可爱、快乐的情侣坐在一个巨大的光泽红色爱心上，身着时尚休闲服，采用柔和的摄影棚灯光和等距视角。

![巨型爱心上的情侣 3D 渲染图](https://cms-assets.youmind.com/media/1771050450240_r8k44z_HA-nb72bUAA3Fqg.jpg)

```
Make a High-quality 3D render of a cute happy Couple sitting on a giant glossy red heart. The character is wearing stylish casual clothes, male holds rose in one hand while female holding a red gift box. Soft studio lighting, pastel pink background, isometric view with 8k resolution.
```

[[Studio Lighting]] [[3D Rendering]] [[Isometric View]] [[Valentine Theme]]

---

### 99. 超逼真时尚大片，搭配吸烟道具

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-02-12  **Language**: en

> 一个高度详细的提示，用于创作超现实主义时尚编辑肖像，其中指定了相机设置（85mm f/1.8）、灯光（柔和的电影级影棚灯）、服装（象牙米色露背上衣和飘逸长裙），并包含一支点燃的香烟作为道具，以营造自信优雅的氛围。

![超逼真时尚大片，搭配吸烟道具](https://cms-assets.youmind.com/media/1770964562744_lyi62e_HA-DVhZbMAAJM98.jpg)
![超逼真时尚大片，搭配吸烟道具](https://cms-assets.youmind.com/media/1770964562754_9e1kf5_HA-DVhZbsAICTcM.jpg)
![超逼真时尚大片，搭配吸烟道具](https://cms-assets.youmind.com/media/1770964562834_d3dtne_HA-DV5vbsAYU7Qw.jpg)

```
{
  "meta": {
    "style": "ultra-realistic fashion editorial photography",
    "quality": "8k high resolution",
    "camera": "Full-frame DSLR",
    "lens": "85mm f/1.8 portrait lens",
    "aperture": "f/2.0",
    "lighting": "soft cinematic studio lighting with warm tones",
    "color_grading": "neutral beige and warm ivory palette",
    "aspect_ratio": "4:5 vertical",
    "mood": "confident, elegant, subtly sensual"
  },

  "subject": {
    "gender": "female",
    "age_range": "mid 20s",
    "skin_tone": "warm medium complexion with smooth luminous finish",
    "body_type": "slim, natural proportions",
    "pose": "seated on the floor with one knee raised toward the camera, the other leg folded beneath, torso slightly angled forward",
    "expression": "calm, confident gaze directly into camera, soft neutral lips, relaxed eyes",
    "hair": {
      "color": "dark brown",
      "style": "long, voluminous, soft waves cascading over shoulders",
      "texture": "smooth with natural shine"
    },
    "makeup": {
      "style": "natural glam",
      "foundation": "flawless matte-satin finish",
      "eyes": "soft brown smoky eyeshadow, defined lashes, subtle eyeliner",
      "brows": "well-shaped and natural",
      "lips": "muted nude lipstick with soft satin texture",
      "highlight": "subtle cheekbone glow"
    }
  },

  "wardrobe": {
    "top": {
      "type": "halter-style wrap crop top",
      "color": "ivory beige",
      "fabric": "soft stretch fabric with smooth texture",
      "fit": "fitted, elegant drape across bust"
    },
    "bottom": {
      "type": "flowing high-waisted skirt",
      "color": "matching ivory beige",
      "fabric": "light chiffon with soft translucent layers",
      "movement": "natural folds and soft draping around legs"
    },
    "accessories": {
      "bracelets": "multiple thin gold bangles on wrist",
      "earrings": "small subtle gold studs"
    }
  },

  "props": {
    "object": "lit cigarette held between fingers",
    "smoke": "thin delicate smoke trail rising naturally",
    "position": "hand raised near face in relaxed gesture"
  },

  "environment": {
    "location": "minimalist indoor studio setting",
    "background": "soft beige wall panels with subtle texture",
    "floor": "smooth neutral-toned floor",
    "depth_of_field": "shallow depth with softly blurred background"
  },

  "lighting_details": {
    "key_light": "soft diffused light from front-left",
    "fill_light": "subtle fill to reduce harsh shadows",
    "rim_light": "gentle back rim light highlighting hair edges",
    "shadow_style": "soft natural shadows for dimensionality"
  },

  "composition": {
    "framing": "medium full-body portrait",
    "focus": "sharp focus on eyes and face",
    "foreground": "raised knee slightly closer to lens for depth",
    "balance": "subject centered with slight asymmetrical pose",
    "aesthetic": "luxury fashion magazine editorial"
  },
```

[[Studio Lighting]] [[Fashion Editorial]] [[85mm Lens]]

---

### 100. 蓝莓薄荷冰饮的优质影棚照片

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-02-12  **Language**: en

> 一个高度结构化的提示，用于生成一张超逼真的蓝莓薄荷冰饮商业产品照片。它详细描述了玻璃杯、液体渐变、冰块、装饰物和环境元素（深色反光表面、海军蓝背景）。灯光被指定为专业的影棚设置，带有柔和漫射的主光和冷色轮廓光，以营造一种情绪化、电影感、高对比度的广告风格。

![蓝莓薄荷冰饮的优质影棚照片](https://cms-assets.youmind.com/media/1770964567216_nl1oqo_HA7guOTbMAAU4PR.jpg)
![蓝莓薄荷冰饮的优质影棚照片](https://cms-assets.youmind.com/media/1770964567300_zoetcw_HA7guP6a4AAXC4I.jpg)
![蓝莓薄荷冰饮的优质影棚照片](https://cms-assets.youmind.com/media/1770964567353_wwbx4n_HA7guM9bwAAdh8D.jpg)
![蓝莓薄荷冰饮的优质影棚照片](https://cms-assets.youmind.com/media/1770964568000_qdmw4w_HA7guO7bsAIsP2A.jpg)

```
{
  "meta": {
    "title": "Blueberry Mint Iced Drink – Premium Studio Shot",
    "version": "1.0",
    "type": "text-to-image",
    "style": "Ultra-realistic beverage photography"
  },
  "scene": {
    "subject": "Tall clear highball glass filled with blue blueberry mint soda",
    "glass": "Transparent faceted glass with condensation droplets",
    "liquid": "Vibrant gradient blue drink (deep blue at bottom fading to clear at top)",
    "ice": "Large crystal-clear ice cubes filling the glass",
    "garnish": [
      "Fresh mint leaves inside and on top",
      "Whole blueberries inside the drink",
      "Blueberries resting around the base",
      "Light wooden straw angled inside the glass"
    ],
    "effects": [
      "Soft misty vapor rising from the top",
      "Tiny bubbles in liquid",
      "Water droplets on glass surface",
      "Slight splash texture at bottom surface"
    ]
  },
  "environment": {
    "background": "Dark navy to black gradient backdrop",
    "surface": "Glossy black reflective surface with scattered blueberries and mint leaves",
    "atmosphere": "Moody, cinematic, high contrast"
  },
  "lighting": {
    "type": "Professional studio lighting",
    "setup": [
      "Soft diffused key light from left",
      "Cool rim light from right to enhance glass edges",
      "Subtle backlight for vapor visibility"
    ],
    "highlights": "Sharp reflections on ice and glass",
    "shadows": "Deep, dramatic shadows"
  },
  "camera": {
    "angle": "Eye-level close-up",
    "lens": "85mm macro lens",
    "aperture": "f/2.8",
    "depth_of_field": "Shallow depth of field, blurred background berries",
    "resolution": "8K ultra-detailed",
    "focus": "Sharp focus on glass center and mint leaves"
  },
  "quality_tags": [
    "hyper-realistic",
    "photorealistic",
    "commercial beverage photography",
    "crisp details",
    "cinematic",
    "high dynamic range",
    "editorial drink advertisement style"
  ]
}
```

[[Studio Lighting]] [[Beverage Product Photography]]

---

### 101. 高端冰沙广告生成（代码风格）

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-12  **Language**: en

> 一个以 Python 类结构编写的提示，定义了用于生成超逼真、电影级 8K 冰沙爆炸广告图像的参数，该图像定格在半空中，突出显示特定的水果元素和液体动态。

```
class PremiumSmoothieAd:
    def __init__(self):
        self.composition = {
            "action": "ultra_realistic_explosion",
            "state": "frozen_mid_air",
            "elements": [
                "banana_slices",
                "strawberry_pieces",
                "blueberry_splash",
                "chia_seeds"
            ],
            "motion": "liquid_swirl"
        }
        
        https://t.co/Oq1q7_settings = {
            "focus": "shallow_depth_of_field",
            "clarity": "ultra_sharp",
            "resolution": "8K_cinematic"
        }
        
        https://t.co/ci6mMG4fGy_vibe = {
            "style": "bright_studio",
            "texture": "glossy_liquid",
            "aesthetic": "premium_health_drink"
        }

    def render(self):
        # Parameters for the generation engine
        return {
            "aspect_ratio": "2:3",
            "version": 6.0,
            "style": "raw"
        }
```

[[Studio Lighting]] [[8K Food Photography]]

---

### 102. 手持自己海报的编辑肖像

**Author**: [Smiling Khan](https://x.com/AIwithkhan)  **Date**: 2026-02-11  **Language**: en

> 一个用于生成高端影棚肖像的提示，其中主体（基于上传的照片）手持一张大型海报，海报上是他们自己面部的艺术化再诠释，强调专业的灯光、简洁的构图和现代的个人品牌形象。

![手持自己海报的编辑肖像](https://cms-assets.youmind.com/media/1770878358866_mld9f8_HA2p-iKaAAEPUW3.jpg)

```
high-end studio portrait using the uploaded photo as the main subject. The person stands smiling against a clean, minimal background in soft neutral tones, holding a large vertical poster in front of them. The poster features an artistic reinterpretation of the same uploaded photo — stylized as a digital illustration, sketch, or painterly artwork — clearly recognizable as the same face. Professional studio lighting with a soft key light and subtle rim light creates gentle shadows and depth. The subject’s expression is calm and confident, body posture relaxed yet strong, evoking a modern personal brand identity. Clean composition, balanced framing, premium editorial aesthetic, shallow depth of field, ultra-realistic skin texture, crisp details, contemporary creator branding vibe, cinematic realism, 1:1 aspect ratio, high resolution.”
```

[[Studio Lighting]] [[Personal Branding]] [[Clean Composition]]

---

### 103. 菠萝和酸奶流体的高速微距摄影

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-02-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一张高速微距照片，内容为一块菠萝块悬浮在半空中，被一股柔和的淡菠萝酸奶轻轻包裹。它强调受控的液体流动、超逼真的水果质感和干净的影棚布光，以呈现高端商业食品广告风格。

```
{
  "image_type": "photograph",
  "genre": "high-speed macro food photography",
  "subject": {
    "main_object": "fresh pineapple chunk",
    "state": "suspended mid-air",
    "interaction": "softly wrapped by a gentle flow of pale pineapple yogurt"
  },
  "composition": {
    "framing": "tight macro close-up",
    "orientation": "vertical",
    "subject_position": "centered",
    "isolation": "isolated object, clean cutout"
  },
  "motion": {
    "liquid_behavior": "smooth, restrained liquid motion",
    "splash_intensity": "minimal splash",
    "droplets": "very few small droplets",
    "fluid_dynamics": "calm and controlled"
  },
  "texture_and_detail": {
    "yogurt_texture": "thick, creamy, silky",
    "fruit_texture": "ultra-realistic pineapple flesh with visible fibers",
    "surface_detail": "high micro-detail, natural moisture"
  },
  "lighting": {
    "style": "professional studio lighting",
    "highlights": "soft diffuse highlights",
    "shadows": "gentle, natural falloff",
    "exposure": "balanced, high dynamic range"
  },
  "background": {
    "color": "pure white",
    "style": "seamless studio backdrop"
  },
  "quality": {
    "realism": "photorealistic",
    "resolution": "ultra-high resolution",
    "sharpness": "crisp focus on subject"
  },
  "constraints": [
    "no CGI",
    "no 3D render",
    "no illustration",
    "no artificial look"
  ],
  "aesthetic": "clean, premium, commercial food advertising style"
}
```

[[Studio Lighting]] [[Macro Photography]] [[Commercial Food Photography]] [[High Speed Photography]]

---

### 104. 橙红色背景的动态低角度肖像

**Author**: [Sadia](https://x.com/SadiaMalik182)  **Date**: 2026-02-09  **Language**: en

> 生成一张男士肖像的提示词，要求图像具有强大的视觉冲击力、照片级真实感，采用戏剧性、高对比度的影棚布光，以橙色和深红色调为主，背景为纯色鲜艳背景，以突出其强大、权威的气场。

![橙红色背景的动态低角度肖像](https://cms-assets.youmind.com/media/1770706206272_1ddwwq_HArYurTW4AAStfu.jpg)
![橙红色背景的动态低角度肖像](https://cms-assets.youmind.com/media/1770706206265_363dk1_HArYuynXMAA42wH.jpg)
![橙红色背景的动态低角度肖像](https://cms-assets.youmind.com/media/1770706206654_aniz5m_HArYu5hbkAAoJJ1.jpg)
![橙红色背景的动态低角度肖像](https://cms-assets.youmind.com/media/1770706207535_gh6c6h_HArYu6eWUAEAVf9.jpg)

```
A powerful editorial, highly detailed, photorealistic, dynamic low-angle portrait featuring a man against a vibrant, solid {argument name="background color" default="orange-red"} background, utilizing dramatic, high-contrast studio lighting dominated by vivid orange and deep red hues. The subject is photographed from a slightly low camera angle, creating a strong, authoritative presence and emphasizing the jawline and facial structure. His head is subtly tilted downward toward the camera while his eyes look slightly
```

[[Studio Lighting]] [[Male Portrait]] [[High Contrast]]

---

### 105. 超逼真 3D 排版雕塑产品概念

**Author**: [ΛRMIN | AI](https://x.com/Arminn_Ai)  **Date**: 2026-02-08  **Language**: en

> 一个详细的提示模板，用于生成一个超逼真的 3D 字体雕塑产品概念。该雕塑完全由与主题性质相关的密集、相互交织的 3D 单词和形容词构成，采用高端商业广告摄影风格设计，并辅以富有戏剧性的影棚布光。

![超逼真 3D 排版雕塑产品概念](https://cms-assets.youmind.com/media/1770619683003_ofyg8y_HAqI5ijbUAAhzv0.jpg)

```
A hyper-realistic 3D typographic sculpture of a {argument name="Subject Name" default="[Subject Name]"}. The entire structure is built exclusively from dense, interlocking 3D words and adjectives related to its nature, with no solid base underneath.

[PART 1]: The {argument name="Part 1 Name" default="e.g., Main Body"} is constructed from 3D letters forming the words '{argument name="Word 1" default="Word 1"}' and '{argument name="Word 2" default="Word 2"}' with a [Texture] texture in [Color] color. [PART 2]: The [e.g., Secondary Part] is made of 3D letters forming the words '[Word A]' and '[Word B]' with a [Texture] texture in [Color] color. [ADDITIONAL COMPONENTS]: (Continue adding as many parts as needed following the same format: "The [Part Name] is made of 3D letters forming the word [word] with a [Texture] texture in [Color] color.")

High-end commercial advertising photography style, clean minimalist cream-colored background, soft studio lighting, long dramatic shadows on the floor. The words are tightly packed to perfectly mimic the [Organic / Mechanical / Sleek] silhouette of the [Subject].
```

[[Studio Lighting]]

---

### 106. 商用食品摄影模块（华夫饼、饼干、冰淇淋棒）

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-02-08  **Language**: en

> 一个复杂的多模块提示，旨在生成超高细节、超逼真的商业食品摄影。它指定了三种不同的食物主体（华夫碗、巧克力饼干棒、冰淇淋棒），具有动态运动效果（溅起的水花、漂浮的食材）、高对比度影棚照明和奢华的调色板。

![商用食品摄影模块（华夫饼、饼干、冰淇淋棒）](https://cms-assets.youmind.com/media/1770619678370_chtq5s_HApIOh0aMAA5yUU.jpg)
![商用食品摄影模块（华夫饼、饼干、冰淇淋棒）](https://cms-assets.youmind.com/media/1770619678124_h82j5m_HApIOg1bMAA_ERd.jpg)
![商用食品摄影模块（华夫饼、饼干、冰淇淋棒）](https://cms-assets.youmind.com/media/1770619678110_tztyir_HApIOiraEAEX9DU.jpg)
![商用食品摄影模块（华夫饼、饼干、冰淇淋棒）](https://cms-assets.youmind.com/media/1770619679312_k0sf65_HApIOh_bIAA0vFZ.jpg)

```
{
  "master_prompt": {
    "global_settings": {
      "resolution": "8K UHD",
      "aspect_ratio": "3:4 vertical",
      "image_quality": "ultra high detail, hyper-realistic, next-gen AI commercial food photography",
      "focus": "razor-sharp subject focus with cinematic depth separation",
      "lighting": "high-contrast studio lighting with soft glow accents and rim highlights",
      "background_style": "luxury gradient backdrop with floating particles and liquid droplets",
      "color_palette": "honey gold, cocoa brown, vanilla cream",
      "motion": "ingredients and liquids frozen mid-splash in dynamic motion"
    },

    "Module_1_Image_1_Style": {
      "subject": "golden waffle bowls filled with vanilla-caramel ice cream",
      "composition": "two waffle bowls floating diagonally, slightly offset for depth",
      "waffle_bowls": {
        "material": "crispy baked waffle",
        "texture": "deep honeycomb grid with toasted edges",
        "color": "warm golden brown with subtle gloss"
      },
      "filling": {
        "type": "vanilla-caramel ice cream",
        "appearance": "creamy, smooth swirls with soft melting edges",
        "color": "light caramel cream with golden highlights"
      },
      "liquid_effects": {
        "caramel_ribbons": "thick caramel streams wrapping around bowls",
        "droplets": "suspended glossy caramel droplets"
      },
      "background": {
        "color": "radiant amber gradient",
        "effects": "bokeh glow, soft spark particles"
      },
      "mood": "warm, indulgent, premium frozen dessert advertisement"
    },

    "Module_2_Image_2_Style": {
      "subject": "chocolate-dipped biscuit sticks with hazelnut crunch",
      "composition": "multiple sticks crossing in mid-air with layered depth",
      "biscuit_sticks": {
        "base": "crunchy biscuit core",
        "coating": "thick milk chocolate shell with crushed nut texture",
        "detail": "visible bite marks revealing biscuit interior"
      },
      "additional_elements": {
        "chocolate_chunks": "floating chocolate shards with embossed branding",
        "nuts": "whole and crushed hazelnuts scattered in motion",
        "chocolate_flow": "liquid chocolate waves trailing behind sticks"
      },
      "background": {
        "color": "deep cocoa brown gradient",
        "effects": "soft blur, floating dust particles"
      },
      "lighting": {
        "style": "directional warm lighting",
        "highlights": "specular reflections on chocolate coating"
      },
      "mood": "bold, crunchy, chocolate-forward commercial look"
    },

    "Module_3_Image_3_Style": {
      "subject": "cookie-crumble ice cream bar with caramel core",
      "composition": "single ice cream bar tilted diagonally, centered in frame",
      "dessert_body": {
        "coating": "vanilla ice cream embedded with dark cookie crumble",
        "texture": "contrast between smooth cream and rough cookie"
```

[[Studio Lighting]]

---

### 107. 超高端抽象构图

**Author**: [SRKDAN](https://x.com/SRKDAN)  **Date**: 2026-02-07  **Language**: en

> 一个为 Nano Banana Pro 设计的简洁提示，旨在通过生成一个抽象构图来压力测试视觉质量。该构图包含大型、流畅的雕塑形式，具有逼真的材质着色、柔和的摄影棚灯光和中性画廊风格的调色板，强调完美的平衡和细节。

![超高端抽象构图](https://cms-assets.youmind.com/media/1770532811154_ey8a1r_HAjtFCKWgAAWy3f.jpg)

```
Ultra-high-end abstract composition. Large smooth sculptural forms with realistic material shading, soft diffused studio lighting from above, gentle shadow gradients with no hard edges, neutral gallery-style color palette, perfect balance and spacing, composed like a contemporary design exhibition piece.
```

[[Studio Lighting]] [[Neutral Color Palette]]

---

### 108. 未来感蓬松玻璃字体艺术

**Author**: [Manish Bhati](https://x.com/mahivisuals)  **Date**: 2026-02-06  **Language**: en

> 一个详细的 JSON 提示，用于生成高端 3D 字体艺术。它着重于使用磨砂玻璃和毛绒纤维的独特组合来渲染文本“Future AI”，并将其置于未来主义渐变背景和柔和的摄影棚灯光下，具有高 3D 深度。

![未来感蓬松玻璃字体艺术](https://cms-assets.youmind.com/media/1770446058022_w9coqw_HAfEasPaYAAVBd7.jpg)

```
{
  "model": "Nano Banana Pro ",
  "aspect_ratio": "16:9",
  "style": "futuristic fluffy glass typography",
  "prompt": {
    "subject": "Futuristic AI name art",
    "text": "{argument name="text to render" default="Future AI"}",
    "text_position": "center",
    "text_design": {
      "font_style": "stylish futuristic custom typography",
      "texture": "soft fluffy fibers blended with transparent glass effect",
      "material": "frosted glass + plush fluffy surface",
      "shape": "bold, smooth, slightly curved futuristic letters",
      "depth": "high 3D depth with glass-like thickness",
      "edges": "rounded glass edges with soft fluffy diffusion",
      "finish": "premium, glossy, futuristic aesthetic"
    },
    "color_palette": {
      "text_colors": [
        "cyan",
        "electric purple",
        "neon pink",
        "aqua blue"
      ],
      "gradient": "multi-color futuristic gradient flowing through glass text"
    },
    "lighting": {
      "type": "soft futuristic studio lighting",
      "highlights": "glass reflections with subtle glow",
      "shadows": "soft ambient shadow beneath text"
    },
    "background": {
      "type": "plain attractive futuristic canvas",
      "color": "smooth gradient background ({argument name="background color" default="deep blue to purple"})",
      "texture": "clean matte with soft light falloff",
      "match_with_text": "harmonized futuristic color tones"
    },
    "composition": {
      "focus": "hero glass-fluffy name typography",
      "style": "clean, modern, high-end",
      "balance": "perfectly centered"
    },
    "quality": {
      "resolution": "ultra HD",
      "detail": "high-detail glass refraction and fluffy fibers",
      "sharpness": "crisp edges with soft diffusion"
    }
  },
  "negative_prompt": [
    "simple flat font",
    "opaque solid text",
    "rough glass",
    "dirty texture",
    "busy background",
    "extra objects",
    "logo",
    "watermark",
    "grain",
    "blur"
  ]
}
```

[[Studio Lighting]] [[Gradient Background]]

---

### 109. 超写实韩式美妆编辑拼贴画

**Author**: [PixPretty](https://x.com/PixPrettyAI)  **Date**: 2026-02-05  **Language**: en

> 一个复杂、结构化的提示，旨在创作一个四格、超高质量、超现实的美容专题拼贴画，风格为韩国美容广告。它指定了对角线网格布局、详细的妆容（玻璃肌、宿醉腮红、抖音睫毛），以及四个特写镜头，分别侧重于妆容的不同方面，强调清晰的焦点和柔和的影棚灯光。

![超写实韩式美妆编辑拼贴画](https://cms-assets.youmind.com/media/1770359914552_f126up_HAYg3mAWoAA-NPD.jpg)

```
{
  "collage": {
    "style": {
      "type": "ultra high-quality hyper-realistic beauty editorial collage",
      "layout": "4 photo panels arranged in a tilted diagonal grid layout",
      "grid_details": "clean white borders separating each frame, forming a modern high-end beauty campaign collage. Each frame is slightly rotated at a different angle, creating a dynamic diagonal composition.",
      "resolution": "8K UHD, hyper-realistic, beauty editorial photoshoot, 2:3",
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

[[Studio Lighting]] [[Beauty Editorial]] [[Glass Skin]]

---

### 110. 高分辨率名人肖像分析（Billie Eilish）

**Author**: [Qaiser Tzq](https://x.com/TzqQaiser)  **Date**: 2026-02-05  **Language**: en

> 一个详细的 JSON 提示结构，旨在分析或生成一张高分辨率的名人肖像，其中根据 Billie Eilish 的形象，详细说明了人物的外貌、服装、摄影技术规格和环境。

![高分辨率名人肖像分析（Billie Eilish）](https://cms-assets.youmind.com/media/1770359973723_6zd2eq_HAXlLG9acActsuw.jpg)

```
{
  "document_info": {
    "file_name": "20260205_094141.jpg",
    "detected_celebrity": "{argument name="celebrity name" default="Billie Eilish"}",
    "image_type": "High-resolution celebrity portrait"
  },
  "visual_analysis": {
    "subject_appearance": {
      "hair_style": {
        "color": "Ash Blonde with dark roots",
        "arrangement": "Elegant messy bun (updo)",
        "features": "Wispy curtain bangs and loose strands framing the face"
      },
      "facial_features": {
        "eye_color": "Blue / Grey",
        "expression": "Dreamy and calm",
        "makeup_details": "Minimalist aesthetic, dewy skin finish, soft pink lip gloss, and natural eyebrows"
      },
      "attire": {
        "fabric": "Intricate floral lace",
        "color_palette": "{argument name="attire color" default="Champagne / Ivory"}",
        "design": "Form-fitting dress with a scalloped V-neckline",
        "aesthetic": "Vintage / Romantic"
      }
    },
    "technical_specs": {
      "lighting_type": "Backlit / Golden Hour (warm tones)",
      "depth_of_field": "Shallow (bokeh effect on background)",
      "color_grading": "Warm and soft contrast",
      "orientation": "Vertical (Portrait)"
    },
    "environment": {
      "setting": "Outdoor red carpet or gala event",
      "background_elements": "Blurred silhouettes of trees and people"
    }
  },
  "metadata_tags": [
    "fashion",
    "red carpet",
    "lace dress",
    "blonde hair",
    "portrait photography",
    "celebrity style"
  ]
}
```

[[Studio Lighting]] [[Fashion Photography]] [[High Resolution Portrait]]

---

### 111. 电影脱口秀肖像（艾米莉亚·克拉克 风格）

**Author**: [Aylin](https://x.com/Ai_aylinfc)  **Date**: 2026-02-04  **Language**: en

> 一个高度详细的提示，用于生成一张逼真的电影级脱口秀肖像：一位美丽的演员（灵感来自艾米莉亚·克拉克）坐在吉米·法伦旁边，身穿优雅的蓝色连衣裙，上面有金色星星和城市景观图案，在专业的演播室灯光下，捕捉到她开怀大笑的瞬间。

![电影脱口秀肖像（艾米莉亚·克拉克 风格）](https://cms-assets.youmind.com/media/1770273469023_65vkr4_HAUxUHfbYAAhldQ.jpg)
![电影脱口秀肖像（艾米莉亚·克拉克 风格）](https://cms-assets.youmind.com/media/1770273469025_1mlbpc_HAUxULDaoAACDpO.jpg)

```
A photorealistic, cinematic talk-show portrait of a beautiful actress with rich chestnut-brown hair styled in soft, glossy waves, parted slightly to the side, and a bright, warm, infectious smile that radiates charm and friendliness, {argument name="actress inspiration" default="Emilia Clarke"}–inspired but not depicting a real person. She is seated confidently on The Tonight Show–style set with Jimmy Fallon, sitting behind a sleek wooden talk-show desk with a professional broadcast microphone placed in front of her.
She is wearing a stylish, elegant blue dress: the fitted top features delicate gold star patterns scattered across a deep navy background, while the flowing skirt displays an intricate cityscape illustration in navy, midnight blue, and muted gold tones, bordered with a refined red trim at the hem. She pairs the outfit with gold strappy high-heeled sandals, legs crossed naturally in a relaxed, confident pose.
Her expression is joyful and animated, captured mid-laugh as if reacting to a humorous comment, with expressive eyes, subtle glowing makeup, softly defined brows, natural blush, and glossy lips. Her skin texture is highly realistic, smooth yet natural, with cinematic highlights and shadows.
The background shows a nighttime city skyline through large studio windows, glowing with bokeh lights and neon reflections, instantly recognizable as a late-night talk show atmosphere. Studio lighting is professional and cinematic: soft key light illuminating her face, gentle rim light separating her from the background, and warm ambient tones enhancing the cozy yet glamorous TV-show mood.
Shot with a full-frame camera, 85mm lens, shallow depth of field, ultra-sharp focus on the subject, hyper-realistic detail, high dynamic range, natural color grading, premium editorial photography quality, 8K resolution, modern Hollywood talk-show aesthetic.
```

[[Studio Lighting]] [[Cinematic Realism]]

---

### 112. 超逼真商业产品摄影展示（酸奶与电解质饮料）

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-02-04  **Language**: en

> 这是一个复杂的多模块提示，专为超逼真的商业产品摄影而设计，详细描述了两种不同的产品风格——一瓶带有冷凝水珠的薰衣草酸奶冰沙，以及一罐带有爆炸性飞溅效果的霓虹青色电解质饮料——两者都强调极致的清晰度和电影级的影棚布光。

![超逼真商业产品摄影展示（酸奶与电解质饮料）](https://cms-assets.youmind.com/media/1770273455273_iqonnd_HAUsk-DaEAAUgtz.jpg)
![超逼真商业产品摄影展示（酸奶与电解质饮料）](https://cms-assets.youmind.com/media/1770273455349_ul47x5_HAUslAaakAE-tIN.jpg)
![超逼真商业产品摄影展示（酸奶与电解质饮料）](https://cms-assets.youmind.com/media/1770273455350_93lhuy_HAUslLkagAA_xOW.jpg)
![超逼真商业产品摄影展示（酸奶与电解质饮料）](https://cms-assets.youmind.com/media/1770273456309_k1cs5o_HAUslbDbIAEvHes.jpg)

```
{
  "master_prompt": {
    "global_settings": {
      "resolution": "8K ultra-high-definition",
      "aspect_ratio": "3:4 vertical",
      "style": "hyper-realistic AI-edited commercial product photography",
      "sharpness": "extreme clarity, micro-detail visibility",
      "lighting_quality": "cinematic studio lighting with controlled highlights and shadows",
      "motion_freeze": "high-speed capture, frozen splashes and particles",
      "noise": "none",
      "artifacts": "none"
    },

    "module_1_image_1_style": {
      "subject": {
        "type": "functional yogurt smoothie bottle",
        "material": "frosted plastic",
        "color": "soft pastel lavender",
        "surface_details": "dense condensation droplets covering the entire bottle",
        "label_text_visible": [
          "probiotic blend",
          "mock up",
          "high protein",
          "LOW FAT",
          "SEPARATED SHADOWS"
        ]
      },
      "pose_and_orientation": {
        "position": "slightly tilted forward",
        "angle": "three-quarter view",
        "motion_feel": "energetic, mid-impact splash moment"
      },
      "liquid_and_motion": {
        "liquid_color": "light purple yogurt smoothie",
        "texture": "thick, creamy, glossy",
        "motion": "smooth splash wrapping around the bottle with upward arcs"
      },
      "floating_elements": {
        "berries": "blackberries and blueberries floating at varying depths",
        "lavender_petals": "soft purple petals suspended mid-air",
        "droplets": "yogurt droplets and micro splashes frozen in motion"
      },
      "background": {
        "color_gradient": "deep violet fading into soft peach highlights",
        "bokeh": "subtle glowing circular light orbs"
      },
      "surface_and_reflection": {
        "base": "matte surface with creamy liquid pooling",
        "shadow_style": "clean, separated soft shadow beneath bottle"
      }
    },

    "module_2_image_2_style": {
      "subject": {
        "type": "sparkling electrolyte drink can",
        "material": "brushed aluminum",
        "color": "icy silver with neon cyan accents",
        "surface_details": "intense cold condensation with crystal-clear droplets",
        "branding_text_visible": [
          "HYDRATE+",
          "Electrolyte Drink",
          "ZERO SUGAR",
          "NEW FORMULA",
          "WITH MINERALS"
        ]
      },
      "pose_and_orientation": {
        "position": "upright and centered",
        "angle": "straight-on front view",
        "presence": "strong hero product stance"
      },
      "liquid_and_motion": {
        "liquid_color": "clear carbonated liquid with bubbles",
        "motion": "explosive splash bursting outward from the base",
        "droplet_behavior": "sharp, glass-like droplets flying outward"
      },
      "floating_elements": {
        "ice_cubes": "transparent ice cubes spinning in mid-air",
        "lime_slices":
```

[[Studio Lighting]] [[Commercial Product Photography]] [[Cinematic Product Shot]]

---

### 113. Nano Banana Pro 的产品拍摄提示：可口可乐冷藏箱中的艺术玩具

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2026-02-04  **Language**: en

> 一个详细、结构化的提示，旨在利用 Nano Banana Pro 生成高质量的商业风格产品照片。场景中，一个收藏级艺术玩具被放置在零售可口可乐冷藏柜内，重点突出光线、构图和纹理，以实现逼真的效果。

![Nano Banana Pro 的产品拍摄提示：可口可乐冷藏箱中的艺术玩具](https://cms-assets.youmind.com/media/1770273498585_02s8i0_HATxOsCbwAAxBSI.jpg)

```
{
  "meta": {
    "image_quality": "High",
    "image_type": "Photo",
    "resolution_estimation": "High resolution, likely smartphone or DSLR portrait crop",
    "file_characteristics": {
      "compression_artifacts": "Low",
      "noise_level": "Low",
      "lens_type_estimation": "Wide aperture, slight telephoto compression (approx 50mm-85mm equivalent)"
    }
  },
  "global_context": {
    "scene_description": "A close-up, eye-level shot inside a retail refrigerator or cooler display stocked densely with red Coca-Cola cans. Centered in the frame, resting on the lower tier of cans, is a collectible art toy (resembling a Labubu figure) wearing a fluffy white bunny costume. The toy holds a miniature Coca-Cola can. The background consists of rows of identical red cans, creating a repetitive pattern broken only by the central figure. Bright artificial lighting creates vertical highlights on the glossy aluminum surfaces.",
    "environment_type": "Indoor/Retail/Supermarket Cooler",
    "time_of_day": "Indiscernible (Artificial lighting)",
    "weather_atmosphere": "Commercial, Organized, Playful",
    "lighting": {
      "source": "Artificial/Fluorescent strip lighting",
      "direction": "Top-down and Frontal",
      "quality": "Hard with specular highlights",
      "color_temperature": "Cool White (approx 5000K)"
    },
    "color_palette": {
      "dominant_hex_estimates": [
        "#D81118",
        "#FFFFFF",
        "#C0C0C0",
        "#000000"
      ],
      "accent_colors": [
        "#F4C2C2",
        "#F2D4B8"
      ],
      "contrast_level": "High"
    }
  },
  "composition": {
    "camera_angle": "Eye-level",
    "framing": "Close-up",
    "depth_of_field": "Medium (Background slightly soft, foreground sharp)",
    "focal_point": "The white plush toy holding the mini can",
    "symmetry_type": "Vertical (approximate due to shelf arrangement)",
    "rule_of_thirds_alignment": "Toy is centered horizontally, occupying the central third vertically"
  },
  "objects": [
    {
      "id": "obj_001",
      "label": "Art Toy (Labubu style)",
      "category": "Toy/Collectible",
      "location": {
        "relative_position": "Center",
        "bounding_box_percentage": {
          "x": 0.38,
          "y": 0.30,
          "width": 0.25,
          "height": 0.35
        }
      },
      "dimensions_relative": "Small relative to frame, comparable height to a standard can",
      "distance_from_camera": "Mid (Focus plane)",
      "pose_orientation": "Facing forward, seated, holding object",
      "material": "Synthetic fur (plush), Vinyl/Plastic (face)",
      "surface_properties": {
        "texture": "Fluffy/Soft (costume), Smooth/Matte (face)",
        "reflectivity": "Low (fur), Medium (face)",
        "micro_details": "Individual fur strands, painted facial features, serrated teeth",
        "wear_state": "New"
      },
      "color_details": {
        "base_color_hex": "#F5F5F"
```

[[Studio Lighting]] [[Product Visualization]]

---

### 114. 通用超逼真 8K 电影摄影模板

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-02-04  **Language**: en

> 一个通用、高质量的模板提示，旨在最大限度地提高图像生成的真实感。它列出了众多技术规格，例如 8K 分辨率、超精细皮肤纹理、专业影棚布光、真实的景深、HDR 和电影级调色，旨在实现优质的编辑级输出。

![通用超逼真 8K 电影摄影模板](https://cms-assets.youmind.com/media/1770273443330_1f7unr_HASWgvGbMAAgwlK.jpg)
![通用超逼真 8K 电影摄影模板](https://cms-assets.youmind.com/media/1770273443475_vyi6o3_HASWgrBbwAAxtVp.jpg)
![通用超逼真 8K 电影摄影模板](https://cms-assets.youmind.com/media/1770273445836_7q9ywv_HASWg4ia4AA-p-6.jpg)
![通用超逼真 8K 电影摄影模板](https://cms-assets.youmind.com/media/1770273445253_9u06z7_HASWgp7a0AAqZ94.jpg)

```
Ultra-realistic 8K cinematic photograph of the subject, hyper-detailed skin texture, natural facial imperfections, sharp focus, professional studio lighting with soft shadows, realistic depth of field, HDR, global illumination, photorealistic colors, shot on a full-frame DSLR, 85mm lens, f/1.8, shallow depth, ultra-high resolution, crisp details, realistic environment, cinematic color grading, premium editorial quality, no blur, no distortion, no artifacts.
```

[[Studio Lighting]] [[8K Resolution]] [[Skin Texture]] [[Cinematic Color Grade]]

---

### 115. 玻璃工作区中主体的微距摄影

**Author**: [ΛRMIN | AI](https://x.com/Arminn_Ai)  **Date**: 2026-02-03  **Language**: en

> 一个详细的提示，用于生成一张超现实的微距照片，内容是一名（按职位指定）在垂直高大的玻璃立方体内的办公桌前工作的人。该提示强调了透明前玻璃与杂乱后墙之间的对比，重点关注逼真的纹理、柔和的蓝色负空间和影室布光。

![玻璃工作区中主体的微距摄影](https://cms-assets.youmind.com/media/1770187122757_dpvrj0_HAQXmZTWsAAbV7X.jpg)
![玻璃工作区中主体的微距摄影](https://cms-assets.youmind.com/media/1770187122810_dbwqfz_HAQXmZYXsAADIXy.jpg)

```
Hyper-realistic macro photography of a real living {argument name="subject job title" default="[Subject/Job Title]"} working at a desk inside a tall vertical rectangular glass cube. Centered composition. The glass structure occupies approximately 80% of the vertical frame height, ensuring a perfect amount of minimalist soft blue negative space on all four sides. The camera distance is a stable medium-close shot.

The Composition: The two glass walls facing the camera are completely clear and empty to allow a perfect view of the interior. In contrast, the interior of the two back walls is cluttered and densely covered from the floor to the very top edge with hundreds of {argument name="specific items" default="[Specific Job-related Items: e.g., sticky notes, charts, blueprints, vibrant mood boards, tiny Pantone color swatches]"}, creating an intense "busy" workload atmosphere.

Interior Details: realistic [Specific Desk Items], and a warm incandescent desk lamp that casts a soft golden glow over the workspace. The interior floor is made of polished white ceramic tiles. The floor around the desk is cluttered with tall, messy stacks of organized papers, open reference books and [Specific  Items]

The Realism: The person is NOT a plastic figure; they have visible skin texture, natural hair, and realistic clothing folds. Every object inside has sharp, crisp, and high-contrast textures. Lighting & Style: Bright studio lighting, clean shadows, macro photography style, minimalist soft blue background. 8k resolution, extremely detailed and sharp focus.
```

[[Studio Lighting]] [[Office Setting]]

---

### 116. 三张名人时尚编辑肖像照

**Author**: [Crystal](https://x.com/Cicily_aura)  **Date**: 2026-02-03  **Language**: en

> 一个 JSON 数组，包含三个不同的提示，用于生成安娜·德·阿玛斯（Ana de Armas）、萨迪·辛克（Sadie Sink）和肯达尔·詹娜（Kendall Jenner）的高分辨率、超写实时尚杂志肖像，每个提示都包含特定的造型、灯光和情绪要求。

![三张名人时尚编辑肖像照](https://cms-assets.youmind.com/media/1770187169684_x0pask_HAOuNgJaAAA8N9a.jpg)
![三张名人时尚编辑肖像照](https://cms-assets.youmind.com/media/1770187169674_vavfl1_HAOuNfwakAA4wH_.jpg)
![三张名人时尚编辑肖像照](https://cms-assets.youmind.com/media/1770187169691_008zhq_HAOuNfwacAAq0cL.jpg)
![三张名人时尚编辑肖像照](https://cms-assets.youmind.com/media/1770187170692_zhfryy_HAOuNfxbwAAJ-0K.jpg)

```
[
    {
      "prompt_details": {
        "subject": {
          "identity": "{argument name="celebrity 1" default="Ana de Armas"}",
          "appearance": "brunette hair, warm brown eyes, natural dewy makeup",
          "pose": "relaxed elegant pose, soft confident gaze",
          "clothing": "champagne-toned silk gown"
        },
        "environment": {
          "setting": "luxury indoor studio",
          "color_palette": "warm gold and dark neutral tones"
        },
        "lighting_and_mood": {
          "lighting_style": "soft cinematic lighting with rim light",
          "mood": "intimate, sophisticated editorial"
        },
        "quality_tags": [
          "4k resolution",
          "photorealistic",
          "sharp focus",
          "fashion editorial",
          "portrait ratio 9:16"
        ]
      }
    },
    {
      "prompt_details": {
        "subject": {
          "identity": "{argument name="celebrity 2" default="Sadie Sink"}",
          "appearance": "red hair updo, fair skin with freckles, blue eyes",
          "pose": "upright elegant posture, direct gaze",
          "clothing": "black lace evening dress"
        },
        "environment": {
          "setting": "classic studio backdrop",
          "color_palette": "black with soft highlights"
        },
        "lighting_and_mood": {
          "lighting_style": "soft dramatic studio lighting",
          "mood": "timeless fashion portrait"
        },
        "quality_tags": [
          "4k resolution",
          "high detail",
          "cinematic look",
          "portrait ratio 9:16"
        ]
      }
    },
    {
      "prompt_details": {
        "subject": {
          "identity": "{argument name="celebrity 3" default="Kendall Jenner"}",
          "appearance": "long dark hair, minimal makeup, sun-kissed skin",
          "pose": "seated relaxed pose, confident gaze",
          "clothing": "minimal neutral lounge outfit"
        },
        "environment": {
          "setting": "luxury resort-style interior",
          "color_palette": "warm beige and earth tones"
        },
        "lighting_and_mood": {
          "lighting_style": "natural window light",
          "mood": "modern lifestyle editorial"
        },
        "quality_tags": [
          "4k resolution",
          "photorealistic",
          "clean aesthetic",
          "portrait ratio 9:16"
        ]
      }
    }
]
```

[[Studio Lighting]] [[Editorial Photography]] [[High Resolution]]

---

### 117. 8K 美妆产品气球拍摄

**Author**: [Max](https://x.com/Max__Build)  **Date**: 2026-02-03  **Language**: en

> 一个超逼真的商业美容产品拍摄宣传提示，画面中一个面膜管被两个亮粉色气球挤压，强调干净的影室灯光、产品标签上的清晰焦点，以及奢华美妆广告的审美。

![8K 美妆产品气球拍摄](https://cms-assets.youmind.com/media/1770187171871_avjgwl_HANfk_6aMAAmVZn.jpg)

```
A photorealistic commercial beauty product shot featuring the CAIA Instant Soothing Face Mask tube tightly squeezed between two large glossy {argument name="balloon color" default="pink"} balloon like spheres. The balloons press inward with soft, rounded tension, creating a realistic compression effect around the tube.
Position the CAIA tube vertically, slightly angled, perfectly centered, with the front label text sharp, readable, and facing directly toward the camera.
Ultra-clean studio beauty lighting with smooth highlights, soft specular reflections on the balloons, and gentle shadow falloff. Background is soft pastel {argument name="background color" default="pink"} with subtle gradient transitions, clean and distraction-free.
The tube features accurate matte plastic material, realistic surface texture, subtle reflections, crisp edges, and ultra sharp focus. Shallow depth of field keeps the product perfectly sharp while balloons remain slightly softer.
Modern, minimalistic, premium skincare advertising aesthetic. High-end commercial look, playful squeeze composition, luxury beauty campaign energy, hyper detailed textures, clean symmetry, editorial grade realism, image size 9: 16 image create
```

[[Studio Lighting]] [[Skincare Product Photography]] [[Commercial Beauty Photography]]

---

### 118. 汽水罐飞溅的超逼真商业产品照片

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-03  **Language**: en

> 一个高度详细、结构化的 JSON 提示，用于生成一张超逼真的商业产品照片，内容为一罐橙汁汽水冲破液体飞溅而出。它要求极高的清晰度、电影级的影棚布光、凝固的液滴和漂浮元素（橙子、冰块）的动态，所有这些都置于纯橙色背景之上。

![汽水罐飞溅的超逼真商业产品照片](https://cms-assets.youmind.com/media/1770187137361_jd4hth_HAM94ETagAEACO-.jpg)
![汽水罐飞溅的超逼真商业产品照片](https://cms-assets.youmind.com/media/1770187137448_k9foqs_HAM94EZaQAAe4YF.jpg)

```
{
  "master_prompt": {
    "global_settings": {
      "resolution": "8K ultra-high-definition",
      "aspect_ratio": "3:4 vertical",
      "style": "hyper-realistic AI-edited commercial product photography",
      "sharpness": "extreme clarity, micro-detail visibility",
      "lighting_quality": "cinematic studio lighting with controlled highlights and shadows",
      "motion_freeze": "high-speed capture, frozen splashes and particles",
      "noise": "none",
      "artifacts": "none"
    },

"module_1_image_1_style": {
      "subject": {
        "type": "orange-flavored soda can",
        "color": "bright orange",
        "surface_details": "condensation droplets across can",
        "branding_text_visible": [
          "{argument name="brand name" default="Sesla"}",
          "{argument name="product type" default="cola"}"
        ]
      },
      "pose_and_orientation": {
        "position": "upright, slightly embedded in splash",
        "angle": "centered frontal view"
      },
      "liquid_and_motion": {
        "liquid_color": "transparent orange-tinted liquid",
        "motion": "high-energy splash bursting upward and outward",
        "splash_detail": "clear liquid arcs with suspended droplets"
      },
      "floating_elements": {
        "oranges": [
          "whole oranges",
          "halved oranges with visible pulp"
        ],
        "ice_cubes": "clear sharp-edged cubes floating mid-air",
        "droplets": "numerous spherical liquid droplets"
      },
      "background": {
        "color": "solid bright orange",
        "lighting": "high-key, evenly lit"
      },
      "surface_and_reflection": {
        "base": "shallow liquid pool",
        "reflection_quality": "strong mirror-like reflection with ripples"
      }
    }
  }
}
```

[[Studio Lighting]] [[Floating Ingredients]] [[Commercial Beverage Photography]]

---

### 119. 超逼真高速水果飞溅摄影

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-02-02  **Language**: en

> 一个高度结构化的提示，旨在生成超逼真、高速的食物摄影作品，内容为一碗混合水果的透明玻璃碗在溅起水花时被捕捉到的瞬间。该提示包括对风格、相机设置（镜头、光圈、快门速度）、照明的详细说明，以及一个全面的负面提示，以实现最大程度的真实感。

```
{  "Ultra-realistic high-speed food photography of a transparent glass bowl filled with fresh mixed fruits captured mid-splash. Vivid {argument name="fruits" default="strawberries, blueberries, raspberries, kiwi slices, and orange wedges"} erupt upward with crystal-clear water splashes frozen in motion. Individual water droplets suspended in the air, realistic fluid dynamics, sharp splash crowns, and natural refraction through glass. Fruits appear fresh, glossy, and richly textured with visible seeds, pulp, and skin detail. Dramatic studio lighting from above and slightly behind creates specular highlights on water and fruit surfaces. Dark, cinematic background with soft bokeh and strong contrast to enhance color saturation. Shallow depth of field with razor-sharp focus on the central splash and fruits. Premium commercial food photography aesthetic, hyper-realistic, ultra-detailed, cinematic realism, 8K quality.",
  "style": "photorealistic",
  "camera": {
    "lens": "85mm macro",
    "aperture": "f/4",
    "iso": 100,
    "shutter_speed": "1/2000"
  },
  "lighting": "high-speed studio lighting with strong backlight and soft fill, specular highlights on water droplets",
  "background": "dark studio background with subtle bokeh and depth",
  "composition": "centered glass bowl with vertical splash action and dynamic fruit distribution",
  "quality": "8K ultra-high resolution",
  "negative_prompt": "cartoon, illustration, CGI look, low detail, blur, motion smear, artificial colors, plastic texture, text, logo, watermark, hands, utensils, distortion"
}
```

[[Studio Lighting]]

---

### 120. 定制异形会议桌俯视图

**Author**: [ᴬˡᵉˣ ᵀᵉᶜʰ ᴬᶤ ᴱˣᵖˡᵒʳᵉʳ ↯](https://x.com/Jeep4x4Sol)  **Date**: 2026-01-31  **Language**: en

> 一个可定制的提示，用于生成一张超现实、超广角、俯视平铺的会议桌照片，该会议桌的形状为特定物体或符号。该提示要求定义桌子的形状、材质以及围坐在桌子旁的人的动作，并强调专业的影棚灯光和清晰的投影。

![定制异形会议桌俯视图](https://cms-assets.youmind.com/media/1769927672921_b0uh8t_HAAnE-zXoAIVugE.jpg)
![定制异形会议桌俯视图](https://cms-assets.youmind.com/media/1769927672926_ws77u5_HAAnFAQWgAAL08a.jpg)

```
Ultra-wide-angle hyper-realistic top-down flat lay photography. The central focus is a custom physical conference table meticulously shaped like {argument name="Shape" default="[SHAPE/NUMBER/SYMBOL]"}.

The table features {argument name="Material" default="[MATERIAL/TEXTURE/COLOR]"} and placed on a [FLOOR COLOR] floor, creating significant negative space around it for a clean, minimalist composition. A group of {argument name="Number of People" default="[NUMBER]"} real people are sitting around the edges of this [SHAPE]-shaped table. [POSITIONING: e.g., 3 on each side, 1 top/bottom]

Actions: [DESCRIBE PEOPLE'S ACTIONS, e.g., working on laptops, drinking coffee].
Lighting & Quality: Professional studio lighting with crisp, distinct drop shadows that define the [SHAPE] silhouette on the floor. 8k resolution, sharp focus, cinematic commercial aesthetic.
```

[[Studio Lighting]] [[Architectural Visualization]] [[Overhead Flat Lay]]

---

### 121. 定制异形会议桌的俯视图（重复）

**Author**: [ΛRMIN | AI](https://x.com/Arminn_Ai)  **Date**: 2026-01-31  **Language**: en

> 一个可定制的提示，用于生成一张超逼真、超广角、俯视平铺的会议桌照片，该会议桌的形状为特定物体或符号。此提示需要定义桌子的形状、材质以及围坐在桌旁的人的动作，并强调专业的影棚灯光和清晰的投影。（重复 ID：2017655603405942826）。

![定制异形会议桌的俯视图（重复）](https://cms-assets.youmind.com/media/1769927676499_7dhvvn_HAAaWTtXkAAiA6-.jpg)
![定制异形会议桌的俯视图（重复）](https://cms-assets.youmind.com/media/1769927676512_a0j2qb_HAAaWUIXkAAqoor.jpg)
![定制异形会议桌的俯视图（重复）](https://cms-assets.youmind.com/media/1769927676541_9dtyn2_HAAaWSZXcAAAoFA.jpg)
![定制异形会议桌的俯视图（重复）](https://cms-assets.youmind.com/media/1769927677166_pwy7zo_HAAaWQiWMAAiILl.jpg)

```
Ultra-wide-angle hyper-realistic top-down flat lay photography. The central focus is a custom physical conference table meticulously shaped like {argument name="Shape" default="[SHAPE/NUMBER/SYMBOL]"}.

The table features {argument name="Material" default="[MATERIAL/TEXTURE/COLOR]"} and placed on a [FLOOR COLOR] floor, creating significant negative space around it for a clean, minimalist composition. A group of {argument name="Number of People" default="[NUMBER]"} real people are sitting around the edges of this [SHAPE]-shaped table. [POSITIONING: e.g., 3 on each side, 1 top/bottom]

Actions: [DESCRIBE PEOPLE'S ACTIONS, e.g., working on laptops, drinking coffee].
Lighting & Quality: Professional studio lighting with crisp, distinct drop shadows that define the [SHAPE] silhouette on the floor. 8k resolution, sharp focus, cinematic commercial aesthetic.
```

[[Studio Lighting]] [[Architectural Visualization]] [[Overhead Flat Lay]]

---

### 122. 反重力色彩盒中的高级时装大片

**Author**: [Saman | AI](https://x.com/Samann_ai)  **Date**: 2026-01-31  **Language**: en

> 一个复杂、参数化的提示，用于生成一张超现实、高级时装的编辑图片，其中主体（使用上传照片锁定身份）在一个超现实、单色的 3D 几何“色彩盒”房间内摆出动态姿势，强调影棚灯光和对比色。

![反重力色彩盒中的高级时装大片](https://cms-assets.youmind.com/media/1769927656045_g94mm2_G__zS1oWcAEJfPx.jpg)

```
[INPUT IMAGE: USER_PHOTO] Use the person in the input image as the ONLY subject. Preserve their identity and facial features clearly.

Create a hyper-realistic high-fashion editorial photo inside a surreal 3D geometric “color box” room (a hollow cube / tilted cube set). Each render MUST randomly choose:
1) a bold single-color box (monochrome environment, vivid and saturated),
2) a dynamic “cool” fashion pose (gravity-defying or extreme stretch / leap / sideways bracing against the walls),
3) a dramatic camera angle (wide-angle 24–35mm equivalent, tilted horizon, strong perspective).

The subject appears full-body and sharp, wearing an avant-garde fashion styling that feels modern and editorial (clean silhouette, stylish layering, premium fabric texture). Keep clothing tasteful and fashion-forward. The subject’s pose should feel athletic, stylish, and unusual—like a magazine campaign shot.

Lighting: studio quality, crisp and cinematic; strong key light with controlled soft shadows, subtle rim light; realistic reflections and bounce light from the colored walls. Ultra-detailed skin texture, natural pores, realistic fabric weave, clean edges, high dynamic range. 
Composition: subject centered with plenty of negative space and strong geometric lines; the box color is a SINGLE bold color and MUST be different each run (random vivid hue). The subject’s outfit contrasts well with the box color.

Output: hyper-real, photorealistic, 8k detail, editorial campaign quality, sharp focus on subject, no motion blur, no distortion of face, natural proportions.
```

[[Studio Lighting]] [[Dynamic Pose]] [[Surreal Fashion Editorial]]

---

### 123. 皮克斯风格 3D 虚拟形象生成提示

**Author**: [Arce.](https://x.com/arceyul)  **Date**: 2026-01-30  **Language**: en

> 一个提示，用于将上传的图像转换为具有皮克斯风格美学的高质量 3D 头像。它指定了愉快的表情、平滑的纹理和柔和均匀的摄影棚灯光，以营造出友好且平易近人的动画外观。

![皮克斯风格 3D 虚拟形象生成提示](https://cms-assets.youmind.com/media/1769841089547_shbg08_G_75rXTXEAAa6pT.jpg)
![皮克斯风格 3D 虚拟形象生成提示](https://cms-assets.youmind.com/media/1769841089559_3dgk42_G_75rXPXcAAFjaX.jpg)

```
Create a high-quality 3D avatar of the person in the uploaded image with a cheerful, expressive face. The character should have a warm smile, bright eyes, and soft facial features that feel friendly and approachable. Render in a Pixar-style aesthetic with smooth textures, subtle skin shading, and slightly exaggerated proportions for a cute, animated look. Lighting should be soft and even, creating a clean studio look with gentle shadows for depth.
```

[[Studio Lighting]] [[Pixar Style]] [[3D Character]]

---

### 124. 高端概念艺术杂志编辑提示

**Author**: [AmirMušić](https://x.com/AmirMushich)  **Date**: 2026-01-30  **Language**: en

> 一个详细的提示模板，用于生成一张高端、光泽的编辑摄影作品，内容是品牌构思的独特、出乎意料的功能性物体。它指定了超高级材料、电影级影棚照明（飞思相机，100mm 微距镜头），以及严格的文本和标志布局，旨在可视化概念杂志创意。

![高端概念艺术杂志编辑提示](https://cms-assets.youmind.com/media/1769841153976_p4imkf_G_7vUKfW0AErSKW.jpg)

```
[BRAND NAME]: 
A high-end, glossy concept art magazine editorial photograph of a unique, unexpected functional object conceptualized and designed by the brand.

**1. The Concept & Object (AI Invention):**
Based on the design philosophy, heritage, and material vocabulary of the specified brand, the AI must invent a novel utility product (NOT standard clothing, shoes, or bags). Examples could be home goods, tech accessories, tools, or sporting equipment, reinterpretated through the brand's lens. The object should feel sculptural yet functional.

**2. Materials & Details (Hyper-Premium):**
The object is constructed from ultra-premium, highly tactile materials characteristic of the brand (e.g., patinated exotic leathers, brushed aerospace-grade titanium, sculpted matte ceramics, molded carbon fiber, or technical high-fashion textiles). Every detail is hyper-realistic: visible stitching, microscopic material grain, precision engravings, and complex texture contrasts.

**3. Photography & Lighting (Cinematic Studio):**
Shot on a medium format Phase One camera with a 100mm macro lens. Extremely shallow depth of field, with sharp focus on the hero details of the object and a creamy, smooth bokeh background. The lighting is sophisticated studio softbox lighting: gentle, enveloping fill light with precise rim lighting to accentuate contours and material textures.

**4. Environment:**
A seamless, impeccably clean studio cyclorama background in a pure, ultra-light pastel tone (e.g., desaturated mint, pale blush, or off-white), free of shadows.

**5. Layout & UI Elements (Strict Placement):**
- **Bottom Right Corner:** A small, understated, monochrome gray logo of the {argument name="brand name" default="BRAND NAME"}.
- **Bottom Left Corner:** Small, minimalist monochrome gray text describing the invented product. The font style looks like Manrope Regular with very tight tracking (kerning) and balanced line spacing. Example format: "CONCEPT STUDY: {argument name="invented product name" default="[AI inserts invented product name]"}. MATERIAL: [AI inserts main materials]. SS25."
```

[[Studio Lighting]] [[Magazine Editorial]]

---

### 125. 夸张沙漏身材健身房自拍提示词

**Author**: [Bethany](https://x.com/JustBethanyai)  **Date**: 2026-01-30  **Language**: en

> 一个详细的 JSON 提示，用于生成一张主体在现代健身房环境中拍摄的镜面自拍，主体拥有夸张的沙漏型身材，重点关注特定的姿势、服装和灯光，以突出曲线和肌肉线条。

![夸张沙漏身材健身房自拍提示词](https://cms-assets.youmind.com/media/1769841077508_xh1uo7_G_7nfa3XMAAibWb.jpg)
![夸张沙漏身材健身房自拍提示词](https://cms-assets.youmind.com/media/1769841077543_ucm6s6_G_7nflsWUAAuSeK.jpg)
![夸张沙漏身材健身房自拍提示词](https://cms-assets.youmind.com/media/1769841077488_qoyq9l_G_7nflxWkAAFNDN.jpg)
![夸张沙漏身材健身房自拍提示词](https://cms-assets.youmind.com/media/1769841078350_ksgif1_G_7nfgGWUAAWhOo.jpg)
![夸张沙漏身材健身房自拍提示词](https://cms-assets.youmind.com/media/1769841078650_pq0fxz_G_x6usVX0AAWUTQ.jpg)
![夸张沙漏身材健身房自拍提示词](https://cms-assets.youmind.com/media/1769841079190_j6drhj_G_x6uurXQAAZXuS.jpg)
![夸张沙漏身材健身房自拍提示词](https://cms-assets.youmind.com/media/1769841080450_aiwtua_G_x6u0KXEAA5E48.jpg)
![夸张沙漏身材健身房自拍提示词](https://cms-assets.youmind.com/media/1769841081406_52u232_G_x6u4RWoAA3N_K.jpg)

```
{
  "subject": {
    "identity": "USE_YOUR_REFERENCE_CHARACTER",
    "body": {
      "description": "An exaggerated hourglass figure with a very narrow, snatched waist and wide, curvaceous hips. The shoulders are comparatively narrow, emphasizing a dramatic waist-to-hip ratio. The glute muscles are heavily developed, with thick, muscular thighs. The spine appears visibly arched due to the pose.",
      "pose": "Kneeling on the floor, facing away from the mirror while looking back over the shoulder, holding a smartphone to take a mirror selfie, emphasizing the back and side profile.",
      "barefoot": true
    },
    "wardrobe": {
      "top": "White crop t-shirt, slightly lifted or tied at the back.",
      "bottom": "Very short athletic shorts in soft pastel pink, made of smooth stretchy fabric, featuring prominent white text (not inverted) that reads '{argument name="shorts text" default="REFERENCE"}' across the back.",
      "accessories": "Smartphone in a soft pink or neutral case, simple necklace."
    }
  },
  "camera": {
    "type": "Smartphone camera (mirror selfie)",
    "lens": "Wide-angle",
    "aspect_ratio": "3:4"
  },
  "lighting": {
    "type": "Artificial night light from large windows combined with soft indoor gym lighting.",
    "quality": "Soft and diffused, highlighting natural skin texture and muscular curves.",
    "direction": "From the left and above."
  },
  "scene": {
    "location": "Modern gym.",
    "background": "Large windows with a blurred {argument name="cityscape" default="Paris"} cityscape at night, out-of-focus cardio machines such as treadmills and bikes, mirror reflections.",
    "props": "Light blue exercise mat on the floor."
  },
  "texture": {
    "clothing": "Soft cotton crop t-shirt, smooth stretchy athletic fabric for the shorts.",
    "skin": "Smooth, natural skin texture."
  },
  "style": {
    "mood": "Cinematic but realistic",
    "detail_level": "High detail",
    "rendering": "Realistic lighting, natural proportions despite stylized curves"
  }
}
```

[[Studio Lighting]] [[Hourglass Figure]] [[Gym Mirror Selfie]] [[Athletic Wear]]

---

### 126. 超逼真浆果冰沙爆炸美食摄影提示

**Author**: [Snow](https://x.com/iamrealsnow)  **Date**: 2026-01-30  **Language**: en

> 一个详细的提示，用于生成 8K 超逼真商业食品摄影，捕捉一个浆果思慕雪碗在空中爆裂，食材悬浮，重点是锐利对焦、影棚布光和高速摄影效果。

![超逼真浆果冰沙爆炸美食摄影提示](https://cms-assets.youmind.com/media/1769841053431_dz92wv_G_6tK_ubIAATt5L.jpg)
![超逼真浆果冰沙爆炸美食摄影提示](https://cms-assets.youmind.com/media/1769841053530_9och9q_G_6tLM3aEAA0wjt.jpg)

```
{
  "resolution": "8K UHD",
  "aspect_ratio": "3:4",
  "image_style": "hyper-realistic commercial food photography",
  "global_settings": {
    "quality": "Ultra-high detail, sharp focus, studio-grade clarity",
    "lighting": "Soft but controlled studio lighting with visible highlights and splash definition",
    "motion": "Frozen mid-air action, ingredients suspended",
    "background_style": "Solid or smooth gradient background, color varies per module",
    "camera": "High-speed photography look, shallow to medium depth of field",
    "post_processing": "Balanced contrast, natural saturation, no artificial glow"
  },

  "modules": {

    "module_1_berry_smoothie_explosion": {
      "scene_description": "A vibrant smoothie bowl exploding with fruit and liquid splashes",
      "bowl": {
        "color": "{argument name="bowl color" default="Deep blue ceramic"} bowl",
        "finish": "Glossy",
        "position": "Centered, floating mid-air"
      },
      "base_contents": {
        "type": "Thick berry smoothie",
        "color": "Deep purple-magenta",
        "texture": "Creamy with visible swirl marks"
      },
      "ingredients": {
        "fruits": [
          "Banana slices (round, pale yellow)",
          "Blueberries (whole, dark blue)",
          "Raspberries (whole, red)"
        ],
        "herbs": [
          "Fresh mint leaves (bright green)"
        ]
      },
      "motion_effects": {
        "liquid": "Berry smoothie splashing upward and outward",
        "particles": "Small droplets suspended in air"
      },
      "background": {
        "color": "{argument name="background color" default="Bright pink"}",
        "texture": "Smooth, seamless"
      }
    }}
```

[[Studio Lighting]]

---

### 127. 皮克斯风格 3D 头像生成提示词

**Author**: [狗富贵](https://x.com/cryptoGFG)  **Date**: 2026-01-30  **Language**: zh

> 一个用于 Gemini Nano Banana Pro 的提示，可将用户的头像转换为具有皮克斯 (Pixar) 美学风格的高质量 3D 虚拟角色。它强调开朗的表情、温暖的笑容和柔和的影棚灯光，以营造友好、亲切的外观。

![皮克斯风格 3D 头像生成提示词](https://cms-assets.youmind.com/media/1769841145146_m488w5_G_5cCBtbUAUln7v.jpg)

```
根据图像创建高质量 3D 虚拟形象，皮克斯风格美学，面部表情欢快，配合柔和工作室灯光...
```

[[Studio Lighting]] [[Pixar Style]] [[Warm Smile]]

---

### 128. 3D 拟人化兔子角色提示词

**Author**: [ShaHid WaNii](https://x.com/meng_dagg695)  **Date**: 2026-01-30  **Language**: en

> 一个结构化提示，用于生成一张 3D 动画风格、风格化写实的图像，描绘一只穿着黄色背带裤的快乐、胖乎乎的拟人化白兔，重点突出蓬松的毛发细节、大而有光泽的眼睛，以及在纯色背景下的柔和工作室照明。

![3D 拟人化兔子角色提示词](https://cms-assets.youmind.com/media/1769841054113_hwvz6c_G_5JMpkbYAAuBiq.jpg)
![3D 拟人化兔子角色提示词](https://cms-assets.youmind.com/media/1769841054123_us53ny_G_5JMj6bgAAkedX.jpg)
![3D 拟人化兔子角色提示词](https://cms-assets.youmind.com/media/1769841054180_fpre49_G_5JMvjbUAgHbCh.jpg)

```
{
  "subject": {
    "type": "anthropomorphic bunny",
    "species": "rabbit",
    "gender": "not specified",
    "age_representation": "childlike / cartoon-styled",
    "pose": "standing on hind legs with one leg lifted forward, one arm raised upward, the other arm slightly bent outward",
    "expression": "happy, joyful, open-mouthed smile",
    "emotion": "cheerful, playful"
  },
  "head_and_face": {
    "head_shape": "round and fluffy",
    "fur_color": "pure white",
    "fur_texture": "very soft, dense, fluffy, fine strands visible",
    "eyes": {
      "size": "very large",
      "shape": "round",
      "color": "blue with darker outer ring",
      "pupils": "large black pupils",
      "eye_style": "glossy, reflective, cartoon-like"
    },
    "nose": {
      "size": "small",
      "shape": "rounded",
      "color": "soft pink"
    },
    "mouth": {
      "state": "open",
      "shape": "small rounded opening",
      "inner_color": "dark pink",
      "teeth": "not visible"
    },
    "cheeks": {
      "shape": "puffy",
      "tint": "light pink blush"
    }
  },
  "ears": {
    "count": 2,
    "position": "upright",
    "shape": "long and slightly curved",
    "outer_fur": "white and fluffy",
    "inner_ear_color": "light pink",
    "accessory": {
      "type": "small hair band",
      "color": "red",
      "placement": "wrapped around one ear"
    }
  },
  "body": {
    "proportions": "chubby, small torso with oversized head",
    "fur_color": "white",
    "fur_texture": "plush, soft, evenly groomed"
  },
  "clothing": {
    "outfit_type": "overalls",
    "material_appearance": "soft fabric with visible texture",
    "color": "{argument name="overalls color" default="yellow"}",
    "design": {
      "straps": 2,
      "buttons": {
        "count": 2,
        "shape": "round",
        "color": "pink",
        "decoration": "flower-shaped"
      }
    },
    "fit": "loose and rounded around the belly"
  },
  "limbs": {
    "arms": {
      "count": 2,
      "fur_color": "white",
      "pose": {
        "left_arm": "raised upward in a waving gesture",
        "right_arm": "slightly bent outward"
      },
      "paws": {
        "shape": "small and rounded",
        "pads_color": "light pink"
      }
    },
    "legs": {
      "count": 2,
      "pose": {
        "support_leg": "standing firmly on ground",
        "raised_leg": "lifted forward in playful motion"
      },
      "feet": {
        "shape": "rounded",
        "pads_color": "light pink"
      }
    }
  },
  "background": {
    "type": "solid color",
    "color": "{argument name="background color" default="coral / warm reddish-pink"}",
    "texture": "smooth, gradient-free"
  },
  "lighting": {
    "type": "soft studio lighting",
    "direction": "even frontal lighting",
    "shadows": "soft and subtle beneath the feet",
    "highlights": "gentle highlights on fur and eyes"
  },
  "render_style": {
    "style": "3D animated character",
    "realism_level": "stylized realism",
    "fur_detail": "high strand"
```

[[Studio Lighting]]

---

### 129. 详细的皮克斯风格 3D 头像生成提示

**Author**: [路飞 🏴‍☠️ AI 研究员🧐](https://x.com/0xluffy_eth)  **Date**: 2026-01-30  **Language**: zh

> 一个为 Gemini Nano Banana Pro 设计的详细提示，用于将上传的图像转换为 3D 虚拟形象。它指定了皮克斯（Pixar）风格的美学，重点是温暖、友好的表情，平滑的纹理，微妙的皮肤阴影，以及略微夸张的比例，在柔和、均匀的摄影棚灯光下渲染。

![详细的皮克斯风格 3D 头像生成提示](https://cms-assets.youmind.com/media/1769841146479_1je0ph_G_4TLNtbUAEgYeg.jpg)

```
根据上传的图像创建一个高质量的 3D 虚拟形象，面部表情欢快有表现力。角色应该有温暖的微笑、明亮的眼睛和柔和的面部特征，给人友好亲切的感觉。采用{argument name="style" default="皮克斯风格美学"}，具有光滑纹理、细微肤色阴影和略微夸张的比例，呈现可爱的动画效果。灯光应柔和均匀，营造干净的工作室效果，柔和的阴影增添深度感。
```

[[Studio Lighting]] [[Pixar Style]] [[Warm Smile]]

---

### 130. 超逼真拼布钩针玩偶产品照片提示

**Author**: [Shams](https://x.com/ShamsAmin56)  **Date**: 2026-01-29  **Language**: en

> 一个详细的图像生成提示，旨在创建一张超逼真的产品照片，内容是一个可爱的、手工制作的拼布织物钩针玩偶。它指定了风格（回收织物、可见缝线、磨损边缘）、灯光（专业摄影棚）和构图（微距摄影、垂直构图），以获得高质量、迷人的视觉效果。

![超逼真拼布钩针玩偶产品照片提示](https://cms-assets.youmind.com/media/1769754973442_fcsfbl_G_3Hjn2XYAADn92.jpg)

```
Hyper-realistic photograph of an adorable handmade patchwork fabric amigurumi {argument name="subject" default="SUBJECT"} made from upcycled cotton scraps, extremely detailed visible mismatched seams, frayed thread edges, varied fabric prints and textures, soft stuffed volume with gentle puckering and folds, charming handmade imperfections, professional product photography, studio lighting, subtle bokeh, against {argument name="background description" default="BACKGROUND DESCRIPTION"}, vertical composition, ultra-detailed, 2k, photorealistic, macro photography style --ar [X:X]--stylize 250 --v 6 --q 2
```

[[Studio Lighting]] [[Macro Photography]] [[Vertical Composition]]

---

### 131. 漂浮西柚气泡罐的奢华商业拍摄

**Author**: [Maercih](https://x.com/Maercihh)  **Date**: 2026-01-29  **Language**: en

> 一个用于生成高真实感、奢华商业广告图像的提示。画面中，一个金属玫瑰粉色饮料罐悬浮在半空中，周围环绕着凝固的液体飞溅、葡萄柚切片和金色散景粒子，背景是柔和的粉桃色和腮红色调，强调影棚级灯光和超洁净反射。

![漂浮西柚气泡罐的奢华商业拍摄](https://cms-assets.youmind.com/media/1769754981966_jwfwrs_G_0vdZCaIAAGpaK.jpg)
![漂浮西柚气泡罐的奢华商业拍摄](https://cms-assets.youmind.com/media/1769754981996_dae8va_G_0vdZEbUAIbFm7.jpg)

```
Floating aluminum beverage can suspended mid-air, metallic rose-pink finish, brand text "{argument name="brand name" default="MAERCIH"}" vertically aligned and sharply legible, surrounded by fresh grapefruit slices and citrus shards, liquid splash frozen in motion beneath the can, sparkling droplets suspended around it, warm golden bokeh particles in the air, soft pastel peach and blush background, tropical hints with subtle palm blur in the distance, studio-quality product lighting with soft rim light and glossy specular highlights, shallow depth of field, ultra-clean reflections on the can, premium beverage advertising style, high realism, cinematic composition, controlled color palette, no distortion, no label warping, no harsh shadows, no over-saturation, luxury commercial look, photorealistic, high detail, smooth gradients, intentional motion freeze
```

[[Studio Lighting]] [[Commercial Product Photography]]

---

### 132. 草莓落入牛奶的特写镜头

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-29  **Language**: en

> 一个高度详细的提示，用于生成一张超逼真的食物动态微距照片。它专注于新鲜草莓落入乳白色牛奶中的瞬间，捕捉浓稠牛奶飞溅形成的皇冠、丝滑的液体波纹和凝固的液滴，采用柔和的影棚布光和高调美食摄影技术，营造出奢华甜点广告的风格。

![草莓落入牛奶的特写镜头](https://cms-assets.youmind.com/media/1769754984132_sumuf6_G_0DNBqbUAAaWmg.jpg)
![草莓落入牛奶的特写镜头](https://cms-assets.youmind.com/media/1769754984373_qk7dol_G_0DNBybEAAH-ke.jpg)
![草莓落入牛奶的特写镜头](https://cms-assets.youmind.com/media/1769754984278_o19g0y_G_0DNAhbIAA9uDJ.jpg)
![草莓落入牛奶的特写镜头](https://cms-assets.youmind.com/media/1769754986297_25n7d5_G_0DNCobUAE1r-2.jpg)

```
Ultra realistic macro of fresh strawberries falling into creamy white milk, thick milk splash crown, silky liquid waves, frozen motion droplets, soft studio lighting, high key food photography, ultra smooth textures, 8K resolution, luxury dessert ad style, shallow depth of field, clean white background with soft shadows. --ar 3:4 --exp 5 --raw
```

[[Studio Lighting]] [[Macro Photography]] [[Food Photography]]

---

### 133. 高端封面视觉生成提示

**Author**: [SRKDAN](https://x.com/SRKDAN)  **Date**: 2026-01-28  **Language**: en

> 一个简单有效的提示模板，用于生成高端封面或专题视觉效果。它指定了居中构图、充足的留白、优质的影棚布光和简洁的背景，以确保在缩略图和全尺寸下都清晰可见。

![高端封面视觉生成提示](https://cms-assets.youmind.com/media/1769668439276_fw97fx_G_dK8oJW0AAkuVY.jpg)

```
High-end cover visual with a single dominant subject.
Centered composition, generous negative space,
soft shadows beneath the subject,
premium studio lighting with subtle highlights,
clean background with gentle gradient,
designed to read clearly at thumbnail size and full scale.
```

[[Studio Lighting]] [[Magazine Cover Design]] [[Centered Composition]]

---

### 134. 超逼真奇异果飞溅微距摄影提示词

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-28  **Language**: en

> 一个用于生成超逼真、8K 宏观摄影的提示，内容是切片猕猴桃溅入水中。该提示强调猕猴桃切片的漂浮构图、悬浮的水滴、影室布光和高细节，以突出纹理和反射，营造出清新、明亮、多汁的美感，并带有浓郁的绿色调。

![超逼真奇异果飞溅微距摄影提示词](https://cms-assets.youmind.com/media/1769668461972_7qxwou_G_wl9x7bYAAv_51.jpg)

```
A hyper-realistic image of a sliced kiwi splashing in a spray of water with droplets suspended in the air. Fresh kiwi slices, dynamically arranged in a floating composition, create a smooth green background. The smooth green gradient creates a fresh, bright, and juicy aesthetic. Studio lighting, soft shadows, high detail, macro photography of objects, an emphasis on texture and reflections. Ultra-realistic rendering, 8K, sharp focus, rich green tones. --ar 9:16 --raw
```

[[Studio Lighting]] [[Macro Photography]] [[8K Food Photography]]

---

### 135. 四格美妆编辑拼贴画

**Author**: [simeon-sanai](https://x.com/Naiknelofar788)  **Date**: 2026-01-27  **Language**: en

> 一个用于生成四格分屏美妆专题拼贴画的提示，画面中是一位留着棕色短波波头、拥有“玻璃肌”美学的女性。它详细描述了“素颜妆”造型、特定配饰（千鸟格帽子），以及 8K 分辨率和商业影棚照明等技术规格，以实现超现实的效果。

![四格美妆编辑拼贴画](https://cms-assets.youmind.com/media/1769582011824_sem074_G_qWFmJbgAAiLrG.jpg)
![四格美妆编辑拼贴画](https://cms-assets.youmind.com/media/1769582011842_1m811d_G_qWHdIbAAIfFpc.jpg)

```
{
  "prompt_type": "beauty_editorial_collage",
  "layout": {
    "structure": "4-panel split-screen grid",
    "dividers": "Thick white diagonal borders",
    "style": "Modern magazine spread aesthetic"
  },
  "subject": {
    "demographic": "Young woman",
    "aesthetic": "Clean girl / K-beauty influence",
    "features": {
      "skin": "Flawless, dewy, 'glass skin' texture, high luminosity",
      "hair": "{argument name="hair style" default="Short brown bob cut with wispy bangs, smooth texture"}",
      "eyes": "Soft grey/hazel contacts"
    }
  },
  "makeup": {
    "style": "No-makeup makeup look",
    "details": [
      "Soft rosy blush high on cheeks",
      "Glossy pink lip tint",
      "Groomed natural fluffy brows",
      "Subtle mascara"
    ]
  },
  "attire_and_accessories": {
    "headwear": "Brown houndstooth pattern newsboy cap (Baker boy hat)",
    "jewelry": "Small delicate gold butterfly stud earrings, thin gold chain necklace"
  },
  "panel_composition": {
    "top_left": "Close-up 3/4 angle, focus on cheek highlight and earring",
    "top_right": "Direct front-facing portrait, symmetrical composition",
    "bottom_left": "Portrait with hat, 3/4 turn, looking at camera",
    "bottom_right": "Extreme close-up side profile, cropping into face"
  },
  "technical_specs": {
    "resolution": "8K",
    "lighting": "Soft commercial studio lighting, ring light reflection in eyes",
    "color_grading": "Desaturated background, warm skin tones, high contrast",
    "style": "High-end beauty photography, hyper-realistic"
  }
}
```

[[Studio Lighting]] [[8K Photography]]

---

### 136. 身着纱丽的超逼真南亚女性肖像

**Author**: [Shreya♡](https://x.com/Shreyayadav)  **Date**: 2026-01-27  **Language**: en

> 一个为 Nano Banana Pro 制作的详尽 JSON 提示词，通过 Gemini 生成，旨在创建一张超逼真的 4K 肖像，描绘一位年轻、曲线优美的南亚女性，身着深粉色缎面纱丽。该提示词细致地描述了人物特征（丰满体型、蓬松卷发、柔和自信的微笑）、姿势（回眸）、服装（露背上衣、逼真的缎面垂坠感）、电影级摄影棚灯光以及相机设置（85mm 镜头、f/1.8 光圈、浅景深），以期获得高质量、优雅、经典的超写实图像。

![身着纱丽的超逼真南亚女性肖像](https://cms-assets.youmind.com/media/1769582039648_l9kurk_G_qC0iYXQAANqqt.jpg)
![身着纱丽的超逼真南亚女性肖像](https://cms-assets.youmind.com/media/1769582039529_7y3ajz_G_qC0j0XQAAwlrW.jpg)
![身着纱丽的超逼真南亚女性肖像](https://cms-assets.youmind.com/media/1769582040100_v9jr7p_G_qC0b_bcAAhg7_.jpg)

```
{
  "image_format": {
    "resolution": "4K UHD",
    "aspect_ratio": "2:3",
    "orientation": "portrait",
    "render_quality": "ultra-realistic",
    "detail_level": "extreme micro-detail, skin texture visible"
  },

  "subject": {
    "gender": "female",
    "ethnicity": "South Asian",
    "age_range": "young adult",
    "body_type": "chubby, curvy, plus-looking physique with soft natural proportions",
    "beauty_description": "beautiful, elegant, confident presence",
    "facial_features": {
      "face_structure": "same face structure as reference",
      "expression": "soft confident smile",
      "eyes": "expressive, warm gaze directed toward camera",
      "skin_tone": "smooth South Asian complexion with natural glow"
    },
    "hair": {
      "style": "voluminous curled hairstyle",
      "length": "long",
      "texture": "soft, bouncy curls with natural shine",
      "movement": "light natural flow, realistic curl definition"
    }
  },

  "pose_and_body_language": {
    "pose": "over-the-shoulder pose",
    "body_orientation": "body slightly turned away from camera",
    "head_position": "head turned back toward camera",
    "expression_mood": "calm, confident, graceful",
    "posture": "relaxed yet poised, natural curves emphasized subtly"
  },

  "clothing_and_fabric": {
    "outfit_type": "traditional saree",
    "saree": {
      "color": "{argument name="saree color" default="deep pink"}",
      "material": "satin",
      "fabric_behavior": "smooth, glossy, soft folds with realistic drape",
      "texture_detail": "highly detailed satin reflections and fabric flow"
    },
    "blouse": {
      "design": "fully open-back blouse",
      "closure": "tied only with thin strings",
      "exposure": "reveals natural back shape tastefully",
      "fabric": "matching satin with smooth finish"
    }
  },

  "lighting": {
    "style": "cinematic studio lighting",
    "key_light": "soft diffused light highlighting skin and fabric",
    "fill_light": "gentle fill to maintain facial softness",
    "rim_light": "subtle rim light outlining hair curls and shoulders",
    "mood": "warm, elegant, intimate yet classy"
  },

  "camera": {
    "camera_type": "full-frame DSLR or mirrorless",
    "lens": "85mm portrait lens",
    "aperture": "f/1.8",
    "focus": "sharp focus on face and eyes",
    "depth_of_field": "shallow background blur (bokeh)",
    "angle": "slightly elevated eye-level portrait angle"
  },

  "background": {
    "environment": "minimal, softly blurred backdrop",
    "color_palette": "neutral warm tones to complement deep pink saree",
    "distractions": "none",
    "depth": "smooth bokeh separation"
  },

  "rendering_and_post_processing": {
    "skin_detail": "natural pores, realistic highlights, no plastic skin",
    "color_grading": "cinematic warm tones",
    "contrast": "balanced contrast with soft highlights",
    "sharpness": "high clarity without over-sharpening",
    "realism": "photorealistic, lifelike presence"
  }
}
```

[[Studio Lighting]] [[85mm Lens Portrait]] [[Ultra-Realistic Portrait]]

---

### 137. 萨曼莎·露丝黑白时尚大片

**Author**: [ShaHid WaNii](https://x.com/meng_dagg695)  **Date**: 2026-01-26  **Language**: en

> 一个高度详细的 JSON 提示，用于生成萨曼莎·鲁斯 (Samantha Ruth) 的 8K 高分辨率影棚时尚肖像。它详细说明了她的姿势、发型、妆容和服装（黑白条纹两件套），强调了影棚灯光、清晰的焦点以及在纯黑色背景下的现代编辑美学。

![萨曼莎·露丝黑白时尚大片](https://cms-assets.youmind.com/media/1769495356326_lwj4jw_G_laDdlaIAAz5cR.jpg)
![萨曼莎·露丝黑白时尚大片](https://cms-assets.youmind.com/media/1769495356410_9zw7t7_G_laDdoaUAANjSg.jpg)
![萨曼莎·露丝黑白时尚大片](https://cms-assets.youmind.com/media/1769495356466_00f3sa_G_laDdMaAAARJUc.jpg)

```
{
  "image_type": "high-resolution studio fashion portrait",
  "aspect_ratio": "3:4",
  "resolution": "8K",
  "subject": {
    "gender_presentation": "female",
    "age_range_visible": "young adult",
    "pose": {
      "body_position": "seated or slightly reclined",
      "upper_body": "torso angled slightly to the right",
      "head": "tilted slightly left",
      "left_arm": "raised with hand touching hair near the head",
      "right_arm": "bent with hand resting near the waist/hip"
    },
    "expression": {
      "face": "neutral to confident",
      "lips": "slightly parted",
      "gaze_direction": "looking directly at camera"
    }
  },
  "face_and_head": {
    "skin_tone": "light to medium",
    "skin_texture": "smooth, evenly lit",
    "makeup": {
      "base": "matte, even complexion",
      "eyes": "defined eyebrows, subtle eyeshadow",
      "lips": "soft nude-pink lipstick"
    },
    "hair": {
      "color": "dark brown with warm highlights",
      "length": "short to medium",
      "style": "wavy, voluminous, slightly tousled",
      "parting": "side-parted"
    }
  },
  "eyewear": {
    "type": "round sunglasses",
    "lens_color": "dark green tint",
    "frame": {
      "material": "metal",
      "color": "gold",
      "thickness": "thin"
    }
  },
  "jewelry_and_accessories": {
    "earrings": {
      "material": "metal",
      "color": "gold",
      "style": "long, geometric, drop-style"
    },
    "bracelet": {
      "wrist": "left",
      "material": "metal",
      "color": "gold",
      "style": "chain bracelet"
    }
  },
  "clothing": {
    "outfit_type": "two-piece set",
    "top": {
      "style": "long-sleeve crop top",
      "design": "front knot/twist at bust",
      "pattern": "bold {argument name="pattern color" default="black and white"} stripes",
      "sleeves": "loose fit, cuffed at wrist"
    },
    "bottom": {
      "style": "high-waisted skirt",
      "length_visible": "above knee (partially visible)",
      "pattern": "matching black and white stripes",
      "waist_detail": "front tie or folded fabric detail"
    }
  },
  "body_details": {
    "midriff": "visible",
    "posture": "relaxed yet confident",
    "proportions": "slim, well-balanced"
  },
  "lighting": {
    "type": "studio lighting",
    "direction": "soft frontal with slight side emphasis",
    "contrast": "moderate to high",
    "highlights": "face, collarbone, midriff",
    "shadows": "soft, controlled"
  },
  "background": {
    "color": "solid black",
    "texture": "smooth, non-distracting",
    "environment": "studio setting"
  },
  "color_palette": [
    "black",
    "white",
    "gold",
    "warm skin tones",
    "dark green"
  ],
  "overall_style": {
    "aesthetic": "modern fashion editorial",
    "mood": "bold, confident, polished",
    "finish": "clean, sharp, high-detail"
  },
  "camera_and_quality": {
    "camera_angle": "eye-level",
    "focus": "sharp on subject",
    "depth_of_field": "shallow to moderat
```

[[Studio Lighting]] [[Pure Black Background]]

---

### 138. 超写实肖像画，画中包含主体画像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-26  **Language**: en

> 生成一张超现实、电影感的 8K 肖像画的提示，画中主体（一位年轻男子）站在画架旁。画架上的画布上有一幅主体身着相同服装的逼真画作，在温暖的摄影棚灯光下营造出一种元艺术构图。

![超写实肖像画，画中包含主体画像](https://cms-assets.youmind.com/media/1769495311929_o5q89j_G_lScrRaMAAmuMK.jpg)

```
A hyper-realistic, cinematic 8K portrait of the same young man standing gracefully beside an easel with a large canvas. On the canvas is a stunning, photorealistic painting of herself, perfectly capturing his beauty, wearing the same dress as in real life. She proudly presents the artwork with a soft, confident expression. Studio lighting casts a warm glow, highlighting both her real face and the painted portrait. The composition is elegant, ultra-detailed, masterpiece quality, with perfect photorealism. Aspect ratio 9:16.
```

[[Studio Lighting]] [[8K Cinematic Portrait]]

---

### 139. 4K 超逼真复古时尚杂志肖像

**Author**: [Milo](https://x.com/Milo_Bahi_02)  **Date**: 2026-01-25  **Language**: en

> 一个为 Nano Banana Pro 设计的详细长提示，用于生成一张 4K 超现实复古时尚杂志风格的宣传图片。主体是一位身穿复古无袖连衣裙的模特，裙子印有大芒果图案，配有白色衣领，并搭配一顶装饰有苹果图案和粉色玫瑰的红色帽子。提示中指定了优雅的姿势、自信的表情、红色口红、经典复古波浪发型、影棚灯光、超现实细节以及在纯白色背景下的超现实水果造型。

![4K 超逼真复古时尚杂志肖像](https://cms-assets.youmind.com/media/1769408703928_1y9bbw_G_e-urvWsAAP8nJ.jpg)

```
Nano Banana Pro || 4K Ultra-Realistic Promotional, a retro inspired fashion editorial portrait of a Boy against a soft beige background. She is wearing a vintage style sleeveless Apple dress with a white collar like a scarf detail, and big mango prints. On her head, a decorative big Red hat with two big Apple prints and Pink roses wrapped around the hat’s rim. He is holding the juice pack from the reference image near her lips. Elegant pose, confident expression, red lipstick, softly curled hair styled in a classic retro wave. Clean white background, studio lighting, smooth skin texture, vibrant yet balanced color palette, sharp focus, high fashion advertising photography, surreal fruit styling, ultra detailed, cinematic lighting, professional product shoot, hyper realistic, 4K quality and image size 4 5.
```

[[Studio Lighting]]

---

### 140. 微缩透视模型：从参考场景重建

**Author**: [Ege](https://x.com/egeberkina)  **Date**: 2026-01-24  **Language**: en

> 这是一个高度详细的结构化提示，旨在将提供的参考图像转换为一个干净、收藏品级的微缩立体模型。它为构图、物体放置、照明（柔和的影棚灯光）和材质美学规定了精确的规则，以确保微缩模型忠实地保留原始场景的空间关系。

![微缩透视模型：从参考场景重建](https://cms-assets.youmind.com/media/1769322275327_svbnzz_G_cpmGmWEAALSJq.jpg)
![微缩透视模型：从参考场景重建](https://cms-assets.youmind.com/media/1769322275246_7gb9dp_G_cpleCXgAAoBhN.jpg)
![微缩透视模型：从参考场景重建](https://cms-assets.youmind.com/media/1769322275406_q16160_G_cpmubWgAA9u7S.jpg)
![微缩透视模型：从参考场景重建](https://cms-assets.youmind.com/media/1769322276466_xpbitl_G_cpncVWEAE7w9m.jpg)

```
{
 "reference_images": {
 "scene_reference": "ATTACHED_IMAGE",
 "usage_rule": "Use this image as the sole and exact source for scene layout, object placement, and composition. Do not reinterpret or replace the scene."
 },

 "concept": {
 "type": "miniature diorama reconstruction",
 "intent": "Rebuild the attached scene as a clean, collectible-scale diorama while preserving the original spatial relationships"
 },

 "environment": {
 "scale": "tabletop miniature",
 "ground": {
 "type": "sculpted base",
 "behavior": "supports all objects naturally without enclosure",
 "edges": "clean, minimal, slightly beveled"
 },
 "background": {
 "type": "seamless studio backdrop",
 "color": "pure white",
 "constraint": "no environment beyond the diorama base"
 }
 },

 "objects_and_elements": {
 "layout_rule": "All objects must remain in the same relative positions as in the reference image",
 "primary_elements": "exact vehicles, structures, props, and terrain visible in the reference",
 "detail_handling": "simplified but faithful miniature proportions",
 "characters": {
 "presence": "only if present in the reference",
 "style": "miniature figurines, no facial realism"
 }
 },

 "composition": {
 "view": "isometric or slightly elevated 3/4 perspective",
 "framing": "entire diorama visible, centered",
 "cropping": "no zoom, no cinematic crop"
 },

 "camera": {
 "lens_equivalent": "35mm–50mm",
 "perspective": "miniature realism",
 "distortion": "none"
 },

 "lighting": {
 "type": "soft studio lighting",
 "direction": "overhead and slightly angled",
 "shadows": "subtle contact shadows only beneath objects",
 "avoid": [
 "dramatic lighting",
 "spotlights",
 "cinematic contrast"
 ]
 },

 "materials_and_style": {
 "surface_finish": "smooth, matte or lightly satin",
 "material_quality": "high-quality scale model materials",
 "aesthetic": "clean, modern, premium diorama"
 },

 "quality_controls": {
 "image_clarity": "ultra-clean",
 "grain": "none",
 "noise": "none",
 "motion_blur": "none"
 },

 "negative_prompts": [
 "glass case",
 "display box",
 "museum enclosure",
 "transparent cube",
 "protective casing",
 "reflections on glass",
 "labels or plaques",
 "text overlays",
 "busy background",
 "cinematic blur"
 ]
}
```

[[Studio Lighting]]

---

### 141. 电影级时尚杂志人像摄影，保留人物特质

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-01-24  **Language**: en

> 一个复杂的 JSON 提示，用于生成超现实、电影级的时尚编辑肖像。其核心功能是严格的身份保留，要求 AI 在将主体置于新场景（坐在现代扶手椅上）、具有特定影棚灯光和服装细节的同时，保持上传参考图像中精确的面部特征、发型和身体比例。

![电影级时尚杂志人像摄影，保留人物特质](https://cms-assets.youmind.com/media/1769322359579_h3a7cz_G_bV0DBasAAxqVu.jpg)

```
{
  "type": "image_generation_prompt",
  "aspect_ratio": "4:5",
  "quality": "ultra-realistic",
  "style": "cinematic fashion editorial",
  "identity_preservation": {
    "use_reference_image": true,
    "strict_identity_lock": true,
    "notes": "Maintain the exact real face, facial structure, hairstyle, skin tone, body proportions, and overall identity of the woman from the uploaded reference image. No alterations or beautification."
  },
  "subject": {
    "gender": "female",
    "pose": {
      "position": "sitting on a modern beige armchair with wooden legs",
      "posture": "leaning slightly forward",
      "hands": "hands gently together in front, relaxed and confident"
    },
    "expression": "intense, confident gaze directed at the camera",
    "appearance": {
      "hair": "same hairstyle as reference image, unchanged",
      "skin_tone": "same natural skin tone as reference image",
      "face": "exact facial features preserved"
    },
    "outfit": {
      "top": "{argument name="top description" default="dark navy blue fitted blouse or dress shirt with top buttons slightly open"}",
      "bottom": "light beige slim-fit pants",
      "footwear": "black loafers with tan soles"
    }
  },
  "environment": {
    "background": {
      "color": "light gray",
      "style": "minimalist smooth gradient"
    }
  },
  "lighting": {
    "type": "soft natural studio lighting",
    "quality": "evenly lit",
    "effect": "subtle shadows for depth and realism"
  },
  "camera": {
    "lens": "50mm",
    "aperture": "f/2.8",
    "framing": "vertical",
    "composition": "full-body",
    "depth_of_field": "shallow to moderate"
  },
  "mood": {
    "tone": "confident, elegant, cinematic",
    "aesthetic": "high-end fashion editorial"
  },
  "rendering": {
    "detail_level": "fine details in skin texture, fabric, and furniture",
    "realism": "high realism, no CGI or illustration look"
  },
  "constraints": [
    "Do not change face or facial structure",
    "Do not change hairstyle",
    "No artificial beauty filters",
    "No cartoon or stylized effects",
    "No text or watermark"
  ],
  "output_goal": "Create a high-end cinematic studio portrait of a confident woman seated on a modern armchair, preserving her exact identity from the reference image with realistic lighting and editorial fashion aesthetics."
}
```

[[Studio Lighting]] [[Editorial Photography]]

---

### 142. 光泽亮片手势肖像

**Author**: [ShaHid WaNii](https://x.com/meng_dagg695)  **Date**: 2026-01-24  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张 8K 超高清特写肖像，描绘一位身穿白色亮片露背连衣裙的女性，强调光泽的皮肤纹理、柔和的影棚灯光，以及她右手扶额的特定姿势。

![光泽亮片手势肖像](https://cms-assets.youmind.com/media/1769322273348_7ubcal_G_bG4-6bMAAqAEg.jpg)
![光泽亮片手势肖像](https://cms-assets.youmind.com/media/1769322273325_ihizrv_G_bG4-4bQAA2C7k.jpg)
![光泽亮片手势肖像](https://cms-assets.youmind.com/media/1769322273405_2422ca_G_bG4-qWYAAc-QX.jpg)

```
{
  "image_type": "photorealistic portrait",
  "resolution_target": "8K ultra HD",
  "aspect_ratio": "3:4",
  "camera_framing": {
    "shot_type": "medium close-up",
    "crop": "from upper chest to slightly above head",
    "orientation": "vertical"
  },
  "subject": {
    "gender_presentation": "female",
    "age_appearance": "adult",
    "skin_tone": "fair with warm undertones",
    "skin_texture": "smooth, glossy, reflective highlights visible on forehead, cheeks, nose, and chin",
    "facial_expression": "neutral to soft-serious, calm and composed",
    "gaze_direction": "looking directly toward the camera",
    "head_position": "slightly tilted, upright posture"
  },
  "face_details": {
    "forehead": "smooth with visible sheen",
    "eyebrows": "dark brown, well-shaped, symmetrical",
    "eyes": {
      "color": "hazel-green",
      "shape": "almond-shaped",
      "eyelashes": "long and defined",
      "eye_makeup": "subtle, natural-toned"
    },
    "nose": "straight, proportionate",
    "lips": {
      "shape": "full",
      "finish": "glossy",
      "color": "soft pink"
    },
    "cheeks": "soft blush visible",
    "jawline": "smooth and defined"
  },
  "hair": {
    "color": "dark brown",
    "style": "pulled back into a low ponytail or tied-back style",
    "loose_strands": "few fine strands visible near face",
    "texture": "smooth with slight natural movement"
  },
  "pose": {
    "arm_position": "right arm raised",
    "hand_position": "right hand resting on forehead",
    "fingers": "relaxed, natural curvature",
    "shoulders": "relaxed, slightly angled"
  },
  "clothing": {
    "garment_type": "sleeveless halter-neck dress",
    "color": "{argument name="dress color" default="white"}",
    "material": "fabric densely covered with reflective sequins or crystal embellishments",
    "pattern": "uniformly distributed reflective elements",
    "neckline": "high neck",
    "fit": "fitted and elegant"
  },
  "accessories": {
    "earrings": {
      "type": "dangling",
      "material": "silver-toned with gemstone-like elements",
      "length": "medium length"
    },
    "bracelet": {
      "wrist": "right",
      "material": "silver-toned",
      "design": "thin chain style"
    }
  },
  "lighting": {
    "type": "soft studio lighting",
    "key_light": "front-facing, diffused",
    "highlights": "strong glossy highlights on skin and dress embellishments",
    "shadow_style": "soft, minimal harsh shadows"
  },
  "background": {
    "setting": "indoor",
    "color_palette": "warm gold and beige tones",
    "elements": "soft curtains or drapery",
    "focus": "blurred (bokeh effect)",
    "contrast_with_subject": "subject sharply separated from background"
  },
  "color_grading": {
    "overall_tone": "warm",
    "contrast": "moderate",
    "saturation": "natural with enhanced highlights"
  },
  "image_style": {
    "realism_level": "highly photorealistic",
    "finish": "AI-enhanced, polished look",
    "det"
  }
}
```

[[Studio Lighting]] [[Close-Up Portrait]] [[8K Ultra HD]]

---

### 143. 数字纸艺青年男子肖像

**Author**: [Mohamed IDBRAHIM](https://x.com/brightcoding)  **Date**: 2026-01-23  **Language**: en

> 此提示用于生成一张超精细的年轻男子数字纸艺肖像，采用几何低多边形纸雕风格。它着重于逼真的纸张纹理、锐利的边缘以及皮肤和头发的暖棕色调，从而呈现出一种具有专业影棚照明的现代艺术雕塑美学。

![数字纸艺青年男子肖像](https://cms-assets.youmind.com/media/1769236048305_6anbbp_G_YjdHiWEAA_dIK.jpg)

```
Ultra-detailed HD digital papercraft portrait of a young man, geometric low-poly paper sculpture style, layered folded paper shapes forming the face and hair, warm {argument name="paper color" default="brown"} paper tones for skin and hair, subtle beard and mustache, thin round glasses, soft confident smile, highly realistic paper texture, sharp edges and clean folds, studio lighting, soft shadows, centered composition, {argument name="background style" default="white minimal background"}, modern art sculpture look, hyper-clear focus, 4K resolution, high contrast, professional art render
```

[[Studio Lighting]]

---

### 144. 时尚社论肖像：现代沙发提示

**Author**: [Emma](https://x.com/emmagpt0)  **Date**: 2026-01-23  **Language**: en

> 一个详细的 JSON 提示，用于生成超高分辨率、逼真的时尚编辑肖像。它描绘了一位时尚女性坐在一张浅灰色现代沙发上，身穿红色格子迷你连衣裙、黑色西装外套和黑色透明丝袜。该提示指定了高角度全身拍摄，采用柔和的影棚灯光，强调高细节和锐利焦点，同时要求严格保留参考图像中的面部特征。

![时尚社论肖像：现代沙发提示](https://cms-assets.youmind.com/media/1769236002476_w185di_G_YM9gGXwAA1fqM.jpg)
![时尚社论肖像：现代沙发提示](https://cms-assets.youmind.com/media/1769236002488_4nyhhl_G_YNCGMXwAAJJjE.jpg)

```
{
  "description": "A stylish adult woman sitting on a light gray modern sofa in a contemporary living room, wearing a {argument name="dress pattern" default="red tartan"} mini dress, black blazer, sheer black tights, and black high heel stilettos. The pose is relaxed and elegant with legs extended and crossed, one arm resting on the sofa back and the other hand on the thigh. The environment is minimalistic with gray curtains, a beige carpet, a red retro table clock, and a brass table lamp in the background. Soft natural studio lighting, editorial fashion photography style, high detail, sharp focus.",
  
  "face_reference": "Use uploaded reference image for face only, do not modify facial structure or identity.",
  
  "camera": {
    "angle": "high-angle slightly tilted",
    "framing": "full body portrait",
    "lens": "35mm-50mm equivalent",
    "depth_of_field": "shallow to medium, background slightly blurred"
  },
  
  "lighting": {
    "type": "soft studio lighting",
    "mood": "natural daylight, low contrast",
    "shadows": "soft shadows, no harsh lighting"
  },
  
  "clothing": {
    "dress": {
      "color": "red",
      "pattern": "tartan plaid with black and white lines",
      "length": "mini",
      "fit": "slim fit, body-hugging"
    },
    "blazer": {
      "color": "black",
      "style": "fitted, single-button"
    },
    "tights": {
      "color": "black",
      "type": "sheer"
    },
    "shoes": {
      "type": "stiletto heels",
      "color": "black",
      "toe": "pointed",
      "detail": "slightly transparent toe panel"
    }
  },
  
  "environment": {
    "location": "modern living room",
    "sofa": "light gray fabric sofa",
    "curtains": "gray",
    "floor": "beige carpet",
    "props": [
      "red retro table clock",
      "brass table lamp with white shade"
    ]
  },
  "style": {
    "genre": "fashion editorial photography",
    "quality": "ultra high resolution, 8k detail",
    "realism": "photorealistic",
    "noise": "low",
    "sharpness": "high"
  },
  
  "negative_prompt": [
    "face modification",
    "blurry",
    "low resolution",
    "oversharpened",
    "extra limbs",
    "distorted body",
    "cartoon",
    "anime",
    "overexposed",
    "harsh shadows"
  ]
}
```

[[Studio Lighting]] [[Identity Locking]] [[Sheer Stockings]]

---

### 145. 皮克斯风格 3D 头像生成提示词

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-21  **Language**: en

> 一个根据上传图片创建高质量 3D 头像的提示。它指定了一个开朗、富有表现力、带着温暖笑容和柔和面部特征的脸庞，以皮克斯风格美学呈现，具有平滑的纹理、夸张的比例和柔和均匀的摄影棚灯光。

![皮克斯风格 3D 头像生成提示词](https://cms-assets.youmind.com/media/1769063180886_u3xh2g_G_M4AVcbQAEqSai.jpg)

```
Create a high-quality 3D avatar of the person in the uploaded image with a cheerful, expressive face. The character should have a warm smile, bright eyes, and soft facial features that feel friendly and approachable. Render in a Pixar-style aesthetic with smooth textures, subtle skin shading, and slightly exaggerated proportions for a cute, animated look. Lighting should be soft and even, creating a clean studio look with gentle shadows for depth.
```

[[Studio Lighting]] [[3D Rendering]] [[Warm Smile]]

---

### 146. 超现实极简主义法拉利平面广告

**Author**: [Guillermo Castellanos](https://x.com/guicastellanos1)  **Date**: 2026-01-21  **Language**: en

> 一个旨在以超现实极简主义风格重现豪华汽车平面广告的提示。主图像描绘了一辆法拉利的前脸被拉伸成细长的液态镀铬条纹，暗示着加速时时间被拉长。它强调了哑光白色画廊背景、大量的留白、影棚灯光和超清晰的 8K 分辨率，并包含了关于标志放置和两字标语的具体说明。

![超现实极简主义法拉利平面广告](https://cms-assets.youmind.com/media/1769063162956_nf4wh0_G_MKA0QXgAEMuJP.jpg)
![超现实极简主义法拉利平面广告](https://cms-assets.youmind.com/media/1769063162967_wdgacf_G_MKIfSWgAACmvA.jpg)
![超现实极简主义法拉利平面广告](https://cms-assets.youmind.com/media/1769063162985_j43d95_G_MKIfRWMAAvjKd.jpg)
![超现实极简主义法拉利平面广告](https://cms-assets.youmind.com/media/1769063163886_r34gzv_G_MKIfWW8AEJX6T.jpg)

```
FERRARI
Surreal minimalist photoreal print-ad. Hero: a Ferrari front fascia extruded into elongated streaks of liquid chrome metal, as if time stretched the vehicle mid-acceleration. One accent max. Matte white gallery background with massive negative space. Studio lighting, micro reflections, 8K ultra-sharp. Official Ferrari shield logo top-left (vector, accurate proportions, subtle ink texture). Two-word slogan bottom-right: “{argument name="slogan" default="Distort Speed"}”. No clutter, no watermark, no extra text.
```

[[Studio Lighting]] [[Negative Space]]

---

### 147. 低多边形风格的 3D 纸艺肖像

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-01-21  **Language**: en

> 一个用于生成高度精细的年轻男子 3D 纸艺肖像的提示。它强调低多边形美学，使用折叠和分层的纸张，带有锐利的几何折痕。调色板为中性色（棕褐色和棕色），并指定柔和的摄影棚灯光，以在纯白色背景下创建逼真的阴影和深度。此提示需要上传照片作为面部参考。

![低多边形风格的 3D 纸艺肖像](https://cms-assets.youmind.com/media/1769063161083_lgxhp8_G_LJvazaoAMIfPi.jpg)
![低多边形风格的 3D 纸艺肖像](https://cms-assets.youmind.com/media/1769063160998_rwcamc_G_LJvbBbIAAbJ3E.jpg)
![低多边形风格的 3D 纸艺肖像](https://cms-assets.youmind.com/media/1769063161024_1pty4g_G_LJva8bkAA__dj.jpg)
![低多边形风格的 3D 纸艺肖像](https://cms-assets.youmind.com/media/1769063162449_hr2rp4_G_LJvbAaoAUDtiw.jpg)

```
A highly detailed 3D paper-craft portrait of a young man with uploaded photo same face with curly brown hair and glasses. The artwork should be made entirely of folded and layered paper, featuring sharp geometric creases and a low-poly aesthetic. The man has a gentle smile and light facial hair stubble. Use a neutral color palette with tan and brown tones for the face and hair, and a crisp white textured paper for his shirt. Soft studio lighting to create realistic shadows, giving it a 3D depth against a plain white background.
```

[[Studio Lighting]]

---

### 148. 橙子切片与牛奶的微距飞溅摄影

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-20  **Language**: en

> 一个用于生成超逼真商业飞溅摄影的详细提示。它侧重于橙子片落入溅起的牛奶中，捕捉浓稠、有光泽的牛奶飞溅形成冠状曲线，在干净的蓝色影棚背景下凝固在半空中。

![橙子切片与牛奶的微距飞溅摄影](https://cms-assets.youmind.com/media/1768977256291_ia05hh_G_H1K-nWkBgY4u5.jpg)
![橙子切片与牛奶的微距飞溅摄影](https://cms-assets.youmind.com/media/1768977256267_9fbejr_G_H1LE1WkAA5Cr2.jpg)
![橙子切片与牛奶的微距飞溅摄影](https://cms-assets.youmind.com/media/1768977257662_hz6l2n_G_H1LA4WkAAOekg.jpg)
![橙子切片与牛奶的微距飞溅摄影](https://cms-assets.youmind.com/media/1768977258009_c6yvmz_G_H1LA4WkAc9Z5o.jpg)

```
"subject": {
    "primary": "Vibrant orange slices",
    "action": "Falling through the air toward rising milk",
    "secondary": "Thick, glossy white milk splash forming arcs and crown-like curves",
    "details": "Milk droplets frozen mid-air with creamy texture"
  },
  "environment": {
    "background": "Clean blue studio backdrop",
    "lighting": "Cinematic soft studio lighting with dramatic highlights and shadows"
  },
  "visual_style": {
    "genre": "Ultra-realistic commercial splash photography",
    "textures": "High-detail creamy milk and fresh citrus pulp",
    "motion": "Frozen action, high-speed capture",
    "depth_of_field": "Shallow depth of field"
  },
  "camera": {
    "lens": "85mm macro",
    "framing": "Wide composition",
    "focus": "Sharp focus on splash and fruit"
  },
  "composition": {
    "aspect_ratio": "3:4",
    "color_palette": ["Vibrant Orange", "Pure White", "Clean Blue"]
  },
  "quality": {
    "detail_level": "Ultra-high detail",
    "rendering": "Photorealistic"
  },
  "profile": "9ewnbdc"
```

[[Studio Lighting]] [[Macro Photography]] [[Commercial Food Photography]] [[High Speed Photography]]

---

### 149. 芬达番石榴汽水罐爆炸产品图

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-20  **Language**: en

> 生成一张超逼真、高端产品广告图片的提示词。画面中，一个红色铝制汽水罐猛烈爆裂，粉红色的番石榴汁、整个番石榴和切片番石榴在凝固的瞬间迸发而出。提示词强调戏剧性的影棚灯光、冷凝水珠和商业广告品质。

![芬达番石榴汽水罐爆炸产品图](https://cms-assets.youmind.com/media/1768977271845_anitgg_G_Hh_hkWYAMkgeW.jpg)
![芬达番石榴汽水罐爆炸产品图](https://cms-assets.youmind.com/media/1768977271869_jok0by_G_Hh9x9XAAAQQXm.jpg)
![芬达番石榴汽水罐爆炸产品图](https://cms-assets.youmind.com/media/1768977271993_o0rb4k_G_Hh9NTW0AIa939.jpg)
![芬达番石榴汽水罐爆炸产品图](https://cms-assets.youmind.com/media/1768977272922_ebdke7_G_Hh-qbW0AA9Xw7.jpg)

```
Ultra-realistic high-end product photography of a red aluminum soda can branded “{argument name="soda brand" default="Fanta Goiaba"},” positioned upright at center frame and violently split open vertically down the middle, the torn metal edges sharp and jagged, with vivid pink guava juice bursting outward in dynamic frozen motion. Fresh whole guavas and thick guava slices with green skin and pink flesh explode upward and outward from inside the can, interspersed with glossy green leaves, all suspended mid-air.

The can surface is covered in fine condensation droplets, highly detailed metallic texture with realistic reflections.

Bright red guava liquid splashes arc dramatically around the composition, droplets frozen crisply. Shot in a controlled studio environment with a seamless warm red background and matching surface, monochromatic color harmony dominated by reds, greens, and pinks. Lighting is dramatic studio lighting with a strong frontal key light and soft fill, creating sharp highlights,defined shadows, and high contrast while maintaining clean product clarity. Camera angle is straight-on at eye level with a slight close-up crop, shallow depth of field but sharp focus on the can and fruit, cinematic realism, commercial advertising quality, hyper-detailed, photorealistic, 8K, ultra-sharp, premium beverage ad aesthetic
```

[[Studio Lighting]] [[Commercial Photography]] [[Beverage Product Photography]] [[High Speed Photography]]

---

### 150. 动态美食广告，尽享风味浪潮

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-20  **Language**: en

> 一个用于生成高分辨率商业美食照片的提示，照片中包含一个动态的“风味波浪”构图，从指定的食物中向外迸发。该提示强调了色彩斑斓的能量丝带、薄雾、运动轨迹、超真实的纹理以及干净、高调的影棚照明。

![动态美食广告，尽享风味浪潮](https://cms-assets.youmind.com/media/1768977278865_vwce20_G_Hfzv3XwAIDUnS.jpg)
![动态美食广告，尽享风味浪潮](https://cms-assets.youmind.com/media/1768977278826_uqnefi_G_HfzycXkAAaICY.jpg)
![动态美食广告，尽享风味浪潮](https://cms-assets.youmind.com/media/1768977278912_oue3pb_G_HfzyaWgAAqFXQ.jpg)
![动态美食广告，尽享风味浪潮](https://cms-assets.youmind.com/media/1768977280102_cvwysp_G_Hfz0lWkAAHgMv.jpg)

```
Dynamic flavor wave composition of {argument name="food item" default="[FOOD]"}, with colorful energy ribbons, mist, and motion streaks bursting outward to represent taste intensity. Ingredient silhouettes embedded within the waves. Clean minimal white background, high-key studio lighting. Ultra-real textures, cinematic motion blur, premium commercial food photography, 8K resolution.
```

[[Studio Lighting]] [[Commercial Photography]] [[Food Photography]]

---

### 151. 极简超现实产品广告静物摄影提示

**Author**: [Keskin](https://x.com/craftian_keskin)  **Date**: 2026-01-20  **Language**: en

> 一个高度具体的提示，用于生成一张超现实、极简主义的广告静物图像，为虚构的安眠药“PILLow”设计。它描述了一个超大的琥珀色玻璃瓶，将微型绗缝枕头洒在哑光蓝色表面上，强调构图、影棚灯光和现代商业美学。

![极简超现实产品广告静物摄影提示](https://cms-assets.youmind.com/media/1768977283648_bqm8ww_G_HRRTiXwAAN5dy.jpg)

```
Minimalist advertising still life featuring an oversized amber glass supplement bottle tipped on its side, open black cap placed nearby. The bottle label reads “{argument name="label text" default="Use for Charging"}” in clean modern typography. From the bottle opening, several small white pillows spill out onto a smooth matte blue surface, arranged organically as if poured.

The pillows are soft, rectangular, quilted, and plush, resembling miniature ergonomic bed pillows. Strong visual contrast between the dark amber glass, crisp white pillows, and muted blue background.

Composition: top-down / three-quarter angle product shot, bottle positioned in the upper left, pillows scattered diagonally across the frame toward the lower right. Clear negative space at the bottom for branding text "PILLow".

Lighting: studio lighting with soft directional shadows, high clarity, subtle reflections on glass, controlled highlights.
Style: modern commercial product photography, surreal conceptual advertising aesthetic.
Color palette: deep blue background, warm amber glass, white textiles, black accents.
Mood: calm, clever, restful, contemporary.
Quality cues: ultra-sharp focus, high resolution, professional advertising campaign look.

Optional Negative Prompt

cluttered scene, harsh lighting, plastic texture, low contrast, messy shadows, distorted text, unrealistic materials
```

[[Studio Lighting]] [[Concept Art]] [[Still Life Photography]]

---

### 152. 身着 DeepSeek 服装的超写实亚洲女性模特提示词

**Author**: [清风徐来028](https://x.com/onlyhuman028)  **Date**: 2026-01-20  **Language**: zh

> 一张高度写实的照片，描绘一位年轻、优雅的亚洲女性，她留着乌黑的长发，身穿白色长袖露脐上衣（印有大大的蓝色“DeepSeek”标志）和红色运动裤。图像采用强烈的侧面柔和光线，以纯黑色背景为衬托，突出身体曲线和面部轮廓，营造出高写实、极简主义且对比强烈的审美效果。

![身着 DeepSeek 服装的超写实亚洲女性模特提示词](https://cms-assets.youmind.com/media/1768977347071_12l3bo_G_HMQiqWwAEqNGt.jpg)

```
一位精致的年轻亚洲女性（图1），留着黑色长发，身穿白色长袖露脐修身短装（胸口印着蓝色的大“{argument name="品牌名称" default="DeepSeek"}” ）及红色运动裤。她在纯黑色背景前侧身而立，1只手轻托脑后，另一只手的食指竖在唇边，展现出自信而迷人的神态，看着镜头。画面运用侧向柔光，细腻地勾勒出人物的身体曲线和面部轮廓，明暗对比强烈，具有极高的写实摄影质感和极简主义美学。 16:9
```

[[Studio Lighting]] [[Fashion Portrait]] [[High Contrast Portrait]]

---

### 153. 发型变化编辑美容拼贴

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-01-20  **Language**: en

> 一个旨在生成 4x3 网格编辑美容拼贴的提示，在保持所有面板中完美的面部一致性和表情的同时，展示同一主体多种发型变化。它指定了柔和的影棚灯光、中性背景和高端编辑质量，非常适合在参考图像上测试不同的造型。

![发型变化编辑美容拼贴](https://cms-assets.youmind.com/media/1768977334297_5h091x_G_F7MyNWIAAnC0B.jpg)

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
    "sleek long straight hair",
    "high ponytail",
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

[[Studio Lighting]] [[Face Consistency]] [[Beauty Editorial]] [[Grid Collage]]

---

### 154. 沙龙自拍，身穿露脐足球衫提示

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-20  **Language**: en

> 一个高度具体的 JSON 提示，用于生成一张超现实的女性在豪华发廊自拍的图像。该提示详细描述了她的外貌（金发、诱惑的表情、带有金色闪粉的戏剧性妆容）和挑逗性的服装（极短的粉色足球衫、紧身破洞牛仔裤），强调了特定的身体特征和戏剧性的影棚灯光。

![沙龙自拍，身穿露脐足球衫提示](https://cms-assets.youmind.com/media/1768977288667_ocr0m1_G_FqhryXAAAOYMJ.jpg)

```
{
  "subject": {
    "type": "woman",
    "ethnicity": "western",
    "
    "hair": {
      "color": "blonde",
      "length": "long",
      "style": "loose"
    },
    "skin": "fair",
    "facial_features": "same as reference image",
    "makeup": {
      "style": "dramatic",
      "details": {
        "golden_glitter_dots": "cheekbones",
        "winged_eyeliner": "sharp",
        "lips": "full, glossy dark red"
      }
    },
    "expression": "seductive"
  },
  "pose": {
    "action": "taking a selfie",
    "camera": "Canon, right hand",
    "left_hand": "touching hair",
    "body_position": "dynamic"
  },
  "clothing": {
    "top": {
      "type": "cropped soccer jersey",
      "color": "{argument name="jersey color" default="pink"}",
      "stripes": "green and red",
      "logo": "Moroccan national team",
      "sponsor": "PUMA",
      "custom_text": "AMUQ",
      "fit": "extremely low-cropped, showing underboob"
    },
    "necklace": "heart-shaped pendant",
    "bracelets": "gold",
    "jeans": {
      "style": "high-waisted skinny",
      "color": "light blue",
      "details": "ripped",
      "fit": "tight, hugging massive curvy hips and thick thighs"
    },
    "tattoos": "small tattoo on arm"
  },
  "environment": {
    "location": "modern luxury hair salon",
    "background": "black leather salon chairs",
    "lighting": {
      "type": "bright ring light and professional studio lighting",
      "effects": "strong rim light, lens flare",
      "mood": "dark dramatic, cinematic"
    }
  },
  "output": {
    "style": "hyper-realistic, photorealistic",
    "resolution": "8k",
    "skin_texture": "high detail"
  }
}
```

[[Studio Lighting]] [[Glamour Portrait]] [[Dramatic Makeup]]

---

### 155. 超逼真电影感社论肖像

**Author**: [Yaseen Khan Gul](https://x.com/YaseenK7212)  **Date**: 2026-01-19  **Language**: en

> 一个高度结构化的提示，用于生成一张超现实、杂志封面品质的特写肖像，灵感来自安娜·德·阿玛斯（Ana de Armas）。它详细描述了面部结构、服装（深红色两件套）、灯光（影棚电影级）和质感（发光肌肤带微妙油光）。

![超逼真电影感社论肖像](https://cms-assets.youmind.com/media/1768890639396_x3qhv0_G_CuvHCW8AAw9wx.jpg)
![超逼真电影感社论肖像](https://cms-assets.youmind.com/media/1768890639914_c93krt_G_CuvG9W8AA_dJT.jpg)
![超逼真电影感社论肖像](https://cms-assets.youmind.com/media/1768890639968_yz8y4s_G_CuvG7XIAARTNT.jpg)

```
{
  "type": "image_generation_prompt",
  "concept": {
    "description": "Hyper-realistic, magazine-cover-quality close-up portrait of a beautiful woman with features inspired by {argument name="celebrity inspiration" default="Ana de Armas"}",
    "intent": "High-fashion editorial photography with cinematic realism",
    "originality_note": "The subject is a look-alike inspired by Ana de Armas, not an exact replica"
  },
  "subject": {
    "gender": "female",
    "age_range": "early 30s",
    "ethnicity": "Latina / Cuban-Spanish inspired",
    "facial_features": {
      "structure": "soft oval face, elegant cheekbones, delicate jawline",
      "eyes": "large almond-shaped eyes, warm brown tone, relaxed eyelids",
      "lips": "full, natural lips slightly parted",
      "expression": "languid, calm, subtly seductive, relaxed confidence"
    },
    "body_visibility": {
      "framing": "close-up portrait extending below the waist",
      "posture": "upright but relaxed, natural editorial pose"
    }
  },
  "wardrobe": {
    "outfit_type": "two-piece outfit",
    "color": "deep vivid red",
    "top": {
      "style": "fitted, minimal, fashion-forward",
      "fabric": "smooth, slightly reflective material"
    },
    "bottom": {
      "style": "mini skirt",
      "fit": "form-fitting, modern cut",
      "visibility": "clearly visible below the waist"
    }
  },
  "skin_and_texture": {
    "skin_quality": "highly detailed, natural pores visible",
    "finish": "glossy, luminous",
    "effect": "subtle sweat or oil sheen on torso and chest, enhancing realism",
    "tone": "warm, healthy glow"
  },
  "hair_and_makeup": {
    "hair": {
      "style": "softly styled, loose waves",
      "color": "deep brown",
      "texture": "natural shine with slight movement"
    },
    "makeup": {
      "style": "editorial glamour",
      "details": "dewy skin, softly defined eyes, natural lips with slight gloss"
    }
  },
  "background": {
    "environment": "indoor setting",
    "primary_elements": [
      "desk or table surface",
      "stacks of papers"
    ],
    "paper_details": {
      "brightness": "partially bright white",
      "arrangement": "slightly messy, layered stacks",
      "focus": "softly blurred to maintain subject dominance"
    },
    "depth_of_field": "shallow, cinematic bokeh"
  },
  "lighting": {
    "style": "studio cinematic lighting",
    "key_light": "soft but directional, highlighting facial structure",
    "fill_light": "gentle fill to preserve skin detail",
    "highlights": "accentuated on glossy skin areas",
    "shadows": "soft, controlled, magazine-style contrast"
  },
  "camera": {
    "shot_type": "close-up portrait",
    "lens": "85mm prime lens",
    "aperture": "f/1.8",
    "focus": "tack-sharp on eyes",
    "sensor_quality": "full-frame, ultra-high resolution"
  },
  "style_and_quality": {
    "visual_style": [
      "hyper-realistic",
      "cinematic",
      "luxury fashion editorial",
```

[[Studio Lighting]] [[Fashion Editorial]] [[Celebrity Inspired Portrait]] [[Red Outfit]]

---

### 156. 超逼真高级时装爬行肖像

**Author**: [Anissa](https://x.com/SimplyAnnisa)  **Date**: 2026-01-19  **Language**: en

> 为 Nano Banana Pro 提供一个高度详细的提示，重点是生成一张超现实、高级时装的女性肖像，姿势低伏爬行，传达出掠夺性的张力。它强调皮肤纹理的极致真实感、自然的解剖结构、电影级的影棚布光（柔和主光、强烈轮廓光）以及具有精致面料和羽毛纹理的前卫时装。

![超逼真高级时装爬行肖像](https://cms-assets.youmind.com/media/1768890709710_4q0uuk_G_CqgkRXwAANPJ6.jpg)

```
Ultra-realistic high-fashion editorial portrait.
A young woman captured in a low, forward-leaning crawling pose, body set diagonally across the frame, conveying controlled dominance and predatory tension. One hand firmly grounded on the studio floor, fingers naturally spread under weight; the other hand lifted close to the face, forming a sharp, claw-like gesture that subtly frames the eyes without distortion.Her expression is seductive yet intimidating — half-lidded eyes with a heavy, deliberate gaze, lips slightly parted, facial muscles relaxed but intentional. Sharp facial structure rendered with natural proportions, visible bone definition, realistic asymmetry, and true skin texture: pores, micro-imperfections, soft tonal transitions, no artificial smoothing.
Long, straight hair with blunt bangs, slightly uneven and organic, glossy but not plastic, individual strands catching the light.
Avant-garde fashion styling: fitted pants with precise tailoring and believable fabric tension; arms wrapped in feathered or fur-textured elements showing individual fibers, irregular density, and tactile depth, clearly separated from skin.
Lighting: cinematic studio setup — soft key light from the upper front shaping facial planes, strong rim light from behind to carve the silhouette, deep controlled shadows with high contrast, no flat illumination.
Camera: fashion editorial perspective, 50–85mm look, shallow depth of field, sharp focus on eyes and hands, subtle falloff across the body.
Minimalist studio background with a dark gradient or solid tone, clean and distraction-free, enhancing the sculptural pose.
Overall mood: dark, glamorous, high-fashion Vogue editorial energy — powerful, sensual, intimidating, grounded in realism.
Extreme detail, photographic realism, natural anatomy, professional fashion editorial quality, 8K clarity.
--ar 9:16 --v 6 --style raw --s 250
🚫 NEGATIVE PROMPT:
extra fingers, fused or deformed hands, incorrect anatomy, distorted joints, exaggerated proportions, plastic skin, over-smoothed texture, flat lighting, low contrast, cartoon, anime, CGI look, blur, low detail, awkward or impossible pose
```

[[Studio Lighting]] [[Skin Texture Detail]]

---

### 157. 极简 3D 等距汽车展厅模型

**Author**: [Favori](https://x.com/favoriyuan)  **Date**: 2026-01-19  **Language**: en

> 一个用于生成简洁、极简主义 3D 等距建筑模型的提示。它指定了一个位于小屋结构内的汽车展厅，强调柔和的摄影棚灯光、逼真的材质、圆润的边缘以及中性背景下的高细节。

![极简 3D 等距汽车展厅模型](https://cms-assets.youmind.com/media/1768890674999_o1djn0_G_CbppYW0AEbevq.jpg)

```
A clean, minimalist 3D isometric model showcasing a [{argument name="location" default="car showroom"}], where [{argument name="display items" default="display items"}] are arranged within a [cabin structure], featuring subtle lighting accents, smooth floor surfaces, soft studio lighting, realistic materials, rounded edges, a miniature architectural style, high detail, and a neutral background.
```

[[Studio Lighting]]

---

### 158. 解构漂浮披萨静物提示词

**Author**: [𝘬𝘦𝘭𝘭𝘺](https://x.com/kelly00056)  **Date**: 2026-01-19  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超逼真的解构披萨构图美食摄影图像。它指定了白色盘子上方的多个漂浮层（披萨饼底、番茄、意大利辣香肠、奶酪片），强调了纹理、融化的奶酪滴落以及干净的影棚柔和照明，以呈现出诱人、具有编辑风格的外观。

![解构漂浮披萨静物提示词](https://cms-assets.youmind.com/media/1768890701347_q06yhd_G_CBrZIWEAAvD8q.jpg)
![解构漂浮披萨静物提示词](https://cms-assets.youmind.com/media/1768890701635_utl6zu_G_CBrZOW0AAJt1X.jpg)

```
{
  "scene_description": "A deconstructed floating pizza composition above a white plate",
  "foreground_objects": [
    {
      "type": "pizza_base",
      "position": "bottom",
      "appearance": {
        "crust": "thick, lightly browned",
        "sauce_visibility": "visible under tomato slices",
        "plate": "white ceramic, round"
      }
    },
    {
      "type": "tomato_slices",
      "quantity": "multiple",
      "position": "above pizza base",
      "appearance": {
        "color": "bright red",
        "thickness": "medium",
        "texture": "moist, glossy"
      }
    },
    {
      "type": "pepperoni_slices",
      "quantity": "many",
      "position": "floating above tomato layer",
      "appearance": {
        "color": "deep red",
        "texture": "smooth",
        "moisture": "slightly oily"
      }
    },
    {
      "type": "cheese_slice",
      "position": "floating between toppings",
      "appearance": {
        "color": "pale yellow",
        "melting": "edges dripping downward"
      }
    },
    {
      "type": "pizza_slice",
      "position": "top",
      "appearance": {
        "cheese": "melted, creamy, dripping",
        "crust": "lightly golden and airy",
        "sauce": "tomato base beneath cheese",
        "seasoning": "black pepper flakes",
        "garnish": "fresh basil leaves"
      }
    }
  ],
  "motion_and_effects": {
    "cheese_drips": "visible downward strings",
    "crumb_particles": "floating near top slice",
    "floating_layers": "pepperoni, cheese, tomato, slice"
  },
  "background": {
    "color": "neutral light gray",
    "texture": "smooth gradient"
  },
  "lighting": {
    "type": "studio soft light",
    "shadow": "subtle beneath plate",
    "highlights": "on cheese and basil leaves"
  },
  "camera": {
    "angle": "frontal mid-shot",
    "depth_of_field": "shallow, food in sharp focus",
    "framing": "centered composition"
  },
  "style": {
    "genre": "food photography",
    "realism": "hyper-realistic",
    "emphasis": "texture, melting cheese, floating layers",
    "mood": "clean, appetizing"
  }
}
```

[[Studio Lighting]] [[Food Photography]] [[Commercial Food Photography]]

---

### 159. 护肤品主视觉图生成器

**Author**: [TheAIHeadquarters](https://x.com/DavisonDabiri)  **Date**: 2026-01-19  **Language**: en

> 一个可定制的提示模板，用于生成超逼真的高端护肤品主视觉。它使用占位符来表示产品、背景颜色和关键成分，重点突出干净的摄影棚灯光、清晰的倒影和漂浮元素（植物、凝胶漩涡、水滴），以营造高端商业美感。

![护肤品主视觉图生成器](https://cms-assets.youmind.com/media/1768890669960_389lzs_G_A1y5CXIAANTX2.jpg)
![护肤品主视觉图生成器](https://cms-assets.youmind.com/media/1768890669812_67410t_G_A1zAVX0AAJa21.jpg)
![护肤品主视觉图生成器](https://cms-assets.youmind.com/media/1768890670260_lu04jb_G_A1y1wWgAAyNDH.jpg)
![护肤品主视觉图生成器](https://cms-assets.youmind.com/media/1768890671110_l4u0yi_G_A1zA8XQAAPvm1.jpg)

```
centered {argument name="product type" default="FACEWASH_PACKAGING"} on a bold {argument name="background color 1" default="BG_COLOR_1"}→{argument name="background color 2" default="BG_COLOR_2"} gradient, modern studio lighting, crisp reflections + soft grounded shadow. Label text perfectly readable: "{argument name="brand name" default="BRAND"} {argument name="product name" default="PRODUCT_NAME"}" only.Surround with floating KEY_INGREDIENT_1, KEY_INGREDIENT_2, BOTANICAL in a balanced ring layout, plus glossy gel/foam ribbon swirls (smooth loops), micro water droplets + light mist. Ultra-sharp focus, shallow DOF, 85mm, HDR, ISO100, clean negative space, no clutter, no watermark.Output {ASPECT} (1:1/4:5/9:16).
```

[[Studio Lighting]] [[Product Photography]] [[Commercial Photography]] [[Beauty Product Photography]]

---

### 160. 超现实波普艺术柑橘主题编辑肖像

**Author**: [TheAIHeadquarters](https://x.com/DavisonDabiri)  **Date**: 2026-01-19  **Language**: en

> 一个用于生成带有超现实波普艺术风格的奢华时尚杂志肖像的提示。画面中，一张男人的脸从茂密的成熟橙子和葡萄柚中浮现，他戴着软呢帽和太阳镜，表情俏皮。风格强调饱和的柑橘色调、干净的影棚灯光和强烈的视觉幽默感。

![超现实波普艺术柑橘主题编辑肖像](https://cms-assets.youmind.com/media/1768890659718_ct2vn8_G_AtD8tXcAANbou.jpg)
![超现实波普艺术柑橘主题编辑肖像](https://cms-assets.youmind.com/media/1768890660113_u9jtdf_G_AtD4nXAAA6kt4.jpg)

```
Luxury fashion editorial portrait with a surreal pop-art twist. A man’s face emerges from a dense composition of ripe oranges and grapefruits, filling the entire frame. He wears a textured fedora hat and dark aviator sunglasses, tongue slightly out in a playful, irreverent expression. One halved grapefruit placed near his mouth adds graphic contrast and bold texture. Saturated citrus color palette in vivid orange and coral tones. Clean, punchy studio lighting with soft specular highlights on fruit skins and subtle shadows around the face. Ultra-detailed textures, crisp focus, strong visual humor. Contemporary high-fashion editorial with ironic attitude, art-direction-driven composition, magazine-cover energy, bold surreal styling, no text.
```

[[Studio Lighting]] [[Fashion Editorial]] [[Surrealism]]

---

### 161. 超现实主义飞蛾翅膀女性肖像

**Author**: [BMX](https://x.com/bmxai13)  **Date**: 2026-01-18  **Language**: en

> 一个用于生成超现实肖像摄影的提示，描绘了一位苍白的人形女性，头部附有巨大的蛾翅，并带有独特的红色圆形眼妆。场景以复古花卉壁纸为背景，配有一个空金色画框，强调了鲜艳的红黑配色和怪异、柔和的影棚灯光。

![超现实主义飞蛾翅膀女性肖像](https://cms-assets.youmind.com/media/1768804237405_6y2b3d_G--0zojXMAABmom.jpg)

```
Surreal portrait photography, eye level, pale humanoid female with large moth wings on head and red circular eye makeup, red textured jacket with black buttons and white collar, standing motionless with intense gaze, red vintage floral wallpaper wall with empty ornate gold frame, vibrant {argument name="color palette" default="red and black"} palette, soft diffuse studio lighting and eerie atmosphere, hyper realistic textures and symmetry, Kodak Ektar 100 + 85mm Short Telephoto lens.
```

[[Studio Lighting]] [[Surrealist Portrait]]

---

### 162. 超精细编辑肖像，带橙色点缀

**Author**: [Artificial intelligence (Ai),Open Ai](https://x.com/Vishnudxe)  **Date**: 2026-01-18  **Language**: en

> 为 Gemini Nano Banana Pro 提供一个高度详细的文本提示，以生成一张具有编辑美学风格的超详细女性特写工作室肖像，重点突出特定的妆容、发型和配饰（橘色墨镜、橘色针织上衣、橘色指甲），置于明亮柔和的工作室灯光下。

![超精细编辑肖像，带橙色点缀](https://cms-assets.youmind.com/media/1768804282405_cbnqgb_G-9Q0dPXAAAg5H6.jpg)

```
Ultra-detailed close-up studio portrait, front-facing and centered composition. A young adult woman with fair, smooth skin and subtle natural freckles. She has striking light blue eyes and dark brown hair styled in a loose, slightly messy updo, with soft, wispy strands falling around her forehead, temples, and cheeks, giving a relaxed yet editorial look. Hair texture appears slightly damp or naturally tousled, not overly styled.  
She wears narrow, rectangular black sunglasses with glossy frames and warm orange-tinted lenses. The sunglasses sit low on the bridge of her nose, partially revealing her eyes above the lenses, creating a playful, confident, fashion-forward expression. Her eyebrows are natural and softly defined. Makeup is minimal and clean: natural skin finish, soft blush, lightly defined lips, no heavy contouring.  
Her facial expression is subtly flirtatious and relaxed, with a gentle closed-mouth smile. One hand is raised toward her face, with her index finger lightly touching her lower lip. Fingernails are neatly manicured and painted a vivid orange that matches her outfit and accessories.  
She is wearing a bright orange sleeveless knitted top with visible woven texture and fine fabric detail. The knit pattern is clearly defined, showing depth and realism in the material. Accessories include bold circular orange hoop earrings that complement the color palette. The color coordination between sunglasses lenses, earrings, nail polish, and clothing is intentional and cohesive.  
Lighting is bright, soft, and evenly diffused studio lighting, with no harsh shadows. Skin tones are natural and well-balanced, highlighting realistic texture and fine details. Background is a clean, minimal, light gray or off-white studio backdrop with no visible objects or distractions.  
Modern fashion editorial photography style. Sharp focus on the face and hand, high-resolution detail, professional studio quality. Neutral color grading with strong emphasis on warm orange tones for visual contrast. Crisp clarity, realistic proportions, natural anatomy, refined aesthetic. Shot with a high-end camera look, shallow depth of field, smooth background separation, polished yet effortless mood. --ar 9:16
```

[[Studio Lighting]] [[Editorial Portrait]] [[Makeup Detail]] [[Close-Up Beauty Shot]]

---

### 163. 高级时尚恋物癖魅力兔女郎面具肖像

**Author**: [Lex](https://x.com/katmanai)  **Date**: 2026-01-18  **Language**: en

> 一个详细的提示，用于拍摄一张具有暗黑奇幻美学风格的迷人、高级时装影棚肖像。它描述了一位诱惑的女性，戴着亮黑色漆皮兔耳面具，头发蓬松，妆容戏剧化，并佩戴水晶莱茵石项圈。技术细节包括强烈的影棚灯光、高对比度以及哈苏 H6D-100c 相机模拟。

![高级时尚恋物癖魅力兔女郎面具肖像](https://cms-assets.youmind.com/media/1768890739256_m0tr16_G-8-OhWWkAAU8x2.jpg)

```
{
  "main_prompt": "glamorous high-fashion studio portrait of a seductive woman in her mid-20s, long silky straight dark brown hair pulled into a high sleek ponytail cascading down her back, flawless bronzed skin with radiant glow, dramatic makeup: sharp black winged eyeliner, extremely long voluminous false lashes, contoured cheekbones, glossy nude-pink lips in soft parted pout, intense sultry gaze looking upward diagonally with half-lidded eyes, wearing glossy black patent leather bunny mask with large pointed bunny ears and cut-out eye holes framed in shiny black, black velvet or satin bunny ears headband integrated, sparkling oversized crystal rhinestone choker necklace with large round diamonds covering most of the neck, long black lace fingerless gloves reaching mid-forearm with intricate floral pattern, sheer black fishnet bodysuit or stockings visible at edges, subtle black latex or leather elements implied, dramatic studio lighting: strong key light from front-right creating catchlights in eyes and specular highlights on mask and skin, rim light from behind outlining hair ponytail and shoulders in white glow, soft fill light for smooth shadows, neutral dark gray seamless background, high contrast cinematic look with deep blacks and bright highlights, photorealistic, ultra-detailed skin texture with subtle pores and sheen, realistic latex shine on mask, crystal reflections on necklace, sharp focus on face and mask, soft bokeh on ponytail and gloves, film grain subtle, luxurious fetish glamour aesthetic, shot on Hasselblad H6D-100c with 80mm f/1.9 lens, shallow depth of field, high-end editorial Playboy / Victoria's Secret meets dark fantasy vibe",
  "negative_prompt": "blurry, lowres, deformed hands, extra fingers, fused fingers, bad anatomy, poorly drawn face, bad proportions, extra limbs, mutated hands, ugly, disfigured, tiling, out of frame, jpeg artifacts, signature, watermark, text, error, cropped, worst quality, low quality, cartoon, anime, 3d render, plastic skin, doll-like, airbrushed skin, overexposed, underexposed, flat lighting, harsh shadows, pale skin, no makeup, heavy filter overload, instagram face, duck lips, smiling happy expression, elderly, child, male, group shot, colorful background, outdoor setting, casual clothing, no mask, no bunny ears, no crystals, desaturated colors, monochrome, cheap materials, visible seams unnatural, low detail on mask shine or crystals",
  "style_tags": [
    "photorealistic",
    "high-fashion fetish glamour",
    "bunny mask editorial",
    "luxury crystal choker focus",
    "dramatic studio lighting",
    "cinematic high contrast",
    "seductive upward gaze",
    "patent leather shine",
    "lace gloves texture",
    "Playboy / dark fantasy aesthetic",
    "ultra-sharp beauty portrait"
  ],
  "technical": {
    "aspect_ratio": "2:3 or 3:4 (vertical high-fashion portrait / magazine cover style)",
    "lighting": "strong directional key light from front-right (~5500K "
```

[[Studio Lighting]] [[High Contrast]] [[Latex Fashion]]

---

### 164. 时尚《Vogue》杂志美妆封面肖像提示词

**Author**: [Sudee🥀](https://x.com/NameIsSudee)  **Date**: 2026-01-18  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张类似《Vogue》美容封面风格的高级时装编辑肖像，主角为 Josephine Langford。它详细说明了姿势、配饰（如透明黑色网纱手套和叠戴钻石珠宝）、服装、妆容以及实现逼真效果的相机技术设置。

![时尚《Vogue》杂志美妆封面肖像提示词](https://cms-assets.youmind.com/media/1768804202767_bskusu_G-88jlAXUAE6Inf.jpg)
![时尚《Vogue》杂志美妆封面肖像提示词](https://cms-assets.youmind.com/media/1768804202784_ev8sb8_G-88lsxXMAAlfvw.jpg)
![时尚《Vogue》杂志美妆封面肖像提示词](https://cms-assets.youmind.com/media/1768804202797_o3z9o9_G-88jx1XwAAC654.jpg)
![时尚《Vogue》杂志美妆封面肖像提示词](https://cms-assets.youmind.com/media/1768804203758_8ks6p3_G-88lstWkAAyRpF.jpg)

```
Magazine beauty cover portrait of {argument name="subject name" default="Josephine Langford"}. Front-facing, chin slightly lowered, eyes locked directly into camera with quiet confidence. One hand raised elegantly, fingers sculpted and spaced, partially framing one eye without covering the face. Pose is minimal, powerful, editorial no exaggeration.

Accessories:
Sheer black mesh gloves on both hands,
multiple stacked diamond rings including a large solitaire,
diamond eternity bands,
layered slim diamond bangles and one thicker bracelet,
diamond tennis choker fitted closely to the neck,
matching diamond stud earrings.

Outfit:
Deep Purple halter-neck couture gown, clean neckline, luxury fabric, sharp tailoring.

Hair & Makeup:
Hair softly voluminous, natural movement.
Makeup is Vogue beauty standard: flawless realistic skin texture, soft sculpted cheekbones, warm nude lips, refined lashes, subtle smoky eyes.

Lighting & Camera:
Soft directional studio lighting, gentle shadow sculpting,
medium-format editorial lens, neutral gray background.

8K ultra-detailed, ultra-sharp focus, shallow depth of field,
true-to-life skin texture, photorealistic,
high-fashion editorial realism,
aspect ratio 9 :16, steps 50, cfg scale 9.5
```

[[Studio Lighting]] [[Celebrity Likeness]] [[Haute Couture Fashion]] [[Diamond Jewelry]]

---

### 165. 极简 3D 等距透视立体模型生成器

**Author**: [AeliaVision](https://x.com/NightXpulse)  **Date**: 2026-01-18  **Language**: en

> 一个简单、可定制的提示模板，用于生成简洁、极简的 3D 等距透视立体模型。它允许用户定义展览类型、展示物品和展台结构，并侧重于逼真的材质和柔和的影棚灯光。

![极简 3D 等距透视立体模型生成器](https://cms-assets.youmind.com/media/1768804232546_vd8e69_G-8YfWxXIAAJ-Af.jpg)

```
A clean, minimal 3D isometric diorama of a {argument name="exhibition type" default="[EXHIBITION TYPE]"}, featuring {argument name="display objects" default="[DISPLAY OBJECTS]"} arranged within a {argument name="pod structure" default="[POD STRUCTURE]"}, subtle lighting accents, smooth floor surfaces, soft studio lighting, realistic materials, rounded
```

[[Studio Lighting]] [[Miniature Diorama]] [[Minimalist Design]]

---

### 166. 一支钢笔的超逼真产品摄影

**Author**: [Milo](https://x.com/Milo_Bahi_02)  **Date**: 2026-01-18  **Language**: en

> 生成一支超逼真、8K 专业影棚产品照片的提示语，内容为一支高端圆珠笔。重点在于展示金属质感、雕刻细节和逼真的反光，采用柔和的电影级灯光和极简奢华背景，非常适合高端商业广告。

![一支钢笔的超逼真产品摄影](https://cms-assets.youmind.com/media/1768804308646_mr7mc5_G-8OLh_XYAEzJfc.jpg)

```
Ultra-realistic professional studio product photography of a premium ballpoint pen, perfectly centered on a clean reflective surface.
The pen is angled slightly for elegance, showcasing metallic texture, engraved details, and realistic reflections.
Soft cinematic lighting with subtle highlights and shadows to emphasize craftsmanship.
Minimalist luxury background with smooth gradient tones.
High-end commercial advertising style, hyper detailed materials, sharp focus, depth of field, editorial product shot.
No text, no watermark, no blur.
Image Size: 3:4
Resolution: 8K
Style: Premium, modern, minimalist, luxury branding
```

[[Studio Lighting]] [[Product Photography]] [[Commercial Photography]]

---

### 167. 8K 编辑工作室肖像提示

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-01-18  **Language**: en

> 一个结构化的 JSON 提示词，用于在简洁的影棚环境中生成一张超高分辨率（8K）的编辑时尚肖像。它指定了专业的影棚布光（柔光箱主光、柔和发光），主体身着现代简约街头服饰，并要求高真实感、准确的肤色和无干扰的背景。

![8K 编辑工作室肖像提示](https://cms-assets.youmind.com/media/1768804265473_528j0d_G-7LwPjW4AAj5na.jpg)
![8K 编辑工作室肖像提示](https://cms-assets.youmind.com/media/1768804265347_17pu5x_G-7LwW0bcAE9Lp7.jpg)

```
{
  "image_type": "studio_photoshoot",
  "shot_type": "half_body",
  "camera": {
    "angle": "eye_level",
    "lens": "85mm portrait lens",
    "aperture": "f/2.8",
    "focus": "tack_sharp_on_subject",
    "depth_of_field": "shallow_background_blur"
  },
  "subject": {
    "gender": "male/female",
    "age_range": "mid_30s_to_early_40s",
    "build": "natural_fit",
    "pose": "relaxed_confident_stance",
    "expression": "calm_confident_neutral",
    "outfit": "casual_streetwear",
    "clothing_details": {
      "top": "well_fitted_tshirt_or_light_jacket",
      "colors": "neutral_muted_tones",
      "style": "modern_minimal"
    }
  },
  "lighting": {
    "type": "professional_studio_lighting",
    "key_light": "softbox_front",
    "fill_light": "subtle_fill",
    "rim_light": "gentle_hair_light",
    "shadows": "soft_natural",
    "skin_tones": "accurate_and_realistic"
  },
  "background": {
    "style": "clean_studio_backdrop",
    "color": "{argument name="background color" default="soft_gradient_neutral"}",
    "texture": "smooth_minimal",
    "distraction_free": true
  },
  "style": {
    "realism": "high",
    "look": "editorial_fashion_portrait",
    "color_grading": "natural_balanced",
    "no_filters": true
  },
  "quality": {
    "resolution": "8K",
    "detail_level": "ultra_high",
    "noise": "none"
  },
  "constraints": [
    "full_focus_on_subject",
    "no_motion_blur",
    "no_overprocessing",
    "no_cartoon_style",
    "no_distorted_anatomy"
  ]
}
```

[[Studio Lighting]] [[Streetwear Fashion]] [[Editorial Portrait]] [[Softbox Lighting]]

---

### 168. 家用物品建筑的 3D 等距透视模型

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-18  **Language**: en

> 一个用于生成简洁、极简的 3D 等距透视立体模型（diorama）的提示，其中指定的家用物品被转化为小型建筑结构。它强调真实的材质、柔和的影棚布光以及微缩建筑模型风格。

![家用物品建筑的 3D 等距透视模型](https://cms-assets.youmind.com/media/1768804300421_dnjx48_G-6zqv-XgAAiRfz.jpg)
![家用物品建筑的 3D 等距透视模型](https://cms-assets.youmind.com/media/1768804300228_vgyh8m_G-6zn0XaUAAJDSL.jpg)
![家用物品建筑的 3D 等距透视模型](https://cms-assets.youmind.com/media/1768804300310_bxodc0_G-6zoUpWwAA3YBF.jpg)
![家用物品建筑的 3D 等距透视模型](https://cms-assets.youmind.com/media/1768804301814_rfw4oq_G-6zsnAXwAAyVnh.jpg)

```
A clean, minimal 3D isometric diorama transforming a {argument name="household object" default="HOUSEHOLD OBJECT"} into a small architectural structure. Functional elements are abstracted into doors, windows, and volumes, realistic materials, soft studio lighting, rounded edges, miniature architectural model style, neutral background.
```

[[Studio Lighting]] [[Miniature Architecture]]

---

### 169. 超写实商业美食摄影提示词

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-01-17  **Language**: en

> 一个详细的提示，用于生成超逼真的商业食品摄影，特别侧重于高分辨率、锐利对焦和受控的影棚照明，以捕捉食材在半空中凝固的瞬间。此提示采用 JSON 结构，可精确控制输出设置和美学细节。

![超写实商业美食摄影提示词](https://cms-assets.youmind.com/media/1768717588616_6tvblq_G-4KPKGWsAEk3FE.jpg)
![超写实商业美食摄影提示词](https://cms-assets.youmind.com/media/1768717588696_15yk0k_G-4KPJqWoAAzMee.jpg)
![超写实商业美食摄影提示词](https://cms-assets.youmind.com/media/1768717588636_hmnjxa_G-4KPJhXsAAoIPq.jpg)
![超写实商业美食摄影提示词](https://cms-assets.youmind.com/media/1768717590696_ewqa6m_G-4KPKCW0AEHtnA.jpg)

```
"resolution": "{argument name="resolution" default="8K UHD"}",

"aspect_ratio": "3:4",

{ "image_style": "{argument name="image style" default="hyper-realistic commercial food photography"}", "quality": "Ultra-high detail, sharp focus, studio-grade clarity", "lighting": "Soft but controlled studio lighting with visible highlights and splash definition", "motion": "Frozen mid-air action, ingredients suspended",

"global_settings": {

"background_style": "Solid or smooth gradient background, color varies per module", 
"camera": "High-speed photography look, shallow to medium depth of field", "post_processing": "Balanced contrast, natural saturation, no artificial glow" }}
```

[[Studio Lighting]] [[Commercial Photography]] [[Food Photography]]

---

### 170. 超逼真商业美食摄影

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-17  **Language**: en

> 一个技术性提示，旨在生成超逼真的商业食品摄影，特别捕捉食材在半空中凝固的瞬间，具有高速相机美学和受控的影棚照明效果。

![超逼真商业美食摄影](https://cms-assets.youmind.com/media/1768717518115_xlrzuh_G-3tFT8aAAAhglp.jpg)
![超逼真商业美食摄影](https://cms-assets.youmind.com/media/1768717518114_mzz1pn_G-3tFTAbkAEXFia.jpg)
![超逼真商业美食摄影](https://cms-assets.youmind.com/media/1768717518102_8djjav_G-3tFTtakAI0WQ3.jpg)
![超逼真商业美食摄影](https://cms-assets.youmind.com/media/1768717519186_r2eeu3_G-3tFVWasAAjgWp.jpg)

```
{

'resolution': '8K UHD',

'aspect_ratio': '3:4',

'image_style': 'hyper-realistic commercial food

photography',

'global_settings': {

'quality': 'Ultra-high detail, sharp focus,

studio-grade clarity',

'lighting': 'Soft but controlled studio lighting with visible highlights and splash definition',

'motion': 'Frozen mid-air action, ingredients

suspended',

'background_style': 'Solid or smooth gradient background, color varies per module',
camera': 'High-speed photography look, shallow to medium depth of field',

'post_processing': 'Balanced contrast, natural saturation, no artificial glow'

}}
```

[[Studio Lighting]] [[Food Photography]]

---

### 171. Jenna Ortega 高级时装大片

**Author**: [Emer](https://x.com/emer_web3)  **Date**: 2026-01-17  **Language**: en

> 生成一张 8k、照片级的时尚编辑照片，以低角度、虫眼视角拍摄 Jenna Ortega，重点突出她精致的高级定制服装和专业的影棚灯光。

![Jenna Ortega 高级时装大片](https://cms-assets.youmind.com/media/1768717507305_wnmd27_G-3nn0XWcAA8rHz.jpg)

```
A low-angle, worm's-eye view shot looking up from the ground at {argument name="person" default="Jenna Ortega"}. She is striking a high-fashion pose wearing a structured corset top with an intricate silver chainmail or wire-mesh overlay, and a voluminous, short black skirt featuring layers of tiered ruffles and textured fabric. She is wearing black strappy high-heeled sandals with small bows. The background is a clean, seamless off-white studio backdrop. The lighting is soft and professional, emphasizing the texture of the clothing and skin. Photorealistic, 8k resolution, editorial fashion photography style.
```

[[Studio Lighting]] [[Fashion Editorial]] [[Low Angle Shot]] [[Celebrity Fashion]]

---

### 172. 极简主义 3D 等距展览舱透视模型

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-17  **Language**: en

> 一个用于生成简洁、极简的 3D 等距透视立体模型图像的模板提示。它旨在可视化一个弹出式展览空间，允许用户自定义展览类型、展示物品和展台结构，所有这些都以微型建筑模型风格和柔和的摄影棚灯光进行渲染。

![极简主义 3D 等距展览舱透视模型](https://cms-assets.youmind.com/media/1768717570869_xdbz00_G-2E_2JaUAAR7Q-.jpg)
![极简主义 3D 等距展览舱透视模型](https://cms-assets.youmind.com/media/1768717571037_97xhnv_G-2FCdTbsAEhLkv.jpg)
![极简主义 3D 等距展览舱透视模型](https://cms-assets.youmind.com/media/1768717570896_tgc8pr_G-2E-79aMAA_5IP.jpg)
![极简主义 3D 等距展览舱透视模型](https://cms-assets.youmind.com/media/1768717572279_b3d735_G-2FEBYbgAAhFx-.jpg)

```
A clean, minimal 3D isometric diorama of a {argument name="exhibition type" default="[EXHIBITION TYPE]"}, featuring {argument name="display objects" default="[DISPLAY OBJECTS]"} arranged within a {argument name="pod structure" default="[POD STRUCTURE]"}, subtle lighting accents, smooth floor surfaces, soft studio lighting, realistic materials, rounded edges, miniature architectural model style, high detail, neutral background.
```

[[Studio Lighting]] [[Minimalist Aesthetic]] [[Miniature Architecture]]

---

### 173. 现代主义水果建筑微距摄影

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-17  **Language**: en

> 一个专为商业美食摄影设计的提示，指示生成一个电影级的微距镜头，拍摄一个完全由热带水果（芒果、奇异果、火龙果）构建的现代主义凉亭。它强调几何构图、反光表面和影室布光，以增强鲜艳的色彩和纹理。

![现代主义水果建筑微距摄影](https://cms-assets.youmind.com/media/1768717536063_xvy70m_G-1NDltXIAAvFzd.jpg)
![现代主义水果建筑微距摄影](https://cms-assets.youmind.com/media/1768717536008_uh5qyo_G-1NDkbXYAAI-WZ.jpg)
![现代主义水果建筑微距摄影](https://cms-assets.youmind.com/media/1768717536370_1ythb2_G-1NDmCXwAA2kgL.jpg)
![现代主义水果建筑微距摄影](https://cms-assets.youmind.com/media/1768717537040_narg4p_G-1NDoGXcAArRyq.jpg)

```
{
  "scene": "Modernist pavilion-style arrangement of tropical fruits",
  "elements": [
    {"type": "fruit", "variety": "mango", "shape": "cubes"},
    {"type": "fruit", "variety": "kiwi", "shape": "slices"},
    {"type": "fruit", "variety": "dragon fruit", "shape": "wedges"},
    {"type": "flower", "variety": "edible", "role": "supporting columns"},
    {"type": "liquid", "variety": "citrus juice", "effect": "dew droplets"}
  ],
  "composition": {
    "geometry": "geometric terraces",
    "surface": "reflective glass"
  },
  "lighting": "studio lighting enhancing vibrant colors and shadows",
  "shot": "cinematic high-definition macro",
  "style": ["ultra-realistic textures", "commercial food photography aesthetics"]
}
```

[[Studio Lighting]] [[Macro Photography]] [[Commercial Food Photography]]

---

### 174. 控制图像生成中的光照

**Author**: [いしみず CG屋](https://x.com/isisi_1023)  **Date**: 2026-01-17  **Language**: ja

> 一个用于展示 Nano Banana Pro 在特定光照条件下生成图像能力的提示。用户将默认生成（未指定光照）的输出与明确要求详细光照的输出进行比较。

![控制图像生成中的光照](https://cms-assets.youmind.com/media/1768717588635_gt9p4b_G-1Kqy1awAAGzLD.jpg)
![控制图像生成中的光照](https://cms-assets.youmind.com/media/1768717588557_458pcd_G-1Ks9ybwAAh4XU.jpg)

```
Nano banana proはお任せでも綺麗な画像が生成されますが、細かくライティングを指定するとそれに応じた画像が生成されます。構図もネタも指定できますし、多くのものを学んでいるようなので、汎用性も高いですね。
左：{argument name="ライティング指定" default="指定無し"}
右：{argument name="ライティング指定" default="指定"}
```

[[Studio Lighting]]

---

### 175. 超逼真女性肖像 2x2 网格

**Author**: [Willy](https://x.com/jw660227)  **Date**: 2026-01-17  **Language**: en

> 一个高度详细的提示，用于生成 2x2 网格的超逼真、高分辨率女性肖像。每个面板都展示了一位不同的女性，她们拥有特定的发型、服装和配饰细节（例如，耳机、针织毛衣、珠宝），所有这些都通过白皙的皮肤、红润的脸颊、俏皮的眨眼以及带有柔和散景背景的电影级灯光统一起来。

![超逼真女性肖像 2x2 网格](https://cms-assets.youmind.com/media/1768717573644_a06cnx_G-1F9SObEAAPnQz.jpg)

```
2x2 grid of ultra-realistic, high-resolution photograph portraits of beautiful young women with fair skin and rosy cheeks, winking playfully, studio quality. 1: Top left: Shoulder-up shot, a stunning woman with long curly strawberry-blonde hair styled in a high bun, wearing white over-ear headphones and pastel pink sunglasses, pink oversized knit cardigan, fluffy cream crop top, light beige lounge shorts with a delicate pink bow. 2: Top right: Intimate headshot, a gorgeous woman with long wavy auburn hair cascading sensually down her shoulders, adorned with gold hoop earrings, wearing a chunky cream knit sweater, soft lavender eyeshadow enhancing her captivating eyes. 3: Bottom left: Alluring head and torso view, a striking woman with long straight platinum blonde hair styled in a high ponytail, a delicate silver chain necklace accentuating her neckline, wearing a powder blue cropped knit sweater, light, tasteful makeup. 4: Bottom right: Sensual close-up head and shoulders shot, a beautiful woman with long messy braided brunette hair adorned with delicate flowers, gold dainty earrings, a cozy forest green chunky knit sweater, natural, enhancing makeup. Warm, soft, and cinematic lighting with pastel bokeh backgrounds in each panel, shallow depth of field, ultra-detailed textures, soft global illumination, smooth skin shading, ultra-high resolution, 8K, sharp focus, clean, vibrant, aesthetic, studio quality. A stylish handwritten signature "Willy" is elegantly and small letters placed at the Bottom Right corner, realistic skin texture, professional photography, shot on Hasselblad X2D, 85mm f/1.2 lens.
```

[[Studio Lighting]] [[Hyperrealistic Portrait]] [[Bokeh Background]]

---

### 176. 西方电视角色 3D 等距微缩模型

**Author**: [Favori](https://x.com/yuanguand)  **Date**: 2026-01-16  **Language**: en

> 一个用于生成美国西部电视剧核心角色风格化、细节丰富、超高保真 3D 等距微缩模型的提示。这些模型置于城市街道上，背景为纯白色，在柔和的摄影棚灯光下展示不同的标志性动作。

![西方电视角色 3D 等距微缩模型](https://cms-assets.youmind.com/media/1768631173816_nsi334_G-ybd-ObcAERfOr.jpg)

```
Stylized and incredibly detailed ultra-high-fidelity 3D isometric miniature models showcase the core characters of the {argument name="TV series genre" default="American Western"} TV series. Each character displays a different signature move, while soft studio lighting creates stunning light and shadow effects. The highly detailed 3D models are placed on {argument name="setting" default="city streets"} against a pure white background.
```

[[Studio Lighting]] [[White Background]]

---

### 177. 极简 3D 等距建筑立体模型

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-16  **Language**: en

> 一个用于生成干净、简约的 3D 等距建筑剖面立体模型的模板提示。该提示允许自定义建筑类型、内部/外部元素和剖面风格，旨在呈现具有柔和工作室照明和逼真材质的微缩建筑模型美学。

![极简 3D 等距建筑立体模型](https://cms-assets.youmind.com/media/1768631167212_chnax0_G-xRiuLbQAATRuP.jpg)
![极简 3D 等距建筑立体模型](https://cms-assets.youmind.com/media/1768631167249_uq1fis_G-xRiuJbQAE9AKC.jpg)
![极简 3D 等距建筑立体模型](https://cms-assets.youmind.com/media/1768631167254_l9b9p2_G-xRiuKbQAA7P5f.jpg)
![极简 3D 等距建筑立体模型](https://cms-assets.youmind.com/media/1768631168636_h31pvg_G-xRiuKagAArqTY.jpg)

```
A clean, minimal 3D isometric diorama of a [{argument name="building type" default="BUILDING TYPE"}] section, featuring [{argument name="elements" default="INTERIOR / EXTERIOR ELEMENTS"}] visible in a [{argument name="style" default="CUTAWAY / OPEN STYLE"}], simple [STRUCTURAL FRAME], subtle [INFORMATIONAL SIGNAGE], smooth [MATERIAL FINISH], soft studio lighting, realistic materials, rounded edges, miniature architectural model style, high detail, neutral background.
```

[[Studio Lighting]]

---

### 178. 珍娜·奥尔特加 (Jenna Ortega) 高级时装编辑提示

**Author**: [jennieee:3](https://x.com/jenniebae_ai)  **Date**: 2026-01-16  **Language**: en

> 一个为 Jenna Ortega 拍摄高级时装编辑照片而设计的图像生成提示，重点在于戏剧性的低角度视角、链甲和层叠荷叶边等精致服装细节，以及专业的影棚灯光，以实现逼真的 8k 效果。

![珍娜·奥尔特加 (Jenna Ortega) 高级时装编辑提示](https://cms-assets.youmind.com/media/1768631116420_wx0bmo_G-wmIQ6a8AAooxv.jpg)

```
A low-angle, worm's-eye view shot looking up from the ground at {argument name="subject" default="Jenna Ortega"}. She is striking a high-fashion pose wearing a structured corset top with an intricate silver chainmail or wire-mesh overlay, and a voluminous, short black skirt featuring layers of tiered ruffles and textured fabric. She is wearing black strappy high-heeled sandals with small bows. The background is a clean, seamless off-white studio backdrop. The lighting is soft and professional, emphasizing the texture of the clothing and skin. Photorealistic, 8k resolution, editorial fashion photography style.
```

[[Studio Lighting]] [[Low Angle Shot]] [[Celebrity Fashion Editorial]] [[8K Photorealism]]

---

### 179. 微距美食摄影提示，带有滴落的液体

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-01-15  **Language**: en

> 一个简洁的提示，用于生成一张适合杂志封面的微距食物照片。它指定了三层食物堆叠在一起，液体向下滴落，背景为白色，采用影棚布光和体积光效果，并使用 Nikon Z6 II 相机风格。

![微距美食摄影提示，带有滴落的液体](https://cms-assets.youmind.com/media/1768544785651_gfb5cl_G-t0mfzbQAMbE4W.jpg)
![微距美食摄影提示，带有滴落的液体](https://cms-assets.youmind.com/media/1768544785651_ljagez_G-t0meKa0AEm7vc.jpg)

```
a stack of three {argument name="food item" default="[FOOD ITEM]"} with {argument name="liquid" default="[LIQUID]"} dripping down, on a white background, in the style of food photography, magazine cover "{argument name="magazine title" default="[FOOD] pixel"}", macro shot, studio lighting, nikon z6 ii, volumetric lighting, neutral tones.
```

[[Studio Lighting]] [[Volumetric Light]]

---

### 180. 极简 3D 等距城市零售亭立体模型

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-15  **Language**: en

> 一个用于生成干净、简约的城市零售亭 3D 等距透视立体模型 的模板提示。它使用占位符进行自定义，重点是柔和的摄影棚灯光、逼真的材质、圆润的边缘和微缩建筑模型风格。

![极简 3D 等距城市零售亭立体模型](https://cms-assets.youmind.com/media/1768544837770_97r4vf_G-sshocaMAADfrO.jpg)
![极简 3D 等距城市零售亭立体模型](https://cms-assets.youmind.com/media/1768544837799_mg1t12_G-sskQzaAAA3mqZ.jpg)
![极简 3D 等距城市零售亭立体模型](https://cms-assets.youmind.com/media/1768544837777_tgj3zl_G-ssl2HbgAAFKvP.jpg)
![极简 3D 等距城市零售亭立体模型](https://cms-assets.youmind.com/media/1768544838969_8naarr_G-ssnHzbQAMl8AX.jpg)

```
A clean, minimal 3D isometric diorama of a [{argument name="urban retail type" default="URBAN RETAIL TYPE"}], featuring a [{argument name="main counter object" default="MAIN COUNTER / DISPLAY OBJECT"}] placed on a [{argument name="ground platform type" default="GROUND / PLATFORM TYPE"}], simple [CANOPY / ROOF STRUCTURE], subtle [SIGNAGE TYPE], smooth [SURFACE MATERIAL], soft studio lighting, realistic materials, rounded edges, miniature architectural model style, high detail, neutral background.
```

[[Studio Lighting]] [[Miniature Architecture]]

---

### 181. 奢华苏打水广告视频提示

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-15  **Language**: en

> 一个详细的多场景提示，用于生成一个 16 秒的奢华饮品商业视频。它专注于超慢动作流体动力学、受控飞溅物理和戏剧性影棚布光，以优雅、高对比度的美学展示单一产品（一个紫色汽水罐）。

![奢华苏打水广告视频提示](https://cms-assets.youmind.com/media/1768544762222_ykrzdt_G-rkSoPbQAQcTxj.jpg)

```
Create a luxury beverage commercial featuring a single {argument name="soda color" default="purple"} soda can standing perfectly upright at the center of the frame on a glossy reflective surface. The environment is dark violet with soft bokeh particles and dramatic studio lighting.
Scene 1 – Stillness (0–2s):
The video opens in complete stillness. Only the can is visible—no berries, no water, no splashes, no particles. Condensation beads glisten on the surface. Subtle rim lighting outlines the can while the background remains moody and minimal.
Scene 2 – Tension Build (2–4s):
A low-frequency vibration begins. The can starts to shake gently, then slightly more intensely, as if pressure is building inside. The camera remains locked and centered, heightening anticipation.
Scene 3 – Burst Moment (4–7s):
The top of the can suddenly bursts open in slow motion. A powerful surge of luminous purple liquid erupts upward. The motion is controlled and cinematic—no chaotic spray. The liquid forms elegant arcs and sculpted waves.
Scene 4 – Flavor Reveal (7–10s):
As the purple liquid rises, glossy grape berries emerge from the opening, carried by the splash. Droplets and fruit are suspended in ultra-slow motion. The splash wraps around the can without hiding it, maintaining full product visibility.
Scene 5 – Hero Composition (10–14s):
The liquid reaches its peak and frames the can in a dramatic crown shape. Berries float in perfect balance around the splash. The reflective surface below mirrors the entire scene, creating depth and luxury.
Final Hold (14–16s):
Motion settles into a striking hero shot: can centered, purple liquid frozen in sculptural form, berries suspended mid-air. No text, no logos, no transitions—pure visual impact.
Style & Mood:
Ultra-premium soda advertisement, dark luxury aesthetic, cinematic slow motion, high-contrast lighting, glossy reflections, dramatic yet elegant energy.
Camera & Technical Direction:
Locked-off camera, high-speed macro cinematography, realistic fluid dynamics, controlled splash physics, volumetric lighting, shallow depth of field, hyper-detailed droplets.
```

[[Studio Lighting]] [[Product Photography]]

---

### 182. 西德尼·斯威尼 (Sydney Sweeney) 风格双联画时尚肖像

**Author**: [Bahar azam](https://x.com/BaharAzamm561)  **Date**: 2026-01-15  **Language**: en

> 一个高度详细、超逼真的提示词，用于创作一张悉尼·斯威尼 (Sydney Sweeney) 风格的双联画（并排比较）编辑肖像。它指定了超逼真的皮肤纹理、90 年代蓬松发型、精致的服装（Celine 抹胸、细条纹衬衫、水洗牛仔裤），以及在高调商业照明下的两种截然不同的情绪状态/姿势（真诚的快乐和性感的时尚）。

![西德尼·斯威尼 (Sydney Sweeney) 风格双联画时尚肖像](https://cms-assets.youmind.com/media/1768544862480_z64dyr_G-qz8oyXYAA0J6c.jpg)

```
{
  "api_version": "3.5",
  "master_specification": {
    "project_id": "SYDNEY_SWEENEY_STYLE_V3.5",
    "rendering_fidelity": "Ultra-Photorealistic / 8K / Raw Photo",
    "aspect_ratio": "4:5 Portrait Orientation"
  },
  "subject_biometrics": {
    "primary_subject": "Sydney Sweeney",
    "facial_architecture": {
      "skin_finish": "Hyper-realistic skin texture, visible fine pores, soft freckles, dewy highlights on cheekbones and nose bridge",
      "eye_detail": "Vibrant icy-blue irises with realistic light reflections, dark lash line, and natural feathered eyebrows",
      "mouth": "Softly parted lips with a natural peach tint and subtle glossy sheen"
    },
    "hair_engineering": {
      "color": "Layered honey-blonde with platinum highlights and darker ash-blonde roots",
      "style": "Voluminous 90s blowout, soft bouncy curls, center-parted with curtain bangs framing the face",
      "physics": "Individual hair strands visible, soft flyaways for authentic realism"
    }
  },
  "wardrobe_encyclopedia": {
    "upper_layer_inner": {
      "item": "Premium ribbed cotton bandeau crop top",
      "branding_specs": "Embroidered black 'CELINE' text in bold sans-serif font across a 2-inch wide white elastic waistband",
      "fabric_texture": "Visible vertical ribbing, soft matte cotton finish"
    },
    "upper_layer_outer": {
      "item": "Lightweight poplin button-down shirt",
      "pattern_details": "Ultra-fine vertical pinstripes in cerulean blue and crisp white",
      "draping": "Worn completely open, cuffs rolled up to the mid-forearm, fabric falling naturally away from the torso"
    },
    "lower_body": {
      "item": "High-quality denim jeans",
      "wash": "Stone-washed light indigo with subtle whiskering at the hip",
      "construction": "Visible copper rivets, heavy-duty stitching, and metallic button detail"
    },
    "accessories": {
      "eyewear": "High-gloss black acetate sunglasses with silver metallic hinges, positioned precisely on the crown of the head",
      "earrings": "14k gold micro-hoop earrings with a polished finish"
    }
  },
  "composition_logic": {
    "layout_type": "Diptych (Side-by-side comparison)",
    "panel_left_logic": {
      "emotional_state": "Candid Happiness",
      "pose_dynamics": "Looking down toward the left, wide smile, eyes partially closed, hands deep in pockets",
      "vibe": "Spontaneous and joyful"
    },
    "panel_right_logic": {
      "emotional_state": "Sultry Editorial",
      "pose_dynamics": "Head tilted slightly upward, eyes looking off-camera, neutral/soft expression, thumb hooked in pocket",
      "vibe": "Confident and high-fashion"
    }
  }, "optical_and_environmental_engine": {
    "lighting": {
      "primary_source": "Large softbox from the front-left to minimize harsh shadows",
      "rim_light": "Subtle backlight to separate blonde hair from the white background",
      "quality": "High-key, clean, and commercial"
   }, 
    "b
```

[[Studio Lighting]] [[Ultra-Realistic Skin Texture]]

---

### 183. 电影级时尚肖像：红色卷发

**Author**: [Prompt Girl](https://x.com/GirlPromptSkin)  **Date**: 2026-01-15  **Language**: en

> 一个详细的提示，用于生成一张电影般的、超精细的时尚肖像。画面中，一位年轻女子拥有一头鲜艳的红色卷发，身穿蓝色抹胸泳衣，优雅地摆姿势，坐在一张深色木桌旁，桌上摆放着特定的道具（酒杯、蜡烛），强调柔和的影棚灯光和 8K 画质。

![电影级时尚肖像：红色卷发](https://cms-assets.youmind.com/media/1768544813900_o02sge_G-qnaXZbQAQzwBl.jpg)

```
Young beauty, cinematic realism, ultra-detailed, photorealistic fashion photography
A young  woman with vibrant {argument name="hair color" default="red"} curly hair, styled naturally with soft volume, wearing a black flower barrette tucked elegantly into her curls. She stands confidently beside a dark wooden table with a glossy polished finish, exuding poise and editorial elegance.
She is dressed in a stylish {argument name="swimwear color" default="blue"} bandeau-style swim top paired with matching high-waisted blue bottoms, tastefully designed and fashion-forward. A delicate gold necklace rests naturally around her neck, catching subtle highlights.
Her pose is confident and refined:
Left hand gently leaning on the table
Right hand resting on her hip
Relaxed posture, natural proportions, graceful stance
On the table:
A clear glass of red wine reflecting soft ambient light
Two blue cylindrical candles placed neatly to the right
The background features a textured, worn gray wall, slightly distressed, adding visual contrast and depth.
Lighting is soft cinematic studio lighting with subtle shadows, natural skin tones, sharp focus, and shallow depth of field.
Captured with a professional DSLR, 85mm lens, high dynamic range, realistic skin texture, editorial fashion composition, 8K quality.
🔻 Negative Prompt (Safe)
low quality, blurry, cartoon, anime, CGI, plastic skin, over-smoothed skin, exaggerated anatomy, distorted proportions, extra limbs, poorly drawn hands, harsh flash, flat lighting, watermark, logo, text, cropped head, overexposed, underexposed
```

[[Studio Lighting]] [[Cinematic Fashion]]

---

### 184. 时尚肖像：曼巴蛇与狼蛛

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-01-14  **Language**: en

> 一组三个高度详细、超现实的时尚编辑提示，用于拍摄一位拥有深邃绿眼和湿润皮肤的女性的特写肖像，超现实配饰包括一条黄色曼巴蛇、一条黑色曼巴蛇或一只黑色狼蛛。这些提示强调电影般的微距摄影、高细节皮肤纹理和影棚布光。

![时尚肖像：曼巴蛇与狼蛛](https://cms-assets.youmind.com/media/1768468532030_ppu2v5_G-pvtQVXQAEsmym.jpg)
![时尚肖像：曼巴蛇与狼蛛](https://cms-assets.youmind.com/media/1768468532100_ez7d6a_G-pvtGfXoAAeaEj.jpg)
![时尚肖像：曼巴蛇与狼蛛](https://cms-assets.youmind.com/media/1768468532337_k9d24u_G-pvtHYXkAA0MEz.jpg)

```
{
  "prompt": "Ultra-realistic extreme close-up fashion portrait of a striking young woman with intense green eyes and wet skin covered in water droplets. Dark slicked-back damp pigtails hair with natural strands falling across her forehead. Glossy full lips, strong defined brows, dramatic eye makeup slightly smudged by moisture. A large {argument name="animal type" default="yellow mamba snake"} coiled elegantly around her neck, its sleek head resting centrally among her ample bust prominently visible through a deep plunging cleavage shirt. One visible metallic hoop earring. High-detail skin texture with glistening droplets on neck and chest, cinematic macro photography, shallow depth of field. Studio lighting with soft highlights and sharp contrast. Editorial high-fashion beauty concept with a bold surreal aesthetic. Photorealistic, ultra-sharp focus, luxury magazine style, 8K quality.",
  "style": "cinematic editorial fashion photography",
  "camera": "macro lens, extreme close-up",
  "lighting": "studio lighting, soft highlights, high contrast",
  "focus": "shallow depth of field, ultra-sharp subject",
  "mood": "bold, surreal, high-fashion",
  "quality": "8K, ultra-realistic, photorealistic"
}

{
  "prompt": "Ultra-realistic extreme close-up fashion portrait of a striking young woman with intense green eyes and wet skin covered in water droplets. Dark slicked-back damp hair with natural strands falling across her forehead. Glossy full lips, strong defined brows, dramatic eye makeup slightly smudged by moisture. A large black mamba snake coiled elegantly around her neck, its sleek head resting centrally among her ample bust prominently visible through a deep plunging cleavage shirt. One visible metallic hoop earring. High-detail skin texture with glistening droplets on neck and chest, cinematic macro photography, shallow depth of field. Studio lighting with soft highlights and sharp contrast. Editorial high-fashion beauty concept with a bold surreal aesthetic. Photorealistic, ultra-sharp focus, luxury magazine style, 8K quality.",
  "style": "cinematic editorial fashion photography",
  "camera": "macro lens, extreme close-up",
  "lighting": "studio lighting, soft highlights, high contrast",
  "focus": "shallow depth of field, ultra-sharp subject",
  "mood": "bold, surreal, high-fashion",
  "quality": "8K, ultra-realistic, photorealistic"
}

Ultra-realistic extreme close-up fashion portrait of a striking young woman with intense green eyes and wet skin covered in water droplets. Dark slicked-back damp hair with natural strands falling across her forehead. Glossy full lips, strong defined brows, dramatic eye makeup slightly smudged by moisture. A large black tarantula spider crawling on her cheek, partially resting on a beige leather glove pressed against her face. One visible metallic hoop earring. High-detail skin texture, cinematic macro photography, shallow depth of field. Studio lighting wi
```

[[Studio Lighting]] [[Surreal Fashion Editorial]]

---

### 185. 时尚专题：复古电视机前吹泡泡糖的女人

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2026-01-14  **Language**: en

> 一个超现实的时尚大片提示词，描绘了一位女性（以梅根·福克斯为原型），身穿修身露脐上衣和粉色迷你裙，斜倚在复古 CRT 电视机旁，吹着一个半透明的粉色泡泡糖泡泡。场景采用鲜艳的柔和色彩、干净的影棚灯光，以及电视屏幕镜像主体的双重现实视觉概念。

![时尚专题：复古电视机前吹泡泡糖的女人](https://cms-assets.youmind.com/media/1768468546286_e9rwju_G-otPBmWoAEgErw.jpg)

```
{
  "type": "image_generation_prompt",
  "style": "ultra_realistic_fashion_editorial",
  "composition": {
    "camera": "studio photograph",
    "lighting": "clean studio lighting",
    "focus": "sharp focus",
    "resolution": "high resolution",
    "aesthetic": "modern pop",
    "color_palette": "vibrant pastels",
    "mood": "cinematic"
  },
  "background": {
    "type": "solid",
    "color": "{argument name="background color" default="pastel yellow"}"
  },
  "subject": {
    "gender": "female",
    "appearance": {
      "hair": "long straight dark hair",
      "makeup": "glossy makeup with soft pink blush highlighted cheekbones bold eye makeup"
    },
    "attire": {
      "top": "fitted white sleeveless crop top",
      "bottom": "high waisted pink pleated mini skirt",
      "accessories": [
        "gold hoop earrings",
        "layered gold chain necklace"
      ]
    },
    "pose": {
      "position": "leaning forward",
      "interaction": "resting arms casually on a retro CRT television",
      "expression": "confident",
      "action": "blowing a translucent pink bubblegum bubble"
    }
  },
  "props": {
    "television": {
      "type": "retro CRT TV",
      "screen_content": "mirrored image of the same woman posing against a pink background",
      "effect": "dual reality visual concept"
    }
  },
  "style_tags": [
    "photorealistic",
    "fashion editorial",
    "cinematic composition",
    "creative concept",
    "pastel aesthetic"
  ]
}
```

[[Studio Lighting]] [[Pastel Color Palette]]

---

### 186. 爆炸青柠汽水罐的超逼真商业产品照片

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-01-14  **Language**: en

> 生成超逼真商业产品照片的提示，内容为青柠汽水罐在半空中爆裂。场景极具动感，细节包括冷凝水、切片青柠、薄荷叶、冰块碎片和戏剧性的水花飞溅，背景为翠绿色渐变，采用电影级影棚布光和超锐利对焦，适用于高端饮品广告。

![爆炸青柠汽水罐的超逼真商业产品照片](https://cms-assets.youmind.com/media/1768468565975_9t356e_G-oDGkzbgAAsipC.jpg)
![爆炸青柠汽水罐的超逼真商业产品照片](https://cms-assets.youmind.com/media/1768468565963_n5pm6y_G-oDGkwbIAAYHan.jpg)
![爆炸青柠汽水罐的超逼真商业产品照片](https://cms-assets.youmind.com/media/1768468565992_j4nmnn_G-oDGk3aUAA9pSG.jpg)

```
A hyper-realistic commercial product shot of a refreshing {argument name="drink flavor" default="lime"} soda can exploding with energy in mid-air. A vibrant green aluminum can covered in condensation, surrounded by sliced limes, mint leaves, and shards of ice, with a dramatic water splash bursting from the top. Lime wedges collide with the can, frozen in motion, droplets suspended in the air. Deep emerald green gradient background with glowing particles, cinematic studio lighting, high contrast highlights, ultra-sharp focus on the can, macro-level texture detail. Dynamic action composition, refreshing summer mood, premium beverage advertising style, photorealistic, 8k resolution.
```

[[Studio Lighting]]

---

### 187. 办公室休闲男士时尚模特提示

**Author**: [タナベ | 動画・音声生成AI解説](https://x.com/tanabe_fragm)  **Date**: 2026-01-13  **Language**: en

> 这是一个为 Nano Banana Pro 设计的提示词，旨在生成一张写实风格的时尚杂志编辑照片，内容为一位穿着优雅商务休闲装的白人男模特。它包含两个略有不同的版本，都强调高分辨率、细腻的皮肤纹理、柔和的影棚灯光和电影般的基调。

![办公室休闲男士时尚模特提示](https://cms-assets.youmind.com/media/1768467007344_893vki_G-hYBDsagAA2_nk.jpg)

```
Fashion magazine style photo,
a 35-year-old Caucasian male model, height 180cm, slim and well-proportioned body,
wearing elegant office casual outfit, refined and sophisticated styling,
tailored navy blazer, light beige inner shirt, slim-fit slacks, leather shoes,
clean and luxurious coordination, premium men’s fashion,
standing naturally, confident and calm expression,
studio shoot, soft diffused lighting, high-end fashion photography,
85mm lens, shallow depth of field, ultra high resolution, extremely detailed skin texture, realistic, photorealistic, cinematic tone, fashion magazine editorial quality.
High-end fashion magazine editorial photo,
a {argument name="age" default="35-year-old"} Caucasian male fashion model, {argument name="height" default="180cm"} tall, slim athletic build,
wearing refined office casual style, elegant and classy outfit,
tailored navy blazer, off-white inner shirt, slim-fit gray slacks, polished leather shoes,
minimal and sophisticated men’s fashion, luxury atmosphere,
natural standing pose, slightly turned body, calm and intelligent facial expression,
professional studio shoot, soft window light, subtle shadows,
fashion editorial lighting, premium photography,
85mm portrait lens, shallow depth of field, ultra-detailed, photorealistic skin, high resolution, no anime, no illustration, no CGI, realistic fashion phot.

Negative prompt:anime, illustration, cartoon, CGI, 3d render, doll, plastic skin, low quality, blurry, overexposed, deformed body, extra fingers, bad hands, bad face, unrealistic proportions
```

[[Studio Lighting]] [[Skin Texture Detail]] [[Photorealistic Portrait]] [[Fashion Editorial Photography]]

---

### 188. 超逼真肖像与迷你卡通自我

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-01-13  **Language**: en

> 一个用于 Gemini 的 Nano Banana Pro 提示，旨在创作一张超写实肖像：一位微笑的年轻男子，指间夹着一个迷你的皮克斯风格卡通版自己，背景是温暖的金色散景光斑和柔和的电影级影棚灯光。

![超逼真肖像与迷你卡通自我](https://cms-assets.youmind.com/media/1768466989622_ohwl08_G-hDJ7ebQAMaMs_.jpg)

```
Ultra realistic portrait of a smiling young man with black hair wearing a blue shirt, holding a tiny 3D cartoon version of himself between his fingers. The miniature character is jumping with both hands raised and wearing a blue shirt and white pants. Warm golden bokeh lights in the background. Soft cinematic studio lighting. Shallow depth of field. High detail skin texture. Natural facial expression. Playful and magical mood. Professional photography. 8k. Sharp focus. Creative concept. Pixar style mini character blended into real photo.
```

[[Studio Lighting]] [[Whimsical Art]] [[3D Character Art]] [[Hybrid Portrait]]

---

### 189. 超逼真的手工巧克力产品视觉效果

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-13  **Language**: en

> 一个高度复杂、多图像的提示结构，用于生成超逼真的手工巧克力美食摄影。它详细描述了四种不同的构图（果仁糖塔、红宝石巧克力排块、白巧克力夹心糖、黑巧克力排块），并指定了馅料、光线、纹理和背景，以营造奢华的编辑美学。

![超逼真的手工巧克力产品视觉效果](https://cms-assets.youmind.com/media/1768466907529_vbys8a_G-glpLEaAAApWp5.jpg)
![超逼真的手工巧克力产品视觉效果](https://cms-assets.youmind.com/media/1768466907478_n2ecad_G-glpKQbQAI7nOb.jpg)
![超逼真的手工巧克力产品视觉效果](https://cms-assets.youmind.com/media/1768466907407_9eaxrj_G-glpIfbQAA1iDp.jpg)
![超逼真的手工巧克力产品视觉效果](https://cms-assets.youmind.com/media/1768466908765_78xikr_G-glpNSbQAER-M1.jpg)

```
"style": "ultra-realistic food photography, luxury editorial, macro-detail, natural textures",
  "images": [
    {
      "id": "image_1",
      "subject": "assorted praline tower",
      "composition": "staggered vertical tower, center frame, loose organic stacking",
      "details": {
        "fillings": [
          "hazelnut chunks irregularly clumped at base",
          "raspberry gel naturally puddled",
          "salted caramel with realistic flow lines",
          "coffee ganache with smooth wave texture",
          "passionfruit filling with visible pulp specks"
        ],
        "accent": "one unique metallic gold nut per filling type placed at layer transitions",
        "stand": "brushed gold stand with subtle reflections"
      },
      "lighting": {
        "type": "dramatic side lighting",
        "angle": "35 degrees left",
        "effects": "authentic filling refractions, layered shadow play"
      },
      "background": "{argument name="background color 1" default="teal-to-navy"} gradient with suspended gold motes",
      "mood": "luxurious, indulgent, artisanal depth"
    },
    {
      "id": "image_2",
      "subject": "ruby chocolate tablet",
      "composition": "floating hexagonal segments above black textured paper liner",
      "details": {
        "surface": "hand-tempered imperfections, translucent ruby pink",
        "inclusions": "embedded fruit flecks visible through chocolate",
        "motion": "ruby cacao nibs falling in gravity-realistic arc from one segment"
      },
      "lighting": {
        "key": "top-down at 12 o'clock",
        "rim": "soft pink rim light at 3 o'clock",
        "effects": "authentic shadows, enhanced translucency"
      },
      "background": "black-to-warm pink radial gradient with subtle sparkle specks",
      "mood": "modern, vibrant, floating tension"
    },
    {
      "id": "image_3",
      "subject": "white chocolate bonbons",
      "composition": "organic cluster on clear glass stand",
      "details": {
        "marbling": [
          "central bonbon with irregular orange passionfruit veins",
          "surrounding bonbons with pink raspberry swirls",
          "green matcha flecks with varied density"
        ],
        "cutaway": "one bonbon sliced vertically showing gel core with real fruit speckles",
        "props": "dried fruit flecks scattered below (orange zest curls, raspberry seeds)"
      },
      "lighting": {
        "key": "soft high-key front light at 10 degrees",
        "rim": "rear rim light at 35 degrees",
        "effects": "enhanced marbling contrast and glass refractions"
      },
      "background": "soft taupe with fruit-toned bokeh",
      "mood": "elegant, fresh, handcrafted"
    },
    {
      "id": "image_5",
      "subject": "dark chocolate pistachio bar",
      "composition": "vertical bar centered on polished black granite slab",
      "details": {
        "cross_section": "precision side cut revealing layered pista
```

[[Studio Lighting]] [[Food Photography]]

---

### 190. 专业企业形象照

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-01-12  **Language**: en

> 一个用于生成适合高端企业形象照的逼真影棚肖像的提示。它指定了一位英俊的成年主体，深色头发，身穿定制的深灰色西装，并强调柔和、均匀的影棚照明、锐利的焦点和自然的皮肤纹理，模仿 85mm 镜头的效果。

![专业企业形象照](https://cms-assets.youmind.com/media/1768319091562_e9timc_G-ea7-FbIAECqYn.jpg)
![专业企业形象照](https://cms-assets.youmind.com/media/1768319092336_h7xmkd_G-ea77PbgAA0gKo.jpg)
![专业企业形象照](https://cms-assets.youmind.com/media/1768319093397_6nr2z4_G-ea77obgAANHz3.jpg)
![专业企业形象照](https://cms-assets.youmind.com/media/1768319094080_wb25vo_G-ea8CPaQAIJFhY.jpg)

```
A realistic studio portrait of a handsome adult man/woman with short, neatly styled dark hair and well-defined facial features, wearing a tailored dark gray suit, crisp white dress shirt, and a navy blue tie. He has a confident, friendly smile and a professional, polished appearance. Soft, even studio lighting, neutral gradient background, sharp focus, natural skin texture, high-end corporate headshot style, photorealistic, 85mm lens look, shallow depth of field.
```

[[Studio Lighting]] [[Natural Skin Texture]] [[85mm Lens Portrait]]

---

### 191. 超写实电影级侧面肖像提示词

**Author**: [Cuties](https://x.com/cuties7377)  **Date**: 2026-01-12  **Language**: en

> 一个高度详细、结构化的提示，旨在生成超逼真、编辑风格的人像。它指定了视觉风格、构图（90 度侧面轮廓）、主体细节（健美、自信的个体）、服装（单色运动服）以及复杂的影棚布光技术（定向侧光以增强轮廓）。此提示非常适合高端个人品牌或健身内容。

![超写实电影级侧面肖像提示词](https://cms-assets.youmind.com/media/1768319103958_12kxrp_G-dgtPgW8AA5Dz_.jpg)

```
{
  "image_type": "ultra-photorealistic portrait photography",
  "visual_style": {
    "aesthetic": "editorial, cinematic, premium",
    "vibe": "confident, elegant, eye-catching",
    "realism": "high-end professional realism"
  },
  "composition": {
    "framing": "mid-to-full body shot",
    "camera_angle": "side profile (90-degree side pose)",
    "subject_position": "slightly off-center for dynamic balance",
    "perspective": "clean side silhouette emphasis"
  },
  "subject": {
    "description": "fit, confident individual with graceful posture",
    "pose": "classic side pose with shoulders relaxed, spine elongated",
    "body_language": "poised, strong yet soft",
    "expression": "calm confidence with subtle intensity",
    "gaze": "looking forward or slightly downward"
  },
  "facial_details": {
    "emotion": "self-assured, composed",
    "micro_details": "sharp jawline, clean profile, natural skin texture"
  },
  "wardrobe": {
    "clothing": "form-fitting athletic or minimalist outfit",
    "textures": "smooth, matte fabric",
    "color_tones": "neutral or monochrome ({argument name="clothing color" default="black, beige, charcoal"})"
  },
  "lighting": {
    "type": "directional studio lighting",
    "quality": "soft but sculpting",
    "direction": "side-lit to enhance contours and depth",
    "highlight_focus": "face profile and body curves",
    "shadow_style": "gentle falloff shadows"
  },
  "color_palette": {
    "primary": [
      "soft neutrals",
      "warm skin tones",
      "muted shadows"
    ],
    "mood": "clean, elegant, modern"
  },
  "environment": {
    "location": "minimal studio or clean indoor space",
    "background": "simple gradient or solid tone",
    "atmosphere": "quiet, focused, premium"
  },
  "camera_details": {
    "lens": "50mm or 85mm portrait lens",
    "focus": "sharp focus on subject profile",
    "depth_of_field": "moderate background blur",
    "resolution": "editorial-grade clarity"
  },
  "quality_control": {
    "skin_realism": "natural texture, no plastic look",
    "anatomy_accuracy": "correct proportions",
    "ai_artifacts": "none"
  },
  "overall_mood": "strong, stylish, confident",
  "intended_use": {
    "primary": "viral post on X",
    "secondary": "fitness, lifestyle, personal branding content"
  }
}
```

[[Studio Lighting]]

---

### 192. 时尚杂志人像摄影与图形叠加提示

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2026-01-12  **Language**: en

> 为 Nano Banana Pro 生成时尚编辑肖像（带图形叠加）的高度详细提示。它指定了以深炭色背景为衬托的侧面肖像，由一个细白色矩形框住，采用柔和、情绪化的影棚照明，并以不对称方式放置白色排版（徽标/引言）。

![时尚杂志人像摄影与图形叠加提示](https://cms-assets.youmind.com/media/1768319158205_xgrewj_G-cun1RbYAAtZHO.jpg)

```
{
  "meta": {
    "image_quality": "High",
    "image_type": "Editorial/Fashion Photography with Graphic Overlay",
    "resolution_estimation": "High resolution, likely 1080x1350 or similar portrait aspect ratio",
    "file_characteristics": {
      "compression_artifacts": "Low",
      "noise_level": "Low",
      "lens_type_estimation": "Portrait lens (approx 85mm), shallow depth of field simulated or real"
    }
  },
  "global_context": {
    "scene_description": "A stylized fashion editorial composition featuring a side-profile portrait of a young woman with short, wavy brown hair. She is framed within a thin white rectangular outline against a dark, matte charcoal-grey background. To her left, outside the frame, is white typography including a logo and a quote. The lighting is soft and moody, highlighting her facial features and hair texture.",
    "environment_type": "Studio",
    "time_of_day": "Indiscernible/Controlled Studio Lighting",
    "weather_atmosphere": "Serene, Sophisticated, Melancholic, Elegant",
    "lighting": {
      "source": "Artificial Studio Softbox",
      "direction": "Front-left relative to the model (illuminating face profile) with subtle rim lighting on hair",
      "quality": "Soft, Diffused",
      "color_temperature": "Neutral to slightly warm on skin tones"
    },
    "color_palette": {
      "dominant_hex_estimates": [
        "#2C2F33",
        "#3A3D42",
        "#E8CBBF",
        "#5D4B42"
      ],
      "accent_colors": [
        "#FFFFFF",
        "#D48C7D"
      ],
      "contrast_level": "Medium-High (due to dark background vs pale skin/white text)"
    }
  },
  "composition": {
    "camera_angle": "Eye-level",
    "framing": "Medium close-up (Head and shoulders)",
    "depth_of_field": "Medium (Subject sharp, background uniform)",
    "focal_point": "The model's face in profile and the white typography",
    "symmetry_type": "Asymmetrical balance (Text on left, Subject on right)",
    "rule_of_thirds_alignment": "Model's face aligns with the right vertical third line; Text aligns with the upper-left intersection area"
  },
  "objects": [
    {
      "id": "obj_001",
      "label": "Background",
      "category": "Backdrop",
      "location": {
        "relative_position": "Full Frame",
        "bounding_box_percentage": {
          "x": 0.0,
          "y": 0.0,
          "width": 1.0,
          "height": 1.0
        }
      },
      "dimensions_relative": "Full canvas",
      "distance_from_camera": "Far",
      "pose_orientation": "Vertical plane",
      "material": "Matte paper or digital fill",
      "surface_properties": {
        "texture": "Smooth with very fine grain",
        "reflectivity": "None",
        "micro_details": "Uniform color",
        "wear_state": "New"
      },
      "color_details": {
        "base_color_hex": "#2C2F33",
        "secondary_colors": [],
        "gradient_or_pattern": "Subtle vignetting or lighting falloff towards cor"
    }
  }
}
```

[[Studio Lighting]] [[Fashion Editorial Photography]]

---

### 193. 牙齿美白贴片剥落效果的微距美容广告

**Author**: [RobertCon](https://x.com/RobertConss)  **Date**: 2026-01-11  **Language**: en

> 一个结构化的 JSON 提示词，用于生成高端、超逼真的牙齿美白贴片微距美容广告。核心概念是牙齿的“剥离”效果，展现出下方显著更洁白的笑容，并包含对灯光、构图和产品放置的具体说明。

![牙齿美白贴片剥落效果的微距美容广告](https://cms-assets.youmind.com/media/1768226032122_3annhf_G-alxpVWkAAFuz1.jpg)
![牙齿美白贴片剥落效果的微距美容广告](https://cms-assets.youmind.com/media/1768226033139_08e0hi_G-alxn6WIAAZPT7.jpg)

```
Use my attached image of my product and use the json profile that is provided to create the full picture.
New Text for Static Ad:

Headline: PEEL AWAY STAINS. REVEAL BRILLIANCE.
Body: Professional-level whitening at home. See a visibly brighter smile in just 30 minutes.
Tagline: Your brightest smile, unleashed.
{
  "meta": {
    "aspect_ratio": "4:5",
    "resolution": "8k",
    "quality": "photorealistic_macro_beauty",
    "style": "high-end beauty editorial, conceptual product advertising, clean and clinical"
  },

  "composition": {
    "subject_position": "full_frame_macro",
    "framing": "extreme close-up on the mouth and teeth of a person",
    "crop": "focused tightly on the smile from nose to chin",
    "visual_hook": "A precise, conceptual 'peeling' effect is applied *only* to the surface of the teeth, revealing a starkly whiter shade underneath."
  },

  "scene": {
    "location": "professional studio",
    "setting": "minimalist beauty background",
    "atmosphere": "fresh, transformative, and premium",
    "background": "solid, smooth neutral beige-pink, matching the original ad's aesthetic"
  },

  "lighting": {
    "primary": "soft, flattering beauty lighting to highlight skin texture and lip gloss",
    "secondary": "specular highlights on the teeth to emphasize enamel and the peeling effect",
    "effect": [
      "gentle shadows that give depth to the peeling layer on the teeth",
      "bright, clean illumination on the revealed white teeth",
      "realistic catchlights on the moist surface of the teeth and lips"
    ]
  },

  "camera_perspective": {
    "angle": "straight-on, eye-level with the mouth",
    "distance": "macro close-up",
    "look": "highly detailed, showing tooth texture and enamel"
  },

  "subject": {
    "appearance": "SEE FIRST ATTACHED IMAGE for the product application.",
    "interaction": "The person is smiling broadly. A thin, translucent layer is being peeled back from the front surface of the teeth, from left to right.",
    "specific_action": "The peel is confined *strictly* to the teeth. The lips, gums, and surrounding skin are not affected by the peeling action. The peeled layer shows a yellower, stained tooth surface, while the area underneath is brilliantly white.",
    "skin_and_lips": "Natural skin texture with visible pores, and healthy, slightly glossy lips."
  },

  "graphic_elements": {
    "the_peel": {
      "texture": "thin, transparent strip-like material, slightly crinkled as it's pulled away",
      "action": "curling away from the teeth, showing the contrast in color",
      "contrast": "dramatic difference between the stained 'before' layer and the bright 'after' teeth"
    },
    "product_placement": {
      "item": "A packet or box of the whitening strips (from your attached image) is placed in the bottom right corner.",
      "logo": "The brand logo is in the bottom left corner."
    }
  }
}
```

[[Studio Lighting]]

---

### 194. 宏伟楼梯上的高级时装肖像

**Author**: [cinema 🎥](https://x.com/FilmHub00)  **Date**: 2026-01-11  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张身穿白色缎面迷你连衣裙的年轻女性的超逼真时尚肖像。场景设置在宏伟、华丽的室内大理石和锻铁楼梯上，强调奢华美学、特定的照明条件和技术相机规格。

![宏伟楼梯上的高级时装肖像](https://cms-assets.youmind.com/media/1768226000469_axp3au_G-ZFJCzawAEdViG.jpg)

```
{
  "image_analysis": {
    "type": "Photorealistic Portrait",
    "style": "High-fashion, Elegant, Luxury aesthetic"
  },
  "subject": {
    "demographics": "Young woman, estimated early 20s",
    "physique": "Slim, fit figure with fair skinned tone",
    "hair": "Long, dark brown, sleek and straight with a center part, draping behind shoulders",
    "face": "Soft glam makeup, defined eyebrows, neutral to soft expression, looking slightly off-camera to the left"
  },
  "attire": {
    "garment": "White off-the-shoulder mini dress",
    "material": "Satin or silk finish with a sheen",
    "design_details": [
      "Sweetheart neckline with a prominent bow tied at the center bust",
      "Ruched/corset-style fitted bodice",
      "Puffed, bubble-hem skirt (voluminous and short)",
      "Draped short sleeves resting on upper arms"
    ],
    "footwear": "Clear (transparent) strap high-heeled sandals showing white pedicure",
    "accessories": "Minimalist silver stud earrings, simple rings"
  },
  "pose": {
    "stance": "Standing on a staircase, weight shifted to the back leg, front leg stepped down and slightly forward",
    "arms": "Relaxed at sides, fingers gently grazing the hem of the bubble skirt",
    "angle": "Full-body shot, slightly low angle to accentuate leg length"
  },
  "environment": {
    "location": "Grand interior staircase within a luxury building or mansion",
    "architecture": [
      "Beige/Cream marble steps",
      "Ornate black wrought-iron railing with a polished wooden handrail on the left",
      "Classic white wall paneling and molding",
      "Black and white checkered marble flooring at the base"
    ],
    "decor": [
      "Framed oil painting hanging on the upper wall",
      "White plaster relief sculpture (draped fabric style) mounted on the wall directly behind the subject",
      "Red upholstered chair visible in the upper background"
    ]
  },
  "lighting_and_atmosphere": {
    "lighting": "Warm, soft indoor ambient lighting",
    "shadows": "Subtle shadows cast against the wall and stairs, highlighting the texture of the dress",
    "mood": "Sophisticated, chic, opulent"
  },
  "technical_specifications": {
    "quality": "4K Ultra HD, Photorealistic, Masterpiece",
    "resolution": "High definition, sharp focus",
    "texture_detail": "High fidelity fabric textures, skin texture, and marble reflections",
    "camera_settings": "DSLR, portrait focal length (e.g., 85mm), shallow depth of field background"
  }
}
```

[[Studio Lighting]] [[Photorealistic Portrait]]

---

### 195. 奢华产品摄影模板

**Author**: [Mo](https://x.com/Kerroudjm)  **Date**: 2026-01-11  **Language**: en

> 这是一个多功能提示模板，专为高端编辑影棚摄影设计，非常适合展示美妆或化妆品。它允许自定义产品形状、材质、颜色、基底表面、液体和装饰元素，以实现精致、简约和有机的审美效果。

![奢华产品摄影模板](https://cms-assets.youmind.com/media/1768225967109_9jofbe_G-VLW3LWYAA4-dN.jpg)
![奢华产品摄影模板](https://cms-assets.youmind.com/media/1768225967536_vmqwwf_G-VLW3NW8AAFh-l.jpg)
![奢华产品摄影模板](https://cms-assets.youmind.com/media/1768225967914_ca5wii_G-VMeirWgAEA37p.jpg)
![奢华产品摄影模板](https://cms-assets.youmind.com/media/1768225968791_a7tra7_G-VLW3OWIAAFIJA.jpg)

```
A high-end editorial studio photograph of a {argument name="product form" default="bottle"}, made of {argument name="material" default="glass"} with a {argument name="color" default="(COLOR)"} {argument name="detail" default="cap"}. The product is placed on a natural, textured {argument name="base surface" default="stone"} slab, itself resting on a round mirror laid on a {argument name="surface tone" default="beige"} surface. Around the mirror and on the slab are scattered droplets of {argument name="liquid" default="serum"} with realistic reflections. A few sprigs of {argument name="decorative natural elements" default="lavender"} lie gently across the slab and mirror, connecting both surfaces naturally. Strong, warm sunlight filters from the top left, casting soft diagonal leaf shadows to simulate filtered daylight. The aesthetic is {argument name="visual style" default="minimalist"}, with realistic materials and natural textures highlighted by golden hour tones. Style: 3D realism, luxury product photography, shallow depth of field. Format: 1:1, ultra-detailed.
```

[[Studio Lighting]] [[Beauty Product Photography]]

---

### 196. 电影级乡村美食摄影提示模板

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-11  **Language**: en

> 一个用于生成特定国家/地区美食的超高质量、超逼真商业食品摄影的模板。它强调电影般的呈现、可见的纹理和层次、细微元素（碎屑、香料）的瞬间凝固、受控的影棚灯光以及 8K 细节的奢华食品广告美学。

![电影级乡村美食摄影提示模板](https://cms-assets.youmind.com/media/1768225964430_c8ecoa_G-XPiRcbAAAhLDE.jpg)

```
Ultra-high-quality, hyper-realistic commercial food photography of [{argument name="country food name" default="COUNTRY FOOD NAME"}], rendered in 8K detail with a (4:3 or 3:4) aspect ratio.

The food is shown in multiple premium visual variations, each highlighting texture, layers, and freshness in a cinematic way.

Food details:
– Authentic [{argument name="country cuisine" default="COUNTRY"}] cuisine presentation
– Clearly visible layers, fillings, or structure specific to [{argument name="food type" default="FOOD TYPE"}]
– Rich, natural colors and realistic textures

Motion & drama:
– Subtle mid-air elements (crumbs, ingredients, sauce, or spices)
– Natural gravity realism, frozen motion
– No mess, clean and controlled composition

Lighting & camera:
– Controlled studio lighting emphasizing texture and shine
– High-speed photography look
– Shallow to medium depth of field

Background:
– Solid or soft gradient background in [BACKGROUND COLOR]
– Clean, seamless, distraction-free

Style & finish:
– Luxury food advertising aesthetic
– Rich contrast, warm natural tones
– Ultra-sharp focus, no artificial glow

Negative prompt:
Text, logos, branding, hands, people, utensils, plates, tables, cartoon style, burnt food, overexposure, low-detail textures, artificial shine.
```

[[Studio Lighting]] [[Commercial Food Photography]]

---

### 197. 时尚肖像：穿靴子的猫 3D 角色

**Author**: [A.D.BARRY](https://x.com/aiwithadb)  **Date**: 2026-01-10  **Language**: en

> 一个用于生成高端时尚编辑肖像的提示，其中包含一个真人模特与一个照片级真实的 3D 动画角色——穿靴子的猫（Puss in Boots）进行互动。该提示详细说明了模特的脸部特征（保持不变）、服装（针织毛衣、深色牛仔裤）、穿靴子的猫的精细渲染（毛发纹理、标志性服装），以及一个带有柔和灯光的简洁影棚环境。

![时尚肖像：穿靴子的猫 3D 角色](https://cms-assets.youmind.com/media/1768143832975_8xgkt1_G-UgxNPWIAAEBHh.jpg)

```
A relaxed, premium fashion portrait in a studio setting. A real human model with a confident, charming smile and a preserved face rests an arm naturally on the shoulder of a true human scale photorealistic 3D animated character, {argument name="animated character" default="Puss in Boots"}. The human wears an oatmeal beige knitted sweater, high-waisted dark jeans, and clean white sneakers. {argument name="animated character" default="Puss in Boots"}, rendered with highly realistic ginger fur texture, expressive large eyes, and his signature leather hat, boots, and belt, stands with a suave, confident posture. The background is a clean warm taupe or neutral studio backdrop. Soft studio lighting with subtle rim light enhances the detailed fur texture and creates a natural chemistry between the subjects. 3/4 framing, high-end fashion editorial.
```

[[Studio Lighting]] [[Fashion Editorial]] [[Knit Sweater]] [[Animated Character Integration]]

---

### 198. 超逼真影棚肖像，带特定服饰

**Author**: [Creator Backstage](https://x.com/CBackstageAI)  **Date**: 2026-01-10  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张超逼真的年轻成年女性（基于安娜·德·阿玛斯 (Ana de Armas) 的形象，但具有东亚民族特征）的摄影棚肖像。它指定了她的着装（白色露脐上衣、米色迷你裙、黑色透明过膝袜）、黑色方框眼镜，以及柔和的摄影棚灯光和浅景深。

![超逼真影棚肖像，带特定服饰](https://cms-assets.youmind.com/media/1768143821197_e6ns5p_G-ScqR5WkAAKwCw.jpg)

```
{
  "metadata": {
    "version": "2.0",
    "aspect_ratio": "3:4",
    "style": "ultra-photorealistic"
  },
  "subject": {
    "identity": {
      "base_model_reference": "{argument name="base model reference" default="Ana de Armas"}",
      "ethnicity": "East Asian",
      "age_group": "young adult",
      "skin": {
        "tone": "light",
        "texture": "natural skin pores, fine details"
      }
    },
    "features": {
      "hair": {
        "color": "dark brown/black",
        "style": "long, wavy, parted in the middle",
        "texture": "voluminous, soft shine"
      },
      "eyes": {
        "color": "brown",
        "eyewear": "black square-frame glasses",
        "gaze": "direct to camera"
      },
      "makeup": {
        "style": "natural/minimalist",
        "details": [
          "defined eyes",
          "pink lip gloss"
        ]
      }
    },
    "posture": {
      "pose": "standing, facing forward",
      "head_angle": "straight",
      "arm_placement": {
        "right": "hand resting on shirt collar",
        "left": "relaxed by side"
      },
      "expression": "neutral, confident, poised"
    }
  },
  "attire": {
    "upper_body": {
      "item": "long-sleeve button-up crop top",
      "color": "white",
      "fabric_detail": "crisp cotton"
    },
    "lower_body": {
      "item": "mini-skirt with front slit",
      "color": "tan",
      "accessories": {
        "belt": "dark brown leather",
        "buckle": "silver"
      }
    },
    "legwear": {
      "type": "thigh-high stockings",
      "opacity": "sheer",
      "color": "black"
    }
  },
  "environment": {
    "setting": "studio",
    "background": {
      "wall_color": "light beige",
      "wall_texture": "smooth plaster",
      "elements": "minimalist/none"
    },
    "lighting": {
      "type": "soft studio lighting",
      "direction": "upper right",
      "shadows": "soft drop shadow on rear wall"
    }
  },
  "camera_settings": {
    "composition": {
      "shot_type": "three-quarter portrait",
      "angle": "eye-level"
    },
    "optics": {
      "lens": "85mm prime",
      "aperture": "f/2.8",
      "focus": "sharp focus on subject",
      "depth_of_field": "shallow bokeh background"
    }
  }
}
```

[[Studio Lighting]] [[White Crop Top]] [[East Asian Model]]

---

### 199. 手持微型人偶的女性肖像提示

**Author**: [Shreya Yadav](https://x.com/Shreyayadav_2)  **Date**: 2026-01-07  **Language**: en

> 一个结构化的提示，用于生成一张年轻女性的工作室肖像照，她手持一个迷你版的、卡通风格的自己的人偶。该提示详细说明了拍摄对象和人偶的外观、动作，以及工作室的灯光/背景，以营造出专注而充满爱意的画面。

![手持微型人偶的女性肖像提示](https://cms-assets.youmind.com/media/1767966116340_bttzw8_G-DOqfDakAAj_i2.jpg)

```
{
  "subject": {
    "type": "portrait",
    "description": "Young woman with warm brown hair, natural makeup, freckles, and a gentle smile.",
    "clothing": {
      "item": "t-shirt",
      "color": "yellow"
    }
  },
  "object": {
    "type": "miniature figurine",
    "description": "Stylized, cartoon version of the woman with large, expressive eyes and brown hair.",
    "pose": "sitting with hands clasped",
    "clothing": {
      "shirt": "yellow t-shirt",
      "pants": "blue jeans"
    }
  },
  "action": {
    "description": "The woman is holding the miniature figurine in her clasped hands, looking at it with affection."
  },
  "lighting": {
    "type": "studio lighting",
    "quality": "soft, directional, highlighting textures"
  },
  "background": {
    "type": "studio backdrop",
    "color": "dark, blurred black/grey"
  }
}
```

[[Studio Lighting]]

---

### 200. 超逼真的特写镜头，一片意式辣香肠披萨，芝士拉丝效果极佳

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-06  **Language**: en

> 一个图像生成提示，旨在创作一张超逼真、电影级的特写镜头，展现一片刚出炉的意式辣香肠披萨被拿起时，芝士被拉出长长丝状的戏剧性瞬间。该提示详细说明了纹理、光照和相机设置（单反相机、50 毫米镜头、浅景深），以实现高端美食广告的效果。

![超逼真的特写镜头，一片意式辣香肠披萨，芝士拉丝效果极佳](https://cms-assets.youmind.com/media/1767804067990_9dwbrs_G99UDb4bIAAuApz.jpg)

```
A hyper-realistic, cinematic close-up of a freshly baked pepperoni pizza slice being lifted from the pie, with long, dramatic cheese pulls stretching down in silky strands.
Golden, slightly charred crust with visible texture, bubbling mozzarella, glossy {argument name="topping" default="pepperoni"} slices, fresh {argument name="herb" default="basil"} leaves on top, and juicy cherry tomatoes scattered across the pizza.
Soft steam rising from the hot slice, creating a warm, mouth-watering atmosphere.
Shot on a DSLR, 50mm lens, shallow depth of field, sharp focus on the cheese stretch, background softly blurred.
Warm studio lighting with natural highlights, rich colors, realistic shadows, premium food-advertisement look.
```

[[Studio Lighting]] [[Food Photography]] [[Commercial Food Ad]] [[Macro Lens]]

---

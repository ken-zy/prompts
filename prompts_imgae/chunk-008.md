# Chunk 008

Total: 200 prompts

### 1. 6 格拍立得照片，粉色连衣裙和玫瑰

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-16  **Language**: en

> 一个高度结构化的提示，用于生成一张 2x3 拍立得风格的照片网格，内容为一位身穿粉色连衣裙的成年女性手持玫瑰，指定六种不同的姿势，采用直射机顶闪光灯照明，并呈现复古胶片美学。

![6 格拍立得照片，粉色连衣裙和玫瑰](https://cms-assets.youmind.com/media/1771310080437_v1cpap_HBTfsxiaEAAZXC2.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "photobooth_film_flash_6panel_grid_no_text",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_PHOTOBOOTH_PINK_DRESS_ROSE_6POSE"
    },
    "input": {
      "mode": "text_to_image",
      "notes": "Create a 2x3 photobooth-style collage with the same adult woman and the same outfit in all six panels. Direct on-camera flash, warm film look, casual candid expressions. No text, no logos, no watermark."
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 1,
      "layout": {
        "type": "grid",
        "rows": 3,
        "cols": 2,
        "gutter": "thin"
      },
      "sharpness": "slightly_soft_film",
      "grain": "true_film_grain"
    },
    "scene": {
      "environment": "simple indoor wall backdrop in warm beige/cream tone, minimal, photobooth feel",
      "style": "vintage film photobooth strip aesthetic, early-2000s casual editorial"
    },
    "subject": {
      "person": "adult woman",
      "hair": "shoulder-length black hair with soft volume, slightly messy playful movement",
      "makeup": "minimal natural makeup, fresh skin, soft lip tint",
      "wardrobe": {
        "dress": "{argument name="dress color and style" default="pink fitted sundress with small red/pink scattered pattern, thin straps, square neckline"}"
      },
      "prop": "{argument name="prop" default="one long-stem pale pink rose with green leaves"}"
    },
    "poses": {
      "panel_1": "standing, playful smile, holding the rose horizontally near the face, eyes closed, head tilted slightly",
      "panel_2": "standing, rose near nose as if smelling it, soft smile, eyes half-closed, relaxed shoulder",
      "panel_3": "standing, extending the rose toward the camera (slight foreshortening), gentle smile, direct eye contact",
      "panel_4": "laughing candidly, body leaning forward slightly, holding the rose close to chest, motion blur in hair",
      "panel_5": "shy giggle pose, one hand covering mouth lightly, rose held in the other hand, head down a bit",
      "panel_6": "calm pose, rose tucked behind ear like a hair accessory, subtle smile, looking at camera"
    },
    "lighting": {
      "style": "direct on-camera flash",
      "effect": "slight halation, bright face highlights, soft shadow behind subject on the wall",
      "white_balance": "warm"
    },
    "camera": {
      "look": "35mm film snapshot",
      "lens": "50mm",
      "depth_of_field": "moderate, face sharp in each panel",
      "imperfections": "tiny film softness, natural skin texture, no heavy retouch"
    },
    "negative_prompt": "text, typography, logo, watermark, extra people, extra limbs, extra fingers, deformed hands, distorted face, beauty filter, over-smooth plastic skin, HDR, ultra sharp digital look, cartoon"
  }
}
```

[[Direct Flash Photography]] [[Vintage Film Aesthetic]]

---

### 2. 巴洛克婚礼专题拍摄：直射闪光灯运用

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一对情侣的高级时装编辑婚礼肖像。场景设定在奢华的巴洛克风格酒店休息室，新娘身穿白色礼服，新郎身着黑色燕尾服。灯光风格至关重要，采用硬直射机顶闪光灯与暖色环境补光相结合，以营造戏剧性的对比和锐利的细节。

![巴洛克婚礼专题拍摄：直射闪光灯运用](https://cms-assets.youmind.com/media/1770706197340_zw48sr_HAvpD-IaUAAf9Bv.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "photoreal_cinematic_editorial_couple_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_BAROQUE_WEDDING_FLASH_EDITORIAL"
    },
    "output": {
      "aspect_ratio": "3:4",
      "resolution": "high",
      "num_images": 4
    },
    "scene": {
      "concept": "high-fashion editorial wedding couple portrait with baroque interior drama and direct flash photography",
      "environment": "luxurious baroque hotel lounge: deep red marbled wallpaper with gold veining, ornate gilded rococo sofa with cream damask upholstery, Persian carpet, two classical oil portrait paintings on the wall, tall floor lamp on the right",
      "composition": "full-body couple shot, sofa centered, bride seated on sofa, groom seated on the floor leaning against sofa, balanced negative space above with wall portraits visible"
    },
    "subject": {
      "couple": "adult bride and adult groom",
      "wardrobe": {
        "bride": "strapless embellished white wedding gown with subtle sparkle texture, elegant updo or sleek hair, minimal jewelry",
        "groom": "black tuxedo with white shirt and black bow tie, polished shoes"
      },
      "pose": "bride seated elegantly with composed expression; groom relaxed on floor leaning on sofa, one arm resting, confident gaze",
      "styling_notes": "luxury editorial, old-money wedding mood, tasteful and cinematic"
    },
    "camera": {
      "shot": "full-body editorial portrait",
      "lens_mm": 35,
      "aperture": 4.0,
      "focus": "sharp on both faces and outfits, crisp furniture details, readable room texture",
      "quality_tags": "ultra-photoreal, crisp detail, realistic skin texture, clean edges, subtle film grain"
    },
    "lighting": {
      "style": "direct on-camera flash + ambient room fill",
      "key_light": "hard direct flash from camera position producing crisp shadows",
      "ambient": "soft warm ambient fill to keep background visible",
      "notes": "avoid blown highlights on dress; preserve texture in white fabric; keep gold sofa details sharp"
    },
    "color_grade": {
      "palette": "deep red + gold + cream + black/white formalwear",
      "contrast": "editorial flash contrast, clean whites, rich reds",
      "tone": "slightly warm, filmic"
    },
    "negative_prompt": "text, logo, watermark, blur, lowres, cartoon, CGI, plastic skin, over-smoothed faces, bad anatomy, extra fingers, deformed hands, warped eyes, duplicate limbs, melted furniture, illegible faces, messy clothing folds"
  }
}
```

[[Direct Flash Photography]] [[High Fashion Editorial]] [[Couple Portrait]]

---

### 3. 复古魅力钢琴系列拼贴提示

**Author**: [AI Tales - Not by Humans](https://x.com/AITalesNBH)  **Date**: 2026-02-08  **Language**: en

> 一个 JSON 提示，用于生成一个“复古魅力钢琴系列”的 4 格拼贴画（网格）。该提示描述了一位年轻女子，她留着深色头发，涂着红色口红，身穿一件透明的、镶满水晶的紧身衣，置身于一间华丽的复古酒店房间内，房间里摆放着一架绿色立式钢琴。提示要求采用高对比度的复古美学，使用直射闪光灯摄影和鱼眼畸变效果。

![复古魅力钢琴系列拼贴提示](https://cms-assets.youmind.com/media/1770619745330_ts5f7l_HApV38rbQAAP53y.jpg)

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

[[Direct Flash Photography]]

---

### 4. 超写实名人肖像，采用直射闪光摄影

**Author**: [FL⭕RA](https://x.com/Flora_Janer8)  **Date**: 2026-02-08  **Language**: en

> 一个详细的提示，用于生成在高级餐厅环境中，名人超写实、高细节的肖像。该提示利用直射闪光摄影，营造出“狗仔队”或“Instagram 抓拍”的效果，并指定了光线、皮肤纹理和统一的姿势（双手比心形）。

![超写实名人肖像，采用直射闪光摄影](https://cms-assets.youmind.com/media/1770619669276_7v9gte_HAnsjBybQAEIP0X.jpg)
![超写实名人肖像，采用直射闪光摄影](https://cms-assets.youmind.com/media/1770619669267_51eeoj_HAnsjCiacAEH06u.jpg)
![超写实名人肖像，采用直射闪光摄影](https://cms-assets.youmind.com/media/1770619670284_sscx3y_HAnsjCAbQAAJmWf.jpg)
![超写实名人肖像，采用直射闪光摄影](https://cms-assets.youmind.com/media/1770619670926_w6gss5_HAnsjBZaoAAnZ9T.jpg)

```
"A hyper-realistic, high-detail portrait of {argument name="Celebrity Name" default="Sadie Sink"} sitting at a table in a dimly lit, upscale restaurant at night. She is looking directly at the camera with a gentle smile, making a heart shape with her hands in front of her chest. She is wearing a solid {argument name="Color" default="Red"} puff-sleeve top with a low-cut sweetheart neckline. Her skin has a dewy, luminous glow. Direct flash photography style, sharp focus on the subject, warm bokeh background with blurred restaurant lights and chandeliers, 8k resolution, cinematic lighting."
```

[[Direct Flash Photography]] [[Skin Texture Detail]] [[Paparazzi Style]]

---

### 5. 一位身穿水晶紧身衣的女士在钢琴旁，四格复古魅力拼贴画

**Author**: [unforgettwble](https://x.com/xbella_bee)  **Date**: 2026-02-08  **Language**: en

> 一个复杂、结构化的提示，旨在生成一个以“复古魅力钢琴系列”为主题的四格拼贴画，画面中一位女性（Taylor Swift）身穿透明、镶满水晶的露背连体衣。它详细说明了环境（华丽的复古酒店房间、绿色立式钢琴）、灯光（直射闪光灯、高对比度），并为四个画面中的每一个都详细描述了独特的姿势和拍摄角度。

![一位身穿水晶紧身衣的女士在钢琴旁，四格复古魅力拼贴画](https://cms-assets.youmind.com/media/1770619724027_mmxek3_HAnfDHha0AAGRE3.jpg)
![一位身穿水晶紧身衣的女士在钢琴旁，四格复古魅力拼贴画](https://cms-assets.youmind.com/media/1770619723978_tnv443_HAncN4Db0AA3dYI.jpg)

```
{
  "project_title": "Vintage Glamour Piano Series",
  "common_elements": {
    "subject": "Young woman with dark blonde hair, straight bangs, and red lipstick.",
    "outfit": "Sheer, dusty pink halter-neck bodysuit covered in large iridescent crystals and sequins, with a fringed skirt layer.",
    "environment": "Ornate vintage hotel room with pink damask wallpaper, heavy maroon curtains, patterned beige carpet, and a retro green upright piano.",
    "lighting_and_style": "Direct flash photography, high contrast, vintage aesthetic, fisheye or wide-angle lens distortion, saturated colors, 4k resolution, hyper-realistic textures."
  },
  "frames": [
    {
      "frame_id": 1,
      "position": "Top Left",
      "visual_prompt": "Low-angle fisheye shot. The subject is perched on top of a green upright piano, leaning back with knees bent. One leg is extended dramatically toward the camera lens, making the foot appear larger than life. She wears pink fishnet socks and pink strappy heels with crystal details. The focus is sharp on the texture of the fishnet and shoe in the foreground, blurring slightly toward her face.",
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

[[Direct Flash Photography]] [[Four Panel Grid]]

---

### 6. Z 世代/千禧年复古风闪光肖像，背景是贴满海报的卧室

**Author**: [Iqra Saifi](https://x.com/IqraSaifiii)  **Date**: 2026-02-04  **Language**: en

> 一个详细的提示，用于生成一张年轻女性的坦率半身肖像，她穿着一件超大号的针织毛衣，利用硬朗、直接的机顶闪光灯摄影，在贴满海报的、装饰密集的独立/复古风格卧室墙壁上投射出清晰、鲜明的阴影。

![Z 世代/千禧年复古风闪光肖像，背景是贴满海报的卧室](https://cms-assets.youmind.com/media/1770273462370_h1ngvj_HAUpg5paQAAYHm_.jpg)

```
"prompt_description": {
    "subject": {
      "appearance": "Young woman with fair skin and dark brown hair styled in a high, messy bun with loose strands framing the face. Soft, fresh makeup with rosy cheeks and mauve lips.",
      "outfit": "Oversized, cream-colored ribbed knit sweater with a wide, folded collar.",
      "environment": "Bedroom setting with a white wall densely decorated with a collage of magazine cutouts, posters, photos, and stickers (indie/retro aesthetic)."
    },
    "technical_style": "Flash photography, candid snapshot, Gen Z/Y2K aesthetic, casual and cozy vibe."
  },
  "pose_specs": {
    "body_position": "Upper body portrait (bust shot). Shoulders slightly hunched/raised in a cozy posture.",
    "head": "Tilted slightly to the side (viewer's left), creating a soft, approachable angle.",
    "expression": "Gentle, closed-mouth smile with kind eyes gazing directly at the camera."
  },
  "camera_settings": {
    "viewpoint": "Eye-level.",
    "focal_length": "28mm to 35mm (Smartphone wide lens).",
    "aperture": "f/4.0 to f/5.6 (Everything in relatively sharp focus from subject to wall).",
    "shutter_speed": "1/60s (Synced with flash).",
    "iso": "400",
    "composition": "Centered subject with a busy, textured background."
  },
  "lighting_setup": {
    "type": "Direct On-Camera Flash.",
    "qualities": "Hard, frontal lighting.",
    "shadows": " distinct, hard drop shadow visible on the poster-covered wall directly behind the subject's head and shoulders, characteristic of point-and-shoot or smartphone flash photography.",
    "color_temperature": "Cool flash white balance (approx 5500K) contrasting with the colorful background."
  }
```

[[Direct Flash Photography]]

---

### 7. 夜间海滩上逼真的智能手机闪光自拍

**Author**: [underwood](https://x.com/underwoodxie96)  **Date**: 2026-02-02  **Language**: en

> 一个高度详细的 JSON 格式提示，用于生成一张在夜晚海滩拍摄的、逼真的高角度智能手机自拍。它侧重于直射闪光灯、带有闪粉/盐粒的湿润皮肤纹理以及黑暗、私密的午夜氛围所产生的特定效果，旨在模仿社交媒体的真实感。

![夜间海滩上逼真的智能手机闪光自拍](https://cms-assets.youmind.com/media/1770100865375_qnk294_HAKfoVHaoAEoSly.jpg)

```
{"subject":{"description":"Aclose,high-anglesmartphoneselfieofayoungwomanatthebeachatnight,skinwetwithtinywaterdropletsandsubtleglitter,lookingupintothelenswithasoft,slightlysultrycalm.","mirror_rules":["notamirrorselfie","nomirroredtextorreflections"],"age":"early20s","expression":{"eyes":{"look":"directeyecontactwiththecamera","energy":"calm,confident,slightlydreamy","direction":"upwardtowardthelens"},"mouth":{"position":"slightlypartedlips","energy":"softandinviting"},"overall":"relaxedbutintense,likeaquietmidnightpausebetweenwaves"},"face":{"preserve_original":true,"makeup":"definedwingedeyeliner,longcurledlashes,brightinner-cornerhighlight,luminouscheekhighlight,softnude-pinklips"},"hair":{"color":"black","style":"wet,slickedbackwithafewloosestrandsaroundthetemples","effect":"dampshine,clingingstrands,beach-watertexture"},"body":{"frame":"slimtocurvy","waist":"notfullyvisible","chest":"visibleupperchestwithdeepVneckline","legs":"notvisible","skin":{"visible_areas":["face","neck","shoulders","upperchest","extendedforearm"],"tone":"lightwarmtone","texture":"dewyandwet,tinydropletsandfineshimmerthatfeelsslightlygrittylikesaltonskin","lighting_effect":"strongspecularhighlightsonforehead,nosebridge,cheekbones,collarbonesfromon-cameraflash"}},"pose":{"position":"standingonwetsandneartheshoreline","base":"onearmextendedholdingthephonehighaboveheadlevel","overall":"headtilteduptowardthelens,shouldersangled,intimateclosedistance"},"clothing":{"top":{"type":"halterone-pieceswimsuit(deepV)","color":"charcoalgray","details":"deepplungingneckline,smoothstretchfabric,minimalseams","effect":"slightlydarkenedbymoisture,clingssubtly"},"bottom":{"type":"one-pieceswimsuitbottom(implied)","color":"charcoalgray","details":"notclearlyvisible"}}},"accessories":{"headwear":"blacksunglassesrestingontopofthehead","jewelry":"smallstudearrings"},"photography":{"camera_style":"smartphoneselfiewithdirectflash,social-mediarealism","angle":"highanglelookingdown,subjectlookingup","shot_type":"tightportrait/upper-torsoclose-upwithextendedarmpartiallyvisible","aspect_ratio":"3:4vertical","texture":"slightsensornoise,softvignette/edgehazelikehumidlens,highcontrastflashlook","lighting":"on-cameraflashaskeylight,backgroundunderexposed,cooldarkambientfromthenightsea","depth_of_field":"subjectsharp,backgroundsoftenedbydarknessanddistance"},"background":{"setting":"nighttimebeachshoreline","wall_color":"none","elements":["darkoceanwater","whiteseafoamandbreakingwaves","wetsandnearthewaterline"],"atmosphere":"humidsaltyair,quietmidnightsurf","lighting":"backgroundmostlynaturaldarknesswithfaintcooltones;flashspillfallsoffquickly"},"the_vibe":{"energy":"low,intimate,after-swimadrenalinefadingintocalm","mood":"midnightbeachglow,privateandcinematic","aesthetic":"realisticsmartphoneflashportrait,glossyskinhighlights,darkoceanbackdrop","authenticity":"slightlyimperfectframing,naturalwethair,flashglareandedgevignette","in
```

[[Direct Flash Photography]]

---

### 8. 豪车内女性直闪人像摄影提示

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-02-01  **Language**: en

> 一个结构化的 JSON 提示，用于生成一张逼真的、抓拍的女性肖像（类似 Sadie Sink），她坐在一辆豪华轿车的后座，在夜晚，强调直射闪光摄影、细致的纹理和都市夜景美学。

![豪车内女性直闪人像摄影提示](https://cms-assets.youmind.com/media/1770014608205_lh7ixk_HADzxXpWYAAHugC.jpg)
![豪车内女性直闪人像摄影提示](https://cms-assets.youmind.com/media/1770014608277_f9td2v_HADzxXqXEAAl2eC.jpg)

```
{
  "prompt": {
    "subject": {
      "description": "A young woman with shoulder-length, curly red hair and bangs. She has fair skin with light freckles, winged eyeliner, and a septum piercing. Her expression is sultry, with her index finger resting gently on her lower lip.",
      "clothing": "She is wearing a tight, long-sleeved black mini dress and sheer black pantyhose.",
      "pose": "She is seated in the back of a car with her legs crossed and pulled up towards her chest, displaying bare feet in sheer hose."
    },
    "environment": {
      "location": "Interior of a luxury car, specifically the back seat.",
      "details": "Light grey leather seats with diamond stitching patterns visible on the side door panel. A 'B' logo (likely Bentley) is embroidered on the headrest.",
      "background": "Through the car window, a night cityscape is visible with blurred city lights, street lamps, and streaks of light from moving traffic on a highway."
    },
    "lighting_and_quality": {
      "lighting": "Direct flash photography illuminating the subject against a darker background.",
      "resolution": "4K HD quality, highly detailed textures on the hair, skin, and leather seats.",
      "style": "Candid, urban night aesthetic, realistic photo."
    }
  }
}
```

[[Direct Flash Photography]] [[Celebrity Lookalike Portrait]]

---

### 9. 奢华衣橱时尚大片拍摄

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-24  **Language**: en

> 一个高度结构化的 JSON 提示，详细描述了一场在奢华步入式衣帽间内进行的高级时装编辑摄影，主角是两位身穿同款紧身胸衣式迷你连衣裙的女性，强调直射闪光摄影、高对比度以及纹理的超逼真渲染。

![奢华衣橱时尚大片拍摄](https://cms-assets.youmind.com/media/1769322259254_786qn2_G_arjp-aEAAchll.jpg)
![奢华衣橱时尚大片拍摄](https://cms-assets.youmind.com/media/1769322259353_z3j9ms_G_arjhWaQAAkE_P.jpg)

```
{
  "prompt_details": {
    "subjects": [
      {
        "id": "subject_standing",
        "appearance": {
          "gender": "Female",
          "skin_tone": "Fair",
          "hair": "Long, dark brown, loose waves, center part",
          "makeup": "Full glam, heavy contour, nude lip, defined brows"
        },
        "pose": "Standing, leaning back against shelving, weight on left leg, right leg bent at knee (flamingo pose), left hand touching hair, right arm resting on shelf, looking away from camera",
        "outfit": {
          "garment": "{argument name="standing subject dress color" default="Taupe/beige"} halter neck mini dress, deep plunging neckline, corset-style laced bodice, fitted skirt, draped fabric train in back",
          "shoes": "Clear/Silver strappy high heels",
          "accessories": "Large gold drop earrings, thin necklace, stacked diamond bracelets"
        }
      },
      {
        "id": "subject_crouching",
        "appearance": {
          "gender": "Female",
          "skin_tone": "Light",
          "hair": "Long, blonde, voluminous waves, center part",
          "makeup": "Full glam, smokey eye, glossy lip"
        },
        "pose": "Crouching/squatting low in profile, head turned to look directly at camera, hand resting near chin",
        "outfit": {
          "garment": "{argument name="crouching subject dress color" default="White"} halter neck mini dress, matching style to standing subject, corset-style laced detailing, fitted silhouette",
          "shoes": "Silver metallic high heel sandals",
          "accessories": "Diamond bracelet on wrist"
        }
      }
    ],
    "environment": {
      "location": "Luxury walk-in closet",
      "architecture": "White built-in shelving units, minimalistic design",
      "props": [
        "Various luxury handbags displayed on shelves (Hermes Birkin/Kelly styles in pink, green, white, black)",
        "Designer clutch bags",
        "Gold high heel shoes visible on lower shelf"
      ],
      "flooring": "Beige textured carpet"
    },
    "lighting": {
      "style": "Direct flash photography",
      "quality": "Hard lighting, high contrast, distinct shadows cast on white walls behind subjects",
      "atmosphere": "Night out, party prep, exclusive, influencer aesthetic"
    },
    "camera_settings": {
      "viewpoint": "Eye-level",
      "shot_type": "Full body / Medium-wide shot",
      "style": "Editorial candid",
      "resolution": "8k",
      "realism": "Ultra-photorealistic, high fidelity textures (skin pores, fabric weave, leather grain)"
    }
  }
}
```

[[Direct Flash Photography]] [[High Contrast]] [[Texture Realism]] [[Corset Mini Dress]]

---

### 10. 奢华步入式衣帽间专题（双人）

**Author**: [Iris](https://x.com/xIrissy)  **Date**: 2026-01-24  **Language**: en

> 一个高度结构化的 JSON 提示词，用于 Gemini Nano Banana Pro 生成一张超写实编辑图片，描绘两名女性（萨迪·辛克/米莉·芭比·布朗 和 亚历山德拉·达达里奥/杜阿·利帕 风格）穿着配套的紧身胸衣式迷你连衣裙，在豪华步入式衣帽间内摆姿势，采用直射闪光摄影和高对比度。

![奢华步入式衣帽间专题（双人）](https://cms-assets.youmind.com/media/1769322336175_ak4hwi_G_ajNK7WMAEG1Ai.jpg)
![奢华步入式衣帽间专题（双人）](https://cms-assets.youmind.com/media/1769322336707_0lvnf1_G_ajNK6XgAEE3Pf.jpg)

```
{
  "prompt_details": {
    "subjects": [
      {
        "id": "subject_standing",
        "appearance": {
          "gender": "Female",
          "skin_tone": "Fair",
          "hair": "Long, dark brown, loose waves, center part",
          "makeup": "Full glam, heavy contour, nude lip, defined brows"
        },
        "pose": "Standing, leaning back against shelving, weight on left leg, right leg bent at knee (flamingo pose), left hand touching hair, right arm resting on shelf, looking away from camera",
        "outfit": {
          "garment": "Taupe/beige halter neck mini dress, deep plunging neckline, corset-style laced bodice, fitted skirt, draped fabric train in back",
          "shoes": "Clear/Silver strappy high heels",
          "accessories": "Large gold drop earrings, thin necklace, stacked diamond bracelets"
        }
      },
      {
        "id": "subject_crouching",
        "appearance": {
          "gender": "Female",
          "skin_tone": "Light",
          "hair": "Long, blonde, voluminous waves, center part",
          "makeup": "Full glam, smokey eye, glossy lip"
        },
        "pose": "Crouching/squatting low in profile, head turned to look directly at camera, hand resting near chin",
        "outfit": {
          "garment": "White halter neck mini dress, matching style to standing subject, corset-style laced detailing, fitted silhouette",
          "shoes": "Silver metallic high heel sandals",
          "accessories": "Diamond bracelet on wrist"
        }
      }
    ],
    "environment": {
      "location": "Luxury walk-in closet",
      "architecture": "White built-in shelving units, minimalistic design",
      "props": [
        "Various luxury handbags displayed on shelves (Hermes Birkin/Kelly styles in pink, green, white, black)",
        "Designer clutch bags",
        "Gold high heel shoes visible on lower shelf"
      ],
      "flooring": "Beige textured carpet"
    },
    "lighting": {
      "style": "Direct flash photography",
      "quality": "Hard lighting, high contrast, distinct shadows cast on white walls behind subjects",
      "atmosphere": "Night out, party prep, exclusive, influencer aesthetic"
    },
    "camera_settings": {
      "viewpoint": "Eye-level",
      "shot_type": "Full body / Medium-wide shot",
      "style": "Editorial candid",
      "resolution": "8k",
      "realism": "Ultra-photorealistic, high fidelity textures (skin pores, fabric weave, leather grain)"
    }
  }
}
```

[[Direct Flash Photography]] [[High Contrast]] [[Corset Mini Dress]]

---

### 11. 雪城中的 Q 版娃娃角色

**Author**: [Lunarion Art](https://x.com/lunarionart)  **Date**: 2026-01-21  **Language**: en

> 一个用于生成 3D 风格化、玩偶般（Q 版风格）年轻女性角色的提示，场景设定在雪中的城市。它详细描述了角色的特征（大头、冰蓝色眼睛、铂金色编发）、服装（蓬松的白色仿皮草大衣、粉色围巾、耳罩）、环境（黄昏、模糊的街灯）和艺术风格（3D 渲染、光滑的乙烯基材质、直射闪光摄影）。

```
Subject: 3D stylized doll-like character of a young woman with a large head and icy blue eyes. Features: Long platinum blonde hair braided to the side, rosy cheeks from the cold, wearing earmuffs. Attire: A fluffy white faux-fur coat, a pastel pink knitted scarf, and glossy white boots. Environment: A snowy city street at twilight with blurred streetlights in the background. Art Style: 3D render with a smooth vinyl texture, lighting style is direct flash photography with sharp shadows against the snow, fashionable and cute aesthetic
```

[[Direct Flash Photography]] [[Ice Blue Eyes]] [[White Faux Fur Coat]] [[3D Chibi Character]]

---

### 12. 现代版多萝西·盖尔美学，搭配直射闪光灯

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2026-01-20  **Language**: en

> 一个高度细致、照片般逼真的提示，生成一个身着现代化多萝西·盖尔（Dorothy Gale）服装（蓝色格子迷你连衣裙，红宝石色闪光高跟鞋）的年轻女性全身图像。场景设置在夜间的半户外庭院中，利用直射机内闪光灯摄影营造出硬光、高对比度，并在主体身后的墙壁上投射出清晰的阴影。

![现代版多萝西·盖尔美学，搭配直射闪光灯](https://cms-assets.youmind.com/media/1768977370474_ujac13_G_HHH0iWYAAbhhq.jpg)
![现代版多萝西·盖尔美学，搭配直射闪光灯](https://cms-assets.youmind.com/media/1768977370507_mxddr5_G_AihfGXQAA5J6l.jpg)

```
{
  "prompt_structure": {
    "subject": {
      "demographics": "Young female adult with a slender, fit physique",
      "hair": "Long dark brown hair styled in two playful braids (pigtails) resting on shoulders",
      "face": "Soft, attractive features with a slight smile, gazing upwards to the right, wearing bright red lipstick and subtle eye makeup"
    },
    "outfit": {
      "costume_theme": "Modernized Dorothy Gale from Wizard of Oz aesthetic",
      "dress": "Blue and white gingham check mini dress featuring a corset-style bodice with vertical boning, sweetheart neckline, and white lace ruffle trim at the hem and neckline",
      "legwear": "Opaque white knee-high stockings featuring large light blue satin bows at the top cuffs",
      "footwear": "Sparkling ruby red glitter pumps (heels) with ankle straps (Mary Jane style)"
    },
    "accessories": {
      "hair": "Red satin ribbons tied into bows at the base of each braid",
      "handheld": "Holding a beige woven straw tote bag/basket in the right hand"
    },
    "pose_and_action": {
      "stance": "Full-body standing pose, legs crossed at the ankles in a playful manner",
      "arms": "Right arm extended down holding the bag, left arm slightly bent and extended back as if balancing or leaning",
      "expression": "Charming, confident, and whimsical mood"
    },
    "environment": {
      "setting": "Semi-outdoor patio or courtyard entrance at night",
      "architecture": "Large wooden double doors with glass panels in the background, white stucco walls, dark wooden support pillar in the foreground",
      "details": "Terracotta tiled flooring, faint glimpse of a railing and indoor plants in the background, a large mirror frame visible on the far left edge"
    },
    "lighting": {
      "style": "Direct on-camera flash photography",
      "characteristics": "Hard lighting creating a distinct shadow of the subject on the wall behind, high contrast between the illuminated subject and the dimmer background, capturing the sparkle of the shoes and sheen of the fabric"
    },
    "camera_technical": {
      "perspective": "Eye-level to slightly low angle full shot",
      "focal_length": "35mm for a lifestyle snapshot feel",
      "quality": "Ultra photorealistic, 8K resolution, sharp focus on subject",
      "textures": "Detailed fabric weave on the gingham, realistic glitter texture on shoes, skin texture visibility"
    }
  }
}
```

[[Direct Flash Photography]] [[High Contrast Photography]] [[Costume Portrait]]

---

### 13. 现代化多萝西·盖尔服装肖像提示

**Author**: [Iris](https://x.com/xIrissy)  **Date**: 2026-01-19  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张超逼真的年轻女性全身肖像，其造型是《绿野仙踪》中现代化后的多萝西·盖尔。它详细描述了复杂的服装细节（紧身胸衣式格子迷你连衣裙、红宝石色闪光高跟鞋）、俏皮的姿势（双腿交叉，手持草编手提包），以及技术设置，例如用于高对比度的直射机内闪光摄影和 8K 分辨率。

![现代化多萝西·盖尔服装肖像提示](https://cms-assets.youmind.com/media/1768890690849_0kzyvk_G_AihfGXQAA5J6l.jpg)

```
{
  "prompt_structure": {
    "subject": {
      "demographics": "Young female adult with a slender, fit physique",
      "hair": "Long dark brown hair styled in two playful braids (pigtails) resting on shoulders",
      "face": "Soft, attractive features with a slight smile, gazing upwards to the right, wearing bright red lipstick and subtle eye makeup"
    },
    "outfit": {
      "costume_theme": "Modernized Dorothy Gale from Wizard of Oz aesthetic",
      "dress": "{argument name="dress pattern" default="Blue and white gingham check"} mini dress featuring a corset-style bodice with vertical boning, sweetheart neckline, and white lace ruffle trim at the hem and neckline",
      "legwear": "Opaque white knee-high stockings featuring large light blue satin bows at the top cuffs",
      "footwear": "Sparkling ruby red glitter pumps (heels) with ankle straps (Mary Jane style)"
    },
    "accessories": {
      "hair": "Red satin ribbons tied into bows at the base of each braid",
      "handheld": "Holding a beige woven straw tote bag/basket in the right hand"
    },
    "pose_and_action": {
      "stance": "Full-body standing pose, legs crossed at the ankles in a playful manner",
      "arms": "Right arm extended down holding the bag, left arm slightly bent and extended back as if balancing or leaning",
      "expression": "Charming, confident, and whimsical mood"
    },
    "environment": {
      "setting": "Semi-outdoor patio or courtyard entrance at night",
      "architecture": "Large wooden double doors with glass panels in the background, white stucco walls, dark wooden support pillar in the foreground",
      "details": "Terracotta tiled flooring, faint glimpse of a railing and indoor plants in the background, a large mirror frame visible on the far left edge"
    },
    "lighting": {
      "style": "Direct on-camera flash photography",
      "characteristics": "Hard lighting creating a distinct shadow of the subject on the wall behind, high contrast between the illuminated subject and the dimmer background, capturing the sparkle of the shoes and sheen of the fabric"
    },
    "camera_technical": {
      "perspective": "Eye-level to slightly low angle full shot",
      "focal_length": "35mm for a lifestyle snapshot feel",
      "quality": "Ultra photorealistic, 8K resolution, sharp focus on subject",
      "textures": "Detailed fabric weave on the gingham, realistic glitter texture on shoes, skin texture visibility"
    }
  }
}
```

[[Direct Flash Photography]] [[8K Photography]] [[Costume Portrait]]

---

### 14. 硬闪光摄影快照，姿态不羁

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-01-18  **Language**: en

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

[[Direct Flash Photography]] [[High Contrast Lighting]] [[Snapshot Aesthetic]] [[Yellow Bikini]]

---

### 15. 车内后座夜间闪光人像 (iPhone 风格)

**Author**: [inanna](https://x.com/inannaai)  **Date**: 2026-01-17  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张超逼真的女性肖像，她夜晚坐在汽车后座上斜倚着，强调原始 iPhone 摄影的真实感、具体的姿势细节，以及夜晚闪光灯对其铂金色头发和黑色服装的影响。

![车内后座夜间闪光人像 (iPhone 风格)](https://cms-assets.youmind.com/media/1768717557675_ntk8l1_G-5mqhoXUAATg_-.jpg)

```
{
"subject": {
"character": "uploaded_photo",
"face_consistency": "true",
"body_consistency": "true",
"gender": "female",
"age_appearance": "young adult, early 20s",
"ethnicity": "Northern European",
"emotion": "composed, soft confidence, direct gaze, late-night editorial",

"hair": {
"color": "icy platinum blonde",
"length": "shoulder-length",
"style": "voluminous waves with a side part",
"texture": "silky, fine, high-shine under artificial light",
"placement": "cascading over shoulders, one hand lightly touching the hair near the temple"
},

"face": {
"visibility": "fully visible, centered",
"profile_visibility": "full frontal",
"skin_tone": "fair, porcelain, luminous",
"expression": "neutral, relaxed lips, intense but soft eye contact"
}
},

"meta": {
"aspect_ratio": "1:1",
"camera": "iPhone 15 Pro Max, Rear Main Camera",
"lens": "24mm f/1.78 aperture equivalent",
"focal_character": "sharp subject focus, natural depth of field, high dynamic range",
"quality": "ultra photorealistic, 8k resolution, raw mobile photography",
"style": "nighttime flash photography, raw iPhone realism, natural skin texture, subtle digital noise in shadows"
},

"visibility_rules": {
"mirror_only": false,
"no_direct_subject_visibility": false,
"no_body_parts_outside_frame": false
},

"camera_angle": {
"vertical_position": "eye level with the subject",
"horizontal_alignment": "centered directly in front of the subject",
"tilt": "0 degree, straight-on shot",
"yaw": "facing directly toward the subject",
"roll": "perfectly level",
"distance_to_subject_meters": 0.8,
"handheld_behavior": "stable, intentional framing"
},

"body_angle": {
"global_orientation": "seated and reclined in a car backseat",
"torso_rotation_degrees": 10,
"shoulder_alignment": "relaxed, leaning back against leather upholstery",
"hip_rotation_degrees": 45,
"weight_distribution": "seated comfortably, reclining into the seat corner",
"posture": "relaxed, effortless lounge"
},

"head_angle": {
"rotation_degrees": 5,
"tilt": "slight upward tilt",
"chin_position": "slightly lifted",
"neck_tension": "relaxed"
},

"pose": {
"legs": {
"stance": "crossed at the thighs",
"front_leg": "draped over the other, extending toward the camera",
"back_leg": "tucked underneath"
},
"hips": {
"action": "settled into the seat cushion"
},
"arms": {
"right_arm": "elbow resting on the seat, hand gently lifting hair",
"left_arm": "extended downward, hand resting naturally on the seat cushion"
}
},

"clothing": {
"outfit_type": "two-piece set",
"color": "solid matte black",
"top": "strapless bandeau/tube top",
"bottom": "matching high-waisted mini skirt",
"material": "stretch fabric, body-con",
"fit": "tight, form-fitting",
"coverage": "midriff-baring, revealing legs",
"style": "minimalist chic, evening wear"
},

"accessories": {
"shoes": "black thin-strap high-heeled sandals, wrap-around ankle straps",
"nails": "natural medium length, soft neutral polish"
},

"environment": {
"lo"
}
}
```

[[Direct Flash Photography]] [[Platinum Hair Portrait]]

---

### 16. 华丽亮粉色晚礼服肖像，搭配频闪灯光

**Author**: [Emma](https://x.com/emmagpt0)  **Date**: 2026-01-17  **Language**: en

> 一个详细的 JSON 提示，用于生成一张魅力十足、高对比度的女性肖像。她身穿一件热粉色高开衩缎面晚礼服，夜晚站在高档的屋顶阳台上。该提示指定使用刺眼的机内闪光灯照明，以营造锐利的阴影并突出反光面料，模仿狗仔队抓拍的效果。

![华丽亮粉色晚礼服肖像，搭配频闪灯光](https://cms-assets.youmind.com/media/1768717553797_s8kmb2_G-5TrJwXkAA9Itf.jpg)

```
"subject": {

"identity_likeness": "Young adult female celebrity, striking resemblance",

"facial_features_expression": "Face is angled downwards in a demure, contemplative look; eyes are downcast with prominent eyelashes; lips are full with a neutral/nude shade; flawless, warm skin tone",

"makeup": "Glowy evening makeup, defined cheekbones with highlighter, soft smoky eye shadow in neutral tones, groomed eyebrows",

"body_language": "Standing pose with weight shifted to the right hip, creating a gentle S-curve; left leg is seductively extended forward through the high slit; left hand rests lightly on the upper thigh with manicured nails; right arm hangs relaxed by the side"

},

"fashion": {

"garment_details": "A striking {argument name=\"dress color\" default=\"hot pink (magenta/fuchsia)\"} evening gown rendered in a luxurious, reflective satin or silk fabric that shimmers under the light. The design features a halter neck strap, a daringly deep sweetheart neckline with plunging cleavage, and intricate ruching/gathering at the waist that creates a flattering draped effect. A daring, ultra-high thigh-high slit on the left side reveals the leg. The skirt falls in soft folds to the floor",

"footwear": "Black, open-toe high-heeled mules. The strap across the toes appears to be embellished with subtle sparkles, crystals, or a textured material that catches the light",

"accessories": "A statement stack of layered necklaces in silver tone; includes at least two distinct chains, one chunkier curb link chain and another finer chain possibly with small pave diamond links or crystals. No earrings are visible due to the hair styling"

},

"environment": {

"location_setting": "An upscale outdoor balcony or rooftop terrace at night, likely penthouse level",

"foreground_elements": "A modern, grey painted metal railing runs horizontally behind the subject. The balcony floor appears to be concrete or stone. The immediate wall is a plain, light beige/off-white stucco",

"background_cityscape": "A blurred, bokeh-filled urban night view. Numerous windows in distant buildings emit warm yellow and orange lights. A distinct red neon sign is visible in the mid-ground on a building facade. The skyline suggests a dense European or cosmopolitan city. The sky is a deep, dark indigo blue, not completely black",

"atmosphere_mood": "Glamorous, exclusive, sophisticated, slightly moody, paparazzi-style capture of a private moment"

},

"technical_specs": {

"lighting_style": "Dominant, direct on-camera flash or hard strobe lighting. This creates a high-contrast look, brightly illuminating the subject and the reflective pink dress while casting distinct, sharp shadows behind her on the balcony wall and making the background lights pop",

"color_palette": "Vibrant magenta/hot pink as the focal color, contrasted with deep midnight blues and blacks of the night, warm golds/yellows from city lights, and cool silver from accessories",

"focus_dof": "Sharp focus on the subject and her atti"
```

[[Direct Flash Photography]] [[Night Photography]] [[Glamour Portrait]] [[Rooftop Setting]]

---

### 17. 夜间海滩闪光照片（网红美学）

**Author**: [Bananai](https://x.com/aibananai)  **Date**: 2026-01-17  **Language**: en

> 一个高度详细的提示，用于生成一张超逼真的闪光照片：一名女性在夜晚跪在浅海水中，强调湿润的皮肤纹理、智能手机闪光灯带来的高对比度照明，以及自信、挑衅的网红美学。

![夜间海滩闪光照片（网红美学）](https://cms-assets.youmind.com/media/1768717521955_9cqect_G-440xAX0AAEBcT.jpg)

```
{
  "meta": {
    "aspect_ratio": "4:5",
    "quality": "ultra_photorealistic",
    "resolution": "8k",
    "camera": "iPhone with Direct Flash",
    "lens": "24mm wide",
    "style": "high-end Instagram aesthetic, flash photography, raw candid realism, wet skin texture"
  },

  "scene": {
    "location": "Urban beach coastline at night ({argument name="location" default="Miami or Dubai"} style)",
    "environment": [
      "shallow ocean water",
      "city skyline lights in distance",
      "wet sand underneath",
      "dark ocean waves with white foam",
      "golden reflections of city lights on water"
    ],
    "time": "late night",
    "atmosphere": "sultry, spontaneous night swim, confident influencer vibe, warm humid night"
  },

  "lighting": {
    "type": "Direct on-camera flash (hard lighting)",
    "key_light": "bright cool-white smartphone flash illuminating subject directly",
    "fill_light": "ambient golden glow from distant city lights",
    "contrast": "high contrast between bright subject and dark background",
    "effect": "specular highlights on wet skin and makeup, sharp drop shadows hidden by water, high-gloss finish"
  },

  "camera_perspective": {
    "pov": "eye-level shot",
    "angle": "front-facing",
    "framing": "full body kneeling (knees to head)",
    "distance": "1.5–2 meters",
    "motion": "still pose"
  },

  "subject": {
    "gender": "female",
    "age": "early 20s",
    "ethnicity": "Caucasian / White",
    
    "body": {
      "type": "slim-thick fit",
      "skin": "tanned, wet, visible skin texture (pores, goosebumps from cold water)",
      "chest": "naturally full, enhanced by bikini cut",
      "waist": "toned abs visible",
      "thighs": "smooth and athletic"
    },

    "hair": {
      "color": "dirty blonde / ash blonde",
      "length": "long",
      "style": "two high playful pigtails",
      "texture": "slightly messy, windblown strands, soft waves"
    },

    "face": {
      "expression": "seductive, eyes closed or looking down, chin tilted up, 'baddie' attitude",
      "makeup": "heavy glam night makeup, sharp contour, matte lipstick, heavy winged eyeliner",
      "details": "flash reflection on forehead and cheekbones"
    },

    "pose": {
      "position": "kneeling in shallow water",
      "legs": "knees spread apart (V-shape)",
      "hands": "resting on upper thighs/hips",
      "posture": "spine arched slightly, chest pushed forward",
      "energy": "confident, dominant, provocative"
    },

    "outfit": {
      "bikini": {
        "color": "{argument name="bikini color" default="chocolate brown"}",
        "top": "triangle halter top, gathered fabric",
        "bottom": "matching string thong bikini, high cut on hips"
      },
      "accessories": {
        "neck": "silver pendant necklace",
        "waist": "layered silver belly chains draping over hips",
        "wrists": "silver bracelet stack on left wrist"
      }
    }
  },

  "details": {
    "vibe": "viral social media post, flash photograp"
  }
}
```

[[Direct Flash Photography]] [[High Contrast]] [[Influencer Aesthetic]] [[Wet Skin Texture]]

---

### 18. 抓拍后台闪光肖像

**Author**: [tusina](https://x.com/tusinaai)  **Date**: 2026-01-17  **Language**: en

> 一个用于生成逼真的、抓拍式的时尚/后台肖像的提示，采用直射机顶闪光灯美学，重点突出原始纹理、自然色彩和极简的影棚/后台环境。

![抓拍后台闪光肖像](https://cms-assets.youmind.com/media/1768717523808_5vqf6t_G-43tJ0XsAAFDvM.jpg)

```
{
  "prompt": "Photorealistic candid fashion/backstage portrait indoors. Medium close-up framing of the subject standing with both arms raised behind the head, looking off to the side with a calm, slightly serious expression. Long loose hair with soft natural waves, warm skin highlights. Wearing a simple black slip dress with thin straps. Background: textured light brick wall and a minimal clothing rack with hangers/garments, subtle studio/backstage vibe. Direct on-camera flash look with bright specular highlights and gentle falloff, slight grain, natural color, editorial realism, high detail, no overprocessing.",
  "negative_prompt": "nudity, explicit sexual content, porn, lingerie, fetish, cameltoe, see-through clothing, exaggerated body proportions, unrealistic anatomy, deformed hands, extra fingers, missing fingers, fused limbs, distorted face, cross-eye, blurry, out of focus, low resolution, plastic skin, over-smoothed skin, heavy HDR, oversaturated, harsh flash, watermark, logo, text, caption, jpeg artifacts, cartoon, anime, CGI",
  "params": {
    "aspect_ratio": "4:5",
    "size": "1024x1280",
    "steps": 30,
    "cfg_scale": 6.5,
    "sampler": "DPM++ 2M Karras",
    "seed": -1
  },
  "camera": {
    "shot_type": "floor-level close-up selfie",
    "lens": "20-24mm wide-angle",
    "focal_style": "wide perspective, realistic distortion",
    "depth_of_field": "moderate (subject sharp, background slightly softer)"
  },
  "lighting": {
    "source": "natural daylight",
    "quality": "soft, warm",
    "contrast": "medium"
  },
  "environment": {
    "location": "CrossFit / functional training gym",
    "key_props": ["rubber mat", "squat rack", "gymnastic rings", "plants/greenery"],
    "mood": "clean, energetic, candid"
  }
}
```

[[Direct Flash Photography]] [[Candid Photography]]

---

### 19. 高对比度闪光摄影夜生活人像

**Author**: [brindley](https://x.com/brindleyai)  **Date**: 2026-01-17  **Language**: en

> 一个详细的提示，用于生成一张超现实的、闪光灯风格的女性肖像，背景设定在一家高档、光线昏暗的酒吧。该提示侧重于后方四分之三视角，强调拍摄对象的体型、露背连衣裙，以及温暖的环境背景光（带有焦外虚化光斑）与拍摄对象身上冷色调的直射闪光灯光线之间的对比。

![高对比度闪光摄影夜生活人像](https://cms-assets.youmind.com/media/1768717529554_bztboj_G-4Xt32WsAAJSrO.jpg)

```
{
"subject": "Young adult female with tanned, glowing skin and long, voluminous hair featuring blonde balayage highlights and loose waves. She is wearing a cream-colored, off-the-shoulder mini dress with a subtle, abstract light brown leaf or animal print. The dress features long sleeves with elastic cuffs and a distinct open-back design secured by thin spaghetti strap ties at the lower back. Her physique is fit and curvaceous, with a visibly arched back, small waist, and a full, prominent bust profile visible from the side. The dress fabric appears lightweight and textured, draping naturally over her curves.",
"pose": "Seated on a high bar stool, angled with her back three-quarters towards the camera (rear 3/4 view). Her torso is twisted slightly to the left, and her head is turned fully to the left in a sharp side profile, looking away from the viewer. Her left arm is raised, with her hand delicately touching the crown of her head or running through her hair. Her right arm rests naturally by her side. Her posture highlights the curve of her spine and the definition of her back muscles.",
"environment": "An upscale, dimly lit bar or lounge setting. Behind the subject is a wooden back bar with glass shelving displaying various liquor bottles. A festive evergreen garland adorned with warm white Christmas lights runs along the top of the shelving unit. The bar counter itself has a metallic, zinc-style surface. On the counter sits a stemmed cocktail glass containing a pinkish-red drink with an orange peel garnish on a white napkin, alongside a small, lit red votive candle.",
"camera": "Medium shot capturing the subject from the mid-thighs up. The camera is positioned at approximately eye level or slightly above, emphasizing the subject's back and profile. A shallow depth of field is used, keeping the subject in sharp focus while blurring the background lights into soft bokeh. The perspective creates a sense of intimacy and immediacy.",
"lighting": "A mix of ambient warm bar lighting and a direct, flash-style source illuminating the subject. The background features warm, glowing bokeh from the garland lights and shelf illumination. The subject is lit by a cool-toned, direct flash or strobe from the front-right (relative to the camera), creating high contrast on her skin, highlighting the texture of the dress, and casting a soft shadow on the bar counter to her left. Skin reflectivity is high due to the direct light.",
"mood_and_expression": "Candid, sophisticated, and slightly pensive. The subject appears unaware of the camera or is posing in a 'caught in the moment' style. The mood is festive yet intimate, evoking a night out at a high-end venue.",
"style_and_realism": "High-fidelity realism with a flash-photography aesthetic common in social media nightlife portraits. Sharp details on hair strands, skin texture, and fabric weave. Realistic representation of light interaction with the metall
```

[[Direct Flash Photography]] [[Bokeh Background]] [[Backless Dress]]

---

### 20. 硬闪光摄影街头风格

**Author**: [Bananai](https://x.com/aibananai)  **Date**: 2026-01-17  **Language**: en

> 一个高度详细的提示，用于生成一张超逼真的图像，使用硬直射机载闪光灯，捕捉一个酷炫、叛逆、富裕的夜生活场景，画面中有一个主体和一辆豪华跑车（保时捷 911 GT3 RS），置身于一个黑暗的停车场。

![硬闪光摄影街头风格](https://cms-assets.youmind.com/media/1768717509811_25dt03_G-4QPHtXgAAza5-.jpg)
![硬闪光摄影街头风格](https://cms-assets.youmind.com/media/1768717509888_aw0nx8_G-4QPHrXAAAfkl8.jpg)

```
{
  "meta": {
    "aspect_ratio": "3:4",
    "quality": "ultra_photorealistic",
    "resolution": "8k",
    "camera": "DSLR with direct on-camera flash",
    "lens": "35mm wide angle",
    "style": "Flash photography, edgy street style, car culture luxury, candid night shoot, raw texture"
  },

  "scene": {
    "location": "Dark asphalt parking lot or street",
    "environment": [
      "Rough asphalt texture with gravel details",
      "Pitch black background (infinite dark)",
      "Luxury sports car side profile"
    ],
    "main_prop": {
      "object": "{argument name="car model" default="Porsche 911 GT3 RS"}",
      "color": "Baby blue (Gulf Blue)",
      "details": [
        "Visible side air intake (black)",
        "Black side decal with 'GT3' text visible",
        "Large rear wing spoiler silhouette",
        "Glossy car paint reflecting the flash"
      ]
    },
    "time": "Deep night",
    "atmosphere": "Cool, rebellious, wealthy nightlife, unbothered attitude"
  },

  "lighting": {
    "type": "Hard Direct Flash",
    "key_light": "Strong frontal flash causing high contrast",
    "shadows": "Sharp, hard drop shadows behind the subject and car",
    "background_falloff": "Immediate falloff to black (vignette effect)",
    "reflections": "Specular highlights on the car door and the subject's forehead/nose"
  },

  "camera_perspective": {
    "pov": "Eye-level / slightly low angle",
    "framing": "Full body seated, car cropped on the left",
    "focus": "Sharp focus on the subject and cat, deep depth of field due to flash"
  },

  "subject": {
    "gender": "female",
    "age": "Early 20s",
    "ethnicity": "Caucasian",
    "body": {
      "posture": "Sitting on the ground, leaning slightly back against the car door",
      "legs": "Bent at knees, splayed comfortably",
      "skin": "Pale tone, realistic texture with minor flash washout on high points"
    },

    "hair": {
      "color": "Platinum blonde with visible dark roots",
      "length": "Long, past shoulders",
      "texture": "Straight but tousled, messy 'bedhead' look, wind-blown strands",
      "shine": "High shine from flash"
    },

    "face": {
      "expression": "Seductive, cool, direct eye contact with camera, pouty",
      "makeup": "Heavy night glam, sharp winged eyeliner, sculpted contour, glossy nude lips",
      "skin_texture": "Visible pores, makeup texture, not airbrushed"
    },

    "outfit": {
      "top": {
        "type": "Basic tank top / crop top",
        "color": "Black",
        "fit": "Tight, sleeveless",
        "fabric": "Cotton matte finish"
      },
      "bottom": {
        "type": "Cargo pants",
        "pattern": "Classic green/brown woodland camouflage",
        "fit": "Baggy, loose fit, resting on shoes",
        "fabric": "Heavy canvas/denim texture"
      },
      "shoes": {
        "type": "Pointed toe stiletto pumps",
        "pattern": "Matching woodland camouflage",
        "heel_height": "High",
        "detail": "Vi"
    }
  }
}
```

[[Direct Flash Photography]] [[Luxury Car]]

---

### 21. Ana de Armas 90 年代/2000 年代复古时尚大片提示词

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2026-01-16  **Language**: en

> 一个详细的 JSON 提示，用于生成一张 90 年代/2000 年代初复古时尚编辑照片，主题人物形似安娜·德·阿玛斯（Ana de Armas）。该提示强调修身豹纹露背连衣裙、直射式机内闪光灯照明，以及在都市环境中突出曲线和轮廓。

![Ana de Armas 90 年代/2000 年代复古时尚大片提示词](https://cms-assets.youmind.com/media/1768631117916_su0q38_G-wAO3mWQAA0B0-.jpg)
![Ana de Armas 90 年代/2000 年代复古时尚大片提示词](https://cms-assets.youmind.com/media/1768631117920_0baf0q_G-wAO4GbQAQgZe3.jpg)
![Ana de Armas 90 年代/2000 年代复古时尚大片提示词](https://cms-assets.youmind.com/media/1768631117919_cfhtdz_G-wAO7kXgAAqR0t.jpg)

```
{
  "type": "image_generation_prompt",
  "subject": {
    "identity": "{argument name="subject identity" default="Ana de Armas"}",
    "likeness": "highly realistic, facial features closely matching Ana de Armas",
    "expression": "subtle smile",
    "pose": "glancing over shoulder toward camera",
    "body_emphasis": "upper and lower body appear fuller and statuesque while remaining natural"
  },
  "era_and_style": {
    "inspiration": ["late 1990s", "early 2000s"],
    "aesthetic": "vintage fashion editorial",
    "mood": "soft glamour, candid yet polished"
  },
  "appearance": {
    "skin": "smooth, radiant, naturally glowing under flash",
    "makeup": {
      "eyes": "light smoky eyes",
      "eyeliner": "thin and subtle",
      "lips": "glossy, natural tone",
      "overall": "soft, natural glamour"
    },
    "hair": {
      "length": "long",
      "style": "loose and sleek",
      "authenticity": "original natural hair"
    },
    "nails": "short, sharp, shiny"
  },
  "wardrobe": {
    "dress": {
      "material": "{argument name="dress material" default="leopard-print spandex"}",
      "fit": "form-fitting, body-clinging",
      "design": "long sleeves, backless, deeply open down to the waist",
      "focus": "emphasizes lower back and curves"
    },
    "accessories": {
      "necklace": "long gold necklace cascading down the back",
      "bracelets": "multiple gold bracelets",
      "bag": "small black leather shoulder bag"
    }
  },
  "environment": {
    "background": "neutral-colored stone wall with architectural structure",
    "lighting_effect_on_background": "slightly dull and dark due to flash"
  },
  "photography": {
    "camera_style": "fashion editorial photography",
    "lens": "85mm portrait lens",
    "lighting": "direct on-camera flash",
    "composition": "over-the-shoulder framing, emphasizing curves and silhouette"
  },
  "technical_specs": {
    "resolution": "16K",
    "quality": "UHD, ultra-detailed, realistic textures",
    "aspect_ratio": "3:4"
  },
  "style_keywords": [
    "realistic",
    "vintage 90s",
    "early 2000s",
    "editorial fashion",
    "soft glamour"
  ],
  "negative_prompt": [
    "cartoon",
    "illustration",
    "CGI",
    "over-retouched skin",
    "harsh makeup",
    "anatomical distortion",
    "blur",
    "noise",
    "watermark",
    "text",
    "logo"
  ]
}
```

[[Direct Flash Photography]] [[Urban Setting]]

---

### 22. 90 年代复古风格：闪光灯下的安娜·德·阿玛斯时尚肖像

**Author**: [​🇦​​🇮​​🇿​​🇦​​🇱​ 🤴](https://x.com/Aizalkhan11sc)  **Date**: 2026-01-15  **Language**: en

> 一个用于生成安娜·德·阿玛斯（Ana de Armas）高分辨率、超逼真肖像的提示，风格为 90 年代/2000 年代初的复古时尚杂志大片。它指定了紧身豹纹氨纶连衣裙、强调曲线的过肩姿势，以及以石墙为背景的直射机内闪光摄影。

![90 年代复古风格：闪光灯下的安娜·德·阿玛斯时尚肖像](https://cms-assets.youmind.com/media/1768544849245_iq32q3_G-sD95SbQAEWLeY.jpg)

```
{
  "type": "image_generation_prompt",
  "subject": {
    "identity": "Ana de Armas",
    "likeness": "highly realistic, facial features closely matching Ana de Armas",
    "expression": "subtle smile",
    "pose": "glancing over shoulder toward camera",
    "body_emphasis": "upper and lower body appear fuller and statuesque while remaining natural"
  },
  "era_and_style": {
    "inspiration": ["late 1990s", "early 2000s"],
    "aesthetic": "vintage fashion editorial",
    "mood": "soft glamour, candid yet polished"
  },
  "appearance": {
    "skin": "smooth, radiant, naturally glowing under flash",
    "makeup": {
      "eyes": "light smoky eyes",
      "eyeliner": "thin and subtle",
      "lips": "glossy, natural tone",
      "overall": "soft, natural glamour"
    },
    "hair": {
      "length": "long",
      "style": "loose and sleek",
      "authenticity": "original natural hair"
    },
    "nails": "short, sharp, shiny"
  },
  "wardrobe": {
    "dress": {
      "material": "{argument name="dress material" default="leopard-print spandex"}",
      "fit": "form-fitting, body-clinging",
      "design": "long sleeves, backless, deeply open down to the waist",
      "focus": "emphasizes lower back and curves"
    },
    "accessories": {
      "necklace": "long gold necklace cascading down the back",
      "bracelets": "multiple gold bracelets",
      "bag": "small black leather shoulder bag"
    }
  },
  "environment": {
    "background": "neutral-colored stone wall with architectural structure",
    "lighting_effect_on_background": "slightly dull and dark due to flash"
  },
  "photography": {
    "camera_style": "fashion editorial photography",
    "lens": "85mm portrait lens",
    "lighting": "direct on-camera flash",
    "composition": "over-the-shoulder framing, emphasizing curves and silhouette"
  },
  "technical_specs": {
    "resolution": "16K",
    "quality": "UHD, ultra-detailed, realistic textures",
    "aspect_ratio": "3:4"
  },
  "style_keywords": [
    "realistic",
    "vintage 90s",
    "early 2000s",
    "editorial fashion",
    "soft glamour"
  ],
  "negative_prompt": [
    "cartoon",
    "illustration",
    "CGI",
    "over-retouched skin",
    "harsh makeup",
    "anatomical distortion",
    "blur",
    "noise",
    "watermark",
    "text",
    "logo"
  ]
}
```

[[Direct Flash Photography]] [[Stone Wall Background]]

---

### 23. 16K 复古 90 年代编辑肖像

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2026-01-15  **Language**: en

> 一个用于生成超细节、16K 照片级写实肖像的提示，风格为 1990 年代/2000 年代初期的复古时尚杂志。主体灵感来自西德尼·斯威尼 (Sydney Sweeney)，身穿紧身豹纹氨纶连衣裙，露背设计，在石墙前用直射机载闪光灯拍摄。

![16K 复古 90 年代编辑肖像](https://cms-assets.youmind.com/media/1768544865181_j5cjk7_G-r6VAEbQAAo7hF.jpg)

```
{
  "type": "image_generation_prompt",
  "subject": {
    "identity": "Sydney Sweeney ",
    "likeness": "highly realistic, facial features closely matching Ana de Armas",
    "expression": "subtle smile",
    "pose": "glancing over shoulder toward camera",
    "body_emphasis": "upper and lower body appear fuller and statuesque while remaining natural"
  },
  "era_and_style": {
    "inspiration": ["late 1990s", "early 2000s"],
    "aesthetic": "vintage fashion editorial",
    "mood": "soft glamour, candid yet polished"
  },
  "appearance": {
    "skin": "smooth, radiant, naturally glowing under flash",
    "makeup": {
      "eyes": "light smoky eyes",
      "eyeliner": "thin and subtle",
      "lips": "glossy, natural tone",
      "overall": "soft, natural glamour"
    },
    "hair": {
      "length": "long",
      "style": "loose and sleek",
      "authenticity": "original natural hair"
    },
    "nails": "short, sharp, shiny"
  },
  "wardrobe": {
    "dress": {
      "material": "leopard-print spandex",
      "fit": "form-fitting, body-clinging",
      "design": "long sleeves, backless, deeply open down to the waist",
      "focus": "emphasizes lower back and curves"
    },
    "accessories": {
      "necklace": "long gold necklace cascading down the back",
      "bracelets": "multiple gold bracelets",
      "bag": "small black leather shoulder bag"
    }
  },
  "environment": {
    "background": "neutral-colored stone wall with architectural structure",
    "lighting_effect_on_background": "slightly dull and dark due to flash"
  },
  "photography": {
    "camera_style": "fashion editorial photography",
    "lens": "85mm portrait lens",
    "lighting": "direct on-camera flash",
    "composition": "over-the-shoulder framing, emphasizing curves and silhouette"
  },
  "technical_specs": {
    "resolution": "16K",
    "quality": "UHD, ultra-detailed, realistic textures",
    "aspect_ratio": "3:4"
  },
  "style_keywords": [
    "realistic",
    "vintage 90s",
    "early 2000s",
    "editorial fashion",
    "soft glamour"
  ],
  "negative_prompt": [
    "cartoon",
    "illustration",
    "CGI",
    "over-retouched skin",
    "harsh makeup",
    "anatomical distortion",
    "blur",
    "noise",
    "watermark",
    "text",
    "logo"
  ]
}
```

[[Direct Flash Photography]]

---

### 24. 狗仔队风格抓拍照片提示

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-01-14  **Language**: en

> 一个旨在生成一张捕捉女性猝不及防的原始、坦率、狗仔队风格照片的提示，强调刺眼的机内闪光灯、高颗粒感（高 ISO）和 2000 年代小报美学，背景是动态模糊的时装周。

![狗仔队风格抓拍照片提示](https://cms-assets.youmind.com/media/1768468532540_dqtv7e_G-mWaEqbQA0HgIZ.jpg)
![狗仔队风格抓拍照片提示](https://cms-assets.youmind.com/media/1768468532543_j9cazc_G-mWaEVboAAGGqj.jpg)
![狗仔队风格抓拍照片提示](https://cms-assets.youmind.com/media/1768468533745_5ywjy4_G-mWaEeaQAAMd1b.jpg)
![狗仔队风格抓拍照片提示](https://cms-assets.youmind.com/media/1768468533297_yqowky_G-mWaEubQAQCj0s.jpg)

```
Paparazzi-style extreme close-up photo of a woman with striking facial features, caught off-guard while turning toward the camera. Face and shoulders only, shot from a low angle. Strong harsh on-camera flash, grainy high-ISO, raw candid street-photography feel. Background shows a crowded scene with motion blur ({argument name="background setting" default="Paris Fashion Week atmosphere"}). Intense, spontaneous energy, imperfect and real. She is wearing a {argument name="clothing item" default="school uniform"}. Ultra-realistic, cinematic realism, high detail skin texture, slight lens distortion.

Camera style: “35mm paparazzi lens, f/2.8, flash blown highlights”
Look: “2000s tabloid photo aesthetic”
Quality: “sharp focus on face, background heavily blurred and streaked”
```

[[Direct Flash Photography]]

---

### 25. 硬闪光露背连衣裙夜间照片提示

**Author**: [laurababy](https://x.com/laurababyai)  **Date**: 2026-01-10  **Language**: en

> 一个详细的 JSON 提示，用于生成一张逼真的夜间照片：一位年轻女性，皮肤黝黑，深色头发，身穿及地黑色露背长裙，背部极低且开放，呈坐姿扭转状，回望镜头，强调硬朗的机内闪光灯照明和真实的皮肤纹理。

![硬闪光露背连衣裙夜间照片提示](https://cms-assets.youmind.com/media/1768143869738_8cgncl_G-Ul8JsWcAAd8Pn.jpg)

```
{
"subject": {
"description": "Young adult female with tanned, bronzed skin and long, dark brunette hair parted in the middle. She has distinct, sharp facial features including high cheekbones, a straight nose, arched eyebrows, and full, glossy lips. She is wearing a floor-length black maxi dress with very thin spaghetti straps. The dress features an extremely low, open back that exposes the entire back down to the lumbar region, revealing the spinal groove and shoulder blades.",
"anatomy_constraints": {
"body_type": "Fit but soft, realistic proportions",
"skin_texture": "High fidelity pores, slight sheen from flash, natural skin imperfections, visible mole/freckle on upper back",
"bust_volume": "Natural fullness implied by side profile visibility, gravity-affected soft tissue",
"back_details": "Visible scapula definition, distinct spinal indentation, smooth muscle tone"
}
},
"pose": {
"type": "Seated twist, looking back",
"description": "The subject is sitting on stone steps, body oriented away from the camera (posterior view). She is twisting her torso significantly to the left to look back over her left shoulder directly at the lens. Her back is arched, accentuating the curve of the spine. The left arm is resting on the leg/knee area (mostly obscured), and the right arm is relaxed. The neck is turned sharply to maintain eye contact.",
"alignment": "Head turned left, eyes locked on camera, chin slightly lowered"
},
"environment": {
"setting": "Outdoors at night, residential or garden staircase",
"elements": [
"Beige/light grey stone steps with dark grout lines",
"Low stone retaining wall",
"Dark green leafy bushes and hedging in the immediate background",
"Night sky (implied dark void)"
]
},
"camera": {
"shot_type": "Medium shot, slightly high angle",
"perspective": "Looking down at the subject, close proximity",
"focal_length": "35mm to 50mm equivalent",
"depth_of_field": "Deep enough to keep face and back in focus, slight fall-off in background foliage"
},
"lighting": {
"type": "Direct on-camera flash (hard flash photography)",
"characteristics": [
"High contrast",
"Sharp, defined shadows cast on the wall behind the subject",
"Bright specular highlights on the shoulder, cheekbone, tip of nose, and forehead",
"Reflective sheen on the skin due to flash intensity",
"Vignetting at the edges due to flash fall-off"
]
},
"mood_and_expression": {
"mood": "Alluring, mysterious, confident, nightlife aesthetic",
"expression": "Sultry, neutral to slightly parted lips, intense direct gaze",
"eye_contact": "Direct, piercing"
},
"style_and_realism": {
"style": "Flash photography, paparazzi style, candid social media aesthetic, raw realism",
"fidelity": "Photorealistic, unpolished texture, high ISO noise simulation"
},
"colors_and_tone": {
"palette": [
"Deep blacks (dress, background shadows)",
"Warm bronzed skin tones",
"Beige/cream stone colors",
"Deep forest greens (foliage)"
],
"tonality": "Warm ski"
```

[[Direct Flash Photography]] [[Skin Texture]] [[Night Portrait]]

---

### 26. 2000 年代初期 Flash 照片身份混合提示

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-01-10  **Language**: en

> 一个为 Nano Banana Pro 设计的提示，旨在将两张上传照片的身份融合到一张图像中，生成一张原始的、闪光灯照明的、复古数码相机美学风格的照片，照片中一名男子和一名女子背靠背站在人行道上，严格保留原始面部特征，同时应用 2000 年代初期的快照风格。

![2000 年代初期 Flash 照片身份混合提示](https://cms-assets.youmind.com/media/1768143913066_f14pts_G-T8RSobkAAfsBo.jpg)

```
Raw early-2000s flash-lit photo, vintage digicam aesthetic; man and woman (keep original faces from both uploaded photos exactly, do not alter facial features in any way, no face changes even 1%) standing back to back on a sidewalk near a street corner; outfits: layered casual looks denim jacket over white tank on her, dark jacket over ribbed tank on him; pose: bodies touching lightly at the back, hands hanging loosely, heads turned slightly away from camera; expression: serious, reserved, emotionally closed; lighting: aggressive direct flash flattening the scene, strong contrast between subjects and background; background: crosswalk, street sign, faded storefronts; composition: waist-up framing, awkward crop, candid street-photo energy; visible skin texture, natural pores, harsh flash emphasizing imperfections; grain, digital artifacts, early-2000s snapshot realism.
```

[[Direct Flash Photography]] [[Retro Digital Camera]] [[Early 2000s Aesthetic]]

---

### 27. 四格闪光肖像拼贴提示

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-01-09  **Language**: en

> 一个用于生成年轻女性四格肖像拼贴画的提示，强调无瑕的肌肤、特定的配饰（粉色透明边框眼镜、蝴蝶项链），并使用直射闪光灯营造柔和、粉嫩、略微过曝的光泽。

![四格闪光肖像拼贴提示](https://cms-assets.youmind.com/media/1768143650804_db4866_G-NnBIvboAAfuIg.jpg)

```
Create a realistic portrait image in a 4-panel collage with a high-angle shot perspective (the face must be 100% identical — do not change or modify it).

Depict a beautiful young woman with fair, smooth, flawless skin that looks healthy and naturally glowing. She has shiny brown hair styled in a loose bun (messy bun). Her makeup uses soft, gentle tones, with flushed pink lips. The camera angle is close to the face.

She is wearing thick, large, transparent clear-frame glasses with a pink tone (clear frame 1.2). She wears a pink T-shirt and a small silver butterfly necklace. Flash lighting illuminates the face and skin, creating soft reflective highlights and giving the skin a slightly pinkish glow. The overall color tone of the image is creamy white / creamy mauve.

She looks directly at the camera with a sexy gaze. Use direct flash with a soft, diffused glow effect, where the flash light spreads evenly and the highlights are slightly overexposed.

Panel details:

Panel 1: {argument name="panel 1 pose" default="Sweet laughing pose"}

Panel 2: {argument name="panel 2 pose" default="Peace sign pose"}

Panel 3: {argument name="panel 3 pose" default="Metal hand sign pose"}

Panel 4: {argument name="panel 4 pose" default="Cute pose"}
```

[[Direct Flash Photography]]

---

### 28. 独立邋遢风 2000 年代街头风格肖像提示

**Author**: [Lex](https://x.com/katmanai)  **Date**: 2026-01-08  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超详细的 8K 肖像，风格为“独立颓废风”，主体是一位女性，身穿红色皮夹克、做旧牛仔迷你裙和亮红色紧身裤，T 恤上印有特定图案文字，置身于一个破旧的复古室内环境中，采用直射闪光灯摄影。

![独立邋遢风 2000 年代街头风格肖像提示](https://cms-assets.youmind.com/media/1767967516650_l6rk78_G-IzDfzXIAAfW8Z.jpg)

```
{
  "image_description": {
    "subject": {
      "gender": "Female",
      "age_range": "Early 20s",
      "hair": {
        "color": "Dark brown / Black",
        "style": "Long, wavy, voluminous, middle-parted",
        "texture": "Natural, slightly messy"
      },
      "facial_features": {
        "expression": "Neutral, intense gaze, direct eye contact",
        "makeup": "Subtle eyeliner, soft pink lipstick",
        "distinguishing_marks": "Small red heart-shaped mark/tattoo on the center of the forehead"
      },
      "tattoos": [
        "Small black ink symbols on fingers",
        "Circular/eye-like tattoo on the back of the left hand"
      ],
      "jewelry": [
        "Silver rings on multiple fingers",
        "Thin silver bangles/bracelets on both wrists"
      ]
    },
    "outfit": {
      "top": {
        "type": "Tight-fitting short-sleeve t-shirt",
        "color": "Light blue / White",
        "text": "{argument name="tshirt text" default="GOD'S SEXIEST SOLDIER"}",
        "text_color": "Bold red",
        "font_style": "Sans-serif, all-caps"
      },
      "outerwear": {
        "type": "Red leather biker jacket",
        "style": "Cropped, open, silver zippers and hardware"
      },
      "bottom": {
        "skirt": "Distressed denim mini skirt, faded blue",
        "layering": "Bright red opaque tights worn high, visible above the skirt waistband"
      }
    },
    "pose_and_composition": {
      "pose": "Standing, slightly leaning forward, holding the lapels of the red jacket with both hands",
      "camera_angle": "Eye level, medium shot",
      "framing": "Upper body and mid-thigh focus"
    },
    "environment": {
      "setting": "Indoor room with a vintage/grungy aesthetic",
      "walls": "Two-tone wall: Upper part is textured beige/ochre with aged plaster look, lower part is dark forest green",
      "flooring": "Old wooden plank floor, polished brown",
      "background_elements": [
        "Wooden framed mirror reflecting a dark interior",
        "White vintage radiator on the right side",
        "Dim, warm indoor lighting"
      ]
    },
    "technical_specs": {
      "lighting": "Direct flash photography, high contrast, sharp shadows on the wall",
      "aesthetic": "Indie sleaze, 2000s street style, cinematic realism",
      "resolution": "Ultra-detailed, 8k, high grain texture for film look"
    }
  }
}
```

[[Direct Flash Photography]] [[8K Portrait]]

---

### 29. 夜间生活情侣肖像，带直射闪光灯提示

**Author**: [Zara](https://x.com/ZaraIrahh)  **Date**: 2026-01-08  **Language**: en

> 一个详细的提示，用于拍摄浪漫情侣的夜间生活肖像，使用强烈的正面闪光灯在黑暗背景下捕捉。它指定了构图（垂直、中景全身照、紧密拥抱）、拍摄对象的服装（迷幻漩涡连衣裙、亚麻度假装）以及高对比度照明效果。

![夜间生活情侣肖像，带直射闪光灯提示](https://cms-assets.youmind.com/media/1767967410554_wgs0rt_G-IX6Hxa0AA42Zw.jpg)

```
{ "image_type": "photograph", "genre": "nighttime lifestyle portrait", "composition": { "framing": "medium-full shot", "orientation": "vertical", "subjects_position": "two subjects centered, standing closely side by side with bodies touching", "camera_angle": "eye-level", "pose": "intimate and relaxed; female subject embracing male subject at chest and waist", "cropping": "cropped slightly below knees", "depth_of_field": "shallow to moderate; subjects in focus, background fades into darkness" }, "subjects": [ { "gender_presentation": "female", "approximate_age": "young adult", "build": "slim", "facial_features": "long wavy dark brown hair, softly contoured cheeks, defined eyebrows, natural makeup with glossy lips", "expression": "calm, subtle smile", "gaze": "looking directly at camera", "clothing": { "type": "fitted sleeveless dress", "pattern": "{argument name="dress pattern" default="bold abstract psychedelic swirl pattern"}", "colors": [ "red", "blue", "green", "orange", "white", "black" ], "fit": "body-hugging, ankle-length" }, "accessories": { "jewelry": "bracelet, ring", "nails": "long, red polished nails" } }, { "gender_presentation": "male", "approximate_age": "young adult", "build": "average to athletic", "facial_features": "curly dark hair, light stubble, soft jawline", "expression": "neutral to slight smile", "gaze": "looking directly at camera", "clothing": { "top": "white lightweight linen button-up shirt, partially unbuttoned", "bottom": "light beige or off-white linen pants", "style": "resort casual, relaxed" }, "accessories": { "wristwear": "dark bracelet", "handheld_object": "short glass tumbler with dark beverage" } } ], "interaction": { "relationship_cues": "romantic, affectionate", "body_language": "close embrace, relaxed shoulders, physical contact at torso and waist" }, "environment": { "setting": "outdoor nighttime location", "background": "dark foliage and greenery", "visibility": "background mostly obscured by darkness", "ground": "grass lawn", "context": "evening social event or party" }, "lighting": { "type": "direct on-camera flash", "key_light": "strong frontal flash", "fill": "minimal ambient light", "color_temperature": "neutral flash with warm skin tones", "shadows": "hard falloff into dark background, minimal shadow detail behind subjects", "skin_tone_rendering": "bright, smooth, slightly reflective highlights" }, "color_palette": { "dominant_colors": [ "black", "white", "green" ], "accent_colors": [ "red", "blue", "orange" ], "contrast_level": "high due to flash against dark background", "overall_mood": "romantic, stylish, intimate" }, "technical_details": { "camera_type": "smartphone or consumer digital camera", "lens_effect": "standard focal length", "focus": "sharp focus on subjects", "exposure": "subjects slightly overexposed relative to background", "noise": "low on subjects, minimal visible grain", "flash_usage": "enabled and dominant" }, "stylistic_characte
```

[[Direct Flash Photography]] [[High Contrast Lighting]] [[Dark Background]]

---

### 30. 现代楼梯上的奢华时尚编辑拼贴画

**Author**: [Dina 🌹](https://x.com/ayzlvibe)  **Date**: 2026-01-07  **Language**: en

> 一个结构化的提示，用于生成一张时尚模特在现代大理石楼梯上摆姿势的四图拼贴画。该提示详细说明了场景（高档住宅内景）、灯光（直射机内闪光灯加柔和补光）和服装（修身棕色迷你连衣裙），旨在营造适合 Instagram 的奢华时尚大片美学。

![现代楼梯上的奢华时尚编辑拼贴画](https://cms-assets.youmind.com/media/1767966069850_ennj5b_G-F3LscWMAADnHN.jpg)

```
{
  "scene": {
    "location": "modern indoor staircase",
    "environment": "light marble steps, white walls, stainless steel handrails",
    "lighting": "direct on-camera flash with soft ambient fill, clean shadows",
    "time_of_day": "evening",
    "set_style": "minimal, upscale residential interior"
  },
  "subject": {
    "description": "fashion model posing on staircase",
    "hair": "long brown hair in loose waves, center part",
    "makeup": "glam evening makeup, bronzed complexion, defined eyes, glossy lips",
    "expression": "confident, composed, editorial gaze",
    "poses": [
      "seated on steps with legs crossed, chin resting on hand",
      "standing sideways on stairs looking back at camera",
      "seated upright with relaxed smile",
      "standing with one hand in hair, body angled"
    ]
  },
  "wardrobe_and_accessories": {
    "outfit": "fitted brown mini dress",
    "shoes": "black open-toe heels",
    "bag": "black designer shoulder bag",
    "jewelry": [
      "gold wristwatch",
      "bracelet",
      "rings"
    ]
  },
  "composition": {
    "layout": "four-image collage",
    "framing": [
      "three-quarter body shot",
      "full-body shot",
      "seated portrait",
      "standing portrait"
    ],
    "camera_angle": "eye level to slightly above",
    "focus": "sharp subject, neutral background",
    "aesthetic": "luxury fashion editorial, Instagram-ready"
  },
  "camera": {
    "lens": "35mm",
    "aperture": "f/2.8",
    "iso": 400,
    "shutter_speed": "1/60",
    "flash": "on-camera flash"
  },
  "style_keywords": [
    "modern luxury",
    "evening fashion",
    "editorial photoshoot",
    "minimal interior",
    "high-end lifestyle"
  ]
}
```

[[Direct Flash Photography]] [[Marble Staircase]] [[Brown Mini Dress]]

---

### 31. 复古美学时尚肖像与额饰

**Author**: [𝐌](https://x.com/Strength04_X)  **Date**: 2026-01-03  **Language**: en

> 一个用于生成年轻女性半身时尚肖像的超写实提示词，严格匹配参考面部。风格为柔和复古美学，带直射机顶闪光灯，身穿白色荷叶边露脐上衣，并佩戴一枚黑色小宾迪。

![复古美学时尚肖像与额饰](https://cms-assets.youmind.com/media/1767604070317_lp6lvg_G9v8ZF0asAAfOs2.jpg)
![复古美学时尚肖像与额饰](https://cms-assets.youmind.com/media/1767604070200_1le9b3_G9v8Y-GakAA4ULY.jpg)

```
{
    "positive": "Mid-shot fashion portrait of a young woman with the exact facial structure of the reference, long blonde hair flowing down her back, and a small black bindi. She is wearing a delicate white ruffled spaghetti-strap crop top that reveals her waist and navel in a classy, natural way. She is standing with a slight curve in her posture, one hand resting on her hip, looking directly at the camera with a warm smile. Direct on-camera flash lighting, soft vintage aesthetic, highly detailed skin texture, realistic shadows, 8k resolution, candid lifestyle photography.",
    "negative": "deformed, ugly, bad anatomy, disfigured, crossed eyes, morphing, extra limbs, blur, watermark, text, cartoon, illustration, painting, low quality, pixelated, oversaturated, bad hands, missing fingers",
    "parameters": {
      "aspect_ratio": "9:16",
      "steps": 30,
      "cfg_scale": 7.0,
      "sampler": "DPM++ 2M Karras",
      "seed": -1,
      "style": "Photorealistic"
    }
  }
```

[[Direct Flash Photography]] [[Retro Aesthetic]]

---

### 32. 高对比度运动社论肖像，搭配 Grillz 和 Oakley

**Author**: [Bananai](https://x.com/aibananai)  **Date**: 2026-01-03  **Language**: en

> 一个高度详细的提示，用于创作一张原始、超现实、高对比度的非洲裔美国男性运动员在更衣室里的体育专题肖像。它特别强调皮肤纹理（毛孔、皮脂、剃须引起的红疹）的极致真实感，详细的配饰（Oakley 环绕式太阳镜、钻石牙套），以及刺眼的直射闪光灯照明。

![高对比度运动社论肖像，搭配 Grillz 和 Oakley](https://cms-assets.youmind.com/media/1767604003722_z7667w_G9vjDnvb0AAma9v.jpg)
![高对比度运动社论肖像，搭配 Grillz 和 Oakley](https://cms-assets.youmind.com/media/1767604004219_pfre7d_G9vjDnxasAQmJy1.jpg)

```
{
  "meta": {
    "aspect_ratio": "4:5",
    "quality": "raw_photorealistic",
    "resolution": "8k",
    "camera": "Hasselblad H6D-100c",
    "lens": "Macro 80mm f/2.8",
    "style": "high-contrast sports editorial, detailed texture realism, backstage aesthetic, raw flash photography"
  },

  "scene": {
    "location": "athlete locker room",
    "environment": [
      "dark grey metal lockers with ventilation slats",
      "industrial background",
      "shallow depth of field but identifiable structure"
    ],
    "lighting": {
      "type": "direct flash with softbox",
      "direction": "front-top-right bias",
      "intensity": "high",
      "highlights": "strong specular highlights on forehead, nose tip, and cheekbones mimicking sweat/oil",
      "shadows": "deep contrast under the chin and nose",
      "reflections": "sharp studio light reflection in sunglasses lenses"
    }
  },

  "subject": {
    "identity_features": {
      "gender": "male",
      "ethnicity": "African American",
      "skin_texture": "hyper-realistic pore visibility, uneven skin tone, visible sebum shine (not plastic matte), razor bumps on neck, mole texture",
      "facial_structure": "strong jawline, high cheekbones, muscular neck"
    },

    "hair_and_grooming": {
      "hair_style": "tightly braided cornrows",
      "hair_texture": "visible scalp lines, natural frizz at hairline",
      "facial_hair": "groomed goatee and mustache, realistic coarse hair texture, distinct stubble on jaw"
    },

    "expression_and_pose": {
      "action": "pulling down lower lip with right index finger",
      "mouth": "teeth gritted/exposed to show {argument name="jewelry type" default="jewelry"}",
      "mood": "aggressive flex, confident, hype",
      "gaze": "eyes hidden behind glasses, face turned slightly to viewer's right"
    },

    "accessories_detailed": {
      "sunglasses": {
        "brand": "{argument name="sunglasses brand" default="Oakley"}",
        "model_type": "futuristic wrap-around shield / visor style",
        "frame_material": "matte silver / magnesium finish",
        "lens_color": "deep fiery orange to red gradient",
        "branding": "distinct 'OAKLEY' logo embossed on the brow bar",
        "details": "small 'BE INSPIRED' text visible on lower lens corner"
      },
      "grillz": {
        "type": "bonded tooth gems / individual diamond studs",
        "placement": "embedded on lower front teeth (incisors and canines)",
        "material": "round cut clear diamonds",
        "look": "sparkling, wet look from saliva (realistic, not metallic block)"
      },
      "earring": {
        "type": "diamond cross stud",
        "location": "right earlobe",
        "material": "silver setting with pave diamonds"
      },
      "necklace": {
        "type": "single row tennis chain",
        "material": "diamonds",
        "visibility": "peeking out from t-shirt collar"
      }
    },

    "outfit": {
      "outerwear": {
        "type": "track jacket / bomber",
        "color": ""
      }
    }
  }
}
```

[[Direct Flash Photography]] [[Hyperrealistic Skin Texture]] [[Diamond Grillz]]

---

### 33. Hyper-realistic smartphone flash photo prompt for AI image generation

**Author**: [Michael Rabone](https://x.com/michaelrabone)  **Date**: 2026-01-02  **Language**: en

> A detailed image generation prompt designed to mimic the aesthetic of a hyper-realistic, amateur smartphone photo taken with a harsh, direct flash. It specifies subject details, outfit, accessories, setting, composition, and technical quality to achieve a distinctive, high-contrast, grainy snapshot look.

![Hyper-realistic smartphone flash photo prompt for AI image generation](https://cms-assets.youmind.com/media/1767508391545_4nqrkw_G9qB1RFX0AAD7wg.jpg)
![Hyper-realistic smartphone flash photo prompt for AI image generation](https://cms-assets.youmind.com/media/1767508391671_b84kxn_G9qB1VvWIAAb5NC.jpg)
![Hyper-realistic smartphone flash photo prompt for AI image generation](https://cms-assets.youmind.com/media/1767508392142_yqwykd_G9qB1VSWQAAQCy5.jpg)
![Hyper-realistic smartphone flash photo prompt for AI image generation](https://cms-assets.youmind.com/media/1767508394583_f0sbzz_G9qB1RGWwAABUo4.jpg)

```
GENERAL DESCRIPTION: Amateur photo taken with a smartphone, captured in a handheld camera flash style. A young woman poses facing the camera with a smile. The harsh flash creates bright, specular highlights on her skin and clothing, with very sharp shadows and slight grain in the dark areas of the background.

SUBJECT DETAILS: Attractive young woman with {argument name="hair color" default="platinum blonde"} hair, styled loose with a wet, glossy effect under the flash. Realistic skin with visible pores, small natural imperfections, and a slight sheen from sweat or makeup.

OUTFIT: Sleeveless jumpsuit with thin straps of vibrant {argument name="outfit color" default="red"} velvet, very form-fitting. The fabric shows natural wrinkles from movement and an intense satin sheen in the areas directly hit by the flash.

ACCESSORIES: An iced-out Cuban link necklace that sparkles brightly in the flash, along with several thin bracelets.

SETTING & COMPOSITION: Background with dark palm trees and distant hills under a deep night sky.

FRAMING: Aspect ratio 4:5. Medium shot from head to calves. She looks directly at the lens, revealing the characteristic circular white reflection of the flash in her eyes.

TECHNICAL QUALITY: High-end phone camera aesthetic, with slightly warm white balance, high contrast, sharp focus on the subject, and very subtle motion blur in the background to give the impression of a quick snapshot.
```

[[Direct Flash Photography]] [[High Contrast Portrait]]

---

### 34. Photorealistic Polaroid Couple Selfie with Christmas Bokeh

**Author**: [Melis✨](https://x.com/miilesus)  **Date**: 2026-01-01  **Language**: en

> A highly detailed, photorealistic text-to-image prompt designed for the NanoBanana Pro tool, focusing on creating an authentic instant-film look. The scene is a handheld flash photo of a Polaroid print showing a couple in Christmas sweaters, set against a heavily blurred background of a Christmas tree with warm golden bokeh. This prompt specifies detailed output settings, composition, and quality rules to achieve a raw, realistic photographic style with shallow depth of field and flash effects.

![Photorealistic Polaroid Couple Selfie with Christmas Bokeh](https://cms-assets.youmind.com/media/1767508430845_jf09gm_G9m2sWLXEAA5mqe.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "text_to_image_photoreal_polaroid_in_hand_christmas_bokeh",
      "version": "v1.0",
      "priority": "high"
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "orientation": "portrait",
      "resolution": "ultra_high_res",
      "render_style": "raw_photographic_realism",
      "sharpness": "foreground_sharp_background_soft",
      "film_grain": "subtle",
      "flash": "on"
    },
    "creative_prompt": {
      "scene_summary": "A realistic handheld flash photo in a cozy living room at night: a hand with glossy red French-tip nails holds a white instant-film Polaroid photo close to the camera. In the background, a decorated Christmas tree is heavily out of focus with warm golden fairy-light bokeh and red ornaments, creating a dreamy holiday glow. The Polaroid print itself is in focus and shows a cute couple selfie wearing matching red-and-white Christmas knit sweaters; their faces are softly lit like an instant camera flash, slightly imperfect and authentic (true instant-film look). The overall vibe is warm, nostalgic, and cozy.",
      "composition": {
        "framing": "close foreground focus on the Polaroid frame, hand visible at bottom-left holding it",
        "depth_of_field": "very shallow DOF; tree becomes large soft bokeh circles",
        "focus_priority": "Polaroid print + its white border tack-sharp; background strongly blurred"
      },
      "foreground_details": {
        "hand": "one hand holding the Polaroid by the bottom edge, glossy nude base nails with crisp red French tips",
        "polaroid": "classic white instant photo border, slight glare from flash, subtle paper texture, tiny imperfections like real instant film"
      },
      "polaroid_photo_content": {
        "subjects": "two young adults close together in a selfie pose, wearing red-and-white Nordic Christmas sweaters",
        "expressions": "natural casual selfie expressions, warm and slightly playful",
        "lighting": "direct on-camera flash look inside the Polaroid image, a bit softer and slightly lower resolution than the outer photo"
      },
      "background": {
        "christmas_tree": "large tree filling the background, warm white string lights, red ornaments and ribbons, heavy bokeh",
        "environment": "cozy indoor night ambience, soft warm tones"
      },
      "camera_notes": {
        "capture_style": "smartphone flash photo (iPhone vibe)",
        "lens_feel": "26mm equivalent, close focus",
        "exposure": "foreground properly exposed by flash; background darker but glowing bokeh"
      },
      "quality_rules": [
        "photorealistic",
        "natural skin texture (no plastic smoothing)",
        "realistic flash reflections and glare",
        "no watermark",
        "no extra text"
      ]
    },
    "negative_prompt": [
      "watermark",
      "lo"
    ]
  }
}
```

[[Direct Flash Photography]]

---

### 35. Ultra-Photorealistic Group Portrait: New Year's Eve Party

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-01-01  **Language**: en

> A structured prompt for generating an ultra-photorealistic group portrait of four young women celebrating New Year's Eve on a rooftop terrace. The image uses harsh, direct on-camera flash (paparazzi style) against a dark city background with exploding red fireworks, emphasizing high contrast and glamorous attire.

![Ultra-Photorealistic Group Portrait: New Year's Eve Party](https://cms-assets.youmind.com/media/1767508371757_mhwv0e_G9l5QtCaEAA3yo2.jpg)

```
{
  "prompt_type": "Ultra Photorealistic Group Portrait",
  "subject_details": {
    "main_subjects": "Group of four young women celebrating",
    "subject_1_left": "Young woman with long dark wavy hair, wearing a beige/gold sleeveless sequin gown, smiling softly at the camera, silver drop earrings",
    "subject_2_center_left": "Young woman with brown hair tied back, wearing a bright {argument name="dress color" default="red"} lace dress with halter neck, one arm raised high in excitement, laughing with head tilted back, large gold hoop earrings",
    "subject_3_center_right": "Young woman with dark hair, close to the group, eyes closed in a happy expression, leaning affectionately onto the woman in red",
    "subject_4_right": "Young woman with long platinum blonde wavy hair, wearing a gold sequin backless dress, looking back over her shoulder at the camera with a sultry expression, small tattoo visible on her mid-back",
    "skin_texture": "High fidelity skin texture, visible pores, realistic makeup finish, slight sheen from flash"
  },
  "fashion_and_styling": {
    "clothing_style": "Glamorous nightlife attire, New Year's Eve party style, sequins, lace, backless cuts",
    "accessories": "Hoop earrings, gold bangles, minimalist jewelry",
    "makeup": "Evening glam, highlighted cheekbones, glossy lips, defined brows"
  },
  "environment_and_background": {
    "setting": "Outdoor rooftop terrace at night overlooking a city",
    "background_elements": "Dark night sky illuminated by bright red fireworks exploding in the distance, blurred city lights (bokeh) on the horizon",
    "atmosphere": "Festive, energetic, exclusive party vibe"
  },
  "lighting_and_atmosphere": {
    "lighting_style": "Direct on-camera flash photography (paparazzi style)",
    "ambient_light": "Red glow from fireworks casting a subtle tint on the sky",
    "contrast": "High contrast between the brightly lit subjects and the dark background",
    "shadows": "Sharp, realistic shadows created by the flash"
  },
  "camera_specifications": {
    "camera_model": "Sony A7R V or Phase One XF IQ4",
    "lens": "35mm wide-angle prime lens",
    "aperture": "f/2.8",
    "shutter_speed": "1/125s",
    "iso": "800",
    "focus": "Sharp focus on the faces, creamy bokeh in the background"
  },
  "technical_quality": {
    "resolution": "8k",
    "details": "Hyper-realistic, insane detail, volumetric lighting, ray tracing, unreal engine 5 render style features",
    "aspect_ratio": "3:4"
  }
}
```

[[Direct Flash Photography]]

---

### 36. Gorpcore Editorial: Extreme Worm's-Eye View of Hiking Boot

**Author**: [Bananai](https://x.com/aibananai)  **Date**: 2026-01-01  **Language**: en

> A highly detailed prompt for generating an ultra-photorealistic, high-end gorpcore editorial image. It captures an extreme worm's-eye view of a technical hiking boot stepping in snow and mud, using direct flash photography at twilight to create a dark, moody, high-contrast aesthetic.

![Gorpcore Editorial: Extreme Worm's-Eye View of Hiking Boot](https://cms-assets.youmind.com/media/1767508357770_53c707_G9llc3vWIAAeGPJ.jpg)
![Gorpcore Editorial: Extreme Worm's-Eye View of Hiking Boot](https://cms-assets.youmind.com/media/1767508359793_sv7kf1_G9llc32XIAAstRh.jpg)

```
{
  "meta": {
    "aspect_ratio": "4:5",
    "quality": "ultra_photorealistic",
    "resolution": "8k",
    "camera": "Sony A7R IV",
    "lens": "16mm ultra-wide angle macro",
    "style": "high-end gorpcore editorial, flash photography in nature, dark moody aesthetic, tactile realism"
  },

  "scene": {
    "location": "rugged mountain terrain at twilight",
    "environment": [
      "dark snowy landscape",
      "patches of moss and dry grass in extreme foreground",
      "gnarled bare tree branches in silhouette",
      "overcast dark blue sky"
    ],
    "time": "blue hour / dusk",
    "atmosphere": "cold, adventurous, cinematic gloom, heavy atmosphere"
  },

  "lighting": {
    "type": "direct flash photography",
    "key_light": "strong camera-mounted flash illuminating the sole and pants",
    "ambient_light": "very low natural blue skylight",
    "contrast": "high contrast between the illuminated shoe/legs and the dark background",
    "shadows": "deep, crushing shadows in the upper frame",
    "reflection": "subtle wet highlights on the rubber sole and synthetic fabric"
  },

  "camera_perspective": {
    "pov": "extreme worm's-eye view (ground level)",
    "angle": "looking straight up at the heel",
    "framing": "macro focus on the shoe sole, legs towering above",
    "distance": "immediate foreground (<10cm from the sole)",
    "motion": "frozen mid-step action, dynamic walking pose"
  },

  "subject": {
    "type": "hiker / outdoor explorer",
    "orientation": "walking away from camera",
    "focus_point": "right foot shoe sole",
    
    "outfit": {
      "pants": {
        "type": "technical oversized cargo trousers",
        "material": "waterproof GORE-TEX or nylon",
        "color": "dark navy or black",
        "texture": "crinkled, baggy fit, gathering around the ankles",
        "details": "visible fabric tension and folds"
      },
      "jacket": {
        "type": "heavy down puffer jacket",
        "color": "black",
        "fit": "oversized, bulky silhouette"
      },
      "backpack": {
        "type": "technical hiking pack",
        "visibility": "partial, black, sitting high on back"
      }
    },

    "footwear_details": {
      "type": "chunky technical hiking sneaker / boot",
      "color": "off-white / cream outsole",
      "sole_design": "aggressive traction lugs, deep grooves",
      "branding": "distinct yellow octagonal Vibram logo embedded in the mid-sole",
      "condition": "slightly used, traces of wet mud and snow in the treads",
      "texture": "matte rubber with granular detail"
    }
  },

  "details": {
    "foreground_textures": {
      "ground": "mixture of melting snow, dark soil, and reddish-brown moss",
      "plants": "sharp focus on small twigs and moss directly under the shoe"
    },
    "imperfections": [
      "mud specs on the white sole",
      "uneven stitching on the pants",
      "natural fabric bunching",
      "film grai"
    ]
  }
}
```

[[Direct Flash Photography]]

---

### 37. 逼真的闪光摄影生活方式照片提示

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-30  **Language**: en

> 一个高度详细、结构化的提示，用于生成逼真的图像，捕捉一位年轻女性在室内俏皮地吃披萨的抓拍、充满活力的生活方式照片，使用直接机顶闪光灯照明，模仿 Z 世代网红美学。

![逼真的闪光摄影生活方式照片提示](https://cms-assets.youmind.com/media/1767455082201_d511za_G9aNV2daYAAYJvE.jpg)

```
{
  "scene_description": "A candid, energetic lifestyle shot of a young blonde woman posing playfully indoors while eating a slice of pizza, captured with direct flash lighting.",
  "subject": {
    "type": "Young woman",
    "age": "Early 20s",
    "features": {
      "hair": "Long, wavy platinum blonde hair, loose and flowing",
      "expression": "Playful, happy smile, looking directly at the camera while taking a bite",
      "skin": "Fair complexion, smooth texture, rosy blush, soft glow",
      "other": "Blue eyes, light makeup, belly button piercing, heart-shaped drop earrings"
    },
    "attire": "Fitted white long-sleeve crop top exposing midriff, dark blue sweatpants/track pants with dual white vertical stripes on the sides",
    "pose_position": "Standing facing forward with torso twisted slightly, right hand holding a slice of pizza to the mouth, left arm raised high in a celebratory gesture"
  },
  "objects_and_props": {
    "main": ["Slice of cheese pizza with slightly browned crust"],
    "secondary": ["Delicate silver necklace", "Simple bracelet on left wrist", "Belly ring"]
  },
  "environment": {
    "setting": "Indoor rustic restaurant or cafe interior",
    "foreground_elements": ["Subject"],
    "background": "Dimly lit interior with wooden paneling on ceiling/walls, a service counter with kitchen equipment, and a window revealing a blue-hour evening city view",
    "atmosphere": "Casual, fun, spontaneous, evening social gathering"
  },
  "lighting": {
    "style": "Direct on-camera flash",
    "key_light": {
      "type": "Frontal flash",
      "direction": "Directly from camera",
      "color": "Cool Red",
      "effects": ["Bright illumination on subject", "Hard cast shadows behind the raised arm", "High contrast against dimmer background"]
    },
    "shadows_contrast": "High contrast characteristic of flash photography, sharp defined shadows"
  },
  "photography_style": {
    "medium": "Smartphone photography / Digital camera with flash",
    "aesthetic": "Gen Z lifestyle, candid influencer snapshot, flash trend",
    "mood": "Playful, carefree, yummy",
    "color_grading": "Vibrant skin tones against a cooler, darker background"
  },
  "camera_and_lens": {
    "angle_view": "Eye-level",
    "framing_composition": "Vertical medium shot (knees or thighs up), centered subject",
    "depth_of_field": "Moderate, subject is sharp while background details are visible but slightly soft",
    "focal_length_feel": "Wide-standard (approx 28-35mm smartphone lens)",
    "bokeh_style": "N/A"
  },
  "render_quality": {
    "realism": "Photorealistic, candid style",
    "resolution": "High resolution",
    "details": "Realistic skin texture, fabric stretch on the crop top, cheese texture on pizza"
  }
}
```

[[Direct Flash Photography]]

---

### 38. 忧郁的日本铁路道口肖像

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2025-12-30  **Language**: en

> 一个高度具体的 JSON 提示，用于生成一张日本郊区铁路道口年轻女性的电影感、高细节肖像照，强调技术相机规格（富士 Fujifilm X-T4, 23mm f/1.4）、强烈的直射闪光灯照明，以及一种忧郁怀旧的氛围。

![忧郁的日本铁路道口肖像](https://cms-assets.youmind.com/media/1767454995476_vkaxvq_G9aFLQKaYAM8bpi.jpg)

```
{
  "image_generation_request": {
    "subject": {
      "description": "Young woman with fair glass-skin, pink blush, dewy glowing skin, softly red-toned lips, and long curled eyelashes.",
      "expression": "Cute, innocent, playful, subtle charm, soft smile looking at camera.",
      "pose": "Frontal view, head-to-waist shot, holding an iPhone 16 Pro Max.",
      "ethnicity_reference": "Use provided face photo for likeness."
    },
    "attire": {
      "headwear": "Mustard-toned knitted Carhartt-style beanie over a neatly styled black hijab.",
      "outerwear": "Black glossy quilted puffer jacket, high collar, oversized structured silhouette.",
      "bottoms": "Light blue wide-leg loose-fit denim jeans.",
      "accessories": "Small minimal silver earrings."
    },
    "environment": {
      "location": "Quiet Japanese suburban railway crossing, residential area.",
      "background_elements": [
        "Lowered yellow-and-black striped crossing barriers",
        "Red glowing railway signal lights",
        "Speeding local commuter train with strong motion blur",
        "Tangled overhead electrical wires and utility poles",
        "Dense green trees and misty cloudy skies",
        "Tactile paving dots and worn asphalt"
      ],
      "lighting_atmosphere": "Overcast day, cool blue tones, moody and nostalgic. Mix of natural ambient twilight and hard paparazzi-style direct camera flash."
    },
    "technical_specs": {
      "camera": "Fujifilm X-T4 mirrorless",
      "lens": "XF 23mm f/1.4",
      "settings": "f/1.8 aperture for shallow depth of field",
      "lighting_technique": "Strong on-camera direct flash, sharp shadow edges, bright white light-bulb effect on face.",
      "composition": "Eye-level front shot, cinematic realism."
    },
    "negative_prompt": [
      "blur",
      "low quality",
      "animation",
      "distortion",
      "cartoon",
      "unreal background",
      "CGI",
      "warm tone",
      "yellow tint",
      "golden hour",
      "foggy light",
      "dreamy haze",
      "dark",
      "underexposed",
      "out of frame",
      "crop error",
      "body at side view"
    ]
  }
}
```

[[Direct Flash Photography]] [[Melancholy Mood]] [[Nostalgic Atmosphere]]

---

### 39. 一位女士吃披萨的抓拍生活照，使用了直射闪光灯

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2025-12-30  **Language**: en

> 一个高度详细、结构化的提示，用于 Gemini Nano Banana Pro 模型，旨在生成一张逼真的、抓拍的 Z 世代年轻女性吃披萨的生活照，特点是高对比度和直接的机顶闪光灯照明。

![一位女士吃披萨的抓拍生活照，使用了直射闪光灯](https://cms-assets.youmind.com/media/1767455073645_fzrzbf_G9ZN6dCXsAAIimx.jpg)

```
{
  "scene_description": "A candid, energetic lifestyle shot of a young blonde woman posing playfully indoors while eating a slice of pizza, captured with direct flash lighting.",
  "subject": {
    "type": "Young woman",
    "age": "Early 20s",
    "features": {
      "hair": "Long, wavy platinum blonde hair, loose and flowing",
      "expression": "Playful, happy smile, looking directly at the camera while taking a bite",
      "skin": "Fair complexion, smooth texture, rosy blush, soft glow",
      "other": "Blue eyes, light makeup, belly button piercing, heart-shaped drop earrings"
    },
    "attire": "Fitted white long-sleeve crop top exposing midriff, dark blue sweatpants/track pants with dual white vertical stripes on the sides",
    "pose_position": "Standing facing forward with torso twisted slightly, right hand holding a slice of pizza to the mouth, left arm raised high in a celebratory gesture"
  },
  "objects_and_props": {
    "main": ["Slice of cheese pizza with slightly browned crust"],
    "secondary": ["Delicate silver necklace", "Simple bracelet on left wrist", "Belly ring"]
  },
  "environment": {
    "setting": "Indoor rustic restaurant or cafe interior",
    "foreground_elements": ["Subject"],
    "background": "Dimly lit interior with wooden paneling on ceiling/walls, a service counter with kitchen equipment, and a window revealing a blue-hour evening city view",
    "atmosphere": "Casual, fun, spontaneous, evening social gathering"
  },
  "lighting": {
    "style": "Direct on-camera flash",
    "key_light": {
      "type": "Frontal flash",
      "direction": "Directly from camera",
      "color": "Cool white",
      "effects": ["Bright illumination on subject", "Hard cast shadows behind the raised arm", "High contrast against dimmer background"]
    },
    "shadows_contrast": "High contrast characteristic of flash photography, sharp defined shadows"
  },
  "photography_style": {
    "medium": "Smartphone photography / Digital camera with flash",
    "aesthetic": "Gen Z lifestyle, candid influencer snapshot, flash trend",
    "mood": "Playful, carefree, yummy",
    "color_grading": "Vibrant skin tones against a cooler, darker background"
  },
  "camera_and_lens": {
    "angle_view": "Eye-level",
    "framing_composition": "Vertical medium shot (knees or thighs up), centered subject",
    "depth_of_field": "Moderate, subject is sharp while background details are visible but slightly soft",
    "focal_length_feel": "Wide-standard (approx 28-35mm smartphone lens)",
    "bokeh_style": "N/A"
  },
  "render_quality": {
    "realism": "Photorealistic, candid style",
    "resolution": "High resolution",
    "details": "Realistic skin texture, fabric stretch on the crop top, cheese texture on pizza"
  }
}
```

[[Direct Flash Photography]] [[High Contrast]] [[Candid Lifestyle Photography]] [[Gen Z Aesthetic]]

---

### 40. 超逼真 Y2K 闪光肖像

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2025-12-29  **Language**: en

> 一个结构化的提示，用于生成一张具有 Y2K 美学风格的超写实肖像，画面中一位女性化着浓艳的妆容，身穿前卫的华丽时装（束身衣、荷叶边迷你裙、过膝袜）。图像采用直射机内闪光灯，营造出强烈的光线、高对比度和锐利的阴影，模拟出复古 CCD 传感器相机的效果。

![超逼真 Y2K 闪光肖像](https://cms-assets.youmind.com/media/1767166895444_2d1xk5_G9WmesDW0AAGlUZ.jpg)

```
{
  "prompt_metadata": {
    "type": "Ultra-Photorealistic Portrait",
    "style": "Flash Photography / Y2K Aesthetic",
    "quality_tier": "Masterpiece, 8k, RAW"
  },
  "subject": {
    "demographics": "Young woman, model",
    "hair": "Long, voluminous blonde hair styled in loose, glamorous waves",
    "face": "Heavy glam makeup, smoky eyeshadow, defined eyeliner, glossy nude lips, sharp contouring",
    "skin": "Fair skin tone with realistic texture, pores, and specular highlights from flash"
  },
  "fashion_and_styling": {
    "upper_body": "Black structured corset with white lace trim along the bustline and sheer black ruffled detailing",
    "lower_body": "White ruffled mini skirt with black ribbon bows attached",
    "accessories": [
      "Sheer black tulle wrist gloves with ruffled edges",
      "White opaque thigh-high stockings",
      "Pearl necklace with a gold pendant",
      "Silver chain belt with 'angel' or text lettering charms draping over the skirt"
    ],
    "aesthetic": "Edgy glamour, 2000s pop star fashion, coquettish"
  },
  "pose_and_action": {
    "stance": "Seated or leaning back against a wall",
    "arms": "Hands placed firmly on the waist/hips, accentuating the corset shape",
    "head_position": "Turned slightly to the right, looking away from the camera",
    "expression": "Confident, sultry, detached coolness"
  },
  "environment": {
    "location": "Minimalist indoor studio",
    "backdrop": "Plain white wall",
    "shadow_play": "Distinct, sharp drop shadow projected directly behind the subject onto the wall"
  },
  "lighting": {
    "type": "Direct on-camera flash (hard lighting)",
    "characteristics": "High contrast, harsh shadows, bright frontal illumination, 'snapshot' aesthetic"
  },
  "camera_technical": {
    "aesthetic": "Digital camera simulation (Canon IXUS or vintage CCD sensor vibe)",
    "focal_length": "35mm",
    "aperture": "f/4.0 (for sharp focus on subject and immediate background)",
    "shutter_speed": "1/125s",
    "iso": "400",
    "details": "Chromatic aberration, slight film grain, sharp focus, ultra-detailed fabric textures"
  }
}
```

[[Direct Flash Photography]] [[High Contrast]]

---

### 41. 闪光摄影：夜间都市人像

**Author**: [Sudee🥀](https://x.com/NameIsSudee)  **Date**: 2025-12-29  **Language**: en

> 一个超写实的肖像提示，模拟夜间城市背景下的原始闪光摄影。主体是一位身穿白色蕾丝鸡尾酒裙的女士，她靠在金属栏杆上，被直接的机顶闪光灯照亮，与城市灯光的散景背景形成高对比度。

![闪光摄影：夜间都市人像](https://cms-assets.youmind.com/media/1767166943902_3t6hlw_G9WRGcfaoAAkgwm.jpg)

```
{
  "prompt_configuration": {
    "type": "Ultra Photorealistic Portrait",
    "aspect_ratio": "3:4",
    "style_model": "Raw Photography"
  },
  "visual_elements": {
    "subject": {
      "description": "Young woman with a fit, slender physique and white skin.",
      "hair": "Long, Platinum white, voluminous curly hair with a slightly wet or glossy texture, draped over the left shoulder.",
      "face": "Defined features, glossy nude lip, subtle smoky eye makeup, looking away from the camera to the left with a candid, relaxed expression.",
      "skin_texture": "High-detail skin pores, natural sheen from flash lighting, realistic complexion."
    },
    "appire_and_styling": {
      "outfit": "White form-fitting cocktail dress (slip style) with lace detailing on the bust cups, a sweetheart neckline, and a small tie-string front. Thin spaghetti straps.",
      "accessories": "Minimalist gold pendant necklace, small stud earrings.",
      "makeup": "Night-out glamour, dewy finish."
    },
    "pose_and_action": {
      "stance": "Leaning forward against a silver metal railing.",
      "hands": "Both hands resting on the railing bar, casual grip.",
      "orientation": "Body angled slightly towards the camera, head turned profile/three-quarters away."
    },
    "environment": {
      "setting": "Nighttime urban waterfront or city bridge.",
      "background": "Dark night sky with out-of-focus city lights (bokeh). Distinct vertical yellow light strips and distant white blurry signage. Dark water visible below the railing.",
      "atmosphere": "City nightlife, vibrant yet dark, candid moment."
    }
  },
  "technical_details": {
    "lighting": {
      "type": "Direct on-camera flash or strobe.",
      "effect": "High contrast between subject and background. Specular highlights on the clavicle, shoulders, and forehead. Sharp shadows falling behind the subject."
    },
    "camera_gear": {
      "camera": "Sony A7R V or Canon EOS R5",
      "lens": "85mm f/1.4 GM",
      "settings": "Aperture f/2.8, ISO 800, Shutter Speed 1/125s",
      "focus": "Sharp focus on the subject's face, shallow depth of field (bokeh background)."
    },
    "quality_tags": [
      "8k resolution",
      "hyper-realistic",
      "raw photo",
      "film grain",
      "paparazzi aesthetic",
      "unreal engine 5 render",
      "masterpiece",
      "highly detailed texture"
    ]
  }
}
```

[[Direct Flash Photography]]

---

### 42. 冬季天使时尚大片提示

**Author**: [Sudee🥀](https://x.com/NameIsSudee)  **Date**: 2025-12-29  **Language**: en

> 一个高度详细、结构化的 JSON 提示，用于生成一张原始、高对比度的时尚社论照片。主体是一位年轻女性，拥有铂金色头发和天使翅膀，夜晚跪在茂密的松树林深雪中，被刺眼的相机闪光灯照亮，营造出神秘、空灵的美感。

![冬季天使时尚大片提示](https://cms-assets.youmind.com/media/1767166902641_gfunzo_G9VtN3FaAAAOjlZ.jpg)
![冬季天使时尚大片提示](https://cms-assets.youmind.com/media/1767166902658_e675b4_G9VtN1faoAA9Vv_.jpg)

```
{
  "prompt": {
    "subject": {
      "appearance": "Young woman with long, straight, platinum white blonde hair parting in the middle, pale complexion, soft features, serious and ethereal expression.",
      "apparel": {
        "top": "Golden strapless corset with structural boning and lace panel detailing.",
        "bottom": "Short golden satin mini-skirt with a flowing hem.",
        "accessories": "Large, realistic white feathered angel wings mounted on the back. White patterned lace/fishnet tights.",
        "footwear": "Knees and lower legs buried in snow (shoes not visible)."
      },
      "pose": "Kneeling on the ground in deep snow, body angled slightly forward, arms relaxed by sides, engaging directly with the camera."
    },
    "environment": {
      "location": "Dense pine forest at night.",
      "atmosphere": "Winter storm, cold and dark.",
      "details": "Tall dark tree trunks in the background, ground covered in a thick layer of fresh white snow, heavy snow falling captured as streaks and distinct flakes."
    },
    "lighting": {
      "style": "Direct camera flash / Flash photography aesthetic.",
      "characteristics": "High contrast between the bright subject and the pitch-black background. Harsh, cool-toned light illuminating the subject's face, outfit, and the immediate snow around her. Light catching the falling snowflakes, making them glow bright white."
    },
    "camera_and_tech": {
      "perspective": "Eye-level shot.",
      "lens_effects": "Slight background blur (bokeh) on the trees, sharp focus on the subject.",
      "aesthetic": "Raw photo, 35mm film grain texture, editorial fashion photography style.",
      "quality": "Ultra photorealistic, 8k resolution, highly detailed textures (feathers, lace, snow crystals, skin texture), masterpiece, cinematic composition."
    },
"Ratio":"5:6"
    "mood": "Mysterious, haunting, angelic, melancholic, ethereal, winter fantasy."
  }
}
```

[[Direct Flash Photography]] [[Platinum Hair]] [[Angel Wings]]

---

### 43. 闪光摄影海滩人像提示（夜间比基尼）

**Author**: [Lina Byte](https://x.com/LinaByteME)  **Date**: 2025-12-26  **Language**: en

> 一个详细的提示，用于生成一张年轻女性在夜晚的黑暗海滩上的半身肖像，使用直射机顶闪光灯摄影，以获得高对比度和光泽的皮肤纹理，并穿着黑色三角比基尼。

![闪光摄影海滩人像提示（夜间比基尼）](https://cms-assets.youmind.com/media/1766988028603_s03ib1_G9Hl-t8XEAE8BvN.jpg)

```
{
  "aspect_ratio": "3:4",
  "scene_type": "night beach fashion portrait photography",
  "environment": {
    "location": "sandy beach at night",
    "background": "dark ocean horizon with faint waves, almost black sky",
    "lighting_conditions": "low ambient light, strong direct camera flash"
  },
  "subject": {
    "type": "young woman",
    "age_range": "early to mid 20s",
    "ethnicity": "white",
    "skin_tone": "light, slightly tanned, wet skin glow",
    "body_type": "slim, athletic, feminine proportions",
    "pose": {
      "arms": "both arms raised with fists placed under cheeks",
      "expression": "playful pout, lips puckered",
      "head_position": "facing camera directly",
      "posture": "upright, confident, relaxed"
    },
    "clothing": {
      "outfit": "black triangle bikini",
      "style": "minimal, modern swimwear",
      "fit": "snug, natural"
    },
    "hair": {
      "color": "blonde",
      "style": "wet, loose, naturally wavy",
      "parting": "center part"
    },
    "face_details": {
      "eyes": "light-colored eyes, open and relaxed",
      "makeup": "minimal or no makeup, natural skin texture",
      "skin_details": "subtle freckles, realistic pores"
    }
  },
  "camera": {
    "shot_type": "medium portrait",
    "framing": "waist-up, centered composition",
    "angle": "eye level",
    "lens": "35mm equivalent",
    "focus": "sharp focus on subject, background slightly falling off"
  },
  "lighting": {
    "key_light": "direct on-camera flash",
    "effect": "high contrast, crisp highlights, glossy skin",
    "shadows": "soft but visible shadows behind subject"
  },
  "style": {
    "photography_style": "flash photography, candid beach portrait",
    "aesthetic": "natural, playful, confident",
    "color_grading": "neutral tones, slightly warm skin highlights"
  },
  "quality": {
    "resolution": "high resolution",
    "detail_level": "skin texture preserved, no over-smoothing",
    "realism": "photorealistic"
  },
  "negative_prompt": [
    "cartoon",
    "anime",
    "illustration",
    "overly sexualized pose",
    "exaggerated anatomy",
    "blurred face",
    "extra limbs",
    "deformed hands",
    "plastic skin",
    "heavy makeup",
    "studio background"
  ]
}
```

[[Direct Flash Photography]]

---

### 44. 闪光灯下的时尚夜间奢华人像

**Author**: [yusra.](https://x.com/chatgptpaglu)  **Date**: 2025-12-23  **Language**: en

> 一个 JSON 提示，用于生成一张魅力四射的夜奢风格女性肖像，她身穿镶有水钻的连衣裙和仿皮草外套，采用直射闪光摄影风格以营造硬朗的阴影。

![闪光灯下的时尚夜间奢华人像](https://cms-assets.youmind.com/media/1766673277451_wfo6cq_G82V035WwAE9XhY.jpg)

```
{
  "image_prompt": {
    "subject": {
      "type": "Young woman",
      "appearance": {
        "hair": "Sleek blonde hair pulled back into a tight bun",
        "skin": "Glowing, tanned complexion",
        "expression": "Playful 'kissy face' with puckered lips"
      }
    },
    "attire": {
      "dress": {
        "color": "{argument name="dress color" default="Nude / Beige"}",
        "style": "Halter neck with a central keyhole cutout at the chest",
        "texture": "Embellished with small sparkling rhinestones or crystals throughout"
      },
      "outerwear": "White plush faux-fur coat or stole, draped loosely around the elbows and forearms"
    },
    "accessories": {
      "eyewear": "Small, sleek rectangular black sunglasses",
      "jewelry": "Thick gold hoop earrings"
    },
    "action": {
      "pose": "Sitting relaxed on a sofa",
      "interaction": "Holding a coupe cocktail glass filled with amber liquid in the right hand, raised slightly"
    },
    "setting": {
      "location": "Indoors, likely a lounge or club",
      "background": "Grey curtain drapes",
      "furniture": "White textured sofa",
      "lighting": "Direct flash photography style with hard shadows behind the subject"
    },
    "mood": "Glamorous, chic, night-luxe, confident"
  }
}
```

[[Direct Flash Photography]] [[Faux Fur Coat]]

---

### 45. 闪光灯直打，打造迷人夜奢人像

**Author**: [ShaHid WaNii](https://x.com/meng_dagg695)  **Date**: 2025-12-23  **Language**: en

> 为 Gemini Nano Banana Pro 生成一张迷人、时尚的年轻女性肖像的提示，背景设定在休息室或俱乐部。主体身穿一件裸色水晶点缀露背连衣裙，搭配橄榄红人造皮草外套、太阳镜和金色大耳环。提示指定采用直射闪光摄影风格，营造出硬朗的阴影，以呈现夜间奢华美学。

![闪光灯直打，打造迷人夜奢人像](https://cms-assets.youmind.com/media/1766673255096_y55y59_G81hxOdX0AEznk0.jpg)
![闪光灯直打，打造迷人夜奢人像](https://cms-assets.youmind.com/media/1766673259353_x2wftt_G81wX4saAAE2JSR.jpg)

```
{
Image size - 1200×1200
  "image_prompt": {
    "subject": {
      "type": "Young woman",
      "appearance": {
        "hair": "Sleek blonde hair pulled back into a tight bun",
        "skin": "Glowing, tanned complexion",
        "expression": "Playful 'kissy face' with puckered lips"
      }
    },
    "attire": {
      "dress": {
        "color": "Nude / Beige",
        "style": "Halter neck with a central keyhole cutout at the chest",
        "texture": "Embellished with small sparkling rhinestones or crystals throughout"
      },
      "outerwear": "{argument name="coat color" default="olive red"} plush faux-fur coat or stole, draped loosely around the elbows and forearms"
    },
    "accessories": {
      "eyewear": "Small, sleek rectangular black sunglasses",
      "jewelry": "Thick gold hoop earrings"
    },
    "action": {
      "pose": "Sitting relaxed on a sofa",
      "interaction": "Holding a coupe cocktail glass filled with amber liquid in the right hand, raised slightly"
    },
    "setting": {
      "location": "Indoors, likely a lounge or club",
      "background": "Grey curtain drapes",
      "furniture": "{argument name="sofa color" default="olive red"} textured sofa",
      "lighting": "Direct flash photography style with hard shadows behind the subject"
    },
    "mood": "Glamorous, chic, night-luxe, confident"
  }
}
```

[[Direct Flash Photography]]

---

### 46. 华丽夜奢人像提示词

**Author**: [Melisa♡](https://x.com/xmliisu)  **Date**: 2025-12-23  **Language**: en

> 为 Gemini Nano Banana Pro 生成的图像提示，详细描述了一位年轻金发女性的迷人夜奢肖像。她身穿米色水钻露背连衣裙，披着白色仿皮草外套，坐在沙发上，手持鸡尾酒杯，采用直射闪光摄影风格。

![华丽夜奢人像提示词](https://cms-assets.youmind.com/media/1766935931998_cfcy1y_G81hxOdX0AEznk0.jpg)

```
{
  "image_prompt": {
    "subject": {
      "type": "Young woman",
      "appearance": {
        "hair": "Sleek blonde hair pulled back into a tight bun",
        "skin": "Glowing, tanned complexion",
        "expression": "Playful 'kissy face' with puckered lips"
      }
    },
    "attire": {
      "dress": {
        "color": "Nude / Beige",
        "style": "Halter neck with a central keyhole cutout at the chest",
        "texture": "Embellished with small sparkling rhinestones or crystals throughout"
      },
      "outerwear": "White plush faux-fur coat or stole, draped loosely around the elbows and forearms"
    },
    "accessories": {
      "eyewear": "Small, sleek rectangular black sunglasses",
      "jewelry": "Thick gold hoop earrings"
    },
    "action": {
      "pose": "Sitting relaxed on a sofa",
      "interaction": "Holding a coupe cocktail glass filled with amber liquid in the right hand, raised slightly"
    },
    "setting": {
      "location": "Indoors, likely a lounge or club",
      "background": "Grey curtain drapes",
      "furniture": "White textured sofa",
      "lighting": "Direct flash photography style with hard shadows behind the subject"
    },
    "mood": "Glamorous, chic, night-luxe, confident"
  }
}
```

[[Direct Flash Photography]] [[Blonde Female Portrait]] [[White Faux Fur Coat]]

---

### 47. 高对比度肖像：直射闪光灯与人造毛皮

**Author**: [Anissa](https://x.com/SimplyAnnisa)  **Date**: 2025-12-22  **Language**: en

> 一个高度技术性的提示，用于生成一张 8k 原始照片肖像，具有极致的微对比度和触感细节。主体带着顽皮的表情，手持一部闪光灯亮起的智能手机，被一个蓬松的白雪公主仿皮草兜帽框住，强调了刺眼的灯光和深景深。

![高对比度肖像：直射闪光灯与人造毛皮](https://cms-assets.youmind.com/media/1766667334182_9udt96_G8v2OR1aUAAl1Ir.jpg)
![高对比度肖像：直射闪光灯与人造毛皮](https://cms-assets.youmind.com/media/1766667335253_3r58nk_G8v2OOLagAAXAKZ.jpg)

```
8k raw photo with natural ISO grain, sharp micro-contrast, tactile surface details. Keep the reference face and body proportions fully consistent. Upper torso framed, cut at mid-chest. Subject's head tilted 5 degrees right, eyes gazing playfully 10 degrees right and 5 degrees up, pupils slightly dilated. Lips parted, tongue peeking out in a mischievous gesture. Skin displays visible skin porosity, sharp micro-details, and fine tactile skin grain, with a subtle dusting of freckles just below the eyes. Natural vellus hair is visible. High-voltage specular highlights and flash feedback on skin, forehead, and nose, indicative of direct flash. Subject's left arm raised, fingers tensed gripping a Silver Mist iPhone with three camera lenses and an active flash module, emitting a bright, circular cool white light. Voluminous, shaggy {argument name="fur color" default="Snow White"} faux fur hood with curly fibers frames the face, lined with smooth Pale Rose satin on the inner ears and trim. A matching Snow White faux fur coat/shawl with fluffy drape covers the shoulders. Direct on-camera flash creates high-contrast illumination, hard shadows behind the phone and subject, and intense specular highlights on all surfaces. Deep depth of field, f/16 aperture, hyperfocal distance, ensuring the background is fully in sharp focus with zero bokeh. Background features a smooth Light Greige wall. A partial Obsidian Black rectangular frame is visible on the left, reflecting an indistinct dark area. Projecting a playful, mischievous aura.
```

[[Direct Flash Photography]] [[Playful Expression]] [[Deep Depth Of Field]]

---

### 48. 夜晚海滩上的倒置闪光照片 (重复)

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2025-12-22  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张创意十足的、高角度拍摄的闪光照片，场景设定在夜晚的沙滩上，采用“倒置”构图，即拍摄主体的头部位于画面底部。它详细描述了主体的波波头、具体服装（热带比基尼上衣、牛仔短裤），以及直射闪光摄影特有的强烈、高对比度光线。这是提示 2003173847890059682 的重复。

![夜晚海滩上的倒置闪光照片 (重复)](https://cms-assets.youmind.com/media/1766667278448_d8po7y_G8vvGbsW8AAAOlY.jpg)

```
{
  "image_description": "A high-angle, top-down shot of a person lounging upside-down on a colorful beach chair at night.",
  "composition": {
    "perspective": "Upside-down portrait, bird's-eye view",
    "subject_positioning": "The subject's head is at the bottom of the frame, with legs extending toward the top",
    "lighting": "Flash photography, direct front-on light creating sharp shadows on the sand"
  },
  "subject_details": {
    "hair": "Short, ash-brown bob with wispy bangs covering part of the forehead",
    "makeup": "Dewy skin finish, glossy pink lips, and defined eyebrows",
    "pose": "Lying flat on the back, one hand resting on the stomach, the other hand near the face with fingers touching the lips",
    "tattoos": "A crescent moon tattoo on the collarbone with delicate script text"
  },
  "clothing_and_accessories": {
    "top": "White spaghetti-strap bikini top with a blue tropical palm tree print",
    "bottom": "Light-wash denim shorts",
    "footwear": "Light blue rubber flip-flops",
    "jewelry": "Gold chain necklace with a sunburst or celestial pendant"
  },
  "environment": {
    "setting": "Sandy beach at night",
    "furniture": "Vintage blue wooden folding beach chair with a multi-colored striped (rainbow) fabric seat",
    "background": "Textured, dry sand with soft shadows"
  },
  "aesthetic_style": {
    "vibe": "Summer night, casual, nostalgic, flash-heavy aesthetic",
    "color_palette": ["Cerulean blue", "Sand beige", "Denim light blue", "Rainbow stripes", "Golden accents"]
  }
}
```

[[Direct Flash Photography]] [[High Contrast Photography]] [[Creative Composition]]

---

### 49. 2x2 网格意大利餐馆快闪拍摄提示

**Author**: [Ditherly - Creative AI Hub](https://x.com/ditherly_art)  **Date**: 2025-12-21  **Language**: en

> 一个结构化的提示词，用于生成一个 2x2 的逼真图像网格，其中包含同一个角色（基于参考图像），置身于光线昏暗的意大利小餐馆中。该提示词指定了“直射闪光灯高对比度颗粒感”的风格，详细描述了人物的外观（盘发、黑色露肩上衣、金色大耳环），以及四个与用餐相关的不同姿势/表情（卷意面、开怀大笑饮酒、被闪光灯晃到、慵懒地斜倚）。

![2x2 网格意大利餐馆快闪拍摄提示](https://cms-assets.youmind.com/media/1766489473469_wwh6r4_G8tikmtWkAAA0Lp.jpg)

```
{
  "generation_request": {
    "meta_data": { "tool": "NanoBananaPro", "task_type": "photorealistic_multi_panel_grid", "version": "v1.0" },
    "output_settings": {
      "layout": { "type": "2x2_grid", "border": "thin_black_gutter", "frame_consistency_rule": "same_person_same_outfit_same_restaurant" },
      "aspect_ratio": "4:5", "resolution": "ultra_high_res", "render_style": "direct_flash_high_contrast_grainy"
    },
    "reference_constraints": {
      "character_reference_image": "{argument name="character reference image" default="UPLOAD_REF_IMAGE"}", "use_reference_face_only": true, "identity_lock": true, "strict_face_match": true
    },
    "global_prompt": {
      "scene": "Dimly lit Italian trattoria at night. White tablecloths. Wine glasses. Plate of pasta. Background is dark and blurry.",
      "subject": {
        "type": "influencer",
        "identity": "same person as reference image",
        "hair": "updo with claw clip, messy face-framing pieces",
        "makeup": "glowy skin, brushed up brows, bitten lip look",
        "outfit": "black off-the-shoulder top (tight), gold hoop earrings, layered necklaces",
        "prop": "fork with pasta or glass of red wine"
      },
      "camera": { "capture": "hard flash", "lens_equivalent": "28mm", "focus": "subject", "depth_of_field": "sharp foreground" }
    },
    "frames": [
      { "frame_id": "A", "position": "top_left", "shot_type": "twirling_pasta", "pose": "Looking down at the pasta, twirling a massive amount on a fork. Flash reflecting off the sauce.", "expression": "focused, hungry" },
      { "frame_id": "B", "position": "top_right", "shot_type": "wine_laugh", "pose": "Holding wine glass by the stem, head thrown back laughing at someone across the table. Hand covering mouth slightly.", "expression": "candid joy" },
      { "frame_id": "C", "position": "bottom_left", "shot_type": "flash_blinded", "pose": "Holding hand up to block the flash, eyes squinting, looking directly at lens.", "expression": "playful annoyance" },
      { "frame_id": "D", "position": "bottom_right", "shot_type": "messy_table", "pose": "Leaning elbows on the table, chin in hands, looking seductive/tired. Table is messy with empty plates.", "expression": "sultry" }
    ]
  }
}
```

[[Direct Flash Photography]] [[Character Consistency]]

---

### 50. Y2K 垃圾摇滚浴室自拍提示

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2025-12-20  **Language**: en

> 一个用于 Gemini 3.0 / Nano Banana Pro 的图像生成提示，内容是一位身穿 Y2K 垃圾摇滚风格服装（黑色哥特图案背心，蝙蝠吊坠）的年轻女性，在涂鸦遍布的粗糙浴室里自拍，利用刺眼的闪光灯摄影营造出前卫的视觉效果。

![Y2K 垃圾摇滚浴室自拍提示](https://cms-assets.youmind.com/media/1766385994259_2vhxu2_G8nsrvraAAAmrD7.jpg)

```
{
  "image_analysis": {
    "subject": {
      "demographics": "{argument name="demographics" default="Young woman, estimated late teens to early 20s"}",
      "skin": "{argument name="skin" default="Light complexion, smooth texture with soft sheen"}",
      "hair": {
        "color": "{argument name="hair color" default="Dark brown/Black"}",
        "style": "{argument name="hair style" default="Long, voluminous, messy/tousled texture, layered"}",
        "details": "{argument name="hair details" default="Framing the face, slightly wind-blown look"}"
      },
      "facial_features": {
        "eyes": "{argument name="eyes" default="Light green/hazel, almond-shaped, sharp winged eyeliner, long lashes"}",
        "lips": "{argument name="lips" default="Full, pouty, glossy pink/nude shade"}",
        "expression": "{argument name="expression" default="Confident, sultry, direct gaze at camera"}"
      }
    },
    "attire": {
      "top": {
        "color": "{argument name="top color" default="Black"}",
        "style": "{argument name="top style" default="Tank top / Camisole with spaghetti straps"}",
        "graphic": "{argument name="graphic" default="White gothic-style font and imagery (resembling a metal band logo or skeleton graphic) across the chest"}"
      },
      "accessories": {
        "necklace": "{argument name="necklace" default="Silver chain with a large, detailed pendant shaped like a bat with spread wings"}",
        "other": "{argument name="other accessories" default="Hint of a dark belt or waistband visible at the bottom"}"
      }
    },
    "environment": {
      "location": "{argument name="location" default="bathroom"}",
      "background_elements": [
        "{argument name="background element 1" default="White/beige tiled walls with grime and wear"}",
        "{argument name="background element 2" default="Black graffiti tags/markers on the tiles"}",
        "{argument name="background element 3" default="Framed advertisement posters on the wall (right side)"}",
        "{argument name="background element 4" default="Overhead fluorescent strip lights on the ceiling"}"
      ]
    },
    "technical_specs": {
      "perspective": "{argument name="perspective" default="Selfie angle (arm visible on left), close-up shot"}",
      "lighting": "{argument name="lighting" default="Direct on-camera flash (harsh lighting on subject, darker background)"}",
      "camera_style": "{argument name="camera style" default="Digital snapshot, slightly grainy/lo-fi aesthetic, 'flash photography'"}",
      "aesthetic": "{argument name="aesthetic" default="Y2K grunge, urban street style, edgy, 'cool girl' vibe, candid night shot"}"
    }
  }
}
```

[[Direct Flash Photography]] [[Y2K Aesthetic]] [[Alternative Fashion]]

---

### 51. 用于 Direct-Flash 复古游戏女孩肖像的结构化提示

**Author**: [Lore](https://x.com/l_w_lorenzen)  **Date**: 2025-12-17  **Language**: en

> 一个为 Degaus Nano Banana Pro 设计的高度结构化 JSON 提示，旨在生成一张年轻女性在复古游戏室中的逼真肖像，采用一种独特的、让人联想到 80/90 年代的直闪摄影风格。该提示详细说明了拍摄对象的样貌、姿势（盘腿而坐，手持控制器）、细致的环境（摆满收藏品的架子），以及由机顶闪光灯产生的高对比度照明效果。

![用于 Direct-Flash 复古游戏女孩肖像的结构化提示](https://cms-assets.youmind.com/media/1766042200149_lpgeok_G8Yi3ixaYAAL7Pi.jpg)

```
{

"label": "direct-flash-gamer-girl",

"tags": [

"direct-flash",

"retro-gamer-room",

"90s-photography",

"film-aesthetic",

"gamer-girl",

"collectibles-shelf",

"low-angle",

"sitting-pose"

],

"CompositionalPortrait": 1,

"Style": [

"direct-flash-photography-3",

"80s-90s-club-photo-2",

"warm-film-tone-2",

"documentary-candid-style-2"

],

"Subject": [

"young woman in her early 20s with fair skin and soft natural features",

"long dark hair styled in two loose braids with subtle flyaways for realism",

"wearing a fitted white cotton camisole top with thin straps and matching high-waisted white shorts",

"minimal natural makeup with a soft pink tint on cheeks and lips",

"eyes looking directly into the camera with a calm, intimate, slightly teasing expression",

"seated cross-legged on a couch, holding a game controller naturally in both hands"

],

"MadeOutOf": [

"white cotton camisole top",

"white high-waisted shorts",

"black over-ear gaming headphones",

"black wireless controller",

"small plush Pikachu toy placed beside her on the couch",

"red textured pillow behind her"

],

"Arrangement": "subject sits centered on a worn retro couch in a relaxed cross-leg position, holding the controller naturally with both hands; direct flash highlights her face and the texture of her outfit, while the surrounding collectible shelves create depth and visual clutter in the background.",

"Accessories": [

"retro gaming consoles stacked on shelves",

"boxed action figures and collectible toys in various sizes",

"soft plush Pikachu next to the subject",

"gaming headset cable draped naturally across her shoulder"

],

"Background": "a dimly lit retro gamer room filled with densely packed shelves of action figures, boxed toys, handheld consoles, and vintage game cases; warm tungsten floor lamp providing ambient background glow; slight shadow falloff caused by the direct flash illuminating the foreground more prominently.",

"RoomObjects": [

"crowded black shelving full of collectible action figures",

"vintage CRT monitor partially visible on lower shelf",

"floor lamp with soft warm bulb",

"stuffed toys in the corner of the couch",

"assorted retro controllers scattered near the subject"

],

"ColorRestriction": [

"overall palette grounded in warm tungsten tones",

"subject outfit remains clean white for contrast",

"background shelves maintain mixed reds, blacks, and muted neons from toy packaging",

"flash introduces slightly cooler highlights on skin and fabric"

],

"Lighting": "strong direct on-camera flash aimed straight at the subject, creating bold highlights on the face and clothing; shadows cast sharply behind objects; ambient tungsten lamp in the background adds warm separation light; overall high contrast with slight film-like grain.",

"Camera": {

"type": "digital rangefinder or compact mirrorless emulating film aesthetic",

"lens": "35mm equivalent prime lens",

"aperture": "f/2.0",

"iso": "40
```

[[Direct Flash Photography]]

---

### 52. 2000 年代模拟胶片联系表肖像提示

**Author**: [Ozgur Can Akbas](https://x.com/ozgurcanakbas)  **Date**: 2025-12-04  **Language**: en

> 一个复杂的提示，旨在生成一张具有 2000 年代原始模拟摄影接触印画风格的肖像。它指定了 4x4 网格布局，特里·理查森（Terry Richardson）风格的刺眼闪光灯照明，背景是深红色墙壁，姿势自然，并包含详细的胶片元素，如可见的边框、“KODAK 160NC”字样和蜡笔标记。

![2000 年代模拟胶片联系表肖像提示](https://cms-assets.youmind.com/media/1765106412468_l752w4_G7UyZ_mXAAApB8F.jpg)
![2000 年代模拟胶片联系表肖像提示](https://cms-assets.youmind.com/media/1765106412443_ilq1jt_G7UyLECWoAAWlwH.jpg)

```
(masterpiece, best quality), [use the person from attached photo, featuring the exact facial features of the attached reference photo]. The subject is wearing something fashionable, captured in a raw analog photography style.
Composition: An authentic 35mm film contact sheet layout, grid of 4x4 vertical film strips on a black backing.
Scene & Lighting: Standing against a solid, vibrant deep red wall. Harsh direct camera flash, hard shadows cast on the red wall behind the subject, Terry Richardson style lighting, shiny skin texture.
Poses: The subject is shown in slight variations of daily casual movements: fixing hair, looking away, laughing, adjusting shirt, looking straight at lens. Not overly posed, very candid and snapshot-like.
Details: Visible film borders with 'KODAK 160NC' text, frame numbers on the sides. Overlay of green and red grease pencil markings, scribble crop marks, and rough selection X's on the film strips. Grainy texture, high saturation, retro 2000s magazine aesthetic.
```

[[Direct Flash Photography]] [[Deep Red Background]]

---

### 53. 直闪玩家少女 Nano Banana Pro JSON 标签提示

**Author**: [ΛRMIN | AI](https://x.com/Arminn_Ai)  **Date**: 2025-11-30  **Language**: en

> 一个结构化的 Nano Banana Pro 图像提示，通过标签和描述性标记定义了一个使用直射闪光灯的玩家女孩场景，非常适合复古游戏室摄影美学。

![直闪玩家少女 Nano Banana Pro JSON 标签提示](https://cms-assets.youmind.com/media/1764577267047_5sdrbr_G7BoKccXgAAimPo.jpg)
![直闪玩家少女 Nano Banana Pro JSON 标签提示](https://cms-assets.youmind.com/media/1764577281117_gzf0nh_G7BoKeoXcAAq0zA.jpg)

```
{
  "label": "{argument name="label" default="direct-flash-gamer-girl"}",
  "tags": [
    "{argument name="lighting style" default="direct-flash"}",
    "{argument name="room theme" default="retro-gamer-room"}",
    "{argument name="era photography" default="90s-photography"}",
    "{argument name="image aesthetic" default="film-aesthetic"}",
    "{argument name="subject type" default="gamer-girl"}",
    "{argument name="background detail" default="collectibles-shelf"}",
    "{argument name="camera angle" default="low-angle"}",
    "{argument name="pose" default="sitting-pose"}"
  ]
}
```

[[Direct Flash Photography]]

---

### 54. 粗犷电影感雨中肖像

**Author**: [Minahil](https://x.com/Minahil42298354)  **Date**: 2026-04-10  **Language**: en

> 一个超高细节的电影感肖像提示词，描绘了一名身处大雨中的男子，呈现出戏剧性的火光与阴影双色调照明效果。

![粗犷电影感雨中肖像](https://cms-assets.youmind.com/media/1776129410908_8gep82_HFhLVombQAQY1X_.jpg)

```
Hyper-realistic cinematic portrait of a {argument name="subject" default="rugged man with intense, glowing sapphire blue eyes"}, drenched in heavy rainfall. His face is weathered and covered in grit and water droplets, featuring a thick, unkempt beard and wet, matted hair clinging to his forehead. {argument name="lighting" default="Dual-tone lighting: one side of his face is illuminated by a warm, flickering orange glow, while the other side is cast in cool, dark shadows"}. Extreme close-up, 8k resolution, shot on {argument name="lens" default="35mm lens"}, moody atmosphere, hyper-detailed skin texture, dramatic chiaroscuro effect.
```

[[Dramatic Lighting]] [[Cinematic Photography]] [[Male Portrait]]

---

### 55. 时尚男士高定大片提示词

**Author**: [Harboris](https://x.com/harboriis)  **Date**: 2026-04-08  **Language**: en

> 这是一份为 PixPrettyAI 上的 Nano Banana 2 编写的详细图像生成提示词，描述了一位身着全黑定制西装的时尚男士，背景为纯黑，配以金色配饰、戏剧性光影，呈现出高定时尚大片的视觉效果。

![时尚男士高定大片提示词](https://cms-assets.youmind.com/media/1775717431090_k2on1o_HFXqRv2a8AAyagp.jpg)

```
A stylish man a sleek, all-black outfit poses confidently against a pitch-black background. He wears a tailored black suit, a black shirt with the top buttons open, and a subtle gold chain around his neck, he sports golden sunglasses and a well-groomed beard, exuding charisma and mystery A luxury wristwatch glint on his left wrist, the lighting is dramatic, highlighting his facial features and casting soft shas, creating a bold, high -fashion editorial look
```

[[Dramatic Lighting]] [[Studio Portrait]] [[Luxury Fashion Editorial]]

---

### 56. 电影感高定时尚肖像，采用明暗对照法 (Chiaroscuro) 布光

**Author**: [Minahil](https://x.com/Minahil42298354)  **Date**: 2026-04-02  **Language**: en

> 这是一个为 Gemini Nano Banana 设计的提示词，旨在创作一张电影感的高定时尚肖像，刻画一位优雅女性，详细描述了发型、妆容、服饰、姿势，并利用强烈的明暗对照法 (Chiaroscuro) 在黑色背景下进行布光。

![电影感高定时尚肖像，采用明暗对照法 (Chiaroscuro) 布光](https://cms-assets.youmind.com/media/1775198516297_bs33un_HE58jdDW8AMj_Yp.jpg)

```
A cinematic, high-fashion portrait of a sophisticated woman looking off-camera. She has voluminous, wavy {argument name="hair color" default="ash-brown"} hair with wind-swept strands across her face. Her expression is poised and enigmatic.
​Styling & Details: * Makeup: Bold, matte deep-red lipstick and subtle, smokey eye makeup.
​Attire: A sheer, pleated black blouse with a large pussy-bow necktie and billowy sleeves.
​Accessories: Elegant teardrop diamond chandelier earrings and deep burgundy manicured nails.
​Pose: One hand delicately tucked under the chin, showcasing a slim gold ring.
​Lighting & Atmosphere: * Chiaroscuro Lighting: Strong rim lighting that highlights the texture of the hair and the silhouette against a solid black background.
​Mood: Elegant, moody, and luxurious.
​Technical: 85mm lens, shallow depth of field, sharp focus on the facial features, professional studio photography style.
```

[[Dramatic Lighting]] [[Black Background]] [[Elegant Female Portrait]] [[Couture Fashion Photography]]

---

### 57. 生物机械头骨的戏剧性明暗对照法油画

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-03-31  **Language**: en

> 这是为 Nano Banana Pro 设计的一款详细提示词，描述了一幅戏剧性的明暗对照法油画，画面主体为镶嵌在水晶中的生物机械头骨，置于大理石阳台上。作品采用深祖母绿和焦赭色调，呈现出明显的笔触感及华丽的金色装饰。

![生物机械头骨的戏剧性明暗对照法油画](https://cms-assets.youmind.com/media/1775026345646_vub6cu_HEvt1TIboAAq94M.jpg)
![生物机械头骨的戏剧性明暗对照法油画](https://cms-assets.youmind.com/media/1775026346396_q1syez_HEvt1TGaQAAgMdY.jpg)
![生物机械头骨的戏剧性明暗对照法油画](https://cms-assets.youmind.com/media/1775026347179_kybmev_HEvt1TIbUAA4Qzo.jpg)
![生物机械头骨的戏剧性明暗对照法油画](https://cms-assets.youmind.com/media/1775026347207_nr80u2_HEvt1SnXoAEKaiN.jpg)

```
Dramatic chiaroscuro oil-painting texture of a biomechanical skull embedded in crystal on a marble balcony, deep emerald and burnt umber tones with visible brushwork, ornate gold accents catching single dramatic light source, museum gallery depth and tactile surface quality.
```

[[Dramatic Lighting]]

---

### 58. 超写实动漫聚光灯人像提示词

**Author**: [Memes](https://x.com/daniayl12)  **Date**: 2026-03-31  **Language**: en

> 一份为 Nano Banana 2 准备的详细提示词，用于生成黑色背景下的超写实动漫女性角色人像，通过仅聚焦于面部的窄光束聚光灯，营造出阴郁、高对比度的戏剧性效果。

![超写实动漫聚光灯人像提示词](https://cms-assets.youmind.com/media/1775026355185_jd0exo_HEu0Dnea0AADMlw.jpg)
![超写实动漫聚光灯人像提示词](https://cms-assets.youmind.com/media/1775026355463_moydfn_HEu0DnsbkAAUmWw.jpg)

```
Generate a hyperrealistic realistic-anime portrait of a female character standing in a completely black background.
Lighting: use a **narrow beam spotlight** focused only on the center of the face. 
The edges of the light must be sharp and dramatic. 
All areas outside the spotlight should fall quickly into deep darkness 
(high falloff shadow), almost blending into the black background. 
Not soft lighting.
Hair: long dark hair with some strands falling over the face. The lower parts of the hair should fade into the shadows.
Pose: one hand raised gently to the lips in a shy, hesitant gesture. 
Eyes looking directly at the camera with a mysterious mood.
Clothing: black long-sleeve knit sweater; 
the sweater and body should mostly disappear into the darkness with minimal detail.
Overall tone: dark, moody, dramatic, mysterious. 
High-contrast only in the lit portion of the face. 
Everything outside the spotlight should be nearly invisible.
```

[[Dramatic Lighting]] [[High Contrast]] [[Black Background]]

---

### 59. 电影感图书馆场景：正在通话的年轻女性

**Author**: [Minahil](https://x.com/Minahil42298354)  **Date**: 2026-03-30  **Language**: en

> 这是一个用于生成高分辨率电影感图像的详细提示词，描绘了一位年轻女性在古典木质图书馆中，神情担忧地使用智能手机通话的瞬间。提示词明确了光影、氛围以及古籍和铅条玻璃窗等背景元素。

![电影感图书馆场景：正在通话的年轻女性](https://cms-assets.youmind.com/media/1774939637931_6ahcfz_HEpe48FWYAArrzk.jpg)

```
A high-resolution cinematic shot of a young woman with wavy light-brown hair standing in a classic, wood-paneled private library. She is wearing an oversized, cozy grey cashmere sweater and dark leggings, looking slightly concerned while talking on a smartphone. In the background, floor-to-ceiling mahogany bookshelves filled with antique books, a leather wingback chair, and a large leaded-glass window showing a glimpse of a lush garden. Soft, natural indoor lighting with a warm, scholarly atmosphere.
```

[[Dramatic Lighting]] [[Cinematic Atmosphere]]

---

### 60. 菠萝浸泡在果汁中的超写实微距摄影

**Author**: [8bit](https://x.com/jiangyuhe618)  **Date**: 2026-03-30  **Language**: en

> 这是一个高度详细的提示词，用于创作一张超写实、电影质感的微距摄影作品，聚焦于一颗伫立在自身果汁池中的菠萝。提示词强调了戏剧性的光影、细微的粉色粉末点缀、凝结的水珠以及纹理丰富的板岩表面，突显了画面的深度与细节。

![菠萝浸泡在果汁中的超写实微距摄影](https://cms-assets.youmind.com/media/1774939638180_mp5f94_HEpNxhGbYAEHhFU.jpg)

```
A hyper-realistic, cinematic macro photograph, vertical composition (9:16 aspect ratio). At the center of the frame is a single, large, perfect pineapple, standing upright with its full crown of vibrant green leaves, in a deep golden-yellow, viscous pool of pineapple juice. This central pineapple is very lightly and subtly dusted with fine pink powder (e.g., pitaya powder or pink confectioner's sugar), a minimal dusting especially around its leafy crown and textured skin, and is slick with intricate, visible condensation water droplets. Delicate, wispy white steam rises from the top and around the pineapple's leafy crown, creating a dramatic interaction with the dark, moody, textured background. The pineapple juice pool is set on a dark, textured slate surface. Around the pool, a natural, textured frame is created by scattered smaller, cut pineapple chunks and slices, delicate pink flowers, and additional scattered pink powder. All these elements surround the central pineapple. The lighting is dramatic and sidelit, precisely highlighting every single scale of the pineapple, leaf edge, water droplet, and the subtle, minimal trace of pink powder, and smoke tendril. The entire scene has a strong sense of depth and cinematic drama, tightly focused on the central pineapple.
```

[[Dramatic Lighting]] [[Cinematic Food Photography]] [[Condensation Water Drops]]

---

### 61. Nano Banana Pro 的 超写实 90 年代 运动服 肖像

**Author**: [Melis✨](https://x.com/miilesus)  **Date**: 2026-03-27  **Language**: en

> 一个高度详细、超写实的提示词，专为 Nano Banana Pro 设计，用于生成一张身着 90 年代运动装的年轻女性的电影感肖像，侧重于戏剧性光线、清晰的皮肤纹理，并捕捉饮水时的动态瞬间。

![Nano Banana Pro 的 超写实 90 年代 运动服 肖像](https://cms-assets.youmind.com/media/1774766199053_lmv26o_HEb-ufDagAA4V4n.jpg)

```
{ "image_generation_prompt": { "subject": { "description": "Young woman with a strong resemblance to {argument name="subject name" default="---------------"}.", "hair": "Voluminous blonde 1950s-style bangs and a high ponytail secured with a purple scrunchie; soft, flowing texture with slight curling at the ends.", "face": "Profile view, mouth open while drinking; dewy, perspiring skin with visible pores and subtle makeup highlighting the cheekbones.", "body": "Athletic, toned physique with visible beads of sweat on the neck and décolletage." }, "attire": { "clothing": "White athletic crop top with blue trim and a 'TuneSquad' logo; matching white high-waisted gym shorts; a thick white cotton towel draped around the neck.", "style": "Retro Sportswear / 90s Pop Culture Cosplay." }, "styling_and_accessories": { "jewelry": [ "Translucent orange plastic water bottle", "Thin white fabric gloves", "Purple textured hair scrunchie" ] }, "environment": { "setting": "Minimalist indoor gym or studio.", "background": "Muted grey concrete walls with vertical architectural recessed lighting strips providing depth.", "water": "Droplets of clear water falling from the mouth and bottle cap, captured in mid-air." }, "pose": { "posture": "Side-profile standing pose, head tilted back at a 45-degree angle to drink.", "arms": "Right arm raised holding the bottle to the lips; left hand resting against the towel on the chest.", "angle": "Medium shot, eye-level camera height positioned to the side to capture the silhouette and facial profile." }, "lighting_and_mood": { "lighting": "Dramatic studio lighting; high-contrast rim lighting to define the body's contours and emphasize skin moisture.", "mood": "Cinematic, energetic, and highly stylized.", "colors": "Neutral grey and white palette punctuated by vibrant translucent orange and soft purple." }, "camera_and_technical": { "style": "Ultra Photorealistic, RAW photo.", "lens": "50mm prime lens for natural proportions with slight depth compression.", "aperture": "f/2.8 for a sharp subject and a softly out-of-focus background.", "quality_tags": [ "8k resolution", "highly detailed", "volumetric lighting", "ray tracing reflections", "hyper-realistic texture", "Hasselblad photography" ] } } }
```

[[Dramatic Lighting]] [[Hyperrealistic Portrait]]

---

### 62. 好莱坞风格电影感时间扭曲照片

**Author**: [Nikhil](https://x.com/NikhilRajX)  **Date**: 2026-03-26  **Language**: en

> 生成一张极具电影感、好莱坞风格的照片，要求以用户上传的人脸为基础，人物平静地坐着，背景以动态模糊旋转，营造出超现实的时间扭曲效果，同时具有戏剧性的光线和高细节。

![好莱坞风格电影感时间扭曲照片](https://cms-assets.youmind.com/media/1774594316616_yjp98f_HEVtgoYasAAOvy9.jpg)

```
Create a highly cinematic, Hollywood-style photo of a person using the face from the uploaded image. The person is sitting calmly on a chair in the center of a large open space, looking relaxed and confident. The camera is focused on the person, who remains perfectly still and sharp. Around them, the entire world appears to be rotating or spinning in motion blur - buildings, lights, and surroundings bending in a circular motion, creating a surreal time-distortion effect. The camera angle is slightly low and dramatic, like a movie scene. Lighting is cinematic with strong contrast, soft highlights on the face, and dynamic shadows. The environment feels epic and intense, like time is moving fast but the person is untouched. Ultra realistic, high detail, atmospheric depth, dramatic motion blur, Hollywood movie scene composition, 8k quality
```

[[Dramatic Lighting]]

---

### 63. 明亮门洞下的电影感剪影

**Author**: [Nikhil](https://x.com/NikhilRajX)  **Date**: 2026-03-25  **Language**: en

> 一个用于生成极具电影感、好莱坞风格照片的提示词，画面中，一个人影逆光站立在一扇极其明亮的白色门框前。它强调戏剧性光线、体积光、深邃的阴影，营造出超现实且神秘的氛围，并要求提供一张面部参考图。

![明亮门洞下的电影感剪影](https://cms-assets.youmind.com/media/1774508267323_9iwmma_HERYfCZbwAAFTlo.jpg)

```
Create a highly cinematic, Hollywood-style photo of a person using the face from the uploaded image. The person is standing in a dark room, facing slightly toward the camera, while a large open doorway behind them emits an intense bright white light. The light is so strong that it creates a powerful silhouette effect around the person, with glowing edges outlining their body. Soft fog or smoke fills the air, making the light rays visible and dramatic. The contrast between the dark room and the bright doorway is strong and cinematic. The person is wearing a stylish outfit such as a long coat, fitted clothes, and boots. Their posture is calm, confident, and slightly mysterious. Ultra realistic photography, dramatic lighting, volumetric light rays, deep shadows, atmospheric depth, Hollywood movie scene composition, 8k detail.
```

[[Dramatic Lighting]] [[Volumetric Light]] [[Mysterious Mood]]

---

### 64. 超写实电影感黑白人像

**Author**: [Harboris](https://x.com/harboriis)  **Date**: 2026-03-24  **Language**: en

> 一个用于生成超写实影棚肖像的提示词，肖像中主体倚靠在椅背上，运用电影感黑白调色。该提示词强调低角度视角、面部特征锐利对焦和戏剧性光线，以达到栩栩如生的效果。

![超写实电影感黑白人像](https://cms-assets.youmind.com/media/1774421475927_oiqyge_HEJGsT6bUAACVw1.jpg)

```
Ultra-realistic studio portrait of him leaning gracefully on the backrest of a chair, dressed in a sleek dark outfit. Shot from a subtle low-angle to accentuate his facial features and confident expression. 

Cinematic black-and-white color grade with refined, natural skin AK details, highlighting textures in her clothing, tones. Solid black background with sharp .hair, and eyes for a dramatic, lifelike effect
```

[[Dramatic Lighting]] [[Low Angle Shot]] [[Film Noir Lighting]]

---

### 65. Gemini Nano Banana Pro 的电影人像提示词

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-03-19  **Language**: en

> 一个详细的提示，用于让 Gemini Nano Banana Pro 生成一张高度逼真的电影级年轻男子肖像，保留参考照片中的面部特征，背景设定在带有戏剧性彩色烟雾效果的摄影棚中。

![Gemini Nano Banana Pro 的电影人像提示词](https://cms-assets.youmind.com/media/1773988992490_ym5ep6_HDu7gUlasAAiQw_.jpg)

```
Create a highly realistic cinematic portrait of a cool young man based on the uploaded reference photo, preserving the same facial identity, facial structure, and overall look. The young man has wavy vintage style hair, neatly styled with a clean cut appearance that frames his face naturally. His expression is calm and confident as he looks slightly to the right, giving a relaxed and thoughtful vibe.

He is seated comfortably on a simple wooden crate in a studio setting. His posture is casual with one leg slightly forward and his shoulders relaxed. In one hand he loosely holds a denim jacket draped naturally over his arm as if he just took it off.

He is wearing a plain loose white t shirt with a soft cotton texture and light colored baggie jeans that fit casually. The fabric folds and natural creases add realism to the clothing while maintaining a minimal stylish look.

The background is a dramatic black studio environment with atmospheric smoke effects in {argument name="smoke color 1" default="blue"} and {argument name="smoke color 2" default="red"} tones slowly spreading behind him. The colored smoke creates a soft glowing contrast against the dark background and adds depth to the scene. Subtle studio lighting highlights the edges of his hair, shoulders, and clothing, while soft shadows fall around the wooden crate.

Professional studio portrait photography style, captured with a full frame camera using an 85mm lens. Shallow depth of field keeps the subject in sharp focus while the colored smoke softly blurs in the background. Ultra photorealistic lighting, natural skin texture, cinematic color grading, high contrast, extremely detailed, 8k resolution.
```

[[Dramatic Lighting]] [[Male Portrait]] [[Face Preservation]] [[Photorealistic Portrait]]

---

### 66. 在黑暗电影院中拍摄的优雅时尚大片

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-03-16  **Language**: en

> 这是一个详细的提示，用于使用 Nano Banana Pro 生成一张高级时装编辑照片。场景中，一位身着丝滑白色羽毛袖口服装的时尚女性，坐在一间黑暗的电影院里，电影院内有红色天鹅绒座椅，强调戏剧性的电影灯光和 35 毫米胶片美学。

![在黑暗电影院中拍摄的优雅时尚大片](https://cms-assets.youmind.com/media/1773729521353_7d2u2z_HDhVb8xakAAGlU2.jpg)

```
Elegant fashion editorial of a stylish woman sitting alone in a dark movie theater, surrounded by rows of red velvet cinema seats, wearing a silky white satin outfit with feather cuffs, legs crossed, eating popcorn from a bucket with some popcorn spilled on the floor, dramatic cinematic lighting, moody atmosphere, centered composition, high fashion photography, soft shadows, 35mm film look, ultra-detailed, realistic, depth of field.
```

[[Dramatic Lighting]] [[35mm Film Aesthetic]]

---

### 67. 英俊青年的电影肖像

**Author**: [Aijaz](https://x.com/iamsofiaijaz)  **Date**: 2026-03-16  **Language**: en

> 一个详细的提示，用于使用 Nano Banana AI 生成一个电影般的、超现实的年轻男子肖像，重点突出戏剧性光线、特定的面部特征和黑色电影氛围。

![英俊青年的电影肖像](https://cms-assets.youmind.com/media/1773729505525_mbugkw_HDfaMnPbsAE-wXF.jpg)

```
Cinematic portrait of a handsome young man with sharp blue eyes, tousled dark brown hair swept back with a loose strand falling forward, and a neatly trimmed beard. Moody low-key lighting with dramatic contrast, cool blue tones with subtle red rim light. Three-quarter profile view, intense gaze toward the camera. Wearing a dark minimalist coat or jacket. Shallow depth of field, soft background bokeh, ultra-realistic skin texture. Film noir atmosphere, modern fashion editorial style, 85mm lens,f/1.8, high detail, photorealistic, 8k quality.
```

[[Dramatic Lighting]] [[Cinematic Atmosphere]] [[Young Male Portrait]] [[Moody Aesthetic]]

---

### 68. 产品组装顺序时间表

**Author**: [Alexandra Aisling](https://x.com/AllaAisling)  **Date**: 2026-03-15  **Language**: en

> 一个复杂的多阶段提示，专为 Nano Banana 2（在 Adobe Firefly 中使用）设计，用于生成一个 5 格水平时间轴，展示产品组装顺序，重点是戏剧性照明、技术精确性和一致的摄像机角度。

![产品组装顺序时间表](https://cms-assets.youmind.com/media/1773643976636_wiorx9_HDdwJpKXoAAU_He.jpg)
![产品组装顺序时间表](https://cms-assets.youmind.com/media/1773643976742_02299d_HDdv2qpWcAAjiia.jpg)
![产品组装顺序时间表](https://cms-assets.youmind.com/media/1773643976909_okb2bb_HDdwtrdWsAEaWaC.jpg)
![产品组装顺序时间表](https://cms-assets.youmind.com/media/1773643977504_81eh7o_HDdxC-xXUAA1QLl.jpg)

```
5-stage horizontal manufacturing timeline, frozen mid-assembly. deep matte black background. dramatic industrial spotlights, deep shadow falloff.  
S1: Components scattered, floating, zero assembly. 
S2: Converging with speed lines, skeleton emerging. 
S3: Half-built, peak tension, fasteners mid-tighten. 
S4: Chassis open, full internals exposed. 
S5: Finished product + ghost wireframe overlay.  
Same 3/4 camera angle across all stages. Dotted trajectory arcs connect each component across stages. Each component color-coded consistently.  Title: "PRODUCT NAME - ASSEMBLY SEQUENCE" Footer: "N parts parts · X hrs · KEY SPEC"  Helvetica Neue Light labels. 4K, tack sharp. Dieter Rams precision.
```

[[Dramatic Lighting]] [[Technical Illustration]]

---

### 69. 电影级影棚人像，精准面部匹配

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-03-14  **Language**: en

> 一个高度详细的结构化提示，用于生成一张电影级的男士工作室肖像，强调从参考图像中精确匹配面部特征、特定的灯光、姿势和服装细节，使用 Google Nano Banana Pro 创建。

![电影级影棚人像，精准面部匹配](https://cms-assets.youmind.com/media/1773556643927_zjgcxw_HDXCapyaMAY8qMq.jpg)
![电影级影棚人像，精准面部匹配](https://cms-assets.youmind.com/media/1773556644010_ce40vx_HDXCaouaMAAtPnp.jpg)
![电影级影棚人像，精准面部匹配](https://cms-assets.youmind.com/media/1773556643956_a779mj_HDXCaqlbYAA5sJO.jpg)

```
{
  "scene": "cinematic studio portrait",
  "reference": {
    "identity_match": "match the uploaded reference face precisely",
    "facial_accuracy": [
      "bone structure",
      "eye shape",
      "nose proportions",
      "jawline",
      "facial symmetry",
      "hairline"
    ],
    "skin_texture": "natural pores and realistic skin detail"
  },
  "subject": {
    "type": "man",
    "age": "around 25–30",
    "expression": "calm, confident, relaxed",
    "gaze": "direct eye contact with camera"
  },
  "pose": {
    "style": "relaxed studio pose",
    "description": "leaning slightly forward with one elbow resting on a wooden table, one hand gently touching the side of the head"
  },
  "hair": {
    "style": "short natural hairstyle with soft volume and visible strands"
  },
  "clothing": {
    "outfit": "soft neutral button-up shirt or lightweight sweater",
    "style": "clean, modern, minimal"
  },
  "lighting": {
    "style": "soft cinematic studio lighting",
    "key_light": "above eye level from viewer's left",
    "effect": "soft highlights
```

[[Dramatic Lighting]] [[Editorial Photography]] [[Face Preservation]] [[Cinematic Studio Portrait]]

---

### 70. 女巫电影海报

**Author**: [Aijaz](https://x.com/iamsofiaijaz)  **Date**: 2026-03-15  **Language**: en

> 一个给 Nano Banana Pro 的提示，用于生成一张超现实电影海报，画面中一位强大的女巫师动态地冲破一张破裂的黑桃皇后扑克牌，强调戏剧性的光影、精致的中世纪奇幻服饰和魔法能量效果。

![女巫电影海报](https://cms-assets.youmind.com/media/1773643981276_xt5huj_HDaQx9PaMAIRCOJ.jpg)

```
Make a hyper-realistic cinematic movie poster of a powerful young female sorcerer bursting through a cracked Queen of Spades playing card. The card explodes outward with stone fragments, dust, and debris frozen mid-air. SHe wears an ornate royal maroon and gold embroidered mediaeval fantasy jacket, rich fabric textures, intricate detailing, regal and Comme mystical.The sorcerer extends one hand forward toward the viewer, fingers glowing with intense magical energy, subtle golden sparks and dark arcane aura surrounding the hand. Intense piercing gaze, confident and dominant expression, cinematic hero framing. Dramatic chiaroscuro lighting, dark moody background, volumetric light rays, ultra-detailed textures, shallow cinematic depth of field. Photorealistic face, epic fantasy realism, movie poster composition, high contrast, dynamic motion, . dust particles, masterpiece quality, ultra-sharp focus, 8K resolution, cinematic color grading.
```

[[Dramatic Lighting]]

---

### 71. 商业产品摄影：Soda Splash 系列

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-03-13  **Language**: en

> 以下是三组提示，用于生成高能量的汽水罐（芬达葡萄味、可口可乐桃子味、雪碧柠檬味）商业产品摄影，画面中汽水罐爆裂，果实和液体飞溅，强调戏剧性光线、冷凝水和超精细纹理。

![商业产品摄影：Soda Splash 系列](https://cms-assets.youmind.com/media/1773469789706_s5m9kj_HDS7Cb9aUAAgCwW.jpg)
![商业产品摄影：Soda Splash 系列](https://cms-assets.youmind.com/media/1773469789736_ycepdv_HDS7CZvbYAAJ_NP.jpg)
![商业产品摄影：Soda Splash 系列](https://cms-assets.youmind.com/media/1773469789821_sdrzu3_HDS7CZobYAAgX99.jpg)

```
1️⃣ Fanta Grape Splash
Prompt:
High-energy commercial product photography of a purple soda can bursting open with fresh grapes exploding out, juicy grape splash and droplets frozen in motion, vibrant purple liquid splashing around the can, glossy grape textures, green grape leaf attached to the bunch, dramatic glowing purple background with sparkling particles, cinematic lighting, condensation on the can, ultra-detailed fruit textures, dynamic beverage advertisement style, 8K.
2️⃣ Coca-Cola Peach Explosion
Prompt:
Cinematic beverage advertisement showing a red soda can torn open with fresh peaches and peach slices bursting out, bright juicy splash of peach soda, floating fruit pieces and droplets, glossy peach skin texture, green leaves around the fruit, glowing orange-red background with dramatic lighting, condensation on the can, high-energy splash effect, ultra-detailed commercial product photography, 8K.
3️⃣ Sprite Lemon Splash
Prompt:
Refreshing soda advertisement featuring a green soda can ripped open with fresh lemons and lemon slices bursting out, fizzy lemon soda splashing dynamically around the can, bright yellow citrus juice droplets, mint leaves floating around, vibrant yellow-green gradient background, dramatic lighting and sparkling bubbles, condensation on the can, ultra-realistic beverage photography, high-energy splash effect, 8K.
```

[[Dramatic Lighting]] [[Commercial Product Photography]] [[Condensation Texture]]

---

### 72. Nano Banana Pro 的单色宣传风格肖像提示

**Author**: [Duet | AI](https://x.com/Sheldon056)  **Date**: 2026-03-10  **Language**: en

> 一个给 Nano Banana Pro 的提示，用于创作一幅高对比度的数字肖像画：一个年轻男子，采用超现实主义的单色风格，灵感来自复古宣传海报，但带有现代电影般的润饰。它详细说明了纹理（皮肤毛孔、画笔笔触、做旧纸张）、戏剧性的灯光以及强大而坚定的情绪。

![Nano Banana Pro 的单色宣传风格肖像提示](https://cms-assets.youmind.com/media/1773210649874_r3zxwg_HDAnwpVbYAAEiqA.jpg)

```
High-contrast digital portrait of a young man looking upward with determination and confidence. Hyper-realistic monochrome face with strong cheekbones and detailed skin pores. Background divided into bold textured blocks of red and black with rough paint strokes and distressed paper textures. Dramatic lighting highlighting facial contours and expression. Inspired by vintage propaganda poster aesthetics with modern cinematic polish. Sharp focus, powerful mood, editorial artwork, 4K.
```

[[Dramatic Lighting]] [[Male Portrait]]

---

### 73. 超精细足球运动员肖像速写提示词

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-03-02  **Language**: en

> 一个用于生成自信男足球运动员超详细肖像的提示，采用手绘插画风格，绘制在纹理纸上。它详细说明了人物特征、服装（红色球衣）、戏剧性光线，以及实现超逼真素描效果的技术细节。

![超精细足球运动员肖像速写提示词](https://cms-assets.youmind.com/media/1772519708720_5192hq_HCYGzFEaMAAi--4.jpg)

```
Hyper-detailed  portrait of a confident male footballer, looking slightly upward, strong jawline, short textured hair, wearing a red jersey with subtle crest detail, realistic skin texture with fine cross-hatching strokes, hand-drawn illustration style on textured paper, soft neutral background, dramatic lighting with gentle shadows, ultra-realistic sketch effect, high detail, 8K, editorial sports portrait
```

[[Dramatic Lighting]]

---

### 74. 沉船暮光场景

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2026-03-01  **Language**: en

> 生成一张照片的提示词：一张电影级的写实照片，一名男子（身份锁定为参考照片）站在黄昏时分的岩石海滩上，抬头凝视着搁浅在悬崖边上那艘巨大、锈迹斑斑的沉船残骸。该提示词强调了戏剧性的视角、凉爽的暮光和神秘的氛围。

![沉船暮光场景](https://cms-assets.youmind.com/media/1772433511634_0qgsek_HCVMqWWbcAAMfes.jpg)

```
Masterpiece, best quality, ultra detailed, photorealistic photograph. Shot from a dynamic low-angle perspective, the scene is dominated by a man from photo in close-up. He stands in three quarter profile on a rocky beach at twilight, his face clearly visible as he gazes upward at the wreck of a massive, rusted ship beached against a cliffside.

The immense shipwreck, with its battered hull and twisted metal, looms in the background against a dramatic teal and blue sky with a crescent moon and stars. The man, wearing a simple dark t-shirt and shorts, is the central focus of the frame, his contemplative expression highlighted by the cool dusk light. The overall mood is cinematic, mysterious, and powerful. Shot on a full-frame camera with a wide-angle lens to enhance the dynamic perspectiv 8K resolution.
```

[[Dramatic Lighting]] [[Cinematic Photography]]

---

### 75. 超逼真产品广告提示

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-03-01  **Language**: en

> 以下是为 Nano Banana 2 提供的详细提示，用于生成一款超逼真、高端的卡布奇诺咖啡瓶产品广告。该提示着重强调动态液体物理效果、戏剧性光照，以及融合了火焰、冰块和大理石纹理等奢华、高对比度的奇幻元素。

![超逼真产品广告提示](https://cms-assets.youmind.com/media/1772433501608_6a5qiu_HCSW8ybbYAAd-bX.jpg)
![超逼真产品广告提示](https://cms-assets.youmind.com/media/1772433501612_5yiq3g_HCSW8yebkAALM0s.jpg)
![超逼真产品广告提示](https://cms-assets.youmind.com/media/1772433501652_ch9611_HCSW8ydbIAAeRFg.jpg)
![超逼真产品广告提示](https://cms-assets.youmind.com/media/1772433502419_pakbqy_HCSW866agAAAOj0.jpg)

```
Ultra-realistic premium product advertisement of a cappuccino coffee bottle, centered composition, surrounded by dynamic liquid splashes of coffee and milk forming elegant swirling shapes in mid-air. Dramatic environments blending elements of fire, lava, ice shards, marble textures, and dark studio backgrounds.
Hyper-detailed liquid physics, droplets frozen in motion, cinematic lighting with high contrast, glowing highlights, and volumetric light. Coffee splashes mixed with creamy textures, energetic explosion effects, sparks, smoke, and mist.
Luxury branding style, glossy reflections on bottle, sharp label details, rich brown and gold color palette, macro photography, shallow depth of field, 85mm lens, commercial advertising style, studio + fantasy hybrid scene, ultra-detailed, 8K resolution.
```

[[Dramatic Lighting]]

---

### 76. 电影时尚肖像提示

**Author**: [Shore Lyn](https://x.com/Shorelyn_)  **Date**: 2026-02-27  **Language**: en

> 一个用于 Nano Banana Pro 的提示，生成一张超现实、电影感的时尚肖像，描绘了一位戴眼镜的年轻男士在城市隧道中的场景，强调戏剧性灯光和青色/橙色调色。

![电影时尚肖像提示](https://cms-assets.youmind.com/media/1772259919732_0vwbpc_HCJzuVLaUAICNhL.jpg)

```
Ultra realistic cinematic fashion portrait of a young man round glasses, looking down at the camera, low angle shot, wearing oversized light puffer jacket and warm orange sweater, standing under bright orange and yellow neon lights in an urban tunnel, strong teal and orange color grading, intense contrast, vibrant glowing background, dramatic lighting on face and jacket, shallow depth of field, soft bokeh, 35mm lens, night city atmosphere.
```

[[Dramatic Lighting]] [[Male Fashion Portrait]]

---

### 77. 电影级美食广告镜头：解构的火鸡面

**Author**: [Meem](https://x.com/mehvishs25)  **Date**: 2026-02-27  **Language**: en

> 一个结构化的 JSON 提示词，用于生成一个超现实、高角度的电影级美食广告镜头。场景捕捉了辣味火鸡面（面条、鸡肉、鸡蛋）的解构元素悬浮在半空中，强调了戏剧性的灯光、质感和地道的韩国拉面店氛围。

![电影级美食广告镜头：解构的火鸡面](https://cms-assets.youmind.com/media/1772259909667_fpfguy_HCISSFlakAAorfo.jpg)
![电影级美食广告镜头：解构的火鸡面](https://cms-assets.youmind.com/media/1772259909765_k0wa0i_HCISSF1aEAAvdFE.jpg)

```
{
  "scene": {
    "subject": "Deconstructed Spicy Buldak Ramen",
    "composition": "High-angle cinematic food commercial shot",
    "physics": "Mid-air suspension / Slow-motion fall",
    "elements": [
      "Vibrant orange-red fire noodles",
      "Grilled chicken slices (charred edges)",
      "Soft-boiled eggs (jammy yolks)",
      "Scallions and red chili flakes",
      "Steaming ceramic bowl of dark spicy broth"
    ],
    "interaction": "Wooden chopsticks lifting a bundle of noodles at peak height"
  },
  "environment": {
    "background": "Authentic Korean ramen shop",
    "depth_of_field": "Softly blurred (bokeh)",
    "atmosphere": "Warm, inviting, aromatic"
  },
  "technical_specs": {
    "lighting": "Dramatic, directional, highlighting steam and texture",
    "resolution": "8K UHD",
    "rendering": "Hyper-realistic",
    "style": "Professional food photography",
    
  }
}
```

[[Dramatic Lighting]] [[High Angle Shot]]

---

### 78. 霓虹灯下的电影感时尚肖像

**Author**: [Duet | AI](https://x.com/Sheldon056)  **Date**: 2026-02-26  **Language**: en

> 一个关于在城市隧道中拍摄年轻男子的超现实、电影感时尚肖像的提示。关键元素包括圆形眼镜、超大夹克、暖橙色毛衣、强烈的青色和橙色调色、戏剧性灯光和浅景深。

![霓虹灯下的电影感时尚肖像](https://cms-assets.youmind.com/media/1772174134656_67n4bu_HCEUsSVaMAEPafo.jpg)

```
Ultra realistic cinematic fashion portrait of a young man round glasses, looking down at the camera, low angle shot, wearing oversized light puffer jacket and warm orange sweater, standing under bright orange and yellow neon lights in an urban tunnel, strong teal and orange color grading, intense contrast, vibrant glowing background, dramatic lighting on face and jacket, shallow depth of field, soft bokeh, 35mm lens, night city atmosphere.
```

[[Dramatic Lighting]] [[Round Glasses]]

---

### 79. 赛博朋克机械师与巨型外骨骼背包

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-02-26  **Language**: en

> 一个高度结构化的提示，用于生成一张超现实、电影感、赛博朋克风格的女性机械师肖像，她身穿一个巨大、细节丰富的机械外骨骼背包，置身于极简的工业车间环境中，强调超高细节的纹理和戏剧性的灯光。

![赛博朋克机械师与巨型外骨骼背包](https://cms-assets.youmind.com/media/1772174152530_hugfvc_HCCvDlhWgAAGfBa.jpg)
![赛博朋克机械师与巨型外骨骼背包](https://cms-assets.youmind.com/media/1772174152444_8qmsaw_HCCvDj4XoAER2Be.jpg)

```
{
  "type": "image_generation_prompt",
  "style": "ultra-realistic, cinematic, sci-fi mech aesthetic, cyberpunk",
  "resolution": "8K",
  "aspect_ratio": "2:3",
  "scene": {
    "location": "industrial workshop",
    "background": "clean minimal workshop environment with subtle machinery elements and soft atmospheric haze"
  },
  "subject": {
    "gender": "female",
    "role": "cyberpunk mechanic",
    "identity": {
      "same_face": true,
      "same_character": true,
      "preserve_facial_features": true,
      "realism": "exact facial structure, skin texture, and expression retained"
    },
    "pose": {
      "stance": "standing strong and confident",
      "body_language": "powerful, grounded posture"
    },
    "appearance": {
      "outfit": {
        "jacket": "purple futuristic techwear jacket",
        "details": [
          "tactical straps",
          "utility pouches",
          "reinforced armored panels",
          "futuristic cyberpunk textures"
        ]
      }
    },
    "equipment": {
      "exosuit_backpack": {
        "type": "massive mechanical industrial exosuit",
        "components": [
          "large industrial engine core",
          "exposed wires and cables",
          "metal pipes and hydraulic tubes",
          "heavy mechanical armor plates",
          "mechanical joints and connectors"
        ],
        "style": "futuristic sci-fi mech design, functional and industrial"
      }
    }
  },
  "lighting": {
    "type": "cinematic industrial lighting",
    "details": [
      "soft dramatic shadows",
      "cool and warm mixed highlights",
      "subtle volumetric light",
      "metal reflections and glow accents"
    ]
  },
  "camera": {
    "focus": "sharp focus on subject and exosuit",
    "depth_of_field": "shallow with soft background separation",
    "composition": "centered, full-body or mid-body portrait"
  },
  "quality": {
    "detail_level": "hyper detailed",
    "textures": "ultra realistic skin, fabric, and metal textures",
    "sharpness": "extremely sharp",
    "noise": "clean high-resolution render"
  },
  "mood": "powerful, futuristic, cinematic, sci-fi industrial",
  "constraints": [
    "no cartoon style",
    "no low detail",
    "no distortion",
    "no watermark",
    "no text overlay",
    "no unrealistic anatomy"
  ],
  "output_goal": "Create a hyper-realistic cinematic portrait of a cyberpunk mechanic girl wearing a massive mechanical exosuit backpack with industrial engine components, wires, pipes, and metal armor, standing strong in a minimal workshop environment with dramatic lighting and ultra-detailed sci-fi mech aesthetics."
}
```

[[Dramatic Lighting]]

---

### 80. 超逼真赛博朋克工作室肖像

**Author**: [simeon-sanai](https://x.com/Naiknelofar788)  **Date**: 2026-02-25  **Language**: en

> 生成一张超现实电影级工作室肖像的提示，描绘一个穿着黑色赛博朋克连帽衫的人，连帽衫上布满发光的霓虹橙色电路线条，强调戏剧性灯光和特定姿势。

![超逼真赛博朋克工作室肖像](https://cms-assets.youmind.com/media/1772087648655_9ib3at_HB_ww7jaoAAVPGt.jpg)
![超逼真赛博朋克工作室肖像](https://cms-assets.youmind.com/media/1772087648663_06cftj_HB_ww7fbcAACHHL.jpg)

```
Ultra-realistic cinematic studio portrait using provided person only. Subject wears black cyberpunk hoodie fully covered in bright glowing neon-orange circuit lines and illuminated zipper, hood up, hands in pockets, three-quarter pose facing right, head slightly down. Round shutter glasses with glowing orange bars. Dramatic studio lighting, glow casting light spill. Smooth dark-to-burnt orange gradient background. Style locked.
```

[[Dramatic Lighting]]

---

### 81. 霓虹夜市美食摄影

**Author**: [Alexandra Aisling](https://x.com/AllaAisling)  **Date**: 2026-02-24  **Language**: en

> 一个详细的、超现实的提示，用于生成具有霓虹夜市美学的电影级美食摄影，灵感来自《银翼杀手 2049》和东京街头小吃。它侧重于动态散落的食材、戏剧性的灯光和高分辨率的细节。

![霓虹夜市美食摄影](https://cms-assets.youmind.com/media/1772001495648_2893fy_HB8JgLHWkAALQhx.jpg)
![霓虹夜市美食摄影](https://cms-assets.youmind.com/media/1772001495767_gkcd68_HB8JyjzXUAAg2Pv.jpg)
![霓虹夜市美食摄影](https://cms-assets.youmind.com/media/1772001495707_v6nt8z_HB8JQPqXMAA6fyQ.jpg)
![霓虹夜市美食摄影](https://cms-assets.youmind.com/media/1772001497720_rqbhv4_HB8KCa4WEAAo2Qk.jpg)

```
Prompt Studio: Neon Night Market, Food, with Nano Banana Pro, in Firefly  

Hyperreal {argument name="dish" default="[DISH]"} floating against a pitch black background, dramatically lit by neon {argument name="color" default="[COLOR]"} underlighting and rim lighting. Ingredients separated and suspended in mid-air in a loose diagonal cascade,  not perfectly stacked, but dynamically scattered as if caught mid-explosion. Steam and sauce splatter glow in the neon light. Sauce drips catch the light like liquid glass. Each floating ingredient has a glowing neon label tag, like a price tag on a wire, in uppercase bold font, backlit. Dish name "{argument name="dish name" default="[DISH NAME]"}" in large neon sign typography at top, flickering glow effect. Subtitle: "[TAGLINE]". Mood: 3am street food energy, cinematic, electric, craveable. Style ref: Blade Runner 2049 meets Tokyo night market meets hyperreal CGI food ad. 4K, ultra sharp, chromatic aberration on edges.
```

[[Dramatic Lighting]]

---

### 82. 电影横截面美食摄影提示

**Author**: [Melis✨](https://x.com/miilesus)  **Date**: 2026-02-23  **Language**: en

> 一个详细的图像生成提示，用于创建一道菜肴的完美电影级横截面切片，以科学插画风格展示内部层次，具有戏剧性照明和特定食材标签，灵感来自韦斯·安德森 (Wes Anderson) 的对称美学。

![电影横截面美食摄影提示](https://cms-assets.youmind.com/media/1771915006301_aonsth_HB3TlotXwAAsLBM.jpg)
![电影横截面美食摄影提示](https://cms-assets.youmind.com/media/1771915006281_0s030u_HB3TlOdW8AAR-hR.jpg)
![电影横截面美食摄影提示](https://cms-assets.youmind.com/media/1771915006304_5ahdgy_HB3TmLUWAAAQQSE.jpg)
![电影横截面美食摄影提示](https://cms-assets.youmind.com/media/1771915006739_yxk0ko_HB3TmeHW8AEDBD-.jpg)

```
Perfect cinematic cross-section cut through {argument name="dish name" default="[DISH]"}, sliced cleanly down the center revealing every internal layer in full detail. The cut face is facing the camera straight-on, like a geological diagram of flavor. Each visible layer is labeled with a thin horizontal line extending to the right — uppercase sans-serif "{argument name="ingredient name" default="[INGREDIENT NAME]"}" with italic descriptor below. Background: flat matte {argument name="background color" default="[COLOR]"}. Lighting: dramatic side light from left casting long shadows, single warm spotlight on the cut face. Every texture hyperreal — visible moisture, air pockets, char, glaze, and steam. Mood: architectural food photography meets scientific illustration. Dish name "[DISH NAME]" in large elegant type at top. Subtitle: "[TAGLINE]". 4K, tack sharp, Style ref: Wes Anderson symmetry meets Michelin-star kitchen.
```

[[Dramatic Lighting]]

---

### 83. 史诗奇幻战士：冰与火电影海报

**Author**: [auqib](https://x.com/auqibhabib)  **Date**: 2026-02-23  **Language**: en

> 一个提示，用于生成一张戏剧性、电影海报风格的肖像，描绘两位史诗般的奇幻战士在冰冻风暴中背靠背站立，象征着冰与火的冲突，并详细说明他们的外貌、服饰以及对比鲜明的灯光和氛围。

![史诗奇幻战士：冰与火电影海报](https://cms-assets.youmind.com/media/1771914992708_puz3gf_HB239A8aYAAPqBf.jpg)

```
A dramatic cinematic poster-style portrait of two epic fantasy warriors standing back-to-back in a frozen storm. On the left, a battle-worn male warrior with wet, curly dark hair, head bowed in quiet resolve, gripping a medieval sword planted into the ice. Frost and snow cling to his fur-lined cloak and shoulders. On the right, a powerful female warrior in profile, pale skin glowing with fiery orange light, her body partially engulfed in flames thatcontrast against the icy blue atmosphere. Snow particles swirl through the air, blending fire and ice in a symbolic clash. Ultra-detailed faces, emotional intensity, volumetric fog, cinematic lighting, cold blue tones mixed with warm fire highlights, shallow depth of field, epic fantasy movie poster, hyper-realistic, 8K resolution, dramatic composition, sharp focus, high contrast, photorealistic textures.
```

[[Dramatic Lighting]]

---

### 84. 建筑美食摄影横截面提示

**Author**: [Alexandra Aisling](https://x.com/AllaAisling)  **Date**: 2026-02-22  **Language**: en

> 一个为 Adobe Firefly 设计的结构化提示，使用 Nano Banana Pro 创作一道菜肴的超现实电影感横截面。它采用科学插画风格，带有标注层、戏剧性灯光和韦斯·安德森（Wes Anderson）美学。

![建筑美食摄影横截面提示](https://cms-assets.youmind.com/media/1771828714501_44tv3i_HByAZOpWMAA6EKv.jpg)
![建筑美食摄影横截面提示](https://cms-assets.youmind.com/media/1771828714581_ln3uws_HBx__gRWgAAGZxt.jpg)
![建筑美食摄影横截面提示](https://cms-assets.youmind.com/media/1771828714446_pqr3od_HByAPUcXkAAvasx.jpg)
![建筑美食摄影横截面提示](https://cms-assets.youmind.com/media/1771828715536_a27cqw_HByAmZMWwAAE3LK.jpg)

```
Perfect cinematic cross-section cut through {argument name="dish" default="[DISH]"}, sliced cleanly down the center revealing every internal layer in full detail. The cut face is facing the camera straight-on, like a geological diagram of flavor. Each visible layer is labeled with a thin horizontal line extending to the right — uppercase sans-serif "{argument name="ingredient name" default="[INGREDIENT NAME]"}" with italic descriptor below. Background: flat matte {argument name="color" default="[COLOR]"}. Lighting: dramatic side light from left casting long shadows, single warm spotlight on the cut face. Every texture hyperreal — visible moisture, air pockets, char, glaze, and steam. Mood: architectural food photography meets scientific illustration. Dish name "[DISH NAME]" in large elegant type at top. Subtitle: "[TAGLINE]". 4K, tack sharp, Style ref: Wes Anderson symmetry meets Michelin-star kitchen.
```

[[Dramatic Lighting]]

---

### 85. Sydney Sweeney 的超逼真电影肖像

**Author**: [Selena 🔥](https://x.com/Queen_khan143)  **Date**: 2026-02-12  **Language**: en

> 一个高度详细、结构化的提示，用于生成一张超现实、电影级的西德尼·斯威尼 (Sydney Sweeney) 特写肖像，重点突出湿发、水润肌肤、戏剧性光线，以及 105mm 微距镜头和 f/1.4 光圈等特定相机设置。

![Sydney Sweeney 的超逼真电影肖像](https://cms-assets.youmind.com/media/1770964573164_973afu_HA785hLbcAAqq8m.jpg)

```
{
  "prompt_configuration": {
    "version": "v4.0",
    "target_aspect_ratio": "3:4",
    "mode": "Photorealistic_Cinematic"
  },
  "scene_graph": {
    "main_subject": {
      "identity": {
        "name": "{argument name="subject name" default="Sydney Sweeney"}",
        "archetype": "Celebrity Portrait",
        "age_appearance": "20s"
      },
      "hair_simulation": {
        "color": "Light Brown",
        "texture": "Wet, high-gloss",
        "style": "Loose wavy strands",
        "framing": "Face-framing locks",
        "physics": "Damp, heavy drape"
      },
      "facial_details": {
        "eyes": {
          "color": "Blue",
          "gaze": "Direct, striking, expressive",
          "makeup": "Natural, clear, no dark eyeliner, clean look",
          "eyebrows": "Well-defined, brushed up"
        },
        "skin": {
          "texture_map": "Hyper-realistic, pore-level detail",
          "finish": "Dewy, luminous, wet sheen",
          "complexion": "Fair, natural redness"
        },
        "mouth": {
          "texture": "Glossy",
          "finish": "High-shine lip gloss",
          "expression": "Neutral, slightly parted"
        }
      },
      "clothing_and_accessories": {
        "visible_apparel": "Minimalist/None visible in close-up",
        "jewelry": "None"
      }
    },
    "environment_lighting": {
      "global_illumination": "Cool ambient",
      "key_light": {
        "type": "Softbox",
        "position": "Front-left",
        "gel": "Cyan/Blue tint",
        "intensity": "Medium-High"
      },
      "mood": {
        "atmosphere": "Dramatic, moody, melancholic",
        "color_grading": "Teal and Orange (muted), cool bluish cast"
      }
    },
    "virtual_camera": {
      "lens_focal_length": "105mm (Macro Portrait)",
      "aperture": "f/1.4",
      "shutter_speed": "1/125",
      "iso": "100",
      "focus_point": "Eyes",
      "depth_of_field": "Shallow, bokeh background"
    },
    "render_engine_keywords": [
      "Octane Render",
      "Unreal Engine 5",
      "Ray Tracing",
      "Subsurface Scattering (SSS)",
      "Global Illumination",
      "8k Resolution"
    ]
  },
  "final_compiled_prompt": "Hyper-realistic close-up portrait of {argument name="subject name" default="Sydney Sweeney"}, wet light brown hair styled in loose wavy strands framing face. Striking expressive eyes, natural look without dark eyeliner, well-defined eyebrows. Skin texture is smooth with a dewy luminous finish, glossy lips. Lighting is dramatic and moody with a cool bluish tint. Shot on 105mm macro lens, f/1.4, shallow depth of field, 8k resolution, cinematic lighting, raw photograph."
}
```

[[Dramatic Lighting]] [[Sydney Sweeney]] [[Wet Hair]] [[Ultra Realistic Portrait]]

---

### 86. 电影级复古魅力肖像提示词

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-11  **Language**: en

> 一个高度详细、结构化的 JSON 提示，用于生成一张电影般的复古好莱坞魅力肖像，描绘一位身着深红色缎面礼服和白色皮草披肩的女性，强调柔焦光晕、戏剧性灯光和模拟胶片美学。

![电影级复古魅力肖像提示词](https://cms-assets.youmind.com/media/1770878334751_hfs1xg_HA5Y5dkW8AA2mfT.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "cinematic_vintage_glam_red_gown_white_fur_halo",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_RED_GOWN_WHITE_FUR_SOFT_HALO_FILM"
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 4,
      "sharpness": "soft_film_crisp_faces",
      "grain": "fine_film_grain"
    },
    "scene": {
      "concept": "vintage Hollywood glamour portrait with dreamy soft-focus halation",
      "environment": "dark studio with a deep red backdrop gradient, subtle light streaks/lens flares, minimal set, cinematic negative space",
      "composition": "3/4 body fashion portrait, subject slightly off-center, strong S-curve pose, generous negative space to the right",
      "mood": "sensual, luxurious, old-Hollywood, dreamy"
    },
    "subject": {
      "person": "adult woman",
      "pose": "standing with shoulders angled, head tilted slightly back, chin lifted, hands gently resting near waist holding a small clutch",
      "expression": "sultry soft gaze, glossy lips, relaxed eyelids",
      "hair": "short to medium wavy bob, vintage-inspired waves, soft volume",
      "makeup": "classic glam: glossy deep red lips, softly smoked eyeliner, luminous skin with highlight",
      "wardrobe": {
        "dress": "deep red satin or velvet slip gown, thin straps, fitted bodice, smooth drape, rich red texture",
        "stole": "white faux-fur stole/shrug with long fluffy fibers, oversized sleeves draping from shoulders"
      },
      "accessories": "delicate necklace with small pendant, subtle earrings",
      "props": "small dark clutch bag held low"
    },
    "camera": {
      "shot_type": "glamour portrait",
      "lens": "85mm",
      "aperture": "f/1.6",
      "focus": "eyes and lips sharp; fur texture detailed; edges softly bloom with halation",
      "framing": "4:5 vertical"
    },
    "lighting": {
      "setup": "soft key light from upper left with diffusion, subtle rim light to separate fur from background, practical light streaks",
      "look": "dreamy bloom/halation, gentle specular highlights on satin, controlled shadows",
      "skin_tone": "warm, cinematic, natural texture preserved (no plastic smoothing)"
    },
    "color_grading": {
      "palette": "deep reds + creamy whites + warm skin tones",
      "look": "analog film, soft glow, slight chromatic aberration, gentle vignette",
      "contrast": "medium",
      "saturation": "rich but controlled"
    },
    "effects": {
      "halation": "strong but tasteful, especially around highlights and fur",
      "lens_flare": "subtle streaks and bloom in upper left, not covering face",
      "vignette": "soft dark vignette around edges"
    },
    "quality_rules": {
      "anatomy_accuracy": "strict",
      "hands": "correct fingers, natural joints, no extra digits",
      "face_integrity": "no warping, no asymmetry ar"
    }
  }
}
```

[[Dramatic Lighting]]

---

### 87. 低调侧面肖像，带单边缘光

**Author**: [Snow](https://x.com/iamrealsnow)  **Date**: 2026-02-10  **Language**: en

> 一个简单、富有氛围感的提示词，用于生成一张以戏剧性光线为焦点的低调肖像。图像应呈现一个侧面男性，仅由一束轮廓光照亮，这束光线将他的面部特征在漆黑的背景下清晰勾勒出来，营造出一种神秘而强烈的氛围。

![低调侧面肖像，带单边缘光](https://cms-assets.youmind.com/media/1770792215213_9u7fm2_HAxJA3WaAAACiMS.jpg)

```
Generate a low-key portrait of a man in profile, illuminated only by a single rim light that outlines his facial features against a pitch-black background. The mood should be mysterious and intense.
```

[[Dramatic Lighting]] [[Male Portrait]] [[Dark Background]] [[Moody Portrait]]

---

### 88. 战术女性角色的电影感照片

**Author**: [FL⭕RA](https://x.com/Flora_Janer8)  **Date**: 2026-02-09  **Language**: en

> 生成一张超逼真的电影级照片的提示词，照片中是两位年轻的女性动作电影角色（灵感来自萨迪·辛克和米莉·鲍比·布朗），她们在一个粗犷的工业电影布景上摆姿势，提示词中需详细说明她们的战术装备、发色以及尘土飞扬的仓库环境中的戏剧性灯光。

![战术女性角色的电影感照片](https://cms-assets.youmind.com/media/1770706170005_wqmmyn_HAuJDVpawAA9dWp.jpg)
![战术女性角色的电影感照片](https://cms-assets.youmind.com/media/1770706170859_dazfsl_HAuJDXgacAA4-Sm.jpg)

```
“A hyper-realistic cinematic photo of two young female action-movie characters posing on a gritty industrial film set. The woman on the left has long {argument name="first woman hair color" default="red"} hair and wears a white tactical plate-carrier vest over fitted white athletic shorts with black elbow pads. The woman on the right has short {argument name="second woman hair color" default="brown"} hair and wears a black tactical vest with black utility shorts. Both wear black fingerless gloves. The background is a dusty warehouse with visible film crew, studio lights, and cameras. High detail, ultra-high resolution, dramatic lighting, professional cinematic photography.”
```

[[Dramatic Lighting]] [[Cinematic Photography]]

---

### 89. 电影巨猫追逐小女人

**Author**: [Ana | The AI Girl](https://x.com/WealthEmpireHQ)  **Date**: 2026-02-09  **Language**: en

> 一个结构化的 JSON 提示词，用于描述一个电影级的 3D 超逼真厨房场景，其中包含大小差异。一个娇小的女人（带面部参考）抱着一只受惊的德国牧羊犬跑过地板，同时被一只巨大的毛茸茸的灰猫追赶。提示词指定了温暖而富有戏剧性的灯光、浅景深和皮克斯级别的真实感。

![电影巨猫追逐小女人](https://cms-assets.youmind.com/media/1770706157565_gdcs4d_HAt7RPwb0AAeYc2.png)

```
{
  "scene": {
    "type": "cinematic 3D photorealistic",
    "setting": "kitchen",
    "lighting": "warm dramatic",
    "camera": {
      "depth_of_field": "shallow",
      "motion_blur": true,
      "focus": "sharp"
    },
    "props": "scattered"
  },
  "subjects": [
    {
      "identity": "woman",
      "size": "tiny",
      "action": "running across wooden floor",
      "holding": "scared German shepherd",
      "face_reference": "use same face as reference image without changes"
    },
    {
      "identity": "cat",
      "size": "giant",
      "appearance": {
        "fur": "fluffy gray",
        "eyes": "yellow"
      },
      "action": "chasing the woman and dog"
    }
  ],
  "style": {
    "realism": "Pixar-level",
    "detail": "ultra-detailed",
    "resolution": "8K"
  }
}
```

[[Dramatic Lighting]] [[Pixar Style]] [[Kitchen Setting]] [[Fantasy Scene]]

---

### 90. 超逼真赛博朋克时尚肖像

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-02-07  **Language**: en

> 一个详细的提示，用于生成一张超现实的电影级肖像，描绘一位时尚年轻女性身处拥挤、霓虹闪烁的赛博朋克城市中。重点强调戏剧性光线、强烈的焦外虚化（bokeh）以及对主体清晰的聚焦。此提示专为 Nano Banana Pro 模型上的高质量图像生成而设计。

![超逼真赛博朋克时尚肖像](https://cms-assets.youmind.com/media/1770532748921_ugqq00_HAhpQfpbIAA8z9x.jpg)

```
Ultra-realistic cinematic portrait of a stylish young woman standing in a crowded street, surrounded by soft motion-blurred people. Neon city lights in {argument name="neon colors" default="teal, cyan, magenta, and warm orange"} glowing in the background, heavy bokeh, shallow depth of field. Subject sharply in focus, confident intense gaze toward camera, sleek short bob haircut, wearing a glossy black high-fashion outfit with a modern futuristic edge. Dramatic cinematic lighting with teal-and-orange color grading, rim light outlining the face, realistic skin texture, natural makeup, moody atmosphere. Shot on a full-frame camera, 85mm lens, f/1.4, street photography meets fashion editorial style, cyberpunk mood, ultra-detailed, photorealistic, 8K quality.
```

[[Dramatic Lighting]] [[Hyperrealistic Photography]] [[Bokeh Effect]] [[Neon City Street]]

---

### 91. 变革性的照片增强提示

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2026-02-06  **Language**: en

> 一个提示，指示 AI 将一张原始照片转换为四种截然不同、富有戏剧性、逼真的风格，每种风格都采用中近景、广角镜头拍摄，具有极端的拍摄角度、复杂的姿势、电影级布光和高对比度，同时保留原始环境。

![变革性的照片增强提示](https://cms-assets.youmind.com/media/1770446079207_z8a2k8_HAfkSzgaEAAdgXI.jpg)

```
Transform the original photo into a dramatic, photorealistic, ultra-detailed set of 4 styles characters are included , each a mid close up wide-angle shot with an extreme, dynamic camera angle complex, powerful pose in a consistent, expanded version of the original environment, with cinematic lighting, high contrast, crisp textures, and precise color grading.
```

[[Dramatic Lighting]] [[High Contrast Photography]] [[Wide Angle Lens]]

---

### 92. 超现实主义碎片化人脸雕塑拼贴画

**Author**: [Heather Green](https://x.com/heathergreen)  **Date**: 2026-02-05  **Language**: en

> 一个用于生成超现实、特写、高角度的碎片化人脸拼贴画的提示。风格是超写实和雕塑感的，人脸像马赛克一样用不同的纹理（光滑、抛光、老化的石头）拼凑而成。它要求戏剧性的灯光、深邃的阴影和泥土色调的配色方案，以唤起一种身份碎片化的感觉。

![超现实主义碎片化人脸雕塑拼贴画](https://cms-assets.youmind.com/media/1770359923336_pqhfi4_HAaFUGpXIAUDdth.jpg)

```
A close-up, high-angle shot showcases a collage of fragmented human faces, rendered in a hyperrealistic, sculptural style. The faces are pieced together like a mosaic, with some appearing smooth and polished, while others are rough and textured, resembling aged stone or clay. The composition is dense, with eyes, noses, and mouths overlapping and interlocking, creating a sense of disarray and intensity. The lighting is dramatic, casting deep shadows and highlighting the intricate details of each facial feature. The color palette is earthy, dominated by browns, grays, and muted skin tones, with occasional pops of color from {argument name="accent color" default="blue eyes"} or a hint of yellow in some skin. The overall effect is surreal and slightly unsettling, evoking a feeling of fragmented identity or a collective consciousness.
```

[[Dramatic Lighting]] [[Deep Shadow]]

---

### 93. JSON 提示词：身着深红色西装的高级时装社论肖像

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-02-05  **Language**: en

> 一个高度详细的 JSON 提示，用于 Gemini Nano Banana Pro，请求拍摄一张超现实的高级时装编辑照片：一位女性（身份与参考图匹配），身穿深红色/酒红色超大羊毛西装，眼神犀利，充满掠夺性，在极简工作室环境中采用戏剧性灯光。

![JSON 提示词：身着深红色西装的高级时装社论肖像](https://cms-assets.youmind.com/media/1770359940216_0pnzuk_HAXwWuxacAAenG5.jpg)

```
{
  "subject": {
    "identity_reference": "uploaded face reference",
    "identity_accuracy": "100% match in facial structure, eyes, lips, nose, jawline, hairline, natural skin texture; do not alter identity",
    "age_range": "adult woman",
    "pose": {
      "body_orientation": "standing, torso twisted, body turned at sharp angle",
      "shoulders": {
        "front_shoulder": "thrust forward prominently toward camera",
        "rear_shoulder": "pulled back"
      },
      "head": {
        "tilt": "chin down, head slightly lowered",
        "gaze": "eyes looking up from under brows, predatory intense gaze"
      },
      "arms": "hanging naturally or one hand in pocket",
      "hands": "bare, realistic fingers"
    },
    "expression": "fierce, predatory, intense, theatrical, smoldering gaze",
    "hair": "tight sleek bun"
  },
  "wardrobe": {
    "suit": {
      "blazer": {
        "color": "deep cherry red / burgundy",
        "fit": "oversized, exaggerated dropped-shoulder, structured broad shoulders, sharp shoulder pads, mid-thigh length",
        "front": "double-breasted, wide peak lapels, slightly boxy silhouette, sleeves slightly long"
      },
      "trousers": {
        "style": "high-waisted, ultra-wide-leg, deep front pleats, long hem pooling over heels"
      },
      "fabric": {
        "material": "premium heavy wool gabardine / wool twill",
        "texture": "dense, matte, slightly dry, visible diagonal twill weave, subtle creases, realistic drape",
        "finish": "no shine, no polyester look"
      }
    },
    "shirt": {
      "color": "crisp white poplin",
      "collar": "stiff, clean texture"
    },
    "tie": {
      "color": "deep cherry red",
      "material": "matte silk twill"
    },
    "accessories": {
      "earrings": "large gold hoop",
      "bracelet": "chunky gold on bare wrist"
    },
    "shoes": {
      "color": "burgundy",
      "style": "stiletto heels with ornate gold buckles"
    }
  },
  "environment": {
    "background": "seamless light-grey studio cyclorama",
    "studio": "clean, minimal, no props"
  },
  "camera": {
    "equipment": "Phase One XF, Schneider Kreuznach 80mm f/2.8 LS",
    "settings": {
      "aperture": "f/8",
      "ISO": 100,
      "shutter_speed": "1/160s"
    },
    "perspective": "vertical 3:4 full-body medium-to-long shot",
    "focus": "tack sharp face and fabric details"
  },
  "lighting": {
    "type": "soft diffused butterfly lighting",
    "fill": "subtle studio fill",
    "effect": "high-fashion clean illumination, emphasizes texture and drape"
  },
  "composition": {
    "framing": "full body, dramatic diagonal lines from torso twist, exaggerated theatrical stance",
    "balance": "centered subject with high-fashion editorial energy"
  },
  "aesthetic": {
    "style": "ultra-realistic high-fashion editorial",
    "mood": "theatrical, fierce, hunter energy, intense predatory attitude",
    "color_palette": ["deep "
  }
}
```

[[Dramatic Lighting]] [[High Fashion Editorial]] [[Luxury Fashion]] [[Minimalist Studio]]

---

### 94. 电影伐木工人肖像提示词

**Author**: [Minahil](https://x.com/Minahil42298354)  **Date**: 2026-02-05  **Language**: en

> 一个电影级写实提示词，用于生成一张特写肖像，描绘一位留着胡须、饱经风霜的中年男子，置身于白雪皑皑的松树林中。该提示词强调戏剧性的光线、超逼真的纹理，以及阳光穿透树林形成的焦外虚化效果。

![电影伐木工人肖像提示词](https://cms-assets.youmind.com/media/1770273499556_2rs3g8_HAXViVGXQAAMZxm.jpg)

```
"prompt": "Cinematic close-up portrait of a rugged middle-aged man with a thick grey-flecked beard and piercing blue eyes. He is wearing a classic red and black checkered flannel lumberjack jacket with a black fleece collar. He is standing in a snowy pine forest during a light snowfall, holding the wooden handle of an axe. Warm sunlight is breaking through the tall trees in the background, creating a soft bokeh effect and lens flare. Hyper-realistic texture, 8k resolution, dramatic lighting.",
    "aspect_ratio": "1:1",
    "style": "photorealistic_cinematic"
  }
```

[[Dramatic Lighting]] [[Hyperrealistic Photography]] [[Bokeh]]

---

### 95. 电影级商业镜头：解构的火鸡面

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-01-31  **Language**: en

> 一个用于生成电影级辣火鸡面美食广告镜头的提示。它侧重于解构视角，食材（面条、鸡肉、鸡蛋）悬浮在半空中，缓慢落入一个冒着热气的碗中，背景设定在一家地道的韩国拉面店，配以戏剧性的灯光和超现实的质感。

![电影级商业镜头：解构的火鸡面](https://cms-assets.youmind.com/media/1769927668687_jbq6af_G__1F17bEAY-h52.jpg)

```
Cinematic food commercial shot, high-angle deconstructed Spicy Buldak Ramen. In the center, a swirl of vibrant orange-red fire noodles, grilled chicken slices, two soft-boiled egg halves with jammy yolks, chopped scallions, and red chili flakes are suspended in mid-air, slowly falling into a steaming ceramic bowl of broth below. A pair of wooden chopsticks holds a large bunch of noodles at the top. The background is a warm, softly blurred authentic Korean ramen shop. Dramatic lighting with visible steam rising from the bowl. Hyper-realistic textures, 8K resolution, slow-motion movement, professional food photography style.
```

[[Dramatic Lighting]] [[Floating Ingredients]]

---

### 96. 超写实解构中东美食提示

**Author**: [Duet | AI](https://x.com/Sheldon056)  **Date**: 2026-01-30  **Language**: en

> 一个详细的 JSON 提示，用于生成超逼真的电影级美食摄影，内容为解构的中东菜肴（沙瓦玛和曼萨夫），采用悬浮元素、戏剧性灯光和质朴的厨房环境。

![超写实解构中东美食提示](https://cms-assets.youmind.com/media/1769841084070_n6r1n4_G_6zsoSakAARMPb.jpg)
![超写实解构中东美食提示](https://cms-assets.youmind.com/media/1769841084447_3xlekf_G_6zsoOboAAGR1N.jpg)

```
{
  "image_prompt": {
    "theme": "Hyper-realistic cinematic food photography of deconstructed Middle Eastern cuisine",
    "composition_style": "Levitating/Floating elements, exploded view",
    "scenes": [
      {
        "dish": "Deconstructed Shawarma",
        "floating_elements": [
          "Slices of seasoned grilled meat",
          "Pickles",
          "Red onion wedges",
          "Fresh parsley leaves",
          "Small ceramic bowls of white garlic sauce and tahini"
        ],
        "dynamic_actions": "Drop of sauce falling from bowl, soft steam rising from meat",
        "base_elements": "Rustic wooden plate with warm flatbread",
        "background_environment": "Moody, dark rustic kitchen with a glowing fireplace"
      },
      {
        "dish": "Deconstructed Jordanian Mansaf",
        "arrangement": "Vertical levitation layers",
        "layers": {
          "top": "Torn shrak bread",
          "middle": "Mound of yellow turmeric rice",
          "lower_middle": "Large chunks of tender cooked lamb",
          "bottom": "Dynamic splash of thick, creamy white jameed sauce"
        },
        "garnish": "Toasted almonds, pine nuts, chopped parsley",
        "base_elements": "Shallow clay dish",
        "background_environment": "Rustic stone kitchen"
      }
    ],
    "lighting_and_atmosphere": {
      "type": "Cinematic lighting",
      "mood": "Warm, moody, dramatic, high contrast",
      "specifics": "Soft highlights, rich textures"
    },
    "technical_specs": {
      "resolution": "8K",
      "camera_settings": "Shallow depth of field",
      "style": "Ultra-realistic commercial food photography"
    }
  }
}
```

[[Dramatic Lighting]] [[Floating Ingredients]] [[Cinematic Food Photography]]

---

### 97. 电影级女性战士肖像提示

**Author**: [邪修玩AI-诗泳](https://x.com/LiEvanna85716)  **Date**: 2026-01-30  **Language**: en

> 一个高度详细的提示，用于生成一张受花木兰启发的女性战士标准半身肖像，强调电影般的画质、逼真的纹理、戏剧性的光线，以及营造高端奇幻图像的特定氛围。

![电影级女性战士肖像提示](https://cms-assets.youmind.com/media/1769841144301_1v0smy_G_6AVtEbkAA1xxd.jpg)

```
Subject Description: A cinematic female warrior inspired by {argument name="inspiration" default="Mulan"}, strong, noble, and restrained beauty, calm yet determined expression
 Outfit: Elegant red ancient Chinese warrior costume inspired by traditional Han-style armor and flowing fabrics, minimal ornamentation, realistic textile texture, battle-worn yet refined
 Detail/Prop: Holding a long steel sword firmly in hand, simple and practical design, subtle reflections on the blade, heroic stance
 Setting: Quiet forest at early morning, soft mist among tall trees, muted natural colors, cinematic depth
 Style & Mood: High-end cinematic fantasy, realistic lighting, dramatic shadows, film still, epic yet poetic atmosphere, 35mm film look, cinematic color grading
```

[[Dramatic Lighting]] [[Cinematic Fantasy]] [[Half-Body Portrait]]

---

### 98. 电影级解构中东美食摄影

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-01-29  **Language**: en

> 一个高度详细、结构化的提示，用于生成电影级的食物摄影，主题是解构的中东菜肴（沙瓦玛和约旦曼萨夫）。该提示指定了悬浮/漂浮的元素、动态动作（酱汁滴落、蒸汽）、质朴的环境以及技术细节（8K 分辨率、电影级照明、浅景深），以营造出戏剧性、高对比度的视觉效果。

![电影级解构中东美食摄影](https://cms-assets.youmind.com/media/1769754976305_fdugme_G_0Lya_bUAEMkUo.jpg)
![电影级解构中东美食摄影](https://cms-assets.youmind.com/media/1769754976883_9nozuw_G_0LybEbYAAawLw.jpg)

```
{
  "image_prompt": {
    "theme": "Hyper-realistic cinematic food photography of deconstructed Middle Eastern cuisine",
    "composition_style": "Levitating/Floating elements, exploded view",
    "scenes": [
      {
        "dish": "Deconstructed Shawarma",
        "floating_elements": [
          "Slices of seasoned grilled meat",
          "Pickles",
          "Red onion wedges",
          "Fresh parsley leaves",
          "Small ceramic bowls of white garlic sauce and tahini"
        ],
        "dynamic_actions": "Drop of sauce falling from bowl, soft steam rising from meat",
        "base_elements": "Rustic wooden plate with warm flatbread",
        "background_environment": "Moody, dark rustic kitchen with a glowing fireplace"
      },
      {
        "dish": "Deconstructed Jordanian Mansaf",
        "arrangement": "Vertical levitation layers",
        "layers": {
          "top": "Torn shrak bread",
          "middle": "Mound of yellow turmeric rice",
          "lower_middle": "Large chunks of tender cooked lamb",
          "bottom": "Dynamic splash of thick, creamy white jameed sauce"
        },
        "garnish": "Toasted almonds, pine nuts, chopped parsley",
        "base_elements": "Shallow clay dish",
        "background_environment": "Rustic stone kitchen"
      }
    ],
    "lighting_and_atmosphere": {
      "type": "Cinematic lighting",
      "mood": "Warm, moody, dramatic, high contrast",
      "specifics": "Soft highlights, rich textures"
    },
    "technical_specs": {
      "resolution": "8K",
      "camera_settings": "Shallow depth of field",
      "style": "Ultra-realistic commercial food photography"
    }
  }
}
```

[[Dramatic Lighting]] [[8K Resolution]] [[Food Photography]] [[Steam Effect]]

---

### 99. Premium Dark Horizon 产品发布提示

**Author**: [Lloyd Creates](https://x.com/lloydcreates)  **Date**: 2026-01-26  **Language**: en

> 一个高级提示，建议生成一张具有“高级暗黑地平线”美学的产品揭示图片，可能涉及时尚设计、深色调和戏剧性灯光。

![Premium Dark Horizon 产品发布提示](https://cms-assets.youmind.com/media/1769495416843_vo3ap3_G_m9D7LW0AAeLY1.jpg)

```
Premium Dark Horizon Product Reveal
```

[[Dramatic Lighting]] [[Luxury Brand Aesthetic]]

---

### 100. 四种风格的戏剧性写实人物肖像

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2026-01-25  **Language**: en

> 一个旨在将 {argument name="person's name" default="Malavika Mohanan"} 的原始照片转换为四张独特、高度精细、超逼真的角色肖像的提示。每张图像都采用中景特写、广角镜头，并辅以极致、动态的摄像角度，强调电影级布光、高对比度和精确的色彩分级，以营造戏剧性的效果。

![四种风格的戏剧性写实人物肖像](https://cms-assets.youmind.com/media/1769408687052_kx431b_G_f1G8OagAAhHx7.jpg)

```
Transform the original photo into a dramatic, photorealistic, ultra-detailed set of 4 different styles characters are included , each a mid close up wide-angle shot with an extreme, dynamic camera angle  and the same person strikes a stylish  with cinematic lighting, high contrast, crisp textures, and precise color grading.
```

[[Dramatic Lighting]] [[High Contrast]] [[Color Grading]] [[Wide Angle Shot]]

---

### 101. 基于对象的宇宙：从一个冻结对象展开的现实

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2026-01-24  **Language**: en

> 一个电影概念艺术提示，用于生成一个 3D 构图，其中一个单一物体在释放出广阔而复杂的现实的那一刻被冻结。该提示描述了物体转变为地形、建筑和象征性地标，小人物在场景中穿梭。它强调了超详细的纹理、戏剧性的灯光以及一种破裂和涌现的紧张氛围。

![基于对象的宇宙：从一个冻结对象展开的现实](https://cms-assets.youmind.com/media/1769322313721_rrda3q_G_ZatE6bAAUoqtU.jpg)
![基于对象的宇宙：从一个冻结对象展开的现实](https://cms-assets.youmind.com/media/1769322313739_f81x6r_G_ZatDnbAAMSjhF.jpg)
![基于对象的宇宙：从一个冻结对象展开的现实](https://cms-assets.youmind.com/media/1769322313664_9noo91_G_ZatDvbAAUiobv.jpg)
![基于对象的宇宙：从一个冻结对象展开的现实](https://cms-assets.youmind.com/media/1769322315261_mwixjg_G_ZatE5bAAAkwpO.jpg)

```
Cinematic 3D composition centered on a {argument name="object" default="[OBJECT]"}, frozen at the instant it releases something far bigger than itself.

From within it, an entire {argument name="world style" default="[WORLD STYLE / THEME]"} reality unfolds, spilling outward into sweeping environments, towering forms, and dynamic motion that suggests this world was hidden there all along.

The object doesn’t just contain the world — it becomes part of it, with its shapes transforming into terrain, architecture, and symbolic landmarks.

Small figures, machines, or creatures navigate the scene, adding life, scale, and narrative.
The moment balances between dream and physics, where visual logic holds even as reality stretches.

The scene is charged with [ATMOSPHERE: glow, fog, particles, smoke, energy], amplifying the sense of rupture and emergence.

A subtle hint of the real world remains visible around the edges, anchoring the spectacle in realism.

Hyper-detailed textures, dramatic lighting, cinematic depth, ultra-realistic, 8K, concept art finish.
```

[[Dramatic Lighting]] [[Miniature Figure]]

---

### 102. JSON 格式的超低角度红毯时尚摄影提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个高度详细的 JSON 提示，用于生成一张戏剧性、时尚前卫的红毯肖像，采用极低角度（虫眼视角）构图。该提示详细说明了服装（紧身胸衣、薄纱裙、细高跟鞋）、环境（《怪奇物语》logo 背景）和灯光，以实现高冲击力的名人风格视觉效果，并要求提供主体身份的参考图像。

![JSON 格式的超低角度红毯时尚摄影提示](https://cms-assets.youmind.com/media/1769235977090_yppbjt_G_VkxnmXkAAv9Aa.jpg)

```
{ "prompt\_type": "text-to-image", "subject": { "identity": "Young woman resembling in the reference image", "appearance": "Long auburn-red hair worn down, fair skin, confident and serious facial expression", "accessories": "Dainty drop earrings" }, "attire": { "upper\_body": "Black corset-style bodice with sheer lace detailing and structured boning", "lower\_body": "Long, flowing black tulle skirt with a high slit, being held open by the subject's left hand", "legwear": "Sheer black tights/pantyhose", "footwear": "Black patent leather stiletto pumps with a pointed toe" }, "composition": { "camera\_angle": "Extreme low angle (worm's-eye view), looking up at the subject from the floor level", "perspective": "Emphasizes the height of the subject and the length of the legs", "framing": "Full body shot dominated by the foreground legs and shoes" }, "environment": { "location": "Red carpet premiere event", "background": "Large, 3D dimensional signage of the '{argument name="event logo" default="STRANGER THINGS"}' logo in the signature red serif font", "surface": "Dark maroon or red carpeted floor" }, "style": { "medium": "Digital photography, celebrity portrait", "lighting": "Professional event lighting, slight gloss on the skin and shoes, high contrast", "quality": "High resolution, 8k, photorealistic, sharp focus" } }
```

[[Dramatic Lighting]] [[Fashion Photography]] [[Low Angle Shot]]

---

### 103. 魔爪能量饮料的震撼产品视频提示

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-01-23  **Language**: en

> 一个用于生成富有戏剧性、高冲击力产品视频的提示，视频中一罐 Monster 能量饮料被金属链条紧紧缠绕在反光的黑色表面上。该提示指定了开场场景（静止的力量）和视觉元素，专为 Veo 等视频生成模型设计。

![魔爪能量饮料的震撼产品视频提示](https://cms-assets.youmind.com/media/1769235962230_ragx86_G_Uz0cibAAI-0CJ.jpg)

```
A dramatic high-impact product video featuring a Monster energy drink can centered on a reflective black surface, wrapped tightly in heavy metallic chains.

SCENE 1 — STILL POWER:
The video opens with a completely still frame. The Monster can stands perfectly upright in the center, wrapped in thick steel chains coiling around the body. The surface below reflects the can and chains like a dark mirror.
```

[[Dramatic Lighting]] [[Reflective Surface]]

---

### 104. 深色金属标志设计提示

**Author**: [AmirMušić](https://x.com/AmirMushich)  **Date**: 2026-01-18  **Language**: en

> 一个简短、描述性的提示，用于生成具有特定视觉风格的徽标或文本：深色金属外观，带有强烈、戏剧性的光照。

![深色金属标志设计提示](https://cms-assets.youmind.com/media/1768804221107_fh31y4_G--JK9pXIAEbRh3.jpg)

```
Dark metallic, heavy-lighted logos
```

[[Dramatic Lighting]] [[Graphic Design]] [[Logo Design]] [[Metallic Texture]]

---

### 105. 电影级未来隧道漫步

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-01-17  **Language**: en

> 一个提示，用于生成一位年轻女性穿梭于未来地下隧道的电影级肖像。它强调运动模糊、浅景深、青色与橙色的色彩对比以及戏剧性照明，以营造出现代时尚杂志的风格。

![电影级未来隧道漫步](https://cms-assets.youmind.com/media/1768717537190_sphpyo_G-2u2uqWIAAZhRm.jpg)

```
A cinematic portrait of a young woman walking through a futuristic underground tunnel, centered composition, shallow depth of field, strong motion blur streaks on both sides creating a speed effect, subject in sharp focus. She has long flowing blonde hair, natural makeup, calm and confident expression. Wearing a vintage-inspired green dress with white polka dots and a slim belt. Neon lights and metallic walls around her, teal and orange color contrast, dramatic lighting, soft film grain, ultra-realistic, high detail, 85mm lens look, f/1.8, cinematic photography, modern fashion editorial style.
```

[[Dramatic Lighting]] [[Motion Blur]] [[Fashion Magazine Style]]

---

### 106. 粗犷男士的高对比度电影感肖像

**Author**: [Favori](https://x.com/yuanguand)  **Date**: 2026-01-11  **Language**: en

> 一个用于生成粗犷英俊男士特写黑白肖像的提示。它强调戏剧性的光线、深邃的阴影、细致的纹理（胡须、胡茬）和忧郁的表情，以打造一幅高对比度的电影杰作。

![粗犷男士的高对比度电影感肖像](https://cms-assets.youmind.com/media/1768226040049_pk9vho_G-Y7Wz9bQAAa-U3.jpg)

```
Extreme close-up black and white portrait of an incredibly handsome rugged man, wild messy windswept hair, thick textured rough beard accentuating a strong angular jaw and sculpted cheekbones, piercing eyes cast downward in thoughtful melancholy. Dramatic single ray of light cuts across his perfectly proportioned face, highlighting flawless bone structure and subtle stubble detail, deep shadows enveloping the rest, conveying raw intensity, brooding solitude and undeniable charisma, high contrast cinematic style, photorealistic masterpiece.
```

[[Dramatic Lighting]] [[High Contrast Monochrome]]

---

### 107. 高对比度黑白影棚肖像提示词

**Author**: [Inspova｜The Prompt Gallery for Daily Inspo](https://x.com/Inspova)  **Date**: 2026-01-10  **Language**: en

> 生成一张高分辨率黑白肖像的提示：一位女孩身穿黑色高领毛衣，梳着韩式发髻，置身于极简工作室中，戏剧性的灯光营造出大胆的几何阴影，最终呈现出电影般的高对比度图像。

![高对比度黑白影棚肖像提示词](https://cms-assets.youmind.com/media/1768143855948_prf3yo_G-VeYVqW4AIUFCz.jpg)

```
A high resolution black and white portrait of a girl wearing a sharp black turtle neck and chic small gold earrings along with Korean bun. She stands confidently in minimal studio setting slightly to the side dramatic studio lighting creates bold geometric shadows on her face and background strong cross beams of light. Cut through the shadows her expression is calm introspective and slightly distant the image has cinematic, high quality nor tone with high contrast and fine detail on her face and suits texture soft brokeh background portrait (9:16) 8K resolution
```

[[Dramatic Lighting]] [[Minimalist Studio]] [[Film Noir]] [[Black Turtleneck]]

---

### 108. 芝士汉堡滋滋作响的电影级特写镜头

**Author**: [Oogie](https://x.com/oggii_0)  **Date**: 2026-01-10  **Language**: en

> 一个生成超逼真、电影级特写美食芝士汉堡的提示。它着重于戏剧性元素，如滋滋作响的焦痕、流淌的切达奶酪、浓厚的蒸汽、漂浮的火花和凝固的油脂滴，所有这些都通过微距镜头在高对比度的黑色背景下捕捉。

![芝士汉堡滋滋作响的电影级特写镜头](https://cms-assets.youmind.com/media/1768143810202_cc6slh_G-TmJNEasAE4Eff.jpg)
![芝士汉堡滋滋作响的电影级特写镜头](https://cms-assets.youmind.com/media/1768143810183_q3zzjj_G-TmJMIbEAAMl-j.jpg)
![芝士汉堡滋滋作响的电影级特写镜头](https://cms-assets.youmind.com/media/1768143810356_sfcnjm_G-TmJNQbgAAPD7g.jpg)

```
A hyper-realistic, cinematic close-up of a sizzling gourmet cheeseburger. The thick, juicy beef patty features a heavy, glossy char and is blanketed in vibrant orange cheddar cheese that melts and oozes down the sides in thick, viscous streams over a toasted brioche bun. The atmosphere is dramatic and smoky, with thick wisps of white and blue steam swirling upwards, surrounded by floating bright orange sparks, glowing embers, and frozen droplets of grease suspended in the air. The lighting is high-contrast and dramatic against a deep black background, emphasizing the glistening textures. Shot with a macro lens, shallow depth of field, and 8k resolution commercial food photography style.
```

[[Dramatic Lighting]] [[Food Photography]] [[Commercial Food Photography]] [[Dark Background]]

---

### 109. 撕开印尼蛋饼的微距美食摄影

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2026-01-10  **Language**: en

> 一个用于生成印尼街头小吃——印尼蛋饼（Martabak Telur）超写实微距美食摄影的提示。它着重捕捉酥脆外皮撕开、馅料爆出的瞬间，强调蒸汽、油光、戏剧性光线以及美食编辑摄影中常见的超高纹理细节。

![撕开印尼蛋饼的微距美食摄影](https://cms-assets.youmind.com/media/1768143798375_rb4cd9_G-S7EnbasAMtjJM.jpg)
![撕开印尼蛋饼的微距美食摄影](https://cms-assets.youmind.com/media/1768143798311_t6i77p_G-S7EpgbQAAYGRV.jpg)
![撕开印尼蛋饼的微距美食摄影](https://cms-assets.youmind.com/media/1768143798419_xc4sfz_G-S7EmOasAQARkS.jpg)
![撕开印尼蛋饼的微距美食摄影](https://cms-assets.youmind.com/media/1768143801552_z5c36t_G-S7EnaaAAAGu7Q.jpg)

```
"Macro food photography of a crispy martabak telur tearing open mid-air, thin golden wrapper shattering with a crack, hot filling of minced beef, scallions, and egg bursting outward. Flecks of fried onion and pepper suspended in motion, steam visible, glossy oil sheen catching the light. Warm Indonesian street-stall lighting, tungsten + charcoal warmth, dramatic rim light, ultra high texture detail (bubbled wrapper, layered interior).Editorial food shot, shallow depth of field, bokeh of night market signage, Nikon Z9 look, 105mm macro, fast shutter freeze, hyper-real crumbs. --ar 3:4"
```

[[Dramatic Lighting]] [[Steam Effect]]

---

### 110. 逼真的战损机甲提示词

**Author**: [はると@AIクリエイター](https://x.com/ai_buty)  **Date**: 2026-01-08  **Language**: en

> 对 Nano Banana Pro 和 Seedream 4.5 在生成战损机甲图像方面的详细比较。所提供的提示描述性极强，侧重于照片级真实感、工业设计、重型装甲、具体的损坏细节（漆面剥落、铁锈）以及具有戏剧性光照的末日废土背景。

![逼真的战损机甲提示词](https://cms-assets.youmind.com/media/1767967500521_lv37m0_G-HDj5La4AAm8r6.jpg)
![逼真的战损机甲提示词](https://cms-assets.youmind.com/media/1767967500695_ucak08_G-HDj5Ia0AIS6lW.jpg)

```
Photorealistic industrial military humanoid mech,
heavy armored, bulky proportions, low center of gravity.
Hard surface mechanical modeling, realistic engineering details.

Massive {argument name="mech color" default="yellow"} armored mech with heavy battle damage:
chipped and peeling paint, scratches, dents, cracks,
exposed metal edges, oil stains, dust, rust,
weathered steel and industrial metal textures.

Extremely wide shoulders, thick legs,
small head embedded into the torso.
Right hand holding a large industrial hammer weapon.
Left arm integrated with a heavy shield-like armor.

Post-apocalyptic ruined city environment,
collapsed buildings, rubble-filled streets.
Cinematic dramatic sunset sky,
warm orange light contrasting cold metallic armor.
Realistic global illumination, high contrast lighting.

Full body shot, static powerful stance,
calm after battle mood,
dark gritty sci-fi realism.

NEGATIVE PROMPT:
anime, anime-style mecha, manga, illustration,
stylized design, exaggerated proportions,
clean shiny armor, toy-like plastic,
slim or agile body,
hero pose, action pose, dynamic motion,
energy effects, glowing parts, fantasy elements,
soft lighting, colorful pastel tone,
low detail, blurry image
```

[[Dramatic Lighting]]

---

### 111. 电影巨头手持迷你版自己

**Author**: [The Muskan](https://x.com/Themuskice)  **Date**: 2026-01-07  **Language**: en

> 一个用于 Gemini Nano Banana Pro 的创意提示，旨在生成一张超现实、电影级的特写镜头，画面中是一个巨大化的参考人物，手中拿着一个微型、与自己一模一样的版本。该提示强调了皮肤的细腻纹理、织物的褶皱以及戏剧性的光照，并要求上传一张参考图片以确定人物身份。

![电影巨头手持迷你版自己](https://cms-assets.youmind.com/media/1767966104663_kijpyn_G-EZmyUaUAAdVrT.jpg)

```
Cinematic ultra-realistic close-up, a giant version of the reference person (uploaded photo) holding a smaller identical version of himself in his hand, facing the camera, fully visible, and highly photogenic. Both are wearing the same outfit: oversized black t-shirt with {argument name="t-shirt text" default="The Muskan"}, black sunnies, cargo pants, and Adidas sneakers.
The giant’s massive hand fills the frame, with realistic skin texture, veins, and natural creases. The smaller figure sits upright in the palm, relaxed and confident, clean facial visibility and balanced pose. The giant’s lifelike face and eyes loom behind, calm and dominant.
Focus on detailed skin texture on the giant hand and face, crisp fabric folds, cargo pocket details, and subtle reflections on the sunglasses. Dramatic lighting, shallow depth of field, documentary style.
9:16 ratio, clear and vibrant, ultra-realistic."
```

[[Dramatic Lighting]] [[Identity Locking]] [[Cinematic Close-Up]]

---

### 112. 受伤的幽灵蜘蛛（复制品）：萨迪·辛克饰演的坚毅电影肖像

**Author**: [Creator Backstage](https://x.com/CBackstageAI)  **Date**: 2026-01-04  **Language**: en

> 一个高度具体的提示，用于生成一张超逼真的电影级肖像，描绘女演员萨迪·辛克（Sadie Sink）饰演受伤、疲惫的幽灵蜘蛛（格温·斯黛西）。场景设定在一个黑暗、极简主义的摄影棚中，强调戏剧性的灯光、撕裂战衣的真实纹理，以及主体手持面具时的情感强度。（此提示复制自推文 2007870235618275613）。

![受伤的幽灵蜘蛛（复制品）：萨迪·辛克饰演的坚毅电影肖像](https://cms-assets.youmind.com/media/1767607002831_id0a8m_G91tJBoXwAAFSId.jpg)

```
{
  "environment": {
    "location": "Dark, minimalist studio setting",
    "background": "Solid, deep black background, completely dark"
  },
  "subject": {
    "person": "Sadie Sink",
    "appearance": {
      "hair": "Wavy, copper red hair, slightly messy",
      "face": "Injured, with dirt, cuts, scratches, and grime, tired expression, tear stains",
      "eyes": "Blue eyes, looking intently at camera"
    }
  },
  "pose": {
    "action": "Holding a white Ghost-Spider mask with both gloved hands, pressing it against her cheek",
    "body_language": "Somber, weary, introspective"
  },
  "lighting": {
    "type": "Dramatic studio lighting, directional from upper right",
    "quality": "Soft highlights on face and suit texture, deep shadows"
  },
  "clothes_and_styling": {
    "costume": "Ghost-Spider (Gwen Stacy) superhero suit",
    "details": "White fabric with pink and black accents, torn, dirty, scuffed, worn, realistic textures",
    "mask": "White textured mask with pink-rimmed eye lenses, held separately"
  },
  "mood": "Somber, intense, gritty, emotional, resilient",
  "photography": {
    "style": "Ultra photorealistic portrait, cinematic quality",
    "camera": "High-resolution DSLR",
    "lens": "Prime lens, f/2.8",
    "focus": "Sharp focus on subject's face and mask, shallow depth of field",
    "texture": "Emphasizing realistic fabric weave, skin pores, and grime"
  }
}
```

[[Dramatic Lighting]] [[Dark Studio Setting]]

---

### 113. 萨迪·辛克 (Sadie Sink) 饰演受伤的幽灵蜘蛛侠 (Ghost-Spider) 的粗犷电影肖像

**Author**: [Lex](https://x.com/lexx_aura)  **Date**: 2026-01-04  **Language**: en

> 一个高度具体的提示，用于生成一张超逼真的电影级肖像，描绘女演员萨迪·辛克（Sadie Sink）饰演受伤、疲惫的幽灵蜘蛛（格温·斯黛西）。场景设定在一个黑暗、极简主义的摄影棚中，强调戏剧性的光线、破损战衣的真实纹理，以及主体手持面具时的情感强度。

![萨迪·辛克 (Sadie Sink) 饰演受伤的幽灵蜘蛛侠 (Ghost-Spider) 的粗犷电影肖像](https://cms-assets.youmind.com/media/1767606995451_nf2usi_G91jUN8XsAANWwk.jpg)

```
{
  "environment": {
    "location": "Dark, minimalist studio setting",
    "background": "Solid, deep black background, completely dark"
  },
  "subject": {
    "person": "Sadie Sink",
    "appearance": {
      "hair": "Wavy, copper red hair, slightly messy",
      "face": "Injured, with dirt, cuts, scratches, and grime, tired expression, tear stains",
      "eyes": "Blue eyes, looking intently at camera"
    }
  },
  "pose": {
    "action": "Holding a white Ghost-Spider mask with both gloved hands, pressing it against her cheek",
    "body_language": "Somber, weary, introspective"
  },
  "lighting": {
    "type": "Dramatic studio lighting, directional from upper right",
    "quality": "Soft highlights on face and suit texture, deep shadows"
  },
  "clothes_and_styling": {
    "costume": "Ghost-Spider (Gwen Stacy) superhero suit",
    "details": "White fabric with pink and black accents, torn, dirty, scuffed, worn, realistic textures",
    "mask": "White textured mask with pink-rimmed eye lenses, held separately"
  },
  "mood": "Somber, intense, gritty, emotional, resilient",
  "photography": {
    "style": "Ultra photorealistic portrait, cinematic quality",
    "camera": "High-resolution DSLR",
    "lens": "Prime lens, f/2.8",
    "focus": "Sharp focus on subject's face and mask, shallow depth of field",
    "texture": "Emphasizing realistic fabric weave, skin pores, and grime"
  }
}
```

[[Dramatic Lighting]]

---

### 114. 高端时尚三联画广告系列的智能提示

**Author**: [AmirMušić](https://x.com/AmirMushich)  **Date**: 2026-01-03  **Language**: en

> 一个为 Nano Banana Pro 设计的精密智能提示，旨在为指定品牌生成一个超现实的时尚编辑摄影三联画活动。AI 将根据品牌的原型自主生成一位缪斯，并创作三幅连贯的特写面板，分别聚焦于肖像、姿态和纹理，运用戏剧性灯光和前卫造型。

![高端时尚三联画广告系列的智能提示](https://cms-assets.youmind.com/media/1767604023303_33eeia_G9untHmX0AAi826.jpg)

```
A high-end, hyper-realistic editorial fashion photography triptych campaign for brand: {argument name="brand name" default="[BRAND NAME]"}.

THE TASK:

Act as a world-class fashion photographer (e.g., Steven Meisel, Paolo Roversi, or Harley Weir) shooting a defining image campaign for {argument name="brand name" default="[BRAND NAME]"}. You must create a cohesive 3-panel editorial layout, stacked horizontally (top, middle, bottom panels). The focus is intensely on cinematic close-ups and textural details.

THE MUSE (AI AUTONOMY):

Analyze the deepest archetype, aesthetic, philosophy, and target audience lifestyle of {argument name="brand name" default="[BRAND NAME]"}. Based only on this analysis, autonomously generate the ultimate human muse for the brand. You determine their gender, age, unique ethnicity, striking features, and charismatic attitude. This person is not a model posing; they are the living embodiment of the brand's spirit.

THE TRIPTYCH NARRATIVE & COMPOSITION (HORIZONTAL STACK - CLOSE-UP FOCUS):

The three stacked panels must form a unified, intimate visual essay about the brand's essence, prioritizing tight framing.

Top Panel (The Intense Portrait): A cinematic, tight headshot focusing on the eyes and face. Intense, communicative gaze. Highlighting skin texture and emotion.

Middle Panel (The Gesture/Action): A tight crop focusing on a specific body part in motion or repose—hands clutching something, the curve of a neck, a mouth smoking a cigarette, posture. It conveys the character's attitude without showing the whole body.

Bottom Panel (The Ultimate Texture/Symbol): An extreme macro close-up. A detail of a unique garment fabric, a piece of jewelry, a symbolic prop relevant to the brand's lifestyle, or an abstract texture from their environment.

STYLING & BOLD CHOICES (CRITICAL):

Push boundaries. The styling must be avant-garde high fashion. Incorporate unexpected elements to create an "art-house" feel: weird accessories, juxtaposed garments, props, or even a touch of deliberate absurdity if it fits the brand's vibe. The image must feel raw, expensive, and tactile.

TECHNICAL AESTHETICS:

Hyper-realism: Strong film grain, highly detailed textures (pores, fabric weave), realistic depth of field.

Lighting: Bold, cinematic, and dramatic. Use chiaroscuro, colored gels, harsh sunlight, or moody shadows depending on the brand's DNA.

Color: A sophisticated, editorial color grading palette that is perfectly harmonious and relevant to {argument name="brand name" default="[BRAND NAME]"}.
```

[[Dramatic Lighting]]

---

### 115. Gemini Nano Banana 魅力照片提示

**Author**: [blogbursthub](https://x.com/blogbursthub)  **Date**: 2025-12-31  **Language**: en

> 这是一个为 Gemini Nano Banana 模型设计的图像生成提示词，旨在为拍摄对象创作一张令人惊艳的魅力照片。该提示词指定了电影般的、高细节的美学风格，并要求使用戏剧性的灯光和特定的调色板。

![Gemini Nano Banana 魅力照片提示](https://cms-assets.youmind.com/media/1767456283511_a9qimq_G9fEt54bIAA92Zu.jpg)

```
A stunning glamour photo of a {argument name="subject" default="woman"}, cinematic, dramatic lighting, high detail, 8k, ultra-realistic, deep shadows, rich colors, {argument name="color palette" default="gold and crimson"} color palette, {argument name="style" default="fashion magazine style"}
```

[[Dramatic Lighting]] [[Editorial Photography]]

---

### 116. 魔法速写本艺术活灵活现

**Author**: [Alexandra Aisling](https://x.com/AllaAisling)  **Date**: 2025-12-30  **Language**: en

> 一个用于 Adobe Firefly 的电影级提示，描述了一本复古的皮革装订速写本，其中一个特定主题神奇地从书页中以超详细的 3D 形式浮现，从铅笔线条过渡到现实，置于一张凌乱的艺术家书桌上，并配有戏剧性的灯光。

![魔法速写本艺术活灵活现](https://cms-assets.youmind.com/media/1767454944785_bfa2uz_G9Ymdl1XwAA5H4E.jpg)
![魔法速写本艺术活灵活现](https://cms-assets.youmind.com/media/1767454944905_rwntpc_G9YnGjyXIAAwIpO.jpg)
![魔法速写本艺术活灵活现](https://cms-assets.youmind.com/media/1767454945696_xkwa41_G9YnNiyXUAAm5dw.jpg)
![魔法速写本艺术活灵活现](https://cms-assets.youmind.com/media/1767454948025_7qhb1q_G9YnVDtXcAAIm6d.jpg)

```
An open vintage leather-bound sketchbook lying on a cluttered artist's desk, with a {argument name="subject" default="[subject]"} magically coming to life and rising fully three-dimensional out of the pages in a breathtaking display of art becoming reality. The {argument name="subject" default="[subject]"} towers magnificently above the book with {argument name="key features" default="[key features]"}, its form transitioning from faint pencil sketch lines at the base into richly textured, hyper-detailed, fully realized 3D form. Magical glowing particles and wisps of ethereal light swirl around the {argument name="subject" default="[subject]"} where drawing meets reality. The {argument name="subject" default="[subject]"} casts dramatic shadows across the book and desk. The desk is scattered with vintage ink bottles, paint jars, worn brushes in ceramic containers, scattered pencils, crumpled paper, and paint splatters. Dark moody background, cinematic golden-hour lighting from the side with subtle rim light, rich browns, deep reds, amber, and warm gold tones, hyper-photorealistic, 8K resolution, extreme intricate detail, dramatic cinematic composition, front-facing view at desk level, masterpiece quality, awe-inspiring.
```

[[Dramatic Lighting]]

---

### 117. 高级时装工作室编辑肖像

**Author**: [Iris](https://x.com/xIrissy)  **Date**: 2025-12-29  **Language**: en

> 一个用于生成高时尚、极简主义编辑肖像的提示：一位女性身穿黑色紧身胸衣迷你连衣裙和超大廓形西装外套，置身于浅灰色无缝影棚背景中。该提示强调戏剧性的聚光灯效果、高光泽的皮肤质感和时尚精致的美学，重点突出拍摄对象自信的表情和服装细节。

![高级时装工作室编辑肖像](https://cms-assets.youmind.com/media/1767166851481_z7hz7o_G9VdFaqbsAAdSwp.jpg)

```
{
  "subject": {
    "gender": "female",
    "appearance": {
      "skin_tone": "bronzed/tanned",
      "skin_texture": "high gloss, hyper-realistic, oily sheen on chest and shoulders",
      "hair": {
        "color": "dark brown/black",
        "style": "sleek, tightly pulled back, center part",
        "finish": "wet look/polished"
      },
      "face": {
        "eyes": "light blue/green, sharp gaze",
        "eyebrows": "structured, dark",
        "lips": "full, nude-pink matte",
        "expression": "sultry, confident, serious model pout"
      }
    },
    "outfit": {
      "coat": {
        "type": "oversized blazer/trench coat",
        "color": "matte black",
        "material": "wool blend",
        "styling": "draped over shoulders (cape style)"
      },
      "dress": {
        "type": "corset mini dress",
        "material": "black satin/silk mix with mesh",
        "details": [
          "structured boning",
          "sheer mesh waist panels",
          "scoop neckline",
          "fitted silhouette"
        ]
      },
      "accessories": {
        "gloves": "black leather, wrist-length",
        "earrings": "small thick gold hoops",
        "bag": "minimalist black rectangular leather clutch"
      }
    },
    "pose": {
      "body": "standing, weight shifted to one hip",
      "arms": "relaxed at sides",
      "hands": "holding clutch in right hand"
    }
  },
  "setting": {
    "background": "seamless studio background",
    "color": "neutral light grey",
    "vibe": "minimalist, high-fashion editorial"
  },
  "lighting_and_composition": {
    "lighting_style": "dramatic spotlight/snoot",
    "key_light": "focused on face and upper chest",
    "shadows": "vignetted edges, soft drop shadow behind subject",
    "shot_type": "medium shot (mid-thigh up)",
    "camera_angle": "eye level, straight on"
  }
}
```

[[Dramatic Lighting]] [[Fashion Photography]] [[Studio Photography]]

---

### 118. 高对比度单色影棚肖像提示词

**Author**: [Hatman 🎩](https://x.com/WhoTFIsHatman)  **Date**: 2025-12-29  **Language**: en

> 一个用于生成高对比度黑白影棚肖像的提示，带有电影胶片颗粒感。它着重于使用强烈、鲜明的主光来雕塑面部特征，并突出原色牛仔衬衫的纹理，强调一种轻松、时尚的氛围和超细节的摄影写实主义。

![高对比度单色影棚肖像提示词](https://cms-assets.youmind.com/media/1767166923107_s7cvo9_G9VDxFNbIAAkPMl.jpg)
![高对比度单色影棚肖像提示词](https://cms-assets.youmind.com/media/1767166923258_6aihyn_G9VDxFQaMAAxMSv.jpg)

```
Create a 1:1 high-contrast monochrome studio portrait with a half-body composition and cinematic film grain. A person with dark, swept-back hair makes direct eye contact, wearing a bright, genuine Duchenne smile. Harsh, vibrant key lighting sculpts sharp facial highlights and reveals the deep texture of a raw denim shirt with rolled sleeves. Underneath is a crisp white V-neck, paired with fitted chinos. Hands rest casually in the pockets. Set against a high-key white backdrop, the mood is relaxed and editorial, with ultra-detailed, photorealistic realism.
```

[[Dramatic Lighting]] [[Film Grain]] [[Fashion Portrait]] [[Studio Photography]]

---

### 119. 侦探证据板生成

**Author**: [Artificial intelligence (Ai),Open Ai](https://x.com/Vishnudxe)  **Date**: 2025-12-29  **Language**: en

> 一个旨在生成侦探证据板视觉概念的提示，模拟了一种痴迷的、深夜黑色电影氛围。它详细描述了软木板上的内容：拍立得照片、地图、报纸剪报、便利贴以及连接证据的红线，强调了来自一个裸露灯泡的戏剧性阴影，以及咖啡渍等逼真的杂乱物品。

![侦探证据板生成](https://cms-assets.youmind.com/media/1767166861840_f5kbrz_G9UejSfa0AAtmYj.jpg)

```
"A detective's evidence board investigating \\{argument name="subject/mystery" default="[SUBJECT/MYSTERY]"}\\\. Cork surface covered with pinned items: polaroid photographs with handwritten dates, a street map with circled locations, newspaper clippings with highlighted passages, sticky notes with theories and question marks, and printed documents with redacted black bars. Red string connects related evidence across the board, creating a web of connections. Thumbtacks in primary colors. A single bare bulb casts dramatic shadows. Coffee ring stains on some papers. The atmosphere is obsessive, late-night, noir—someone has been piecing this together for months. A few pins have fallen, suggesting frantic recent activity."
```

[[Dramatic Lighting]] [[Film Noir]]

---

### 120. 忧郁电影爵士俱乐部肖像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2025-12-29  **Language**: en

> 一个详细的图像生成提示，用于创作一张情绪化、电影感十足、方形构图的肖像照：一位魅力四射的女性身处昏暗的爵士俱乐部中，重点突出戏剧性的光影效果、深邃的阴影，以及散景和自然颗粒等高质量胶片美学。

![忧郁电影爵士俱乐部肖像](https://cms-assets.youmind.com/media/1767166954430_p6a7pg_G9ThZYiaUAAX3sQ.jpg)

```
A moody, square-format 1:1 cinematic shot of a beautiful woman in a glamorous {argument name="outfit" default="silk gown"} sitting in a dimly lit, smoky jazz club. Cinematic lighting, dramatic shadows, dreamy atmosphere. Shallow depth of field, creamy bokeh, 8K resolution. Natural film grain, light leaks, soft focus edges, sharp central face details, authentic moment, nostalgic film feel.
```

[[Dramatic Lighting]] [[Glamour Photography]] [[Film Noir]] [[Moody Atmosphere]]

---

### 121. 高级时尚单色矢量插画提示

**Author**: [Gagan Singh](https://x.com/GaganSingh8u)  **Date**: 2025-12-29  **Language**: en

> 这是一个专为图像到图像生成设计的提示，指示 AI 在严格保留身份的同时，将上传的图像转换为全新的高级时装编辑姿势。最终输出必须是纯粹的黑白插画，融合精致的矢量艺术，并以戏剧性的灯光和极简的背景呈现。

![高级时尚单色矢量插画提示](https://cms-assets.youmind.com/media/1767166904778_j1w948_G9SPE8iagAA5TRz.jpg)
![高级时尚单色矢量插画提示](https://cms-assets.youmind.com/media/1767166904743_x6zqj8_G9SPE8ibgAAqiHI.jpg)

```
{
  "prompt": "Use the uploaded image strictly as an identity reference. Preserve 100% exact face match, facial structure, expressions, skin tone (translated accurately into grayscale), hairstyle, and identity of every person visible in the reference image. Do not add or remove any person. Create a new high-fashion editorial pose (for example: confident upright stance, slight profile angle, strong posture, composed expressions) while keeping anatomy natural and elegant. Convert the scene into a pure black-and-white illustration blended with refined vector art. Use crisp black ink outlines, smooth grayscale shading, and controlled contrast to define facial structure and form. Skin tones should translate naturally into grayscale values without losing identity. Clothing should remain similar in type but rendered in monochrome with clear vector edges, folds, and tonal separation. Lighting should be dramatic and directional, emphasizing facial features and silhouettes through light–shadow contrast. Redesign the background into a minimal editorial vector backdrop using negative space, gradients in grayscale, or subtle geometric balance. Render in ultra high resolution with sharp edges, clean layers, and a sophisticated magazine-style black-and-white finish.",
  
  "negative_prompt": "face mismatch, identity change, extra person, missing person, wrong facial features, bad anatomy, extra fingers, extra limbs, color elements, photorealism, heavy textures, painterly strokes, low quality, blur, noise, grain, watermark, logo, text",
  
  "style": "black and white editorial illustration + vector art",
  "mood": "bold, elegant, high-fashion",
  "lighting": "dramatic directional monochrome lighting",
  "background": "minimal grayscale vector backdrop",
  "detail_level": "high and refined",
  "render_quality": "ultra high resolution, editorial clarity",
  "composition": "same persons, new editorial pose, monochrome palette",
  "reference_strength": 0.8
}
```

[[Dramatic Lighting]] [[Style Transfer]] [[Vector Art]] [[Fashion Illustration]]

---

### 122. 迷人黑色亮片迷你连衣裙时尚肖像

**Author**: [KeorUnreal](https://x.com/KeorUnreal)  **Date**: 2025-12-28  **Language**: en

> 生成一张时尚秀上魅力四射的年轻女性的超写实图像的详细提示。她身穿一件黑色薄纱亮片迷你连衣裙，裙摆饰有夸张的羽毛，头戴黑色贝雷帽。图像采用柔和而富有戏剧性的灯光捕捉，突出了亮片和纹理，营造出一种高级时尚、诱人的氛围。

![迷人黑色亮片迷你连衣裙时尚肖像](https://cms-assets.youmind.com/media/1767061673283_7vmpxo_G9Rky2RWUAAD-cV.jpg)

```
{
  "prompt": "A glamorous young woman with long, wavy blonde hair and fair skin sits confidently in the front row of a dimly lit fashion show or event venue, gazing directly at the camera with a subtle, enigmatic smile. She wears a striking black beret tilted stylishly on her head and a luxurious sheer black sequined mini dress completely covered in sparkling silver sequins that catch the light, featuring dramatic black feather trim around the high neckline and long sleeves, the feathers cascading elegantly over her shoulders and arms. The dress is form-fitting and short, revealing her toned legs in sheer black stockings. She holds a {argument name="phone case color" default="red"} phone case in one hand, long manicured nails visible, while the other rests on her thigh. The background shows a blurred audience seated in rows of white chairs, overhead spotlights, and a modern ceiling with hanging lights, creating a high-fashion, runway atmosphere with soft dramatic lighting that highlights the sparkle of her outfit and the texture of the feathers. Ultra-realistic skin and sequin details, luxurious and seductive vibe, highly detailed feather trim, sequin reflections, hair waves, beret angle, and subtle venue ambiance."
}
```

[[Dramatic Lighting]] [[Glamour Portrait]] [[Sequin Dress]]

---

### 123. Noir 镜面反射肖像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2025-12-28  **Language**: en

> 一个简洁而富有启发性的提示，用于生成一张高对比度的黑白电影肖像，风格为经典黑色电影，重点描绘一个男人面对镜子，镜中的倒影显得更暗、更强烈，并突出他下颌线清晰的阴影。

![Noir 镜面反射肖像](https://cms-assets.youmind.com/media/1767061711059_rwcn12_G9RIA_ibQAAe0YA.jpg)

```
High-contrast black and white cinematic portrait of a man facing a mirror, reflection appearing darker and more intense, low-key lighting, sharp jawline shadows, classic noir style, ultra-realistic facial texture, cinematic framing
```

[[Dramatic Lighting]] [[High Contrast Photography]] [[Black And White Photography]] [[Film Noir]]

---

### 124. 金色火焰奇幻肖像对比

**Author**: [Hoor](https://x.com/hoor_world06)  **Date**: 2025-12-28  **Language**: en

> 一个结构化的提示，旨在生成一幅对比鲜明的女性奇幻肖像。图像中，主体身着象牙色礼服，礼服上点缀着柔和的金色火焰，置身于一个漂浮着余烬的黑暗石室中，强调了受控的强度和一种白皙、温暖的光芒。

![金色火焰奇幻肖像对比](https://cms-assets.youmind.com/media/1767061667508_41xddi_G9Qnt-gaYAAb2W0.jpg)

```
{
  "render_goal": "Contrasting fantasy portrait",
  "subject": {
    "pose": "female standing centered",
    "expression": "controlled intensity",
    "skin_tone": "fair warm glow"
  },
  "wardrobe": "{argument name="wardrobe item" default="ivory gown"} with soft {argument name="flame color" default="golden"} flames along the hem",
  "environment": {
    "location": "dark stone chamber",
    "props": "floating embers, soft shadows"
  }
}
```

[[Dramatic Lighting]] [[Fantasy Portrait]]

---

### 125. Noir 侦探证据板可视化

**Author**: [Alexandra Aisling](https://x.com/AllaAisling)  **Date**: 2025-12-27  **Language**: en

> 生成一张经典侦探证据板的超写实图像的提示。它详细描述了构图，包括宝丽来照片、地图、报纸剪报，以及用红线连接的证据，所有这些都置于戏剧性的灯光下，以营造出一种痴迷的、深夜黑色电影的氛围。

![Noir 侦探证据板可视化](https://cms-assets.youmind.com/media/1766987652954_jissvt_G9JTkAyX0AA90JY.jpg)
![Noir 侦探证据板可视化](https://cms-assets.youmind.com/media/1766987653303_q6f5nh_G9JTqNyW0AAioz4.jpg)
![Noir 侦探证据板可视化](https://cms-assets.youmind.com/media/1766987654344_h9fl2y_G9JTxn8XoAABakD.jpg)
![Noir 侦探证据板可视化](https://cms-assets.youmind.com/media/1766987655731_ahotza_G9JT4psXkAE9osz.jpg)

```
A detective's evidence board investigating {argument name="subject or mystery" default="[SUBJECT/MYSTERY]"}. Cork surface covered with pinned items: polaroid photographs with handwritten dates, a street map with circled locations, newspaper clippings with highlighted passages, sticky notes with theories and question marks, and printed documents with redacted black bars. Red string connects related evidence across the board, creating a web of connections. Thumbtacks in primary colors. A single bare bulb casts dramatic shadows. Coffee ring stains on some papers. The atmosphere is obsessive, late-night, noir—someone has been piecing this together for months. A few pins have fallen, suggesting frantic recent activity.
```

[[Dramatic Lighting]] [[Film Noir]]

---

### 126. 构建不可能的提示：微型工程师

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2025-12-24  **Language**: en

> 为 Gemini Nano Banana Pro 提供的提示：生成一张大型建筑工地的图片，其中微型工程师或建筑工人正在一块一块地组装一个超大的日常物品，重点突出真实的材料和戏剧性的光线。

![构建不可能的提示：微型工程师](https://cms-assets.youmind.com/media/1766936161050_0uic4u_G85rp0PagAIpbWb.jpg)
![构建不可能的提示：微型工程师](https://cms-assets.youmind.com/media/1766936161383_k2ws78_G85rp13agAIa97T.jpg)
![构建不可能的提示：微型工程师](https://cms-assets.youmind.com/media/1766936161835_lznjss_G85rp4UagAEKrWx.jpg)
![构建不可能的提示：微型工程师](https://cms-assets.youmind.com/media/1766936163502_7d5umj_G85rp90agAA0fqL.jpg)

```
A large-scale construction site where tiny {argument name="workers" default="ENGINEERS / BUILDERS"} assemble an oversized {argument name="object" default="EVERYDAY OBJECT"} piece by piece. Scattered components, tools scaled correctly, realistic materials, dramatic worksite lighting.
```

[[Dramatic Lighting]] [[Forced Perspective]] [[Conceptual Photography]]

---

### 127. 戴牛仔帽的小丑数字绘画

**Author**: [Chandan Singh](https://x.com/cbsingh_oo3)  **Date**: 2025-12-24  **Language**: en

> 一个 JSON 提示，用于生成一张高度细致的小丑数字绘画。该提示详细描述了他的经典小丑妆容、狂野的绿色头发和独特的服装：一顶大大的紫色牛仔帽和一件紫色西装外套。风格为油画，具有丰富的纹理、鲜艳的色彩、戏剧性的光线，以及一个黑暗、混乱的抽象背景。

![戴牛仔帽的小丑数字绘画](https://cms-assets.youmind.com/media/1766935990264_nwf1ar_G85nzR4asAANVrM.jpg)

```
{
  "prompt": "A highly detailed digital painting of the Joker in a menacing close-up portrait. He has pale white skin with classic clown makeup: black diamond shapes around his intense yellow-green eyes, a red nose, and an exaggerated wide red smile revealing teeth. His hair is wild, curly, and green-tinted. He wears a large {argument name="hat color" default="purple"} cowboy hat with a wide brim and a green hat band. His outfit consists of a purple suit jacket with a Joker playing card pinned to the lapel, a colorful patterned shirt, and a loose green cravat tie. The background is an abstract, textured blend of warm and cool colors including purples, yellows, oranges, and teals with visible brush strokes and subtle star shapes. Dramatic lighting emphasizes his sinister grin and facial details. Oil painting style with rich textures, vibrant colors, high contrast, and a dark, chaotic atmosphere."
}
```

[[Dramatic Lighting]]

---

### 128. 电影级黑白特写肖像

**Author**: [Anissa](https://x.com/SimplyAnnisa)  **Date**: 2025-12-23  **Language**: en

> 一个用于生成电影级黑白特写肖像的提示，描绘了一位摆出模特姿势的女孩，重点在于戏剧性的灯光、增加的颗粒感，以及优雅地遮住部分脸部的手部姿势。

![电影级黑白特写肖像](https://cms-assets.youmind.com/media/1766673302544_tzv1vl_G83RaoPagAUqNJK.jpg)
![电影级黑白特写肖像](https://cms-assets.youmind.com/media/1766673303989_hi43nv_G83RajHbsAEiMMU.jpg)

```
A black-and-white portrait.
Cinematic style with added grain. The image shows an extreme close-up of half of the girl’s face. She looks directly at the camera, with her skin illuminated. She poses like a model, with her hand raised, elbow resting on her cheek, the hand in a graceful pose. The background is dark.
Only her long hair is visible, partially obscuring her face.
```

[[Dramatic Lighting]] [[Film Grain]] [[Black And White Portrait]]

---

### 129. 崎岖地貌中的电影感时尚大片

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2025-12-23  **Language**: en

> 一个详细的图像生成提示，用于创作一张电影级、高写实度的时尚摄影作品：画面中，模特置身于一个情绪化的多岩石地貌中，光线富有戏剧性，重点突出纹理和氛围。

![崎岖地貌中的电影感时尚大片](https://cms-assets.youmind.com/media/1766673270448_ldo4hw_G80kWO0agAAA5TL.jpg)

```
The model sits on a rock with her legs stretched to the side, against a backdrop of a dramatic dark sky and a rocky landscape, with dense grass and autumn vegetation on both sides. She is wearing a {argument name="sweater color" default="gray"} wool sweater, {argument name="pants color" default="black"} cargo-style pants, and tactical sneakers. The atmosphere of the shot is austere, elegant, and cinematic. Her hair is slightly blowing in the wind. The light is soft and diffused, as if before a storm, creating realistic shadows and emphasizing the rich texture of the fabric. Background: a moody rocky landscape; cinematic lighting, detailed fabric texture, dramatic cloudy sky, autumn palette, 8K realism, professional studio-quality fashion lighting.
```

[[Dramatic Lighting]]

---

### 130. 冰与液混合标志设计

**Author**: [Aleena Amir](https://x.com/aleenaamiir)  **Date**: 2025-12-22  **Language**: en

> 一个用于设计超现实、电影级微距风格 Logo 的提示，该 Logo 视觉上结合了冰冻的冰块和流动的液体元素，强调高对比度和戏剧性照明。此提示可根据具体的品牌名称进行定制。

![冰与液混合标志设计](https://cms-assets.youmind.com/media/1766667266735_qazyrj_G8wsEGJaMAArZ03.jpg)
![冰与液混合标志设计](https://cms-assets.youmind.com/media/1766667266790_im5xty_G8wsEIMb0AA28aL.jpg)
![冰与液混合标志设计](https://cms-assets.youmind.com/media/1766667266991_wukf5r_G8wsEMra4AAwWkA.jpg)
![冰与液混合标志设计](https://cms-assets.youmind.com/media/1766667269069_sb25im_G8wsESQbgAAgm1K.jpg)

```
Design the {argument name="Brand Name" default="[Brand Name]"} logo combining frozen ice and flowing liquid. Contrast between solid crystal ice and glossy fluid sections. High realism, dramatic lighting. Visually striking, cinematic macro style.
```

[[Dramatic Lighting]] [[High Contrast Lighting]] [[Brand Identity]] [[Macro Photography Style]]

---

### 131. 超写实暗黑巫师肖像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2025-12-19  **Language**: en

> 一个详细的提示，用于生成一张超现实的强大黑暗巫师奇幻肖像。它侧重于戏剧性元素，如发光的红色能量法术、电影般的灯光、深邃的阴影以及面部和手部的复杂细节，并特别指示如果使用参考图，则保留原始面部。

![超写实暗黑巫师肖像](https://cms-assets.youmind.com/media/1766238106683_ex1svu_G8i9q1BaEAA42yj.jpg)

```
Hyperrealistic fantasy portrait of a powerful dark sorcerer casting a red energy spell, intense glowing red magical aura swirling around his hand, intricate fiery energy rings in motion, cinematic lighting, dramatic shadows on face, deep focused gaze, rugged masculine features, wearing a dark hooded cloak, moody atmosphere, dark mystical background illuminated by red energy, fine details on hand and face, ultra-detailed textures, dynamic light reflections, 8k resolution, digital art, concept art style, fantasy movie poster, painted realism, volumetric red glow, atmospheric smoke and embers around, epic and powerful composition [keep original face exactly same]
```

[[Dramatic Lighting]] [[Fantasy Character]]

---

### 132. 带纹理细节的矢量化侧面肖像

**Author**: [Harboriis](https://x.com/harboriis)  **Date**: 2025-12-19  **Language**: en

> 一个用于 Nano Banana Pro 的图像生成提示，要求生成一张特写、高细节的肖像，采用矢量化风格，并带有平面、饱和的色块。提示中指定了主体（其面部必须与参考图像匹配）的侧面视图，戴着太阳镜，穿着深色夹克，背景为纯勃艮第红色，并带有戏剧性的右前方照明。

![带纹理细节的矢量化侧面肖像](https://cms-assets.youmind.com/media/1766238159887_2v34v4_G8iHXH2aoAEOz9b.jpg)

```
Close-up, high-detail portrait of an individual (face shape exactly the same as reference) rendered in a vectorized style with flat, saturated color blocking. The individual is in profile, looking right, with a serious expression. They wear small, round black sunglasses pushed down to reveal the eye. Outfit is a dark {argument name="jacket color" default="forest green/teal"} high-collared jacket. Lighting is bright, clean, and dramatic, originating from the front-right, creating sharp, well-defined shadows. Solid deep {argument name="background color" default="burgundy-red"} background instead of teal. High resolution, extreme detail, vertical orientation, clear edges.
```

[[Dramatic Lighting]]

---

### 133. 银行金库劫案场景，配有金色手枪

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2025-12-18  **Language**: en

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

[[Dramatic Lighting]] [[Low Angle Shot]] [[Action Photography]] [[Latex Outfit]]

---

### 134. Gemini Nano Banana 惊艳照片提示词

**Author**: [blogbursthub](https://x.com/blogbursthub)  **Date**: 2025-12-18  **Language**: en

> 这是一个专为 Gemini Nano Banana 模型设计的绝美照片提示词，旨在生成一张高质量、细节丰富的宏伟装甲巨龙图像，置身于戏剧性的奇幻场景中。该提示词强调强烈的灯光、电影般的构图和超现实的风格。

![Gemini Nano Banana 惊艳照片提示词](https://cms-assets.youmind.com/media/1766237960501_o02lab_G8bkSP9aMAAyleI.jpg)

```
A majestic, armored dragon, scales shimmering with metallic iridescence, perched atop a jagged, snow-capped mountain peak. The dragon is bathed in the dramatic, golden light of a setting sun, casting long, sharp shadows. Its eyes glow with an inner fire. Cinematic composition, hyper-detailed, photorealistic, fantasy art, 8k, volumetric lighting, deep focus, dramatic atmosphere.
```

[[Dramatic Lighting]] [[Ultra-Realistic Photography]] [[Cinematic Composition]] [[Fantasy Character]]

---

### 135. 电影级肖像提示：灰度主体与彩色小丑面具

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2025-12-16  **Language**: en

> 一个象征性且富有电影感的 JSON 提示词，用于生成一幅探索二元性和隐藏身份的艺术肖像。该提示词要求严格保留身份特征，同时将灰度主体（沉思、忧郁）与部分遮盖面部的鲜艳小丑式面具形成对比，并运用戏剧性照明和高对比度。

![电影级肖像提示：灰度主体与彩色小丑面具](https://cms-assets.youmind.com/media/1766042191534_b5u8k3_G8TH3kTaMAE3YCi.jpg)

```
{
  "type": "image_generation_prompt",
  "style": "cinematic, symbolic, high-contrast, artistic portrait",
  "theme": "duality and hidden identity",
  "identity_preservation": {
    "use_reference_image": true,
    "alter_face": false,
    "strict_identity_lock": true,
    "notes": "Use the uploaded reference image as a 100% faithful source. Preserve the woman’s exact facial features, proportions, skin texture, and natural appearance without any modification."
  },
  "subject": {
    "gender": "female",
    "appearance": {
      "color_treatment": "grayscale",
      "expression": "thoughtful, melancholic, introspective",
      "visible_eye": "expressive and emotional, conveying inner conflict"
    },
    "pose": {
      "action": "holding a Joker-style clown mask in front of part of her face",
      "hand": {
        "detail": "highly detailed hand, possibly gloved or armored",
        "color_treatment": "grayscale"
      }
    }
  },
  "mask": {
    "type": "Joker-style clown mask",
    "color": "full vibrant color",
    "details": {
      "smile": "bright red exaggerated smile",
      "nose": "red clown nose",
      "eye_markings": "blue markings around the eyes"
    },
    "symbolism": "cheerful, unsettling facade masking a darker inner reality"
  },
  "environment": {
    "background": {
      "style": "dark and minimalistic",
      "purpose": "to emphasize contrast between the grayscale subject and the colorful mask"
    }
  },
  "lighting": {
    "style": "dramatic, cinematic",
    "effects": [
      "strong contrast between light and shadow",
      "focused illumination on face, eye, and mask",
      "subtle falloff into darkness"
    ]
  },
  "color_contrast": {
    "subject": "entirely grayscale",
    "mask": "fully saturated vivid colors",
    "intent": "visual metaphor of duality, identity, and emotional conflict"
  },
  "mood": {
    "atmosphere": "dark, psychological, introspective",
    "tone": "mysterious, symbolic, emotionally charged"
  },
  "quality": {
    "realism": "highly photorealistic",
    "detail_level": "ultra-detailed skin, mask texture, and hand realism",
    "rendering": "cinematic and artistic"
  },
  "output_goal": "Create a striking, ultra-realistic cinematic portrait of a woman expressing duality and hidden identity, using a vivid Joker-style mask contrasted against a grayscale, emotionally subdued reality, while preserving her exact facial identity."
}
```

[[Dramatic Lighting]] [[Editorial Photography]] [[High Contrast]]

---

### 136. 超现实恐怖肖像

**Author**: [KARIM](https://x.com/sat0oshi)  **Date**: 2025-12-14  **Language**: en

> 一个用于超现实、8K 电影概念艺术肖像的详细图像生成提示，具有超现实恐怖美学。它描述了一个年轻男子将自己的脸撕开，露出下面逼真的人类头骨，强调极致的纹理细节、戏剧性的光照和高对比度。

![超现实恐怖肖像](https://cms-assets.youmind.com/media/1765991302520_wke3vf_G8KSt3mXMAEaaS1.jpg)

```
{
  "prompt": "front face shot of Hyper-realistic, cinematic concept art portrait of a young man with black turtle neck and a baclk new era cap pulling the skin of his face apart with both hands, revealing a realistic human skull underneath on the right side of his face. The exposed skin appears stretchy, wet, and visceral, with visible sweat droplets, lifelike skin pores, and extreme texture detail. She has a wide-eyed, intense expression conveying shock and horror. Dramatic, moody cinematic lighting with strong contrast, deep shadows, and a dark, minimal background. Surreal horror aesthetic, macro photography look, ultra-detailed, 8K resolution, photorealistic finish.",
  "negative_prompt": "cartoon, anime, illustration, 3d render, CGI, drawing, painting, blurry, low resolution, low quality, bad anatomy, distorted fingers, extra fingers, deformed hands, mutated face, text, watermark, logo, signature, messy composition",
  "aspect_ratio": "3:4",
  "style": "surreal horror, cinematic, hyper-realistic",
  "quality": "ultra high",
  "resolution": "8k",
  "signature": "{argument name="signature" default="Karim Sat0oshi"}"
}
```

[[Dramatic Lighting]] [[High Contrast]] [[Surrealism]] [[Cinematic Concept Art]]

---

### 137. Moody High-Contrast Portrait with Rim Light

**Author**: [majeokey](https://x.com/majeokey)  **Date**: 2025-12-11  **Language**: en

> A concise Nano Banana Pro prompt for generating a moody portrait of a man leaning against a concrete wall. The prompt emphasizes high contrast, with the body mostly in darkness, and a thin, dramatic diagonal beam of light highlighting the cheekbone and jawline, using cold tones.

![Moody High-Contrast Portrait with Rim Light](https://cms-assets.youmind.com/media/1765967679160_myvoz1_G75MxwTW4AAun8k.jpg)

```
Moody portrait of a man leaning against a concrete wall with his body mostly in darkness. Only a thin diagonal beam of light cuts across his cheekbone and jawline. Dark shirt, dark jeans, subtle highlight on his watch. Heavy contrast, cold tones.
```

[[Dramatic Lighting]] [[Male Portrait]] [[High Contrast Photography]] [[Rim Lighting]]

---

### 138. 电影级人像，搭配戏剧性的红色灯光

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2025-12-11  **Language**: en

> 一个高度结构化的提示，旨在生成一张超现实的 8K 电影级年轻男子肖像。该提示详细说明了拍摄对象的面部特征、衣着、姿势，并着重强调了深哑光红色背景下戏剧性的高对比度红色调照明。

![电影级人像，搭配戏剧性的红色灯光](https://cms-assets.youmind.com/media/1765967640909_tz01sp_G72zSVKbkAEsftV.jpg)

```
{
  "Objective": "Generate an ultra-realistic {argument name="resolution" default="8K"} cinematic portrait of a young man in dramatic {argument name="lighting color" default="red-toned"} lighting.",

  "Subject": {
    "Description": "Young man with a sharp facial structure and tousled dark hair",
    "Wardrobe": {
      "Jacket": "{argument name="jacket color" default="Black"} suit jacket",
      "Shirt": "White shirt, slightly unbuttoned"
    },
    "Pose_Expression": {
      "Posture": "Standing, facing camera",
      "Mood": "Intense, cinematic, confident",
      "Facial_Tone": "Strong defined features emphasized by lighting"
    }
  },

  "Lighting": {
    "Primary_Light": "Dramatic red side light casting bold highlights",
    "Shadow": "Soft black shadow partially covering the face",
    "Mood": "High contrast, powerful, atmospheric intensity"
  },

  "Background": {
    "Color": "Deep matte red",
    "Texture": "Smooth, non-reflective backdrop",
    "Purpose": "Enhances mood and complements lighting contrast"
  },

  "Visual_Style": {
    "Resolution": "Ultra-realistic 8K",
    "Aesthetic": "Cinematic portrait with dramatic lighting interplay",
    "Details": [
      "High clarity skin texture",
      "Defined jawline and hair texture",
      "Subtle color gradation between red light and dark shadows"
    ]
  },

  "Output_Requirements": {
    "Format": "Image",
    "Orientation": "Portrait",
    "Quality": "Editorial-grade, dramatic cinematic realism"
  }
}
```

[[Dramatic Lighting]] [[Male Portrait]] [[High Contrast Photography]]

---

### 139. 超写实漫画肖像的结构化提示词

**Author**: [Abdullah AI](https://x.com/Abdullah__Ai7)  **Date**: 2025-12-09  **Language**: en

> 一个为 Google Gemini/Nano Banana 3 Pro 设计的详细、结构化的 JSON 提示词，旨在生成一张超现实的老年男性漫画肖像。它具体要求夸张的面部特征、戏剧性的光线、正式的着装和极简的工作室背景，重点在于绘画般的真实感和严肃的氛围。

![超写实漫画肖像的结构化提示词](https://cms-assets.youmind.com/media/1765440084247_gvs4ek_G7wfKstaAAAq0dA.jpg)

```
{
  "style": {
    "type": "hyperrealistic caricature",
    "lighting": "soft studio lighting",
    "mood": "serious, dramatic",
    "details": "exaggerated facial proportions, smooth skin texture, painterly realism"
  },
  "subject": {
    "type": "older man",
    "features": {
      "hair": "{argument name=\"hair style\" default=\"light blond, voluminous, swept to the side with dramatic flow\"}",
      "face": "{argument name=\"face features\" default=\"large exaggerated cheeks and chin, deep frown lines, pronounced brows, slightly drooping eyelids\"}",
      "expression": "{argument name=\"expression\" default=\"stern, pouting, serious\"}"
    },
    "clothing": {
      "outfit": "dark formal suit",
      "shirt": "light-colored dress shirt",
      "tie": "{argument name=\"tie color\" default=\"light blue textured tie\"}"
    },
    "pose": "straight posture, facing forward"
  },
  "background": {
    "type": "plain dark gradient",
    "atmosphere": "studio portrait, minimalistic"
  },
  "camera": {
    "angle": "straight-on",
    "depth_of_field": "shallow, soft background",
    "focus": "sharp on
```

[[Dramatic Lighting]] [[Studio Portrait]] [[Exaggerated Features]]

---

### 140. 忧郁大理石半身像肖像

**Author**: [Myluna](https://x.com/monicamoonx)  **Date**: 2025-12-09  **Language**: en

> 一个为 Nano Banana Pro 设计的简洁提示，聚焦于一个富有戏剧性、私密的场景。它描绘了一位红发女子斜倚在一尊古典大理石半身像旁，强调温暖、富有戏剧性的光线，深褐色调，大理石和织物的超现实纹理，置身于一个尘土飞扬的博物馆中，以唤起一种忧郁的情绪。

![忧郁大理石半身像肖像](https://cms-assets.youmind.com/media/1765440143411_qpevzg_G7wZI1pXAAAT1Rt.jpg)
![忧郁大理石半身像肖像](https://cms-assets.youmind.com/media/1765440144476_h8i5bg_G7wZI1oXkAAopKw.jpg)

```
red-haired woman in sheer embroidered ancient dress leaning head against classical marble bust, warm dramatic lighting, dusty museum, sepia tones, intimate melancholic mood, hyper-realistic marble and fabric.
```

[[Dramatic Lighting]] [[Melancholic Mood]] [[Museum Setting]] [[Red Hair Portrait]]

---

### 141. 极简轮廓聚光灯提示与签名

**Author**: [Vivek HY](https://x.com/Vivekhy)  **Date**: 2025-12-09  **Language**: en

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

[[Dramatic Lighting]] [[Minimalist Composition]]

---

### 142. 宇宙灾难停电场景

**Author**: [Saul Goodman](https://x.com/Goodmanprotocol)  **Date**: 2025-12-09  **Language**: en

> 一个超现实、超电影感的提示，用于生成一个末日视觉效果：地球在白昼时突然经历了一秒钟的漆黑停电，所有运动都凝固了，地平线上留下一抹诡异的红色光芒。

![宇宙灾难停电场景](https://cms-assets.youmind.com/media/1765440074991_2pa2i5_G7uU83caEAA54AA.jpg)

```
Earth in broad daylight—but suddenly everything goes completely pitch black for exactly one second, as if the sun itself blinked. People on streets freeze mid-step, their outlines barely visible in the instantaneous darkness. Birds hang motionless in the sky, wings suspended as though reality paused. Rivers and lakes turn perfectly smooth and reflective like black glass mirrors, capturing faint silhouettes. Around the distant horizon, a thin red glow lingers—soft, eerie, unnatural—hinting at something cosmic and catastrophic. Render in hyper-real 16K detail, doomsday visual style, natural camera physics, atmospheric scattering, zero CGI appearance. Photoreal shadows, micro-texture on skin and surfaces, subtle grain, slight lens distortion, chilling documentary realism. Ultra-cinematic, ultra-detailed, surreal but grounded in reality.
```

[[Dramatic Lighting]] [[Cinematic Scene]] [[Surreal Landscape]]

---

### 143. 超逼真闪光自拍犯罪现场提示（JSON 格式）

**Author**: [Daniel](https://x.com/udanielx)  **Date**: 2025-12-08  **Language**: en

> 一个强烈、高度详细的 JSON 提示，用于生成超现实、电影犯罪现场风格的闪光自拍。它指定了极端的相机设置、戏剧性的主题（逃跑新娘遭遇赛博惊悚）、一个被毁坏的顶层公寓环境，以及诸如炫目闪光和深红色紧急灯光等戏剧性照明效果。

![超逼真闪光自拍犯罪现场提示（JSON 格式）](https://cms-assets.youmind.com/media/1765438538836_t1xiss_G7pkGhwWgAAfwg5.jpg)

```
{
  "my_prompt": {
    "core_style": "insane hyper-realistic flash selfie, cinematic crime-scene energy",
    "target_quality": "16K raw photorealism, zero beauty filters",
    "main_rule": "face locked exactly to reference, no softening or reshaping",

    "shot_setup": {
      "type": "mirror selfie in abandoned luxury hotel suite",
      "camera": "iPhone 16 Pro Max, flash cranked to maximum",
      "lens": "24 mm, slight barrel distortion on edges",
      "angle": "phone held high above head, shooting downward (dutch tilt 15°)",
      "framing": "full body + massive cracked mirror reflection, phone dominating foreground"
    },

    "subject": {
      "age": "24-27",
      "vibe": "high-fashion runaway bride meets cyber-thriller",
      "pose": "perched on the edge of a shattered glass coffee table, knees wide, one stiletto dangling off toe, leaning forward aggressively toward mirror, one hand gripping a half-empty champagne bottle by the neck, the other holding phone like a weapon",
      "hair": "long blood-red hair, wet and slicked back on top, loose chaotic waves below, strands stuck to face and neck",
      "outfit": "ripped white silk wedding dress torn to mini length, smeared with real blood and red wine stains, black leather harness over torso, thigh-high patent black boots with broken heel on one side"
    },

    "accessories": [
      "smudged black eyeliner running down cheeks",
      "diamond choker + torn veil hanging from it",
      "bloody fingerprints on champagne bottle",
      "silver ring flash reflecting in eyes"
    ],

    "environment": {
      "location": "trashed penthouse suite at 4 AM",
      "background": "floor-to-ceiling windows showing city skyline at dawn, overturned furniture, shattered mirror wall, rose petals and broken glass everywhere, police caution tape visible through open door",
      "lighting": "only source is dying red EMERGENCY EXIT sign + iPhone flash cutting white-hot through crimson haze"
    },

    "lighting": {
      "main_source": "blinding white flash creating nuclear highlights and pitch-black shadows",
      "ambient": "deep blood-red emergency lighting + faint blue pre-dawn glow from windows",
      "effect": "face lit like an interrogation, red rim light bleeding into hair, reflections in blood puddles"
    },

    "render_details": {
      "skin": "sweat, wine, and blood droplets with real refraction",
      "glass": "microscopic shards catching flash individually",
      "motion": "slight hand shake blur on phone, subject frozen by flash",
      "sensor": "heavy noise, lens flare streaks, crushed blacks"
    },

    "negative": [
      "cute, soft, clean",
      "smiling",
      "studio lighting",
      "anime/cartoon",
      "perfect skin",
      "intact dress",
      "daylight"
    ]
  }
}
```

[[Dramatic Lighting]] [[Flash Photography]]

---

### 144. 高端产品影棚照片提示词

**Author**: [Louis Gleeson](https://x.com/aigleeson)  **Date**: 2025-12-08  **Language**: en

> 一个高质量、可用于生产的 Nano Banana Pro 图像提示，专门用于生成一张戏剧性、高端的影棚产品照片，置于湿润反光表面上，并带有电影级灯光和霓虹点缀。

![高端产品影棚照片提示词](https://cms-assets.youmind.com/media/1765438634608_y0pqa9_G7o-1gWaYAAnlVC.jpg)

```
Create a high-end studio photo of a product on a wet reflective surface with neon light accents. Sharp edges, cinematic contrast.
```

[[Dramatic Lighting]] [[Product Photography]] [[Reflective Surface]]

---

### 145. 史诗级冰冻悬崖战士场景

**Author**: [Saul Goodman](https://x.com/Goodmanprotocol)  **Date**: 2025-12-07  **Language**: en

> 一个高度详细、超现实的 Nano Banana Pro 在 Gemini App 上的提示，描述了一名孤独的战士在冰冻的悬崖上，面对即将到来的暴风雪，强调戏剧性的光线、冷蓝色高光以及雪、霜和冰等纹理的极致细节。

![史诗级冰冻悬崖战士场景](https://cms-assets.youmind.com/media/1765421913276_70gut7_G7lIkYraIAAbpwE.jpg)

```
A lone warrior stands at the edge of a frozen cliff as the first storm of winter approaches — icy winds tearing through his cloak, snow swirling violently around him. The sky is a dark steel-grey, heavy with an unstoppable blizzard rolling in like a wall of white fury. Frost clings to his beard, his armor, his breath visible in the freezing air. The landscape below is a vast frozen valley with shattered trees, frozen rivers, and distant mountains disappearing into the storm. Ultra-realistic textures: every snowflake sharp, every gust of wind visible, every crack of ice detailed. Dramatic lighting: cold blue highlights, deep shadows, glowing white reflections off the ice. Atmospheric, epic, heavy mood — the world preparing for something powerful and inevitable. Cinematic realism at its peak.
```

[[Dramatic Lighting]]

---

### 146. 电影街头肖像 (JSON)

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2025-12-07  **Language**: en

> 一个详细的 JSON 提示，旨在创作一幅电影感十足、情感丰富的街头肖像，采用 Midjourney 的写实风格，聚焦于一个清晰的主体，背景是模糊移动的人群，并运用戏剧性的焦外虚化和温暖的街头色调。

![电影街头肖像 (JSON)](https://cms-assets.youmind.com/media/1765421919268_zx65t9_G7kjjXzbQAA9JFi.jpg)

```
{
  "Objective": "Create a cinematic, emotionally resonant AI-generated street portrait reminiscent of Midjourney's realism, suitable for a final slide in a storytelling carousel.",

  "Narrative_Caption": {
    "Primary_Text": "In a crowd full of motion, the ones who stand still make the loudest noise. 🎞✨",
    "Description": "A cinematic realism aesthetic created in Midjourney—alive with emotion, where every face feels like a story waiting to be told."
  },

  "Visual_Style": {
    "Theme": "Midjourney cinematic realism",
    "Mood": "Moody, emotional, atmospheric",
    "Lighting": "Soft, filmic contrast with dramatic bokeh depth",
    "Color_Palette": "Warm street tones mixed with urban neutrals",
    "Depth": "Strong depth-of-field, blurred crowds, sharp subject",
    "Texture": "High-detail realism highlighting expressive facial textures"
  },

  "Scene_Description": {
    "Setting": "Urban street environment filled with movement and diverse people",
    "Atmosphere": "Busy crowd where a single still figure creates visual tension and narrative contrast",
    "Composition": "Bokeh-heavy crowd motion with one calm subject anchoring the frame"
  },

  "Aesthetic_Tags": [
    "midjourney",
    "cinematic realism",
    "ai photography",
    "emotional street portrait",
    "traveler aesthetic",
    "urban crowd art",
    "bokeh depth shot",
    "storytelling image",
    "realistic ai portrait",
    "creative ai generation",
    "moody cinematic visual",
    "viral ai post",
    "travel inspired realism",
    "ai storytelling composition"
  ],

  "Output_Requirements": {
    "Use_Case": "Carousel last slide caption, cinematic AI-art showcase, storytelling post",
    "Format": "Image or caption metadata",
    "Style": "Cinematic, narrative-driven, emotionally resonant"
  }
}
```

[[Dramatic Lighting]] [[Bokeh Background]] [[Cinematic Street Portrait]] [[Emotional Photography]]

---

### 147. 博物馆级世界遗产立体模型生成器

**Author**: [Maki@Sunwood AI Labs.](https://x.com/hAru_mAki_ch)  **Date**: 2025-12-07  **Language**: ja

> 这是一个为 Nano Banana Pro 设计的综合系统提示，用于根据提供的坐标生成一个巨大、高度精细、博物馆级别的世界遗产或著名地标立体模型图像。该提示指示 AI 扮演立体模型建筑大师的角色，强调比例、历史诠释、戏剧性照明，并包含一个参照人物以突显模型的巨大尺寸。

```
あなたは国立博物館の展示を手掛ける**「マスター・ジオラマ・アーキテクト（建築模型士）」**です。
最後に提供される入力テキスト（緯度・経度）を解析し、その地点にある世界遺産やランドマークを再現した**「博物館展示クラスの超巨大・高精細ジオラマ」**の画像を生成してください。

その際、添付された参照画像のキャラクターを、**「ジオラマを見学している観光客、または模型を修復中の巨人サイズの職人」**として配置し、ジオラマのスケール感（大きさ）を引き立たせてください。

▼ 生成プロセスへの指示 (Thinking Process)
Nano Banana Proの推論能力を活かし、描画前に以下の思考プロセスを実行してください。

1.  *[ステップ1: 地理的特定と歴史的解釈]*: 入力された緯度・経度が示す「世界遺産」や「著名な都市景観」を特定してください。その場所の建築様式（ゴシック、和風、古代遺跡など）や、自然環境（ジャングル、砂漠、断崖）の特徴を深く分析します。
2.  **[ステップ2: スケールの拡張]**: 前回の小さな箱庭とは異なり、周辺環境（周囲の森、参道、都市のスカイライン）まで含めた広大な範囲を切り取ってください。数千人の群衆（ミニチュアの人々）や、細かい樹木を配置し、圧倒的な密度感を演出します。
3.  **[ステップ3: ミュージアム演出]**: 博物館の照明（スポットライト）をシミュレートし、重厚感のある台座の上に設置します。現実の風景そのものではなく、「究極にリアルな模型」としての質感（塗装の剥げ、素材の質感）を追求してください。

▼ デザイン・スタイル指定
* *構図・レイアウト*: 広角レンズを使用した、ダイナミックな俯瞰視点（バードアイ）。全体を見渡しつつ、中心の遺産が際立つ構図。
* **テイスト**: プロフェッショナルな建築模型写真。極めて高いディテール、ドラマチックな陰影、埃っぽさや経年変化（ウェザリング）の表現。
* *テキスト*: 台座の重厚な金属プレートに、**「遺産の名称（英語/現地語）」**と**「建設年または登録年」**を、明朝体やセリフ体で優雅に刻印してください。
* **キャラクター**: 参照キャラクターを配置し、ジオラマとの対比で「模型の巨大さ」または「模型の精巧さ」を強調する演出を行う。

▼ 入力テキスト
{argument name="緯度・経度" default="13.1631° S, 72.5450° W"}
```

[[Dramatic Lighting]] [[Miniature Architecture]]

---

### 148. Gemini App 超逼真电影级板球场景提示词

**Author**: [Saul Goodman](https://x.com/Goodmanprotocol)  **Date**: 2025-12-07  **Language**: en

> 这是一个为 Gemini App（Lyra 风格）设计的详细、超现实图像生成提示，旨在创作一个来自灰烬杯板球系列赛的电影化瞬间。它着重捕捉投球手和击球手之间紧张对峙的画面，强调戏剧性的光线、纹理细节（汗水、泥土、磨损的球场）以及旋转红球上的运动模糊，以传达板球对抗赛的原始坚韧和高风险。

![Gemini App 超逼真电影级板球场景提示词](https://cms-assets.youmind.com/media/1765421903090_b09hpa_G7jnThHa4AEZDmU.jpg)

```
A hyper-realistic, cinematic moment from the Ashes cricket series — an intense face-off between bowler and batsman under dramatic stadium floodlights. Fine dust and ashes float in the air like glowing embers. The pitch shows worn cracks and scattered grass fragments, capturing the brutality of Test cricket. Players’ jerseys have realistic sweat textures, dirt stains, and creases. The red ball spins mid-air with visible seam detail, motion blur, and shallow depth of field. Crowd in the background slightly defocused, but stadium lights flare with photorealistic bloom. Cool-toned shadows contrast with warm stadium lights for a gritty, high-stakes atmosphere. Wind sweeps light dust across the pitch. Capture tension, realism, and raw grit of elite cricket.

---

Parameters (Lyra Style)

{
  "style": "ultra-realistic",
  "resolution": "8K",
  "ratio": "16:9",
  "camera": {
    "angle": "low-angle action shot",
    "lens": "telephoto (200mm)",
    "shutter_speed": "1/2000",
    "depth_of_field": "shallow",
    "focus": "sharp on red cricket ball mid-air"
  },
  "lighting": {
    "type": "stadium floodlights",
    "contrast": "high",
    "mood": "tense, dramatic",
    "color_palette": ["cool shadows", "warm highlights", "red ball emphasis"]
  },
  "environment_details": {
    "stadium": "MCG / Lords atmosphere",
    "weather": "dry dust with drifting ashes",
    "crowd": "blurred, realistic silhouettes",
    "background": ["light flares", "stadium banners", "scoreboard glow"]
  }
}
```

[[Dramatic Lighting]] [[Motion Blur]]

---

### 149. 用于复制主体外观的肖像提示

**Author**: [D. Humann](https://x.com/dhumann)  **Date**: 2025-12-07  **Language**: en

> 一个详细的肖像提示，旨在精确复制上传主体的面部特征和外貌，将其置于特定的工作室环境中，并采用戏剧性的明暗对比照明。

![用于复制主体外观的肖像提示](https://cms-assets.youmind.com/media/1765438507436_19c8dp_G7i1uvta8AAdTg2.jpg)

```
The main subject is the person in the attached photo (hereinafter referred to as THE_SUBJECT). Carefully and accurately replicate THE_SUBJECT’s facial features, hairstyle, skin tone, proportions, and overall appearance exactly as shown in the reference photo. Dark magenta studio infinite background; THE_SUBJECT is sitting on a metal folding chair, legs crossed in a relaxed lean, arm on backrest, face looking back in the opposite direction; lighting is soft and minimal with a chiaroscuro mood creating dynamic light and shadow areas. Blue light from the left. Pink light from the right.
```

[[Dramatic Lighting]] [[High Contrast Lighting]] [[Studio Photography]]

---

### 150. 黑白肖像生成提示

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2025-12-07  **Language**: en

> 一个详细的图像生成提示，旨在创建一幅戏剧性、高质量的黑白肖像。它指定了从上方角度拍摄的面部特写，展现出骄傲的表情，采用 35mm 镜头美学，并使用深黑色阴影背景，以将焦点完全集中在拍摄对象的面部、上胸部和肩部。

![黑白肖像生成提示](https://cms-assets.youmind.com/media/1765421863680_xstlg3_G7ibiq9bEAE3KXl.jpg)

```
Generate a top-angle and close-up black and white portrait of my face, focused on the head facing forward. Use a {argument name="lens look" default="35mm"} lens look, {argument name="quality" default="10.7K 4HD"} quality. {argument name="expression" default="Proud"} expression. Deep black shadow background - only the face, the upper chest, and the shoulder.
```

[[Dramatic Lighting]] [[35mm Lens]] [[High Contrast Shadow]]

---

### 151. 广告食品摄影中的动态凝结技巧

**Author**: [Nano Banana Pro](https://x.com/NanoBanana)  **Date**: 2025-12-07  **Language**: en

> 这是一个用于使用 Nano Banana Pro 创作高分辨率、广告风格美食摄影的提示模板。它包含两个主体，一个摆放在质朴的桌面上，另一个悬浮在上方，同时捕捉到第一个主体飞溅的瞬间。该模板指定了选择性柔焦、用于文本的干净留白以及戏剧性的灯光效果。

![广告食品摄影中的动态凝结技巧](https://cms-assets.youmind.com/media/1765990908590_iph7d1_G7hnikwWwAEjlEP.jpg)

```
Advertising-style food photography of {argument name="subject 1" default="[subject 1]"} arranged on a rustic table, with {argument name="subject 2" default="[subject 2]"} floating above in mid-air and a splash of {argument name="subject 1 repeat" default="[subject 1]"} frozen in motion. High-resolution photo manipulation with selective soft focus, clean negative space for text, dramatic lighting, and crisp detail.
```

[[Dramatic Lighting]] [[Food Advertising Photography]]

---

### 152. 电影级 3D 标志，自动分配纹理

**Author**: [Kris Kashtanova](https://x.com/icreatelife)  **Date**: 2025-11-22  **Language**: en

> 一个用于生成电影级 3D 标志的提示，其中 AI 会根据品牌风格选择逼真的纹理，并带有戏剧性的灯光和产品广告的感觉。

![电影级 3D 标志，自动分配纹理](https://cms-assets.youmind.com/media/1763885708637_4kfc88_G6WCcaKWYAAc2oH.jpg)
![电影级 3D 标志，自动分配纹理](https://cms-assets.youmind.com/media/1763885710942_3vh3ht_G6WCcaXWMAEAcnS.jpg)
![电影级 3D 标志，自动分配纹理](https://cms-assets.youmind.com/media/1763885713621_w5wm5e_G6WCcaWXwAE3TpL.jpg)
![电影级 3D 标志，自动分配纹理](https://cms-assets.youmind.com/media/1763885716719_yxkd1w_G6WClZeXwAARoPn.jpg)

```
Create a cinematic 3D logo for {argument name="brand" default="[BRAND]"}
Automatically assign a realistic texture (glass, fire, neon, chrome, liquid, ice, lava, wood, or cloud) based on the brand style.
Use dramatic lighting, depth of field, and a soft glowing background.
Style: product ad / reveal shot, cinematic tone, ultra HD.
```

[[Dramatic Lighting]] [[Product Advertisement]] [[Brand Identity]]

---

### 153. 儿童时尚专题双联画提示词

**Author**: [Cherry 2.O](https://x.com/Mind_Boticni)  **Date**: 2026-04-09  **Language**: en

> 一份用于生成蓝色背景下儿童时尚专题双联画的详细提示词，描述了两个具有特定服装、配饰和插画元素的独特场景。

![儿童时尚专题双联画提示词](https://cms-assets.youmind.com/media/1776096294652_w1ie9o_HFeDJGfbMAA5clB.jpg)

```
A children's fashion editorial diptych against a blue background. The left panel shows a joyful child in a navy rashguard and mint shorts, wearing sandals and goggles around their neck, with cartoon chalk water splashes. The right panel shows a child in a white rashguard and navy shorts looking down at their yellow water shoes near an illustrated stream, rocks, and a red crab.
```

[[Editorial Photography]]

---

### 154. 成熟男士高端杂志风肖像

**Author**: [Jahan Zaib](https://x.com/jzaib4269)  **Date**: 2026-04-02  **Language**: en

> 这是一份针对 Gemini Nano Banana Pro 的详细图像生成提示词，旨在创作一张高分辨率、具有电影质感的成熟男士杂志风肖像，涵盖了服装、发型、光影及背景细节。

![成熟男士高端杂志风肖像](https://cms-assets.youmind.com/media/1775198515668_t4r5sc_HE6FKaxaoAA91bS.jpg)
![成熟男士高端杂志风肖像](https://cms-assets.youmind.com/media/1775198515689_9zmnvo_HE6FKf5bkAAuqg4.jpg)
![成熟男士高端杂志风肖像](https://cms-assets.youmind.com/media/1775198515657_uchi33_HE6FKjuWQAAqG4p.jpg)

```
A high-end editorial portrait of a mature man in his 60s with a warm, beaming smile. He has thick, swept-back salt-and-pepper hair, a well-groomed stubble beard, and character lines around his eyes. He is wearing a tailored {argument name="clothing color" default="olive green"} linen blazer over a white scoop-neck shirt and a silver chain necklace. The lighting is soft and cinematic with a warm golden glow, set against a blurred, sophisticated interior background. Shot in high resolution with a shallow depth of field.
```

[[Editorial Photography]] [[High Resolution Portrait]] [[Cinematic Quality]]

---

### 155. 赛博朋克风格人像，霓虹灯光效

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-03-21  **Language**: en

> 一个用于生成戴着圆框眼镜的沉思男士的超现实电影感肖像的提示，强调戏剧性的霓虹灯光（蓝色和洋红色/紫色调）和赛博朋克美学。该提示指定了侧面特写、清晰的面部细节、自然的皮肤纹理和编辑摄影风格。

![赛博朋克风格人像，霓虹灯光效](https://cms-assets.youmind.com/media/1774161427198_11tl5z_HD5cvaOXMAAEWh-.jpg)

```
Ultra-realistic cinematic portrait of a thoughtful man wearing round glasses, side profile close-up, dramatic neon lighting with contrasting blue and magenta/purple tones, soft gradient background blending colors, moody atmosphere, sharp facial details with natural skin texture, subtle shadows, shallow depth of field, studio lighting, cyberpunk aesthetic, high contrast, 8K, editorial photography style.
```

[[Editorial Photography]] [[Cyberpunk Aesthetic]] [[Round Glasses]]

---

### 156. Kling 3.0：从 Nano Banana Pro 图像生成视频

**Author**: [空想写真家](https://x.com/KusoPhoto)  **Date**: 2026-03-16  **Language**: ja

> 这条推文描述了一个工作流程：四张由 Nano Banana Pro 生成的图片被用作 Kling 3.0 Omni 视频生成的输入。所提供的提示是一个电影化的描述，用于图片和视频生成，但由于图片是首先生成的，因此这被提取为 Nano Banana Pro 的提示。

![Kling 3.0：从 Nano Banana Pro 图像生成视频](https://cms-assets.youmind.com/media/1773729531515_h12dt6_HDgEGPGbcAA0lSN.jpg)

```
シネマティックで温かみのあるフィルム調の映像。自然光と浅い被写界深度の中、女性が日記を書く静かな時間を描く。ノートを開く手元、紙を走るペン先のクローズアップ、ふと見せる柔らかな微笑み、そしてノートを閉じるまでの繊細な所作を捉え、親密で情緒的な雰囲気を表現する。
```

[[Editorial Photography]] [[Image-to-Video Workflow]] [[Kling Video Generation]]

---

### 157. 奢华座驾与山地风情编辑精选

**Author**: [Synthia](https://x.com/AIwithSynthia)  **Date**: 2026-03-14  **Language**: en

> 以下是生成一张时尚编辑图片的提示：一位时尚年轻女性（基于上传的面部）坐在一辆哑光红色豪华跑车上，置身于风景优美的山路上。画面中融入了红玫瑰、优雅的黑色缎面服装和一杯麦当劳冰饮，以营造奢华与休闲元素的对比。此图片使用 Nano Banana Pro 创建。

![奢华座驾与山地风情编辑精选](https://cms-assets.youmind.com/media/1773556645559_ho2zmg_HDYQTuLbwAA8jhJ.jpg)

```
A stylish young woman with the uploaded image face, wearing an elegant black satin outfit and trendy sunglasses, sits confidently on the back of a matte red luxury sports car parked on a scenic mountain road. Red roses are scattered across the car’s trunk and spoiler, creating a romantic cinematic aesthetic. She holds a McDonald’s iced drink toward the camera as if offering it, with a McDonald’s paper bag and another drink beside her. Moody cloudy mountains in the background, soft cinematic lighting, fashion editorial photography style, shallow depth of field, ultra-realistic, luxury lifestyle vibe.
```

[[Editorial Photography]] [[Outdoor Lifestyle Portrait]]

---

### 158. 电影场景：国际妇女节快乐

**Author**: [Synthia](https://x.com/AIwithSynthia)  **Date**: 2026-03-08  **Language**: en

> 生成一个超现实电影场景的提示：一位快乐的女性将气球放飞到空中，气球组成“Happy Women’s Day”字样，强调充满活力的节日氛围和编辑摄影的细节。

![电影场景：国际妇女节快乐](https://cms-assets.youmind.com/media/1773038303652_wk5r5m_HC5XyY-aMAE9nlL.jpg)

```
ltra-realistic cinematic scene of a joyful woman standing in an open plaza releasing dozens of purple, gold, and white balloons into the sky forming the words “Happy Women’s Day”, bright sunlight, confetti floating in the air, vibrant festive atmosphere, editorial photography, 8k detail.
```

[[Editorial Photography]]

---

### 159. 奢华时尚编辑肖像与背部项链

**Author**: [gauche](https://x.com/gaucheai)  **Date**: 2026-02-25  **Language**: en

> 一个高度详细的提示，用于生成一张高端奢华时尚编辑照片，作为情人节营销活动的一部分。照片中，一位年轻女性身着红色丝绸吊带裙，佩戴精致的金色背链，置身于华丽的巴黎室内。

![奢华时尚编辑肖像与背部项链](https://cms-assets.youmind.com/media/1772087649636_i1s5nw_HCAtCj7WEAAZgQo.jpg)
![奢华时尚编辑肖像与背部项链](https://cms-assets.youmind.com/media/1772087649533_w4kmcp_HCAtBDqWYAAUSao.jpg)

```
High-end luxury fashion editorial photograph, Parisian haute couture Valentine's Day campaign, Vogue Paris romantic glamour aesthetic, fine jewelry brand advertisement quality. Young woman mid-20s sitting on ornate antique French Louis XV style gilded armchair, body positioned at three-quarter angle with back toward camera, torso elegantly twisted looking back over right shoulder toward camera creating classic over-the-shoulder pose, seated on edge of chair cushion with weight resting on right hip, legs crossed at knees with left leg crossed over right leg, legs angled toward left side of frame, left arm bent at elbow with left hand raised gracefully near left side of face and neck in delicate feminine gesture with fingers softly curled near jawline, right arm relaxed downward at side resting gently on chair seat, head turned looking back over right shoulder with chin slightly lowered, soft subtle enigmatic smile with lips gently parted, direct eye contact with camera through slightly lowered lashes creating sultry elegant alluring gaze, spine elongated with graceful poised posture, bare back fully visible with shoulder blades subtly defined. Dark rich chocolate brown hair medium length falling just past shoulders, soft loose romantic waves with natural movement and volume, side parted on left with hair flowing down naturally, some strands falling forward over right shoulder, healthy glossy shine. Fair to medium olive skin tone with warm golden undertone, natural radiant luminous complexion, subtle peachy-pink flush on cheeks, defined natural brows with soft elegant arch, warm brown smoky eyeshadow with subtle champagne shimmer on lids, black volumizing mascara on lashes, nude-mauve pink lips with soft satin finish, small delicate crystal drop earrings visible on ear. Wearing elegant red silk satin mini slip dress in vibrant true red scarlet color, thin delicate spaghetti straps over shoulders, very low-cut dramatic open back plunging down to lower back waist level revealing entire bare back, smooth bias-cut draped fabric skimming body curves elegantly, mini length hemline ending at upper thigh, luxurious lustrous silk fabric catching and reflecting light beautifully. Sheer black semi-transparent pantyhose tights on legs creating elegant hosiery look. Exquisite delicate gold back necklace body chain jewelry draped artfully across bare back, multiple thin fine gold chains cascading in layered swooping draped design, chains connecting at both shoulders near dress straps and draping down across spine in elegant chandelier swag pattern, small sparkling crystal or diamond teardrop pendant drops hanging from chains at various points creating sophisticated decorative effect across entire back, high-end fine jewelry piece. Opulent luxurious Parisian palace interior setting, ornate French Rococo Baroque style classical decor, walls painted
```

[[Editorial Photography]] [[Gold Jewelry]]

---

### 160. Red Studio 时尚专题：动态回声效果

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-23  **Language**: en

> 一个高度结构化的 JSON 提示，用于生成一张身穿黑色燕尾服的男士高级时装影棚肖像。关键特征是“动态回声”效果，在纯深红色无缝背景下，为主体创建 2-3 个半透明、偏移的拖影副本，以实现高对比度、光泽的编辑效果。

![Red Studio 时尚专题：动态回声效果](https://cms-assets.youmind.com/media/1771915002874_n5wyjd_HB3SrFcXYAAV9ik.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "task_type": "studio_fashion_editorial_motion_echo_portrait",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_RED_STUDIO_TUX_MOTION_ECHO"
    },
    "input": {
      "mode": "text_to_image",
      "notes": "Create a high-fashion studio portrait of a stylish adult man in a classic black tuxedo with a bow tie and white pleated shirt. Solid deep-red seamless backdrop and red floor, monochrome red environment. Subject is leaning/sitting in a relaxed pose with one hand slightly raised near the face (fingers softly bent), the other hand resting lower near the waist. Add a strong multi-exposure / motion-echo effect: 2–3 translucent offset duplicates trailing to the right, like a long-exposure movement smear. Keep the main face sharp and dominant, with the echoes softer and semi-transparent. Lux editorial retouching, crisp fabric texture, subtle skin texture, cinematic contrast. Clean image: no text, no logos, no watermark."
    },
    "output": {
      "aspect_ratio": "4:5",
      "resolution": "ultra_high",
      "num_images": 1,
      "sharpness": "editorial_crisp",
      "grain": "subtle_analog"
    },
    "scene": {
      "environment": "studio cyclorama seamless backdrop, fully red, minimal set",
      "lighting": {
        "style": "hard studio key + subtle fill",
        "key_light": "beauty dish or small softbox slightly above eye level, forward-left",
        "fill": "very light fill to keep shadows readable",
        "rim": "faint rim to separate tux from red background",
        "look": "high contrast, glossy editorial finish"
      },
      "camera": {
        "shot_type": "3/4 portrait",
        "angle": "slightly above eye level",
        "lens_look": "85mm portrait compression",
        "depth_of_field": "medium shallow, face tack sharp"
      },
      "color_grade": {
        "palette": "dominant deep reds, true blacks, clean whites",
        "contrast": "high",
        "highlights": "controlled",
        "skin_tone": "natural but slightly warm under red bounce"
      }
    },
    "subject": {
      "person": "adult man",
      "appearance": {
        "hair": "short, styled, slightly tousled",
        "facial_hair": "short beard/stubble, well-groomed",
        "expression": "serious, confident gaze to camera"
      },
      "wardrobe": {
        "tuxedo": "black tuxedo jacket, sharp lapels",
        "shirt": "white pleated dress shirt",
        "bow_tie": "black bow tie",
        "pocket_square": "white pocket square",
        "accessories": "watch on wrist, subtle ring if desired"
      },
      "pose": {
        "body": "leaning/sitting with torso angled slightly",
        "hands": "one hand lifted near face, other hand lower near waist",
        "motion": "capture implied movement for multi-exposure echo"
      }
    },
    "effects": {
      "motion_echo": {
        "enabled": true,
        "echo_count": 3,
     }
```

[[Editorial Photography]] [[Deep Red Background]]

---

### 161. 赛博朋克高定时装肖像提示词

**Author**: [Shah](https://x.com/ai_with_shah)  **Date**: 2026-02-09  **Language**: en

> 一个结构化的提示模板，旨在生成超现实、时尚赛博朋克风格的肖像，适合用于社论或网红视觉内容，特点是情绪化的双色调照明和特定的主体细节。

![赛博朋克高定时装肖像提示词](https://cms-assets.youmind.com/media/1770706257816_fldu3z_HAt-ZRba4AE5g8e.jpg)
![赛博朋克高定时装肖像提示词](https://cms-assets.youmind.com/media/1770706257770_rg4542_HAt-ZSCb0AAeSpO.jpg)
![赛博朋克高定时装肖像提示词](https://cms-assets.youmind.com/media/1770706258144_fw3022_HAt-ZM9aMAAB0eq.jpg)
![赛博朋克高定时装肖像提示词](https://cms-assets.youmind.com/media/1770706259812_4nyu1d_HAt-ZRgbYAAHLzX.jpg)

```
{ "meta": { "purpose": "High-fashion cyberpunk portrait for editorial or influencer visuals", "style": "Cinematic hyper-realistic, moody dual-tone lighting, 8K resolution" }, "subject": { "description": "{argument name="subject description" default="Person with wet dark tousled hair"}", "expression": "{argument name="expression" default="Direct gaze, subtle intensity"}", "makeup": "{argument name="makeup" default="Graphic eyeshadow in metallic blues"}", "hair": "{argument name="hair style" default="Partially covering face"}", "attire": "{argument name="attire" default="Sleek metallic top"}" }, "effects": { "visor": "{argument name="visor effect" default="Glowing horizontal neon orange light bar across eyes"}", "lighting": "cool teal shadows contrasted with warm orange glow" }, "composition": { "angle": "{argument name="angle" default="Low angle looking up"}", "framing": "close-up portrait", "depth_of_field": "soft bokeh" }, "technical_specs": { "quality": "hyper-realistic skin textures, edgy cyberpunk editorial", "aspect_ratio": "1:1" }, "negative": ["blurry", "overexposed", "cartoonish", "low detail"] }
```

[[Editorial Photography]]

---

### 162. 斯堪的纳维亚室内楼梯的编辑肖像

**Author**: [Kaila](https://x.com/kaila3535)  **Date**: 2026-02-06  **Language**: en

> 一张写实照片的提示，用于拍摄一张社论照片，内容是一位年轻女性坐在白色室内楼梯上，置身于简约、现代的斯堪的纳维亚风格室内。强调柔和的自然日光、简洁的构图、高细节以及柔和的皮肤纹理。

![斯堪的纳维亚室内楼梯的编辑肖像](https://cms-assets.youmind.com/media/1770446066519_i5himz_HAdBN0PXwAE9HSE.jpg)

```
{
  "prompt": "a young woman with long straight dark hair, green eyes sitting on white indoor stairs, soft natural daylight from a large window, minimal modern interior with white bookshelves in the background, calm and confident expression, slightly parted lips, one hand touching her face, beige fitted t-shirt with subtle text, black and white plaid pants, casual yet elegant aesthetic, Scandinavian interior style, clean composition, shallow depth of field, ultra realistic, high detail, soft skin texture, natural makeup, editorial photography",
  "negative_prompt": "overexposed, harsh shadows, exaggerated makeup, distorted face, extra fingers, bad anatomy, low resolution, blurry, artificial lighting, heavy retouching",
  "style": "photorealistic",
  "lighting": "soft natural window light",
  "camera": {
    "type": "DSLR",
    "lens": "35mm",
    "aperture": "f/2.8",
    "angle": "slightly low angle"
  },
  "resolution": "1024x1024",
  "quality": "high",
  "seed": 42
}
```

[[Editorial Photography]] [[Soft Natural Daylight]] [[Minimalist Modern Interior]] [[Clean Composition]]

---

### 163. 超逼真高对比度室内肖像提示

**Author**: [Minhaa](https://x.com/tabu_8114)  **Date**: 2026-02-05  **Language**: en

> 一个用于生成逼真的提示词，描绘了一位酷似安娜·德·阿玛斯（Ana de Armas）的女性，她坐在一张豪华的白色沙发上，呈现出率真、俏皮的肖像。该提示词强调了强烈的自然光、高对比度和深阴影，以营造出戏剧性而优雅的室内场景，重点突出拍摄对象的服装和俏皮的表情。

![超逼真高对比度室内肖像提示](https://cms-assets.youmind.com/media/1770359960044_39wi1s_HAYmF13bcAEPYX-.jpg)
![超逼真高对比度室内肖像提示](https://cms-assets.youmind.com/media/1770359960020_elm4cv_HAYmFm_aEAA7H1z.jpg)
![超逼真高对比度室内肖像提示](https://cms-assets.youmind.com/media/1770359960019_6pa32e_HAYmFz2bEAABtY5.jpg)

```
{
  "image": {
    "general": {
      "style": "photorealistic",
      "mood": "candid, playful",
      "lighting": {
        "type": "natural",
        "intensity": "harsh",
        "effect": {
          "high_contrast": true,
          "highlights": {
            "intensity": "strong",
            "focus": "on the subject and couch"
          },
          "shadows": {
            "intensity": "deep",
            "focus": "on the subject, couch"
          }
        }
      },
      "image_ratio": "3:4"
    },
    "scene": {
      "location": {
        "type": "indoor",
        "style": "modern living room",
        "elements": {
          "sofa": {
            "type": "plush",
            "color": "white",
            "texture": "soft, luxurious"
          },
          "lighting_source": {
            "type": "sunlight",
            "direction": "streaming from a large window",
            "effect": "bright and direct"
          },
          "room_features": [
            "minimalistic decor",
            "large windows",
            "open space with natural light"
          ]
        }
      }
    },
    "subject": {
      "identity": {
        "name": "{argument name="subject name" default="Ana de Armas"}",
        "age_range": "mid-20s to early 30s",
        "characteristics": [
          "Latin descent",
          "light skin",
          "youthful appearance"
        ]
      },
      "physical_appearance": {
        "hair": {
          "color": "brown",
          "texture": "wavy",
          "length": "long",
          "style": "high pigtails",
          "details": "loose strands around the face"
        },
        "eyes": {
          "expression": "playful",
          "focus": "winking at the camera"
        },
        "facial_expression": {
          "emotion": "playful",
          "details": "slight smile with a wink"
        },
        "body_type": {
          "build": "slender",
          "focus": "natural curves"
        }
      },
      "outfit": {
        "top": {
          "type": "corset-style",
          "color": "black",
          "details": "fitted design accentuating the figure"
        },
        "bottom": {
          "type": "mini dress",
          "fit": "tight",
          "material": "stretch fabric"
        },
        "style": "elegant yet casual"
      },
      "pose": {
        "body_position": "seated",
        "position_details": {
          "sitting": "on a white plush sofa",
          "legs": "crossed at the knees",
          "arm_position": "one arm resting on the sofa, the other holding a strand of hair"
        },
        "facial_focus": "winking and playful expression",
        "gesture": "subtle motion, holding hair with one hand, the other hand resting casually on the sofa"
      }
    },
    "visual_effects": {
      "lighting_effects": {
        "shadows": {
          "depth": "deep",
          "focus": "on the figure and sofa, creating a dramatic effect"
        },
        "highl
```

[[Editorial Photography]] [[Playful Expression]] [[Luxury Interior]]

---

### 164. 身穿人造皮草大衣的超时尚杂志肖像照

**Author**: [Kashberg](https://x.com/Kashberg_0)  **Date**: 2026-02-05  **Language**: en

> 生成一张超时尚的杂志肖像照的提示词：一位自信的女模特，身着奢华的冰蓝色仿皮草大衣，坐在一张超大号的纹理皮草扶手椅中。照片背景为深色、情绪化的影棚，采用柔和的电影级灯光，并以 85mm 镜头呈现《Vogue》/《Harper’s Bazaar》的审美风格。

![身穿人造皮草大衣的超时尚杂志肖像照](https://cms-assets.youmind.com/media/1770359902846_9qe2io_HAXbK9NasAAchuG.jpg)
![身穿人造皮草大衣的超时尚杂志肖像照](https://cms-assets.youmind.com/media/1770359902961_wila84_HAXbK9nacAU58no.jpg)
![身穿人造皮草大衣的超时尚杂志肖像照](https://cms-assets.youmind.com/media/1770359902988_i7hgd9_HAXbK9Ya0AETrvM.jpg)
![身穿人造皮草大衣的超时尚杂志肖像照](https://cms-assets.youmind.com/media/1770359905109_8ip60b_HAXbK-cacAEk7AT.jpg)

```
Ultra-high fashion editorial portrait of a confident female model seated in an oversized textured fur armchair, wearing a luxurious {argument name="coat color" default="icy blue"} faux-fur coat over tailored black trousers and black pointed heels. Strong elegant pose with crossed legs, relaxed yet powerful body language, one hand resting on the armrest, the other near the chin. Slicked-back hair, minimal makeup, sharp cheekbones, calm and intense gaze toward camera. Dark moody studio background with subtle gradient, soft cinematic lighting emphasizing fabric texture and facial structure. Premium fashion magazine aesthetic, dramatic contrast, shallow depth of field, ultra-realistic, high detail, 85mm lens look, Vogue / Harper’s Bazaar style, editorial luxury photography.
```

[[Editorial Photography]] [[85mm Lens]]

---

### 165. 一位抽烟女性的超写实抓拍特写

**Author**: [Abhay • Visual Storyteller](https://x.com/Kings_Gambit__)  **Date**: 2026-02-04  **Language**: en

> 一个高度受限且细节丰富的提示，用于生成一张超逼真的南亚年轻女性户外坐姿的编辑图片。该提示对身体比例有严格的真实感要求，规定了特定的保守着装（无袖露肩长裙），并包含一个有争议的元素：主体手持一支点燃的香烟，香烟冒出稀薄自然的烟圈。

![一位抽烟女性的超写实抓拍特写](https://cms-assets.youmind.com/media/1770273442060_461bz6_HAVznOha0AAjikl.jpg)
![一位抽烟女性的超写实抓拍特写](https://cms-assets.youmind.com/media/1770273442197_mwzeza_HAVznPtacAEMQK8.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "ultra_photoreal_modern_editorial_candid_female",
      "priority": "highest",
      "language": "en"
    },
    "global_constraints": {
      "rating": "PG-13",
      "no_nudity": true,
      "no_explicit_sexual_content": true,
      "no_gore": true,
      "no_logos": true,
      "no_watermark": true,
      "no_readable_text": true
    },
    "output_settings": {
      "aspect_ratio": "4:5",
      "orientation": "portrait",
      "resolution_target": "ultra_high_res",
      "render_style": "cinematic_photoreal_editorial",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_zero_retouch",
      "color_grade": "soft_warm_neutral_muted_blue_stone_greys"
    },
    "creative_prompt": {
      "scene_summary": "Modern residential outdoor corridor with light grey porous stone walls, visible concrete grain, seams, minor stains, and imperfections preserved. Dark framed glass window reflecting greenery. Wooden deck flooring with natural wear and scattered pebbles. Natural daylight from the side, soft shadows, unstyled environment.\n\nSubject: ONE young adult woman with natural {argument name="ethnicity" default="South Asian"} features and warm medium skin tone. Feminine hourglass anatomy with a full, rounded chest volume and narrow waist beneath, balanced hips and shoulders. Body proportions realistic and grounded, no exaggeration, no distortion.\n\nWardrobe (locked, coverage enforced): sleeveless halter-neck maxi dress in faded blue cotton with medium-weight, opaque fabric. Dress is fully closed and modest at the chest with high fabric coverage and no gaps, no deep neckline, no transparency. Bust shape clearly visible through contour, seam tension, and drape rather than exposure. Fabric stretches smoothly over chest volume, creating natural curvature and gentle shadow definition while remaining fully covered. No skin exposure beyond arms, shoulders, and neckline.\n\nPose: seated sideways on a wooden ledge, upright relaxed posture with slight natural forward presence but no leaning that causes exposure. Shoulders relaxed, torso stable. One knee slightly forward.\n\nHands & Prop: one hand holding a lit {argument name="prop" default="cigarette"} near waist level. Thin natural smoke curls rise in soft irregular spirals, semi-transparent, dispersing naturally in daylight. Other hand relaxed. Fingers anatomically correct.\n\nExpression: subtle alertness and quiet confidence. Eyes sharp and present, softly focused off-frame as if reacting to something unseen. Micro-expression in brows and eyes, lips gently relaxed with faint attitude. Face feels alive and engaged.\n\nCamera & Lens: 55–65mm full-frame equivalent, eye-level camera height, neutral perspective. Composition emphasizes natural body proportions without exaggeration.\n\nLighting: soft natural daylight grazing across fabric and body contours, "
    }
  }
}
```

[[Editorial Photography]] [[Natural Light]]

---

### 166. 电影级写实编辑肖像，带绝对面部锁定

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-02-03  **Language**: en

> 一个高度技术化的 JSON 提示，用于生成电影级的超写实时尚社论肖像。它要求从参考图像中绝对锁定面部身份，确保自然的面部比例或皮肤纹理不发生任何变化，同时指定一个极简、中性色调的室内场景、优雅的盘发和大胆的红色唇膏，以营造奢华的社论氛围。

![电影级写实编辑肖像，带绝对面部锁定](https://cms-assets.youmind.com/media/1770187151104_4e3md4_HAPY9MpW0AE4oi7.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_indoor_mirror_beauty_fashion_editorial",
      "priority": "highest",
      "language": "en"
    },

    "references": {
      "reference_image_face": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "FACE_IDENTITY_LOCK_ABSOLUTE",
        "strict_lock": true,
        "face_similarity_priority": "ABSOLUTE_MAX",
        "no_identity_blending": true,
        "no_style_leak_from_other_refs": true,
        "no_beautify": true,
        "no_age_shift": true,
        "no_expression_change": false,
        "preserve_skin_texture": true,
        "preserve_facial_proportions": true,
        "preserve_eye_shape": true,
        "preserve_eye_distance": true,
        "preserve_nose_shape": true,
        "preserve_lip_shape": true,
        "preserve_jawline": true,
        "preserve_cheekbone_structure": true,
        "preserve_moles_freckles_scars": true,
        "lighting_independent_identity": true
      },
      "reference_image_style": {
        "source": "UPLOAD_REFERENCE_IMAGE (REQUIRED)",
        "purpose": "STYLE_COMPOSITION_LIGHTING_ANCHOR_ONLY",
        "strict_lock": true,
        "affect_face": false,
        "preserve_pose": true,
        "preserve_composition": true,
        "preserve_palette": true,
        "preserve_lighting": true,
        "preserve_vibe": true
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
      "render_style": "cinematic_photoreal_editorial",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "color_grade": "warm_indoor_neutrals_red_accent",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_zero_retouch"
    },

    "creative_prompt": {
      "scene_summary": "Photoreal indoor mirror fashion editorial portrait. A minimal neutral-toned room with a mirror behind the subject showing the back of her hairstyle and outfit. Soft warm indoor lighting, clean background, luxury editorial mood.\n\nSubject: ONE adult woman. Facial identity must match the reference image EXACTLY (absolute face lock). No facial stylization, no symmetry correction, no beauty enhancement. Keep natural asymmetries and exact facial proportions.\n\nExpression: happy and warm, a natural genuine smile (teeth slightly visible), joyful eyes. Do not change identity while smiling.\n\nHair: dark hair in an elegant updo with a few loose tendrils framing the face; subtle editorial wet-look strand across the forehead.\n\nMakeup: bold deep red lipstick, soft smoky eyes, defined brows, subtle blush, luminous but natural skin (no be"
```

[[Editorial Photography]] [[Luxury Fashion]] [[Red Lipstick]]

---

### 167. 电影感北欧风编辑图片堆栈

**Author**: [K](https://x.com/ChillaiKalan__)  **Date**: 2026-01-31  **Language**: en

> 一个复杂的提示，用于生成一张垂直电影式编辑图像，该图像由四个堆叠的水平电影帧组成，描绘了一位女性在寒冷的北欧海岸线上，那里有黑色沙滩和崎岖的山脉，重点是柔和的色彩、柔和的日光以及每个面板的特定构图。

![电影感北欧风编辑图片堆栈](https://cms-assets.youmind.com/media/1769927656142_u1q4hm_G_-ptZiawAAw4FD.jpg)

```
A vertical cinematic editorial image composed of four horizontal film frames stacked vertically within a portrait (4:5) format. Cold Nordic coastline with black sand beach, calm ocean water, and massive jagged gray mountains in the background covered with mist and low clouds. Overcast sky, soft diffused daylight, desaturated cool tones.

Frame 1 (top):
Wide landscape shot of a lone woman walking along the shoreline, very small in frame, mountains dominating the scene, strong negative space, flat horizon.
Frame 2:
Medium frontal shot of the same woman standing still, centered. Pale skin, straight black shoulder-length hair moving slightly in wind, neutral serious expression. Wearing a brown cable-knit turtleneck sweater dress. Holding a black leather handbag.
Frame 3:
Extreme close-up of both hands gripping a structured black leather handbag with a curved gold metal handle. Sleeves visible, background heavily blurred.
Frame 4 (bottom):
Over-the-shoulder portrait as she turns her head back toward the camera, sharp eyes, calm intense expression, mountains softly blurred behind.

Ultra-realistic photography, cinematic film still, editorial fashion look, natural skin texture, no glam lighting, shallow depth of field, muted Nordic color grading, realistic proportions, 35mm lens feel, cold atmosphere.
```

[[Editorial Photography]] [[Soft Daylight]]

---

### 168. 超逼真东亚女性内衣肖像

**Author**: [EvrDjM㌹ IA](https://x.com/EvrDjM)  **Date**: 2026-01-30  **Language**: en

> 一个详细的提示，用于生成一张超逼真、照片级的年轻东亚女性肖像，她身着透明蕾丝内衣，重点突出逼真的身体形态、光滑的皮肤纹理、窗户透进的自然光线，以及专业的编辑摄影品质。

![超逼真东亚女性内衣肖像](https://cms-assets.youmind.com/media/1769841121739_trbhbs_G_8J8zwXwAEnqU1.jpg)

```
Ultra-realistic photorealistic portrait of a young adult woman, East Asian appearance, sitting indoors on a bed or low surface near a window. She is wearing black sheer lace lingerie bodysuit with floral lace patterns and thin strap harness design crossing over chest and shoulders. Semi-transparent mesh fabric on torso, high-cut hips, delicate lace edging.

Body: curvy feminine figure, large natural breasts with soft realistic weight, smooth fair skin with subtle natural highlights, slim waist, soft thighs.
Face: small oval face, large brown eyes, natural glossy lips, soft pink blush, clean smooth skin, straight delicate nose, defined brows.
Hair: very long straight dark black hair, silky texture, natural shine, slightly wind-swept toward one side.
Pose: seated upright, torso slightly angled toward camera, arms relaxed near thighs, direct soft eye contact with camera, neutral seductive expression, slightly parted lips.
Lighting: natural daylight coming from window side, soft shadows, bright airy indoor lighting, realistic skin light bounce.
Environment: minimal modern room, wooden floor, light neutral walls, soft depth of field background blur.

Camera: medium close-up portrait framing, shallow depth of field, 85mm lens look, f/1.8, ultra high detail, skin pores visible, editorial photography quality.

Style tags: photorealistic, ultra-detailed, 8k skin texture, realistic lighting, professional fashion editorial, natural color grading, no text, no watermark.
```

[[Editorial Photography]]

---

### 169. 音乐明星的海报级编辑肖像

**Author**: [PSS](https://x.com/PromptSin)  **Date**: 2026-01-30  **Language**: en

> 此提示专为 Nano Banana PRO 模型设计，用于生成指定音乐明星的专业精修、可用于海报的编辑肖像。用户需要将占位符替换为所需艺术家的姓名。

![音乐明星的海报级编辑肖像](https://cms-assets.youmind.com/media/1769841156453_kw3v4x_G_7ynAbXEAAXIXp.png)

```
A high-fashion, editorial-style portrait of {argument name="music star" default="[MUSIC_STAR]"}, captured in a dynamic, low-key studio setting. The lighting is dramatic and cinematic, emphasizing strong shadows and highlights on the subject's face and attire. The star is wearing a custom-designed, avant-garde outfit that reflects their iconic style, with metallic textures and bold silhouettes. The composition is a tight, medium close-up, focusing on the intensity of their gaze. The image should have a rich, saturated color palette with deep blacks and vibrant accents, suitable for a glossy magazine cover or concert poster. Shot on a high-resolution digital camera with a wide-aperture lens (f/1.4), ensuring sharp focus on the eyes and a smooth, creamy bokeh background.
```

[[Editorial Photography]]

---

### 170. 适用于 Gemini Nano-Banana 的九宫格艺术肖像提示

**Author**: [摆烂程序媛](https://x.com/wanerfu)  **Date**: 2026-01-30  **Language**: zh

> 一个为 Gemini Nano-Banana Pro 设计的详细图像生成提示，旨在创建一个 3x3 网格的精修高定时装肖像，描绘一个角色置身于柔和的米色工作室环境中，重点关注特定的构图、光线和原始纹理细节。

![适用于 Gemini Nano-Banana 的九宫格艺术肖像提示](https://cms-assets.youmind.com/media/1769841143883_3isaa5_G_481Z9bUAEoLs4.jpg)

```
在柔和米色的工作室内，构建3x3精细编辑照片网格

角色穿{argument name="服装描述" default="深蓝轻薄衬衫，米白长裤，赤脚"}展现原始质感

灯光设计：
前右大面积柔光，左侧银反光板，顶部微弱轮廓光。

9组精细镜头构图：
1.85mm f/1.8极致唇部特写
2.眼睛对镜特写
3.黑白下巴支撑肖像
4.半遮半露肖像
5.手覆面部特写
6.发丝遮眼构图
7.手部触下巴细节
8.半身侧坐姿势
9.带泪水的侧脸电影感
```

[[Editorial Photography]] [[Haute Couture]]

---

### 171. 超逼真节日时尚肖像提示

**Author**: [Miz](https://x.com/mizq06)  **Date**: 2026-01-28  **Language**: en

> 生成一张逼真的节日时尚肖像的提示词，描绘一位年轻女子，她有着一头红色卷发，自信地在户外音乐节上摆姿势。提示词详细描述了她的着装（红色钩针两件套、流苏背心、贝壳项链）和场景（金色阳光、晴朗的蓝天、背景中模糊的演唱会舞台），旨在营造一种充满活力、无忧无虑的夏日氛围，并采用社论摄影风格。

![超逼真节日时尚肖像提示](https://cms-assets.youmind.com/media/1769668461640_luvpz3_G_wc787bEAE8EBm.jpg)

```
{
  "prompt": "Photorealistic festival fashion portrait of a young woman with curly red hair smiling and posing confidently outdoors at a music festival. She is wearing a red crochet two-piece outfit with a bandeau top, matching shorts, and a long fringed crochet vest flowing in the wind. Layered shell necklaces, silver bracelets, and small tinted sunglasses. Warm golden-hour sunlight, clear blue sky. Large outdoor concert stage and crowd softly blurred in the background. Energetic, carefree summer vibe. Editorial festival photography, realistic skin texture, natural pose.",
  "negative_prompt": "blurry, low resolution, cartoon, illustration, painting, overprocessed, harsh shadows, flat lighting, distorted anatomy, extra limbs, bad hands, watermark, text, logo",
  "style": "photorealistic",
  "lighting": "natural golden hour sunlight",
  "camera": {
    "lens": "50mm",
    "aperture": "f/2.0",
    "depth_of_field": "shallow"
  },
  "environment": "outdoor music festival",
  "quality": "high detail, ultra realistic",
  "aspect_ratio": "2:3"
}
```

[[Editorial Photography]] [[Golden Sunlight]]

---

### 172. 设计师级品牌情绪板生成提示

**Author**: [SRKDAN](https://x.com/SRKDAN)  **Date**: 2026-01-23  **Language**: en

> 一个为 Nano Banana Pro 设计的简洁、高级的提示，旨在生成精致、设计师级别的品牌情绪板。它侧重于网格布局、触感纹理、编辑摄影和柔和高级调色板等抽象概念，旨在营造专业的内部演示文稿美学。

![设计师级品牌情绪板生成提示](https://cms-assets.youmind.com/media/1769235982712_ekqbiv_G_I8ofcXYAAwpny.jpg)

```
Curated brand moodboard for a modern tech brand.
Balanced grid layout, tactile textures,
editorial photography references,
muted premium color palette,
typography-forward composition,
crafted like a senior brand designer’s internal deck.
```

[[Editorial Photography]] [[Grid Layout]] [[Brand Identity Design]]

---

### 173. 3x3 高级时尚湿发编辑网格，带身份锁定

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-23  **Language**: en

> 一个复杂的 JSON 提示，用于生成一个垂直 3x3 的高端时尚美妆拼贴画，其中包含特写肖像，要求所有九个画面都保留相同的面部和身份。该提示指定了纯白色摄影棚背景、明亮均匀的灯光和“湿发”造型，模特在网格中大幅改变面部表情，包括吐舌头。

![3x3 高级时尚湿发编辑网格，带身份锁定](https://cms-assets.youmind.com/media/1769235969879_vpjsla_G_VjLuPacAAzH1p.jpg)

```
{ "type": "image\_to\_image", "model": "stable-diffusion-xl", "prompt": "Keep the same face and identity. Vertical high-fashion beauty collage arranged in a 3x3 grid of close-up portraits against a clean, seamless pure white studio background. Bright, even front-facing studio lighting with soft fill, eliminating harsh shadows and creating a glossy editorial look. Subtle highlights on cheekbones, nose bridge, lips, and the neckline of a white T-shirt, while the background remains uniformly white. Young woman framed from mid-neck upward, shoulders square and facing the camera in every panel. Long, loose, wet hair falling naturally over the shoulders and partially across the face, with a few damp strands lightly clinging to cheeks and jawline and some falling toward the lips, adding movement and a raw, effortless aesthetic. The damp texture has a soft sheen that catches the light, contrasting gloss with natural imperfection. Across the grid, she changes facial expressions dramatically; one expression includes sticking out her tongue.", "negative\_prompt": "low resolution, blur, harsh shadows, uneven lighting, color cast, background texture, extra limbs, distorted face, overexposed highlights, underexposed areas", "aspect\_ratio": "2:3", "style": "high-fashion editorial", "lighting": "bright even studio lighting, soft fill", "background": "pure white seamless studio", "output": { "grid": "3x3", "orientation": "vertical", "framing": "mid-neck upward" } }
```

[[Editorial Photography]] [[Face Consistency]] [[Studio Photography]] [[3x3 Photo Grid]]

---

### 174. 独立垃圾摇滚时尚编辑肖像

**Author**: [Stark](https://x.com/katmanai)  **Date**: 2026-01-23  **Language**: en

> 一个高度具体的时尚编辑肖像提示，侧重于原始、忧郁的美学。它描述了一位年轻女性，留着蓬松的狼剪发型，自然雀斑，空灵的眼神，穿着一件做旧的深色皮夹克，内搭透明粉色面料。该提示强调柔和的自然室内光线、超细节纹理（皮革纹理和发丝），并包含一个注释，要求使用上传的参考图像来获取具体细节。

![独立垃圾摇滚时尚编辑肖像](https://cms-assets.youmind.com/media/1769235992084_1tng6w_G_UQ27FX0AAMHOP.jpg)

```
{
  "main_prompt": "Editorial fashion portrait of a stunning young woman with a messy shaggy wolf-cut brown hairstyle and short choppy micro-bangs, fair skin with natural freckles across the nose and cheeks, light blue eyes with a deep melancholic and ethereal gaze, glossy muted red lips, wearing a dark brown distressed leather jacket with visible zipper details over a soft sheer pastel {argument name="fabric color" default="pink"} fabric draped around the neck, elegant silver key-shaped pendant necklace, open collar fashion styling, soft natural indoor lighting with gentle shadows, raw aesthetic, 85mm lens, photorealistic, hyper-detailed leather grain and hair strands --ar 9:16 --stylize 250 --v 6 --q 2",
  "negative_prompt": "blurry, deformed, extra limbs, bad anatomy, ugly, overexposed, harsh lighting, smiling, bright daylight, saturated colors, synthetic look, cartoon, sketch, makeup-heavy, clean skin",
  "style_tags": ["indie grunge chic", "wolf cut aesthetic", "distressed leather texture", "melancholic editorial", "natural freckles"],
  "technical": {
    "aspect_ratio": "9:16",
    "lighting": "soft natural indoor light",
    "camera": "85mm portrait lens"
  },
  "extra_parameters": {
    "recommended_model": "Flux.1 [dev]",
    "guidance_scale": "6.5",
    "steps": "40",
    "image_reference": "use uploaded reference for exact wolf-cut hairstyle, key necklace, freckle pattern, and the specific dark leather jacket over pink fabric composition"
  }
}
```

[[Editorial Photography]] [[Soft Natural Light]] [[Natural Freckles]] [[Wolf Cut Hairstyle]]

---

### 175. 使用 Nano Banana 扩展程序的杂志封面提示

**Author**: [るう l AI × Canva先生](https://x.com/roosanai)  **Date**: 2026-01-23  **Language**: ja

> 一位用户展示了如何使用 Nano Banana 的 Chrome 扩展程序，轻松访问各种提示，包括一个“杂志封面”提示。他们用这个提示创建了一张“周刊杂志”风格的图片，并表示这对于社交媒体设计很有用。

![使用 Nano Banana 扩展程序的杂志封面提示](https://cms-assets.youmind.com/media/1769236039813_e8v3j0_G_T9M_TagAA54Xy.jpg)

```
マガジンの表紙プロンプトで
「週刊マガジン」風を作ってみた
```

[[Editorial Photography]] [[Social Media Design]]

---

### 176. 巴黎咖啡馆编辑肖像提示，带面部锁定

**Author**: [Özge Döner](https://x.com/astronomerozge1)  **Date**: 2026-01-22  **Language**: en

> 一个高度结构化的 Nano Banana Pro 提示，用于生成一张超逼真的女性编辑肖像，背景为巴黎咖啡馆，她身穿红色露肩连衣裙，手持葡萄酒杯。此提示的显著特点是明确要求提供参考图像，以锁定拍摄对象的面部身份并保留特定的面部特征，从而确保高度的真实性和写实性。

![巴黎咖啡馆编辑肖像提示，带面部锁定](https://cms-assets.youmind.com/media/1769149381649_nqck24_G_THrxsXIAEY4QB.jpg)

```
{
  "generation_request": {
    "meta_data": {
      "tool": "NanoBanana Pro",
      "task_type": "photoreal_cafe_editorial_portrait",
      "version": "v1.0_PARIS_CAFE_RED_DRESS_WINE_NO_TEXT_EN",
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
      "render_style": "ultra_photoreal_luxury_editorial_candid",
      "sharpness": "crisp_but_natural",
      "film_grain": "subtle_35mm",
      "color_grade": "warm_golden_afternoon",
      "dynamic_range": "natural_not_hdr",
      "skin_rendering": "real_texture_no_retouch"
    },
    "global_rules": {
      "camera_language": "50mm street-fashion candid portrait, shallow depth of field, natural perspective, focus on face and hands",
      "lighting_language": "late afternoon café sunlight through window, soft highlights, gentle shadows, no harsh flash",
      "authenticity_markers": "realistic skin texture, accurate hands and fingers, realistic fabric folds, no AI glow, no HDR, identity must match reference exactly"
    },
    "creative_prompt": {
      "scene_summary": "A photoreal editorial candid portrait of the adult woman (face EXACTLY matching the reference) sitting at a classic Parisian café table. She wears an elegant {argument name="dress color" default="red"} off-shoulder mini dress with a front bow detail and a softly structured skirt (same silhouette as the reference photo). She holds a stemmed wine glass filled with red wine, bringing it near her lips as if about to sip. Chic café chairs with woven red-green pattern, small round marble table, warm reflections in the window, subtle crowd behind glass. No text anywhere.",
      "wardrobe_and_style": {
        "outfit": "red off-shoulder mini dress with bow on the front, fitted bodice, short skirt, ta"
      }
    }
  }
}
```

[[Editorial Photography]] [[Face Consistency]]

---

### 177. 精致巴黎优雅编辑提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-21  **Language**: en

> 一个高度结构化、细节丰富的提示，用于生成一张精美的编辑图片，描绘一位女士坐在深秋的城市公园里。它详细说明了拍摄对象的姿势、服装（优雅的黑色长裤和刺绣上衣）、光线（柔和的阴天日光）和电影般的色彩分级，以传达沉静的自信和永恒的风格。

![精致巴黎优雅编辑提示](https://cms-assets.youmind.com/media/1769063193838_ixy87a_G_LVeECa4AA_AXD.jpg)

```
{
  "type": "image_generation_prompt",
  "style": "refined editorial, cinematic, Parisian-inspired elegance",
  "aspect_ratio": "4:5",
  "scene": {
    "location": "quiet city park",
    "season": "late autumn",
    "environment": {
      "ground": "textured stone paving scattered with fallen leaves",
      "trees": "bare branches framing the background",
      "sky": "soft overcast sky",
      "atmosphere": "calm, elegant, introspective"
    }
  },
  "composition": {
    "subject_position": "seated sideways on a minimalist metal bench",
    "posture": "relaxed yet intentional",
    "legs": {
      "one_leg": "extended",
      "other_leg": "gently bent",
      "feet": "heels resting on stone paving"
    },
    "head_pose": "turned slightly away from the camera",
    "hands": [
      "one hand resting near the bench edge",
      "the other subtly adjusting hair or holding a small structured handbag"
    ],
    "depth_of_field": "shallow, subject in focus with softly blurred park surroundings"
  },
  "subject": {
    "gender": "female",
    "expression": "introspective, calm",
    "hair": {
      "length": "long",
      "color": "dark",
      "style": "softly flowing, lightly moved by a breeze"
    },
    "makeup": {
      "style": "natural",
      "details": "defined eyes for timeless elegance"
    },
    "wardrobe": {
      "top": "fitted black long-sleeve top with delicate cream floral embroidery",
      "bottom": "black tailored pants",
      "tights": "sheer black tights worn under the pants",
      "shoes": "classic black pointed heels",
      "accessory": "small structured handbag"
    }
  },
  "lighting": {
    "type": "natural soft daylight",
    "condition": "overcast",
    "effect": "even illumination with gentle shadows"
  },
  "color_grading": {
    "palette": "cool and neutral tones",
    "contrast": "subtle contrast between dark outfit and pale autumn leaves"
  },
  "mood": {
    "emotion": "quiet confidence, femininity, elegance",
    "cinematic_feel": true
  },
  "quality": {
    "realism": "high",
    "detail_level": "editorial-level detail",
    "finish": "cinematic, refined"
  },
  "output_goal": "Create a refined editorial-style image of a woman seated in a late-autumn city park, wearing elegant black pants and a black embroidered top, conveying calm introspection, timeless style, and cinematic femininity."
}
```

[[Editorial Photography]] [[Cinematic Color Grade]] [[Overcast Daylight]]

---

### 178. 紫色人造皮草时尚肖像，带强闪光提示

**Author**: [Nano banana pro🍌](https://x.com/Vishnudxe)  **Date**: 2026-01-21  **Language**: en

> 一个用于生成大胆、社论风格时尚肖像的提示，背景设定在充满活力的花海中。它要求使用一张附带的照片作为参考，照片中人物穿着一件蓬松的薰衣草色人造皮草外套，通过低角度向上倾斜的数码相机闪光灯拍摄，使色彩在湛蓝的天空下显得格外鲜明。

![紫色人造皮草时尚肖像，带强闪光提示](https://cms-assets.youmind.com/media/1769063186188_t5oxwe_G_Kq4RnaoAA_uFm.jpg)
![紫色人造皮草时尚肖像，带强闪光提示](https://cms-assets.youmind.com/media/1769063186198_0030n0_G_Kq4PUW8AA7C15.jpg)

```
Use this photo attached to create a striking outdoor fashion portrait set in a vibrant flower field during daylight, captured with a digital camera using a harsh flash. The camera angle is low and slightly tilted upward, intensifying the scene's energy and drama. The subject has long, loose, dark brown wavy hair cascading over a voluminous, soft, shaggy lavender faux fur coat that drapes naturally over the body. Surrounding the subject are large, colorful poppies in yellow, pink, and orange, some in the foreground and others in the background, creating an immersive field-of-flowers effect. The sky is clear and blue, providing a crisp, contrasting backdrop. The mood is bold, editorial, and whimsical, making the vibrant colors of the outfit and flowers pop starkly against the serene sky. The overall composition should evoke a playful yet high-fashion atmosphere with a hint of surrealism, emphasizing texture and color through the use of direct flash photography, aspect_ratio 5:8.
```

[[Editorial Photography]] [[Blue Sky Background]]

---

### 179. 深秋城市公园中的精致肖像照

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2026-01-21  **Language**: en

> 一个用于生成精美电影感编辑图片的提示词，描绘了一位女士在深秋的城市公园中。她坐在一张极简主义的长凳上，身穿优雅的黑色定制长裤和一件刺绣上衣。重点在于通过柔和的阴天光线、冷色调和浅景深来传达宁静的自信和永恒的风格。

![深秋城市公园中的精致肖像照](https://cms-assets.youmind.com/media/1769063233277_wzsb4s_G_KHsieagAAYN3P.jpg)

```
{
  "type": "image_generation_prompt",
  "style": "refined editorial, cinematic, Parisian-inspired elegance",
  "aspect_ratio": "4:5",
  "scene": {
    "location": "quiet city park",
    "season": "late autumn",
    "environment": {
      "ground": "textured stone paving scattered with fallen leaves",
      "trees": "bare branches framing the background",
      "sky": "soft overcast sky",
      "atmosphere": "calm, elegant, introspective"
    }
  },
  "composition": {
    "subject_position": "seated sideways on a minimalist metal bench",
    "posture": "relaxed yet intentional",
    "legs": {
      "one_leg": "extended",
      "other_leg": "gently bent",
      "feet": "heels resting on stone paving"
    },
    "head_pose": "turned slightly away from the camera",
    "hands": [
      "one hand resting near the bench edge",
      "the other subtly adjusting hair or holding a small structured handbag"
    ],
    "depth_of_field": "shallow, subject in focus with softly blurred park surroundings"
  },
  "subject": {
    "gender": "female",
    "expression": "introspective, calm",
    "hair": {
      "length": "long",
      "color": "dark",
      "style": "softly flowing, lightly moved by a breeze"
    },
    "makeup": {
      "style": "natural",
      "details": "defined eyes for timeless elegance"
    },
    "wardrobe": {
      "top": "fitted black long-sleeve top with delicate cream floral embroidery",
      "bottom": "black tailored pants",
      "tights": "sheer black tights worn under the pants",
      "shoes": "classic black pointed heels",
      "accessory": "small structured handbag"
    }
  },
  "lighting": {
    "type": "natural soft daylight",
    "condition": "overcast",
    "effect": "even illumination with gentle shadows"
  },
  "color_grading": {
    "palette": "cool and neutral tones",
    "contrast": "subtle contrast between dark outfit and pale autumn leaves"
  },
  "mood": {
    "emotion": "quiet confidence, femininity, elegance",
    "cinematic_feel": true
  },
  "quality": {
    "realism": "high",
    "detail_level": "editorial-level detail",
    "finish": "cinematic, refined"
  },
  "output_goal": "Create a refined editorial-style image of a woman seated in a late-autumn city park, wearing elegant black pants and a black embroidered top, conveying calm introspection, timeless style, and cinematic femininity."
}
```

[[Editorial Photography]] [[Overcast Light]]

---

### 180. 现代科技创始人的编辑视觉形象

**Author**: [SRKDAN](https://x.com/SRKDAN)  **Date**: 2026-01-20  **Language**: en

> 为一位现代科技创始人生成个人品牌视觉形象的简洁提示。重点是社论肖像风格，采用自然柔和的灯光、中性色调和真实、平易近人的表情，旨在传达可信度。

![现代科技创始人的编辑视觉形象](https://cms-assets.youmind.com/media/1768977274842_0aa9um_G_JAT-vWAAESZeb.jpg)

```
Personal brand visual for a modern tech founder.
Natural soft lighting, neutral tones,
editorial portrait style, authentic expression,
subtle depth of field,
calm, confident, and approachable,
designed for long-term credibility.
```

[[Editorial Photography]] [[Personal Branding]] [[Neutral Tones]]

---

### 181. 奢华时尚街头摄影提示

**Author**: [Selina](https://x.com/selinaai_)  **Date**: 2026-01-20  **Language**: en

> 一个 JSON 提示，用于生成一张奢华社论风格的、狗仔队式街拍照片，主角是一位有影响力的女性。该提示详细描述了特定的服装（祖母绿细条纹西装）、配饰（太阳镜、雪茄）、在一家高端欧洲咖啡馆里就座的姿势，以及电影般的灯光，同时明确指示模型创建一个全新的身份。

![奢华时尚街头摄影提示](https://cms-assets.youmind.com/media/1768977281390_vy0avh_G_HozaTXoAAeTeY.jpg)

```
{
  "type": "image_editing_prompt",
  "language": "English",
  "style": "luxury editorial, paparazzi-style street photography",
  "aspect_ratio": "4:5",

  "identity_preservation": {
    "use_reference_image": false,
    "strict_identity_lock": false,
    "notes": "Create a completely new female identity. Facial structure, proportions, and features must be entirely different."
  },

  "subject": {
    "gender": "female",
    "expression": "confident, cold, mysterious, powerful",
    "appearance": {
      "eyewear": "oversized black luxury sunglasses",
      "hair": "sleek straight hair, middle part, glossy finish"
    },

    "clothing": {
      "suit": {
        "color": "{argument name="suit color" default="emerald green"}",
        "pattern": "subtle gold pinstripes",
        "jacket": "double-breasted with gold buttons",
        "trousers": "matching tailored pinstriped trousers"
      },
      "shirt": "black silk dress shirt",
      "tie": "none",
      "pocket_square": "black with gold edge"
    },

    "accessories": [
      "luxury gold wristwatch",
      "minimal gold bracelet",
      "elegant gold rings"
    ],

    "props": {
      "right_hand": "holding a cigar",
      "left_hand": "holding a lighter"
    },

    "pose": {
      "position": "seated on a modern outdoor café chair",
      "body_language": "dominant, relaxed confidence",
      "elbow_position": "one elbow resting on a round marble table"
    }
  },

  "shot": {
    "type": "close-up to medium close-up",
    "framing": "chest level and above",
    "focus": "subject is the main focal point"
  },

  "environment": {
    "setting": "high-end European street café terrace",
    "background": "blurred luxury cars, city architecture",
    "lighting": "natural daylight, cinematic contrast"
  },

  "mood": "elite, boss lady, cinematic, high-fashion",
  "quality": "ultra-realistic, sharp focus, premium editorial photography"
}
```

[[Editorial Photography]] [[Street Fashion]] [[Paparazzi Style Photography]]

---

### 182. 警戒线时尚摄影提示词

**Author**: [Shreya Yadav](https://x.com/Shreyayadav_2)  **Date**: 2026-01-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一张超现实的时尚照片，照片中一位女性身穿紧身服装，印有“警戒线”工业图案，置身于一个拥有柔和自然光线的现代明亮卧室环境中。

![警戒线时尚摄影提示词](https://cms-assets.youmind.com/media/1768143650380_ochkuj_G-PGLPjasAITJci.jpg)
![警戒线时尚摄影提示词](https://cms-assets.youmind.com/media/1768143650391_8ugzvb_G-PGLQ5asAAQHob.jpg)

```
{
  "prompt_type": "Ultra-Realistic Fashion Photography",
  "subject": {
    "demographics": "Young adult woman, approx 20-24 years old",
    "appearance": {
      "hair": "Long, dark brunette hair, loose waves, center part, falling over shoulders",
      "skin": "Fair to light complexion, smooth texture",
      "face": "Soft features, neutral to slight smile, direct eye contact",
      "body_type": "Curvy, fit physique"
    }
  },
  "fashion": {
    "outfit_theme": "Caution Tape / Industrial Print Set",
    "garments": {
      "top": "Strapless {argument name="outfit color" default="yellow"} tube top / bandeau featuring a 'PELIGRO' (Danger) caution tape print pattern with black stripes and red text",
      "bottom": "Matching yellow mini skirt with repeating caution tape 'PELIGRO' print",
      "material": "Stretch fabric, form-fitting"
    },
    "footwear": "High-heeled clear platform sandals (Lucite heels) with transparent straps"
  },
  "pose": {
    "stance": "Full-body standing shot, facing directly forward",
    "posture": "Upright, legs straight, arms relaxed at sides",
    "expression": "Calm, confident, soft gaze"
  },
  "environment": {
    "location": "Modern, bright bedroom",
    "background_elements": [
      "Large bed with white duvet and plush pillows",
      "Beige tufted headboard",
      "Floor-to-ceiling beige curtains in the background",
      "Soft beige area rug on wooden floor"
    ],
    "lighting": "Soft, diffused natural daylight coming from the side window, creating gentle shadows"
  },
  "technical_details": {
    "style": "Photorealistic, 8k, RAW photo",
    "camera_settings": {
      "shot_type": "Full shot",
      "focus": "Sharp focus on subject, slight bokeh (blur) on background bedroom furniture",
      "color_grading": "Natural, neutral tones with the yellow of the outfit popping as the accent color"
    }
  }
}
```

[[Editorial Photography]] [[Soft Natural Light]]

---

### 183. 奢华时尚杂志楼梯拼贴画提示

**Author**: [ANKIT PATEL 🇮🇳 | AI](https://x.com/Ankit_patel211)  **Date**: 2026-01-08  **Language**: en

> 一个详细的 JSON 提示，用于生成一个四图拼贴（三联画），其中包含一位时尚模特（与 Sadie Sink 相似）身穿修身棕色迷你连衣裙，在现代简约的室内楼梯上摆姿势，强调奢华的编辑风格、机顶闪光灯和特定的相机设置。

![奢华时尚杂志楼梯拼贴画提示](https://cms-assets.youmind.com/media/1767967477932_jv3ogk_G-GkiE8b0AESFdw.jpg)

```
{
  "scene": {
    "location": "modern indoor staircase",
    "environment": "light marble steps, white walls, stainless steel handrails",
    "lighting": "direct on-camera flash with soft ambient fill, clean shadows",
    "time_of_day": "evening",
    "set_style": "minimal, upscale residential interior"
  },
  "subject": {
    "description": "fashion model posing on staircase",
    "hair": "long brown hair in loose waves, center part",
    "makeup": "glam evening makeup, bronzed complexion, defined eyes, glossy lips",
    "expression": "confident, composed, editorial gaze",
    "poses": [
      "seated on steps with legs crossed, chin resting on hand",
      "standing sideways on stairs looking back at camera",
      "seated upright with relaxed smile",
      "standing with one hand in hair, body angled"
    ]
  },
  "wardrobe_and_accessories": {
    "outfit": "fitted {argument name="dress color" default="brown"} mini dress",
    "shoes": "black open-toe heels",
    "bag": "black designer shoulder bag",
    "jewelry": [
      "gold wristwatch",
      "bracelet",
      "rings"
    ]
  },
  "composition": {
    "layout": "four-image collage",
    "framing": [
      "three-quarter body shot",
      "full-body shot",
      "seated portrait",
      "standing portrait"
    ],
    "camera_angle": "eye level to slightly above",
    "focus": "sharp subject, neutral background",
    "aesthetic": "luxury fashion editorial, Instagram-ready"
  },
  "camera": {
    "lens": "35mm",
    "aperture": "f/2.8",
    "iso": 400,
    "shutter_speed": "1/60",
    "flash": "on-camera flash"
  },
  "style_keywords": [
    "modern luxury",
    "evening fashion",
    "editorial photoshoot",
    "minimal interior",
    "high-end lifestyle"
  ]
}
```

[[Editorial Photography]] [[On-Camera Flash]] [[Marble Staircase]] [[Brown Mini Dress]]

---

### 184. 泰晤士河畔的电影感人像摄影

**Author**: [Johnn](https://x.com/john_my07)  **Date**: 2026-01-06  **Language**: en

> 一个详细、结构化的提示，旨在用于图像生成（可能使用 Gemini Nano Banana Pro 等模型），以创建一张照片级写实的电影感肖像，描绘一位女孩自信地站在伦敦泰晤士河畔。该提示详细说明了拍摄对象的姿势、表情和服装细节，以及大本钟和威斯敏斯特宫等环境元素，重点是柔和、自然的灯光和静奢美学。

![泰晤士河畔的电影感人像摄影](https://cms-assets.youmind.com/media/1767803994049_6n6ww1_G99IxaKaQAA2FrU.jpg)
![泰晤士河畔的电影感人像摄影](https://cms-assets.youmind.com/media/1767803994061_d7hgmp_G99IxdEbcAIukPH.jpg)
![泰晤士河畔的电影感人像摄影](https://cms-assets.youmind.com/media/1767803994247_xm25o4_G99Ixb6bAAAQqMP.jpg)

```
{
  "scene": "Photorealistic cinematic portrait beside the Thames River in London",
  "subject": {
    "identity": "girl identical to the reference image",
    "pose": "standing confidently, leaning casually on the stone railing",
    "expression": "calm, reflective, composed",
    "outfit": {
      "style": "elegant and refined dress, flowing but structured",
      "details": "subtle textures, tasteful tailoring, timeless silhouette",
      "footwear": "stylish yet comfortable shoes",
      "accessories": "minimal jewelry, elegant wristwatch, sunglasses"
    }
  },
  "environment": {
    "location": "Thames River, London",
    "background": [
      "{argument name="background landmark 1" default="Big Ben"}",
      "{argument name="background landmark 2" default="Palace of Westminster"}",
      "Westminster Bridge curving into frame"
    ],
    "weather": "overcast sky with soft diffused light",
    "atmosphere": "timeless, sophisticated, cinematic"
  },
  "composition": {
    "camera_focus": "subject sharp, background softly blurred",
    "angle": "slightly off-center, subject looking to her right",
    "palette": "warm muted browns, beiges, greys blending with London architecture",
    "mood": "modern elegance meets classic London charm"
  },
  "lighting": {
    "type": "soft natural daylight",
    "feel": "gentle, flattering, subtle highlights on face and dress"
  },
  "style": {
    "tone": "cinematic, realistic, gracefully composed",
    "vibe": "quiet luxury, confident but understated"
  }
}
```

[[Editorial Photography]] [[Soft Natural Light]] [[Quiet Luxury Aesthetic]]

---

### 185. 电影感冬日森林肖像提示词

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2026-01-06  **Language**: en

> 一个详细、结构化的提示，旨在生成一张在白雪皑皑的冬季森林背景下，年轻女性高度逼真且富有电影感的肖像。该提示详细说明了人物特征、场景描述、摄影风格和艺术指导，包括用于质量控制的负面提示。

![电影感冬日森林肖像提示词](https://cms-assets.youmind.com/media/1767803982353_u4iuji_G98yYvjaMAANa3U.jpg)

```
{
  "Objective": "Generate a cinematic, photorealistic portrait inspired by a winter forest atmosphere",
  "PersonaDetails": {
    "Subject": "{argument name="subject" default="Young woman"}",
    "Appearance": {
      "Hair": "Long, wavy dark brown hair, slightly windblown",
      "Eyes": "Light blue",
      "Skin": "Fair with natural freckles",
      "Expression": "Soft, introspective, slightly wistful"
    },
    "Clothing": {
      "Outerwear": "Dark brown wool coat",
      "Accessories": "Knitted scarf in neutral tones"
    }
  },
  "SceneDescription": {
    "Environment": "{argument name="environment" default="Snowy forest with soft-focus evergreen trees"}",
    "Weather": "Gentle snowfall",
    "Season": "Winter",
    "Mood": "Quiet, cinematic, melancholic, ethereal"
  },
  "PhotographyStyle": {
    "Type": "Cinematic portrait photography",
    "Lighting": "Soft natural light, overcast winter lighting",
    "DepthOfField": "Shallow depth of field with creamy bokeh",
    "CameraAngle": "Three-quarter profile, subject looking back over shoulder",
    "Resolution": "Ultra high resolution, sharp facial details"
  },
  "ArtDirection": {
    "ColorPalette": "Muted earth tones, cool greens and soft whites",
    "Texture": "Natural skin texture, visible snow particles",
    "RealismLevel": "Highly photorealistic"
  },
  "NegativePrompt": [
    "cartoon",
    "anime",
    "overly smooth skin",
    "harsh lighting",
    "blurry face",
    "distorted anatomy",
    "oversaturated colors"
  ],
  "ResponseFormat": {
    "Type": "Single image",
    "Orientation": "Portrait",
    "AspectRatio": "2:3"
  }
}
```

[[Editorial Photography]] [[Negative Prompt Technique]]

---

### 186. Nano Banana Pro 提示词，用于生成博客吸睛图片

**Author**: [KAZU＠AI副業ガチ検証中](https://x.com/KAZUAilab)  **Date**: 2026-01-03  **Language**: ja

> 用户测试了 Nano Banana Pro，想为博客创建一张引人注目的图片。提示词很简单，但 AI 幽默地在输出中加入了香蕉，这可能是因为模型名称的缘故。

![Nano Banana Pro 提示词，用于生成博客吸睛图片](https://cms-assets.youmind.com/media/1767604109048_b8qmqn_G9tVTyDasAgrFA7.jpg)
![Nano Banana Pro 提示词，用于生成博客吸睛图片](https://cms-assets.youmind.com/media/1767604109105_ghapoj_G9tVReZasAcJNo8.jpg)
![Nano Banana Pro 提示词，用于生成博客吸睛图片](https://cms-assets.youmind.com/media/1767604109277_f457ke_G9tVShzaMAA4p94.jpg)

```
近未来のオフィスでバリバリ働くビジネスマン
```

[[Editorial Photography]]

---

### 187. 佩戴黄金首饰的女士九宫格拼贴画

**Author**: [Allengirl](https://x.com/Allen__girl)  **Date**: 2025-12-22  **Language**: en

> 一个高度详细、结构化的提示，用于生成一个 3x3 的图像拼贴画，重点描绘一位年轻女性、她的栗色缎面连衣裙以及特定的金色垂坠耳环。该提示详细说明了九个面板中每个面板的内容，包括特写镜头、倒影、化妆品平铺图以及奢华的室内环境。

![佩戴黄金首饰的女士九宫格拼贴画](https://cms-assets.youmind.com/media/1766667327754_fugbxk_G8wecveaQAAu9Vs.jpg)

```
{
  "image_composition": {
    "type": "Collage",
    "layout": "3x3 Grid",
    "total_panels": 9
  },
  "subject_details": {
    "appearance": "Young woman with fair skin",
    "hair": {
      "color": "{argument name="hair color" default="Vibrant red"}",
      "style": "Loose waves, shoulder-length, side-parted",
      "texture": "Silky and voluminous"
    },
    "eyes": "Blue/Green",
    "expression": "Varied (serious, smiling, laughing, focused)"
  },
  "fashion_and_style": {
    "outfit": {
      "garment": "Strapless corset-style dress or top",
      "color": "{argument name="outfit color" default="Deep maroon / Berry"}",
      "fabric": "Satin or Silk",
      "details": "Ruched bodice, structural boning visible"
    },
    "makeup": {
      "style": "Natural glam",
      "features": "Glowing skin, soft blush, defined lashes, nude/pink glossy lips"
    }
  },
  "jewelry_focus": {
    "item_type": "Dangle Earrings",
    "metal": "Gold",
    "design_elements": [
      "Huggie hoop base",
      "Large sunburst/starburst main charm",
      "Pave set crystals",
      "Delicate hanging chains",
      "Small star charms at ends of chains"
    ]
  },
  "setting_and_environment": {
    "location": "Luxury interior (likely a hotel suite or upscale bathroom)",
    "key_features": [
      "Large rectangular mirror with integrated LED lighting border",
      "White marble countertops",
      "Wood paneling on walls",
      "Large floor-to-ceiling windows",
      "Beige curtains"
    ],
    "lighting": "Mix of natural daylight and warm artificial vanity lighting"
  },
  "props_and_objects": {
    "cosmetics": [
      "Lip gloss tube",
      "Mascara/Eyeliner tube",
      "Glass perfume bottle with gold cap",
      "Round compact powder"
    ],
    "tech": "Black smartphone",
    "background_props": "Beige silk/satin fabric cloth (in flat lay)"
  },
  "panel_breakdown": {
    "top_row": [
      "Reflection in lit mirror applying makeup",
      "Flat lay of jewelry and cosmetics on marble",
      "Close-up putting on earring near window"
    ],
    "middle_row": [
      "Extreme close-up of earring on ear",
      "Side profile focusing on hair texture and shoulder",
      "Waist-up portrait facing forward near window"
    ],
    "bottom_row": [
      "Portrait touching hair looking away",
      "Reflection in mirror laughing/smiling",
      "Flat lay of earrings on folded beige silk cloth"
    ]
  }
}
```

[[Editorial Photography]] [[Luxury Interior]] [[Mirror Reflection]] [[Satin Dress]]

---

### 188. Toile de Jouy 街头时尚专题报道

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2025-12-22  **Language**: en

> 一个用于生成都市街头时尚大片图像集的 Gemini Nano Banana Pro 提示词。它描述了一位身穿配套的法式印花（toile de jouy）图案牛仔夹克和长裤的女性，重点突出精致的妆容、柔顺的秀发以及带有柔和粉色点缀的单色调配色方案，旨在营造出现代街头风格的美感。

![Toile de Jouy 街头时尚专题报道](https://cms-assets.youmind.com/media/1766667263150_30090l_G8vVFWmWwAAHvOv.jpg)
![Toile de Jouy 街头时尚专题报道](https://cms-assets.youmind.com/media/1766667263829_7lclbz_G8vVFWoXcAA2T2_.jpg)

```
{
  "subject": {
    "person": {
      "gender": "female",
      "facial_features": {
        "eyebrows": "well-defined, arched, dark",
        "eyes": "almond-shaped, dark, featuring dramatic false eyelashes and eyeliner",
        "lips": "full, matte mauve or dusty rose lipstick",
        "makeup": "glamorous, contoured skin, soft pink blush, winged eyeliner"
      },
      "hair": {
        "style": "high ponytail with a sleek, rounded top section (half-up look)",
        "color": "jet black",
        "texture": "straight and smooth"
      },
      "pose": "standing, looking directly at the camera, slight tilt of the head, right hand resting on hip"
    },
    "clothing": {
      "top": "toile de jouy patterned denim jacket, light grey and charcoal, belted waist with a silver buckle, button-up front, structured collar",
      "bottom": "matching toile de jouy patterned trousers",
      "accessories": "small sparkling diamond or crystal stud earrings, light pink manicured nails"
    }
  },
  "environment": {
    "setting": "urban street, upscale residential area",
    "background_elements": [
      "black wrought iron spiked fence",
      "classic cream-colored building facade with arched windows",
      "grey stone pavement",
      "soft natural daylight with mild shadows"
    ]
  },
  "composition": {
    "shot_type": "medium-full shot",
    "framing": "centered subject",
    "lighting": "bright, even outdoor lighting, professional photography style",
    "color_palette": {
      "primary": "monochromatic greys, whites, and blacks",
      "accents": "soft pinks and skin tones"
    },
    "aesthetic": "fashion editorial, street style, polished and modern"
  }
}
```

[[Editorial Photography]] [[Street Fashion Photography]] [[Urban Fashion]]

---

### 189. 坐在扶手椅上与绵羊合影的女性编辑摄影

**Author**: [Ender Mimtaş](https://x.com/endermimtas)  **Date**: 2025-12-16  **Language**: en

> 一个 JSON 提示，指定了用于生成一张社论照片的视觉元素、构图和调色板。场景中，一位女士坐在扶手椅上，背景是带有绵羊的自然景观，利用温暖的黄金时段光线和深景深。

![坐在扶手椅上与绵羊合影的女性编辑摄影](https://cms-assets.youmind.com/media/1766042092737_sxvkk1_G8UihEuXQAMF1hP.jpg)
![坐在扶手椅上与绵羊合影的女性编辑摄影](https://cms-assets.youmind.com/media/1766042092905_uetna0_G8UihFVWcAQlT5l.jpg)

```
{
  "colors": {
    "palette": [
      "#4B4B4B",
      "#8B6C5C",
      "#D9D3C5",
      "#2B3A42",
      "#A59C84"
    ],
    "dominant_colors": {
      "foreground": "#D9D3C5",
      "background": "#A59C84",
      "accents": "#8B6C5C"
    }
  },
  "typography": null,
  "composition": {
    "layout": "Portrait",
    "focal_point": "Central subject (woman in armchair)",
    "framing": "Wide shot, full body view, natural landscape background",
    "depth_of_field": "Deep, with sharp focus on subject and mid-ground sheep, soft background mountains"
  },
  "effects": {
    "lighting": "Warm, golden hour sunlight, soft shadows",
    "atmosphere": "Pastoral, serene, natural, editorial photography",
    "texture": "Fabric of dress, leather of chair and boots, grass, wool of sheep"
  }
}
```

[[Editorial Photography]] [[Golden Hour Light]] [[Deep Depth Of Field]]

---

### 190. 空灵蓝光编辑肖像 (中国语境)

**Author**: [ttmouse](https://x.com/ttmouse)  **Date**: 2025-12-11  **Language**: en

> 一个高度详细、技术性的 JSON 提示，用于生成一位年轻女性的艺术编辑特写肖像。图像的特点是戏剧性的深蓝色照明、一道突出面部轮廓的冷白色对角光束，以及宁静、内省的氛围，并指定了严格的相机设置。

![空灵蓝光编辑肖像 (中国语境)](https://cms-assets.youmind.com/media/1765967705572_e38suy_G757exuagAAjVKY.jpg)

```
{
  "type": "image_generation_prompt",
  "concept": {
    "description": "An artistic editorial close-profile portrait of a young woman, immersed in dramatic blue lighting. Her eyes are closed, with her head gently tilted upward, expressing serenity and introspection. A diagonal beam of cold white light crosses her face, illuminating her eyes, nose, and lips with precise intensity. A solid deep blue background enhances the ethereal, emotional aesthetic.",
    "mood": "quiet, introspective, ethereal",
    "color_theme": "deep blue with cold white highlights"
  },
  "subject": {
    "gender": "female",
    "identity_preservation": {
      "use_reference_image": true,
      "alter_face": false,
      "notes": "Maintain the subject’s exact facial features, structure, skin tone, and identity from the uploaded image."
    },
    "pose": {
      "name": "Blue Profile",
      "head_position": "slightly tilted upward",
      "eyes": "closed",
      "expression": "serene and introspective",
      "highlight": "diagonal beam of light crossing the face, enhancing facial contours"
    },
    "appearance": {
      "hair": {
        "style": "curly, voluminous, well-defined",
        "lighting_effect": "subtle blue reflections"
      },
      "clothing": {
        "shirt": "{argument name=\"shirt description\" default=\"petroleum-blue shirt with light gray micro-geometric print\"}",
        "fabric": "lightweight material with soft shine under direct light",
        "collar": "traditional, top button open to reveal part of the neck",
        "details": {
          "cuffs": "adjusted cuffs",
          "stitching": "visible dark blue stitching",
          "fit": "elegant and modern"
        }
      },
      "accessories": "none visible"
    }
  },
  "camera_settings": {
    "camera": "Canon EOS R5",
    "lens": "85mm f/1.4",
    "aperture": "f/2.2",
    "iso": 320,
    "shutter_speed": "1/200s",
    "framing": "close-up profile, vertical 4:5 format",
    "resolution": "Ultra-HD 8K",
    "focus": "absolute focus on the face, capturing skin texture, hair, and light transitions"
  },
  "lighting": {
    "type": "dramatic cold white diagonal beam",
    "background": "deep solid blue",
    "effects": [
      "precise illumination on eyes, nose, and mouth",
      "soft enhancement of facial contours",
      "editorial contrast and silence-like aesthetic"
    ]
  },
  "visual_style": {
    "genre": "artistic editorial portrait",
    "contrast_level": "medium-high",
    "tone": "cold, atmospheric",
    "keywords": [
      "cinematic",
      "high-fashion",
      "introspective",
      "ethereal"
    ]
  },
  "output_goal": "Create an ultra-realistic editorial portrait of a young woman in dramatic blue lighting, preserving her identity while capturing a serene, introspective moment in close-profile composition."
}
```

[[Editorial Photography]] [[Portrait Photography]] [[Introspective Mood]]

---

### 191. 赛博朋克数字依赖肖像

**Author**: [Heisenberg](https://x.com/rovvmut_)  **Date**: 2025-12-11  **Language**: en

> 一个对比 Nano Banana Pro 和 Grok Imagine 的提示，要求生成一个单色调的数字人，跪在黑暗空间中。主体被连接到头部、四肢和胸部的发光白色电缆缠绕，身穿带有霓虹条纹的未来主义运动服，手持智能手机。风格为社论式、赛博朋克，具有鲜明对比和数字依赖的主题。

![赛博朋克数字依赖肖像](https://cms-assets.youmind.com/media/1765967683033_hgogdc_G75Pxy0a0AAx46C.jpg)
![赛博朋克数字依赖肖像](https://cms-assets.youmind.com/media/1765967683323_hmllja_G75PxWabgAAR0V4.jpg)

```
A monochromatic digital human kneeling in a dark space, wrapped in glowing white cables connected to head, limbs, and chest. Wearing a futuristic tracksuit with neon stripes. Holding a smartphone, staring intensely. Editorial lighting, cyberpunk mood, themes of digital dependence and identity. Stark contrast, surreal atmosphere.
```

[[Editorial Photography]] [[Cyberpunk Aesthetic]] [[Monochrome Portrait]]

---

### 192. 戏剧性蓝光下的编辑肖像

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2025-12-11  **Language**: en

> 一个高度结构化的提示，用于生成一张超现实的女性编辑肖像照。它要求保持主体在参考图像中的身份，并将其置于一个由深蓝色灯光和一道精确的对角线冷白光束所定义的戏剧性环境中，这束光线照亮了她紧闭的双眼和面部轮廓。

![戏剧性蓝光下的编辑肖像](https://cms-assets.youmind.com/media/1765967661222_dlybbk_G75AgEpaUAAQf1g.jpg)

```
{
  "type": "image_generation_prompt",
  "concept": {
    "description": "An artistic editorial close-profile portrait of a young woman, immersed in dramatic blue lighting. Her eyes are closed, with her head gently tilted upward, expressing serenity and introspection. A diagonal beam of cold white light crosses her face, illuminating her eyes, nose, and lips with precise intensity. A solid deep blue background enhances the ethereal, emotional aesthetic.",
    "mood": "quiet, introspective, ethereal",
    "color_theme": "deep blue with cold white highlights"
  },
  "subject": {
    "gender": "female",
    "identity_preservation": {
      "use_reference_image": true,
      "alter_face": false,
      "notes": "Maintain the subject’s exact facial features, structure, skin tone, and identity from the uploaded image."
    },
    "pose": {
      "name": "Blue Profile",
      "head_position": "slightly tilted upward",
      "eyes": "closed",
      "expression": "serene and introspective",
      "highlight": "diagonal beam of light crossing the face, enhancing facial contours"
    },
    "appearance": {
      "hair": {
        "style": "curly, voluminous, well-defined",
        "lighting_effect": "subtle blue reflections"
      },
      "clothing": {
        "shirt": "{argument name="shirt color and pattern" default="petroleum-blue shirt with light gray micro-geometric print"}",
        "fabric": "lightweight material with soft shine under direct light",
        "collar": "traditional, top button open to reveal part of the neck",
        "details": {
          "cuffs": "adjusted cuffs",
          "stitching": "visible dark blue stitching",
          "fit": "elegant and modern"
        }
      },
      "accessories": "none visible"
    }
  },
  "camera_settings": {
    "camera": "Canon EOS R5",
    "lens": "85mm f/1.4",
    "aperture": "f/2.2",
    "iso": 320,
    "shutter_speed": "1/200s",
    "framing": "close-up profile, vertical 4:5 format",
    "resolution": "Ultra-HD {argument name="resolution" default="8K"}",
    "focus": "absolute focus on the face, capturing skin texture, hair, and light transitions"
  },
  "lighting": {
    "type": "dramatic cold white diagonal beam",
    "background": "deep solid blue",
    "effects": [
      "precise illumination on eyes, nose, and mouth",
      "soft enhancement of facial contours",
      "editorial contrast and silence-like aesthetic"
    ]
  },
  "visual_style": {
    "genre": "artistic editorial portrait",
    "contrast_level": "medium-high",
    "tone": "cold, atmospheric",
    "keywords": [
      "cinematic",
      "high-fashion",
      "introspective",
      "ethereal"
    ]
  },
  "output_goal": "Create an ultra-realistic editorial portrait of a young woman in dramatic blue lighting, preserving her identity while capturing a serene, introspective moment in close-profile composition."
}
```

[[Editorial Photography]] [[Face Preservation]] [[Portrait Photography]]

---

### 193. 8K 高级时装电影感人像，暖光呈现

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2025-12-11  **Language**: en

> 一个为 Nano Banana Pro 设计的结构化 JSON 提示，专注于生成一张超现实的 8K 高级时尚肖像。它要求严格保留面部特征，并指定戏剧性的暖红色-橙色电影光照、深邃的阴影，以及主体佩戴大号金边太阳镜。

![8K 高级时装电影感人像，暖光呈现](https://cms-assets.youmind.com/media/1765967747775_123cvl_G7408LkaAAA3sOx.jpg)

```
{
  "Objective": "Create an ultra-realistic 8K high-fashion cinematic portrait of the subject under dramatic warm lighting.",
  
  "Identity_Safety": "Maintain facial features, hairstyle, and overall appearance consistent with the provided reference image without alteration.",
  
  "Subject": {
    "Appearance": {
      "Expression": "Calm and confident",
      "Head_Position": "Turned slightly away from the camera",
      "Eyewear": "Large round gold-rimmed sunglasses obscuring the eyes",
      "Hair": "Styled naturally with realistic texture"
    },
    "Wardrobe": {
      "Style": "High-fashion portrait styling",
      "Accessories": ["Gold-rimmed sunglasses"]
    }
  },

  "Lighting": {
    "Tone": "Intense warm red-orange palette",
    "Type": "Strong directional cinematic lighting",
    "Effects": [
      "Deep dramatic shadows",
      "Bright sculpted highlights",
      "Color-saturated glow enhancing facial structure"
    ]
  },

  "Visual_Style": {
    "Quality": "8K hyper-realistic high-resolution",
    "Aesthetic": "Cinematic high-fashion portrait",
    "Detail_Characteristics": [
      "Natural skin texture and pores",
      "Accurate reflective highlights on sunglasses",
      "Deep shadow separation",
      "Editorial-grade tonal contrast"
    ],
    "Mood": "Bold, stylish, dramatic and fashion-forward"
  },

  "Composition": {
    "Orientation": "Portrait",
    "Framing": "Tight or medium close-up emphasizing the face and lighting",
    "Focus": "Sharp on the subject with strong atmospheric depth"
  },

  "Output_Requirements": {
    "Format": "Image",
    "Resolution": "8K",
    "Style": "High-fashion, cinematic, hyper-realistic"
  }
}
```

[[Editorial Photography]] [[High Fashion Photography]] [[Deep Shadow]]

---

### 194. 8K 企业高端时尚编辑 JSON

**Author**: [𝗦𝗮𝗻𝗶𝗮](https://x.com/saniaspeaks_)  **Date**: 2025-12-10  **Language**: en

> 一个极其详细的 JSON 提示，用于生成一张超逼真的 8K 企业高定时装社论肖像，描绘一位女性高管，重点是 100% 保留参考图像中的面部特征，使用特定的相机设备，并在现代办公室环境中采用柔和的自然窗户光线。

![8K 企业高端时尚编辑 JSON](https://cms-assets.youmind.com/media/1765509721651_pc88x1_G7zUz4Fa4AAFgb2.jpg)
![8K 企业高端时尚编辑 JSON](https://cms-assets.youmind.com/media/1765509722408_ros8l9_G7zUz4JaMAMUNqL.jpg)

```
{
  "type": "image_generation_prompt",
  "style": "cinematic, corporate high-fashion editorial, ultra-realistic",
  "camera": {
    "camera_model": "Canon EOS R5",
    "lens": "RF 85mm f/1.2L USM",
    "film_look": "clean modern digital with subtle Kodak Portra 400 warmth",
    "grain": "very subtle, almost none",
    "color_tones": "crisp neutral tones with soft natural warmth from window light"
  },
  "subject": {
    "gender": "female",
    "identity_preservation": {
      "use_attached_image": true,
      "face_consistency": "100%",
      "alter_face": false,
      "notes": "Maintain exact facial features, proportions, skin texture, eye color, hairstyle, and expressions from the reference image – zero deviation"
    },
    "pose": {
      "stance": "leaning forward elegantly",
      "arms": "both forearms and interlaced hands resting on the back of a light beige ergonomic office chair placed at an angle",
      "torso": "upright, no slouching, confident posture",
      "body_orientation": "viewed from the side",
      "head_position": "turned directly toward the camera",
      "gaze": "straight into lens",
      "emotion": "slight confident smile, poised and self-assured"
    }
  },
  "wardrobe": {
    "outfit_style": "high-end female executive power suit",
    "top": "perfectly tailored blazer in charcoal or deep navy with subtle sheen",
    "bottoms": "matching tailored trousers or pencil skirt",
    "shirt": "crisp white or ivory silk blouse",
    "details": "luxury fabric with natural drape, sharp lines, understated elegance"
  },
  "scene": {
    "location": "luxury modern corporate office",
    "environment": [
      "floor-to-ceiling window with view of contemporary skyscrapers",
      "clean minimalist decor",
      "polished concrete or dark wood floor",
      "light beige ergonomic office chair as main prop"
    ]
  },
  "lighting": {
    "time_of_day": "daytime, soft overcast sky",
    "type": "beautiful soft natural window light mixed with subtle cool office ambient",
    "direction": "side-front from the large window",
    "effects": [
      "gentle rim light outlining hair and shoulders",
      "soft shadows",
      "clean rectangular catchlights in eyes",
      "premium three-dimensional depth"
    ]
  },
  "skin_rendering": {
    "realism": "hyper-realistic 8K",
    "details": "visible natural skin texture, pores, subtle imperfections",
    "retouching": "none – zero airbrushing or artificial smoothing"
  },
  "quality": {
    "resolution": "8K ultra-high",
    "realism": "absolute photorealism, indistinguishable from real photography",
    "detail_level": "professional studio editorial, luxury campaign quality"
  },
  "output_goal": "Create a flawless, ultra-realistic 8K corporate editorial portrait of the exact attached woman as a powerful high-end executive, preserving 100% facial and body identity, shot in a bright modern office with perfect natural window light and impeccable fashion sophis"
}
```

[[Editorial Photography]] [[Face Preservation]] [[Natural Window Light]] [[Office Setting]]

---

### 195. 通用 JSON 模板，适用于编辑产品广告

**Author**: [AI Tales - Not by Humans](https://x.com/AITalesNBH)  **Date**: 2025-12-09  **Language**: en

> 一个为 Nano Banana Pro 设计的综合性 JSON 模板，用于自动生成任何产品的编辑风格广告，且不显示可见的标志。该模板定义了输入要求、图像规格、创意指令、场景生成参数（环境、主体、产品展示）以及广告文案结构。

![通用 JSON 模板，适用于编辑产品广告](https://cms-assets.youmind.com/media/1765440012154_mi78ui_G7wqnaYWQAAfPbg.jpg)

```
{
  "project": "Nano Banana - Universal Product Editorial Ad",
  "version": "1.1",

  "input_requirements": {
    "reference_product_image": {
      "upload_required": true,
      "usage": "extract visual characteristics, color palette, possible target user, and implied purpose"
    },
    "branding_elements": {
      "allowed": false,
      "description": "no visible logos, trademarks, or brand names in the generated result"
    }
  },

  "image_specification": {
    "meta": {
      "clean_generation": true,
      "distraction_free": true
    }
  },

  "creative_directive": {
    "freedom_level": "full_creative_imagination",
    "Nano_Banana_role": "interpret product essence to design the rest of the scene",
    "editorial_intent": "produce a visually compelling advertisement based solely on the product reference"
  },

  "scene_generation": {
    "environment": {
      "type": "indoor_or_outdoor",
      "chosen_by": "best_use_case_for_product",
      "lighting": {
        "selection_method": "depends_on_product_use_case",
        "goal": [
          "enhance product visibility",
          "create a clean editorial mood",
          "support emotional impact"
        ]
      }
    },

    "subject_character": {
      "identity": "derived_from_product_reference",
      "gender": "male_or_female",
      "attributes_selection": [
        "style_inspired_by_product_color_palette",
        "personality_inferred_from_product_category",
        "age_and_vibe_matching_intended_audience"
      ],
      "pose": "chosen_by_creative_engine",
      "interaction_with_product": "natural and meaningful"
    },

    "product_presentation": {
      "visibility": "clear",
      "placement": "hero_position",
      "integration": "harmonized with entire composition"
    }
  },

  "ad_copy": {
    "text": {
      "placement": "editorial_style_overlay",
      "tone": "clean, modern, descriptive",
      "content": "short metaphorical line describing the product’s essence and purpose without naming a brand"
    }
  },

  "render_style": {
    "aesthetic": "editorial_magazine_ad",
    "resolution": "high_detail",
    "color_grading": "optimized_based_on_product_visuals",
    "medium": "photorealistic"
  }
}
```

[[Editorial Photography]] [[Product Advertisement]] [[Prompt Template]]

---

### 196. 杂志风格旅行照片集生成

**Author**: [ttmouse](https://x.com/ttmouse)  **Date**: 2025-12-09  **Language**: zh

> 以下是两组提示词，用于根据指定地点和上传的人物图片生成杂志风格的旅行照片。第一个提示词侧重于封面设计，第二个则侧重于详细的专题页面，两者都强调 100% 的人物面部保真度和精美的 9:16 布局。

![杂志风格旅行照片集生成](https://cms-assets.youmind.com/media/1765440106955_q8g97v_G7ups-ha0AIvBjq.jpg)
![杂志风格旅行照片集生成](https://cms-assets.youmind.com/media/1765440107170_flc52d_G7upt_ka4AAyRxN.jpg)

```
提示词（封面版）

请将指定角色融入到位于  [{argument name="地点" default="上海迪士尼"}] 的实景中，呈现他们在此地观光的场景。务必确保角色本人脸部特征（包括五官、比例等）100% 保留且完整一致。整体排版需如同摄影集般精致，充分利用9:16的画面比例，制作成杂志封面。以“这是能影响游客数量的重要页面”为心态进行打造。

提示词（特辑页面版）
请将指定角色融入到位于 [{argument name="地点" default="上海迪士尼"}] 的实景中，呈现他们在此地观光的场景。务必确保角色本人脸部特征（包括五官、比例等）100% 保留且完整一致。整体排版需如同摄影集般精致，充分利用9:16的画面比例，制作成日本杂志的特辑内容页。以“这是能影响游客数量的重要阅读页面”为心态进行打造，并加入丰富的资讯与细节。
```

[[Editorial Photography]] [[Travel Photography]] [[Magazine Layout]] [[Face Fidelity]]

---

### 197. 别致的深夜街头时尚大片

**Author**: [Sharon Riley](https://x.com/Just_sharon7)  **Date**: 2025-12-09  **Language**: en

> 一个详细的 JSON 提示，用于生成一张年轻女性在城市夜景中的编辑风格照片，重点突出 Kith 风格的特定时尚、氛围感低调照明以及专业时尚摄影般的高分辨率照片细节。

![别致的深夜街头时尚大片](https://cms-assets.youmind.com/media/1765440063144_9u3si7_G7uUjRdasAAqkyY.jpg)
![别致的深夜街头时尚大片](https://cms-assets.youmind.com/media/1765440063140_wf4l6r_G7uUjRnbYAASJfG.jpg)

```
{
  "prompt": "A highly detailed, editorial-style photograph of a young woman standing outdoors at night, possibly in an urban setting like Paris, based on the sophisticated fashion and backdrop. The woman has long, rich dark brown hair styled with loose waves, framing a delicately contoured face with a strong jawline and full, slightly glossy nude-pink lips. Her makeup is refined and natural, featuring defined eyebrows and subtle smokey eyeshadow. She is wearing a light grey heathered quarter-zip sweatshirt, which appears slightly oversized, with a small, embroidered logo (likely 'Kith' based on the style) visible on the left chest. The sweatshirt's collar is partially zipped. Over her shoulders, she has a dark brown or black leather bomber or biker jacket draped, giving a casual yet edgy feel. She is wearing black shorts or a mini-skirt, paired with sheer black hosiery or tights, and possibly over-the-knee boots, though only the tops are clearly visible. Her hands are placed casually into the pockets of the shorts or held near her waist. She carries a black leather handbag, visible on her left arm. The lighting is low-key and atmospheric, with warm yellow light hitting her from the left, highlighting the texture of her hair and clothing, while the background remains dark. The background features a pale, textured building facade on the left and a dark doorway or window on the right, reflecting the ambient streetlights and creating subtle, complex shadows. A small black heart emoji is overlaid near the bottom right of the sweatshirt. The overall mood is chic, confident, and late-night street style. Photographed with a high-resolution, professional camera, reminiscent of fashion photography, perhaps a Canon EOS R5 with an 85mm lens, using available light and subtle fill flash."
}
```

[[Editorial Photography]] [[Street Fashion Photography]] [[Urban Night Photography]]

---

### 198. 电影感街头摄影：标题与视觉风格

**Author**: [Taaruk](https://x.com/Taaruk_)  **Date**: 2025-12-08  **Language**: en

> 一个结构化的 JSON 提示词，旨在创建一张电影感的街头摄影图片，并配以特定、富有深思的标题，用于 Instagram 轮播帖的最后一页。它定义了目标、标题文本、视觉风格（情绪、光线、纹理）和相关标签，强调 Midjourney 风格的真实感和叙事性。

![电影感街头摄影：标题与视觉风格](https://cms-assets.youmind.com/media/1765438557352_84lckc_G7pclp_bIAA5Y-F.jpg)

```
{
  "Objective": "Create a cinematic street-photography inspired final slide caption paired with Midjourney-style realism and storytelling aesthetics.",

  "Caption": {
    "Primary_Text": "In a crowd full of motion, the ones who stand still make the loudest noise. 🎞✨",
    "Description": "Created in Midjourney — cinematic realism that feels alive, where every face becomes a story waiting to be told."
  },

  "Visual_Style": {
    "Theme": "Cinematic street realism",
    "Mood": "Emotional, atmospheric, reflective",
    "Lighting": "Soft filmic contrast with vivid bokeh depth",
    "Aesthetic": "Traveler-inspired realism with expressive human storytelling",
    "Texture": "High clarity, realistic skin details, natural film-like grain",
    "Composition": "Moving urban crowd with a single still subject anchoring the scene"
  },

  "Tags": [
    "midjourney",
    "cinematic realism",
    "ai photography",
    "emotional street portrait",
    "traveler aesthetic",
    "urban crowd art",
    "bokeh depth shot",
    "storytelling image",
    "realistic ai portrait",
    "creative ai generation",
    "moody cinematic visual",
    "viral ai post",
    "travel inspired realism",
    "ai storytelling composition"
  ],

  "Output_Requirements": {
    "Use_Case": "Final slide in an Instagram carousel, cinematic AI-art caption, aesthetic storytelling post",
    "Format": "Caption with associated visual-style metadata",
    "Tone": "Poetic, cinematic, thought-provoking"
  }
}
```

[[Editorial Photography]] [[Street Photography]] [[Cinematic Mood]] [[Text Overlay]]

---

### 199. 大理石楼梯上的高角度时尚肖像

**Author**: [𝙕arᎧon](https://x.com/Zar_xplorer)  **Date**: 2025-11-21  **Language**: en

> 一张详细的时尚肖像提示，描绘一位亚洲男模特倚靠在大理石楼梯上，保留参考对象的面部特征，并指定发型、服装和姿势，非常适合编辑风格的拍摄或个人资料图片。

![大理石楼梯上的高角度时尚肖像](https://cms-assets.youmind.com/media/1764209332870_azbk15_G6P-AKiacAAf0BH.jpg)

```
High-angle fashion portrait of a {argument name="age" default="25-year-old"} {argument name="ethnicity" default="Asian"} man, with the
same facial features as the man in the reference photo, messy hairstyle framed on his face, leaning casually on a
{argument name="stair_material" default="white marble"} staircase banister. He is wearing an oversized {argument name="shirt_colors" default="light blue and white"} plaid shirt over a
```

[[Editorial Photography]] [[Fashion Portrait]] [[High Angle Shot]]

---

### 200. 超逼真名人团体封面大片

**Author**: [eijo](https://x.com/eijo_AIart)  **Date**: 2025-11-20  **Language**: en

> 一个提示，用于生成一张超现实的大画幅编辑风格合影，其中包含来自不同时代的众多名人，其布光和构图如同电影杂志封面。

![超逼真名人团体封面大片](https://cms-assets.youmind.com/media/1763886355130_0kcbd4_G6Oxvk-acAEcFvW.jpg)

```
Create a hyper-realistic, ultra-sharp, full-color large-format image featuring a massive group of celebrities from different eras, all standing together in a single wide cinematic frame. The image must look like a perfectly photographed editorial cover with impeccable lighting.
```

[[Editorial Photography]] [[Magazine Cover Design]]

---

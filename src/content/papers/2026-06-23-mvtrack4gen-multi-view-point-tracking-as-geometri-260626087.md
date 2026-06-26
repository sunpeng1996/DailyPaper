---
title: 'MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video
  Generation'
title_zh: 'MVTrack4Gen: Multi-View Point Tracking as Geometri'
authors:
- JoungBin Lee
- Jaewoo Jung
- Jongmin Lee
- Tongmin Kim
- Hyunsung Kim
- Takuya Narihira
- Kazumi Fukuda
- Jahyeok Koo
- Jisang Han
- Yuki Mitsufuji
arxiv_id: '2606.26087'
url: https://arxiv.org/abs/2606.26087
pdf_url: https://arxiv.org/pdf/2606.26087
published: '2026-06-23'
collected: '2026-06-26'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: Synthesizing a novel-view video from a monocular reference video along
  a target camera trajecto...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: huggingface-daily
depth: abstract
---

### 摘要

Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

---
title: 'Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation'
title_zh: Vidu S2：支持实时交互、可编辑的空间视频生成系统
authors:
- Jintao Zhang
- Kai Jiang
- Jintao Chen
- Xu Wang
- Deyuan Liu
- Jungang Li
- Dechuang Chen
- Ming Lin
- Jingjiang Zhou
- Haopeng Jin
affiliations:
- Tsinghua University
- Shengshu Technology
arxiv_id: '2609.11638'
url: https://arxiv.org/abs/2609.11638
pdf_url: https://arxiv.org/pdf/2609.11638
published: '2026-09-10'
collected: '2026-09-12'
category: Multimodal
direction: 多模态生成 · 实时视频生成与编辑
tags:
- Video Generation
- Real-time AI
- Video Editing
- Digital Avatar
- Spatial Video
one_liner: 推出集成实时数字人、实时视频编辑模块的Vidu S2，支持720P实时空间视频生成，性能超所有基线
practical_value: '- 电商虚拟试穿、数字人直播场景可复用实时视频流编辑框架，实现服装、背景的毫秒级替换，降低直播内容制作与运营成本

  - 商品短视频批量生产场景可参考动态参考实时更新的生成逻辑，快速生成多规格、多风格的商品展示视频，大幅提升内容供给效率

  - 个性化短视频推荐链路可引入实时交互生成范式，支持用户边看边调整视频内容元素，显著提升用户留存与内容消费时长'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有主流视频生成模型均采用离线单轮生成范式，用户输入prompt后需等待数分钟至数十分钟才能获得完整视频，过程中无法交互调整，无法适配直播、互动内容创作等实时场景需求。
### 方法关键点
Vidu S2包含两大核心组件：1）Vidu S2-Avatar实时交互数字人模型，支持任意时刻更新的动态参考输入，指令跟随能力更强；2）Vidu S2-Editing实时视频流编辑模型，支持风格渲染、虚拟试穿、人物替换、背景替换等操作，同时探索了两大模块的实时空间视频生成能力。
### 关键结果数字
- 相比Vidu S1，Avatar模块支持720p实时视频生成，可实现跳舞等复杂指令跟随
- 整体模型性能优于所有对比基线，已上线可交互在线Demo

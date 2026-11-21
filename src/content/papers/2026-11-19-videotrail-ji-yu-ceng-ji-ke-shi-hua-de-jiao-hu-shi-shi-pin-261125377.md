---
title: 'VideoTrail: Interactive Video Foraging Through Hierarchical Visualization'
title_zh: VideoTrail：基于层级可视化的交互式视频信息探寻系统
authors:
- Catherine Yeh
- Bryan Wang
- Fernanda Viégas
- Martin Wattenberg
affiliations:
- Harvard University
- Adobe Research
- Google DeepMind
arxiv_id: '2611.25377'
url: https://arxiv.org/abs/2611.25377
pdf_url: https://arxiv.org/pdf/2611.25377
published: '2026-11-19'
collected: '2026-11-21'
category: Multimodal
direction: 多模态交互 · 视频内容定向导航
tags:
- Multimodal
- Information Foraging
- Interactive Visualization
- Video Navigation
- User Experience
one_liner: 基于信息觅食理论打造多模态自适应层级可视化插件，提升视频定向内容查找效率
practical_value: '- 电商直播/短视频场景可复用层级语义分段逻辑，为用户提供可直接跳转的卖点片段导航，降低用户检索商品信息的时间成本

  - 借鉴信息觅食理论的 information scent 设计思路，给推荐的内容/商品附加高价值语义标签（如核心卖点、适配场景），提升用户决策效率

  - 自适应多模态线索优先级策略可复用到多模态内容理解场景，根据内容类型动态优先展示文本/视觉特征，降低用户信息获取成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
用户从长视频、直播中定位目标片段效率极低，现有拖拽进度条等线性查找方式仅依赖视觉扫描，缺乏定向导航的有效支持，难以满足目标导向的内容查找需求。
### 方法关键点
1. 受信息觅食理论启发，将视频语义、结构线索作为 information scent，生成可交互的层级分段路线图，每个分段附带标题、关键帧、摘要、语义维度色带
2. 采用多模态自适应设计，可根据视频内容类型动态调整视觉或文本 scent 的展示优先级
3. 实现为浏览器插件，支持用户层级展开分段、点击直接跳转对应视频时间点
### 关键结果
16人用户研究表明，相比传统时间轴，VideoTrail可帮助用户高效定位关键片段，同时支持更多新型导航策略

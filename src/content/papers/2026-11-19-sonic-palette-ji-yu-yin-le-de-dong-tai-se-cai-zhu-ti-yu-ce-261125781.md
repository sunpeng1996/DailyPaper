---
title: 'Sonic Palette: Predicting Dynamic Color Themes from Music'
title_zh: Sonic Palette：基于音乐的动态色彩主题预测框架
authors:
- Wen-Li Wei
- Kenneth Yang
- Jen-Chun Lin
affiliations:
- Institute of Information Science, Academia Sinica
- Graduate Institute of Communication Engineering, National Taiwan University
arxiv_id: '2611.25781'
url: https://arxiv.org/abs/2611.25781
pdf_url: https://arxiv.org/pdf/2611.25781
published: '2026-11-19'
collected: '2026-11-22'
category: Multimodal
direction: 跨模态音画生成 · 时序色彩预测
tags:
- Cross-modal
- Transformer
- Sequence Prediction
- Multimodal Generation
- Creative AI
one_liner: 提出音乐条件驱动的自回归Transformer框架，实现随音频演化的动态色彩主题序列预测
practical_value: '- 可直接复用到电商短视频/直播场景，根据配乐自动生成适配的动态色彩滤镜，提升内容视觉吸引力与点击转化率

  - 跨模态条件自回归Transformer建模时序关联的思路，可迁移到用户行为序列预测、动态兴趣召回等推荐任务

  - 音画时序配对数据集的构建逻辑，可参考用于多模态内容标签标注、跨模态检索数据集生产'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音乐转色彩方案仅输出静态调色板，无法匹配音乐随时间变化的节奏、情绪特征，难以支撑动态音画联动的创意生产需求。
### 方法关键点
将音-色对应关系建模为跨模态序列预测任务，采用音乐条件驱动的自回归Transformer逐帧输出包含5个主色的色彩主题；构建覆盖265个官方完整版MV的音色配对时序数据集支撑模型训练；配套调色板引导的重着色流程，保留图像结构的同时呈现与音乐同步的动态色彩效果。
### 关键结果
定量评估中预测色彩主题与ground truth匹配度显著优于静态基线；主观测评显示时序色彩过渡自然度、音色氛围匹配感知度均更优。

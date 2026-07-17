---
title: 'SceneBind: Binding What and Where Across Vision, Audio and Language'
title_zh: SceneBind：跨视觉、音频、语言模态绑定场景语义与空间信息
authors:
- Mingfei Chen
- Zijun Cui
- Ruoke Zhang
- Hyeonggon Ryu
- Eli Shlizerman
affiliations:
- University of Washington
- University of Texas at Dallas
- Hankuk University of Foreign Studies
arxiv_id: '2607.15265'
url: https://arxiv.org/abs/2607.15265
pdf_url: https://arxiv.org/pdf/2607.15265
published: '2026-07-16'
collected: '2026-07-17'
category: Multimodal
direction: 多模态场景表示 · 语义空间联合建模
tags:
- Omni-modal Representation
- 3D Spatial Understanding
- Cross-modal Retrieval
- Object Grounding
- Multimodal Pre-training
one_liner: 提出融合语义与3D空间感知的视音语多模态场景表示框架SceneBind，性能达SOTA
practical_value: '- 多模态商品/内容召回场景可复用「全局语义embedding+对象级空间slot」的轻量建模方案，仅新增少量token即可在现有预训练编码器基础上叠加空间感知能力

  - 跨模态检索任务可借鉴语义-空间匹配机制，融合全局相似度与细粒度对象对齐结果，提升检索准确率

  - 线下门店/AR试穿/3D商品展示场景可复用跨模态语义空间对齐的训练协议，支撑音视语多模态内容的空间定位需求'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多模态编码器仅擅长实例级语义识别（是什么），缺乏显式3D空间结构感知（在哪里），无法支撑需要空间理解的跨模态场景检索、对象定位等任务。

### 方法关键点
1. 提出SceneBind多模态场景表示，将每个场景建模为语义-空间实体，融合全局语义embedding与对象中心的语义-空间slot，显式捕捉对象级语义、空间属性与不确定性；
2. 配套SceneBind Matching语义-空间匹配机制，融合全局场景相似度与对象对齐结果，支持跨模态检索与对象grounding；
3. 兼容现有大规模预训练语义编码器，仅新增少量token实现轻量空间建模，同时构建了带结构化语义与空间标注的真实双耳音视频数据集支撑训练评估。

### 关键结果
在场景检索、空间检索任务上达到SOTA，在音视频定位等下游任务上实现优异的零样本迁移效果。

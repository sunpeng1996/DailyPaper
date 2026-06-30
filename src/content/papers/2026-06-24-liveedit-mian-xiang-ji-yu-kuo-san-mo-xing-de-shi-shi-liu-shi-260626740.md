---
title: 'LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing'
title_zh: LiveEdit：面向基于扩散模型的实时流式视频编辑
authors:
- Xinyu Wang
- Chongbo Zhao
- Fangneng Zhan
- Yue Ma
affiliations:
- THU
- HKUST
arxiv_id: '2606.26740'
url: https://arxiv.org/abs/2606.26740
pdf_url: https://arxiv.org/pdf/2606.26740
published: '2026-06-24'
collected: '2026-06-30'
category: Other
direction: 实时视频编辑 · 扩散模型效率优化
tags:
- diffusion model
- video editing
- knowledge distillation
- mask cache
- real-time inference
one_liner: 提出三阶段知识蒸馏+AR导向掩码缓存，实现稳定低延迟实时流式视频编辑
practical_value: '- 局部修改类场景可复用mask cache思路，复用非修改/不变区域的计算，大幅降低实时推理延迟，可用于电商商品图实时编辑、图文广告局部修改等场景

  - 三阶段渐进蒸馏可将双向大模型的能力迁移到高效单向流式模型，兼顾效果和推理效率，适合把通用大模型能力落地到端侧/实时业务场景

  - 流式序列任务中，因果逐步处理配合知识蒸馏可保证长序列输出稳定性，可借鉴到流式推荐用户建模、实时对话Agent等场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有流式视频编辑落地受两个核心瓶颈限制：一是长时间编辑难以维持背景和非编辑区域的时序稳定性，二是难以满足实时交互场景的低延迟要求。现有流式视频生成方法针对生成任务设计，无法满足编辑的严格内容保留、区域控制需求，无法直接复用。

### 方法关键点
1. 设计三阶段渐进蒸馏流水线，逐步将双向大基础模型的编辑能力迁移到高效单向流式编辑器，兼顾长时序编辑稳定性和视觉保真度；
2. 提出AR-oriented mask cache机制，跨帧复用编辑区域相关计算，消除冗余处理加速推理；
3. 构建了首个流式视频编辑专属基准测试集。

### 关键结果
在现有流式基线中达到SOTA视觉质量，推理速度提升至12.66 FPS，满足交互式AR应用的实时性要求

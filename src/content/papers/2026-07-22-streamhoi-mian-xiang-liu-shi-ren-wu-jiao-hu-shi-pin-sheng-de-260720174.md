---
title: 'StreamHOI: Interaction-aware Temporal Memory Adaptation for Streaming HOI
  Video Generation'
title_zh: StreamHOI：面向流式人-物交互视频生成的交互感知时序记忆适配
authors:
- Zejing Rao
- Haoxian Zhang
- Xiaoqiang Liu
- Yiping Meng
- Guoxin Zhang
- Pengfei Wan
- Fan Tang
- Tong-Yee Lee
arxiv_id: '2607.20174'
url: https://arxiv.org/abs/2607.20174
pdf_url: https://arxiv.org/pdf/2607.20174
published: '2026-07-22'
collected: '2026-07-23'
category: Multimodal
direction: 多模态生成 · 流式HOI视频生成
tags:
- Streaming Generation
- Human-Object Interaction
- Diffusion Transformer
- Temporal Memory
- Low Latency
one_liner: 提出低延迟流式HOI视频生成框架StreamHOI，通过时序记忆适配提升长视频生成效率与交互合理性
practical_value: '- 可借鉴分块偏好画像+专属训练的思路，优化流式生成场景下不同Transformer块的KV cache配置，降低生成延迟，适配直播/实时交互业务需求

  - 记忆距离缩放模块可迁移至长序列生成任务（如电商直播脚本连续生成、长会话Agent记忆管理），强化早期关键信息的访问效率，提升序列一致性

  - 离线感知画像+偏置引导训练的范式可复用在对交互一致性要求高的生成场景（如虚拟人直播带货的动作连贯生成），降低生成内容的割裂感'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有HOI（人-物交互）视频生成多采用离线短视频范式，驱动条件复杂，无法满足虚拟人直播、Embodied Agent交互等实时场景的低延迟长视频生成需求。
### 方法关键点
1. 针对标准sink-local记忆设计的效果-效率权衡问题，先执行离线HOI感知的Transformer块画像，匹配不同块对HOI区域、周边区域的差异化历史记忆偏好
2. 采用偏置引导的记忆专属训练，让生成器适配块特定的记忆布局，平衡交互保留与延迟约束
3. 新增记忆距离缩放模块，强化对早期交互状态的长程访问能力，提升长视频的交互一致性
### 关键结果
相比长视频基线与HOI生成SOTA方法，在交互合理性、物体保真度、人物生成质量上均表现优异，推理速度达17.6 FPS，首块生成延迟仅0.75s

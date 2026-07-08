---
title: 'Wan-Streamer v0.2: Higher Resolution, Same Latency'
title_zh: Wan-Streamer v0.2：保持延迟不变的高分辨率音视频交互模型
authors:
- Lianghua Huang
- Zhi-Fan Wu
- Yupeng Shi
- Wei Wang
- Mengyang Feng
- Junjie He
- Chen-Wei Xie
- Yu Liu
- Jingren Zhou
- Ang Wang
affiliations:
- Alibaba Group Wan Team
arxiv_id: '2607.04443'
url: https://arxiv.org/abs/2607.04443
pdf_url: https://arxiv.org/pdf/2607.04443
published: '2026-07-04'
collected: '2026-07-08'
category: Multimodal
direction: 多模态实时音视频交互模型优化
tags:
- Multimodal Interaction
- Real-time Generation
- KV Cache
- Distributed Inference
- Video Generation
one_liner: 采用thinker-performer拆分架构，在保持200ms模型侧延迟的前提下大幅提升输出视频分辨率
practical_value: '- 大计算量生成任务可复用thinker-performer拆分架构：低延迟单GPU路径跑感知、语言逻辑、缓存构建，多GPU并行跑高成本生成任务，既控延迟又提效果

  - 高成本长序列生成（如高清视频、长文本生成）可采用预分片KV缓存+序列分块并行计算方案，降低跨卡通信 overhead

  - 实时交互类Agent（如电商直播数字人、客服数字人）优化时可优先把算力倾斜到生成侧，逻辑侧保持轻量单卡路径，平衡体验与成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
实时音视频交互Agent（如数字人）原有模型输出分辨率低，人物姿态、手部动作、周边物品展示模糊，直接提升分辨率会导致延迟上升，破坏实时交互体验。

### 方法关键点
1. 保持原有模型范式不变，拆分推理架构为单GPU的thinker路径+多GPU的performer路径：thinker负责流感知、短语言/状态Transformer计算、生成缓存构建与最终解码，走低延迟通路；performer采用Ulysses风格上下文并行组，负责高成本的下一个单元隐变量生成。
2. KV缓存预分片到performer各卡本地，长高清视频隐序列跨卡拆分去噪后通过Ulysses通信聚合，短音频隐序列无需分片直接生成，仅传递KV作为条件避免额外语言序列通信开销。

### 关键结果
模型侧25FPS下信号到信号延迟保持约200ms，输出分辨率从192×336提升到640×368；包含350ms双向网络开销的端到端远程交互延迟约550ms，支撑中景数字人姿态、视线、手部动作、周边物品与场景布局的清晰实时展示。

---
title: 'MiniWorld: Democratizing the Training of Video World Models from Scratch'
title_zh: MiniWorld：从零训练视频世界模型的轻量可复现框架
authors:
- Yian Zhao
- Ruochong Zheng
- Hongcan Guo
- Yu Yan
- Jian Zhang
- Jie Chen
affiliations:
- Peking University
arxiv_id: '2608.01127'
url: https://arxiv.org/abs/2608.01127
pdf_url: https://arxiv.org/pdf/2608.01127
published: '2026-08-01'
collected: '2026-08-06'
category: Agent
direction: 具身Agent 视频世界模型训练优化
tags:
- Video World Model
- Diffusion Transformer
- Flow Matching
- KV Cache
- Embodied AI
one_liner: 提出低算力可复现的视频世界模型训练框架MiniWorld，单8卡数天即可完成从零训练
practical_value: '- 做3D商品交互预览、电商虚拟导购Agent仿真场景的团队，可直接复用MiniWorld的低算力训练方案，大幅降低视频世界模型落地成本

  - 推理侧rolling KV cache + 流水线异步去噪的优化trick，可迁移到流式商品短视频生成、GenRec流式内容生成场景，提升推理效率

  - 块因果Video Diffusion Transformer + 两阶段续训的架构设计，可复用在用户动作触发的交互式广告生成、动态内容推荐任务中'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频世界模型多依赖预训练模型微调/蒸馏，训练管线复杂、算力需求高，且存在双向预训练与因果流式推理的适配差问题，缺乏低算力、可复现的从零训练基线。
### 方法关键点
1. 架构采用预训练Video VAE隐空间下的块因果Video Diffusion Transformer，基于Flow Matching训练；
2. 结合Diffusion Forcing，用分块非递减噪声调度+两阶段续训优化时序建模能力与训练稳定性；
3. 推理侧融合rolling KV cache与流水线异步去噪，实现有限算力下的高效流式生成。
### 关键结果
整套模型可在单8-GPU服务器上数天内完成训练，已开源全量代码、预训练权重与实现细节。

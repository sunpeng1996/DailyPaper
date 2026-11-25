---
title: On-Policy Codec Distillation for Efficient All-in-One Video Generation
title_zh: 同策略编码蒸馏实现高效多条件全场景视频生成
authors:
- Boyang Wang
- Kevin Blackburn-Matzen
- Oindrila Saha
- Matheus Gadelha
- Zezhou Cheng
affiliations:
- Adobe Research
- University of Virginia
arxiv_id: '2611.31184'
url: https://arxiv.org/abs/2611.31184
pdf_url: https://arxiv.org/pdf/2611.31184
published: '2026-11-22'
collected: '2026-11-25'
category: Training
direction: 生成模型效率优化 · token剪枝与蒸馏
tags:
- Token Pruning
- Knowledge Distillation
- DiT Adapter
- KV Cache
- Video Generation
one_liner: 结合视频编解码token剪枝与同策略自蒸馏，实现视频生成多倍提速降显存且无质量损失
practical_value: '- 多模态输入的冗余token剪枝思路可直接迁移到LLM4Rec/生成式广告场景，裁剪用户历史行为、物品属性冗余token，降低推理时延

  - on-policy自蒸馏训练轻量Adapter的方案可复用，无需重训基座大模型，仅需少量数据即可对齐剪枝后的token分布，落地成本极低

  - KV cache显存优化的结论可复用在大模型推理服务中，高并发推荐/广告生成场景下显存占用最高可降低70%以上'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前多条件输入的视觉生成模型中，条件token占计算成本的比例极高，大量冗余时空信息导致推理慢、显存占用大，是工业落地的核心瓶颈。
### 方法关键点
1. 借鉴传统视频编解码识别新增信息的思路，设计条件token剪枝方法，直接丢弃冗余时空token；
2. 配套on-policy self-distillation（OPSD）策略，仅训练DiT轻量Adapter即可学习剪枝后的token分布，无需重训基座，无生成质量损失。
### 关键结果
平均剪枝66%条件token，无明显生成质量下降；去噪速度提升2倍，KV cache模式下显存最高降低73%；可扩展到16种条件模态的SOTA图像/视频生成模型，更高分辨率、更长帧、更多条件下收益更显著，极端场景最高提速8.4倍。

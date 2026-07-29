---
title: 'AngelSpec: Towards Real-World High Performance Inference with Speculative
  Decoding'
title_zh: AngelSpec：面向真实场景高性能推理的投机解码框架
authors:
- Hong Liu
- Rui Cen
- Junhan Shi
- Guangshuo Qin
- Jiebin Zhang
- Tianyu Liu
- Runzhi Fan
- Guoliang Zhao
- Ruobing Xie
- Kai Zhang
affiliations:
- Tencent Inc.
arxiv_id: '2607.25852'
url: https://arxiv.org/abs/2607.25852
pdf_url: https://arxiv.org/pdf/2607.25852
published: '2026-07-28'
collected: '2026-07-29'
category: LLM
direction: LLM推理优化 · 投机解码加速
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Multi-Token Prediction
- Block Diffusion
- Throughput Optimization
one_liner: 针对跨场景负载差异优化投机解码训练与推理，最高实现2.4倍自回归解码速度提升
practical_value: '- 电商/Agent类LLM服务可按负载类型匹配Drafter：高熵对话/导购咨询场景用MTP Drafter，代码/结构化内容生成场景用DFly块扩散Drafter，兼顾吞吐与输出一致性

  - 训练多token预测模块可复用TTT+接受度对齐蒸馏方案，配合目标模型生成的对齐数据集，可提升10%+的token接受率，降低推理时延

  - 高并发LLM服务可落地D-cut动态验证机制，按token置信度排序分配验证算力，高负载下可提升15%+吞吐，仅损失不到2%的接受长度

  - 落地投机解码无需追求通用Drafter，按业务场景细分训练轻量专用Drafter的性价比远高于单一大模型适配全场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有投机解码方案普遍训练通用Drafter适配平均负载，但真实业务请求覆盖开放对话、代码生成、数学推理等多场景，输出分布的熵与结构差异极大，单一Drafter结构无法在所有场景下实现最优加速，导致LLM推理成本高、并发上限低。

### 方法关键点
- 训练层分场景定制Drafter：高熵对话场景用对话数据优化自回归MTP Drafter，代码/数学等强结构场景用代码/数学数据增强的DFly块扩散Drafter
- DFly架构优化：混合目标条件骨干融合全局特征与层专属特征，搭配前置条件自回归头，提升块内依赖建模能力同时保留并行生成高吞吐
- 推理层引入D-cut动态验证：将验证算力作为批次级共享资源，按各请求token置信度排序分配，结合在线负载与硬件成本模型自适应调整验证深度，避免算力浪费
- 开源AngelSpec统一训练框架，支持MTP与块并行投机解码的分布式训练、接受度评估等全流程能力

### 关键结果
在Hy3-A21B模型上测试，DFly相比自回归解码实现1.98~2.40倍速度提升，吞吐比现有方案DFlash高10.5~11.8%；在腾讯生产流量上，D-cut在64并发高负载场景下相比纯DFly再提升15.7%吞吐，仅损失1.5%的平均接受长度。

> 最值得记住的结论：投机解码的最优效果不依赖通用强Drafter，按业务负载分场景定制轻量Drafter+动态调度算力，能以极低的成本获得翻倍的推理加速收益

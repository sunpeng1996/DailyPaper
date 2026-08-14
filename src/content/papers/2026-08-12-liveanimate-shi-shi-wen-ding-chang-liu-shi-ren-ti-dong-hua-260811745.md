---
title: 'LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time'
title_zh: LiveAnimate：实时稳定长流式人体动画生成系统
authors:
- Yuxuan Zhang
- Haozhong Xiong
- Yubo Huang
- Jiayi Song
- Jinpeng Yu
- Haofan Wang
- Jiaming Liu
- Ruihua Huang
- Liwei Wang
affiliations:
- The Chinese University of Hong Kong
- Qwen Applications Business Group of Alibaba
- Liblib AI
arxiv_id: '2608.11745'
url: https://arxiv.org/abs/2608.11745
pdf_url: https://arxiv.org/pdf/2608.11745
published: '2026-08-12'
collected: '2026-08-14'
category: Other
direction: 实时长视频生成 · 流式Diffusion推理优化
tags:
- Diffusion Transformer
- KV cache
- Real-Time Generation
- Streaming Inference
- Video Synthesis
one_liner: 基于14B参数量视频DiT的实时长流式人体动画系统，实现20FPS推理且长序列质量稳定
practical_value: '- PR-Sink bounded KV-cache机制可迁移到长序列生成式推荐场景，解决长序列推理内存、latency随长度上涨的问题，适配需保留历史用户/商品特征的流式推荐需求

  - 两阶段蒸馏将扩散模型采样步压缩至3步的方法，可复用在Diffusion-based GenRec的实时推理优化中，大幅降低生成响应延迟

  - 静态锚点+动态召回历史上下文的注意力设计，可用于Agent长会话上下文管理，无需存储全量会话即可还原关键历史信息

  - 块级因果自回归生成+序列并行+算子融合的工程优化方案，可参考用于大模型流式推荐服务的性能提速'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
姿态驱动人体动画是直播、虚拟数字人等交互场景的核心技术，现有扩散方案推理延迟高、长序列生成质量劣化严重，无法满足实时交互要求。

### 方法关键点
1. 基于14B参数量视频DiT架构，两阶段训练：先通过参考锚定的教师强制适配把预训练双向DiT改造成块级因果自回归生成器，再通过块级自强制蒸馏将采样步压缩到3步；
2. 提出Pose-Retrieval Sink Attention（PR-Sink）bounded KV-cache机制，由永久锚定初始块的静态槽、姿态召回的动态历史槽、3槽滚动窗口组成，无需保留全序列即可还原重复姿态对应的外观上下文，内存和单块延迟不随流长度增长；
3. 配合Ulysses序列并行和算子融合优化推理性能。

### 关键结果
2张H100上推理速度达19.63FPS；3分钟长序列生成中，从首30秒到最后1分钟感知质量和人物ID几乎无衰减，远优于现有方案

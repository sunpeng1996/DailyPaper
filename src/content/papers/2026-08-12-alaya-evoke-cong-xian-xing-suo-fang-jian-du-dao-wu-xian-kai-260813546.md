---
title: 'Alaya-EVOKE: From Linear-Scaling Supervision to Endless World'
title_zh: Alaya-EVOKE：从线性缩放监督到无限开放世界生成
authors:
- Yuanyang Yin
- Gongxuan Wang
- Yifan Zhan
- Chuanhao Li
- Kaipeng Zhang
- Feng Zhao
affiliations:
- MoE Key Lab of BIPC, USTC
- Shanghai Innovation Institute
- Alaya Lab
arxiv_id: '2608.13546'
url: https://arxiv.org/abs/2608.13546
pdf_url: https://arxiv.org/pdf/2608.13546
published: '2026-08-12'
collected: '2026-08-15'
category: Other
direction: 交互世界模型 · 长序列生成优化
tags:
- World Model
- Long-Horizon Generation
- External Memory
- Sparse Attention
- Low-Latency Inference
one_liner: 通过外置世界状态库与长视程专用教师模型，实现低延迟高记忆的开放式交互世界模型
practical_value: '- 长对话/交互类Agent场景可复用外置记忆库思路：按会话维度索引历史状态，仅召回当前请求相关上下文，控制KV cache与模型上下文长度，解决长会话延迟飙升问题

  - 长序列生成类任务（如电商长短视频生成、用户行为序列建模）可借鉴稀疏注意力+分块分组+远程帧检索方案，在控制计算成本线性增长的同时保留长程依赖建模能力

  - 少步蒸馏方案可迁移至高实时性要求的生成场景：用长序列能力强的大模型做教师蒸馏出少步学生模型，兼顾生成质量与响应速度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
交互世界模型需同时满足持久记忆、低延迟交互、长视程生成三个要求，现有方案将历史存储在denoiser上下文或KV cache会导致成本随会话长度线性增长，且少步低延迟生成的能力受教师模型上限限制。

### 方法关键点
1. 外置持久化世界状态库，按相机索引场景几何信息，仅召回当前视图相关内容，保证会话增长时denoiser上下文长度可控
2. 专门设计长视程监督教师模型：稀疏attention结合分块分组、远程帧检索、线性attention全局状态，实现内存与计算线性增长
3. 采用30秒分布匹配目标+自强制滚动，将能力蒸馏到无CFG的3步学生模型，抗长期漂移的同时保留响应速度

### 关键结果
单H200上384×640分辨率下，1.5s内容块生成耗时2.11s；WBench上取得SOTA，VBench-Long、VBench-2.0上性能具备竞争力

---
title: 'REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding'
title_zh: REAL损失：针对投机解码的真实预期接受长度优化方法
authors:
- Yu Tian
affiliations:
- The University of Hong Kong
arxiv_id: '2611.14399'
url: https://arxiv.org/abs/2611.14399
pdf_url: https://arxiv.org/pdf/2611.14399
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: LLM推理加速 · 投机解码训练损失优化
tags:
- Speculative Decoding
- Training Loss
- LLM Inference
- Expected Acceptance Length
- Unbiased Estimation
one_liner: 通过无偏路径估计与方差缩减实现投机解码草稿模型的预期接受长度直接优化
practical_value: '- 业务中使用LLM做生成式推荐文案、Agent工具调用响应、实时搜索Query改写等低延迟场景时，可直接集成REAL loss训练投机解码小草稿模型，无需修改架构即可提升推理速度、降低部署成本

  - 做多步序列级优化目标（比如多轮对话、长文案生成的指标优化）时，可复用路径权重校正分布偏差、Rao–Blackwellization降方差的方法论，避免边际乘积代理目标导致的梯度反向问题

  - 对温度较高的生成场景（比如个性化推荐理由生成、创意文案生成），优先采用REAL训练的草稿模型做概率式投机解码，接受长度相对WTV基线提升约1.6%，服务吞吐更高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
投机解码是LLM低延迟推理的主流方案，加速比完全由预期接受长度（EAL）决定。传统CE、KL等训练目标仅做token级分布匹配，近年的块级优化目标均为EAL的代理函数，存在协方差偏差，甚至会出现梯度方向反转问题，导致训练目标与推理指标脱节，亟需可直接无偏优化EAL的训练损失。
### 方法关键点
- 推导现有WTV等代理目标的偏差来源为路径权重与后续接受率的协方差，明确梯度反转的理论成因
- 基于路径权重校正实现无偏EAL估计，在目标模型采样轨迹上对每个token加权`min(1, q(yi)/p(yi))`，还原真实的提议-接受分支分布
- 引入Rao–Blackwellization对每个项的最后一步做边际化，保留无偏梯度的同时将聚合梯度方差降低52~58%
- 最终REAL损失加入辅助CE项稳定训练，仅需修改训练损失，无需改动草稿模型架构与推理流程，无额外开销
### 关键实验结果
以Qwen3.6-35B-A3B MoE为目标模型、Domino为草稿模型，在9个任务子集（含HumanEval、GSM8K、RAG等）对比WTV、VSD、DBLast、静态LK等基线：
- 概率式服务场景下REAL接受长度达4.792，领先所有基线（基线最高4.749），温度1.0场景下优势最显著
- 跨温度泛化性优于无RB的变体，训练收益随epoch增加持续累积，无早期饱和问题
### 核心结论
多步序列优化目标不能直接用边际概率乘积作为代理，否则会因分支依赖的协方差偏差导致梯度反向，先乘后平均的路径加权是无偏估计的核心

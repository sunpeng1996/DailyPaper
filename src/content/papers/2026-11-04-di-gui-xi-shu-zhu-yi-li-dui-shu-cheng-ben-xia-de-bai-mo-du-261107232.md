---
title: 'Recursive Sparse Attention: Million-Token Length Extrapolation at Logarithmic
  Cost'
title_zh: 递归稀疏注意力：对数成本下的百万Token长度外推
authors:
- Ruitian Wang
- Xinyu Yang
- Minshen Zhang
- Hao Zhang
affiliations:
- University of California, San Diego
- Carnegie Mellon University
arxiv_id: '2611.07232'
url: https://arxiv.org/abs/2611.07232
pdf_url: https://arxiv.org/pdf/2611.07232
published: '2026-11-04'
collected: '2026-11-06'
category: LLM
direction: LLM长上下文 · 稀疏注意力优化
tags:
- Sparse Attention
- Long Context
- KV Cache
- RoPE
- Length Extrapolation
one_liner: 提出仅需短序列训练的递归稀疏注意力，实现对数成本的百万token上下文外推
practical_value: '- 长上下文Agent场景可复用KV分层树+候选局部RoPE方案，无需长序列训练即可将上下文拓展到百万级，适配全链路用户行为、长对话导购等需求

  - KV cache优化可参考分层存储+offloading方案，将原始token存放主机内存、仅保留上层摘要在GPU，大幅降低长序列推理显存开销，适配高并发大促场景

  - 已有LLM4Rec模型可复用其pooler蒸馏方案，从原有稠密注意力蒸馏分层选择器，无需全量重训即可快速适配长序列稀疏注意力需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前百万级token长上下文LLM面临三重痛点：稠密注意力prefill和解码成本随长度平方增长，长序列训练数据稀缺，现有稀疏注意力要么选择成本为O(L)、要么外推时相对距离超出训练分布，精度损失严重。

### 方法关键点
- 分层KV树结构：每16个连续KV组成父节点，父节点key由每层共享的可学习pooler生成，value为均值池化，自动新增层级适配更长序列，选择成本仅O(logL)
- 候选局部RoPE：每个节点的RoPE位置取其在当前层级候选列表的索引，所有相对距离不超过4096，完全落在32K训练序列的覆盖范围，无OOD问题
- 两阶段训练：第一阶段冻结骨干蒸馏pooler对齐稠密注意力分布，第二阶段冻结pooler微调骨干适配稀疏注意力，全程仅使用32K短序列
- 工程优化：拆分RoPE旋转到query和key侧实现prefill块复用，KV offloading把原始token放主机内存仅上层摘要留GPU，大幅降低显存占用

### 关键结果
基于Qwen3-4B训练0.62B token，RULER测评1M token下得分60.5，远超最优基线Dense+DCA的40.0；H200单卡下524K长度prefill加速3.2倍，解码加速3.8倍，2M token下解码仅10.7ms/token，远快于稠密注意力的2.9s/token。

最值得记住的结论：仅用32K短序列训练的稀疏注意力方案，就能实现2M token的高效长上下文外推，完全不需要长训练数据。

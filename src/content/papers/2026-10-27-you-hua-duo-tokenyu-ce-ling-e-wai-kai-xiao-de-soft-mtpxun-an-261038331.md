---
title: Multi-Token Prediction Done Right
title_zh: 优化多Token预测：零额外开销的Soft-MTP训练方案
authors:
- Jayden Teoh
affiliations:
- MIT
arxiv_id: '2610.38331'
url: https://arxiv.org/abs/2610.38331
pdf_url: https://arxiv.org/pdf/2610.38331
published: '2026-10-27'
collected: '2026-10-30'
category: Training
direction: 大模型训练 · 多Token预测优化
tags:
- Multi-Token Prediction
- Speculative Decoding
- Self-Distillation
- Gradient Routing
- LLM Training
one_liner: 通过1行代码的KL梯度恢复技巧，无开销消除多Token预测训练的噪声残差，全维度提升效果
practical_value: '- 业务中使用MTP实现LLM推测解码加速的场景，可直接复用1行代码的Soft-MTP改造，无额外开销即可提升1~3%的推理速度，兼容DeepSeek、Meta两种MTP架构，无需修改现有训练框架的fused
  cross-entropy kernel

  - 做电商/广告域垂直大模型预训练时，引入MTP+Soft-MTP，无需新增参数即可提升模型推理能力，1.2B规模下数学、代码类任务精度最高提升3.1个百分点

  - KL梯度恢复通用技巧可迁移至推荐/搜索的自蒸馏场景：只要师生模型共享线性输出头，即可避免全词表logit计算的内存开销，实现无额外成本的自蒸馏'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多Token预测（MTP）已广泛用于DeepSeek、GLM-5等大模型预训练，既能提升下游推理能力，又能支撑Speculative Decoding提速，但标准MTP训练的交叉熵梯度包含高噪声残差，会干扰NTP和MTP学习，且随模型scale增大影响更显著；直接用KL自蒸馏对齐MTP和NTP分布的方案需要全词表logit计算，内存开销高，不兼容现有fused cross-entropy kernel，落地成本高。

### 方法关键点
- 对标准MTP的交叉熵梯度做精确分解：分为KL自蒸馏项（引导MTP头对齐NTP分布，高SNR）和残差项（低SNR，干扰学习）
- 提出KL梯度恢复trick：通过straight-through梯度路由，复用现有NTP和MTP的交叉熵梯度计算，精确提取KL自蒸馏梯度，完全移除残差项，不需要显式计算KL或生成全词表logit
- 基于该trick实现Soft-MTP，仅需1行代码修改，无额外参数、无可感知开销，兼容DeepSeek/Meta两种MTP架构和现有fused kernel

### 关键实验
在167M~1.2B参数的LLaMA风格模型上预训练，对比标准MTP、显式KL自蒸馏（KL-MTP）基线：
- Speculative Decoding速度全场景提升1~3%，接受长度提升1.8~2.2%，Math域提升最高达3.7%
- 1.2B规模下零-shot平均精度比标准MTP高0.5个点，超过纯NTP基线；GSM8K精度+1.1pct，MATH-500+1.8pct，HumanEval pass@64+3.1pct，MBPP pass@64+1.2pct
- 训练开销和标准MTP完全一致，比KL-MTP吞吐量高5.6%，峰值内存低21GB

### 核心结论
Soft-MTP是MTP优化的免费午餐，仅1行代码改造就能在零额外开销的前提下全维度提升MTP的训练效果与推理效率

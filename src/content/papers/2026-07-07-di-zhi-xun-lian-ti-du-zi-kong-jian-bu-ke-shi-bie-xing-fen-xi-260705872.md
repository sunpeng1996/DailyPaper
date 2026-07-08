---
title: 'No Subspace to Track: Non-Identifiability and Optimizer State in Low-Rank
  Training'
title_zh: 低秩训练梯度子空间不可识别性分析与优化器调优方案
authors:
- Noel Thomas
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2607.05872'
url: https://arxiv.org/abs/2607.05872
pdf_url: https://arxiv.org/pdf/2607.05872
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: 低秩训练 · 内存高效优化器调优
tags:
- Low-Rank Training
- GaLore
- Adam Optimization
- LLM Training
- Memory Efficient Training
one_liner: 实测低秩优化器依赖的梯度子空间无稳定可跟踪结构，给出优化器状态修复与调优方案
practical_value: '- 做电商垂域LLM（商品文案生成、推荐理由生成、Agent工具调用微调）时，用GaLore类低秩优化器建议直接把Adam β2从默认0.999降到0.99，训练步数>20K时可降低perplexity约2，成本为0

  - 低秩训练前可先通过拆分同批次梯度算可重现秩k⋆，投影秩r设置为k⋆即可，多余维度都是噪声，不仅无助效果还会导致优化器状态过期

  - 无需尝试梯度子空间滑动平均来稳定训练，实验验证4个数量级的平均窗口对最终效果影响<0.36PPL，纯浪费算力

  - 有工程能力的团队可直接适配LDAdam类支持子空间刷新时状态迁移的优化器，1B参数场景下比调β2的原生GaLore再降0.5+PPL'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
GaLore等低秩梯度优化器通过定期刷新梯度top-r子空间将训练显存降至全秩Adam的几分之一，其核心前提是假设该子空间为缓慢漂移、可跟踪的稳定结构，但这一前提从未被定量验证，各类补丁方案的效果差异也缺乏统一解释。
### 方法关键点
- 设计同批次拆分对照实验：同一训练步拆分出两个无重叠的mini-batch，分别计算梯度top-r子空间的差异，分离估计噪声与真实子空间漂移
- 量化可重现有效秩k⋆：统计跨批次子空间中一致的方向数量，结合梯度谱分析不可识别的成因
- 对比三类优化方案的效果：子空间滑动平均、优化器状态跨刷新迁移、降低Adam第二动量的β2衰减系数
### 关键结果
实验覆盖70M~6.9B参数的4类LLM架构、ViT视觉模型，基线为原生GaLore、全秩AdamW：
1. r=128时仅约39个方向可跨批次重现，子空间刷新时96.7%~99.6%的旋转来自估计噪声，而非子空间真实漂移
2. 子空间滑动平均完全无效，10000步平均窗口仅能将旋转幅度从97%降至84%的最大值，最终PPL波动<0.36
3. 降低β2到0.99可让原生GaLore PPL降2.23，LDAdam通过状态迁移+β2=0.99，最终PPL达到16.92，比调优后的原生GaLore再降2.36
### 最值得记住的结论
低秩训练的核心是捕获梯度能量而非跟踪稳定子空间，投影秩超过有效可重现秩的部分都是无意义的噪声

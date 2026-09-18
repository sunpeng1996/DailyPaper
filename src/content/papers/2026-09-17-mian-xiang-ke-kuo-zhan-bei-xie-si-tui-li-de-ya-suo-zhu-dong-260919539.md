---
title: Compressed Active Subspaces for Scalable Bayesian Inference
title_zh: 面向可扩展贝叶斯推理的压缩主动子空间方法
authors:
- Thomas Flynn
- Sanket Jantre
- Byung-Jun Yoon
- Kibaek Kim
affiliations:
- Brookhaven National Laboratory
- Texas A&M University
- Argonne National Laboratory
arxiv_id: '2609.19539'
url: https://arxiv.org/abs/2609.19539
pdf_url: https://arxiv.org/pdf/2609.19539
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: 可扩展贝叶斯推理 · 主动子空间压缩优化
tags:
- Bayesian Inference
- Active Subspace
- Uncertainty Quantification
- Model Compression
- Scalable Training
one_liner: 提出压缩主动子空间CAS方法，大幅降低大模型贝叶斯推理内存开销，保持预测性能与鲁棒不确定性估计
practical_value: '- 对需要做不确定性量化的推荐/广告模型（如冷启动打分、OOD样本风险控制），可借鉴CAS的结构化等距嵌入思路，降低主动子空间构造的内存开销，实现大模型的贝叶斯推理落地

  - 做推荐模型低秩适配/参数压缩时，可参考CAS先降维再找高影响参数方向的思路，减少全量梯度存储需求，提升大模型微调的资源效率

  - 面向Agent的决策不确定性评估场景，CAS方法可在不损失不确定性估计鲁棒性的前提下，降低大语言模型贝叶斯微调的计算成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
主动子空间是高维模型预测不确定性量化的高效方案，但构造过程需要存储大量全维模型梯度，随模型规模增长内存开销会达到不可接受的水平，无法支撑大模型贝叶斯推理落地。
### 方法关键点
提出压缩主动子空间（CAS）可扩展框架：首先通过结构化等距嵌入将全量模型参数映射到低维压缩空间，再在压缩后的参数空间内构造主动子空间，全程无需存储全维梯度。
### 关键结果
在不同规模神经网络上验证，CAS可将主动子空间构造的内存开销降低1~2个量级，同时保持与标准主动子空间方法相当的预测性能、鲁棒不确定性估计能力，可支持原方法无法适配的大模型贝叶斯推理任务。

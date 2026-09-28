---
title: 'Beyond Empirical Support: Structured Outlier Generation via Sinkhorn Optimal
  Transport'
title_zh: 超越经验数据支撑：基于Sinkhorn最优传输的结构化离群点生成
authors:
- Haixiang Sun
- Andrew L. Liu
affiliations:
- Edwardson School of Industrial Engineering, Purdue University
arxiv_id: '2609.31470'
url: https://arxiv.org/abs/2609.31470
pdf_url: https://arxiv.org/pdf/2609.31470
published: '2026-09-25'
collected: '2026-09-28'
category: Eval
direction: 离群点生成 · 模型鲁棒性优化
tags:
- Sinkhorn Optimal Transport
- Outlier Generation
- Model Robustness
- Latent Sampling
- Stress Testing
one_liner: 提出融合Sinkhorn最优传输的SBOG框架，生成语义可控的跨模态结构化离群点用于模型鲁棒性评测
practical_value: '- 可复用SBOG的「语义约束+分布边界采样」思路，生成推荐/Agent系统长尾压力测试case，覆盖历史未出现的极端用户行为、异常query场景，提升鲁棒性评测覆盖度

  - 做RecSys/LLM4Rec的分布外鲁棒性训练时，可引入Sinkhorn诱导的支撑成本指导采样，生成语义可控的分布外样本做数据增强，避免无效噪声样本干扰训练

  - 跨模态推荐的异常样本生成场景可直接复用该框架的跨模态适配能力，无需针对图像/文本/序列模态单独定制离群点生成逻辑'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有ML系统鲁棒性评测依赖的离群点大多来自历史数据集，有限样本无法覆盖未来可能出现的极端分布偏移；传统离群点合成方法依赖稀疏邻域、分类器边界等启发式规则，稳定性差、与模态/模型架构强绑定，无法生成语义可控的结构化压力场景。
### 方法关键点
提出SBOG结构化离群点生成框架，在隐空间将Sinkhorn最优传输几何结构与分布鲁棒边界建模结合：用Sinkhorn诱导的支撑成本引导采样器向分布弱支撑的边界区域采样，同时加入语义约束防止样本漂移出目标上下文，生成相对于分布内参考样本的可控偏差样本，而非任意稀疏区域的无意义样本。
### 关键结果
在时序异常生成、图像离群点合成任务上验证，生成的离群点具备高信息量、语义可控特性，跨模态场景下均能提升下游模型鲁棒性评测的有效性。

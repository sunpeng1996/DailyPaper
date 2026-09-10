---
title: 'Let It Go or Learn to Self-Correct: Continuous Diffusion for Constrained Discrete
  Tasks'
title_zh: “放手”还是自校正：面向受限离散任务的连续扩散优化
authors:
- Mariia Drozdova
- Stéphane Liem Nguyen
- François Fleuret
affiliations:
- University of Geneva
arxiv_id: '2609.09009'
url: https://arxiv.org/abs/2609.09009
pdf_url: https://arxiv.org/pdf/2609.09009
published: '2026-09-08'
collected: '2026-09-10'
category: Training
direction: 扩散模型 · 受限离散任务优化
tags:
- DDPM
- Diffusion Sampling
- Self-Correction
- Train-Inference Alignment
- Discrete Reasoning
one_liner: 针对连续扩散在受限离散任务的误差累积问题，提出无重训采样优化与自校正训练大幅提升效果
practical_value: '- 做GenRec中带约束的离散生成（如满足库存/价格约束的Item序列、合规营销文案）时，可直接复用无重训采样trick：扩散推理时直接输出模型干净预测，无需贴合上一步噪声状态，大幅降低约束违反率

  - 若业务生成任务存在训练推理分布 mismatch，可引入自校正训练：训练阶段让模型接触自身推理产生的错误样本，提升推理误差鲁棒性，无需额外引入外部约束模块

  - 推荐/广告领域的组合优化任务（如多约束广告投放预算分配、流量调控），可复用本文扩散优化范式，替代传统搜索类方法降低推理耗时'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
连续扩散模型在图像、视频等连续域生成效果优异，但在数独、N皇后、图连通性等带全局约束的离散任务中，标准采样策略会保留早期产生的离散错误，难以后续修正，存在严重的训练-推理分布 mismatch。
### 方法关键点
1. 无重训采样优化：推理阶段直接输出模型的干净预测，不再强制每步更新贴合当前噪声状态，从根源避免早期错误累积
2. 自校正训练：训练阶段让模型接触自身生成的预测样本，提升对推理阶段产生的误差的鲁棒性，进一步缩小训练-推理分布 gap
### 关键结果
仅修改采样策略无需重训，数独任务的合法率从31%提升至95%，其余受限离散任务均获得一致性收益；自校正训练可进一步大幅提升标准扩散采样器的性能。

---
title: On-Policy and Off-Policy Learning for Large Action Spaces
title_zh: 面向大动作空间的同策略与异策略学习
authors:
- Imad Aouali
affiliations:
- Institut Polytechnique de Paris
- CREST, ENSAE
- Criteo AI Lab
- University of Technology Nuremberg
arxiv_id: '2607.28408'
url: https://arxiv.org/abs/2607.28408
pdf_url: https://arxiv.org/pdf/2607.28408
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 上下文老虎机 · 大动作空间推荐优化
tags:
- Contextual Bandit
- Large Action Space
- On-Policy Learning
- Off-Policy Learning
- Thompson Sampling
one_liner: 针对大动作空间上下文老虎机痛点，提出系列可扩展同/异策略算法，兼顾统计与计算效率
practical_value: '- 大动作空间在线A/B测试/冷启动探索可复用meTS的混合效应建模思路，将商品/广告按类目、语义特征分组构造共享潜效应，大幅降低汤普森采样的内存和时间开销，同时减少探索regret

  - 离线异策略训练时，当动作空间规模达十万/百万级，优先选择PWLL目标而非复杂IPS类估计器，其优化景观更友好，可避免陷入局部最优，实测效果更稳定

  - 离线DM类方法可借鉴sDM的共享潜结构设计，无需日志覆盖所有候选动作，仅保证最优动作的覆盖即可实现稳定收敛，适配稀疏日志的长尾商品推荐场景

  - 做策略优化时不要盲目追求reward估计精度，大动作空间下目标函数的优化可处理性对最终策略效果的影响远大于估计误差，是核心设计准则'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
推荐、在线广告等交互系统可建模为上下文老虎机，现有同策略（在线）、异策略（离线）算法在大动作空间（十万至百万级商品/广告候选）下，要么面临计算复杂度爆炸问题，要么统计效率极低、数据需求量大，无法适配工业级落地需求。
### 方法关键点
- 同策略方向：提出混合效应汤普森采样meTS，通过L个共享潜效应（如类目、语义分组）耦合所有动作参数，将贝叶斯 regret 降至$	ilde{O}(\\sqrt{T d K_{eff}})$，内存复杂度从$O(K^2d^2)$降至$O((L^2+K)d^2)$；进一步提出扩散汤普森采样dTS，用预训练扩散模型建模动作间复杂关联，复杂度进一步降至$O((L+K)d^3)$，无需额外超参调优。
- 异策略方向：提出结构化直接法sDM，通过共享潜结构建模动作参数，无需严格全日志覆盖假设，实现$O(1/\\sqrt{n})$的贝叶斯次优性收敛；证明大动作空间下优化难度对策略效果的影响远大于估计精度，提出policy-weighted log-likelihood（PWLL）目标，适配随机优化，在百万动作场景下效果远超复杂IPS类估计器；结合指数平滑正则与PAC-贝叶斯悲观原则，给出可导的低方差异策略训练目标。
### 关键结果
在合成数据集、Criteo广告数据集、百万级动作公开数据集上测试，对比标准TS、LinUCB、普通DM、IPS等基线：meTS在百万动作场景下regret比标准TS低42%；sDM比普通DM在十万动作场景下次优性降低36%；PWLL目标比IPS类方法在百万动作场景下策略价值高29%。

**最值得记住的一句话**：大动作空间交互学习的核心不是直接套用经典算法，而是要利用动作间结构做信息共享，同时优先保证目标函数的优化可处理性，而非盲目追求估计精度。

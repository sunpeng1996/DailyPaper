---
title: Learning Generative Ranking Policies for Whole-Page Optimization
title_zh: 面向整页优化的生成式排序策略学习方法
authors:
- Chen Qiu
- Zhigang Hua
- Qi Xu
- Jizhe Zhang
- Sha Hua
- Ren Mao
- Luke Simon
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2611.25527'
url: https://arxiv.org/abs/2611.25527
pdf_url: https://arxiv.org/pdf/2611.25527
published: '2026-11-19'
collected: '2026-11-20'
category: GenRec
direction: 生成式推荐 · 整页优化
tags:
- Generative Reranking
- Whole-Page Optimization
- Policy Improvement
- Listwise Ranking
- Recommender System
one_liner: 提出整页策略优化方法，通过逐位置监督训练生成式重排器，实现低时延整页推荐效果最优
practical_value: '- 生成式重排训练可直接复用逐位置监督范式：无需额外学习critic，通过当前生成器补全剩余页面得到整页评分，重加权得到各位置训练目标，降低训练复杂度

  - 推理阶段可放弃beam search：直接贪婪生成整页序列，在Meta工业数据集上对比宽度32的beam search，page score更高且时延降低400倍以上，无需调用evaluator，适配高吞吐推荐场景

  - 训练时可采用候选采样降低计算开销：仅对Top κ+随机采样κr个候选做整页评分，剩余候选概率保持不变，保证性能提升的同时大幅减少evaluator调用次数

  - 工业落地可复用现有资产：直接用线上已训练好的整页价值模型作为训练监督信号，无需额外标注，天然适配多目标排序、带位置约束排序等电商/内容feed场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐页作为整体被用户消费，物品间存在注意力竞争、互补、冗余效应，简单拼接单点最优物品无法得到全局最优页面。整页优化的可行组合空间随长度呈指数级增长，无法枚举求解；现有生成式重排方法要么用全局页级信号分配给所有位置，存在credit分配偏差，要么拟合固定的预构造目标页，无法随生成器迭代更新，性能存在明显瓶颈。
### 方法关键点
- 迭代式训练流程：每轮用当前生成器π_k采样页面，对每个部分页的候选，放置候选后用π_k补全剩余物品得到完整页，调用预训练的固定evaluator得到整页评分Q
- 逐位置闭形式目标：基于带KL正则的局部优化目标，推导得到目标分布正比于π_k的当前概率乘以exp(Q/τ)；仅采样部分候选评估时，未评分候选的概率保持不变，降低计算开销
- 交叉熵拟合更新生成器，理论证明精确更新下页级期望得分单调提升，迭代可收敛到全局最优
### 关键实验
在KuaiRand-1K、RL4RS-SeqSlate公开数据集、Meta工业内容feed数据集、合成最优已知数据集上验证，对比GFN4Rec、DeGRe、PPO、GRPO等SOTA基线：
- KuaiRand-1K平均页得分较最强基线提升1.6pct，工业数据集相对基线提升1.17pct，效果超过宽度32的prefix beam search；合成数据集达到97.16%的最优页得分，较次优PPO高2.52pct
- 推理阶段无需evaluator调用，时延较宽度32的beam search降低2~3个数量级

最值得记住的一句话：整页优化的核心是每个位置的物品选择必须考虑其对后续所有物品的全局影响，而非仅评估当前位置的局部价值。

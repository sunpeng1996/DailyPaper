---
title: 'Let''s Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Scale
  Mixture-of-Experts'
title_zh: 面向大规模MoE的计算高效两步超参迁移框架
authors:
- Nayeon Kim
- Hojin Lee
- Yunju Bak
- Jaesun Park
- Boseop Kim
affiliations:
- Kakao Corp.
- Upstage AI
arxiv_id: '2608.20061'
url: https://arxiv.org/abs/2608.20061
pdf_url: https://arxiv.org/pdf/2608.20061
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: 大模型训练 · MoE超参迁移
tags:
- MoE
- Hyperparameter Transfer
- μP
- Scaling Law
- Learning Rate
- Pretraining
one_liner: 通过μP适配+token维度缩放律，用小代理模型预测大MoE万亿token训练的最优学习率
practical_value: '- 训练业务侧MoE基座（如生成式推荐Item生成、Agent决策大模型）时，可直接复用该两步超参迁移框架，替代传统2D超参扫描，算力成本降低90%+

  - 直接复用论文给出的MoE μP适配规则（向量/矩阵类参数的初始化方差、LR缩放系数），可快速适配MLA+Muon优化器的MoE训练场景，避免重复调参

  - 超参搜索阶段用EMA替代学习率衰减的trick，可从单次小代理模型训练中提取多token规模的最优LR，大幅降低小样本超参搜索的计算开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE架构可在算力不成正比增长的前提下大幅提升模型容量，是当前大模型规模化的核心路径，但超参尤其是学习率的调优成本极高：传统方法需跨模型规模、token规模做2D超参扫描，万亿参数+万亿token级训练的扫描开销完全不可承受，且现有面向稠密模型的μP超参迁移方案不兼容MoE的稀疏缩放逻辑。
### 方法关键点
1. **MoE适配的μP参数化**：将MoE参数分为向量类（embedding、偏置、专家FC2层）和矩阵类（FFN、注意力、路由、专家FC1层），分别设置初始化方差和学习率缩放系数，固定层数、注意力头维度、专家中间维度、单token激活专家数，仅缩放模型宽度和总专家数，最优学习率可跨不同宽度的MoE模型零样本迁移。
2. **两步超参迁移框架**：先用小体量代理模型做短token预算训练，训练阶段用EMA权重平滑替代学习率衰减，从单次训练中提取多token规模的最优学习率；再在log-log空间做线性回归拟合学习率随token规模的缩放律，直接外推到万亿token级目标训练场景。
### 关键结果
小代理模型仅需完成500B token训练，拟合的token缩放律R²达0.95，外推10T token最优学习率的平均误差仅4.4%；用预测的学习率训练155B总参/17B激活参的MoE基座，训练全程损失无 spike，MMLU-Pro表现处于同算力帕累托最优前沿，超参搜索的总算力仅为传统2D扫描方案的1/98。
### 核心结论
大规模MoE预训练的最优学习率完全可以通过小体量代理模型的低成本实验准确预测，无需昂贵的全规模超参扫描

---
title: 'Cut Binary Cross Entropy: Efficient Large-Vocabulary Loss and Gradient Kernels
  for Sequential Recommendation'
title_zh: CutBCE：面向序列推荐的大词表高效BCE损失与梯度算子
authors:
- Yaoyiran Li
- Haowen Ning
- Mohamed Hammad
affiliations:
- Google Cloud
arxiv_id: '2610.05559'
url: https://arxiv.org/abs/2610.05559
pdf_url: https://arxiv.org/pdf/2610.05559
published: '2026-10-04'
collected: '2026-10-06'
category: RecSys
direction: 序列推荐 · 大词表训练效率优化
tags:
- Sequential Recommendation
- BCE Loss
- TPU Kernel
- Training Efficiency
- JAX
one_liner: 面向大词表序列推荐的硬件加速BCE算子，降65.7%HBM、提225.9%训练速度
practical_value: '- 若团队基于JAX/TPU训练百万级item词表的多标签序列推荐模型，可直接复用开源CutBCE算子替代原生BCE，零额外开发成本下解决OOM问题、提升训练速度

  - BCE损失拆分思路可迁移：将损失拆分为稠密背景损失+稀疏正样本修正项，分块计算避免全量logits落HBM，该数学分解可直接用于GPU/Triton自定义算子开发

  - 训练指标计算trick可复用：前向计算时直接聚合TP/FP/FN/TN计数，无需存储全量logits即可监控训练精度，无额外HBM开销

  - 大词表多标签训练无需硬上负采样，CutBCE支持全词表精确训练无采样偏差，适合电商/内容推荐多意图Session的多目标预测场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级序列推荐的item词表通常达1e5~1e7量级，多标签训练用原生全词表BCE损失时，需要生成[B,N,V]的稠密logits张量存入HBM，内存开销达O(BNV)，极易触发OOM；现有大词表损失优化均针对LLM的Softmax交叉熵，无针对BCE的硬件加速方案，严重限制了大batch、长序列推荐模型的训练效率。

### 方法关键点
- 数学分解：将BCE损失拆分为稠密背景损失+稀疏正样本修正项，与原生BCE精确等价，无精度损失
- 词表分块计算：将词表切分为4096大小的块，逐块计算logits、累计损失后立即丢弃，峰值中间内存从O(BNV)降至O(BN*块大小)
- 自定义VJP与Pallas TPU内核：反向传播时按需重计算分块logits，全量logits与梯度全程不落HBM，同时支持动态VMEM预算、分布式分片优化
- 零开销训练指标：前向过程直接聚合分类混淆矩阵计数，无需存储全量logits即可计算训练阶段的精度、召回等指标

### 关键实验
基于Yambda-50M数据集（876k item）训练多标签SASRec模型，8卡TPU v6e环境下对比原生Keras BCE：相同batch=64、seq_len=256配置下，CutBCE降低65.7%峰值HBM（单卡节省14.7GiB），训练速度提升225.9%，Hit@8仅从0.186降至0.183，精度损失可忽略；原生BCE在batch=128或seq_len=512配置下直接OOM，CutBCE可稳定运行，长序列下Hit@8提升至0.211。

### 核心结论
大词表多标签推荐训练的OOM瓶颈本质是不必要的全量logits存储开销，通过数学分解+分块计算+自定义内核即可在无精度损失的前提下大幅提升训练效率。

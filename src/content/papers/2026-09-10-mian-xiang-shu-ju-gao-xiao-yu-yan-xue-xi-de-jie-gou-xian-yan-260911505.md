---
title: Structural priors for data-efficient language learning
title_zh: 面向数据高效语言学习的结构先验方法
authors:
- Yana Veitsman
- Jonas Mayer Martins
- Jonathan Lautenschlager
- Lisa Beinborn
affiliations:
- University of Göttingen, Germany
arxiv_id: '2609.11505'
url: https://arxiv.org/abs/2609.11505
pdf_url: https://arxiv.org/pdf/2609.11505
published: '2026-09-10'
collected: '2026-09-12'
category: LLM
direction: LLM低资源训练 · 结构先验权重初始化
tags:
- Low-Resource-LLM
- Structural-Prior
- Weight-Initialization
- Transfer-Learning
- Data-Efficiency
one_liner: 探究非语言数据预训练引入结构先验的权重初始化方案，提升语言学习数据效率
practical_value: '- 小语种电商/垂类推荐场景模型冷启动时，若语料不足，可先用同结构的用户行为序列、商品属性结构化数据做预训练初始化，加快收敛

  - 垂类小样本LLM训练时，优先选择和目标数据序列结构匹配的符号数据预训练，相比随机初始化可降低预训练loss，节省算力成本

  - 预训练next-token-prediction损失下降不代表下游推荐/Agent交互任务性能提升，垂类模型训练必须结合业务指标验证，不能仅以预训练loss为终止条件'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
大语言模型性能高度依赖海量语料与算力投入，低资源语言、垂类小样本场景下数据稀缺问题突出，亟需提升训练数据效率。
### 方法关键点
提出结构迁移思路，先在音乐、概率语法、元胞自动机三类非语言符号数据上预训练，为多语言建模提供权重初始化，从next-token-prediction损失、训练阶段权重偏移量、下游语言基准三个维度评估迁移效果。
### 关键结果
- 三类非语言数据预训练的初始化方案，相比随机初始化语言建模损失更低
- 后续语言训练阶段权重偏移量更小，说明初始化参数落在更优参数空间
- 更低的预训练损失无法稳定转化为下游任务性能提升，非语言数据迁移效率低于补充等量语言数据，仅可作为next-token-prediction目标下的语言数据部分替代品

---
title: 'SurvICL: a Foundation Model for in-context Survival Analysis'
title_zh: SurvICL：面向上下文生存分析的基础模型
authors:
- Julie Alberge
- Linus Bleistein
- Judith Abécassis
- Marine Le Morvan
- Gaël Varoquaux
- David Holzmüller
affiliations:
- Inria de Saclay
- EPFL
- probabl.
arxiv_id: '2610.22242'
url: https://arxiv.org/abs/2610.22242
pdf_url: https://arxiv.org/pdf/2610.22242
published: '2026-10-15'
collected: '2026-10-17'
category: Other
direction: 表格基础模型 · 生存分析建模
tags:
- Tabular Foundation Model
- Survival Analysis
- In-context Learning
- Quantile Regression
- Synthetic Pre-training
one_liner: 提出上下文学习型生存分析表格基础模型，无需微调即可超越经典Cox模型
practical_value: '- 可直接将SurvICL的生存分析范式迁移到电商用户流失预测、复购时间预测场景，ICL无微调能力可降低小样本业务建模成本

  - 可控合成数据预训练+普通分位数回归损失的训练范式，可复用在带删失数据的业务建模（如未点击隐性负样本处理）

  - 小样本表格数据建模可参考ICL类表格基础模型路线，相比传统树模型泛化性更优'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有表格基础模型（TFM）在分类、回归任务效果已超过梯度提升树，但在带删失数据的生存分析场景下，性能始终不如已有50年历史的Cox模型，尤其小样本场景下表现更差。
### 方法关键点
1. 提出SurvICL上下文学习型TFM，基于全新灵活比例odds先验生成纯合成数据集完成预训练
2. 利用合成数据提供的无删失事件时间，直接采用普通分位数回归损失训练，无需适配删失的特殊损失函数
3. 构建目前规模最大的生存分析基准，覆盖103个不同数据集
### 关键结果
在63个未参与模型设计的holdout数据集上，SurvICL无需微调即可超过20个树模型、深度学习、基础模型基线：综合Brier score两两对比胜率达82.9%，远超第二名Cox模型的71.3%，是首个在小数据集上效果超越Cox的模型

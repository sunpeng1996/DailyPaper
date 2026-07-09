---
title: 'TimEE: End-to-end Time Series Classification via In-Context Learning'
title_zh: TimEE：基于上下文学习的端到端时间序列分类模型
authors:
- Jaris Küken
- Shi Bin Hoo
- Martin Mráz
- Frank Hutter
- Lennart Purucker
affiliations:
- University of Freiburg
- Zuse School ELIZA Darmstadt
- Prior Labs
- ELLIS Institute Tübingen
arxiv_id: '2607.07500'
url: https://arxiv.org/abs/2607.07500
pdf_url: https://arxiv.org/pdf/2607.07500
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: 时序分类 · 合成数据预训练ICL
tags:
- Time Series Classification
- In-Context Learning
- Synthetic Pre-training
- PFN
- Meta Learning
one_liner: 4.5M参数小模型仅用合成时序数据预训练，实现免微调端到端时序分类SOTA
practical_value: '- 电商用户行为时序分类（如购买意图预判、异常行为识别）可复用合成数据预训练+ICL范式，省去单业务数据集微调成本

  - 小参数业务模型训练可参考PFN元训练框架，仅用合成数据即可逼近全监督SOTA效果，降低真实数据依赖与合规风险

  - 冷启动时序分类任务可复用端到端ICL推理逻辑，输入少量标注样本即可直接输出预测结果，快速适配新场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统时序分类（TSC）采用「特征编码器+任务分类器」两阶段范式，存在表征学习与分类目标解耦、需单数据集单独训练、推理无法利用标签信息三大痛点，落地成本高。
### 方法关键点
1. 推出仅4.5M参数的TimEE基础模型，基于PFN（prior-data fitted network）框架，全程仅用合成时序任务完成元训练
2. 支持端到端In-Context Learning推理：输入带标注的支持集+查询时序，单轮前向传播直接输出分类分布，无需目标数据集微调
### 关键结果
在UCR时序基准测试中，ROC AUC指标位列所有对比方法（含基础模型、全监督深度学习基线）第一，准确率排名第三，是首个仅用合成数据预训练就达到UCR SOTA性能的模型。

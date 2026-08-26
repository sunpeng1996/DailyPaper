---
title: When Do Supervised UQ Ensembles Improve LLM Hallucination Detection? A Robustness
  Study
title_zh: 监督式UQ集成优化LLM幻觉检测的适用场景与鲁棒性研究
authors:
- Mohit Singh Chauhan
- Vipin Gyanchandani
- Dylan Bouchard
affiliations:
- CVS Health
arxiv_id: '2608.24492'
url: https://arxiv.org/abs/2608.24492
pdf_url: https://arxiv.org/pdf/2608.24492
published: '2026-08-25'
collected: '2026-08-26'
category: LLM
direction: LLM幻觉检测 · 不确定性量化集成
tags:
- Hallucination Detection
- Uncertainty Quantification
- Ensemble Learning
- LLM Robustness
- Closed-book LLM
one_liner: 系统验证监督UQ集成幻觉检测的样本效率、跨分布迁移能力与跨生成范式表现
practical_value: '- 落地LLM驱动的电商客服、商品文案生成、导购Agent场景时，可优先采用监督UQ集成做幻觉检测，仅需100-200条标注样本即可获得优于单一UQ指标的效果

  - 若无法获取LLM的token概率（如调用第三方LLM API），仅用黑盒UQ信号（多轮生成一致性、语义相似度、自评分）做集成，可达到接近全信号集成的效果

  - 集成策略优先选L2正则logistic回归，跨短文本/长文本/代码生成场景均表现稳定，收敛快且不易过拟合；标注样本充足时可尝试随机森林获取更高AUROC

  - 同领域跨数据集迁移时可直接复用训练好的UQ集成模型，平均AUROC损失仅0.02，无需重新标注全量数据，适配业务场景的数据分布漂移情况'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
封闭书场景（无外部检索、无参考文档）下LLM幻觉是业务落地核心瓶颈，单一UQ（不确定性量化）指标在不同生成范式、不同LLM、不同领域下表现波动大，零-shot阈值极易失效；现有监督UQ集成的鲁棒性缺乏系统验证，样本效率、跨分布迁移能力、跨场景适用性均不明确，难以直接指导业务落地。

### 方法关键点
- 集成框架输入覆盖四类UQ信号：黑盒一致性（多生成样本的语义/文本相似度、代码功能一致性）、白盒token概率（序列概率、熵、概率裕度）、自评估评分、长文本claim级图特征，训练二分类器判别幻觉
- 对比4种集成策略：L2正则logistic回归、随机森林、梯度提升树、约束加权平均
- 评估覆盖3个生成范式：短文本QA、长文本生成、代码生成，4款主流闭源LLM（Gemini 2.5 Flash/Pro、GPT-4o/4o-mini），9个公开数据集

### 关键结果数字
- 全量标注下，监督UQ集成在32个测试设置中30个优于最优单一UQ指标，AUROC最高提升0.07；仅需100条标注样本即可获得稳定增益
- 同领域跨分布迁移场景下，28个测试设置中23个优于最优单一UQ指标，平均AUROC损失仅0.02
- 黑盒仅信号集成在19/20个短文本设置下优于最优单一黑盒指标，效果接近全信号集成；仅用白盒信号的集成增益有限
- 校准性大幅提升，29/32设置下ECE（期望校准误差）低于0.06，输出分数可直接用于阈值触发人工审核，无需额外调参

只要有少量标注样本，监督UQ集成就是封闭书场景下LLM幻觉检测的默认最优方案，黑盒集成是第三方LLM API场景下的鲁棒fallback。

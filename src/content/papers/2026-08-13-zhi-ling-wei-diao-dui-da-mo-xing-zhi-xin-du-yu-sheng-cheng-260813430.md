---
title: Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence
  and Lexical Diversity
title_zh: 指令微调对大模型置信度与生成内容词汇多样性的影响研究
authors:
- Irina Proskurina
- Mayank Kumar
- Oyindolapo O. Komolafe
affiliations:
- Cohere Labs Community
- Laboratoire Hubert Curien, UMR CNRS 5516
- Bennett University
- Western University
arxiv_id: '2608.13430'
url: https://arxiv.org/abs/2608.13430
pdf_url: https://arxiv.org/pdf/2608.13430
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: 大模型指令微调效果评估
tags:
- Instruction Tuning
- LLM Confidence
- Lexical Diversity
- Model Calibration
- Question Answering
one_liner: 量化指令微调对LLM问答置信度、校准度及生成理据词汇多样性的差异化影响
practical_value: '- 电商Agent商品咨询场景做指令微调时，可通过监控生成理据的跨样本多样性变化，间接评估模型过置信风险，避免误导用户

  - 生成式推荐场景若需稳定的解释输出（如商品推荐理由），可优先选用指令微调模型，其跨样本理据一致性更高，减少解释偏差

  - 业务侧LLM优化时不要仅依赖预测准确率判断微调效果，需单独设计置信度、多样性度量指标，避免出现准确率不变但过置信的问题'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
指令微调LLM在多生成任务上表现优异，但普遍存在口头过置信问题，现有研究未明确微调诱导的置信度变化与生成理据的词汇多样性变化的关联。
### 方法关键点
选取3组配对的基座/指令微调LLM，在多个问答基准上开展对照测试，控制答案选择、理据长度变量，对比置信度、校准度、词汇多样性的变化差异。
### 关键结果
1. 指令微调后预测准确率变化有限，但模型置信度显著改变，基于似然的校准度下降；
2. 生成理据的跨样本多样性一致下降，表层词汇多样性的变化方向、幅度随模型和基准差异较大；
3. 上述差异与答案选择、理据长度无关，置信度和多样性是指令微调带来的两个独立效应。

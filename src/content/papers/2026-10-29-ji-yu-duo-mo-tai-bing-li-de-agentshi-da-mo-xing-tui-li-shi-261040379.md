---
title: Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal
  medical records
title_zh: 基于多模态病历的Agent式大模型推理实现儿童糖尿病预后预测
authors:
- Daniel Palacios
- Guantong Qi
- Anna Kadi
- Natali Borrego
- Sukru Aras
- Michael L. Ferm
- Elizabeth Kubota-Mishra
- Maria J. Redondo
- Zhandong Liu
- Mustafa Tosur
affiliations:
- Baylor College of Medicine
- Texas Children's Hospital
- USDA/ARS Children's Nutrition Research Center
- NYU Grossman School of Medicine
arxiv_id: '2610.40379'
url: https://arxiv.org/abs/2610.40379
pdf_url: https://arxiv.org/pdf/2610.40379
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: LLM Agent 多模态风险预测推理
tags:
- LLM Agent
- Multimodal Reasoning
- Risk Prediction
- Self-auditing
- Evidence Citing
one_liner: 提出具备证据引用、自审计能力的LLM Agent管线CEDAR，在儿童糖尿病预后预测上显著优于传统ML
practical_value: '- 可复用「证据引用+自审计」的Agent架构，解决推荐/广告场景高风险决策（如大促选品、个性化营销内容生成）的可解释性、结果溯源需求

  - 多模态异构数据（结构化属性+非结构化文本+时序行为）的Agent推理范式，可迁移到用户建模场景，融合用户标签、评论、浏览时序提升冷启动预估准确率

  - 小样本场景下Agent推理性能显著优于传统ML的结论，可参考用LLM Agent搭建低资源垂类（如新类目推荐）的快速基线'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM Agent临床预测方案未在儿科场景验证，该场景存在数据集规模小、预后事件稀疏的问题，传统机器学习方法性能受限。

### 方法关键点
CEDAR是具备证据自动引用、自审计能力的LLM Agent管线，输入覆盖结构化病历数据、临床笔记提取的社会决定因素、连续血糖监测时序数据等多模态信息，基于18个月随访数据预测24个月时的糖尿病预后指标。

### 关键结果数字
- T2D队列AUC达0.815，优于传统ML的0.656~0.700；T1D队列AUC达0.756，优于传统ML的0.603~0.631
- 70246条引用证据仅4条与原始病历不符，证据准确率达99.99%
- 儿童内分泌医生仅参考CEDAR给出的证据与推理逻辑，90%的预测结果与CEDAR一致，医生间共识率达90.5%

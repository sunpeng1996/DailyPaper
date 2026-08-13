---
title: 'ENTLORE: A Graph-Grounded Benchmark for Latent Organizational Reasoning in
  Enterprise Question Answering'
title_zh: ENTLORE：面向企业问答潜在组织推理的图驱动基准框架
authors:
- Akrin Zheng
- Alexander Wu
- Alaia Liu
affiliations:
- ScitiX.ai
arxiv_id: '2608.10679'
url: https://arxiv.org/abs/2608.10679
pdf_url: https://arxiv.org/pdf/2608.10679
published: '2026-08-11'
collected: '2026-08-12'
category: Eval
direction: 企业QA · 隐式关系推理基准构建
tags:
- Enterprise_QA
- Benchmark
- Graph_RAG
- Implicit_Reasoning
- Document_Retrieval
one_liner: 发布面向企业问答隐式组织关系推理的图驱动基准数据集及构建框架
practical_value: '- 企业级RAG系统可参考将文档、结构化表、操作记录统一构建真值图，校验隐式关系推理正确性，提升内部QA/电商售后规则问答准确率

  - 做内部知识库/电商规则类QA时需额外关注隐式关系推理场景，这类场景仅靠召回金标文档仍有30%+错误率，需补充结构化实体图做推理增强

  - 评测内部RAG/QA系统能力时，可参考该框架构建分层测试集（显式查询/跨源组合/隐式推理），全面评估系统能力边界'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有企业QA基准普遍预设固定答案路径，仅能测试显式事实组合能力，无法评估从跨源异构文档中恢复语料未直接提及的隐式组织关系的潜在组织推理能力。
### 方法关键点
提出ENTLORE图驱动基准构建框架，从常规文档、权威组织表、运营记录中重建可审计的企业世界，用版本化组织规范校验真值图中的推导关系，匿名发布时仅公开文档语料、隐藏私有结构和目标关系。基准包含3类来源共2341份文档、907个问题，覆盖显式查询、跨源组合、潜在组织推理三类任务。
### 关键结果
在56种模型+访问配置下测试，将语料构建为诱导实体图或可导航知识库的部署方案效果最优；即使提供金标文档，隐式推理问题仍有30.4%无法回答，显式、组合类问题的未答率仅为12.6%、6.2%。

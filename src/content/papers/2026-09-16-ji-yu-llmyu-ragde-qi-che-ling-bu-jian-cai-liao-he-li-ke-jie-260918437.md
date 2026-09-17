---
title: Exploring LLMs and RAG for Plausible and Explainable Material Prediction of
  Vehicle Components
title_zh: 基于LLM与RAG的汽车零部件材料合理可解释预测研究
authors:
- Frederik Wagner
- Annerose Eichel
- Sabine Schulte im Walde
affiliations:
- University of Stuttgart, Institute for Natural Language Processing, Germany
arxiv_id: '2609.18437'
url: https://arxiv.org/abs/2609.18437
pdf_url: https://arxiv.org/pdf/2609.18437
published: '2026-09-16'
collected: '2026-09-17'
category: RAG
direction: 垂直领域RAG效果验证与落地
tags:
- RAG
- LLM
- Chain-of-Verification
- Domain Adaptation
- Expert Evaluation
one_liner: 对比原生LLM、单轮RAG、带CoVe的RAG在汽车零部件材料预测的效果，验证现有RAG未超越基线
practical_value: '- 垂直场景落地RAG前务必先测试原生LLM基线效果，避免过度投入RAG架构优化反而性能不及基线，可复用在电商垂类Agent、工业场景推荐系统的方案选型阶段

  - 无公开金标准的垂直任务可自研结构化专家标注工具完成效果评估，该思路可直接迁移到非标品推荐、垂类Agent回答准确率的人工评测链路中

  - 垂直领域RAG性能瓶颈核心是高质量合规领域语料，语料质量不足时优先优化语料库而非RAG链路本身，适合电商商品知识、工业领域知识库建设参考'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
汽车维修等高安全垂直场景亟需可靠的AI辅助工具，现有LLM在垂直领域的预测可靠性、可解释性缺乏验证，且汽车零部件材料预测任务无公开金标准数据集与评估方案。
### 方法关键点
对比三类方案的任务表现：1. 原生生成式LLM基线；2. 单轮RAG，采用汽车领域过滤的维基百科语料作为检索库；3. 迭代式Chain-of-Verification（CoVe）增强的RAG方案；自研web端结构化标注工具支撑领域专家完成效果评估。
### 关键结果
原生LLM生成效果大幅超过此前领域SOTA；测试的两类RAG方案均未超越原生LLM基线；暴露RAG落地核心痛点：超参优化复杂度高、高质量合规领域语料稀缺、专家评估方案设计难度大

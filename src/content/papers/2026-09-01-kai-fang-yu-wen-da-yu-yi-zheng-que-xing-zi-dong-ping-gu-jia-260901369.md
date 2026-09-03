---
title: How Correct Is Your Answer? A Semantic Correctness Framework for Open QA Evaluation
title_zh: 开放域问答语义正确性自动评估框架
authors:
- Elitsa Yotkova
- Violeta Kastreva
- Petar Velkov
- Hristo Boyanov
- Dimitar Dimitrov
- Ivan Koychev
- Preslav Nakov
affiliations:
- Sofia University "St. Kliment Ohridski"
- ETH Zürich
- University of Zurich
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2609.01369'
url: https://arxiv.org/abs/2609.01369
pdf_url: https://arxiv.org/pdf/2609.01369
published: '2026-09-01'
collected: '2026-09-03'
category: Eval
direction: 大模型开放问答语义正确性自动评估
tags:
- OpenQA
- LLM Evaluation
- NLI
- Hallucination Detection
- Benchmark
one_liner: 提出开放问答语义正确性分类体系、配套数据集与双向NLI驱动的CAP评估指标，效果优于现有基线
practical_value: '- Agent问答模块效果评估可复用8类语义正确性分类体系，精细化拆解幻觉、信息不全、内容矛盾等错误类型，替代粗粒度对错标注

  - 电商商品问答、客服LLM的自动评估可借鉴CAP指标思路，用双向NLI匹配参考回答，避免表面相似度高但语义错误的误判

  - 垂直领域问答评估模型训练可复用QA对转声明式语句的数据集构造方法，大幅降低标注成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
开放问答的自由形式回答存在多种正确表述，也存在信息不全、内容矛盾、幻觉生成、认可错误前提等不同错误类型，现有基于人工判断或语义相似度的指标无法区分这些差异，是LLM问答正确性评估的核心瓶颈。
### 方法关键点
1. 构建8阶有序语义正确性分类体系，可清晰区分表述冗余但正确、存在幻觉污染等不同回答类型
2. 开源两个配套数据集：8.8k样本的CAP-Correctness基准，覆盖主流QA数据集；11k样本的CAP-Statements，支持将QA对转换为声明式语句，用于NLI训练和语句级评估
3. 提出参考式评估指标CAP，基于双向NLI对问题约束下的回答语句进行打分
### 关键结果
在检验指标是否符合分类体系预设排序的单调性协议测试中，CAP表现显著优于所有已有基线指标。

---
title: 'CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases'
title_zh: CorporateBench：面向时序知识库的大规模问答评测基准
authors:
- Sil Hamilton
- Albert Yu Sun
- Oscar J. Romero
- Carl-Leander Henneking
- David Mimno
- Bishan Yang
- Igor Labutov
affiliations:
- Epiq AI Labs
- Cornell University
arxiv_id: '2608.27391'
url: https://arxiv.org/abs/2608.27391
pdf_url: https://arxiv.org/pdf/2608.27391
published: '2026-08-27'
collected: '2026-08-28'
category: Eval
direction: 大模型评测 · 企业级多文档问答
tags:
- Benchmark
- Multi-document QA
- Temporal KB
- Enterprise LLM
- RAG Evaluation
one_liner: 构建了贴合企业真实场景的23万+文档规模、时序一致的多任务问答评测基准
practical_value: '- 搭建企业内部知识库Agent/电商跨时段规则问答RAG系统时，可直接用该基准测试大模型长上下文多文档推理性能，辅助模型选型

  - 构建业务专属评测集时，可借鉴「用时序演化知识库生成一致语料」的方法，解决人工标注逻辑矛盾、样本量不足的问题

  - 电商跨活动规则查权益、广告投放多周期效果归因等场景，可参考该基准的双维度设计分层效果评估指标'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
企业级多文档问答是LLM落地核心场景，但现有评测存在两大痛点：企业不愿公开内部敏感语料，开源合成数据集逻辑一致性差、规模过小，无法匹配真实业务复杂度。
### 方法关键点
基于时序演化的一致性知识库生成4个规模从12人到10000人的模拟企业语料，构建总规模超23万文档的多任务问答基准，覆盖信息抽取、知识库查询两大维度，所有跨文档逻辑自洽，单问题平均对应87.6份参考文档，远高于此前同类基准的1.5。
### 关键结果
在5款主流LLM上测试验证，当输入规模接近真实企业量级时，模型性能出现显著下滑，可有效衡量大模型的企业场景推理能力。

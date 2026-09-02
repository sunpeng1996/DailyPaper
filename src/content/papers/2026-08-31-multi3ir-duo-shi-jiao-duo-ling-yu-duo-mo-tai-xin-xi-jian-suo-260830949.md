---
title: 'MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information
  Retrieval'
title_zh: MULTI3IR：多视角多领域多模态信息检索基准
authors:
- Seokwon Song
- Sohyeon Kim
- Gunhee Kim
affiliations:
- Seoul National University
arxiv_id: '2608.30949'
url: https://arxiv.org/abs/2608.30949
pdf_url: https://arxiv.org/pdf/2608.30949
published: '2026-08-31'
collected: '2026-09-02'
category: Eval
direction: 多模态信息检索 · 基准构建与优化
tags:
- Multimodal IR
- Benchmark
- Open-ended Query
- Embedding Optimization
- Efficient Tuning
one_liner: 推出含104.9K标注查询的多视角多域多模态IR基准Multi3IR及高效优化方法SPIN
practical_value: '- 电商开放式搜索/导购场景做query召回时，可借鉴SPIN的噪声向量引导嵌入思路，提升多视角结果覆盖，避免结果同质化，满足用户多元隐含需求

  - 构建业务内部搜索/召回效果评估基准时，可参考Multi3IR的多视角标注方法，覆盖用户query的隐含需求维度，提升评估的全面性和合理性

  - 面向电商咨询、导购的RAG系统针对开放式用户问题做文档召回时，可复用SPIN方法优化召回结果的视角多样性，减少关键信息遗漏'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有IR基准多聚焦封闭式query，即使是开放query基准也大多局限于单领域单模态，无法评估召回对开放query多视角隐含需求的覆盖能力，难以适配开放式搜索、RAG等场景的效果评估需求。
### 方法关键点
1. 构建Multi3IR基准，包含104.9K来自Stack Exchange的开放query，每个query标注了对应隐含视角的描述，覆盖多领域多模态场景。
2. 提出参数、标注高效的SPIN方法，仅学习噪声向量引导嵌入向多样且有意义的语义方向偏移，无需大规模调参或标注。
### 关键结果
实验证明现有多模态召回器普遍存在单视角偏见，SPIN可在Multi3IR上大幅提升视角覆盖率，且可泛化到未见过的开放域IR基准。

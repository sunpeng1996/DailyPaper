---
title: 'ARCS: Towards Precise Text-to-SQL via Structured Disambiguation'
title_zh: ARCS：通过结构化消歧实现精准Text-to-SQL
authors:
- Yihao Hu
- Yanlin Feng
- Naoki Otani
- Nikita Bhutani
affiliations:
- Duke University
- Megagon Labs
arxiv_id: '2610.09396'
url: https://arxiv.org/abs/2610.09396
pdf_url: https://arxiv.org/pdf/2610.09396
published: '2026-10-06'
collected: '2026-10-13'
category: Reasoning
direction: 大模型推理 · Text-to-SQL消歧与基准构建
tags:
- Text-to-SQL
- Ambiguity Resolution
- Benchmark
- LLM Reasoning
- Structured Interaction
one_liner: 提出结构化消歧范式，构建首个覆盖真实歧义的Text-to-SQL基准数据集ARCS
practical_value: '- 面向商家/运营的数据分析Agent可复用结构化消歧思路，用约束式选项替代自由对话澄清查询歧义，降低用户交互成本

  - 搭建业务专属Text-to-SQL能力时，可参考ARCS的标注范式，补充歧义点、多合法解释、对应SQL的标注，提升模型鲁棒性

  - 评估内部Text-to-SQL系统性能时，可引入类似ARCS的含歧义测试集，避免无歧义基准带来的性能虚高问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有主流Text-to-SQL基准多由无歧义、过明确的查询构成，与真实用户自然提问的偏差极大；传统采用自由对话澄清歧义的方案效率低、认知成本高，与实际用户工作流不匹配，歧义已成为Text-to-SQL落地的核心错误来源。
### 方法关键点
提出结构化消歧新范式，通过显式、受约束的交互替代自由对话解决歧义；构建ARCS基准，是首个覆盖真实数据库上自然存在的无约束歧义的Text-to-SQL数据集，完整标注了所有合法歧义点、对应解释及正确SQL语句。
### 关键结果
存在歧义的场景下Text-to-SQL性能大幅下降：gpt-6-sol端到端执行准确率仅为51%，所有开源模型的准确率均不超过27%。

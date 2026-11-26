---
title: When Does Reasoning Help Entity Disambiguation? Small LLMs In-Domain and Under
  Shift
title_zh: 推理何时助力实体消歧：域内与域偏移下的小LLM效果研究
authors:
- Samy Haffoudhi
- Fabian M Suchanek
- Nils Holzenberger
affiliations:
- Télécom Paris, Institut Polytechnique de Paris
arxiv_id: '2611.30334'
url: https://arxiv.org/abs/2611.30334
pdf_url: https://arxiv.org/pdf/2611.30334
published: '2026-11-22'
collected: '2026-11-26'
category: Reasoning
direction: 小LLM推理 · 实体消歧
tags:
- Entity Disambiguation
- Small LLM
- Reasoning
- Domain Shift
- Zero-shot Learning
one_liner: 对比小LLM实体消歧三类候选选择范式，明确推理收益随域偏移提升的适用边界
practical_value: '- 电商搜索Query实体消歧场景，域内流量优先用轻量reranking方案，推理范式仅留作冷启动/跨域新类目场景补充，降本提效

  - 可复用「reranker不确定性+域偏移程度」双维度决策逻辑，动态切换小LLM的候选选择范式，平衡性能与推理成本

  - 小LLM做推理类任务时，可通过蒸馏+强化学习组合训练范式，在零样本场景下获得接近大模型的泛化能力'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
大LLM基于推理的实体消歧已实现SOTA零样本泛化能力，但小LLM场景下推理范式的性价比边界尚未明确，传统实体消歧多依赖重排序方案，缺乏跨场景的系统性效果对比。
### 方法关键点
在经典的从粗到精实体消歧 pipeline 中，对比 pointwise 重排序、listwise 直接选择、推理式三类候选选择范式，覆盖域内常规、少样本、真零样本三种业务常见场景，推理范式采用知识蒸馏+强化学习组合方式训练。
### 关键结果
域内场景下推理范式收益可忽略；真零样本跨域场景下推理范式效果显著占优；两类范式的效果差异可通过重排序模型的候选不确定性定位，域偏移程度直接决定范式冲突时的正确选择。

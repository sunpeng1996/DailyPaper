---
title: 'MultiGhostBench: A Multilingual Benchmark for Long-Form LLM-Generated Text
  Attribution under Distribution Shifts'
title_zh: 面向分布偏移的多语言长文本LLM生成归属评测基准MultiGhostBench
authors:
- Matteo Greco
- Anudeex Shetty
- Andrea Tagarelli
- Jey Han Lau
affiliations:
- The University of Melbourne, Australia
- University of Calabria, Italy
arxiv_id: '2609.02379'
url: https://arxiv.org/abs/2609.02379
pdf_url: https://arxiv.org/pdf/2609.02379
published: '2026-09-02'
collected: '2026-09-05'
category: Eval
direction: LLM生成内容归属 · 多语言评测基准
tags:
- LLM Attribution
- Multilingual Benchmark
- Distribution Shift
- Long-form Text
- Evaluation
one_liner: 推出覆盖6种语言、平均单文本5.9万字的多语言长文本LLM生成归属评测基准，支持三类分布偏移评测
practical_value: '- 电商多语言站点的AI生成商品文案、种草内容归属检测，可优先选用Transformer-based检测器，跨语言迁移效果优于统计/指纹类方案

  - LLM生成内容风控系统上线前，可参考该基准的分布偏移评测范式，验证跨域、跨语言、跨生成模型场景下的鲁棒性，规避线上性能下跌

  - 小语种电商内容风控场景不建议直接复用其他语言的统计/指纹类检测模型，需针对目标语言单独优化特征和规则'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LLM生成文本归属（AA）评测基准多聚焦英文、短文本、受控场景，缺乏覆盖多语言、长文本、分布偏移场景的公开评测资源，难以支撑鲁棒AA方法的研发验证。
### 方法关键点
构建MultiGhostBench基准，包含5款最新LLM生成的928本图书，覆盖6种语言、3种书写系统，单本平均长度约59K词，支持域、生成模型、语言三类分布偏移场景下的AA方法评测。
### 关键结果
无单一AA方法在所有评测场景下性能最优，分布偏移下所有方法性能普遍下降；Transformer类检测器可跨语言保留生成模型相关特征，迁移效果随语言对差异浮动，统计/指纹类检测器语言依赖性更强，跨语言迁移效果差

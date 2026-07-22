---
title: 'Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark
  for Factual Completeness'
title_zh: 面向开放生成的双层元评分规则：事实完整性评估基准GAMUT
authors:
- Xilun Chen
- Zhaleh Feizollahi
- Ross Goodwin
- Seungwhan Moon
- Scott Yih
- Pinar Donmez
- Babak Damavandi
- Luna Dong
affiliations:
- Meta AI
arxiv_id: '2607.19322'
url: https://arxiv.org/abs/2607.19322
pdf_url: https://arxiv.org/pdf/2607.19322
published: '2026-07-20'
collected: '2026-07-22'
category: Eval
direction: 大模型生成评估 · 事实完整性检测
tags:
- Evaluation
- Factuality
- LLM Benchmark
- Open-ended Generation
- Factual Completeness
one_liner: 提出双层元评分规则框架，推出跨模态开放生成事实完整性评估基准GAMUT
practical_value: '- 生成式推荐/Agent应答的事实校验场景，可复用双层评分架构：先定义结构化内容要求与权重，再拆解为可自动打分的二分类校验项，补足传统校验仅查准确率、不覆盖完整性的短板

  - 电商商品详情生成、智能客服应答的效果评估，可参考该框架搭建自定义校验规则，兼顾信息覆盖度、优先级与逻辑关联，避免漏传核心商品卖点、活动规则等关键信息

  - 用LLM judge做生成内容评估时，先将模糊的评估要求拆解为结构化元规则再转成可执行checklist，能大幅提升评估一致性，降低人工标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有长文本生成事实性评估多聚焦precision，主流decompose-search-verify pipeline仅能识别错误声明，无法衡量应答的事实完整性；事实集合往往带有层级、顺序、关联关系，传统独立布尔校验无法覆盖这类复杂要求。
### 方法关键点
1. 推出双层元评分规则框架：上层结构化元评分规则定义所需内容的组织结构、重要性权重，自动编译为扁平的可机器打分的二分类校验清单，供LLM judge可靠评分
2. 落地为GAMUT基准，覆盖10个领域共1813个基于真实可穿戴设备影像的问题，配套专家标注的证据支撑校验规则，同时提供纯文本版本
### 关键结果
对14个前沿/开源模型测试，最高得分仅为Gemini 3.1 Pro的58.7%，基准难度高、区分度强、评估结果不受LLM judge选择影响

---
title: 'LLMs Can See the Smoke but not the Fire: Evaluating Abductive Reasoning with
  Elenchos'
title_zh: 《LLM 可见烟不见火：基于 Elenchos 的溯因推理能力评估》
authors:
- Julius Steiglechner
- Lucas Mahler
- Gabriele Lohmann
arxiv_id: '2607.12733'
url: https://arxiv.org/abs/2607.12733
pdf_url: https://arxiv.org/pdf/2607.12733
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: 大语言模型溯因推理能力评估
tags:
- Abductive Reasoning
- LLM Evaluation
- Elenchos
- Reasoning Benchmark
- Inference Performance
one_liner: 提出Elenchos生成式评估框架，发现LLM溯因推理存在检测-归因解离缺陷
practical_value: '- 做Agent决策归因、用户行为异常归因、推荐效果波动根因分析等场景时，不可完全依赖LLM单轮推理输出，需搭配规则校验补全归因漏判

  - 涉及多变量交互的根因分析任务，可将复杂关联问题拆解为单变量推理子任务，缓解LLM在多突变场景下的性能衰减

  - 内部评估LLM推理能力时，可复用Elenchos的「参考系统对比→突变检测→根因归因」三层范式，定制业务场景推理benchmark'
score: 8
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前LLM在模式识别、文本生成任务上表现优异，但溯因推理（从观测现象反推潜在解释性假设的能力）的性能边界尚未被系统量化，缺乏针对性的评估方案。
### 方法关键点
提出Elenchos生成式评估框架，将溯因推理转化为结构逆问题：给定参考正式系统（如lambda演算）与其可能发生规则突变的变体，要求被测Agent完成两个子任务：1. 判断系统是否发生突变；2. 反推造成行为差异的具体规则修改点。
### 关键结果
1. 前沿、中端LLM均存在稳定的检测-归因解离现象：超80%场景下可准确识别系统发生变更，但仅不足30%场景能准确定位底层突变规则；
2. 存在多突变交互时性能大幅衰减，仅能识别不到20%的全部底层突变；
3. 增加推理时计算预算的收益边际递减，推理预算翻倍仅带来最高12%的归因准确率提升，增益有限。

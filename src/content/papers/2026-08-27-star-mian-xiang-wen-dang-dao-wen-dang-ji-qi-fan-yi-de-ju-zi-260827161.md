---
title: 'STAR : Sentence Translation Alignment Rate for Document-to-Document Machine
  Translation'
title_zh: STAR：面向文档到文档机器翻译的句子翻译对齐率
authors:
- Yichen Dong
- Hao Wang
- Junhui Li
- Linlong Xu
- Longyue Wang
- Weihua Luo
affiliations:
- Soochow University
- Alibaba Group
arxiv_id: '2608.27161'
url: https://arxiv.org/abs/2608.27161
pdf_url: https://arxiv.org/pdf/2608.27161
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: LLM训练优化 · 结构保真对齐
tags:
- Doc2Doc Translation
- Preference Optimization
- Structural Fidelity
- LLM Training
- Evaluation Metric
one_liner: 提出句级结构保真指标STAR与StarPO偏好优化框架，提升文档到文档翻译质量
practical_value: '- 电商场景下商品详情页多语言翻译、长文案生成任务，可引入STAR类句级对齐指标，评估信息完整度，避免遗漏核心卖点

  - 做LLM偏好优化时可复用动态对齐掩码思路，仅针对错误/缺失片段梯度更新，降低训练token成本，提升小模型性能

  - 长文本生成类Agent任务（比如合同翻译、商品内容批量生成）可参考StarPO框架，先排序生成假设再优化错漏段，减少幻觉'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM支撑文档到文档（Doc2Doc）机器翻译从单句生成升级为整文档单次生成，能提升全局连贯性，但普遍存在句子遗漏、幻觉等结构错位问题，无法满足源-目标内容严格对应的核心要求。
### 方法关键点
1. 提出STAR（Sentence Translation Alignment Rate）辅助指标，显式量化句级结构保真度；
2. 提出STAR-masked Preference Optimization（StarPO）框架：先按结构质量对文档级生成假设排序，再通过动态对齐掩码，仅针对未对齐片段做优化。
### 关键结果
在新闻、文学两个领域测试，基于Qwen2.5-7B实现的方案STAR达98.43%，小模型效果超过GPT-4o等大体积商用系统，同时token效率更优，漏句、幻觉问题大幅减少。

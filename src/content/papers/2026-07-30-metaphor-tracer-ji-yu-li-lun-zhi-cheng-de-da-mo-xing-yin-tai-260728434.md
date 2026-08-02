---
title: 'Metaphor Tracer: A Theory-Informed Analysis of Hidden States'
title_zh: Metaphor Tracer：基于理论支撑的大模型隐状态分析方法
authors:
- Marc Heimann
- Roxana Assadi Moghaddam
- Olga Brovkina
- Mark Pettifor
- Lutz Goetzmann
affiliations:
- Hermeneutic AI
arxiv_id: '2607.28434'
url: https://arxiv.org/abs/2607.28434
pdf_url: https://arxiv.org/pdf/2607.28434
published: '2026-07-30'
collected: '2026-08-02'
category: LLM
direction: LLM隐状态可解释性分析
tags:
- Hidden States
- LLM Interpretability
- Zero-training Analysis
- Token Representation
- Structural Feature Extraction
one_liner: 无需训练仅单次前向传播即可从LLM隐状态提取token结构特征，匹配人类文本理解标注
practical_value: '- 可复用无训练隐状态分析思路，在RAG/电商导购Agent场景下快速识别query/上下文的核心结构token，过滤冗余信息，降低召回成本

  - 文本token的上下文关联属性结论可用于用户评论/商品详情的语义核心提取，替代传统关键词匹配，提升推荐系统特征质量

  - 基础模型与指令微调模型的结构感知差异结论可指导推荐场景LLM底座选型，优先选择指令微调版本提升文本语义理解保真度'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM隐状态分析多聚焦token固有语义属性，缺乏对其在单篇文本中上下文结构作用的高效度量方案，且大多需要额外训练成本，难以直接落地。

### 方法关键点
提出Metaphor Tracer无训练分析框架，仅通过单次前向传播即可对每个token位置输出两类得分：①aggregator：衡量该位置是否将全文信息整合为稳定配置；②differentiator：衡量其他token是否被临时携带到该位置的子空间。所有常量仅在单篇探索文本上冻结，其余样本全部用于验证。

### 关键结果数字
跨3种异源LLM验证指标有效性：engineered语域边界识别任务准确率达6/6；预标注临床转录文本结构匹配任务准确率达34/36，效果显著优于词汇层面基线；指令微调可提升结构感知保真度，且不会改变词汇类型迁移特性。

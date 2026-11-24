---
title: 'Needwise: Generation-Free Conversational Recommendation from Need-Level Typed
  Decisions'
title_zh: Needwise：基于需求层级分类决策的无生成式对话推荐框架
authors:
- Sungchul Kim
- Weixiao Huang
- Mekala Raja Sekhar Reddy
- Amrutha Srinivasan
affiliations:
- Adobe Research
- Adobe Inc.
arxiv_id: '2611.31175'
url: https://arxiv.org/abs/2611.31175
pdf_url: https://arxiv.org/pdf/2611.31175
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 对话式推荐 · 分类决策优化
tags:
- Conversational Recommendation
- Typed Decision Model
- Preference Tracking
- Reranking
- Cost Optimization
one_liner: 用分类决策替代生成式LLM构建对话推荐，性能持平顶级LLM且延迟、成本大幅降低
practical_value: '- 对话推荐场景可采用分类决策替代全生成LLM做偏好解析、候选校验，能在保持效果的前提下将延迟降低50%+、API成本降至1/10左右，适合高并发业务

  - 可复用must-first排序逻辑：先硬性过滤品类、位置、价格等强约束，再融合整体匹配分和细粒度需求匹配分，无调参需求易落地，还能输出每个需求的匹配解释

  - 历史需求校验结果可缓存复用，用户修改/撤回需求时无需全量重新计算，大幅降低多轮对话的计算开销

  - 分类决策模型对需求撤回的识别准确率偏低（20%左右），落地时可叠加轻量生成式意图识别模块修正这类bad case'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有基于LLM的对话推荐每轮都要重读全量对话和候选，延迟高、成本高，且无法输出每个需求的匹配依据；同时用户需求动态变化（新增/撤回/反转），传统方案难以高效跟踪状态，还面临商品库schema无法覆盖所有用户需求的问题。

### 方法关键点
- 全流程采用分类决策模型（无生成文本），仅输出选项概率：首先对用户输入做分类解析，映射到商品库已有的字段属性，无法映射的需求直接保留用户原句作为软特征
- 需求分为硬约束（品类、位置、价格，必须满足）和软偏好，对每个候选+需求对输出三分类结果：支持/矛盾/证据不足，计算证据分=支持概率-矛盾概率
- 提供三种排序策略：Needwise-F仅用需求级证据分排序，Needwise-H用单问题整体评估候选匹配度，Needwise-HF融合两者，硬约束优先，同层级内整体分和需求级分等权重相加，无调参
- 多轮对话状态用分类决策跟踪，自动识别用户新增/撤回/反转需求，已计算的候选-需求匹配结果缓存复用，无需重复计算

### 关键实验
在Google Local（320条请求）、Yelp（320条请求）数据集上对比GPT-4o、GPT-5、GPT-6 Sol/Luna、Qwen系列重排器等基线：Needwise-HF在Google Local上nDCG@10达0.383，比GPT-6 Sol高0.04，持平最强基线GPT-5；Yelp上nDCG@10达0.428，与GPT-6 Sol、Qwen3.8-27B无显著差异；中位数延迟仅2.5s，是GPT-6 Sol的45%，每千次请求成本3美元，仅为GPT-6 Sol的7%。

### 核心结论
对话推荐不一定需要全生成LLM，用轻量分类决策做意图解析、候选校验，在效果持平的前提下能获得数倍的成本和延迟优势，是工业落地的优选项

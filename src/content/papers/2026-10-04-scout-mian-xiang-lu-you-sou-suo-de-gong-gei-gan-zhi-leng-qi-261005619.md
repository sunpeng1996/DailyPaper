---
title: 'SCOUT: Supply-Aware Cold-Start Proactive Query Suggestion for Travel Search'
title_zh: SCOUT：面向旅游搜索的供给感知冷启动主动查询推荐
authors:
- Hao Li
- Shashank Reddy
- Kedar Bellare
- Ashish Jain
- Stephanie Moyerman
affiliations:
- Airbnb, Inc.
arxiv_id: '2610.05619'
url: https://arxiv.org/abs/2610.05619
pdf_url: https://arxiv.org/pdf/2610.05619
published: '2026-10-04'
collected: '2026-10-06'
category: QueryRec
direction: Query推荐 · 冷启动供给感知优化
tags:
- QuerySuggestion
- ColdStart
- GRPO
- LLM4IR
- ReinforcementLearning
one_liner: 基于供给侧RL训练LLM实现无用户日志的旅游冷启动主动Query推荐，零额外推理成本
practical_value: '- 冷启动无用户行为数据场景，可复用现有系统的供给侧信号（如搜索排序匹配分）替代用户反馈做RL训练，无需依赖标注/历史日志

  - 对生成多样性要求高的Query推荐/文案生成场景，优先选GRPO做偏好优化，可大幅降低DPO/RPO容易出现的多样性坍缩风险

  - 实时链路的生成类需求可把serving阶段best-of-N的校验成本摊销到训练阶段，上线后零额外推理延迟和成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式Query推荐依赖用户历史查询、点击数据做对齐，且不感知供给库存；旅游搜索场景既无历史自由文本Query日志，又受属地化实体库存限制，生成无对应库存的query会直接导致空结果页，而serving时做best-of-N过滤的方案延迟和成本过高，无法落地实时链路。

### 方法关键点
- 无标注评估体系：定义IMR@18（Query返回首页18个房源与query的语义匹配率）衡量库存匹配度，distinct%@0.9（嵌入聚类后不同query占比）衡量生成多样性，两者均可通过LLM judge和预训练嵌入自动计算，无需人工标注
- 低成本奖励设计：复用现有搜索排序模块的query-房源语义匹配分作为RL的免费奖励信号，与IMR@18的斯皮尔曼相关系数达0.45，无需额外推理开销
- 训练框架：基于Qwen3-8B做LoRA微调，用GRPO做策略优化，将搜索系统作为RL环境，把库存感知能力直接蒸馏到模型权重

### 关键结果
训练/测试集按目的地拆分保证泛化性，对比few-shot prompting、RSFT、DPO、RPO基线：SCOUT的IMR@18相对提升12.3%，distinct%@0.9仅下降0.31个百分点基本持平，效果等同于serving时best-of-8的方案，但零额外推理成本。

最值得记住的一句话：没有用户行为数据的冷启动场景，供给侧系统自带的信号是可直接用于LLM对齐的高质量反馈源。

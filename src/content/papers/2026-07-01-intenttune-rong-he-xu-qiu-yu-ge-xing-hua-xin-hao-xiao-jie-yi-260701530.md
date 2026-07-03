---
title: 'IntentTune: Using user demand and personalization to resolve "unknown" query
  intents for e-commerce search'
title_zh: IntentTune：融合需求与个性化信号消解电商搜索未知查询意图
authors:
- Rachith Aiyappa
- Ishita Khan
- Chester Palen-Michel
- Jayanth Yetukuri
- Samarth Agrawal
- Mehran Elyasi
- Shuang Zhou
affiliations:
- eBay Inc., USA
arxiv_id: '2607.01530'
url: https://arxiv.org/abs/2607.01530
pdf_url: https://arxiv.org/pdf/2607.01530
published: '2026-07-01'
collected: '2026-07-03'
category: QueryRec
direction: 电商搜索 · 模糊查询个性化意图补全
tags:
- Query Understanding
- E-commerce Search
- Personalization
- Intent Inference
- Ambiguous Query
one_liner: 提出融合全局消费需求与用户行为信号的查询意图补全框架，提升电商模糊搜索效果
practical_value: '- 可直接在现有query理解流水线新增IntentTune插件：基线模型输出unspecified时触发处理，无需改动原有成熟意图模型，落地成本低

  - 模糊query意图补全的信号优先级可直接复用：近1个月高置信度历史查询 > 静态用户Profile > 全局需求统计，按该顺序选取特征即可获得最优效果

  - 低成本LLM落地范式可复用：Prompt仅需包含意图类定义、模糊查询、高置信度历史行为/候选分类列表，无需微调模型即可实现不错的个性化意图推断效果

  - 类目优化可直接复用逻辑：基于用户行为从基线输出的候选类目中筛选最优，可在68.5%的场景下将多候选压缩为单正确类目，有效降低下游检索算力消耗'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
电商搜索中存在大量短模糊查询（如"watch""shirt"），仅依赖文本的BERT类基线意图模型无法推断性别、年龄、尺码等隐式属性，输出"unspecified"标签，导致下游检索召回低、排序质量差，仅靠全局消费需求统计无法覆盖用户个性化差异，亟需低成本的意图补全方案。

## 方法关键点
- 插件式架构：原有基线意图模型输出缺失属性的查询时触发IntentTune，无需修改现有流水线，包含两个互补模块：
  1. 需求模块：基于基线类目预测模型的top置信度类目反推性别、年龄属性，不适用于尺码维度避免损伤召回；
  2. 个性化模块：输入近1个月高置信度（性别置信>0.8、年龄置信>0.9）的历史查询、用户Profile属性，调用内部LLM完成缺失属性推断，同时支持从基线输出的候选类目中筛选最优细分类目。

## 关键实验结果
基于eBay真实时尚类搜索数据构建900组人工标注的模糊query-用户对，对比三类方案：
- 年龄维度：历史查询方案加权F1达0.816，较需求基线提升17%；
- 性别维度：历史查询方案准确率0.741，较需求基线提升近1倍，加权F1提升超90%；
- 尺码维度：历史查询方案加权F1达0.853；
- 类目优化：68.5%的多候选类目可被压缩为单正确类目，大幅降低下游检索压力。

## 核心结论
电商查询理解不应是静态通用的，而需结合用户行为做个性化、上下文感知的推断

---
title: 'Next-Gen Sponsored Search: Crafting the Perfect Query with Inventory-Aware
  RAG (InvAwr-RAG) Based GenAI'
title_zh: 面向电商赞助搜索的库存感知RAG生成式查询改写方案
authors:
- Md Omar Faruk Rokon
- Weizhi Du
- Zhaodong Wang
- Musen Wen
affiliations:
- Walmart AdTech
arxiv_id: '2607.03880'
url: https://arxiv.org/abs/2607.03880
pdf_url: https://arxiv.org/pdf/2607.03880
published: '2026-07-04'
collected: '2026-07-07'
category: QueryRec
direction: QueryRec · 电商赞助搜索查询改写
tags:
- Query Rewriting
- RAG
- Sponsored Search
- LoRA
- E-commerce Advertising
one_liner: 沃尔玛提出InvAwr-RAG查询改写方案，将无广告返回查询的填充率提升68%
practical_value: '- 做零结果广告查询补全时，优先采用绑定实时库存、广告预算约束的RAG架构，避免纯生成改写的query无对应可投放广告，浪费流量

  - Query Rewrite LLM可选择7B级开源模型用LoRA微调，在垂直场景效果优于通用GPT-4，兼顾成本与落地效率

  - 改写query池可采用LLM生成+历史高转化热门query融合的方案，兼顾生成的多样性和历史验证的转化稳定性

  - 落地参数可参考配置：召回Top20相关库存商品、生成5条改写query，平衡匹配覆盖度、相关性与计算开销'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商赞助搜索是平台核心营收来源，沃尔玛平台约13%的用户搜索查询无法匹配到任何可投放的广告，既造成直接营收损失，也影响用户购物体验与广告主投放ROI；现有查询改写方案多只关注语义相似性，忽略实时库存、广告投放预算等业务约束，改写后的query仍经常无对应广告可投，无法解决零填充率问题。
### 方法关键点
- 整体为双塔BERT+LoRA微调Llama2 7B的库存感知RAG架构（InvAwr-RAG），专门针对低填充率查询做改写
- 核心流程：规则分类识别低填充率查询→召回Top20满足预算约束的相关库存商品→结合原query与商品属性构造prompt→LLM生成改写query→补充历史高转化相似热门query→融合后取5条最优query用于广告检索→交叉编码器校验广告相关性
- 训练数据基于半年内累积点击超500次的query-商品对，加人工标注过滤冗余query，保证改写query的真实转化效果
### 关键实验
离线测试集为1万条历史0填充率的用户查询，基线填充率为0，GPT-4改写方案实现53%填充率、NDCG@8为0.6458；InvAwr-RAG实现68%填充率，NDCG@8达0.6847，相关性更优。
### 最值得记住的一句话
工业级赞助搜索查询改写不能只追求语义匹配，必须绑定实时库存、广告预算等业务约束，才能真正把无效流量转化为营收。

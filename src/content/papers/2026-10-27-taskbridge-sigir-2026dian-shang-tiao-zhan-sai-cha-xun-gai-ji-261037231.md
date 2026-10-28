---
title: 'TaskBridge: Technical Report for SIGIR 2026 eCommerce Challenge'
title_zh: TaskBridge：SIGIR 2026电商挑战赛查询改写赛道技术报告
authors:
- Zhiheng Fu
- Yupeng Hu
- Zixu Li
- Zhiwei Chen
- Qinlei Huang
- Shaokun Wang
- Han Liu
- Fan Liu
- Weili Guan
- Liqiang Nie
affiliations:
- Shandong University
- Harbin Institute of Technology (Shenzhen)
- City University of Hong Kong
- Southeast University
arxiv_id: '2610.37231'
url: https://arxiv.org/abs/2610.37231
pdf_url: https://arxiv.org/pdf/2610.37231
published: '2026-10-27'
collected: '2026-10-28'
category: QueryRec
direction: 电商搜索 · 任务型Query改写
tags:
- QueryReformulation
- E-commerceSearch
- BM25
- LLM4IR
- CatalogAnchoring
one_liner: 基于商品目录锚定的任务型电商查询改写框架，获SIGIR2026电商挑战赛第一名
practical_value: '- 做任务型query改写时可先离线构建商品目录的语义锚（仅保留可购买的类目、实体、配件），避免LLM生成的query和商品库词汇不匹配的问题，直接提升BM25检索的召回准确率

  - 多候选生成+协议感知选择的架构可直接复用：针对单query/多query场景，分别优先选质量最高的单条，或选质量+结果多样性平衡的候选集，适配自动搜索/交互式搜索不同业务需求

  - 无需训练的全推理pipeline可快速落地：直接调用开源LLM、Embedding、Reranker模型组合即可上线，不用标注大量业务训练数据，冷启动成本极低

  - 迭代改写的边际阈值控制可复用：反馈改写时仅当新候选的代理分超过当前候选δ时才更新，避免生成式改写过度漂移偏离用户原始意图'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索中用户常输入任务型query（如"做千层面"），不直接指定商品，和商品库标题存在明显词汇鸿沟，普通BM25检索无法召回匹配商品；现有生成式改写容易出现改写不足（漏覆盖所需商品）或过度改写（引入无关商品）的问题，且需适配单条输出的自动搜索、多条输出的交互场景的不同需求。
### 方法关键点
- Catalog Semantic Anchoring模块：离线从商品库构建两类词表，标题词表用于生成仅包含可购类目的语义锚集合，全字段词表用于改写时的词汇约束，避免生成商品库不存在的词汇
- Unified Five-Candidate Rewriting模块：生成5类互补候选，分别为原始query、多轮反馈改写query、多角色投票改写query、保守需求感知改写query、紧凑商品导向改写query，覆盖不同改写程度的可能性
- Protocol-Aware Selection模块：用BM25 Top10结果的Reranker加权分作为候选质量代理分，自动场景选质量最高的单条，交互场景通过加权Jaccard重叠度选质量和结果多样性平衡的4条候选
### 关键实验
在SIGIR2026电商挑战赛任务型query改写数据集上，对比原始query直接BM25检索的基线，Open阶段自动场景NDCG@10从0.42提升到0.49，交互场景NDCG@10提升到0.58；Closed阶段自动场景NDCG@10为0.27，交互场景为0.31，位列赛道第一名。
> 最值得记住的一句话：任务型电商query改写的核心是在不丢失原始任务意图的前提下，将隐含需求映射到商品库真实存在的词汇，而非生成语义通顺但无匹配商品的query。

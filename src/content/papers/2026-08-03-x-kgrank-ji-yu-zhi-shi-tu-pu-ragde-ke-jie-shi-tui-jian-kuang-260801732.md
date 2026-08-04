---
title: 'X-KGRank: A Knowledge Graph RAG Framework for Explainable Recommendations
  via Pattern Mining and LLM Re-Ranking'
title_zh: X-KGRank：基于知识图谱RAG的可解释推荐框架
authors:
- Meenakshi Rajpurohit
- Jainish Patel
affiliations:
- San Jose State University
arxiv_id: '2608.01732'
url: https://arxiv.org/abs/2608.01732
pdf_url: https://arxiv.org/pdf/2608.01732
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 可解释推荐 · 知识图谱RAG+LLM优化
tags:
- Knowledge Graph
- RAG
- Explainable Recommendation
- LightGCN
- LLM
- Re-Ranking
one_liner: 融合知识图谱RAG、LightGCN排序与LLM解释，通过热门度路由降低检索成本并提升推荐效果
practical_value: '- 可直接复用热门度选择性路由策略：仅对长尾/冷启动商品做KG路径检索，热门商品直接用LLM预训练知识生成解释，可减少至少50%的检索计算量

  - LightGCN的item embedding可采用SBERT编码的商品语义信息（标题、品类、属性等）初始化，能显著缓解冷启动商品的向量噪声问题，提升排序效果

  - 做推荐解释场景的LLM选型时，1.5B级小模型在KG路径grounding的前提下，解释流畅度可媲美7B模型，但高可信场景优先选择7B及以上模型降低幻觉风险

  - 可复用四层KG路径降级检索策略：直接最短路径→共享属性桥→协同行为桥→语义相似fallback，保证所有候选都有可解释依据，避免解释空值'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前主流推荐方案存在明显短板：协同过滤类方法能捕捉用户行为信号但无法生成可理解的推荐理由，纯LLM推荐虽能生成流畅解释，但 hallucination 问题严重，且缺乏用户历史行为的扎实 grounding，用户信任度低。

### 方法关键点
- 构建包含用户、物品、属性三类节点，交互、从属属性、协同共现三类边的异质知识图谱，存储于Neo4j方便路径查询
- 用SBERT编码物品文本属性（标题、品类等）初始化LightGCN的item embedding，采用带评分权重的BPR目标训练排序模型，缓解冷启动问题
- 引入热门度选择性路由：按交互量中位数将物品分为热门和长尾两类，仅对长尾物品做2跳KG路径检索，减少约50%的检索开销
- 设计四层KG路径降级策略，保证任意候选都能获取grounding证据，LLM基于检索到的路径生成个性化推荐解释，最终排序保留LightGCN得分，避免LLM排序不稳定

### 关键结果数字
在MovieLens-1M数据集上，对比强热门度基线，NDCG@10和Recall@10均提升17.1%，NDCG@20提升15.6%，MRR提升14.6%；LLM对比实验中，Qwen2.5-1.5B的解释质量得分（0.97）略高于Mistral-7B（0.94），但小模型事实错误率显著更高。

### 核心结论
外部KG grounding可以大幅降低推荐解释任务对LLM参数量的依赖，但事实可靠性仍需要更大模型或额外的事实校验模块保障。

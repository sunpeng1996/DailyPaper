---
title: Do Current Retrievers Cover All the Evidence? A Controlled Study of Conjunctive
  Cross-Page Retrieval
title_zh: 合取跨页检索对照研究：现有检索器的证据覆盖能力评测
authors:
- Sungguk Cha
- DongWook Kim
- Mintae Kim
- Youngsub Han
- Byoung-Ki Jeon
- Sangyeob Lee
affiliations:
- LG Uplus, Seoul, South Korea
arxiv_id: '2607.24165'
url: https://arxiv.org/abs/2607.24165
pdf_url: https://arxiv.org/pdf/2607.24165
published: '2026-07-27'
collected: '2026-07-28'
category: Eval
direction: 检索系统评测 · 跨页合取检索
tags:
- Cross-Page Retrieval
- Conjunctive Query
- RAG
- Retrieval Evaluation
- Multimodal Fusion
one_liner: 通过70组对照实验量化跨页合取检索的发现-完成差距，明确条件拆分、多模态融合的优化价值
practical_value: '- 电商/广告多条件合取query检索场景（如用户同时要求「平价+防水+户外适用」），不要直接用联合向量检索，可拆分为单个条件分别检索再按最小/乘积规则聚合，实测能提升6.8-7.3个点的全条件文档优先排序准确率

  - 长文档多条件检索不要盲目上通用大模型reranker，实验验证4款通用reranker均会降低全条件文档的排序效果，反而文本+多模态（页面视觉）的等权RRF融合能带来8.7个点的效果提升，ROI更高

  - 不要盲目堆embedding模型参数量：实验中Qwen3-Embedding从0.6B扩容到8B，全条件优先排序的准确率无任何提升，优先做条件拆分、多模态融合的收益更高

  - 电商规则类、商品说明书类长文档检索场景，需新增单独的条件覆盖校验逻辑，不要仅依赖单文档相关性得分，避免将满足部分条件的干扰文档排在全条件匹配文档之前'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有检索系统与RAG应用面对多条件合取查询时，常出现全条件匹配的长文档（证据分散在不同页面）虽被召回，但排名低于仅满足部分条件的干扰文档的问题，传统检索指标仅关注是否召回相关文档，无法暴露这一核心瓶颈，直接导致RAG生成内容缺失关键信息、无法满足用户完整需求。

### 方法关键点
- 构建受控测试集CrossPage：包含1000个2/3条件的合取查询、2021份真实长文档（平均20.5页），标注每份文档满足的条件数、对应证据的页码，确保全条件匹配文档的证据分散在不同页面，同时构造天然的部分匹配干扰文档
- 定义核心指标n-Clue Score@k：要求top-k召回的全条件匹配文档必须排在所有部分匹配文档之前，区别于仅衡量召回率的Gold Hit指标，精准量化「发现-完成差距」
- 测试70组检索配置：覆盖不同参数量的dense检索器、稀疏检索、多模态检索、条件拆分聚合、RRF融合、通用reranker等方案，所有模型均为冻结推理，无额外调参，确保对比公平

### 关键结果
最优混合方案（BM25+多模态检索RRF融合）的Gold Hit@10达81.1%，但n-Clue Score@10仅35.8%，差距达45.3个点；条件拆分聚合提升dense backbone效果6.8-7.3个点，文本+视觉RRF融合再提8.7个点，4款通用reranker均降低Gold-NDCG；Qwen3-Embedding从0.6B扩容到8B，complete-first成功率无任何提升；多模态系统仅能在5.1%-5.3%的查询中返回所有条件对应的证据页。

多条件合取检索的核心瓶颈不是召回不到全条件文档，而是无法区分全条件匹配和部分匹配的文档，盲目堆模型参数量的收益远低于做条件拆分和多模态融合

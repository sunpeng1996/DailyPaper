---
title: 'SPEAR: Selection-aware Personalized End-to-end Adaptive Rewriting and Retrieval
  for Community Search'
title_zh: SPEAR：面向社区搜索的个性化端到端自适应查询重写检索框架
authors:
- Wenbin Wu
- Yuzhong Wu
- Yufan Xu
- Kuan Fang
- Xing Xu
- Cheng Ye
- Xiaobin Hu
affiliations:
- National University of Singapore
- Shanghai Dewu Information Group Co., Ltd.
arxiv_id: '2608.01738'
url: https://arxiv.org/abs/2608.01738
pdf_url: https://arxiv.org/pdf/2608.01738
published: '2026-08-03'
collected: '2026-08-04'
category: QueryRec
direction: QueryRec · 端到端查询重写优化
tags:
- query_reformulation
- end_to_end_retrieval
- dense_retrieval
- e_commerce_search
- personalized_retrieval
one_liner: 通过梯度隔离、乘法门控、动态选择器解决端到端查询重写的语义漂移与通用词优势问题
practical_value: '- 端到端优化query重写+检索链路时，可直接复用梯度隔离机制拆分召回/排序分支，避免CTR信号侵蚀召回侧语义表示，解决语义漂移问题

  - 替换路径式模型的加法聚合为乘法门控聚合，只有改写置信度和商品相关性同时高时才贡献分数，从结构上消除通用词作弊的捷径

  - 动态改写选择器可根据用户+原始query生成请求级权重和校准系数，无需依赖规则或预定义阈值就能适配不同query的改写偏好

  - 离线评估可同时用click recall、semantic similarity双指标，平衡业务转化和语义一致性，避免离线指标和线上效果错配'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有电商搜索的query重写和检索分阶段优化存在结构性错位，直接迁移推荐领域的路径式端到端架构会出现「通用词优势效应」：模型偏好高频通用改写，虽路径得分高但偏离原query语义，无法同时满足检索相关性和用户参与度要求。

### 方法关键点
- 双嵌入骨干网络：拆分召回、排序分支，通过梯度隔离禁止CTR梯度更新召回侧参数，避免语义结构被侵蚀，新增InfoNCE辅助loss保证召回侧语义对齐
- 乘法门控聚合器：改写得分需同时满足选择置信度、商品相关性两个条件才会生效，直接消除通用词仅靠置信度拿高分的捷径
- 动态改写选择器：基于用户+原query生成请求级的改写权重、个性化缩放与偏置项，自适应调整不同请求的改写偏好与相关性校准逻辑
- 保留原query的残差直连路径作为兜底，避免改写质量差时检索效果雪崩

### 关键实验
在得物100K工业搜索会话离线测试，对比生产基线PDN：rewrite semantic similarity@10提升+18.2%，click recall@10提升+99.5%；线上A/B测试query-view CTR提升+0.259%，平均阅读深度提升+0.733%，2025年已全量部署得物社区搜索。

### 核心结论
端到端优化query改写与检索的核心是在不丢失原query语义约束的前提下，让改写决策直接受下游业务信号监督，而非单独优化改写的语言学合理性

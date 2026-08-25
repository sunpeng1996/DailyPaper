---
title: 'WARP: Wasserstein-Aligned RAG for Population Opinions'
title_zh: WARP：基于Wasserstein对齐的RAG实现群体观点真实表征
authors:
- Aman Singh Thakur
- Aditya Agrawal
- Alwarappan Nakkiran
- Alex Karlsson
affiliations:
- Amazon.com
arxiv_id: '2608.22859'
url: https://arxiv.org/abs/2608.22859
pdf_url: https://arxiv.org/pdf/2608.22859
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: RAG优化 · 群体观点分布校准
tags:
- RAG
- Wasserstein Distance
- Re-ranking
- Opinion Summarization
- Distribution Calibration
one_liner: 提出训练无关的后检索重排框架WARP，用Wasserstein距离校准召回观点分布贴合群体真实分布
practical_value: '- 做电商商品评价/社区类RAG问答时，可引入W1距离作为重排目标替代KL/JS散度，更贴合观点的序数属性，降低分布失真，真实呈现正负评价占比，减少用户预期偏差

  - 针对召回池少数观点缺失的问题，可复用赤字感知池扩展策略：仅当某观点占比低于阈值时触发定向重召回，无赤字时自动旁路，几乎无额外开销

  - 可直接复用部署决策矩阵：召回池实体匹配率≥85%用轻量W1 Minimizer（仅9ms延迟），稀疏池用W1-MMR兼顾相关性和分布校准，完全满足生产级SLA要求

  - 观点类生成任务评估可参考文中LLM评委设计：区分比例准确性和观点覆盖度两个维度，更贴合用户对观点类回答的真实需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG系统处理「大家对X怎么看」类观点query时，标准top-k余弦召回仅优先选择与query相似度高的内容，导致少数观点被淹没，生成的回答看似有真实来源，但完全无法反映真实群体观点分布；现有多样性重排（MMR、DPP）无明确目标分布，KL/JS校准又将观点视为无序列类别，强正面与强负面错配的成本与相邻类别错误一致，不符合观点的序数属性。

### 方法关键点
- 两阶段pipeline：第一阶段语义召回得到Top-N候选池；1.5阶段赤字感知池扩展，对比当前池与群体目标分布Ppop，针对占比不足的观点类别做定向重召回，无赤字时自动旁路零开销；第二阶段W1重排选择最终k个文档
- 三种重排变体适配不同场景：W1 Minimizer针对稠密实体池（实体匹配率≥85%），仅从实体匹配候选中贪心选择最小化W1距离的文档，延迟仅9ms；W1-MMR针对稀疏池，混合相关性和分布校准增益打分；WassRank OT做全局最优运输分配，无超参数适配未知场景
- 采用Wasserstein-1距离作为校准目标，天然支持观点的序数属性，强正负错配成本是相邻类别的6倍，计算仅需O(m)（m为观点分箱数，本文用7档情感强度），无需训练

### 关键结果
在3个评论数据集（亚马逊卖家论坛8K、Yelp酒店14K、OpinRank汽车13K，共156个query、26个实体）上对比Top-k、MMR、DPP、KL校准等基线：分布误差比Top-k最低降低43%（稀疏池）、最高降低88%（稠密池+池扩展），重排p99延迟低于330ms；k≤5时，5个LLM评委的盲测中，86%的对比场景下用户更偏好WARP生成的回答。

**最值得记住的一句话：** 观点类RAG的核心目标不是召回最相关的内容，而是召回能真实反映群体观点分布的内容，W1距离是比KL/JS、多样性指标更适配观点序数属性的校准目标。

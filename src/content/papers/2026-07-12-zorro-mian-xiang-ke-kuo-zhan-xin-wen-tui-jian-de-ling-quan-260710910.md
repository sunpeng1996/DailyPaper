---
title: 'ZoRRO: A Zero-Weight Personalized Recommender System for Scalable News Recommendation'
title_zh: ZoRRO：面向可扩展新闻推荐的零权重个性化推荐系统
authors:
- Johannes Kruse
- Ryotaro Shimizu
- Kasper Lindskow
- Jon Tofteskov
- Michael Riis Andersen
- Julian McAuley
- Jes Frellsen
affiliations:
- Technical University of Denmark
- ZOZO Research
- JP/Politikens Media Group
- University of California San Diego
arxiv_id: '2607.10910'
url: https://arxiv.org/abs/2607.10910
pdf_url: https://arxiv.org/pdf/2607.10910
published: '2026-07-12'
collected: '2026-07-14'
category: RecSys
direction: 新闻推荐 · 轻量化无训练推荐框架
tags:
- News Recommendation
- Scalable RecSys
- Cold Start
- Inference Efficiency
- Lightweight Model
one_liner: 提出零权重无训练的新闻推荐框架，性能匹配SOTA神经模型且推理速度超600倍
practical_value: '- 冷启动严重、内容更新快的场景（如资讯/短内容/电商新品推荐）可直接复用ZoRRO的结构：内容语义+类目相似度加权，再加候选物品的时间衰减权重，无需训练即可快速上线基线。

  - 推理性能优化可参考：预计算所有物品的语义/类目嵌入，在线仅做向量相似度计算+权重乘积，无需模型推理，轻松达到亚毫秒级延迟，适合大流量低延迟要求的场景。

  - 评估推荐系统不能只看离线AUC/MRR等排序指标，相同CTR的模型可能在内容分布、多样性、话题集中度上差异极大，需结合业务生态目标设计多维度评估体系。

  - 新闻/内容推荐场景优先选用领域内预训练的对比学习语义嵌入，比通用BERT/RoBERTa效果更好。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
新闻推荐场景内容更新极快、生命周期短，物品和用户冷启动问题突出，现有深度学习推荐模型训练维护成本高、推理延迟大，很多场景下简单方案反而落地性更强，亟需平衡效果、效率和落地成本的轻量化方案。

### 方法关键点
- 零权重无训练设计，得分由两部分乘积构成：候选物品的固有relevance（用发布时间的指数衰减函数建模，仅需调衰减系数λc）、候选和用户历史点击物品的关联relevance（语义嵌入余弦相似度+类目向量余弦相似度之和）
- 用户侧历史行为的固有权重可配置时间衰减λh，实验发现用户历史无需时间衰减效果最优
- 物品表示可灵活替换，支持One-hot类目、word2vec、对比学习嵌入、预训练语言模型嵌入等多种输入

### 关键实验
- 离线用EB-NeRD数据集（3700万impression、100万用户、12.5万文章），对比NRMS、LSTUR、NPA等SOTA新闻推荐基线，ZoRRO离线AUC达63.80，超最强基线NRMS的62.46，推理吞吐量达1954 req/s，比神经基线快600倍以上，单请求延迟仅0.5ms
- 线上A/B测试覆盖46万用户，ZoRRO CTR达4.19%，仅略低于NRMS的4.33%，远高于热门基线的2.96%

### 核心结论
离线排序指标的提升不一定直接对应线上CTR增长，相同CTR的推荐模型可能带来完全不同的内容分发生态，需重视离线线上指标的对齐和超越精度的多维度评估。

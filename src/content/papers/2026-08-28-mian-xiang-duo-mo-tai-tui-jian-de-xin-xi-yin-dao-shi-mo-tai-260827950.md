---
title: Information-Guided Selective Modality-Interest Alignment for Multimodal Recommendation
title_zh: 面向多模态推荐的信息引导式模态-兴趣选择性对齐框架
authors:
- Wenze Ma
- Chenyu Sun
- Yanmin Zhu
- Qiwen Gu
- Xuhao Zhao
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2608.27950'
url: https://arxiv.org/abs/2608.27950
pdf_url: https://arxiv.org/pdf/2608.27950
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 多模态推荐 · 模态-兴趣对齐
tags:
- Multimodal Recommendation
- Modality Alignment
- Information Theory
- Graph Learning
- Contrastive Learning
one_liner: 提出AMUR多模态推荐框架，以信息论为指导选择性对齐偏好相关模态信号并保留特有信息
practical_value: '- 电商图文丰富品类（服饰、数码等）可复用行为校准模态图的trick：用用户共点击item对修正纯模态相似度构建的item-item图，过滤模态相似但偏好不一致的边，降低噪声输入

  - 跨模态对齐可借鉴维度选择门设计：不对齐全量模态特征，仅选择和用户兴趣相关的共享子空间做对齐，避免抹除模态特有有效信息（如图像风格、文本优惠信息等）

  - 信息论特征分解思路可复用：将模态特征拆分为与用户兴趣高互信息的有效部分+高条件熵的残差噪声部分，分别设计增强/抑制目标，比启发式注意力可解释性更强、调优更有方向'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态推荐通常无差别引入所有模态信息，但用户决策往往只依赖部分模态信号，无关内容会引入噪声；传统跨模态对齐强制全特征空间一致，容易抹除模态特有的互补信息，且现有对齐策略多为隐式启发式，缺乏明确的偏好对齐选择目标。

### 方法关键点
- 基于信息论分解模态表示：将模态特征拆分为与用户兴趣互信息高的偏好相关部分、条件熵高的残差噪声部分，整体优化目标为最大化前者权重、抑制后者影响
- 第一阶段做选择性模态-兴趣精炼：先基于模态相似度构建item-item图，通过KL散度正则让图的边分布对齐用户共点击行为，过滤偏好不匹配的边；再通过兴趣感知对比学习，让交互item的模态表示与用户协同表示拉近，增强兴趣相关信息
- 第二阶段做选择性跨模态共享兴趣对齐：学习维度级软选择门，从各模态表示中筛选共享兴趣子空间，仅在该子空间内做一致性最大化和差异正则，保留模态特有信息
- 最终融合用户/物品协同表示与全量精炼后的模态表示，用BPR loss优化推荐任务

### 关键实验
在Baby、Sports、Clothing三个公开多模态推荐数据集上，对比17个SOTA基线（含图方法、对比学习、扩散模型、Transformer类等），Recall@20相对最优基线分别提升1.56%、3.96%、2.26%，NDCG@20分别提升2.24%、7.78%、3.65%；抗模态噪声能力显著优于基线，训练效率仅比最快基线MGCN高1.5min，性价比突出。

**最值得记住的一句话**：多模态信息不是越多越好，只有和用户兴趣对齐的部分才对推荐有价值，跨模态对齐应避免为了一致性损失模态特有互补信息

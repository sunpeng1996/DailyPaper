---
title: Adaptive Item-based Collaborative Structures via Noise Rescheduling in Diffusion
  for Generative Recommendation
title_zh: 面向生成式推荐的扩散模型自适应物品协同结构噪声重调度方法
authors:
- Jiaqi Wang
- Tianying Liu
- Heng Chang
- Jihong Guan
- Wengen Li
- Shuigeng Zhou
affiliations:
- Tongji University
- Huawei Technologies Co., Ltd.
- Fudan University
arxiv_id: '2608.23400'
url: https://arxiv.org/abs/2608.23400
pdf_url: https://arxiv.org/pdf/2608.23400
published: '2026-08-24'
collected: '2026-08-25'
category: GenRec
direction: 生成式推荐 · 离散扩散 Semantic ID
tags:
- Generative Recommendation
- Discrete Diffusion
- Semantic ID
- Collaborative Filtering
- Noise Scheduling
one_liner: 将物品协同信号融入语义ID构造与离散扩散自适应噪声重调度，显著提升生成式推荐性能
practical_value: '- 语义ID构造时可融合物品共现SVD特征与文本语义特征，无需复杂图模型就能引入协同先验，大幅降低生成式推荐的特征工程成本

  - 离散扩散训练可替换原有均匀噪声调度，基于token上下文可恢复性+行为级物品依赖动态分配去噪权重，在不增加推理开销的前提下提升召回/排序效果

  - 扩散生成阶段可加入SID有效性约束，实时过滤不符合已生成token的候选物品，避免生成无效ID，提升线上部署的稳定性

  - 短序列、中长尾物品场景下，基于协同信号优化的Semantic ID比纯语义ID表现更稳定，可直接复用该构造方法优化现有生成式推荐基线'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前离散扩散类生成式推荐方法存在两个核心缺陷：一是Semantic ID仅基于文本语义构造，缺失物品协同过滤先验；二是扩散训练采用统一噪声调度，忽略不同token的上下文依赖差异，无法有效建模物品间协同关系，导致推荐精度瓶颈。

### 方法关键点
- 物品共现引导的Semantic ID生成：先基于用户交互序列构造物品共现矩阵，经SVD分解得到协同嵌入，与文本语义嵌入融合后用RQ-KMeans量化为分层Semantic ID，同时保留语义相似度与物品共现模式
- 物品级自适应噪声重调度：去噪权重由两部分加权得到：静态局部可恢复性（基于intra-item/inter-item的几何距离衰减）、动态行为依赖（基于item级注意力的用户行为序列关联度），对上下文支撑充足的token分配更高去噪权重
- 推理阶段加入SID有效性约束，每步生成时仅保留与已生成token匹配的真实物品ID候选，避免生成无效序列

### 关键实验结果
在5个公开数据集（Amazon 3个子集、MovieLens、Steam）上对比16个SOTA基线，相比最优扩散基线LLaDA-Rec，Scientific数据集Recall@1提升24.5%，MovieLens数据集NDCG@5提升8%，Steam数据集Recall@10提升8.4%，在短序列、中长尾物品场景下均稳定优于基线。

最值得记住的结论：生成式推荐中离散扩散的性能瓶颈并非来自生成范式本身，而在于是否能将经典协同过滤信号有效融入语义ID构造与扩散训练的全流程。

---
title: Tackling the Modality Inhibitance Effect with Wavelet-based Modality Integration
  in Multi-modal Recommendation
title_zh: 基于小波模态整合解决多模态推荐的模态抑制效应问题
authors:
- Rongqing Kenneth Ong
- Andy W. H. Khong
affiliations:
- Nanyang Technological University
arxiv_id: '2610.16229'
url: https://arxiv.org/abs/2610.16229
pdf_url: https://arxiv.org/pdf/2610.16229
published: '2026-10-12'
collected: '2026-10-17'
category: RecSys
direction: 多模态推荐 · 模态融合消噪
tags:
- Multi-modal Recommendation
- Wavelet Decomposition
- Graph Learning
- Modality Fusion
- E-commerce Recommendation
one_liner: 提出MMWave多模态推荐框架，通过小波分解消噪+自适应融合缓解多模态加入后的性能下降
practical_value: '- 多模态特征处理可复用小波分解思路，仅保留低频核心特征过滤高冗余噪声，无需复杂MLP消噪，计算开销低还可避免特征压缩带来的信息损失

  - 模态融合阶段可借鉴交叉加权集成策略，用融合特征权重重加权单模态、单模态权重重加权融合特征，缓解多模态引入后的性能下跌问题

  - 多模态图构建阶段可复用预构造跨模态融合图的方案，训练前完成谱分解+特征融合，不增加训练时的计算与内存开销

  - 若业务场景需接入超过2种模态（如图文+视频+音频/3D模型），可直接复用MMWave完整架构解决模态抑制导致的性能下降问题'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有多模态推荐系统在从双模态扩展到三模态时普遍出现性能显著下降的模态抑制效应，核心原因是新增模态自带噪声、多模态特征冗余度高，传统注意力拼接/求和的融合方案无法有效过滤冗余、适配多模态场景，导致业务中接入更多模态特征反而拖累推荐效果，该问题在电商、短视频等多模态内容丰富的场景尤为突出。

### 方法关键点
- 小波模态混合器：对每个模态的原始特征做L层Haar小波分解，仅保留低频近似系数训练可学习权重过滤噪声，再通过逆小波变换重构无冗余的单模态特征，结合ID embedding做门控融合保留行为信号
- 结构感知多模态图学习：预构造每个模态的item相似度稀疏图，通过谱分解交换不同模态的特征值丰富图结构信息，平均池化得到跨模态融合图，训练前完成构造无额外开销，再用轻量图卷积编码高阶结构信息
- 自适应模态调节器：设计交叉加权策略，用融合特征的注意力权重重加权所有单模态特征、用所有单模态的注意力权重平均后重加权融合特征，结合ID embedding的行为门控做最终特征聚合，搭配InfoNCE对比损失提升特征区分度

### 关键实验
在Baby、Sports、Clothing三个亚马逊电商双模态数据集，以及TikTok三模态数据集上验证，对比BPR、LightGCN、MMGCN、FREEDOM、LGMRec等12个SOTA模型，平均Recall@K、NDCG@K提升6.48%；TikTok三模态场景下Recall@10达0.0827，比此前最优的BM3高出14.5%。

### 核心结论
多模态推荐性能下跌不一定是模态不平衡导致，更可能是多模态冗余带来的模态抑制效应，用小波分解提取核心特征+交叉加权融合可低成本解决该问题。

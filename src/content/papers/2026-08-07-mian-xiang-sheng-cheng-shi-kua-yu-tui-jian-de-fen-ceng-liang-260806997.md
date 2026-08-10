---
title: Hierarchical Quantization with Domain-Adaptive Sparse Routing for Generative
  Cross-Domain Recommendation
title_zh: 面向生成式跨域推荐的分层量化与领域自适应稀疏路由方法
authors:
- Haiying He
- Xiaopeng Li
- Yuchen Gu
- Kuo Cai
- Bo Chen
- Jingtong Gao
- Yejing Wang
- Derong Xu
- Ruiming Tang
- Guorui Zhou
affiliations:
- City University of Hong Kong
- Kuaishou Technology
arxiv_id: '2608.06997'
url: https://arxiv.org/abs/2608.06997
pdf_url: https://arxiv.org/pdf/2608.06997
published: '2026-08-07'
collected: '2026-08-10'
category: GenRec
direction: 生成式推荐 · 跨域知识迁移
tags:
- GenRec
- Cross-Domain Recommendation
- Semantic ID
- MoE
- Vector Quantization
one_liner: 提出HD-REC生成式跨域推荐框架，结合分层量化、稀疏MoE和路由一致性正则实现跨域知识迁移
practical_value: '- Semantic ID构造可复用分层量化设计：前几层用全局共享码本建模通用粗粒度语义，最后一层用动态路由的领域专属码本建模细粒度领域差异，适配跨域场景下的异构物品语义，无需显式域对齐

  - 跨域GenRec骨干网络可借鉴DAS MoE架构：固定1个全局共享专家处理通用特征，每个token仅额外激活1个稀疏路由的专属专家，仅增加<3%推理开销即可大幅提升跨域适配能力

  - 可复用跨粒度路由一致性正则：对同个item的多个语义token的MoE路由分布加KL散度约束，正则权重λ设为0.01时效果最优，能降低6x路由方差同时稳定提升推荐效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式推荐（GenRec）扩展到跨域场景时，统一模型难以同时适配不同领域的异构物品语义和用户行为模式：现有方法要么依赖全局共享表征，对域间异质性建模能力不足；要么需要显式实体重叠或大量辅助数据做域对齐，无法高效实现跨域知识迁移，数据稀疏域的推荐效果提升有限。

### 方法关键点
- 分层域感知量化器（HDQ）：前L-1层用全局共享码本提取物品粗粒度通用语义，最后一层用Gumbel-Softmax路由动态选择专属码本做残差量化，兼顾跨域语义对齐和领域特有特征建模
- 域自适应稀疏MoE（DAS MoE）：每个token固定走1个全局共享FFN专家，同时动态选择1个专属专家，稀疏激活控制计算量，实现模型容量的按需分配
- 跨粒度路由一致性损失（CRCL）：约束同个item的多个语义token的MoE路由分布与item全局平均分布的KL散度，降低intra-item路由波动，提升表征稳定性

### 关键实验结果
在3组公开跨域基准（Amazon服饰-运动、Amazon电子-手机、豆瓣图书-电影）上对比12个SOTA基线，对比最强基线GenCDR：H@10最高提升17.6%（运动域）、16.3%（电子域）、9.9%（手机域）；推理开销仅增加2%-2.5%，路由一致性提升6倍。

### 核心结论
跨域生成式推荐的核心是在语义层面做好「通用-专属」容量的分层解耦，而非单纯增加全局模型容量。

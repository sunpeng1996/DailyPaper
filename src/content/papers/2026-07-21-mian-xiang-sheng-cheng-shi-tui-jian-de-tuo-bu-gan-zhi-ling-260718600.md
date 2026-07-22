---
title: Topology-Aware Tokenization for Generative Recommendation
title_zh: 面向生成式推荐的拓扑感知令牌化方法
authors:
- Yaokun Liu
- Yifan Liu
- Zhenrui Yue
- Gyuseok Lee
- Zelin Li
- Ruichen Yao
- Dong Wang
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.18600'
url: https://arxiv.org/abs/2607.18600
pdf_url: https://arxiv.org/pdf/2607.18600
published: '2026-07-21'
collected: '2026-07-22'
category: GenRec
direction: 生成式推荐 · 语义ID令牌化
tags:
- Generative Recommendation
- Semantic ID
- RQ-VAE
- Tokenization
- Topology Preservation
one_liner: 提出分层拓扑蒸馏的TopoTok令牌化框架，解决生成式推荐语义ID量化的拓扑失真问题，Recall@5最高提升9.42%
practical_value: '- 做Semantic ID生成时，可直接复用TopoTok的三层蒸馏逻辑，在RQ-VAE训练阶段额外增加拓扑损失，无推理开销，适合线上业务落地

  - 分层蒸馏的粒度可根据RQ-VAE的codebook利用率动态调整：低利用率层用组间蒸馏、中层用组内蒸馏、高利用率层用item级蒸馏，适配不同深度的量化结构

  - 拓扑损失的权重α建议先在0.1~0.3区间调优，平衡拓扑保留和语义重建效果，避免过强正则导致性能下降'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐将序列推荐转化为自回归生成任务，依赖Semantic ID把连续item嵌入量化为离散令牌，但现有RQ-VAE量化过程存在严重拓扑失真：连续空间中item的邻接关系在量化后被破坏，三层RQ-VAE的Top-20邻域重合度从第一层的63%降到第三层的27%，误导模型对item相似度的判断，成为生成式推荐的性能瓶颈。

### 方法关键点
- 提出拓扑蒸馏框架：将拓扑保留转化为相似度排序对齐任务，最小化教师（连续嵌入空间）和学生（量化令牌空间）的相似度分布KL散度，避免直接对齐距离的不适配问题
- 设计三层分层蒸馏策略，对齐RQ-VAE的粗到细语义层次：①组间蒸馏（第一层）：对齐粗粒度语义簇的全局邻接关系；②组内蒸馏（第二层）：对齐同一语义簇内的item局部邻接关系；③item间蒸馏（第三层及更深）：对齐全局item级的细粒度邻接关系
- 训练时在原有RQ-VAE的重建+承诺损失基础上叠加拓扑损失，推理阶段无额外开销

### 关键实验
在Amazon的Industrial Scientific、Musical Instruments、Video Games三个5-core数据集上验证，对比TIGER、ETEGRec、LETTER、CoST等SOTA生成式推荐基线，TopoTok在TIGER backbone上最高提升Recall@5达9.42%，在端到端ETEGRec backbone上最高提升Recall@5达4.42%，同时三层量化的Top-20邻域重合度最高提升9.2pct。

**最值得记住的一句话**：生成式推荐的Semantic ID质量核心不仅是语义重建精度，更要保留item之间的拓扑邻接关系，分层拓扑蒸馏是低成本提升令牌化质量的有效方案

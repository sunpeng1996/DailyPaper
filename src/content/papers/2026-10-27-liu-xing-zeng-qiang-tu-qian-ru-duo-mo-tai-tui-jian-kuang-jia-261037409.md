---
title: Can Complementary Signals Bridge Similarity Islands? Manifold-Augmented Graph
  Embedding for Multimodal Recommendation
title_zh: 流形增强图嵌入多模态推荐框架MAGE：桥接互补信号打破相似性孤岛
authors:
- Zhenye Yang
- Jinpeng Chen
- Wenbo Fu
- Jun Ma
- Huan Li
- Qimin Zhou
- Tao Wang
- Li Sun
- Senzhang Wang
affiliations:
- Beijing University of Posts and Telecommunications
- Zhejiang University
- Central South University
arxiv_id: '2610.37409'
url: https://arxiv.org/abs/2610.37409
pdf_url: https://arxiv.org/pdf/2610.37409
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 多模态推荐 · 互补品建模
tags:
- Multimodal Recommendation
- GNN
- Complementary Recommendation
- Manifold Learning
- Heterophily
one_liner: 提出MAGE框架拆分互补信号建模为离线流形增强与在线非对称传播，缓解多模态推荐相似性孤岛问题
practical_value: '- 离线流形增强模块可作为通用插件直接替换现有多模态推荐系统的文本特征输入，无需修改模型架构即可在3C、服饰等互补需求高的品类获得稳定增益

  - 商品文本预处理可复用LLM证据约束提取方案，离线一次性过滤营销话术、保留功能属性，无需线上调用LLM即可提升特征有效性

  - 可复用非对称双模态设计思路：将视觉特征作为商品身份稳定锚点，增强后的文本特征作为互补信号探针，平衡语义一致性与探索性

  - 异构图构建时给互补边设置低于相似边的权重，配合局部gap约束控制注入强度，避免语义漂移风险'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态推荐基于同质性假设的图传播偏向推荐语义相似的替代品，而电商场景下用户大量购买功能互补的异质商品（如手机和充电器），这类互补品在原始多模态特征空间中语义距离远，形成「相似性孤岛」，直接在异质边上做传播会导致语义漂移，互补品推荐效果差。

### 方法关键点
- 离线预处理：通过LLM离线提取商品文本的功能性属性，过滤营销噪声，生成高质量文本embedding
- 离线流形增强：用Soft Conceptor从共购邻域提取互补感知残差方向，通过局部gap约束自适应控制残差注入强度，避免破坏原有语义结构
- 在线非对称传播：视觉特征基于纯相似性图传播作为身份稳定锚点，增强后的文本特征基于融合共购边的混合图传播作为互补信号探针
- 自校准融合：通过门控机制自适应融合双模态特征与协同ID特征，平衡身份保留与互补探索

### 关键实验
在4个Amazon公开数据集（Baby、Sports、Clothing、Electronics）上对比LightGCN、GUME、MENTOR等10个强基线，Recall@20相对最优基线分别提升2.77%、4.81%、6.25%、6.53%；针对低语义相似度共购商品的硬互补子集，相对最优基线平均提升9.87%；离线增强模块可直接迁移到GUME、MGCN等现有模型，无需改动架构即可获得1%-3%的稳定增益。

### 核心启示
多模态推荐中互补信号的建模不能只靠加异质边，先做特征空间的几何校正再做拓扑传播，能以极低的额外成本大幅提升互补品推荐效果

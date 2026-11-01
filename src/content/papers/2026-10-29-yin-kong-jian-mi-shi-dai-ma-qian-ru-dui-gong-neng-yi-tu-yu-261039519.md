---
title: 'Lost in the Latent Space: How Code Embeddings Represent Functional Intent
  and Implementation Fidelity'
title_zh: 隐空间迷失：代码嵌入对功能意图与实现保真度的表征研究
authors:
- Lu Sun
- Yuheng Huang
- Lei Ma
- Zhijie Wang
affiliations:
- The University of Tokyo
- University of Alberta
- Concordia University
arxiv_id: '2610.39519'
url: https://arxiv.org/abs/2610.39519
pdf_url: https://arxiv.org/pdf/2610.39519
published: '2026-10-29'
collected: '2026-11-01'
category: Other
direction: 代码嵌入表征能力实证分析
tags:
- Code Embedding
- Representation Learning
- Empirical Study
- Functional Intent
- Implementation Fidelity
one_liner: 针对14个SOTA代码嵌入模型开展实证分析，揭示其表征存在的抽象-保真权衡规律
practical_value: '- 嵌入模型存在固有抽象-保真权衡，召回/粗排用的语义嵌入优先选泛化性高的，精细化内容匹配/审核场景优先选细节保留能力强的，无需追求单一通用嵌入

  - 评估嵌入模型不要只看公开检索榜单指标，需补充场景内语义不变扰动测试（如同款商品的不同标题/描述变体），验证嵌入对语义等价内容的对齐能力

  - 检索性能相近的嵌入模型对特征扰动的响应差异大，业务上线前要针对自身场景的常见语义变换做针对性验证，不要直接复用开源评测结论'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有代码嵌入模型的评估多聚焦下游任务性能，无法解释单一嵌入能否同时支撑功能抽象与实现敏感分析两类需求，内部表征规律尚不清晰。
### 方法关键点
针对14个SOTA代码嵌入模型开展三类互补分析：有监督探测验证功能抽象与实现保真能力、零样本检索实验评估嵌入空间几何相似性、受控扰动实验测试嵌入对语义不变代码变换的响应特性。
### 关键结果
1. 嵌入存在稳定的抽象-保真权衡：结构/风格信号保留更好的模型语义泛化能力显著更差；
2. 检索性能相近的模型对同一实现变更的响应存在显著差异；
3. 目前不存在通用统一代码表征，需根据场景需求针对性选择、部署嵌入模型。

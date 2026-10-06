---
title: 'RepICL: Reusable In-Context Prediction Across Heterogeneous Representation
  Spaces'
title_zh: RepICL：跨异构表示空间的可复用上下文预测方法
authors:
- Yu-Hsiang Liu
- Kuan-Yu Chen
- Chih-Sheng Chen
- Meng-Hsuan Chang
- Yu-Chen Den
- Tien-Hao Chang
affiliations:
- SinoPac Holdings, Taipei, Taiwan
arxiv_id: '2610.05852'
url: https://arxiv.org/abs/2610.05852
pdf_url: https://arxiv.org/pdf/2610.05852
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 跨模态少样本 · 可复用预测
tags:
- In-Context Learning
- Few-Shot Learning
- Meta Learning
- Representation Alignment
- Cross-Modality
one_liner: 提出带 episodic whitening 的元训练上下文学习器，跨异构表示空间少样本预测超逐episode逻辑回归
practical_value: '- 电商冷启动少样本分类场景可直接复用 episodic whitening 预处理逻辑，无需为每个新类目/新编码器单独适配分类头，大幅降低冷启动适配成本

  - 跨模态（文本/图像/商品视频/音频）统一召回排序任务中，可借鉴这套异构表示空间归一化思路，避免为每个模态的特征单独设计适配层

  - 多编码器融合的推荐场景中，可复用RepICL的元训练预测逻辑，统一处理不同预训练模型输出的异构特征，提升特征复用效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前预训练编码器的表示复用已经成为机器学习主流范式，但每个新任务、新编码器都需要单独拟合下游分类头，现有上下文学习器在跨异构表示空间（不同维度、协方差、几何结构）的少样本任务上性能普遍弱于逐episode拟合的Logistic Regression，缺乏能跨数据集、编码器、模态通用的可复用预测流程。

### 方法关键点
- 构建RepShiftBench基准，覆盖1218个编码器-数据集任务，跨文本/图像/音频三模态，支持 unseen 数据集、编码器、联合、模态四类泛化能力评估
- 核心设计episodic whitening：逐episode做PCA+坐标标准化，将异构表示映射到统一规范空间，无需编码器特定的对齐逻辑
- 提供两个变种：RepICL-I（归纳式，仅用标注支持集做白化和预测）、RepICL-T（直推式，加入未标注查询集做白化和全episode注意力）
- 元训练阶段使用跨任务的5-way 5-shot episode训练，损失采用查询集交叉熵

### 关键结果
- RepICL-I在12个基准评估设定上全部超过逐episode Logistic Regression，平均提升0.3~1.26个百分点；RepICL-T在所有12个设定上超过现有直推式方法，平均提升2.65~6.66个百分点
- 跨模态迁移验证：仅用文本+音频训练的模型在CLIP视觉特征的11个少样本任务上，对比基线TAIL从90.47%提升到92.31%
- 消融实验证明episodic whitening是性能提升核心，且其不是通用预处理步骤，只有和元训练结合才能生效

最值得记住的一句话：可复用的少样本预测流程可以像预训练表示一样跨异构表示空间泛化，无需针对每个任务/编码器单独拟合分类头

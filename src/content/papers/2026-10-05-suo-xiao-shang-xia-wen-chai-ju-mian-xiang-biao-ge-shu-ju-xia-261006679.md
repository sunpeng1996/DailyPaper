---
title: 'Closing the Context Gap: Activation Alignment for Tabular In-Context Learning'
title_zh: 缩小上下文差距：面向表格数据上下文学习的激活对齐方法
authors:
- Yoel Zeldes
affiliations:
- Independent Researcher
arxiv_id: '2610.06679'
url: https://arxiv.org/abs/2610.06679
pdf_url: https://arxiv.org/pdf/2610.06679
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 表格大模型 · 上下文学习效率优化
tags:
- In-Context Learning
- Activation Alignment
- Tabular Foundation Model
- Knowledge Distillation
- Efficient Inference
one_liner: 通过轻量无GPU的激活对齐方法，缩小小上下文与全上下文表格ICL模型的性能差距
practical_value: '- 电商用户/商品特征这类表格数据的ICL推理场景，可直接套用激活对齐范式，以全上下文大模型为teacher、小上下文模型为student，加轻量线性层对齐中间激活，在不提升推理成本的前提下补性能缺口

  - 对齐层仅需合成无标签数据训练，无需GPU，可在业务端CPU环境快速迭代上线，适配推荐系统小流量快速实验的需求

  - 低数据量的冷启动推荐场景（如新类目、新用户），可通过该方法恢复近50%的全上下文模型性能增益，平衡冷启动速度与推荐效果'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
表格基础模型的ICL推理需在每次前向传播处理全部上下文样本，推理成本随上下文长度飙升；若裁剪上下文压缩成本，会带来显著性能损失，此前无低开销的折中方案。

### 方法关键点
提出激活对齐方法：以全上下文模型为teacher、裁剪上下文的小模型为student，用合成无标签数据训练轻量线性变换层，将student的中间激活映射到teacher的激活分布；对齐层训练无需GPU，在普通CPU上仅需数秒到数分钟即可收敛。

### 关键结果
在TabArena基准的38个分类数据集上测试TabPFN-3、TabFM两个主流表格基础模型，所有上下文长度预算下，对齐后student模型相对基线均有统计显著的性能提升；低数据场景下可恢复近50%的teacher模型性能优势，同时保持小上下文的推理速度。

---
title: 'Interior interpretability with attention rollout: contraction and propagation
  profiles in Transformers'
title_zh: 基于注意力展开的内部可解释性：Transformer中的收缩与传播剖面
authors:
- Umberto Biccari
- Qian Huang
- Enrique Zuazua
arxiv_id: '2607.22367'
url: https://arxiv.org/abs/2607.22367
pdf_url: https://arxiv.org/pdf/2607.22367
published: '2026-07-24'
collected: '2026-07-27'
category: LLM
direction: Transformer可解释性 · 注意力机制分析
tags:
- Interpretability
- Attention Rollout
- Transformer
- Feature Attribution
- Doeblin-Dobrushin Theory
one_liner: 提出内部可解释性框架，用量化收缩理论解析Transformer注意力传播的结构特性
practical_value: '- 可基于注意力展开方法分析推荐/广告场景下Tabular Transformer的特征交互传播路径，定位核心影响特征

  - 用Dobrushin系数量化注意力传播的收敛性，可诊断排序/召回Transformer模型的层数冗余度，优化模型深度

  - 注意力传播剖面差异可用来校验微调后LLM/推荐模型是否学到符合业务逻辑的特征交互模式，避免过拟合虚假关联'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有特征归因方法（如SHAP、梯度类方法）仅能建立输入变量与模型输出的贡献关联，无法刻画Transformer中间层特征交互算子的组合传播逻辑，缺少对模型内部组织规律的量化分析框架。
### 方法关键点
1. 提出「内部可解释性」传播分析视角，将注意力展开建模为行随机算子，编码特征Token间的注意力介导传播关系；
2. 引入Doeblin-Dobrushin收缩理论，证明Dobrushin系数小的展开算子近似于秩一随机矩阵，其行向量由归一化列和决定，可结构化解释传播剖面。
### 关键结果
- 代谢组年龄预测任务的Transformer中，注意力展开收缩强度随模型深度提升；
- 训练后与随机初始化的模型传播剖面存在显著差异；
- 与PCA、SHAP梯度近似方法相比，仅在高排名特征上局部一致，全排序一致性弱，注意力展开仅适用于传播诊断，不可作为完整因果归因依据。

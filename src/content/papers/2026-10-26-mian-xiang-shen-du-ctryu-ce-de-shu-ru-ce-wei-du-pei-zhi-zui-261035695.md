---
title: Towards a Unified Framework of Optimal Input-Side Dimensional Configuration
  for Deep CTR Prediction
title_zh: 面向深度CTR预测的输入侧维度配置最优统一框架
authors:
- Chaohua Yang
- Fuyuan Lyu
- Xing Tang
- Dugang Liu
- Xiuqiang He
- Zhong Ming
affiliations:
- Shenzhen University
- McGill University
- Shenzhen Technology University
arxiv_id: '2610.35695'
url: https://arxiv.org/abs/2610.35695
pdf_url: https://arxiv.org/pdf/2610.35695
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: CTR预测 · 输入侧信息优化
tags:
- CTR-Prediction
- Feature-Selection
- Sample-Selection
- Embedding-Pruning
- Optimal-Transport
one_liner: 提出OptIDC框架联合优化三级输入选择，用最优运输消解跨层级冲突提升CTR效果
practical_value: '- 可直接复用三级选择联动思路，无需分别独立优化样本去噪、特征选择、嵌入剪枝模块，避免单级优化的决策冲突，降低多模块调参成本

  - 最优运输跨层级协调的trick可直接迁移，采用余弦距离作为运输成本，无需硬对齐不同粒度的掩码，实现成本低、涨点稳定

  - 搜索+重训的两阶段流程对线上服务友好，搜索阶段得到的硬掩码可固化到特征预处理流程，推理侧无额外开销，适配大流量生产环境

  - 实测单级输入选择一般可带来1‰左右的AUC提升，三级联合+OT协调可额外带来1-2‰的AUC增益，在电商CTR场景可转化为明确的营收提升'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有CTR模型的输入侧优化大多独立在样本、特征、嵌入单元单层级进行，忽略了三者的天然依赖关系：被过滤的特征对应的嵌入剪枝决策完全无效，高权重样本如果大部分特征被抑制也无法贡献有效梯度，导致优化冲突，无法发挥输入侧优化的最大收益。

### 方法关键点
- 提出OptIDC统一框架，同时学习样本权重、特征门控、嵌入单元掩码三类选择器，三者共享选择权重的掩码本质，分别作用在输入张量的不同轴上
- 引入选择加权的Optimal Transport机制，分别对样本-特征、特征-嵌入单元、样本-嵌入单元三类粗到细关系建模，用余弦相似度作为运输成本，对齐不同粒度的选择决策，缓解跨层级冲突
- 采用搜索+重训两阶段流程：搜索阶段用退火的可微门控联合优化选择器和CTR损失，得到硬掩码后重训backbone，推理侧只保留固化的特征、嵌入掩码，无额外开销

### 关键实验
在Avazu、Criteo、MovieLens、AliCCP四个公开数据集，搭配DNN、DeepFM、DCN、AutoInt、FinalMLP五种主流CTR backbone，对比OptFS、OptEmbed、AutoDenoise等10余种单级/两级选择基线：单级选择平均AUC提升约1‰，无协调的三级联合选择提升约2‰，加入OT协调的OptIDC在所有配置下稳定领先，比最优基线最高AUC提升1.6‰（Avazu+FinalMLP配置下从0.7925到0.7941），推理开销仅比纯backbone高20%左右。

### 核心结论
CTR输入侧优化不是单级模块的简单堆叠，跨层级协同带来的增益远高于独立优化各模块的收益之和

---
title: 'MoR4Rec: Mixture-of-Recursion for Sequential Recommendation'
title_zh: MoR4Rec：面向序列推荐的混合递归自适应计算框架
authors:
- Tiwari Ankit Satyaprakash
- Adamya Shyam
- Vikas Kumar
- Bharti Rana
- Venkateswara Rao Kagita
affiliations:
- University of Delhi, India
- K.R. Mangalam University, India
- National Institute of Technology Warangal, India
arxiv_id: '2611.29462'
url: https://arxiv.org/abs/2611.29462
pdf_url: https://arxiv.org/pdf/2611.29462
published: '2026-11-22'
collected: '2026-11-24'
category: RecSys
direction: 序列推荐 · 自适应计算效率优化
tags:
- Sequential Recommendation
- Mixture-of-Recursion
- Adaptive Computation
- KV Sharing
- Gated Attention
one_liner: 将混合递归范式引入序列推荐，实现交互级自适应计算深度，兼顾效果与效率
practical_value: '- 可复用混合递归+KV共享的设计改造现有Transformer基序列推荐模型：给每个交互项动态分配计算深度，浅处理高频重复行为、深处理偏好偏移类交互，在不增加参数量的前提下提升效果

  - 参考负载均衡正则的实现解决动态路由的坍缩问题：无需直通估计器，仅通过平均路由概率与实际分配比例的乘积项做正则，保证不同深度的计算资源被均匀利用

  - 可根据业务数据稀疏度选择门控策略：数据稠密的场景（如电商高活用户）用elementwise门控提升细粒度特征调制能力，稀疏长尾场景用vanilla注意力避免过拟合

  - 工程侧可参考级联token选择+增量KV更新的逻辑优化推理效率：随着递归深度增加仅处理活跃token，KV缓存仅更新活跃项的状态，降低推理时的计算开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Transformer基序列推荐采用固定计算深度处理所有用户交互，而用户行为天然异构：大部分重复习惯性交互仅需浅层次建模，少量反映偏好偏移、长程依赖的交互才需要深度上下文处理，固定深度会导致模型容量利用效率低、算力浪费，同时带来不必要的推理开销。

### 方法关键点
- 三层Transformer架构：独立输入层做初始上下文编码、共享递归中间块（参数全局复用，参数量不随递归次数上升）、独立输出层做预测前表征精炼
- 轻量线性路由层为每个交互项动态分配递归深度，配合级联token选择机制：仅递归深度≥当前层级的token参与计算，退出时将表征与初始表征做残差融合
- 跨递归步KV共享策略：仅增量更新活跃token的KV状态，非活跃token复用历史缓存，大幅减少冗余计算
- 可选头/元素级门控注意力自适应抑制噪声上下文，加入负载均衡正则避免路由坍缩，保证训练稳定性

### 关键实验
在MovieLens 1M、亚马逊Video Games、Industrial & Scientific三个公开数据集上，对比BERT4Rec、LRURec、SIGMA等10个SOTA基线，平均较最优基线提升Recall@5 2.28%、NDCG@5 2.50%、MRR@5 2.0%；相比同深度 vanilla Transformer，MFLOPs降低约3%，参数量降低约10%，推理速度最大提升25%。

### 核心结论
用户交互的复杂度天然异构，给不同交互分配差异化计算资源，是比盲目堆叠模型深度更高效的序列推荐优化路径。

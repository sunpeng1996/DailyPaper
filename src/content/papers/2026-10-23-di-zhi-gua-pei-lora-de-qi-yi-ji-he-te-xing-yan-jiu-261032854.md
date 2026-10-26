---
title: Singular Geometry of Low-Rank Adaptation
title_zh: 低秩适配(LoRA)的奇异几何特性研究
authors:
- Kamillo Ferry
- Anthea Monod
- Keisuke Yano
affiliations:
- Imperial College London, UK
- Institute of Statistical Mathematics, Japan
arxiv_id: '2610.32854'
url: https://arxiv.org/abs/2610.32854
pdf_url: https://arxiv.org/pdf/2610.32854
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: 参数高效微调理论 · LoRA复杂度分析
tags:
- LoRA
- Parameter-Efficient Fine-Tuning
- Singular Learning
- RLCT
- Transformer
one_liner: 基于奇异学习理论RLCT量化LoRA学习复杂度，揭示其层依赖的奇异几何特性
practical_value: '- 选择LoRA适配层时可优先筛选前向后向协方差在目标低秩方向非退化的层，降低不可辨识参数带来的训练波动

  - 调优LoRA秩r超参时可结合对应层的前向后向协方差性质，无需盲目提升秩值浪费参数预算

  - 曲率校正的多温度RLCT估计器可用于评估不同LoRA配置的实际学习效率，缩小超参搜索范围'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
LoRA作为当前主流的参数高效微调方法，其低秩分解天生存在参数不可辨识性，属于奇异统计模型，仅用参数维度无法准确描述其学习复杂度，现有理论缺乏对该复杂度影响机制的明确解释。
### 方法关键点
引入奇异学习理论中的真实对数典范阈值（RLCT）量化LoRA的学习复杂度，对预训练模型做局部线性化推导得到前向后向协方差（由适配层输入激活、反向传播灵敏度构造），以此判断低秩扰动的统计可观测性；分别从局部可观测切向/残差奇异、全局行列式簇仿射截面两个维度刻画LoRA的奇异几何，同时提出曲率校正的多温度RLCT估计器适配有限样本场景。
### 关键结果
MLP、Transformer架构实验验证LoRA的前向后向几何存在强层依赖，全局协方差退化不代表适配相关的低秩方向同样退化，全局学习复杂度可能由非真值参数所在秩层的奇异点主导。

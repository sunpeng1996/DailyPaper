---
title: Optimal Allocation of Embedding Dimensions under Finite-Sample Constraints
title_zh: 有限样本约束下的嵌入维度最优分配方法
authors:
- Vasileios E. Papageorgiou
affiliations:
- National and Kapodistrian University of Athens
arxiv_id: '2608.24592'
url: https://arxiv.org/abs/2608.24592
pdf_url: https://arxiv.org/pdf/2608.24592
published: '2026-08-25'
collected: '2026-08-27'
category: Training
direction: 嵌入优化 · 有限样本维度分配
tags:
- Embedding
- Dimension Allocation
- Finite Sample
- Constrained Optimization
- Tabular Learning
one_liner: 将嵌入维度选择建模为约束分配问题，给出闭式分配规则，提升有限样本下的预算使用效率
practical_value: '- 电商/推荐场景下的多分类特征（用户ID、商品ID、类目、场景等）嵌入维度分配可直接复用该闭式规则，维度与「特征近似价值/类别数」的平方根成正比，避免统一设维度或仅按类别数设维度的容量浪费

  - 可基于各分类特征pilot预训练嵌入的奇异值尾计算近似价值参数$a_j$，仅需少量预训练即可得到最优维度分配方案，无需暴力网格搜索调参，大幅节省算力成本

  - 总嵌入预算$B$可通过验证集小范围搜索确定，在样本量有限、特征异构性强的场景（如冷启动业务、垂类小流量业务）下优化收益最为明显'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
嵌入维度的传统选择多依赖启发式调参（如统一固定值、按类别数开根号），直接影响模型复杂度、拟合能力与有限样本泛化性，尤其在总参数预算受限、特征异构性强的场景下，易造成容量浪费或过拟合，缺乏理论层面的分配准则。
### 方法关键点
- 将多分类特征的嵌入维度选择建模为固定全局预算下的约束优化问题，明确拆解近似误差（维度不足丢失潜在结构）与估计误差（维度过高提升过拟合风险）的权衡关系
- 近似误差通过嵌入矩阵的奇异值尾表征，估计误差与总嵌入参数量正相关，推导得到闭式分配规则：单特征分配维度$d_j \propto \sqrt{a_j/N_j}$，其中$a_j$为特征的近似价值（由预训练嵌入的奇异值衰减拟合得到），$N_j$为特征的类别数
- 工程实现流程：先通过pilot预训练得到各特征的嵌入矩阵奇异值，拟合$a_j$，代入规则得到维度分配方案，再通过验证集小范围搜索最优总预算$B$
### 关键结果数字
仿真实验中，低/中预算区间比均匀分配、基数启发式分配的MSE降低10%~25%，特征异构性越强收益越高；真实医疗预测任务上，比均匀分配MLP准确率高1.8pct、MCC高3.9pct、预期校准误差ECE低17pct，比基数启发式分配准确率高8pct。
> 最值得记住的一句话：嵌入维度分配不是经验调参，而是有限样本下的资源分配问题，样本越有限、特征异构性越强，原则化分配的收益越大。

---
title: Personalized Task Dependency Graphs for Mitigating Signal Erosion in Multi-Task
  Recommendation
title_zh: 用于缓解多任务推荐信号衰减的个性化任务依赖图方法
authors:
- Fuyuan Liu
- Tiandeng Wu
- Yaqun Fang
- Wei Zhou
- Zehao Zhou
- Wenping Chen
- Qishun Mei
- Jiaxin Zhou
- Heng Chang
- Yi Cao
affiliations:
- Huawei Technologies Co., Ltd.
arxiv_id: '2609.04862'
url: https://arxiv.org/abs/2609.04862
pdf_url: https://arxiv.org/pdf/2609.04862
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 多任务推荐 · 任务依赖建模
tags:
- MTL
- CVR-Prediction
- GCN
- Task-Dependency
- Recommender-Systems
one_liner: 提出个性化任务依赖图PTDG 缓解多任务推荐深层稀疏目标的信号衰减
practical_value: '- 多任务建模可复用低秩动态任务依赖矩阵+硬因果掩码的设计，既适配不同物品的转化路径差异，又保证因果顺序不逆，推理延迟增量极低

  - Adaptive Progressive Masking（APM）策略可直接迁移到现有多任务模型，按任务标签稀疏度动态调整参数共享比例，从结构层面缓解梯度冲突，无推理
  overhead

  - 多任务损失权重可采用EMA加权的动态缩放方案，统一各任务损失量级，大幅提升训练稳定性，无需人工调试静态权重

  - 工业部署时低秩维度q取任务数的1/3即可平衡效果和计算开销，适配广告、电商多转化目标CVR预估场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业多任务推荐普遍采用固定转化漏斗的统一依赖结构，忽略不同物品（如重度游戏、轻量化工具）的任务依赖强度差异，层级消息传递会导致深层稀疏转化目标的信号逐层衰减，现有优化方法多聚焦梯度重加权，未从结构层面解决问题，且复杂方案难以适配工业级低延迟要求。
### 方法关键点
- 个性化拓扑学习：通过低秩分解生成物品专属的任务依赖邻接矩阵，注入用户、场景特征作为偏置动态调整依赖强度，复杂度仅为O(T*q)远低于全邻接矩阵学习
- 因果约束消息传递：添加硬因果掩码保证行为顺序（如Click→Pay不可逆），基于GCN在动态依赖图上做消息传递，自适应建立跨任务捷径避免冗余路径的信号衰减
- 自适应渐进掩码（APM）：按任务标签正样本率动态设置参数掩码比例，稀疏任务保留更多专属参数从结构层面缓解梯度冲突，训练完成后掩码固定无推理开销
- 损失优化：采用EMA动态加权各任务损失，统一不同任务损失量级，无需人工调参即可稳定训练
### 关键实验
在KuaiRand1K（8.4M样本、6个任务）和华为13.2M样本的工业数据集上，对比MMoE、PLE、PMTRec等工业常用SOTA，稀疏深层转化任务AUC最高提升1.45%，整体平均AUC提升1.2%以上；线上A/B测试相对MMoE基线CVR提升1.2%，eCPM提升1.9%，端到端推理延迟仅增加8ms，完全符合服务SLA要求。
> 最值得记住：多任务推荐的任务依赖并非全局统一，按实例动态调整依赖强度+结构层面解耦参数共享，是提升深层稀疏转化目标效果的高性价比路径。

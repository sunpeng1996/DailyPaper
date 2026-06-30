---
title: 'MuonSSM: Orthogonalizing State Space Models for Sequence Modeling'
title_zh: MuonSSM：面向序列建模的正交化状态空间模型
authors:
- Thai-Khanh Nguyen
- Ngoc-Bich-Uyen Vo
- Thieu N. Vo
- Tan M. Nguyen
- Cuong Pham
affiliations:
- Dainam University
- Hanoi University of Science and Technology
- Posts and Telecommunications Institute of Technology
- University of Bath
- National University of Singapore
arxiv_id: '2606.30461'
url: https://arxiv.org/abs/2606.30461
pdf_url: https://arxiv.org/pdf/2606.30461
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: 序列建模 · SSM训练优化
tags:
- SSM
- Sequence Modeling
- Long Context
- Mamba
- Training Stability
one_liner: 为状态空间模型引入动量路径与轻量正交化变换，稳定训练且保留并行扫描效率，提升多模态长序列任务表现
practical_value: '- 可作为drop-in替换现有推荐系统中用于用户行为序列建模的Mamba等SSM骨干，无需修改整体架构即可提升长程行为记忆能力，尤其是训练窗口外的序列泛化性能，适配用户半年以上历史行为的召回场景

  - 单步Newton–Schulz归一化trick可直接复用，无需SVD即可实现低秩更新的谱约束，计算成本极低，可迁移到RAG记忆更新、用户兴趣状态迭代等场景，缓解记忆退化问题

  - 动量路径的设计思路可迁移到实时推荐的用户兴趣增量更新模块，通过引入时间惯性降低短期噪声行为对长期兴趣表示的干扰，提升推荐结果的稳定性

  - MuonSSM收敛速度比原生SSM快1.3倍，同等训练成本下可获得更优效果，适合大流量电商场景下的序列模型快速迭代，降低训练资源消耗'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有SSM（如Mamba）作为长序列建模的线性时间替代方案，存在一阶更新导致的谱各向异性、长程梯度衰减、记忆覆盖干扰问题，长序列下性能退化、训练不稳定；现有优化仅通过标量门控间接缓解，未从更新几何结构、梯度传播路径层面解决根因。
### 方法关键点
- 新增动量辅助状态矩阵Mt，累积多步更新方向，提供独立的梯度传播路径，缓解长程梯度消失
- 对低秩输入注入做单步Newton–Schulz归一化，无需SVD即可约束奇异值范围，保证更新的谱条件良好，同时保留秩结构
- 将耦合的双状态更新转化为块仿射递归，完全适配并行扫描，保持O(L)时间复杂度、O(logL)并行深度，仅增加常数级计算开销
### 关键结果
跨语言、视觉、时间序列3类模态验证，对比原生Mamba、LongHorn、Gated DeltaNet等主流SSM基线：
- 语言建模：170M参数预训练后，8K上下文针检索任务准确率平均提升7pct，训练收敛速度快1.3倍
- 视觉任务：作为MambaVision的替换模块，ImageNet分类Top-1最高提升0.38pct，分布偏移下的鲁棒性显著提升
- 时间序列动作识别：高噪声复杂数据集MMAct上F1最高提升2.67pct，状态条件数降低18倍，训练稳定性大幅提升
> 最值得记住：针对序列模型的优化，从记忆更新的几何结构入手加归一化和动量路径，收益远高于单纯扩增状态维度，且不破坏并行效率。

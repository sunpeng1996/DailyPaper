---
title: Intelligent Embedding Pruning for Large-Scale Recommendation Models
title_zh: 面向大规模推荐模型的智能嵌入剪枝方法
authors:
- Anish Khazane
- Alex Saad-Falcon
- Guanchu Wu
- Marcio Porto
- Jasper Shan
- Fei Yu
- Eugene Shulga
- Intaik Park
- Yongzhe Zhang
- Xiaoyu Deng
affiliations:
- Meta
arxiv_id: '2611.25288'
url: https://arxiv.org/abs/2611.25288
pdf_url: https://arxiv.org/pdf/2611.25288
published: '2026-11-18'
collected: '2026-11-20'
category: RecSys
direction: 推荐系统 · 嵌入层压缩与训练优化
tags:
- Embedding Pruning
- Feature Importance
- DLRM
- Training Optimization
- Recommendation System
one_liner: 用特征重要性指导训练中嵌入表剪枝率分配，实现20-40%内存节省且精度不下降
practical_value: '- 可直接复用FI-ITEP逻辑，对大参数量CTR模型先用低开销permutation方法计算各嵌入表的特征重要性，给低重要性表分配更高剪枝率，避免原尺寸启发式剪枝的精度损失

  - 特征重要性（FI）计算仅占训练时长4-11%，且月级稳定性高（Top100特征Spearman相关性0.85+），可每1-2个月重计算一次，无需每轮训练都算进一步降低开销

  - TB级超大推荐模型可通过FI-ITEP压缩内存后减少训练GPU数量，文中112卡降到80卡后单卡吞吐量提升8%，单轮训练省108+GPU小时，频繁迭代的业务模型收益尤其显著

  - 小模型（<100GB嵌入）可先尝试原有尺寸启发式剪枝，FI-ITEP在小模型上收益较低，可根据GPU成本与剪枝收益阈值决定是否引入'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大规模推荐模型的内存瓶颈主要来自高基数categorical特征对应的稀疏嵌入层，现有训练中嵌入剪枝（ITEP）采用按表尺寸分配剪枝率的启发式规则，忽略特征对模型效果的实际贡献，容易出现剪枝后精度下降的问题，且内存压缩效率有优化空间。

### 方法关键点
- 采用两种扰动式特征重要性（FI）计算方法：permutation shuffle（打乱单特征batch内取值，观测loss变化量化重要性）、Shapley Value Sampling（近似计算特征边际贡献），实测shuffle方法稳定性更高、调参更简单，优先选用。
- FI-ITEP框架基于预计算的FI分数为每个嵌入表分配剪枝率，低FI表分配更高剪枝率，复用原有ITEP的ID映射、频率统计逻辑，仅需修改剪枝率配置即可嵌入现有训练管线，适配分布式多GPU训练。

### 关键实验
数据集覆盖Meta内部3个不同规模工业级DLRM（嵌入尺寸80GB~1.1TB）、开源Criteo 1TB数据集，对比baseline为按表尺寸分配剪枝率的percentile ITEP。核心结果：FI-ITEP实现20~40%总内存节省，相对baseline内存压缩效率提升8.3%~14.2%，精度损失降低32%~51.3%；1TB级模型训练GPU数量从112降到80，单卡吞吐量提升8%，单轮训练省108GPU小时，全生命周期省1000+GPU小时，FI计算仅带来4%~11%的训练时长overhead。

### 核心结论
对于TB级大规模推荐模型，用特征重要性指导嵌入剪枝的收益远高于计算成本，既能压缩内存降低GPU开销，还能通过正则效应提升模型精度。

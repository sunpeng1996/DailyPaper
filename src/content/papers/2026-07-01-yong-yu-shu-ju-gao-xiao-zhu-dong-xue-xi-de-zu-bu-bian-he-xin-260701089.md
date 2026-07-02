---
title: Group-invariant Coresets for Data-efficient Active Learning
title_zh: 用于数据高效主动学习的组不变核心集（GRINCO）框架
authors:
- L. C. Ayres
- J. C. M. Bermudez
- S. J. M. de Almeida
- R. A. Borsoi
arxiv_id: '2607.01089'
url: https://arxiv.org/abs/2607.01089
pdf_url: https://arxiv.org/pdf/2607.01089
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: 主动学习 · 数据高效训练 coreset 优化
tags:
- Active Learning
- Coreset
- Data Efficiency
- Invariance
- Sample Selection
one_liner: 提出组不变核心集框架GRINCO，在商空间选择样本消除变换冗余，提升主动学习标签效率
practical_value: '- 推荐/广告系统冷启动主动标注时，可将同item的不同视角/变换样本（如同一商品的不同主图、标题变体）归为同一个orbit，避免重复标注浪费预算

  - 构建训练样本coreset时，可引入商空间度量做k-center选择，优先覆盖不同语义/类目轨道，提升少样本下模型泛化性

  - 多模态商品表征训练时，可复用轨道平均损失做不变性训练，降低同item不同模态/视角带来的表征波动'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
主动学习通过筛选高信息密度样本标注降低成本，但传统coreset方法忽略数据固有变换对称性（如同一实例的旋转、缩放、语义变体），易重复标注同一样本的不同变换版本，浪费标注预算。
### 方法关键点
1. 提出GRINCO组不变coreset框架，在变换群诱导的商空间做样本采集，选择逻辑作用于轨道（同一样本所有变换实例的集合）而非原始样本；
2. 采用规范代表或学习到的轨道分离不变嵌入定义商空间度量，结合商空间k-center选择与轨道平均损失的不变训练策略；
3. 推导泛化界，明确超额轨道平均风险与商空间覆盖度、标签不确定性、轨道内变异的量化关联。
### 关键结果
在缩放不变合成数据、带旋转冗余的图像基准测试中，GRINCO相比传统coreset基线轨道覆盖度提升明显，标签效率更高，组诱导冗余度越高时性能增益越显著

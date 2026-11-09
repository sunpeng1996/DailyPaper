---
title: 'Orthogonal Norm Growth in Two-Tower Retrieval: A Popularity Mechanism for
  Unified Discovery'
title_zh: 双塔检索中正交范数增长：统一搜推的流行度产生机制
authors:
- Andrei Atamaniuk
affiliations:
- Wildberries
arxiv_id: '2611.09294'
url: https://arxiv.org/abs/2611.09294
pdf_url: https://arxiv.org/pdf/2611.09294
published: '2026-11-06'
collected: '2026-11-09'
category: RecSys
direction: 双塔召回 · 统一搜推流行度偏差机制
tags:
- Two-Tower Retrieval
- Embedding Norm
- Popularity Bias
- Unified Search & Recommendation
- Contrastive Loss
one_liner: 推导余弦损失下双塔item向量范数增长的充分条件，给出统一搜推共享表征审计方案
practical_value: '- 可直接复用论文4步审计方法检测业务双塔范数问题：先测step后item向量更新的切向性，再分搜索/推荐流统计更新次数与累积切向能量，最后对比raw
  dot与归一化cos的排序差诊断范数影响

  - 若业务采用共享item encoder的统一搜推双塔，且item侧为lookup embedding+row-wise优化器（如Exact RowWise
  Adagrad），需注意搜推更新会累积推高热门item范数，raw dot召回会放大热门曝光

  - 测试时直接归一化item向量可快速消除范数带来的流行度放大，但要注意该操作可能带来17%~22%的召回效用损失，需结合业务目标权衡

  - 若要缓解范数带来的流行度偏差，不建议直接移除ID embedding的范数增长，优先调整负采样策略或在训练目标中加入范数正则，避免直接干预导致效用下降'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
统一搜索推荐系统通常共享item encoder提升工程效率，但搜索、推荐两个任务的训练更新会共同改变item向量表征，当召回层使用未归一化点积计算相似度时，item向量范数的变化会直接干预排序结果。现有研究普遍默认余弦损失的输出梯度正交就会带来范数增长，但忽略了编码器参数更新到输出位移的映射误差，也未明确跨任务更新的范数累积效应，需要明确范数增长的边界条件和业务影响机制。
### 方法关键点
- 推导item向量切向更新的严格充分条件：item编码器为参数线性、lookup等价，损失仅依赖余弦相似度，item参数块采用正标量乘梯度更新（无动量、额外正则）
- 提出跨任务范数累积的路径计算方法，搜索、推荐流的切向更新能量可叠加到同一item的平方范数上
- 设计对照实验拆分ID embedding更新、共享内容编码器更新对范数的贡献，通过ID更新回退实验验证范数增长的因果影响
### 关键实验
在MovieLens 32M、Amazon Books数据集测试：
1. 满足充分条件的场景下，item更新频率与范数的皮尔逊相关系数达0.66/0.63，raw dot召回下top1%热门item占top100的比例比cos召回高0.43/0.54
2. 混合ID+内容编码器场景下，回退ID更新的范数增长可让频率-范数相关度下降0.266/0.256，同时raw dot的Recall@100下降17%~22%
### 核心结论
余弦梯度正交是输出层的性质，实际item表征的切向运动是参数更新的性质，直接归一化item向量可快速消除范数带来的流行度放大，但并非无成本的去偏方案

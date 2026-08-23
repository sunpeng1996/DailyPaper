---
title: Structured Affinity for Unsupervised Visual Class-Incremental Memory in Deep
  Artificial Immune Networks
title_zh: 基于结构化亲和度的深度人工免疫网络无监督视觉类增量记忆方法
authors:
- Siphesihle Sithungu
affiliations:
- University of Johannesburg
arxiv_id: '2608.20104'
url: https://arxiv.org/abs/2608.20104
pdf_url: https://arxiv.org/pdf/2608.20104
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 无监督类增量学习 · 人工免疫网络
tags:
- Artificial Immune Network
- Class-Incremental Learning
- Unsupervised Learning
- Gradient-Free Learning
- Visual Representation
one_liner: 提出结构化无梯度亲和度机制，实现无需重放的深度人工免疫网络视觉类增量记忆学习
practical_value: '- 做增量用户/物品表征体系迭代时，可借鉴无需旧样本重放的记忆保留思路，降低旧数据回流的存储与计算开销

  - 多模态商品特征匹配场景可参考结构化亲和度（ZNCC滤波）方案，替代传统扁平化向量相似度计算，保留特征空间结构信息

  - 分层表征的增量更新可复用层-wise自适应尺度校准trick，缓解不同层增量更新带来的特征分布偏移问题'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统视觉人工免疫网络（AIN）依赖扁平化向量亲和度计算，忽略空间结构，无法支持无需重放的类增量表征记忆学习。
### 方法关键点
1. 将视觉B细胞形式化为结构化模板，引入偏移模板亲和度、零归一化互相关（ZNCC）滤波、特征图绑定profile设计；
2. 免疫库同时作为记忆库和表征生成基，将绑定profile响应图输入下一层免疫层搭建深度结构；
3. 加入自适应层-wise尺度校准，支持隐空间自适应重组，同时保留旧类的可恢复结构。
### 关键结果
sklearn digits数据集上逻辑回归下游探针平衡准确率最高达0.978，初始类保留率0.978；Fashion-MNIST准确率达0.814，KMNIST达0.853，全程无需旧样本重放、标签驱动免疫更新或免疫层反向传播。

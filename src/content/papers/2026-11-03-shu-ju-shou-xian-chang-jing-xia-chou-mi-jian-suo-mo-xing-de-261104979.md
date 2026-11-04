---
title: Scaling Laws For Data-Constrained Dense Retrieval
title_zh: 数据受限场景下稠密检索模型的缩放定律
authors:
- Bowen Fu
- Jingtao Zhan
affiliations:
- Tsinghua Shenzhen International Graduate School
- Xi'an Jiaotong University
arxiv_id: '2611.04979'
url: https://arxiv.org/abs/2611.04979
pdf_url: https://arxiv.org/pdf/2611.04979
published: '2026-11-03'
collected: '2026-11-04'
category: RecSys
direction: 稠密检索 · 数据受限训练缩放定律
tags:
- Dense Retrieval
- Scaling Law
- Data Constrained Training
- Fine-tuning
- MAEL
one_liner: 提出数据受限稠密检索的MAEL乘法缩放定律及资源分配最优策略
practical_value: '- 在服务性能可承载的前提下，优先升级更大的预训练基座模型，效率是增加独有训练数据的1.46倍，可直接用于电商搜索召回、RAG检索模块的预算分配决策

  - 训练调优可复用最优weight decay规则：固定模型和学习率时，独有训练数据减半则weight decay翻倍，无需逐数据集网格搜索，适配所有稠密召回模型训练场景

  - 可复用最优训练步数缩放公式（Step∝N^-0.5 * U^0.92 / lr）提前估算训练停止点，避免无效训练浪费算力，适合大批次召回模型的训练调度

  - 可用MAEL替代传统固定步长评估来筛选最优checkpoint，MAEL与下游MRR/Recall的相关系数超过0.98，大幅降低超参搜索成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有大模型缩放定律默认训练数据充足，而稠密检索依赖的标注点击数据、用户交互日志非常稀缺，训练时通常重复多轮迭代，传统缩放定律无法指导这类数据受限场景的模型选型、数据采购和训练调优，资源分配缺乏量化依据。

### 方法关键点
- 定义最小可实现评估损失（MAEL）作为性能度量，验证不同学习率下相同模型和数据配置的MAEL几乎一致，CKA相似度接近1，不受学习率等优化超参干扰
- 提出MAEL与非嵌入层参数量N、独有训练样本数U的乘法幂律关系，优于传统Chinchilla/Kaplan的加法缩放公式，同时推导最优训练步数、最优weight decay的缩放规则
- 量化模型扩容与数据扩容的算力效率比，给出固定预算下的资源分配策略

### 关键结果
在MS MARCO数据集上微调35个不同参数量的BERT系稠密检索模型，覆盖5K~320K独有训练样本：
- MAEL乘法缩放公式拟合R²达0.99，外推预测平均相对误差仅3%左右
- MAEL与下游MRR@10、Recall@100的斯皮尔曼相关系数均达-0.996，完全匹配真实检索效果排序
- 相同微调算力下，升级预训练模型大小的效率是增加独有训练数据的1.46倍
- 按EMA时长配置最优weight decay可跨数据集稳定提升检索效果，域内NDCG@10最高提升1.7%，域外BEIR基准最高提升2.2%

### 核心结论
数据受限的稠密检索微调场景下，优先升级预训练基座比采购标注数据的投入产出比更高。

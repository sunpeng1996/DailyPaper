---
title: Spectral characteristics of autoencoder parameters as a vector representation
  of data
title_zh: 基于自编码器参数谱特征的数据向量表示方法
authors:
- Maria Nikitina
- Anton Bishuk
- Oleg Bakhteev
arxiv_id: '2609.03495'
url: https://arxiv.org/abs/2609.03495
pdf_url: https://arxiv.org/pdf/2609.03495
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 自编码器 · 数据表征学习
tags:
- Autoencoder
- Spectral Analysis
- Vector Representation
- Embedding
- Model Interpretability
one_liner: 利用自编码器参数矩阵的谱特征构造数据向量表示，无需依赖原样本或复杂向量生成算法
practical_value: '- 电商用户/商品表征场景可尝试用轻量自编码器参数的谱特征替代原数据嵌入，降低原始样本存储与传输开销

  - 推荐模型迭代前，可通过比对不同数据子集训得的自编码器谱特征，快速验证数据分布差异，无需全量样本统计

  - 冷启动场景下无需存储原始样本，仅通过轻量自编码器参数即可生成目标数据表征，简化推理链路复杂度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有数据向量表征方案多依赖原始样本或复杂生成算法，训练数据分布与模型参数的映射关系不明确，无法利用已训模型参数直接提取数据特征。
### 方法关键点
1. 提出将自编码器参数作为对应训练数据的稠密向量表示，基于参数矩阵的谱特征构造表征向量
2. 理论证明自编码器参数矩阵的奇异值与训练数据协方差矩阵的特征值强相关，可保障数据空间到参数空间的信息传递有效性
### 关键结果
在CIFAR-10、FashionMNIST数据集上，该表征无需原始样本、无需复杂生成算法，即可高准确率区分不同数据子集训练得到的自编码器，验证了表征的有效性。

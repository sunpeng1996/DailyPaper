---
title: 'LFM: Leveraging Foundation Models for Source-Free Universal Domain Adaptation'
title_zh: LFM：利用基础模型实现无源通用域适配
authors:
- Jing Li
- Pan Liu
- Meng Zhao
- Wanli Xue
- Yanhong Yang
- Xu Cheng
- Fan Shi
- Jianhua Zhang
- Qinghua Hu
- Shengyong Chen
arxiv_id: '2607.17653'
url: https://arxiv.org/abs/2607.17653
pdf_url: https://arxiv.org/pdf/2607.17653
published: '2026-07-20'
collected: '2026-07-23'
category: Training
direction: 无源通用域适配 · 基础模型应用
tags:
- Domain Adaptation
- Foundation Model
- VLM
- Pseudo Label
- Gaussian Mixture Model
one_liner: 结合VLM、LLM与二元高斯混合模型，实现无源头数据、适配标签偏移的通用域迁移框架
practical_value: '- 跨域冷启动场景下，可复用VLM+LLM生成未知类语义标签的思路，无需源数据就能快速适配新域样本分类

  - 针对未知类别识别需求，可直接套用二元高斯混合模型拟合相似度分布的trick，替代人工调阈值的低效方案

  - 多模型共识伪标签优化策略可迁移到推荐系统跨域召回场景，融合源预训练模型与大模型知识提升伪标签准确率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有无源通用域适配（SF-UniDA）方法依赖阈值调优、聚类等低效技术，未充分利用基础模型的泛化与零样本能力，无法高效同时处理协变量偏移与标签偏移问题。

### 方法关键点
1. 用VLM计算目标样本与文本标签的相似度，其中未知类文本标签通过prompt LLM生成
2. 基于相似度样本得分的变异系数判断标签偏移类型，通过拟合二元高斯混合模型识别未知样本
3. 采用共识策略，用源预训练模型初始化的目标模型优化VLM生成的伪标签，融合源域与基础模型知识后训练目标模型

### 关键结果
在全类型标签偏移场景、多个通用域适配基准测试集上效果显著优于现有SF-UniDA方法

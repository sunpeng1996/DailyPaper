---
title: Attribute-Prompted Kernel Hashing for Unsupervised Data-Efficient Cross-Modal
  Retrieval
title_zh: 面向无监督数据高效跨模态检索的属性提示核哈希方法
authors:
- Runhao Li
- Xiaoxu Ma
- Zhenyu Weng
- Yue Zhang
- Guibo Luo
- Huiping Zhuang
- Zhiping Lin
- Yap-Peng Tan
arxiv_id: '2607.00379'
url: https://arxiv.org/abs/2607.00379
pdf_url: https://arxiv.org/pdf/2607.00379
published: '2026-07-01'
collected: '2026-07-02'
category: Multimodal
direction: 多模态检索 · 低数据量哈希建模
tags:
- Cross-Modal Retrieval
- Hashing
- Prompt Learning
- Kernel Method
- Data-Efficient Learning
- Unsupervised Learning
one_liner: 基于视觉语言大模型属性先验构建数据高效无监督跨模态哈希框架，低数据量下检索泛化性优于SOTA
practical_value: '- 电商图文搜商品等跨模态检索场景标注不足时，可复用CAKM模块通过prompt学习动态属性核，降低对齐标注成本

  - 稀疏跨模态配对数据训练时可借鉴KSCA的核分布平滑思路，替代点对点对比学习，缓解小样本过拟合问题

  - 跨模态召回层可直接复用该哈希编码方法，将高维多模态特征压缩为低维哈希码，大幅降低存储和检索时延'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有无监督跨模态哈希方法高度依赖大规模对齐图文对，采集/标注成本高，且易过拟合已见训练类别，对未见类别泛化性差，无法满足隐私受限、标注稀缺场景的检索需求。
### 方法关键点
1. 提出APKH框架，基于视觉语言大模型的通用属性先验构建模态对齐的紧凑汉明空间；
2. 设计CAKM模块，通过超球面RBF核映射实现跨模态对齐，用prompt学习优化动态属性核捕捉模态不变语义；
3. 设计KSCA模块，将有限配对数据建模为连续核分布，替代传统点对点对比学习，平滑模态差异缓解稀疏配对过拟合。
### 关键结果
数据受限场景下，可见类别到未见类别的跨模态检索任务中，APKH性能全面优于当前SOTA哈希方法。

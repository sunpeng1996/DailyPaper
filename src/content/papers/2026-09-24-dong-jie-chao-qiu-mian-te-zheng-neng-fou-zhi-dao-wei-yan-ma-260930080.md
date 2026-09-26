---
title: Can Frozen Hyperspherical Features Guide the Selection of Pseudo Masks?
title_zh: 冻结超球面特征能否指导伪掩码选择？
authors:
- Xinge Guo
- Fengyang Xiao
- Dingming Zhang
- Yuhan Chen
- Rihan Zhang
- Xingjian Li
- Tianyang Wang
- Chunming He
- Sina Farsiu
affiliations:
- Duke University
- Carnegie Mellon University
- University of Alabama at Birmingham
arxiv_id: '2609.30080'
url: https://arxiv.org/abs/2609.30080
pdf_url: https://arxiv.org/pdf/2609.30080
published: '2026-09-24'
collected: '2026-09-26'
category: Other
direction: 无监督图像分割 · 伪标签筛选
tags:
- PseudoLabel
- UnsupervisedSegmentation
- SAM
- DINOv2
- SelfSupervisedLearning
one_liner: 提出基于冻结超球面特征的SphereTrust方法，无需标注即可优选SAM生成的伪掩码并支撑无监督训练
practical_value: '- 电商商品图抠图场景可复用超球面特征对比逻辑，无需额外标注即可优选SAM输出的商品掩码，降低标注成本

  - 针对三类常见错误分别设计打分维度的思路，可迁移到推荐系统伪正负样本过滤、RAG候选块排序场景，提升数据/候选质量

  - 冻结预训练backbone特征做无监督排序的方案，可用于低算力要求的粗排场景，无需额外训练即可上线'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
SAM等基础分割模型对无标注图像会输出多份候选伪掩码，若训练时选择错误掩码会导致学生模型精度下降，现有掩码选择方法需额外调用大模型或基于标注训练质量头，部署成本高。
### 方法关键点
利用冻结DINOv2的归一化patch特征天然分布在超球面的特性，候选掩码会将超球面拆分为前景、背景两个特征簇；提出SphereTrust，针对掩码漏检、背景泄露、选错目标三类常见错误，分别用簇间角度对比度、前景外观模式覆盖率、边框接触度三个维度打分，单图候选排序仅需0.55s，无需额外标注或训练。
### 关键结果数字
在8个SAM/SAM3候选掩码集上，6个集的平均选择Dice比最强基线高1.7~9.3个百分点；低光照伪装场景下Dice仅落后最优标注适配方法0.1个百分点，灾难性错误率更低；用于训练时加权F比固定标签训练高2.3~5.5个百分点，在19个测试集上性能比肩现有SOTA无监督分割方法。

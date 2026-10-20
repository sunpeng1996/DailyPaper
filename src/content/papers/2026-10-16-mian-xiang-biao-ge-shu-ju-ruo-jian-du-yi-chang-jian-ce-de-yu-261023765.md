---
title: Universal Semantic Enhancement for Weakly Supervised Anomaly Detection
title_zh: 面向表格数据弱监督异常检测的通用语义增强方法
authors:
- Siyu Zhou
- Yuqin Xie
- Hao Yuan
- Yingjie Zhou
affiliations:
- The Hong Kong University of Science and Technology
- Sichuan University
arxiv_id: '2610.23765'
url: https://arxiv.org/abs/2610.23765
pdf_url: https://arxiv.org/pdf/2610.23765
published: '2026-10-16'
collected: '2026-10-20'
category: Other
direction: 表格数据弱监督异常检测 · 特征融合
tags:
- Anomaly Detection
- Weakly Supervised
- Tabular Data
- Feature Fusion
- Foundation Model
one_liner: 融合预训练表格大模型通用语义与领域特征，提升少标签下表格数据弱监督异常检测性能
practical_value: '- 电商风控、异常刷单/账号检测等少标签表格类任务，可复用「预训练表格基础模型通用语义+领域特征融合」的框架，降低对标注数据的依赖

  - 特征融合环节可借鉴prototype-conditioned调制机制，平衡跨域通用知识和业务域特有分布的权重，避免少标签下过拟合

  - 业务侧标注成本极高的异常检测场景，可参考仅用8个标注样本就能训练的方案，快速上线基线模型'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
表格数据弱监督异常检测是金融风控、电商反作弊等业务场景的核心需求，现有方法仅针对目标域分布建模特征，存在异常特征覆盖不全、极少标注样本下易过拟合的痛点。
### 方法关键点
1. 通用语义增强的弱监督异常检测框架，融合预训练表格基础模型的跨域通用语义知识，与目标域数据学习到的领域特有特征，二者形成天然互补；
2. 设计原型条件调制机制，高效融合两类特征，实现互相强化的异常表达学习。
### 关键结果
仅提供8个标注异常样本参与训练时，方法性能优于所有对比SOTA方案。

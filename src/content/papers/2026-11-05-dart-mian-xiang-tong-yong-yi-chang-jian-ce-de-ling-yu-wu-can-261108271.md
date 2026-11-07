---
title: 'DART: Domain-Agnostic Residual Transfer for Generalist Anomaly Detection'
title_zh: DART：面向通用异常检测的领域无关残差迁移方法
authors:
- Muhammad Aqeel
- Maham Nazir
- Marco Cristani
- Francesco Setti
affiliations:
- University of Verona
- Beihang University
- Reykjavik University
arxiv_id: '2611.08271'
url: https://arxiv.org/abs/2611.08271
pdf_url: https://arxiv.org/pdf/2611.08271
published: '2026-11-05'
collected: '2026-11-07'
category: Other
direction: 通用异常检测 · 跨域残差解耦
tags:
- Anomaly Detection
- Cross-Domain Transfer
- Disentangled Representation
- Meta Training
- Plug-in Module
one_liner: 提出可插拔残差解耦框架DART，解决通用异常检测残差领域纠缠导致的跨域迁移差问题
practical_value: '- 残差解耦思路可迁移至跨域推荐场景，分离用户通用长期兴趣与场景/平台特有噪声，提升跨域推荐泛化性

  - 可插拔架构设计范式可复用，无需改动现有推荐pipeline核心逻辑即可插入特征优化模块，大幅降低落地成本

  - 跨域元训练的episode构造方法可借鉴到少样本跨域推荐任务，强化分布偏移下的模型鲁棒性

  - 电商商品合规、内容风控的异常检测场景，可直接复用DART框架实现跨品类异常识别，降低小样本标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
通用异常检测（GAD）旨在仅用少量参考样本识别unseen域的异常，现有利用异常参考的方法存在残差纠缠问题：可迁移异常线索与纹理、几何、采集条件等领域特有外观因子混合，限制跨域迁移效果，易在新域产生伪激活。
### 方法关键点
提出可插拔框架DART：
1. 新增残差解耦模块，保留异常判别信息的同时抑制领域特有信息
2. 搭配跨域元训练策略，跨源域构造训练episode优化解耦效果
整体架构无关，可直接插入现有GAD pipeline的残差计算与检测头之间，无需改动原有逻辑。
### 关键结果
在MVTec AD、VisA、BraTS三个公开数据集上相对多个基线方法取得一致提升，域偏移幅度越大时模型增益越显著。

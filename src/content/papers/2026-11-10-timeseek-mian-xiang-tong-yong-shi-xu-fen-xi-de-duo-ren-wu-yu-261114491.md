---
title: 'TimeSeek: Multi-Task and Multi-Domain Pretraining for Generalized Time Series
  Analytics'
title_zh: TimeSeek：面向通用时序分析的多任务多域预训练框架
authors:
- Peng Chen
- Yihang Wang
- Zhongwen Rao
- Yang Shu
- Yuying Qiu
- Yuxuan Chen
- Lujia Pan
- Bin Yang
- Chenjuan Guo
arxiv_id: '2611.14491'
url: https://arxiv.org/abs/2611.14491
pdf_url: https://arxiv.org/pdf/2611.14491
published: '2026-11-10'
collected: '2026-11-12'
category: Other
direction: 通用时序分析 · 多任务多域预训练
tags:
- Time_Series_Foundation_Model
- Multi_Domain_Pretraining
- Multi_Task_Learning
- Time_Series_Forecasting
- Anomaly_Detection
one_liner: 提出多域特征提取与多任务协同训练的通用时序预训练模型，跨任务跨场景性能达SOTA
practical_value: '- 电商流量预测、异常订单检测、用户行为序列建模等多时序任务可复用其多任务协同训练思路，通过任务定制+跨任务训练兼顾共性与特性，减少多任务重复建模成本

  - 多域用户行为时序数据建模可借鉴其多域特征提取器的渐进式多尺度建模+自适应槽通道建模trick，自适应适配不同业务域的时序特征差异，提升跨域迁移效果

  - 少样本/零样本时序下游场景（如新业务线销量预测）可复用其预训练范式，降低冷启动阶段标注数据依赖，兼顾推理效率与效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有时序基础模型（TSFM）存在两大核心缺陷：一是依赖堆叠Transformer层扩参，无法自适应建模多域复杂时序模式；二是预训练多针对单任务，少量多任务方案未充分利用任务共性与特性，性能表现不佳。
### 方法关键点
1. 核心设计思路为域/任务异质性下的选择性信息共享；
2. 多域特征提取器包含渐进式多尺度建模、自适应槽通道建模模块，可基于域特征自适应捕获时序依赖与通道关联；
3. 多任务协同训练机制通过任务定制、跨任务训练平衡任务共性与特性，预训练阶段即可统一适配多类时序任务。
### 关键结果
大规模时序数据预训练后，在预测、异常检测、分类三类任务的少样本、零样本场景下均达到SOTA，同时具备优异推理效率

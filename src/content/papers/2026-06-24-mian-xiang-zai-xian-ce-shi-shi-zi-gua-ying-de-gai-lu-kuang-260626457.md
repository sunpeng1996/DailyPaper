---
title: A probabilistic framework for online test-time adaptation
title_zh: 面向在线测试时自适应的概率框架
authors:
- Daniel Corrales
- David Ríos Insua
affiliations:
- Institute of Mathematical Sciences, ICMAT-CSIC, Spain
- Universidad Autónoma de Madrid, Spain
arxiv_id: '2606.26457'
url: https://arxiv.org/abs/2606.26457
pdf_url: https://arxiv.org/pdf/2606.26457
published: '2026-06-24'
collected: '2026-06-27'
category: Training
direction: 测试时自适应 · 分布偏移适配
tags:
- Test-Time-Adaptation
- Distribution-Shift
- State-Space-Model
- Probabilistic-Model
- Online-Adaptation
one_liner: 基于状态空间建模构建可适配分布偏移的在线测试时自适应概率框架
practical_value: '- 电商推荐/广告系统遭遇大促、热点事件引发的用户行为分布偏移时，可复用该状态空间建模思路做在线无标注数据自适应，无需全量重训，大幅节省标注与算力成本

  - 线上推理服务的测试时自适应模块可参考该框架的参数时序演化、先验调优流程，提升模型在分布动态变化场景下的鲁棒性

  - 新业务冷启动阶段，可基于该框架用实时无标注数据快速适配模型，降低冷启动期的推荐/广告效果损失'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有监督学习默认训练与测试分布一致，实际部署场景（如推荐系统用户行为变迁、跨域模型部署）普遍存在分布偏移，重新采集标注数据、全量重训的时间与经济成本极高，现有方法无法高效利用无标注测试数据实现自适应。
### 方法关键点
基于状态空间建模架构搭建通用概率框架，支持测试阶段直接用无标注数据做在线自适应，无需依赖新增标注，可统一刻画参数学习、参数时序演化、先验调优、预测四大核心环节，适配任意类型的分布偏移场景。
### 关键结果
框架已完成完整理论推导，可直接迁移至各类存在分布漂移的离线/在线模型部署场景，无需定制化改造

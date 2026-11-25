---
title: 'Antom 3-in-1 Transformer: A Payment Foundation Model'
title_zh: Antom 三合一 Transformer：支付领域基础大模型
authors:
- Weiyu Han
- Haoyu Jiang
- Jie Sheng
- Youxi Pan
- Xianglong Liu
- Zeqi Ren
- Dongquan Yi
- Yinhao Liu
- Ruobing Zuo
- Ze Zhao
affiliations:
- Ant International
- East China Normal University
- Shanghai Jiao Tong University
- Tongji University
arxiv_id: '2611.25403'
url: https://arxiv.org/abs/2611.25403
pdf_url: https://arxiv.org/pdf/2611.25403
published: '2026-11-18'
collected: '2026-11-25'
category: LLM
direction: 领域大模型 · 支付风控异构表示融合
tags:
- Foundation Model
- Sparse Activation
- Risk Detection
- Heterogeneous Representation
- Transfer Learning
one_liner: 提出融合序列、表格、图表示的7B稀疏激活支付大模型，大幅提升跨场景风控效果
practical_value: '- 多源异构数据融合思路可直接复用：序列+表格+图的联合表示方案适配电商风控、用户全链路行为建模场景，解决跨业务数据分布不一致问题

  - 稀疏激活大模型架构可参考：7B总参数单任务仅激活1.7B的路由设计，平衡大模型效果与推理延迟，适配推荐/风控等低延迟要求的线上业务

  - 小样本冷启动方案可落地：预训练大模型仅需25%标注即可超过全量标注从零训练的基线，可复用在新业务、新市场的推荐/风控冷启动场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
跨境支付跨市场、跨业务数据分布差异大，欺诈手段迭代快，传统风控模型泛化性差、维护成本高，亟需通用支付基础模型支撑跨场景风险防控。
### 方法关键点
采用7B参数三合一Transformer架构，统一融合序列（用户行为）、表格（交易属性）、图（主体关系）三类异构数据表示；内置稀疏路由激活机制，单任务仅激活1.7B参数；基于海量支付数据预训练学习通用行为与关系表示。
### 关键结果
- 跨业务迁移场景下，相比同架构从零训练指标提升34.5%
- 仅用25%标注数据，AP、Recall@0.5%均超过全量标注从零训练的基线
- 亿级流量线上实验4个月，相比XGB-Online基线整体损失率降低37.88%

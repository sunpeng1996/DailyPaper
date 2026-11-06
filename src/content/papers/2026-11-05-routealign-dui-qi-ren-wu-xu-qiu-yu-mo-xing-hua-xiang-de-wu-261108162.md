---
title: 'RouteAlign: Aligning Task Requirements with Model Profiles for LLM Service
  Selection'
title_zh: RouteAlign：对齐任务需求与模型画像的LLM服务选择方法
authors:
- Jihao Zhao
- Ding Chen
- Yanfang Chen
- Bo Tang
- Feiyu Xiong
- Junchi Yan
- Zhiyu Li
affiliations:
- MemTensor (Shanghai) Technology Co., Ltd.
- Renmin University of China
- Shanghai Jiao Tong University
arxiv_id: '2611.08162'
url: https://arxiv.org/abs/2611.08162
pdf_url: https://arxiv.org/pdf/2611.08162
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: LLM服务路由 · 需求-能力对齐
tags:
- LLM Routing
- Model Profiling
- Service Selection
- Cost Efficiency
- Task Alignment
one_liner: 通过任务需求与模型能力画像对齐实现LLM服务最优选择，平衡任务质量与调用成本
practical_value: '- 电商/推荐多LLM调用场景可复用该框架的能力-需求对齐思路，先对用户query做10类能力+4级难度画像，匹配对应模型的历史分档表现，避免仅用语义相似召回导致的能力错配

  - 多模型服务迭代时可复用冻结的打分器，仅更新新增模型的能力画像即可，无需重新训练路由策略，大幅降低模型更新后的运维成本，适合频繁迭代的线上广告/推荐LLM服务集群

  - 可借鉴λ参数调节质量-成本偏好的设计，业务侧可根据不同场景（大促优先质量、日常低优query优先成本）动态调整λ，不需要重新训练路由模型

  - 本地证据加权思路可迁移到冷启动模型的效果预估，结合语义相似query的历史表现补全新模型的画像缺口，减少新模型上线的测试成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM服务路由多依赖全局评分或语义相似匹配，忽略了任务的能力组合需求与难度差异，导致同一场景下模型排序波动大，要么调用大模型成本过高，要么小模型能力不足导致效果下降，同时模型 catalog 迭代后路由策略需要重新训练，运维成本高。

### 方法关键点
- 设计0.6B小参数量的需求分析器，将query拆解为10维能力权重（编码、推理、数据分析等）+4级难度标签，作为统一的需求表示
- 构建分能力分难度的全局模型画像，结合语义召回的150个相似query的本地性能证据，通过共享线性打分器融合多维度特征预估模型在当前query的表现
- 引入可调λ参数控制质量-成本偏好，选择最优模型；模型catalog更新时仅需更新新增模型的画像数据，冻结的打分器可直接复用

### 关键实验
在10个公开数据集、13个LLM服务的基准上测试，对比RouteLLM等14种基线方法，Sample-Avg和Dataset-Avg分别超出RouteLLM 1.38、2.22个百分点，仅增加1.05%的调用成本；比最强Jev-style后端高5.22、6.44个百分点，调用成本还低9.7%；catalog迭代场景下，在初始7个模型上训练的打分器在后续8次更新中始终保持最优效果，平均领先次优基线4.41个百分点。

最值得记住的一句话：LLM路由的核心不是匹配query和模型的语义相似性，而是对齐任务的能力需求、难度与模型的分档表现，同时保留本地相似任务的性能证据，才能兼顾效果、成本与可维护性。

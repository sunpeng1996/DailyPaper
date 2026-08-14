---
title: MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification
title_zh: 面向鲁棒跨数据集图像分类的MLLM路由异构集成框架
authors:
- Daniel Perkins
- John Squires
- Janou Milligan
- Chandra Raskoti
- Linda Ungerboeck
affiliations:
- University of Tennessee, Knoxville
- The Bredesen Center for Interdisciplinary Research and Graduate Education
arxiv_id: '2608.13463'
url: https://arxiv.org/abs/2608.13463
pdf_url: https://arxiv.org/pdf/2608.13463
published: '2026-08-13'
collected: '2026-08-14'
category: Agent
direction: Agent 异构模型动态路由调度
tags:
- MLLM
- Dynamic Routing
- Ensemble Learning
- Cross-domain Classification
- Vision Agent
one_liner: 采用MLLM作为无训练动态路由Agent，匹配输入与异构视觉backbone，实现高性能跨域图像分类
practical_value: '- 电商多模态商品分类、内容审核场景可直接复用该MLLM无训练路由架构，新增分类模型/适配新类目仅需修改prompt，大幅降低迭代成本

  - 推荐/搜索多召回源调度场景可借鉴该思路：提前刻画各召回源的优劣势分布，用大模型路由匹配query/用户特征到最优召回源，替代传统训练式路由

  - 路由过程输出的自然语言推理trace可直接用于bad case归因，适合广告审核、电商合规等对可解释性要求高的业务场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
单数据集训练的图像分类模型在跨域、跨难度场景泛化能力极差，传统基于训练的异构模型路由方案适配新场景需重新训练，成本高且无推理可解释性，无法支撑复杂落地需求。
### 方法关键点
提出ARMDIL自适应路由框架：首先构建包含ResNet、自监督表示学习模型、VLM的异构视觉backbone池，所有模型基于多源数据集对齐的统一标签空间训练，提前完成各模型在不同视觉域的优劣势画像；采用MLLM作为无训练动态路由Agent，仅通过prompt引导即可分析输入图像特征，匹配最优backbone执行分类任务，路由过程同步输出自然语言推理链。
### 关键结果
跨数据集分类性能与专门训练的路由方案持平；适配新域/新增模型仅需修改路由prompt，无需重新训练；推理全程可追溯，bad case排查效率大幅提升。

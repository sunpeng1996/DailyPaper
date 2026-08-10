---
title: Pre-Inference Routing for Cost-Efficient Document Field Extraction
title_zh: 面向低成本文档字段提取的推理前路由方法
authors:
- Sreerekha Rajendran
affiliations:
- Independent Researcher
arxiv_id: '2608.06607'
url: https://arxiv.org/abs/2608.06607
pdf_url: https://arxiv.org/pdf/2608.06607
published: '2026-08-06'
collected: '2026-08-10'
category: LLM
direction: LLM推理优化 · 低成本路由
tags:
- model_routing
- cost_efficient_inference
- document_extraction
- interpretable_features
- inference_optimization
one_liner: 通过推理前轻量难度预测路由大小提取模型，在F1损失≤0.02的前提下大幅降低文档提取推理成本
practical_value: '- 电商广告合规审核、商品OCR信息提取场景可复用该路由架构，先上小标注Pilot验证路由收益再全量，避免无效投入

  - 路由模块无需复杂设计，用bow或简单人工特征即可达到最优效果，工程实现成本极低、ROI高

  - 路由模型不可跨数据集迁移，即使同品类文档也需单独小样本训练，避免直接复用的效果下跌'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前文档字段提取系统统一使用单一大模型，存在简单样本推理成本浪费、困难样本效果不足的矛盾，亟需低成本推理优化方案。
### 方法关键点
用极低overhead的文档表层特征（图像质量、布局、词袋特征）提前预测样本难度，将样本路由到低成本小模型或强效果大模型；提出路由生效的两个前置条件：小模型错误率足够高、错误可通过表层特征预测，可通过小标注Pilot提前验证条件是否满足。
### 关键结果数字
满足前置条件的场景下，路由策略可将收据类处理成本降低31-33%、退化广告采购表单成本降低77%，同时F1值相比全用大模型仅下降≤0.02；简单词袋路由效果与人工设计特征相当，路由模型不可跨数据集迁移，即使同品类也需单独训练。

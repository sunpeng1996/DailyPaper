---
title: 'MM-Spectrum: Multimodal Multi-spectral Molecular Structural Elucidation with
  a Stable MoE Framework'
title_zh: MM-Spectrum：基于稳定MoE框架的多模态多光谱分子结构解析
authors:
- Hai-tao Yu
- Nan Min
- Zheng Fang
- Hongyu Zhan
- Yusen Tan
- Yuhan Wang
- Jun Xia
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Southeast University
- Fudan University
- The Hong Kong University of Science and Technology
arxiv_id: '2608.27286'
url: https://arxiv.org/abs/2608.27286
pdf_url: https://arxiv.org/pdf/2608.27286
published: '2026-08-27'
collected: '2026-08-29'
category: Training
direction: 多模态MoE训练 · 模态不平衡优化
tags:
- MoE
- Multimodal
- Modality Routing
- Imbalance Mitigation
- Heterogeneous Experts
one_liner: 提出带模态感知路由的异质专家MoE框架，解决多模态异质性与不平衡导致的性能衰减问题
practical_value: '- 多模态融合类任务（如多模态内容推荐、多模态召回）可复用模态感知路由设计，路由层同时输入模态ID与token表征，缓解不同模态信息量差异大导致的模态淹没问题

  - MoE架构拆分单模态专属、跨模态交互、通用共享三类异质容量专家的方案，可直接迁移至多模态推荐场景，分别提取单模态特征、跨模态关联特征、通用特征，降低噪声干扰

  - 该框架在模态缺失场景下性能稳定，适合电商场景中用户行为/商品属性/内容模态不全的业务环境'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态多光谱分子结构解析任务中，直接拼接异质多模态输入的传统范式会出现异常性能衰减，核心诱因是模态间异质性强、模态不平衡引发的梯度冲突。
### 方法关键点
1. 面向多光谱场景定制稀疏MoE框架MM-Spectrum；
2. 新增显式模态感知路由机制，路由层同时输入光谱身份标识与token内容表征，适配多模态不平衡下的信息特征；
3. 引入共享专家、交互专家搭配异构专家容量，分别提取各模态独有信息、跨模态协同信息，同时抑制噪声干扰。
### 关键结果数字
在全模态、双模态、模态缺失三类设置下，对比最佳单模态基线，Top-1准确率最高提升31.8%，解决了基线多模态融合时准确率下降25.5%的性能崩塌问题。

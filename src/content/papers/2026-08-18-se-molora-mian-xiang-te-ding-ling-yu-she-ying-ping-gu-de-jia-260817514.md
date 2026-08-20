---
title: 'SE-MoLoRA: Shared-Expert LoRA Adapters for Domain-Specific Photographic Assessment'
title_zh: SE-MoLoRA：面向特定领域摄影评估的共享专家LoRA适配器
authors:
- Bishwash Khanal
- Anlan Zhang
- Sasu Tarkoma
- Tommi Mikkonen
- Abhishek Kumar
affiliations:
- University of Jyväskylä
- Adobe Research
- University of Helsinki
arxiv_id: '2608.17514'
url: https://arxiv.org/abs/2608.17514
pdf_url: https://arxiv.org/pdf/2608.17514
published: '2026-08-18'
collected: '2026-08-20'
category: Training
direction: 大模型参数高效微调 · 多模态垂域适配
tags:
- LoRA
- Parameter-Efficient Fine-Tuning
- Multimodal
- Domain Adaptation
- Regularization
- MoE
one_liner: 提出共享专家+路由子专家的模块化参数高效适配框架，提升多模态垂域评估的效果与可控性
practical_value: '- 做垂类多模态LLM适配时，可复用「通用高秩共享LoRA+垂类低秩路由LoRA」的架构，兼顾降参、通用知识继承与垂类效果

  - 多专家路由场景下，加入正交正则约束减少不同专家的表征重叠，提升各垂类任务输出的特异性与可控性，可直接迁移到电商商品多模态打分、内容审核等场景

  - 垂类训练数据不足时，可采用公开社区数据蒸馏打标签的方式低成本构造训练集，降低领域适配的数据成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
VLM通用视觉理解能力强，但语义内容与审美判断纠缠，无法输出摄影这类垂域的可落地评估建议，单LoRA适配效果差、全量微调成本高。
### 方法关键点
- 采用SE-MoLoRA模块化参数高效适配框架，拆分通用摄影知识与细分领域（构图/光线/技术质量）专项判断
- 高秩（rank 64）共享LoRA始终激活学习通用摄影知识，低秩（rank 32）路由子LoRA学习细分领域残差特征，搭配轻量查询路由器选择对应子专家
- 加入正交正则约束减少专家表征重叠，训练数据由Reddit摄影评论数据集蒸馏打标签得到
### 关键结果数字
对比单块LoRA，BERTScore-F1从0.2317提升至0.4215，84.6%的成对人工评估更偏好输出结果，激活参数比独立专项模型更少，消融实验验证共享-专家拆分与正交正则可有效降低专家重叠

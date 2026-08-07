---
title: Training-Free Token-Level Steering for LLM Personalized Co-Writing
title_zh: 无需训练的Token级引导LLM个性化协同写作方法
authors:
- Wenhao Mao
- Chengbin Hou
- Weixiao Wang
- Jialiang Zhu
- Min Liu
- Yibin Hao
- Hairong Lv
affiliations:
- Tsinghua University
- Fuyao University of Science and Technology
- Henan Provincial People’s Hospital
arxiv_id: '2608.06069'
url: https://arxiv.org/abs/2608.06069
pdf_url: https://arxiv.org/pdf/2608.06069
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: LLM个性化生成 · 免训练推理优化
tags:
- Training-Free
- Token-Level Steering
- Personalized Generation
- LLM Adaptation
- Co-Writing
one_liner: 提出免训练SteerWrite框架，实现token级引导的LLM个性化协同写作，性能SOTA且降低人工编辑成本
practical_value: '- 电商个性化营销文案（商品详情页、直播间话术、定制化Push）场景可直接复用该免训练框架，无需fine-tuning即可快速适配品牌文风/用户偏好，降低算力成本与迭代周期

  - 推荐系统配套的个性化内容生成场景可借鉴其token级引导逻辑，解决传统RAG生成内容颗粒度粗、不符合用户表达习惯的问题，提升内容转化率

  - 小样本域适配场景可复用其针对小数据集的免训练适配设计，无需大量标注数据即可快速落地个性化生成能力，适配冷启动场景需求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM面向个性化场景适配时存在三类核心痛点：一是fine-tuning类方案算力成本高，迭代周期长，无法适配域数据快速更新的业务需求；二是RAG类免训练方案仅能在prompt中注入上下文，无法实现细粒度token级生成引导，生成内容的个性化贴合度不足；三是当前LLM主流交互为对话范式，编码场景外的生产级协同写作能力未被充分挖掘，无法满足个性化内容生成需求。
### 方法关键点
提出免训练框架SteerWrite，无需任何梯度更新即可将通用基座LLM适配到特定域，针对小样本数据集做了专项适配设计，可实现token级的生成过程引导，支撑个性化协同写作场景需求。
### 关键结果
在多类型数据集、多评估指标、多开源基座LLM（Qwen、Llama系列等）上均达到SOTA性能，可显著降低人工编辑工作量。

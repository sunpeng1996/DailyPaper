---
title: LLM-Based Generative Retrieval for Snapchat Content Recommendation
title_zh: Snapchat 基于大语言模型的短视频生成式检索系统
authors:
- Liam Collins
- Jiwen Ren
- Donald Loveland
- Bhuvesh Kumar
- Clark Mingxuan Ju
- Xuan Guo
- Mo Li
- Alvin Hou
- Yi Cui
- Peng Yang
affiliations:
- Snap Inc.
arxiv_id: '2607.28895'
url: https://arxiv.org/abs/2607.28895
pdf_url: https://arxiv.org/pdf/2607.28895
published: '2026-07-30'
collected: '2026-08-03'
category: GenRec
direction: 生成式推荐 · Semantic ID 工业落地
tags:
- Generative Retrieval
- Semantic ID
- LLM4Rec
- Production Deployment
- Inference Optimization
one_liner: 工业级落地LLM驱动生成式检索系统SnapLGR，提供全链路建模与工程优化方案，线上指标优于TIGER基线
practical_value: '- Semantic ID构造可复用PPR-based共曝光对比学习方案，注入协同信号的同时降低ID碰撞，适配商品、短视频等多模态内容场景

  - 新增SID词汇的两阶段训练流程可大幅降低LLM适配成本：先CPT冻结基座仅对齐SID与文本语义，再SFT全参数微调序列推荐任务

  - 大流量生成式检索工程侧可直接复用优化组合：TensorRT-LLM CUDA波束搜索+去中心化worker架构+异步I/O，实测单GPU吞吐提升45.7倍

  - 生成式检索架构优先选decoder-only小基座，相同参数量下比encoder-decoder的T5架构检索效果高30%以上'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统TIGER风格生成式检索采用随机初始化的encoder-decoder小模型，无法利用LLM的语义先验与强序列建模能力，而直接将LLM改造为工业级生成式检索器面临三大核心挑战：自定义Semantic ID不在预训练词表、ID碰撞率高无法支撑大规模corpus、推理延迟与成本不符合上线要求，亟需全链路协同优化方案。
### 方法关键点
- SID构造：基于Qwen3-VL多模态embedding做残差量化，加入PPR计算的用户共曝光item对做对比学习，同时注入协同信号、提升码本利用率、降低ID碰撞
- 两阶段训练：先执行CPT（冻结LLM基座参数，仅通过SID到视频文本描述的生成任务训练新增SID嵌入，对齐LLM原有语义空间），再执行SFT（全参数微调，基于用户历史SID交互序列预测下一个点击SID）
- 工程优化：训练侧通过FlashAttention-2、动态序列打包、torch编译+迁移H100 GPU实现3.63倍训练吞吐提升；推理侧通过TensorRT-LLM CUDA波束搜索、去中心化worker架构、异步I/O实现45.7倍单GPU推理吞吐提升
### 关键实验
离线基于Snapchat大规模短视频数据集，和同SID、同训练数据的T5基线相比，Pass@32提升2.27倍，Recall@32提升2.4倍；线上7天A/B测试，比现有TIGER生产基线View Time提升0.37%，Time Spent提升0.09%，Deep Sessions提升0.18%，均统计显著。
### 核心结论
工业级LLM生成式检索落地不是单纯替换模型基座，需要SID构造、训练流程、工程架构的全链路协同优化，其中decoder-only架构选型是效果提升的最大贡献因素。

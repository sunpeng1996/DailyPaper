---
title: What Really Works for Universal Multimodal Embeddings? A Controlled Study of
  Contrastive Training Strategies
title_zh: 通用多模态嵌入对比训练策略的有效性对照研究
authors:
- Duo Li
- Haojun Pan
- Zuhao Yang
- Xintong Wang
- Chengfu Huo
- Shijian Lu
- Liang Ding
affiliations:
- Nanyang Technological University
- Alibaba Group
- Universität Hamburg
- Sichuan University
arxiv_id: '2610.15035'
url: https://arxiv.org/abs/2610.15035
pdf_url: https://arxiv.org/pdf/2610.15035
published: '2026-10-09'
collected: '2026-10-14'
category: Training
direction: 多模态嵌入 · 对比训练优化
tags:
- Multimodal Embedding
- Contrastive Learning
- MLLM
- Hard Negative Mining
- Training Strategy
one_liner: 统一基准下系统评测多模态对比训练策略，给出可落地的最优训练组合方案
practical_value: '- 训练电商多模态商品/内容Embedding时，不要单独使用梯度调制类策略（如给高相似负样本加权），会同时放大有效梯度和假负样本的误导梯度，反而导致效果下降

  - 不要将正负样本相似度分布的分离度作为Embedding效果的核心离线评估指标，全局分布分离度不代表实例级排序效果，应直接使用业务真实召回/排序指标评估

  - 多模态检索/Embedding训练可直接复用B3组合策略：同时做假负样本过滤、实例级难负样本挖掘、难负样本批次构造，相比基线可带来约6%的相对效果提升

  - 做Embedding效果bad case分析时，可复用MLLM-as-Judge框架，将错误拆分为假负、难负、易负三类，比单纯看Precision更易定位训练问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
近年多模态对比学习的训练策略（负样本选择、批次构造、梯度调制等）百花齐放，但不同方法的验证环境不统一，无法区分是策略本身有效还是超参数/架构优化带来的增益，亟需在可控条件下验证各类策略的真实效果，给出可落地的训练配方。

### 方法关键点
- 统一基准：以VLM2Vec为基线框架，固定Qwen2-VL-2B/7B、Qwen3.5-2B作为backbone，统一训练超参数（学习率1e-4、LoRA rank=16、last token pooling等），在MMEB基准上对比8种代表性对比训练策略
- 诊断框架：提出MLLM-as-Judge分析框架，将Top1检索结果拆解为标注正样本、假负样本（未标注的有效匹配）、难负错误、易负错误四类，细粒度定位策略的失效模式
- 控制变量实验：分别测试梯度调制、假负缓解、批次构造三类单维度策略的效果，再验证多维度组合策略的增益

### 关键结果
在覆盖36个数据集的MMEB基准上测试，基线VLM2Vec的整体Precision@1为65.1%；单维度策略最多仅带来0.2%的绝对增益，多数甚至降点；将假负过滤、难负挖掘、难批次构造三者结合的B3策略，整体Precision@1达到69.0%，相比基线相对提升6%，跨模型测试也稳定带来1.5~3.3个百分点的绝对增益，额外加入梯度调制反而掉点。

### 核心结论
单维度优化对比训练策略的增益非常有限，同时覆盖实例级难负挖掘、假负过滤、批次级难负构造的组合方案才能带来稳定的效果提升，不要盲目迷信单一的“先进”训练策略。

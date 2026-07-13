---
title: Complexity-Guided Component-wise Initialization for Language Model Pretraining
title_zh: 复杂度引导的大语言模型预训练组件级初始化方法研究
authors:
- Konstantin Garbers
- Nicholas Oh
affiliations:
- Peking University
arxiv_id: '2607.09204'
url: https://arxiv.org/abs/2607.09204
pdf_url: https://arxiv.org/pdf/2607.09204
published: '2026-07-10'
collected: '2026-07-13'
category: Training
direction: 大语言模型预训练 · 权重初始化优化
tags:
- LM Pretraining
- Weight Initialization
- Transformer
- Spectral Analysis
- GPT-2
one_liner: 分析11种GPT-2风格预训练模型的权重谱规律，验证仅粗粒度谱匹配的初始化方案无预训练性能增益
practical_value: '- 自研电商/推荐场景垂直小LLM预训练时，无需额外开发粗粒度权重谱匹配的初始化方案，直接采用常规随机初始化或开源预训练权重微调即可，减少无效研发投入

  - 可复用论文提出的Frobenius范数、有效秩熵指标，作为自有预训练LLM的结构诊断工具，快速定位训练异常的Transformer层/子组件

  - 若尝试基于预训练权重规律设计初始化方案，不要仅做组件级尺度和奇异值形状匹配，需保留更丰富的权重信息才能获得性能收益'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有大语言模型预训练普遍采用随机初始化，忽略了不同训练配置下Transformer模型普遍存在的层间、组件间权重谱规律，亟需验证这类通用规律能否用于优化初始化，提升预训练效率与效果。

### 方法关键点
1. 分析11个跨大小、语言、分词器、训练语料的GPT-2风格预训练checkpoint，统计各层及Transformer子组件的Frobenius范数、有效秩熵；
2. 基于观测到的通用权重谱特征（如残差写矩阵随深度增大幅值、谱集中度提升），设计模仿预训练模型组件级尺度和谱分布的初始化方案，与多种现有初始化方法做对比实验。

### 关键结果
1. 新初始化方案可显著改变模型结构谱模式，但未带来对应预训练性能优势；
2. 直接复用预训练权重的效果仍最优，仅粗粒度谱匹配不是可靠的预训练优化策略；
3. 预训练权重谱可作为训练后模型结构的有效诊断工具，但有效复用需保留比组件级尺度、奇异值形状更丰富的信息。

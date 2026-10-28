---
title: The Lexical Imprint of Pre-training Data
title_zh: 预训练数据的词汇印记：词级交叉熵对齐度量及多场景应用
authors:
- Jeonghoon Kim
- Woojin Chung
- Woomin Song
- Cheonbok Park
- Nako Sung
- Jinwoo Shin
affiliations:
- NAVER Cloud
- KAIST
arxiv_id: '2602.10657'
url: https://arxiv.org/abs/2602.10657
pdf_url: https://arxiv.org/pdf/2602.10657
published: '2026-10-25'
collected: '2026-10-28'
category: LLM
direction: LLM预训练数据对齐 · 零样本性能与推理优化
tags:
- UCE
- pre-training data
- zero-shot performance
- data selection
- speculative decoding
one_liner: 提出模型无关的词级单字交叉熵UCE，可追踪预训练数据的零样本词汇印记，支持数据选择、推理路由优化
practical_value: '- 垂域LLM/生成式推荐模块训练时，可先用UCE计算业务数据集与候选训练语料的对齐度，优先选UCE低的语料，无需预训练就能预判适配性，大幅降低语料筛选成本

  - 领域微调阶段，可通过UCE-filter筛选与业务目标对齐的训练文档，在相同token预算下提升垂域任务（如商品文案生成、query理解）的零/少样本准确率

  - 多垂域Agent/多模型推理部署场景，可基于用户query与各领域小模型语料的UCE做路由，类似文中Speculative Decoding调度逻辑，平均可提升5%+推理吞吐量，不损失效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
以往LLM零样本性能常被直接归因于模型通用能力，但预训练语料与目标任务的词汇分布对齐对表现的影响未被量化，且现有分析易与训练配方、模型规模、训练历史等因素耦合，亟需一种无需模型、Tokenizer无关的高效对齐度量方法，量化预训练数据的词汇层面影响。

### 方法关键点
- 提出词级单字交叉熵（UCE），通过预训练语料和目标数据集的词频分布计算交叉熵，等于目标分布熵加两者的KL散度，无Tokenizer偏差，计算效率极高
- 支持三个层级的落地应用：语料级对齐度排序、文档级数据过滤（UCE-filter）、Prompt级推理路由

### 关键实验结果
- 控制变量预训练：覆盖3种模型规模（400M/1.33B/3.36B）、4种预训练语料、10个零样本基准，UCE与零样本准确率呈强负相关（R²最高达0.928），UCE越低准确率越高
- 文档筛选：UCE-filter在7个目标常识任务上，相比随机采样最多提升3.6pp零样本准确率，效果优于DSIR等现有数据选择方法
- 推理路由：Speculative Decoding场景下基于UCE路由Prompt，相比通用Drafter平均提升5.3pp解码速度

### 核心结论
似然训练会让模型的预测分布向预训练语料的词汇分布倾斜，零样本性能很大程度上反映了预训练语料与目标任务的词汇对齐程度，而非仅模型本身的通用能力

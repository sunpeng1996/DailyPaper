---
title: 'Making Collaborative Signals Count: Graph-Aware Large Language Models for
  Sequential Recommendation'
title_zh: 面向序列推荐的图感知大语言模型框架GALLM
authors:
- Fenglin Yan
- Bohao Wang
- Jian Zhang
- Yu Cui
- Tongya Zheng
- Ye Feng
- Can Wang
- Jiawei Chen
affiliations:
- Zhejiang University
- University of Science and Technology of China
arxiv_id: '2608.12184'
url: https://arxiv.org/abs/2608.12184
pdf_url: https://arxiv.org/pdf/2608.12184
published: '2026-08-12'
collected: '2026-08-13'
category: GenRec
direction: 生成式推荐 · 协同信号原生注入
tags:
- Sequential Recommendation
- LLM4Rec
- Graph Attention
- Collaborative Filtering
- Attention Bias
- LoRA
one_liner: 通过轻量可学习注意力偏置将协同图关系注入LLM，实现语义与全局协同信号联合建模的序列推荐方案
practical_value: '- 可复用三元关系（Text-Text/Item-Text/Item-Item）注意力偏置设计，无需修改LLM主干，仅新增极少量可学习参数即可注入业务侧商品关联、用户行为等结构化信号，适配现有LoRA微调流程

  - 全局商品共现强度分桶方案可直接迁移，将商品搭配、类目关联、共点击等业务先验离散为有限类别，对应不同注意力偏置，规避稀疏共现数据的噪声干扰

  - 「商品文本Token + 专属Item Token」的混合Prompt构造方式，可解决协同嵌入与LLM文本空间对齐差的痛点，同时保留LLM原生语义理解能力

  - 方案在1B/3B/8B不同规模LLaMA3上均稳定生效，中小模型也可获得明显收益，适配对推理延迟要求高的电商推荐线上场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM-based推荐存在两大核心痛点：一是通过外部推荐模型注入协同信号的方式，存在协同表示与LLM文本空间对齐差的问题，实证显示协同嵌入对预测结果的贡献远低于文本token；二是仅建模用户序列内的商品依赖，无法捕捉跨用户的全局协同模式，限制推荐效果提升，亟需探索更原生的LLM协同信号注入方式。

### 方法关键点
- 混合Prompt构造：每个历史商品对应「文本描述Token + 专属Item Token」，Item Token embedding可由传统推荐模型（如SASRec）的商品表示经MLP映射初始化，提供协同先验
- 协同图构建：定义三类Token间异构关系：Text-Text（保留文本语义依赖）、Item-Text（对齐Item Token与对应商品文本描述）、Item-Item（基于全局商品共现频率分桶定义协同强度）
- 图感知注意力注入：将三类关系转化为对应可学习注意力偏置，直接加入Transformer自注意力计算，保留原有因果掩码，无需修改LLM主干或新增外部图编码器，仅训练LoRA和偏置参数即可

### 关键实验
在Amazon Toys/Clothing/Books、MovieLens-10M四个公开数据集上，对比SASRec、LightGCN、LLaRA、HatLLM等10个SOTA基线，HR@5平均提升9.76%（最高达16.30%），NDCG@5平均提升7.62%；在1B/3B/8B不同规模LLaMA3上均稳定优于对比基线，无模型规模依赖。

### 核心结论
将全局协同结构化信息转化为LLM原生的注意力偏置，比外部注入协同嵌入的方式更能有效激活LLM的协同信号建模能力。

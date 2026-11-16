---
title: 'LECAT: Measuring LLM Category Learning from Pretraining Data'
title_zh: LECAT：分析大语言模型从预训练数据中学习类别知识的框架
authors:
- Jimin Mun
- Maarten Sap
- Yanai Elazar
affiliations:
- Carnegie Mellon University
- Bar-Ilan University
arxiv_id: '2611.18419'
url: https://arxiv.org/abs/2611.18419
pdf_url: https://arxiv.org/pdf/2611.18419
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: 大语言模型预训练 · 类别知识学习
tags:
- LLM Pretraining
- Category Learning
- Knowledge Acquisition
- Evaluation Framework
- Data Curation
one_liner: 推出LECAT分析框架，量化LLM类别知识学习能力，揭示预训练数据表达的影响规律
practical_value: '- 垂直领域LLM微调/预训练时，避免仅重复直白规则表述（如“XX品类性价比高”），混合加入上下文增强/削弱、例外、实例等多种知识表达形式，可提升模型知识灵活运用能力，减少生硬规则过拟合

  - 推荐系统的用户/物品标签、品类属性知识注入场景，可复用论文的log概率差（G值）指标快速验证模型对类别-属性关联的学习效果，相比LLM-as-a-judge大幅降低评估成本

  - Agent知识库构建时，针对类别类常识（如“3C产品需售后保障”），提升类别与特征的PMI（共现点互信息）、增加多样化上下文表达，更利于LLM灵活调用知识应对复杂用户query'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有研究多关注LLM事实类知识的习得机制，对可泛化的类别知识（如“飞机速度快”“柠檬是黄色的”）的学习规律、预训练数据的影响尚不明确。类别知识的学习效果直接决定LLM的推理准确性、刻板印象抑制能力、下游场景的知识灵活调用能力，是LLM落地的核心影响因素之一。

### 方法关键点
- LECAT双层框架，输出层从记忆、泛化、上下文灵活性三个维度用log概率差（G值）指标量化类别知识学习效果，经LLM-as-a-judge验证相关系数达0.87以上
- 定义5种类别知识表达形式：直白重复、实例表述、例外、上下文增强、上下文削弱，可用于数据分析或合成训练数据
- 分别在开源预训练模型（Pythia、OLMo3，14M到32B参数）和可控合成训练场景（68M小模型，基于TinyStories注入虚构类别对）上开展验证

### 关键结果
- 开源模型测试覆盖199个人工标注+模型生成的类别-特征对，泛化能力随模型规模提升：2.8B Pythia模型的基础规则到不变上下文的泛化通过率达95.5%，但上下文灵活性始终较差，削弱上下文与错误上下文的区分通过率仅10%~24%
- 可控训练实验显示，混合多种知识表达形式的训练集整体通过率最高（0.51），仅使用直白重复规则的训练集上下文增强通过率仅0.03，远低于混合训练的0.37

### 核心结论
预训练数据的知识表达形式比单纯的曝光频次更影响类别知识的灵活学习，直白重复会降低模型上下文灵活性，多样化表达才能提升鲁棒性

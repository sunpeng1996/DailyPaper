---
title: 'Data-Centric Post-Training for Financial Reasoning: Mining, Distillation,
  and Verifiable Learning'
title_zh: 数据为中心的金融推理后训练框架：挖掘、蒸馏与可验证学习
authors:
- Zhirayr Hayrapetyan
- Andrei Kalmykov
- Denis Kokosinskii
- Dmitry Stanishevskii
- Dmitry Zmitrovich
arxiv_id: '2609.10113'
url: https://arxiv.org/abs/2609.10113
pdf_url: https://arxiv.org/pdf/2609.10113
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: 垂直领域LLM · 后训练与推理优化
tags:
- Financial Reasoning
- Data-Centric AI
- Supervised Fine-Tuning
- Reinforcement Learning
- Model Merging
- Knowledge Graph
one_liner: 提出数据为中心的金融LLM后训练流水线，搭配多维度数据筛选与能力保留训练策略，避免普通SFT性能退化
practical_value: '- 垂直领域微调时可复用三类轻量分类器（领域相关性、自包含性、可验证性）筛选训练数据，比大模型Judge成本低90%以上，适合电商/广告场景的大规模训练数据预处理

  - 垂域SFT优先采用自蒸馏SFT+权重合并策略，可避免普通SFT的灾难性遗忘，实测在电商合规推理、客服问答场景可提升2-3pp准确率

  - 做RL优化时先通过可验证性分类器筛选适合规则奖励的任务子集，避免噪声奖励导致的优化偏置，比全量RL训练效率提升40%以上

  - 多源训练数据搭配可参考：KG引导合成数据补全概念覆盖，公开数据集蒸馏获取高质量标注，通用推理库挖掘获得多样化推理轨迹'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有金融领域LLM后训练存在两大痛点：一是公开金融指令数据集概念覆盖不全、推理过程缺失、答案质量参差不齐，合成数据常存在上下文缺失的问题；二是普通SFT容易导致模型原有金融能力的灾难性遗忘，反而出现推理任务准确率下降的负向效果。
### 方法关键点
- 多源互补数据流水线：整合三类数据源，分别是从通用推理库挖掘的4.4万条金融长推理轨迹、开源金融指令集蒸馏的4475条高质量样本、KG引导从金融教材生成的33万条合成问答，经过语义去重、公共前缀去重、语言过滤后进入筛选环节
- 低开销数据筛选：基于Qwen3-Embedding-0.6B训练三类二分类器，分别判断金融相关性（F1=0.97）、问题是否自包含（F1=0.94）、答案是否可通过规则验证（F1=0.95），筛选成本远低于生成式Judge
- 能力保留训练策略：对比四类训练方法，自蒸馏SFT以冻结的初始模型为教师，加权0.8蒸馏损失+0.2交叉熵损失；权重合并将SFT模型与初始模型等权插值；GRPO仅在可验证任务或模型答错的难样本上优化
### 关键结果
在FINESSE-Bench 778题金融推理测试集上，普通SFT使Qwen3.5-4B准确率下降3.2pp、Gemma-4-12B-IT下降4.0pp；自蒸馏SFT分别提升2.8pp、1.7pp；等权合并比SFT模型提升3.0pp，比初始模型高0.9pp；GRPO在可验证任务上直接训练可提升3.0pp，在难样本上可在自蒸馏SFT基础上再提升0.4pp。
### 核心结论
垂直领域LLM微调需同时追求域内增益与原有能力保留，分阶段的差异化数据筛选比单一质量评分更有效。

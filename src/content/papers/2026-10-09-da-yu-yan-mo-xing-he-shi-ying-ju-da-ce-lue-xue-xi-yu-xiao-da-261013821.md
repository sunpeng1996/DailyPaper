---
title: Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer
  Selection
title_zh: 大语言模型何时应拒答？策略学习与校准答案选择对比研究
authors:
- Juan Terven
- Diana-Margarita Córdova-Esparza
- Ruben Gomez
- Carlos Miranda Rocha
- Julio-Alejandro Romero-González
- Edgar Chavez-Urbiola
affiliations:
- CICATA Qro., Instituto Politécnico Nacional, México
- Facultad de Informática, Universidad Autónoma de Querétaro, México
arxiv_id: '2610.13821'
url: https://arxiv.org/abs/2610.13821
pdf_url: https://arxiv.org/pdf/2610.13821
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM校准 · 事实问答拒答
tags:
- Abstention
- Calibration
- LoRA
- Reinforcement_Learning
- Fact_QA
one_liner: 对比RL微调与独立答案选择器实现LLM拒答，验证同分布下后者更优
practical_value: '- 电商客服/导购Agent可复用独立答案选择器方案：固定生成模型，单独用LoRA训练轻量正确性判别器，比直接RL微调生成模型成本低（1.88h
  vs 23.68h 12轮训练），同分布下准确率更高、覆盖率更高

  - 事实类Query回答场景可复用校准流程：用Platt缩放对正确性得分做后校准，跨阈值泛化性更好，避免单一阈值过拟合

  - 跨域部署时需额外做校准适配：TriviaQA训练的选择器迁移到NQ数据集效用仍低于全拒答，说明这类判别方法跨域泛化性有限，业务场景换域必须重新校准甚至微调选择器'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在事实问答场景易产生幻觉，错误回答的代价远高于拒答，现有方案分为两类：一是微调生成模型直接学习回答/拒答策略，二是固定生成模型加独立选择器判断是否输出答案，二者的效果、成本对比缺乏受控实验验证，无法指导业务选型。

### 方法关键点
- 基座采用Qwen3-14B，对比两类方案：1）4种RL变体用LoRA微调生成模型，直接学习根据阈值输出回答/IDK；2）固定生成模型，训练独立LoRA选择器判别候选答案正确性，搭配Platt缩放校准得分后按阈值过滤
- 训练数据为2000条TriviaQA，训练阈值为0.6/0.75/0.9，测试用未见过的阈值0.65/0.85，同时跨域测试NQ-Open数据集，所有实验用3个种子消除随机性影响
- 评估指标兼顾效用（正确奖励+错误惩罚+拒答得0）、覆盖率、错误率，以及置信度得分的ROC AUC、Brier score

### 关键结果
- TriviaQA同分布场景：独立选择器较原生校准过滤器，平均覆盖率从20.2%提升至30.9%，输出答案的错误率从23.0%降至14.5%，平均效用提升75.6%；RL微调方案无统计显著增益，训练成本是选择器的12.6倍
- 跨域到NQ-Open：选择器相对原生过滤器仍有相对提升，但效用仍低于全拒答（0效用线），跨域泛化性不足

### 核心结论
同分布场景下，轻量独立答案选择器+校准的方案，比直接RL微调生成模型实现LLM拒答的成本更低、效果更稳定

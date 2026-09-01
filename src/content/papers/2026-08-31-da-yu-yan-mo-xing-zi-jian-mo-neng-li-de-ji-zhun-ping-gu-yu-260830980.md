---
title: Evaluating and Improving LLM Self-Modeling
title_zh: 大语言模型自建模能力的基准评估与训练优化方法
authors:
- Siqi Zeng
- Andre N. Assis
- Rowan Wang
affiliations:
- University of Illinois Urbana-Champaign
- Constellation
- Anthropic
arxiv_id: '2608.30980'
url: https://arxiv.org/abs/2608.30980
pdf_url: https://arxiv.org/pdf/2608.30980
published: '2026-08-31'
collected: '2026-09-01'
category: LLM
direction: LLM 自建模能力评估与训练
tags:
- Self-Modeling
- LLM Evaluation
- Reinforcement Learning
- Synthetic Data
- LoRA
one_liner: 构建多任务自建模评估基准，提出可扩展合成数据+RL训练框架提升LLM自建模能力
practical_value: '- 做Agent prompt调试时可借鉴自建模思路，让Agent预判prompt修改对输出的影响，大幅减少人工试错成本

  - 优化LLM4Rec模块时可复用「合成数据生成+LoRA+RL」轻量训练流程，提升模型对自身推荐行为的自解释能力，满足合规审核需求

  - 做LLM可解释性评估时可复用「行为ground truth对比虚拟预测」的评估范式，无需访问模型内部状态，落地成本极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM在预判自身行为（如prompt修改是否改变输出、回答置信度）时存在系统性偏差，缺乏统一评估基准与低成本优化方案，而自建模能力是Agent调试、可解释性审核、安全审计等落地场景的核心需求。
### 方法关键点
- 构建覆盖9类自建模任务的统一基准，支持二分类、多选、标量、自由文本等输出格式，所有ground truth均来自模型实际输入输出行为，无需访问内部状态
- 设计可扩展合成数据pipeline：单-turn场景基于开源数据集自动生成扰动，通过生成-验证-修订循环得到带行为标签的训练样本；多-turn场景基于BLOOM框架生成多轮交互样本
- 采用LoRA+RL轻量训练范式，奖励函数匹配评估指标，额外增加格式合规奖励，支持单任务/多任务训练
### 关键实验结果
在GSM8K、HumanEval、WildGuardTest、BBQ四个跨领域数据集上测试，18款主流模型的自建模技能最高仅为0.147（远低于1的理论上限）；多任务RL训练后，Llama-3.1-8B、Qwen3-8B、GPT-OSS-20B三款开源模型的自建模技能平均提升0.03-0.08，存在跨任务、跨场景（多转到单转）迁移性；跨模型迁移实验表明自建模能力主要来自通用行为规律学习，而非特权内省访问。
### 核心结论
LLM的自建模能力是可度量、可训练的行为能力，无需依赖内部状态访问即可实现显著提升

---
title: AI Persona Dialogue Pipeline; From Survey Report to Conversational Personas,
  Evaluated by LLMs and Experts
title_zh: 端到端AI人格对话流水线：从调研报告生成对话式人格并经大模型与专家评估
authors:
- Jinyoung Jeong
- Inhee Cho
- Byungju Kim
- Jiwon Baek
- Youngjae Yoo
affiliations:
- Hanyang University ERICA
- Seoul National University
- Hanyang University
- Independent Researcher
- Dankook University
arxiv_id: '2611.33736'
url: https://arxiv.org/abs/2611.33736
pdf_url: https://arxiv.org/pdf/2611.33736
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 人格构建与对话仿真
tags:
- LLM-persona
- dialogue-simulation
- LLM-as-judge
- persona-evaluation
- zero-shot-enactment
one_liner: 提出可跨人群复用的端到端对话式人格生成评估流水线，无需微调即可调用通用LLM实现人格扮演
practical_value: '- 构建用户仿真Agent时可直接复用「调研原始报告→LLM生成人格背景→零样本调用通用LLM扮演」的流水线，无需微调成本，适合快速搭建用户仿真环境

  - 做仿真效果验证时不要完全依赖LLM-as-judge结果，当前LLM评委与领域专家的评估一致性较差，核心场景必须补充人工校验

  - 电商用户调研环节可基于该方案生成小众/难触达人群（如银发族、下沉市场特定群体）的对话Agent，提前仿真测试商品话术、活动规则接受度，降低真人调研成本'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM驱动的人格对话仿真流水线均为单任务定制，切换目标人群时需重新设计人格生成、扮演、评估全链路，复用性极低，而小众/难触达人群的真人调研、对话仿真成本极高。
### 方法关键点
1. 可跨人群复用的端到端流水线：输入官方人群调研报告，由LLM自动生成结构化人格背景，直接调用通用LLM零样本扮演对应人格，无需任何微调；
2. 双层评估机制：先由3个LLM评委对8款候选仿真LLM做初筛，再由目标人群的领域专家做最终效果校验。
### 关键结果
在30个韩国独居老人人格场景测试中，专家评定生成的人格背景与对话真实度整体达标，核心缺陷为人格行为能力常高于背景设定；LLM评委与专家评估的一致性未达统计学要求，全套流水线、人格数据集、对话语料已开源。

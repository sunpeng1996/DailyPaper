---
title: 'Hy-MultiTurn: A Six-Dimensional Benchmark for Deep Multi-Turn Dialogue Understanding'
title_zh: Hy-MultiTurn：面向深层多轮对话理解的六维评测基准
authors:
- Eileen Ye
- Jiawen Tao
- Yaoming Li
- Chenxu Liu
- Wenhan Yu
- Yaxin Fan
- Xiaokun Yuan
- Mengzhou Wu
- Yanbing Jiang
- Maxm Pan
affiliations:
- Hunyuan Team, Tencent
- Peking University
arxiv_id: '2607.29196'
url: https://arxiv.org/abs/2607.29196
pdf_url: https://arxiv.org/pdf/2607.29196
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 多轮对话理解能力评测
tags:
- Multi-turn Dialogue
- Benchmark
- Agent Evaluation
- LLM Evaluation
- Chinese NLP
one_liner: 基于真实对话失效场景构建覆盖6项核心能力的中文长多轮对话理解评测基准并完成22个前沿模型评测
practical_value: '- 构建电商导购、客服类Agent的多轮交互评测集时，可直接复用本文提出的6个核心评测维度，覆盖绝大多数长交互场景的典型失效点

  - 迭代长多轮对话Agent时，可针对6个维度做定向优化，例如电商导购Agent重点优化约束记忆、指代消解、动作抑制（用户条件未满足时不执行下单等操作）

  - 上线前评测Agent性能时，可参考本文的任务构造方法，加入无关话题干扰、口语化表达等扰动项，提升评测结果的业务适配性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多轮对话评测基准多覆盖短交互场景，缺乏中文长多轮对话的细粒度能力评估，也无法清晰定位模型失效原因，难以支撑客服、导购类Agent的长交互能力评测需求。
### 方法关键点
从真实聊天机器人失效案例中抽象6类共性问题，对应设计6个可控评测维度：约束记忆、精确执行、约束综合、实体定位、动作抑制、指代消解；共构建209个可控评测任务，对话轮次覆盖12-76轮，额外加入无关话题干扰、口语化表达等扰动项提升任务难度。
### 关键结果
完成22个前沿大模型配置的评测，即使性能最强的GPT-5.5也仅能在41.1%的响应中满足全部要求，无模型在6个评测维度上均取得最优表现。

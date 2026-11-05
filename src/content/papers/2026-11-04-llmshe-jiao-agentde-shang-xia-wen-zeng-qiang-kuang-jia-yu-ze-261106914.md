---
title: A Framework for Context Enrichment and Selective Robustness in LLM Social Agents
title_zh: LLM社交Agent的上下文增强框架与选择性鲁棒性评估体系
authors:
- Mattia Greiche
- Reihaneh Rabbany
- Maximilian Puelma Touzel
affiliations:
- McGill University
- Mila - Quebec Artificial Intelligence Institute
arxiv_id: '2611.06914'
url: https://arxiv.org/abs/2611.06914
pdf_url: https://arxiv.org/pdf/2611.06914
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: LLM Agent 鲁棒性优化与评估
tags:
- LLM Agent
- Robustness
- Prompt Engineering
- Social Simulation
- Context Enrichment
one_liner: 提出可控上下文增强范式与选择性鲁棒性评估标准，优化LLM社交Agent行为稳定性
practical_value: '- 做LLM Agent prompt工程时可复用5级上下文拆分范式，优先添加描述性/规范性决策 grounding 信息，避免无效中性padding或无关背景，可将Agent行为表面敏感度最高降低87%

  - 评估Agent鲁棒性不要仅测不变性，需引入「选择性鲁棒性」校验：既要对同含义的prompt句式/格式变体不敏感，也要对业务相关输入变化做出符合预期的定向响应，避免把僵性误判为鲁棒性

  - 电商导购Agent、协商Agent上线前可参考本文测试范式，构造同语义多格式prompt、业务决策相关输入变体做批量校验，提前识别行为波动大的prompt版本，降低线上故障'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM社交Agent在模拟场景中行为对prompt语义不变的表层变体极度敏感，最高可导致决策概率波动76pp，现有鲁棒性评估仅要求输入不变时输出稳定，无法区分「真鲁棒」和「完全忽略上下文的僵性响应」，缺乏标准化的上下文优化和校验框架。

### 方法关键点
- 拆分5种可控上下文增强条件：最小上下文、中性padding、通用社交背景、描述性决策grounding、规范性决策grounding，所有增强条件仅替换prompt指定块，无其他变量叠加
- 提出「选择性鲁棒性」双维度评估：①表面敏感度：同语义不同格式（ prose/ bullets/ 键值表/ 改写 prose）下决策概率的平均绝对差，越低越稳定；②世界响应度：决策相关的真实上下文变化下，决策概率的定向差值，越高说明Agent对有效信息感知越强

### 关键实验结果
在类囚徒困境的医院物资分配场景下测试GPT-5.6 Sol和Terra两个模型，对比5种上下文条件：
- 采用描述性/规范性决策grounding时，Sol的表面敏感度从最高27.9pp降至3.7pp，世界响应度从最高51.1pp升至92pp，达到最优选择性鲁棒性
- Terra在相同grounding条件下，世界响应度从-2.1pp升至77.1pp，但表面敏感度仍有15pp左右，对部分改写prompt存在89.9pp的决策波动

### 核心结论
LLM Agent的鲁棒性必须是「选择性」的：对语义无关的表层变化不敏感，对语义相关的业务变化会做出符合预期的定向响应，两者缺一不可。

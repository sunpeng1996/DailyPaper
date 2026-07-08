---
title: 'Rating the Pitch, Not the Product: User Evaluations of LLMs Reflect Expectations
  More Than Performance'
title_zh: 用户对LLM的评价更多反映预期而非模型实际性能
authors:
- Robert Morabito
- Tyler McDonald
- Charitra Viswanath
- Angel Hsing-Chi Hwang
- Susanne Gaube
- Jad Kabbara
- Ali Emami
affiliations:
- Brock University
- Emory University
- University of Southern California
- University College London
- Massachusetts Institute of Technology
arxiv_id: '2607.05113'
url: https://arxiv.org/abs/2607.05113
pdf_url: https://arxiv.org/pdf/2607.05113
published: '2026-07-06'
collected: '2026-07-08'
category: Eval
direction: LLM用户评价影响因素研究
tags:
- LLM
- User Evaluation
- Expectation Management
- Human-AI Interaction
- Preference Data
one_liner: 通过162人对照实验证实LLM用户评价高度受前置预期影响，与实际任务表现相关性极低
practical_value: '- 上线AI导购/Agent类产品时，前端宣传需匹配模型实际能力，避免过度宣传拉高预期，导致实际使用时用户满意度降低

  - 收集用户对AI推荐、生成结果的反馈数据时，需控制前置预期变量，避免反馈失真误导模型迭代方向

  - 构建LLM偏好排序数据集时，需排除预期锚定效应干扰，否则公开排行榜排名无法真实反映模型性能

  - 对需要用户输入prompt的AI工具（如AI文案生成、AI选品助手），可通过预期引导调整用户prompt风格，提升交互效率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM的用户评价、偏好数据被广泛用于模型迭代、公开排行榜排序，但前置预期对评价结果的干扰程度尚未被量化验证。

### 方法关键点
开展162人对照实验：参与者使用6款不同LLM完成3项协作任务，任务前向用户传递匹配、高估、低估三类模型能力的前置信息，跟踪用户评价、交互行为、任务表现三类数据。

### 关键结果数字
1. 前置预期显著影响用户评价与交互：被高估模型的用户给出更高评分，使用更多指令式prompt；被低估模型的用户写出更长的协作式prompt
2. 人机协作产出质量仅与模型真实能力相关，与前置预期无关
3. 用户使用后的印象变化与任务表现无关（β=-0.01/0.11，均不显著），核心驱动为预期是否被满足（β=0.47/0.50，p<0.001）和用户使用自信度（β=0.47/0.36，p<0.001）
4. 用户评价对预期管理的敏感度至少与对模型本身性能的敏感度相当

---
title: Why Large Language Models and Humans Converge and Diverge in Evaluating Creativity
title_zh: 大语言模型与人类创意评估的趋同及分歧原因研究
authors:
- Pengzhao Lyu
- Yeun Joon Kim
- Hanlin Xiao
- Yingyue Luna Luan
affiliations:
- University of Cambridge Judge Business School
- University of Cambridge Institute of Metabolic Science
- University of Manchester Department of Computer Science
- University of Manchester Institute of Biotechnology
- University of Queensland School of Business
arxiv_id: '2607.22218'
url: https://arxiv.org/abs/2607.22218
pdf_url: https://arxiv.org/pdf/2607.22218
published: '2026-07-24'
collected: '2026-07-27'
category: Eval
direction: LLM评估 · 人-模型对齐边界探索
tags:
- LLM Evaluation
- Human Alignment
- Creativity Assessment
- Context-aware Evaluation
- Evaluation Standard
one_liner: 通过三组实验明确LLM与人类创意评估的对齐边界，给出LLM评估器的适用场景
practical_value: '- 电商/广告创意文案自动化评估场景，优先用LLM做创意新颖性维度初筛，可大幅降低人工审核成本，涉及市场适配性、合规性等上下文相关维度仍需人工复核

  - 搭建LLM自动评估链路时，优先选择评估标准覆盖维度更全的LLM作为评估器，可显著提升与人类评分的相关性

  - 需结合热点、品牌调性、用户特征的创意评估需求，必须通过RAG等方式给LLM注入对应上下文知识库，否则评估结果偏差极大'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM被广泛用作创意评估器，但与人类评估的对齐性表现波动大，缺乏明确的趋同/分歧原因解释，无法指导实际落地。
### 方法关键点
覆盖6款主流LLM，开展3组对照实验，拆解创意评估的多维度标准，对比不同维度、不同信息输入场景下LLM与人类评估的差异。
### 关键结果数字
1. 二者在新颖性维度对齐度最高，在包含社会、市场、声誉信息的上下文维度对齐度最差；
2. 1103条创意样本测试显示，LLM与人类评估呈中等相关，评估标准覆盖越广的LLM，区分人类认可创意的能力越强；
3. 1195条样本测试显示，上下文信息会显著改变人类评分，但对LLM评分几乎无影响。

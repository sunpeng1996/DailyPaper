---
title: 'PerSo: Investigating Facets of LLMs'' Social Intelligence in Real-World Persuasion
  Scenarios'
title_zh: PERSO：真实说服场景下大模型社交智能多维度评测基准
authors:
- Ali Zamani
- Soroush Esfahanian
- Erfan Shahabi
- Mohammad Taher Pilehvar
- Azadeh Shakery
- Yadollah Yaghoobzadeh
affiliations:
- University of Tehran
- Cardiff University
- Institute for Research in Fundamental Sciences (IPM)
- Tehran Institute for Advanced Studies
- Khatam University
arxiv_id: '2610.20548'
url: https://arxiv.org/abs/2610.20548
pdf_url: https://arxiv.org/pdf/2610.20548
published: '2026-10-14'
collected: '2026-10-16'
category: Eval
direction: LLM社交智能多维度评测基准
tags:
- Social Intelligence
- LLM Evaluation
- Persuasion Scenario
- Benchmark
- Theory of Mind
one_liner: 基于Reddit真实说服对话构建同时评测LLM认知与行为维度社交智能的基准PERSO
practical_value: '- 电商营销/客服说服类Agent的能力评测可复用这套框架：拆分认知（用户心理预判）+行为（话术效果判断）双维度，用真实业务对话构造MCQ评测集，比纯合成数据更贴合落地场景

  - 做说服类话术生成/推荐时可参考结论：情感预判是最难环节，针对高情感相关品类（美妆、奢侈品）的Agent可专门开启thinking模式提升情感识别准确率，其他信息明确的场景无需开启以节省算力

  - 业务话术A/B测试可复用文中LLM-in-the-loop标注流水线，自动生成选项+校验，降低人工标注成本，同时可通过用户转化+社区反馈双信号锚定有效话术，对齐真实用户偏好'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM社交智能评测大多依赖合成场景，且单独评估认知（心理状态推理）或行为（社交动作选择）能力，缺乏真实场景下的联合评测，而说服场景天然同时需要两种能力，对电商营销、客服Agent、多Agent协作等落地场景的能力评估有重要参考价值。

### 方法关键点
- 数据来源：从Reddit ChangeMyView社区抽取2024-2025年真实说服对话，筛选标准为同一发帖人下有两个说服者回复，一个获得delta（被说服标记）一个未获得，且成功回复点赞数更高，最终得到200条高质量对话样本
- 任务设计：①认知智能任务：要求模型仅基于发帖人原文+说服者回复，预测发帖人后续回复的信念、情绪、意图三类心理状态，为四选一MCQ题，用Gemini 2.5 Pro自动生成题目和干扰项，人工标注校验；②行为智能任务：要求模型从两个说服者回复中选出更能说服发帖人的那一个，用评分法规避位置偏差
- 评测设计：认知任务为预测未出现的回复状态，而非从已有文本抽取，更贴近真实业务的预判需求

### 关键实验
评测了Gemma、Qwen、DeepSeek、Claude、Gemini等十余个不同规模LLM，核心结果：①行为任务上最强模型Qwen-3.5-397B准确率76%，略超人类最佳水平75%；②认知任务上情绪维度是最大短板，最强模型Sonnet-4.6情绪准确率仅59%，比人类最佳低6个百分点，信念、意图准确率分别低2、4.5个百分点；③开启thinking模式仅对情绪预判有稳定提升，对其他维度无增益甚至会降效。

### 核心结论
LLM的认知与行为社交智能是可解离的两类能力，情绪预判是当前LLM社交智能的最大短板，推理模式仅在高模糊度任务上有价值。

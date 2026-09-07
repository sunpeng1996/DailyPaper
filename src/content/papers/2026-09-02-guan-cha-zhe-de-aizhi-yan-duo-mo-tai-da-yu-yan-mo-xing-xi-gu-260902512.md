---
title: 'Beauty is in the AI of the beholder: MLLMs systematically overrate facial
  attractiveness'
title_zh: 观察者的AI之眼：多模态大语言模型系统性高估人脸吸引力
authors:
- Santiago Grandas
- Juan Sebastian Cely-Acosta
- Mohit Mendiratta
- Shafee Hassan
- Macken Murphy
affiliations:
- QOVES Lab
- Qoves Inc., Wilmington, DE, United States
arxiv_id: '2609.02512'
url: https://arxiv.org/abs/2609.02512
pdf_url: https://arxiv.org/pdf/2609.02512
published: '2026-09-02'
collected: '2026-09-07'
category: Eval
direction: 多模态大模型评估 · 人脸吸引力判断
tags:
- MLLM
- Facial Attractiveness Rating
- Model Evaluation
- Human Alignment
- Multimodal
one_liner: 对比4款商用MLLM与人的颜值评分，证实MLLM系统性高估人脸吸引力，排序与人类判断强相关
practical_value: '- 美妆/医美类智能导购Agent、内容推荐场景使用商用MLLM做人脸颜值打分时，需新增偏移校准模块修正系统性高估偏差

  - 颜值相关排序类任务（如达人推荐、颜值内容排序）可直接复用MLLM输出的排序结果，无需额外校准排序逻辑

  - 多模态任务模型评估需同时覆盖排序相关性、绝对数值偏差两类指标，避免业务侧出现不符合用户预期的输出

  - 人脸相关多模态应用优先选择Claude/Gemini/GPT，避开Grok这类与人类审美一致性更低的模型'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
多模态大语言模型（MLLM）的颜值评估能力已被用户、企业、美容行业广泛应用，其判断是否符合人类真实审美缺乏系统验证。
### 方法
开展预注册探索性研究，对比2513名人类参与者与Claude、Gemini、GPT、Grok 4款主流商用MLLM的人脸吸引力评分差异。
### 关键结果
1. MLLM系统性给人脸打更高分，评分区间比人类更窄，绝对值与人类评分不匹配；
2. MLLM评分与人类判断强相关，可准确还原人脸吸引力的排序关系；
3. 仅年龄是人类与所有MLLM共有的颜值预测因子，不同模型对种族、性别的影响模式无统一规律；
4. 除Grok外，其余MLLM之间一致性高，Grok同时也是与人类评分一致性最低的模型。

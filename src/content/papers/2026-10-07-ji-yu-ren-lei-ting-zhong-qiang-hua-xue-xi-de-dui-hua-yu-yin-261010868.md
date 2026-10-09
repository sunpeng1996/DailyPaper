---
title: Conversational Voice Aesthetic Model with Reinforcement Learning from Human
  Listeners
title_zh: 基于人类听众强化学习的对话语音美感评估模型
authors:
- Xilin Jiang
- Shun Zhang
- Tejas Jayashankar
- Yinghao Aaron Li
- Osama Hanna
affiliations:
- Columbia University
- Meta Superintelligence Labs
arxiv_id: '2610.10868'
url: https://arxiv.org/abs/2610.10868
pdf_url: https://arxiv.org/pdf/2610.10868
published: '2026-10-07'
collected: '2026-10-09'
category: LLM
direction: 语音LLM · 人类偏好对齐
tags:
- Speech LLM
- RLHF
- Human Alignment
- Voice Aesthetics
- GRPO
one_liner: 提出融合监督微调与人类对齐RL的语音大模型CVAM，实现对话场景语音美感精准评估
practical_value: '- 针对主观感知类任务（如电商语音客服音色优化、短视频口播质量打分）可复用「SFT+基于人类标注的相对RL」对齐框架，解决无明确ground
  truth的标注难题

  - 处理主观属性标注时，单样本采集多份人类标注再做组相对偏好优化，比单标注训练的模型更贴合群体感知，可复用在广告文案、商品评价的主观质量打分场景

  - 多维度分类属性+自然语言描述联合训练的范式，可迁移到UGC、直播语音内容的多维度质量审核与排序场景'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
对话语音交互场景下，语音美感的emotion、表达风格等属性高度主观，缺乏明确ground truth，现有语音模型难以匹配人类感知偏好，无法满足对话Agent、语音合成等场景的评估需求。
### 方法关键点
1. 基于CANDOR语料构建3k条真实/合成语音样本库，每条样本采集约10份人类标注，覆盖性别、pitch、语速、emotion、表达等9类属性；
2. 先基于合成的美感描述与标签做SFT，再采用Group Relative Policy Optimization（GRPO）基于人类判断做偏好对齐。
### 关键结果数字
CVAM与人类听众的一致性优于Gemini 3.1 Pro及开源语音LLM，且一致性超过单个人类标注者与其余标注者的平均一致性。

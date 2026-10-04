---
title: 'Beyond Text: LLM-Based Dimensional Emotion Evaluation in Multimodal Dialogue'
title_zh: 超越文本：多模态对话中基于大语言模型的维度情绪评估
authors:
- Yutong Hu
- Jinho Choi
affiliations:
- Emory University
arxiv_id: '2609.39072'
url: https://arxiv.org/abs/2609.39072
pdf_url: https://arxiv.org/pdf/2609.39072
published: '2026-09-30'
collected: '2026-10-04'
category: LLM
direction: 多模态对话 · LLM维度情绪评估
tags:
- LLM
- Multimodal
- Emotion Recognition
- LoRA
- IEMOCAP
one_liner: 提出融合音频文本描述的LLM框架，在IEMOCAP上刷新维度情绪评估SOTA
practical_value: '- 智能客服Agent情绪识别场景可复用「非文本特征转自然语言描述喂给LLM」的范式，无需适配多模态大模型，大幅降低落地成本

  - 垂类小模型任务优先选择LoRA微调而非大模型prompt工程，电商客服、内容互动等情绪识别场景可在更低成本下取得更优效果

  - 非文本特征转文本描述的融合思路可迁移到用户行为、点击等结构化特征的prompt改造，降低LLM适配业务特征的门槛'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
对话情绪识别现有研究多聚焦离散分类任务，基于LLM的多模态连续维度（Valence-Arousal-Dominance，VAD）情绪评估领域存在空白，且缺乏适配LLM输入要求的多模态特征融合方案。
### 方法关键点
遵循SpeechCueLLM范式将声学特征转化为自然语言描述，融合对话文本上下文输入LLM，同时完成离散情绪分类、VAD三维度连续评估两类任务；对比测试LLaMA、GPT、Qwen三个系列共6个模型在zero-shot prompting、few-shot prompting、LoRA微调三种设置下的表现。
### 关键结果数字
1. LoRA微调的LLaMA模型效果大幅优于prompt工程优化的更大参数GPT模型，最优模型Valence维度CCC达0.7822，刷新IEMOCAP数据集SOTA
2. 小模型引入语音文本描述可提升3.5~3.6加权F1，大模型该增益不显著
3. VAD三维度的效果差异和数据集标注一致性层级完全匹配

---
title: 'Real-TurnTurk: A Multimodal Turkish Corpus for Turn-Taking Prediction'
title_zh: Real-TurnTurk：面向对话轮次切换预测的多模态土耳其语语料库
authors:
- Ahmet Tuğrul Bayrak
- Fatma Nur Korkmaz
- Bekir Berker Türker
- Mustafa Sertaç Türkel
- Alper Kaplan
affiliations:
- Ata Technology Platforms
- Luxembourg National Research Fund
arxiv_id: '2608.22071'
url: https://arxiv.org/abs/2608.22071
pdf_url: https://arxiv.org/pdf/2608.22071
published: '2026-08-21'
collected: '2026-08-30'
category: Other
direction: 多模态对话语料 · 轮次切换预测
tags:
- multimodal corpus
- turn-taking prediction
- genetic algorithm
- rule optimization
- conversational AI
one_liner: 发布首个土耳其语自然多模态对话语料库，提出遗传算法优化的可解释轮次切换预测框架
practical_value: '- 开发电商智能客服对话Agent时，可参考其多模态特征（语音、语义、视觉表情）融合的轮次切换规则构建思路，替代单一静默检测逻辑，降低用户等待时长

  - 可复用遗传算法优化AND-OR混合规则的方案，实现可解释的对话状态判断逻辑，便于业务规则迭代和问题排查

  - 搭建小语种多模态对话数据集时，可参考其同步音视频采集、分说话人音频拆分、时间对齐转录的标注规范'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
同步自然对话系统的轮次切换建模仍存在较大挑战，现有多模态轮次预测研究多面向主流语言，缺少面向土耳其语的自然对话语料支撑，无法覆盖小语种对话动力学特性。

### 方法关键点
1. 构建Real-TurnTurk多模态土耳其语对话语料库，包含无脚本双人交互的同步正面视频、分说话人独立音频通道（可定位重叠语音归属）、时间对齐转录文本；
2. 将轮次切换预测建模为二分类任务，采用遗传算法优化视觉、声学、语言学三类特征衍生的可解释决策规则，通过混合AND-OR规则表达轮次切换前的多信号组合模式。

### 结果
已完成语料库构建与可解释预测框架落地，填补了土耳其语多模态对话轮次预测领域的基准数据空白。

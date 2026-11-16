---
title: 'Contagious Fingerprints: When LLMs Inherit Another Model''s Identity'
title_zh: 传染式指纹：大语言模型会继承其他模型的身份特征
authors:
- Zailong Tian
affiliations:
- Nanyang Technological University
arxiv_id: '2611.18104'
url: https://arxiv.org/abs/2611.18104
pdf_url: https://arxiv.org/pdf/2611.18104
published: '2026-11-13'
collected: '2026-11-16'
category: LLM
direction: LLM身份审计 · 多轮对话指纹检测
tags:
- LLM Fingerprint
- Model Audit
- Multi-turn Conversation
- API Fraud Detection
- Reference Sampling
one_liner: 发现多轮对话中LLM身份指纹可传染，提出Lineup方法检测API服务商的模型代换欺诈
practical_value: '- 对于调用第三方LLM搭建电商导购Agent、推荐文案生成系统的场景，可复用Lineup方法检测服务商是否偷偷替换低成本模型，避免业务效果下降

  - 多轮对话中LLM会模仿上文风格的结论可用于优化推荐文案生成：用目标风格的历史上下文引导LLM输出符合要求的话术，降低LoRA微调成本

  - 做LLM生成内容溯源审计时，不能用单轮无上下文的指纹库，要引入同上下文的参考样本比对，大幅降低误判率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM身份审计方法默认指纹是模型固有属性，基于无上下文的参考样本比对，完全无法检测API服务商先用付费模型承接首句、后续偷偷切换低成本模型的欺诈行为。
### 方法关键点
1. 验证指纹传染的核心原因是模型会模仿对话历史的风格，导致自身指纹发生偏移；2. 提出Lineup检测方法，针对相同对话历史从宣称的正版模型采样参考回复，通过待检测回复在参考样本中的排序判断是否被替换，无需拟合阈值或依赖log概率。
### 关键结果
传统分类器检测代换模型的准确率从0.97降至0.72（DeepSeek替换Claude Sonnet）、0.87降至0.54（同厂商降级为Haiku）；Lineup方法假阳性率仅0.056，4轮对话后跨6组代换对的检测率达0.81。

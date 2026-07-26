---
title: Toward Generalizable Cognitive Impairment Detection with Speech-Based Multimodal
  Large Language Models
title_zh: 基于语音多模态大模型的高泛化性认知障碍检测框架
authors:
- Yingchao Huang
- Xin Wang
- Yuhan Su
- Shanshan Yao
affiliations:
- Saskatchewan Polytechnic
- Hebei University
- University of Alberta
arxiv_id: '2607.21496'
url: https://arxiv.org/abs/2607.21496
pdf_url: https://arxiv.org/pdf/2607.21496
published: '2026-07-23'
collected: '2026-07-26'
category: Multimodal
direction: 多模态大模型 · 隐私友好跨域分类
tags:
- Multimodal LLM
- Speech Feature
- Feature Fusion
- Privacy Preserving
- Classification
one_liner: 基于开源LLM融合语音声学与转写文本特征，实现隐私友好的高准确率跨数据集认知障碍检测
practical_value: '- 多模态特征融合轻量方案：无需对齐原始模态数据，仅拼接各模态预训练embedding做下游分类，可快速复用到电商多模态内容（图文/音视频）分类、风控等场景

  - 隐私友好的特征处理范式：仅使用提取后的特征向量训练，不访问原始敏感数据，可借鉴到涉及用户敏感数据（语音/聊天记录）的用户画像建模任务

  - 跨域泛化优化思路：基于开源LLM通用表征能力提升跨数据集泛化性，可复用在冷启动场景下的跨域推荐排序任务中'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
认知障碍早筛是公共卫生重点需求，现有基于语音的检测方案泛化性弱、易泄露用户隐私，单模态表征无法覆盖认知衰退对应的全部语言、声学标记。
### 方法关键点
1. 基于开源LLM搭建多模态融合框架，分别从原始语音提取声学embedding、从自动转写文本生成文本embedding
2. 直接拼接两类模态专属特征向量输入下游分类器，全程无需访问原始敏感用户数据，隐私友好
3. 无需修改LLM主干结构，部署适配成本低
### 关键结果
在ADReSS20、ADReSSo21基准数据集上认知障碍分类准确率达92.4%，显著优于单模态基线，跨数据集泛化性达到SOTA水平。

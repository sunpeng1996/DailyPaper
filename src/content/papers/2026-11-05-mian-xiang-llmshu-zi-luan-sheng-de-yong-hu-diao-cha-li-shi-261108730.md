---
title: 'Structuring Survey Histories for LLM Digital Twins: A Controlled Study of
  Background, Decision Procedure, and Evaluation Profiles'
title_zh: 面向LLM数字孪生的用户调查历史结构化BDE框架研究
authors:
- Iris Ye
- Tianze Deng
- Ozan Candogan
affiliations:
- University of Chicago Booth School of Business
arxiv_id: '2611.08730'
url: https://arxiv.org/abs/2611.08730
pdf_url: https://arxiv.org/pdf/2611.08730
published: '2026-11-05'
collected: '2026-11-09'
category: Agent
direction: Agent 数字孪生用户画像构建
tags:
- Digital Twin
- User Profiling
- Persona Representation
- LLM Agent
- Behavioral Simulation
one_liner: 提出背景/决策过程/评估三分段的BDE用户画像结构，提升LLM数字孪生预测准确率
practical_value: '- 电商/推荐场景用户画像可参考BDE三分法，优先抽取用户偏好、预算、支付意愿等Evaluation类内容，对定价、转化类预测增益最大

  - 结构化用户画像无需做过度深度推理，直接从行为/问卷提取的显性信息已足够，额外推理不会带来统计显著的效果提升

  - 同长度下结构化分类的画像是比自由文本摘要更优的选择，尤其是商品定价、个性化推荐场景效果更明显'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM数字孪生需要基于用户历史应答预测其在新场景的决策，现有研究发现用户历史的压缩不必然降低预测准确率，说明信息组织方式比信息量更重要，但缺乏可落地的结构化用户画像构建框架。

### 方法关键点
- 提出BDE固定结构，将用户调查历史拆分为三类：Background（身份、认知、信念）、Decision procedure（不确定场景下的推理方式、认知风格）、Evaluation（偏好、预算、支付意愿等价值判断）
- 设计3级提取深度，V1仅提取显性陈述信息，V2支持人口属性、跨量表推理，V3允许更宽泛的推理及自报告可信度评估
- 设置多组对照：同长度自由文本画像、去头部标签BDE画像，排除长度、压缩带来的效果干扰

### 关键实验结果
- 基于Twin-2K-500数据集的100个用户样本，覆盖17类任务、120个标注项（80个认知偏差项+40个定价项），baseline为原始调查文本、同长度自由文本摘要
- V3 BDE相对原始文本，在gpt-5.4-nano上整体准确率提升1.27pp（p<0.01），在gpt-5.4-mini上提升1.19pp（p<0.001），定价类任务增益分别达1.85pp、2.10pp
- 相对同长度自由文本，BDE在定价任务上分别提升2.15pp（nano，p<0.01）、1.38pp（mini，p<0.05）
- 消融实验显示，增加Evaluation模块是效果增益的核心来源，相对仅bg+dp的画像，整体提升1.22-1.44pp，定价提升2.60-3.40pp（p<0.001），而提升提取深度无统计显著增益

### 核心结论
用户画像的效果提升核心来自有效信息的分类组织，而非信息量多少或过度深度推理。

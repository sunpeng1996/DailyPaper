---
title: 'Personalization as Inverse Planning: Learning Latent Design Intents for Agentic
  Slide Generation via Structural Denoising'
title_zh: 个性化即逆规划：基于结构去噪的智能体幻灯片生成隐式意图学习
authors:
- Tianci Liu
- Zihan Dong
- Linjun Zhang
- Haoyu Wang
- jing Gao
- Emre Kiciman
- Ranveer Chandra
- Wei-Ting Chen
affiliations:
- Purdue University
- Rutgers University
- University at Albany
- Microsoft
arxiv_id: '2607.00407'
url: https://arxiv.org/abs/2607.00407
pdf_url: https://arxiv.org/pdf/2607.00407
published: '2026-06-30'
collected: '2026-07-03'
category: Agent
direction: Agent 多智能体协作个性化视觉生成
tags:
- MultiAgent
- ReinforcementLearning
- StructuralDenoising
- InversePlanning
- PersonalizedGeneration
one_liner: 通过结构去噪自监督训练双智能体，实现无模板/长指令的页面级幻灯片个性化生成
practical_value: '- 可复用结构化去噪自监督范式：对有离散结构化属性的生成任务（如电商海报/商品详情页个性化排版），可通过人工构造属性扰动的自监督信号替代昂贵人工标注，大幅降低训练成本

  - 双智能体解耦训练架构：将意图规划与反馈判别拆分为两个独立智能体，用RL分别优化，可避免黑盒渲染器梯度不可导问题，同时降低策略梯度方差，适合所有下游渲染逻辑不可控的生成类业务场景

  - 少样本偏好适配方法：仅需少量用户参考样本即可推理隐式设计意图，可迁移到电商店铺装修、品牌物料生成等需要对齐用户个性化风格的场景，无需为每个用户单独微调大模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前智能体幻灯片生成方案依赖预定义模板或冗长用户指令，无法捕捉用户隐式页面级设计意图，页面级个性化（PSP）问题难以解决；同时传统优化方案因黑盒渲染器不可导、像素级相似度无法衡量结构化设计质量，端到端优化不可行。

### 方法关键点
- 将PSP建模为逆规划问题，把设计意图作为隐变量，解耦意图规划与下游黑盒渲染器，意图可跨渲染器复用
- 提出Spire框架，构造结构去噪自监督信号：对金标幻灯片的布局、视觉层级、样式三类离散属性做随机扰动，生成带噪样本与对应的标注差异列表，无需人工标注
- 双智能体分工：Critic智能体基于带噪样本与参考样本输出可落地修改反馈，用DAPO RL训练以最大化反馈准确率；Planner智能体基于用户指令、参考样本与Critic反馈输出可执行设计计划，同样用RL训练以最大化计划与金标样本的匹配度
- 理论证明该结构去噪目标是PSP任务的一致代理目标，双智能体架构可严格降低RL策略梯度方差

### 关键实验
在Zenodo10k、SlideBench数据集上测试，对比AutoPresent、PPTAgent、GPT-4o-mini基线，仅用7B级小模型的Spire在OOD场景下VLM评判平均分达0.7333，远超GPT-4o-mini基线的0.5338，同时视觉相似度达0.6870，仅略低于GPT基线的0.7433。

### 最值得记住的一句话
对于需要捕捉用户隐式偏好的结构化生成任务，基于离散属性扰动的自监督信号+双智能体解耦RL优化，可在小模型上实现远超通用大模型的个性化效果。

---
title: Learning to Think and Explore in 3D World
title_zh: 面向3D空间的视觉语言模型主动思考与探索方法
authors:
- Yijiang Li
- Bingyang Wang
- Nuno Vasconcelos
affiliations:
- University of California San Diego
- Georgia Institute of Technology
arxiv_id: '2610.21783'
url: https://arxiv.org/abs/2610.21783
pdf_url: https://arxiv.org/pdf/2610.21783
published: '2026-10-14'
collected: '2026-10-19'
category: Agent
direction: 多模态Agent · 3D空间主动探索
tags:
- VLM
- Reinforcement Learning
- 3D Reasoning
- Active Exploration
- Multimodal Agent
one_liner: 基于轨迹微调+结果导向RL的多模态Agent，无需预输入3D表征即可自主探索3D空间完成问答
practical_value: '- 3D商品导购多模态Agent可复用探索策略：用户咨询时自主调整商品视图解答遮挡、尺寸对比类问题，无需预设全量视图输入，降低前端加载成本

  - 交互类Agent训练可复用结果导向RL框架：仅用最终任务正确性做奖励，无需标注最优探索路径，大幅降低标注成本

  - 自适应探索逻辑可迁移到搜索推荐场景：初始信息可直接回答的请求不做额外召回/补全，信息不足的请求主动触发多轮交互/多源检索，平衡效率与效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有3D视觉语言模型依赖预输入的多视图、3D表征等全量观测，无法模拟人类主动交互探索的行为，难以适配真实开放3D交互场景。
### 方法关键点
1. 保留VLM原生单图编码范式，不预输入3D结构/多视图数据，将3D环境作为交互对象，通过移动、转向等动作获取新视角观测；
2. 先通过轨迹监督微调做初始化，再采用仅基于最终答案正确性的RL训练，不标注最优探索路径，让模型自主学习高效探索策略。
### 关键结果
6个3D基准平均准确率达53.2%，较基线Qwen提升22%，超越Gemini 3.6 Flash；比现有开源3D方法少用50~70%输入帧效果仍更优；未知域泛化较监督初始化提升5.9%，需大量探索的问题上增益达16.3%。

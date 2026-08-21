---
title: 'DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based
  Image Editing'
title_zh: DARS：面向指令驱动图像编辑的双层信用分配强化学习框架
authors:
- Haoxiang Cao
- Jiajiong Cao
- Xuanpu Zhang
- Changqian Yu
- Chaoqun Wang
affiliations:
- South China Normal University
- KlingAI Research
arxiv_id: '2608.20161'
url: https://arxiv.org/abs/2608.20161
pdf_url: https://arxiv.org/pdf/2608.20161
published: '2026-08-20'
collected: '2026-08-21'
category: Multimodal
direction: 多模态指令图像编辑 · RL信用分配
tags:
- Reinforcement Learning
- Credit Assignment
- Vision-Language Model
- Diffusion Model
- Image Editing
one_liner: 提出双层信用分配RL框架DARS，解决指令图像编辑两阶段pipeline的错误归因难题
practical_value: '- 电商商品图指令编辑场景可直接复用该双层归因框架，解决VLM规划+扩散生成pipeline训练效率低的问题

  - 多模块串联生成系统（如Agent工具调用、生成式文案配图pipeline）可借鉴跨模块信用分配思路拆分错误责任

  - 结构化推理输出+前缀门控奖励方法可迁移到大模型推理trace细粒度监督场景，降低全局反馈训练成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有指令驱动图像编辑采用VLM规划+扩散渲染两阶段pipeline，仅靠最终图像奖励训练效率极低，既无法区分错误归属规划还是渲染模块，也难以定位规划侧自由推理轨迹中的具体错误点。
### 方法关键点
1. 跨模块层：通过多规划多渲染采样，计算规划间、规划内奖励方差实现软模块路由，同时用采样平均奖励生成自适应学习课程；
2. 规划模块内部：采用四字段结构化推理输出，实现前缀门控奖励与token级优势重加权，将全局结果反馈转化为局部监督信号。
### 关键结果
在5个基准测试集上性能优于相同骨干、数据、奖励模型、采样预算的Joint RL基线，推理密集型编辑任务提升幅度最大。

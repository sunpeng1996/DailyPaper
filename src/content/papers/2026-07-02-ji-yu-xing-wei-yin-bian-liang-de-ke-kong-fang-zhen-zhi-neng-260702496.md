---
title: Controllable Sim Agents with Behavior Latents
title_zh: 基于行为隐变量的可控仿真智能体框架
authors:
- Juanwu Lu
- Junyu Zhu
- Ziran Wang
affiliations:
- Purdue University
- University of Tokyo
arxiv_id: '2607.02496'
url: https://arxiv.org/abs/2607.02496
pdf_url: https://arxiv.org/pdf/2607.02496
published: '2026-07-02'
collected: '2026-07-04'
category: Agent
direction: 可控仿真智能体 · 行为隐变量调控
tags:
- Controllable Agent
- Simulation
- Generative Model
- Variational Inference
- Eligibility Gate
one_liner: 提出基于行为隐变量的可控仿真智能体CNeVA，实现多维度可解释的行为调控
practical_value: '- 做可控生成类Agent时，可借鉴封闭形式共轭变分更新方法从通道级收益推断行为隐变量，实现多维度可解释的行为调控

  - 应对奖励信号稀疏问题时，可复用soft eligibility gates设计，用平滑指数衰减替代硬二分类阈值，保留近阈值样本的梯度信号

  - 采用classifier-free guidance做生成任务时，可参考混合通道掩码课程训练策略，平衡生成结果的可控性与真实度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有仿真智能体要么真实度不足要么缺乏可解释的可控性，无法满足变量隔离、边缘案例复现等测试需求，同时奖励信号稀疏易导致梯度消失。
### 方法关键点
1. 提出CNeVA可控仿真智能体框架，通过封闭形式共轭变分更新从通道级折扣收益推断每个智能体的高斯行为隐变量；
2. 整流流轨迹生成器采用混合通道掩码课程训练，支持无分类器引导的可控生成；
3. 提出soft eligibility gates，用平滑指数衰减替代硬二值阈值，保留近阈值智能体的梯度信号。
### 关键结果
在Waymo Open Motion数据集上真实度达到SOTA基准水平，同时具备现有高排名模仿模型缺失的通道级可控性；速度、加速度维度调控输出单调无奖励作弊，引入软资格门后安全维度可控性显著提升，同时实现可调控的地图合规性。

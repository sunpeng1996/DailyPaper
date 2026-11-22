---
title: 'Inhabitant: An Agent Framework for Long-Horizon Human-Scene Interaction with
  Spatial Control and Quantitative Feedback'
title_zh: Inhabitant：支持空间控制与量化反馈的长时序人机交互Agent框架
authors:
- Yao Zhang
- Zhuchenyang Liu
- Yu Xiao
affiliations:
- Aalto University
arxiv_id: '2611.25005'
url: https://arxiv.org/abs/2611.25005
pdf_url: https://arxiv.org/pdf/2611.25005
published: '2026-11-17'
collected: '2026-11-22'
category: Agent
direction: 具身Agent · 长时序交互优化
tags:
- Agent
- EmbodiedAI
- SpatialControl
- QuantitativeFeedback
- LLMPlanning
- Benchmark
one_liner: 提出免训练长时序3D场景人机交互Agent框架，配套75项家居任务基准，最高完成率98.7%
practical_value: '- 布局线下导购Agent、AR家居布置交互Agent时，可复用「空间控制参数化+执行偏差量化反馈」的闭环逻辑，解决多步连续动作执行偏差问题

  - 多步任务的Agent规划可借鉴免训练的参数化动作定义方式，无需全量微调LLM即可适配复杂序列任务，降低落地成本

  - 做Agent业务能力评测时，可参考链式多目标任务基准的构建思路，更贴合真实场景下的长流程需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有长时序人机交互LLM Agent缺乏运动空间控制能力与执行结果的量化反馈，在多步日常交互任务中序列完成率极低，无法适配真实场景落地需求。
### 方法关键点
1. 推出免训练的Inhabitant Agent框架，将每个动作拆解为位置、路径、姿态三类可量化的控制参数；
2. 新增执行偏差度量模块，实时对比实际执行结果与预期意图的差异，自动修正控制参数实现闭环迭代；
3. 构建Inhabit基准，覆盖31种公寓家具布局下的75项链式多目标家居交互任务。
### 关键结果
搭配Claude Opus 5.5时任务完成率达98.7%，使用Claude Sonnet 5.5、Gemini 4 Argon分别达93.3%、82.7%；消融实验证实缺失空间控制时大部分任务失败，缺失量化反馈会显著降低动作精度。

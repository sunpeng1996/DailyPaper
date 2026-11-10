---
title: Toward the Era of Agentic Embodied Intelligence
title_zh: 迈向具身智能体时代：A2-MEAS多智能体具身控制框架
authors:
- Chao Liang
- Ke Chen
- Fengxiaoxiao Li
- Shibo Huang
- Yufeng Sun
- Zhaokai Yin
- Jianhuan Lai
- Haozhe Feng
- Chenghuan Jia
- Zhipeng Zhang
affiliations:
- 上海交通大学人工智能学院AutoLab
- Anyverse Dynamics Research Lab
arxiv_id: '2611.09124'
url: https://arxiv.org/abs/2611.09124
pdf_url: https://arxiv.org/pdf/2611.09124
published: '2026-11-05'
collected: '2026-11-10'
category: Agent
direction: 具身智能 · 多智能体协作控制
tags:
- EmbodiedAI
- MultiAgent
- VLA
- RobotControl
- FaultRecovery
one_liner: 提出以代码为扩展接口的多智能体具身框架A2-MEAS，大幅提升长时序机器人自主控制与故障恢复性能
practical_value: '- 多智能体解耦架构可复用：任务调度、感知诊断、执行模块分离的设计，可直接迁移到推荐/广告系统的链路故障自修复、大促流量动态调优场景，无需修改核心模型权重即可叠加故障修正逻辑

  - 轻量Adapter修正机制可借鉴：冻结主干大模型权重，仅用小参数Adapter承载修正知识，类似推荐系统冷启/个性化增量微调，训练成本低、上线速度快，无需全量重训主模型

  - 偏差样本挖掘范式可迁移：从已有的成功演示中挖掘基模型的预测偏差构造监督样本，无需真实故障数据即可训练故障恢复能力，可用于推荐系统bad case自动修复模型的训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型引导机器人行动的方案，难以同时兼顾高效连续控制和突发故障的快速恢复，长时序自主执行成功率低，训练和推理效率也不足以支撑规模化落地。

### 方法关键点
- 提出A2-MEAS多智能体框架，分为三大模块：MetaBrain负责任务进度监控、故障诊断与修复指令生成；诊断智能体负责感知、时空、交互层面的物理证据采集；A2-WLA动作模型负责连续控制指令生成
- 核心设计为**code as scaling interface**：将修复指令、空间证据、执行历史、基模型动作提案编码为统一correction code，通过轻量残差Adapter微调动作模型的隐层状态，全程冻结主干模型权重
- A2-WLA动作模型融合运动感知历史编码器、多视角潜变量世界模型、18层Transformer动作专家，支持长时序动作预测与进度估计

### 关键结果
- 在BEHAVIOR 2026 50任务子集上，A2-WLA单模型Q-score达0.5755，是2025年竞赛冠军的2.21倍；完整A2-MEAS系统在100任务全集上Q-score达0.6411，整任务成功率45.40%
- 实机测试中，故障修复环节将咖啡制作滤布放置步骤的失败后完成率从14%提升至94%、从8%提升至82%；训练吞吐量达427.1样本/秒，是π0.5参考实现的4.03倍

最值得记住的一句话：将大模型的推理能力与轻量化专用模型的执行效率结合，通过统一的可扩展接口实现跨模块知识互通，是兼顾通用性与落地性的智能系统设计核心思路

---
title: 'Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World
  Model Predictive Control'
title_zh: 时序距离JEPA：面向潜变量世界模型预测控制的规划感知表示学习
authors:
- Jiaxin Bai
- Jiaxuan Xiong
affiliations:
- Hong Kong Baptist University
arxiv_id: '2607.25337'
url: https://arxiv.org/abs/2607.25337
pdf_url: https://arxiv.org/pdf/2607.25337
published: '2026-07-27'
collected: '2026-07-30'
category: Agent
direction: Agent 世界模型表示学习与规划优化
tags:
- JEPA
- World Model
- Representation Learning
- Offline Learning
- Planning
- Predictive Control
one_liner: 从无奖励离线轨迹挖掘定向时序代价，缩小JEPA世界模型规划器的训练-规划性能gap
practical_value: '- 针对用户行为序列等轨迹类表示学习任务，可复用同轨迹时序正负对+跨轨迹负例的构造方法，无需额外标注即可强化表示的时序进度感知能力

  - Agent多步决策/推荐系统长序列决策场景下，可将推理时的代价函数与训练目标联合设计，有效缩小训练与线上推理的性能gap

  - 离线日志驱动的表示学习任务，可加入和推理horizon匹配的rollout一致性约束，提升长序列预测/规划的稳定性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统JEPA训练聚焦短程潜变量预测，规划时依赖的欧氏距离是表示学习的副产品而非从日志挖掘的进度代价，存在明显训练-规划gap，无法适配多步规划的未来排序需求。
### 方法关键点
基于LeWM的编码器-预测器骨干，从无奖励轨迹中挖掘定向时序代价：1）用同轨迹步序构造正样本对，跨轨迹对作为启发式负样本；2）加入和规划horizon匹配的rollout一致性项；3）挖掘的监督信号既可以作为拓扑进度场景的部署规划代价，也可以作为表示信号优化欧氏规划效果。
### 关键结果
锁定评估下，挖掘的代价将Two-Room任务成功率从LeWM的97.4%提升至100%；同checkpoint下的欧氏规划将OGB-Cube指标较LeWM提升14.2个点，Push-T任务效果也有提升；在所有测试环境上性能均匹配或超过LeWM、RC-aux基线。

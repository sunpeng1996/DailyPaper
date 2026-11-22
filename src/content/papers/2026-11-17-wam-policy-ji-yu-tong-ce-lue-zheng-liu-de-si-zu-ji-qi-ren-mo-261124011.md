---
title: 'WAM-Policy: World Action Models with On-Policy Distillation for Quadrupedal
  Loco-Manipulation'
title_zh: WAM-Policy：基于同策略蒸馏的四足机器人运动操作世界动作模型
authors:
- Junlin Long
- Xu Deng
- Yiran Wang
- Yue Yang
- Yang Zhao
- Zeyu Zhang
affiliations:
- Australian Centre for Robotics, USYD
- UNSW Sydney
- Maincode
- La Trobe University
arxiv_id: '2611.24011'
url: https://arxiv.org/abs/2611.24011
pdf_url: https://arxiv.org/pdf/2611.24011
published: '2026-11-17'
collected: '2026-11-22'
category: Other
direction: 四足机器人 · 语言条件运动操作策略
tags:
- On-Policy Distillation
- World Model
- Reinforcement Learning
- Robot Manipulation
- Knowledge Distillation
one_liner: 通过两阶段跨形态适配与多教师同策略蒸馏，实现高效语言驱动的四足机器人运动操作策略
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
无臂四足机器人可通过单前腿完成运动操作，但现有策略不支持语言指令；现有面向机械臂的语言条件世界动作模型（WAM）采样速度慢，无法直接适配四足形态。

### 方法关键点
分两阶段完成策略迁移与优化：1. 跨形态策略适配加速：将以机械臂为中心的WAM适配到四足场景，通过on-policy自蒸馏（OPSD）将迁移后的教师策略蒸馏为仅需1帧视频、2步动作推理的轻量学生模型；2. 任务专项优化融合：通过RL微调教师模型得到专项策略，再通过多教师on-policy蒸馏（M-OPD）将多个慢速专项教师合并为单一小样本学生模型。

### 关键结果数字
在QLM-Bench 10项仿真任务上，初始迁移策略准确率77.0%，OPSD学生模型保持76.7%准确率的同时采样速度提升14倍；经RL微调+M-OPD后准确率提升至85.0%，已在Unitree Go2 Air实体机器人完成部署。

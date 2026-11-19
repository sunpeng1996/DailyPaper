---
title: 'Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player
  Co-Development'
title_zh: Game2Player：环境-玩家协同开发的视觉Agent游戏体验扩展框架
authors:
- Xirui Jiang
- Yuxi Chen
- Rui Yang
- Feng Luo
- Pengcheng Wang
- Bingxuan Li
- Zihao Zhao
- Yushan Li
- Han Wang
- Manling Li
affiliations:
- UIUC
- UC Santa Barbara
- Georgia Tech
- Northwestern University
- IBM
arxiv_id: '2611.24154'
url: https://arxiv.org/abs/2611.24154
pdf_url: https://arxiv.org/pdf/2611.24154
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: 视觉Agent训练 · 环境智能体协同迭代
tags:
- Visual Agent
- VLM
- Trajectory Collection
- SFT
- Agent Benchmark
one_liner: 提出环境-玩家协同迭代框架，低成本规模化生成可验证的游戏Agent训练数据与评测基准
practical_value: '- 可复用「环境-智能体协同迭代」范式，在电商模拟环境中自动生成用户/商家Agent交互轨迹，降低真实交互数据采集成本

  - 训练时可借鉴progress-weighted SFT思路，给搜索推荐链路中对转化/点击有正向贡献的行为步骤分配更高微调权重，提升模型业务效果

  - 构建业务Agent评测集时，可参考基于状态校验的任务定义方法，自动完成任务成功率/完成进度的指标计算，减少人工标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉Agent游戏训练依赖昂贵的人类 gameplay 标注，从游戏视频学习需推断缺失动作，且公开数据集覆盖游戏少、无明确任务与可验证结果，难以规模化训练。
### 方法关键点
提出Game2Player闭环框架，Builder Agent适配现有网页游戏、暴露内部状态、定义带进度度量和成功校验的任务；Coding Player与VLM Player执行任务并反馈问题给Builder修复，交互过程同时完成环境验证与训练轨迹采集；训练时采用progress-weighted SFT，给推进任务进度的步骤分配更高权重。
### 关键结果
构建568个验证网页游戏、3436个任务，采集15.7K条轨迹（共307小时 gameplay），开源50个游戏的PlayerBench基准；基于该数据训练的Game2Player-9B，在PlayerBench上任务进度从14.3%提升至31.2%，在外部GameWorld基准上从30.0%提升至53.1%。

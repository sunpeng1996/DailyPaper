---
title: 'RoboTTT: Context Scaling for Robot Policies'
title_zh: RoboTTT：面向机器人策略的上下文长度扩展方法
authors:
- Yunfan Jiang
- Yevgen Chebotar
- Ruijie Zheng
- Fengyuan Hu
- Yunhao Ge
- Jimmy Wu
- Tianyuan Dai
- Scott Reed
- Li Fei-Fei
- Yuke Zhu
affiliations:
- NVIDIA
- Stanford University
- The University of Texas at Austin
arxiv_id: '2607.15275'
url: https://arxiv.org/abs/2607.15275
pdf_url: https://arxiv.org/pdf/2607.15275
published: '2026-07-15'
collected: '2026-07-17'
category: Other
direction: 机器人基础模型 · 长上下文扩展
tags:
- Test-Time Training
- Long Context
- Robot Foundation Model
- Fast Weights
- Visuomotor Policy
one_liner: 将机器人基础模型视觉运动上下文扩展至8K步，不增推理延迟同时大幅提升长horizon任务表现
practical_value: '- Test-Time Training + fast weights 压缩长上下文的思路，可迁移到长会话用户行为建模，避免KV
  cache膨胀、推理延迟上涨

  - 序列动作强制 + 截断时序反向传播的训练recipe，可复用在长序列推荐/多轮Agent决策的长上下文预训练任务中

  - 上下文长度可作为模型缩放新轴的结论，可参考优化推荐系统的用户行为序列长度上限，验证更长序列的业务收益'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人基础模型仅支持单步/短历史视觉运动上下文，无法支撑长horizon多阶段任务，扩展上下文长度同时控制推理成本是核心痛点。
### 方法关键点
1. 集成Test-Time Training到视觉-语言-动作策略中，用梯度更新的fast weights作为循环状态，将历史上下文压缩到权重空间，不依赖KV cache存储长序列，推理延迟不随上下文长度上涨；
2. 训练侧结合序列动作强制与截断backpropagation through time，支撑8K timestep上下文长度训练。
### 关键结果
比单步上下文基线整体性能提升87%，首次完成5分钟10阶段装配任务；8K上下文预训练模型比1K版本性能高62%，首次观测到闭环性能随预训练上下文长度提升稳定增长

---
title: Reinforcement Learning for Controller Parameters in the Auto-Bidding System
  at Pinterest
title_zh: Pinterest自动出价系统中基于强化学习的控制器参数优化
authors:
- Yichu Zhou
- Qinyi Chen
- Fei Feng
- Jacob Loh
- Mehdi Ben Ayed
- Lin Yang
- Andrei Curelea
- Jiajing Xu
affiliations:
- Pinterest Inc.
- University of California, Los Angeles
arxiv_id: '2610.33248'
url: https://arxiv.org/abs/2610.33248
pdf_url: https://arxiv.org/pdf/2610.33248
published: '2026-10-23'
collected: '2026-10-27'
category: RecSys
direction: 广告自动出价 · RL+PID混合架构
tags:
- auto-bidding
- reinforcement learning
- PID control
- budget pacing
- computational advertising
one_liner: 采用RL作为元控制器动态调整自动出价PID参数，兼顾生产稳定性与自适应优化效果
practical_value: '- 工业场景部署RL优先选择「元控制器+成熟生产组件」的混合架构，而非直接替换现有链路，既保留原有系统的稳定性、可解释性，又能通过RL获得自适应优化收益，大幅降低上线风险

  - 多目标优化场景可采用多头DQN分别拟合不同目标的Q值，在推理阶段通过状态依赖的权重动态融合，无需重新训练即可适配不同业务阶段的优先级调整，适合业务目标灵活变动的场景

  - 奖励设计优先采用相对基线的lift值而非绝对指标，既消除不同场景下的指标量级差异，也能放大RL的优化信号，提升模型对微小收益的感知能力，训练效率更高

  - 高频生产链路的RL推理可采用「离线预计算参数+查表」的部署方式，无需在线跑模型，完全不增加请求时延，适合QPS极高的广告、推荐系统场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界广告自动出价系统广泛使用PID控制器实现预算平滑投放与成本控制，但其固定参数无法适配异构campaign的生命周期差异、非稳态的流量与竞价市场环境，而直接用RL生成出价又存在稳定性差、难解释、上线风险高的问题，亟需兼顾安全与效果的RL落地方案。

### 方法关键点
- 混合RL+PID架构：RL作为元控制器，每日为每个campaign选择PID参数的乘性调整系数（仅调整kp、ki，范围限制在默认值的±20%，共9种离散动作），保留PID做毫秒级高频出价调整，推理阶段仅需加载预计算的参数对照表，无在线模型开销
- 多头DQN设计：分别为预算利用率、CPC优化两个目标训练独立的Q头，训练阶段无需固定目标权重，推理阶段根据campaign剩余生命周期动态调整融合权重，剩余天数越少越偏向预算消耗
- 相对lift奖励：奖励定义为指标相对生产基线的提升率，消除不同campaign的指标量级差异，放大优化信号

### 关键实验
离线用21天历史数据训练、7天holdout验证，相对lift奖励相比绝对奖励，campaign最后一天营收提升2.77%，非末期CPC降低3.02%；线上7天A/B测试显示全量campaign eCPC显著降低0.25%且无营收损失，高预算组eCPC降低0.90%、点击提升0.81%；全量上线2个月后，剩余生命周期≥7天的campaign eCPC降低0.98%、CTR提升0.66%，剩余<7天的campaign预算利用率提升0.60%、eCPC降低0.72%。

### 核心结论
在安全敏感的工业生产系统中，RL作为成熟链路的增强组件而非替代方案，是快速落地获得收益的务实路径。

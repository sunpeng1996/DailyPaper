---
title: Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning
title_zh: 面向隐空间世界模型强化学习的密度引导自举边界方法
authors:
- Shashank Gupta
- Pilhwa Lee
affiliations:
- University of Michigan
- Morgan State University
arxiv_id: '2610.41022'
url: https://arxiv.org/abs/2610.41022
pdf_url: https://arxiv.org/pdf/2610.41022
published: '2026-10-29'
collected: '2026-11-02'
category: Agent
direction: Agent强化学习 · 世界模型轨迹优化
tags:
- Reinforcement-Learning
- World-Model
- Adaptive-Bootstrapping
- DreamerV3
- Trajectory-Optimization
one_liner: 提出密度引导的轨迹自适应自举边界机制，降低隐世界模型强化学习的累计预测误差
practical_value: '- 做LLM驱动的轨迹规划类Agent（如电商导购Agent、用户行为预测Agent）时，可借鉴自适应截断思路，不固定轨迹模拟步数，根据模拟轨迹置信度动态停止，减少累计误差

  - 借鉴软硬两种边界门控机制：硬边界可直接截断低置信度轨迹，软边界可动态调整模型预测和历史critic估值的权重，平衡仿真效率与精度

  - 基于相对密度代理的置信度评估方法可迁移到GenRec的假样本筛选场景，过滤低质量生成交互样本，避免污染模型训练'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
隐空间世界模型RL依赖想象轨迹学习策略，但固定想象步长不考虑轨迹可靠性，要么引入累计模型误差，要么过度依赖critic近似估值。
### 方法关键点
1. 设计分数感知的相对密度代理，沿想象路径累计特征偏移网络+噪声条件分数估计器构成的辅助场的估计散度，作为轨迹置信度指标
2. 提出两种门控机制：硬边界在离散状态直接截断回报展开，软边界连续将回报递归转向critic自举，二者均保留边界估值并为actor/critic损失分配对应存活权重
3. 无关于具体动力学模型，在DreamerV3中实现，理论证明门控Bellman算子是严格压缩映射，提前自举可单调降低条件目标方差
### 关键结果
在连续控制任务和Atari Pong上，相比固定步长、带辅助模块的基线方法，动态边界选择的样本效率和训练后期性能均有提升

---
title: Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning
title_zh: 基于测试时模型强化学习的世界模型记忆编码方法
authors:
- Maxime Burchi
- Fayaz Ali Dharejo
- Radu Timofte
affiliations:
- University of Würzburg, Germany
arxiv_id: '2611.09625'
url: https://arxiv.org/abs/2611.09625
pdf_url: https://arxiv.org/pdf/2611.09625
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agent 世界模型长时序记忆优化
tags:
- MBRL
- World Model
- Test-Time Training
- Long-Term Memory
- Reinforcement Learning
one_liner: 通过测试时梯度更新将 episodic 记忆编码到世界模型参数，显著提升长时序规划任务性能
practical_value: '- 测试时会话级适配思路可迁移到推荐系统：给每个用户会话做轻量梯度更新，将会话专属信息编码到模型参数，替代纯长序列context输入，缓解长上下文的性能衰减问题

  - 测试时微调的trick可直接复用：微调时混合全局历史数据和当前会话数据防过拟合，冻结通用的Embedding层/编码器仅更新上层动态模块，兼顾效果和推理效率

  - 长时序任务性能增益随有效观测数线性提升的结论可参考：电商长会话路径规划、用户购物旅程预判等场景，可通过累积会话观测动态调整模型效果'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有基于MBRL的世界模型仅靠架构优化（RNN/Transformer/SSM）承载长时序记忆，泛化到新episode时只能通过上下文表示建模场景专属信息，在部分可观测、长规划周期任务中预测误差随时间快速累积，性能远低于人类水平，且纯架构优化已遇到明显瓶颈。

### 方法关键点
- 每个测试episode初始化时复用全局预训练权重，维护独立的测试时回放缓存存储当前episode的观测轨迹
- 测试时梯度更新采用50%全局训练样本+50%当前episode样本的混合采样策略，避免小样本过拟合
- 冻结通用的编码器、解码器参数，仅更新时序动态模块、奖励/终止预测头、Actor-Critic网络，移除重建损失，大幅降低测试时计算开销

### 关键实验
- 基准覆盖Memory Maze 2D/3D全尺寸、DeepMind Control、Atari 100k，对比DreamerV3、TWISTER、R2I等主流世界模型
- 3D Memory Maze 15×15任务上，R2I结合TT-MBRL后得分从42.0提升到54.1，接近人类基线67.7，单episode 4000步后单位步长奖励提升53.7%，达到新SOTA
- 非记忆类任务上无性能损失，DMC 20任务平均得分从776.2提升到788.2，Atari 100k平均得分从109.5%提升到111.1%

### 核心结论
参数级记忆是上下文记忆的有效互补，测试时轻量微调能够以可控计算成本大幅提升Agent对当前任务场景的适配能力

---
title: Concept-Guided Spatial Regularization for World Models in Atari Pong
title_zh: 面向Atari Pong环境世界模型的概念引导空间正则化方法
authors:
- Yukuan Lu
- Zaishuo Xia
- Weyl Lu
- Yubei Chen
affiliations:
- UC Davis
arxiv_id: '2607.15142'
url: https://arxiv.org/abs/2607.15142
pdf_url: https://arxiv.org/pdf/2607.15142
published: '2026-07-16'
collected: '2026-07-19'
category: Agent
direction: Agent 世界模型建模优化
tags:
- World Model
- Model-based RL
- Regularization
- Concept Learning
- Reinforcement Learning
one_liner: 针对视觉世界模型独立部署时的动态偏差问题，提出概念引导空间正则化方法优化关键物体建模
practical_value: '- 做交互类Agent（如智能导购、直播场控Agent）的世界建模时，可借鉴CGSReg思路，对业务核心实体（商品、优惠券、用户交互动作）单独增加重构损失，避免核心实体生成/逻辑错误

  - 评估世界模型能力时，不要仅依赖端到端RL效果，可新增冻结世界模型、单独训练新策略的零样本评估范式，提前发现模型隐性缺陷

  - 做推荐系统用户行为路径仿真时，可对点击、加购等关键行为节点加语义/空间正则，避免生成不符合业务逻辑的虚假交互路径'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有MBRL体系通常端到端评估整体性能，极少单独验证世界模型的独立建模可靠性：主流5种视觉世界模型在Atari Pong任务中独立rollout时存在球消失、运动逻辑错误、碰撞失效等核心问题，冻结世界模型后单独训练的新策略迁移到真实环境的效果大幅跳水，DreamerV3平均回报从-5.5暴跌至接近下限的-20.9。
### 方法关键点
提出Concept-Guided Spatial Regularization (CGSReg)，对分割后的任务关键概念区域新增辅助像素重构损失，强化核心实体的动态建模精度。
### 关键结果
CGSReg可同时提升DreamerV3、DIAMOND、TWISTER三类模型的闭环rollout效果与像素空间零样本MBRL性能，单独使用该正则无法覆盖所有世界模型瓶颈。

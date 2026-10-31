---
title: 'world2vec: Mechanistic world models through latent dynamics learning'
title_zh: world2vec：基于隐态动力学学习的机制型世界模型
authors:
- Tobias Schmidt
- Rodrigo Gonzalez Laiz
- Krisztián Szuppinger
- Steffen Schneider
affiliations:
- Helmholtz Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.40637'
url: https://arxiv.org/abs/2610.40637
pdf_url: https://arxiv.org/pdf/2610.40637
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 世界模型 · 隐态动力学无监督学习
tags:
- World Model
- Latent Dynamics
- Reward-free Learning
- Representation Learning
- System Identification
one_liner: 提出无奖励训练的轻量world2vec世界模型，长时序动态还原精度高，参数量较同类低一个数量级
practical_value: '- 轻量世界模型压缩思路可复用在端侧Agent决策场景，无奖励训练范式降低业务标注成本

  - 长时序隐态动态对齐方法可迁移到用户行为长序列建模、电商大促销量预判等预测任务

  - 无监督隐态表征学习框架可适配推荐冷启动、广告投放效果预判等无明确reward的场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有世界模型往往仅能保障控制性能，无法忠实还原环境真实动态，可解释性差，且大多依赖奖励信号训练，参数量庞大，限制了其在长时序决策、科学发现场景的落地潜力。
### 方法关键点
提出world2vec机制型世界模型，无需奖励信号输入，仅通过观测值与动作数据即可训练；学习与真实系统演化严格对齐的隐态动力学，架构上做了极致的参数量压缩。
### 关键结果数字
参数量较DreamerV3、TD-MPC2、LeWM等同类SOTA模型低至少1个数量级；像素输入的连续环境控制性能达SOTA；在71个吸引子基准测试集上实现高精度系统识别。

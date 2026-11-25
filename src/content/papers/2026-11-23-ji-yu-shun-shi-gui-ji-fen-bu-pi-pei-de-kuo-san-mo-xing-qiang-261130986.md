---
title: Reinforcing Diffusion Models by Instantaneous Trajectory Distribution Matching
title_zh: 基于瞬时轨迹分布匹配的扩散模型强化优化方法
authors:
- Yihong Luo
affiliations:
- Hong Kong University of Science and Technology
arxiv_id: '2611.30986'
url: https://arxiv.org/abs/2611.30986
pdf_url: https://arxiv.org/pdf/2611.30986
published: '2026-11-23'
collected: '2026-11-25'
category: Training
direction: 扩散模型 RL 对齐训练优化
tags:
- Diffusion Model
- Reinforcement Learning
- Distribution Matching
- Training Stability
- Preference Alignment
one_liner: 提出瞬时轨迹分布匹配iTDM，解决扩散RL训练梯度漂移问题，收敛快3倍可扩展到大参数扩散模型
practical_value: '- 生成式推荐类diffusion模型做RL对齐时，可直接复用iTDM替代原有RWR类方法，解决CFG采样下训练不稳定问题，收敛速度提升近3倍

  - 离线/离策略更新场景的生成模型微调，可借鉴iTDM锚定行为速度的梯度构造思路，避免基线漂移导致的训练崩溃

  - 5B级大参数多模态生成推荐模型的偏好对齐，可直接复用iTDM开源实现，无需额外学习奖励倾斜目标得分，降低训练开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有前向扩散RL方法依赖带符号奖励加权回归，隐含的「策略速度等于行为边际速度」假设在classifier-free guidance(CFG)采样、离线/离策略更新、在线自一致性不足等场景不成立，会破坏基线不变性、引入梯度漂移，导致训练不稳定。

### 方法关键点
提出瞬时轨迹分布匹配(iTDM)，对轨迹分布匹配取无穷小极限，通过后验得分恒等式得到锚定行为速度的样本级梯度，无需额外学习奖励倾斜目标得分；搭配在线辅助去噪器跟踪速度，在辅助最优时保证严格基线不变性，可同时抑制在线/离线RL场景的基线漂移。

### 关键结果数字
在组合生成、文本渲染、偏好对齐任务上取得SOTA表现；GenEval2基准上收敛速度比竞品快近3倍，得分可达0.87无训练崩溃；可平滑扩展到5.6B FLUX.3模型，域内、未见指标均优于现有方案。

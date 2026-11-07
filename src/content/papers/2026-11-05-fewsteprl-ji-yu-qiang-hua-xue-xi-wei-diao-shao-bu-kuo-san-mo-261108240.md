---
title: 'FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning'
title_zh: 《FewStepRL：基于强化学习微调少步扩散模型》
authors:
- Haitao Lin
- Minsi Ren
- Yang Li
- Xingtong Ge
- Zheyuan Hu
- Peiyan Hu
- Tailin Wu
affiliations:
- Tencent Hunyuan
- Westlake University
- University of Chinese Academy of Sciences
arxiv_id: '2611.08240'
url: https://arxiv.org/abs/2611.08240
pdf_url: https://arxiv.org/pdf/2611.08240
published: '2026-11-05'
collected: '2026-11-07'
category: Training
direction: 少步扩散模型 · RL微调优化
tags:
- Reinforcement Learning
- Diffusion Model
- Fine-tuning
- Few-step Sampling
- Training Optimization
one_liner: 系统性适配RL目标到少步扩散模型，输出多类主流方法的少步版本与统一模块化代码
practical_value: '- 生成式推荐（如商品营销素材、文案生成）场景的扩散模型微调可直接复用本框架的少步RL适配方法，大幅降低RL微调算力成本

  - 若业务奖励函数可导优先选择奖励梯度类方法，不可导时选DiffusionNFT类方法，可在迭代效率和单步成本间取最优平衡

  - 生成类推理场景可训练时用少步采样降本，推理时将采样步数提升2-4倍针对性优化优质输出质量，无需全局加步数'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统扩散模型RL微调依赖多步采样器，每轮迭代的策略rollout占训练成本的绝大多数；少步扩散虽能降本，但现有RL目标为多步采样的瞬时速度设计，无法直接适配少步的区间平均速度建模逻辑。

### 方法关键点
通过三阶段框架系统性适配RL目标到少步扩散：1）x空间变换，将密度、速度、奖励类目标统一映射到公共策略预测空间对齐；2）梯度分解，把所有目标梯度拆为参考自回归项+奖励增强项，仅需调整锚点和权重即可适配不同方法；3）少步适配，从少步模型的传输终点或切线计算锚点，从主干或辅助网络恢复瞬时速度。基于该框架输出FlowGRPO、AWM等5种主流扩散RL方法的少步版本，统一模块化代码。

### 关键结果
奖励可导时奖励梯度类方法效果最优；奖励不可导时DiffusionNFT类方法仅需较少迭代即可达到高奖励；推理采样步数提升到训练的2-4倍时，部分输出质量明显提升，但无全局系统性收益

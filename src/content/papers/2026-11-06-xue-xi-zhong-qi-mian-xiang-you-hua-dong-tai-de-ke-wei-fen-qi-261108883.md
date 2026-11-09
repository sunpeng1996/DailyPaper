---
title: 'Learning to Restart: Differentiable Restart Policies for Optimization Dynamics'
title_zh: 学习重启：面向优化动态的可微分重启策略
authors:
- Yiman Fong
- Zhonglin Xie
- Zaiwen Wen
affiliations:
- 清华大学工业工程系
- 北京大学北京国际数学研究中心
arxiv_id: '2611.08883'
url: https://arxiv.org/abs/2611.08883
pdf_url: https://arxiv.org/pdf/2611.08883
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: 优化算法 · 可微分学习重启策略
tags:
- Learning_to_Optimize
- Surrogate_Gradient
- Optimization_Restart
- Differentiable_Programming
one_liner: 提出基于连续时间极限的可微分框架，解决优化器重启策略学习非可微问题，性能优于手工规则且支持零样本迁移
practical_value: '- 训练推荐/广告CTR预估大模型时，可借鉴本方法思路用数据驱动学习优化器重启时机，替代现有手工重启规则，加速模型收敛、降低训练成本

  - 离散决策的surrogate gradients处理方法可迁移到MoE路由选择、召回截断决策等场景，解决离散操作导致的梯度断流问题

  - 合成数据集预训练的重启策略可零样本迁移到真实业务的LR、宽深模型训练场景，无需额外调参即可获得收益'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前加速一阶优化器的自适应重启机制均为手工设计，离散重启事件导致优化轨迹对算法参数不可微，无法用梯度法优化重启策略，限制了Learning to Optimize（L2O）在重启场景的落地。

### 方法关键点
1. 基于连续时间极限构建重启策略的可微分框架，绕开离散事件的非可微问题
2. 设计针对重启事件和优化轨迹的surrogate gradients，计算效率高且可证明收敛到连续时间对应值

### 关键结果
1. 训练得到的重启策略在二次规划、线性规划任务上效果优于标准手工自适应重启准则
2. 在合成二次数据集上训练的策略可零样本迁移到真实数据集的logistic回归任务，无需额外微调

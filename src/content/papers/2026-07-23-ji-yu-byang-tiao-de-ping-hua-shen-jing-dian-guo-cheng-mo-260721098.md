---
title: Smooth Neural Point Processes via B-Splines
title_zh: 基于B样条的平滑神经点过程模型
authors:
- Michele Bellomo
- Riccardo Ramaschi
- Alberto Dolara
- Tomaso Aste
affiliations:
- Politecnico di Milano
- University College London
arxiv_id: '2607.21098'
url: https://arxiv.org/abs/2607.21098
pdf_url: https://arxiv.org/pdf/2607.21098
published: '2026-07-23'
collected: '2026-07-25'
category: RecSys
direction: 时序行为建模 · 神经点过程优化
tags:
- Temporal Point Process
- B-spline
- User Behavior Modeling
- Sequential Recommendation
- Efficient Training
one_liner: 用B样条基函数参数化条件强度函数，实现神经点过程的并行训练、精确NLL计算与性能提升
practical_value: '- 电商用户浏览、加购、下单等连续时序行为建模可复用B样条参数化CIF的思路，替代传统TPP的数值积分计算，降低训练开销

  - 训练时可直接并行计算所有事件的NLL贡献，无需串行执行，适配万级以上批次的大规模用户行为序列训练任务

  - 内置的二阶导数平滑正则项可直接复用，无需额外设计正则策略，即可提升用户行为时序预测的稳定性与准确率'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有神经TPP多直接建模补偿器而非条件强度函数（CIF），对神经网络架构存在强约束，且负对数似然（NLL）计算需串行执行，训练效率低，无法适配大规模用户行为序列建模需求。
### 方法关键点
1. 直接将CIF参数化为B样条基函数的非负线性组合，系数由神经网络预测；2. 该形式支持NLL的精确计算，无需数值积分，且所有事件的NLL贡献可并行计算，无架构约束；3. 天然支持通过积分二阶导数平方项实现CIF平滑正则。
### 关键结果
相比基准神经TPP模型，在合成及真实数据集上同时实现计算效率与预测准确率的双重提升。

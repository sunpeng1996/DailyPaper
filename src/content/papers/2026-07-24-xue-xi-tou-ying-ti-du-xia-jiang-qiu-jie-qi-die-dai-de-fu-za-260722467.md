---
title: Complexity Bounds and Approaches to Learning Projected Gradient Descent Solver
  Iterates
title_zh: 学习投影梯度下降求解器迭代的复杂度边界与方法
authors:
- Anjian Li
- Ryne Beeson
affiliations:
- Princeton University
- Department of Electrical and Computer Engineering
- Department of Mechanical and Aerospace Engineering
arxiv_id: '2607.22467'
url: https://arxiv.org/abs/2607.22467
pdf_url: https://arxiv.org/pdf/2607.22467
published: '2026-07-24'
collected: '2026-07-28'
category: Training
direction: 生成模型训练 · 数据增强与泛化性分析
tags:
- Generative Model
- Data Augmentation
- Rademacher Complexity
- Projected Gradient Descent
- Optimization
one_liner: 提出k邻域迭代数据增强策略，推导泛化界，降低优化问题生成模型训练的数据开销
practical_value: '- 训练生成式推荐/召回模型时，可复用k邻域数据增强思路：不只用最优收敛的样本做训练，将梯度下降迭代的中间有效样本也加入训练集，无需额外任务运行即可扩充数据规模，降低训练数据成本

  - 小样本场景下微调LLM/Agent决策模型时，可借鉴该数据增强逻辑，复用求解/推理过程中的中间结果扩充训练数据，减少标注/采样开销

  - 评估推荐/排序模型泛化性时，可参考其基于Rademacher复杂度的泛化界推导框架，量化模型在分布外样本上的表现'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
训练用于生成参数优化问题初始解的生成模型时面临核心数据稀缺痛点：传统方案仅保留每次求解器运行的最终收敛解，需运行大量求解任务才能攒够训练数据，计算成本极高。
### 方法关键点
1. 提出k邻域数据采集策略，在原有收敛解数据集基础上，补充投影梯度下降求解器迭代过程中的中间结果作为训练数据，无需额外运行求解器即可扩充数据量
2. 针对单侧盒约束二次规划场景，推导基于Rademacher复杂度的泛化界，明确k邻域大小等参数对模型泛化性的影响
### 关键结果
可在不增加求解器运行次数的前提下将训练数据量提升k倍（k为邻域覆盖的迭代步数），大幅提升数据-模型-优化循环效率，适配动态数据驱动应用系统范式

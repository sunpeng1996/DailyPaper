---
title: 'SympFormer: Inertial Attention Blocks from Damped Hamiltonian Dynamics on
  Spaces of Probability Measures'
title_zh: SympFormer：基于概率测度空间阻尼哈密顿动力学的惯性注意力模块
authors:
- Viktor Stein
- Levin Maier
- Wuchen Li
- Gabriele Steidl
affiliations:
- Technical University of Munich
- Munich Center for Machine Learning
- Institute for Advanced Study (Princeton)
- University of South Carolina
- Technische Universität Berlin
arxiv_id: '2610.31600'
url: https://arxiv.org/abs/2610.31600
pdf_url: https://arxiv.org/pdf/2610.31600
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: LLM注意力优化 · 最优传输几何建模
tags:
- Transformer
- Attention Mechanism
- Wasserstein Geometry
- Hamiltonian Dynamics
- Linear Attention
- Model Acceleration
one_liner: 从概率测度空间的阻尼哈密顿动力学推导惯性注意力块，解决token范数爆破问题并验证几何修正效果
practical_value: '- 线性注意力的token范数爆破预测方法可复用到长序列推荐/用户行为建模场景，提前设置截断阈值避免深层模型输出退化

  - 注意力层的几何修正技巧可直接融入LLM4Rec的SFT/ LoRA微调流程，在推理成本可控的前提下降低序列预测损失

  - 基于Nesterov加速的惯性注意力设计思路，可用于优化召回排序模块的梯度更新策略，加速训练收敛'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
Transformer注意力的动力学机制长期缺乏严谨数学解释，现有梯度流视角无法解释token范数随层深爆破的问题，也缺少将Nesterov加速引入注意力优化的严格理论支撑。
### 方法关键点
1. 提出局部移动几何和商Stein几何两套框架，分别为softmax注意力和线性注意力的梯度流、阻尼哈密顿动力学构建严谨数学基础，填补了非紧域下注意力梯度流形式化的理论空白
2. 推导线性注意力的有限维ODE等价形式，给出全局存在性和有限时间二阶矩爆破的严格条件，建立连续域矩爆破与离散层深下token范数超限的定量关联
3. 基于有限token几何推导token与动量更新的几何修正项，得到SympFormer惯性注意力块
### 关键结果
在TinyStories和OpenWebText的nanoGPT实验中，相比仅动量的基线，几何修正的注意力块验证集next token预测负对数似然有小幅下降，计算成本相应提升。

最值得记住的一句话：注意力层的动力学行为可以完全嵌入最优传输的几何框架，从连续动力系统视角设计的修正能直接改进离散Transformer的实际效果。

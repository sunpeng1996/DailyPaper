---
title: U-Statistics-Powered LLM Reasoning
title_zh: 基于U统计量的GRPO组大小自适应选择方法优化LLM推理训练
authors:
- Shijin Gong
- Kai Ye
- Victor Chernozhukov
- Xinyu Zhang
- Chengchun Shi
affiliations:
- University of Science and Technology of China
- London School of Economics and Political Science
- Massachusetts Institute of Technology
- Chinese Academy of Sciences
arxiv_id: '2611.33064'
url: https://arxiv.org/abs/2611.33064
pdf_url: https://arxiv.org/pdf/2611.33064
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: LLM推理训练 · GRPO超参数优化
tags:
- GRPO
- U-Statistics
- LLM Reasoning
- Reinforcement Learning
- Hyperparameter Tuning
one_liner: 利用U统计量推导GRPO最优组大小公式，提出悲观估计器自适应选组提升LLM推理训练效率
practical_value: '- 做Agent、推理型导购LLM的GRPO对齐训练时可直接复用该自适应组大小方法，替代手动调参，仅增加不到11%的训练开销即可稳定提升训练效果

  - 悲观比值估计的思路可迁移到推荐/广告场景的比值类超参数优化（如冷热流量分配比例、召回阈值），避免分母估计偏小时的结果不稳定

  - 可直接复用GRPO梯度MSE分解公式指导RLHF训练的采样预算分配，固定总token量下平衡prompt批次大小和每prompt生成回复数的tradeoff'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
GRPO是当前LLM推理、Agent对齐训练的主流算法，但其核心超参数组大小G长期依赖人工试错，G取值直接影响梯度估计MSE和训练稳定性：过大会降低prompt多样性、提升prompt间方差，过小会降低单prompt内奖励估计精度、提升prompt内方差，严重时会导致梯度爆炸、训练崩溃，缺乏有统计理论支撑的自适应选择方法。

### 方法关键点
1. 挖掘GRPO随机梯度的U统计量结构，通过Hoeffding分解推导出固定总采样预算下最优组大小的闭式解：$G^*=1+\sqrt{c_3/c_1}$，其中$c_1$为prompt间方差、$c_3$为prompt内方差，将组大小选择转化为方差比值估计问题
2. 对比有偏、无偏两种比值估计器的tradeoff：无偏估计在常规场景精度更高，但在弱信号（$c_1$极小）场景下会因分母估计接近0导致结果极不稳定
3. 提出悲观估计器，给候选组大小的损失项加不确定性惩罚，同时裁剪分母下界，兼顾常规场景精度和弱信号场景稳定性

### 关键实验结果
在Reasoning Gym合成推理任务、GSM8K数学推理、AceCode代码生成任务上测试，对比固定$G \in \{2,4,8,16,32,64\}$的基线：
- 梯度相对超额MSE在27/30个实验设置下为所有方法最低
- 在10个跨难度数学推理benchmark上平均准确率比最优固定G基线高0.67个百分点
- 训练时间仅增加7.03%~10.33%

### 核心结论
GRPO组大小选择的核心是平衡prompt间方差与prompt内方差，弱信号场景下带不确定性惩罚的悲观估计远优于纯无偏估计

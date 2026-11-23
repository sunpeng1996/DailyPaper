---
title: 'Distillation with Errors: Sparse Unbiased Backpropagation for Knowledge Distillation'
title_zh: 带误差蒸馏：用于知识蒸馏的稀疏无偏反向传播
authors:
- Yuyang Zhang
- Yuxin Li
affiliations:
- University of Science and Technology of China
arxiv_id: '2611.27131'
url: https://arxiv.org/abs/2611.27131
pdf_url: https://arxiv.org/pdf/2611.27131
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 知识蒸馏 · 大模型训练效率优化
tags:
- Knowledge Distillation
- Sparse Backpropagation
- Training Efficiency
- Unbiased Gradient Estimation
- Large Language Model
one_liner: 提出稀疏无偏的知识蒸馏反向传播方法DWE，在效果持平前提下最高实现2.2倍输出头提速
practical_value: '- 生成式推荐/语义ID模型做小模型蒸馏时，可直接复用DWE方案替代全词表KD，训练时间降10%+且下游推荐效果无损失，适合电商大词表商品推荐模型的轻量化落地

  - 业务中大词表分类/预测任务（如query推荐、商品ID召回头训练）可复用零和梯度配对采样思路，无需计算全词表梯度，降低反向传播算力开销

  - 几何感知配对的trick可直接复用：提前缓存输出层权重的主成分投影排序，无需迭代求解最优传输即可降低梯度估计方差，工程实现开销极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型知识蒸馏（KD）中全词表输出头反向传播算力开销极高，现有top-k梯度筛选方案会引入偏差，重要性采样（IS）梯度估计方差大，亟需兼顾无偏、低方差、低计算量的反向传播优化方案。
### 方法关键点
- 利用logit梯度的零和特性，拆分正负梯度为两个独立分布，各采样1个坐标赋予相反权重，构造二稀疏无偏梯度估计，消除IS的随机符号分配方差
- 提前基于输出层权重的主成分投影生成词表固定一维排序，做几何感知配对，降低隐层梯度估计误差
- 引入分层采样，将采样区间拆分为K等份各采1个量化对，进一步降低估计方差，每token最多仅需反向传播2K个输出行
- 理论证明该梯度估计无偏，误差随采样数K增加以1/K速率下降
### 关键结果
实验基于Qwen3系列多尺度模型蒸馏任务，对比全词表KD、重要性采样IS两个基线：
1. 相同采样预算下，DWE比IS降低隐层梯度MSE 63.5%、输出权重梯度MSE 57.9%，16次采样的精度等价于IS的44次
2. 离策略KD场景下，输出头提速1.63~1.95倍，总训练时间降10.4~15.7%，7个零样本下游benchmark效果与全词表KD持平
3. 同策略蒸馏场景下，输出头最高提速2.2倍，13个推理benchmark效果无损失
### 核心洞察
小批量训练本身就是梯度近似，无需每个token位置都做精确的全词表反向传播，通过无偏稀疏估计可在几乎无损效果的前提下大幅降低训练成本。

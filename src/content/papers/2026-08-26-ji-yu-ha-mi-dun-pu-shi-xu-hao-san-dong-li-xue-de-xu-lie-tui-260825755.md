---
title: Hamiltonian Spectral-Temporal Dissipative Dynamics for Sequential Recommendation
title_zh: 基于哈密顿谱-时序耗散动力学的序列推荐模型
authors:
- Shuiying Liao
- P. Y. Mok
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2608.25755'
url: https://arxiv.org/abs/2608.25755
pdf_url: https://arxiv.org/pdf/2608.25755
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 序列推荐 · 二阶动力学建模
tags:
- Sequential Recommendation
- Hamiltonian Dynamics
- Spectral Modeling
- State Space Model
- User Behavior Modeling
one_liner: 将用户偏好演化建模为二阶耗散哈密顿系统，提出HSR序列推荐模型，效果与效率均优于现有SOTA
practical_value: '- 用户行为建模可引入二阶动力学假设，拆分稳定偏好（position）和短期趋势（momentum）两个维度，对惯性、周期性、突变行为的建模增益明显，尤其适合电商/短视频等稀疏短序列场景

  - 频率域计算优化可复用：用RFFT/IRFFT实现O(TlogT)长序列处理，比Transformer O(T²)、SSM顺序计算效率更高，单用户推理延迟比Mamba4Rec低44%，吞吐量高77%，适配高QPS线上推荐场景

  - 抗噪设计可直接落地：物理约束的阻尼参数天然充当低通滤波器，能抑制误点击等高频噪声，冷启动、短序列场景下效果优于现有SOTA，适合新用户、低活用户推荐优化

  - 模型轻量化参考：HSR参数比Mamba4Rec少22%，训练速度快49%，精度更高，可替换现有序列推荐基座，降低部署成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐模型均基于一阶状态转移假设，仅依赖当前隐状态预测下一行为，无法捕捉用户行为的惯性、周期性、突发偏移等二阶动力学特征，在稀疏、短序列、高噪的电商/内容推荐场景下表现受限。

### 方法关键点
- 用耗散哈密顿系统建模用户偏好演化，在隐相空间拆分position（稳定偏好）和momentum（短期趋势）两个耦合变量，物理参数（质量/阻尼/刚度）通过softplus约束为正，可解释性强
- 全局谱传播模块：将二阶微分方程转换到频率域求解，通过FFT实现O(TlogT)的长序列建模，避免梯度消失和长序列性能衰减
- 局部脉冲优化分支：用1D深度卷积拟合误点击、突发好奇等短期异常行为，和全局谱模块结果门控融合
- 相空间外推预测：用终端状态的momentum做一步欧拉外推，预测用户下一时刻的偏好，而非直接用当前状态打分

### 关键结果
在MovieLens-1M、Amazon-Beauty、Amazon-Video-Games三个公开数据集上对比SASRec、BERT4Rec、Mamba4Rec、DIFF等SOTA，稀疏Amazon数据集上NDCG@10最高提升10.57%，MRR@10最高提升17.42%，参数比Mamba4Rec少22%，训练速度快49%，单用户推理延迟低44%，吞吐量高77%，抗噪、冷启动表现均优于基线。

最值得记住的一句话：基于物理先验的二阶动力学建模，能以更低的计算成本、更高的鲁棒性，解决现有序列推荐对用户行为高阶特征捕捉不足的问题

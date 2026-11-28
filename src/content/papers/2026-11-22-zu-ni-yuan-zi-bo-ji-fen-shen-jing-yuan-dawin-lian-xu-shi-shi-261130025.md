---
title: 'Damped Atomic Wave Integration Neurons (DAWIN): A Universal Primitive for
  Continuous-Time Spatiotemporal Learning'
title_zh: 阻尼原子波积分神经元(DAWIN)：连续时间时空学习通用基元
authors:
- Byunggu Yu
- Justin Kim
affiliations:
- University of the District of Columbia
- Department of Computer Science and Information Technology, University of the District
  of Columbia
arxiv_id: '2611.30025'
url: https://arxiv.org/abs/2611.30025
pdf_url: https://arxiv.org/pdf/2611.30025
published: '2026-11-22'
collected: '2026-11-28'
category: Training
direction: 基础神经网络 · 连续时空建模
tags:
- DAWIN
- Continuous-Time Learning
- Spatiotemporal Modeling
- Neural Primitive
- Triton Kernel
one_liner: 提出可直接替换标准线性层的连续时间神经元DAWIN，实现高效精准的连续时空联合建模
practical_value: '- 处理电商用户行为序列、线下动线轨迹等不规则时间采样数据时，可尝试用DAWIN替换现有模型中的Linear/ReLU层，无需额外时间编码即可精准建模时间依赖

  - 长序列推荐、Agent长上下文记忆等场景可复用DAWIN的Triton前缀扫描实现思路，降低推理延迟与GPU显存占用，适配实时业务要求

  - 连续时空预测类业务（如用户复购间隔预测、物流时效预测）可直接迁移DAWIN结构，避免神经常微分方程求解器带来的性能损耗'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统神经元将空间特征聚合与连续物理时间解耦，建模不规则采样时空序列时依赖效率极低的数值微分方程求解器，无法作为通用替换层适配MLP、Transformer、GNN等各类主流架构。
### 方法关键点
提出DAWIN神经元，将空间投影与基于时间间隔的波激发耦合，通过闭式阻尼演化积分得到局部复数状态，无需数值求解器；证明原子波积分的结合性，基于Triton实现DAWINLinear算子，并行深度为O(log L)，无串行递归瓶颈。
### 关键结果
11个参数匹配的任务中，9个优于Neural CDE，8个优于ReLU-MLP；临床动态预测NRMSE达0.9531，死亡率预测AUROC达0.9993；NVIDIA B200 GPU上推理较串行实现最高加速2630倍，相比Mamba峰值显存最高降低97.6%

---
title: Curvature-Aware Zeroth-Order Optimization for Memory-Efficient Test-Time Adaptation
title_zh: 面向内存高效测试时自适应的曲率感知零阶优化方法
authors:
- Junming Zhang
- Shuyu Yin
- Peilin Liu
- Rendong Ying
- Fei Wen
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2608.12279'
url: https://arxiv.org/abs/2608.12279
pdf_url: https://arxiv.org/pdf/2608.12279
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: 测试时自适应 · 零阶优化
tags:
- Test-Time Adaptation
- Zeroth-Order Optimization
- Hessian Estimation
- On-Device Deployment
- Memory Efficiency
one_liner: 提出曲率感知零阶优化方法，实现仅前向测试时自适应的精度与内存效率SOTA平衡
practical_value: '- 端侧部署的推荐/Agent小模型遇到域漂移时，可采用CAZO的仅前向零阶优化方案替代BP微调，大幅降低端侧内存占用

  - 零阶优化梯度估计方差大的问题，可复用滑动平均估计对角Hessian构造协方差矩阵做各向异性扰动采样的trick，提升估计精度

  - 做业务模型测试时自适应可参考「冻结主模型权重+仅优化adapter参数+零阶梯度估计」的架构，平衡适配效果和部署成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有测试时自适应（TTA）方案多依赖反向传播（BP）微调，端侧部署时内存与计算开销过高；无需BP的零阶（ZO）优化仅需前向计算，但梯度估计方差大、适配效果差。
### 方法关键点
1. 核心观测：TTA过程中损失的Hessian存在持续低秩结构
2. 提出CAZO方法：通过滑动平均估计对角Hessian构造协方差矩阵，采用各向异性扰动采样降低梯度估计方差
3. 架构设计：冻结预训练模型权重，仅优化极少量adapter参数，全程仅依赖前向传播完成适配
### 关键结果
实验效果显著优于现有TTA方法，达到SOTA精度，内存开销远低于基于BP的TTA方案

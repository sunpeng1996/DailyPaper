---
title: Learning Anisotropic Prediction Targets for Flow Models
title_zh: 面向流生成模型的各向异性可学习预测目标方法
authors:
- Rayhan Zirvi
- Hansheng Chen
- Gordon Wetzstein
- Leonidas Guibas
affiliations:
- Stanford University
- California Institute of Technology
arxiv_id: '2611.17767'
url: https://arxiv.org/abs/2611.17767
pdf_url: https://arxiv.org/pdf/2611.17767
published: '2026-11-12'
collected: '2026-11-19'
category: Training
direction: 生成模型训练 · 流模型优化
tags:
- Flow Model
- Generative Model
- Training Optimization
- Prediction Target
- Quantization
one_liner: 为流生成模型引入可学习各向异性预测目标，无需改架构即可提升生成质量减少推理artifact
practical_value: '- 生成式推荐、电商文案生成场景可复用可学习预测目标思路，替换固定噪声/干净样本预测目标，无需改模型架构即可提升生成质量，额外训练成本极低

  - 低精度推理降本场景（如端侧推荐模型部署、大模型推理量化），可引入各向异性权重优化预测目标条件数，消除量化带来的输出 artifacts，保障低精度推理效果

  - 用户/物品语义表征建模时，可参考各维度权重与数据方差线性对齐的结论，自适应调整不同表征维度的损失权重，降低模型预测难度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
流生成模型传统采用人工预设的固定预测目标（如速度、噪声、干净数据），目标选择直接决定训练效率与生成样本质量，固定目标无法适配不同数据分布的特性。

### 方法关键点
1. 提出AnisoFlow，将固定预测目标替换为全可学习的各向异性目标，在联合学习的基空间中为每个方向分配独立非负权重缩放噪声分量
2. 支持通过闭式映射从网络预测中精确恢复速度，无需改动原有模型架构、流匹配损失与采样器，仅优化预测目标即可降低网络预测难度
3. 理论证明各方向最优噪声权重与对应维度的数据方差近似线性相关，与实验观测一致

### 关键结果
- ImageNet 256×256生成任务上，仅优化预测目标无需改架构，相比JiT基线FID从1.90降至1.55
- 像素空间文生图任务中，FP8块量化推理下基本消除基线存在的块接缝artifact，同时提升整体生成图像质量

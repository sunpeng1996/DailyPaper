---
title: 'H3DNAS: Hardware-Aware ONNX-Native 3D Point Cloud Model Compression'
title_zh: H3DNAS：硬件感知的原生ONNX 3D点云模型压缩框架
authors:
- Anchit Mulye
- Rhythm Baghel
- Sujay Kumar Ingle
- Hardik Jain
affiliations:
- Indian Institute of Technology Jodhpur
arxiv_id: '2609.02684'
url: https://arxiv.org/abs/2609.02684
pdf_url: https://arxiv.org/pdf/2609.02684
published: '2026-09-02'
collected: '2026-09-04'
category: Other
direction: 模型压缩 · ONNX原生硬件感知优化
tags:
- Model Compression
- ONNX
- Neural Architecture Search
- Edge Deployment
- 3D Point Cloud
one_liner: 无需原模型源码直接基于ONNX计算图的硬件感知3D点云模型压缩框架，大幅减参提效且精度损失可忽略
practical_value: '- 若业务涉及AR/3D商品建模、3D商品识别等点云模型边缘部署需求，可直接复用H3DNAS无源码ONNX压缩流水线，大幅降低第三方模型适配门槛

  - 基于输出保真度的零样本无标注候选模型排序策略，可迁移到其他缺乏训练标注的模型压缩场景，降低数据依赖

  - 通道依赖图的拓扑不变压缩上限计算方法，可用于任意ONNX格式模型的压缩潜力预评估，避免无效优化尝试'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
3D点云模型在Jetson Orin Nano等边缘硬件部署受算力、内存限制严重，现有压缩方法要求获取模型原源码，无法直接处理厂商/开源库分发的ONNX格式二进制模型。

### 方法关键点
1. 构建通道依赖图（CDG），将ONNX算子分为4类约束，证明自由参数占比$\rho_f$为拓扑不变量，可在$\mathcal{O}(|V|+|E|)$复杂度下计算理论压缩上限；
2. 采用两阶段分层搜索：先通过$L_1$重要性通道选择剪枝候选架构，再用无标注零样本输出保真度排序，对帕累托最优候选应用GhostConv结构突变；
3. 整个流程仅通过ONNX图外科手术实现，无需原模型架构定义、源码或梯度访问。

### 关键结果
在ModelNet40数据集上，对PointNet、PointNet++、PointMLP分别减参65.5%、43.2%、49.1%，推理提速1.99×、1.29×、1.67×，精度损失可忽略。

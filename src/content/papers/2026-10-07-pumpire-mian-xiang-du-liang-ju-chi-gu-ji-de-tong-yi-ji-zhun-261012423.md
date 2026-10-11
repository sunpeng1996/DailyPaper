---
title: 'Pumpire: Unified Benchmark for Metric Distance Estimation'
title_zh: Pumpire：面向度量距离估计的统一基准
authors:
- Siyu Chen
- Zehan Wang
- Jiayang Xu
- Yihan Wu
- Jialei Wang
- Junming Chen
- Ziang Zhang
- Yutong Ying
- Zhou Zhao
affiliations:
- Zhejiang University
- Zhejiang University of Technology
- Shanghai Jiaotong University
arxiv_id: '2610.12423'
url: https://arxiv.org/abs/2610.12423
pdf_url: https://arxiv.org/pdf/2610.12423
published: '2026-10-07'
collected: '2026-10-11'
category: Other
direction: 3D基础模型 · 度量距离估计评估
tags:
- 3D Foundation Model
- Benchmark
- Metric Distance Estimation
- Evaluation Protocol
- Real-world Dataset
one_liner: 推出Pumpire统一基准及6k帧标注数据集，可直接评估3D基础模型的点对距离估计能力
practical_value: '- 做3D商品展示/AR试穿/AR家装场景的业务，可复用其点对距离误差评估逻辑，校验3D重建模型的物理尺寸准确性，避免虚拟商品尺寸和实际不符的用户投诉

  - 开发空间感知类Agent（如线下导购Agent、仓储巡检Agent）的团队，可引入该基准的评估范式，验证3D感知模块的度量精度，降低空间导航/操作失误率

  - 涉及多模态大模型空间推理能力评估的业务，可参考其直接度量物理尺度的评估思路，替代传统仅看几何相似度的间接评估方法'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有3D基础模型评估多单独测算深度、相机内参，或通过几何相似度指标评估点云，无法直接反映点到点距离估计能力，而该能力是空间感知类系统的核心基础，此前评估范式存在明显缺口。

### 方法关键点
1. 构建Pumpire-6k数据集，覆盖100个真实场景，每个场景标注经物理测量的点对距离，单场景含64帧，总规模6400帧；
2. 设计统一评估协议，同时支持图像级、视频级3D基础模型评估，兼容带/不带深度先验的多场景横向对比，直接输出点对距离误差指标。

### 关键结果
完成29种主流3D基础模型配置的基准测试，输出了各模型在距离估计任务上的全面性能分析结果。

---
title: ANTShapes Benchmarking Datasets for Event-Based Neuromorphic Object Classification
title_zh: ANTShapes：面向事件驱动神经形态目标分类的基准数据集
authors:
- M. Middleton
- H. Kayan
- B. Sen Bhattacharya
- T. Ali
- E. Baikas
- M. Vousden
- C. Perera
- O. Rhodes
- E. Gheorghiu
- M. A. Trefzer
affiliations:
- University of York, UK
- Cardiff University, UK
- University of Manchester, UK
- University of Stirling, UK
- University of Southampton, UK
arxiv_id: '2608.27150'
url: https://arxiv.org/abs/2608.27150
pdf_url: https://arxiv.org/pdf/2608.27150
published: '2026-08-27'
collected: '2026-08-31'
category: Other
direction: 神经形态计算 · 事件视觉数据集构建
tags:
- SNN
- Neuromorphic Computing
- Event-based Vision
- Dataset
- Benchmark
one_liner: 基于ANTShapes工具生成4个不同难度的事件驱动视觉数据集，验证工具生成数据的可用性
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统帧基相机+云端计算的事件目标分类方案存在设备体积/功耗高、云端数据传输有隐私风险、延迟高、强依赖网络连接的缺陷，SNN+神经形态硬件可有效解决上述问题，但当前事件视觉分类研究缺乏高质量标注数据集支撑。
### 方法关键点
基于已有的ANTShapes仿真工具生成4个不同难度的标注事件视觉数据集，采用卷积SNN作为基准分类模型，与N-MNIST、CIFAR10-DVS等4个业内常用脉冲数据集进行性能对比验证。
### 关键结果
验证了ANTShapes工具生成的数据集满足事件视觉研究的要求，产出的4个不同难度的新数据集可直接用于后续事件驱动目标分类相关实验。

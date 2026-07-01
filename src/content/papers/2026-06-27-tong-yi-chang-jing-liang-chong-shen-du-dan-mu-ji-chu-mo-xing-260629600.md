---
title: 'One Scene, Two Depths: Probing Geometric Ambiguity in Monocular Foundation
  Models'
title_zh: 同一场景两种深度：单目基础模型的几何歧义性探究
authors:
- Xiaohao Xu
- Feng Xue
- Xiang Li
- Haowei Li
- Shusheng Yang
- Tianyi Zhang
- Matthew Johnson-Roberson
- Xiaonan Huang
affiliations:
- University of Michigan, Ann Arbor
- Carnegie Mellon University
- New York University
- Vanderbilt University
arxiv_id: '2606.29600'
url: https://arxiv.org/abs/2606.29600
pdf_url: https://arxiv.org/pdf/2606.29600
published: '2026-06-27'
collected: '2026-07-01'
category: Other
direction: 单目深度估计 · 基础模型几何歧义分析
tags:
- Monocular Depth Estimation
- Visual Prompting
- Foundation Model
- 3D Scene Understanding
- Benchmark
one_liner: 提出MD-3k双层深度基准，验证免训练拉普拉斯视觉提示可大幅提升单目深度模型多层空间关系识别精度
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
单目深度估计默认每个像素仅输出一个深度标量，在存在透明物体等多层几何结构的场景下，同一相机射线可同时穿过前景、背景，标注深度受标注规则、训练数据约束，并非场景固有真值，现有模型的深度层选择偏好缺乏统一度量标准。
### 方法关键点
1. 构建MultiDepth-3k（MD-3k）稀疏双层序贯基准，用于量化深度模型的层偏好与多层空间关系准确率（ML-SRA）；
2. 提出免训练的拉普拉斯视觉提示（LVP）光谱输入变换方法，无需微调即可改变冻结深度模型的输出深度层选择。
### 关键结果数字
主流单目深度基础模型在标准RGB输入下的层偏好差异显著；最优RGB+LVP组合DAv2-L的ML-SRA可达75.5%，验证不同深度模型可互补表达标准RGB推理未覆盖的几何假设。

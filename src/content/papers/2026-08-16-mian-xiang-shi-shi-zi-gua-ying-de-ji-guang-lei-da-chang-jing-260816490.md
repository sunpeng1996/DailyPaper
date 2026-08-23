---
title: Towards Real-Time and Adaptable LiDAR Scene Completion
title_zh: 面向实时自适应的激光雷达场景补全方法
authors:
- Azhar Hussian
- Martin Vossiek
- Vasileios Belagiannis
affiliations:
- Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany
arxiv_id: '2608.16490'
url: https://arxiv.org/abs/2608.16490
pdf_url: https://arxiv.org/pdf/2608.16490
published: '2026-08-16'
collected: '2026-08-23'
category: Other
direction: 自动驾驶3D感知 · LiDAR场景补全
tags:
- LiDAR
- 3D Scene Completion
- Autonomous Driving
- Real-time Perception
- BEV Feature
one_liner: 提出RapidLiDAR架构，精度持平SOTA的同时比现有最快方法提速2.3倍，匹配车载LiDAR 10Hz采集要求
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有LiDAR场景补全的初始化-优化范式存在两大痛点：生成式方法需迭代优化高斯噪声，速度慢无法满足实时要求；非生成式方法用固定噪声扰动输入点，大缺口/遮挡区域补全能力差，新传感器配置需手动重校准参数。

### 方法关键点
1. 提出数据驱动的自适应初始化模块，对每个输入点预测空间可变位移，将稀疏观测扩展为适配局部几何的粗场景初始化，无需手动调优噪声参数；
2. 设计多尺度重构模块，查询输入扫描构建的多尺度3D体素、2D BEV特征图，进一步优化点位置提升补全精度；
3. 替换最远点采样、kNN等点邻域算子为体素/BEV特征提取，天然支持多分辨率输入，推理速度显著提升。

### 关键结果
在SemanticKITTI、KITTI-360数据集上补全精度持平SOTA，单场景补全耗时0.1s，比现有最快方法快2.3倍，匹配车载LiDAR 10Hz采集速率。

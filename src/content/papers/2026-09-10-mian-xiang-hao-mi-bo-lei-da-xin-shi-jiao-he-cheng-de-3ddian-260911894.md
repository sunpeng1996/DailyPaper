---
title: 3D Point Splatting for mmWave Radar Novel View Synthesis
title_zh: 面向毫米波雷达新视角合成的3D点溅射方法
authors:
- Adnan Armouti
- Yixuan Gao
- Rajalakshmi Nandakumar
affiliations:
- Cornell Tech
arxiv_id: '2609.11894'
url: https://arxiv.org/abs/2609.11894
pdf_url: https://arxiv.org/pdf/2609.11894
published: '2026-09-10'
collected: '2026-09-13'
category: Other
direction: 毫米波雷达感知 · 新视角合成
tags:
- mmWave Radar
- Novel View Synthesis
- 3D Point Splatting
- Differentiable Renderer
- Perception
one_liner: 提出首个雷达专用可微点渲染器3DPS，同时满足物理保真、复值输出、多视角可扩展三大要求
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有毫米波雷达新视角合成（NVS）方法无法同时满足物理保真、复值输出、多视角可扩展三大核心要求：可微蒙特卡洛光线追踪物理准确且支持复值输出，但多视角优化效率低、扩展性差；从光学NVS迁移的NeRF、3D高斯等方案训练速度快，但丢失相位信息、无显式材质建模，仅能输出功率级距离-方位（RA）幅值，适用场景受限。

### 方法关键点
1. 直接基于雷达方程的标准立体角形式推导3DPS，是首个雷达专用可微点渲染器，物理一致性高
2. 每个带朝向的3D点搭载ITU-R P.2040材质模型，闭式计算后将复相量通过预计算点扩散函数（PSF）溅射至距离仓
3. 输出为通用复值，同一优化场景可经标准FFT pipeline生成ADC、CRP、RA多格式输出，无需针对不同格式重训

### 关键结果
- 6个户外ColoRadar场景测试中，保留RA图像的平均皮尔逊相关系数达0.587，是3个光学NVS基线的1.7~5.2倍
- 单RTX 4090上单场景训练耗时仅约3分钟

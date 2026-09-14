---
title: Guided Super-Resolution of Digital Elevation Models with Diffusion-Based Image
  Generators
title_zh: 基于扩散图像生成器的数字高程模型引导式超分辨率
authors:
- Armand Mihai Nicolicioiu
- Dominik Narnhofer
- Nando Metzger
- Daniel Panangian
- Ksenia Bittner
- Konrad Schindler
affiliations:
- Photogrammetry and Remote Sensing, ETH Zürich
- Remote Sensing Technology Institute, German Aerospace Center (DLR)
arxiv_id: '2609.11886'
url: https://arxiv.org/abs/2609.11886
pdf_url: https://arxiv.org/pdf/2609.11886
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 扩散模型 遥感超分辨率与多源数据融合
tags:
- Diffusion Model
- Super-Resolution
- Data Fusion
- Remote Sensing
- DSM
one_liner: 利用高分辨率光谱图像引导扩散模型，实现5m DSM到0.5m的超分辨率重建，效果优于传统方法
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.CV
depth: abstract
---

### 动机
高分辨率DSM在城市分析、3D建筑重建、基础设施监测等场景价值极高，但数据采集成本高、复杂度高导致覆盖度不足，而商用粗分辨率DSM与高分辨率光学影像获取门槛低，二者存在明显分辨率 mismatch。

### 方法关键点
- 提出引导式DSM超分辨率方案，以高分辨率光谱图像为引导信号，基于去噪扩散模型将图像中独有的清晰轮廓、精细化屋顶结构等信息迁移到高程图中
- 替代传统插值、滤波类超分辨率方案，还原更精准的地表细节

### 关键结果数字
在中欧多个城市数据集上验证，可将5m分辨率DSM直接提升到0.5m分辨率，重建结果的结构细节丰富度、表面几何精度均显著优于传统方法

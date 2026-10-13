---
title: Gaussian Splatting with Reflections Guided by What is Seen
title_zh: 结合可见信息引导反射建模的高斯溅射方法
authors:
- Yiming Liang
- Tianyu Xiao
- Hiroshi Ishikawa
affiliations:
- Waseda University, Japan
arxiv_id: '2610.13757'
url: https://arxiv.org/abs/2610.13757
pdf_url: https://arxiv.org/pdf/2610.13757
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 新视角合成 · 反射场景高斯溅射优化
tags:
- 3D Gaussian Splatting
- Novel View Synthesis
- Specular Reflection
- 2D Gaussian Splatting
one_liner: 提出基于2DGS的框架，融合可见环境信息与混合反射表示，提升近场反射场景的渲染质量与几何精度
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有NeRF、3D Gaussian Splatting等新视角合成方法在普通场景表现优异，但难以捕捉视角依赖的镜面效果，尤其近场反射场景建模精度差；现有方案要么采用仅能表示无穷远光源的环境贴图，要么仅依赖反射的间接监督，无法满足高精度建模需求。
### 方法关键点
1. 基于2D Gaussian Splatting框架，直接复用输入图像中可观测的环境信息作为监督信号；
2. 融合混合反射外观表示与视角依赖的镜面建模模块。
### 关键结果
在公开基准与新构建的近场反射数据集上，渲染质量与几何精度均显著优于现有基线方法。

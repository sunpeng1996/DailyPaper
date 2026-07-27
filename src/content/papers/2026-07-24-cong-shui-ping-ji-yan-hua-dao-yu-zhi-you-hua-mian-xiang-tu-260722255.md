---
title: 'From level set evolution to threshold optimization: A grayscale level set
  framework for image segmentation'
title_zh: 从水平集演化到阈值优化：面向图像分割的灰度水平集框架
authors:
- Xingkai Li
- Jiebao Sun
- Fanghui Song
- Zhichang Guo
affiliations:
- School of Mathematics, Harbin Institute of Technology
arxiv_id: '2607.22255'
url: https://arxiv.org/abs/2607.22255
pdf_url: https://arxiv.org/pdf/2607.22255
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 图像分割 · 退化图像快速处理
tags:
- image-segmentation
- level-set
- threshold-optimization
- degraded-image
- fast-inference
one_liner: 证明水平集长度正则项非必要，提出将PDE演化转为阈值搜索的退化图像快速分割框架
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有水平集图像分割方法普遍引入长度正则项约束分割轮廓几何形状，易引发数值不稳定、计算开销过高问题，无法适配强噪声、强度不均等多退化场景的高效分割需求。
### 方法关键点
1. 理论证明特定平滑约束下长度正则项非必要，且其存在会破坏$|\nabla φ|=1$的性质；
2. 定义平滑图像类别，构建灰度水平集，将传统PDE演化过程转换为一维阈值搜索，大幅降低计算复杂度。
### 关键结果
在各类退化图像上验证了分割精度表现，针对大规模图像的推理速度相比传统水平集方法有显著优势，同时解决了原有方法的数值不稳定问题。

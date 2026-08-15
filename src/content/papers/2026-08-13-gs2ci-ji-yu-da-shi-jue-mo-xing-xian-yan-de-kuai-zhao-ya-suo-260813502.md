---
title: 'GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via
  Large Vision Model Priors'
title_zh: GS²CI：基于大视觉模型先验的快照压缩成像鲁棒高斯溅射方法
authors:
- Yanming Yang
- Chenxi Song
- Ping Wang
- Xin Yuan
- Chi Zhang
affiliations:
- Westlake AGI Lab
arxiv_id: '2608.13502'
url: https://arxiv.org/abs/2608.13502
pdf_url: https://arxiv.org/pdf/2608.13502
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 计算机视觉 · 3D场景重建
tags:
- 3D Gaussian Splatting
- Snapshot Compressive Imaging
- Vision Foundation Model
- 3D Reconstruction
one_liner: 结合3D高斯溅射与大视觉模型先验，实现单张SCI测量的高质量3D场景重建
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于快照压缩成像（SCI）的3D场景重建方法受信息丢失、视角多样性不足、3D表示与相机位姿联合优化计算负担重的限制，性能和稳定性不佳。

### 方法关键点
1. 融合3D Gaussian Splatting（3DGS）与大视觉基础模型（VFM）先验，先基于测量导出的3D VFM初始化结果做SCI感知的高斯粗优化
2. 粗阶段收敛后，引入辅助2D VFM为合成视角提供伪视角监督，实现局部外观精修
3. 提出OSGR专属致密化策略：通过局部不透明度统计扩充分裂候选、均值不透明度正则抑制不透明度异常膨胀、显式约束控制高斯数量上限，解决3DGS优化不稳定问题

### 关键结果
多基准数据集测试下整体性能最优，重建质量、视角变化鲁棒性领先，计算效率具备竞争力。

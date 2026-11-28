---
title: 'DynMF2: Rigid Motion Factorization by Expectation-Maximization for Monocular
  4D Reconstruction and Motion Segmentation'
title_zh: DynMF2：基于EM算法的单目4D重建与运动分割刚性运动因子分解
authors:
- Agelos Kratimenos
- Yile Hua
- Kostas Daniilidis
affiliations:
- University of Pennsylvania
- Robotics Institute, Athena RC
arxiv_id: '2611.34931'
url: https://arxiv.org/abs/2611.34931
pdf_url: https://arxiv.org/pdf/2611.34931
published: '2026-11-25'
collected: '2026-11-28'
category: Other
direction: 4D视觉 · 无监督运动分割与单目重建
tags:
- 4D_Reconstruction
- Motion_Segmentation
- EM_Algorithm
- Monocular_Vision
- Rigid_Motion
one_liner: 提出无掩码EM框架的刚性运动因子分解方法，实现单目视频4D重建与无监督运动分割
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单目随手拍摄视频的动态场景重建存在深度歧义，现有基于掩码的方法易丢失细薄结构、远背景小运动物体等细节，依赖预标注掩码部署灵活性差。
### 方法关键点
1. 基于Expectation-Maximization框架实现刚性运动因子分解，M步闭式求解每个SE(3)运动轨迹对应的点集参数，E步将3D点重分配到重构误差最小的运动轨迹，背景直接归为相机自身运动无需额外掩码输入；
2. 新增requery补全跟踪遗漏点、merge合并共运动轨迹、split拆分非共运动轨迹三个后处理步骤，自适应匹配场景实际运动数量，无需预先定义运动类别。
### 关键结果
无需掩码前提下，iPhone、NVIDIA数据集视图合成效果显著优于掩码基线，iPhone数据集3D跟踪精度领先；无训练分割任务的情况下，MOVi-F、iTACO数据集运动分割效果达到竞争基准水平。

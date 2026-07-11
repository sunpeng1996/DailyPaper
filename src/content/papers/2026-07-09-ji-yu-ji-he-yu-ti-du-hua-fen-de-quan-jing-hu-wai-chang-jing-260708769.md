---
title: Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction
title_zh: 基于几何与梯度划分的全景户外场景重建方法
authors:
- Weijian Chen
- Weibo Yao
- Yuhang Zhang
- Xiaolin Tang
- Guo Wang
- Weijun Zhang
- Xitong Gao
- Yihao Chen
- Hongde Qin
- Lu Qi
affiliations:
- Insta360 Research
- Sun Yat-sen University
- South China University of Technology
- University of Chinese Academy of Sciences
- Harbin Engineering University
arxiv_id: '2607.08769'
url: https://arxiv.org/abs/2607.08769
pdf_url: https://arxiv.org/pdf/2607.08769
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 3D高斯泼溅 · 大规模全景场景重建
tags:
- 3D Gaussian Splatting
- Panoramic Reconstruction
- 3D Reconstruction
- Block-wise Training
- Dataset
one_liner: 提出适配全景3DGS的分块训练框架PanoLOG，配套首个大规模户外全景重建基准数据集Pano360
practical_value: '- 梯度重要性评分分配计算资源的思路，可迁移到大规模LLM/推荐模型的分块并行训练场景，降低全局训练开销

  - 粗阶段引入弱监督先验保证基础效果、精阶段自适应调优的两阶段范式，可复用在多阶段推荐排序、Agent任务规划流程中

  - 若业务涉及3D商品展示、VR探店、AR试穿等场景，可直接复用全景深度监督、天空球建模的工程trick，也可复用开源Pano360数据集做预训练'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
3D Gaussian Splatting (3DGS) 拓展到大规模户外场景时，数据采集、计算成本双高；全景图像虽可通过360°视域降低采集量，但全视野特性会导致传统基于局部相机视锥体的分块策略失效，分块优化直接退化为全局训练，效率极低。
### 方法关键点
1. 两阶段粗到细框架PanoLOG：粗阶段引入天空球建模+全景单目深度监督，生成可靠初始几何结构
2. 几何+梯度联合划分策略G²PS：精阶段通过视差驱动的不确定性构建自适应边界体积，基于梯度重要性评分给各分块分配对应相机，实现块级并行训练
3. 开源Pano360数据集：首个大规模户外全景场景重建基准数据集
### 关键结果
G²PS渲染质量达SOTA，同时支持可扩展的块并行训练，代码、模型、数据集全部公开

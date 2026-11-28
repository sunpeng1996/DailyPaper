---
title: A Mesh for Every Moment
title_zh: MEMO：面向动态4D场景的逐帧高精度网格重建方法
authors:
- Roy Or-El
- Jeong Joon Park
- Ira Kemelmacher-Shlizerman
affiliations:
- University of Washington
- University of Michigan
arxiv_id: '2611.34939'
url: https://arxiv.org/abs/2611.34939
pdf_url: https://arxiv.org/pdf/2611.34939
published: '2026-11-24'
collected: '2026-11-28'
category: Other
direction: 4D动态场景 高斯泼溅几何重建
tags:
- Gaussian Splatting
- 4D Reconstruction
- Dynamic Scene
- Mesh Extraction
- Novel View Synthesis
one_liner: 提出基于时序高斯核的4D动态重建方法MEMO，支持任意时刻网格提取，几何重建精度达SOTA
practical_value: '- 电商3D商品动态展示场景：可复用MEMO方法生成服装、饰品等动态展示的逐帧高精度3D网格资产，降低3D内容制作成本

  - AR试穿/虚拟直播间场景：MEMO的轨迹初始化方案可适配人体快速运动场景，提升动态几何重建的稳定性与精度

  - 3D内容生成相关业务可直接复用其无需额外网格融合步骤的高斯场导出网格逻辑，简化管线复杂度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有动态高斯泼溅方法存在三类缺陷：仅建模外观无法输出几何、仅支持经掩码分割的孤立对象、依赖固定网格的TSDF/泊松重建导致几何细节损失，且普遍未适配实际采集常见的大位移快速运动场景。
### 方法关键点
1. 核心采用高斯过程启发的逐高斯运动模型，将每个高斯的位置、旋转时序变化表示为时序高斯核的组合，全程保持高斯为有效表面元素，可直接从高斯场导出任意时刻的网格，无需额外融合步骤
2. 设计基于点轨迹的初始化方案，通过闭式解拟合高斯初始轨迹，适配快速大运动场景
### 关键结果
在自建含9个动画场景的Blender-Moments基准、2个真实数据集上测试，几何重建精度优于所有SOTA方法，新视角合成效果、训练速度与现有主流方法持平。

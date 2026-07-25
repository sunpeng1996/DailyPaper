---
title: 'GEAR: Reconstruction of Classical Paintings via Geometry Grounding and Appearance
  Restitution'
title_zh: GEAR：基于几何对齐与外观复原的古典绘画3D重建
authors:
- Qinyu Zhang
- Xinda Liu
- Yunchen Li
- Yunzhuo Liu
- Chenxi Hu
- Kang Li
- Guohua Geng
affiliations:
- Northwest University
arxiv_id: '2607.17519'
url: https://arxiv.org/abs/2607.17519
pdf_url: https://arxiv.org/pdf/2607.17519
published: '2026-07-20'
collected: '2026-07-25'
category: Multimodal
direction: 多模态 · 单幅古典绘画3D重建
tags:
- 3D Reconstruction
- Training-free
- Multimodal Generation
- Benchmark
- 3D Gaussian Splatting
one_liner: 提出无训练两阶段3D重建框架GeAR，配套CP3D任务与10k级绘画基准数据集
practical_value: '- 针对非自然图像（如电商手绘商品图、国风宣传素材）的3D重建可复用两阶段思路：先补全几何光照提示提升3D高斯重建稳定性，再还原原始风格纹理

  - 训练免微调的跨模态生成框架设计可迁移到小样本商品3D建模场景，大幅降低定制化训练成本

  - 领域特定基准构建逻辑可复用：针对小众业务场景先搭建标准化测试集，再迭代算法优化方向'
score: 5
source: arxiv-cs.MM
depth: abstract
---

### 动机
古典绘画具备高文化价值，转为可交互3D场景可支撑数字典藏、沉浸展览等场景，但现有基于自然图像先验的3D重建方法无法适配绘画弱透视、弱深度、风格化的特征，难以同时保证几何合理性与原作出处观保真度。
### 方法关键点
1. 定义全新CP3D任务，目标为单幅古典绘画输入下同时满足几何合理、外观贴合原画、新视角合成自然
2. 提出无训练两阶段框架GeAR：先将输入转换为带连贯光照、着色的几何对齐表示，提升3D高斯重建稳定性；再在空间、多视角一致性约束下还原原画笔触与风格细节
3. 构建包含10160张高分辨率古典画作的HeriArch基准数据集支撑任务评测
### 关键结果
实验与用户研究显示，GeAR在几何合理性、外观保真度、用户偏好度三类指标上均显著优于现有SOTA基线。

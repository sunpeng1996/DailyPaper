---
title: 'M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View
  Synthesis'
title_zh: M3GD：面向相机-激光雷达新视角合成的多模态多视角几何扩散模型
authors:
- Yang Zhou
- Jiuhong Xiao
- Shizhao Ye
- Long Quang
- Carlos Nieto-Granda
- Giuseppe Loianno
arxiv_id: '2609.30056'
url: https://arxiv.org/abs/2609.30056
pdf_url: https://arxiv.org/pdf/2609.30056
published: '2026-09-24'
collected: '2026-09-27'
category: Multimodal
direction: 多模态 · 跨传感器新视角合成
tags:
- Multimodal Fusion
- Novel View Synthesis
- Diffusion Model
- LiDAR
- Foundation Model
one_liner: 无需预训练跨模态翻译器，融合2D图像与3D点云预训练模型实现相机-激光雷达新视角合成
practical_value: '- 跨模态特征融合可参考：无需单独预训练跨模态翻译器，利用空间/语义对齐的天然关联直接融合不同模态预训练模型的冻结特征，降低训练成本

  - 生成模型条件注入可复用：用轻量residual adapter注入额外模态条件，保留主干模型原有结构、训练目标不变，大幅降低适配开发量

  - 线上部署可参考：通过调整推理步数等超参数实现质量-算力成本的可控权衡，适配不同业务场景的算力配额要求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
机器人新视角合成(NVS)需同时还原视觉外观与度量3D结构，现有生成式NVS方法大多仅依赖图像输入，忽略机器人平台标配的LiDAR传感器互补信息，传统跨模态融合方案需额外预训练跨模态翻译器，训练成本高。
### 方法关键点
1. 直接组合独立预训练的2D图像、3D点云基础模型，无需单独预训练跨模态翻译器；利用相机投影后冻结LiDAR与图像特征的共享空间结构，天然构建跨模态表示；2. 将显式几何统计与点云描述符合并为图像隐空间网格上的视角对齐包，通过轻量残差适配器注入多视角流匹配生成器，全程保留主干模型的隐空间、解码器、训练目标不变。
### 关键结果
在GrandTour数据集上，相比同主干的纯图像版本，目标视角RGB与深度合成效果显著提升；消融实验验证收益来自像素对齐的LiDAR内容，目标视角LiDAR可作为几何查询关联请求视角与源观测；地面机器人部署验证落地性，可通过欧拉积分步数灵活配置质量-算力权衡。

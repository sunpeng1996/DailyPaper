---
title: 'HairDeck: Animation-Ready Stylized Hair Cards from a Single Image'
title_zh: HairDeck：单张图像生成可直接驱动动画的风格化发片资产
authors:
- Yuze He
- Yixiang Wei
- Wang Zhao
- Chuhao Chen
- Yanning Zhou
- Yong-Jin Liu
affiliations:
- Tsinghua University
- Carnegie Mellon University
- The Chinese University of Hong Kong
arxiv_id: '2610.40599'
url: https://arxiv.org/abs/2610.40599
pdf_url: https://arxiv.org/pdf/2610.40599
published: '2026-10-28'
collected: '2026-10-31'
category: Other
direction: 单图3D资产生成 · 风格化发型建模
tags:
- 3D Generation
- Diffusion Transformer
- Digital Human
- Content Creation
- Computer Vision
one_liner: 用集合扩散Transformer并行生成发片token，单图输出可动风格化头发资产，精度速度远超现有SOTA
practical_value: '- 虚拟主播/数字人带货场景可直接复用该方案快速生成风格化发型资产，大幅降低美术制作成本

  - 无序集合类生成任务可借鉴「单原子元素映射为单个token+集合扩散Transformer并行生成」思路，替代自回归生成大幅提升推理速度

  - UGC互动电商平台可接入该能力，支持用户上传头像一键生成可动数字人形象，提升玩法趣味性与用户停留时长'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有唯一的风格化发片生成方案CHARM采用自回归解码控制点序列，速度慢、精度低，无法满足游戏/虚拟人资产快速生产需求；传统图像转3D方案仅能输出融合网格，无法生成可直接用于动画的结构化发片资产。

### 方法关键点
1. 将发型建模为无序的艺术家定义基元集合，每张发片映射为单个token，消除自回归生成的序列依赖
2. 基于集合扩散Transformer并行对所有发片token去噪，同时生成发片结构与驱动动画的弹簧骨链，输出可直接导出到下游工具的即用资产。

### 关键结果
在CHARM官方测试集上，Chamfer距离降低44%，发片朝向误差减半，推理速度提升33倍；单图生成效果全面优于CHARM、传统图像转3D管线、基于发丝的建模方法。

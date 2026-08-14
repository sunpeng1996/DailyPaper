---
title: 'Learning How the World Evolves: Extrapolative Video World Models via Latent
  Dynamics Reasoning'
title_zh: 学习世界演化规律：基于隐空间动力学推理的可外推视频世界模型
authors:
- Haodong Li
- Shaoteng Liu
- Tianyu Wang
- Chongjian Ge
- Sihui Ji
- Jiahan Zhang
- Xin Lin
- Haolin Lu
- Zhe Lin
- Manmohan Chandraker
affiliations:
- UCSD
- Adobe
arxiv_id: '2608.09926'
url: https://arxiv.org/abs/2608.09926
pdf_url: https://arxiv.org/pdf/2608.09926
published: '2026-08-09'
collected: '2026-08-14'
category: Other
direction: 视频世界模型 · 隐空间动力学推理
tags:
- World Model
- Latent Dynamics
- Video Generation
- Out-of-Distribution Generalization
- Kinematics Integration
one_liner: 提出隐空间动力学推理LDR方法，实现首个可跨分布外推物理规律的视频世界模型
practical_value: '- 做用户行为序列/商品热度趋势预测时，可借鉴LDR显式动力学积分思路，仅回归高阶残差，降低建模难度同时提升OOD泛化性

  - 生成商品展示短视频/3D商品动态效果时，可复用结构化隐空间+动力学建模架构，减少参数同时提升生成速度与物理合理性

  - 做跨域推荐迁移时，可参考低阶规则显式建模+高阶残差学习的范式，缩小分布内与分布外的效果gap'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频扩散模型仅拟合像素分布，未建模帧间运动规律，生成画面视觉合理但不符合物理规则，完全无法泛化到训练分布外场景。
### 方法关键点
1. 提出Latent Dynamics Reasoning (LDR)：将隐空间转换建模为显式运动学积分，低阶动力学直接数值积分，模型仅回归驱动序列生成的三阶及以上残差
2. 选择结构化隐空间而非稠密卷积特征执行积分，进一步提升外推能力
### 关键结果
- 分布内/外误差差比视频扩散基线小20倍以上
- 参数量仅为基线的1/26，推理速度快143倍
- 仅用左移红球训练，可正确预测右移蓝方块、皮卡丘等完全OOD样本的运动规律，是首个可跨分布外推动力学的视频世界模型

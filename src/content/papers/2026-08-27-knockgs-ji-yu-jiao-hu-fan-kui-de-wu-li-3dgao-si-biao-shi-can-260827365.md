---
title: KnockGS:interaction-Grounded Calibrationof Physical Gaussian Representations
title_zh: KnockGS：基于交互反馈的物理3D高斯表示参数校准方法
authors:
- Chenchen Ge
- Hanwen Shen
- Bowen Jing
- Jiyuan Cai
- Xiaofeng Wang
- Hongsen Lei
- Weitao Zhou
- Dandan Zhang
- Haibao Yu
affiliations:
- Tuojing Intelligence
- Southeast University
- Stevens Institute of Technology
- Tsinghua University
- Imperial College London
arxiv_id: '2608.27365'
url: https://arxiv.org/abs/2608.27365
pdf_url: https://arxiv.org/pdf/2608.27365
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 3D重建 · 物理高斯表示参数校准
tags:
- 3D Gaussian Splatting
- Physics Simulation
- Parameter Calibration
- 3D Reconstruction
- Deformable Object
one_liner: 通过已知外力下的物体动态响应校准物理3D高斯表示的弹性与密度参数
practical_value: '- 面向AR/VR电商3D商品建模场景，可借鉴该方法校准柔性商品（服饰、玩具、家居软装等）的物理参数，还原真实交互动态效果

  - 需从观测动态反推物体物理属性的场景，可复用「外力刺激-提取时序响应特征-参数回归-模拟器回写验证」的闭环流程

  - 不涉及3D物理模拟的推荐/广告/Agent业务无直接迁移价值，无需重点关注'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有集成物理属性的3D高斯表示pipeline依赖已知或手动标注的材料参数，无法从观测到的物体动态反推对应参数，适用场景严重受限。
### 方法关键点
以已知外力作用下物体的动态响应作为校准信号，先从观测动态中提取时序响应特征，再基于特征估计3D高斯对象的弹性、密度系数，将估计得到的参数固化后回写至原模拟器，可直接支持未训练过的交互场景模拟。
### 关键结果
在5组留出材料目标上，参数恢复精度大幅优于响应检索、全局回归、固定默认材料三类基线，且固化的参数在不同方向、不同量级的交互下仍保持较高的预测准确性，可实现渲染外观与模拟响应一致的高斯资产校准。

---
title: 'GrainGS: Gradient-Decoupled Gaussian Splatting for Efficient Dynamic Novel
  View Synthesis'
title_zh: GrainGS：面向高效动态新视角合成的梯度解耦高斯溅射方法
authors:
- Jiahao He
- Yihua Shao
- Zhengkai Zhao
- Pan Gao
- Fei Ma
- Jingcai Guo
- Hao Tang
- Nicu Sebe
- Qi Tian
arxiv_id: '2607.21448'
url: https://arxiv.org/abs/2607.21448
pdf_url: https://arxiv.org/pdf/2607.21448
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 动态3D场景重建 · 神经渲染
tags:
- 3D Gaussian Splatting
- 4D Reconstruction
- Neural Rendering
- Dynamic View Synthesis
one_liner: 提出梯度解耦动态高斯框架GrainGS，兼顾动态场景重建精度、渲染效率与存储紧凑性
practical_value: '- 梯度解耦训练trick可复用：多任务联合训练时用stop-gradient阻断无关梯度通路，避免不同优化目标互相干扰，可直接适配推荐系统多目标优化场景

  - 分层锚点+细粒度偏移的架构设计可迁移：先预训练固定全局基础结构再学习局部微调偏移，适配生成式推荐中全局规则性+局部个性化的平衡需求

  - 基础-残差特征分解思路可借鉴：将稳定通用特征与动态变化特征分离建模，适合用户行为建模中长期兴趣与短期偏好的拆分训练'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
动态场景3D高斯溅射重建需同时平衡细粒度运动建模、结构稳定性、表示紧凑性三大需求，现有两类方案存在明显缺陷：per-primitive方法易出现基元冗余增长，锚点类方法以抑制局部可变运动为代价提升空间规整性，均无法兼顾三者。
### 方法关键点
1. 采用分层锚点骨架+逐高斯形变的融合框架，先通过静态预热阶段学习跨时间步的时间不变规范表示
2. 联合训练时引入stop-gradient操作阻断形变路径传递到规范位置的梯度，仅保留重建目标的直接优化通路，每个高斯独立预测位置、旋转、缩放的时间偏移，在结构约束下实现精细局部运动建模
3. 设计规范-残差外观分解机制建模帧相关光度变化，避免将光度差异强行纳入几何形变优化
### 关键结果
合成基准测试下平均PSNR达36.98dB，渲染速度435.6FPS，存储仅4.67MB，同时实现高重建质量、实时新视角合成与紧凑存储。

---
title: 'SM4RT: Cascaded Feed-forward Model for 4D Reconstruction'
title_zh: SM4RT：用于4D动态场景重建的级联前馈模型
authors:
- Pang-Chi Lo
- Jhao-Syun Lai
- Tsung-Wei Ke
affiliations:
- Carnegie Mellon University
- National Taiwan University
arxiv_id: '2611.08436'
url: https://arxiv.org/abs/2611.08436
pdf_url: https://arxiv.org/pdf/2611.08436
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 多模态4D动态场景重建
tags:
- 4D Reconstruction
- Cascaded Model
- Weakly Supervised Learning
- Dynamic Scene Understanding
- Geometry Reconstruction
one_liner: 提出级联前馈4D重建框架，先做3D几何重建再引导运动估计，降低相机运动带来的歧义
practical_value: '- 电商3D商品建模、AR试穿/试用场景可借鉴先重建静态3D几何再估计运动的级联范式，降低拍摄视角变动带来的误差

  - 标注数据不足的多任务建模场景，可复用跨时间步用已标注点位置正则化未标注点运动的弱监督损失设计

  - 多任务串联架构可参考，以前置任务输出作为后置任务先验，避免多任务互相干扰导致的性能trade-off

  - 纯搜索/推荐/广告算法业务场景无直接可复用点，仅对涉及3D/4D内容生成的相关业务有参考价值'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有前馈4D动态场景重建方法通常独立处理几何重建与运动估计，单坐标系下预测运动需额外适配相机位移，歧义性高，同时真实场景运动标注稀疏，模型训练难度大。
### 方法关键点
1. 采用级联多任务范式，先完成3D几何重建，再基于预测的结构引导后续运动估计；
2. 每个像素的3D运动在对应相机坐标系下表达，直接消除相机运动带来的预测歧义；
3. 引入弱监督损失，通过另一时间步的已标注点位置正则化未标注点的运动，缓解标注不足问题。
### 关键结果
在Kubric、Waymo、Point Odyssey 3个动态数据集的运动估计任务上，多数指标优于现有基线；在5个动态场景数据集的几何重建任务上，性能达到SOTA水平。

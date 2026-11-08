---
title: 'MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation'
title_zh: MOMASPLAT：面向移动操作的动态新视角演示增强框架
authors:
- Sateesh Kumar
- Arnav Balaji
- Arpit Bahety
- Skand Peri
- Georgios Pavlakos
- Roberto Martín-Martín
affiliations:
- University of Texas at Austin
arxiv_id: '2611.08372'
url: https://arxiv.org/abs/2611.08372
pdf_url: https://arxiv.org/pdf/2611.08372
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 移动机器人操作 · 演示数据增强
tags:
- 3D Gaussian Splatting
- Imitation Learning
- Novel View Synthesis
- Mobile Manipulation
- Data Augmentation
one_liner: 提出融合3D高斯溅射的动态新视角演示增强框架，大幅提升移动操作策略对未知位姿的鲁棒性
practical_value: '- 对输入视角/分布偏移敏感的下游任务（如多视角商品识别、AR试穿匹配）可参考「静态背景+动态对象分离建模」思路做数据增强，降低实采数据成本

  - 多视角数据生成策略可迁移到电商跨场景商品匹配任务，通过3D重建合成不同摆放角度、拍摄视角的训练样本，提升模型鲁棒性

  - 几何一致性校验的增强数据生成思路可复用在生成式推荐的样本扩增环节，避免合成样本出现逻辑冲突'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
模仿学习训练的视觉运动策略对相机视角变化极度敏感，移动操纵场景下机器人导航误差、定位漂移会导致实际执行位姿与演示采集位姿不一致；现有新视角合成增强方法默认静态场景，无法渲染接触交互阶段的动态操作对象，核心交互环节数据增强缺失。
### 方法关键点
利用移动操纵采集过程中天然生成的多视角观测，结合3D Gaussian Splatting、前馈3D基础模型、基于运动学的动作重定向，分别重建静态场景与操作对象，从新视角渲染生成几何一致的合成演示与对应转换后的动作标签。
### 关键结果
在5个真实世界移动操纵任务、3种场景下测试，平均成功率是最强基线的2倍以上；在所有基线完全失效的大基座位移场景下仍保持有效成功率，同时大幅降低大规模真实数据采集需求。

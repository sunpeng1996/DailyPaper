---
title: 'LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding
  via Multi-Task Distillation'
title_zh: LucidLyra：基于多任务蒸馏的前馈生成式3D场景重建与联合理解
authors:
- Oliver Hahn
- Rodrigo Marcuzzi
- Sangeetha Grama Srinivasan
- Alessandro Burzio
- Sherwin Bahmani
- Jiahui Huang
- Stefan Roth
- Shengyu Huang
- Qunjie Zhou
- Laura Leal-Taixé
affiliations:
- NVIDIA
- TU Darmstadt
- Università degli Studi di Modena e Reggio Emilia
- ELIZA
- hessian.AI
arxiv_id: '2610.40495'
url: https://arxiv.org/abs/2610.40495
pdf_url: https://arxiv.org/pdf/2610.40495
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 3D生成 · 多任务蒸馏
tags:
- 3D Reconstruction
- Multi-Task Distillation
- 3DGS
- Diffusion Model
- Vision Foundation Model
one_liner: 通过多任务蒸馏实现无需逐场景优化的可查询语义生成式3D场景重建
practical_value: '- 电商3D商品/场景生成场景可复用多任务蒸馏思路，同时生成3D资产+语义标签，无需额外标注，降内容生产成本

  - 家居/家装类AR推荐场景，可直接基于单张图生成带语义的3D场景，支撑虚拟搭配、空间适配等交互功能

  - 具身Agent训练场景，可快速生成带实例标注的3D模拟环境，降低交互训练数据采集成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有生成式3D重建仅能输出无结构视觉内容，下游机器人、3D交互应用需要语义、实例标注信息，传统3D理解方案依赖多视图数据、逐场景优化，成本高、泛化能力弱。
### 方法关键点
1. 设计多任务蒸馏框架，从相机可控视频扩散模型、冻结2D视觉基座模型中蒸馏互补知识，映射到统一表示
2. 联合推断编码几何、外观、开放词表语义、类无关实例线索的3D Gaussian表征，无需逐场景优化，训练阶段也不需要手工3D标注与多视图采集数据
### 关键结果数字
在合成、真实图像基准上效果优于SOTA 3DGS分割+生成式3D重建的基线方案，同时保留原重建质量，可扩展到单目视频生成动态结构化3D场景，支撑3D编辑、资产挖掘、机器人模拟等下游应用

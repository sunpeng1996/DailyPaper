---
title: 'RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation'
title_zh: RoGe：基于端到端隐式重建与生成的新视角合成方法
authors:
- Xiaolei Lang
- Ze Kang
- Zehao Huang
- Naiyan Wang
affiliations:
- Xiaomi EV
- Northeastern University
arxiv_id: '2609.02847'
url: https://arxiv.org/abs/2609.02847
pdf_url: https://arxiv.org/pdf/2609.02847
published: '2026-09-02'
collected: '2026-09-04'
category: Other
direction: 新视角合成 · 端到端隐式建模
tags:
- Novel View Synthesis
- Diffusion Model
- Implicit 3D Representation
- Video Generation
- Joint Training
one_liner: 提出无显式3D中间表示的端到端重建生成统一框架RoGe，实现稀疏输入下时序一致的新视角漫游视频合成
practical_value: '- 电商商品3D展示场景可复用隐式特征直连扩散模型的架构，跳过显式3D重建步骤降低计算开销，支持仅用少量商品实拍图生成自由视角漫游视频

  - 虚拟试穿、家装AR等多模态生成场景可借鉴联合训练范式，用下游生成任务损失直接反向更新上游表征模块，减少中间表示的信息损耗

  - 内容生成场景可复用射线查询隐式特征的trick，提升同一场景不同视角生成结果的几何一致性，避免视角切换时的内容穿帮'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
稀疏输入下的新视角合成现有混合方法依赖渲染图或点云、3D高斯等显式3D中间表示桥接重建与生成模块，存在信息损失，且重建模块无法获得生成侧反馈校正误差，导致生成结果几何一致性、时序连贯性不足。
### 方法关键点
1. 提出端到端统一框架RoGe，移除重建与生成间的显式桥接，无任何3D中间表示；
2. 前馈重建模块基于稀疏输入视图构建隐式场景表征，通过目标相机射线查询得到逐视角几何特征；
3. 几何特征直接作为条件注入视频扩散模型，双模块联合训练，生成目标直接优化上游几何表征。
### 关键结果
在DL3DV数据集上，图像质量、视频时序一致性指标均全面超越重建类、生成类、混合架构基线；消融实验验证射线查询隐式特征作为条件效果优于原始重建token、渲染RGB，联合训练可带来额外性能增益。

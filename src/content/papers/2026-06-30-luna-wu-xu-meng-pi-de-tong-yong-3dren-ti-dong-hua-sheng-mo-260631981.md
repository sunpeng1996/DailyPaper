---
title: 'LUNA: Learning Universal 3D Human Animation Beyond Skinning'
title_zh: LUNA：无需蒙皮的通用3D人体动画生成模型
authors:
- Peng Li
- Rawal Khirodkar
- Junxuan Li
- Yuan Dong
- Chen Cao
- Yuan Liu
- Wenhan Luo
- Yike Guo
- Shunsuke Saito
affiliations:
- The Hong Kong University of Science and Technology
- Codec Avatars Lab, Meta
arxiv_id: '2606.31981'
url: https://arxiv.org/abs/2606.31981
pdf_url: https://arxiv.org/pdf/2606.31981
published: '2026-06-30'
collected: '2026-07-02'
category: Other
direction: 3D人体动画生成 · 多模态隐式驱动
tags:
- 3D_Gaussian_Avatar
- Multimodal_Control
- Hybrid_Supervision
- Zero_Shot_Generalization
- Transformer
one_liner: 提出无需线性混合蒙皮的通用3D人体动画模型，支持多模态2D驱动，实现零样本跨身份泛化
practical_value: '- 核心为计算机视觉3D动画方向学术贡献，与电商/搜推/LLM+Agent核心业务关联度极低

  - 仅若涉及数字人直播、3D avatar内容生产等边缘电商内容业务，可参考其多模态驱动、混合监督训练范式'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有单目图像生成高保真可动画3D人体avatar高度依赖Linear Blend Skinning（LBS）与参数化人体模型，拟合误差易产生伪影，表达能力受强约束。
### 方法关键点
1. 提出无LBS的端到端通用神经动画模型LUNA，跳过显式人体拟合，直接将图像、关键点、草图、未知身份等多模态2D控制信号映射为3D高斯形变；
2. 核心采用transformer-based运动回归器，解耦全局刚性运动与细粒度局部动态，同时捕捉连贯动作与细微非刚性效果；
3. 引入混合监督策略：从LBS教师模型蒸馏软结构先验，设计损失同时兼容有限标注拟合数据与大规模野生无标注视频训练，解决2D转3D固有歧义。
### 关键结果
与LBS-based方法视觉保真度相当，可生成真实人体动作，在多类驱动模态下实现零样本跨身份泛化，是首个支持隐式2D驱动的端到端3D可动画模型。

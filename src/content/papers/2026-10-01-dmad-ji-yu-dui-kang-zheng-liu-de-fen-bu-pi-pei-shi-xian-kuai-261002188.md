---
title: 'DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation'
title_zh: DMAD：基于对抗蒸馏的分布匹配实现快速视觉生成
authors:
- Zhengming Yu
- Junkun Yuan
- Haotian Yang
- Gordon Guocheng Qian
- Yizhi Wang
- Angtian Wang
- Yiding Yang
- Bo Liu
- Xin Li
- Wenping Wang
affiliations:
- Texas A&M University
- ByteDance
arxiv_id: '2610.02188'
url: https://arxiv.org/abs/2610.02188
pdf_url: https://arxiv.org/pdf/2610.02188
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 扩散模型蒸馏 · 少步生成加速
tags:
- Diffusion Model
- Adversarial Distillation
- Distribution Matching
- Fast Generation
- Knowledge Distillation
one_liner: 将分布匹配重构为对抗分类任务，省去辅助扩散模型开销，实现更优的少步视觉生成
practical_value: '- 电商商品图/营销短视频的少步生成蒸馏可复用DMAD架构，省去辅助扩散模型的显存与计算开销，大幅降低推理时延

  - gap-based reweighting策略可迁移到多噪声水平的生成式模型蒸馏任务，自动适配不同训练阶段的教师监督权重

  - 判别器logit映射对数密度比的结论可复用在各类分布对齐的生成任务中，替代显式分布拟合步骤降低复杂度'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有DMD类分布匹配蒸馏需额外维护拟合学生分布的辅助扩散模型，显存、计算开销高，限制少步生成模型落地。
### 方法关键点
1. 将分布匹配重构为分类任务，基于共享骨干的双判别器头区分真实数据、教师样本、学生样本，用logit线性损失训练学生，无需辅助分数拟合；
2. 理论证明判别器最优时损失等价于DMD的分布匹配梯度；
3. 引入gap-based重加权，基于真实数据头的真实/教师样本logit差自适应调整不同噪声水平的教师监督权重。
### 关键结果
ImageNet-64x64单步生成FID达1.04；4步SDXL在COCO-10K上FID 14.47；4步Wan2.1-T2V-14B的VBench总分85.15；4步音视频生成学生相对DMD2、rCM的人类偏好率分别达79.1%、84.6%，均优于对比的少步方法与多步教师。

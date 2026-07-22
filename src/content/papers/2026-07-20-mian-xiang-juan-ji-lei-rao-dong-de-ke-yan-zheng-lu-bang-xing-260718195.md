---
title: Certified Training for Convolutional Perturbations
title_zh: 面向卷积类扰动的可验证鲁棒性训练方法
authors:
- Benedikt Brückner
- Alessio Lomuscio
affiliations:
- Safe Intelligence
- Imperial College London
arxiv_id: '2607.18195'
url: https://arxiv.org/abs/2607.18195
pdf_url: https://arxiv.org/pdf/2607.18195
published: '2026-07-20'
collected: '2026-07-22'
category: Training
direction: 视觉模型可验证鲁棒性训练
tags:
- Certified Training
- Convolutional Perturbation
- Adversarial Robustness
- Motion Blur
- Model Safety
one_liner: 提出高效编码卷积扰动的认证训练方法，训练具备形式化安全保证的抗扰动视觉模型
practical_value: '- 多模态推荐/广告场景的图像特征提取模型可参考该认证训练思路，优化抗运动模糊、抖动等真实场景噪声的能力，避免特征失准影响排序召回效果

  - 对电商合规审核等高风险业务的视觉模型，可复用卷积扰动编码方法，提升模型鲁棒性的可验证性，降低合规风险

  - 兼顾标准精度与鲁棒精度的训练范式可迁移至多模态特征抽取模型调优，替换传统对抗训练方案获得更优的噪声抵抗能力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前视觉模型易受运动模糊、抖动等真实场景下的卷积类扰动影响，传统数据增强、对抗训练方案仅能提升经验鲁棒性，无形式化安全保证，无法排查隐藏漏洞，限制了其在高风险场景的落地。
### 方法关键点
提出新型认证训练框架，通过对卷积类扰动做高效编码，在训练损失中加入模型输出边界约束项，直接训练具备可验证鲁棒性的视觉模型，无需依赖后验验证环节。
### 关键结果数字
在CIFAR10数据集上，针对合理强度的运动模糊扰动，鲁棒精度超过80%，同时标准精度与传统对抗训练方案基本持平，鲁棒性能显著优于现有对抗训练方法。

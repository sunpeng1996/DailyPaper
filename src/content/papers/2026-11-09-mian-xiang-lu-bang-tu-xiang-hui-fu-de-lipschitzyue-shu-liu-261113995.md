---
title: Lipschitz-Controlled Flow Matching for Robust Image Restoration
title_zh: 面向鲁棒图像恢复的Lipschitz约束流匹配方法
authors:
- Sedjro Salomon Hotegni
- Konstantin Sonntag
- Paul-Christian Bürkner
- Sebastian Peitz
affiliations:
- Paderborn University
- TU Dortmund University
arxiv_id: '2611.13995'
url: https://arxiv.org/abs/2611.13995
pdf_url: https://arxiv.org/pdf/2611.13995
published: '2026-11-09'
collected: '2026-11-12'
category: Other
direction: 生成式图像恢复 · 鲁棒性优化
tags:
- Flow Matching
- Lipschitz Regularization
- Diffusion Transformer
- Image Restoration
- Adversarial Robustness
one_liner: 提出LipsFlower框架，结合Lipschitz约束与定制Transformer，降低流匹配图像恢复的扰动放大效应
practical_value: '- 电商商品图/用户头像高清修复、去噪场景可借鉴Lipschitz约束思路，降低输入小扰动（压缩噪声、模糊）导致的生成结果跳变，提升服务稳定性

  - 生成模型向量场架构可复用LipHDiT的3个优化trick：稳定近似谱归一化、有界调制、凸残差混合，兼顾鲁棒性与生成质量

  - 生成类服务稳定性优化可参考adversarial finite-radius gain正则化思路，惩罚模型对输入的过度敏感性，减少bad case'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
流匹配模型在图像恢复任务中生成质量优异，但学习到的动力学易放大小规模输入扰动，导致重构结果不稳定，难以满足落地场景的可靠性要求。
### 方法关键点
1. 推导了Flow-from-Y（从含噪观测初始化ODE）、观测条件后验采样两种流匹配范式的稳定性边界
2. 设计Lipschitz感知的沙漏扩散Transformer（LipHDiT）作为流匹配的向量场架构，融合稳定近似谱归一化、有界调制、凸残差混合三个核心优化
3. 新增插值状态下的对抗有限半径增益正则化，惩罚模型对状态和观测的过度敏感性
### 关键结果
在盲人脸恢复任务上，LipsFlower可有效降低扰动放大效应，同时恢复结果的感知质量与现有主流基线持平，无明显性能损失

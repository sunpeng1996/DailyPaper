---
title: Uncertainty-Guided Latent Diffusion Models for Faithful Super Resolution
title_zh: 不确定性引导的隐式扩散模型实现高保真图像超分辨率
authors:
- Ren Wang
- Yung-Yu Chuang
affiliations:
- National Taiwan University
- NTU AI-CoRE
arxiv_id: '2608.25998'
url: https://arxiv.org/abs/2608.25998
pdf_url: https://arxiv.org/pdf/2608.25998
published: '2026-08-26'
collected: '2026-08-27'
category: Other
direction: 图像超分辨率 · 扩散模型优化
tags:
- Diffusion Model
- Super Resolution
- Uncertainty Estimation
- Perception Distortion Trade-off
- Latent Diffusion
one_liner: 提出UGDiff扩散引导范式，优化超分感知-失真权衡，平衡图像保真度与感知质量
practical_value: '- 电商商品主图高清修复场景可借鉴不确定性引导思路，仅在纹理复杂区域补全高频细节，既保证原图保真度又提升视觉质感

  - 扩散生成任务中可复用「结合采样器后验方差动态调整引导强度」的trick，降低生成后期对ground truth的依赖，平衡生成质量与保真度

  - 多模态推荐的商品图像预处理pipeline可引入该方法，低清商品图一键升清不破坏原有商品特征，避免误导用户'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单图像超分长期存在感知-失真权衡核心挑战：现有扩散基超分方法生成的图像感知真实度高但保真度不足，优化保真度的方案又因强依赖高保真参考图导致感知质量下降，无法实现二者平衡。

### 方法关键点
1. 提出UGDiff不确定性引导扩散范式，先估计高保真图像对应隐特征的重建不确定性
2. 用不确定性引导扩散过程，仅在高不确定区域选择性恢复高频细节，其余区域优先保障保真度
3. 结合扩散采样器每一步后验方差自适应识别高不确定区域，降低采样后期对高保真参考图的依赖。

### 关键结果
在多项超分基准测试中表现优于当前SOTA扩散基超分方法，实现更优的感知-失真平衡。

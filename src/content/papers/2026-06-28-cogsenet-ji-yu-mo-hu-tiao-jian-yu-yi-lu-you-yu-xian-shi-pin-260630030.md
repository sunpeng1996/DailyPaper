---
title: 'CogSENet: Blind Image Deblurring with Blur-Conditioned Semantic Routing and
  Explicit Frequency Fusion'
title_zh: CogSENet：基于模糊条件语义路由与显式频率融合的盲图像去模糊
authors:
- Pan Wang
- Yihao Hu
- Xiujin Liu
affiliations:
- University of Science and Technology of China
- Westlake University
- University of Michigan, Ann Arbor
arxiv_id: '2606.30030'
url: https://arxiv.org/abs/2606.30030
pdf_url: https://arxiv.org/pdf/2606.30030
published: '2026-06-28'
collected: '2026-07-03'
category: Other
direction: 低阶视觉 · 图像盲去模糊与多任务恢复
tags:
- Image Deblurring
- State Space Model
- Frequency Fusion
- CLIP Prior
- Semantic Routing
one_liner: 模拟鹰视觉系统提出语义对齐动态盲去模糊框架，性能超SOTA且参数量更低
practical_value: '- 电商商品图/广告素材修复场景可复用高低频分离+CLIP语义先验融合的思路，去除模糊、雨雾噪点等瑕疵提升素材质量

  - 多模态推荐/Agent系统中，可借鉴语义驱动状态空间模块的长距离视觉依赖建模方法，优化图像特征提取效果

  - 空间非均匀退化的图像修复场景可复用连续模糊场估计trick，适配不同拍摄场景下的低质素材修复'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有盲图像去模糊方法对真实场景空间变化退化的处理效果差，缺乏语义感知能力，难以区分有效纹理和伪影。
### 方法关键点
1. 受鹰视觉系统启发设计动态语义对齐重建框架CogSENet
2. 语义驱动状态空间模块（SDSSM）通过可微路由实现语义感知token重组，支持prompt条件下的长距离依赖建模
3. 双频融合块（BFFB）通过小波变换拆分高低频特征，实现纹理与结构的可解释恢复
4. 从模糊图像估计连续模糊场（CBF），与CLIP语义先验融合调制深层隐特征，适配空间非均匀模糊的自适应恢复
### 关键结果
盲图像去模糊任务上视觉质量与结构保真度均优于SOTA方法，参数量更低，同时在去雾、去雨、去噪等多任务上表现优异

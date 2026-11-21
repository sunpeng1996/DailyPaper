---
title: 'Fixing the Last Mile: Failure-Aware Image Restoration with Region-Specific
  Guidance'
title_zh: 修复最后一公里：带区域特定引导的故障感知图像恢复
authors:
- Hongyu An
- Fanghua Yu
- Kainan Yan
- Luc Van Gool
- Chao Dong
- Jinjin Gu
affiliations:
- INSAIT, Sofia University "St. Kliment Ohridski"
- The University of Hong Kong
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
- Shenzhen University of Advanced Technology
arxiv_id: '2611.26456'
url: https://arxiv.org/abs/2611.26456
pdf_url: https://arxiv.org/pdf/2611.26456
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 图像恢复 · 局部故障感知修复
tags:
- Image Restoration
- Local Failure Detection
- Region-specific Guidance
- Perceptual Quality
- Generative Prior
one_liner: 提出故障感知图像恢复框架FAIR，通过区域特定引导解决图像恢复局部失效问题
practical_value: '- 电商商品图修复场景可复用区域感知思路，优先对人脸、文字等用户敏感区域做针对性修复，避免局部瑕疵影响商品转化率

  - 现有生成式图像生成/修复管线可直接叠加FAIR模块做后处理，不需要改动原有主流程即可提升局部感知质量

  - 可迁移到广告素材生成的后处理环节，解决AIGC素材局部纹理不一致、文字乱码等常见落地问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前图像恢复算法全局保真度已达到较高水平，但普遍存在人脸、文字等语义关键区域的局部失效问题，即使小面积瑕疵也会大幅降低整体感知质量，成为落地的核心阻碍。
### 方法关键点
- 放弃全图统一生成先验，单趟推理同时引入「局部故障高发区域位置」「各区域所需校正引导」两个条件信号，实现细粒度可控修复
- 可直接作为现有恢复管线的补充模块，将优化重心从全局保真转向局部感知可接受度，既保障关键区域语义准确、风格一致，也不破坏其他区域的恢复质量
### 关键结果
大量实验验证，该方案可覆盖绝大多数常见局部失效场景，有效提升整体感知质量，填补技术精度与实际落地可用性的差距。

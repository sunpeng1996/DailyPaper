---
title: 'PRISM: Distribution-Gated Flow Matching for Controllable Unpaired Image Translation'
title_zh: PRISM：面向可控无配对图像翻译的分布门控流匹配框架
authors:
- Elad Yoshai
- Natan T. Shaked
affiliations:
- Tel Aviv University
arxiv_id: '2608.06240'
url: https://arxiv.org/abs/2608.06240
pdf_url: https://arxiv.org/pdf/2608.06240
published: '2026-08-06'
collected: '2026-08-07'
category: Other
direction: 可控图像生成 · 无配对域翻译
tags:
- Flow Matching
- Image Translation
- Controllable Generation
- Domain Adaptation
- Image Generation
one_liner: 提出逐特征分布门控的无GAN流匹配框架，实现高可控无配对图像翻译
practical_value: '- 电商商品图风格迁移、跨场景渲染（如白天转黑夜、款式换色）可复用逐特征门控逻辑，精准区分需保留的商品结构与需修改的外观，避免生成图形变

  - 无配对训练的域迁移任务可借鉴任务匹配corruption设计策略：结构保留类任务用AdaIN锚定内容，结构变更类任务用部分锚定平衡生成效果与保真度

  - 推理阶段无需重训即可通过文本/检测器局部覆盖门控的机制，可用于定制化商品图修图需求，比如保留logo、特定纹理的同时修改其他区域'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
无配对图像翻译缺乏配对监督，现有扩散类方案依赖全局噪声/引导值控制内容保留逻辑，无法精准拆分需保留的核心内容与需修改的外观属性，生成效果可控性差。
### 方法关键点
1. 提出GAN-free的PRISM流匹配框架，用基于源特征到目标域分布标准化距离的逐特征门控替代全局控制：远离目标分布的特征自由生成，符合目标分布的特征直接保留；
2. 同门控同时控制隐空间初始化（混合源隐向量与任务匹配的corruption）和ODE积分的传输时序，适配不同任务需求；
3. 推理阶段无需重训即可通过文本/检测器局部覆写门控，自定义保留区域。
### 关键结果
5个自然/生物医学基准测试中，4个基准取得最优FID、KID，病理图像数据集的细胞核计数比最接近理想值，兼顾目标真实感和结构保留度。

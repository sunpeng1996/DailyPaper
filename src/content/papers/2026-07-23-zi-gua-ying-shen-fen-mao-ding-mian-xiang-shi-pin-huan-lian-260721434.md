---
title: 'Adaptive Identity Anchoring: Closed-Loop Keyframe Placement for Synthetic
  Paired Supervision in Video Face Swapping'
title_zh: 自适应身份锚定：面向视频换脸合成配对监督的闭环关键帧放置
authors:
- Logan Robbins
arxiv_id: '2607.21434'
url: https://arxiv.org/abs/2607.21434
pdf_url: https://arxiv.org/pdf/2607.21434
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 视频生成 · 视频换脸监督数据合成
tags:
- Video Generation
- Face Swapping
- Synthetic Supervision
- Diffusion Transformer
- Adaptive Anchoring
one_liner: 提出自适应身份锚定与纹理修复方案，解决视频换脸身份漂移与过度平滑问题
practical_value: '- 自适应闭环插锚思路可迁移至长序列生成式推荐的一致性控制，通过插入得分最差的结果作为锚点缓解语义漂移

  - 闭环反馈+自动数据过滤的链路可复用在AIGC电商内容（商品短视频、虚拟试穿）的生成质量校验流程

  - 跨区域纹理迁移的方案可用于生成式推荐的商品细节还原，例如虚拟试妆/试穿时保留原始商品的纹理特征'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
视频换脸无天然配对标注数据，现有方案仅选用视频首尾两帧作为身份锚点，长视频、遮挡、大姿态变化场景下极易出现身份漂移，同时生成结果存在皮肤过度平滑的失真问题，此前无研究针对锚点数量与放置策略做优化。
### 方法关键点
1. 提出自适应身份锚定（AIA），适配扩散强迫式Transformer架构，支持任意锚点集输入，通过将锚点帧token钳位为零噪声实现条件注入；
2. 设计闭环反馈回路，逐帧计算生成帧与参考身份的匹配分，在得分最低帧插入换脸锚点，直到整体质量达标或触达锚点预算，同时复用回路结果自动过滤低质量数据；
3. 搭配现实参考纹理修复模块，从真实帧非人脸区域迁移颗粒度、分频段传递微纹理，新增光谱接受通道对齐真实视频频谱。
### 关键结果
已设计漂移-间隔曲线、固定预算下均匀/自适应锚点对比、AIA生成数据训练学生模型、纹理消融人体实验等可证伪验证方案。

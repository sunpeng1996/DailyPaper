---
title: 'SPEED: One-Step Pixel Diffusion for High-quality Video Frame Interpolation'
title_zh: SPEED：基于单步像素扩散的高质量视频帧插值方法
authors:
- Zihao Zhang
- Haoyu Zhao
- Siqian Yang
- Yidi Wu
- Yudong Jiang
- Zuxuan Wu
affiliations:
- Fudan University
- Bilibili Inc
arxiv_id: '2607.15585'
url: https://arxiv.org/abs/2607.15585
pdf_url: https://arxiv.org/pdf/2607.15585
published: '2026-07-17'
collected: '2026-07-21'
category: Multimodal
direction: 视频插帧 · 单步扩散性能优化
tags:
- Diffusion Model
- Video Frame Interpolation
- One-step Sampling
- Attention Optimization
- Pixel Generation
one_liner: 提出单步像素扩散框架SPEED，解决视频插帧细节丢失、推理延迟高内存占用大问题
practical_value: '- Noise-Update-Only Attention可迁移到商品短视频、广告素材等条件生成任务，既保留条件语义不退化，还能降低近50%计算开销

  - 漂移感知时间步采样+定制训练目标的单步扩散思路，可复用在实时素材渲染、直播插帧等低延迟生成场景，无需多步采样即可保障生成质量

  - 动态patch缩放的多阶段架构，可借鉴到多分辨率商品图/视频生成任务，更好捕捉多尺度特征'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于扩散的视频插帧方法存在两大瓶颈：一是隐空间扩散重建回像素空间时会丢失细粒度细节，二是多步采样带来过高的内存消耗与推理延迟，无法适配高实时性落地需求。
### 方法关键点
1. 采用带动态patch缩放的渐进式多阶段架构，高效学习多尺度运动、结构与外观表征
2. 提出Noise-Update-Only Attention机制，避免干净条件帧语义退化的同时降低近50%计算开销
3. 引入漂移感知时间步采样策略搭配定制训练目标，直接在像素空间预测图像，实现无质量损失的单步推理
### 关键结果
- SNU-FILM数据集上，LPIPS降低8.8%，推理速度提升63.3%，内存占用降低10.6%
- 4K基准测试集上，LPIPS较此前SOTA方法最高提升51.5%

---
title: Speculative Forcing for Efficient Autoregressive Video Generation
title_zh: Speculative Forcing：提升自回归视频生成效率的新框架
authors:
- Hyunwook Choi
- Seungryong Kim
- Dongyoon Han
- Sangdoo Yun
affiliations:
- KAIST AI
- NAVER AI Lab
arxiv_id: '2610.22347'
url: https://arxiv.org/abs/2610.22347
pdf_url: https://arxiv.org/pdf/2610.22347
published: '2026-10-15'
collected: '2026-10-17'
category: Other
direction: 自回归生成推理加速 · 动态token退出
tags:
- Autoregressive Generation
- Inference Optimization
- Speculative Decoding
- Video Generation
- KV Cache
one_liner: 通过逐token动态提前退出减少冗余去噪，在不损失生成质量前提下大幅提升自回归视频生成速度
practical_value: '- 生成式推荐/广告文案生成场景可复用该动态token退出思路，对已收敛的语义token提前冻结，降低大模型推理延迟

  - 两种验证器设计可直接复用：训练-free的相似度+稳定性判断适合快速上线，小学习验证器适合算力充足场景进一步提效

  - 已冻结token的KV cache保留复用的设计，可迁移到所有自回归生成任务的推理优化，降低显存开销同时提升上下文利用率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
少步自回归视频生成器支持流式生成，但所有token都需走完完整去噪步骤，存在大量冗余计算：多数token在早期生成步骤就已接近最终全步输出，无需后续 refinement。
### 方法关键点
提出Speculative Forcing框架，将中间去噪结果作为草稿，逐token判断是否可提前接受；接受后的token冻结为最终输出，不再参与后续去噪，但其KV cache保留为上下文供剩余token使用；提供两种验证器实现：训练-free版本基于与干净内容的相似度、跨步骤稳定性判断，可学习版本基于生成器中间特征预测token与最终输出的差距。
### 关键结果
全场景下生成质量与全步骤采样持平：
- LongLive数据集：单token平均去噪步骤仅~1.7，推理速度提升1.5x以上，帧率达41.7/37.8fps
- Lingbot-World 2.0数据集：单token平均去噪步骤~2.5，速度提升1.35x，帧率达24.5fps

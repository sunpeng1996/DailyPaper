---
title: 'Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation'
title_zh: Kandinsky 6.0 Video：音视频同步生成扩散基础模型家族
authors:
- Team Kandinsky
- Julia Agafonova
- Bulat Akhmatov
- Mikhail Aksyutin
- Grigorii Alekseenko
- Anastasia Aliaskina
- Olga Androsova
- Vladimir Arkhipkin
- Anna Averchenkova
- Alexander Belykh
affiliations:
- KandinskyLab
arxiv_id: '2610.05608'
url: https://arxiv.org/abs/2610.05608
pdf_url: https://arxiv.org/pdf/2610.05608
published: '2026-10-04'
collected: '2026-10-10'
category: Multimodal
direction: 多模态生成 · 音视频同步扩散模型
tags:
- Diffusion Model
- Text-to-Video
- Text-to-Audio
- Multimodal Generation
- Cross-Attention
one_liner: 推出3B/29B两款音视频同步生成扩散模型，采用双流CrossDiT架构实现音视频对齐，性能领先且全开源
practical_value: '- 双流交叉注意力跨模态对齐方案可迁移到电商多模态内容生成场景，实现商品短视频画面与配音、口播的精准同步

  - 先单模态预训练再跨模态联合训练的范式可复用，降低多模态模型训练的资源开销与效果对齐难度

  - 3B轻量版模型可直接二次开发，用于商家端低成本批量生成带同步音频的商品种草短视频，提升内容生产效率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频生成方案普遍存在音画不同步、语音音质差、输出分辨率不足等缺陷，无法满足商业化内容生产的落地要求

### 方法关键点
1. 推出3B参数量Lite版、29B参数量Pro版两款双流CrossDiT架构扩散模型，预训练视频流与新训音频流通过双向cross-attention实现时序、语义双对齐
2. 采用渐进训练策略：先在大规模音频语料上从零训练音频流，再在音视频配对数据上联合训练保留单模态保真度，后续叠加SFT、RL post-training、蒸馏优化
3. 内置超分模块可将输出上采样至1080P全高清，支持T2AV、I2AV两种生成模式，可生成带唇形同步的44kHz高保真音频的5s短视频

### 关键结果
人类侧评中Pro版明显优于前代Kandinsky 5.0 Video Pro，语音质量指标领先行业头部音视频生成模型，全代码、权重、diffusers集成以MIT协议开源

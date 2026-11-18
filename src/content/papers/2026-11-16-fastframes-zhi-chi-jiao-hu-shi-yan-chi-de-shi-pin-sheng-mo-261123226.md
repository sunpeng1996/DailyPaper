---
title: 'FastFrames: Video Generation at Interactive Latency'
title_zh: FastFrames：支持交互式延迟的视频生成模型
authors:
- Gene Chou
- Guandao Yang
- Fujun Luan
- Lars Mescheder
- Wei Dong
- Stephan Richter
- Vladlen Koltun
affiliations:
- Apple
- Cornell University
arxiv_id: '2611.23226'
url: https://arxiv.org/abs/2611.23226
pdf_url: https://arxiv.org/pdf/2611.23226
published: '2026-11-16'
collected: '2026-11-18'
category: Multimodal
direction: 多模态视频生成 · 推理性能优化
tags:
- Video Generation
- Diffusion Model
- KV Cache
- Inference Optimization
- Autoregressive
one_liner: 重构自回归视频扩散高延迟底层组件，实现不降质的交互式视频生成
practical_value: '- 做Agent多模态交互、商品短视频生成等生成类业务时，先对推理全链路做profile，优先优化延迟占比超50%的核心瓶颈，不要默认基础组件不可替换

  - 生成服务部署时，KV cache、VAE这类常被视为固定实现的模块可替换为轻量版本，能在基本不降质的前提下大幅降低端到端延迟

  - 不同参数规模的多模态生成模型可参考对应硬件配比：1.3B级用单张B200部署，14B级用8卡B200节点部署，平衡性能与成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频扩散模型适配交互式视觉体验需求，但现有方案延迟比流畅交互要求高几个数量级；行业默认VAE解码、KV cache更新等底层操作是不可替换的固定组件，从未针对该类环节做延迟优化。

### 方法关键点
对SOTA自回归视频扩散模型推理全链路做深度profile，发现上述底层操作占端到端推理延迟的50%以上；推翻组件不可替换假设，用轻量替代方案重构所有高延迟环节，推出FastFrames系列模型。

### 关键结果
1.3B参数版本单B200 GPU单帧延迟36ms、RPS达28，生成质量与速度慢8倍的SOTA模型持平；14B参数版本8卡B200节点单帧延迟45ms、RPS达22，视觉真实度显著更优，可支持相机、物理条件驱动的实时视频生成交互。

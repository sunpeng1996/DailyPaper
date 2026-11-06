---
title: 'LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive
  Worlds'
title_zh: LiveFoley：面向沉浸式交互场景的流式实时视频转音频生成
authors:
- Yusheng Dai
- Vladimir Iashin
- Kangdi Wang
- Yuxuan Jiang
- Ilpo Viertola
- Weiqiang Wang
- Qiuhong Ke
- Min Zhao
- Jianfei Cai
affiliations:
- Monash University
- Nanjing University
- ShengShu Technology
- Tampere University
- Alibaba Group
arxiv_id: '2611.05988'
url: https://arxiv.org/abs/2611.05988
pdf_url: https://arxiv.org/pdf/2611.05988
published: '2026-11-04'
collected: '2026-11-06'
category: Multimodal
direction: 多模态生成 · 流式实时音视频同步
tags:
- Video-to-Audio
- Streaming Generation
- Diffusion Model
- Autoregressive Generation
- Multimodal
- Real-Time Generation
one_liner: 提出低延迟流式因果自回归扩散架构，实现媲美离线模型的实时音视频生成效果
practical_value: '- 实时流式推理场景可复用Trailing Sliding Window思路，无需重训即可将非因果段级编码器转为流式模块，大幅降低多模态实时服务的改造成本

  - 电商直播、虚拟数字人互动等对多模态同步要求高的实时场景，可借鉴Unified Varhop框架，根据业务算力/延迟要求灵活配置跳步，平衡用户体验与资源成本

  - 自回归扩散生成类任务可复用History LocDiT优化思路，无额外延迟引入历史上下文提升生成质量，资源宽松场景可加轻度未来预热进一步提效'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
流式视频转音频（V2A）是沉浸式交互场景的核心能力，但现有流式方案受实时约束存在两大瓶颈：视觉前端为降低前瞻 latency 压缩感受野，导致音画对齐精度大幅下降；因果自回归扩散后端孤立对每个音频 patch 降噪，音频质量远劣于离线模型。
### 方法关键点
1. 视觉端引入Trailing Sliding Window，无需重训即可将非因果段级编码器转换为流式模块，通过窗口重对齐保障音画对齐精度，配置可调跳步将前端前瞻延迟控制在人类感知阈值以下，配套Unified Varhop框架适配不同延迟/算力预算场景；
2. 音频端扩展局部扩散Transformer（LocDiT）降噪窗口的时序范围，默认采用History LocDiT无额外延迟引入历史上下文提升音质，可选Future-Warmup LocDiT以可接受的轻度前瞻延迟进一步优化生成效果。
### 关键结果
音画时序对齐效果与离线模型持平，生成质量领先所有现有流式V2A系统。

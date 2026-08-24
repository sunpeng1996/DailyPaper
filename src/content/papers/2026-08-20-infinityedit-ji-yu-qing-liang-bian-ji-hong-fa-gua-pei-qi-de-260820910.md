---
title: 'InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter'
title_zh: InfinityEdit：基于轻量编辑触发适配器的无限视频编辑
authors:
- Yunze Tong
- Mushui Liu
- Canyu Zhao
- Shiyi Zhang
- Didi Zhu
- Peng Zhang
- Wanggui He
- Jinlong Liu
- Ying Chen
- Hao Jiang
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2608.20910'
url: https://arxiv.org/abs/2608.20910
pdf_url: https://arxiv.org/pdf/2608.20910
published: '2026-08-20'
collected: '2026-08-24'
category: Multimodal
direction: 多模态 · 流式视频指令编辑
tags:
- Video Editing
- Lightweight Adapter
- Streaming Generation
- Instruction Following
- Diffusion Model
one_liner: 提出轻量编辑触发适配器，为流式视频生成器赋予无边界指令驱动编辑能力
practical_value: '- 电商直播场景可复用流式按需编辑架构，实时响应滤镜、特效、动态商品植入等编辑指令，无需预处理全段视频

  - 仅在编辑请求到达的分片激活Adapter的推理策略，可大幅降低算力开销，适配高并发实时内容生成场景

  - 时序因果自注意力仅向前传递时序线索的设计，可迁移到各类流式生成任务，避免未来信息泄露保证生成连续性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有指令驱动视频编辑方法依赖固定时长视频片段的逐帧原地对齐假设，无法适配直播、持续拍摄等开放流式场景的动态编辑需求，面临编辑需忠实延续内容、多轮编辑累积后生成质量稳定两大挑战。
### 方法关键点
1. 搭建无限视频编辑场景专属数据采集pipeline；
2. 设计包含三类注意力模块的轻量Edit Adapter：历史交叉注意力用输入帧引导帧去噪、时序因果自注意力约束时序线索仅从过往帧向后续帧传递、编辑交叉注意力注入用户编辑指令；
3. 推理阶段仅在编辑请求到达的视频片段激活Adapter，后续片段复用重置锚帧的原生生成模型，保留原生无限生成能力。
### 关键结果
实验验证，方案可在无边界多轮编辑序列下忠实延续视频流，生成质量无明显衰减。

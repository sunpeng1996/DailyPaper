---
title: 'FrameMorrow: Future-guided Frame Selection with Prospective Tokens for Long-Horizon
  Video Generation'
title_zh: FrameMorrow：基于前瞻Token的未来导向长时序视频生成帧选择方法
authors:
- Bo Yin
- Xiaobin Hu
- Jiaqi Zhao
- Shuicheng Yan
affiliations:
- National University of Singapore
- Harbin Institute of Technology (Shenzhen)
arxiv_id: '2609.38839'
url: https://arxiv.org/abs/2609.38839
pdf_url: https://arxiv.org/pdf/2609.38839
published: '2026-09-29'
collected: '2026-10-05'
category: Multimodal
direction: 长时序视频生成 · 历史信息筛选
tags:
- Long-Video Generation
- Prospective Tokens
- History Selection
- Plug-and-Play
- Frame Selection
one_liner: 通过预测少量前瞻Token引导历史帧选择，可即插即用提升多类长视频生成效果
practical_value: '- 长序列推荐/Agent对话/RAG场景可复用核心思路：不用全生成未来内容，仅预测紧凑的未来需求表征引导历史信息筛选，解决当前导向筛选遗漏后续关键信息的问题

  - 跨基座适配的模块设计可借鉴：筛选显式历史输入而非依赖模型内部状态，实现即插即用，大幅降低不同基座模型的适配成本

  - 长序列推理优化场景可复用：轻量前瞻Token预测的架构额外推理成本极低，可直接迁移到KV cache压缩、长用户行为序列召回等场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
长时序视频生成需处理不断增长的历史内容，全量保留成本高、冗余度高；现有基于当前内容的历史筛选方法仅关注当下需求，易丢弃后续生成所需的关键信息，导致长序列一致性差、内容失真。
### 方法关键点
1. 核心逻辑：不需要生成完整未来内容，仅预测少量代表未来信息需求的prospective tokens，即可引导历史关联信息筛选
2. 工程特性：筛选对象为显式历史帧而非生成器内部状态，可即插即用适配包括闭源模型在内的各类生成器，额外推理成本极低
### 关键结果
在5个基准数据集、11类生成模型（覆盖长视频生成、交互生成、动作条件世界模型）上验证，全场景下长序列一致性、视觉质量、动作对齐度均获得稳定提升。

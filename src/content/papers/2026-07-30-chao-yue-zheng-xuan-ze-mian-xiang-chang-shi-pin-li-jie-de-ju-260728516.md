---
title: 'Beyond Frame Selection: Generative Latent Evidence Aggregation for Long-Video
  Understanding'
title_zh: 超越帧选择：面向长视频理解的生成式隐式证据聚合框架
authors:
- Bowen Liu
- Shuning Wang
- Xinpeng Ding
- Zhiheng Wu
- Bodong Du
- Xiaomeng Li
affiliations:
- The Hong Kong University of Science and Technology
- Baidu Inc.
- Alibaba Group
- Xidian University
arxiv_id: '2607.28516'
url: https://arxiv.org/abs/2607.28516
pdf_url: https://arxiv.org/pdf/2607.28516
published: '2026-07-30'
collected: '2026-08-01'
category: Multimodal
direction: 多模态理解 · 长视频隐式证据聚合
tags:
- Video-MLLM
- Long-Video Understanding
- Latent Aggregation
- Adaptive Invocation
- Multimodal Reasoning
one_liner: 提出GenEvA生成式隐式证据聚合框架，极低开销下大幅提升Video-MLLM长视频理解性能
practical_value: '- 电商直播/短视频内容理解场景可复用查询条件分布方法，在有限采样帧下聚合跨帧关联信息，降低token开销同时提升理解准确率

  - 自适应证据调用机制可直接迁移至多模态LLM推理链路，按需触发跨帧信息聚合，无需对主干模型做大规模改造

  - 极低开销的后处理聚合模块设计，适合落地到资源受限的端侧/边缘侧多模态内容审核、商品打标等业务'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有长视频理解方案仅聚焦筛选相关帧作为显式证据，未解决跨时间片段互补线索的整合问题，导致Video-MLLM推理准确率受限，高token开销也难以适配落地场景。

### 方法关键点
1. 新增帧选择后隐式证据接口层，提出GenEvA分布引导的生成式隐式证据聚合框架；
2. 基于查询感知的证据分布引导聚合过程，仅对相关帧信息做跨帧融合，生成紧凑跨帧隐式证据；
3. 同一分布同时判断是否需要插入隐式补充信息，实现自适应证据调用。

### 关键结果
在4个基准数据集、2个Video-MLLM主干上均稳定超越匹配帧基线：8帧输入下LLaVA-Video四基准平均精度提升+5.2个点，Qwen2.5-VL在LVBench上精度提升+10.1个点，仅带来0.11%~0.40%的平均视频token额外开销。

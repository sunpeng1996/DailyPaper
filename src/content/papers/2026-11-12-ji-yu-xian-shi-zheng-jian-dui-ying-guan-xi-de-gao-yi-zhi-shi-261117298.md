---
title: Consistent Video-to-Video Translation via Explicit Correspondences
title_zh: 基于显式帧间对应关系的高一致性视频转视频生成方法
authors:
- Gaurav Parmar
- Zhengqi Li
- Richard Zhang
- Jun-Yan Zhu
- Srinivasa Narasimhan
- Eli Shechtman
- Yotam Nitzan
affiliations:
- Carnegie Mellon University
- Adobe Research
arxiv_id: '2611.17298'
url: https://arxiv.org/abs/2611.17298
pdf_url: https://arxiv.org/pdf/2611.17298
published: '2026-11-12'
collected: '2026-11-14'
category: Multimodal
direction: 多模态视频生成 · 时序一致性优化
tags:
- Vid2Vid
- Temporal Consistency
- Real-time Generation
- Cross-attention
- Autoregressive Generation
one_liner: 通过输入帧块级对应检索历史生成结果，兼顾实时性与长视频生成的时序一致性
practical_value: '- 电商商品短视频/直播AI特效生成场景，可复用帧块对应检索思路，避免长视频中商品外观、背景风格漂移，降低人工剪辑校正成本

  - 实时交互Agent的长序列生成场景（如直播数字人画面/话术同步生成），可借鉴滑动窗口+历史对应检索的架构，平衡推理时延与长序列内容一致性

  - 多模态长序列生成的性能优化上，可复用对应交叉注意力机制，无需缓存全量历史KV cache即可降低内存开销，维持实时推理效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
实时视频转视频应用需同时满足低时延与长时序一致性，现有方案为控制推理速度采用固定长度因果滑动窗口，关键信息滑出窗口后易出现内容漂移，而全量缓存历史会导致内存与时延线性上升，无法适配实时场景。
### 方法关键点
1. 基于「输入视频中匹配的区域，输出视频中对应区域也应匹配」的核心观察，提出vid2vid-long框架；
2. 先计算输入视频的patch级帧间对应关系，根据对应关系检索对应区域的历史生成结果；
3. 新增correspondence cross-attention层，将检索到的历史patch作为生成条件，无需依赖全量历史缓存。
### 关键结果
在现有主流视频生成模型上集成后，长程时序一致性显著提升，同时完全保留原模型的生成质量与实时推理性能。

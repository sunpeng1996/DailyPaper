---
title: 'StreamEmbed: Real-Time Indexing from Pixels for Screenshot Retrieval'
title_zh: StreamEmbed：面向截图检索的像素级实时索引系统
authors:
- Dayoon Ko
- Yichuan Wang
- Soyeong Jeong
- Joseph E. Gonzalez
- Gunhee Kim
- Sewon Min
affiliations:
- University of California, Berkeley
- Seoul National University
- KAIST
arxiv_id: '2611.18516'
url: https://arxiv.org/abs/2611.18516
pdf_url: https://arxiv.org/pdf/2611.18516
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agent视觉记忆 · 多模态检索优化
tags:
- Multimodal Retrieval
- KV Cache
- Real-time Indexing
- Agent Memory
- LoRA
- Quantization
one_liner: 利用截图时空冗余，通过剪枝+KV复用实现3.7倍编码提速的实时截图检索系统
practical_value: '- 端侧Agent视觉记忆场景可直接复用空间剪枝+跨帧KV复用策略，对商品浏览录屏、客服操作录屏等高冗余连续多模态输入，无需全量编码即可大幅降低编码延迟

  - 处理高冗余连续多模态输入（如直播帧、商品详情页滑动截图）时，可借鉴像素级差分判断冗余块的规则，配合小LoRA适配器做一致性对齐，几乎无损降低计算量

  - 长周期多模态向量索引场景可复用1-bit前512维量化+磁盘重排方案，1年截图索引仅占0.13GB RAM，检索延迟<0.1s，适配端侧大存量检索需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
端侧Agent与个人用户的屏幕历史可作为可检索的视觉记忆，但现有方案存在明显缺陷：OCR索引丢失视觉布局、选中态等信息，Recall@10比全量视觉编码低10个点；全量视觉编码延迟高达2.3s/张（M2 Pro GPU），无法满足5秒/次的实时截图索引需求，且连续截图存在极高时空冗余，全量重编码完全没有必要。
### 方法关键点
- 空间token剪枝：将截图拆分为32×32像素块，仅保留与左/上邻居像素差超过阈值的块，每3×3块强制保留1个避免均匀区域信息丢失，减少33%~41%计算量
- 时序KV复用：跨截图对比同位置块的像素差，仅重计算变化块的KV，缓存不变块的KV在ViT和LM中复用，每10帧或变化块占比超90%时全量刷新避免漂移，再减少34%~57%计算量
- 一致性适配器：用小LoRA蒸馏全量编码的模型输出，对齐剪枝/复用后的embedding与全量编码的相似度，合并进权重无额外推理开销
### 关键实验
在自建SCREENMEMEVAL基准（10426个查询、184小时人类/Agent屏幕历史）上测试：对比OCR+BM25、Qwen3-VL全量编码等基线，M2 Pro GPU下比全量编码快3.7倍，精度损失<2%；比同延迟的OCR索引高6.3个Recall@10；采用1-bit前512维量化后，1年截图索引仅占0.13GB RAM，检索延迟<0.1s。
### 核心结论
对于高冗余的连续多模态输入，基于像素级差分的冗余跳过+缓存复用策略，配合轻量蒸馏对齐，可在几乎无损精度的前提下大幅降低编码延迟，是端侧实时多模态索引的可行路径

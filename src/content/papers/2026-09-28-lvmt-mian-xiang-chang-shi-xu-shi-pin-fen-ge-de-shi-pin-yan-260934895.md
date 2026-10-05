---
title: 'LVMT: Video Mask Transformer for Long-term Video Segmentation'
title_zh: LVMT：面向长时序视频分割的视频掩码Transformer
authors:
- Narges Norouzi
- Niccolò Cavagnero
- Idil Esen Zulfikar
- Bastian Leibe
- Gijs Dubbelman
- Daan de Geus
affiliations:
- Eindhoven University of Technology
- RWTH Aachen University
arxiv_id: '2609.34895'
url: https://arxiv.org/abs/2609.34895
pdf_url: https://arxiv.org/pdf/2609.34895
published: '2026-09-28'
collected: '2026-10-05'
category: Other
direction: 长时序视频分割 · 掩码Transformer
tags:
- Video Segmentation
- Transformer
- GRU
- Temporal Propagation
- Training Strategy
one_liner: 提出带GRU时序传播与TQP训练策略的长视频分割模型，性能SOTA且速度为前代SOTA的10倍
practical_value: '- 长序列训练的TQP截断回传策略可直接迁移到长用户行为序列推荐模型训练，解决长序列OOM、梯度消失问题，无需修改推理逻辑

  - GRU自适应筛选传播信息的设计思路，可复用在用户兴趣演化建模模块，过滤用户历史冗余行为，提升兴趣表征精准度

  - 若涉及电商短视频/直播场景的商品实例分割、跟踪需求，可直接复用LVMT开源架构，兼顾精度与推理效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有在线视频分割方法难以应对长复杂视频中的长期遮挡跟踪问题，且长视频训练存在内存不足、梯度消失缺陷。
### 方法关键点
1. 设计轻量GRU基时序传播模块，可自适应筛选跨时间存储、传播的目标信息，解决时序传播冗余问题；
2. 提出Truncated Query Propagation (TQP)训练策略：将视频按帧分块处理，块间仅传播跟踪目标信息，块内独立执行反向传播，既支持更长时序监督，又避免OOM、梯度消失，且无额外推理开销。
### 关键结果
在6个基准集上取得多类视频分割任务SOTA，速度是此前SOTA的10倍；基于ViT-S/ViT-B/ViT-L backbone分别比基线PMT提升7.8/5.7/4.6个精度点

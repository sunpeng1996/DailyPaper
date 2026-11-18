---
title: 'Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models'
title_zh: Spool：面向混合视觉语言模型的低延迟流式推理框架
authors:
- Rui Ning
- Om Chabra
- Hari Balakrishnan
affiliations:
- MIT Computer Science and Artificial Intelligence Laboratory
arxiv_id: '2611.23228'
url: https://arxiv.org/abs/2611.23228
pdf_url: https://arxiv.org/pdf/2611.23228
published: '2026-11-17'
collected: '2026-11-18'
category: Multimodal
direction: 多模态大模型 · 流式推理优化
tags:
- VLM
- Streaming Inference
- KV Cache
- Low Latency
- Hybrid Model
one_liner: 无需训练实现混合VLM滑动窗口高效维护，p95首包延迟几何平均降6.6倍
practical_value: '- 直播电商实时内容审核、实时商品理解、多模态导购Agent场景的混合VLM部署，可复用滑动窗口维护思路，避免窗口滑动时全量重算的延迟尖峰，提升实时响应能力

  - Attention+Recurrent混合架构大模型的推理优化，可借鉴缓存单帧仿射变换+段树合并的思路，平衡内存开销与计算效率

  - KV缓存回收可复用尾填充（tail filling）方案，无需全量KV拷贝即可回收过期槽位，降低GPU内存占用

  - 长时流式场景下RoPE位置索引溢出问题，可采用定期rebasing方案，无需重新计算所有token的RoPE即可正常推理'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
混合VLM在实时视频理解、直播审核、多模态Embodied Agent等流式场景下需维护滑动帧窗口，传统prefix缓存滑动时完全失效，全量重算会带来29倍以上的延迟尖峰；且Recurrent层的全局共享状态无法像Attention KV缓存一样单独删除过期帧影响，现有方案延迟高、精度损失大，无法满足实时性要求。

### 方法关键点
- 无需额外训练，利用GDN/Mamba等Recurrent层更新的仿射特性，缓存每帧对应的（A,B）变换矩阵，删除过期帧时直接跳过对应变换即可重建当前窗口状态，无需重算保留帧
- 用段树存储连续帧的合并变换，将状态重建复杂度从O(W)降至O(log W)，W为窗口长度
- KV缓存采用尾填充方案，将尾部存活KV移到过期槽位，仅拷贝需移动的KV即可回收内存，避免全量拷贝开销
- 定期对RoPE做rebasing，统一减去位置偏移量并旋转缓存的Key，解决长流式场景下位置索引溢出RoPE表的问题

### 关键实验
在5个覆盖0.8B~122B参数的开源混合VLM、4个视频推理基准上测试，对比vLLM-Omni两个基线：20组模型-基准测试中p95 TTFT全部最低，几何平均比最优基线快6.6倍，最高提速35.7倍，16组测试p95 TTFT低于1s；在线精度平均比基线高2.3个百分点，最高提升18.4个百分点；离线精度与基线误差控制在±1.8个百分点以内；全系统内存开销仅比朴素缓存高9.2%，单帧摄入延迟降低7%~17%。

### 核心结论
对循环层的仿射更新特性进行缓存复用，是无需训练即可大幅降低混合架构大模型流式推理延迟的核心思路。

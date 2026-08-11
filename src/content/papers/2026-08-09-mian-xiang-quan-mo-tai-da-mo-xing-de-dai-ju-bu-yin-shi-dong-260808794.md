---
title: Deferred Audio Pruning with Local Audio-Visual Dynamics for Omni-LLMs
title_zh: 面向全模态大模型的带局部音视动态的延迟音频剪枝方法
authors:
- Kyeongyoon Lee
- Hongyeob Kim
- Youngeun Kim
- Sungeun Hong
affiliations:
- Sungkyunkwan University
- AWS AI Labs
arxiv_id: '2608.08794'
url: https://arxiv.org/abs/2608.08794
pdf_url: https://arxiv.org/pdf/2608.08794
published: '2026-08-09'
collected: '2026-08-11'
category: LLM
direction: 多模态LLM · 推理压缩加速
tags:
- Omni-LLM
- Token Pruning
- KV Cache
- Inference Acceleration
- Multimodal Compression
one_liner: 提出免训练两阶段全模态LLM token压缩框架，兼顾推理效率与多模态理解性能
practical_value: '- 电商多模态内容理解（直播、商品短视频打标/审核）场景可复用两阶段压缩思路：前置保留高价值的口播音频token、压缩冗余视频帧，后置基于用户/运营query剪枝无关内容，在不损失理解准确率的前提下降低推理成本

  - 可复用短窗口CKA局部音视动态匹配trick，替代传统token-wise跨模态匹配，避免直播口播与商品画面的时序错位匹配问题，提升多模态内容召回、打标的准确率

  - 免训练的渐进式KV cache剪枝方案可直接迁移至多模态Agent推理链路，在query相关度损失极小的前提下，降低长上下文（如1小时直播回放）的KV缓存开销，提升单卡推理并发量'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
全模态大模型可同时处理音视频+文本，在电商内容理解、多模态导购Agent等场景应用广泛，但长音视频序列会带来极高的预填FLOPs和KV缓存开销；现有压缩方案均在LLM前置阶段统一剪枝，容易丢失短时但高价值的音频信号（如直播的商品上新提示、用户关键提问），且token-wise跨模态匹配易关联时序错位的内容，导致多模态理解效果下降。

### 方法关键点
- 核心观测：音频单token任务相关信息密度是视频的9.8倍，表征多样性是视频的1.7倍，前置剪枝音频的收益低、损失风险高
- 第一阶段（LLM前置）：完整保留音频token，仅压缩视频；用窗口大小为3的Centered Kernel Alignment（CKA）计算局部音视动态相似度，结合query相关度分配视频token预算，再通过锚帧采样移除视频帧内冗余
- 第二阶段（LLM内部）：从中间 decoder 层开始，基于最后一个query token与各音视频token的注意力得分，按固定比例渐进式剪枝低相关token及对应KV cache条目，实现延迟音频剪枝，避免前置剪枝丢失关键信息

### 关键实验
基于Qwen2.5-Omni-7B/3B底座，对比FastV、OmniZip等7个SOTA免训练压缩方案，在AVUT、WorldSense等4个多模态基准测试：激进压缩场景下预填FLOPs最高降低78%，仅损失3%平均精度，解码throughput最高提升2.21倍，AVUT场景下GPU内存降低2.3GB。

**最值得记住的一句话：跨模态压缩需要根据不同模态的信息密度特性分阶段选择剪枝时机，而非统一前置剪枝，才能兼顾效率与效果。**

---
title: First Passage Attention
title_zh: 首次通路注意力（FPA）：基于路径极值的长上下文注意力优化机制
authors:
- Yuxuan Liu
affiliations:
- University of Bergen, Norway
arxiv_id: '2610.22714'
url: https://arxiv.org/abs/2610.22714
pdf_url: https://arxiv.org/pdf/2610.22714
published: '2026-10-14'
collected: '2026-10-21'
category: LLM
direction: LLM注意力优化 · 长上下文外推
tags:
- Attention
- Long Context
- KV Cache
- Transformer
- Length Extrapolation
one_liner: 提出基于路径极值的首次通路注意力，兼容现有遗忘机制，大幅提升长上下文外推能力与KV cache压缩率
practical_value: '- 长上下文业务场景（电商用户全生命周期行为序列建模、Agent长对话记忆、长文档RAG）可直接复用FPA的KV cache压缩策略，仅保留25%缓存即可实现100%长序列召回，大幅降低推理内存开销

  - 序列存在局部失效场景（比如用户会话边界、已取消的订单、失效的历史偏好）可借鉴FPA的深度优先而非时长优先的遗忘逻辑，避免一刀切的滑动窗口或单调衰减误删有效旧信息

  - FPA的训练推理性能与现有注意力模块接近，可直接替换Transformer中的标准注意力，无需大幅改造工程架构即可获得长上下文能力增益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有带遗忘门的注意力机制依赖路径累加计算，衰减逻辑单调，无法在保留老旧有效token的同时精准删除中间失效token；且累加计算易混淆事件深度与持续时长，引入额外计算开销，长上下文外推能力、KV cache压缩率均存在明显瓶颈。
### 方法关键点
- 提出First Passage Attention（FPA），用路径区间最小值取代传统累加计算，key的logit衰减仅与后续序列中低于key level的最深跌幅相关，与跌幅持续时长无关
- 单头常数维度即可实现任意存活key集合，兼容FoX、Expire-Span、ALiBi等已有机制作为特殊case
- 采用直通过估计器解决训练时梯度消失问题，自研Triton kernel的训练速度与PyTorch SDPA基本持平
### 关键实验结果
基于110M参数语言模型，训练上下文长度2048，对比FoX、Selective Attention、RoPE Softmax等基线：
- 长上下文passkey检索在8倍训练长度（16384）下准确率100%，同期FoX仅20%
- KV cache压缩到25%仍可保持100% passkey检索准确率，远优于基线的压缩上限
- 训练吞吐量为FoX的91.4%，8k长度下推理延迟22ms/token，优于Softmax的23.9ms
### 核心结论
基于路径极值的遗忘逻辑可在不损失长上下文召回能力的前提下，实现远高于传统累加机制的KV cache压缩率和长度外推能力

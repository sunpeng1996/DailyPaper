---
title: 'Factorized Context Attention: From Emulated to Native Grid Probing'
title_zh: 因子化上下文注意力：从模拟网格探测到原生实现
authors:
- Mohamed Eltahir
- Manar Eyad
- Yara Alzahrani
- Fatimah Albesher
- Duaa M. Tahir
- Tanveer Hussain
- Naeemullah Khan
affiliations:
- King Abdullah University of Science and Technology (KAUST)
- Edge Hill University
arxiv_id: '2611.32423'
url: https://arxiv.org/abs/2611.32423
pdf_url: https://arxiv.org/pdf/2611.32423
published: '2026-11-23'
collected: '2026-11-25'
category: LLM
direction: LLM长上下文推理 · 注意力优化
tags:
- Long-Context LLM
- Sparse Attention
- KV Cache
- Grid Probing
- Training-Free
one_liner: 训练-free的原生块稀疏注意力FCA，数倍提升网格探测效率且完全保持精度
practical_value: '- 电商/推荐场景处理超长用户行为序列、商品评论集、直播回放内容时，可直接用FCA替代传统网格探测，无需微调现有LLM，在保持长上下文理解精度的前提下，算力成本降低50%以上，还能突破原生窗口限制处理4倍长度内容

  - 多轮客服Agent、用户多轮意图推荐场景下，FCA一次编码上下文即可支持多轮问答，后续请求延迟仅为网格探测的1/10，完全满足线上高并发的低延迟要求

  - stair位置编码方案可直接复用到现有长序列处理链路，无需额外做位置插值微调，解决跨片段位置偏移问题，节省微调成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文推理是LLM落地电商、内容场景的核心瓶颈：单pass长序列推理存在明显精度衰减，且受限于模型原生上下文窗口；稀疏注意力等优化方案无法解决窗口限制和精度问题；近年提出的网格探测类方法虽然能突破窗口、保持精度，但每个上下文片段都需要单独调用模型，重复编码带来极高的算力成本，无法落地高并发线上场景。

### 方法关键点
- 首次将网格探测定义为外置的模拟注意力，提出训练-free的因子化上下文注意力（FCA），无需微调冻结模型即可实现原生网格探测逻辑
- 上下文仅做一次编码存入KV cache，所有本地、跨步片段的探测请求通过掩码注意力在单批量前向中完成，彻底消除重复编码开销
- 设计stair位置调度策略，让所有片段的位置编码都落在模型训练的有效范围内，避免位置偏移导致的精度损失
- 完全复用网格探测的分数pooling与证据定位逻辑，保持原方案的精度和可解释性

### 关键实验
在长文本QA（InfiniteBench、SCBench）、长视频QA（LongVideoBench、Video-MME）、图像grounding三类任务上测试，对比单pass推理、网格探测两类基线：精度与网格探测持平，长文本任务比单pass高9~14个点，长视频任务高约10个点；可稳定处理4倍于模型原生窗口的上下文，单问题推理速度是网格探测的1.1~3.9倍，多轮场景下后续请求延迟仅为网格探测的1/10~1/7。

### 最值得记住的一句话
外置prompt层的长上下文优化逻辑可以转化为模型原生的注意力模式，在无需微调的前提下兼顾效果、效率和可扩展性。

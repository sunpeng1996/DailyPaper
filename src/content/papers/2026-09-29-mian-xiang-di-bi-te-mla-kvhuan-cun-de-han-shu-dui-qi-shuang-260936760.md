---
title: 'QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching'
title_zh: 面向低比特MLA KV缓存的函数对齐双路径量化方案QuantMLA
authors:
- Zunhai Su
- Yuxuan Sun
- Jianchao Tan
- Tao Zhang
- Ruihan Hu
- Yuchen Xie
- Xunliang Cai
- Ngai Wong
affiliations:
- The University of Hong Kong
- Meituan LongCat Team
- South China University of Technology
- Harbin Institute of Technology
arxiv_id: '2609.36760'
url: https://arxiv.org/abs/2609.36760
pdf_url: https://arxiv.org/pdf/2609.36760
published: '2026-09-29'
collected: '2026-10-12'
category: LLM
direction: LLM推理优化 · MLA KV缓存低比特量化
tags:
- KV cache
- MLA
- quantization
- INT4
- LLM serving
one_liner: 实现MLA双路径联合INT4 KV缓存量化，缓存压缩3.59倍、高负载吞吐量提升5.168倍
practical_value: '- 部署MLA架构大模型（如DeepSeek-V3、美团LongCat系列）的电商智能客服、推荐导购Agent可直接复用QuantMLA方案，在精度损失<0.3%的前提下实现3倍以上KV缓存压缩，提升长对话场景的并发承载能力

  - RoPE路径量化误差是内容路径的1.94~6.86倍的结论可迁移到所有带RoPE的LLM量化优化，做KV缓存压缩时优先对RoPE路径做精度保护，可大幅降低整体量化失真

  - 离线可融合变换的设计思路可复用在各类模型结构的量化落地中，所有变换提前融合到模型权重，无需修改推理算子逻辑，可无缝适配vLLM等主流推理框架

  - 混合精度缓存策略（首尾关键token保留BF16、中间历史用低比特）可直接落地到长上下文RAG、用户行为序列建模场景，在内存和精度之间取得最优平衡'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Multi-Head Latent Attention(MLA)已被DeepSeek-V3、Kimi K3、美团LongCat等主流长上下文大模型采用，通过共享内容缓存+解耦RoPE密钥缓存的设计大幅降低KV缓存开销，但现有方案仅对内容缓存做FP8量化、RoPE缓存保留高精度，联合低比特量化的误差传递机制不明确，限制了长上下文场景下的推理吞吐提升，高并发Agent服务、长对话推荐等业务场景的部署成本居高不下。
### 方法关键点
- 建立双路径量化误差模型，实验证实相同缓存重建误差下，RoPE路径导致的输出失真比内容路径高1.94~6.86倍，RoPE误差仅通过位置匹配环节传递、对输出更敏感
- 推导路径专属的离线可融合变换空间：内容路径用正交旋转+通道缩放，RoPE路径用频率对旋转+绑定缩放，所有变换可离线融合到模型参数，无在线推理开销
- 设计函数对齐的学习目标：内容路径用注意力输出重建目标捕捉匹配+聚合的耦合误差，RoPE路径用位置QK重建目标控制位置逻辑误差，后者有理论输出失真界保障
- 实现原生低比特MLA算子，将解包、反量化融合到注意力计算，搭配混合精度策略（前4个sink token+最近128个token保留BF16，其余用低比特）
### 关键实验
覆盖4个MLA模型家族，对比RTN、SmoothQuant、QuaRot等基线，INT4联合量化(C4R4)下10任务平均精度仅比BF16低0.13~0.26个百分点；128K上下文下KV缓存压缩率达3.59倍，同等vLLM调度策略下缓存高负载场景的整任务输出吞吐量是BF16的5.168倍，无任务抢占。
> 最值得记住：RoPE路径的量化误差放大效应远高于内容路径，针对路径功能设计专属量化目标、离线融合变换是低比特量化无精度损失、无额外开销的核心

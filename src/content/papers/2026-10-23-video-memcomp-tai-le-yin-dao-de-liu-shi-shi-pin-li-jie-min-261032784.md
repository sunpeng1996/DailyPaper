---
title: 'Video-MemComp: Taylor-Guided Sensitivity-Aware Memory Management for Streaming
  Video Understanding'
title_zh: Video-MemComp：泰勒引导的流式视频理解敏感度感知内存管理框架
authors:
- Yonghui Niu
- Yuhao Ji
- Chang Nie
- Jiao Zhang
- Yilong Li
- Junlan Feng
- Ran He
- Caifeng Shan
- Chaoyou Fu
affiliations:
- NJU
- Jiutian AI
- CASIA
arxiv_id: '2610.32784'
url: https://arxiv.org/abs/2610.32784
pdf_url: https://arxiv.org/pdf/2610.32784
published: '2026-10-23'
collected: '2026-10-26'
category: LLM
direction: 多模态大模型 · KV缓存推理优化
tags:
- KV cache
- Taylor Expansion
- Streaming Video
- MLLM
- Memory Optimization
one_liner: 基于一阶泰勒分解的训练无关流式视频KV缓存优化，降90%内存同时提升推理精度
practical_value: '- 训练无关的KV缓存优化方案可直接落地到直播/短视频导购Agent的长视频理解场景，无需微调模型即可将消费级GPU的显存占用降低90%，避免OOM

  - 一阶泰勒分解拆分误差为层敏感度+局部近似误差的思路可复用在长文本/多模态推荐场景的LLM推理优化，优先给浅层高敏感层分配缓存预算，抑制误差放大

  - Pre-RoPE token聚合加log(fusion count) logit bias的trick可直接用于多模态召回/排序的视觉特征压缩阶段，在保留注意力权重一致性的前提下降低计算开销

  - 离线梯度先验+在线上下文熵的混合预算分配策略比纯启发式缓存裁剪更稳定，可复用在所有长上下文LLM服务的资源调度流程中'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
流式视频理解是直播内容审核、AR导购、具身Agent等业务场景的核心能力，但多模态大模型（MLLM）的KV缓存随输入序列长度线性增长，在资源受限的端侧或消费级GPU上极易触发OOM，现有压缩方法普遍忽略误差逐层放大效应，要么精度损失严重，要么内存节省幅度不足。
### 方法关键点
- 基于一阶泰勒展开将全局输出误差分解为两个正交可优化分量：层结构敏感度Sl（梯度范数，表征该层误差对最终输出的放大系数）、局部近似误差El（每层压缩引入的信息损失）
- 最小化El：在RoPE注入前的特征空间做token聚合，按每个存活token融合的原始token数加log(f_i)的logit bias，保证聚合后注意力质量不被稀释；同时每层用通用对话模板构造代理Query计算KV重要性，做稀疏裁剪
- 管控Sl：离线预计算各层的Sl梯度先验，在线结合层注意力熵和特征范数，采用三混合策略动态分配KV缓存预算，给浅层高敏感层分配更多额度，低敏感层大幅裁剪
- 完全训练无关、模型架构无关，实现严格O(1)内存占用
### 关键实验
在MLVU、VideoMME、EgoSchema、RVS等主流视频理解基准上测试，对比Full KV、InfiniPot-V、StreamMem等SOTA方案：
- Qwen2.5-VL-3B上，KV缓存压缩到每层6000token，节省90%+显存的同时，整体精度从62.3%提升至64.1%
- Qwen2-VL-7B上6K预算下精度达65.5%，超过Full KV基线的64.9%和InfiniPot-V的64.7%
- 流式RVS基准内存受限场景下平均精度56.6%，优于所有对比方案
### 核心洞察
基于误差传播原理的结构化资源分配远优于纯启发式缓存裁剪，合理的冗余过滤不仅不会损失精度，反而能实现"少即是多"的效果

---
title: 'C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference'
title_zh: C²KV：面向高效LLM推理的可压缩可组合KV缓存复用框架
authors:
- Chuheng Du
- Junyi Chen
- Hanlin Tang
- Kan Liu
- Tao Lan
- Lin Qu
- Chaoyue Niu
- Shengzhong Liu
- Guihai Chen
- Fan Wu
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
arxiv_id: '2607.17715'
url: https://arxiv.org/abs/2607.17715
pdf_url: https://arxiv.org/pdf/2607.17715
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: LLM推理优化 · 可组合KV缓存复用
tags:
- KV Cache
- LLM Inference
- Long Context
- KV Compression
- Non-prefix Reuse
one_liner: 通过轻量外挂模块与结构化注意力，实现可压缩可组合非前缀KV缓存复用，最高17倍长上下文推理提速
practical_value: '- 电商/Agent场景的RAG服务可直接复用C2KV的离线预压缩KV方案，将商品详情、知识库文档提前预处理为可任意拼接的C2KV，大幅降低在线请求的TTFT，提升用户交互体验

  - 仅需新增约10%参数量的轻量侧car模块，基座LLM完全冻结无需全量微调，适配业务多基座快速迭代需求，训练和落地成本极低

  - 结构化注意力流+压缩拼接联合训练的设计思路可迁移到个性化推荐的用户长行为序列编码场景，降低长序列召回/排序的存储和计算开销

  - 长上下文LLM导购、商品文案生成等场景可落地C2KV，大幅降低KV缓存存储与内存带宽开销，显著提升单卡推理并发吞吐'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM推理（如RAG、Agent长记忆、多文档问答等场景）的KV缓存存储与内存带宽已成为核心瓶颈，现有非前缀KV复用方案仅优化预计算开销，忽略存储传输成本；而普通KV压缩方法生成的表示与原始上下文强绑定，跨请求拼接复用时会出现严重精度损失，两类方案无法直接叠加使用。
### 方法关键点
- 设计轻量外挂C2Extractor模块，基座LLM完全冻结，仅新增可学习C2Token作为压缩槽位和专属QKV投影头，额外参数量仅约10%
- 采用结构化信息流（SIF）的注意力掩码约束：原token不可关注C2Token保证基座原生能力不变，C2Token仅关注对应块的原token与前置C2Token，生成位置无关的模块化KV表示
- 采用压缩-拼接联合训练策略，基于多文档拼接的问答任务做SFT，让压缩后的KV天然支持任意位置拼接复用，推理时直接加载拼接无需额外重计算
### 关键实验
在LongBench、RULER等长上下文基准测试，覆盖Qwen3、Llama3.1等多个模型家族，对比Full Recompute、CacheBlend、EPIC等5个基线方案；最高实现17倍长上下文推理提速，4倍压缩下精度接近全量预填充基线，16倍压缩下性能仍优于现有KV复用方案，解码时延随上下文长度增长的趋势被大幅平缓。
### 核心结论
KV缓存压缩和复用不能简单叠加，必须联合设计位置无关的可组合表示，才能同时优化计算、存储、带宽三类长上下文推理开销

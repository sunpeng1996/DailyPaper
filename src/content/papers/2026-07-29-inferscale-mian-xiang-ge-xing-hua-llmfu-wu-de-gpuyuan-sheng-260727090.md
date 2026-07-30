---
title: 'InferScale: GPU-Native KV Injection for Personalized LLM Serving'
title_zh: InferScale：面向个性化LLM服务的GPU原生KV注入系统
authors:
- Peter Li
- Prashant Pandey
affiliations:
- Northeastern University
arxiv_id: '2607.27090'
url: https://arxiv.org/abs/2607.27090
pdf_url: https://arxiv.org/pdf/2607.27090
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: LLM服务优化 · KV cache复用
tags:
- KV cache
- LLM Serving
- RoPE
- vLLM
- Personalized LLM
one_liner: 通过预计算记忆KV直接注入vLLM分页缓存，大幅降低带个性化记忆的LLM服务延迟
practical_value: '- 落地带用户长期记忆的电商导购/智能客服Agent时，可将用户画像、历史行为等固定记忆预计算KV存储在GPU，避免每次请求重复拼接prompt预填充，TTFT可降低70%+，大幅提升用户体验

  - Chunked RoPE技巧可直接复用：存储预旋转的Key，注入时按实际位置动态施加RoPE，无需改模型或微调即可实现动态拼接上下文的KV复用，适配所有RAG场景

  - Context-Window Encoding方案可借鉴：离线编码记忆片段时携带前序小窗口上下文，仅保留目标片段KV，既保留上下文消歧义能力，又不增加在线推理成本，精度接近prompt注入

  - 工程实现可直接基于vLLM的KV connector接口开发插件，无需修改vLLM内核，适配现有LLM服务栈的成本极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
带持久个性化记忆的LLM服务（如电商导购、个人助理）当前普遍依赖Mem0类RAG系统，将检索到的记忆拼接进prompt后重复预填充，TTFT随检索记忆量增长快速上升，传统前缀KV缓存仅支持固定位置prompt复用，无法适配动态拼接的检索上下文。

### 方法关键点
- 离线预计算每个记忆片段的KV表示，与语义embedding共同存储在GPU端，在线检索后直接将KV注入vLLM分页缓存，仅需预填充query部分
- 设计Chunked RoPE：存储Key时不施加旋转，注入时根据记忆在当前prompt的实际位置动态计算旋转后Key，保证任意位置KV注入与prompt预填充效果完全等价
- 提出Context-Window Encoding：离线编码记忆时携带前序小窗口对话上下文，仅保留目标记忆的KV，缓解独立编码丢失跨片段上下文的精度损失
- 完全基于vLLM KV connector接口实现，无需修改服务引擎、模型微调，兼容现有检索流水线

### 关键结果
在LoCoMo长对话QA数据集对比SOTA记忆系统Mem0：Llama-3.1-8B上检索量k从5涨到50时，TTFT仅上升4%（16.6→17.3ms），Mem0上升106%（33.2→68.3ms）；k=50时TTFT降低72~79%，精度仅低3pp（60.3% vs 63.3%），100并发下吞吐量是Mem0的3.7~4.5倍。

> 最值得记住：可复用KV状态可实现带记忆LLM服务延迟与检索上下文大小解耦，几乎无精度损失

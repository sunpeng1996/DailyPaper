---
title: 'Written as a Record, Read as an Address: What a Forward Pass Leaves in an
  Operation''s KV Cache'
title_zh: 《前向传播在操作段KV缓存中留存的可恢复记录机制研究》
authors:
- Lingfeng Wu
- Behzad Shomali
affiliations:
- University of Bonn
- Lamarr Institute
arxiv_id: '2609.24635'
url: https://arxiv.org/abs/2609.24635
pdf_url: https://arxiv.org/pdf/2609.24635
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: LLM可解释性 · KV cache机制
tags:
- KV_cache
- LoRA
- Transformer
- Causal_Probing
- LLM_Mechanism
one_liner: 通过冻结写KV的基座单独训练读端，证明操作段KV缓存同时存储路由地址与载荷信息
practical_value: '- 做LLM驱动的电商/广告Agent状态追踪时，可直接抽取Llama 12-15层、Mistral 14-17层操作数token的KV值获取状态更新结果，无需全量重跑上下文

  - 推理优化时，操作类场景可针对性缓存操作段固定层KV值，降低缓存占用的同时，可搭配轻量LoRA适配器直接读状态，大幅降低长上下文推理延迟

  - 微调场景下，对需要从历史操作中提取信息的任务（如订单操作查询、用户行为回溯），可采用仅训练读端LoRA的隔离训练范式，冻住基座降低训练成本，不破坏基座原生能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
过往LLM实体追踪研究仅关注模型推理时实际使用的信息，传统探测方法存在假阳性，无法区分KV缓存中实际存储的内容和模型原生会读取的内容，也无法明确前向传播在操作段KV缓存中到底留存了什么信息。

### 方法关键点
- 提出冻结写端、训练读端的因果验证范式：写端为无梯度、无LoRA的基座LLM，处理完整上下文生成KV缓存；读端仅能看到操作段token，注意力屏蔽所有状态描述行，仅对查询/回答段的q/k/v/o加rank16 LoRA训练，确保读端获取的所有信息都来自原生KV缓存
- 设计三种读视图做对照：OPEN（全上下文可见）、OP_ONLY（仅操作段可见）、BLOCKED（全屏蔽，零信息基线），搭配跨世界操作段KV移植实验，验证KV的因果作用
- 定义两类核心能力指标：路由（KV控制下游读哪条外部状态）、载荷（直接从KV读取操作结果，无需外部状态）

### 关键结果
- 测试覆盖合成盒子交换任务、代码操作任务、ToMi、GSM8K，模型包括Llama-3.2-1B、Llama-3.1-8B、Mistral-7B
- 原生模型仅使用操作段KV做路由，OP_ONLY下回答准确率≤0.06；隔离训练后OP_ONLY准确率提升到0.75~1.00，同时完全保留原生路由能力
- 路由与载荷信息都存储在操作数字段token的中层KV：Llama 3.1-8B为12~15层，Mistral-7B为14~17层

**最值得记住的一句话**：LLM操作段KV缓存天生存储了路由和完整操作结果信息，只是原生模型只会把它当地址用，不会直接读取结果。

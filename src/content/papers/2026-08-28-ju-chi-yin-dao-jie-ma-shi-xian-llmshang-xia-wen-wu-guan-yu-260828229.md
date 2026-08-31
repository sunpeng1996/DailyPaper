---
title: 'Stay Within Your Bounds: Distance-Guided Decoding for Guaranteed Context-Free
  Grammar Compliance'
title_zh: 距离引导解码实现LLM上下文无关语法输出100%合规性
authors:
- Vincenzo Collura
- Karim Tit
- Eleonora Giunchiglia
- Mike Papadakis
- Maxime Cordy
affiliations:
- University of Luxembourg
- Imperial College London
arxiv_id: '2608.28229'
url: https://arxiv.org/abs/2608.28229
pdf_url: https://arxiv.org/pdf/2608.28229
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM结构化生成 · CFG约束解码
tags:
- Constrained Decoding
- Context-Free Grammar
- Pushdown Automaton
- Structured Generation
- Beam Search
one_liner: 基于下推自动机预计算可达距离的CFG约束解码框架，实现全场景结构化输出语法100%合规
practical_value: '- 电商Agent调用工具/生成SQL/返回结构化JSON时，可复用该框架实现100%语法合规，避免下游解析失败导致的链路故障

  - 生成式推荐需要输出固定格式的商品标签/结构化文案时，可将格式规则抽象为CFG，通过预计算距离估计引导解码，不需要反复采样校验降低延迟

  - 可复用其距离引导重排序逻辑，在有限token预算下优先选择更接近完成状态的候选token，避免生成长而无效的中间结构

  - 对于固定格式的生成任务，语法到PDA的转换和距离预计算可离线完成，跨请求复用，仅带来可接受的解码延迟开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有CFG约束解码仅做局部前缀可行性校验，在tokenizer与语法不匹配、有限token预算场景下，即使每一步前缀都合法，最终输出仍可能语法无效；同时局部校验缺乏全局进度感知，容易生成大量无意义嵌套结构，浪费token预算也无法满足下游解析要求。
### 方法关键点
- 离线阶段：将目标CFG转换为下推自动机（PDA），基于加权下推系统预计算不同PDA配置到接受状态的最小token距离上界，存储到配置库可跨请求复用
- 在线解码：融合LLM Top-K候选与PDA自动生成的合法候选token，通过预计算的距离估计过滤剩余token预算不足以完成的无效路径
- 距离引导重打分：对合法候选token，根据其距离接受状态的远近调整logit，优先选择推进度快的候选，配合beam search保留高价值路径
- 实现tokenizer感知的PDA状态转移，兼容子词token与语法终端的匹配问题，保证输出语法健全性
### 关键实验
在JSON、SQL、LTL三个结构化生成任务上，对比Outlines、XGrammar、SynCode、GenLM等主流约束解码方法，跨Llama3.1-8B、Llama3.2-3B、Qwen2.5-7B三个基座均实现100%语法正确性；JSON任务同时实现100% Schema合规，SQL任务执行精度最高提升8.2pct，LTL任务精度最高提升12.5pct，解码延迟仅略高于轻量级局部校验方法，远低于采样校验方案。
> 最值得记住：局部前缀合法≠最终输出合法，为CFG约束解码增加全局距离感知信号，可在几乎不损失生成质量的前提下实现100%语法合规

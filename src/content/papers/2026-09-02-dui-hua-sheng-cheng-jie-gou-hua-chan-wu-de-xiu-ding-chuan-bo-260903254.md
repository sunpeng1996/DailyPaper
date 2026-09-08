---
title: What Else Needs Fixing? Exploring Cost-Effective Test-Time Compute for Revision
  Propagation in Artifacts Generated Through Conversation
title_zh: 对话生成结构化产物的修订传播及高性价比测试时计算探索
authors:
- Daisuke Kikuta
affiliations:
- NTT, Inc.
arxiv_id: '2609.03254'
url: https://arxiv.org/abs/2609.03254
pdf_url: https://arxiv.org/pdf/2609.03254
published: '2026-09-02'
collected: '2026-09-08'
category: LLM
direction: LLM测试时计算 · 结构化内容修订
tags:
- Test-time Compute
- Revision Propagation
- JSON Editing
- LLM Benchmark
- Structured Output
one_liner: 构建对话生成JSON产物修订传播基准，验证3样本并行选择的测试时计算方案性价比最优
practical_value: '- 电商场景下结构化内容（购物车、订单、营销方案、用户权益配置）的联动修订需求，优先采用3样本并行+MED选择方案，仅需1.2~1.5倍基线推理延迟，即可提升2.2~9.7%的修订准确率，成本增加极低

  - 所有涉及对话生成的结构化内容修订场景，必须同时传入最终结构化产物+完整对话历史作为上下文，相比仅传产物最多可提升22%的准确率（如Qwen3.5-9B从62%提升至83%）

  - 低延迟要求的实时修订场景（如购物车修改、订单地址变更后的联动更新），避免使用串行REFLECT迭代方案，优先选择并行采样+MED方案，延迟远低于串行迭代

  - 对准确率要求极高的场景（如发票修订、财务结算配置调整），可采用4样本并行+LLM SELECT方案，准确率最高可提升12.5%，成本可控'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM多轮对话生成结构化产物（如行程、订单、配置方案）的修订场景中，用户通常仅提出局部修改要求，LLM需要识别隐式依赖并将修订传播到所有关联部分。但现有研究多聚焦于依赖可静态解析的场景（代码、文档、知识编辑），缺乏对依赖隐式存在于对话历史场景的统一评估基准，也没有经过验证的高性价比测试时计算优化方案。
### 方法关键点
- 构建RevPropBench人工标注基准，覆盖9个领域（含购物车、发票、行程等电商相关场景），共150个样本，分10/50/100元素三种JSON产物规模，覆盖算术重计算、时间偏移等6种修订传播模式
- 对比9种修订方法：3种单推理基线（仅传产物J/仅传历史H/传J+H）、串行REFLECT迭代优化、4种并行采样+规则选择（OR/AND/MAJ/MED）、并行采样+LLM选择（SELECT）
- 测试6款不同参数规模的主流LLM：gpt-oss-20b/120b、gpt-5.4-mini、qwen3.5-9b/27b/122b
### 关键结果
- 单推理基线中J+H（产物+历史）效果最优，准确率范围68.3%（qwen3.5-9b）~93%（gpt-5.4-mini），比仅传J最高提升22%
- 测试时优化方案中，3样本并行的MED/SELECT性价比最高，相比基线准确率提升2.2~9.7%，其中MED仅需1.2~1.5倍基线延迟，SELECT最高提升12.5%
- 串行REFLECT方案增益仅0.5~8.2%，延迟为基线的2~6倍，性价比远低于并行方案

> 最值得记住：依赖隐式的结构化内容修订场景，3样本并行+MED/SELECT是兼顾准确率、成本、延迟的最优测试时优化方案

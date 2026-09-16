---
title: 'Shared-Prefix KV Reuse Across Standard LoRA Adapters: Quality and Serving
  Tradeoffs'
title_zh: 标准LoRA适配器间共享前缀KV复用的效果与服务权衡
authors:
- Dushyant Rajput
affiliations:
- AltSlate Labs LLP
arxiv_id: '2609.17109'
url: https://arxiv.org/abs/2609.17109
pdf_url: https://arxiv.org/pdf/2609.17109
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: LLM 推理部署 · KV cache 复用
tags:
- LoRA
- KV cache
- inference optimization
- serving latency
- LLM deployment
one_liner: 量化无需重训的标准LoRA间复用基模型前缀KV缓存的质量损失与推理性能收益
practical_value: '- 多LoRA并行的Agent/推荐场景（如同一用户上下文同时跑意图识别、商品推荐、营销文案生成）可直接复用基模型前缀KV缓存，8K上下文下TTFT提升约16倍，仅损失个位数精度，可优先在对精度要求不敏感的场景上线

  - 无需尝试KV翻译器、部分前缀重计算类复杂优化，实测两类方案性价比均低于直接全前缀KV复用

  - 现有KV复用实现仅能降低计算开销无法节省内存，要实现跨LoRA物理内存共享需对接PagedAttention等分页缓存架构，无需在普通缓存上做内存优化

  - 精度损失幅度与LoRA初始化种子、上下文长度强相关，上线前必须使用业务自有LoRA做验证，不要直接复用论文中的损失数值'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前小模型部署普遍采用「共享基座+多LoRA专家」架构，电商/推荐场景中同一用户上下文常需同时跑意图识别、召回排序、文案生成等多个LoRA，原生服务会对每个LoRA重复计算相同前缀的KV缓存，浪费算力；现有KV复用方案要么需要重训LoRA适配缓存，要么面向跨基座模型场景，不兼容已训好的标准LoRA，亟需明确无重训复用的收益与损失。
### 方法关键点
- 基座采用Qwen3-1.7B，训练2个标准LoRA：HotpotQA抽取式QA、GSM8K数学推理，rank=16、α=32
- 复用逻辑：关闭LoRA完成前缀预填充得到基模型KV缓存，切换目标LoRA后仅处理剩余prompt后缀+生成，无需额外KV映射
- 对比4种接管边界：原生（全量LoRA预填充）、早期接管、问题接管、全前缀复用
- 采用配对bootstrap 95%置信区间评估，降低随机误差干扰
### 关键实验结果
- 性能收益：8K上下文下warm-cache TTFT从486ms降至30ms，提升约16倍；双LoRA并行时8K上下文峰值内存仅降12%，无物理内存共享，仅减少了重复预填充的激活峰值
- 质量损失：GSM8K任务全前缀复用EM降4.6pp（160token生成预算），提至320token预算后降3pp，换初始化种子后仅降0.8pp，多数置信区间包含0；QA任务700token上下文精度无损失，2K/8K上下文F1分别降6.6/4.5pp
- 负结果：KV ridge翻译器、部分前缀重计算均无显著收益，性价比低于直接全前缀复用
### 核心结论
标准LoRA跨适配器全前缀KV复用是性价比极高的推理优化手段，优先在对TTFT敏感、精度容忍度高的场景落地即可，无需为极小的精度损失做复杂额外优化

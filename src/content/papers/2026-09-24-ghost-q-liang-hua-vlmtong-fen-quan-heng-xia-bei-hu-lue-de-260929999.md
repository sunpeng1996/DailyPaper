---
title: 'GHOST-Q: Towards Studying Grounding Hallucinations Overlooked Under Same-score
  TradeOffs in Quantized VLMS'
title_zh: 《GHOST-Q：量化VLM同分权衡下被忽略的视觉Grounding幻觉研究》
authors:
- Saim Rehman
- Muhammad Shafique
affiliations:
- New York University Abu Dhabi (NYUAD)
- eBRAIN Lab, NYUAD Division of Engineering
arxiv_id: '2609.29999'
url: https://arxiv.org/abs/2609.29999
pdf_url: https://arxiv.org/pdf/2609.29999
published: '2026-09-24'
collected: '2026-09-25'
category: Eval
direction: 多模态大模型量化 · 幻觉评估
tags:
- VLM
- Quantization
- Hallucination
- Visual Grounding
- Model Evaluation
one_liner: 提出逐样本配对的量化VLM评估框架，验证总精度不变时grounding幻觉风险显著上升
practical_value: '- 电商多模态商品理解、多模态Agent场景选用量化VLM时，不能仅校验总精度，必须新增grounding幻觉专项评测，避免商品属性识别错误、图文不符等问题

  - 量化VLM上线前必须在业务部署的硬件上做端到端压测，内存下降不代表推理latency降低，避免线上性能不符合预期

  - 8B级开源VLM做INT8/NF4量化时，需提前验证生成截断问题，不同架构的生成预算censoring程度差异大，影响商品文案生成、多轮对话等长输出场景'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM量化评估仅关注聚合任务精度与内存收益，忽略量化对视觉grounding行为的影响，相同总得分下可能存在隐性幻觉风险，且量化的推理延时收益也缺乏端到端验证。
### 方法关键点
提出GHOST-Q跨精度对照评估框架，对Qwen3-VL、InternVL3、Idefics3共3款8B参数VLM，分别在FP16、INT8、NF4精度下逐样本配对对比预测结果，同时覆盖普通任务基准与幻觉敏感基准，搭配A100端到端推理性能 profiling，以及AMBER开放生成审计。
### 关键结果
6款量化变体中有5款MMStar精度波动≤±2pp，但36组配对效应中10组经FDR校正后仍显著，其中9组出现在幻觉敏感场景；量化带来的内存下降不必然对应推理latency降低；不同架构、不同精度下的生成预算截断效应差异显著。

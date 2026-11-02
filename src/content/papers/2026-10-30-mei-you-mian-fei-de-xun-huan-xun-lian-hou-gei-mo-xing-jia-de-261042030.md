---
title: 'There Is No Free Loop: When Does Looping a Trained Model Pay for Its Inference
  Compute?'
title_zh: 没有免费的循环：训练后给模型加层循环的推理成本收益分析
authors:
- Rhea Sanjay Sukthanker
- Pashmina Cameron
affiliations:
- Microsoft Applied Sciences Group
arxiv_id: '2610.42030'
url: https://arxiv.org/abs/2610.42030
pdf_url: https://arxiv.org/pdf/2610.42030
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: LLM推理优化 · 层循环性价比
tags:
- Looped Transformer
- Inference Optimization
- Model Scaling
- FLOP Efficiency
- Small LLM
one_liner: 提出双层测试框架验证预训练后加层循环的收益，证明仅小模型在固定参数预算下值得加循环
practical_value: '- 端侧小模型（如电商端搜、端推荐的端侧小LLM）在固定参数/内存预算时，可尝试加层循环，0.8B量级模型可获得4%左右的推理精度提升，推理开销仅增加25%~29%

  - 4B及以上规模的服务端LLM（如电商文案生成、Agent推理用大模型）无需尝试后加循环，同推理算力下升级更大模型、增加采样次数的收益更高

  - 小模型推理优先加入budget forcing这类零成本解码规则，可提升10%以上的答案完成率，基础收益高于加循环

  - 评估模型优化策略时必须做对等参数量、对等算力双维度对比，避免将额外算力/训练量带来的收益误算为策略本身的价值'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
给预训练完成的模型加层循环无需提升参数量、训练成本、内存占用，看似是低成本提效的优质方案，但循环会增加每token推理开销，当前尚无明确标准判断后加的循环能否覆盖额外推理成本，不同模型规模下的收益差异也不清晰。
### 方法关键点
- 设计双层测试框架：第一层等参数量对比，校验加循环模型与同参数量、同训练流程的无循环基准模型的精度差；第二层等FLOPs对比，校验加循环模型与同推理算力下最优无循环方案（更长推理步数、更大模型等）的精度差，仅两层测试均胜出的循环才有实用价值
- 测试覆盖0.8B/4B/9B的Qwen3、Qwen3.5系列模型，循环推理开销控制在1.25~1.29倍，对比时统一加入零成本的budget forcing解码规则，消除答案未完成带来的精度偏差
### 关键结果
在GSM8K、MATH-500等推理基准上测试：
- 仅0.8B小模型通过双层测试：等参数量下精度提升4.1个百分点，等FLOPs下精度提升2.5~4个百分点
- 4B、9B模型等参数量下精度无显著提升甚至下降，完全无法通过测试
- 无训练的循环在8B模型上无显著收益，同算力下直接升级到14B模型的精度提升远高于加循环
### 核心结论
没有免费的循环，仅当参数/内存预算严格受限无法升级更大模型时，给1B以下小模型加循环才是划算的

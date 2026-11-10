---
title: 'Inference Validation for Regulated AI: Building a Decision Pipeline on NVIDIA
  AIPerf'
title_zh: 监管场景AI推理验证：基于NVIDIA AIPerf的决策流水线构建
authors:
- Dev Akre
- Roman Bobalo
- Manoj Dobbali
affiliations:
- MasterControl, Inc.
arxiv_id: '2611.12737'
url: https://arxiv.org/abs/2611.12737
pdf_url: https://arxiv.org/pdf/2611.12737
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: LLM推理部署 · 可审计验证与选型
tags:
- LLM_Inference
- AIPerf
- TensorRT-LLM
- vLLM
- Inference_Benchmark
- Regulated_AI
one_liner: 提出基于NVIDIA AIPerf的可审计LLM推理验证框架Runway，给出多场景推理配置选型实测结论
practical_value: '- 做LLM推理引擎选型时，不要仅测试低并发性能，需匹配业务实际并发区间测试：TensorRT-LLM默认配置在低并发占优，vLLM默认配置在并发>50时性能更好

  - GPU成本核算不要仅看小时单价，需按单请求成本测算：如g7e实例单价是g6e的1.81倍，但单请求成本反而低1%-15%

  - Speculative decoding（MTP）收益与引擎、并发强相关：vLLM在并发>16时开启MTP反而降性能，TensorRT-LLM全并发区间开启均有收益，配置调优收益可能超过引擎本身选型收益

  - 可复用Runway架构思路：基于开源成熟的AIPerf做推理性能测试，无需自研压测工具，将精力放在上层实验管理、SLA校验、审计存储上，降低合规与研发成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
监管行业部署LLM时，传统仅在合成负载下选最高吞吐量配置的做法无法满足合规要求，监管方要求可追溯、可证明的选型证据；且合成负载与真实生产负载差异大，单指标选型易出错，自研压测工具的正确性需额外举证，研发与合规成本极高。
### 方法关键点
- 设计Runway框架，完全复用NVIDIA AIPerf执行基准测试，不修改上游代码，避免压测工具的正确性举证成本
- 架构分三阶段：实验设计阶段自动扩缩测试维度网格，缓存命中直接复用历史结果；测试阶段全权委托AIPerf执行，保证过程标准可溯源；后置阶段自动做SLA校验、成本建模、生成审计报告
- 存储设计将缓存与审计能力统一，每个测试结果路径明确编码测试参数，指纹校验保证结果可复现，所有配置、SLA版本、结论全链路留痕
### 关键结果
测试基于Qwen3/Qwen3.5系列模型，对比不同引擎、GPU实例、配置的性能：
1. 并发<10时TensorRT-LLM吞吐量高10%-35%，并发>50时vLLM吞吐量高3%-19%，引擎排序随并发反转
2. g7e（Blackwell）实例吞吐量是g6e的1.82-2.13倍，小时单价高1.81倍，单请求成本反而低1%-15%
3. TensorRT-LLM开启MTP全并发区间吞吐量提升32%-157%，vLLM在并发>16时开启MTP反而降低8%-20%性能；仅调整TensorRT-LLM调度策略就带来2.55倍吞吐量提升，配置调优收益超过引擎选型差异

**最值得记住的一句话**：LLM推理配置选型时，单基准点测试的结论没有参考价值，匹配真实业务负载的多维度可追溯测试才能兼顾性能、成本与合规要求。

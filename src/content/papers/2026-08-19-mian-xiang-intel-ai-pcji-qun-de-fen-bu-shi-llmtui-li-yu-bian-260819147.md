---
title: Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets
title_zh: 面向Intel AI PC集群的分布式LLM推理预编译流水线分片方案
authors:
- Tate Berenbaum
- Muthaiah Venkatachalam
affiliations:
- Not Community Labs Inc.
- Intel Corporation
arxiv_id: '2608.19147'
url: https://arxiv.org/abs/2608.19147
pdf_url: https://arxiv.org/pdf/2608.19147
published: '2026-08-19'
collected: '2026-08-20'
category: LLM
direction: LLM分布式推理 · 端侧集群部署
tags:
- Distributed Inference
- Pipeline Parallelism
- Speculative Decoding
- KV Cache
- OpenVINO
one_liner: 提出三项优化实现Intel消费级AI PC集群分布式LLM推理，性能超同硬件单节点基准
practical_value: '- 端侧LLM部署KV缓存优化：用OpenVINO部署端侧/边缘LLM时，投机解码无需物理裁剪被拒token，直接通过attention_mask掩码即可，相比物理裁剪节省约48ms/次，几乎零成本

  - 分布式推理工程优化：多节点流水线并行时，仅返回top-1 logits（8字节）代替全量logits（约500KB），WAN场景下吞吐量提升8倍以上，大幅降低跨节点传输开销

  - 模型编译优化技巧：用OpenVINO导出模型分片时，注入beam_idx Gather算子触发IndirectKVCache融合，可将分片推理性能提升15%，达到与单块模型相当的水平

  - 投机解码调参参考：LAN场景选K=5-7平衡计算成本与接受率，WAN场景选K=10最大化单轮往返验证token数，适配不同网络环境的性能要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Intel AI PC自带集成GPU、NPU与16GB以上统一内存，多数时间处于闲置状态，但单节点显存无法容纳70B等大参数模型，现有分布式推理方案要么依赖OpenVINO不支持的paged attention API，要么分片后性能远低于单块模型，普通网络下多节点延迟过高无法满足交互要求。

### 方法关键点
- 预编译流水线分片：将模型按层拆分为多个INT4 OpenVINO图分片，每个分片注入beam_idx Gather算子触发IndirectKVCache融合，分片推理性能与单块模型差距缩小至4%以内
- 掩码式KV缓存回退：投机解码时无需物理裁剪被拒绝的draft token，直接将对应缓存位置的attention_mask设为0，结果与物理裁剪完全一致，几乎无额外开销
- 流水线微批调度：多用户请求交错进入流水线，每个请求携带独立KV缓存，大幅提升多并发场景下的硬件资源利用率

### 关键结果
- 2节点部署Llama 3.1 8B INT4，服务2个并发用户时吞吐量达43.97 tok/s，是同硬件单节点单用户基准的1.79倍
- 模拟100ms/hop WAN延迟场景下，naive分布式推理性能低于5 tok/s的交互阈值，本方案单流吞吐量仍达5.6 tok/s，保持可用
- 4节点Lunar Lake AI PC集群部署Llama 3.1 70B INT4，单用户可达到交互速度，输出与非投机解码完全一致

最值得记住的一句话：闲置消费级AI PC集群通过针对性的编译、缓存与调度优化，可低成本运行单节点无法承载的大模型，性能甚至超过同硬件单节点基准。

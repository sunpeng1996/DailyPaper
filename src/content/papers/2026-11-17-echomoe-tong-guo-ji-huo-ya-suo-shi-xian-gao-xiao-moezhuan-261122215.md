---
title: 'Communicate the Change: Efficient Expert Parallelism via Activation Compression'
title_zh: EchoMoE：通过激活压缩实现高效MoE专家并行通信
authors:
- Fengyuan Liu
- Jay Gala
- Siva Reddy
- Dzmitry Bahdanau
affiliations:
- Mila - Quebec AI Institute
- McGill University
- Periodic Labs
- Canada CIFAR AI Chair
arxiv_id: '2611.22215'
url: https://arxiv.org/abs/2611.22215
pdf_url: https://arxiv.org/pdf/2611.22215
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: 大模型推理 · MoE 通信优化
tags:
- MoE
- Expert Parallelism
- Activation Compression
- Inference Optimization
- LLM Serving
one_liner: 轻量改造现有预训练MoE，通过跨层参考残差压缩降低专家并行通信开销，提升推理吞吐量
practical_value: '- 自建MoE大模型推理服务（如生成式推荐、Agent调度）时，可直接复用EchoMoE的vLLM集成实现，在可接受精度损失下降低通信瓶颈，提升吞吐量降低部署成本

  - 跨层残差压缩思路可迁移到多机部署的分布式推荐模型场景，利用相邻层激活相似性降低节点间通信开销

  - 少量微调适配（仅需预训练0.01%量级token）的改造思路可复用，无需重新预训练即可优化现有大模型服务性能

  - 压缩参数配置搜索方法可借鉴：先分别测试单路径压缩损失再叠加估算，无需全量遍历配置空间，降低调优成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE架构通过稀疏激活实现参数扩容的同时不显著提升单token计算量，但分布式部署下专家并行（EP）的两次同步通信（激活调度、输出合并）已成为性能瓶颈，现有方案要么需重新预训练模型，要么仅优化单字节传输成本，无法减少总传输元素量；而Transformer残差流增量更新的特性导致相邻层激活高度相似，全量传输存在大量冗余。
### 方法关键点
- 分层分组机制：将所有MoE层按步长s划分为若干组，每组首层作为参考层，广播全量激活到所有节点缓存为参考值z，组内后续层仅传输当前激活与z的残差
- 双路径压缩：调度路径用低维线性压缩器编码残差，通过算子折叠避免显式重建全量激活；合并路径直接压缩专家输出，每个节点仅返回低维压缩结果
- 轻量适配流程：先最小化激活重建误差初始化压缩参数，再用仅为预训练规模1/8500的token端到端微调，无需重新预训练即可适配现有MoE
### 关键实验
在Qwen3-30B-A3B等5个主流开源MoE模型上验证，覆盖18个知识、推理、代码、指令跟随基准，对比普通激活压缩、LSH-MoE等基线：最优配置减少58%跨节点RDMA流量，推理吞吐量提升22.6%，平均任务性能仅下降3.8pp；带宽受限的以太网环境下吞吐量最高提升2.38倍。
### 核心结论
利用Transformer残流的跨层相似性做残差压缩，是用极小精度代价换取MoE分布式通信效率大幅提升的高性价比方案。

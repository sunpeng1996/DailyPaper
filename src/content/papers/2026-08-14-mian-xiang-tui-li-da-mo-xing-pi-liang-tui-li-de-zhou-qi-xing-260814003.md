---
title: 'Batch-wise Adaptive Pruning: Periodic Neuron Activation-Aware Weight Pruning
  for Language Reasoning Model'
title_zh: 面向推理大模型批量推理的周期性神经元激活感知权重剪枝方法
authors:
- Yongmin Kim
- Shota Takashiro
- Yusuke Iwasawa
- Takeshi Kojima
- Yutaka Matsuo
affiliations:
- The University of Tokyo
arxiv_id: '2608.14003'
url: https://arxiv.org/abs/2608.14003
pdf_url: https://arxiv.org/pdf/2608.14003
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: 大语言模型 · 推理剪枝 批量推理优化
tags:
- Pruning
- Batch Inference
- Large Reasoning Model
- Training-free
- Inference Acceleration
one_liner: 提出免训练批量自适应剪枝方法，解决推理大模型批量推理下自适应剪枝性能暴跌问题并实现推理加速
practical_value: '- 若业务中使用开源推理大模型做Agent决策、生成式推荐文案、搜索query改写的批量推理，可直接复用这套剪枝方案，无需微调即可在50%稀疏度下保持推理性能，同时获得1.4x左右的推理速度提升，降低部署成本

  - 做LLM推理优化的团队可借鉴核心设计：将离线阈值选神经元替换为批量top-k选择+周期性更新剪枝掩码+激活记忆缓存，解决批量场景下分布偏移导致的稀疏率漂移、性能崩溃问题，适配高吞吐批量部署需求

  - 可直接与现有量化、KV cache压缩技术叠加使用，例如和FP8量化、R-KV压缩组合几乎无额外精度损失，进一步提升推理效率，适合电商大促等高并发场景下的LLM服务降本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大推理模型（LRM）依靠长链思维（CoT）实现复杂推理能力，但推理算力成本极高，生产环境依赖批量推理保障高吞吐。现有免训练自适应剪枝方法在批量场景下性能暴跌：离线校准的阈值仅适配单样本激活分布，批量聚合后分布偏移导致实际稀疏率漂移，推理任务精度直接崩溃；静态剪枝又无法跟踪长CoT过程中动态变化的激活模式，性能同样大幅下降。
### 方法关键点
- 免训练设计，无需微调，仅依赖推理时实时激活做剪枝决策，仅针对Transformer FFN层做结构化剪枝，无需特殊硬件即可加速
- 用批量聚合后top-k神经元选择替代阈值选择，不受批量激活分布偏移影响，从根源避免稀疏率漂移
- 基于重要神经元周期性重激活的观测，采用每20token更新一次剪枝掩码的策略，而非每token更新，大幅降低剪枝计算开销
- 新增激活记忆模块，跨更新周期累积神经元重要性，保留反复激活的关键神经元，适配长CoT推理场景
### 关键实验
在DeepSeek-R1系列7B/8B推理模型上测试，覆盖GSM8K、MATH500等5个推理基准，对比Wanda、Griffin、TEAL等SOTA免训练剪枝方法：batch size=4、50%目标稀疏度下，比TEAL平均精度高39.7个百分点；50%实际稀疏度下比稠密推理快1.40x，且性能几乎不随batch size升高而下降。
> 最值得记住的一句话：现有自适应剪枝在批量推理下崩溃的核心原因是阈值选择对分布偏移敏感，替换为top-k选择+周期性更新+激活记忆就能以极低 overhead 解决问题，适配高吞吐批量部署场景

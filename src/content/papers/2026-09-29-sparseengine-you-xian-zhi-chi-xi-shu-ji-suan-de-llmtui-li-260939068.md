---
title: 'SparseEngine: Sparse-First Inference Engine'
title_zh: SparseEngine：优先支持稀疏计算的LLM推理引擎
authors:
- Jitai Hao
- Quansheng Gu
- Qiang Huang
- Jun Yu
affiliations:
- 哈尔滨工业大学
- M3AIL
arxiv_id: '2609.39068'
url: https://arxiv.org/abs/2609.39068
pdf_url: https://arxiv.org/pdf/2609.39068
published: '2026-09-29'
collected: '2026-10-09'
category: LLM
direction: LLM稀疏推理 · KV缓存优化
tags:
- KV cache
- Sparse Attention
- LLM Inference
- Agent Serving
- Prefix Caching
one_liner: 提出稀疏优先的LLM推理引擎，兼容15种稀疏KV方法，推理吞吐量、Agent端到端速度均大幅领先现有系统
practical_value: '- 多轮电商导购Agent、生成式推荐场景可直接复用Chain Cache机制，跨轮复用压缩后的KV状态，大幅降低长对话推理延迟与GPU成本

  - 推荐系统LLM RAG召回、长周期用户兴趣建模场景，可复用可控Prefix-Cache Pruning能力，定向清理过期浏览记录等低价值KV，平衡精度与成本

  - 业务已落地的稀疏KV优化方法（如H2O、SnapKV）可通过生命周期钩子快速集成，无需修改模型代码即可获得性能增益，降低适配成本

  - 高并发LLM推荐/广告文案生成场景，可按需选型15种兼容的稀疏方法，相同GPU预算下最高提升10倍推理吞吐量，支撑更高QPS'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多轮LLM Agent的交互历史持续增长，会带来KV cache内存不足、attention计算延迟过高的双重GPU瓶颈，现有稀疏推理引擎仅支持特定KV布局或工作流，无法同时兼容多类稀疏方法与连续batching、前缀缓存等通用服务能力，成为长上下文Agent业务落地的核心性能阻碍。
### 方法关键点
- 定义统一生命周期契约，在prefill、decoding全阶段暴露细粒度钩子，支持不同稀疏方法自定义KV表示、计算逻辑与状态更新规则，无需修改模型代码即可覆盖动态稀疏attention、KV eviction、KV压缩、KV量化4大类共15种稀疏方法
- 设计Chain Cache机制，为KV eviction类方法保留逻辑前缀与压缩后的KV、元数据，跨轮交互时可直接复用历史状态，仅需prefill新增后缀
- 提供可控Prefix-Cache Pruning能力，支持业务指定历史区间、KV保留比例，定向清理低价值历史KV，同时保留逻辑前缀匹配能力
### 关键结果
在LongBenchV1/V2、AIME、SWE-BenchLite等基准上对比vLLM、Vortex、Tangram等基线：开启KV eviction时解码吞吐量较vLLM提升10倍以上，相同并发下解码速度较vLLM快2.5倍以上；多轮Agent基准端到端提速最高达2.24倍，所有稀疏方法的任务精度与原生实现平均差异仅0.17个百分点，几乎无精度损失。
### 核心启示
统一抽象层兼容多类稀疏优化、同时保留通用服务能力，是稀疏推理技术从算法验证走向业务落地的核心路径。

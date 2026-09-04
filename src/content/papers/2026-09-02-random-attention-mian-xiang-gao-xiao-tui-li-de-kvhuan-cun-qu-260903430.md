---
title: 'Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning'
title_zh: Random Attention：面向高效推理的KV缓存驱逐策略重思考
authors:
- Heng Wang
- Jielin Qiu
- Wenting Zhao
- Cheng Qian
- Liangwei Yang
- Jiawei Han
- Heng Ji
- Silvio Savarese
- Shelby Heinecke
- Huan Wang
affiliations:
- Salesforce AI Research
- University of Illinois Urbana-Champaign
arxiv_id: '2609.03430'
url: https://arxiv.org/abs/2609.03430
pdf_url: https://arxiv.org/pdf/2609.03430
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: LLM推理优化 · KV缓存驱逐
tags:
- KV cache
- LLM Inference
- Throughput Optimization
- Attention Mechanism
- Efficient Reasoning
one_liner: 提出无评分的随机KV缓存驱逐策略，精度持平SOTA的同时vLLM吞吐量提升32-43%
practical_value: '- 部署LLM驱动的Agent/生成式推荐/智能导购服务时，可直接复用Random Attention策略，固定保留prompt后对其他KV按head随机驱逐，无需复杂评分逻辑即可大幅提升推理吞吐量，精度损失可忽略

  - 做长链推理类任务（比如用户意图深度挖掘、多轮导购答疑）时，优先保障prompt全量缓存即可大幅降低KV缓存驱逐的精度损失，无需额外开发复杂的KV重要性评分算法

  - 自研KV缓存优化方案时，可将Random Attention作为baseline，所有需要额外做评分的策略必须优于该基线才具备实际落地价值'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型长推理链下KV缓存随生成长度线性增长，成为严重内存瓶颈；现有KV缓存驱逐方法都基于「对缓存token打分保留高分项」的范式，打分逻辑复杂度高，推理 overhead 大，实际部署收益受限。

### 方法关键点
- 核心规则：固定保留全部prompt（系统提示、用户query、聊天模板等prefill内容），永不驱逐
- 其余KV缓存项在每个attention head内独立均匀随机采样保留，无任何打分计算，仅需一次随机数生成和topk操作即可完成驱逐

### 关键实验结果
- 测试4个模型（Qwen3-4B/14B/32B、Phi-4-reasoning）、6类推理任务（数学、科学、代码），~4倍压缩率下精度与当前最强KV驱逐基线TriAttention持平，31/60组对比实验显著优于其他基线
- vLLM部署32k token生成任务时，吞吐量比TriAttention高32-43%，是全注意力的1.6-2.7倍
- 控制实验验证：prompt是缓存中最脆弱的部分，只要保留prompt，推理trace本身存在文本级和跨head级冗余，随机采样足够保留模型所需信息

### 最值得记住的一句话
KV缓存驱逐的精度核心取决于对prompt的保护，而非对其余token的复杂排序打分，无信号的随机驱逐在绝大多数推理场景下已足够好用

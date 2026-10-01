---
title: Retrieval Capacity of Self-Attention Under Competition
title_zh: 竞争场景下自注意力的有效检索容量分析
authors:
- Timur Mudarisov
- Mikhail Burtsev
- Radu State
affiliations:
- University of Luxembourg
- London Institute for Mathematical Sciences
arxiv_id: '2609.37879'
url: https://arxiv.org/abs/2609.37879
pdf_url: https://arxiv.org/pdf/2609.37879
published: '2026-09-28'
collected: '2026-10-01'
category: LLM
direction: LLM自注意力 · 长上下文效率优化
tags:
- Self-Attention
- Long Context
- KV Cache Optimization
- Context Retrieval
- Inference Efficiency
one_liner: 量化自注意力有效保留token阈值，揭示上下文竞争与归一化对检索容量的影响
practical_value: '- 做LLM长上下文推理（比如Agent工具调用、电商用户长会话召回）时，可优先保留Top-N注意力权重/贡献度最高的token，同性能下最多减少80%以上需要处理的token量，降低KV
  cache占用

  - 长上下文场景下关键信息（比如电商用户历史订单、Agent支撑事实）的召回会被无关背景挤压，可通过对关键内容加注意力偏置、调整关键信息在上下文的位置提升召回率

  - 对保留的注意力权重做重归一化，可进一步降低30%以上需要保留的token阈值，不损失性能的前提下提升推理速度，适合大流量生成式推荐/广告文案生成场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有研究缺乏对LLM自注意力实际使用上下文token数量的量化分析，也未明确不同场景下该数量的影响因素，无法为长上下文推理效率优化、KV cache裁剪等工程落地提供可复用的量化依据。

### 方法关键点
- 提出有用token假设，定义**有效注意力集大小N*_τ**：在损失上升不超过容忍阈值τ的前提下，每层每个头每个query需要保留的Top-N token最小数量
- 对比两种token排序策略：仅按注意力权重α排序、按贡献度||αv||₂排序，以随机选择为基准baseline
- 设计两组对照实验：固定预测目标下扩展上下文长度、固定支撑事实下增加背景干扰，同时验证重归一化保留权重的效果

### 关键实验结果
实验覆盖9个主流开源LLM（Qwen2.5、Gemma、Llama2/3、Mistral系列），数据集包括OpenWebText、WikiText-103、BABILong QA1。核心结论：1k-token上下文下，仅保留Top32~Top128 token即可让NLL上升不超过5%，比随机选择性能高2个数量级；上下文长度从256拓展到2048时，N*_τ从8~64增长到32~256，但占上下文的比例从12.5%降到9.4%；背景从0K增长到4K时，支撑事实的Top64召回率最高下降60%，重归一化可降低30%以上的N*_τ需求。

### 核心结论
自注意力的有效检索容量不是固定值，既取决于有用信息的规模，也受无关上下文的竞争和权重聚合方式的影响，裁剪KV cache时不能仅按距离query的远近选择，要结合注意力权重/贡献度排序。

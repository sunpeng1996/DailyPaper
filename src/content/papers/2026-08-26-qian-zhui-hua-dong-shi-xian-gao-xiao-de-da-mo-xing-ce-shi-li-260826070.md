---
title: Prefix Sliding for efficient test-time scaling
title_zh: 前缀滑动：实现高效的大模型测试时算力扩展
authors:
- Niklas Muennighoff
- Zhengyang Wang
- Zeyi Chen
- Weijia Shi
- Binyuan Hui
- John Yang
- Dapeng Jiang
- Mika Senghaas
- Fares Obeid
- Johannes Hagemann
affiliations:
- Stanford University
- University of California at Santa Barbara
- Prime Intellect
- University of Washington
arxiv_id: '2608.26070'
url: https://arxiv.org/abs/2608.26070
pdf_url: https://arxiv.org/pdf/2608.26070
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: 大模型推理优化 · 测试时算力扩展
tags:
- Prefix Sliding
- Test-time Scaling
- Attention Optimization
- Long Context Reasoning
- KV Cache
one_liner: 提出无需训练的前缀滑动注意力机制，推理提速3倍且支持超10万token长推理链
practical_value: '- 电商/推荐场景的Agent长会话推理可直接复用该方案：固定用户Profile、系统指令作为前缀保留，仅滑动最近对话/推理token，KV
  cache内存占用恒定，降低长链推理的 latency 和成本

  - 针对需要长思考链的生成式推荐（如个性化穿搭方案生成、多步导购Agent），无需微调现有LLM即可获得3倍推理提速，同时保持生成效果不降

  - 做LLM GRPO训练长推理样本时，可复用截断反向传播技巧：仅回传4倍滑动窗口大小的token即可获得接近全量回传的效果，大幅降低训练OOM风险

  - 短生成任务（如搜索Query补全、短文案生成）无需使用该方案，窗口未填满时无明显性能收益，避免过度优化'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
测试时算力扩展通过增加推理时长提升大模型效果，是复杂任务的主流优化方案，但全注意力机制需要保留所有推理token的KV cache，单token生成成本随序列长度线性增长，长推理场景成本极高。观察发现推理过程中90%以上中间token的注意力权重极低，仅前缀（系统指令、任务Prompt）和最近数千个token对后续生成有核心价值，现有滑动窗口、摘要、last k等方案要么丢失关键前缀信息，要么存在额外计算开销、超参数繁多。

### 方法关键点
- 推理阶段仅保留固定前缀和大小为W的滑动窗口KV cache，总内存占用恒定为前缀长度+W，单token生成成本不随推理长度增长
- 位置编码采用Continue PE方案，直接复用已有token的位置编码缓存，性能损失可忽略
- 训练阶段支持超10万token的RL rollout，采用截断反向传播：仅回传最后4倍滑动窗口大小的token计算梯度，即可达到接近全量回传的效果，大幅降低OOM风险
- 基于FlashAttention实现双级过滤内核：瓦片内掩码保证计算正确性，瓦片间跳过无效区域，性能接近原生滑动窗口注意力

### 关键结果
- 无训练场景下Qwen3-1.7B对比全注意力，推理提速3倍且效果持平，窗口大小4096时推理速度稳定在5000 token/s，不受序列长度影响
- 同等内存预算下RL训练支持最长10万+token推理链，效果优于内存受限的全注意力方案
- 对比baseline：效果比普通滑动窗口高22%，效率比last k、摘要方案高31%，仅需调整滑动窗口大小1个超参数

长推理场景下绝大多数中间token无后续价值，仅保留前缀和最近窗口即可实现降本提效与效果的最优平衡

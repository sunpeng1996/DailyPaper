---
title: 'Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context'
title_zh: Windowed-MTP：消除百万token上下文下MTP推理的全上下文Draft KV开销
authors:
- Alagappan Valliappan
affiliations:
- NVIDIA
arxiv_id: '2607.21535'
url: https://arxiv.org/abs/2607.21535
pdf_url: https://arxiv.org/pdf/2607.21535
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: LLM长上下文投机解码加速
tags:
- Speculative Decoding
- MTP
- KV Cache
- Long Context
- Inference Acceleration
one_liner: 为内置MTP投机解码的draft注意力加滑动窗口+sink，无训练无损，1M上下文解码成本降28-44%
practical_value: '- 所有用带内置MTP头的大模型做长上下文任务（用户全生命周期行为理解、长商品详情页摘要、多轮对话Agent）的场景，无需微调权重，直接接入该改造即可拿到20%+的解码延迟收益，输出质量完全不变

  - 长上下文生成式推荐场景（如基于用户历史行为生成个性化推荐理由、排序后商品文案生成），可直接复用滑动窗口+注意力sink逻辑接入现有SGLang推理栈，同时回收7-11%的KV内存，提升单卡并发量

  - 做Agent长会话推理的团队，无需额外训练小草稿模型，即可解决长上下文下投机解码反而变慢的问题，避免低接受率任务下投机解码出现负收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前前沿大模型普遍内置MTP（多token预测）投机解码头，默认草稿计算开销可忽略，但在百万token长上下文下，MTP头每步都要读全量KV缓存，开销随上下文线性增长，甚至会超过验证阶段开销，导致投机解码反而比不解码还慢；尤其是目标模型转向混合/线性attention后，验证成本降低，草稿的全attention开销占比进一步被放大，严重制约长上下文推理效率。

### 方法关键点
- 仅对MTP的draft注意力加StreamingLLM风格的滑动窗口+注意力sink，目标验证阶段仍保留全attention，完全无训练、可直接落地，且机制上保证无损：输出由全attention的目标模型决定，窗口仅影响候选token生成，不影响最终接受的token
- 把draft的KV工作集限制为固定大小（实验用4K窗口+64个sink token），1M上下文下减少99%的draft侧KV读取量
- 实现draft KV的环形缓冲区复用，无需保存全量draft KV，可回收7.7-11%的总KV内存

### 关键结果
在SGLang框架、单B200 GPU上测试Qwen GDN-MoE 35B/122B、Mamba2混合120B三类模型，1M上下文下：
- 每解码步成本比原生MTP降28%~44%，收益随上下文长度增长而扩大
- 端到端解码延迟比原生MTP快11%~53%，比无投机解码快1.58~2.55倍
- draft KV回收后单卡可承载的1M上下文并发请求量比原生MTP高15%~25%，Pareto最优性全面优于原生MTP和无投机解码

### 最值得记住的一句话
长上下文下投机解码的草稿侧不需要全量上下文，仅加固定窗口就能无损拿到显著的延迟和内存收益，无需付出任何训练成本

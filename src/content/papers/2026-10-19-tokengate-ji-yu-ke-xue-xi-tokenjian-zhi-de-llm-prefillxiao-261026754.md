---
title: 'TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned
  Token Pruning'
title_zh: TokenGate：基于可学习Token剪枝的LLM Prefill效率优化方案
authors:
- Liana Patel
- Rishabh Ranjan
- Ion Stoica
- Matei Zaharia
- Carlos Guestrin
affiliations:
- Stanford University
- UC Berkeley
arxiv_id: '2610.26754'
url: https://arxiv.org/abs/2610.26754
pdf_url: https://arxiv.org/pdf/2610.26754
published: '2026-10-19'
collected: '2026-10-20'
category: LLM
direction: LLM推理优化 · Prefill效率提升
tags:
- Token Pruning
- Prefill Optimization
- LLM Inference
- TTFT Reduction
- KV Cache
one_liner: 为现有LLM提供可插拔可训练token剪枝组件，无精度损失下大幅降低prefill延迟与内存占用
practical_value: '- 电商RAG客服、长商品文档解析、用户评论分析等长上下文场景可直接集成TokenGate，无精度损失下TTFT最高降11.3倍，峰值内存降3.4倍，提升单卡并发量

  - TokenGate仅需配合LoRA微调即可适配业务场景，训练开销接近标准LoRA，无需重新预训练大模型，落地成本极低

  - Token-gated attention的可学习剪枝思路可迁移到生成式推荐长用户行为序列处理，对历史行为token动态剪枝降生成延迟，同时保留核心行为权重

  - 不可微算子的梯度回传设计（参考MoE门控）可复用在推荐多通路召回动态路由等场景，无需额外辅助loss即可端到端训练'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM应用（如RAG、编码Agent、长文档分析）的prefill阶段是核心性能瓶颈：无训练token剪枝方法加速比有限、易损失精度，架构改造方案需要重新预训练，落地成本极高，亟需适配现有预训练模型、低开销、无精度损失的prefill优化方案。
### 方法关键点
- 可插拔Gate模块：在Transformer中间层插入轻量MLP评分网络，对token重要性打分后保留Top-K，后续层仅处理保留token，大幅减少计算量与KV cache开销
- Token-gated attention：参考MoE门控思路，将token重要性得分融入attention logits重加权，解决top-K剪枝算子不可微问题，支持端到端训练
- 高效训练策略：训练时同时计算全量token与随机剪枝token的损失加权求和，无需额外辅助loss，配合LoRA即可完成微调，一次训练适配不同推理剪枝比例
### 关键实验
在代码补全、多跳QA、多文档摘要、医疗抽取、NIAH共5类任务测试，对比FastKV、SlimInfer等SOTA剪枝方案：无精度损失下TTFT降低1.4~11.3×，峰值prefill内存降低1.5~3.4×；相比最优基线prefill速度最高快6.4×，内存最高省2×；训练开销仅比标准LoRA高30%，多数任务收敛更快总训练时长更低。
### 核心结论
无需重新预训练大模型，仅需轻量微调即可实现长上下文prefill的大幅效率提升，是业务侧落地长上下文LLM应用的高性价比方案

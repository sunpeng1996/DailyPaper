---
title: 'Learning how to Forget: Fine-tuning for Long-Context Sparse Attention'
title_zh: 学会遗忘：面向长上下文稀疏注意力的微调方法
authors:
- Matthias Seeger
- Zeyu Zhang
- Vihang Patil
- Konstantinos Benidis
- Sebastian Schelter
affiliations:
- Amazon Web Services
- University of Amsterdam
- Amazon
- Technical University Berlin
arxiv_id: '2608.19920'
url: https://arxiv.org/abs/2608.19920
pdf_url: https://arxiv.org/pdf/2608.19920
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: LLM长上下文 · KV cache优化
tags:
- KV cache
- Sparse Attention
- Long-Context LLM
- Fine-tuning
- H2O
one_liner: 提出适配任意KV缓存策略的低成本长上下文稀疏注意力微调方法及优化H2O实现与开源库
practical_value: '- 业务中使用长上下文LLM的Agent（如处理全量用户行为序列、长对话导购、长文档解析）可直接复用本方法的稀疏注意力微调逻辑，单A100
  40GB显卡即可完成4B规模模型128k上下文的微调，无需多卡序列并行资源

  - 现有KV缓存策略（如H2O）可直接套用本文的增量编码、嵌套激活检查点、CPU offload组合优化方案，在不损失效果的前提下降低长上下文推理的显存占用与延迟

  - 长上下文LLM部署时优先保证训练与推理的KV缓存策略一致，可避免序列并行训练模型在稀疏推理时输出冗余、准确率下降的问题，短输出类任务准确率最高可提升50%以上'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前长上下文LLM推理依赖稀疏注意力与KV缓存压缩降低显存开销，但主流微调方法采用序列并行的精确注意力训练，模型未适配KV缓存淘汰逻辑，导致稀疏推理时效果下降明显；同时现有稀疏注意力微调方案要么需定制化硬件内核，要么资源需求极高，难以落地。

### 方法关键点
- 兼容任意KV缓存策略：通过重放日志记录前向传播时的缓存淘汰决策，反向传播时直接复用决策无需对不可导的淘汰策略求导，适配H2O、最近留存等所有主流KV缓存策略
- 低显存优化组合：采用嵌套激活检查点、CPU offload、KV缓存增量编码三层优化，将微调显存占用降低至与推理相当，单A100 40GB即可支持4B模型、128k上下文的微调
- 优化H2O实现：基于Triton和FlashInfer SDPA内核实现支持输出注意力权重和的H2O版本，延迟远优于原生H2O实现，接近vLLM等主流推理库的性能
- 开源KeysAndValues库：封装所有优化实现，开箱即用支持长上下文推理与微调

### 关键实验
在Helmet 10个长上下文基准数据集（64k/128k上下文）上对比，基线为采用序列并行训练的Qwen3-4B模型；本文方法微调的模型在6个短输出类任务上准确率远超基线，json kv任务上SubEM指标从基线的0提升至50%，clinc150任务上准确率从基线的68%提升至94%，输出长度与真实目标一致，无基线的冗余输出问题。

### 最值得记住的一句话
长上下文LLM的训练条件必须与推理时的KV缓存策略对齐，才能避免推理效果的大幅下降，且无需高成本多卡资源即可实现该对齐。

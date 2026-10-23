---
title: Task-Preserving Multilingual Instruction Tuning for Open-Ended QA in WMT 2026
  MIST
title_zh: WMT2026 MIST开放域多语言问答的任务保留指令微调方案
authors:
- Aleix Sant
- Jordi Luque
- Carlos Escolano
affiliations:
- Telefónica Innovación Digital
- Universitat Politècnica de Catalunya
arxiv_id: '2610.29926'
url: https://arxiv.org/abs/2610.29926
pdf_url: https://arxiv.org/pdf/2610.29926
published: '2026-10-21'
collected: '2026-10-23'
category: LLM
direction: 多语言LLM指令微调 · LoRA适配
tags:
- Multilingual
- Instruction Tuning
- LoRA
- Open-Domain QA
- Cross-lingual Augmentation
one_liner: 基于LoRA微调Qwen3-8B，结合任务保留多语言数据集，在10种语言开放域QA上相对提升7.8%
practical_value: '- 做跨境电商多语言客服、商品问答、小语种Agent场景时，可复用任务保留的数据集本地化方法，避免直接翻译破坏任务逻辑，大幅提升小语种生成质量

  - 针对特定业务任务做LoRA微调时，可对业务核心小数据集做重复采样提升占比，平衡大规模通用辅助数据和业务场景的对齐度，不用额外标注大量数据

  - 多语言生成场景下可直接复用greedy解码+1.08重复惩罚的参数配置，避免生成时出现语言漂移、混写等问题

  - 小语种专项微调会带来非目标任务/语言的性能下降，业务上若需要覆盖多任务多语言，可补充对应场景的回放数据缓解负迁移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多语言指令微调是提升小语种大模型任务遵循能力的核心路径，但直接翻译英文指令数据集会破坏原任务的约束逻辑，导致监督信号失效；WMT 2026 MIST多语言指令任务要求10B参数以下模型适配24种语言的3类指令任务，现有方案难以平衡目标场景增益与跨任务/语言的性能保留。
### 方法关键点
- 基座选用Qwen3-8B，仅对注意力层Q/K/V/O投影矩阵做LoRA微调，秩设为16，仅训练15.3M参数，基座完全冻结
- 训练数据混合三类：官方MIST清洗后数据集（重复采样4次，占比提升至7%）、EuroAlpaca任务保留本地化多语言数据集、CrossEuroAlpaca跨语言增强数据集，共1.2M有效样本
- 推理采用greedy解码+1.08重复惩罚，规避多语言生成时的语言/脚本漂移问题
### 关键结果
对比原生Qwen3-8B基线，在10种目标语言开放域QA上，Gemma-4 judge评分相对提升7.8%，合格响应占比从49.6%提升至62.6%；Aya评测集27种语言上，ROUGE-L相对提升41.5%，BERTScore-F1相对提升2.9%；但目标语言上下文QA评分下降0.83分，非目标语言全任务性能均出现下滑。
### 核心结论
针对特定语言和任务的小参数LoRA微调只会带来选择性增益，不会全局提升模型能力，非目标场景的性能下降可通过补充对应任务回放数据缓解。

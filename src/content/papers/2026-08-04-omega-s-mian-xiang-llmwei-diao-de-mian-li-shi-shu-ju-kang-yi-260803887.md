---
title: 'Omega-S: A Functional Resilience Index for LLM Fine-Tuning'
title_zh: Omega-S：面向LLM微调的免历史数据抗遗忘正则化指标
authors:
- Alberto Acedo
affiliations:
- Biome Makers Inc.
arxiv_id: '2608.03887'
url: https://arxiv.org/abs/2608.03887
pdf_url: https://arxiv.org/pdf/2608.03887
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: LLM 微调正则化 · 灾难性遗忘缓解
tags:
- LoRA
- Fine-tuning
- Catastrophic Forgetting
- Regularization
- LLM
one_liner: 提出仅依赖当前权重的Omega-S正则器，无需历史数据即可缓解LLM微调的灾难性遗忘
practical_value: '- 做LLM领域/任务迁移微调（如通用大模型调电商客服/商品文案/推荐Prompt生成模型）时，可直接接入Omega-S正则，无需留存上游任务数据即可保留原模型能力，规避数据隐私/存储问题

  - LoRA微调场景下可直接复用其开源工程实现：仅需3行代码接入，每10-50步触发一次，单步overhead低于4%，FSDP分布式训练无额外通信开销

  - 缓解灾难性遗忘可优先从权重度方差控制入手，相比需要历史权重/数据的EWC等方法落地成本更低，10种子测试下比调优后权重衰减高22pp+的能力留存率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM微调新任务时普遍存在灾难性遗忘问题，原有领域能力严重退化，企业需要重复付出算力修复损失；主流抗遗忘方案如EWC依赖历史任务数据、旧权重或Fisher矩阵，生产环境中受隐私合规、存储成本、数据过期等限制难以落地，亟需轻量无依赖的抗遗忘正则方案。

### 方法关键点
- 源自土壤微生物群落的拓扑弹性指标，仅基于当前权重矩阵构造伪邻接图，无需任何历史数据/权重/Fisher矩阵，可直接嵌入现有PyTorch训练循环，仅3行代码即可接入
- 最终采用对数比率形式的正则项，解决原始迹惩罚对权重尺度过度敏感的问题，实际生效机制为对权重节点度方差施加惩罚（设计中的拓扑项因sigmoid压缩处于惰性状态）
- LoRA微调场景下无需额外GPU通信，每10~50步触发一次计算，单步训练开销低于4%

### 关键实验
在Llama-3-8B LoRA顺序微调任务（先学代码、后学散文）上，对比无正则、调优后权重衰减、调优后EWC等baseline：
- 10种子测试下，原代码能力的HumanEval pass@1从0.173提升至0.238，相对提升37.7%，能力留存率从62.9%提升至84.1%
- 10/10种子优于调优后的权重衰减，8/10种子优于调优后的EWC，且完全规避了EWC对历史数据、旧权重的依赖要求

### 最值得记住的一句话
缓解LLM微调灾难性遗忘的高性价比落地路径，无需依赖复杂的历史数据驱动方案，仅通过轻量的权重度方差控制即可实现远超常规正则的效果

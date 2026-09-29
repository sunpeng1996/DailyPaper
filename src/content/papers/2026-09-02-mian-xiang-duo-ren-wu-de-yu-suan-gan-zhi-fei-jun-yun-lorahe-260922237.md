---
title: 'Not All Ranks Are Equal: Budget-Aware LoRA Merging Across Tasks'
title_zh: 面向多任务的预算感知非均匀LoRA合并方法
authors:
- Avinash Amballa
- Yashas Malur Saidutta
- Wenbo Li
- Lazar Valkov
- Srinivas Chappidi
affiliations:
- Samsung Research America
arxiv_id: '2609.22237'
url: https://arxiv.org/abs/2609.22237
pdf_url: https://arxiv.org/pdf/2609.22237
published: '2026-09-02'
collected: '2026-09-29'
category: Training
direction: 多任务LoRA合并 · 非均匀秩分配
tags:
- LoRA
- Model Merging
- Multi-Task Learning
- PEFT
- SVD
one_liner: 提出无数据Net Utility指标，全局优选奇异方向，同预算下显著提升多任务LoRA合并效果
practical_value: '- 电商多业务（搜索/推荐/广告）多LoRA部署场景，可直接用Net Utility做非均匀秩分配，同推理成本下提升多任务性能，消除LoRA热切换开销

  - 端侧电商导购Agent等紧预算部署场景，无需花满全部秩预算，仅保留正Net Utility的奇异方向，即可同时降延迟提效果

  - 现有LoRA合并 pipeline（DARE/TIES/TSV等）可直接叠加该秩分配模块，无需修改原有合并逻辑，即可获得2%~3%的性能提升

  - 多业务任务难度差异大的场景，Net Utility自动给难任务分配更高秩占比，无需人工调优任务权重，降低调参成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多任务LoRA合并方法默认所有层、所有任务分配均匀秩预算，忽略了不同层、不同任务的LoRA更新能量分布极不均匀的问题，是合并后性能与单任务LoRA差距的核心来源；而最优秩分配是NP难问题，且端侧/边缘部署对LoRA秩带来的推理延迟极其敏感，紧预算下的高效秩分配需求迫切。

### 方法关键点
- 提出无数据Net Utility指标：对每个任务LoRA经SVD分解得到的奇异方向，计算其对所属任务的贡献减去对其他任务的干扰，无需任何业务数据、验证集或前向传播。
- 全局秩分配：跨所有层、所有任务的奇异方向统一按Net Utility排序，仅保留得分最高的正得分方向，允许秩预算在层与任务间自由流动，无需预先为每层/任务分配固定秩。
- 全兼容：适配Task Arithmetic、TIES、DARE、TSV等几乎所有主流LoRA合并算子，以及Full、Core、KnOTS等多种合并空间，无需修改原有合并逻辑即可直接叠加。

### 关键结果
在7个CV任务（ViT-B/32 backbone）、6个NLP NLI任务（Qwen3-4B backbone）上测试：同预算下平均比均匀秩分配性能高2.1%（CV）、2.2%（NLP），最大提升可达3.8%（CV R=64 + DARE合并）；紧预算（R=16）下增益更明显，高预算下甚至仅用不到50%的秩预算，就能超过满预算均匀分配的效果3.19%。

### 最值得记住的结论
LoRA合并的性能瓶颈往往不是合并算子本身，而是不合理的均匀秩分配，低奇异值但与其他任务正交的方向，可能比高奇异值但冲突严重的方向价值更高。

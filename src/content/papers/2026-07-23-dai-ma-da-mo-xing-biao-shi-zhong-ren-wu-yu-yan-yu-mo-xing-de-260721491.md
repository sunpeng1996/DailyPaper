---
title: 'What, Where, and How: Disentangling the Roles of Task, Language, and Model
  in Code Model Representations'
title_zh: 代码大模型表示中任务、语言与模型的角色解耦研究
authors:
- Piotr Wilam
affiliations:
- University College London
arxiv_id: '2607.21491'
url: https://arxiv.org/abs/2607.21491
pdf_url: https://arxiv.org/pdf/2607.21491
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: 大语言模型可解释性 · 概念电路分析
tags:
- LLM Interpretability
- Concept Circuit
- Code LLM
- Representation Analysis
- Universality
one_liner: 通过2×2实验设计解耦代码大模型概念电路的三类依赖，明确电路通用性边界
practical_value: '- 下游LLM微调（如电商文案生成、Agent工具调用）时可优先复用任务层面通用概念电路，降低微调成本

  - 多场景LLM部署做KV cache优化时，可针对不同基座的概念计算层位置做定向缓存裁剪，提升推理速度

  - 跨领域LLM迁移时可统计不同领域概念的电路重合度，重合度高的领域可共用LoRA权重，减少存储开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
独立训练的不同代码大模型是否对相同概念有一致表示、概念电路的通用性边界尚不清晰，缺乏量化解耦任务、语言、模型三类因素影响的研究。
### 方法关键点
采用2×2实验设计，覆盖Python/Rust两种编程语言、Qwen2.5-Coder-7B/DeepSeek-Coder-V1-6.7B两个基座，提取115个语法概念对应的概念电路，从「什么概念有专属电路、电路所在层位置、电路层间演化模式」三个维度做对比分析。
### 关键结果数字
任务决定哪些概念有专属电路，跨模型概念一致性Spearman ρ≈0.65；模型决定电路位置与演化模式，Qwen电路集中在L17-19，DeepSeek在L6-7；Rust语法结构的专属电路规模是Python的2-3倍，DeepSeek跨语言神经元共享度是Qwen的1.94倍。

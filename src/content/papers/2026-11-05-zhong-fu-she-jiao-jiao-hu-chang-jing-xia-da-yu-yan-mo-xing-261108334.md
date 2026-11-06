---
title: Cultural Adaptation within Repeated Social Interactions
title_zh: 重复社交交互场景下大语言模型的文化适配机制研究
authors:
- Chen Cecilia Liu
- Roi Reichart
- Anna Korhonen
affiliations:
- University of Cambridge
- Technion - Israel Institute of Technology
arxiv_id: '2611.08334'
url: https://arxiv.org/abs/2611.08334
pdf_url: https://arxiv.org/pdf/2611.08334
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: LLM Agent 交互驱动文化适配
tags:
- LLM Agent
- Cultural Adaptation
- External Memory
- Social Interaction
- Norm Assimilation
one_liner: 通过轻量外部记忆实现LLM在重复社交交互中的隐性文化规范习得与迁移
practical_value: '- 跨境电商出海的导购/客服Agent可直接复用会话级反射记忆（MemoryR）机制，每轮交互后总结场景化当地文化规范存入长时记忆，无需微调即可适配不同区域文化规则，避免冒犯用户

  - 记忆更新粒度优先选择会话级而非逐轮级，可减少局部噪声干扰，长期适配效果更稳定，同时还能降低检索和更新的计算开销

  - 评估Agent的隐性规则习得能力时，可参考论文的沙箱交互评估范式，以任务达成作为隐性激励，无需显式标注规则，评估结果更贴近真实业务场景的适配效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM文化适配多依赖静态知识问答评估，忽略了真实场景中文化规范多为隐性、需通过交互逐步习得的特性，静态Prompt或微调方案无法支持交互场景下的持续文化适配，也难以验证模型的自适应可塑性。

### 方法关键点
- 构建覆盖中国、法国、日本、新西兰、沙特5种文化的1264个社交交互沙箱场景，以任务达成为隐性激励，要求Agent在无显式规则告知的前提下习得场景文化规范
- 对比三类机制：无记忆的情境推理（SR）、逐轮更新的BDI记忆（MemoryBDI）、会话级更新的反射记忆（MemoryR），均采用外部非参数记忆，无需微调模型权重
- 采用LLM Judge输出的社会声誉分（-1违规/0中性/1合规）作为核心指标，同时验证跨场景泛化、多语言适配能力

### 关键结果
- 对比无记忆基线，MemoryR在所有评测模型上均取得统计显著提升，在Gemma4-E4B上平均声誉分提升+0.21，跨5种文化平均得分达0.34
- MemoryR支持跨场景泛化，Gemma4-E4B在未见过的场景上声誉分比基线高0.12，多语言场景下平均提升+0.21
- 会话级记忆的长期适配效果远优于逐轮更新的BDI记忆，后者仅在小部分模型上有效

### 核心结论
交互驱动的文化适配核心是合理的记忆更新粒度，会话级的规则总结比逐轮动态调整更能稳定实现隐性规范的长期习得与泛化

---
title: 'Faithfulness to Refusal: A Causal Audit of Neuron Selectors'
title_zh: 《从忠实性到拒答：针对神经元选择器的因果审计》
authors:
- Ananth Eswar
- Pratinav Seth
- Utsav Avaiya
- Vinay Kumar Sankarapu
affiliations:
- Lexsi Labs
arxiv_id: '2607.05355'
url: https://arxiv.org/abs/2607.05355
pdf_url: https://arxiv.org/pdf/2607.05355
published: '2026-07-06'
collected: '2026-07-07'
category: LLM
direction: LLM安全 · 神经元归因与编辑
tags:
- Neuron Attribution
- LLM Safety
- Causal Audit
- Model Pruning
- Mechanistic Interpretability
one_liner: 通过单步神经元行置零双审计框架验证归因选元因果有效性，可实现低副作用LLM安全拒答注入
practical_value: '- 做业务LLM轻量化剪枝时，可引入本文的单步神经元置零因果审计替代秩稳定性等代理指标，避免剪枝后推理效果异常下降

  - 垂直域LLM新增安全拒答能力时，可复用有害/良性对比归因+神经元置零方案，成本低于全量SFT，且可降低正常query的过度拒答率

  - 开展LLM行为编辑/可解释性工作时，无需强求定位唯一的行为相关神经元通路，找到可生效的冗余子集即可满足业务需求'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前神经元归因分数广泛应用于LLM剪枝、可解释性分析、安全编辑等场景，但业界极少直接验证其筛选的神经元是否具备因果重要性，常用的秩稳定性等代理指标会遗漏大量选择器失效问题。
### 方法关键点
1. 设计两套基于one-shot神经元行置零的配对因果审计流程，分别在语言建模层面、行为层面验证归因选择器的有效性；
2. 行为测试引入有害/良性对比信号驱动归因，精准定位与拒答行为强相关的神经元集合。
### 关键结果
- 归因方法识别可裁剪神经元的效果显著优于激活、幅值类基线，覆盖5款不同架构LLM；
- 基于归因选择的神经元置零可实现仇恨、犯罪类query拒答能力注入，同时保持良性query低过度拒答率与语言流畅度，同层随机置零对照组无该效果；
- 高秩稳定性的选择器因果有效性可能极低，拒答行为对应的神经元子空间高度冗余，不同归因方法找到的有效神经元集合重合度极低。

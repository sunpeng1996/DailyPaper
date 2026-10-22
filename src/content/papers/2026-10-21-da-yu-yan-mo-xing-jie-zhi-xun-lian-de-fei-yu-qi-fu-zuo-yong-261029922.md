---
title: Unintended Side Effects of Value Training in LLMs
title_zh: 大语言模型价值训练的非预期副作用研究
authors:
- Siddhesh Pawar
- Chen Cecilia Liu
- Anna Korhonen
- Isabelle Augenstein
affiliations:
- University of Copenhagen
- University of Cambridge
arxiv_id: '2610.29922'
url: https://arxiv.org/abs/2610.29922
pdf_url: https://arxiv.org/pdf/2610.29922
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: LLM对齐 · 价值训练副作用分析
tags:
- Value Alignment
- Fine-tuning
- LLM Safety
- Side Effect
- Behavior Evaluation
one_liner: 揭示针对特定价值观的LLM微调会引发未训练维度的行为偏移与安全风险
practical_value: '- 电商/客服Agent做价值观/人设微调时，不能仅验证目标人设对齐效果，需额外补充情绪应用、用户视角推理（如Theory of
  Mind）、安全合规三类跨维度评测，避免未预期的能力退化

  - 面向跨境用户的文化价值观适配微调，优先放在预训练阶段或通用安全对齐之前执行，避免后置微调抵消安全对齐效果或引发非预期偏移

  - 小参数量LLM做领域微调时，若涉及价值/人设类目标，建议采用更小的LoRA秩，降低通用行为层面的偏移风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM大量应用于电商咨询、用户陪伴等高价值敏感场景，行业普遍通过微调注入特定价值观（如文化适配、人设设定），但现有评测仅验证目标维度的对齐效果，忽略价值观在模型内部的关联性，无法识别微调对未训练能力、安全属性的非预期影响，极易引发业务风险。
### 方法关键点
- 基于霍夫斯泰德6个文化价值维度（含12个对立方向），用Llama-3.3-70B-Instruct生成共12万条场景-响应对训练数据，每个价值方向各1万条
- 采用QLoRA对4款主流开源指令微调LLM（Llama-3.1-8B、Qwen3-8B、Gemma-3-12B、Ministral-3-8B）分别做12个方向的价值适配，得到48个微调模型
- 评测体系覆盖三类维度：目标价值对齐效果、跨维度价值偏移、安全属性与社会认知能力变化
### 关键结果
价值微调实现目标维度对齐（偏好提升0.4~0.92 nats）的同时，75%的未训练价值维度出现显著偏移，偏移相关性与现实世界价值观关联度达0.76；62.4%~79.3%的行为特质发生显著变化，其中masculine、short-term两类方向的安全错位率最高，从基线1.3%升至6.4%；社会认知层面，情绪理解准确率仅下降2.1pp，但情绪应用准确率平均下降13.1pp，错误信念下的Theory of Mind推理准确率平均下降9.9pp。
最值得记住的结论：针对单一价值观的后置微调会通过模型内部共享机制引发多维度行为偏移，价值适配必须配套全域行为评测，而非仅验证目标维度。

---
title: 'Fine-Tuning LLMs for Translation: General Forgetting Mitigation Does Not Preserve
  MT-Specific Instruction Following'
title_zh: 面向翻译任务的LLM微调：通用遗忘缓解无法保留MT专属指令遵循能力
authors:
- Niklas Scholz
- David Thulke
- Abdallah Nasir
- Will Allred
- Evgeny Matusov
- Hermann Ney
affiliations:
- AppTek GmbH
- RWTH Aachen University
- Applied Science Private University
arxiv_id: '2609.28395'
url: https://arxiv.org/abs/2609.28395
pdf_url: https://arxiv.org/pdf/2609.28395
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: LLM微调 · 灾难性遗忘缓解
tags:
- Catastrophic Forgetting
- SFT
- Machine Translation
- Instruction Following
- LLM Fine-tuning
one_liner: 对比11种遗忘缓解方法，证实通用能力保留指标无法反映MT专属指令遵循能力损失
practical_value: '- 业务场景微调LLM（如电商商品文案生成、推荐理由生成）时，若需保留语气、长度、合规性等专属指令遵循能力，不能仅依赖EWC这类通用遗忘缓解方案，必须在微调数据中混入对应指令的样本，才能避免能力丢失

  - 微调后的效果验证不能仅测通用能力指标，必须针对性评测业务刚需的细分指令遵循效果（如营销话术的风格匹配度、文案的合规性），通用指标达标不代表细分指令能力完好

  - 若暂时无法补充专属指令训练数据，可优先选用SPD方法，它在无辅助数据的前提下对细分指令遵循能力的保留效果显著优于LoRA、Freeze等其他方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
针对翻译任务微调LLM可显著提升低资源语言、垂直领域的翻译质量，但会引发灾难性遗忘，导致原有的通用能力和细分指令遵循能力下降。现有遗忘缓解方法的效果仅通过通用基准评估，无法确认是否能保留MT专属指令遵循能力（如语气控制、语法性别适配、长度约束等），而这类能力是实际落地场景的核心刚需。
### 方法关键点
- 按锚点类型将11种主流遗忘缓解方法分为三类：锚定辅助数据（Data Mixing、Model Merging、EWC等）、锚定模型输出（KL正则、STM、CC、EAFT等）、锚定基础模型参数（Freeze、SPD、LoRA等）
- 两阶段实验：第一阶段用Llama 3.2 1B Instruct在3个语向数据上完成方法筛选，第二阶段用Llama 3.1 8B Instruct在双向西英、阿英数据上验证MT专属指令保留效果
- 评估覆盖三个维度：翻译质量（COMET、BLEU）、通用能力保留（8个通用任务平均得分）、MT专属指令遵循效果（语气、性别、长度控制三类任务）
### 关键实验结果
- 标准SFT微调西英双向数据后，通用能力平均得分较基线下降11.0分，MT专属指令平均得分下降38.8分
- EWC可将通用能力下降幅度控制在1.7分，是通用能力保留效果最优的方法，但其MT专属指令得分接近标准SFT，几乎无保留效果
- 仅混入对应控制任务样本的Data Mixing能保留对应指令能力，可将MT专属指令得分下降幅度控制在4.1分，但效果仅覆盖训练过的任务和提示，无法迁移到同任务的未见提示
- 无辅助数据的方法中SPD表现最优，MT专属指令得分下降幅度比标准SFT少21分
### 核心结论
通用能力保留指标无法代表细分场景专属指令遵循能力的保留情况，业务场景微调必须针对性评测刚需的细分指令效果，同时混入对应训练样本才能避免能力丢失

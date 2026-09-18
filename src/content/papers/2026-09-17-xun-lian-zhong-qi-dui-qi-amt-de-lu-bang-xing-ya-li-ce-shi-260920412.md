---
title: Stress-testing Alignment Midtraining
title_zh: 训练中期对齐（AMT）的鲁棒性压力测试研究
authors:
- Sid Baines
- Jonathan Bostock
- Maria Angelica Martinez
- Andrew Draganov
- David Africa
- Daniel Tan
affiliations:
- Arcadia Impact
- Resolution
arxiv_id: '2609.20412'
url: https://arxiv.org/abs/2609.20412
pdf_url: https://arxiv.org/pdf/2609.20412
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: LLM训练对齐 · 中期对齐鲁棒性评估
tags:
- Alignment Midtraining
- LLM Alignment
- Fine-tuning
- Robustness Test
- Model Training
one_liner: 通过10B到110B参数规模的受控实验，验证训练中期对齐技术对下游微调扰动的高脆弱性
practical_value: '- 做电商导购Agent、推荐系统对齐微调时，不要过度依赖预训练/中期训练注入的业务规则，必须在下游SFT/RL阶段明确覆盖所有核心规则，2%的冲突样本即可覆盖190M
  token的中期训练效果

  - 若通过中期预训练注入业务价值观（如推荐不优先推高佣低质商品），必须配套下游微调的全量规则校验，避免少量标注错误的冲突样本冲掉预设规则

  - 跨任务规则迁移场景下，仅靠预训练注入描述性规则无法实现有效泛化，必须配合至少少量对应规则的演示样本，否则泛化率最高仅53%'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
训练中期对齐（AMT）被业界视为提升LLM对齐泛化性的核心方案，通过在预训练后期注入对齐相关文档，让模型学习底层原则而非仅拟合微调样本。但现有研究极少验证其鲁棒性，真实场景下微调数据难免存在噪声、规则覆盖不全等问题，AMT的实际落地价值尚未得到验证。
### 方法关键点
- 实验覆盖10B-110B参数规模模型，中期训练token量从1M到1B不等，覆盖多个主流开源模型家族
- 设计两类受控评估场景：Dispatch场景（模型做船舶调度，可选优先遵循公平宪章/最大化利润两类动机）、Python4场景（学习虚构的Python方言规则）
- 训练流程严格控制变量：中期对齐训练→通用指令微调→下游任务微调（EFT），所有实验组除核心变量外配置完全一致
### 关键实验结果
- 无冲突微调时AMT可让模型90%+概率遵循注入动机，但仅需2%的冲突微调样本即可反转偏好，8万冲突token就能覆盖1.9亿中期训练token的效果
- 仅在中期训练注入、未在微调出现的规则，模型泛化率最高仅53%，去掉中期训练中的规则演示样本后泛化率进一步下降30%以上
- 下游微调从SFT换成RL后，AMT效果几乎完全消失，即使模型仍能背诵注入的规则，也不会在实际行为中遵循
### 核心结论
训练中期对齐仅能在理想微调环境下生效，少量下游数据扰动、规则缺失就会使其失效，无法作为对齐问题的通用解决方案

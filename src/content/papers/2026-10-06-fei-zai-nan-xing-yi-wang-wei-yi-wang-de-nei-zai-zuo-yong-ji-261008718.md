---
title: 'When Forgetting is not Catastrophic: On the Mechanics of Spurious Forgetting'
title_zh: 非灾难性遗忘：伪遗忘的内在作用机制研究
authors:
- Vedant Palit
- Florent Draye
- Nicolas Zucchet
- Zhijing Jin
- Bernhard Schölkopf
affiliations:
- MPI for Intelligent Systems, Tübingen
- University of Toronto & Vector Institute
- Stanford University
- ELLIS Institute Tübingen
- EuroSafeAI
arxiv_id: '2610.08718'
url: https://arxiv.org/abs/2610.08718
pdf_url: https://arxiv.org/pdf/2610.08718
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: 大语言模型 · 微调伪遗忘机制
tags:
- Spurious Forgetting
- Fine-tuning
- Continual Learning
- Transformer
- Knowledge Preservation
one_liner: 揭示伪遗忘由可逆共享偏移与不可逆事实侵蚀构成，提出移除权重更新主方向恢复旧知识的方法
practical_value: '- 垂域LLM微调时优先控制新数据答案分布：若新数据答案集中在固定输出区间，旧知识大概率只是被隐藏，可通过延长微调时间自动恢复60%以上旧能力，无需额外回刷旧数据

  - 微调时可裁剪权重更新的top奇异方向：在新事实准确率损失低于7%的前提下，最高可恢复90%以上被遗忘的旧事实召回，适合需保留通用能力的电商客服/导购大模型微调场景

  - 增量更新商品/用户知识时采用低学习率小步长更新：降低旧表征的共享偏移幅度，减少旧知识召回塌陷深度，平衡新旧知识的保留效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大语言模型微调时的灾难性遗忘是工业界落地的核心痛点，但大量实践表明多数性能下降并非知识被擦除，只是暂时无法访问的伪遗忘，当前对伪遗忘的产生条件、可逆边界缺乏量化解释，无法指导业务场景平衡新旧知识保留需求。
### 方法关键点
- 构建三层验证体系：最小关联记忆模型、合成传记数据训练的可控Transformer、真实预训练OLMo 2 1B模型，逐层拆解遗忘机制
- 将旧知识表征变化分解为两类：**共享偏移**（所有旧表征沿同一方向整体移动，可逆）、**个体漂移**（单事实表征独立偏移，不可逆）
- 提出两种可落地干预方案：从输出logit中减去共享偏移、从权重更新中移除top奇异方向，验证旧知识可恢复性
### 关键实验结果
- 可控Transformer实验：减去共享偏移可完全消除旧事实召回塌陷，仅保留低于10%的不可逆侵蚀损失
- OLMo 2 1B实验：移除权重更新top奇异方向，可在新事实准确率损失不超过7%的前提下，恢复90%以上被遗忘的旧事实召回
- 当新事实的主题与答案无关联时，持续微调无需回刷旧数据即可自动恢复60%以上的旧事实召回
### 核心结论
只有让旧表征相互分离的更新才是灾难性的，让所有旧表征整体移动的更新只会导致可恢复的伪遗忘

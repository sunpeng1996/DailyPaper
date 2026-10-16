---
title: 'Towards Continual Learning: Mitigating Forgetting With Subspace Tuning'
title_zh: 面向持续学习：基于子空间调优缓解大模型灾难性遗忘
authors:
- Arnav Chavan
- Kusha Sareen
- Rishabh Tiwari
- Abhranil Chandra
- Johan Obando-Ceron
- Kurt Keutzer
- Scott Niekum
- Inderjit S Dhillon
- Devvrit Khatri
affiliations:
- UC Berkeley
- Mila
- McGill University
- UMass Amherst
- Google
arxiv_id: '2610.22293'
url: https://arxiv.org/abs/2610.22293
pdf_url: https://arxiv.org/pdf/2610.22293
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: LLM持续学习 · 子空间调优
tags:
- Continual Learning
- Catastrophic Forgetting
- Fine-tuning
- Subspace Tuning
- LLM Adaptation
one_liner: 提出子空间调优SST方法，约束LLM微调更新到非主奇异子空间，大幅降低灾难性遗忘
practical_value: '- 垂直领域LLM微调（如电商导购Agent、商品文案生成模型）可直接复用SST方案，冻结99%主奇异子空间，适配垂直数据的同时保留指令遵循、推理等通用能力，避免微调后基础能力崩盘

  - 多阶段持续微调场景（如给Agent依次添加商品查询、售后咨询能力）可搭配SST的refresh机制，按步长更新保护基，实现技能累加无明显遗忘，无需每轮混合全量历史训练数据

  - 多垂直域专家模型合并时，SST训练的专家更新仅落在低能量子空间，可直接做任务向量算术合并，无需额外调参，跨域干扰比普通SFT专家低60%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM通过微调适配新任务时普遍存在灾难性遗忘问题，预训练阶段获得的通用推理、指令遵循、常识等能力会大幅退化；而预训练原始数据通常不可获取，现有缓解方案（如SDFT）仍存在明显遗忘，严重阻碍大模型的持续迭代与多技能积累，对需要频繁更新垂直能力的电商、广告、Agent场景极不友好。
### 方法关键点
- 对权重矩阵的优化器最终更新量做双边投影，仅保留落在非主奇异子空间的更新分量，冻结占比99%的主奇异子空间（承载原有核心能力），完全避免更新泄露到保护区域
- 投影作用于优化器输出的最终更新量而非原始梯度，适配Adam、Muon等所有带状态优化器，无训练流程侵入性，可与SFT、SDFT等任意微调配方组合
- 新增基刷新机制：每K步基于当前权重重新计算奇异子空间保护基，平衡新任务适配能力与旧能力保留效果，K越小适配性越强、遗忘程度略有上升
### 关键实验
在Qwen3 1.7B~32B、4个垂直领域（科学、金融、病理、医学）数据集上测试，对比SFT、SDFT等基线：8B及以上模型用SST微调后，原有通用能力退化小于1pp，新任务精度与无约束SFT持平，遗忘程度比基线降低90%以上；KL漂移比基线低2~4倍，大幅减少幻觉、推理链缩短等非精度维度的能力退化；3阶段持续微调后，SST训练的模型可保留95%以上已学技能，普通SFT则会丢失20~30pp的旧技能。

**最值得记住的结论**：大模型灾难性遗忘不是学习新任务的必然代价，仅需将权重更新约束在低能量奇异子空间，即可在不损失新任务效果的前提下几乎消除遗忘。

---
title: Continual Learning Mechanisms Compose for Long-Horizon Memorization
title_zh: 面向长时记忆的持续学习机制组合优化方法
authors:
- Zheyuan Zhang
- Alvin Zhang
- Daniel Khashabi
- Tianmin Shu
affiliations:
- Johns Hopkins University
arxiv_id: '2609.06986'
url: https://arxiv.org/abs/2609.06986
pdf_url: https://arxiv.org/pdf/2609.06986
published: '2026-09-06'
collected: '2026-09-16'
category: Training
direction: LLM持续训练 · 灾难性遗忘缓解
tags:
- Continual Learning
- LoRA
- Catastrophic Forgetting
- Long-Horizon Memorization
- SFT
one_liner: 组合三类锚定机制与merged LoRA，将长时任务记忆保留率提升28倍
practical_value: '- 做LLM增量SFT（如持续学习新商品知识、用户规则）时，优先用merged LoRA+生成式replay组合，两者有超加性增益，效果远高于单种机制

  - 若需要参数不随任务数增长的持续更新方案，可直接复用「三类锚+merged LoRA」组合，无需存储历史训练数据，内存开销固定

  - 可直接复用task-level successive halving策略快速筛选多机制组合的最优超参，无需跑完所有长时任务即可得到可靠配置

  - 搭建长时交互Agent时，可采用这套机制缓解多次SFT后的知识遗忘，比纯LoRA微调的记忆保留率高20个百分点以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM通过持续SFT增量学习新知识时会发生严重的灾难性遗忘，现有单种持续学习机制在100个以上长序列任务场景下记忆保留率极低，且无法满足「不存储历史训练数据、推理时不需要任务ID」的落地要求，需要组合互补的遗忘缓解机制解决长时记忆问题。

### 方法关键点
- 从「保留什么」「在哪更新」两个维度设计组合框架：三类锚定机制分别从不同层面约束更新：数据锚用上一版本模型生成伪样本做回放，函数锚通过自蒸馏约束当前任务输出和旧模型一致，权重锚通过重要性正则惩罚对旧任务重要的参数修改；两类LoRA分配规则：shared LoRA跨任务复用同一个适配器，merged LoRA每完成一个任务就把适配器合并进主权重，再重新初始化新适配器
- 提出task-level successive halving搜索策略，随任务数增加逐步淘汰表现差的组合，大幅降低多机制组合的超参搜索成本

### 关键实验
在Symbol-QA、LLM-QA、Real-QA三个100任务QA数据集上测试，对比naive SFT、单种持续学习机制等基线：naive SFT最终记忆保留率仅1.2%，最优单机制仅8.1%，组合三类锚+merged LoRA的方法达到34.9%，提升28倍，记忆半衰期从1-2个任务提升到19-44个任务。

**最值得记住的结论**：生成式replay（数据锚）和merged LoRA是所有强持续学习组合的核心，两者的增益是超加性的，远高于各自单独增益的总和。

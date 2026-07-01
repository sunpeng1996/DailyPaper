---
title: 'Introspective Coupling: Self-Explanation Training Tracks Behavioral Change
  Despite Fixed Supervision'
title_zh: 自省耦合：固定监督下自解释训练可追踪模型行为变化
authors:
- Zifan Carl Guo
- Laura Ruis
- Jacob Andreas
- Belinda Z. Li
affiliations:
- MIT EECS
arxiv_id: '2606.32038'
url: https://arxiv.org/abs/2606.32038
pdf_url: https://arxiv.org/pdf/2606.32038
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: LLM自解释训练 · 自省耦合机制
tags:
- Self-Explanation
- Fine-Tuning
- Behavioral Regularization
- Introspection
- LLM Interpretability
one_liner: 发现带行为正则的固定监督自解释训练可让解释自动匹配模型当前行为
practical_value: '- 做LLM驱动的推荐理由生成、Agent决策可解释性时，只需在自解释训练中加入行为正则，无需频繁更新解释标注，模型会自动适配业务微调后的行为，大幅降低标注成本

  - 同领域模型可复用自解释标注：只要模型间行为相似度≥70%，即可直接复用其他模型的解释标注作为训练目标，减少重复标注工作量

  - 可用于推荐/广告模型的漂移监控：在常规后训练流程中同时加入轻量自解释训练，无需额外监督就能让模型自动报告行为变化，低成本检测微调、策略迭代带来的意外行为漂移

  - 面向用户的推荐解释场景下，该范式能保证生成的解释与真实排序逻辑对齐，避免解释和实际推荐结果不一致的体验问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有自解释训练普遍采用初始模型生成的静态标注，但训练过程中模型行为会发生漂移，导致生成的解释匹配旧行为而非当前实际行为，若要保证解释可信度需要频繁重标，成本极高，且无法适配后训练阶段的行为变化。

### 方法关键点
- 从基础模型M0生成反事实行为对（保留/删除输入中特定cue的输出差异），构造对应的反事实解释标注E(M0)
- 训练目标为双损失：解释生成的交叉熵损失 + 行为正则项（当前模型与M0行为分布的KL散度）
- 定义「自省耦合」：模型解释匹配自身当前行为的准确率（Self）高于匹配初始M0行为的准确率（Orig），即Self > Orig

### 关键结果
- 实验覆盖Hint-MMLU、AITA（奉承行为检测）、Refusal（拒绝行为检测）三个任务，主模型采用Qwen3-8B：加正则的模型跨三个任务Self准确率分别比Orig高11.1%、7.0%、9.5%，无正则时该效应消失甚至反转
- 跨模型复用标注可行：即使100%采用Llama的解释标注训练Qwen，仍出现Self > Orig，仅整体解释准确率下降19%
- 自解释可泛化到新增行为：对仅做行为微调的无先验新任务Jabberwocky，自解释准确率仍达79.8%

### 最值得记住的一句话
只要训练过程中解释标注与当前模型行为的相似度≥70%，固定静态解释标注即可让模型生成匹配当前自身行为的可信解释，无需动态更新标注。

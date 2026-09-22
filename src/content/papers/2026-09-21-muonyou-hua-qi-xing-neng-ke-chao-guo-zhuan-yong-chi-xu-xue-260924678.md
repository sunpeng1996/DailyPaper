---
title: Muon Can Outperform Dedicated Continual Learning Methods
title_zh: Muon优化器性能可超过专用持续学习方法
authors:
- Sebastian George Sincari
- Bogdan Alexandru Gheorghe
- Antonio Barbalau
affiliations:
- University of Bucharest
- Bitdefender
arxiv_id: '2609.24678'
url: https://arxiv.org/abs/2609.24678
pdf_url: https://arxiv.org/pdf/2609.24678
published: '2026-09-21'
collected: '2026-09-22'
category: Training
direction: 持续学习 · LoRA训练优化
tags:
- LoRA
- Continual Learning
- Muon Optimizer
- Incremental Fine-tuning
- Catastrophic Forgetting
one_liner: 用正交化更新的Muon训练增量LoRA，性能追平甚至超过专用持续学习方法
practical_value: '- 电商/推荐多场景增量微调LoRA时，可直接将AdamW替换为Muon优化器，无需额外改造持续学习损失，就能降低灾难性遗忘，减少多场景适配的精度损失

  - 现有业务已加任务感知遗忘惩罚损失的，可评估去掉冗余约束，避免双重约束导致的约8.4%精度下降，同时提升模型对新任务的适配可塑性

  - 迭代LLM4Rec/Agent能力做持续更新时，无需堆叠复杂专用持续学习模块，仅优化更新几何分布即可获得相当效果，大幅降低架构复杂度'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于LoRA的持续学习方案普遍通过任务感知损失惩罚新更新与历史权重的重叠，仅限制更新方向却不控制更新能量分布，额外引入的任务依赖机制复杂度高。
### 方法关键点
直接使用自带更新正交化能力的Muon优化器训练极简增量LoRA（IncLoRA），无需额外添加持续学习专属约束，通过优化更新的几何分布缓解灾难性遗忘。
### 关键结果
- 在Standard CL基准上，IncLoRA+Muon精度追平O-LoRA、ELLA等专用持续学习方法；在TRACE基准上效果优于所有AdamW配置的方案
- 同时施加损失层+优化器层双重约束会导致精度下降8.4个点，损失新任务适配可塑性
- Muon的更新分散到7.0个有效奇异方向，远高于AdamW的1.4~1.8个，二者更新方向无重叠

---
title: 'Ask to Distill: Learning to Synthesize Data for On-Policy Distillation'
title_zh: Ask to Distill：面向同策略蒸馏的合成数据生成方法
authors:
- Jiashuo Sun
- Hao Zhang
- Xueqiang Xu
- Heng Wang
- Yixuan Xie
- Pengcheng Jiang
- Zhenrui Yue
- Jiajun Fan
- Peiran Li
- Ge Liu
affiliations:
- University of Illinois Urbana-Champaign
- Hong Kong University of Science and Technology
- Texas A&M University
arxiv_id: '2610.27450'
url: https://arxiv.org/abs/2610.27450
pdf_url: https://arxiv.org/pdf/2610.27450
published: '2026-10-19'
collected: '2026-10-22'
category: Training
direction: 大模型同策略蒸馏 · 合成数据生成
tags:
- On-policy Distillation
- Synthetic Data
- Knowledge Distillation
- GRPO
- RL
one_liner: 提出无需标注的合成问题生成框架A2D，大幅提升同策略蒸馏的知识迁移效率
practical_value: '- 业务场景做小模型蒸馏时，可复用A2D思路，无需人工标注训练数据，基于当前师生模型的分布差异自动生成适配的训练query，比如电商客服Agent、生成式推荐小模型的蒸馏场景可直接复用该流程降低标注成本

  - 奖励设计可直接迁移：将模型间分布分歧+目标模型输出在待优化模型候选集内的覆盖率作为核心价值信号，叠加长度、多样性正则的范式，可用于生成式推荐prompt优化、召回蒸馏的样本价值打分等场景

  - 跨域蒸馏结论可复用：同策略蒸馏的知识迁移不局限于问题所属域，可低成本用现有域的合成数据提升跨域模型效果，比如用搜索域合成数据优化推荐场景模型的推理能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
同策略蒸馏（OPD）可高效将大模型能力迁移到小模型，但传统方案依赖外部标注问题库，问题的蒸馏价值高度绑定特定师生模型对，现有方法无法在无标准答案的前提下评估合成问题的价值，难以生成适配特定师生对的高质量训练数据。

### 方法关键点
- 提出A2D框架，用学生模型初始化问题生成器，基于GRPO做RL训练，训练全程师生模型冻结，无需标注答案、任务特定正确性奖励
- 三重奖励设计：token级价值结合师生KL分歧（待教内容量）与老师输出落在学生top-K候选的概率（可吸收内容量），叠加长度正则避免长响应刷奖励、多样性正则避免重复问题
- 生成问题经格式过滤、语义去重后组成纯prompt库，直接适配标准OPD流程

### 关键实验
覆盖数学推理、代码生成、Agent三类任务，对比Vanilla OPD、KL过滤OPD、Evol-Instruct等基线：数学推理任务上最高实现99.9%的师生性能gap恢复，比基线最高提升22.3个百分点；代码生成任务平均性能比基线最高提升14.7个百分点；Agent任务gap恢复率达95.2%，比基线提升16个百分点；合成问题触发的学生响应长度比真实问题短20%，总学习信号高28%。

### 核心结论
同策略蒸馏中，问题的价值不在于自身表面难度，而在于它能在特定师生对之间激发出多少可被学生吸收的分布差异信号。

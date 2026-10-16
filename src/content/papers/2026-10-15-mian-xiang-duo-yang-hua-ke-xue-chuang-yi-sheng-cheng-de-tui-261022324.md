---
title: Training Reasoning Models to Generate Diverse Scientific Ideas
title_zh: 面向多样化科学创意生成的推理模型训练方法
authors:
- Manya Wadhwa
- Pranav Narayanan Venkit
- Hiroaki Hayashi
- Yu Li
- Tuhin Chakrabarty
- Chien-Sheng Wu
affiliations:
- New York University
- Stony Brook University
- Salesforce AI Research
arxiv_id: '2610.22324'
url: https://arxiv.org/abs/2610.22324
pdf_url: https://arxiv.org/pdf/2610.22324
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: LLM训练 · 多样化生成优化
tags:
- RL
- GRPO
- Diversity
- Creative Generation
- LLM Training
one_liner: 提出集合级RL训练目标，8B模型创意生成效果超过Claude Opus 4.8与GPT-6 Astra
practical_value: '- 集合级RL奖励可直接迁移到电商多候选生成场景：比如多套推荐理由、多组搜索Query、多版本营销文案生成，单条奖励乘以与前序候选的语义距离，避免重复，同时不损失内容质量

  - 两阶段训练范式可复用：先SFT对齐业务输出规范（比如文案长度、合规要求、商品匹配规则），再用自定义集合级奖励做GRPO tuning，比直接RL收敛更快，还能避免生成内容偏离业务约束

  - 一次性生成K个候选优于独立重复采样：让模型在同一次推理中逐个生成、主动回避重复，比采样K次的多样性更高，还能节省KV cache开销，适合搜索suggestion、实时文案生成等低延迟场景

  - 若业务对内容溯源/对齐要求高，可加思维链模块：虽会小幅降低最终指标，但能大幅提升生成内容与输入上下文的匹配度，比如种草文案与商品属性、推荐理由与用户历史行为的对齐'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM创意生成仅优化单条输出质量，多样性依赖随机采样，易出现模式坍塌，无法满足多候选决策场景需求，算力效率与候选集效果都存在明显短板。
### 方法关键点
- 集合级RL训练目标：单条输出奖励=自身质量 × 与之前所有输出的最小语义距离，冗余内容即使质量高也无法获得高奖励，从训练侧强制模型生成多样化候选
- 两阶段训练流程：先SFT对齐任务输出格式与思维规范，再用GRPO基于集合级奖励优化，支持带/不带思维链两种模式
- 开放场景适配的评估算子：质量为与领域金标准创意的 pairwise 对比得分，距离为问题、主张、方法多维度语义距离平均值，无需标准答案即可计算奖励
### 关键实验
在自构建无数据泄露的1740条科研创意测试集、GiantsBench、IdeaSeed基准上对比Claude Opus 4.8、GPT-6 Astra、DARLING等基线：8B无思维链版本的Creative Utility达0.64，较Claude Opus 4.8提升68%，较DARLING提升23%；人工评估候选集质量与Claude相当，多样性提升4%，编码Agent执行成功率与Claude持平，无质量损失。
### 核心结论
面向多候选生成任务，集合级联合奖励训练比独立优化单条输出的综合收益更高，可在不损失质量的前提下大幅提升多样性。

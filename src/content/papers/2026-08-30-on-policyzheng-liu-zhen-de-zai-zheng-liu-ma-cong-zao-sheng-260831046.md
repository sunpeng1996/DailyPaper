---
title: Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement
title_zh: On-Policy蒸馏真的在蒸馏吗？从噪声教师到模型自提升
authors:
- Yi Ding
- Ruqi Zhang
affiliations:
- Purdue University
arxiv_id: '2608.31046'
url: https://arxiv.org/abs/2608.31046
pdf_url: https://arxiv.org/pdf/2608.31046
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: 大模型RL后训练 · 无监督自适配优化
tags:
- On-Policy Distillation
- Reinforcement Learning
- Self-Improvement
- LLM Training
- Mathematical Reasoning
one_liner: 揭示On-Policy蒸馏增益并非来自教师知识迁移，提出无外部监督的熵自适应自提升方法OPSA
practical_value: '- 做LLM驱动的Agent/生成式推荐后训练时，可直接复用OPSA替代OPD：砍掉昂贵的教师模型依赖，仅对最低20% logp的生成token施加熵自适应负优势，零标注/零外部监督即可实现性能提升，大幅降低训练成本

  - 解决生成内容的准确率与多样性平衡问题：借鉴OPSA的分布优化逻辑，低熵生成位置（如商品属性、确定性回答）强化置信度，高熵分叉位置（如文案创意、推理分支）保留探索性，既减少低质量生成，又避免输出多样性坍缩

  - 现有OPD训练链路优化：无需花费大量资源优化教师噪声问题，OPD核心增益来自抑制低概率token而非知识蒸馏，直接替换为自适应负优势方案即可简化链路，同时获得比原OPD更好的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-Policy Distillation（OPD）原本被用于解决RLVR奖励稀疏的问题，通过教师模型提供token级密集监督，但教师需要给学生生成的off-policy轨迹打分，存在大量噪声，且学生性能对噪声极不敏感，OPD的真实增益来源长期不清晰，亟需拆解其核心机制以降低训练对外部监督的依赖。
### 方法关键点
- 定量分析发现OPD教师噪声随规模升高：4B教师噪声率30.6%，235B教师噪声率达50.6%，且学生无论用全量、干净或仅噪声数据训练，最终性能无显著差异
- 拆解增益核心：OPD有效学习完全集中在学生生成的最低20% logp token上，仅用固定负优势即可达到与原OPD相当的性能，证明增益本质是抑制低概率尾token，无需教师参与
- 提出无监督训练方法OPSA：仅对最低20% logp的token分配熵自适应负优势，高熵位置施加更强负信号，将尾token概率重分配给头token，低熵位置强化置信度、高熵位置保留探索性
### 关键结果
在Qwen3-1.7B/4B、Qwen3.5-9B上验证，训练仅用DAPO-17k的问题无任何标注，对比GRPO、OPD、OPSD等基线：Qwen3-1.7B在AIME24上Avg@32提升35.41点（相对增益263%），Pass@32翻倍，比OPD高16.77点，在代码、通用QA任务上也有稳定跨域增益。
### 核心结论
On-Policy蒸馏的核心增益并非来自教师知识迁移，而是通过抑制低概率token优化模型自身输出分布，完全可实现零外部监督的自提升

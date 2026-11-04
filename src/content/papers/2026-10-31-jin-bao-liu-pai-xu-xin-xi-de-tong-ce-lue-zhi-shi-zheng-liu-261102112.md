---
title: Order-Only On-Policy Distillation
title_zh: 仅保留排序信息的同策略知识蒸馏O³PD
authors:
- Guangzeng Han
- Yu Wu
- Xiaolei Huang
affiliations:
- University of Memphis
- University of Missouri
arxiv_id: '2611.02112'
url: https://arxiv.org/abs/2611.02112
pdf_url: https://arxiv.org/pdf/2611.02112
published: '2026-10-31'
collected: '2026-11-04'
category: Training
direction: LLM知识蒸馏 · 同策略训练优化
tags:
- Knowledge Distillation
- On-Policy Training
- LLM
- Ranking Loss
- Model Compression
one_liner: 提出仅对齐教师top-K token排序的同策略蒸馏方法，免温度调优且效果优于传统OPD
practical_value: '- 做LLM4Rec、Agent小模型蒸馏时，可放弃传统KL匹配教师概率的方案，改用仅对齐top-K候选排序的损失，省掉温度调优成本，尤其适合师生模型容量差大的场景，比如将大模型推荐/决策能力蒸馏到端侧小模型

  - 排序损失默认选相邻两两对比的Adjacent Logistic即可，不需要全量两两对比，计算量小且能达到和ListMLE相当的效果，top-K取值8左右即可获得最优效果，候选召回、query排序的蒸馏场景可直接复用该超参设置

  - 训练稳定性远优于传统OPD，不会出现训到后期效果退化的问题，不需要频繁筛选最优checkpoint，大幅降低线上蒸馏训练的工程成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统同策略蒸馏（OPD）要求学生匹配教师的token概率分布，但概率值混杂了教师的偏好排序和自身置信度，小容量学生根本无法复现大教师的置信度分布，还导致OPD对教师温度超参极度敏感，甚至训练后期效果退化，温度调优成本极高。

### 方法关键点
- 提出O³PD，仅提取教师在学生生成的前缀下的top-K token排序，不需要教师的具体概率值，训练学生让相邻排序的token满足前置得分更高，损失采用相邻两两逻辑回归损失
- 损失天然对教师温度不敏感，因为温度缩放不改变排序，完全不需要温度调优，训练全程稳定
- 兼容多种排序损失，相邻对比的损失仅需K-1个约束，通过传递性即可保证全排序对齐，计算量远低于全两两对比

### 关键实验
在6组Qwen3师生模型对、3个数学推理基准（HMMT25、AIME24、AIME25）上测试，O³PD在所有配置下平均得分都超过传统OPD，最高提升2.9个百分点，AIME25最高提升5.6个百分点，同时优于SFT、GRPO基线；训练全程性能持续提升，不会出现OPD后期退化的问题。

### 核心结论
同策略知识蒸馏真正需要迁移的是教师对候选的排序偏好，而非具体的概率数值，概率匹配反而会成为小模型学习的不必要约束

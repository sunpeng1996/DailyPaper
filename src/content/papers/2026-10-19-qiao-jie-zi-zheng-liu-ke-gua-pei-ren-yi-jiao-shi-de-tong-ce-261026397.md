---
title: Bridged Self-Distillation for On-Policy Learning
title_zh: 桥接自蒸馏：可适配任意教师的同策略学习统一框架
authors:
- Runsheng Chen
- Yihong Liu
- Raoyuan Zhao
- Michael A. Hedderich
- Hinrich Schütze
- Matthias Grabmair
affiliations:
- Technical University of Munich
- LMU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.26397'
url: https://arxiv.org/abs/2610.26397
pdf_url: https://arxiv.org/pdf/2610.26397
published: '2026-10-19'
collected: '2026-10-23'
category: Training
direction: LLM蒸馏 · 跨场景同策略训练
tags:
- Self-Distillation
- On-Policy Learning
- Knowledge Distillation
- LLM Training
- Reasoning
one_liner: 通过引入自教师桥接外部教师推理轨迹，实现跨共享/跨分词器/闭源API三类场景的统一同策略蒸馏
practical_value: '- 做闭源大模型能力蒸馏到小模型的业务（比如Agent推理、商品文案生成、query改写）时，可复用BSD框架，无需对齐分词器、无需获取闭源模型logits，仅需拿闭源模型的输出文本作为特权上下文即可，大幅降低蒸馏门槛

  - 优化基于GRPO的RLHF类训练流程（比如推荐排序模型、个性化内容生成模型）时，可引入自教师模块，将优质历史样本/大模型生成的优质轨迹作为特权上下文，对错误生成序列的token做加权惩罚，提升训练效率和效果

  - 小模型蒸馏避免直接用SFT模仿大模型输出，防止出现性能崩塌、输出长度漂移问题，BSD仅对失败rollout加权的策略可保留小模型自身的正确推理路径，训练稳定性更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
同策略蒸馏（OPD）是将大模型推理能力迁移到小模型的核心方案，但现有方法依赖教师模型的token概率或分词器对齐，无法同时适配三类常见教师场景：同分词器同家族模型、跨分词器异家族模型、仅提供文本输出的闭源API模型；且直接SFT模仿大模型推理轨迹易因师生能力差距出现性能崩塌、输出漂移问题，亟需统一的蒸馏框架。

### 方法关键点
- 外部教师仅需输出推理轨迹文本，无需提供logits、无需对齐分词器，天然适配所有三类教师场景
- 新增自教师模块：学生模型的冻结副本，输入为问题+外部教师的推理轨迹（特权上下文，仅训练时可用），对学生生成的同一条rollout做token级打分
- 基于自教师和学生对同一token的打分差生成token级指导，仅对验证失败的rollout做惩罚加权：自教师打分更低的token（出错概率高）加大惩罚，反之降低惩罚；成功rollout沿用原GRPO更新逻辑，保留学生自主探索的正确路径

### 关键实验
在3个数学推理基准（AIME2024、AIME2025、HMMT2025）、12组师生对（覆盖三类教师场景，学生参数从0.6B到4B）上测试：BSD在11组师生对中取得最优平均得分，相比base模型最高提升4.7个百分点；相比SFT完全避免了闭源API场景下的性能崩塌（比如0.6B模型SFT后Avg@4从10.8降到2.8，BSD仍保持12.5），训练全程稳定无输出长度漂移。

### 核心结论
用学生自身的副本作为桥接，将外部教师的推理能力转化为学生token空间的指导信号，是跨场景蒸馏的高效路径。

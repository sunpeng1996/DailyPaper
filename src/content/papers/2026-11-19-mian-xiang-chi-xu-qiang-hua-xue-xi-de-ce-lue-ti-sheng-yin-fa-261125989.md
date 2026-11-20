---
title: Policy Improvement-Guided Replay for Continual Reinforcement Learning
title_zh: 面向持续强化学习的策略提升引导回放方法
authors:
- Qin-Wen Luo
- Haoxuan Gao
- Sheng Ren
- Xiang Chen
- Sheng-Jun Huang
affiliations:
- Nanjing University of Aeronautics and Astronautics
arxiv_id: '2611.25989'
url: https://arxiv.org/abs/2611.25989
pdf_url: https://arxiv.org/pdf/2611.25989
published: '2026-11-19'
collected: '2026-11-20'
category: Training
direction: 大模型持续强化学习 · 经验回放优化
tags:
- ContinualRL
- ExperienceReplay
- CatastrophicForgetting
- VLM
- ReinforcementLearning
one_liner: 提出对比似然回放CoLiR，缓解持续强化学习的灾难性遗忘，同时保持新任务学习能力
practical_value: '- 电商/推荐系统持续迭代新任务场景，可复用CoLiR的对比似然评分筛选高价值历史样本回放，无需额外生成样本，仅复用训练阶段缓存的log-likelihood即可计算，计算成本极低；

  - 用RL finetune大模型做Agent、文案生成的场景，无需全量存储历史训练数据，仅保留每任务top-80高评分样本即可实现优秀的遗忘抑制效果，大幅节省存储和训练资源；

  - 持续训练正则策略可借鉴：无需对全量训练样本加KL约束，仅对回放的历史样本加小系数KL正则，既能防止历史性能退化，又不会限制新任务的学习效果。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
持续强化学习（CRL）要求大模型学习新任务的同时保留历史任务性能，现有方法多侧重参数约束、知识蒸馏的稳定性视角，没有直接量化策略更新对历史任务性能的影响，且受限回放内存下的历史样本选择缺乏RL原生的策略提升视角指导，易出现严重的灾难性遗忘。

### 方法关键点
- 基于性能差异引理推导得出：保留历史性能等价于维持当前策略在历史任务分布上的期望优势非负，从理论层面验证了历史prompt回放的必要性；
- 提出对比似然评分Si：结合最终策略对正确响应的似然增益、初始策略对错误响应的似然衰减两个维度，可作为优势的可计算代理指标，无需额外推理成本；
- CoLiR流水线：任务训练结束时，用缓存的训练rollout和log-likelihood计算所有样本的对比得分，选择top-B样本存入回放池；后续新任务训练时，均匀采样回放样本与新任务样本联合优化，仅对回放样本施加KL正则约束。

### 关键实验
在MRCL多模态持续RL基准（覆盖医疗VQA、导航、数学推理等5类任务）上，对比FullSFT、LoRA、GSPO、CPO等9种基线，在2B/4B/8B三档Qwen3-VL模型上均取得最优结果：4B模型的平均最终准确率（MFN）达69.35%，比次优方法CPO高7.76个百分点，平均任务准确率（MTA）高3.91个百分点，同时新任务学习性能与无回放的GSPO相当。

### 最值得记住的一句话
持续RL场景下无需全量保留历史数据，仅保留少量策略提升最显著的历史样本做回放，就能同时实现低遗忘、高新任务性能，且训练额外开销极低。

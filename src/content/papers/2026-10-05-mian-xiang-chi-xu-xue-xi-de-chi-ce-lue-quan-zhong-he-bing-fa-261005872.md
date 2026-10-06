---
title: Off-Policy Merging Beats On-Policy Self-Distillation for Continual Learning
title_zh: 面向持续学习的离策略权重合并方法优于同策略自蒸馏
authors:
- Chen Henry Wu
- Thomas Zhang
- Aditi Raghunathan
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.05872'
url: https://arxiv.org/abs/2610.05872
pdf_url: https://arxiv.org/pdf/2610.05872
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: 大模型持续学习 · 离策略权重合并
tags:
- Continual Learning
- Off-Policy Training
- Model Merging
- Self-Distillation
- LLM Training
one_liner: 提出grafting离策略权重合并范式，在持续学习场景下效果超越同策略自蒸馏且训练提速10倍
practical_value: '- 推荐/Agent模型持续迭代时，可替换原有同策略自蒸馏方案，直接采用grafting流程：用同系列早期预训练ckpt作为donor微调新业务数据（如新品类数据、新场景交互数据），计算权重差后合并到线上模型，既避免灾难性遗忘，又省去同策略采样的高额成本

  - 给模型注入领域新知识（如电商大促规则、新增类目知识、新运营话术规范）时，可增加Fisher敏感权重掩码，仅mask 0.1%-1%的高敏感权重方向，即可同时实现新知识的高准确率注入和旧推荐/推理能力的几乎无损保留

  - 做模型自提升迭代（如用业务场景的正确反馈蒸馏模型）时，用grafting替换现有SFT流程，可在新场景性能提升的同时，避免原有泛化能力下降的问题，训练效率较OPSD提升10倍'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型持续学习领域长期认为同策略训练是避免灾难性遗忘的前提，但同策略自蒸馏（OPSD）存在推理坍塌、采样成本高昂的问题，直接对成品模型做SFT引入离策略新数据又会严重损伤原有能力，无法兼顾新任务性能与旧能力保留。

### 方法关键点
- 核心方案grafting解耦更新的学习载体与应用目标：不直接微调成品线上模型，选择同系列更早的预训练checkpoint（最优选择通常是预训练结束前的早期ckpt）作为donor微调新数据
- 计算donor微调前后的权重差∆，乘以缩放系数λ后合并到成品模型权重上，本质是带约束的模型合并
- 可选优化：通过Fisher信息估计成品模型的高敏感权重方向，mask掉前ρ比例的最敏感更新方向，进一步降低旧能力的损伤

### 关键结果
覆盖三类主流持续学习场景（专家轨迹蒸馏、STaR/Pedagogical RL自提升、新知识注入），对比SFT、不同α配置的OPSD baseline：grafting在所有场景下实现帕累托最优，新任务性能较基线最高提升100%，旧任务性能无下降甚至有提升；训练速度较OPSD提升10倍，完全省去昂贵的同策略采样成本；知识注入场景下仅mask 0.1%的高敏感权重即可实现99.5%的新知识注入准确率，同时旧任务性能保留率接近100%。

### 核心结论
同策略训练不是大模型持续学习的必需条件，合理设计的离策略权重更新方案可以在训练成本、新能力学习、旧能力保留三个维度全面超越同策略自蒸馏。

---
title: Scaling Laws of Ensemble Uncertainty in Language Models
title_zh: 大语言模型集成不确定性的缩放定律
authors:
- Siamak Ravanbakhsh
- David Nitchi
- Khang Ngo
affiliations:
- McGill University
- Mila
arxiv_id: '2611.32801'
url: https://arxiv.org/abs/2611.32801
pdf_url: https://arxiv.org/pdf/2611.32801
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: 大语言模型 · 集成不确定性量化与缩放
tags:
- Large Language Models
- Ensemble Learning
- Uncertainty Quantification
- Scaling Law
- LoRA
- Bayesian Deep Learning
one_liner: 提出三类幂律量化LLM集成不确定性的缩放规律，验证大尺度下集成优于单一大模型的可行性
practical_value: '- 做LLM4Rec/电商Agent风险判断时，10B以上参数量级可优先考虑将总参数拆分为2-3个独立小模型集成，相比单大模型可同时获得更低预测损失和更可靠的不确定性估计，冷启动、长尾品类等OOD场景收益更高

  - 若预算有限无法做完全独立的模型集成，尽量在训练流程早期分支，训练过半后分支会损失63%的集成多样性，LoRA集成的多样性比同分支点全参数集成低2~4倍，不适合作为高可靠不确定性估计的方案

  - 推荐难例、低质query识别场景下，优先选用集成几何分歧度作为排序指标，大模型上其和真实认知不确定性的Spearman相关性高于单模型熵10%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有贝叶斯深度学习不确定性估计方法受限于固定模型族，无法捕获大模型尺度下的完整认知不确定性，且集成方案的效果、成本随模型规模的变化规律无定量指导，工业界难以平衡集成的投入产出比。
### 方法关键点
- 将认知不确定性拆分为**可见部分**（集成分歧可捕获）和**不可见部分**（模型族容量限制导致），采用几何spread作为集成分歧量化指标，避免算术池化依赖真实标签的问题
- 实验覆盖77个公开预训练模型、98个自训练字符级模型，参数量横跨1M到1T量级，验证不同数据域、上下文长度、训练分支点、集成方式下的缩放规律
- 对比独立种子集成、晚分支集成、LoRA集成三类主流低成本集成方案的效果差异
### 关键结果
- 集成分歧随模型参数量呈幂律衰减，指数γ约0.08~0.2，远低于单模型损失的衰减指数0.19~0.31，因此模型越大集成捕获的可见不确定性占比越高，10B参数量级下可见占比可达20%以上
- 总参数固定时，大尺度下多模型集成的预测效果优于单一大模型，OOD场景下交叉点出现更早
- 晚分支集成分歧度随共享训练比例的平方根衰减，训练过半时分支损失63%的独立集成分歧，LoRA集成分歧度比同分支点全参数集成低2~4倍
### 核心结论
LLM规模越大，集成的投入产出比越高，盲目堆单模型参数的效率不如将等量参数拆分做独立集成。

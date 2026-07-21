---
title: Teach it to stop, not just to click
title_zh: 计算机使用Agent的修复可靠性分析与难度梯度研究
authors:
- Barada Sahu
- Shivesh Pandey
affiliations:
- Cabal AI
- Para AI
arxiv_id: '2607.17136'
url: https://arxiv.org/abs/2607.17136
pdf_url: https://arxiv.org/pdf/2607.17136
published: '2026-07-19'
collected: '2026-07-21'
category: Agent
direction: Agent 训练可靠性与修复优化
tags:
- Computer Use Agent
- Reinforcement Learning
- Verifier
- Reproducibility
- On-policy Distillation
- LoRA
one_liner: 量化计算机使用Agent训练的方差来源，给出修复难度梯度与可复现评估协议
practical_value: '- 落地GUI Agent（如电商智能导购、后台自动化Agent）时优先做固定token类动作（如`done()`指令）的LoRA蒸馏注入，成功率可达97%，投入产出比远高于坐标点击、生成式填字段等开放动作

  - Agent RL训练评估必须做多seed+独立数据划分的重复实验，高难度任务下数据分布方差贡献占比最高达48%，单跑结果符号错误率可达33%以上，优先控制训练数据一致性再调训练参数

  - 可复用Verifier作为统一校正基底，同时承担in-context提示、蒸馏Teacher、奖励信号、推理Gate四个角色，无需单独开发多套模块，降低迭代成本

  - 单点修复仅在该动作是任务唯一剩余瓶颈时可提升端到端成功率，多步任务优先做全局瓶颈分析，不要盲目堆单点校正能力'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前计算机使用Agent（CUA）的RL训练结果普遍仅报告单跑指标，方差来源不透明，结果复现性差，不同校正策略的修复效果无统一量化标准，工业界落地踩坑率极高。

### 方法关键点
- 以35B MoE视觉语言CUA为测试基底，搭建5个可重置、带DB级Oracle评估的Web镜像环境，覆盖停止检测、坐标点击、生成式字段填充等多类修复场景
- 设计统一Completion Verifier架构，同时承担4种角色：in-context提示、蒸馏教师、奖励信号、推理安全门
- 提出SA-OPSD训练方法，结合GRPO策略项和优势门控的行为蒸馏项，用LoRA对基座模型做微调
- 设计交叉方差分解实验：3组独立数据采样×8个训练seed的网格测试，拆分评估、训练seed、数据采样、运行非确定性四类方差来源

### 关键结果
- 修复难度梯度明确：固定token类动作修复成功率97±0.06%，近坐标点击71±26%，远坐标点击53±35%，生成式字段填充仅14±4%
- 方差分解结论：评估方差≈0，训练seed方差占比≤10%，数据采样方差占比随任务难度上升至最高48%；高难度任务训练结果呈双峰分布，单跑结果符号错误率达33%
- 端到端效果：修复动作是任务唯一瓶颈时，任务成功率从0/15提升至8/20，否则无显著提升

**最值得记住的一句话**：永远不要信任Agent RL的单跑实验结果，控制数据分布一致性优先于调训练seed，固定token类校正的投入产出比远高于开放动作校正

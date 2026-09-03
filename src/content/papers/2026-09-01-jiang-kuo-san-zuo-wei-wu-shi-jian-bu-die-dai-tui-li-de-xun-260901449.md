---
title: Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning
title_zh: 将扩散作为无时间步迭代推理的训练课程
authors:
- Mariia Drozdova
- Aidan Sirbu
- Pietro Miotti
- Robert Obryk
- Mayalen Etcheverry
- Eyvind Niklasson
- Blake Richards
affiliations:
- Google, Paradigms of Intelligence Team
- University of Geneva
- McGill University
- Mila - Quebec AI Institute
- CIFAR
arxiv_id: '2609.01449'
url: https://arxiv.org/abs/2609.01449
pdf_url: https://arxiv.org/pdf/2609.01449
published: '2026-09-01'
collected: '2026-09-03'
category: Reasoning
direction: 无时间步迭代推理 · 扩散训练课程
tags:
- diffusion
- iterative reasoning
- training curriculum
- anytime solver
- denoising
one_liner: 改造扩散模型得到无时间步迭代推理器，证实扩散核心价值为训练课程而非推理采样
practical_value: '- 推理类Agent做电商规则校验、选品组合优化等复杂任务时，可借鉴「去掉扩散时间步条件+添加持久隐状态」的架构，实现不受训练反向传播窗口限制的任意深度迭代推理

  - 复杂决策类任务训练可复用扩散退火噪声课程训练范式，提升模型迭代推理泛化性，推理阶段无需保留渐进去噪步骤即可实现高性能

  - 推荐组合优化、广告创意筛选等解空间探索类任务，可借鉴单轨迹持续高斯噪声注入方法，替代多并行rollout降低推理算力成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散模型与递归推理器均为迭代架构，但迭代间信息传递机制差异大，现有迭代推理器受训练回滚长度限制，推理深度无法灵活扩展，且依赖并行采样、外部验证器，部署成本高。
### 方法关键点
1. 为扩散去噪器添加持久隐状态，移除时间步条件，得到共享更新算子，可支持任意深度的推理迭代；
2. 训练阶段保留扩散的渐进退火噪声curriculum，推理阶段无需渐进去噪，每步仅对非线索变量注入最大程度高斯噪声即可。
### 关键结果
Sudoku-Extreme求解准确率达99.90%，Maze-Unique求解率达98.93%；推理深度远超训练时反向传播窗口仍能持续提升精度，单轨迹即可完成解空间探索，无需并行rollout或外部验证器

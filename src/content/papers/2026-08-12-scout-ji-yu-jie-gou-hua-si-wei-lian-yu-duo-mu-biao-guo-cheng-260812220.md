---
title: 'SCOUT: Unlocking Enhanced Spatial Reasoning via Structured Chain-of-Thought
  and Multi-Objective Process Reward'
title_zh: SCOUT：基于结构化思维链与多目标过程奖励的空间推理增强方案
authors:
- Zile Zhou
- Huining Yuan
- Weichen Zhang
- Xinlei Chen
- Xiao-ping Zhang
affiliations:
- Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2608.12220'
url: https://arxiv.org/abs/2608.12220
pdf_url: https://arxiv.org/pdf/2608.12220
published: '2026-08-12'
collected: '2026-08-13'
category: Reasoning
direction: 视觉语言模型 · 空间推理优化
tags:
- VLM
- Chain-of-Thought
- Reinforcement Learning
- Spatial Reasoning
- Process Reward
one_liner: 提出融合结构化CoT与多目标过程奖励RL的SCOUT框架，大幅提升VLM空间推理能力，7B版性能超GPT-4o 4.28%
practical_value: '- 电商3D商品展示、AR试穿/试戴等多模态理解任务，可复用结构化CoT建模3D空间感知的思路，提升交互相关推理准确率

  - 多步骤推理Agent任务（如商品导购路径规划、虚拟数字人动作决策），可借鉴多目标过程奖励+定制化优势估计方法，优化中间步骤信用分配

  - 跨模态泛化业务场景（如单商品图推理到商品短视频标签生成、内容匹配），可参考其单图训练泛化到多图/视频的数据集构造和训练范式'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有VLM空间推理能力存在明显瓶颈，RL类优化方法存在中间推理步骤信用分配差的问题，而现有结构化推理方案缺少3D深度感知建模，无法支撑全面的3D场景理解。

### 方法关键点
1. 设计结构化CoT框架，显式建模3D环境感知，保障空间理解与推理的鲁棒性；
2. 提出带多目标过程奖励的RL算法，搭配定制化优势估计方法，实现推理轨迹不同分段的细粒度信用分配；
3. 构造SCOUT-24k结构化空间推理CoT数据集，支撑框架训练。

### 关键结果
SCOUT-3B在通用空间基准、复杂空间推理任务上较基线分别提升16.85%、6.3%；SCOUT-7B性能超GPT-4o 4.28%，仅用单图训练即可泛化到多图、视频场景。

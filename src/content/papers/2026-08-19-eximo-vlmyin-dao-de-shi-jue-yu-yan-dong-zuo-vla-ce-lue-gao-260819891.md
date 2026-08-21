---
title: 'EXIMO: VLM Guided Exploration of VLA Policies'
title_zh: EXIMO：VLM引导的视觉语言动作（VLA）策略高效微调框架
authors:
- Bhavya Sukhija
- Oliver Groth
- Mohit Shridhar
- Tim Hertweck
- Michael Bloesch
- Markus Wulfmeier
- Abbas Abdolmaleki
- Martin Riedmiller
affiliations:
- Google DeepMind
arxiv_id: '2608.19891'
url: https://arxiv.org/abs/2608.19891
pdf_url: https://arxiv.org/pdf/2608.19891
published: '2026-08-19'
collected: '2026-08-21'
category: Agent
direction: 多模态机器人Agent策略微调
tags:
- VLM
- VLA
- Policy Finetuning
- Reinforcement Learning
- Robotics
one_liner: 提出探索-模仿-优化三阶段框架，大幅提升VLA机器人策略微调的样本效率与性能
practical_value: '- 长流程电商导购/用户运营Agent任务可复用「上层大模型拆分长任务为短子任务、再微调下层执行模型」的架构，降低人工标注成本

  - 少样本适配新业务场景时，可借鉴“先基于大模型生成的合成数据做监督微调、再用残差RL做性能对齐”的两阶段微调范式，提升样本效率

  - 多模态交互Agent落地时，可引入独立的VLM规划模块降低执行端大模型的任务复杂度，平衡推理成本与效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有大参数量VLA（视觉语言动作）机器人策略微调存在两大痛点：一是人工遥操作标注数据集成本极高，二是RL方案样本效率极低，尤其长horizon任务表现差，且VLA大模型架构也不直接适配RL训练。
### 方法关键点
提出EXIMO三阶段微调框架：
1. 探索阶段：引入VLM作为独立规划器，将复杂长任务拆分为VLA可执行的短任务，二者协同采集新任务的结构化数据集，无需人工标注；
2. 模仿阶段：用自采集的结构化数据做行为克隆，微调VLA主干；
3. 优化阶段：采用残差off-policy RL进一步优化策略细节，提升最终性能。
### 关键结果
ablation实验验证三阶段缺一不可，相比现有SOTA方法，样本效率与最终任务成功率均实现显著提升

---
title: Internalizing Agent Experience into Diffusion Model Weights via On-Policy Context
  Distillation
title_zh: 基于在线策略上下文蒸馏将智能体经验内化至扩散模型权重
authors:
- Wenxuan Wang
- Zekai Liu
- Weinan Zhang
- Yu Cheng
- Yang Yang
affiliations:
- 哈尔滨工业大学
- 上海人工智能实验室
- 山东大学
- 南洋理工大学
- 上海交通大学
arxiv_id: '2610.07250'
url: https://arxiv.org/abs/2610.07250
pdf_url: https://arxiv.org/pdf/2610.07250
published: '2026-10-04'
collected: '2026-10-08'
category: Agent
direction: Agent 经验蒸馏 · 模型协同进化
tags:
- Agent
- Knowledge Distillation
- Diffusion Model
- On-Policy Learning
- Co-Evolution
one_liner: 提出D-OPCD方法将T2I智能体的Prompt优化经验内化到扩散模型，实现二者协同进化
practical_value: '- 可复用D-OPCD蒸馏范式：将电商推荐/营销文案场景下Agent侧积累的<用户原始Query, 优化后Prompt>配对经验蒸馏到底层生成/推荐模型，推理阶段无需Agent调度即可保留优化效果，大幅降低延迟与调用成本

  - 可借鉴ASE技能沉淀框架：将业务中跑通的Prompt优化、召回排序策略沉淀为可复用技能库，定期评估出稳定有效的技能后蒸馏进模型，避免技能库无限膨胀带来的检索与调度开销

  - 可直接套用Agent-模型协同迭代流程：每轮蒸馏完成后重置Agent中已被内化的饱和技能，让Agent聚焦探索新的优化策略，形成「Agent探索-模型内化-再探索」的正向循环'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Text-to-Image（T2I）场景中，包裹扩散模型的Agent harness可通过记忆、技能迭代、Prompt优化、结果验证等流程大幅提升生成效果，但所有增益完全依赖Agent推理阶段的实时调度，存在两大痛点：一是技能、记忆积累过多后，相关策略的检索难度持续上升；二是每次用户请求都要重复执行推理、验证、多轮生成流程，推理成本极高。亟需将Agent积累的稳定增益内化到底层模型权重中，降低推理侧对Agent的依赖。
### 方法关键点
- 提出**D-OPCD（Diffusion On-Policy Context Distillation）**：以「原始用户Query + Agent优化后Prompt」作为EMA教师模型的输入，仅用原始Query作为学生模型输入，在学生自身的去噪轨迹上做对齐蒸馏，把Agent的Prompt优化能力内化到学生扩散模型权重，推理阶段仅需原始Query即可获得接近Agent调度的效果
- 配套**ASE（Auto Skill Evolver）**框架：自动将Agent的历史执行轨迹沉淀为可复用的Prompt优化技能，批量生成<原始Query, 优化后Prompt>配对数据集供蒸馏使用
- 设计Agent-模型协同进化流程：每轮蒸馏完成后重置Agent中已被内化的饱和技能库，让Agent围绕更新后的模型继续探索新的优化策略，实现二者的迭代增益
### 关键实验
在GenEval、GenEval2、WISE、R2I-Bench四个T2I基准测试：D-OPCD蒸馏后的模型直接生成平均得分从基线的60.52提升至65.09；蒸馏后模型搭配无技能Agent的平均得分达82.33，超过原始带技能Agent的81.83；第二轮技能进化后得分进一步提升至84.16，相比SFT、Diffusion-DPO、D-OPSD等基线方法，平均增益最高领先1.71分。
### 核心结论
Agent侧积累的经验不需要一直依赖推理阶段调度，通过合理的蒸馏方式内化到底层模型权重，可实现成本和效果的双赢，还能开启二者协同进化的正向循环

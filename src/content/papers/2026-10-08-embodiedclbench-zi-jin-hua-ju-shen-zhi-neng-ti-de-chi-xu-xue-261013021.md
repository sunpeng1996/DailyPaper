---
title: 'EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied
  Agents'
title_zh: EmbodiedCLBench：自进化具身智能体的持续学习能力评测基准
authors:
- Jie Huang
- Yanan Chen
- Ruixun Liu
- Kaichen He
- Xinyi He
- Rui Huang
- Zilong Zheng
- Zhenliang Zhang
- Yiwu Zhong
affiliations:
- 北京大学
- 北京通用人工智能研究院（BIGAI）
- 香港大学
arxiv_id: '2610.13021'
url: https://arxiv.org/abs/2610.13021
pdf_url: https://arxiv.org/pdf/2610.13021
published: '2026-10-08'
collected: '2026-10-12'
category: Agent
direction: 具身Agent 持续学习能力评测
tags:
- Embodied Agent
- Continual Learning
- Benchmark
- Compositional Generalization
- Self-Evolving Agent
one_liner: 推出首个面向具身模拟场景的自进化Agent持续学习评测基准，基于组合泛化设计任务并揭示现有Agent性能规律
practical_value: '- 做Agent技能迁移评估时，可直接复用「基础技能学习→复合任务测试」的组合泛化评测范式，无需从零设计评测逻辑

  - Agent做技能沉淀时无需盲目积累大量样本，实验显示1个相关基础任务的经验即可带来大部分性能提升，更多样本无额外增益，可降低经验存储与推理成本

  - 开发多步决策类Agent（如电商购物引导Agent、智能客服）时，可优先优化无效动作过滤能力，这是经验迁移提升成功率的核心来源

  - 做离线Agent评测可复用状态转移图方案，无需运行实时模拟器，支持并行测试，大幅降低评测工程成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有持续学习评测均集中在非具身的数字/符号场景，无法捕捉具身环境的空间复杂度与物理约束；而现有具身智能评测基准未针对持续学习能力设计，无法评估自进化Agent积累经验、迁移技能解决未知复杂任务的能力，存在明显的评测空白。

### 方法关键点
- 核心以组合泛化为评测原则，任务分为三级：原子动作（单物体交互）、基础任务（少量原子动作组成的简单家居操作）、高级任务（2-4类基础任务技能组合成的未见过的复合任务）
- 基于TongSim家居仿真环境构建离线状态转移图，每个节点对应环境状态、第一视角图像、动作候选，支持无模拟器的离线、可复现、并行评测
- 评测流程分为学习阶段（完成基础任务积累经验）和测试阶段（尝试未知高级任务），对比Zero-shot、In-Context Learning（保留完整交互轨迹）、Skill Learning（仅保留技能总结）三种范式

### 关键实验结果
基准包含168个基础任务、100个高级复合任务，覆盖6类家居技能；测试4种Agent框架搭配Qwen3.8-Flash、GPT5.6-Terra两个大模型，核心结果：
1. 零样本下高级任务成功率仅~10%，经过基础任务学习后成功率提升至~30%+
2. 仅1个基础任务的经验即可带来大部分性能增益，更多学习样本不会带来持续提升
3. 经验迁移使Agent的无效动作选择率降低13%~20%，是成功率提升的核心来源

### 核心结论
当前自进化Agent的持续学习能力仍处于初步阶段，少量相关经验即可带来显著性能提升，但暂不支持随经验规模线性增长的可扩展持续学习。

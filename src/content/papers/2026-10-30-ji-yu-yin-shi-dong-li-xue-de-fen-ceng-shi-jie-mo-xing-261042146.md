---
title: Hierarchical World Models with Implicit Dynamics
title_zh: 基于隐式动力学的分层世界模型
authors:
- Gaoyue Zhou
- Yvonne Wu
- Zichen Jeff Cui
- Nicolas Ballas
- Mido Assran
- Lerrel Pinto
- Yann LeCun
affiliations:
- New York University
- Meta-FAIR
- AMI Labs
arxiv_id: '2610.42146'
url: https://arxiv.org/abs/2610.42146
pdf_url: https://arxiv.org/pdf/2610.42146
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: 具身Agent · 分层世界模型长时程规划
tags:
- World Model
- Hierarchical Planning
- Diffusion Model
- Implicit Dynamics
- Embodied Agent
one_liner: 提出分层世界模型ID-WM，解耦可达性与控制，长时程规划性能超SOTA方法38.5%
practical_value: '- 可借鉴分层解耦思路优化长序列推荐/会话Agent规划：上层用生成模型做粗粒度候选召回（类似高维子目标生成），下层做精细排序/动作映射，大幅降低长序列搜索复杂度

  - 扩散模型隐式高斯空间作为搜索空间的思路可复用：在电商多轮推荐中，将高斯噪声映射为可行的用户转化路径候选，避免脱离业务可行性的无效规划

  - 子目标搜索+落地的两阶段框架可直接迁移到导购Agent：上层生成可达的用户转化路径节点，下层生成对应触达动作/话术，降低长链路转化的累积误差'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有世界模型规划存在两个核心痛点：长时程任务下预测误差累积、搜索复杂度随规划 horizon 指数级上升，而传统分层方法依赖预定义技能、任务特定值函数或奖励标签，泛化性差且难以兼顾细粒度控制，无法支撑零样本长时程决策需求。

### 方法关键点
- 提出ID-WM分层架构：完全解耦状态可达性与底层控制，上层为基于DDPM的扩散模型，仅建模Δ步内的可行邻域状态分布，将输入噪声作为隐式高层动作，搜索空间为天然光滑的各向同性高斯空间，从根源避免模式塌陷与拓扑不连续问题
- 下层为Transformer架构的确定性世界模型，作为逆动力学求解器，给定当前状态与子目标，输出可执行的精准动作序列
- 推理采用两阶段MPC规划流程：上层用CEM优化隐式噪声序列生成可达子目标链，下层用CEM搜索对应动作落地子目标，加入噪声正则项避免规划器 exploit 隐空间的不合理区域

### 关键实验
在Wall、PushT、Maze三类导航与操作环境测试，对比GCBC、HIQL、Diffuser、单级世界模型等SOTA方法，整体性能提升38.5%，相比单级WM MPC长时程任务性能提升135%，视觉输入的长时程PushT任务中随机目标成功率达26%，远超第二名HWM的2%。

### 最值得记住的结论
将分层规划的上层搜索锚定在物理可行的局部动力学约束上，而非全局行为模式，是突破长时程任务泛化性与稳定性的核心。

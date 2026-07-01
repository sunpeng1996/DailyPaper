---
title: 'QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents'
title_zh: QVal：长时序LLM Agent密集监督信号的低成本评估框架
authors:
- Sergio Hernández-Gutiérrez
- Matteo Merler
- Ilze Amanda Auzina
- Joschka Strüber
- Ameya Prabhu
- Matthias Bethge
affiliations:
- University of Tübingen
- Fondazione Bruno Kessler
arxiv_id: '2606.32034'
url: https://arxiv.org/abs/2606.32034
pdf_url: https://arxiv.org/pdf/2606.32034
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: 长时序LLM Agent · 密集监督信号评估
tags:
- LLM Agent
- Dense Supervision
- Q-value
- Training-free Evaluation
- Long-horizon Task
one_liner: 提出无需训练的Q-alignment评估范式，低成本对比21种长时序Agent密集监督信号质量
practical_value: '- 做多步交互电商导购Agent、用户旅程推荐Agent的密集奖励信号选型时，优先测试direct prompting或ranking类简单方案，实验证实两类方法的Q-alignment平均领先其他家族20%以上

  - 复用Q-alignment评估思路，在Agent RL训练前先离线评估候选监督信号与金标Q值的排序相关性，筛除无效信号，可降低至少60%的训练试错成本

  - 固定流程的结构化Agent场景（如客服工单处理、标准化商品导购）可尝试code-based监督信号；开放交互场景优先用text模态状态表示，比image模态的信号一致性高20%以上

  - 同方法家族内优先验证简单变体的效果，实验表明复杂变体相比简单baseline的Q-alignment平均提升不足0.05，无显著业务收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长时序LLM Agent执行多步任务（如多轮导购、复杂问题解决）时，仅依赖最终结果的稀疏奖励无法为中间动作优化提供有效指导。现有密集监督信号的评估需嵌入完整RL训练 pipeline，成本高、受优化策略、损失函数等工程变量干扰，不同方法无法公平对比，导致信号选型效率极低。
### 方法关键点
- 定义Q-alignment核心指标：以最优参考策略输出的Q值为金标，计算候选监督信号对state-action对的排序结果与金标的Spearman相关系数，直接衡量信号质量，无需下游训练
- 发布QVAL-v1.0基准：覆盖FrozenLake、ALFWorld、OpenApps、TerminalBench 4个跨模态跨复杂度环境，生成带Q值标注的state-action对数据集，每个状态采样4个候选动作保证排序评估公平性
- 支持7类共21种密集监督方法即插即用评估，统一控制输入上下文、backbone等变量，完全隔离信号本身的质量差异
### 关键结果数字
- 累计完成1.2K+实验，覆盖6个开源LLM/VLM backbone（9B~122B参数）
- ranking与direct prompting类方法平均Q-alignment达0.5~0.6，显著领先其他方法家族；同家族内复杂变体相比简单baseline的Q-alignment平均提升不足0.05，无显著收益
- text模态状态输入的Q-alignment比image模态平均高0.22，开放场景下表现更稳定
### 核心结论
长时序Agent的密集监督信号选型优先尝试简单prompting类baseline，无需为提升下游表现盲目增加信号复杂度，提前做Q-alignment评估可大幅降低训练试错成本

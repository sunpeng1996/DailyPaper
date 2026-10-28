---
title: 'SetGRPO: Calibrating Grader-Induced Policy Optimization'
title_zh: SetGRPO：校准评分器偏差的GRPO强化学习训练方法
authors:
- Jiale Huang
- Zixu Li
- Zhiwei Chen
- Zhiheng Fu
- Jinhe Bi
- Yupeng Hu
affiliations:
- 山东大学
- 新加坡国立大学
- 智能媒体研究中心(iLearn)
arxiv_id: '2610.36807'
url: https://arxiv.org/abs/2610.36807
pdf_url: https://arxiv.org/pdf/2610.36807
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: 大模型对齐 · GRPO训练校准
tags:
- GRPO
- RLHF
- LLM Alignment
- Conformal Prediction
- Training Optimization
one_liner: 通过集值校准、几何引导恢复、风险门控解决GRPO训练中评分偏差导致的更新方向反转问题
practical_value: '- 做LLM驱动的推荐Agent/生成式推荐对齐时，可直接复用SetGRPO模块替换原生GRPO的训练系数计算逻辑，无需修改原有裁剪、KL约束等组件，落地成本低

  - 生成式推荐RL微调阶段若存在多维度业务评分噪声，可借鉴联合奖励集校准方法，建模组内评分归一化带来的系数耦合偏差，减少无效更新

  - 对于合规要求高的电商文案/推荐话术生成场景，可复用选择性风险门控思路，用独立校准集选阈值，将更新方向反转概率控制在预设范围内

  - SetGRPO单步训练耗时仅增加25.6%，换4.7+的宏观指标提升，资源充足的业务场景可直接落地，无需修改推理侧逻辑'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于评分规则的GRPO训练广泛用于LLM开放任务对齐，但评分器的随机偏差会通过组内归一化耦合传播到整组训练系数，结合当前策略的梯度几何还可能导致更新方向反转，最终降低训练效果甚至引入错误行为，现有方法未刻画该偏差传播机制，无法系统性控制更新风险。

### 方法关键点
- 联合奖励集校准（JRSC）：用同一组响应的两次评分残差建模组内系数的耦合偏差，构造椭球形联合系数不确定集，保证有限样本下的覆盖率
- 几何引导安全恢复（GGSR）：将候选系数映射到当前策略的更新空间和奖励空间，找到最大的方向一致的系数恢复比例，平衡训练进度和方向安全
- 选择性风险门控优化（SRGO）：在独立校准集上选择全局阈值，控制接受更新的条件方向反转风险，仅保留符合阈值的组参与更新，完全保留原GRPO的目标结构

### 关键实验
在Qwen3.5、Llama3.2两个系列共5个不同规模基座上测试，覆盖医疗、写作、指令跟随3个领域10个基准，对比GRPO、RuscaRL、RubricHub等基线，Qwen3.5-9B上Macro Avg达63.51，比RubricHub高1.4个百分点，比原生GRPO高4.82个百分点，单步训练耗时仅增加25.6%，方向反转风险控制在5%以内。

### 核心结论
GRPO训练中评分偏差的危害远不止单样本误差，会通过组内归一化和策略梯度耦合放大，仅优化评分质量无法完全规避，必须结合训练过程本身的校准机制。

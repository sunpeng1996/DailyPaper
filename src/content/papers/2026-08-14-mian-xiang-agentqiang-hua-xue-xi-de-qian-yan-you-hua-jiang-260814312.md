---
title: 'Envs-FORGE: Frontier-Optimized Reward-Grounded Environment Synthesis for Agent
  RL'
title_zh: 面向Agent强化学习的前沿优化奖励感知训练环境合成框架Envs-FORGE
authors:
- Xiaojun Wu
- Cehao Yang
- Honghao Liu
- Xueyuan Lin
- Zhichao Shi
- Hao Zhou
- Xuhui Jiang
- Chengjin Xu
- Jia Li
- Jian Guo
affiliations:
- IDEA Research
- The Hong Kong University of Science and Technology (Guangzhou)
- DataArcTech Ltd.
arxiv_id: '2608.14312'
url: https://arxiv.org/abs/2608.14312
pdf_url: https://arxiv.org/pdf/2608.14312
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: Agent 强化学习训练环境自动合成
tags:
- Reinforcement Learning
- Environment Synthesis
- MILP
- Agent Training
- GRPO
one_liner: 根据当前Agent能力动态选择任务演化策略，合成适配学习前沿的可执行RL训练环境
practical_value: '- 电商客服、运营自动化等终端Agent训练时，可复用难度感知的样本生成逻辑：对当前Agent通过率>80%的任务加复杂度、<20%的拆分为桥接任务、50%附近的做同难度多样化，大幅提升RL训练效率

  - 推荐系统RL排序模块的模拟交互环境生成，可借鉴6种动作+MILP选择框架，平衡样本难度分布和技能覆盖，降低RL训练的样本需求量

  - 做Agent指令微调数据集时，可复用该同步改写+黄金验证流程，保证指令、测试用例、预期输出的一致性，避免无效样本污染训练集'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
终端Agent（如SWE-agent、OpenHands）的RL训练需要可执行、难度适配的环境，现有固定生成策略（Few-shot、Self-Instruct、Evol-Instruct）对所有种子任务采用同一改写规则，生成的环境要么过易无训练信号，要么过难无法学习，无法匹配当前Agent的能力前沿，浪费合成和训练资源。
### 方法关键点
- 先对每个种子任务执行当前Agent rollout，预估任务通过率，定义6种候选合成动作：3种难度投影（提升复杂度/降低复杂度/同难度多样化）×2种演化方向（同技能链深度拓展/邻接技能广度拓展）
- 基于固定先验预估每个动作调整后的任务通过率，用高斯函数计算其与目标学习前沿（最优学习效率对应通过率≈50%）的匹配得分
- 构建单种子混合整数线性规划（MILP）问题，在可选技能覆盖约束下选择得分最高的动作，指导指令、输入数据、Oracle解、测试用例、Docker环境的同步改写
- 仅当生成的环境通过黄金验证（Oracle解执行所有测试得到满分奖励）时，才进入RL训练池
### 关键实验结果
基于Qwen 3.5 35B + GRPO训练，所有对比方法均生成100个验证通过的训练环境，合成token消耗控制在2.27M~2.88M的相当水平，对比Few-shot、Self-Instruct、Evol-Instruct基线：
- tb-core数据集Pass@1达49.2%，较Base提升9.2个百分点，较最强基线Evol-Instruct高2.4个百分点
- tb-2.0数据集Pass@1达29.4%，较Base提升6.4个百分点，较最强基线Self-Instruct高2.1个百分点
- 在4B~35B全尺寸Qwen 3.5模型上均获得6.8~9.2个百分点的稳定提升
### 核心结论
Agent RL的环境合成要先判断每个种子相对于当前策略的难度位置，再决定改写策略，而非对所有任务套用固定生成模板

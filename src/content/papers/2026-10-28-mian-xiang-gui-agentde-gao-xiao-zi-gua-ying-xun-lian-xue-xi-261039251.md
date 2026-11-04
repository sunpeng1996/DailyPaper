---
title: 'Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI
  Agents'
title_zh: 面向GUI Agent的高效自适应训练：学习位置与执行长度联合优化
authors:
- Yuxiang Chai
- Quyu Kong
- Panrong Tong
- Steven Hoi
- Yue Wang
affiliations:
- Alibaba Group
- The Chinese University of Hong Kong
arxiv_id: '2610.39251'
url: https://arxiv.org/abs/2610.39251
pdf_url: https://arxiv.org/pdf/2610.39251
published: '2026-10-28'
collected: '2026-11-04'
category: Agent
direction: GUI Agent 强化学习效率优化
tags:
- GUI Agent
- Reinforcement Learning
- GRPO
- Adaptive Training
- Checkpoint
one_liner: 基于动作分歧选点与两阶段自适应训练，GUI Agent RL交互成本降低56%-61%且性能提升
practical_value: '- 多步交互Agent（电商导购、自动化运营Agent）训练可复用专家轨迹中间checkpoint，跳过已掌握前缀执行，大幅降低环境交互成本

  - 训练 pivot 选择可采用动作分歧指标替代奖励方差，在奖励稀疏场景下更早识别模型决策不确定的状态，提升训练定位效率

  - 两阶段自适应训练策略可直接复用：先做不确定点单步RL warmup，再根据任务成功率动态切换Local/Suffix/Root训练模式，平衡效率与泛化性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
轨迹级GRPO是多步GUI Agent的主流训练方案，但存在两类核心低效问题：一是任务级奖励对中间步骤监督稀疏，长路径下信用分配难度高；二是每次从任务根节点启动执行，会重复运行策略已经熟练掌握的前缀步骤，环境交互成本随任务长度线性增长，多步任务下训练性价比极低。

### 方法关键点
- 可复用中间checkpoint：从验证通过的专家成功轨迹中抽取中间状态快照，支持直接从任意中间节点恢复执行，无需重放前缀动作，10步前缀的恢复延迟相比动作重放降低71.6%~81.1%
- 动作分歧选训练pivot：对候选状态多次采样策略输出的GUI动作，计算动作分布的离散度作为动作分歧，选择分歧超过阈值的状态作为训练核心节点，比奖励方差更早识别决策不确定的训练点
- 两阶段自适应训练：Stage I 对选中的pivot做单步RL warmup，快速优化局部不确定决策；Stage II 根据任务根节点成功率动态分配训练模式：成功率<0.25做Local单步训练，0.25~0.75做Suffix训练（从最深pivot逐步往前推进执行长度），>0.75做轻量化Root训练，逐步扩展策略的全链路执行能力

### 关键实验
在MobileGym、CUA-Gym-Hub两个公开GUI基准环境测试，对比Vanilla GRPO基线，全方法降低56%~61%的环境交互量，同时训练集Avg@4提升13~17个百分点，域外测试集Avg@4提升9~11个百分点，域外性能比同专家数据做SFT的方案高7个百分点以上。

最值得记住的一句话：多步交互Agent的训练效率提升核心，是将资源精准投向未掌握的决策步骤，而非重复执行已熟练的前缀。

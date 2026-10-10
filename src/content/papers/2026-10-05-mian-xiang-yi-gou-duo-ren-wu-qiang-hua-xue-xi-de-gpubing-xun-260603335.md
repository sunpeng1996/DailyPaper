---
title: A GPU-Parallel Framework for Heterogeneous Multi-Task Reinforcement Learning
title_zh: 面向异构多任务强化学习的GPU并行训练框架
authors:
- Rui Zhang
- Qiwei Wu
- Zhengyu Zhang
- Tao Li
- Hongyu Zhou
- Xiang Li
- Yunrong Guo
- Junjie Lai
- Renjing Xu
- Weihua Zhang
affiliations:
- NVIDIA
- The Hong Kong University of Science and Technology (Guangzhou)
- Tsinghua University
arxiv_id: '2606.03335'
url: https://arxiv.org/abs/2606.03335
pdf_url: https://arxiv.org/pdf/2606.03335
published: '2026-10-05'
collected: '2026-10-10'
category: Training
direction: 多任务强化学习 · GPU并行训练框架
tags:
- Multi-Task RL
- GPU Parallel
- Policy Optimization
- Benchmark
- Reinforcement Learning
one_liner: 推出GPU并行异构多任务RL基准Hebero与示范引导优化算法，提升多任务策略表现
practical_value: '- IW-ABC中基于任务进度的滞后任务加权方法，可直接迁移至多目标推荐、多意图Agent训练，解决不同任务收敛不均衡问题

  - DGPO将少量示范转换为稠密跟踪奖励的思路，可用于推荐冷启动、小样本新任务场景，降低训练样本依赖

  - Hebero单策略跨多任务GPU并行训练范式，可复用至多目标推荐模型训练，降低算力成本与迭代周期'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有GPU并行RL基准未覆盖异构多任务场景的标准化评估，单策略跨多任务训练存在稀疏奖励、样本有限、任务收敛不均衡痛点。
### 方法关键点
1. 推出基于Isaac Lab的GPU并行基准Hebero，支持单策略跨40个异构操纵任务的联合训练与评估；
2. 提出DGPO算法，复用少量示范生成稠密跟踪奖励，搭配非对称价值学习解决稀疏奖励问题；
3. 新增IW-ABC模块，通过任务进度信号自适应调整行为克隆权重，同时对滞后任务做PPO更新重要性加权。
### 关键结果数字
单任务仅需50个示范时，状态输入版本平均成功率达90.1%，较最优基线FAMO-ABC高7.8pp；视觉输入版本平均成功率达93.5%；仿真训练的单多任务策略可在实体机器人上完成4类任务。

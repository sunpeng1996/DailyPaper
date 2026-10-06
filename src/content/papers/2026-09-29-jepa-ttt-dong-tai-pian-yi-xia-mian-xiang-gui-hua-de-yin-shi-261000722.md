---
title: 'JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning
  under Dynamics Shifts'
title_zh: JEPA-TTT：动态偏移下面向规划的隐式世界模型持续测试时训练
authors:
- Zheyuan Zhang
- Suyu Ye
- Nakul Agarwal
- Hossein Nourkhiz Mahjoub
- Ehsan Moradi Pari
- Daniel Khashabi
- Tianmin Shu
- Vaishnav Tadiparthi
affiliations:
- Honda Research Institute USA
- Johns Hopkins University
arxiv_id: '2610.00722'
url: https://arxiv.org/abs/2610.00722
pdf_url: https://arxiv.org/pdf/2610.00722
published: '2026-09-29'
collected: '2026-10-06'
category: Agent
direction: Agent 世界模型测试时自适应
tags:
- JEPA
- World Model
- Test-Time Training
- Planning
- Dynamics Adaptation
one_liner: 仅更新预训练JEPA动态预测器，通过自监督持续测试时训练适配环境动态偏移，大幅提升规划性能
practical_value: '- 面对推荐系统的环境偏移（如大促流量漂移、用户行为模式突变），可借鉴「冻结特征编码器+价值头、仅更新动态预测分支」的轻量适配方案，避免表示漂移同时快速适配新分布

  - 对于电商交互Agent（如智能导购、直播间运营Agent），可复用dense replay机制，对所有时序偏移的交互窗口采样更新，用少量在线交互数据快速适配新用户/场景

  - 无需在线reward的自监督适配思路可迁移到推荐冷启动场景，只用用户行为序列的前后依赖做更新，无需等待延迟的转化标签'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
预训练世界模型在部署时如果遇到训练未见过的环境动态偏移，预测准确率会大幅下降导致规划失效；传统测试时适配要么需要在线reward，要么每轮重置无法积累知识，适配效率低。

### 方法关键点
- 冻结预训练JEPA世界模型的视觉编码器和离线训练的奖励头，仅更新隐态动态预测器，避免表示漂移和任务目标偏移，无需在线reward或目标图像即可完成规划
- 采用dense replay机制，在每个时序偏移处构造预测窗口存入持续增长的缓冲区，均匀采样小batch做自监督更新，用观测到的(状态,动作,下一个状态)三元组作为监督信号
- 预测器参数、优化器状态、回放缓冲区跨episode持续保留，适配知识可累计，无需每轮重置

### 关键实验
在4个连续控制环境的8种动态偏移场景下测试，对比Frozen JEPA、PPO-TTT、AdaJEPA三个基线；500轮测试episode后，自回归隐态预测误差平均降低83%，规划性能相对冻结JEPA提升153%，平均归一化AUC从0.267提升到0.571，6个场景性能接近甚至超过在目标动态下直接预训练的离线模型。

最值得记住的一句话：仅更新动态预测分支、保留跨轮知识的轻量自监督测试时训练，是解决预训练模型部署后分布偏移问题的高性价比方案。

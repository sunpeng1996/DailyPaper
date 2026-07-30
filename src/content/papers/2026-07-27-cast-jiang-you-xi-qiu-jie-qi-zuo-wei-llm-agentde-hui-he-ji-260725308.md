---
title: 'CAST: Game Solvers as Turn-Level Teachers for LLM Agents'
title_zh: CAST：将游戏求解器作为LLM Agent的回合级教师
authors:
- Yu Wang
- Yi-Kai Zhang
- Wentao Shi
- Ziang Ye
- Yuchun Miao
- Yueqing Sun
- Qi Gu
- Xunliang Cai
- Lan-Zhe Guo
- Han-Jia Ye
affiliations:
- University of Science and Technology of China
- Nanjing University
- Wuhan University
- Meituan
arxiv_id: '2607.25308'
url: https://arxiv.org/abs/2607.25308
pdf_url: https://arxiv.org/pdf/2607.25308
published: '2026-07-27'
collected: '2026-07-30'
category: Agent
direction: Agent训练 · 回合级信用分配
tags:
- LLM Agent
- Reinforcement Learning
- Credit Assignment
- On-policy Distillation
- RLVR
one_liner: 利用游戏求解器生成回合级优势信号注入RLVR，实现无logit蒸馏提升LLM Agent长时序决策能力
practical_value: '- 训练长时序决策Agent时，可引入领域成熟规则求解器/价值评估模块作为轻量教师，无需教师logits，仅用单步状态价值变化即可生成低成本细粒度训练信号，solver
  overhead仅占训练总耗时的73ppm，几乎可忽略

  - RL训练的信号预处理可复用asinh压缩+批次RMS归一化组合，既保留小信号区分度，又压缩极端值避免训练不稳定，同时不破坏信号正负语义（收益/惩罚的指示性）

  - 无精确求解器的业务场景（如电商用户路径优化、推荐链路价值归因），可用预训练DQN价值网络替代精确求解器，仍能保留大部分性能增益，降低落地门槛'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时序决策场景下，RLVR依赖的稀疏终局奖励无法解决回合级信用分配问题，现有稠密过程信号要么标注成本高要么精度不足，而成熟领域求解器可以低成本输出任意中间状态的价值，是理想的细粒度监督源。

### 方法关键点
- 定义求解器优势为动作前后求解器输出的剩余最优步数差值，平移后得到「正收益对应向目标前进、负对应后退/死锁」的直观可解释信号
- 信号预处理采用asinh压缩极端值+批次RMS归一化策略，保留信号正负语义的同时解决跨场景尺度不一致问题
- 将处理后的回合级优势与GRPO的轨迹级终局优势加权融合，替换原单值优势进行训练，理论证明该模式等价于无需教师logit的在线蒸馏

### 关键结果
在Sokoban、扫雷、Rush Hour三个游戏上训练，对比GRPO、DAPO等同参数基线，域内平均准确率提升17.4pct，unseen难度提升9.7pct，训练收敛速度提升1.7~2倍；零样本迁移到ALFWorld、WebShop两个下游Agent任务上，平均得分分别达到37.9、22.7，比最优基线高5.8pct、4.8pct。

最值得记住的结论：可靠的状态价值评估是将稀疏终局反馈转化为细粒度训练信号的通用路径，无论评估源是精确求解器还是学习到的价值网络。

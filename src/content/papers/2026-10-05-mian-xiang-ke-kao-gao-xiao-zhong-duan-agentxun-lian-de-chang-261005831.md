---
title: Selecting Long-Horizon Trajectories for Reliable and Efficient Terminal-Agent
  Training
title_zh: 面向可靠高效终端Agent训练的长轨迹选择方法
authors:
- Cuong Dang
- Hoang Anh Just
- Ruoxi Jia
affiliations:
- Virginia Tech
arxiv_id: '2610.05831'
url: https://arxiv.org/abs/2610.05831
pdf_url: https://arxiv.org/pdf/2610.05831
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: 终端Agent 长轨迹训练优化
tags:
- Terminal Agent
- Imitation Learning
- Supervision Horizon
- Data Selection
- SFT
one_liner: 提出两阶段选择性长轨迹精炼策略，兼顾终端Agent训练的可靠性与效率
practical_value: '- 训练长序列交互Agent（如电商导购Agent、客服Agent）时，无需盲目拉长训练序列长度，可先测试找到最优中间horizon平衡点，比全量长序列训练降本提效

  - 两阶段训练trick可直接复用：先在短序列全量数据上暖启，再用暖启模型给长轨迹的新增后缀打分，选高似然样本做精炼，兼顾训练成本与任务成功率

  - 长序列训练数据质量优先于数量，即使只用50%的精选长序列数据，效果也可超过全量长序列训练，适合算力有限的业务场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
终端Agent通常通过模仿长教师轨迹做SFT训练，但监督序列长度（horizon）对效果、成本以及Agent行为的影响未被系统研究，盲目拉长horizon会导致训练成本激增，甚至出现效果下降，还会让Agent产生过早终止或过度执行的行为偏差，亟需明确长序列训练的最优设计范式。

### 方法关键点
- 首先明确监督horizon的行为影响规律：短horizon导致Agent欠持久（遇到错误易过早终止），中等horizon支持高效错误恢复，过长horizon导致过持久（任务完成后仍冗余执行）；从理论上分解为时序监督偏差（随horizon拉长降低）和有限样本估计误差（随horizon拉长升高）的权衡。
- 提出两阶段选择性长轨迹精炼策略：第一阶段用全量短轨迹前缀暖启模型；第二阶段用暖启模型对长轨迹的新增后缀段打分，保留与短阶段学到的策略兼容性高的高似然样本做长horizon精炼。

### 关键实验
Base模型为Qwen3-8B，训练数据集为Nemotron终端交互语料，对比基线为4K/8K/12K/16K单阶段全量训练。核心结果：12K单阶段训练比16K训练时间少30%，Terminal-Bench任务解决数更高（29±0.7 vs 26±0.8）；16K场景下，选择性精炼比全量训练成功尝试数从110±2.7提升到126±2.1，6/8次尝试成功的任务数从9±0.7提升到14±0.6，训练时间降低23%，效果在多基准上一致迁移。

最值得记住的结论：长horizon训练中，选择合适的轨迹比训练所有轨迹更重要

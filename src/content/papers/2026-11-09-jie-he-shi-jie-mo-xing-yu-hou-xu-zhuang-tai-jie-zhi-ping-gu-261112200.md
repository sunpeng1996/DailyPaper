---
title: Learning to Act with World Models by Valuing What Comes Next
title_zh: 结合世界模型与后续状态价值评估的智能体强化学习方法WM-PPO
authors:
- Chenghao Gao
- Zhi Zhang
- Dian Jin
- Yihe Pan
- Doudou Zhou
affiliations:
- National University of Singapore
- University of California, Los Angeles
- Fudan University
arxiv_id: '2611.12200'
url: https://arxiv.org/abs/2611.12200
pdf_url: https://arxiv.org/pdf/2611.12200
published: '2026-11-09'
collected: '2026-11-11'
category: Agent
direction: Agent强化学习 · 世界模型+PPO优化
tags:
- World Model
- PPO
- Sparse Reward
- Reinforcement Learning
- LoRA
one_liner: 将世界模型预测后续状态与PPO critic结合，为稀疏奖励多步任务提供稳定辅助学习信号
practical_value: '- 电商导购Agent、广告投放策略Agent等仅能拿到稀疏最终转化奖励的场景，可借鉴WM-PPO思路：训练轻量世界模型预测候选动作的后续状态，用现有价值网络评估候选价值生成辅助优势信号，无额外标注即可提升训练效率

  - 价值信号校准方法可复用：用历史真实分支数据动态调整不同价值差区间的信号权重，仅当价值差大于阈值时才作为可靠信号用于训练，避免噪声价值误导更新，适合搜索推荐排序信号降噪场景

  - 训练推理解耦设计可直接复用：推理阶段仅保留策略网络，无需部署世界模型和critic，不会增加线上推理延迟，适配电商高并发业务要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多步决策Agent训练通常只有稀疏终端奖励，无法为中间步骤提供有效反馈；世界模型能预测动作带来的环境变化，但无法直接判断变化对最终成功的影响，传统PPO的critic仅能评估已访问状态的价值，无法覆盖未执行的候选动作，导致样本效率低、在需要前置条件的复杂任务上表现差。

### 方法关键点
- 提出WM-PPO框架，仅在PPO基础上新增1个世界模型组件，策略、critic、世界模型均为基座大模型的LoRA适配器，无参数共享，推理阶段仅保留策略，无额外开销
- 训练时对每个状态采样K个候选动作，世界模型预测每个动作的下一个观测，critic评估预测的后续状态得到每个动作的transition value；政策通道用transition value排序生成辅助优势信号更新策略，价值通道用transition value的均值作为critic的辅助目标更新价值网络
- 新增可靠性门控机制：用分支采样的真实交互结果，动态校准不同transition value差区间的信号权重，仅保留可靠的价值比较信号用于更新，避免噪声误导

### 关键结果
在ALFWorld、ScienceWorld两个多步文本交互环境测试：与同样本量的PPO-160相比，ALFWorld成功率从63.5%提升至87.5%，ScienceWorld成功率从39.3%提升至52.9%，比最优PPO变体在ScienceWorld上高6.5个百分点；样本效率显著优于PPO，达到相同成功率仅需60%左右的真实交互步数。

### 核心结论
用世界模型预演未执行候选动作的后果，再用现有价值网络评估后果价值，无需额外标注即可大幅提升稀疏奖励下Agent的训练效率与效果。

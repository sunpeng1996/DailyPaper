---
title: 'PACT: From Credit Assignment to Critic Alignment'
title_zh: PACT：从信用分配到评论家对齐
authors:
- Jiayan Fu
- Hang Xu
- Yong Zhang
- Zhaokai Luo
- Yao Hu
- Dongyan Zhao
- Mu Chuan
affiliations:
- AllSpark Team
- Peking University
- Xiaohongshu
arxiv_id: '2609.26355'
url: https://arxiv.org/abs/2609.26355
pdf_url: https://arxiv.org/pdf/2609.26355
published: '2026-09-21'
collected: '2026-09-24'
category: Training
direction: LLM RL后训练 · 信用分配优化
tags:
- Credit Assignment
- Actor-Critic
- RLHF
- LLM Training
- PPO
- GRPO
one_liner: 提出token级信用唯一表征定理，以及Actor优先更新的评论家对齐训练方法PACT，显著优于PPO、GRPO等现有RL算法
practical_value: '- 长序列Agent/推理LLM RL训练时，直接将GAE的λ设为1，可消除中间Critic估计误差，避免PPO训练崩溃，无需再调λ参数

  - Critic训练把默认MSE损失替换为BCE损失，无需修改其他逻辑即可加快Critic收敛速度，提升正负轨迹的价值区分度

  - 现有Actor-Critic训练框架可直接复用PACT的Actor-then-Critic更新逻辑，增加重要性采样修正Critic目标，解决Actor与Critic的策略滞后问题，提升对齐效果

  - 若当前使用GRPO/RLOO等无Critic的RL算法无需盲目优化token级信用分配，论文已证明其期望梯度与最优token级信用等价，现有方案具备理论合理性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM RL后训练中，token级信用分配长期缺乏统一数学定义，长序列场景下传统PPO的GAE中间Critic误差易盖过真实信用信号，Actor与Critic的策略滞后问题也会严重降低训练稳定性与效果，现有不同RL算法的表现差异缺乏统一解释框架。
### 方法关键点
- 提出三个信用分配正则条件：完备性、前缀一致性、中立性，证明满足条件的token级信用唯一，等于相邻步条件奖励期望的差值
- 统一解释现有算法：理想老师的On-Policy Distillation等价于隐式Critic，RLOO响应级信号的期望梯度与最优token级信用等价，GAE取λ=1可消除中间Critic误差
- 提出PACT训练流程：先更新Actor再更新Critic，用重要性采样修正Critic训练目标，Critic改用BCE损失替代MSE提升估计精度
### 关键实验
数学推理任务基于Qwen3.5-4B，4个基准平均准确率72.87%，较GRPO高8.8pct、较PPO高13.16pct；SWE-bench Verified编码任务基于Qwen3.6-35B-A3B，通过率67.4%，较GRPO高2pct、较PPO高2.4pct。
**最值得记住的结论**：token级信用唯一等于每步新增信息带来的奖励预期增量，长序列LLM RL训练中保证Critic与当前Actor的对齐，比追求细粒度信用估计优先级更高。

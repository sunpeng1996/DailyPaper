---
title: Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning
title_zh: 面向长程智能体强化学习的树感知后验蒸馏方法
authors:
- Heming Zou
- Qi Wang
- Yixiu Mao
- Yun Qu
- Yuyi Guo
- Zeyuan Liu
- Chenglin Li
- Weijie Liu
- Saiyong Yang
- Xiangyang Ji
affiliations:
- Tsinghua University
- Tencent
arxiv_id: '2610.23181'
url: https://arxiv.org/abs/2610.23181
pdf_url: https://arxiv.org/pdf/2610.23181
published: '2026-10-15'
collected: '2026-10-19'
category: Agent
direction: 长程Agent强化学习·无critic自蒸馏
tags:
- Agentic RL
- Long-Horizon
- Self-Distillation
- Credit Assignment
- Reinforcement Learning
one_liner: 提出无critic的树感知后验自蒸馏框架TreeOPSD，解决长程Agent RL的信用分配与策略陈旧问题
practical_value: '- 长程多轮交互类Agent（如电商导购Agent、用户意图探索Agent）训练时，可复用共享前缀分支采样+终端奖励递归回传方法，无需标注中间步骤奖励即可获得稠密turn-level信用信号，大幅降低标注成本

  - 做RLHF/RLVR训练时，可替换现有PPO/GRPO的策略更新逻辑为Forward-KL后验蒸馏方案，自动修正策略漂移导致的更新过冲问题，无需额外引入critic网络，降低训练复杂度

  - 采样预算有限的场景下，可参考rollout分配策略：将部分全轨迹采样预算替换为共享前缀的分支采样，相同成本下可获得更优模型效果，适合资源受限的业务落地'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
长程多轮Agent的RL训练存在两个核心痛点：仅用终端奖励会导致turn-level信用分配稀疏、方差高；固定rollout批次的顺序小批量更新会引发策略陈旧，当前策略与行为策略偏离后易出现更新过冲。现有方法要么依赖难训练的critic、昂贵的步骤级标注，要么需要外部强教师，训练复杂度高且缺少明确的更新终止目标。

### 方法关键点
- 构建无critic的TreeOPSD框架，将每轮交互作为树节点，从共享前缀分支生成多组后续轨迹，递归将终端奖励回传为隐式turn-level信用，无需额外价值网络或标注
- 基于行为策略的似然比将每轮信用映射为闭式有界的教师分布，避免重要性采样的指数级方差
- 用Forward-KL最小化学生策略与固定教师分布的差异，初始点梯度等价于树策略梯度，更新过程中自适应调整步长，过冲时自动反转梯度方向，抑制策略漂移

### 关键实验结果
在Multi-Hop QA和Deep Research两个长程任务上测试，对比ReAct、GRPO、GSPO、TreePO等同预算基线，Qwen3-30B模型在Deep Research场景平均准确率比GRPO高4.97个点，比TreePO高3.61个点，长程任务收益更明显；相同采样预算下，4条初始轨迹+2次分支的分配方式比全独立轨迹效果更优。

### 最值得记住的一句话
无额外标注、无critic的共享前缀树后验蒸馏方案，是长程多轮Agent低成本RL训练的高性价比路径。

---
title: 'Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL'
title_zh: Co-RL：多智能体强化学习中多样化群组催生无监督推理能力
authors:
- Yunhao Yang
- Yuexin Bian
- Yunjie Tian
- Di Fu
- Tianjin Huang
- Yuanyuan Shi
- Ziang Xiao
- Nuno Vasconcelos
- Yijiang Li
affiliations:
- Johns Hopkins University
- UC San Diego
- University of Exeter
- Independent Researcher
arxiv_id: '2608.17253'
url: https://arxiv.org/abs/2608.17253
pdf_url: https://arxiv.org/pdf/2608.17253
published: '2026-08-18'
collected: '2026-08-20'
category: Agent
direction: 多智能体RL · 无监督推理能力优化
tags:
- Multi-agent RL
- Unsupervised Reasoning
- GRPO
- Cross Supervision
- Label-free RL
one_liner: 提出无参数共享的多智能体交叉监督RL框架Co-RL，无需真值标签即可提升LLM/VLM推理性能
practical_value: '- 可复用多智能体交叉监督思路优化导购/客服Agent推理能力：无需标注真值，用不同基座Agent互相生成奖励做RL微调，降低标注成本，避免自奖励的偏差放大问题

  - 优化Agent集群时可刻意引入异构性：组合不同基座、参数规模、输入改写版本的Agent，降低错误相关性，提升交叉监督的伪标签质量

  - 推荐系统多模型融合训练可借鉴该框架：召回/排序层的异构模型做交叉监督，无需额外标注就能提升精度，避免单模型自训练塌陷

  - 工程实现可复用轻量设计：仅在奖励阶段交互，无参数/梯度共享，无需额外LLM裁判，训练开销低，适合业务场景落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RL提升大模型推理能力严重依赖真值标注，成本高且无法适配能力超过人类评估水平的场景；自奖励RL则易放大模型固有偏差、降低输出多样性，最终导致训练塌陷，亟需无真值、无外部裁判的高效RL训练框架。

### 方法关键点
- 群组架构：多个无参数共享的异构Agent构成训练集群，每个Agent对同一无标注prompt生成K个响应，提取答案后多数投票得到伪标签
- 交叉奖励机制：每个Agent的响应奖励完全由另一个指定Agent的伪标签判定，与自身输出解耦，打断自奖励的偏差放大循环
- 多样性增强：从模型架构/参数规模、训练输入改写、独立参数更新三个维度引入异构性，降低Agent间错误相关性，提升伪标签可靠性
- 优化适配：采用GRPO做策略优化，每个Agent独立更新，仅通过奖励信号耦合

### 关键结果
- 文本推理：在GSM8K、MATH-500等7个基准上，平均性能提升3.0~8.6%，比最优自奖励基线高0.8~2.0%；比CoMAS等多智能体RL方法高4.0%，且仅用一半数量的Agent
- 多模态推理：在MathVista等4个多模态数学推理基准上，平均性能提升2.3~7.2%，部分场景超过有真值监督的GRPO效果

### 核心结论
只要两个异构Agent对同一任务的初始正确率之和大于1，交叉监督就能让两者都收敛到100%正确率，大幅优于自奖励的学习效果

---
title: 'Environments as Scaffold: Enriching Feedback to Bootstrap Self-Evolving Agents
  in Long-Horizon Tasks'
title_zh: 环境作为支架：通过丰富反馈赋能长程任务自进化Agent
authors:
- Hongbang Yuan
- Zhuoran Jin
- Yixin Cao
affiliations:
- Fudan University
- CASIA
- Shanghai Innovation Institute
arxiv_id: '2609.08404'
url: https://arxiv.org/abs/2609.08404
pdf_url: https://arxiv.org/pdf/2609.08404
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: 长程任务Agent RL训练环境优化
tags:
- LLM Agent
- Reinforcement Learning
- Long-horizon Task
- Feedback Enrichment
- Policy Optimization
one_liner: 提出反馈丰富环境FEEs范式，解决长程任务Agent RL训练奖励稀疏问题，稳定训练提升性能
practical_value: '- 做电商导购Agent、多轮搜索推荐Agent这类长交互任务的RL训练时，可复用「早期动作引导+后期状态补充」的反馈策略，早期直接提示下一步可调用的查询/推荐接口、需要补全的用户信息，后期补充当前会话状态、任务进度，解决早期奖励稀疏导致的训练不动问题

  - 用GRPO/GSPO等组式RL算法训练Agent时，同一采样组内的反馈规则必须保持一致，禁止随机给同组不同样本差异化的补充反馈，否则会导致优势估计失真，训练出现大幅波动

  - 训练阶段引入的丰富反馈无需在推理时携带，FEE训练学到的能力会内化到模型权重中，推理切回标准环境依然能保留性能增益，不会增加额外推理成本

  - 针对用户多轮决策类推荐任务（如套餐选购、服饰搭配），可模仿FEE思路构造课程化训练环境，逐步降低引导强度，平衡探索效率和策略泛化性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程任务下基于RL训练LLM Agent普遍面临严重奖励稀疏问题，Agent易陷入零奖励轨迹导致梯度消失；传统Agent侧SFT热启动依赖高质量专家轨迹，采集成本高且易限制探索空间，难以适配复杂长程交互场景。
### 方法关键点
- 范式从Agent侧优化转向环境侧适配，构造**反馈丰富环境（FEEs）**，从「反馈内容」和「投放时机」两个维度系统设计引导策略
- 反馈内容分为两类：Action Guidance（AG）直接给出下一步可行操作，快速剪枝无效搜索空间；Observation Enrichment（OE）补充环境隐藏状态信息，降低POMDP部分可观测性
- 投放时机覆盖两个时间尺度：单episode内的交互阶段、训练全周期的迭代阶段，最优策略为「AG配早期、OE配后期」，即单episode前半段+训练前半周期投放AG，单episode后半段+训练后半周期切换为OE
### 关键结果
在SciWorld、BFCL两个长程Agent基准上测试，覆盖Qwen3-4B/8B模型，GRPO/DAPO/GSPO三种主流RL算法：
- 相比标准环境，FEEs训练跨模型、跨算法平均性能提升2.82%，最优配置下Qwen3-8B+GSPO的SciWorld任务提升7.03%，Qwen3-4B+GRPO的BFCL基础任务提升10%
- FEEs可降低策略熵波动，无熵正则化时训练崩溃节点从250步延迟到300步以上；困难任务上性能额外提升4.3%，且反馈会内化到模型权重，推理时无需携带额外引导信息
### 核心结论
长程Agent RL训练的瓶颈往往不在Agent侧，环境侧的课程化反馈设计能以极低成本带来稳定的性能提升

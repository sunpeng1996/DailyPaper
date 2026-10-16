---
title: Learning to Steer LLM Agents and Multi-Agent Systems
title_zh: LLM单智能体与多智能体系统的动态引导代理学习方法
authors:
- Leyang Shen
- Yaxin Gong
- Yang Zhang
- Chenxiao Fan
- Jiakai Wang
- Dong Wang
- Yang Liu
- Fuli Feng
- Chun Kai Ling
- Tat-Seng Chua
affiliations:
- National University of Singapore
- University of Science and Technology of China
- Qwen Business Unit of Alibaba
arxiv_id: '2610.22316'
url: https://arxiv.org/abs/2610.22316
pdf_url: https://arxiv.org/pdf/2610.22316
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: Agent 目标漂移实时矫正
tags:
- LLM Agent
- Multi-Agent System
- Goal Drift
- Reinforcement Learning
- GRPO
- On-the-fly Supervision
one_liner: 提出快慢路径结合RL训练的引导代理，实时纠正目标漂移，提升单/多智能体性能与效率
practical_value: '- 电商导购Agent、多角色商品文案生成多智能体系统可直接复用该架构：新增独立引导代理无需微调执行端Agent，即可实时纠正执行中偏离用户需求/任务目标的问题，降低无效交互、提升任务成功率

  - 快慢路径的低开销设计可直接迁移到搜索/推荐的低延迟场景：fast path用单token预测干预优先级，开销仅为一次LLM前向推理，仅高优先级场景触发slow
  path生成干预，平衡效果与 latency 要求

  - 训练方案可复用：采用pairwise ranking + GRPO的无标注RL训练范式，仅依赖任务最终反馈即可优化引导能力，训练好的引导代理可跨不同基座执行Agent迁移，无需为每个基座单独重训

  - 可通过调整fast path阈值动态控制干预频率，适配不同业务的资源约束：高价值用户场景调高阈值提升效果，普通场景调低阈值降低计算成本，无需重新训练模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长链路LLM Agent和多智能体系统执行时普遍存在目标漂移问题：单智能体可能反复执行无用检索、多智能体各角色过度关注局部目标偏离全局任务，传统事前规划、事后校验的方案要么无法应对动态执行偏差，要么补救滞后、成本高，造成资源浪费和任务失败。

### 方法关键点
- 设计独立引导代理，观测任务目标与执行上下文，判断是否干预、如何干预，采用快慢双路径架构共享LLM backbone：fast path通过单token yes/no概率计算干预优先级，低开销判断是否触发干预；slow path仅在优先级超过阈值时触发，通过CoT生成具体干预动作
- 采用RL联合训练双路径：fast path用pairwise ranking loss学习给高价值干预状态打更高分；slow path用GRPO优化干预动作生成，训练时执行器完全冻结，仅更新引导代理参数

### 关键结果
- 单智能体搜索QA场景下，7个基准数据集平均F1较无干预提升6.66分，单任务仅触发0.93次干预，执行轮次降低3%；最高干预频率下F1提升可达17.11分
- 引导能力可泛化到域外任务，跨未见过的执行基座迁移时，最高可给Llama-3.1-8B带来15.78分的F1提升，无需重新训练
- 五角色多智能体搜索场景下，较无干预平均F1提升5.34分，远优于零样本引导的负向效果

### 核心结论
对于长链路Agent系统，独立的动态引导模块比事前规划、事后校验的矫正效率更高，且无需修改执行端即可快速落地

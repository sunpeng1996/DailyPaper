---
title: 'QwenGyre: An Elastic Reinforcement Learning Framework for Training xLong-Horizon
  Agents'
title_zh: QwenGyre：面向超长时序Agent训练的弹性强化学习框架
authors:
- Weiqi Wang
- Yuxin Zhou
- Mouxiang Chen
- Siyuan Zhang
- Yi Zhang
- Yuyan Luo
- Zhiyu Yin
- Chencan Wu
- Jiemin Jiang
- Wentao Yao
affiliations:
- Alibaba Group
- University of Science and Technology of China
- Tsinghua University
arxiv_id: '2609.33848'
url: https://arxiv.org/abs/2609.33848
pdf_url: https://arxiv.org/pdf/2609.33848
published: '2026-09-26'
collected: '2026-09-29'
category: Agent
direction: Agent 超长时序RL训练优化
tags:
- LLM-Agent
- Reinforcement-Learning
- Training-Framework
- Scheduling
- Trajectory-Optimization
one_liner: 提出弹性调度+分支轨迹优化的RL训练框架，大幅提升超长时序Agent训练效率与效果
practical_value: '- 电商多轮导购/售后Agent、搜索query多轮改写等场景的RL训练，可复用弹性调度策略，动态分配GPU在rollout与训练间的算力，降低GPU
  idle率，减少训练成本

  - 存在分支轨迹的多轮交互Agent训练，可借鉴轨迹树共享前缀去重+按角色优先级采样的方法，减少冗余训练样本，提升训练效率

  - Agent训练的超时样本不要直接丢弃，可参考其partial progress打分后纳入训练，充分利用长尾交互数据，提升多轮任务最终效果

  - KV cache跨节点RDMA迁移的trick可用于多轮对话服务的负载调度场景，减少会话切换的prefix重计算开销，降低推理延迟'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent越来越多地承担超长时序（XLong）任务，单轮rollout需数百次模型-环境交互、单条轨迹近1M token，在线RL训练面临两个核心痛点：一是rollout执行方差大、延迟长导致GPU大量空闲；二是轨迹非线性分支多、冗余度高，传统Colocate、Async调度框架无法适配，训练效率极低。

### 方法关键点
- 弹性调度器：将GPU划分为可独立切换角色的细粒度弹性cell，不中断正在执行的rollout任务的前提下，动态调整rollout与训练的算力分配；新增节点可随时加入正在进行的训练batch，流式训练平衡各节点进度，减少空闲间隙
- 轨迹处理器：将分支执行的轨迹组织为带共享前缀的轨迹树，支持对超时执行的部分进度打分；单轮执行最多选Jmax条高优先级（主Agent>子Agent>摘要轨迹）样本训练，共享前缀的目标仅计算一次loss，避免冗余

### 关键实验
在NL2RepoBench、DeepSWE、TerminalBench三个数据集测试，对比Colocate、Async基线：相同GPU预算下，端到端训练速度比Colocate最高快1.85×，比Async最高快1.78×，效果持平；2.4T参数的Qwen 3.8模型在NL2RepoBench上仅48步就将passrate从52.5%提升到58.5%，绝对提升6个百分点。

### 核心结论
超长时序Agent RL训练的核心瓶颈是算力利用效率和轨迹冗余，通过系统层弹性调度+数据层轨迹去重可实现数倍效率提升，同时不损失训练效果。

---
title: 'EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement
  Learning'
title_zh: EnvSched：面向高效Agent强化学习训练的环境感知调度器
authors:
- Sihan Yang
- Weichen Bai
- Ruichuan An
- Yiming Cheng
- Zhiyuan Feng
- Tianyi Jiang
- Renye Yan
- Ning Ding
- Yifan Zhang
- Renrui Zhang
affiliations:
- Peking University
- Xi'an Jiaotong University
- Tsinghua University
- Samsung Research
- CASIA
arxiv_id: '2610.37609'
url: https://arxiv.org/abs/2610.37609
pdf_url: https://arxiv.org/pdf/2610.37609
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent RL训练优化 · 环境感知调度
tags:
- Agent RL
- Scheduling
- GRPO
- Rollout Efficiency
- Graph Modeling
one_liner: 基于环境-任务双关系图实现无探针Agent RL调度，相同预算下训练效率提升3倍
practical_value: '- 做电商导购/客服Agent RL训练时，可直接复用50%覆盖+50%利用的batch分配规则，相同rollout预算下快速提升模型性能，无额外探针开销

  - 多场景Agent训练可借鉴双关系图设计：同场景基于任务语义、工具结构建边，跨场景基于抽象操作（查/改/校验等）建边，实现训练信号跨场景迁移

  - 推荐系统训练数据调度可复用其奖励方差+覆盖度的排序逻辑，优先选高奖励方差样本提效，加相似性惩罚避免batch冗余

  - 工程上可直接参考其O(N)调度实现，调度耗时仅占单训练步的2%左右，可快速集成到现有GRPO训练管线'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Agent RL训练的执行环境规模已从数十扩展到数千，rollout生成与验证成本占比大幅攀升；现有调度方法仅建模任务本身，完全忽略了环境（工具接口、状态转移规则、校验逻辑等）对训练信号质量的影响，相同rollout预算下训练效率极低。

### 方法关键点
- 以「环境-任务对」为最小调度单元，离线构建双关系图：同环境边基于任务语义、共享工具/状态/校验规则计算相似度，跨环境边基于抽象执行流程（查询、校验、更新等）计算相似度
- 沿两类边传播历史rollout的奖励方差、均值统计量，结合任务自身历史预测当前奖励方差，作为任务信息丰富度的核心指标
- 调度逻辑：每批50%配额分给未充分观测的环境/任务保障覆盖度，50%分给高预测奖励方差的任务保障信息密度，同时加环境配额限制、相似性惩罚避免batch冗余
- 完全复用历史训练数据，无需额外pilot rollout探针开销

### 关键结果
在EnvScaler数据集（51个环境、2550个任务）上用GRPO训练Qwen3全系列模型，对比随机调度、DPS、LEEPS等基线：
- Qwen3-8B训练40步在3个基准上的平均得分48.81，超过随机调度120步的最高得分，训练效率提升3倍
- 200步训练预算下，全系列模型在BFCL-v3、τ-Bench、ACEBench-Agent上平均提升2-4个百分点
- 单步调度耗时仅占Qwen3-4B训练步的2.3%，无显著额外开销

**最值得记住的一句话**：Agent RL训练的效率提升不仅要选对任务，还要选对承载任务的环境，奖励差异度与环境覆盖度是同等重要的两个优化目标。

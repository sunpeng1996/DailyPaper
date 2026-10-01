---
title: 'OPTS-TTPO: Enhancing Finite-Sample Policy-Gradient Learning with Tree Search'
title_zh: OPTS-TTPO：结合树搜索优化有限样本策略梯度学习
authors:
- Junyu Lu
- Shichao Weng
- Zhiqiang Wang
- Haojie Luo
- Jingfan Zhang
- Yuhua Zhou
- Cheng Du
- Yuzhuo Zhang
- Xi Li
- Jinwei Du
affiliations:
- Dobot Robotics
- Zhejiang University
- Fudan University
- Osaka University
- Beijing Institute of Technology Zhuhai
arxiv_id: '2609.40035'
url: https://arxiv.org/abs/2609.40035
pdf_url: https://arxiv.org/pdf/2609.40035
published: '2026-09-30'
collected: '2026-10-01'
category: Training
direction: 强化学习训练 · 树搜索+策略梯度优化
tags:
- Policy Gradient
- Tree Search
- PPO
- RLHF
- On-Policy Training
one_liner: 提出同策略并行树搜索与树轨迹策略优化框架，有限预算下提升策略梯度性能并控制偏差
practical_value: '- 做电商导购Agent、营销文案生成的RLHF/RLAIF训练时，可复用TTPO的分支加权聚合逻辑，避免树采样时高价值分支过计数导致的梯度偏差，无需额外做重要性采样校正。

  - 有限推理预算下处理复杂用户Query的多步导购、检索增强生成时，可采用OPTS的性能差异引导的分支扩展策略，相比独立重复采样可提升正确答案覆盖率2~3个百分点。

  - 高回报样本稀缺的推荐冷启动、广告创意优化场景，可复用该方法的高回报轨迹挖掘逻辑，在有限样本下提升长尾优质策略的召回效率，降低采样成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有策略梯度方法（如PPO）依赖有限同策略轨迹采样，极易遗漏稀有高回报轨迹，导致梯度估计偏差大、样本效率低；普通树搜索虽能提升轨迹覆盖，但会引入不可控的梯度偏差，且缺乏统一的树数据聚合和有限预算分配机制，难以直接落地到LLM、推荐等业务场景。
### 方法关键点
- 证明分支聚合引理：当分支决策仅依赖前缀信息时，通过分支加权的树统计量可完全恢复普通链状轨迹的期望，无需额外的动作分布校正。
- 设计TTPO（树轨迹策略优化）：在PPO裁剪目标中加入分支权重修正，同时配套TreeGAE优势估计方法，从根源解决分支采样导致的状态访问计数偏差问题。
- 设计OPTS（同策略并行树搜索）：基于critic输出的性能差异估计，自适应选择最优状态扩展新的同策略后缀，在确定性环境下有策略回报单调提升的理论保证；自适应扩展引入的偏差可被显式约束，通过max backup机制给引导到高回报后缀的前缀分配额外信用，加速优质策略收敛。
### 关键结果
跨三类任务验证效果：① MuJoCo连续控制任务尾回报比PPO平均提升18.7%，最高提升28.6%；② Atari-57游戏基准上，尾回报对PPO取得34胜22负1平的成绩；③ LLM数学推理任务上，四款Qwen3模型的avg@32比PPO提升0.72~2.32个百分点，pass@32提升0.44~2.33个百分点。相同采样预算下，OPTS的正确答案覆盖率比独立同分布采样高2~3个百分点，TTPG的梯度偏差稳定在0.12左右，远低于朴素PG的0.49。

有限采样预算下，树搜索结合分支加权的梯度校正，可以在可控偏差范围内大幅提升高回报轨迹的覆盖率，样本效率远优于独立同分布采样。

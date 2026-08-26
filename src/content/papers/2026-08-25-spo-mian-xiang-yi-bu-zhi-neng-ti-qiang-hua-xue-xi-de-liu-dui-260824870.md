---
title: 'SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL'
title_zh: SPO++：面向异步智能体强化学习的流对齐策略优化
authors:
- Kai Ruan
- Jinghao Lin
- Qianshan Wei
- Ziqi Zhou
- Zihe Huang
affiliations:
- 中国人民大学高瓴人工智能学院
- Independent Researcher
- 中国科学院自动化研究所
- 杜克大学
- 中国科学院计算技术研究所
arxiv_id: '2608.24870'
url: https://arxiv.org/abs/2608.24870
pdf_url: https://arxiv.org/pdf/2608.24870
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent异步强化学习策略优化
tags:
- RL
- Asynchronous Agent
- Policy Optimization
- Online Learning
- SPO
one_liner: 修正SPO的基线时序与归一化度量偏差，提升异步Agent RL的在线学习效率
practical_value: '- 做异步Agent RL（如电商导购Agent、工具调用类推荐Agent训练）时，可直接替换SPO的归一化策略为action-token-measure归一化，解决轨迹长度和优势协变带来的训练偏差，实测可提升10pct左右的学习效率

  - 异步训练场景下，采用按策略事件坐标而非请求接收顺序更新prompt基线的方案，可消除系统调度时序对训练稳定性的影响，无需额外引入critic模块

  - 单流RL训练的优化思路可迁移到生成式推荐的RLHF/RLAIF pipeline中，减少对同prompt多采样的依赖，降低长序列生成场景的训练成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
GRPO类组相对强化学习需要等待同prompt的所有并行采样轨迹完成才能更新，对于工具调用、长交互的Agent场景训练延迟极高；现有单流策略优化SPO消除了组依赖，但存在两个核心偏差：一是prompt基线按请求接收顺序更新受系统调度干扰，二是轨迹级优势归一化和token平均的actor损失存在度量不匹配，导致训练不稳定、效率低。

### 方法关键点
- 设计事件时间prompt记忆模块：请求分发时冻结当前prompt基线，轨迹返回后按生成该请求的策略事件坐标更新历史证据，基线计算与请求接收顺序完全无关
- 提出动作令牌度量归一化：按轨迹的有效动作token数加权计算优势的均值和方差做归一化，保证归一后的优势在token平均损失下的加权均值为0，消除轨迹长度和优势协变带来的偏差
- 保留SPO的单轨迹更新、无critic、终端奖励的核心特性，仅修改基线更新逻辑和优势归一化策略，迁移成本极低

### 关键实验
在ALFWorld（0.8B/2B Qwen3.5模型）和Math-TIR（0.8B Qwen3.5）两个任务上和SPO做对比：ALFWorld 0.8B场景下奖励曲线AUC提升19pct，最终奖励高7.86pct；ALFWorld 2B场景下AUC提升15.92pct，最终奖励高4.88pct；Math-TIR场景下AUC提升2.5pct，最终奖励高5.03pct；消融实验验证动作令牌度量归一化单独贡献10.7pct的性能提升。

### 核心结论
单流RL的持久统计量需要同时和策略时钟、actor优化的度量对齐，才能在消除组依赖的同时保证训练效率和稳定性。

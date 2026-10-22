---
title: 'From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent
  Manipulation'
title_zh: 从VLM规划器到机器人智能体：面向历史依赖操作的自演化框架
authors:
- Tingwen Du
- Haoyu Guo
- Hanxue Zhang
- Xuanxu Wang
- Junting Dong
- Chao Gao
- Mingfei Han
- Tao Lu
- Mulin Yu
- Chunhua Shen
affiliations:
- University of Science and Technology of China
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Mohamed bin Zayed University of Artificial Intelligence
- Zhejiang University
arxiv_id: '2610.29560'
url: https://arxiv.org/abs/2610.29560
pdf_url: https://arxiv.org/pdf/2610.29560
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: 具身Agent 长周期历史依赖任务规划
tags:
- VLM
- Embodied Agent
- Self-Evolution
- Task Planning
- Long-Horizon Task
one_liner: 提出带可编辑上下文管理模块的自演化机器人Agent SERA，提升长周期具身任务成功率
practical_value: '- 可借鉴「上下文动态更新+执行反馈驱动规划迭代」的架构，迁移到电商多轮导购Agent、长周期用户行为路径推荐场景，解决非马尔可夫决策依赖问题

  - 自演化配置选型思路可复用：先通过小流量环境rollout评估不同prompt/规则配置，再固化最优配置上线，降低大模型Agent的线上试错成本

  - 高低阶分层控制（固定低阶执行器+可变高阶规划层）的架构可参考，平衡推荐/导购Agent的响应稳定性和策略灵活性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
VLA模型在具身操作任务表现优异，但长周期任务存在非马尔可夫依赖，需保留任务进度、历史交互信息，现有方案未充分利用执行反馈迭代规划策略，长期执行误差易累积。

### 方法关键点
- 采用分层Agent架构SERA：固定VLA低阶执行器负责底层控制，高阶VLM规划层搭配可编辑harness模块，基于观测值、执行反馈动态维护更新任务上下文，指导后续规划。
- 自演化机制通过环境rollout生成、评估harness的不同修订版本，选最优配置固化后用于测试。

### 关键结果
在RoboMME基准上，带自演化选择的SERA整体成功率达51.38%，较无自演化基线提升7个百分点。

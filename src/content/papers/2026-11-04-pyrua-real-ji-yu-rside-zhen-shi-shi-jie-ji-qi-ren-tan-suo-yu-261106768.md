---
title: 'PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real
  World'
title_zh: PyRUA-REAL：基于RSI的真实世界机器人探索与自适应学习
authors:
- Qiang Wang
- Jianxin Bi
- Shulong Jiang
- Ruiyang Si
- Wenbo Huang
- Kaiqi Chen
- Jiaxin Li
- Liyun Li
- Xuanyi Li
- Daquan Zhou
affiliations:
- Peking University
- EngineAI
- National University of Singapore
arxiv_id: '2611.06768'
url: https://arxiv.org/abs/2611.06768
pdf_url: https://arxiv.org/pdf/2611.06768
published: '2026-11-04'
collected: '2026-11-07'
category: Agent
direction: 具身Agent · 递归自改进框架设计
tags:
- Embodied Agent
- Recursive Self-Improvement
- Code as Policy
- Persistent Memory
- Skill Reuse
one_liner: 提出支持具身递归自改进的PyRUA-REAL框架，可将物理交互经验转化为可复用机器人技能
practical_value: '- 可复用Agent技能沉淀思路：将交互经验转化为可执行的结构化技能+持久化记忆，替代全链路在线推理，适合搜推/广告Agent的运营策略跨场景复用，降低推理成本

  - 反馈驱动的迭代机制：基于执行反馈自动精调策略的逻辑，可直接迁移到搜推线上AB实验的自动调优链路，减少人工介入

  - 多Agent协作模式：多Agent分工探索+共享技能池的架构，可借鉴到多Agent搜推系统的能力迭代，提升跨任务迁移效率'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前大模型驱动的编码Agent可实现空间推理到机器人可执行行为的映射，但无法将单次物理交互经验转化为持久化可复用能力，难以实现跨任务的持续能力提升。
### 方法关键点
1. 提出PyRUA-REAL框架，支持具身递归自改进（RSI），核心是将编码Agent的交互经验存储为持久化记忆和可复用执行技能，指导后续探索与策略优化
2. 量化验证多Agent协作模式、执行反馈类型、已有技能储备对代码精调效果、任务鲁棒性和迁移能力的影响，生成的最终策略可脱离在线Agent独立部署
### 关键结果
- 8项真实世界物理操作任务平均成功率达91.1%
- RoboDojo基准42项任务平均成功率达84.4%

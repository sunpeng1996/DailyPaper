---
title: Benchmarking and Enhancing Skill-Level Memory for Partially Observable Robotic
  Manipulation
title_zh: 部分可观测机器人操作场景下技能级记忆的基准构建与优化
authors:
- Yansong Shi
- Jiange Yang
- Xijie Yang
- Shaowei Zhang
- Yuhan Zhu
- Tao Lu
- Limin Wang
affiliations:
- 中国科学技术大学信息科学技术学院
- 上海人工智能实验室
- 浙江大学计算机科学与技术学院
- 上海交通大学计算机科学与技术学院
- 南京大学计算机软件新技术国家重点实验室
arxiv_id: '2609.38886'
url: https://arxiv.org/abs/2609.38886
pdf_url: https://arxiv.org/pdf/2609.38886
published: '2026-09-29'
collected: '2026-10-04'
category: Other
direction: 机器人操作 · 部分可观测场景记忆优化
tags:
- Robotic Manipulation
- Partial Observability
- Memory Mechanism
- Benchmark
- Framework
one_liner: 提出面向部分可观测机器人操作的HIDE记忆评测基准，以及融合多记忆机制的SEEK优化框架
practical_value: '- 多互补记忆机制融合的架构思路可迁移至电商 Agent 决策系统，针对不同任务匹配对应记忆模块，避免单一记忆的适配边界问题

  - 部分可观测场景下隐状态建模的思路可复用至用户行为序列建模，捕捉当前交互无法体现的隐藏用户偏好，提升长序列推荐效果

  - 依赖历史信息的任务评测设计方法可用于优化序列推荐系统的基准评测体系，覆盖强历史依赖类推荐场景的效果验证'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人操作策略多依赖当前观测或有限时序上下文，无法应对真实场景中决策信息隐藏、需依赖交互历史的部分可观测场景，缺乏统一的技能级记忆能力评测基准。
### 方法关键点
1. 构建HIDE评测基准，覆盖重复计数、历史状态召回、执行进度跟踪3大类共15个任务，设置随机初始配置与必须依赖历史信息才能正确决策的测试点
2. 提出SEEK框架，融合三类互补记忆机制留存历史证据、跟踪任务执行隐状态
### 关键结果
现有主流策略在HIDE上表现存在明显局限，记忆增强方案可同时提升仿真与真实实验的任务成功率；单一记忆机制存在任务适配性局限，三类机制融合的SEEK在所有评测配置中取得最高平均成功率。

---
title: 'ASPIRE: Agentic /Skills Discovery for Robotics'
title_zh: ASPIRE：面向机器人的智能体技能自主发现系统
authors:
- Runyu Lu
- Yubo Wu
- Ethan Kou
- Letian Fu
- Wenli Xiao
- Ajay Mandlekar
- Yinzhen Xu
- Guanya Shi
- Ken Goldberg
- Ang Chen
affiliations:
- NVIDIA
- UMich
- UIUC
- UC Berkeley
- CMU
arxiv_id: '2607.00272'
url: https://arxiv.org/abs/2607.00272
pdf_url: https://arxiv.org/pdf/2607.00272
published: '2026-06-29'
collected: '2026-07-04'
category: Agent
direction: 机器人Agent 可复用技能持续学习
tags:
- Agentic Learning
- Skill Library
- Continual Learning
- Code-as-Policy
- Evolutionary Search
- Sim-to-Real
one_liner: 提出自主迭代探索的机器人持续学习系统，自动生成优化控制程序并沉淀可复用技能库
practical_value: '- 可复用技能库的沉淀逻辑可迁移到电商Agent/推荐系统：将业务中反复验证的流程、算子、规则蒸馏为可调用的原子能力，大幅降低新任务适配成本

  - 闭环执行+故障自修复架构可用于电商Agent用户交互链路：自动识别推荐结果、交互话术的无效反馈，实时生成修复方案并验证，提升转化率

  - 进化搜索生成多样任务序列的思路可用于推荐系统离线评测：生成更丰富的用户交互序列、异常场景，提升评测覆盖度和模型鲁棒性'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
传统机器人编程门槛极高，需协同多模态感知、处理物理接触动态、适配复杂环境配置与执行故障，人工定义的流程泛化性差。
### 方法关键点
基于code-as-policy范式的持续学习系统，采用三段式开环学习架构：
1. 闭环执行引擎输出细粒度多模态trace，支持自主故障诊断、修复方案生成与验证
2. 持续扩张的技能库，将验证通过的修复逻辑蒸馏为可迁移的通用知识
3. 进化搜索模块生成多样化任务序列与控制程序，突破单轨迹优化边界
### 关键结果
- 扰动下LIBERO-Pro操作任务超此前最优方法77%，Robosuite双手交接任务提升72%，BEHAVIOR-1K长周期家庭任务提升32%
- 零样本泛化未见过的LIBERO-Pro Long长周期任务成功率31%，远超此前方法的4%
- 模拟环境发现的技能可实现sim-to-real迁移，大幅降低不同实体机器人编程工作量

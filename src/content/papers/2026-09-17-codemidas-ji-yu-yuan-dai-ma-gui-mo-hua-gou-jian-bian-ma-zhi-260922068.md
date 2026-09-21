---
title: 'CodeMidas: Scaling Agentic Coding RL Environments from Code Itself'
title_zh: CodeMidas：基于源代码规模化构建编码智能体RL训练环境
authors:
- Bowen Ye
- Lei Li
- Shicheng Li
- Zihao Yue
- Linghao Zhang
- Hanglong Lv
- Yuanxin Liu
- Wenhan Ma
- Hao Tian
- Rang Li
affiliations:
- Xiaomi LLM Core
- Peking University
- University of Hong Kong
- Renmin University of China
arxiv_id: '2609.22068'
url: https://arxiv.org/abs/2609.22068
pdf_url: https://arxiv.org/pdf/2609.22068
published: '2026-09-17'
collected: '2026-09-21'
category: Agent
direction: Agent 编码RL训练环境自动构建
tags:
- CodingAgent
- RL
- EnvironmentSynthesis
- GRPO
- MultiDomain
one_liner: 仅以源代码为输入自动构建多语言多领域编码RL训练环境，显著提升代码智能体多任务表现
practical_value: '- 做领域Agent（如电商导购Agent、运营工具Agent）训练时，可复用本方法从存量已实现的业务代码、历史执行记录自动生成RL训练任务，自带验证逻辑，无需依赖人工标注/工单记录，大幅降低训练数据构建成本

  - 训练数据过滤范式可直接复用：先做执行一致性校验排除不稳定任务，再用对抗Rollout排查数据泄露，最后过滤全过/全挂的无效任务；实验证明5k高质量过滤后数据效果优于8k未过滤脏数据，任务质量优先级远高于数量

  - RL训练的行为观测指标可迁移：在业务Agent训练中可追踪「上下文探索次数、推理草稿与最终输出重合度、自我验证次数」三个指标，提前预判模型能力提升，无需等待全量评测'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有代码Agent的RL训练任务高度依赖issue、PR、commit、人工编写的测试用例等开发产物，任务覆盖范围受限于上述产物的丰富度，难以规模化生成多语言多领域的高质量训练任务，限制了代码Agent的泛化能力提升。
### 方法关键点
- 仅以源代码为唯一任务输入，通过智能体自动化完成四步环境构建流程：
  1. 任务设计：识别代码库公开可观测功能，删除核心实现生成待完成任务，保留原代码为参考解
  2. 测试构造：执行参考代码生成输入输出对，构造仅校验行为一致性的测试用例，不限制内部实现
  3. 执行校验：验证空代码必失败、参考代码必通过，排查执行不稳定问题
  4. 后过滤：通过对抗Rollout排查信息泄露、审核验证器正误、过滤全过/全挂的无效任务
- 训练采用GRPO算法，奖励直接使用测试用例的二进制执行结果，无需额外训练奖励模型
### 关键结果
构建了覆盖23种编程语言、15个技术领域的5545个高质量训练任务，训练MiMo-V2.5后在5个基准测试上全面提升：DeepSWE pass率+11.7pp，ProgramBench Almost Solved得分+17pp，Terminal-Bench v2.1 pass率+8.5pp；ablation显示5.5k过滤后数据效果优于8k未过滤数据，任务质量优先级高于数量。
### 核心结论
仅从存量已实现的资源即可自动化构造出有效的RL训练环境，高质量训练任务的价值远高于单纯的数量提升

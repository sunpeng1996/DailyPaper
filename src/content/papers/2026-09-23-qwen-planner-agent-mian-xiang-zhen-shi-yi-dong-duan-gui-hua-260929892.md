---
title: 'Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile
  Planner Agents'
title_zh: Qwen-Planner-Agent：面向真实移动端规划Agent的闭环AI-for-AI框架
authors:
- Tingyu Qu
- Weigao Sun
- Yuecheng Liu
- Yucheng Zhao
- Yi Zhu
- Yifeng Ding
- Qiyi Wang
- Sihan Cao
- Pengkun Jiao
- Hanlei Xie
affiliations:
- Alibaba Group
- MAI Team, Alibaba Token Hub
arxiv_id: '2609.29892'
url: https://arxiv.org/abs/2609.29892
pdf_url: https://arxiv.org/pdf/2609.29892
published: '2026-09-23'
collected: '2026-09-25'
category: Agent
direction: Agent 开发框架 · 模型编排协同进化
tags:
- Agent
- LLM
- Closed-Loop
- Reinforcement Learning
- Mobile Agent
one_liner: 提出闭环AI-for-AI开发框架 打造性能超GPT-6 Astra的低成本移动端规划Agent
practical_value: '- 可复用AI驱动的数据飞轮设计：通过Agent自动生成任务、采集交互轨迹，结合模型表现动态下采样已掌握任务、上采样不稳定行为数据，大幅降低Agent训练的人工标注成本

  - 可迁移CARE强化学习训练策略：根据任务组成功率分阶段配置奖励（进度引导→结果巩固→效率优化），搭配质量保留的优势校准机制，兼顾Agent任务完成率和推理成本

  - 可落地模型-Harness协同进化架构：将场景规则、工具依赖、用户记忆等动态配置放在Harness层，无需频繁重训大模型，仅通过Harness迭代+小版本模型更新即可快速适配业务场景变化'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent落地面临长周期任务可靠性差、真实环境交互成本高、传统开发流程人工投入大等痛点，难以规模化迭代。移动端规划作为典型复杂长周期场景，是验证AI全流程参与Agent开发可行性的理想测试场。

### 方法关键点
- 闭环AI-for-AI框架分为3个协同阶段：AI for Data打造人工gated的Agent数据飞轮，自动生成任务、采集交互轨迹，根据模型表现动态调整训练数据采样权重；AI for Training先通过规划导向的监督微调完成冷启动，再用程序沙箱+LLM仿真+真机的混合环境做在线RL，引入CARE（能力感知奖励与优势工程）机制，根据任务组成功率自适应切换奖励策略，在保证效果的前提下降低推理与工具调用成本；AI for Harness实现模型与编排层协同进化，Harness层统一管理技能、持久化记忆、工具路由，线上反馈同时迭代模型和Harness配置。

### 关键结果
在含1700+任务、200+移动端工具、13个领域的MobilePA-Bench上测试：Qwen-Planner-Agent 27B Overall得分77.05%，超过GPT-6 Astra（76.84%）、Claude Opus 5（75.71%）等商用闭源模型，排名第一；推理成本仅2.41美元/千任务，低于所有参测商用LLM；相比基线Qwen 27B，整体性能提升9.83个百分点，工具使用、记忆、技能、子Agent协调能力均大幅提升。

### 核心洞见
Agent迭代不应仅优化模型参数，通过AI驱动的闭环流程协同优化数据、训练策略、编排层，能以更低成本实现更高的落地性能

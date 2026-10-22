---
title: Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures
title_zh: 构建用于自主发现线性注意力架构的AI研究团队
authors:
- Yujian Liu
- Li An
- Zelin He
- Jacob Helwig
- Jiabao Ji
- Rohit Jain
- Siyu Zhu
- Shiyu Chang
affiliations:
- UC Santa Barbara
- Pennsylvania State University
- LinkedIn
arxiv_id: '2610.28887'
url: https://arxiv.org/abs/2610.28887
pdf_url: https://arxiv.org/pdf/2610.28887
published: '2026-10-19'
collected: '2026-10-22'
category: MultiAgent
direction: 多Agent协作 · 架构自动搜索
tags:
- MultiAgent
- Autonomous Research
- Linear Attention
- Architecture Search
- UCB
one_liner: 提出异构背景Agent组成的自主研究框架，发现性能更优的线性注意力架构CFDN
practical_value: '- 搭建业务多Agent协作系统时，可复用「异构背景配置+私有历史记忆+共享知识库」的设计，给不同Agent分配用户增长、营收、体验等差异化业务视角，避免策略探索陷入局部最优

  - 资源有限的实验调度场景（如推荐ABTest配额分配、大模型微调任务调度），可采用带折扣的UCB策略分配机会，平衡新方向探索和优质方向的资源倾斜

  - 多目标优化场景需明确多维度考核标准，单目标（如仅优化点击率）优化的结果泛化性差，电商推荐等场景要避免单一指标导向导致其他业务指标下滑

  - 业务策略迭代可复用「提案-双维度评审-实验-复盘-经验共享」的闭环流程，提升迭代效率和创新产出质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单Agent或固定流程的自主搜索系统易陷入设计空间局部最优，且在实验成本较高的场景下无法高效平衡探索与利用，难以在有限预算下持续产出优质创新成果。
### 方法关键点
- 团队由16名具备不同学科背景（动态系统、贝叶斯滤波、流式算法等）的Agent组成，每个Agent保留私有研究历史，同时所有Agent共享提案、实验结果、经验总结三类公共知识
- 迭代流程：每轮通过带折扣的UCB策略选择1名Agent输出提案，经技术可行性、创新性两轮评审通过后，由独立实现Agent完成代码开发、训练与评估，最后提案Agent复盘更新私有记忆并同步通用经验到公共知识库
- 线性注意力架构搜索采用语言建模、常识推理、检索三类指标加权计算效用，作为Agent奖励和架构优劣的判断标准
### 关键结果
以GDN2为基线，150M参数规模下80轮迭代发现的CFDN架构，检索准确率较GDN2提升3.97pct，语言建模困惑度下降2.41；1.3B规模下CFDN在所有评估任务上均优于GDN2。Ablation实验显示去掉学科背景、私有记忆、自适应分配机制后，最优架构效用分别下降48%、46%、27%。

持续的自主发现不仅依赖更强的单个Agent能力，更取决于探索主体的多样性、记忆机制和资源分配策略。

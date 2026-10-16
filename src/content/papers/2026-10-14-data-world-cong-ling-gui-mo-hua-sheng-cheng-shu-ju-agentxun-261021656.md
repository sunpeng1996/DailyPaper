---
title: 'Data World: Scaling Data Environments from Scratch'
title_zh: Data World：从零规模化生成数据Agent训练与评测环境
authors:
- Zhanli Li
- Zeyuan Xu
- Chaoxu Pang
- Zeyuan Liu
- Anyang Ji
- Te Sun
- Kongcheng Zhang
- Wenbo Xu
- Xubin Yue
- Shipeng Luo
affiliations:
- Nanjing University
- Meituan Longcat Interaction Team
- Zhongnan University of Economics and Law
- Hunan University
- Shanghai Jiao Tong University
arxiv_id: '2610.21656'
url: https://arxiv.org/abs/2610.21656
pdf_url: https://arxiv.org/pdf/2610.21656
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 数据Agent · 合成环境与训练范式
tags:
- DataAgent
- SyntheticEnvironment
- RLforAgents
- Benchmark
- MultiAgent
one_liner: 提出机制优先的多Agent数据环境合成引擎，生成可审计训练任务与评测基准
practical_value: '- 业务数据Agent训练可复用「先定义数据生成机制再生成观测文件」的范式，规避真实数据隐私风险，生成的任务自带可验证rubric，大幅降低人工标注成本

  - 可复用分层生成+独立审计的多Agent协作链路生成业务场景合成数据，比如电商交易、本地生活配送场景的模拟数据，确保数据因果关系可追溯、目标结论可从观测数据恢复

  - 做Agent RL训练时可采用rubric分维度（计算/洞察）奖励机制，无需依赖强模型蒸馏轨迹，仅用自身rollout即可实现能力提升，同时不会损耗基础模型的通用能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前数据Agent训练面临三大核心痛点：真实环境标注成本极高，隐私、IP限制导致真实数据难以复用；真实数据的生成过程未知，开放分析类任务的评估缺乏ground truth，常出现符合数据的正确结论因未被标注而得不到分的情况；现有合成环境的可扩展性和任务可验证性不足，成为Agent能力迭代的核心瓶颈。

### 方法关键点
- 机制优先的生成范式：先定义场景的因果依赖DAG、世界合约（实体、时间线、生成机制、全局约束），再分层生成canonical真实状态，最后投影成带噪声的观测文件（模拟真实业务系统的缺失值、ID不统一、schema漂移等问题）
- 独立审计机制：审计Agent单独验证目标结论是否可从观测文件中恢复，确保生成的任务可解
- 任务与rubric自动生成：基于因果DAG的上下游路径生成原因追溯、结果推演两类任务，rubric区分数据计算和洞察发现两个维度，自动生成的评估标准可直接作为RL奖励
- 无蒸馏RL训练：仅用合成任务的rubric奖励做RL-zero训练，不需要强模型的轨迹蒸馏

### 关键结果
- 生成覆盖16个领域的DataWorld-Bench（100个测试任务）和2135个训练任务
- 10个前沿模型评测显示所有模型都存在计算-洞察gap（4.87~21.35分），最高整体得分仅74.43
- 基于Qwen3.6-35B-A3B做RL-zero训练后，相对base模型在DataWorld-Bench提分7.06，DAComp提14.28，DABstep-Hard提20.90，跨职业的JobBench提12.13，同时通用能力无明显下降

### 核心结论
机制优先的合成环境不仅能解决数据Agent训练的隐私和标注瓶颈，其生成的可验证监督信号还能实现无蒸馏的RL训练，效果可迁移到真实业务场景。

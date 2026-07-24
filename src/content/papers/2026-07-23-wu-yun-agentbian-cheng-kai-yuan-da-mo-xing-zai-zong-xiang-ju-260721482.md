---
title: 'Agentic coding without the cloud: evaluating open-weight large language models
  on longitudinal data preparation tasks'
title_zh: 无云Agent编程：开源大模型在纵向数据准备任务上的性能评估
authors:
- Mack Nixon
- Liam Wright
- Yevgeniya Kovalchuk
- Alison Fang-Wei Wu
- Martin Danka
- Andy Boyd
- David Bann
affiliations:
- University College London
- University of Bristol
- UK Longitudinal Linkage Collaboration
arxiv_id: '2607.21482'
url: https://arxiv.org/abs/2607.21482
pdf_url: https://arxiv.org/pdf/2607.21482
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: 本地部署开源LLM Agent效能评测
tags:
- Local-Deployment
- Open-Weight-LLM
- Agent
- Code-Generation
- Benchmark
one_liner: 提出开源评估框架RRBench，测试消费级硬件可部署开源LLM Agent的数据准备代码生成能力
practical_value: '- 敏感用户数据场景下，可复用本地部署31-35B开源LLM Agent完成代码类数据处理任务，规避数据出境合规风险

  - 可参考其「代码正确性+输出数据一致性」双校验的范式，搭建内部LLM代码生成任务的自动化评测流水线

  - 消费级硬件即可跑通30B级模型的Agent代码任务，中小团队无需高算力集群即可落地轻量数据处理Agent'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
云部署LLM Agent处理敏感数据存在合规限制，涉及个人隐私的研究、业务场景下数据无法传输至外部服务，亟需本地可部署的开源LLM Agent方案，同时缺乏针对纵向数据准备这类高频代码任务的标准化评估体系。

### 方法关键点
1. 开源RRBench评估框架，包含英国队列研究6轮数据清洗的真值数据集、类别对齐/多波合并等20类数据准备任务定义、LLM生成R代码及输出数据的自动校验流程
2. 覆盖消费级硬件可部署的全量级开源LLM开展基准测试

### 关键结果数字
31-35B参数量的SOTA开源模型平均任务完成率可达87.9%，接近基准上限，消费级硬件运行开源LLM完成标准化数据准备任务已具备落地可行性

---
title: 'AgentVQA: A Unified Benchmark for Agentic Visual Understanding'
title_zh: AgentVQA：面向智能体视觉理解的统一评测基准
authors:
- Advait Gupta
- Sachin Konan
- Tom Yin
- Gabriel Sarch
- Zhuang Liu
affiliations:
- University of Maryland, College Park
- Princeton University
arxiv_id: '2610.31494'
url: https://arxiv.org/abs/2610.31494
pdf_url: https://arxiv.org/pdf/2610.31494
published: '2026-10-21'
collected: '2026-10-24'
category: Eval
direction: Agent多模态视觉理解统一评测
tags:
- AgentVQA
- VLM
- Visual Understanding
- Benchmark
- Agent Evaluation
one_liner: 构建覆盖5类Agent场景的离线VQA基准，可快速评估VLM的智能体视觉理解能力
practical_value: '- 开发电商多模态导购Agent、自动化UI操作Agent时，可参考本基准的场景设计思路，搭建低成本离线评测集，替代高成本的线上仿真评测

  - 优化多模态交互Agent性能时，优先迭代视觉状态接地、时序状态跟踪、3D空间关系推理模块，收益远高于优化逻辑推理模块

  - 跨场景Agent能力验证可复用其「离线评测模型排名对齐线上排名」的数据集构建逻辑，大幅提升评测有效性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM在Agent场景的性能评估高度依赖高成本、难规模化的线上仿真/真实环境测试，已有的离线VQA基准覆盖Agent场景碎片化，无法支撑快速跨域模型对比。
### 方法关键点
1. 从23个源数据集人工筛选1000个高难度真实Agent样本，覆盖Web Agents、机器人、第一人称视频、游戏、空间规划5大领域，适配离线VQA评测范式
2. 数据集构建过程保证离线评测得到的模型排名与对应线上评测结果高度对齐，评测结果具备可落地参考性
### 关键结果
22款参测VLM的最高准确率仅为58.5%；错误主因是视觉状态接地、时序状态跟踪、3D空间关系推理能力缺陷，而非任务理解或下游逻辑推理不足。

---
title: 'Breaking Diffusion: Parallel Reasoning with Draft Refinement'
title_zh: 破除Diffusion局限：基于草稿迭代优化的并行推理框架
authors:
- Jaesang Yu
- Seoyeon Byun
- Yun Wang
- Yan Lu
- Juho Kim
affiliations:
- KAIST
- Microsoft Research Asia
- SkillBench
arxiv_id: '2610.26542'
url: https://arxiv.org/abs/2610.26542
pdf_url: https://arxiv.org/pdf/2610.26542
published: '2026-10-18'
collected: '2026-10-21'
category: Reasoning
direction: 大语言模型 · 并行推理优化
tags:
- Parallel Reasoning
- Discrete Diffusion
- Draft Refinement
- Energy-based Model
- Non-autoregressive Generation
one_liner: 提出草稿修订语言模型DRLM，单去噪器兼顾并行修订与质量评估，小参数远超自回归/扩散基线
practical_value: '- 生成式推荐（GenRec）场景可复用并行草稿修订逻辑：生成推荐候选列表、营销文案时，先生成完整初始草稿再并行修订，比逐词自回归生成效率更高，还能解决推荐结果上下文矛盾（如搭配不合理、价格冲突）问题，降低后续校验成本

  - 电商Agent、搜索query复杂改写等推理场景可复用propose-read-retain迭代框架：不用堆大模型参数，小模型加多轮迭代即可大幅提升推理准确率，且每轮都可返回当前最优结果，适配低延迟业务的提前终止需求

  - 生成结果评估环节可复用cavity energy单步打分方案：无需额外训练独立评分模型，通过修正生成模型的自token偏好，仅用1次前向pass即可得到全局一致性得分，减少推理链路的模型调用量，降低部署成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
自回归模型生成时提前锁定早期token，无法修正后续出现的上下文逻辑矛盾；离散扩散模型的采样过程受反向过渡调度约束，token修订效率低，且现有并行修订方法缺乏有效的全局一致性评估能力，常出现局部合理的token更新反而破坏整体语义/逻辑的问题，强约束推理任务性能不佳。

### 方法关键点
- 训练阶段：对完整草稿做均匀随机token corruption，采用全位置交叉熵损失训练单去噪器，同时学习正确token的保留和错误token的修复，无需依赖扩散反向过渡链路
- 评估阶段：提出cavity energy修正方案，通过除以已知的自token似然，消除模型对当前草稿token的原生偏好，仅需1次前向pass即可得到基于prompt和全局上下文的一致性得分，无需额外训练独立评分模型
- 推理阶段：采用propose-read-retain迭代流程，每轮对当前最优草稿加噪后并行生成候选，计算候选能量分，仅当得分更低时替换最优草稿，固定预算下返回能量最低的结果

### 关键实验
在Countdown数学推理、Sudoku-Extreme、Maze-Hard三个强约束推理任务上测试，仅6M参数的DRLM对比同规模自回归、离散扩散基线：Countdown-5准确率达44.4%，超最强扩散基线34.1pp；Sudoku-Extreme准确率93.9%，超最强扩散基线28.4pp；Maze-Hard准确率73.0%，超最强扩散基线33.7pp，性能远超13B LLaMA SFT微调模型（Countdown-5准确率仅7.4%）。

### 核心结论
无需依赖大模型参数或复杂扩散调度，基于完整草稿的并行修订加单模型能量评估，即可在强约束推理任务上实现数量级的性能提升。

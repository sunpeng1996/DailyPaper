---
title: 'h1: A Taste of the Bitter Lesson in Automated Theorem Proving'
title_zh: 自动定理证明场景下的AI苦涩一课验证研究
authors:
- Skander Moalla
- Ahmad Rammal
- Niket Patel
- Remi Munos
- Julia Kempe
affiliations:
- FAIR at Meta
- EPFL
- CERMICS, ENPC, Institut Polytechnique de Paris
- New York University
arxiv_id: '2610.35962'
url: https://arxiv.org/abs/2610.35962
pdf_url: https://arxiv.org/pdf/2610.35962
published: '2026-10-24'
collected: '2026-10-29'
category: Agent
direction: Agent 闭环推理优化 · 自动定理证明
tags:
- Agent
- Reasoning
- LLM
- Execution Feedback
- Automated Theorem Proving
one_liner: 提出无预设搜索结构的简单Agent证明框架h1，性能超越专用复杂定理证明工作流
practical_value: '- 搭建业务Agent（如选品Agent、文案审核Agent）时先跑「简单闭环+高效工具反馈」的基线，不要上来就堆叠多层规划、任务分解模块，避免过度设计带来的冗余成本

  - 工具调用接口的效率直接决定Agent任务成功率和成本，对接业务工具（如库存查询、规则校验接口）时优先优化响应速度、返回信息的结构化程度

  - 对比不同工作流方案时必须固定基座模型、算力配额，否则无法区分增益来自工作流优化还是模型/算力投入，避免无效迭代'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前形式化定理证明领域普遍依赖人工设计的复杂规划、任务分解、多工具编排工作流，其效果增益常与更强基座模型、更高算力投入混淆，需要验证AI领域「苦涩一课」（简单可扩展方法最终胜过人设计的复杂流程）是否成立。
### 方法关键点
设计极简Agent框架h1，仅为大模型提供高效Lean 4验证器接口，靠验证器实时反馈+自反思迭代求解，完全不预设任务分解逻辑或搜索结构。
### 关键结果
在PutnamBench、FATE-X、FormalConjectures100-Solved数据集上达到SOTA，解决FormalConjectures中8个公开未解决问题；同基座模型下性能匹配或超越Goedel-Architect、AlphaProof Nexus等专用复杂工作流；ablation实验显示高效Lean接口决定了70%+的求解率与成本差异。

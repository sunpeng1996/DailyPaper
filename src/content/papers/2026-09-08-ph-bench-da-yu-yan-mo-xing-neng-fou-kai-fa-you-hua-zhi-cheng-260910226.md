---
title: 'Φ-Bench: Can Large Language Models Engineer the Infrastructure That Powers
  Them?'
title_zh: Φ-Bench：大语言模型能否开发优化支撑自身运行的基础设施
authors:
- Leilei Ding
- Shumin Wang
- Yuting Huang
- Fanqi Wan
- Yinmin Zhang
- Qi Han
- Yiming Xu
- Feiyuan Zhang
- Xiaomeng Chu
- Guoliang You
affiliations:
- University of Science and Technology of China
- StepFun
- Peking University
- The Hong Kong University of Science and Technology
- Yale University
arxiv_id: '2609.10226'
url: https://arxiv.org/abs/2609.10226
pdf_url: https://arxiv.org/pdf/2609.10226
published: '2026-09-08'
collected: '2026-09-10'
category: Eval
direction: LLM能力评测 · 基础设施工程优化
tags:
- LLM
- Benchmark
- Infrastructure
- Code Generation
- System Optimization
one_liner: 推出首个覆盖LLM基础设施全栈的评测基准Φ-Bench，系统评估LLM开放长周期工程能力
practical_value: '- 若团队需做AI辅助的推荐/LLM推理服务性能优化，可复用Φ-Bench的任务范式设计KV cache优化、MoE路由算子调优等业务场景专项评测，筛选适配工程优化需求的LLM底座

  - 可直接复用Φ-Bench的分层任务设计逻辑（从kernel补全到端到端优化），用于评估自有代码生成Agent的能力，避免仅测孤立简单任务带来的评估偏差

  - 参考论文对当前LLM工程能力边界的结论，合理划分人和LLM的分工：简单算子优化交由LLM完成，长周期复杂系统优化保留人工介入，最大化效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM代码评测基准多聚焦孤立kernel、预定义算子与固定优化目标，无法评估LLM在开放、长周期场景下开发优化自身基础设施的能力，而基础设施优化直接决定LLM训练/推理成本、GPU利用率，产业价值极高。
### 方法关键点
推出Φ-Bench评测集，任务全部来自前沿研究优化问题与真实工业界代码仓库，覆盖LLM基础设施全栈，分层设计三类不同复杂度的任务：1）局部kernel级函数补全；2）模块级功能实现；3）长周期端到端系统优化，可系统性量化LLM的工程能力。
### 关键结果
对当前主流前沿LLM的测试显示，现有模型仅能较好完成简单kernel级任务，在长周期复杂系统优化任务上表现存在显著缺陷，距离实现AI基础设施全自主优化仍存在较大技术差距。

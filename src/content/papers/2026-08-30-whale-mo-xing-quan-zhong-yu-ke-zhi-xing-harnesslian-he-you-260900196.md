---
title: 'WHALE: A Simple Recipe for Joint Harness-Weight Optimization'
title_zh: WHALE：模型权重与可执行Harness联合优化框架
authors:
- Haechan Kim
- Yoonho Lee
- Gisang Lee
- Chelsea Finn
- Kangwook Lee
affiliations:
- KRAFTON
- KAIST
- Stanford University
arxiv_id: '2609.00196'
url: https://arxiv.org/abs/2609.00196
pdf_url: https://arxiv.org/pdf/2609.00196
published: '2026-08-30'
collected: '2026-09-04'
category: Agent
direction: Agent 权重与Harness联合优化
tags:
- LLM Agent
- Harness Optimization
- Joint Optimization
- Alternating Training
- Rejection Sampling SFT
one_liner: 交替更新模型权重与可执行Harness，多领域Agent任务精度大幅领先各类基线
practical_value: '- 优化电商导购/搜索工具类Agent时，放弃先训模型再调工具链的阶段式方案，采用小步交替更新权重与harness的策略，可提升5-9pp精度，同时节省50%以上的rollout成本

  - 新Agent任务上线前，先用少量rollout做harness搜索判断瓶颈：若harness优化即可拿到不错效果，优先调整工具调用逻辑、上下文管理规则，无需急于做全量模型微调，大幅降低研发成本

  - 交替更新的周期无需手动调参，采用自适应patience规则：每个阶段跑够最小长度后，训练信号无提升即切换，比人工调优的固定周期效果更好，还能节省调参成本

  - 工具调用类Agent的联合优化不要只停留在prompt层面，扩展到可执行harness全链路的搜索，相比仅优化prompt的联合方案可提升4-13pp的精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Agent性能由模型权重与管控上下文、工具调用、控制流的可执行harness共同决定，单独优化任一组件都会被另一冻结组件限制瓶颈；现有联合适配方案仅支持优化文本prompt，不覆盖全链路harness，且两者更新周期不匹配，协同优化难度高。

### 方法关键点
- WHALE为交替优化框架，循环执行两个阶段：固定当前harness，通过online rejection-sampling fine-tuning（RSFT）更新模型权重，仅使用验证通过的轨迹做SFT；再固定更新后的模型，通过Meta-Harness迭代搜索更优可执行harness，覆盖prompt、工具调用逻辑、上下文管理、错误处理全链路
- 支持两种阶段切换策略：固定周期调度，或自适应patience规则，每个阶段满足最小运行长度后，训练信号连续多步无提升即切换，无需手动调优周期超参

### 关键结果
基于Qwen3.5-2B/4B模型，在SearchQA、数学推理、国际象棋谜题三个领域测试，对比weight-only、harness-only、仅优化prompt+权重的Fast-Slow Training（FST）基线：WHALE较单组件基线精度高7.67~24.38pp，较FST高4.15~13.00pp；小步交替更新较先全量训模型再全量调harness的阶段式方案精度高5.32~9.16pp，仅用29%~49%的rollout即可达到阶段式方案最终效果；自适应调度较最优手动调参的固定周期在SearchQA上精度再高2.73pp，节省23%的rollout成本。

### 核心结论
Agent系统的模型和harness不是独立的工程产物，应当作为联合系统协同优化，小步交替更新远优于单组件独立优化或阶段式优化。

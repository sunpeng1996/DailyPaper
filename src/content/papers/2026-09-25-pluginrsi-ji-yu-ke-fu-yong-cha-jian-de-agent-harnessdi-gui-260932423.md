---
title: 'PluginRSI: Recursive Improvement of Agent Harnesses with Reusable Plugins'
title_zh: PluginRSI：基于可复用插件的Agent Harness递归优化框架
authors:
- Yaorui Shi
- Yuchun Miao
- Yuxin Chen
- Jiayuan Zhang
- Yueqing Sun
- Xierui Song
- Xiang Wang
- An Zhang
affiliations:
- University of Science and Technology of China
- Meituan
- Wuhan University
- National University of Singapore
arxiv_id: '2609.32423'
url: https://arxiv.org/abs/2609.32423
pdf_url: https://arxiv.org/pdf/2609.32423
published: '2026-09-25'
collected: '2026-10-06'
category: Agent
direction: Agent Harness 递归自优化
tags:
- Agent
- Harness Optimization
- Plugin
- Recursive Self-Improvement
- LLM Agent
one_liner: 提出以插件为核心的Agent Harness递归优化方法，实现机制可复用、跨模型泛化的性能提升
practical_value: '- 可将电商推荐/客服Agent的业务逻辑（用户意图识别、召回规则、排序策略等）拆为标准化接口插件，独立迭代优化，避免整体修改工作流时覆盖有效逻辑

  - 优化Agent工作流可复用两阶段迭代思路：先单插件灰度验证收益，再全局重组工作流，降低迭代风险，同时沉淀可复用的业务组件库

  - 跨LLM部署Agent时，优化后的插件库和工作流可直接迁移，无需针对新模型全量重调，降低大模型切换的适配成本

  - 冷启动新场景Agent时，可复用其他场景沉淀的插件库，迭代收敛速度可提升20%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent Harness递归优化均为整体重写实现，不同机制耦合难以拆分，有效逻辑易被覆盖丢失，无法跨迭代复用，导致优化收敛慢、泛化性差，且需要反复调整全量逻辑，落地成本高。

### 方法关键点
- 将Harness拆分为标准化接口的原子插件+协调工作流，插件按角色、工具、技能、内存四类划分，有效插件沉淀到共享库跨迭代复用
- 每轮优化分两个阶段：1）插件突变：基于执行反馈单独修改单个插件，固定其余逻辑验证收益，收益为正的插件入库；2）Harness重组：从更新后的库中选择插件，调整工作流生成新的候选Harness
- 全程固定底层LLM权重，仅优化Harness层面逻辑，无模型训练成本

### 关键结果
实验覆盖SWE-bench Verified软件工程、Terminal-Bench命令行交互、多领域QA三类任务，对比ReAct、ACE、GEPA、Meta-Harness等基线：
- SWE-bench任务上Held-out分辨率比最优基线Meta-Harness高6~10个百分点
- 优化后的Harness无需额外调整即可迁移到其他LLM，仍保持性能优势
- 复用演化后的插件库，仅需2步迭代即可达到69%的Held-out分辨率，比无复用场景高4个百分点，且所需solver rollout更少，收敛速度更快

最值得记住的结论：Agent迭代的核心是沉淀可复用的原子能力，而非每次整体重写工作流。

---
title: 'RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent'
title_zh: RSIFlow：耦合自适应工作流与进化元代理的递归自改进框架
authors:
- Huan Zhang
- Mingju Chen
- Dongxu Zhou
- Can Lv
- Sen Cui
- Faguo Wu
- Shiji Zhou
affiliations:
- Beihang University
- Tsinghua University
- Beijing Academy of Artificial Intelligence
arxiv_id: '2610.21791'
url: https://arxiv.org/abs/2610.21791
pdf_url: https://arxiv.org/pdf/2610.21791
published: '2026-10-14'
collected: '2026-10-20'
category: Agent
direction: Agent递归自优化 · 元代理进化
tags:
- LLM-Agent
- Recursive-Self-Improvement
- Meta-Agent
- Workflow-Orchestration
- Self-Evolution
one_liner: 提出瓶颈感知的自适应工作流编排与元代理进化耦合的Agent自改进框架，多任务性能超越SOTA
practical_value: '- 电商导购/客服Agent迭代可复用其瓶颈诊断+组件选择逻辑：根据用户反馈/执行错误，动态选择是做LoRA微调、优化Prompt/Harness、还是直接修正输出话术，避免固定迭代流程的资源浪费

  - 可复用其结构化技能蒸馏机制：将每次迭代的成功/失败经验沉淀为带适用条件的可复用技能库，无需每次重新探索优化路径，降低迭代成本

  - 预算受限场景下可参考其Pareto最优的资源分配逻辑：优先将算力投到当前最核心的瓶颈组件，相同预算下可获得更高的性能收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent自改进方法大多采用固定工作流，无法适配随Agent能力提升动态偏移的性能瓶颈，且元代理的编排能力无法随迭代经验进化，导致自改进效率低、无法形成闭环递归优化。

### 方法关键点
- 设计三类组件级改进工作流：Model更新（基于成功轨迹做SFT/RL微调）、Harness更新（定位问题后优化Prompt/规划/工具调用逻辑）、Artifacts更新（固定模型与Harness直接修正输出结果）
- 元代理先基于执行轨迹与环境反馈诊断当前Task Agent的性能瓶颈，动态选择匹配的改进工作流
- 从每次迭代的成败结果中蒸馏出组件专属技能和跨组件通用原则，更新元代理自身的Harness（元代理模型参数固定），形成递归优化闭环

### 关键实验
覆盖代码生成、工具调用、搜索QA三个领域共6个公开基准，采用Qwen3-4B/8B作为Task Agent backbone，对比SFT、GRPO、AFlow、SIA等7类基线，在12组基准-backbone设置中11组领先，相比最强基线平均提升3.11%，4B/8B版本整体性能分别提升6.06%/3.86%，预算-性能表现处于Pareto前沿。

**最值得记住的一句话**：自适应瓶颈感知的工作流编排+经验驱动的元代理进化，能以更低的迭代成本获得更持续的Agent性能提升

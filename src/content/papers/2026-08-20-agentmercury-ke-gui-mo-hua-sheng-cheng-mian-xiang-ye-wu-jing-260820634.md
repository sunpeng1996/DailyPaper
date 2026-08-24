---
title: 'AgentMercury: Your Agent Can Synthesize Verifiable Environments for Business
  Scenarios at scale'
title_zh: AgentMercury：可规模化生成面向业务场景的可验证Agent交互环境
authors:
- Minbyul Jeong
- Chanwoong Yoon
affiliations:
- Meridian Intelligence Global Inc.
- University of Massachusetts Amherst
arxiv_id: '2608.20634'
url: https://arxiv.org/abs/2608.20634
pdf_url: https://arxiv.org/pdf/2608.20634
published: '2026-08-20'
collected: '2026-08-24'
category: Agent
direction: Agent · 业务场景可执行交互环境生成
tags:
- Agent Environment
- Business Scenario
- Reinforcement Learning
- Policy Optimization
- Environment Synthesis
one_liner: 提出可规模化生成业务场景可验证Agent交互环境的框架，大幅提升Agent泛化能力并支持环境自主构建
practical_value: '- 做电商/广告业务Agent训练时，可复用「先从业务场景生成通用可执行环境、再衍生多任务」的范式，避免任务绑定导致的泛化性差问题，降低人工构造训练环境的成本

  - 跨业务场景的Agent训练可参考其RL训练选型思路：小模型用GRPO、大模型用SAO，兼顾训练效率与泛化性，同时引入SQL化可验证约束做deterministic结果校验，避免模型hallucination导致的效果虚高

  - 若需快速生成垂直领域（如电商客服、商家运营）的Agent训练环境，可直接复用其公开的环境构造数据集与PLANET组件，fine-tune后快速生成符合业务流程的可交互环境，成功率最高可达83.3%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent训练环境多为任务中心化，人工构造或围绕预设基准生成，无法适配真实业务中动态演化、多任务自然涌现的工作流，且环境与特定任务强绑定，难以规模化生成符合真实业务复杂度的交互场景，导致训练出的Agent泛化性差。
### 方法关键点
- 核心设计包含PLANET组件，从高层业务场景出发，分步骤实例化包含实体、服务、工具、状态、跨服务可执行不变量的持久化世界，再从同一世界衍生多样化任务与交互轨迹，实现环境与任务解耦
- 内置基于SQL的可执行验证器，将跨服务约束转化为可执行校验条件，支持交互轨迹的确定性打分，避免依赖模型评估的偏差
- 针对不同模型规模适配RL训练策略：小模型采用GRPO多采样相对优化，大模型采用SAO单轮异步优化，兼顾训练效率与泛化性
### 关键实验结果
- 覆盖14个行业（含电商）、50个国家，共生成4783个可执行环境，衍生43300个训练任务
- Qwen3.5-4B经训练后，EnterpriseOps-GYM得分从12.3提升至15.7（+27.6%），AIME26得分从45.9提升至56.0（+22%），跨推理、编码、工具使用等多领域基准均有稳定提升
- 环境自主构造能力：Qwen3.5-35B-A3B经构造轨迹fine-tune后，零样本生成可执行环境的成功率从3.3%提升至83.3%，达到主流闭源API模型水平

有效环境扩容无需围绕基准任务生成孤立实例，提升底层世界的多样性、结构性与真实性，反而能为Agent提供跨任务迁移的通用交互信号。

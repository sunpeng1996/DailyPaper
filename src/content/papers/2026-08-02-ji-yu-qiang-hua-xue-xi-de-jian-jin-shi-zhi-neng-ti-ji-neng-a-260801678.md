---
title: Progressive Agent Skill Generation via Reinforcement Learning
title_zh: 基于强化学习的渐进式智能体技能生成框架Skill-α
authors:
- Junhao Shen
- Zhanqiu Zhang
- Yiwen Guo
- Hong Cheng
affiliations:
- The Chinese University of Hong Kong
- LIGHTSPEED
arxiv_id: '2608.01678'
url: https://arxiv.org/abs/2608.01678
pdf_url: https://arxiv.org/pdf/2608.01678
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: Agent技能生成 · 强化学习优化
tags:
- LLM Agent
- Agent Skill Generation
- GRPO
- Skill Editing
- Reinforcement Learning
one_liner: 提出带回滚奖励的强化学习框架 统一跨异构证据源的Agent技能自动生成
practical_value: '- 技能生成场景可复用回滚奖励设计：对比技能修改前后同一锚定query的执行效果，解决技能质量无直接监督信号的问题，适合电商Agent导购、客服流程优化等场景的技能迭代

  - 渐进式技能编辑范式可迁移：把技能生成拆解为增/改/合并/剪枝/无操作5类原子动作，避免一次性生成长技能的上下文溢出和信用分配问题，可用于生成电商运营SOP、推荐策略规则等结构化知识

  - 训练阶段可参考GRPO优化小样本策略：用小参数模型（8B）做技能编辑器，下游Worker用大模型不动，训练成本低，适合业务侧快速迭代专属技能库，无需重训大模型

  - 证据粒度调优经验可复用：每步输入4个左右证据单元效果最优，避免单条证据过拟合、多条证据信息过载，适合从用户反馈、运营规则、历史对话等多源数据提炼技能时的参数调优'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能生成多依赖启发式规则或定制化pipeline，需针对不同证据源（文档/经验）单独设计，且技能质量缺乏直接监督信号，只能通过下游任务效果间接衡量，信用分配困难，无法形成统一的学习框架。

### 方法关键点
- 把技能生成拆解为渐进式局部编辑序列，定义5种原子动作：CREATE（新增规则）、UPDATE（修正规则）、MERGE（合并冗余）、PRUNE（删除无效内容）、NOOP（无操作），逐段处理输入证据更新技能
- 提出rollback reward作为监督信号：每次编辑后，用原技能和修改后的技能在同一锚定query上执行，对比执行效果给编辑动作打分，解决信用分配问题
- 训练采用GRPO优化技能编辑策略：先基于Qwen3-8B做SFT暖身学习编辑语法，再用回滚奖励做RL优化，下游Worker模型固定不动，仅训练编辑策略

### 关键实验
在CL-Bench（文档转技能）、tau2-bench、SpreadsheetBench（经验转技能）上测试，Worker用GPT-4o时，Skill-α比最强基线在CL-Bench高3.3个百分点，在tau2-bench高6.7个百分点，生成的技能可跨模型迁移到Claude-Sonnet-4.5仍有明显增益；ablation验证rollback reward和完整编辑空间是效果提升的核心来源，每步输入4个证据单元时效果最优。

### 核心结论
技能的价值不取决于文本通顺度，而取决于其对下游Agent执行效果的提升，基于执行反馈的局部编辑优化比一次性生成更可靠。

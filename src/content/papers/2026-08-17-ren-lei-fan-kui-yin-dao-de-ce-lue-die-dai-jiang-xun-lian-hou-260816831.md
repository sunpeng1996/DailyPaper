---
title: 'Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context
  Learning'
title_zh: 人类反馈引导的策略迭代：将训练后RL引入上下文学习范式
authors:
- Minh-Ha Nguyen
- Cathy Shyr
affiliations:
- Vanderbilt University
- Vanderbilt University Medical Center
arxiv_id: '2608.16831'
url: https://arxiv.org/abs/2608.16831
pdf_url: https://arxiv.org/pdf/2608.16831
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: Agent 上下文学习策略迭代优化
tags:
- Policy Iteration
- Human Feedback
- In-context Learning
- RLHF
- Frozen LLM
- Agent
one_liner: 提出PIHF框架，冻结LLM权重，迭代优化自然语言策略与工具集实现任务性能提升
practical_value: '- 可复用「冻结大模型权重+迭代优化外部自然语言策略」范式，降低推荐/营销Agent调优成本，无需反复做LoRA微调

  - 借鉴过程+结果双校验准入机制：先通过LLM critic定位Agent推理/工具调用错误点修改策略，再用业务指标（点击率、转化率）做回归校验后上线，降低bad
  case风险

  - 稀缺业务专家反馈场景（如奢侈品导购、健康推荐）可复用专家审核+版本回滚机制，把专家经验沉淀为可复用策略资产，支持跨模型迁移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RLHF类方法需微调LLM权重，调优成本高、迭代慢，且上下文学习的能力无法通过外部策略做可解释的持续优化，尤其在稀缺专家反馈场景下，亟需无需修改模型权重、可解释、易迭代的优化范式。

### 方法关键点
- 将策略表示为独立于LLM的可版本化自然语言政策$P_t$与工具集$T_t$，冻结执行LLM的所有权重，所有优化都在外部策略层进行
- 迭代流程：当前策略在开发集跑完所有case生成完整轨迹，用LLM critic定位推理/工具调用的重复错误点，生成修改提案
- 双准入校验：候选策略需同时满足①Recall@1/Recall@5不低于旧策略；②专家审核确认策略合理、解决泛化性问题，否则回滚到上一版本

### 关键实验
实验覆盖3B~49B参数的4个主流模型（包括GPT-5.4、Qwen3.6-35B），在罕见病诊断公开基准数据集上对比原生无策略LLM：GPT-5.4的Recall@1提升32.7个百分点，Qwen3.6-35B提升31.1个百分点，跨模型效果差异仅1.7个百分点，策略迁移性极强。

### 核心结论
不需要微调LLM权重，仅通过迭代优化外部自然语言策略即可接近全参数微调RLHF的效果，且策略可解释、可复用、易回滚。

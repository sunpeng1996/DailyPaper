---
title: 'Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?'
title_zh: 大语言模型对外部指导的选择性依赖能力研究
authors:
- Minghan Wang
- Boyuan Wang
- Jinhang Zuo
- Yuxin Tao
- Fang kong
affiliations:
- Southern University of Science and Technology
- City University of Hong Kong
arxiv_id: '2609.39578'
url: https://arxiv.org/abs/2609.39578
pdf_url: https://arxiv.org/pdf/2609.39578
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent 外部指导选择性依赖优化
tags:
- Agent
- LLM
- Guidance Robustness
- Benchmark
- SFT
- Reinforcement Learning
one_liner: 提出Box2-Bench评估框架与训练策略，让LLM可选择性使用外部指导而非盲从
practical_value: '- 电商导购Agent可复用反事实SFT+RL训练范式：先喂错误推荐路径的SFT数据教模型不盲从预设流程，再用最终转化奖励RL调优，既保留有效流程增益又避免错误流程坑用户

  - 推荐系统RAG召回校验可借鉴选择性依赖思路：对召回的候选物料/用户标签不直接复用，增加一致性校验环节，可靠信息用、错误信息忽略，提升推荐鲁棒性

  - 多智能体客服协作场景可直接复用迁移结论：经选择性依赖训练的Agent对同伴输出的修正率提升，能减少错误回复率，无需额外做跨Agent纠错训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent普遍依赖预设工作流/外部指导提升执行效果，但当指导不可靠时会严重拖累性能，现有基准仅测试任务完成度或流程遵从性，无法评估模型「有用指导就用、错误指导就拒」的选择性依赖能力，是Agent落地的核心鲁棒性缺口。

### 方法关键点
- 构建Box2-Bench评估基准：固定任务、模型、环境，仅变更工作流可靠性，设置无工作流、全好、全坏、前缀好后缀无、前缀好后缀坏5种匹配条件，隔离工作流可靠性对性能的影响
- 训练分两步：第一步反事实SFT，给模型喂错误工作流+正确执行轨迹，教模型无视错误指导完成任务；第二步基于任务结果的RL，仅用最终成功奖励优化，恢复模型对有效指导的使用意愿，避免全拒所有指导
- 训练仅用错误工作流数据，好工作流留作测试，同时验证能力是否可迁移到多Agent协作、记忆增强推理场景

### 关键实验
在数学推理(AIME2026)、电商搜索(WebShop)等任务上测试，反事实SFT可将错误工作流带来的性能损失从20个点降到6.7个点，叠加RL后可恢复6.7个点的好工作流增益；该能力可迁移到多Agent场景，将同伴修正的正收益从2次修复/2次错误提升到11次修复/1次错误。

### 核心结论
Agent的鲁棒性不止看单任务完成度，更要看对外部信息的选择性依赖能力——有用就用、错了就拒，才是落地场景下可靠Agent的核心特质。

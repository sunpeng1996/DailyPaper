---
title: Harness-Model Collaboration for Long-Horizon Continual Learning
title_zh: 面向长时序持续学习的外部记忆-模型协同框架HaMo
authors:
- Zhen Bi
- Zhizhi Peng
- Yan Wang
- Xueshu Chen
- Haofei Zhang
- Yaobo Zhang
- Zeyu Yang
- Qing Shen
- Jungang Lou
affiliations:
- 湖州师范学院
- 阿里巴巴集团
- 浙江大学
- 宁夏大学
arxiv_id: '2610.34724'
url: https://arxiv.org/abs/2610.34724
pdf_url: https://arxiv.org/pdf/2610.34724
published: '2026-10-25'
collected: '2026-10-28'
category: Agent
direction: 长时序Agent · 持续学习双轨优化
tags:
- Continual Learning
- LLM Agent
- Long-Horizon Task
- LoRA
- Memory Retrieval
one_liner: 提出外部记忆与参数适配协同的双轨框架，解决长时序Agent持续学习的遗忘与性能平衡问题
practical_value: '- 电商导购/购物决策Agent可直接复用双轨架构：高频通用购物策略存外部经验卡实现零训练复用，低频共性策略蒸馏进LoRA适配，平衡响应效率与泛化能力

  - 基于检索覆盖度的训练样本筛选trick可直接落地：从业务交互轨迹中选互补代表性样本更新LoRA，大幅降低持续训练冗余，缓解灾难性遗忘

  - 经验条件训练范式可迁移至多场景推荐Agent：仅维护单份LoRA即可适配搜索、导购、售后等多场景，无需为每个场景单独训练模型，降低工程维护成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时序Agent（尤其是电商Web Agent）反复执行多步任务时会产生大量可复用流程知识，但现有方案存在明显缺陷：纯参数更新方案训练成本高、易发生灾难性遗忘；纯外部记忆方案只能做硬匹配，无法将经验泛化到新场景，两者都无法平衡知识复用效率、泛化能力与旧知识保留度。

### 方法关键点
- 双轨协同架构：harness层将每条交互轨迹蒸馏为包含任务上下文、初始条件、策略大纲的经验卡，存入非参数外部记忆，新经验无需训练即可立即复用
- 模型层仅更新单份LoRA适配器，采用经验条件训练目标，训练模型学习根据检索到的策略卡适配当前场景生成动作，而非直接记忆固定动作序列
- 基于检索覆盖度的贪心选样机制，筛选兼具代表性与互补性的轨迹作为锚点样本参与训练，大幅降低训练数据冗余
- 搭配历史轨迹回放机制缓解遗忘，全程冻结LLM主干参数，训练成本可控

### 关键结果
在ScienceWorld、ALFWorld、WebShop三个基准上测试，对比Base、Base+Harness、AgentTuning、ETO等基线：
- 跨域场景（训练顺序S→A→W）下HaMo在三个域得分分别为52.43、66.79、59.64，比各域最强非HaMo基线分别高13.02、19.71、5.16分
- 旧域性能几乎无下降，训练完成后首个学习域的性能仅比训练后立即测试的峰值低1.76分，远低于基线的遗忘幅度

### 核心结论
长时序Agent持续学习需平衡「快速复用的外部经验存储」与「渐进内化的参数适配能力」，两者协同才能同时兼顾新任务适配与旧知识保留。

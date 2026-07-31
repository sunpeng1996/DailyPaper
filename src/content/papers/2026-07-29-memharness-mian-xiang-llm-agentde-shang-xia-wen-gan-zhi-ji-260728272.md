---
title: 'MemHarness: Memory Is Reconstructed, Not Replayed'
title_zh: MemHarness：面向LLM Agent的上下文感知记忆重构框架
authors:
- Rong Wu
- Daocheng Fu
- Licheng Wen
- Xuemeng Yang
- Shu Zou
- Jianbiao Mei
- Yuxin Wang
- Hairong Zhang
- Yu Yang
- Tao Hu
affiliations:
- Zhejiang University
- Shanghai Artificial Intelligence Laboratory
- Fudan University
- Shanghai Jiao Tong University
- University of Science and Technology of China
arxiv_id: '2607.28272'
url: https://arxiv.org/abs/2607.28272
pdf_url: https://arxiv.org/pdf/2607.28272
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: LLM Agent 记忆增强优化
tags:
- LLM Agent
- Memory Augmentation
- GRPO
- Sequential Decision Making
- OOD Robustness
one_liner: 提出基于GRPO端到端训练的记忆重构范式，替代静态回放提升LLM Agent决策性能
practical_value: '- 电商导购/搜索Agent可复用记忆重构范式：召回用户历史行为/运营经验后，新增状态对齐校验环节，避免直接复用历史策略导致的场景错配，比如大促/日常场景下的推荐策略自适应调整

  - 工程上可复用GRPO训练记忆适配能力：无需额外标注记忆重构的ground truth，仅用业务最终reward（如下单成功、搜索目标达成）即可端到端优化记忆适配策略，降低标注成本

  - 记忆库设计可参考：存储记忆时同时保留经验原文+产生该经验的原始场景状态，召回时基于当前状态做适用性校验，无效记忆直接返回空fallback到自主推理，避免负迁移

  - OOD场景优化可复用：当业务环境发生变化（如新品类上线、用户特征迁移），动态重构的记忆比静态回放记忆的鲁棒性更高，可降低分布漂移带来的效果衰减'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有记忆增强Agent普遍采用检索后直接回放的范式，忽略了记忆产生的历史场景和当前决策场景的差异，容易导致负迁移；而参数化记忆虽然自适应，但可解释性差、难以干预追溯，两者之间存在未填补的空白：如何保留显式记忆可追溯性的同时实现动态场景适配。

### 方法关键点
- 框架分为3个阶段：记忆检索（基于当前状态从显式记忆库召回top3相关经验，每条经验同时存储策略内容和产生该策略的原始场景状态）、上下文感知记忆重构（统一策略对比记忆原始场景和当前场景，对记忆进行保留/修改/丢弃，不适用则返回`<EMPTY>` fallback到自主推理）、动作生成（基于重构后的记忆生成执行动作）
- 训练采用GRPO端到端优化，无需记忆重构的标注数据，仅用任务最终奖励+少量格式奖励联合优化，重构过程作为隐变量和动作生成共享参数
- 记忆库采用动态更新机制：自动从成功/失败轨迹中蒸馏记忆，嵌入去重、效用评分、低效用记忆pruning策略，避免记忆冗余

### 关键实验
在ALFWorld（ embodied交互任务）和WebShop（电商导购模拟任务）上测试，对比10+基线包括GPT-4o、Gemini-2.5-Pro、纯GRPO、静态记忆增强GRPO等，7B参数的MemHarness在ALFWorld上成功率85.2%，比纯GRPO高8.8%，比Gemini-2.5-Pro高23.1%；WebShop上成功率75.6%，比纯GRPO高9.5%，比Gemini-2.5-Pro高39.7%；OOD场景下ALFWorld成功率85.9%，比静态记忆回放基线高9.6%。

### 核心结论
记忆的价值不是原样回放，而是基于当前场景重构适配后的可落地指导。

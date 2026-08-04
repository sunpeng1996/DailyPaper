---
title: Self-Improving Large Language Models via Progressive Experience Evolution
title_zh: 基于渐进式经验演化的大语言模型自提升框架
authors:
- Shijie Ren
- Xiting Wang
- Meng Li
- Yujie Guo
- Yunhang Yao
- Ziheng Peng
- Xunlong Wang
- Yuetan Chen
- Haoyang Zhou
- Yunlong Liang
affiliations:
- 中国人民大学高瓴人工智能学院
- 腾讯微信AI
arxiv_id: '2608.02139'
url: https://arxiv.org/abs/2608.02139
pdf_url: https://arxiv.org/pdf/2608.02139
published: '2026-08-03'
collected: '2026-08-04'
category: Training
direction: 大模型自提升 · 经验蒸馏与RL结合
tags:
- Self-Improvement
- Experience-Distillation
- GRPO
- On-Policy-Distillation
- Reinforcement-Learning
one_liner: 提出融合渐进式经验演化与RL的统一自提升框架SPEE，将交互经验转化为持久模型能力
practical_value: '- Agent 交互经验沉淀可复用该框架：从用户交互的成功/失败轨迹中抽取通用策略（如推荐话术、搜索Query改写规则）存入全局经验池，通过蒸馏内化到模型，比纯RL迭代效率高28%

  - 推荐/广告场景的RL优化可前置经验蒸馏阶段：先蒸馏已验证的排序策略、转化话术经验，再用GRPO优化，能降低RL冷启动难度，减少无效探索

  - 经验池的迭代筛选机制可直接复用：对抽取的策略做效用验证，仅保留能提升业务指标的经验，避免模型学习到个案偏置或错误模式'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大模型自提升范式割裂：测试期方法可显式提取经验但无法内化到模型参数，受上下文长度、检索精度限制；训练期RL方法可更新参数但仅通过稀疏奖励信号间接吸收轨迹经验，探索效率低、对初始模型质量敏感，缺失的经验蒸馏中间环节导致自提升效果受限，还容易出现事后合理化问题。

### 方法关键点
- 双阶段统一框架SPEE：第一阶段显式经验演化，第二阶段隐式策略优化，形成「经验积累→模型提升→更优质经验生成」的自增强闭环
- 全局动态经验池：从多轮交互的成功/失败轨迹中抽取可迁移经验（如通用推理策略、任务约束、高频失败模式），经合并去重、双阶段效用验证后迭代更新，过滤低价值经验，避免个案偏置
- 特权引导的On-Policy自蒸馏（OPSD）：教师分支接入经验池作为训练期特权信息，学生分支仅可见原始任务，通过反向KL散度对齐分布，将经验内化到模型参数
- GRPO策略优化：基于蒸馏后的初始化策略做奖励驱动探索，进一步挖掘超出现有经验池的高性能行为，提升能力上限

### 关键实验
在AIME24/25、GSM8K、MATH500、MinervaMath共5个数学推理基准上测试，对比Base、Domain Prompt、GRPO、SDPO 4个基线，覆盖Qwen3-1.7B/4B/8B三个模型尺寸：比Base模型最高提升6.96%，比纯GRPO平均提升1.16%，相同性能下训练数据量比GRPO少28%。

### 核心结论
自提升的核心不是暴力RL探索，而是先将瞬态交互经验转化为可复用的结构化知识，再内化到模型中，可同时提升训练效率和性能上限。

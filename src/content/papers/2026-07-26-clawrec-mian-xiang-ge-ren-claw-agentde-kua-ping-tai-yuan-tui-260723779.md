---
title: 'ClawRec: A Claw-Native Recommender System'
title_zh: ClawRec：面向个人Claw Agent的跨平台原生推荐系统
authors:
- Chenghao Wu
- Kesha Ou
- Xiaolei Wang
- Bowen Zheng
- Bingqian Li
- Enze Liu
- Wayne Xin Zhao
- Weitao Li
- Long Zhang
- Sheng Chen
affiliations:
- Renmin University of China
- Meituan
arxiv_id: '2607.23779'
url: https://arxiv.org/abs/2607.23779
pdf_url: https://arxiv.org/pdf/2607.23779
published: '2026-07-26'
collected: '2026-07-28'
category: Agent
direction: Agent 跨平台个性化推荐系统设计
tags:
- Cross-platform Recommendation
- Personal Agent
- User State Modeling
- Complementary Curation
- Recommendation Benchmark
one_liner: 首个面向Claw个人Agent的跨平台推荐系统，基于跨源行为建模输出互补推荐集合
practical_value: '- 跨平台用户行为建模可复用「统一事件标准化+证据链关联+时间状态生命周期管理」方案，避免直接拼接碎片化行为喂给LLM，提升用户意图推断准确率，适配多端多源数据融合场景

  - 多源候选排序可借鉴「按功能角色划分召回源+边际效用选品」思路，替代纯相关性排序，减少推荐冗余，适合电商互补品推荐、搜索多源结果整合等场景

  - 跨端推荐评估可参考ClawRec-SimBench的「基于用户生命周期事件生成跨平台行为轨迹」的构造方法，解决真实跨平台用户数据难获取、评估难对齐的问题'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统均局限于单平台边界内，仅能观测到用户碎片化的局部行为痕迹，无法覆盖用户跨平台搜索、内容消费、对比决策的完整任务链路，推荐候选池也被限制在单平台范围内，无法匹配用户真实需求。随着Claw类可访问授权跨平台上下文的个人Agent普及，亟需适配Agent生态的原生推荐范式，围绕用户完整任务而非平台边界做推荐。

### 方法关键点
- 统一事件构造：将跨平台异构行为（搜索、浏览、对比等）标准化为带来源、语义、置信度、证据链的统一事件，保留可追溯性
- 用户状态推理：拆分状态为任务槽、偏好槽、来源角色槽三类，按「活跃/冷却/过期/抑制」生命周期动态管理，精准区分当前任务、长期偏好、过时噪声信号
- 角色感知规划：基于当前任务匹配对应功能的召回源（如经验类找社区、权威信息找官方站点），同时支持基于历史行为动态扩展可信来源池
- 边际效用选品：先评估单候选的相关性、角色匹配度，再基于已选候选的增量价值选品，输出无冗余、功能互补的推荐集合

### 关键实验
基于自建的ClawRec-SimBench benchmark（含109个模拟用户、545个生命周期事件、166个来源），对比非LLM方法、直接LLM推理、三类Agent基线，ClawRec NDCG@20达0.6134，较最强基线提升0.1126；Hit@20达0.6944，较最强基线提升0.0854，用户状态一致性得分也为所有方法最高。

最值得记住的一句话：推荐系统可以跳出单平台边界，围绕用户完整任务而非平台利益做跨源互补推荐，个人Agent是该范式落地的核心载体。

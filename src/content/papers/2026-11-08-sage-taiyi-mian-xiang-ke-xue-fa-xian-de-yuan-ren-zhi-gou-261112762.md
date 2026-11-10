---
title: 'Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery'
title_zh: Sage-Taiyi：面向科学发现的元认知Agent架构
authors:
- Weida Wang
- Benteng Chen
- Yigeng Jiang
- Shuchen Pu
- Weiping Shen
- Zichao Liu
- Yulin Su
- Zitong Wang
- Siyu Zhou
- Zifu Wang
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2611.12762'
url: https://arxiv.org/abs/2611.12762
pdf_url: https://arxiv.org/pdf/2611.12762
published: '2026-11-08'
collected: '2026-11-10'
category: Agent
direction: 科学发现Agent · 元认知调控
tags:
- Agent
- Metacognition
- Scientific Discovery
- Benchmark
- Architecture
one_liner: 提出元认知双层级Agent架构，在科学创意基准全面超越SOTA，支持真实科研落地
practical_value: '- 可复用双层级元认知Agent架构：将任务执行（对象层）和路径调控（元层）解耦，可迁移到推荐系统的召回排序链路迭代、电商创意文案生成等需要动态调整策略的场景，避免重复踩无效路径，提升探索效率

  - Target Tree + Idea Graph的结构化信息沉淀方式：可用于电商推荐的用户需求拆解、多召回路径的效果溯源与组合优化，记录每个策略的假设、适用边界、效果证据，降低策略迭代的信息损耗

  - 通用算子库+动态选择机制：可抽象电商/推荐场景下的通用算子（如用户画像建模、冷启动策略、归因方法），元层根据当前任务状态自动选择适配算子，减少人工调参的重复劳动'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有科学Agent仅依赖单轮反馈迭代，无法沉淀跨探索分支的经验、假设与适用边界，容易重复犯错或在无效路径上浪费资源，缺少对整体探索过程的全局调控能力，无法高效适配跨学科的复杂科研任务。
### 方法关键点
- 双层级架构设计：对象层负责具体科研任务执行，通过Target Tree拆解研究目标、Idea Graph记录创意演化路径、Evidence State沉淀实验/文献/专家反馈；元层负责全局调控，维护Cognitive State记录当前任务的全局认知状态，Cognitive Repertoire存储通用及领域适配的方法论启发式与认知算子
- 监控-控制闭环机制：监控模块从对象层执行结果中更新元层认知状态，控制模块基于认知状态从方法库中选择适配的启发式与算子，动态调整对象层的探索方向、主动终止无效分支
- 可扩展方法库机制：通用方法库可通过领域文献实例化适配不同学科，任务执行的成功/失败反馈可迭代优化方法库的适用边界与执行效果
### 关键结果
- 自建Taiyi-Bench基准，覆盖10个学科、50篇论文、265个任务，对比10个基线（含GPT-5.6-Sol、AI Scientist-v2等），Sage-Taiyi在全部8项指标上排名第一，总体得分54.0，比SOTA基线AI Scientist-v2高6.1分，ELO评分1322.5，对AI Scientist-v2的胜率达66.3%，平均生成时间29.9分钟，比AI Scientist-v2快24%
- 真实科研落地案例中，钴催化羰基化反应产率从痕量提升至84%，光催化烯丙基胺化产率从13%提升至69%，在超材料、合金设计、压缩机工程3个领域也验证了落地效果
### 核心结论
将元认知的监控调控能力引入Agent架构，让Agent不仅会执行任务，还能动态反思调整探索策略，是大幅提升复杂任务执行效率与效果的核心路径。

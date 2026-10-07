---
title: 'ShanLiangRen: A Nutrition Agent for Personalized Daily Meal Planning'
title_zh: 《ShanLiangRen：面向个性化每日膳食规划的营养智能体》
authors:
- Miao Xie
- Xiao Zhang
- Yuan Wang
- Ruixin Zhu
- Chunli Lv
affiliations:
- College of Information and Electrical Engineering, China Agricultural University
- Key Laboratory of Precision Nutrition and Food Quality, China Agricultural University
arxiv_id: '2610.07886'
url: https://arxiv.org/abs/2610.07886
pdf_url: https://arxiv.org/pdf/2610.07886
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: 垂直领域Agent · 约束感知个性化规划
tags:
- Agent
- RAG
- Multi-Objective Optimization
- Personalized Recommendation
- Constrained Generation
one_liner: 基于精确RAG与帕累托优化的营养Agent，生成完全满足个性化约束的可量化膳食方案
practical_value: '- 多约束个性化推荐场景可复用「精确RAG先缩可行域+LLM后生成优化」的架构，避免LLM幻觉导致硬约束违反，可直接迁移到电商定制化礼盒、健康/医药类合规推荐等场景

  - 帕累托引导的迭代优化流程可复用至多目标推荐任务：用确定性规则计算各目标偏差，让LLM做最小修改调优，平衡用户偏好满足与核心业务指标

  - 结构化知识库+确定性验证模块的设计，可解决生成式推荐结果的可解释、可核验问题，适合对合规性要求高的推荐场景

  - 用户交互层面可参考「静态属性结构化收集+动态需求自然语言输入」的模式，既降低交互门槛又避免对话漂移，适合垂直领域Agent产品'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有膳食规划要么无法适配用户动态变化的个性化约束（过敏、口味、餐食结构等），要么生成的方案缺乏量化参数、营养指标不符合官方指南，通用LLM直接生成的方案常出现硬约束违反、营养数据幻觉，无法落地为可执行的日常配餐方案。

### 方法关键点
- 抽象出全量化多目标膳食规划问题，明确两类硬约束（用户个性化约束、官方膳食指南结构约束），以营养指标落在推荐区间的总偏差最小为优化目标
- 精确RAG模块：先基于硬约束过滤食材/菜谱库，再将餐食结构、品类覆盖要求抽象为查询子图，在知识图谱上做精确匹配缩小可行候选集，从根源避免LLM生成违反硬约束的内容
- 帕累托引导的迭代优化：基于结构化营养成分表做确定性营养计算，将偏差反馈给LLM做最小修改，保留帕累托最优解，迭代至优化收敛
- 后端知识库覆盖155万+菜谱、6.4万+食材，每类食材标注64维营养属性，输出全量化食材分量、营养达标报告的可执行方案

### 关键实验
在300个覆盖不同个性化需求的配餐实例上，对比GPT-5.4、Gemini-3、Doubao-seed 2.0三个基线：ShanLiangRen的个性化硬约束满足率（PCS）100%、方案完整率（EPC）100%，营养指标达标率（NIA）78.9%，平均营养偏差（AND）0.09，四项核心指标均显著优于基线，仅端到端延迟61s略高于基线，符合日常配餐场景的延迟容忍度。

### 核心结论
垂直领域生成式规划类Agent，先通过结构化检索把可行域缩小到完全满足硬约束的范围再做生成优化，效果远好于直接靠prompt约束LLM。

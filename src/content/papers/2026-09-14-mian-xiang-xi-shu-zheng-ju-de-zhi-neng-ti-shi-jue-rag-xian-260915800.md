---
title: 'Navigating Sparse Evidence: Agentic Visual RAG via Explicit Context Selection
  and Consolidation'
title_zh: 面向稀疏证据的智能体视觉RAG：显式上下文选择与整合框架
authors:
- Yucheng Shen
- Lingyong Yan
- Jiulong Wu
- Shuaiqiang Wang
- Jianmin WU
- Dawei Yin
- Min Cao
affiliations:
- Soochow University
- Baidu Inc.
arxiv_id: '2609.15800'
url: https://arxiv.org/abs/2609.15800
pdf_url: https://arxiv.org/pdf/2609.15800
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: 智能体视觉RAG · 证据选择与整合
tags:
- VRAG
- Agent
- ReinforcementLearning
- EvidenceOrganization
- ContextManagement
one_liner: 提出SCORE统一智能体框架，显式选择整合视觉证据，解决VRAG证据稀疏与组织混乱问题
practical_value: '- 电商图文问答（如商品参数查询、商家手册答疑）场景可复用架构：探索阶段用文本台账存相关证据+原始资源指针，回答前重载原始资源整理排序，既控制上下文长度，又避免文本蒸馏损失

  - 训练智能体RAG时可采用「冷启动蒸馏高覆盖轨迹+证据感知RL奖励」范式，奖励同时兼顾证据召回率、精准度、答案正确率，比仅用答案正确率监督效果更好

  - 多轮多模态智能体可采用「固定滑动窗口保留最近交互+持久化文本台账存核心历史信息」的上下文构造方式，显著降低视觉token消耗，提升推理效率

  - 处理小区域稀疏证据场景（如从商品详情图角落取参数、长文档取分散指标），可复用bbox局部放大工具，降低整页高分辨率带来的token开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
VRAG处理图文混排文档时存在两大痛点：一是答案相关证据稀疏，可能仅占单页小区域或分散在多页；二是现有智能体方法直接基于探索轨迹或压缩文本记忆生成答案，易受噪声干扰且证据溯源性差，仅优化检索召回无法根本解决问题。

### 方法关键点
- 统一智能体循环：探索阶段每步输出观察摘要、相关性判断、动作，仅将相关观察及对应原始图像/区域指针存入文本证据台账，原始视觉上下文仅保留最近2轮，大幅控制token开销
- 新增`consolidate`终止动作：探索结束后重载台账引用的原始图像，筛选、重排为逻辑证据链后再生成答案，实现探索过程与最终推理解耦，保留回答到原始图像的溯源链路
- 两阶段训练范式：冷启动阶段蒸馏强教师生成的高覆盖（金标页全召回+答案正确）轨迹做SFT；RL阶段采用证据感知奖励，同时优化金标页覆盖率、证据链紧凑度、答案正确率

### 关键实验
在SlideVQA、ViDoSeek、MMLongBench三个VRAG基准测试，对比EVisRAG、VISOR、VRAG-RL等基线，7B Qwen2.5-VL backbone下，SlideVQA整体准确率77.16%（较SOTA VISOR提升4.79pp），ViDoSeek准确率75.31%（提升0.44pp），MMLongBench准确率31.52%（提升3.07pp），3B backbone下也取得一致SOTA效果。

> 最值得记住：稀疏证据场景下，主动选择和组织证据，而非单纯提升检索召回量，是提升RAG回答准确率的核心

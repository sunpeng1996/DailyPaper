---
title: 'SCoRD: Semantic-Assisted Continual Retriever-Reranker Distillation for LLM-Based
  Recommendation'
title_zh: 面向LLM推荐的语义辅助持续召回-重排蒸馏框架SCoRD
authors:
- Seunghyun Baek
- Gyuseok Lee
- Seunghan Lee
- Wonbin Kweon
- Dong Wang
- SeongKu Kang
affiliations:
- Korea University
- University of Illinois at Urbana-Champaign
- Sungkyunkwan University
arxiv_id: '2608.19998'
url: https://arxiv.org/abs/2608.19998
pdf_url: https://arxiv.org/pdf/2608.19998
published: '2026-08-20'
collected: '2026-08-21'
category: RecSys
direction: LLM推荐 · 召回重排持续蒸馏
tags:
- Knowledge Distillation
- Retrieval-Rerank
- Continual Learning
- LLM4Rec
- Semantic Intent
one_liner: 通过轻量语义推理助理实现LLM重排器与ID召回器的低成本异步持续共适配
practical_value: '- 可借鉴低置信度硬序列筛选机制：仅对召回效果差的20%用户序列做LLM蒸馏即可覆盖大部分增益，大幅降低LLM调用成本，适合大流量电商推荐场景

  - 可复用动态意图记忆+轻量语义助理设计：离线把LLM的用户意图推理能力蒸馏为可复用模块，无需高频调用LLM即可给召回提供语义信号，优化新用户冷启动效果

  - 可参考兴趣漂移感知负采样方法：通过用户历史意图分布变化构造难负例，比随机负采样更能提升召回对换季、大促等场景下用户兴趣快速变化的适配速度'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM+推荐的两阶段召回重排架构落地时存在核心矛盾：LLM重排器训练推理成本高，无法频繁迭代；轻量ID召回器单独更新时容量有限、缺乏语义信号，难以适配用户兴趣漂移、新用户/新物品涌入的动态数据流，现有持续蒸馏方法仅适配ID类师生模型，无法利用LLM的语义能力。

### 方法关键点
- 设计轻量语义推理助理：离线蒸馏LLM的用户意图推理能力到动态意图记忆库，通过内存匹配方式给召回器提供语义引导，无需实时调用LLM
- 异步更新流程：LLM重排器仅在低置信度硬序列上做蒸馏；召回器高频更新时用协同意图伪标签、漂移感知负采样增强训练，无需LLM参与；重排器低频更新时注入召回器的实时表示和漂移信号，对齐最新用户行为
- 双向蒸馏机制：覆盖重排器到召回的排序+意图蒸馏、召回端自监督持续更新、召回器到重排器的行为信号反向蒸馏三个阶段

### 关键结果
在Amazon Books、Yelp、Amazon Movies三个真实数据集上对比CCD、LLMD4Rec、PISA等SOTA基线，重排端N@5平均提升4.2%~7.6%，召回端N@5平均提升15.3%~24.1%，同时LLM意图生成成本比CoT类方案降低10倍左右，对新用户、兴趣漂移用户的提升尤其显著。

最值得记住的一句话：LLM推荐落地不需要高频迭代大模型，把大模型的语义能力蒸馏成轻量可复用的信号模块，即可低成本解决动态数据流的适配问题

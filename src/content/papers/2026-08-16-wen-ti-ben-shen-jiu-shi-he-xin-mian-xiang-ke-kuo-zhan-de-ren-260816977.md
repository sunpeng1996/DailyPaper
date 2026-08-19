---
title: 'The Problem Is the Problem: Towards Scalable Mathematical Discovery'
title_zh: 问题本身就是核心：面向可扩展的人机协作数学发现
authors:
- Zeyu Zheng
- Shengtong Zhang
- Jeremy Avigad
- Prasad Tetali
- Sean Welleck
affiliations:
- Carnegie Mellon University
- Anysphere Co.
arxiv_id: '2608.16977'
url: https://arxiv.org/abs/2608.16977
pdf_url: https://arxiv.org/pdf/2608.16977
published: '2026-08-16'
collected: '2026-08-19'
category: Reasoning
direction: 人机协作推理 · 级联过滤推荐应用
tags:
- Cascade Filtering
- Human-AI Collaboration
- Mathematical Reasoning
- Recommender System
- Information Retrieval
one_liner: 提出借鉴搜索推荐级联过滤的FAR框架，实现高效人机协作规模化数学发现
practical_value: '- 可复用FAR的级联过滤思路，在高成本标注/审核的推荐场景（如广告素材合规审核、高价值内容筛选）中，用多阶段自动化过滤降低人力成本，将有限人工资源集中在高置信度候选上

  - 可迁移「从粗粒度用户意图（如兴趣方向而非具体query）出发召回候选+多轮过滤排序」的范式，用于长周期用户兴趣推荐、探索式搜索场景

  - 稀缺算力资源调度可参考该资源分配逻辑，在LLM推理、MoE路由等场景中优先把高成本算力分配给经过初筛的高价值候选，提升整体ROI'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前AI辅助数学发现流程中，前沿模型推理资源、专家审核资源均极为稀缺，人工选题、成果审核两个环节成为规模化研究的核心瓶颈。
### 方法关键点
提出新型人机协作范式，人工仅需输入感兴趣的研究方向而非预先选定具体问题；借鉴搜索推荐系统的级联过滤思路，搭建FAR（Find, Attempt, and Recommend）文献到审核的流水线，先从海量文献中召回候选开放问题，再经多轮自动推理、分类过滤，仅输出高价值候选给专家审核。
### 关键结果数字
组合数学领域实验中，从5245篇论文提取6453个候选猜想，过滤得到4717个有效开放问题，经后续推理筛选出77个高价值候选供专家审核，最终产出多个知名公开猜想的相关新成果。

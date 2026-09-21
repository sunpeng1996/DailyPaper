---
title: LLMs as Feature Engineers for Text-and-Tabular Prediction
title_zh: 面向文本+表格预测任务的LLM自动特征工程框架
authors:
- Merwan Barlier
- Blaz Skrlj
affiliations:
- Teads
arxiv_id: '2609.21894'
url: https://arxiv.org/abs/2609.21894
pdf_url: https://arxiv.org/pdf/2609.21894
published: '2026-09-18'
collected: '2026-09-21'
category: RecSys
direction: 推荐系统 · LLM自动特征工程
tags:
- Feature Engineering
- LLM4Rec
- CTR Prediction
- Interpretability
- Tabular Learning
one_liner: 双LLM+错误驱动反馈迭代框架，从文本提取可解释分类特征增强表格预测模型
practical_value: '- CTR/推荐场景可直接复用双LLM分工架构：用大能力LLM（如GPT-4o、Llama 3 70B）离线生成语义特征定义，用轻量LLM（如Llama
  3 8B）批量做文本打标，既保证特征质量又大幅降低推理成本，离线计算不影响在线延时

  - 可直接复用错误驱动反馈范式：把现有模型badcase（比如CTR排序反转对、高残差样本）转成自然语言prompt指导LLM生成特征，相比无引导搜索最高提3倍收敛速度，大幅减少LLM调用成本，缩短特征迭代周期

  - 现有文本特征体系升级可参考三视图互补思路：LLM生成的语义分类特征、TF-IDF、文本Embedding三者信号完全正交，全量叠加后在三类文本数据集上AUC均达最优，可直接复用到现有特征栈实现无风险提效

  - 合规要求高的场景可优先采纳该类特征：LLM生成特征普遍占据SHAP重要性排名头部，每个预测都可生成清晰的语义审计路径，完美满足算法监管的可解释性要求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
当前广告/推荐场景广泛使用的表格预测模型（如CTR预估模型）难以直接利用原始文本信息，现有方案要么是稠密文本Embedding（黑盒不可解释，无单预测审计路径），要么是人工构造语义特征（成本高、跨任务迁移性差），急需兼顾效果、效率与可解释性的自动化文本语义特征提取方案。

## 方法关键点
- 双LLM分工架构：大能力LLM仅离线调用，生成符合固定schema的分类特征定义（含名称、可选值、语义描述）；轻量LLM批量对全量文本做零样本分类打标，输出结构化特征列，大幅降低推理成本
- 迭代优化闭环：生成特征送入下游表格模型（如HistGradientBoosting）评估效果，通过贪心前向选择保留最优特征进入「名人堂」，避免重复生成
- 错误驱动反馈机制：将下游模型错误（如AUC任务的排序反转对）转化为自然语言prompt，指导下一轮特征生成定向解决badcase，无需人工干预

## 关键实验
在Kickstarter（短文本）、亚马逊图书评论（中长文本）、Stack Overflow（富格式长文本）三个公开数据集验证：对比无引导搜索基线，错误驱动范式特征发现效率最高提升3倍；LLM生成的语义特征、TF-IDF、稠密Embedding三者信号正交，叠加后三个数据集AUC分别达0.7692、0.8510、0.9700，均为最优；工业部署到广告CTR预估场景，在线A/B测试最高带来6.6%总营收提升，冷启动阶段13个小时桶中12个AUC正向。

## 核心结论
LLM生成的离散语义特征与传统TF-IDF、稠密Embedding信号完全独立，三者结合可在不破坏现有特征体系的前提下同时提升预测效果与可解释性

---
title: Document Topic Alignment Metrics for Evaluating Topic Models of Short-Text
  Public Health Communications on Social Media
title_zh: 面向社交媒体公共健康短文本主题模型的文档-主题对齐评估指标
authors:
- Wangjiaxuan Xin
- Shuhua Yin
- Yaorong Ge
- Shi Chen
affiliations:
- The University of North Carolina at Charlotte, College of Computing and Informatics
- The University of North Carolina at Charlotte, Department of Public Health and Health
  Administration
arxiv_id: '2609.14256'
url: https://arxiv.org/abs/2609.14256
pdf_url: https://arxiv.org/pdf/2609.14256
published: '2026-09-13'
collected: '2026-09-15'
category: Eval
direction: 短文本主题模型评估 · 语义对齐度量
tags:
- Topic Modeling
- Evaluation Metrics
- Short Text
- Semantic Alignment
- Social Media Analysis
one_liner: 提出感知主题分配的DoTA评估框架，量化短文本与分配主题的语义对齐度，更贴合人工评估结果
practical_value: '- 做用户评论、社交舆情、搜索Query的主题挖掘时，可复用DoTA的语义对齐思路，替代纯主题层面的评估，降低人工校验成本

  - 主题分配置信度、区分度的margin变体设计，可迁移到推荐系统的兴趣标签分配质量校验场景，优化标签召回准确率

  - 做LLM生成主题的效果评估时，可补充DoTA类分配感知指标，弥补传统困惑度、一致性指标和实际业务效果脱节的问题'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有主题模型评估指标仅聚焦生成主题本身，缺乏量化评估短文本与分配主题语义匹配度的手段，无法保障主题分配的实际可用性。
### 方法关键点
提出DoTA评估框架，是感知主题分配的度量体系，核心计算文档与分配主题的语义对齐度；同时设计margin-based、判别式两类变体，分别衡量主题分配的置信度与不同主题间的可区分性。
### 关键结果
在X平台3个公共健康相关社交媒体数据集上对5种主流主题模型测试，DoTA指标与人工评估的一致性远高于传统主题类指标，可提供传统指标覆盖不到的互补评估信号，让主题模型评估更贴合实际业务价值。

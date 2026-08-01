---
title: (Towards) Scalable Reliable Automated Evaluation with Large Language Models
title_zh: 面向大语言模型的可扩展可靠自动化评估框架
authors:
- Bertil Braun
- Martin Forell
affiliations:
- KIT
arxiv_id: '2607.28282'
url: https://arxiv.org/abs/2607.28282
pdf_url: https://arxiv.org/pdf/2607.28282
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: LLM输出无参考自动化评估
tags:
- LLM Evaluation
- Pairwise Comparison
- Elo Rating
- Reference-free Metric
- Automated Assessment
one_liner: 基于多LLM两两比较与Elo评级的无参考自动化评估框架，可对齐专家判断降低人工成本
practical_value: '- 电商/推荐场景下的生成式文案、推荐理由、Agent回复质量评估可复用该框架，无需构建参考标注集，大幅降低人工标注成本

  - 生成内容的排序、Bad case过滤可直接复用Elo评级逻辑，输出的排序结果稳定性高、可解释性强

  - 可调一致性阈值可适配不同业务优先级：高优场景（如营销文案）用全一致规则保证评估准确率，低优场景用多数投票提升覆盖效率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM生成文本的自动评估指标难以捕捉复杂语义差异，且普遍依赖参考标注，仅能用于有客观基准的领域，人工评估成本极高无法规模化落地。
### 方法关键点
1. 采用多LLM对生成输出做两两比较，抵消单模型评估的固有bias；
2. 引入Elo评分体系输出稳定、可解释的生成结果排序；
3. 支持从全票一致到多数投票的可调一致性阈值，灵活平衡评估置信度与覆盖范围。
### 关键结果
在科学摘要能力画像提取任务的评估中，自动生成的排序结果与专家判断相关性优异，可大幅降低人工干预需求。

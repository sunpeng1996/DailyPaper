---
title: 'Prompting Beats Fine-Tuning: Generative Expected Value Scoring for Statutory
  Term Retrieval'
title_zh: Prompt 优于微调：面向法律术语检索的生成式期望值打分
authors:
- Alvin Wang
- Jaromir Savelka
affiliations:
- Carnegie Mellon University
arxiv_id: '2607.05582'
url: https://arxiv.org/abs/2607.05582
pdf_url: https://arxiv.org/pdf/2607.05582
published: '2026-07-06'
collected: '2026-07-09'
category: RecSys
direction: 检索排序优化 · LLM Prompt 对比微调
tags:
- Information Retrieval
- LLM Prompting
- Fine-Tuning
- Sentence Ranking
- Zero-Shot Learning
one_liner: 对比编码器微调与解码器零样本Prompt方案，证明后者在法律术语解释判例句子排序任务上效果更优
practical_value: '- 低资源领域的内容/商品排序任务可优先测试Decoder-only大模型零样本Prompt方案，成本更低效果可能优于编码器微调

  - 相关性打分场景可复用生成式期望值打分思路，替代传统Encoder类分类打分模型，降低标注依赖

  - 冷启动检索/推荐任务无标注数据时，先跑Prompt baseline再判断是否投入资源做微调训练，减少试错成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
法律条文术语表述模糊，从业者需检索判例句子解释术语，现有检索结果相关性参差不齐，人工筛选成本极高，亟需高效的判例句子相关性排序方案。
### 方法关键点
对比两类排序方案：1）仅编码器模型（ModernBERT）监督微调做相关性分类打分；2）仅Decoder大模型零样本Prompt，生成句子对目标术语的解释价值评分实现排序。实验采用覆盖42个美国法典概念、标注4类解释价值的26959条判例句子公开数据集。
### 关键结果
ModernBERT微调效果与此前BERT系列基线表现相当；Decoder-only模型Prompt方案整体效果最优，最佳系统超过该任务所有此前SOTA结果，全NDCG截断指标均领先。

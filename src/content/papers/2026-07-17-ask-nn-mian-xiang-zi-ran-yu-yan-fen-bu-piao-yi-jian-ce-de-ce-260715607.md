---
title: 'ASK-NN: An Asymmetric Nearest-Neighbor Test that detects Distribution Drifts
  in Natural Language'
title_zh: ASK-NN：面向自然语言分布漂移检测的非对称最近邻测试
authors:
- Sergey Zakharov
- Rodion Oblovatny
- Alexey Zaytsev
affiliations:
- Saint-Peterburg university
- Risk AI Research Lab
- Applied AI Institute
arxiv_id: '2607.15607'
url: https://arxiv.org/abs/2607.15607
pdf_url: https://arxiv.org/pdf/2607.15607
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: LLM鲁棒性 · 分布漂移与幻觉检测
tags:
- Distribution Drift
- Hallucination Detection
- k-NN
- RAG
- Two-sample Test
one_liner: 基于有向k-NN图的非对称双样本测试，可高效检测LLM幻觉与人工文本
practical_value: '- RAG问答/商品文案生成场景可直接复用ASK-NN做幻觉检测，仅需对比prompt/检索上下文与生成结果的token级隐层分布漂移，无需额外标注

  - 搜索推荐query改写的质量校验场景，可引入该非对称测试对比原始query与改写query的分布差异，过滤低质量改写结果

  - 算法实现简单、计算高效，可直接嵌入现有LLM推理流水线的后置校验模块，额外 overhead 极低'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
LLM生成内容的幻觉、人工文本问题本质为prompt/检索上下文（参考样本）与生成响应（查询样本）的隐层分布偏差，现有双样本测试未适配两类样本角色、长度不对称的特性，存在精度或效率短板。
### 方法关键点
基于有向k-NN图构建非对称双样本测试ASK-NN，统计混合样本中最近邻仍为参考点的参考点数量作为统计量；可直接得到有限样本下的精确条件均值、方差，具备渐近正态性与一致性，无需额外训练，实现简单、计算高效。
### 关键结果
在合成基准、人工文本检测、LLM幻觉检测三类任务上性能与基于核、图的基线方法持平，仅输入token级隐层特征即可实现有效检测。

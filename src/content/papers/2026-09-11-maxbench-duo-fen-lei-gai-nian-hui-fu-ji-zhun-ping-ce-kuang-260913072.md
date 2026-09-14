---
title: 'MAxBench: A Multinomial Concept Recovery Benchmark'
title_zh: MAxBench：多分类概念恢复基准评测框架
authors:
- Divya Appapogu
- Freya Behrens
- Yonatan Belinkov
- Aaron Mueller
affiliations:
- 波士顿大学计算机系
- 以色列理工学院计算机系
- 哈佛大学Kempner研究所计算机系
arxiv_id: '2609.13072'
url: https://arxiv.org/abs/2609.13072
pdf_url: https://arxiv.org/pdf/2609.13072
published: '2026-09-11'
collected: '2026-09-14'
category: Eval
direction: LLM可解释性 · 概念引导评测
tags:
- Concept Steering
- LLM Interpretability
- Evaluation Benchmark
- Activation Space
- Multinomial Concept
one_liner: 提出几何无关的多分类概念表示评测框架MAxBench，对比10种定位方法给出最优结构选择
practical_value: '- 做LLM行为引导（如Agent话术控制、推荐文案风格校准）时优先选择仿射子空间方案，比单方向/线性子空间召回更高、稳定性更强

  - 仿射子空间的性能增益核心来自非零偏移而非基选择，工程实现时可优先优化偏移参数，降低计算复杂度

  - 多分类概念引导无需过度追求复杂定位方法，Prompting基线效果仍有竞争力，可优先用Prompting快速验证业务效果'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM概念引导研究多针对二元概念，电商/推荐场景常见的多分类概念（如商品品类、用户地域、内容标签）的表示几何空间远大于二元概念，缺乏统一评测框架验证最优表示方法与几何结构。
### 方法关键点
提出几何无关的MAxBench评测框架，基于恢复后的概念表示采样完成评估，覆盖10种概念定位方法、5类几何结构，在6种多分类概念、4个不同规模LLM上完成横向对比。
### 关键结果
① 仿射子空间引导的可靠性与召回显著优于秩1方向、线性子空间方案；
② 其性能增益核心来自非零偏移项，而非基向量选择；
③ 流形引导在适用场景下效果与当前最优方法持平；
④ 所有定位方法均未稳定超过Prompting基线效果。

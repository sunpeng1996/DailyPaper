---
title: 'Floor, Ceiling, and the Fusion Gap: How Much of Crowd Reading Attention Can
  Machines Predict?'
title_zh: 基准上下界与融合缺口：机器对人群阅读注意力的预测上限分析
authors:
- Kazuki Nakayashiki
- Keisuke Watanabe
affiliations:
- Glasp Inc.
arxiv_id: '2608.01704'
url: https://arxiv.org/abs/2608.01704
pdf_url: https://arxiv.org/pdf/2608.01704
published: '2026-08-03'
collected: '2026-08-05'
category: Eval
direction: 大模型任务性能边界评估
tags:
- Performance Benchmark
- Ensemble Learning
- Knowledge Distillation
- Zero-shot Learning
- Attention Prediction
one_liner: 构建人群阅读注意力预测任务的性能上下界，验证多模型融合及蒸馏可显著提升预测表现
practical_value: '- 落地新AI任务前先构建性能上下界：以naive方案为下界、人类一致性为上界，避免无意义的SOTA攀比，可快速对齐业务预期

  - 跨厂商不同基座的无权重多模型融合是低成本提效手段，收益稳定鲁棒，可直接迁移到文案理解、用户意图预测、内容高亮等场景

  - 多模型融合的知识蒸馏到轻量7B/8B级模型可保留90%以上增益，适合线上低延迟部署要求

  - 语义敏感任务慎用prompt compressor：LLMLingua-2在该任务上效果低于随机基线，上线前必须做充分验证'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
基准分数若无朴素方案下界与最优理论上界做参考，不具备实际评估价值，当前缺少人群无指导阅读注意力预测任务的性能边界量化。
### 方法关键点
构建包含337份网页文档的真实用户无指导高亮标注数据集，以naive截断取首为性能下界、人群对半拆分互测为上界，测试单模型、跨厂商无权重融合、知识蒸馏等方案的表现。
### 关键结果
- 上下界AP差为0.2028，语义特征占性能缺口的95%，位置长度特征仅能覆盖5%缺口
- 前沿大模型Zero-shot可覆盖35%~53%的性能缺口，LLMLingua-2效果低于下界，接近随机选择
- 5款跨厂商模型无权重融合加位置先验可覆盖60%缺口，比最优单模型AP高0.0159，该收益在217份独立文档上复现成功
- 融合模型蒸馏到8B开源模型可保留90%融合增益，性能与最强单模型统计持平

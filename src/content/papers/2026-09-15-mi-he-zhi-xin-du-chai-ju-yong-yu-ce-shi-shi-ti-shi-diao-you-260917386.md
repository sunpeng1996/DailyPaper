---
title: 'Bridging the Confidence Gap: Temperature Scaling for Calibrating Test-Time
  Prompt Tuning'
title_zh: 弥合置信度差距：用于测试时提示调优校准的温度缩放方法
authors:
- Yuwei Liang
- Jian Liang
- Dapeng Hu
- Yinuo Xu
- Ran He
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
- Independent Researcher
arxiv_id: '2609.17386'
url: https://arxiv.org/abs/2609.17386
pdf_url: https://arxiv.org/pdf/2609.17386
published: '2026-09-15'
collected: '2026-09-16'
category: Training
direction: 大模型调优 · 测试时校准
tags:
- Prompt Tuning
- Temperature Scaling
- Test-time Adaptation
- Calibration
- Zero-shot Learning
one_liner: 提出CoTS与E-CoTS后验校准方案，在保精度前提下大幅降低测试时提示调优的校准误差
practical_value: '- LLM驱动的搜索/推荐prompt调优场景可直接复用CoTS温度缩放方法，在不损失召回/排序精度的前提下降低置信度偏差，减少bad
  case

  - 弱-强多增强集成策略可迁移到电商多模态商品分类、用户意图识别任务，同时提升推理精度与输出校准性

  - E-CoTS可与现有CTR预估校准方法结合，同时提升推荐精度与置信度校准效果，优化流量分配的合理性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Test-time prompt tuning (TPT)支持单测试样本自适应提升精度，但会严重损失校准性能；现有校准方法多引入额外正则项，易导致推理精度下降，而zero-shot预测天然具备良好的校准特性。
### 方法关键点
1. 提出CoTS后验校准方法，通过温度缩放最小化TPT自适应后预测与zero-shot预测的置信度差距，全程不损失推理精度
2. 新增弱-强集成策略充分利用自适应过程中的多数据增强结果进一步提升精度，结合CoTS得到E-CoTS，同时兼顾精度与校准效果
### 关键结果
在ImageNet变体数据集上，E-CoTS将TPT的平均期望校准误差从11.90%降至5.38%，同时精度从60.74%提升至62.95%；与现有校准方法集成时，可同步提升两者表现

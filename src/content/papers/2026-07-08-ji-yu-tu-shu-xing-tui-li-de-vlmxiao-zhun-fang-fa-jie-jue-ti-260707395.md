---
title: 'When Prompts Ignore Structure: Graph-Based Attribute Reasoning for Calibrated
  VLMs'
title_zh: 基于图属性推理的VLM校准方法 解决提示忽略结构问题
authors:
- Tanay Sodha
- Aditya Sharma
- Ramya Hebbalaguppe
- Vinti Agarwal
- Pranav Murthy Yeluripaty
affiliations:
- Birla Institute of Technology and Science, Pilani
- TCS Research, New Delhi
arxiv_id: '2607.07395'
url: https://arxiv.org/abs/2607.07395
pdf_url: https://arxiv.org/pdf/2607.07395
published: '2026-07-08'
collected: '2026-07-09'
category: Multimodal
direction: 多模态大模型 · VLM测试时校准优化
tags:
- VLM
- Calibration
- GAT
- Contrastive Learning
- Test-time Adaptation
one_liner: 构建符号属性图建模属性关联，提出两种属性选择策略，大幅降低VLM测试时校准误差
practical_value: '- 电商多模态商品检索场景可复用符号属性图建模商品属性关联，优化CLIP类模型的置信度校准，减少过召回问题

  - 属性选择策略可迁移到商品标签生成：ARGTCA-DIV提升同品类属性多样性，ARGTCA-DISC强化跨品类属性区分度

  - 测试时prompt tuning场景下，对比学习+GAT生成结构化属性嵌入的方法，可缓解过置信问题，提升多模态分类可靠性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLM测试时prompt tuning虽能提升零样本准确率，但会因熵驱动的过置信问题导致校准效果下降，现有方法仅独立处理LLM生成的类属性，忽略属性间的关联结构，校准效果有限。
### 方法关键点
1. 提出ARGTCA框架，将（类、属性）对作为节点构建符号属性图，用Graph Attention Network（GAT）结合对比目标训练，生成捕捉属性间依赖的结构化嵌入；
2. 设计两类属性选择策略：ARGTCA-DIV面向类内属性多样性优化，ARGTCA-DISC面向类间属性区分度优化。
### 关键结果
在9个基准数据集上实验显示，ARGTCA-DIV相对基线平均降低Expected Calibration Error（ECE）约37%，ARGTCA-DISC相对基线平均降低ECE约17%，校准效果显著优于现有测试时调优方案。

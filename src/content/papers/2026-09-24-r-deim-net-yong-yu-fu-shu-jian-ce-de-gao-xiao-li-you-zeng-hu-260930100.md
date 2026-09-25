---
title: 'R-DEIM Net: An Efficient Rationale-Augmented Dual-Expert Interaction Model
  for Paraphrase Detection'
title_zh: R-DEIM Net：用于复述检测的高效理由增强双专家交互模型
authors:
- Pushp
- Vaibhav Prajapati
- Himangshu Sarma
affiliations:
- Indian Institute of Information Technology (IIIT), Sri City, India
- University of Technology Nuremberg (UTN), Germany
arxiv_id: '2609.30100'
url: https://arxiv.org/abs/2609.30100
pdf_url: https://arxiv.org/pdf/2609.30100
published: '2026-09-24'
collected: '2026-09-25'
category: QueryRec
direction: Query复述检测 · 双专家轻量架构
tags:
- Paraphrase Detection
- Dual Expert
- Flan-T5
- Rationale Generation
- Lightweight Model
one_liner: 76M参数双专家结构实现高性能复述检测，同时输出可解释推理依据
practical_value: '- 电商搜索相似Query/商品标题去重、客服话术匹配场景可直接复用双专家架构，76M小参数规模兼顾效果、推理成本与可解释性要求

  - 可复用「直接提取Decoder隐状态池化作为分类补充特征」的trick，避免生成文本二次编码的额外开销，降低在线推理延迟

  - 交互专家的多尺度2D卷积+可变长注意力头设计，可迁移到短文本匹配任务，替代纯Transformer结构降低小样本场景过拟合风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有复述检测方案存在三重矛盾：大模型准确率高但计算开销极大，小参数Siamese-BERT类方案易落地但可解释性缺失，无法同步生成人类可读的推理依据，无法满足高可信场景要求。

### 方法关键点
76M参数双专家架构R-DEIM Net：
1. 交互专家：通过多尺度2D卷积+可变长注意力头，抽取跨文本token级相似匹配特征
2. 推理专家：基于Flan-T5-small解码器生成可解释理由作为辅助监督，直接提取解码器隐状态池化作为分类补充特征，省略生成文本二次编码的冗余开销

### 关键结果
在Quora Question Pairs数据集10折交叉验证下，获90.07%准确率、90.16% F1，效果接近MFAE BERT的90.54%准确率、追平LLaMA-70B的基线表现，参数量仅为大模型的千分之一，同时可输出预测对应的可读推理依据。

---
title: Scalable Visual Pretraining for Language Intelligence
title_zh: 面向语言智能的可扩展视觉预训练方法
authors:
- Yiming Zhang
- Zhonghan Zhao
- Wenwei Zhang
- Haiteng Zhao
- Tianyang Lin
- Yunhua Zhou
- Demin Song
- Kuikun Liu
- Haochen Ye
- Haian Huang
affiliations:
- Shanghai Artificial Intelligence Laboratory
- University of Science and Technology of China
- Zhejiang University
- Shanghai Jiao Tong University
arxiv_id: '2607.09657'
url: https://arxiv.org/abs/2607.09657
pdf_url: https://arxiv.org/pdf/2607.09657
published: '2026-07-09'
collected: '2026-07-13'
category: LLM
direction: 大语言模型预训练 · 多模态视觉信号融合
tags:
- LLM Pretraining
- Multimodal Learning
- Unsupervised Learning
- Visual Pretraining
- Foundation Model
one_liner: 提出直接利用视觉文档的无监督预训练范式，无需文本提取即可提升大模型语言智能表现
practical_value: '- 处理电商商品详情页、广告物料这类带排版/图表的富文本数据时，可直接用视觉预训练范式替代OCR+文本解析的链路，减少信息损失

  - 训练电商场景文案生成、商品属性抽取的垂直大模型时，可引入视觉预训练阶段，提升对版式、公式、图表类非结构化信息的理解能力

  - 搜索推荐场景的Query理解/商品理解模块，可复用该无监督视觉预训练思路，无需额外标注即可提升多模态输入的理解精度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有大模型预训练默认所有知识可无损编码为纯文本序列，将文档、网页等富视觉资源转纯文本时会丢失版式、图表、公式等关键信息，存在固有损失，也不符合人类借助视觉信号推理的认知规律。

### 方法关键点
提出无需文本提取、无需图文配对标注的无监督视觉预训练范式，直接输入视觉文档完成预训练，可适配多种主流大模型骨干架构，无需修改下游任务训练流程。

### 关键结果数字
在相同语料规模、相同计算成本下，视觉预训练在所有语言智能基准测试中效果始终优于纯文本预训练基线，无需额外标注即可实现能力提升，具备高度可扩展性。

---
title: 'GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation'
title_zh: GoiBERT：基于两阶段知识蒸馏的紧凑越南语语言模型
authors:
- Quang Anh Kiet Tran
- Nam Anh Tran
- Manh Hung Trinh
- Thanh Danh Le
- Khang Nhat Hoang Vo
- Huynh Dai Nhan Tran
affiliations:
- UIT, VNU-HCM
- IU, VNU-HCM
- TwoHearts Technologies Co., Ltd.
- University of Eastern Finland
- MBZUAI
arxiv_id: '2610.30067'
url: https://arxiv.org/abs/2610.30067
pdf_url: https://arxiv.org/pdf/2610.30067
published: '2026-10-21'
collected: '2026-10-23'
category: Training
direction: 小语种语言模型 · 知识蒸馏压缩
tags:
- Knowledge Distillation
- Model Compression
- BERT
- Pre-trained Language Model
- Low-resource NLP
one_liner: 采用两阶段知识蒸馏得到26M/49M参数越南语紧凑BERT，性能领先且推理效率翻倍
practical_value: '- 垂直域/小语种预训练模型压缩可直接复用两阶段蒸馏框架，无需额外标注数据就能平衡性能与体积

  - 电商评论情感分析、客服文本分类等简单NLP任务，采用该蒸馏方案可实现几乎无损压缩，推理吞吐量提升100%，大幅降低部署成本

  - 实体抽取、语义推理类复杂任务需避免过高压缩比，实测该类任务压缩后性能损失明显，选型要权衡精度与效率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有越南语预训练编码器普遍参数量大、依赖外部分词组件，部署算力成本高，难以落地到低资源生产环境。
### 方法关键点
1. 采用两阶段互补知识蒸馏策略：第一阶段用同分词器的越南语教师模型传授通用表征，第二阶段用大模型生成无标注软标签提供任务级指导，全程无需额外标注数据；
2. 推出26M参数的GoiBERT-base和49M参数的GoiBERT-large两个紧凑版本，支持直接处理原始文本，无需外部分词。
### 关键结果
- 8个基准任务（文本分类、ABSA、自然语言推理、NER）上，GoiBERT-large平均得分居所有非教师模型首位，参数量不到最强紧凑基线的1/2，吞吐量是其2倍；
- GoiBERT-base仅为基线1/4大小，保留99%的基线性能；
- 情感分析、文本分类类简单任务压缩几乎无损，推理、NER类复杂任务压缩性能损失较高。

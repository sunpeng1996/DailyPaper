---
title: 'Knowing What Not to Answer: Selective Non-Compliance in Vision-Language Models'
title_zh: 知道哪些不该回答：视觉语言模型的选择性不服从能力研究
authors:
- Minji Kim
- Jihyoung Jang
- Hyounghun Kim
affiliations:
- Graduate School of Artificial Intelligence, POSTECH
- Department of Computer Science and Engineering, POSTECH
arxiv_id: '2609.04720'
url: https://arxiv.org/abs/2609.04720
pdf_url: https://arxiv.org/pdf/2609.04720
published: '2026-09-03'
collected: '2026-09-08'
category: Multimodal
direction: 多模态大模型 · 安全对齐评测
tags:
- VLM
- Selective Non-compliance
- Alignment
- Evaluation
- Fine-tuning
- Safety
one_liner: 提出KoNA基准评测VLM选择性不服从能力，混合微调方案兼顾安全与正常问答性能
practical_value: '- 电商多模态导购Agent可复用该思路，对包含错误前提、不可回答成分的复合用户query做分段处理，可回答部分正常响应，需拒绝部分明确说明，降低幻觉引发的用户投诉

  - 多模态内容/商品推荐的query理解模块可参考5类不可回答维度（错误前提、视觉不可达、通用未知、任务不可行、安全）做bad case标注与过滤，提升响应准确率

  - 大模型对齐微调时可采用「不可回答样本+全可回答样本」混合训练的范式，保证安全性提升的同时，最大程度保留正常业务任务的性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM对齐评测多基于整query粒度判断是否需要拒绝回答，默认单query要么全可回答要么全需拒绝，未覆盖实际场景中同时包含可回答、需拒绝成分的复合query场景，导致VLM在真实交互中易出现该拒不拒、不该拒乱拒的问题。
### 方法关键点
1. KoNA评测基准覆盖错误前提、视觉不可达、通用未知、任务不可行、安全5类场景，同时支持整query粒度、成分粒度的选择性不服从能力评测；
2. 采用「KoNA选择性不服从样本+全可回答样本」混合微调VLM，避免微调后模型出现过度拒绝的问题。
### 关键结果
评测发现主流VLM在复合query选择性不服从任务上的失败率显著高于单query场景；经混合微调方案优化后，VLM不服从准确率实现大幅提升，同时全可回答任务性能几乎无损失，可准确区分可回答成分与需拒绝成分。

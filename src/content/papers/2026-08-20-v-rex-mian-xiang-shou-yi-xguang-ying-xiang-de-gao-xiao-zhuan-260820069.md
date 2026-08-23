---
title: 'V-REX: Efficient Specialist VLM Training for Veterinary X-Rays'
title_zh: V-REX：面向兽医X光影像的高效专用VLM训练方案
authors:
- Tim Elsner
- Nicole McNally
- Andre Dourson
- Michael Fitzke
affiliations:
- Vyyo AI
- Mars Petcare
arxiv_id: '2608.20069'
url: https://arxiv.org/abs/2608.20069
pdf_url: https://arxiv.org/pdf/2608.20069
published: '2026-08-20'
collected: '2026-08-23'
category: Multimodal
direction: 多模态 · 垂直领域专用VLM高效训练
tags:
- VLM
- Efficient Training
- Domain Adaptation
- Multimodal
- Foundation Model
one_liner: 重构VLM全链路优化训练，用小参数低成本得到超越通用大模型的垂直领域专用VLM
practical_value: '- 垂直领域多模态任务（如电商商品图理解、短视频文案生成）无需盲目微调大底座，可从tokenizer到推理全链路优化，用小参数实现远超通用大模型的效果

  - 可复用其提出的预训练、对齐优化策略，提升业务数据利用率，大幅降低垂直场景多模态模型的训练算力与数据成本

  - 无需依赖外部公开数据集，仅用自有业务数据即可训练适配性更强的专用模型，适合用户数据隐私要求高的业务场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
通用VLM训练算力成本极高，行业默认垂直领域专用模型必须微调超大参数基础模型，资源投入大，且通用模型在垂直细分场景的性能表现不佳。
### 方法关键点
重构VLM全链路设计，覆盖文本tokenization、预训练、grounding到推理全流程，提出全新的生成式预训练与grounding策略，针对性提升训练效率与数据利用率，无需依赖外部补充数据。
### 关键结果
仅占用通用大模型极小比例的参数、训练数据与算力，训练得到首个可生成兽医X光诊断报告的专用VLM，性能大幅领先现有开源通用基础模型。

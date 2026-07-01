---
title: 'Little Brains, Big Feats: Exploring Compact Language Models'
title_zh: 《小模型大能量：紧凑型语言模型应用探索》
authors:
- Dari Baturova
- Elena Bruches
- Ivan Chernov
- Roman Derunets
- Arsenii Fomin
- Andrey Kostin
affiliations:
- Siberian Neuronets LLC
arxiv_id: '2606.30062'
url: https://arxiv.org/abs/2606.30062
pdf_url: https://arxiv.org/pdf/2606.30062
published: '2026-06-28'
collected: '2026-07-01'
category: RAG
direction: RAG系统 · 小语言模型端侧推理
tags:
- SLM
- RAG
- On-device Inference
- Model Benchmark
- Edge Deployment
one_liner: 验证RAG系统搭配小语言模型可在无GPU端侧以合理时延完成推理
practical_value: '- 端侧智能导购/推荐场景可尝试用SLM做RAG生成模块，无需GPU即可降低部署成本，适配无云端算力的离线场景

  - 资源受限的边缘端推荐/营销文案生成任务，可优先验证SLM+RAG方案，平衡推理速度与输出准确性

  - 可复用论文开源的SLM RAG评测代码，针对业务私有数据集做适配，快速筛选适合自身场景的轻量模型'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前大语言模型在RAG生成阶段算力需求高，部署成本高，不适配端侧/低资源场景；而小语言模型（SLM）实用价值被广泛低估，缺乏RAG场景下的系统性性能基准验证。

### 方法关键点
搭建覆盖多学科领域、多问题类型的混合评测数据集（含开源数据+业务私有数据），针对RAG系统的生成模块做单变量测试，固定召回模块逻辑，仅替换不同参数规模的SLM做生成推理，重点测试无GPU硬件条件下的端侧运行表现。

### 关键结果
搭载SLM的RAG系统可完全脱离GPU，直接在端侧设备上运行，且推理时延处于业务可接受的合理区间，配套评测代码与数据集已在GitHub开源。

---
title: Multilinguality in Hybrid Attention LLMs
title_zh: 混合注意力大模型的多语言特性研究与层序优化
authors:
- Lucas Bandarkar
- Junlin Hu
- Chenyuan Yang
- Mohsen Fayyaz
- Nanyun Peng
affiliations:
- University of California, Los Angeles
- Fudan University
arxiv_id: '2609.35378'
url: https://arxiv.org/abs/2609.35378
pdf_url: https://arxiv.org/pdf/2609.35378
published: '2026-09-27'
collected: '2026-10-07'
category: LLM
direction: 混合注意力LLM · 多语言性能优化
tags:
- Hybrid-Attention
- Multilingual-LLM
- Cross-Lingual-Alignment
- Knowledge-Distillation
- Layer-Order-Optimization
one_liner: 揭示混合注意力LLM多语言表征规律，提出首层用全注意力的层序优化方案训练提速最高2.5倍
practical_value: '- 自研/微调多语言混合注意力LLM时，固定第一层为全注意力，可降低40%+训练成本，同时提升东南亚、南亚等小语种的理解性能

  - 跨境电商出海场景的长上下文多语言query理解、商品文案生成任务，优先选用混合注意力LLM，显存占用显著降低，长上下文下性能损失极小

  - 多语言LLM蒸馏落地时，保留首层为全注意力，其余层可按需求替换为循环注意力，兼顾推理效率与跨语言迁移效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前混合注意力LLM（Qwen、Kimi、Nemotron等系列）是长上下文Agent、推理场景的主流架构，但现有研究完全未涉及混合注意力对多语言处理的影响，而多语言是出海Agent、跨境电商场景的核心需求；同时混合注意力的循环层归纳偏置可能改变语言处理逻辑，其层序排布的合理性也缺乏验证。

### 方法关键点
- 提出SoftCKA跨语言对齐度量，无需显式token配对即可衡量不同语言的表征相似度，降低跨语言表征分析的噪声
- 对比4组混合注意力LLM与非混合对照模型的层间表征变化，定位全注意力层对多语言表征的影响规律
- 多语言蒸馏实验中固定全注意力层占比为25%，仅调整全注意力层的排布位置，对比5种不同层序方案的效果

### 关键实验
基于覆盖26种语言的FineWeb数据集开展蒸馏实验，基线为业界通用的周期性层序（循环层在前、全注意力在后）：所有首层用全注意力的方案均显著超过基线，仅需34.5%~42.5%的训练token即可达到基线1B token训练的最终效果，训练速度最高提升2.5倍；其中reverse periodic方案（每块首层用全注意力）在25种语言上效果最优，泰卢固语、缅甸语等小语种性能提升最高达13%。

**最值得记住的一句话**：多语言混合注意力LLM仅需把第一个解码器层设为全注意力，就能以极小的架构改动获得训练效率与小语种性能的双重提升。

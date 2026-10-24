---
title: On the Token Collapse Phenomenon in Textual Graph Soft Prompting
title_zh: 文本图软提示中的Token坍缩现象研究
authors:
- Andrea Giuseppe Di Francesco
- Rishabh Jain
- Franco Maria Nardini
- Nicola Tonellotto
- Pietro Liò
- Fabrizio Silvestri
affiliations:
- Sapienza University of Rome
- ISTI-CNR
- University of Cambridge
- University of Pisa
arxiv_id: '2610.31572'
url: https://arxiv.org/abs/2610.31572
pdf_url: https://arxiv.org/pdf/2610.31572
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: LLM软提示 · 图结构信息注入
tags:
- Soft Prompt
- Graph LLM
- Token Collapse
- KGQA
- LoRA
one_liner: 揭示图软提示的跨输入Token坍缩问题，提出图-Token对齐评估方法与两阶段缓解方案
practical_value: '- 电商/Agent场景做知识图谱+LLM的RAG链路时，不要默认图软提示能有效传递图谱信息，需新增干预测试（如替换为损坏图的Token）验证信息是否真被LLM利用，避免无效优化

  - 若业务中使用图软提示效果不符合预期，可尝试论文提出的两阶段训练方案规避Token坍缩，提升图信息注入的有效性

  - 评估图软提示效果不要仅看下游任务精度，新增Token跨样本相似度检测与对齐度探针，提前发现坍缩问题降低线上风险'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有图软提示方案（如G-Retriever）被广泛用于将知识图谱结构信息注入LLM，但其效果归因不清晰，未发现潜在的性能退化路径。
### 方法关键点
1. 对G-Retriever开展跨3个benchmark、3种图编码器、2类LLM架构、frozen/LoRA微调模式的系统性干预实验，明确定义Token坍缩现象：不同输入生成的图Token几乎无差异，仅起到通用软提示作用，未传递有效图信息
2. 提出两阶段训练方案缓解坍缩，同时设计解码探针与干预实验评估图-Token对齐度，替代仅依赖任务精度的传统评估方式
### 关键结果
标准设置下，用数据集均值Token、其他样本Token、损坏图生成的Token替换原图Token，任务精度无显著变化；完全不访问图的固定常量软提示在3个KGQA基准上效果持平甚至超过G-Retriever；两阶段方案在多数场景下保持竞争力的同时解决Token坍缩问题

---
title: 'Benchmarking Large Language Models on Heterogeneous Cognitive and Biomedical
  Knowledge Graphs: The Role of Graph Grounding in Multi-Hop Reasoning and Hallucination
  Mitigation'
title_zh: 大语言模型异构认知与生物医学KG基准：图接地对推理与幻觉的作用
authors:
- Ali Sarabadani
- Kheirolah Rahsepar Fard
- Tahereh Jeirani
affiliations:
- Department of C
arxiv_id: '2611.08315'
url: https://arxiv.org/abs/2611.08315
pdf_url: https://arxiv.org/pdf/2611.08315
published: '2026-11-05'
collected: '2026-11-06'
category: Eval
direction: LLM多跳推理 · 幻觉缓解评测
tags:
- LLM
- Knowledge Graph
- Multi-hop Reasoning
- Hallucination Mitigation
- Graph Grounding
- Benchmark
one_liner: 构建跨5个异构KG的LLM推理基准，验证图接地可显著降低所有模型幻觉率
practical_value: '- 垂直领域LLM应用优先采用「通用大模型+KG grounding」方案，比直接用垂直小模型的推理准确率更高、幻觉率更低

  - 多跳推理场景可按查询复杂度分层选型：单跳简单查询用轻量模型，多跳复杂查询用通用大模型+KG，平衡效果与算力成本

  - 构建垂直领域LLM评测集时可复用多层级query设计+多人标注框架，用Cohen/Fleiss kappa验证标注一致性，保障评测可靠性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
生物医学、认知神经科学领域LLM落地加快，但异构知识图谱（KG）上的可靠推理能力缺乏系统性评测，幻觉问题是落地核心障碍。
### 方法关键点
选取GPT-5.1、Gemini 2.0 Pro、Llama 3、Qwen、BioGPT共5款LLM，在DrugBank、NeuroSynth等5个异构KG上开展测试；构建多层级查询数据集，对比KG-aware（图接地）和KG-agnostic两种模式下的推理深度与事实准确率，采用Cohen's kappa、Fleiss' kappa验证标注一致性。
### 关键结果
1. 标注一致性达标：Cohen's kappa达0.781，Fleiss' kappa达0.77；
2. 通用大模型（GPT-5.1、Gemini 2.0 Pro）多跳推理表现优于垂直领域模型，性能随查询复杂度上升明显下降；
3. 图接地可降低所有测试模型的幻觉率，无图接地时垂直领域模型未优于通用大模型。

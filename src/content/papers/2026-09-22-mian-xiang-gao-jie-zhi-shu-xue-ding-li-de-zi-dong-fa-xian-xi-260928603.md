---
title: Learning to Discover Interesting Mathematics
title_zh: 面向高价值数学定理的自动发现学习方法
authors:
- Niket Patel
- Ahmad Rammal
- Amaury Hayat
- Remi Munos
- Julia Kempe
affiliations:
- FAIR @ Meta
- New York University
- CERMICS, ENPC, Institut Polytechnique de Paris
arxiv_id: '2609.28603'
url: https://arxiv.org/abs/2609.28603
pdf_url: https://arxiv.org/pdf/2609.28603
published: '2026-09-22'
collected: '2026-09-26'
category: Reasoning
direction: LLM推理 · 数学定理自动发现
tags:
- LLM
- Mathematical Reasoning
- Theorem Proving
- Metric Learning
- Automatic Knowledge Expansion
one_liner: 提出可量化的定理价值度量，训练27B模型实现无人干预的高价值新定理自动发现
practical_value: '- 生成内容价值度量思路可迁移：可复用「产出下游复用价值/生成成本」的比值型指标，作为UGC、商品文案、Agent生成话术的价值排序信号，降低人工标注成本

  - 低重叠生成优化方法可复用：通过自定义价值度量优化生成目标，可降低生成内容与现有存量库的重复率，适合电商新品文案、个性化推荐理由的原创性提升

  - 自迭代知识库构建范式可复用：可直接套用「生成候选→按自定义度量筛选→迭代扩库」的流程，搭建无需持续人工标注的领域知识库，如电商商品知识图谱、行业话术库'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM已具备解决数十年悬而未决的高难度数学问题的能力，但自动生成的定理是否具备研究价值/实用性缺乏可量化的评估标准，无法支撑无人干预的数学知识规模化扩展。
### 方法关键点
1. 定义定理内在价值为「证明长度/定理陈述长度」，验证该指标与定理下游效用的强相关性；
2. 以给定前提集下的证明难度为核心原语，训练27B专用模型，证明难度预测精度优于前沿通用大模型；
3. 采用「候选定理生成→价值排序筛选→迭代扩展知识库」的自迭代框架，无需人工给定目标。
### 关键结果
优化价值度量后，生成定理与Mathlib的大幅/完全重叠率从91.9%降至30.6%，可自动生成大量分布外高价值新定理，支撑自扩展机器验证数学库构建。

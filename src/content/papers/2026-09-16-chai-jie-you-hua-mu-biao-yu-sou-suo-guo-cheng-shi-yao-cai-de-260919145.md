---
title: 'Objective vs. Search: Decomposing What Makes a Good Tokeniser'
title_zh: 拆解优化目标与搜索过程：什么才是好的Tokenizer设计
authors:
- Ahmetcan Yavuz
- Clara Meister
- Tiago Pimentel
affiliations:
- ETH Zürich
- EPFL
arxiv_id: '2609.19145'
url: https://arxiv.org/abs/2609.19145
pdf_url: https://arxiv.org/pdf/2609.19145
published: '2026-09-16'
collected: '2026-09-17'
category: LLM
direction: LLM基础组件 · Tokenizer设计优化
tags:
- Tokenizer
- BPE
- UnigramLM
- Preprocessing
- Language Model
one_liner: 构造2×2 tokenizer设计空间，验证搜索过程而非优化目标是影响LM性能的核心因素
practical_value: '- 业务域内自定义Tokenizer优先选bottom-up搜索框架（BPE/BottomUpLL），可稳定降低域内文本BPB，提升LM推理效率和上下文利用率

  - 小词汇量（<32k）场景下可优先采用log-likelihood目标的BottomUpLL，比传统BPE的BLiMP语法准确率高~2%，适合Agent对话、商品文案生成等对语义理解要求高的场景

  - 多语言电商/跨境业务场景可尝试top-down类Tokenizer，对形态丰富的小语种语法理解能力更优'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有主流Tokenizer（BPE、UnigramLM）同时在优化目标（压缩/对数似然）和搜索过程（自底向上合并/自顶向下剪枝）两个维度存在差异，过往对比无法定位性能差异的核心来源，业务侧自定义Tokenizer缺乏明确选型指导。
### 方法关键点
- 补全2×2设计空间的两个空白算法：BottomUpLL（自底向上合并+对数似然目标）、TopDownComp（自顶向下剪枝+压缩目标）
- 所有Tokenizer统一预处理流程，控制变量仅保留优化目标和搜索过程两个可变维度
- 推导两类算法的高效增量更新公式，可支撑大词汇量Tokenizer的落地训练
### 关键结果
在英文FineWeb-Edu、5语言多语语料上训练100M~1B参数LM，对比4类Tokenizer：
- 几乎所有场景下bottom-up类Tokenizer的BPB比top-down类低1%~2.8%，搜索过程是影响语言建模性能的核心因素
- 小词汇量（8k）下对数似然目标的Tokenizer效果优于压缩目标，BLiMP语法准确率高1.7%
- 多语语法评测无明显一致规律，top-down类对形态丰富的小语种（德、西、土耳其语）效果更优

> 最值得记住的结论：Tokenizer设计中搜索过程的影响远大于优化目标，业务自定义Tokenizer优先选自底向上搜索框架

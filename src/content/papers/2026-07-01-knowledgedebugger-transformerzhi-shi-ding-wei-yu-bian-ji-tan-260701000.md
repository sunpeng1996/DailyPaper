---
title: KnowledgeDebugger -- an Exploration Tool for Knowledge Localization and Editing
  in Transformers
title_zh: KnowledgeDebugger：Transformer知识定位与编辑探索工具
authors:
- Eric Benz
- Lennart Stöpler
- Nikolai Bolik
- Artur Andrzejak
affiliations:
- Heidelberg University
arxiv_id: '2607.01000'
url: https://arxiv.org/abs/2607.01000
pdf_url: https://arxiv.org/pdf/2607.01000
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: LLM工具 · 知识定位与编辑
tags:
- Knowledge Editing
- Transformer
- Debug Tool
- EasyEdit
- GUI
one_liner: 推出无代码GUI工具KnowledgeDebugger，对接EasyEdit实现Transformer知识定位与编辑
practical_value: '- 做LLM4Rec/Agent的知识修正时，可直接用该工具快速验证单样本知识编辑效果，无需手写适配EasyEdit的代码，降低前期验证成本

  - 排查LLM调用的事实错误（如商品属性、活动规则答错），可通过该工具定位错误知识对应的参数位置，为定向优化提供依据

  - 该工具的无代码GUI交互设计思路可复用，用于内部LLM推荐/Agent系统的调试面板开发，降低算法排查门槛'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前Transformer知识存储机制研究、知识编辑实验分两阶段开展，第一阶段的单样本现象探索缺乏低门槛工具支持，现有LM-Debugger不兼容主流知识编辑方法，操作成本高。

### 方法关键点
1. 设计GUI化交互工具KnowledgeDebugger，参考LM-Debugger的细粒度激活查看逻辑，无代码对接SOTA知识编辑库EasyEdit，支持调用各类主流知识编辑算法
2. 支持单样本粒度的知识定位、编辑干预、效果即时验证，可直观呈现知识修改对模型前向传播过程的影响

### 关键结果
通过复现知识编辑领域近年的多个经典研究结论的案例，验证了工具的有效性，代码与文档已完全开源

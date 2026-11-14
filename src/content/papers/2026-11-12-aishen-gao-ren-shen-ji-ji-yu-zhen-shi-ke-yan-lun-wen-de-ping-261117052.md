---
title: 'Auditing AI peer reviewers: a benchmark on real scientific papers'
title_zh: AI审稿人审计：基于真实科研论文的评测基准
authors:
- Íñigo Zubeldia
- Boris Bolliet
- Francisco Villaescusa-Navarro
- Pablo Villanueva-Domingo
- Miles Cranmer
affiliations:
- University of Cambridge
- Flatiron Institute
- Universitat Autònoma de Barcelona
- Polymathic AI
arxiv_id: '2611.17052'
url: https://arxiv.org/abs/2611.17052
pdf_url: https://arxiv.org/pdf/2611.17052
published: '2026-11-12'
collected: '2026-11-14'
category: Eval
direction: LLM系统评测 · 多智体工具调用
tags:
- Evaluation Benchmark
- MultiAgent
- Tool Calling
- RAG
- LLM
one_liner: 构建真实论文注入可控错误的AI审稿评测基准，提出带工具调用的多智体审稿系统
practical_value: '- 搭建电商内容审核、广告合规校验等场景的评测基准时，可复用「注入可控已知错误+统计检测率/误报率」的量化评估范式，避免主观评测偏差

  - 垂直领域Agent做事实校验可按任务类型拆分工具链：引用类用RAG召回原始资料、数值类调用代码执行、公式类调用专用计算引擎，效果优于单LLM调用

  - 工具调用增益与LLM领域知识掌握程度负相关：若LLM已充分学习目标领域语料，额外RAG召回的边际收益会大幅降低，可据此优化架构选型'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM驱动的审稿系统已规模化落地，但缺乏客观统一的评测体系，难以量化不同系统的错误检测能力和误报水平。
### 方法关键点
1. 构建通用评测基准：在天体物理、机器学习两个领域共30篇真实arXiv预印本中，注入4类（通用问题、数学、数值、引用）3个严重级别的共357个可定位客观错误，同时统计系统在干净论文上的误报率。
2. 提出多智体审稿系统Skepthical：针对不同错误类型调用专属工具，引用类错误召回原始引文校验，数学类错误用计算机代数系统验证，数值类错误执行代码复现。
### 关键结果
相同prompt下3款前沿LLM的总检测率差距达50个百分点；大部分系统误报率低于10%，数学类报错是误报主要来源；天体物理领域Skepthical的引用错误检测率大幅领先所有单LLM系统，机器学习领域因LLM对领域文献掌握更好，其引用检测优势不显著

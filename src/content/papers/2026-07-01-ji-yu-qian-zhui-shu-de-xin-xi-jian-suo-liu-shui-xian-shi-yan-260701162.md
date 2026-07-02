---
title: Trie-based Experiment Plans for Efficient IR Pipeline Experiments
title_zh: 基于前缀树的信息检索流水线实验高效规划方法
authors:
- Irene Anu
- Craig Macdonald
affiliations:
- University of Glasgow, United Kingdom
arxiv_id: '2607.01162'
url: https://arxiv.org/abs/2607.01162
pdf_url: https://arxiv.org/pdf/2607.01162
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: IR级联流水线实验效率优化
tags:
- Trie
- Information Retrieval
- Pipeline Evaluation
- PyTerrier
- Experiment Efficiency
one_liner: 采用Trie结构设计级联IR流水线对比实验方案，减少重复组件计算提升效率
practical_value: '- 级联召回/重排流水线多方案对比测试时，可复用Trie结构缓存公共组件（如BM25召回、基础重排层）的计算结果，避免重复计算降低测试耗时

  - 内部离线效果验证/AB实验平台可参考该思路，自动识别多个实验流的公共执行路径，做全局缓存与复用，提升整体实验吞吐量

  - 基于PyTerrier做检索/推荐系统基线实验的团队可直接集成该Trie实验规划方法，现有流程无需大幅改造即可获得20%+的耗时收益'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前级联检索/推荐流水线多方案对比实验中，不同变体通常共享大量公共组件（如召回层、前序重排层），线性逐流水线执行会产生大量重复计算，PyTerrier原生框架未针对该场景做效率优化。
### 方法关键点
1. 用Trie数据结构表征所有待对比的流水线变体，公共前缀对应流水线共享组件，公共分支仅执行一次；
2. 自动将多流水线对比任务转化为Trie遍历执行计划，共享节点的计算结果全局缓存复用，无需人工标注公共路径。
### 关键结果
- 在MSMARCO v2数据集上，对包含BM25召回、MonoT5、DuoT5重排的多流水线对比实验，相比线性执行方案耗时降低26%；
- 学生用户调研显示该方案可降低实验配置复杂度，大幅提升研究效率。

---
title: 'Same Problem, Different Field: Cross-Domain Solution Import via Domain-Stripped
  Computational Fingerprints'
title_zh: 基于去领域计算指纹的跨领域同计算问题解决方案迁移
authors:
- Eryk Kulikowski
affiliations:
- LIBIS
- KU Leuven
arxiv_id: '2609.07595'
url: https://arxiv.org/abs/2609.07595
pdf_url: https://arxiv.org/pdf/2609.07595
published: '2026-09-07'
collected: '2026-09-09'
category: RAG
direction: 跨领域知识检索 · LLM蒸馏表示
tags:
- Cross-Domain Retrieval
- LLM Distillation
- Document Embedding
- Computational Fingerprint
- Faceted Representation
one_liner: 通过去领域分面计算指纹实现跨学科同计算问题的解决方案检索复用
practical_value: '- 跨场景/跨域推荐召回场景，可借鉴去领域指纹思路，剥离品类、业务场景等领域特有属性，提取核心用户行为/排序的计算逻辑特征，匹配不同域下的同构问题解法。

  - RAG跨领域知识检索场景，可复用本方法的LLM蒸馏流程：一次缓存LLM调用生成去领域骨架+控制面特征，结合轻量嵌入器即可大幅提升同问题跨域检索精度，效果优于主流学术嵌入器。

  - 多业务线算法方案复用（如电商广告排序和内容推荐排序的同构问题迁移），可参考本方法的计算逻辑匹配框架，降低重复开发成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
不同领域往往存在本质完全相同的计算问题，但受术语命名、领域语境差异限制，现有基于主题、引用的学术嵌入方法无法识别这类同构问题，难以实现跨领域解决方案复用。
### 方法关键点
1. 利用LLM蒸馏生成去领域名、方法名的分面计算指纹，包含自由文本计算逻辑骨架+受控计算维度标签；
2. 定义可调的分面选择距离用于指纹相似度匹配；
3. 全流程仅需单篇文档一次缓存LLM调用+轻量嵌入器，计算成本极低。
### 关键结果
109篇论文基准测试中，骨架特征将跨域检索平均精度从纯摘要的0.222提升至0.513，完整指纹可达0.557，效果优于4种主流学术嵌入器；501篇开放语料测试中Top30结果有23对为已知同构问题对，盲测Top5有3对、Top30有8对为可落地迁移候选，已有4个成功迁移落地案例。

---
title: The Head Complexity of Boolean Functions in Single-Layer Attention
title_zh: 单层注意力中布尔函数的头复杂度研究
authors:
- Rajmohan Rajaraman
- Ravi Sundaram
- Amanuel Tesfaye
affiliations:
- Northeastern University
arxiv_id: '2609.04046'
url: https://arxiv.org/abs/2609.04046
pdf_url: https://arxiv.org/pdf/2609.04046
published: '2026-09-03'
collected: '2026-09-06'
category: LLM
direction: LLM基础理论 · 注意力头计算复杂度
tags:
- Attention
- Complexity Theory
- Transformer
- Boolean Function
- Computational Bound
one_liner: 从理论层面刻画单层注意力头的计算能力边界，证明嵌入维度与精度无法替代头数
practical_value: '- 主要为学术理论贡献，电商/推荐业务可直接复用的工程方法有限

  - 做Transformer架构裁剪优化时，可参考头数与计算能力的对应关系权衡头数配置

  - 多跳推理相关Induction Head任务的头数下界结论，可作为LLM推理架构设计参考'
score: 4
source: arxiv-cs.LG
depth: abstract
---

## 动机
Transformer性能与注意力头数强相关，但此前缺乏严格理论刻画单层纯注意力模型的头计算能力边界，也无法验证嵌入维度、数值精度等资源是否可替代头数。
## 方法关键点
定义头复杂度为单层纯注意力模型计算目标布尔函数所需的最少头数，基于交替和阻塞构造下界证明，结合多项式展开、计数论证推导通用函数的头数上下界。
## 关键结果
1. k个头可计算k位奇偶校验，无法计算k+1位，该下界不受嵌入维度、数值精度大小影响；
2. 任意可计算函数的嵌入维度与精度仅由头数、字母表大小、序列长度即可界定，无限维度/精度无法替代头数；
3. n位二元函数头数上界为2^n，几乎所有函数需要Ω(2^n/n²)个头，二者仅差poly(n)因子。

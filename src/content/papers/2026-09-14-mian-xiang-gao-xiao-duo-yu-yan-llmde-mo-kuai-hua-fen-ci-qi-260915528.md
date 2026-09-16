---
title: 'To Each Language Its Tokenizer: Modular Tokenizers for Efficient Multilingual
  LLMs'
title_zh: 面向高效多语言LLM的模块化分词器：每语言专属子分词器
authors:
- Franck Signe
- Hippolyte Pilchen
- François Yvon
- Édouard Grave
affiliations:
- Kyutai
- Sorbonne Université
- CNRS
- Univ. Grenoble Alpes
- Grenoble INP
arxiv_id: '2609.15528'
url: https://arxiv.org/abs/2609.15528
pdf_url: https://arxiv.org/pdf/2609.15528
published: '2026-09-14'
collected: '2026-09-16'
category: LLM
direction: 多语言LLM 模块化分词器效率优化
tags:
- Multilingual-LLM
- Tokenizer
- Modular-System
- Inference-Optimization
- Cross-lingual-Fairness
one_liner: 提出可拆分的多语言模块化分词器框架与预训练策略，兼顾性能、效率与跨语言公平性
practical_value: '- 跨境电商多语言LLM应用（客服、商品文案生成、多语言搜索query理解）可复用模块化分词思路，针对落地的目标语言裁剪子词表，大幅降低小模型部署的内存占用，提升推理速度

  - 多语言LLM预训练时可复用子分词器采样策略，无需在全量大词表上计算softmax，降低训练成本，同时支持任意语言组合的推理需求，无需额外微调

  - 多语言内容处理场景可借鉴公平性优化思路，避免小语种内容分词长度过长导致的KV cache浪费、上下文窗口利用率低的问题，尤其适合小语种商品评论、搜索query的处理'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统多语言LLM采用单一份共享词表，存在两大核心痛点：一是各语言压缩率不均，小语种分词后序列长度是英语的数倍，导致上下文窗口利用率低、计算成本高；二是大词表带来的嵌入和输出矩阵占参比例过高（2.6B的Gemma2有22%参数属于词表相关矩阵），部署时如果仅用到少数语言，大量参数冗余，内存和推理效率极差。

### 方法关键点
- 分别适配Unigram和BPE两种主流分词器的模块化构建方案：Unigram通过合并单语言分词器后重估全局概率，BPE采用顺序增量训练策略，保证每个语言的子分词器可独立提取，压缩率接近独立训练的单语言分词器
- 配套预训练策略：每批采样子分词器（单语言或n种语言组合），损失仅在对应子词表上计算，无需近似softmax；同时暴露少量跨语言token做正则，避免推理时混合语言场景的分布偏移
- 工程上采用CPU offload存储全量词表参数，训练时仅加载当前批用到的子词表，支持扩展到上百种语言无额外训练 overhead

### 关键结果
在21种语言（含6种低资源语言）上训练2.5B参数模型，对比Gemma3、Llama3等开源多语言分词器：
1. 提取的单语言子分词器压缩率和独立训练的单语言分词器差距<4%，低资源语言序列长度比开源分词器最多缩短8.1倍
2. 单语言部署时用24k子词表替代256k共享词表，2.5B模型参数量减少35%，推理速度最高提升7.3倍，KV cache占用降低22%-44%
3. 下游MCQ、翻译、摘要任务性能和传统共享词表基线完全持平

**最值得记住的一句话**：多语言LLM的分词器不需要做大一统的共享词表，模块化拆分+灵活组合的思路可以同时兼顾跨语言公平性、部署效率和下游性能。

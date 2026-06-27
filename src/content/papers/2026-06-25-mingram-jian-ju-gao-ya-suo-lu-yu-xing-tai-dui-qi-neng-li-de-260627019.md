---
title: 'MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive
  Morphological Alignment'
title_zh: MinGram：兼具高压缩率与形态对齐能力的极简Unigram分词器
authors:
- Sander Land
affiliations:
- Writer, Inc.
arxiv_id: '2606.27019'
url: https://arxiv.org/abs/2606.27019
pdf_url: https://arxiv.org/pdf/2606.27019
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: LLM分词器优化 · 高压缩率Unigram实现
tags:
- Tokenizer
- Unigram
- BPE
- Compression
- Morphological Alignment
- LLM Training
one_liner: 简化Unigram分词器训练流程，实现高于BPE与标准Unigram的压缩率同时保留形态对齐能力
practical_value: '- 自研垂直领域分词器时，可借鉴MinGram的训练简化思路：用BPE做种子词表、Hard EM+单次剪枝替代传统Unigram的复杂流程，大幅降低训练成本

  - 处理电商/广告场景长文本（商品详情、用户评论）时，可采用「先最小token数再概率打分」的解码逻辑，压缩序列长度，降低KV cache开销，提升大模型推理速度

  - 针对小语种/垂直领域（美妆、3C等）的分词优化，可复用tiebreak设计，在保证压缩率的同时保留专业术语形态完整性，提升RAG检索和语义匹配准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统Unigram分词器形态对齐能力强、词表易编辑，但训练依赖后缀数组、前后向传播、迭代剪枝等复杂流程，开发门槛高；BPE训练简单但形态对齐差、词表效率低，高压缩率和形态对齐的tradeoff难以兼顾，简化Unigram训练流程同时保留其优势具备较高工程价值。

### 方法关键点
- 初始化：用BPE训练得到的词表作为种子，替代传统Unigram的后缀数组候选集，降低初始化复杂度
- 解码目标：优先最小化token数，再用Unigram log概率打分做tiebreak，兼顾压缩率和形态合理性
- 训练流程：用最小token路径上的Hard EM替代传统Unigram的边际EM，去掉前后向传播，训练后仅做1次分数剪枝得到目标大小词表，无需迭代剪枝

### 关键结果
在英/德/芬兰/俄/阿拉伯/韩6种语言的5GB FineWeb语料上训练，对比BPE、标准Unigram等7种基线：
1. 默认MinGram压缩率比标准Unigram高1.83%，比BPE高0.4%，形态对齐得分介于BPE和标准Unigram之间
2. 下游LLM训练时，MinGram的bits-per-byte指标优于BPE 0.22%，仅产生9个低频token，远少于BPE的172个
3. 压缩优先的MinGram-PP压缩率比标准Unigram高2.33%，接近最优的PathPiece，同时形态对齐得分比PathPiece高53.7%

**最值得记住的结论**：仅将Unigram概率得分作为分词tiebreak项，就能在几乎不损失压缩率的前提下大幅提升形态对齐效果，纯压缩率导向的分词器反而会降低下游LLM建模效果

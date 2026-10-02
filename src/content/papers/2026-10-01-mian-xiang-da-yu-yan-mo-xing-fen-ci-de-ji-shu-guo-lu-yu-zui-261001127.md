---
title: Counting and Min-Cost Encoding for Tokenization in Large Language Models
title_zh: 面向大语言模型分词的计数过滤与最小代价编码方法
authors:
- Shuming Shi
- Xiang Zhang
- Hao Yu
- Wenbo Fei
- Changjian Wang
- Zhan Wang
- Guoqing Pang
- Guangye Yu
- Quan Lu
- Ning Jiang
affiliations:
- Mashang Consumer Finance Co., Ltd.
- National-Mathematics Artificial Intelligence Institute in Chongqing (NMAII)
arxiv_id: '2610.01127'
url: https://arxiv.org/abs/2610.01127
pdf_url: https://arxiv.org/pdf/2610.01127
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: LLM分词优化 · 高效token压缩
tags:
- Tokenizer
- BPE
- Token Efficiency
- LLM Inference
- Vocabulary Construction
one_liner: 无合并CNF词汇构建与MCE全局编码分词框架，不损失下游效果前提下大幅提升token效率
practical_value: '- 现有基于BPE的LLM服务可直接将编码逻辑替换为MCE算法，无需修改原有词汇表即可获得15%+的token压缩率，降低KV
  cache占用、缩短长文本（商品详情、用户评论、多轮会话）的推理耗时

  - 自研垂直领域LLM（电商客服Agent、商品文案生成、导购大模型）可采用CNF方法构建领域专属词汇表，将高复现的商品名、营销话术、品类术语加入候选，进一步提升垂直场景的token效率

  - 长上下文推荐场景可参考MCE的全局最优拆分思路，设计用户行为序列、语义召回单元的压缩编码规则，降低序列建模的计算开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
主流BPE分词器依赖顺序合并规则，会产生大量低利用率的中间token，固定词汇量下压缩率受限；UnigramLM则需要迭代概率估计，训练成本高。更高的token压缩率意味着相同文本下token序列更短，可直接降低LLM推理耗时、减少KV cache显存占用，对长上下文应用收益显著。

### 方法关键点
- 计数过滤（CNF）词汇表构建：无合并步骤，先统计语料中合法子串的出现频次构造原始词汇表，再通过分词过滤掉实际使用中低频的token，得到最终词汇表
- 最小代价编码（MCE）算法：全局最优分词，代价函数由token单位成本、跨单元边界惩罚、token偏好项三部分组成，通过动态规划求解最小代价拆分结果，支持BPE、Unigram、CNF等任意类型词汇表

### 关键实验结果
跨6类文本（英文网页、PDF、数学、代码、中文、多语言）对比OpenAI o200k、Qwen250k等主流BPE分词器：250K词汇量下英文网页文本压缩率提升26.7%~32.4%；词汇量扩展到1M时，token效率提升超60%，词汇利用率从BPE的52.9%提升到96.9%；1.8B、8B参数LLM从头训练，11个下游基准平均效果与BPE基线完全持平。

### 核心结论
CNF-MCE分词框架在不损失下游效果的前提下，可将token压缩率提升20%以上，且兼容现有BPE词汇表，落地成本极低。

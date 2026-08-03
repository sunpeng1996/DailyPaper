---
title: Tokenizer-Agnostic Engram Module
title_zh: 与分词器无关的Engram条件存储模块
authors:
- Jia Peng Lim
- Hai Leong Chieu
affiliations:
- Singapore Management University
- DSO National Laboratories
arxiv_id: '2607.29065'
url: https://arxiv.org/abs/2607.29065
pdf_url: https://arxiv.org/pdf/2607.29065
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: LLM效率优化 · 跨分词器Engram复用
tags:
- Engram
- Tokenizer
- Hashing
- LLM Efficiency
- Knowledge Transfer
one_liner: 用多项式哈希替换Engram的XOR哈希，实现跨分词器的Engram嵌入复用，性能与原版相当
practical_value: '- 落地LLM驱动的电商文案生成/query理解场景时，若引入Engram模块降低推理成本，可直接替换原XOR哈希为多项式哈希，无需为不同分词器的模型单独训练Engram权重，大幅降低训练成本

  - 跨模型迁移知识时，可借鉴字节级哈希对齐思路，无需依赖token级对齐，尤其适合多语种/多业务线不同分词器LLM的能力复用

  - 做用户行为序列N-gram特征建模时，可参考共享N-gram嵌入空间的设计，无需为不同长度的N单独维护特征表，降低存储与维护开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
DeepSeek提出的Engram模块通过N-gram哈希查表实现低开销的条件记忆，可大幅平衡LLM的存储与推理性能，但原设计依赖token级XOR哈希，与分词器强绑定：不同分词器的模型必须从零训练Engram嵌入，无法复用已有权重，极大限制了Engram的落地灵活性，尤其小模型选择分词器时还需额外权衡嵌入与前馈参数的比例，落地成本高。
### 方法关键点
- 将N-gram从token级离散空间建模改为字节序列采样：只要底层字节序列相同，无论分词方式如何，都映射到同一个哈希键，实现字节等价的哈希对齐
- 替换原XOR哈希为多项式哈希，支持流式计算，算法复杂度与原XOR哈希完全一致，无额外开销
- 取消不同长度N的N-gram独立嵌入表，改用统一共享嵌入空间，同时新增1-gram支持，适配不同分词器的切分粒度差异
### 关键结果数字
- 单分词器训练场景下，多项式哈希版Engram与原版XOR版性能相当：在SmolLM2-1.7B上平均准确率比无Engram基线高10.2%，仅比XOR版高1.2个百分点，bits/byte指标基本一致
- 跨分词器迁移场景下，使用cl100k_base分词训练的7B模型Engram冻结权重，直接给用SmolLM2分词的0.8B小模型使用，平均准确率比无Engram基线高3.8%，其中BoolQ提升10%、COPA提升7%
- 消融实验证明仅用1-gram时Engram无明显增益，效果来自N>1的跨分词器N-gram对齐
### 核心结论
Engram的核心价值来自对底层字节序列的记忆，而非特定分词器产出的token级N-gram结构

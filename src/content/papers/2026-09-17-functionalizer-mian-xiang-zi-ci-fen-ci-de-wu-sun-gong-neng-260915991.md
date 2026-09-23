---
title: 'The Functionalizer: Lossless Functional Decomposition for Subword Tokenization'
title_zh: Functionalizer：面向子词分词的无损功能分解框架
authors:
- Connor Makowski
- Willem Guter
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2609.15991'
url: https://arxiv.org/abs/2609.15991
pdf_url: https://arxiv.org/pdf/2609.15991
published: '2026-09-17'
collected: '2026-09-23'
category: LLM
direction: 大语言模型 · 子词分词优化
tags:
- Tokenization
- Subword
- Vocabulary Compression
- LLM Training
- Code Generation
one_liner: 提出基于Unicode私用区的无损预分词框架，拆分字形变换与基础词元以压缩词表、提升下游生成效果
practical_value: '- 开发垂域LLM（电商文案生成、客服Agent）时，可复用该预分词框架压缩词表，将大小写、特殊符号等格式变换拆为独立opcode，减少冗余词元占用，提升Embedding空间利用率

  - 电商场景处理多语言商品标题、带格式营销文案时，可基于该无损分解方案保留全量格式信息，同时避免字形变体导致的词表膨胀

  - 代码生成类Agent的分词环节可复用REPEAT算子设计，统一编码缩进、重复符号等结构，实验显示该方案可将Python语法正确率相对提升18.4%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前子词分词存在两难困境：要么把`hello/Hello/Héllo`等字形变体当成独立词元，导致词表冗余、Embedding空间碎片化；要么通过归一化丢弃变体信息，造成不可逆的信息损失，现有方案无法同时兼顾无损信息保留与词表效率。

### 方法关键点
- 借鉴CPU指令集架构，将字形/结构变化拆分为`opcode（变换算子）+ operand（标准基础词元）`的组合结构，所有opcode编码在Unicode私用区（PUA），完全可逆可复现
- 内置四类算子：大小写变换、13种变音符号处理、单字符重复、子序列重复，规则确定无需依赖外部词典或频率统计
- 可无缝对接BPE等标准分词器，支持算子与基础词元分离/融合两种模式：分离模式保证基础词元Embedding全局共享，融合模式可平衡序列长度开销

### 关键实验结果
数据集覆盖自然语言（Wikitext、FineWeb-Edu）、代码（Python-Codes-25k、GitHub-Code-Python），对比基线为LLaMA标准预分词流程：
1. 全语料覆盖下词表压缩率最高达19.7%（FineWeb-Edu数据集），平均压缩17.16%
2. 98M参数GPT-2训练后，Python代码生成语法正确率从7.70%提升至9.12%，相对提升18.4%
3. 自然语言生成重复n-gram占比从66.0%降至55.8%，代码生成重复n-gram从25.5%降至17.9%

### 核心结论
功能分解可以在仅引入少量序列长度开销的前提下，同时实现子词分词的无损信息保留、词表效率提升与下游生成质量优化

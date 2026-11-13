---
title: 'Parsed, Plausible, Wrong: Output Format Controls Silent Errors in Small-Model
  Semantic Parsing'
title_zh: 小模型语义解析中输出格式对静默错误的调控效应研究
authors:
- Umar Ahmed
- Maxim Dunaev
- Mohammad Nour Al Awad
- Sergey Ivanov
- Ivan Khodnenko
affiliations:
- ITMO University
arxiv_id: '2611.17169'
url: https://arxiv.org/abs/2611.17169
pdf_url: https://arxiv.org/pdf/2611.17169
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: 小模型语义解析 · 输出格式优化
tags:
- Semantic Parsing
- LoRA
- Small Language Model
- Silent Error
- Output Format
one_liner: 通过6种无损编码对比验证小模型语义解析采用自然词汇输出可降静默错误、提推理速度
practical_value: '- 端侧部署电商导购、点餐等场景的语义解析小模型时，优先选用自然词汇组成的输出格式，可比JSON/s-expression等符号格式减少3/4输出token，推理速度提升3~4倍，同时静默错误率降低1.8~2.3倍

  - 低资源场景微调语义解析模型时，输出格式尽量对齐预训练自然词表，可比等长符号格式提升4~8个点的精确匹配率，训练数据越少收益越显著

  - 设计Agent指令解析模块的评估体系时，可复用论文的四维度指标（精确匹配率/静默错误率/不可解析率/合法请求拒识率），全面量化解析可靠性，避免隐性错误造成业务损失

  - 给语义解析模块添加非法请求拒识能力时，仅需在训练集中加入30%负样本、10%自校正样本，即可实现95%+的域外请求拒识率，对合法请求的准确率影响极小'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
小参数LLM成本低、易部署，适合端侧运行语义解析任务（如电商导购指令抽取、线下点餐意图识别），但存在两类错误：可检测的解析失败/拒识，以及输出格式合法但内容错误的静默错误，后者直接导致业务损失。直觉认为输出token越短错误越少，但该假设从未被严谨验证，输出格式对静默错误的影响机制尚不清晰。

### 方法关键点
- 选取两款亚十亿参数模型（Qwen3.5-0.8B、LFM2.5-350M），统一用LoRA微调，超参数对齐
- 设计6种语义树的无损编码格式，包含两组长度匹配对照对，分离输出长度和表面形式的影响
- 训练集加入30%非法请求负样本、10%带用户自修正的样本，所有格式共享输入和训练逻辑
- 采用四维度评估体系，用分层bootstrap和Holm校正保证统计显著性

### 关键结果
在PIZZA点餐语义解析基准上完成300组对照实验：
1. 自然词汇格式WORDS精确匹配率最高（Qwen上87.5% vs 原生s-expression的85.8%），输出token数仅为原生格式的1/4，推理速度提升3.7倍
2. WORDS静默错误率相比原生格式降低2.3倍（Qwen上4.5% vs 10.3%）、1.8倍（LFM2上10.0% vs 17.9%），其中否定语义错误率降低90%
3. 输出长度本身不影响准确率，等长自然词汇格式比符号格式准确率高5~8个点，数据量越少优势越明显
4. 所有格式都实现95.9%~99.0%的非法请求拒识率，代价是2.1%~10.1%的合法礼貌请求被误拒

> 最值得记住的结论：小模型语义解析的输出格式设计，优先对齐预训练自然词表比单纯压缩输出长度更重要，可同时获得更高准确率、更低静默错误和更快推理速度

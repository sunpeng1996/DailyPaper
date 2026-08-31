---
title: 'Lost in Compression: A Controlled Cross-Lingual Audit of Extractive Prompt
  Compressors'
title_zh: 抽取式Prompt压缩器的可控跨语言效果审计
authors:
- Mantas Lukauskas
affiliations:
- Hostinger
- Kaunas University of Technology
arxiv_id: '2608.26175'
url: https://arxiv.org/abs/2608.26175
pdf_url: https://arxiv.org/pdf/2608.26175
published: '2026-07-26'
collected: '2026-08-31'
category: LLM
direction: 大模型Prompt压缩 · 跨语言效果评估
tags:
- Prompt Compression
- Cross-Lingual
- LLMLingua
- Inference Optimization
- Multilingual
one_liner: 揭示英文训练的抽取式Prompt压缩器跨语言迁移差距，给出非英语场景压缩实践指南
practical_value: '- 非英语/多语言RAG、Agent系统不要直接使用英文训练的抽取式压缩器，keep rate<0.5时中文等语言的上下文利用率几乎为0，效果远不如TF-IDF、前缀截断等确定性方法

  - 多语言压缩场景优先选择原生多语言数据训练的查询感知压缩器（如XProvence v1），上线前必须做单语言校准，避免出现类似v2版本92%中文上下文被清空的无报错故障

  - 非英语场景需要高压缩率时可尝试「翻译到英文→压缩」的pipeline，成本仅为原生压缩的1/2，立陶宛语、芬兰语等语言下效果优于原生压缩，适合离线/批量任务

  - 生产环境要监控各语言请求压缩率与实际压缩率的差值，英文训练压缩器在非英语下容易出现不压缩（如Kompress-v2对中文keep rate达0.96）或过度压缩的隐性故障'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
抽取式Prompt压缩是降低LLM推理成本的核心手段，现有主流压缩器（如LLMLingua-2）均在英文场景下训练和评测，但非英语语言本身token成本比英文高1.3~1.8倍，若压缩效果在跨语言场景下大幅下降，会导致非英语用户承担「token贵+压缩质量差」的双重损失，此前无系统性的可控跨语言审计验证这一问题。

### 方法关键点
- 采用10种语言、5种书写系统的完全平行语料，对齐目标模型tokenizer的token预算，排除任务难度、分词器差异的干扰
- 审计4种学习型压缩器（3种英文训练：LLMLingua-2 XLM-R/mBERT、Kompress-v2；1种多语言训练：XProvence）和4种确定性baseline
- 测试11款来自10个厂商的目标LLM，累计25万+次推理调用，采用归一化上下文利用率（相对于全上下文/无上下文的准确率占比）作为核心指标

### 关键结果
- 压缩率越高跨语言差距越明显：0.75 keep rate下各语言表现接近，0.33 keep rate下英文保留57~62%的上下文利用率，立陶宛语仅10~24%，中文利用率甚至低于无上下文基线
- 差距由训练数据而非架构决定：3种英文训练压缩器平均差距0.23~0.31，确定性方法无显著差距，原生多语言训练的XProvence v1无跨语言差距，但基于翻译数据训练的v2在激进阈值下92%的中文上下文被清空
- 长上下文场景下英文训练压缩器的非英语上下文利用率降到无上下文水平，「翻译到英文再压缩」的pipeline成本仅为原生压缩的一半，3/5测试语言下效果优于原生压缩

最值得记住的一句话：英文训练的Prompt压缩器的非英语安全压缩预算仅为英文的一半，激进压缩下中文等语言的上下文几乎完全失效。

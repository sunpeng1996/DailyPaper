---
title: 'Your Transformer Can Hold Two Thoughts at Once: Evidence of Linear Superposition
  in LLMs'
title_zh: Transformer可同时处理两路语义：LLM线性叠加特性的实证研究
authors:
- Pavel Tikhonov
- Anton Korznikov
- Matvey Mikhalchuk
- Nikita Dragunov
- Temurbek Rahmatullaev
- Polina Druzhinina
- Anton Razzhigaev
- Ivan Oseledets
- Elena Tutubalina
arxiv_id: '2609.29845'
url: https://arxiv.org/abs/2609.29845
pdf_url: https://arxiv.org/pdf/2609.29845
published: '2026-09-23'
collected: '2026-09-26'
category: LLM
direction: 大语言模型 · 线性叠加推理效率优化
tags:
- Linear Superposition
- LLM Inference
- KV Cache
- Lightweight Fine-tuning
- Decoder-only Transformer
one_liner: 证实Transformer固有输入嵌入线性叠加特性，轻量微调后单前向传播可同时生成两路连贯文本
practical_value: '- 高并发推理降本：电商导购、批量文案生成等高并发场景，可利用线性叠加特性将2路用户请求/文案任务的嵌入混合后单次推理，理论吞吐量提升2倍，KV
  cache占用减半，大促场景下可大幅降低算力成本

  - RAG效率优化：搜索推荐/Agent的多文档RAG场景，可将多路召回的top N文档嵌入线性混合后单次送入LLM，避免多轮前向开销，尤其适合多商品对比、多方案推荐的用户咨询场景

  - 低成本微调落地：如需上线叠加推理能力，可复用论文的自蒸馏微调范式，仅用0.025%的预训练数据量即可恢复模型线性特性，无需全量重训，适配业务侧的小算力微调资源

  - 低侵入解码实现：叠加输出的分离可采用轻量Joint Contrastive方案，仅需引入小参数引导模型做logit修正，无需修改大模型主干结构，工程落地成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM推理默认单流语义处理，多独立请求需串行或独立批处理，算力与KV cache开销极高；尽管Transformer包含自注意力、非线性激活等大量非线性组件，已有研究证实残差流的层间转换存在近似线性结构，但该特性能否扩展到端到端输入输出映射尚未被验证，若可落地将为LLM推理降本提供全新路径。

### 方法关键点
- 提出叠加线性假设：将两路独立输入的token嵌入逐元素平均后输入LLM，输出的next token分布近似为两路独立输出分布的算术平均
- 跨预训练轨迹验证特性来源：通过不同训练阶段的checkpoint验证线性叠加是Transformer架构固有特性，而非训练习得，且随预训练推进线性度逐步下降
- 轻量自蒸馏微调：以冻结的原预训练模型为教师，最小化混合输入输出与两路输出平均的KL散度，仅用0.025%预训练数据量即可大幅恢复线性特性
- 引导解码设计：提出Joint Contrastive解码方法，用小参数辅助模型提供单流logit引导，分离混合输出为两路独立连贯文本

### 关键结果
实验覆盖Pythia、Llama 3.2、Qwen2.5等主流开源模型，数据集采用TinyStories、FineWeb：
- 原生预训练模型下，叠加输入后单流真实next token进入top10的概率达30-40%，top100达60-65%，远高于随机基线
- 微调后，叠加输出与目标分布的KL散度从1.86降至0.27，真实token进入top5的概率从30%提升至60%以上
- 引导解码下，Llama 3.2-3B叠加推理的LAMBADA准确率达0.43，接近单流1B小模型基线的0.54，吞吐量较串行推理提升近2倍，KV cache占用减半

### 最值得记住的结论
Transformer的线性叠加是架构固有特性，仅需极低成本微调即可激活，是当前LLM推理降本增效的可行新路径

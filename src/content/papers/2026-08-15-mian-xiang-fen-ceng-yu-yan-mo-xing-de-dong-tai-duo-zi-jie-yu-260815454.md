---
title: Dynamic Multi-Byte Prediction With Hierarchical Language Models
title_zh: 面向分层语言模型的动态多字节预测方法
authors:
- Abraham Toluwase Owodunni
- Chibuzor Okocha
- Christan Grant
- Tomasz Limisiewicz
- Sachin Kumar
affiliations:
- The Ohio State University
- University of Florida
- University of Washington
arxiv_id: '2608.15454'
url: https://arxiv.org/abs/2608.15454
pdf_url: https://arxiv.org/pdf/2608.15454
published: '2026-08-15'
collected: '2026-08-19'
category: LLM
direction: 字节级LLM · 推理加速优化
tags:
- Byte-level LM
- Multi-token Prediction
- Inference Acceleration
- Hierarchical LM
- Causal Attention
one_liner: 通过边界感知LCA掩码实现分层字节LM无额外参数的多字节并行推理加速
practical_value: '- 落地LLM驱动的电商文案生成、智能客服、商品标题改写等场景时，可复用LCA-MBP方案，在几乎不损失生成质量的前提下提升29%~37%推理吞吐，无额外参数开销，显著降低推理成本

  - 做多Token预测优化时可放弃固定数量的多MLP头设计，改用段对齐单头+自定义因果掩码的架构，避免参数随并行数线性增长，还支持推理时动态调整并行候选数适配不同业务的精度/速度要求

  - 可借鉴动态阈值τ的调优逻辑：对容错率高的文案生成类场景调小τ换更高吞吐，对商品属性抽取、Query语义理解等精度敏感场景调大τ；搭配投机解码可100%保留原有模型精度，同时获得1.4~1.7倍速提升'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
字节级语言模型彻底解决了传统子词分词带来的语言/语系偏见、稀有词过分割、跨域/多语言泛化差等问题，是无Tokenizer LLM的核心发展方向，但逐字节自回归生成的推理延迟过高，是业务落地的核心瓶颈。现有多Token预测（MTP）加速方案存在两个固有缺陷：固定偏移的预测窗口无法适配语言天然的可变局部结构，新增多组预测头的设计会随并行数线性增加显存开销，无法直接适配分层字节LM的架构特性。

### 方法关键点
- 设计Latent Causal Attention（LCA）掩码：同一段内的字节仅可关注自身、段内更早位置及前一段所有字节，在严格保证因果性的前提下支持同段内多字节并行预测
- 仅新增1个共享的多字节预测（MBP）头，无需随并行字节数增加参数，预测窗口与分层LM动态学习到的字节段自然对齐，替换传统MTP的固定偏移预测逻辑
- 推理支持两种验证策略：概率阈值接受（可调τ灵活平衡速度与精度）、投机解码验证（完全保留基线模型精度），支持推理时动态调整并行候选数n，无需重新训练

### 关键结果
基于373M参数模型在50B字节FineWeb-edu语料预训练，在指令跟随、QA、摘要、机器翻译4类任务上验证，对比LlamaByte、FlexiTokens、MLP-MBP等参数匹配的基线：
LCA-MBP在3/4任务上处于性能-吞吐的帕累托最优前沿，仅用1个预测头性能远超同等参数规模的多MLP头MTP方案；采用投机解码验证时，并行候选数n从3提升到7可获得29%~37%的吞吐提升，且生成精度完全不变；作为同规模基线模型的draft模型时，可实现1.4~1.7倍的推理加速，精度完全匹配基线。

> 最值得记住的结论：分层字节LM学到的隐式语义段不仅可用于压缩序列长度降低训练成本，还可直接作为并行生成的单元，在无额外参数开销的前提下实现推理速度的显著提升。

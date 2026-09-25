---
title: 'Scoring Both Directions: LLMs realize the MRS they cannot reliably parse'
title_zh: 《双向评测：大语言模型可生成MRS却无法可靠解析它》
authors:
- Soham Dan
affiliations:
- Scale AI
arxiv_id: '2609.30071'
url: https://arxiv.org/abs/2609.30071
pdf_url: https://arxiv.org/pdf/2609.30071
published: '2026-09-24'
collected: '2026-09-25'
category: Eval
direction: LLM语义理解能力双向评测
tags:
- MRS
- LLM Evaluation
- Semantic Parsing
- Text Generation
- Formal Semantics
one_liner: 双向评测Claude系列模型MRS与文本的转换能力，证明仅生成分数无法证明模型理解形式语义
practical_value: '- 做Agent语义理解任务时，不能仅用生成效果评估语义理解能力，必须增加反向解析/结构化输出的校验环节，避免高估模型能力

  - 涉及形式化语义（如商品属性结构化、query意图语义Graph解析）的场景，不要盲目用通用LLM替代专用规则/模型，通用LLM结构化解析准确率远低于专用系统

  - 做生成类任务时，可采用「专用系统生成候选+LLM排序选优」的组合架构，能低成本提升生成效果，本实验中该方案帮Sonnet提了近4个BLEU点'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
过往仅用MRS到文本的生成分数评估LLM对形式语义的理解能力，缺少反向文本到MRS解析的双向验证，结论可信度不足。

### 方法关键点
重构10K句的MRS-文本双向评测基准，零样本测试Claude Sonnet 4.5、Claude Opus 5在两个方向的效果，对比专用解析生成系统ACE、以及过往训练的seq2seq模型。

### 关键结果
- 生成方向（MRS→文本）：3 shot下Opus达到76.3 BLEU，远超72K对数据训练的seq2seq模型的66.1 BLEU，接近百万级数据训练模型的77.2 BLEU；Sonnet原生65.7 BLEU，选择ACE候选提至69.6 BLEU，混入Opus候选提至77.0 BLEU
- 解析方向（文本→MRS）：Sonnet F1仅57.2，Opus仅65.5，远低于ACE的91.0，Exact Match仅1%左右

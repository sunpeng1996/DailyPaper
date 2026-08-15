---
title: 'Alignment Drift in Single-Model Speculative Decoding for ASR: Mechanism, Correction,
  and Cost'
title_zh: 单模型推测解码在ASR中的对齐漂移：机制、修正与开销
authors:
- Xinyu Wang
- Huapeng Zhou
- Ziyu Zhao
- Silin Meng
- Ke Bai
- Dongming Shen
- Xiao-Wen Chang
- Alex Smola
affiliations:
- Boson AI
- McGill University
arxiv_id: '2608.12703'
url: https://arxiv.org/abs/2608.12703
pdf_url: https://arxiv.org/pdf/2608.12703
published: '2026-08-13'
collected: '2026-08-15'
category: LLM
direction: 大模型推理 · 推测解码优化
tags:
- Speculative Decoding
- ASR
- Alignment Drift
- Inference Acceleration
- AnchorDraft
one_liner: 发现ASR场景下单模型推测解码的对齐漂移问题，提出AnchorDraft方案提升推理速度
practical_value: '- 单模型挂载轻量draft模块做推测解码的思路，可迁移到LLM驱动的Agent、生成式推荐场景降低推理延迟，无需维护额外小模型

  - AnchorDraft训练时注入位置跟踪能力、不改动推理图的设计，可复用在商品文案生成、智能客服回复等低开销生成加速场景

  - 验证阶段注意力回传位置信息修正draft漂移的trick，可平衡接受率提升和额外开销，适配搜索推荐Query补全等对latency敏感的场景'
score: 4
source: arxiv-cs.MM
depth: abstract
---

**动机**
单模型推测解码通过挂载轻量draft模块生成候选token、目标模型批量验证实现生成加速，但应用到ASR场景时出现draft音频位置跟踪偏差的对齐漂移问题，导致候选接受率随步数下降，加速效果受损。
**方法关键点**
1. 定位漂移根源：draft每步可读取全量音频但无法动态匹配已生成文本对应的音频位置，极端场景下draft位置误差中位数达21帧，远高于目标模型的2帧；
2. 两种修正方案：从验证阶段注意力中读取音频位置引导下一轮draft生成；AnchorDraft训练时让draft学习音频位置跟踪能力，推理无额外开销。
**关键结果**
AnchorDraft在两种不同规模目标模型上均实现端到端推理速度提升，正确的音频位置匹配可让后续候选token接受率翻倍

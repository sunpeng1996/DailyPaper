---
title: 'ARB: A Matched Authorship-Rewriting Benchmark Dataset for AI-Text Detector
  Evaluation'
title_zh: ARB：面向AI文本检测器评估的匹配式作者身份重写基准数据集
authors:
- Gaetano Perrone
- Simon Pietro Romano
affiliations:
- University of Napoli Federico II, Italy
arxiv_id: '2607.29539'
url: https://arxiv.org/abs/2607.29539
pdf_url: https://arxiv.org/pdf/2607.29539
published: '2026-07-31'
collected: '2026-08-04'
category: Eval
direction: LLM文本检测 · 基准评估
tags:
- AI-text-detection
- Benchmark
- LLM-rewriting
- Evaluation
- Paraphrase
one_liner: 构建含4种作者/重写模式的匹配基准，验证传统AI文本检测基准对LLM重写人类文本场景的评估失效
practical_value: '- 业务侧若需识别AI生成/改写的商品文案、用户评价、客服话术，不能仅用传统「人vs原生AI文本」的评估范式，需补充LLM重写人类文本的测试集，避免高估检测器实际效果

  - 若要检测LLM改写的人类原生内容，现有主流开源检测器（FastDetectGPT、Binoculars等）召回率仅15%~31%，不满足业务要求，需针对性补充H2L样本重训检测模型

  - 同模型生成的文本经同模型重写后，检测器召回率仍保持78%~83%，业务侧识别纯AI生成后改写的内容可直接复用现有主流检测器'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统AI文本检测基准仅对比人类原生文本和LLM直接生成文本，无法反映检测器在LLM重写人类内容场景下的真实性能，存在严重评估偏差。
### 方法关键点
构建ARB基准，包含1800条人类源文本（XSum、WritingPrompts、OpenWebText各600条），搭配Llama-3.2-3B、Qwen2.5-7B等4个开源生成模型，为每条样本生成4类匹配变体：人类原生（HUMAN）、LLM直接生成（Free-LLM）、LLM重写人类文本（H2L）、同模型重写自身生成文本（LLM2L）；在1%误报率的严格工作点下评估5款主流开源检测器的TPR@1%FPR。
### 关键结果数字
Top2检测器对直接LLM生成文本的召回率达91.2%~93.5%，但对H2L样本召回率骤降60~78个百分点至15.1%~30.8%；对LLM2L样本召回率仅下降10~13个百分点，保持78.3%~83.0%；BERT类检测器在所有场景下召回率均低于3%。

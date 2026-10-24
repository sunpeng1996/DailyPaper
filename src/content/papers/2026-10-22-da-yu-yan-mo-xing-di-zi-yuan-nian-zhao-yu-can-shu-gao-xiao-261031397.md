---
title: 'Parameter-Efficient Adaptation of Large Language Models to a Low-Resource
  Agglutinative Language: A Corpus, Datasets, and a Reproducible Benchmark for the
  Bashkir Language'
title_zh: 大语言模型低资源黏着语参数高效适配：巴什基尔语语料与可复现基准
authors:
- Mullosharaf K. Arabov
- Svetlana S. Khaybullina
affiliations:
- Kazan (Volga Region) Federal University
arxiv_id: '2610.31397'
url: https://arxiv.org/abs/2610.31397
pdf_url: https://arxiv.org/pdf/2610.31397
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: LLM低资源语言参数高效适配
tags:
- Low-resource LLM
- QLoRA
- Continual Pre-training
- Tokenizer
- Benchmark
one_liner: 发布巴什基尔语开源语料数据集，系统评测低资源黏着语LLM适配方案效果
practical_value: '- 面向小语种跨境电商/推荐场景做LLM适配时，优先选择QLoRA方案搭配同语系预训练基座，效果优于编码器模型全微调

  - 小语种适配前先测试tokenizer fertility指标，该指标与最终适配效果正相关，优先选择同语系预训练的tokenizer

  - 低资源场景下持续预训练(CPT)收益和基座强相关，不要盲目上线，先做小范围AB验证，通用基座(如Mistral)的CPT提分更明显'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
巴什基尔语是西里尔书写的低资源黏着语，现有LLM对其支持度极低，缺乏公开适配基准与语料资源。

### 方法关键点
构建包含7.16万文档、46.9M token的巴什基尔网页语料库，以及3个文本分类标注数据集；在8种82M~8B参数量基座上，系统评测全微调、QLoRA、上下文学习三类适配方案，以及持续预训练(CPT)的增益。

### 关键结果数字
- 3.8~8B模型QLoRA适配在二分类任务上超过编码器基线，带CPT的YandexGPT-5-Lite-8B macro-F1达0.748，较XLM-R、mBERT高近10pct，统计显著
- 同参数级下有俄语预训练的YandexGPT效果优于Mistral-7B、Phi-3-mini，多分类任务人工评分高30%以上
- CPT对Mistral-7B二分类任务macro-F1提升达4.0pct，tokenizer fertility差异最高达2.67倍且与适配效果正相关

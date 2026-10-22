---
title: 'Every Part Has Its Role: Part-of-Speech Effects in LLM Post-Training'
title_zh: 各司其职：大语言模型后训练中的词性效应研究
authors:
- Laya Iyer
- Chen Shani
affiliations:
- Stanford University
- Tel Aviv University
arxiv_id: '2610.29843'
url: https://arxiv.org/abs/2610.29843
pdf_url: https://arxiv.org/pdf/2610.29843
published: '2026-10-21'
collected: '2026-10-22'
category: Training
direction: LLM后训练 · 概念增强优化
tags:
- Post-Training
- Concept Augmentation
- Part-of-Speech
- LoRA
- Llama-3
- Perplexity
one_liner: 揭示不同词性概念增强对LLM后训练的效果差异，验证动词增强可带来最稳定的下游任务收益
practical_value: '- 做领域LLM后训练的数据增强时，优先做动词的同义词/上位词替换，比全词性替换收益更稳定，尤其适配商品分类、评论情感识别、用户意图识别等电商/推荐类下游任务

  - 选择概念增强的替换源时，新闻/用户评论类语料优先用字典类超/同义词替换，科学文献类语料可考虑上下文感知的替换策略，能降低下游LoRA微调的收敛成本

  - 不要把perplexity作为后训练效果的唯一评估指标，perplexity降低和下游任务收益的相关性仅为0.3-0.38，需要结合业务任务的小样本验证选择增强策略

  - 做Agent意图理解模型增强时，优先针对动词做概念增强，能在不明显改变预训练原表征的前提下提升下游意图识别准确率，减少知识遗忘'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统LLM后训练的NTP损失仅针对单个token优化，无法利用同义/近义概念的语义关联；现有概念增强方案多仅针对名词优化，未考虑不同词性的语义结构差异对增强效果的影响，无法指导业务场景下的定制化增强策略设计。

### 方法关键点
- 基于Llama-3-8B开展后训练，仅使用数据增强优化，不修改NTP损失，隔离词性变量的影响
- 设计4类增强对照组：仅替换名词、仅替换动词、仅替换形容词、全词性替换，每类支持同义词/上位词两种语义关系，以及上下文感知生成/字典抽取两种概念来源
- 下游任务统一采用LoRA做序列分类微调，对比匹配训练量级的vanilla后训练基线，排除数据量干扰

### 关键结果
- 训练语料覆盖arXiv、新闻、YouTube评论3个领域，下游任务包含GLUE、SNLI、评论分类等7个基准
- 新闻领域概念增强平均降低perplexity 5.5%，arXiv领域反而升高8.2%；动词增强在8类语义关系×语料的组合中6类取得最优下游收益，平均准确率最高提升4.5%
- perplexity降低与下游准确率提升的相关性仅为0.3-0.38；全词性增强带来的表征变化最大（CKA最低0.743）但未取得最优下游效果，动词增强表征最接近基线（CKA 0.810）但收益最稳定

### 核心结论
概念增强的收益不取决于表征变化的幅度，而取决于变化的语义信息类型，针对性的词性增强效果优于全词性无差别增强

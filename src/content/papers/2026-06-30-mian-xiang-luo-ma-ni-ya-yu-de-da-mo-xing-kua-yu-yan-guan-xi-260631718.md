---
title: 'Cross-lingual Relation Extraction with Large Language Models: Zero-Shot, Few-Shot,
  and Fine-Tuned Evaluation on Romanian'
title_zh: 面向罗马尼亚语的大模型跨语言关系抽取：零/少样本及微调评估
authors:
- Dragos-Mitrut Vasile
- Elena-Simona Apostol
- Stefan-Adrian Toma
- Adrian Paschke
- Ciprian-Octavian Truica
affiliations:
- National University of Science and Technology POLITEHNICA Bucharest
- Military Technical Academy ‘Ferdinand I’
- Freie Universität Berlin
- Fraunhofer Institute for Open Communication Systems
- Academy of Romanian Scientists
arxiv_id: '2606.31718'
url: https://arxiv.org/abs/2606.31718
pdf_url: https://arxiv.org/pdf/2606.31718
published: '2026-06-30'
collected: '2026-07-02'
category: Eval
direction: 跨语言NLP · 低资源语言LLM性能评估
tags:
- Cross-lingual Relation Extraction
- QLoRA
- Low-resource NLP
- LLM Evaluation
- Zero-shot Learning
- Few-shot Learning
one_liner: 测评罗马尼亚语跨语言关系抽取下不同配置大模型与小参数基线的性能与资源效率
practical_value: '- 低资源语言语义理解任务可先测小参数单语种BERT类基线，无需盲目上大模型，大幅降低推理成本

  - 跨语言任务标注数据不足时，可先用LLM翻译现有高资源语言基准数据集，快速完成冷启动测评

  - 单任务语义理解场景下，小参数Encoder模型微调后性能可逼近几十倍参数的LLM，资源受限场景优先选用

  - 跨语言任务存在明显性能gap时，可通过QLoRA微调大模型快速缩小不同语言间的性能差'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
低资源语言关系抽取（RE）任务普遍受标注语料匮乏限制，缺乏不同模型配置下的性能对比与选型参考。
### 方法关键点
基于LLM翻译流水线将SemEval-2010 Task 8英文基准数据集翻译为罗马尼亚语，分别测试零样本、少样本、QLoRA微调的Gemma 4 31B性能，与125M~560M参数的4种Encoder基线（XLM-RoBERTa、罗马尼亚语BERT等）在实体标记关系分类、端到端抽取两种任务范式下做对比。
### 关键结果数字
纯Prompt场景下罗马尼亚语比英语性能低3~5pp，少样本相比零样本增益有限；QLoRA微调可将两种语言的macro F1提升22pp以上，跨语言gap从3.3pp降至1.4pp；小参数Encoder基线比Gemma 31B小50~250倍，性能仅低1~4pp，125M罗马尼亚语BERT性能与278M多语言XLM-R持平，计算敏感场景无需用大参数LLM做单任务RE

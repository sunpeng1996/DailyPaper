---
title: 'Language-Specific versus Cross-Lingual Knowledge Graphs for Implicit Aspect
  Identification in Arabic: A Comparative Study of Reasoning and Adaptation Strategies'
title_zh: 阿拉伯语隐式方面识别的单语与跨语言知识图谱对比研究
authors:
- Lujain A. Alawwad
affiliations:
- Saudi Electronic University
arxiv_id: '2607.20056'
url: https://arxiv.org/abs/2607.20056
pdf_url: https://arxiv.org/pdf/2607.20056
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: 低资源语言NLP · LLM适配与KG选型
tags:
- Low-resource NLP
- Knowledge Graph
- LoRA
- Zero-shot Prompting
- Cross-lingual Transfer
- ABSA
one_liner: 对比阿拉伯语隐式方面识别的单/跨语言KG与LLM适配策略，给出低资源语言任务选型依据
practical_value: '- 面向小语种电商评论情感分析任务，优先构建Native语言KG，比跨语言复用成熟英文KG的micro-F1最高可提升0.251

  - 形态丰富的小语种NLP任务中无需盲目堆大模型参数，优先做任务特定LoRA微调，效果远优于零样本Prompt

  - 小语种UGC的隐式语义识别（如商品评论隐式负面点挖掘）可复用「LLM抽取+KG推理」的混合Pipeline'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：低资源语言（如阿拉伯语）的隐式方面识别任务存在KG选型困境：是通过多语言嵌入复用成熟英文KG，还是构建小成本原生单语KG；同时LLM适配策略（零样本/微调）的效果差异也缺乏定量参考。
**方法**：在统一的「LLM抽取+KG推理」混合Pipeline下，控制变量对比两种KG选型方案，以及8B参数LLM的两种适配策略（零样本Prompt、任务特定微调），在3个阿拉伯语ABSA基准数据集上测试。
**结果**：原生阿拉伯语KG比跨语言英文KG在M-ABSA、SemEval-2016上分别提升0.199、0.251 micro-F1，精度召回双升；任务微调将显式抽取micro-F1从零样本的≤0.13提升至0.66~0.76，小语种任务中适配策略比模型规模更关键。

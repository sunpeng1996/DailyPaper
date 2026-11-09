---
title: Using an LLM to Tackle Difficult Cases in NER for Nepali Tweets
title_zh: 基于大语言模型的尼泊尔语推特命名实体识别难例处理
authors:
- Claire Wang
affiliations:
- Brandeis University
arxiv_id: '2611.08967'
url: https://arxiv.org/abs/2611.08967
pdf_url: https://arxiv.org/pdf/2611.08967
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: 低资源场景 LLM NER 难例优化
tags:
- NER
- Low-resource NLP
- LLM
- Prompt Engineering
- Ensemble Learning
one_liner: 提出PLM划分易/难例+LLM处理难例的混合NER方案，难例F1较基线提升近10个点
practical_value: '- 可复用「PLM处理易样本+LLM兜底难样本」的分级处理架构，在搜索query理解、评论实体识别等场景降低大模型推理成本，同时提升长尾case效果

  - 难例划分可直接复用「基于微调PLM的token概率阈值」方案，无需额外标注即可快速拆分样本难度，适配多种序列标注任务

  - 少样本prompt优化时优先选择语义相似示例、适当增加示例数量，可快速提升LLM序列标注任务效果，投入产出比高'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
低资源语言社交媒体数据噪声高、标注稀缺，NER任务难度大；微调PLM在难例上表现不佳，LLM整体性能弱于PLM但难例处理存在潜力。

### 方法关键点
1. 基于微调PLM输出的token概率将尼泊尔语推特测试集划分为易/难两类样本
2. 对比16种prompt配置下LLM处理难例的效果，验证PLM+LLM混合架构的性能

### 关键结果
- 采用语义相似示例选样+增加示例数量的prompt方案，LLM难例F1较基线提升近10个点
- LLM在全量/易样本集上性能弱于PLM，但难例集上效果反超PLM
- PLM+LLM混合方案整体性能优于单一PLM

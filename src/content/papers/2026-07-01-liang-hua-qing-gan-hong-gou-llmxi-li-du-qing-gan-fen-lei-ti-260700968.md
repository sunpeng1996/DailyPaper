---
title: 'Quantifying the Affective Gap: A Zero-Shot Evaluation of LLMs on Fine-Grained
  Emotion Taxonomies'
title_zh: 量化情感鸿沟：LLM细粒度情感分类体系零样本评估
authors:
- Lawrence Obiuwevwi
- Krzysztof J. Rechowicz
- Jessica M. Johnson
- Vikas Ashok
- Sachin Shetty
- Sampath Jayarathna
affiliations:
- Old Dominion University
arxiv_id: '2607.00968'
url: https://arxiv.org/abs/2607.00968
pdf_url: https://arxiv.org/pdf/2607.00968
published: '2026-07-01'
collected: '2026-07-02'
category: Eval
direction: LLM评测 · 细粒度零样本情感分类
tags:
- Emotion-Classification
- Zero-Shot
- LLM-Evaluation
- Claude
- GPT
- Gemini
one_liner: 统一零样本评测三大商用LLM细粒度情感分类能力，明确性能差异与当前天花板
practical_value: '- 电商用户评论/咨询的细粒度情感识别业务，不要直接依赖零样本商用LLM，其准确率天花板不足40%，建议补充few-shot示例或微调垂直小模型

  - 选择商用LLM做情感相关任务时，优先选择Gemini，零样本性能更高且类别平衡性优于Claude和GPT

  - 情感分类任务中，love/confusion/shame是通用LLM的共性薄弱项，建议针对这三类单独做样本增强或规则兜底

  - 对话Agent的情感响应模块可直接复用LLM在sarcasm/desire两类的识别能力，无需额外优化'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM情感能力评测多聚焦粗粒度极性或6种基础情绪，缺乏统一实验条件下的细粒度情感分类零样本跨模型对比，无法明确当前商用LLM的情感能力上限。
### 方法关键点
2026年4月统一调用Claude、GPT-5.4、Gemini三大商用LLM生产API，基于boltui/emotions数据集的1000条分层抽样句子，采用无示例统一prompt开展13类细粒度情感分类零样本评测。
### 关键结果
Gemini以39.9%准确率、0.363的macro-F1排名第一，其次为GPT-5.4（38.8%、0.291）、Claude（38.0%、0.159）；三类模型均擅长讽刺、欲望识别，在爱、困惑、羞耻三类上表现极差；统计检验显示三类模型性能无显著差异，已达到零样本细粒度情感分类的共同天花板，Claude存在明显类别不平衡预测偏差。

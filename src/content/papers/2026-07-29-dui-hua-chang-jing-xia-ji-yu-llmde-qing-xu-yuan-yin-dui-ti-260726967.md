---
title: Generation or Judgement? A Paradigm Perspective on LLM-Based Emotion-Cause
  Pair Extraction in Conversation
title_zh: 对话场景下基于LLM的情绪原因对提取：生成与判断范式对比
authors:
- Weijie Feng
- Hongchuang Wang
- Binbin Liu
- Zhiyong Cheng
affiliations:
- Hefei University of Technology
arxiv_id: '2607.26967'
url: https://arxiv.org/abs/2607.26967
pdf_url: https://arxiv.org/pdf/2607.26967
published: '2026-07-29'
collected: '2026-07-31'
category: LLM
direction: LLM任务范式优化 · 因果关系抽取
tags:
- LLM
- Task Paradigm
- Causal Relation Extraction
- Conversation Understanding
- Inference Optimization
one_liner: 对比对话情绪原因对提取的两种LLM范式，提出低开销辅助检索方案提升F1
practical_value: '- 做电商客服会话情绪归因、用户评论情感原因提取等LLM抽取任务时，优先选「候选召回+逐对判断」范式，比直接生成全量结果准确率更高

  - LLM输出的排序置信度比统一阈值的二分类判断更可靠，可针对排序边界的低置信度候选做二次校验，用极低推理开销换效果提升

  - 涉及多实体/多关系的生成任务，不要让LLM一次性输出全量结果，拆解为「候选召回+逐例判断+边界校验」架构可大幅降低漏召概率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
对话场景情绪原因对提取（ECPEC）现有LLM实现分为两类范式：对话级直接生成全量因果对、逐例判断候选对是否成立，二者性能差异的底层原因未明确，缺乏可落地的最优架构指导。
### 方法关键点
1. 开展18组受控对照实验，系统性对比两种范式的性能差异；
2. 定位范式差距根源：LLM可识别92.7%~98.1%的显式给出的因果对，但自主发现并输出完整全量对的能力较弱；
3. 针对判断范式统一二分类阈值的误判问题，新增辅助检索器选择性重检低置信度边界样本。
### 关键结果
判断范式在18组对照中全部优于生成范式；新增辅助检索器后，3个数据集的F1值稳定提升0.50~1.46个点，推理时间仅为基线判断范式的1.49倍

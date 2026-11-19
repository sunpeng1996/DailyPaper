---
title: 'Dreaming Up Authors: Factual Prevalence and LLM Hallucinations in Academic
  Authorship Attribution'
title_zh: 学术作者归属场景下LLM幻觉与事实流行度的关联研究
authors:
- Sijia Zhong
- Tamir Yirga
- Yijia Ma
- Thai Le
- Yifan Hu
affiliations:
- University of Texas at Arlington
- Northeastern University
- Indiana University
arxiv_id: '2611.23530'
url: https://arxiv.org/abs/2611.23530
pdf_url: https://arxiv.org/pdf/2611.23530
published: '2026-11-17'
collected: '2026-11-19'
category: LLM
direction: LLM幻觉成因 · 事实流行度关联分析
tags:
- Hallucination
- Factual Prevalence
- Citation Proxy
- Authorship Attribution
- LLM Evaluation
one_liner: 验证LLM幻觉率与事实流行度负相关，揭示低流行度事实幻觉源于检索瓶颈而非知识缺失
practical_value: '- 构建RAG知识库时可给实体/知识标注流行度权重，低流行度内容（如长尾商品、小众规则）优先触发RAG召回，降低参数记忆带来的幻觉

  - 做LLM生成内容校验时，对涉及低流行度实体的query（如小众商品咨询、长尾活动规则查询）提升校验强度，增加多轮交叉核验规则

  - 设计LLM Agent知识链路时，可依据查询对应实体的流行度动态调度路径，低流行度查询直接走外部检索，跳过参数记忆环节提升准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在知识密集场景易出现事实冲突类幻觉，严重影响高可靠性场景落地，但训练数据中事实的出现频率与幻觉的关联缺乏系统量化研究，且商用LLM训练数据不公开，难以直接开展分析，亟需可靠的代理指标和可复现的验证范式。

### 方法关键点
- 采用论文引用量作为事实流行度的代理指标，验证其与Google搜索热度、公开LLM预训练语料的n-gram出现频率均呈正相关，可用性优于搜索量、n-gram计数等指标
- 构建覆盖8个学科的1.92M篇学术论文数据集，分层抽取9108篇跨引用量级的样本用于评估
- 设计3种互补的幻觉率量化指标，覆盖不同错误模式，采用模糊字符串匹配实现全自动可复现的评估
- 通过多选识别实验、开源模型隐藏态探针分别验证幻觉成因和模型内部的流行度编码机制

### 关键实验结果
在GPT-4o、DeepSeek-R1、Claude Sonnet 4.5三款SOTA LLM上测试，结果显示：引用量0-2的低流行度论文幻觉率超98%，引用量4097+的高流行度论文幻觉率最低降至16.9%；二者的负相关关系在所有模型和学科中均统计显著，Spearman相关系数最高达-0.553；低流行度论文的多选识别准确率仍达79%，证明幻觉主要源于检索瓶颈而非参数知识缺失。

### 核心结论
LLM对长尾事实的错误大多不是真的未学习到相关知识，而是生成阶段的检索能力不足，针对低流行度内容优先触发外部检索是性价比最高的幻觉缓解方案

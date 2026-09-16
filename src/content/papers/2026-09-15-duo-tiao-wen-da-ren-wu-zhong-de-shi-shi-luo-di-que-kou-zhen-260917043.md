---
title: Diagnosing the Fact-Grounding Gap in Multi-Hop Question Answering
title_zh: 多跳问答任务中的事实落地缺口诊断研究
authors:
- Kevin Mo
- Nathan Mo
- Richard Zhu
affiliations:
- Independent
- Northwestern University
arxiv_id: '2609.17043'
url: https://arxiv.org/abs/2609.17043
pdf_url: https://arxiv.org/pdf/2609.17043
published: '2026-09-15'
collected: '2026-09-16'
category: RAG
direction: RAG错误诊断 · 多跳推理
tags:
- Multi-hop QA
- RAG
- Error Diagnosis
- Fact Grounding
- LLM Judge
one_liner: 发现多跳QA近半单跳缺陷为已检索文档缺所需事实的提取失败，配套低成本检测干预方案
practical_value: '- 多轮检索类Agent（如电商导购、多轮搜索）做错误诊断时，不要仅看召回是否命中相关文档，需新增事实存在性检测，避免召回率达标但实际缺失所需信息的问题

  - 可复用论文中的轻量DeBERTa分类器方案，用少量LLM打标数据训练即可实现实时事实缺失检测，成本远低于全链路LLM判分，适合线上触发重召回的判断依据

  - 多步推理RAG系统不要盲目对每一步都做召回增强/重排，仅针对检测到缺事实的步骤做干预，可节省近一半检索成本，还能避免无关上下文干扰后续推理

  - 若业务知识库覆盖度高（如电商标准商品库），提取失败占比低可优先优化召回；若为开放域、UGC类知识库，需额外关注事实落地缺口问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多跳问答、多轮RAG系统普遍默认「召回正确文档即可得到正确答案」，错误全归因于召回失败，从未系统验证已召回文档是否真的包含单步推理所需的具体事实。这导致大量优化资源投入召回却无法解决近半错误，且标准召回指标（如召回率、MRR）完全无法识别这类问题，尤其影响知识密集型Agent、多轮搜索系统的优化效率。

### 方法关键点
- 拆分两类单跳失败模式：召回失败（未命中黄金支撑段落）、提取失败（已命中黄金段落但缺失推理所需的具体关系事实，即事实落地缺口）
- 构造经人工验证的LLM事实存在性判分器（Cohen's κ=0.840），避免字符串匹配高估事实存在率的问题（高估幅度达10.7个百分点）
- 用LLM打标的单跳数据微调轻量DeBERTa-v3-large分类器，实现毫秒级单跳事实存在性预测，成本仅为LLM判分的几十分之一
- 设计选择性干预策略：仅对分类器判定缺事实的单跳做子问题改写重召回/扩大召回集重排，避免全链路干预带来的无关上下文干扰和成本浪费

### 关键实验
在MuSiQue、HotpotQA、2WikiMultihopQA三个标准多跳QA数据集上验证：MuSiQue数据集上提取失败占所有单跳缺陷的47%，所有召回优化手段都无法解决提取失败问题；针对性干预比全链路每步干预节省50%的检索调用量，准确率相当甚至更高（MuSiQue上重排干预准确率达60.3%，仅比全链路干预低0.6%）；DeBERTa分类器F1达0.785，准确率比基于召回分数的基线高11.3个百分点。

### 核心结论
仅靠召回优化存在明确天花板，即使是完美召回的系统也无法解决近一半的多跳推理错误，必须区分召回失败和提取失败两类问题分别优化。

---
title: 'Blind Men and the Elephant: Probing the Epistemic Myopia of LLMs under Long-Tail
  Divergent Knowledge'
title_zh: 盲人摸象：探究LLM在长尾分歧知识下的认知短视问题
authors:
- Zhuoshi Pan
- Junru Lu
- Yan Qian
- H. Vicky Zhao
- Di Yin
- Xing Sun
affiliations:
- Tsinghua University
- Tencent Youtu Lab
- University of Warwick
arxiv_id: '2608.28478'
url: https://arxiv.org/abs/2608.28478
pdf_url: https://arxiv.org/pdf/2608.28478
published: '2026-08-27'
collected: '2026-08-31'
category: Eval
direction: LLM知识记忆评测 · 分歧长尾知识
tags:
- LLM Evaluation
- Long-tail Knowledge
- Parametric Memory
- Benchmark
- Knowledge Conflict
one_liner: 提出ElephantBench闭卷评测基准，检测LLM参数记忆中长尾多源事实的完整召回能力
practical_value: '- 电商多源知识对齐场景可复用「知识聚类+实体匹配+LLM冲突判别」流水线，大幅降低多源事实冲突的识别成本

  - 构建业务域LLM评测集时，可借鉴其从低曝光语料挖掘多答案QA+权威源验证+人工审核的流程，提升评测集鲁棒性

  - 优化Agent事实回答能力时，优先提升长尾分歧知识的小众版本语料曝光，比单纯扩容模型/加推理步数的ROI更高

  - 预训练数据筛选阶段不要直接丢弃低分长尾语料，可从中挖掘分歧事实补充训练，缓解LLM认知短视问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统事实QA默认单标准答案，无法检测LLM Parametric Memory中是否同时保留了长尾事实的不同可信版本，导致LLM常出现仅记住主流版本、遗漏小众版本的认知短视问题；现有基准要么是单答案长尾QA，要么是开卷知识冲突评测，均无法实现闭卷场景下的Parametric Memory完整性检测。
### 方法关键点
- 基准构建流水线：先从低曝光网页语料中，通过知识点聚类+实体匹配召回候选文档对，再用LLM判断文档间的支持/冲突关系，构建全局文档图
- QA生成：基于冲突子图生成命名实体类、线索类两类QA，每个QA对应至少2个经权威公共源验证、人工审核的可信答案
- 评测规则：采用纯闭卷设置，模型仅能依赖Parametric Memory回答，用LLM-as-judge将结果分为完全召回、部分召回、失败召回三类，计算完整率等核心指标
### 关键结果
数据集包含1094条跨22个领域的多答案QA，覆盖32款主流LLM；最强模型Kimi-K3的完全召回率仅52.4%，剩余近47.6%的问题仅能召回单版本答案；模型规模扩容、开启推理仅能提升单版本召回率，无法消除认知短视；小众答案的语料曝光量每提升1个标准差，完全召回率提升15.13个百分点。
### 核心结论
LLM对长尾分歧知识的回答完整性，和小众版本的语料曝光量相关性远高于整体知识的曝光频率，单纯扩大模型规模、增加推理步数无法解决认知短视问题

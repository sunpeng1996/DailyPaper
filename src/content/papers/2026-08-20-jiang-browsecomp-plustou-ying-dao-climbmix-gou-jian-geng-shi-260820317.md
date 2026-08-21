---
title: 'Projecting BrowseComp-Plus onto ClimbMix: Toward More Realistic Corpora for
  Agentic Search'
title_zh: 将BrowseComp-Plus投影到ClimbMix：构建更真实的智能体搜索语料库
authors:
- Sahel Sharifymoghaddam
- Lingwei Gu
- Yijun Ge
- Jimmy Lin
affiliations:
- University of Waterloo
arxiv_id: '2608.20317'
url: https://arxiv.org/abs/2608.20317
pdf_url: https://arxiv.org/pdf/2608.20317
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: 智能体搜索 · 评估基准构建
tags:
- Agentic_Search
- Benchmark
- Corpus_Projection
- Retrieval_Evaluation
- ClimbMix
one_liner: 提出通用跨语料投影流水线，生成贴近真实场景的智能体搜索评估基准
practical_value: '- 多轮推理类业务Agent（如电商导购、客服、选品Agent）的评估可直接复用「问题拆分为原子推理跳→逐跳验证语料支撑性」的流水线，避免人工构造小语料导致的效果虚高，评估结果更贴近真实落地表现

  - 做垂直场景Agent检索评估时，可直接复用ClimbMix作为通用大规模背景语料库，替代自研小体量人工语料，更准确衡量召回组件的真实能力

  - Agent效果评估不要只看最终答案准确率，需搭配证据召回率、检索调用次数两个指标，才能区分是模型记忆了答案还是真的通过检索获得有效信息，尤其适合电商场景下的导购Agent评测

  - 语料标注时的近重复判断方法（MinHash+5-gram Jaccard≥0.7匹配）可直接复用在召回相关的qrels构建环节，提升标注覆盖率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
原有BrowseComp-Plus智能体搜索基准采用100K规模的人工构建语料，证据、负样本均围绕查询定向生成，与真实web检索的语料规模、分布差距极大，导致评估结果无法迁移到落地场景，也无法准确拆分智能体推理能力与检索组件的效果贡献。

### 方法关键点
- 通用跨语料投影流水线：将查询拆分为必选推理跳（缺失则答案不唯一）、可选验证跳，逐跳在目标语料中检索支撑证据，仅保留所有跳都有语料支撑的查询
- 四层校验机制：自动可回答性校验→独立Agent验证证据充分性→人工逐跳审核→基于MinHash+Jaccard≥0.7的近重复文档扩充标注，确保标注可靠性
- 采用NVIDIA发布的400B token、553M文档的ClimbMix通用预训练语料作为目标库，完全脱离基准构建的人工干预，更贴近真实检索场景

### 关键结果
- 830条原测试查询经过投影后最终保留57条有效查询，构成公开基准BrowseComp-PlusCM
- 最强GPT-5.6 Sol Agent在新语料上答案准确率仅下降5.3pp（从86.0%到80.7%），但证据召回率从84.3%暴跌到21.4%，检索调用次数增加63%；Gemma 4 31B、Qwen 3.5 9B等开源小模型的证据召回率不足3%
- 闭卷测试下GPT-5.6可答对70.2%的投影后查询，说明仅靠最终答案准确率无法区分模型是靠记忆还是检索得到结果

### 核心结论
小体量人工构建的检索评估语料会严重高估Agent的真实检索能力，真实落地场景下检索难度才是限制智能体搜索效果的核心瓶颈，而非推理能力。

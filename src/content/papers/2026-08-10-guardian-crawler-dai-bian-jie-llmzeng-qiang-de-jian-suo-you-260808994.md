---
title: 'Guardian Crawler: Retrieval-First Knowledge Discovery with Bounded LLM Augmentation
  for Noisy Web Intelligence'
title_zh: Guardian Crawler：带边界LLM增强的检索优先网页知识发现系统
authors:
- Joshua Castillo
- Santosh Nukavarapu
- Ravi Mukkamala
affiliations:
- Old Dominion University
arxiv_id: '2608.08994'
url: https://arxiv.org/abs/2608.08994
pdf_url: https://arxiv.org/pdf/2608.08994
published: '2026-08-10'
collected: '2026-08-11'
category: RAG
direction: RAG检索优先架构 噪声网页知识发现
tags:
- RAG
- Information Retrieval
- Grounded Generation
- Web Mining
- Testbed
one_liner: 提出检索优先、LLM角色受限的噪声网页知识发现测试床，实现高准度检索与带引用的可信生成
practical_value: '- 电商/广告敏感品类搜索排序可复用风险感知重排思路：在BM25基础上叠加领域合规/高价值关键词加权重排，优先召回合规、高相关性内容，提升敏感场景排序准确率

  - RAG系统可信度评估可复用双校验方案：先做确定性词汇覆盖快速过滤明显幻觉，再用LLM judge做语义级事实一致性校验，大幅降低幻觉漏判率

  - 检索/RAG系统ablation实验可复用固定候选池控制变量法：所有重排变体基于同一批BM25召回候选，排除召回差异干扰，精准衡量重排信号的真实增益

  - 可借鉴LLM角色受限架构设计：将LLM限定在标注、生成、评估三个边界明确的环节，不替代检索/排序核心链路，平衡生成能力和系统可控性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
噪声网页下的知识发现面临内容异构、无关信息多、生成结论易无依据等问题，尤其敏感领域实验用真实网页存在隐私伦理风险，现有检索+RAG方案缺乏可复现的可控测试环境，且普遍存在LLM滥用、检索和生成效果无法拆分评估的痛点。

### 方法关键点
- 构建可复现合成类网页语料库，模拟公告、新闻、噪声、无关四类页面，自带链接结构，完全可控标注，规避真实数据隐私问题
- 检索优先模块化架构：第一阶段固定用BM25做召回，第二阶段支持三类重排：风险感知重排（叠加领域风险关键词加权）、语义重排（query-文档embedding相似度加权）、混合重排（融合 lexical、风险、语义三类信号）
- LLM角色严格受限：仅用于语料生成、页面分类、带引用摘要生成、事实一致性评估四个边界清晰的环节，不参与核心召回排序链路
- 拆分评估逻辑：检索效果用P@10、NDCG@10衡量，生成事实性先做词汇覆盖校验，再用独立LLM judge做语义级支持度评估

### 关键结果
基于900篇合成文档、10个查询的测试集，对比BM25基线：BM25+风险重排（α=1.0）效果最优，P@10达1.00，NDCG@10达0.94，较基线的0.94、0.81大幅提升；最优混合重排NDCG@10也达0.94，BM25+语义重排最优NDCG@10为0.88；生成的41条摘要全部通过词汇覆盖校验，LLM judge判定87.8%完全符合事实，9.8%为无依据声明。

### 核心结论
检索优先、LLM角色边界明确的架构，在噪声场景下的效果和可控性远优于端到端生成方案，且检索和生成效果拆分评估是优化RAG系统可信度的核心前提

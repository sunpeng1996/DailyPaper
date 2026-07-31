---
title: 'EMBL AI Librarian: Life-Sciences Knowledge Layer for AI Agents'
title_zh: EMBL AI Librarian：面向AI Agent的生命科学知识层
authors:
- Luigi Sigillo
- Matteo Silvestri
- Francesco Tabaro
- Rajat Bhatnagar
- Syed Irtaza Mubashar
- Matt Jeffryes
- Daljit Nijjer
- Vittorio Perera
- Ola Spjuth
- Julio Saez-Rodriguez
affiliations:
- EMBL Rome
- EMBL-EBI
- Sapienza University of Rome
- Uppsala University
- Heidelberg University
arxiv_id: '2607.28229'
url: https://arxiv.org/abs/2607.28229
pdf_url: https://arxiv.org/pdf/2607.28229
published: '2026-07-30'
collected: '2026-07-31'
category: Agent
direction: Agent 垂直领域知识检索层设计
tags:
- Agent
- RAG
- Retrieval
- Knowledge Layer
- LLM Orchestration
one_liner: 复用现有生命科学文献检索引擎，打造Agent友好的自然语言知识检索层
practical_value: '- 搭建垂直领域Agent知识层时，可直接复用现有成熟的结构化检索基础设施（如电商商品库、广告素材库），无需从零搭建全量向量库，大幅降低存储与运维成本

  - 检索pipeline可采用「LLM生成多组互补结构化子query → 调用现有检索引擎召回 → 段落级BM25排序 → LLM过滤重排提取证据片段」的架构，兼顾召回率与精准度

  - 优化LLM调用成本时，可让LLM输出段落/句子ID而非重写全文，大幅减少解码token数，同时降低响应延迟

  - 垂直领域检索可优先尝试「结构化检索+LLM编排」方案，当前大模型能力下该方案性价比普遍优于全量稠密向量检索'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有垂直领域检索工具多面向人类设计，AI Agent使用时需要学习复杂查询语法、多次检索、通读全文，token成本极高；而常用的稠密向量库方案需要海量存储、丢弃结构化元数据、可解释性差，不适配Agent的轻量化检索需求。

### 方法关键点
- 无自有索引，直接对接Europe PMC实时检索能力，复用其4000万+文献的结构化检索（支持基因、蛋白、疾病等字段过滤）能力
- 三段式检索流程：1）LLM生成最多7组互补的结构化子query，经语法校验后执行；2）召回的论文拆分为段落，结合所属章节信息做BM25排序，每篇保留最高的16段+摘要；3）LLM批量过滤重排段落，输出带引用元数据的证据片段，调用时仅返回句子ID降低解码成本
- 模型无关，可替换任意基座LLM，新模型能力提升直接带动检索效果增益

### 关键结果
在4个基准测试上均大幅超越基线：ScholarQA-Bench文献合成任务Citation F1比SOTA基线高16+分；ProClaim声明校验任务比原检索层提升5个百分点的专家共识匹配度；LitQA2开放问答任务比GPT-5.4+网页搜索高8.6个准确率点；LAB-Bench生物任务中GPT-5.4使用后平均准确率提升4.2个点，序列操作任务提升11.3个点。

### 核心结论
垂直领域Agent的知识检索不需要重复造轮子，复用现有成熟的结构化检索基础设施+LLM编排的方案，性价比远超自建全量稠密向量库。

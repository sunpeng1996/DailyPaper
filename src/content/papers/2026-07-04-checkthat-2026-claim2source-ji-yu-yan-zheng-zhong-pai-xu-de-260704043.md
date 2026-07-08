---
title: 'Claim2Source at CheckThat! 2026: Improving Multilingual Scientific Claim-Source
  Retrieval with Verification-based Re-Ranking'
title_zh: CheckThat! 2026 Claim2Source：基于验证重排序的多语言科学声明来源检索优化
authors:
- Tobias Schreieder
- Harsh Khandelwal
- Yu-Ling Zhong
- Michael Färber
affiliations:
- TU Dresden & ScaDS.AI Dresden/Leipzig
- Friedrich-Alexander University of Erlangen–Nuremberg
arxiv_id: '2607.04043'
url: https://arxiv.org/abs/2607.04043
pdf_url: https://arxiv.org/pdf/2607.04043
published: '2026-07-04'
collected: '2026-07-08'
category: RAG
direction: RAG 多语言检索 · 验证式重排序
tags:
- Cross-lingual Retrieval
- Re-ranking
- Fact Verification
- Dense Retrieval
- Metadata Enhancement
one_liner: 提出融合双语表示、元数据增强与双阶段重排序的多语言来源检索框架，登顶CheckThat!2026赛道榜首
practical_value: '- 跨语言业务场景可复用「双语Query表示+语言专属适配微调dense检索模型」的设计，适配多站点跨语种商品/内容召回需求

  - 多阶段检索架构可新增「验证式重排序」模块：在相似度重排后引入业务相关性验证信号（如商品属性匹配度、内容合规性校验）提升TopK准确率

  - 召回侧可引入源侧元数据增强表示：电商场景可融合商品标题、属性、销量等结构化元数据优化item embedding，缓解Query与item语义错配问题'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
多语言科学声明来源检索任务中，社交平台传播的声明和原始文献存在语言、措辞、细节粒度差异，语义错配问题突出，检索准确率低。
### 方法关键点
提出多阶段渐进式优化的检索框架：1）表征层：采用双语声明表征、元数据增强的源文献表征，对dense检索模型做语言专属适配，解决跨语言检索难点；2）召回层：第一阶段基础检索生成候选池；3）重排序层：先做相似度重排序提升高相关源的排名，再新增验证式重排序环节，引入验证信号筛选最匹配的支撑源。
### 关键结果
在英语、德语、法语多语言测试集上平均MRR@5达0.7628，位列CheckThat! 2026任务1排行榜第一名。

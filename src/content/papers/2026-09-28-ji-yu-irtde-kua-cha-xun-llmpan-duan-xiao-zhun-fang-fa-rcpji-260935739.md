---
title: 'Rubric-Calibrated Preferences: Cross-Query Calibration of LLM Judgments via
  Item Response Theory'
title_zh: 基于IRT的跨查询LLM判断校准方法RCP及检索评估指标RCP-nDCG
authors:
- Fabian David Schmidt
- Donato Crisostomi
- Carlos Lassance
- Nils Reimers
affiliations:
- Cohere
arxiv_id: '2609.35739'
url: https://arxiv.org/abs/2609.35739
pdf_url: https://arxiv.org/pdf/2609.35739
published: '2026-09-28'
collected: '2026-09-29'
category: Eval
direction: 检索评估 · LLM Judge 跨查询校准
tags:
- LLM-as-Judge
- Item Response Theory
- Reranking Evaluation
- nDCG
- Calibration
one_liner: 结合LLM相对排序偏好与绝对评分规则，通过IRT实现跨查询检索判断校准，输出连续可比的 relevance 标签
practical_value: '- 电商搜索/推荐多场景排序评估可直接复用RCP框架：自定义业务相关的二元评分规则（如相关性、性价比、合规性维度），即可校准跨query的LLM
  judge排序结果，解决传统人工标注稀疏、nDCG易饱和失效的问题

  - 做LLM-as-Judge评估时，可复用「listwise Bradley-Terry锦标赛排序+IRT跨组校准」技术链路，既能保留单query内的细粒度排序差异，又能实现不同query、不同业务场景的评估得分可比，适配多业务线统一效果衡量的需求

  - Reranker模型迭代的效果验证可替换传统qrel-nDCG为RCP-nDCG，在不增加人工标注成本的前提下，可多区分近1倍的Reranker效果差异，加速模型迭代的效果校验效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统nDCG依赖稀疏离散的人工 relevance 标注，在Reranker效果趋近的当下极易出现饱和、地板效应、分数压缩问题，45.6%的NanoBEIR查询和30.7%的BRIGHT查询存在上述失效情况。LLM judge的相对排序判断可区分细粒度差异但跨query不可比，绝对评分跨query可比但粒度过粗，亟需融合两者优势的校准方案。
### 方法关键点
- Stage A：对每个query的候选文档做listwise Bradley-Terry锦标赛排序，通过窗口式LLM rerank得到单query内的细粒度相对得分，保留query内排序顺序
- Stage B：用5个严格度递增的二元评分规则（主题匹配、信息有用性、实体匹配、直接回答、深度覆盖）对文档做绝对评分，生成跨query统一的锚定信号
- 校准层：通过2参数Item Response Theory（IRT）模型，将单query相对得分通过查询级缩放、偏移参数映射到跨query统一的logit尺度，输出连续校准的 relevance 概率
- RCP-nDCG：用校准后的连续概率替代传统nDCG的离散标注作为增益值，计算评估得分
### 关键结果
在13个NanoBEIR数据集、12个BRIGHT任务、TREC-DL、ViDoRe v3上验证，对比传统qrel-nDCG：1. 跨query与人类标注相关性的Spearman系数从原始BT得分的0.538提升至0.795；2. 区分有用/无用文档的AUC达0.910，远高于qrel的0.651；3. 72.4%的人工与指标分歧场景下RCP-nDCG判断正确；4. NanoBEIR上可区分的Reranker对数量是传统nDCG的1.9倍。
> 核心结论：仅需一套业务自定义的二元评分规则，即可通过IRT校准得到跨场景可比、高对齐人类偏好的连续 relevance 标签，大幅降低排序模型迭代的评估成本

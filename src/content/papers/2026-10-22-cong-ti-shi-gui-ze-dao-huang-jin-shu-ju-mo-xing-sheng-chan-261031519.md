---
title: 'From Prompt Rules to Golden Data Model: Production-Scale Generation of Personalized,
  Compliant Pharmaceutical Claims'
title_zh: 从提示规则到黄金数据模型：生产级合规个性化医药宣传语生成
authors:
- Suyash Mishra
- Qiang Li
- Subhabrata Adak
- Upender Phogat
- Srikanth Patil
- Satyanarayan Pati
affiliations:
- Roche
- Accenture
- Involead
arxiv_id: '2610.31519'
url: https://arxiv.org/abs/2610.31519
pdf_url: https://arxiv.org/pdf/2610.31519
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: LLM 受控生成 · 工业级落地架构
tags:
- RAG
- Controlled Generation
- Golden Data Model
- LLM Deployment
- Compliance Generation
one_liner: 将合规个性化信号从提示层转移到检索时元数据，提升医药宣传语生成质量并降低生产部署成本
practical_value: '- 做高合规要求的生成场景（如电商合规广告、营销话术生成）时，无需堆砌prompt规则，将合规、人群、场景等约束下沉到检索层的元数据过滤，比提示工程更稳定可扩展

  - 可复用6C多维度质量评分框架，针对业务内容资产做量化打分，检索时优先召回高分内容，大幅降低下游生成的hallucination风险和人工审核成本

  - 成本优化可参考：提升首次生成准确率减少用户重复请求，即使单请求成本小幅上升，整体总成本仍可下降，适合电商营销文案、个性化push文案等需反复调试的场景

  - 内容资产治理可复用方案：对历史物料做语义去重、关联构建、结构化打标，形成统一黄金数据层，是RAG类生成系统效果的核心底座，ROI高于换大模型、调prompt'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
医药等强监管行业用LLM生成宣传话术时，传统基于prompt规则的方案存在三大痛点：一是prompt规则堆砌到一定量级后逻辑冲突、可扩展性差，易出现人群错配、内容不符合合规要求、相关性低等问题；二是生成质量不稳定，用户需要反复提交请求调试，拉高API成本；三是历史已过审的内容资产复用率低，优质变体没有被充分利用。
### 方法关键点
1. 构建Golden Data Model（GDM）：整合1867条已过审医药宣传语的全链路元数据，包括引用来源、受众标签、物料类型、使用历史、变体（MTV）关联关系，以及6C质量评分（Clarity、Completeness、Consistency、Connectivity、Compliance、Context）。
2. 混合检索架构：将原prompt层的合规、人群、场景约束下沉到检索层，采用「语义相似度+元数据过滤+使用信号」的混合召回，再基于6C评分和历史使用量重排，确保召回的内容100%符合要求。
3. 生成层仅基于召回的合规内容做适配性改写，每条内容自带专属guardrail，避免hallucination。
### 关键结果
数据集为罗氏4款药物的1867条美国市场已过审宣传语，对比基线为原规则prompt方案：适应症匹配率提升29%，内容类型匹配率提升62%，目标受众匹配率提升67%，6C质量分提升86%，宣传语变体复用率提升34%，周API总成本下降29.5%，请求成功率从99.2%提升至100%。
### 核心结论
在监管严格、可控性要求高的生成场景，将约束信号从prompt层转移到检索时的结构化元数据过滤，是比堆prompt规则、换更大模型ROI更高的优化方向。

---
title: Towards Full-Text Scholarly Argument Mining using Entity-Anchored Claim Extraction
title_zh: 基于实体锚定主张提取的全文学术文献论点挖掘方法
authors:
- Bhuvanesh Verma
- Andy Lüking
- Mounika Marreddy
- Leon Lukas Hammerla
- Alexander Mehler
affiliations:
- Text Technology Lab, Goethe University Frankfurt
- Fakultät für Germanistik, Technische Universität Chemnitz
arxiv_id: '2610.40196'
url: https://arxiv.org/abs/2610.40196
pdf_url: https://arxiv.org/pdf/2610.40196
published: '2026-10-29'
collected: '2026-10-31'
category: LLM
direction: LLM 学术文本论点挖掘优化
tags:
- Argument Mining
- Entity Anchoring
- LLM Ensemble
- Silver Standard Dataset
- Scholarly Text Analysis
one_liner: 采用科学实体锚定+LLM多数投票生成银标数据，解决学术文献论点挖掘标注与长依赖难题
practical_value: '- 低标注资源场景可复用多LLM多数投票生成银标数据集的方案，替代小批量人工标注，降本同时提升模型效果

  - 长文本信息抽取任务可采用领域实体作为锚点定位目标片段，降低长距离依赖建模难度，可迁移到电商评论观点抽取、商品卖点挖掘等场景

  - 跨领域抽取场景可复用实体锚定的抽取范式，提升零样本迁移效果，适合跨品类评论分析、广告文案合理性校验等需求'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
全文学术文献论点挖掘面临两大核心痛点：一是长文本长距离依赖建模难度高，二是句级论点组件的全文档标注成本极高，现有研究多聚焦摘要或单章节内容，无法覆盖全文场景。
### 方法关键点
1. 提出科学实体锚定范式，以任务、数据集、模型等领域实体为锚点，定位并结构化提取文献中的主张内容
2. 标注50篇情感分析领域全文论文，构建Krippendorff's α=0.80的高可靠人工金标数据集，包含113条主张句、199条结构化主张记录
3. 采用多LLM多数投票集成策略生成含1487条主张的银标数据集，破解标注瓶颈
### 关键结果
仅在银标数据集上微调的编码器，效果优于基于小批量人工金标数据训练的模型，且对训练语料外的NLP论文具备较强零样本迁移能力

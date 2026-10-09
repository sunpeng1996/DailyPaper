---
title: 'Project Greenhouse: Progress Toward Fully Open and Sovereign Agentic Search'
title_zh: 温室计划：构建完全开源可自主掌控的智能搜索系统进展
authors:
- Jimmy Lin
- Sahel Sharifymoghaddam
- Lingwei Gu
- Nour Jedidi
affiliations:
- University of Waterloo
arxiv_id: '2610.11922'
url: https://arxiv.org/abs/2610.11922
pdf_url: https://arxiv.org/pdf/2610.11922
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: 智能搜索 · 开源可控重排器构建
tags:
- Agentic Search
- Reranker
- Open-source LLM
- Sovereign AI
- LLM4IR
one_liner: 仅用少量GPU从零训练出性能媲美主流方案的开源可控点式重排器，支撑自主智能搜索落地
practical_value: '- 垂直场景自研轻量重排器可复用两步训练范式：先用公开通用语料从零预训练，再基于领域标注数据微调，仅需少量GPU即可达到媲美第三方开源重排器的效果，规避第三方依赖的合规、定价变动风险

  - 电商搜索/广告推荐场景可直接接入Gaggle点式重排器，对召回的商品/广告候选集做二次排序，尤其适合对数据安全要求高、无法调用外部重排服务的业务

  - 需全链路可控的业务可参考论文提出的LLM训练超图溯源方法，清晰管控训练全链路的数据源、代码、配置依赖，满足等保、数据合规要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前主流智能搜索组件多依赖第三方开源预训练基座，存在数据授权不透明、服务稳定性不可控、合规风险高等问题，中小团队也缺乏低成本从零训练高性能搜索组件的可行路径，亟需完全开源、全链路自主可控的智能搜索构建方案。
### 方法关键点
- 采用两步无第三方依赖训练范式：第一步基于公开ClimbMix语料从零预训练因果语言模型，第二步基于RLHN-250K公开查询-文档相关性标注数据做有监督微调，全程不依赖第三方预训练基座。
- 采用model soup权重融合策略，平均4次微调试验的权重得到最终Gaggle重排器，降低训练波动，提升效果稳定性。
- 采用点式重排逻辑，独立对每个<query, document>对打分排序，训练和推理复杂度低，易集成到现有检索pipeline中。
### 关键结果
- 评测覆盖TREC Deep Learning 2019-2023、7个BEIR公开检索数据集，核心指标为nDCG@10，对比BM25、MonoT5、Qwen3-Reranker、GPT-6.1 Sol等10+ baseline。
- 3B参数的Gaggle重排器在TREC DL数据集上平均nDCG@10达0.641，超过所有对比的开源重排方案，仅略低于GPT-6.1 Sol的0.653；在BEIR数据集上平均nDCG@10达0.547，性能与26B参数的Gemma-4相当。
- 全流程算力要求极低：微调仅需单张现代GPU，预训练仅需8卡H100即可完成，中小团队可轻松复现。
> 最值得记住的一句话：面向垂直场景的专用大模型不需要盲目追求大参数量、依赖第三方基座，仅用少量计算资源从零训练即可达到媲美主流方案的效果，还能实现全链路自主可控。

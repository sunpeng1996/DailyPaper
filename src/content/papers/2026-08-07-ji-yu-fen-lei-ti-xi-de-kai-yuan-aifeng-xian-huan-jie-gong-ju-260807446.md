---
title: Taxonomy-Driven Analysis of Open-Source AI Risk Mitigation Tools
title_zh: 基于分类体系的开源AI风险缓解工具分析
authors:
- Afreen Alam
- Evgenija Popchanovska
- Ana Gjorgjevikj
- Maryan Rizinski
- Lubomir T. Chitkushev
- Irena Vodenska
- Dimitar Trajanov
affiliations:
- Boston University
- Ss. Cyril and Methodius University, Skopje
arxiv_id: '2608.07446'
url: https://arxiv.org/abs/2608.07446
pdf_url: https://arxiv.org/pdf/2608.07446
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: LLM风险治理 · 开源工具能力评估
tags:
- LLM Risk Governance
- Open-source Tool
- Taxonomy Mapping
- RAG
- Risk Mitigation
one_liner: 基于MIT AI风险分类体系映射21款开源LLM安全工具能力，明确覆盖缺口并给出自动化评估协议
practical_value: '- 落地LLM驱动的推荐/Agent业务时，可直接复用本文的MIT风险分类体系梳理业务风险点，匹配对应开源工具降低安全合规成本

  - 做内部工具能力自动化盘点时，可借鉴文中的LLM+RAG分析源码/文档提取能力的方案，替代人工梳理提升效率

  - 搭建企业级GenAI治理框架时，可参考文中结论优先补全治理、合规类工具缺口，搭配人工管控形成多层防护'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
企业LLM规模化落地后，人工风险识别与缓解难以扩展，开源安全/评估工具碎片化，技术描述与治理风险分类不匹配，难以快速匹配工具与风险、识别能力缺口。
### 方法关键点
基于扩展的MIT AI风险缓解与响应分类体系（32个子类），构建LLM辅助RAG pipeline，自动分析21款主流开源LLM评估、安全工具的源码与文档，提取能力并完成分类映射，搭配3名独立评审做可靠性校验。
### 关键结果数字
映射协议经多数投票后F1达75.5%，评审间一致性Fleiss' Kappa=0.509；现有开源工具集中覆盖技术、运营类控制能力，治理、合规、金融市场类风险控制能力存在明显缺口。

---
title: Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter
  Data
title_zh: 面向工业智能电表数据的隐私保护自然语言访问方案
authors:
- Carlos Martín-Abellán
- Mark Kröll
affiliations:
- Valencian Research Institute for Artificial Intelligence (VRAIN)
- Universitat Politècnica de València
- Know Center Research GmbH
arxiv_id: '2611.09372'
url: https://arxiv.org/abs/2611.09372
pdf_url: https://arxiv.org/pdf/2611.09372
published: '2026-11-06'
collected: '2026-11-09'
category: MultiAgent
direction: 多智体协同 · 隐私约束下本地LLM应用
tags:
- Multi-Agent
- LLM Orchestration
- Text-to-SQL
- Privacy-Preserving
- Local Deployment
one_liner: 提出无模式依赖的多智体系统OpenMeter，支持本地运行的智能电表数据自然语言查询兼顾隐私与易用性
practical_value: '- 针对电商用户行为、交易等敏感数据的内部查询场景，可借鉴本地部署多Agent协同的Text-to-SQL架构，避免敏感数据出域满足合规要求

  - 资源受限的本地硬件上优先采用全多Agent编排方案，可获得6.1pp的准确率提升；算力充足的云端场景可按需裁剪Agent组件平衡成本与效果

  - 搭建内部运营类自然语言查询工具时可采用schema无关设计，降低不同业务数据库的适配成本，大幅降低非技术人员的数据分析门槛'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
1. 工业智能电表数据规模大、结构异构，非技术电网运营人员查询分析需要专业SQL与数据工程能力，使用门槛极高；
2. 智能电表涉及用户隐私数据，受能源基础设施监管约束无法上传至云端LLM处理，存在数据安全与分析效率的核心矛盾。

### 方法关键点
提出schema无关的多智体系统OpenMeter，可将用户自然语言查询自动转换为可执行SQL，同时输出可读性强的分析结论，整套架构支持完全本地部署，无需调用云端LLM，严格满足隐私合规要求。

### 关键结果
资源受限的本地硬件上，全多Agent编排方案相比最优单Agent配置的EX-R指标提升6.1pp；算力充足的大规模场景下可按需选择组件，全编排的额外成本仅在隐私要求本地执行的场景下具备性价比。

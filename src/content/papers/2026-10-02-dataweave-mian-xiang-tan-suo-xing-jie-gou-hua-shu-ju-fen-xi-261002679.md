---
title: 'DataWeave: Deploying Human-LLM Analytics for Exploratory Structured Data Analysis'
title_zh: DataWeave：面向探索性结构化数据分析的人机协同LLM系统
authors:
- Raquib Bin Yousuf
- Harith Laxman
- Vitaliy Shkremetko
- Eunice Son
- Shambhavi Verma
- Brian O'Leary
- Venketesh Subramony
- Sylvain Nazef
- Jacquelyn Elias
- Ron Coddington
affiliations:
- Virginia Tech
- The Chronicle of Higher Education
arxiv_id: '2610.02679'
url: https://arxiv.org/abs/2610.02679
pdf_url: https://arxiv.org/pdf/2610.02679
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: 人机协同 LLM 结构化数据分析
tags:
- Human-LLM Collaboration
- Structured Data Analysis
- Schema Grounding
- SQL Generation
- Exploratory Analysis
one_liner: 提出面向探索性结构化数据分析的人机协同LLM系统DataWeave，沉淀落地设计原则与实践经验
practical_value: '- 做电商交易、用户行为等结构化数据的自然语言查询系统时，不要做端到端黑盒输出，可将LLM生成的schema匹配、分析计划、SQL中间态暴露给运营/分析人员编辑修正，大幅降低幻觉

  - 针对频繁更新的业务库（如实时商品库、流量统计库）的schema漂移问题，可复用schema grounding+人工校验的闭环流程，提升结构化查询准确率

  - 落地领域专用LLM分析系统时，可参考其迭代式架构优化思路，先做小范围核心用户测试再逐步推广，沉淀适配业务的设计原则'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
数据新闻等领域的探索性结构化数据分析需处理多源、多变量、schema频繁更新的数据集，分析师需掌握专业编码能力，效率极低；现有LLM直接生成SQL/答案的方案存在schema漂移适配差、领域语义理解错误、隐性假设幻觉等问题，无法适配动态迭代的分析需求。
### 方法关键点
1. 搭建DataWeave系统，整合对话交互、schema grounding、分析规划、可执行查询生成四大核心模块；
2. 摒弃LLM作为自主答案引擎的定位，将其转化为可被人工校验、修正、引导的交互式协作伙伴，匹配分析假设动态调整的工作流。
### 关键结果
面向专业记者的美国教育部IPEDS高复杂度、高schema更新频率数据集测试验证了系统可用性，通过多轮迭代优化形成适配实际工作流的架构，沉淀出可信人机LLM协作的核心设计原则。

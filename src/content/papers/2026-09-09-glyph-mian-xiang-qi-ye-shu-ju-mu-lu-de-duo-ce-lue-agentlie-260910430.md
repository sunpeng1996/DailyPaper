---
title: 'Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology
  Tagging of Enterprise Data Catalogs'
title_zh: 《Glyph：面向企业数据目录的多策略Agent列标注系统》
authors:
- Kostia Kudriavtsev
- Parvez Rafi
- Sha Sundaram
affiliations:
- Apple
arxiv_id: '2609.10430'
url: https://arxiv.org/abs/2609.10430
pdf_url: https://arxiv.org/pdf/2609.10430
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: Agent 企业数据敏感分类自动标注
tags:
- MultiAgent
- RAG
- ContrastiveLearning
- ReciprocalRankFusion
- DataGovernance
one_liner: 基于双LLM Agent架构实现无需读取单元格值的企业数据列描述生成与敏感标签标注
practical_value: '- 多异构信号融合可复用RRF方案：当多路召回、多策略标注等场景下不同模块输出排名的分数尺度不统一时，无需额外校准即可用RRF直接融合，效果优于多数定制化加权方案

  - 敏感场景无数据推理设计：电商用户隐私数据标注、合规标签生成可借鉴代码/元数据接地思路，无需读取原始敏感数据即可完成分类，规避合规风险

  - Agent生产落地优化技巧：批量处理降本（整表列统一调用LLM而非单条调用）、不同模型分任生成/法官角色规避自增强偏差、每步状态校验保障生产稳定性

  - 领域嵌入优化方案：针对业务特有短文本/结构化元数据（如类目路径、SKU属性串），用batch内对比损失微调轻量encoder可大幅提升检索匹配精度，成本远低于大模型微调'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业数据湖表单增长速度远超人工标注承载能力，列描述缺失、敏感标签未分配会直接导致数据发现效率低、访问权限控制失效、合规风险高；传统列标注方案依赖读取单元格内容，无法适配高保密级别数据，且跨异构存储引擎适配性差，百万级列规模下人工标注成本可达30人年以上。
### 方法关键点
- 双LangGraph Agent架构：Descriptor Agent生成列描述，通过主动RAG调用企业GitHub检索对应列的生产代码做接地，采用不同模型家族分别承担生成与LLM-as-Judge评分角色，规避自增强偏差，支持迭代优化，全程不读取单元格值
- Tagger Agent并行跑3路异构标注策略：描述标签器基于列描述语义检索本体候选后LLM选标；正则标签器基于业务规则匹配列名输出高精度标签；元数据标签器用对比学习微调的MiniLM编码列全路径元数据，向量检索历史标注候选后LLM选标
- 多策略融合：3路输出的排名结果用RRF（k=60）直接融合，无需分数校准，再按标签敏感层级加权重排，每个标签附带全来源溯源信息，满足企业审计要求
### 关键结果
- 元数据编码器对比微调后，同标签检索NDCG@10从0.55提升到0.92，MAP@100从0.19提升到0.90
- 端到端标注对比：单路元数据标签器F2为0.880，3路融合后总体F2达0.890，p50 latency 57.8s
- 生产落地6周后，人工对标签建议的接受率从63.3%提升至99.8%
> 最值得记住的结论：冗余异构信号加有原则的融合，远好于任何单一精巧信号，尤其适配对可解释性、稳定性要求高的生产场景

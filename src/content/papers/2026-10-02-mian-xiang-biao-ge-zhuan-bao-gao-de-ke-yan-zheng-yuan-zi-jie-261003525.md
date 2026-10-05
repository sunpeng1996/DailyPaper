---
title: Structured Composition of Verifiable Atomic Insights for Table-to-Report Generation
title_zh: 面向表格转报告的可验证原子洞见结构化组合框架
authors:
- Teng Lin
- Xinyu Liu
- Nan Tang
affiliations:
- HKUST(GZ)
arxiv_id: '2610.03525'
url: https://arxiv.org/abs/2610.03525
pdf_url: https://arxiv.org/pdf/2610.03525
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: 数据Agent · 表格自动分析报告生成
tags:
- LLM Agent
- Table-to-Report
- Data Analysis
- Verifiable Insight
- Multi-Relational Graph
one_liner: 提出ComInsight框架，基于原子洞见多关系图生成可验证表格分析报告，解决数据Agent探索偏差
practical_value: '- 可直接复用原子洞见定义+8种预定义分析模板，适配电商域销售/流量/物流多表分析场景，自动生成可SQL验证的运营洞见，减少人工取数分析成本

  - 多关系图+社区检测的洞见组合思路可迁移到用户行为分析、归因分析场景，将零散的用户/商品指标组合成有逻辑的因果/关联结论，提升运营分析报告的完整性

  - 轻量级Llama-3-8B + SFT/DPO做洞见有用性筛选的方案，可低成本适配业务自定义的「高价值洞见」标准，过滤85%无用分析结果，降低后续LLM推理成本

  - 因果边构造的「格兰杰检验+LLM语义验证」双校验思路可复用在电商归因场景，提升因果结论的可信度，避免纯统计或纯LLM推理的错误'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有表格转报告方案依赖顺序探索的ReAct风格数据Agent或直接LLM生成，存在严重探索偏差：早期局部发现会约束后续动作，导致遗漏跨表、跨维度的关联洞见，DDR-Bench的错误分析显示58%的分析错误来自探索广度不足，且生成的结论难以溯源验证，无法满足企业决策支持的可信要求。

### 方法关键点
- 定义8种可执行的原子洞见分析模板（MAX/MIN/AVG/SUM/COUNT/GROUP_BY/CORR/TREND），先枚举所有合法原子洞见，再通过统计显著性过滤+SFT/DPO微调Llama-3-8B的语义过滤器筛选高价值原子，过滤掉85%无效候选
- 构建多关系洞见图，节点为验证过的原子洞见，边对应比较、关联、上下文、时序、因果5种关系，其中因果边采用格兰杰检验+LLM语义验证的双校验规则，确保关系可信
- 基于Leiden社区检测对同关系子图的原子洞见做聚类，按关系类型合成高阶组合洞见，所有输出均附带可执行SQL和证据链，全程可追溯

### 关键实验
在InsightBench、DDR-Bench、T2R-Bench三个公开基准上测试，对比AgentPoirot、DeepSeek-R1、Claude 4.5 Sonnet、GPT-5.5等强基线：InsightBench上洞见级LLaMA-3-Eval得分0.73，超GPT-5.5 43.1%；T2R-Bench上平均得分83.5%，超原生GPT-5.5 18.89个百分点，数值准确率提升26.48个百分点；DDR-Bench 10-K场景准确率达79.34%，超Claude 4.5 Sonnet 2.2个百分点。

**最值得记住的一句话**：结构化的证据组合推理效果远优于纯LLM的语言拼接或顺序探索Agent的局部优化，是生成可信、高价值数据分析结论的核心路径

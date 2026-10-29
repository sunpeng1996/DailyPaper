---
title: 'Governed Sovereign RAG for Public Administration: Tripartite Epistemic Routing,
  Facet-Guided Clarification, and Deterministic Numeric Verification in Citizen Services'
title_zh: 面向公共服务的受控主权RAG：三方路由、维度澄清与数值校验架构
authors:
- Andres Cruz Degante
affiliations:
- Universidad Autónoma de Occidente (UAdeO), Mexico
arxiv_id: '2610.36561'
url: https://arxiv.org/abs/2610.36561
pdf_url: https://arxiv.org/pdf/2610.36561
published: '2026-10-27'
collected: '2026-10-29'
category: RAG
direction: 主权RAG · 合规性幻觉治理
tags:
- RAG
- Sovereign AI
- Deterministic Guardrail
- Epistemic Routing
- Hallucination Mitigation
one_liner: 提出本地化CPU部署的受控主权RAG架构，零费用幻觉，Top-1准确率较基线高10pp
practical_value: '- 确定性优先的分层响应架构可直接复用：将80%+高频请求用规则/模板响应，仅10%以下长尾请求调用LLM生成，大幅降低延迟与
  hallucination 风险，适配电商客服、商品咨询等高吞吐低容错场景

  - 数值校验guardrail可直接迁移到电商导购场景：生成后自动提取价格、优惠券金额、库存等数值，与召回的官方商品库校验，不匹配则fallback到模板，完全避免价格类幻觉

  - 三方认知路由机制替代传统二元拒识：将请求分为直接响应/澄清/拒识三类，对模糊请求返回结构化维度选项（如品牌、价格区间），较硬拒识提升10%+有效转化率，适配搜索、客服歧义query处理

  - 异构知识库解耦索引：避免短文本条目（如联系方式、短规则）挤占长文本（如商品详情、服务规则）的排序位置，提升长文本召回准确率6pp以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
政务服务RAG落地面临三重刚性约束：一是监管要求零费用/规则幻觉，错误输出需承担行政责任；二是数据主权要求所有计算本地化，不可调用商用云大模型API；三是公民输入query歧义性高、跨管辖范围的无效请求占比达12.63%。现有方案要么依赖高成本GPU集群，二元拒识的误拒率高达29.23%，要么缺乏确定性校验机制，幻觉风险不可控，无成熟的本地化CPU部署高可用合规方案。

### 方法关键点
- 确定性优先的分层响应架构：89.47%请求通过Level 0确定性模板直接返回，仅10.53%长尾歧义请求调用3B/4B量化小模型生成，大幅降低算力消耗
- 双阶段三方认知路由：先通过clarify_policy规则做粗分类，再基于AnyJev输出的玻尔兹曼分布计算置信度，将请求分为三类：高置信直接响应、中等置信返回维度澄清选项、低置信超范围拒识，替代传统二元拒识
- 三层数值幻觉防护：Level 0无生成流程→Level 1采用0温度抽取式生成→生成后自动校验所有数值（费用、有效期）是否属于召回的官方记录，不匹配则自动fallback到模板
- 异构知识库解耦索引：办事流程长文本与联系方式短文本分开存储索引，避免短文本挤占长文本排序位置，提升长文本Hit@1 6.15pp

### 关键实验结果
实验基于200条分层标注benchmark、380条8周生产真实trace开展，对比基线为传统二元神经拒识分类器：核心指标Strict Top-1准确率达86.5%，较基线提升10pp（pHolm=0.01172）；生产环境40次生成请求零费用幻觉（95%置信区间幻觉率上限≤8.81%）；Level 0直接响应p50延迟0.445s，全局p50延迟0.665s，仅普通CPU服务器即可运行；考虑澄清环节53.33%的用户流失率后，系统有效解决率为70.87%。

### 核心洞察
高合规、低算力预算的RAG系统应优先反转生成金字塔，用确定性规则覆盖绝大多数请求，仅将大模型能力严格限定在管控范围内的长尾场景，而非全链路依赖生成式输出。

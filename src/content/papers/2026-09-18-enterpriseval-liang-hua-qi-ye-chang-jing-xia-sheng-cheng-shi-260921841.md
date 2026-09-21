---
title: 'EnterpriseVal: Quantifying the Efficacy, Reliability and Value of Generative
  AI in the Enterprise'
title_zh: EnterpriseVal：量化企业场景下生成式AI的效能、可靠性与价值
authors:
- Abbas Raza Ali
- Muhammad Ajmal Siddiqui
- Moona Zahid
arxiv_id: '2609.21841'
url: https://arxiv.org/abs/2609.21841
pdf_url: https://arxiv.org/pdf/2609.21841
published: '2026-09-18'
collected: '2026-09-21'
category: Eval
direction: 生成式AI · 企业场景评估体系
tags:
- GenAI Evaluation
- Enterprise LLM
- LLM-as-judge
- Workflow Assessment
- Risk Quantification
one_liner: 提出面向企业场景的GenAI用例级评估体系，量化效能、可靠性与业务价值
practical_value: '- 可复用其按用例风险等级、自动化程度匹配评估强度的逻辑，降低自家Agent/LLM4Rec项目的评估成本，避免无效全量测评

  - 可直接套用六维度指标目录（保真度、效用、效率、可靠性、安全合规、人工审核成本）搭建电商GenAI应用（AI客服、商品文案生成、推荐理由生成等）的评估框架

  - 采用「专家盲评+校准后LLM-as-judge+预测驱动推理」的分级评分协议，平衡评估准确度与人力成本，适合大流量业务的常态化迭代评估'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前公开LLM基准仅能回答模型通用能力边界，无法适配企业场景下「特定数据、特定管控规则下的工作流是否适合上线、值得规模化」的决策需求，导致大量企业GenAI/Agent项目无法落地或无法证明业务价值。

### 方法关键点
提出EnterpriseVal用例级评估体系，核心包含5模块：1）用例与全链路配置（模型、Prompt、RAG、工具、护栏、人工审核规则）的正式化定义，按自治等级、风险等级确定评估强度；2）覆盖保真、效用、效率、可靠性、安全、审核成本的六维度指标库；3）结合盲专家评、校准后LLM-as-judge、预测驱动推理的分级评分协议；4）可执行双阈值门控逻辑，输出REJECT/CONDITIONAL/SCALE三类决策；5）纳入审核拦截率作为参数的价值-风险模型。

### 关键结果
全球银行3个工作流试点中，最优模型的信贷备忘录起草引用精度达88%、幻觉率1.6%（达标阈值分别为70%、5%）；流程转换场景下分析师单文档优化耗时从27.4小时降至2.9小时。

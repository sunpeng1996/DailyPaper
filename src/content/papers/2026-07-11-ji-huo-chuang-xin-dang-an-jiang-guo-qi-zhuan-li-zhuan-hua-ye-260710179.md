---
title: 'From Patent Expiry to Business Pathways: AI Workflows for Activating Innovation
  Archives'
title_zh: 激活创新档案：将过期专利转化为商业路径的AI工作流框架
authors:
- Sidney Shapiro
- Mark Price
affiliations:
- University of Lethbridge
- University of St. Thomas
arxiv_id: '2607.10179'
url: https://arxiv.org/abs/2607.10179
pdf_url: https://arxiv.org/pdf/2607.10179
published: '2026-07-11'
collected: '2026-07-14'
category: Other
direction: 专利商业化 · AI工作流与系统架构
tags:
- PatentAnalytics
- NLP
- WorkflowAutomation
- StructuredOutput
- Commercialization
one_liner: 提出分层架构与可解释评分工作流，将过期专利转化为可落地商业路径
practical_value: '- 分层数据摄入+可解释权重评分的架构可直接迁移到电商公域素材/过期版权内容的商业化挖掘场景，配套的权重扰动鲁棒性测试方法可复用，保障业务排序规则的稳定性

  - 规则+本地LLM的混合工作流+强制结构化输出的设计，适合合规要求高的业务场景（如电商侵权排查、资质审核），既降低幻觉风险，又避免敏感数据外泄到第三方模型

  - 专业领域文档到业务路径的翻译框架可复用，比如将供应链标准、合规条款等专业文本转化为可落地的业务动作建议，不需要端到端大模型就能落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
全球专利库是最大的公共技术知识档案，但过期/失效专利的商业化价值长期被低估，专利文本的专业法律/技术语言门槛、跨司法辖区的法律状态校验复杂度、商业化路径的缺失，使得大量公共领域技术知识无法被中小企业、创业团队复用，传统专利分析仅聚焦法律风险或竞争情报，缺乏从专利文本到可落地商业路径的端到端工具。

### 方法关键点
- 三层数据摄入架构：Tier1为各国官方专利局权威数据源，Tier2为EPO等跨司法辖区聚合数据，Tier3为分析数仓，隔离原始数据、衍生特征、生成结果，保证可审计
- 可解释机会评分模型：融合专利法律状态、到期时间、家族风险、商业相关性、SaaS可行性多个维度，权重透明可调整，支持敏感度测试
- 四模块工作流：到期专利发现、趋势检测、专利到路径翻译、评审包生成，规则+本地LLM（Qwen3.6）混合实现，强制JSON结构化输出，降低幻觉
- 风险显式标注：所有输出均标注法律状态不确定性、家族风险等未解决问题，明确AI仅作决策支持而非法律建议

### 关键结果
用加拿大CIPO一周的378份ST.96专利档案做POC，识别出20份过期/失效/2年内到期的候选专利；评分权重±20%扰动下，排名Kendall τ系数高于0.87，top5重合度≥4/5，排序稳定性极强；本地Qwen3.6生成结构化评审包的格式合规率100%，无JSON解析错误。

### 核心结论
AI在专业档案挖掘场景的核心价值是降低解释负担，而非替代专家评审，所有高风险决策必须保留人工审核与溯源能力

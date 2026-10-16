---
title: 'Twenty Days Later: A Pre-Registered Test of History-Based Forecasts of Brand
  Mentions in Gemini Answers'
title_zh: Gemini回答中品牌提及历史预测的20天有效性预注册验证
authors:
- Dmitrij Żatuchin
affiliations:
- Rankfor.AI Sp. z o.o., Wrocław, Poland
arxiv_id: '2610.19608'
url: https://arxiv.org/abs/2610.19608
pdf_url: https://arxiv.org/pdf/2610.19608
published: '2026-10-14'
collected: '2026-10-16'
category: Eval
direction: 生成式推荐 · 品牌提及稳定性评估
tags:
- LLM
- brand mention
- recommendation stability
- pre-registration
- Gemini
one_liner: 预注册实验验证固定版本Gemini的品牌提及率历史预测20天内保持稳定
practical_value: '- 电商AI导购、生成式商品推荐业务中，若LLM版本不变，每月重测一次品牌/商品提及率即可，无需高频采样，可大幅降低测试成本

  - 采集LLM推荐的品牌分布时，单个session采样3次即可获得接近9次采样的预测精度，采样量减少2/3的前提下效果几乎无损失

  - 品牌提及标签可采用全词匹配+别名库+文本归一化的自动规则，召回率接近100%，远高于人工标注效率，可直接用于业务监控

  - 固定模型版本下，用单query的历史提及率预测未来输出效果远优于全局品牌流行度baseline，可直接用于生成式推荐的冷启动预测'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前用户大量通过LLM助手询问商品/品牌推荐，品牌方布局GEO、企业做LLM导购推荐都依赖历史观测的LLM品牌提及率，但此前无预注册实验验证这类历史预测的长期有效性：如果观测结果几天就失效，所有基于历史数据的业务决策都没有意义。
### 方法关键点
- 实验对象为gemini-3.1-pro-preview，固定所有请求参数（开启搜索工具、temperature=1.0、无系统指令等），4波测试的请求体完全一致，最长间隔20.3天
- 覆盖3类软件（电商平台、项目管理、CRM）的54个问题，跨3种语言、2个目标市场，对应12个候选品牌，每波生成648个品牌提及标签
- 全流程预注册：实验规则、预测逻辑、评估指标全部提前冻结哈希并在OSF登记，完全规避数据泄露风险
- 品牌提及标签采用全词匹配+别名库、NFKC归一化、大小写折叠的自动规则，负提及同样计数
### 关键实验结果
- 核心指标采用Brier得分（越低越好）、log loss（越低越好），对比baseline包括单波历史、品牌全局历史、全局提及率、常数0.5
- 基于前3波9次回答的 pooled cell rate 预测20天后的提及率，Brier得分0.0281、log loss 0.126，远优于品牌历史（Brier 0.104）、全局提及率（0.234），仅比8小时间隔的预测得分高0.0022，远低于预注册的0.0559上限
- 仅用最近1波3次回答的预测Brier得分0.0292，和9次样本的效果无统计显著差异
- 202个前序波结果完全一致的样本中，194个20天后结果不变，无从全提及到完全不提及的反转情况
### 核心结论
固定模型版本下，LLM的品牌提及率20天内稳定性极高，少量短周期采样即可支撑长期业务决策

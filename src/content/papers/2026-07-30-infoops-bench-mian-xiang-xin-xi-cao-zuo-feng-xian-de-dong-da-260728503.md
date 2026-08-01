---
title: 'InfoOps Bench: A live information operations safety benchmark'
title_zh: InfoOps Bench：面向信息操作风险的动态大模型安全评测基准
authors:
- Dorian Quelle
- Lisa-Maria Neudert
- Jonathan Bright
- John Gallacher
affiliations:
- pattrn.ai
arxiv_id: '2607.28503'
url: https://arxiv.org/abs/2607.28503
pdf_url: https://arxiv.org/pdf/2607.28503
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: 大模型安全评测 · 抗信息操作滥用
tags:
- LLM Safety
- Benchmark
- Info Operations
- Model Evaluation
- Dynamic Benchmark
one_liner: 推出动态更新的大模型信息操作安全评测基准，基于2100+真实案例测试17款主流大模型的抗滥用能力
practical_value: '- 可参考动态基准的构建思路，搭建业务场景下的实时对抗风险评测集，比如反营销诈骗、反虚假宣传的大模型安全评测，周更迭代避免过拟合

  - 可复用多prompt framing测试思路，在内容生成、智能客服等场景下多维度测试大模型合规性，避免单一prompt漏测风险

  - 可借鉴完整性得分、事实核查率等指标，平衡生成式推荐/Agent的可用性与合规性，降低内容输出的合规风险'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
国家背书的信息操作是重大公共安全风险，现有静态大模型安全基准容易被饱和适配，缺乏针对真实信息操纵场景的动态评测能力。
### 方法关键点
基于实时监控的2100+来自俄、中、伊的官方信息资产操作案例，构建每周更新的动态评测基准，覆盖4类prompt框架，测试8家厂商的17款前沿大模型。定义完整性得分为模型拒绝违规请求的比例，同时统计事实核查率、内容有害性等维度表现。
### 关键结果数字
各模型完整性得分区间为8.8%~94.5%，85.7个百分点的差异无法由模型大小解释；事实核查率区间为2.9%~72.9%，部分模型生成内容有害性高于原始素材；多数国产大模型对涉华负面真实诉求的合规率相对良性诉求下降48~70个百分点，仅GLM 5.2为例外。

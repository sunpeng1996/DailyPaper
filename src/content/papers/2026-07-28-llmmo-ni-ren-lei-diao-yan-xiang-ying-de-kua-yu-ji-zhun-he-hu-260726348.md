---
title: 'When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human
  Survey Responses'
title_zh: LLM模拟人类调研响应的跨域基准：合成用户失效场景分析
authors:
- Zihan Chen
- Di Zhu
- Lei Nico Zheng
affiliations:
- Stevens Institute of Technology
- University of Massachusetts Boston
arxiv_id: '2607.26348'
url: https://arxiv.org/abs/2607.26348
pdf_url: https://arxiv.org/pdf/2607.26348
published: '2026-07-28'
collected: '2026-07-30'
category: Eval
direction: LLM应用评测 · 合成用户仿真
tags:
- Synthetic User
- LLM Evaluation
- Survey Simulation
- User Modeling
- Bias Detection
one_liner: 验证LLM作为合成用户的两类系统性偏差，推出跨域评估框架判断其决策支持适用性
practical_value: '- 用LLM做合成用户调研前，必须先用历史真实用户数据做基准校验，避免偏差导致的市场/产品决策错误

  - 不可直接依赖LLM输出的人群偏好差异结论，LLM会放大人口属性对偏好的影响2~4倍，易选错目标客群

  - 构建用户画像/用户反馈仿真系统时，需校正LLM的刻板印象偏差，避免推荐/广告策略出现人群歧视

  - 可复用论文的评测框架，对自研合成用户系统做跨域有效性验证，明确其可安全应用的场景范围'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前大量场景用LLM作为合成用户替代真人输出调研反馈，支撑产品、市场决策，但缺乏统一的有效性校验框架，无法预判合成用户的输出偏差。
### 方法关键点
覆盖从8B到前沿能力的2个系列共4款LLM，在全美社会态度调查、跨文化价值观调查两个真实人类响应数据集上做标准化评测，与基于留存真人数据拟合的非LLM基线做对比。
### 关键结果数字
1. 个体响应预测层面，所有LLM效果均弱于最强非LLM基线，跨文化价值观场景差距更为显著
2. 所有模型均系统性高估人口属性对态度的预测作用，刻板印象偏差稳定存在，且增大模型参数无法修复
3. 人群定向任务中，模型将群体间差异放大2~4倍，50%美国场景、多数跨文化场景会选错目标客群，还会生成不存在的群体拆分

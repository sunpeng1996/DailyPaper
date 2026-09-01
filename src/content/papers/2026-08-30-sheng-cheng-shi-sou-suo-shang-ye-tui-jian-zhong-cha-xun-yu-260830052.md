---
title: 'The Language of the Question Selects the Market: Query Language and Exit IP
  as Separable Factors in Commercial Recommendations from a Generative Search Interface'
title_zh: 生成式搜索商业推荐中查询语言与出口IP的独立影响机制研究
authors:
- Dmitrij Żatuchin
affiliations:
- Estonian Entrepreneurship University of Applied Sciences
- Rankfor.AI OÜ
arxiv_id: '2608.30052'
url: https://arxiv.org/abs/2608.30052
pdf_url: https://arxiv.org/pdf/2608.30052
published: '2026-08-30'
collected: '2026-09-01'
category: GenRec
direction: 生成式推荐 · 本地化影响因子研究
tags:
- Generative Search
- Recommendation Localization
- LLM Evaluation
- Multilingual IR
- Controlled Experiment
one_liner: 通过对照实验证实生成式搜索商业推荐中查询语言与出口IP为独立影响因素，前者决定本地商家露出门槛
practical_value: '- 做跨境电商生成式推荐/AI搜索优化时，不要只用英文做测试，必须针对目标市场的官方语言单独测试推荐露出效果，否则本地商家完全不会出现在英文查询结果里

  - 生成式推荐的本地化策略需拆分两个变量：查询语言决定是否开启本地商家召回开关，出口IP决定召回哪个市场的商家池，两者可独立优化

  - 受国家监管的品类（如财税、合规类服务）的本地化推荐效果远高于无监管的通用品类，做细分品类推荐时可优先对齐监管属性配置召回规则

  - 生成式推荐的单次输出无统计意义，评估效果必须做多次重复测试（至少6次以上），否则会误判噪声为真实效果'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式搜索的商业推荐效果评估普遍默认采用英文测试，未明确区分查询语言、用户出口IP两个核心变量的独立作用，导致区域市场的本地化商家露出效果测量严重失真，也无法指导跨境场景下的生成式推荐优化。
### 方法关键点
- 2026年8月针对登出状态ChatGPT网页端、OpenAI API开展234组对照测试，覆盖4个出口国家、6种查询语言，每个变量组合固定做6次重复测试，全程无账号历史信息干扰
- 独立控制查询语言、出口IP两个变量，选择受国家监管的自由职业者会计软件为处理组，无强监管的营销agency项目管理软件为对照组
- 品牌匹配采用大小写敏感规则，避免查询语言中普通词汇与品牌名重名导致的统计误差
### 关键结果
- 当查询语言为出口国官方语言时，24次测试仅1次出现全球品牌；同IP下用英文查询时，爱沙尼亚、土耳其的12次测试中本地商家露出率为0
- 固定查询语言仅切换出口IP，推荐商家池会切换为IP对应市场的品牌，回答语言保持不变；少数族裔语言（如爱沙尼亚的俄语）的本地商家露出率（4/6）介于官方语言（6/6）和英文（0）之间
- 6次相同查询中4次的Top推荐结果不一致，网页端、API（开/关web search）的不稳定性发生率完全一致

最值得记住的结论：用英文测量生成式搜索的区域市场推荐效果，等同于在测试一个你根本没有参与竞争的市场，本地竞品和用户真实看到的结果都会完全不可见。

---
title: Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains
  of Generative Engine Optimization via LIVE-GEO
title_zh: 真实Web环境下GEO增益有效性验证及LIVE-GEO评估基准
authors:
- Runze Kong
- Haibo Jin
- Xucheng Yu
- Xiaoqi Wang
- Huimin Zeng
- Haohan Wang
affiliations:
- University of Michigan, Ann Arbor
- University of Illinois Urbana-Champaign
- Starc Institute
arxiv_id: '2611.01126'
url: https://arxiv.org/abs/2611.01126
pdf_url: https://arxiv.org/pdf/2611.01126
published: '2026-10-31'
collected: '2026-11-03'
category: Eval
direction: GEO评估 · 真实环境基准
tags:
- GEO
- Generative Search
- Benchmark
- Content Optimization
- Evaluation
one_liner: 提出首个真实Web上线的GEO评估基准LIVE-GEO，验证不同GEO策略在生成式搜索下的实际可见性增益
practical_value: '- 做电商商品页GEO优化时优先选用CORE策略，其在ChatGPT、Gemini、Grok三大主流生成式搜索引擎上Top-1率可达66.3%~76.3%，远高于其他现有GEO策略

  - 内部离线评估GEO效果时优先选用DeepSeek作为评估模型，其与主流GE的排序相关性达ρ=0.50，接近不同GE之间的一致性水平，避免使用Claude做GEO离线评估（其与GE排序为负相关）

  - 商品文案优化严禁添加无依据的数值描述，JEV数值一致性校验准确率达90.7%，无依据数值会被标记，直接导致商品排序垫底

  - 生成式搜索排序对候选展示顺序高度敏感，做GEO效果A/B测试时必须随机打乱商品展示顺序，避免顺序偏差导致的结果误判'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GEO策略的评估均在固定候选集或受控检索流水线中完成，未在真实公网环境验证，无法确定GEO优化后的内容在生成式搜索引擎（GE）真实爬取、排序下是否真的能获得更高可见性，离线评估的增益可能无法复现到线上。
### 方法关键点
- 构建LIVE-GEO基准，覆盖18个品类80个虚构品牌的商品，同品牌商品仅描述、评价存在差异，价格波动控制在±0.2%，排除其他因素干扰
- 支持用户上传自定义GEO改写后的商品内容，经过安全校验、JEV数值一致性校验后上线为真实可访问的公网页面
- 评估链路完全对齐真实用户场景，直接调用ChatGPT(GPT-6)、Gemini 3.6 Thinking、Grok Expert等主流GE的网页访问能力获取排序结果，同时对比5个直接文本评估模型的结果一致性
### 关键实验结果
对比CORE、AgenticGEO、C-SEO、E-GEO、Statistics Addition共5种现有GEO策略，核心结论：① CORE在7/8个评估器上取得最高Top-1率，三大GE上Top-1率达66.3%~76.3%，领先第二名56~66个百分点；② 不同GE之间排序一致性较低，仅48.8%~66.3%的品牌会选出相同Top-1商品，离线评估模型中仅DeepSeek与GE的相关性最高（Spearman ρ=0.50），Claude与GE排序负相关；③ 生成式搜索对候选展示顺序高度敏感，CORE在ChatGPT上的Top-1率在不同固定顺序下波动达20个百分点；④ JEV数值校验准确率达90.7%，所有添加无依据数值的Statistics Addition策略改写内容均被标记，排序直接垫底。
### 核心结论
只有基于真实Web环境的GEO评估结果具备业务参考性，离线评估的品牌级增益大多无法复现到线上。

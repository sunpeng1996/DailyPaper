---
title: Characterizing Adversarial GEO via Implicit Brand Injection
title_zh: 基于隐式品牌注入的对抗性生成式搜索引擎优化研究
authors:
- Shobhnik Kriplani
- Haohan Wang
affiliations:
- Indian Institute of Science
- University of Illinois Urbana-Champaign
arxiv_id: '2611.04005'
url: https://arxiv.org/abs/2611.04005
pdf_url: https://arxiv.org/pdf/2611.04005
published: '2026-11-02'
collected: '2026-11-04'
category: MultiAgent
direction: 生成式搜索优化 · 多Agent内容植入
tags:
- GEO
- Multi-Agent
- Generative Search
- Brand Exposure
- Adversarial Attack
- RAG
one_liner: 提出多Agent隐式品牌注入框架IBI，实现生成式搜索下低感知高转化的品牌曝光
practical_value: '- 电商品牌做GEO时可复用IBI的多Agent植入流程：先选植入位置、改写单句、迭代校验，既保证内容自然不被平台检测，又能提升检索和生成曝光率

  - 生成式搜索/推荐平台做风控时，可针对单句品牌植入的特征优化检测逻辑：比如比对语义一致性、局部上下文困惑度变化、是否有隐性品牌植入

  - 内容类电商的软文生成可借鉴这套框架，在干货内容中自然植入商品，降低用户抵触同时提升转化

  - 做RAG系统防投毒时，可增加多源交叉验证规则，单一来源的陌生品牌提及不直接输出到生成结果'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式搜索逐渐成为用户发现商品、服务的核心入口，传统SEO转向GEO（生成式搜索引擎优化），现有对抗GEO方法多依赖显性指令或重复关键词，容易被检测，而低感知的隐性品牌植入的效果和可行性尚未被系统验证，同时当前缺乏标准化的评估基准衡量这类植入的检索曝光、生成传播全链路效果。
### 方法关键点
- 提出多Agent框架IBI，拆分四个模块：Placement Planner选合适植入位置，Content Rewriter仅改写单句植入品牌，Verifier从语义保留、上下文连贯、无促销属性等维度校验，不合格的返回重写，Coordinator选最优候选，最后做确定性规则校验
- 构建IBIBench基准：覆盖12个领域1000篇纯信息类文章，60个合成品牌（消除模型先验认知干扰），每篇文章匹配同领域内生品牌、跨领域外生品牌各一个，共2000组文章-品牌对
### 关键结果
对比Direct Prompting、同调用预算的Best-of-N基线，在2个稠密检索器、5个主流生成模型上验证：内生品牌+文章关联查询场景下，IBI Hit@10达82.2%，MRR@10达0.74，品牌提及率（BMR）最高62.7%，条件传播率（CP）最高75.9%；相比Best-of-N基线，Hit@10提升6.7~11.3个百分点，BMR平均提升8.4个百分点，同时植入内容促销感知率比基线低26个百分点。
### 核心结论
仅在信息类文章中植入1次无促销属性的自然品牌提及，就可显著提升该品牌在生成式搜索结果中的曝光率，这既给品牌GEO提供了低成本路径，也给生成式搜索/推荐平台的商业内容风控提出了新挑战。

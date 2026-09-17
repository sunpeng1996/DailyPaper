---
title: '"If I Had to Buy Just ONE: Galaxy S26 Ultra": Auditing AI-Generated Product
  Recommendations'
title_zh: AI生成商品推荐审计：跨平台一致性、来源及API与前端差异
authors:
- Lucas G. Uberti-Bona Marin
- Thales Bertaglia
- Giovanni Astante
- Bram Rijsbosch
- Gijs van Dijck
- Anikó Hannák
- Gerasimos Spanakis
- Konrad Kollnig
affiliations:
- Maastricht University
- Utrecht University
- University of Zurich
arxiv_id: '2609.18729'
url: https://arxiv.org/abs/2609.18729
pdf_url: https://arxiv.org/pdf/2609.18729
published: '2026-09-16'
collected: '2026-09-17'
category: GenRec
direction: 生成式推荐 · 效果合规审计
tags:
- LLM4Rec
- Generative Recommendation
- Audit
- E-commerce
- API-UI Gap
one_liner: 基于真实用户消费查询审计3款主流生成式推荐系统，揭示响应不一致及API与前端的显著差异
practical_value: '- 做电商购物Agent/生成式推荐产品时，不要直接对齐API的输出效果，必须以用户实际使用的前端界面的返回结果为准做测试，避免线上推荐内容、来源与测试环境差异过大

  - 可复用论文的推荐稳定性评估方法：用多次请求的推荐商品Jaccard重叠度、来源重叠度作为指标，优化生成式推荐的一致性，降低同一个query返回差异过大导致的用户信任损失

  - 优化生成式推荐的RAG来源池时，可参考不同大模型的来源偏好：ChatGPT偏好科技评测站，Gemini偏好UGC/视频内容，Google AI Overviews更侧重社区内容，针对性补充高权重来源提升推荐可信度

  - 做生成式推荐的合规审计时，不能仅依赖API采样，需多次重复请求、采集用户前端的真实输出，才能覆盖用户实际遇到的所有推荐情况，满足监管要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前用户越来越依赖AI聊天机器人获取购买建议，OpenAI、Google等厂商已开始在生成式推荐场景嵌入广告，现有生成式搜索审计多基于API和人工构造query，既未针对商品推荐场景做专项分析，也无法反映普通用户在前端实际收到的推荐内容，存在明显研究缺口，也不符合欧盟DSA等监管的合规审计要求。
### 方法关键点
- 从真实对话数据集LMSYS-Chat-1M、WildChat-1M中筛选得到2528条用户消费咨询query数据集CONSUMERQ，进一步抽样117条无地域限制的通用实物商品query作为测试集
- 同时测试5种场景：ChatGPT前端/API、Gemini前端/API、Google搜索AI Overviews，每个query重复3次，控制请求地理位置为荷兰，API与前端请求时间差控制在0.3秒以内，排除时间、地域变量干扰
- 从推荐表述风格、推荐商品一致性、引用来源重叠度三个维度对比跨平台、跨渠道的差异
### 关键结果
- ChatGPT 79%的推荐回复使用第一人称表达偏好，远高于Gemini的7%和AI Overviews的2%；73%的回复会标注某个商品为「最佳」，也远高于另外两个平台的43%、48%
- 相同query下ChatGPT与Gemini的引用域名重叠率仅5.4%，76.7%的对比场景无任何共同域名
- ChatGPT前端与API的引用域名重叠率仅12.0%，Gemini为14.8%，API无法作为前端的审计代理

> 最值得记住的结论：单条响应或API采样都不能代表用户实际收到的AI商品推荐，审计必须覆盖多次重复请求、用户前端真实环境。

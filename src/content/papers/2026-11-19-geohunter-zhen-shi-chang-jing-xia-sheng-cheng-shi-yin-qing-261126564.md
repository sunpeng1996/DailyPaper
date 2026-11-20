---
title: 'GEOHunter: Mapping a Generative Engine Optimization Network in the Wild'
title_zh: GEOHunter：真实场景下生成式引擎优化黑产网络测绘工具
authors:
- Sean Tang
- Peiran Wang
- Ying Li
- Esha Shivakumar
- Tao Meng
- Yuan Tian
affiliations:
- University of California, Los Angeles
- Georgia Institute of Technology
arxiv_id: '2611.26564'
url: https://arxiv.org/abs/2611.26564
pdf_url: https://arxiv.org/pdf/2611.26564
published: '2026-11-19'
collected: '2026-11-20'
category: Eval
direction: 生成式搜索安全 · 黑产量化测量
tags:
- GEO
- Generative Search
- Search Spam
- UGC
- Content Manipulation
- RAG Security
one_liner: 开发双工具测绘真实GEO黑产网络，验证其对9款主流生成式引擎的渗透效果
practical_value: '- 生成式推荐/AI导购的RAG模块可新增两个负向特征：跨账号内容模板相似度、多账号同时间段发布同品牌内容的协同度，能有效降低GEO黑产内容的召回权重，避免推荐结果被操纵

  - 电商品牌做GEO投放可复用黑产的内容优化策略：优先发布带用户搜索query匹配、年份标识、超级词的排名类listicle内容，可大幅提升内容被生成式引擎引用的概率

  - 平台批量识别营销号网络可复用GEOHunter的雪球挖掘框架：从已知营销号的推广品牌关键词出发，结合协同发布信号做扩召回，识别准确率可达92%以上

  - 生成式搜索的防御不能仅依赖单篇内容审核，需将账号的历史发布行为、跨平台关联关系作为核心风控信号，防御效率远高于内容层面的检测'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
带网页检索能力的生成式引擎/AI助手已成为70%以上中国用户获取消费决策信息的核心渠道，GEO（Generative Engine Optimization）黑产通过在UGC平台批量发布未标注的付费软文，操纵生成式引擎的回答结果，在医疗、金融等高风险领域易造成严重用户损害，但此前尚无研究对真实落地的GEO黑产的运作模式、规模、渗透效果做系统性量化测量。
### 方法关键点
- 构建GEOHunter账号测绘工具：从已知付费软文账号为种子，通过推广品牌名做雪球式扩召回，以「同时推广多个无关客户、跨账号复用相同标题模板、2个以上账号同天发布同个客户内容」三个协同信号判定黑产账号，覆盖B站、百家号、360快传三大主流UGC平台。
- 构建GEOPRobe引擎探测工具：针对黑产覆盖的消费品类构造匹配用户真实搜索习惯的查询，对9款中美主流生成式引擎做批量探测，从严格（作者为黑产账号）、扩展（标题与黑产内容相似度≥0.8）、宽泛（内容提及对应推广客户）三个层级做内容归因。
### 关键结果
共识别1985个有效黑产账号、46.6万条付费推广软文，96%内容推广普通消费类商品，2024-2025年排名类listicle内容占比从16%提升至57%，黑产账号中位数粉丝仅9个，完全依赖生成式引擎检索获取曝光。9款生成式引擎的引用页面中，4.5%（严格）~20%（宽泛）来自该黑产网络；针对黑产客户的品类查询中，52%的回答会提及黑产客户，仅比品类头部品牌的68%提及率低16pct。
### 核心结论
单篇内容级的审核完全无法防御GEO黑产的协同攻击，必须基于账号级的协同发布信号、跨平台关联关系做识别和拦截。

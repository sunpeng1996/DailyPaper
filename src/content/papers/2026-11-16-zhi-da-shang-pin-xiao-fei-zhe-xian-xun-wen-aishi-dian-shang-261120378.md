---
title: 'Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First'
title_zh: 直达商品：消费者先询问AI时电商零售商遗漏的流量价值
authors:
- Michael Iannelli
- Alan Ai
affiliations:
- Scrunch AI
arxiv_id: '2611.20378'
url: https://arxiv.org/abs/2611.20378
pdf_url: https://arxiv.org/pdf/2611.20378
published: '2026-11-16'
collected: '2026-11-17'
category: RecSys
direction: 电商AI推荐 · 用户行为与效果评估
tags:
- LLM
- E-commerce
- Conversational Recommendation
- User Behavior
- Recommendation Evaluation
one_liner: 通过跨站点用户行为关联证实AI购物推荐转化效果，提出无需referral数据的follow-through评估指标
practical_value: '- 流量归因优化：现有referral报告仅能捕捉11%的AI推荐带来的访问，需叠加搜索框产品名查询、直接访问产品页的数据联动，才能准确统计AI导购的真实引流效果

  - 商品搜索优化：针对AI助手常用的产品命名规则优化商品标题、站内搜索匹配逻辑，确保用户搜索AI推荐的商品名时能精准匹配到对应商品页

  - 详情页承接优化：AI推荐带来的用户浏览多商品的概率比普通访问高5.2个百分点，需在商品详情页强化相关推荐、搭配商品的露出，提升转化

  - 新客触达优化：一周未访问的新客点击AI推荐链接的概率比老客高14.7个百分点，可针对AI导购渠道做定向新客召回权益设计'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前电商平台的流量归因完全依赖referral标记，无法识别用户先询问AI导购获得商品推荐后，自行搜索/直接访问商品的转化链路，严重低估AI导购的引流价值，也缺乏无服务商依赖的AI购物助手效果评估方法。

### 方法关键点
- 采用英美市场opt-in用户面板数据，关联同一用户的ChatGPT、Gemini等主流AI助手对话记录，与20家头部电商的后续浏览行为
- 用LLM分类器标注AI回答类型（特定产品推荐/店铺推荐/仅提及店铺），匹配用户后续浏览的商品页与AI推荐商品的一致性，允许尺寸、颜色等变体算匹配
- 三重对照设计：用户自身过往14/21/28天的行为基线、他人同品类同店铺的匹配回答对照、同时段无AI推荐的活跃时刻对照，排除用户习惯、热门商品的干扰

### 关键结果
- AI给出特定商品推荐后，24小时内用户访问对应商品页的比例从基线0.02%升至2.07%，提升100倍；有商品页访问的日期中44%的访问是AI推荐的商品，对照他人回答仅1.5%
- 89%的AI推荐带来的访问无AI referral标记，54%来自搜索引擎搜索推荐的商品名，搜索该商品名的概率是基线的24倍
- AI推荐带来的用户访问中，浏览2个及以上商品的比例比普通访问高5.2个百分点

> 最值得记住的一句话：89%的AI导购引流价值被现有归因体系漏掉，AI推荐的商品名称是链接用户决策与后续访问的核心锚点

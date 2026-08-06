---
title: Investigating Click Behaviors On Google Search Result Pages That Produce an
  AI Overview
title_zh: 《谷歌搜索AI概览结果页用户点击行为研究》
authors:
- Athena Chapekis
- Anna Lieb
- Sono Shah
- Aaron Smith
affiliations:
- Pew Research Center
arxiv_id: '2608.04831'
url: https://arxiv.org/abs/2608.04831
pdf_url: https://arxiv.org/pdf/2608.04831
published: '2026-08-05'
collected: '2026-08-06'
category: Other
direction: AI搜索 用户行为分析
tags:
- AI Search
- Click-Through Rate
- User Behavior
- SERP
- Logistic Regression
one_liner: 基于900名美国成年用户1个月浏览数据，分析谷歌AI概览触发特征及对用户搜索行为的影响
practical_value: '- 做搜索类AI摘要产品可复用触发规则：长query、疑问词开头、同时含名动的query优先触发，提升信息获取效率

  - 电商搜索上线AI摘要功能需做权衡：AI摘要会降低结果点击量，若核心目标是引流商品页需强化跳转引导设计

  - 可复用混合效应逻辑回归方法，控制用户个体、query属性等混淆变量，准确量化新功能对用户行为的真实影响'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
2024年谷歌上线搜索结果顶部AI概览功能，其对用户搜索行为的影响尚未被系统量化，大量在线出版商同时担忧该功能会导致自有网站流量大幅下滑。
### 方法关键点
基于900名美国成年代表性用户的1个月网页浏览数据，首先挖掘AI概览的触发query特征，再通过混合效应逻辑回归模型，控制用户个体随机效应、query属性等混淆变量，精准量化AI概览与用户行为的关联。
### 关键结果数字
① 长query、疑问词开头、同时包含名词和动词的query更易触发AI概览；② AI概览引用来源的点击率仅约1%；③ 存在AI概览的搜索页用户整体点击量更低，会话结束率更高，控制混淆变量后该关联仍显著成立。

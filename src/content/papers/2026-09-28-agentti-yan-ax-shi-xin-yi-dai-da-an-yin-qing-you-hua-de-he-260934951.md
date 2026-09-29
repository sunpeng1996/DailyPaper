---
title: AX is the New AEO
title_zh: Agent体验（AX）是新一代答案引擎优化的核心策略
authors:
- Ido Finder
- Assaf Elovic
- Gad Shalev
affiliations:
- ora research
arxiv_id: '2609.34951'
url: https://arxiv.org/abs/2609.34951
pdf_url: https://arxiv.org/pdf/2609.34951
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent 网页可访问性优化
tags:
- AX
- AEO
- Web Agent
- Grounding
- Answer Accuracy
one_liner: 基于37927次Agent旅程实验验证AX对企业推荐率、回答准确率的提升效果显著优于AEO
practical_value: '- 电商/品牌官网可优先优化AX：放开Agent爬虫限制、提供静态内容fallback、配置llms.txt等，可直接提升Agent明确推荐率1.9倍

  - 开发Agent导购、商品调研类应用时，优先抓取品牌官方静态页作为信息源，回答准确率可提升41%，单条有效回答成本降低64%

  - 企业AI端流量运营ROI优先级：自有站AX优化 > 传统SEO > 第三方站AEO布局，控制AX变量后AEO无显著增益'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统AEO（答案引擎优化）是企业获取AI搜索流量的核心手段，核心逻辑是通过站外露出提升检索召回概率，但随着多轮搜索、自动网页读取的Agent成为用户查询的主流处理载体，仅完成搜索露出已不足以影响最终回答，Agent能否读取企业自有站内容的影响尚未被量化验证。

### 方法关键点
- 匹配1056家真实企业样本，控制品牌知名度、模型训练数据先验知识、2类AEO代理指标完全一致，仅按AX（Agent可读性）得分分为两组
- 覆盖4套独立Agent运行栈（跨OpenAI、Anthropic两家模型厂商，2类搜索后端），共运行37927次用户查询Agent旅程，采用盲审标注避免评估偏见
- 核心评估维度包括第一方内容占比、用户推荐率、回答准确率、Agent运行成本四类

### 关键结果
- Agent回答中仅7-10%来自训练知识，AX达标企业的回答78%内容来自自有站，比未达标企业高22pct，明确推荐率是后者的1.9倍
- 基于自有站内容生成的回答准确率比第三方内容高41%，第三方内容回答完全遗漏用户问题的概率是前者的3.7倍
- AX未达标企业的单次grounded回答成本平均高64%，控制AX变量后AEO指标对所有结果无显著影响

### 核心结论
Agent时代，网站被Agent可读比被第三方站点提及重要得多，优化AX是企业可控的最高杠杆AI流量运营手段

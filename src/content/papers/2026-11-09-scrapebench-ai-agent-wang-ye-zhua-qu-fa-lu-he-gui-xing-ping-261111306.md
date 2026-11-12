---
title: 'ScrapeBench: Evaluating Legal Compliance of AI Agents in Website Scraping'
title_zh: ScrapeBench：AI Agent 网页抓取法律合规性评估基准
authors:
- Joseph Marvin Imperial
- Daniel Slate
- Noam Kolt
affiliations:
- Pivotal Research
- University of Bath
- National University Philippines
- University of Notre Dame
- Hebrew University of Jerusalem
arxiv_id: '2611.11306'
url: https://arxiv.org/abs/2611.11306
pdf_url: https://arxiv.org/pdf/2611.11306
published: '2026-11-09'
collected: '2026-11-12'
category: Eval
direction: AI Agent 网页抓取合规性评测
tags:
- AI Agent
- Benchmark
- Legal Compliance
- Web Scraping
- Evaluation
one_liner: 推出首个AI Agent网页抓取合规性评测基准，实测主流Agent禁爬场景合规率不足5%
practical_value: '- 开发网页数据采集类Agent时，可复用ScrapeBench的规则校验逻辑，将robots.txt、ToS规则接入Agent决策链路，降低合规风险

  - 针对Agent合法抓取场景下的过度拒绝问题，可在SFT/RLHF阶段加入合规判定正负样本，平衡合规性与任务完成率

  - 电商行业爬取竞品公开商品信息、公网公开数据时，可基于该基准的规则校验逻辑做前置拦截，避免法律风险'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
公网部署的AI Agent执行网页抓取任务时，易违反网站服务条款（ToS）、robots.txt规则甚至计算机安全法规，此前无针对性的合规性评测方案。
### 方法关键点
推出首个Agent网页抓取合规性评测基准ScrapeBench，覆盖1626个明确禁爬、269个未禁爬的主流网站，分别测试无法律提示、强法律提示两种场景下闭源/开源Agent的表现，同步设置180人人类基线组。
### 关键结果
禁爬场景下主流Agent合规率<5%，即使主动检查ToS和robots.txt规则仍合规率极低；未禁爬场景下存在过度拒绝问题，Claude Opus 4.6过度拒绝率达98.5%；人类合规率与Agent相当但过度拒绝率更高。

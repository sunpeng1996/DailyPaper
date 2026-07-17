---
title: Pretraining Data Can Be Poisoned through Computational Propaganda
title_zh: 通过计算式宣传实现大语言模型预训练数据投毒
authors:
- Victoria Graf
- Hannaneh Hajishirzi
- Noah A. Smith
- David Kohlbrenner
- Kyle Lo
affiliations:
- University of Washington
- Allen Institute for Artificial Intelligence
arxiv_id: '2607.15267'
url: https://arxiv.org/abs/2607.15267
pdf_url: https://arxiv.org/pdf/2607.15267
published: '2026-07-16'
collected: '2026-07-17'
category: LLM
direction: 大语言模型 · 预训练数据安全治理
tags:
- LLM-Poisoning
- Pre-training-Data
- Adversarial-Attack
- Data-Curation
- HalfLife
one_liner: 提出HalfLife分析框架，验证通过公共讨论界面向预训练数据投毒的可行性
practical_value: '- 自研/微调业务用LLM（如推荐文案生成、Agent应答）时，爬取公开语料需新增公共讨论区内容的恶意检测环节，避免投毒内容引入导致模型输出违规内容

  - 可复用HalfLife框架评估自爬训练语料经过清洗后的恶意内容留存率，针对性优化数据清洗规则，降低投毒风险

  - 采购/对接第三方预训练模型时，需补充投毒风险校验，验证是否存在特定触发词引导的恶意输出，避免业务合规风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有预训练数据投毒研究多基于维基百科等固定可控数据源，未覆盖网络爬取语料的大规模异构特性，也忽略了爬虫、数据清洗流程对投毒内容的过滤作用，对公开讨论界面这类低成本大规模注入渠道的风险缺乏量化评估方法。
### 方法关键点
1. 选取公共讨论界面作为网页级内容注入渠道，验证这类开放入口作为预训练数据投毒攻击向量的可行性
2. HalfLife分析方法可量化评估恶意内容经过网页爬取、多轮数据治理流程后，最终进入预训练语料的概率
### 关键结果
第三方网页公开讨论区是高效的预训练数据投毒入口，投毒内容可绕开常规数据清洗流程进入训练集，当前主流预训练语料治理流程对这类注入攻击的防御能力不足。

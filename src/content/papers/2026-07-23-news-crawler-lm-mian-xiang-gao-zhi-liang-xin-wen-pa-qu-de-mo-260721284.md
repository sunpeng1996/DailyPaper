---
title: 'news-crawler-LM: A Small Long-Context Model For High-Quality News Crawling'
title_zh: news-crawler-LM：面向高质量新闻爬取的小型长上下文模型
authors:
- Pascal Stolzenburg
- Jonas Golde
- Max Dallabetta
- Alan Akbik
affiliations:
- Humboldt-Universität zu Berlin
arxiv_id: '2607.21284'
url: https://arxiv.org/abs/2607.21284
pdf_url: https://arxiv.org/pdf/2607.21284
published: '2026-07-23'
collected: '2026-07-25'
category: LLM
direction: 长上下文小模型 · HTML结构化信息提取
tags:
- Long-Context LLM
- Fine-tuning
- HTML Parsing
- Web Crawling
- Small Language Model
one_liner: 微调得到低算力需求的小型长上下文模型，兼顾新闻HTML结构化提取的精度与泛化性
practical_value: '- 针对网页结构化提取任务，可复用「小长上下文模型微调+人工标注高质量训练集」的方案，替代大模型降本，适配电商商品详情页、评论页的结构化信息抽取需求

  - 跨域网页提取场景下，优先用规则库覆盖常见站点，长尾新站点用小模型兜底，平衡精度与部署成本

  - 信息提取任务可设计多输出范式（同时支持plaintext、Markdown、JSON输出），适配下游推荐、舆情分析等不同链路的输入要求'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前新闻网页HTML结构化提取面临两难：规则法精度高但跨站点需人工配置，泛化性差；通用大模型泛化好但算力成本高，无法大规模落地部署。

### 方法关键点
基于高质量人工校验的Fundus新闻爬取库标注数据，微调得到小参数量长上下文模型news-crawler-LM，支持原始HTML直接转纯文本、Markdown、结构化JSON三类输出，覆盖标题、作者、发布时间、正文等核心字段。

### 关键结果数字
- HTML转Markdown任务较基线提升+4.8 BLEU、+6.1 METEOR
- HTML转JSON任务较基线提升+2.2 BLEU、+4.1 METEOR
- 仅在未见过的发布商纯文本提取任务上，性能仅略优于规则解析库

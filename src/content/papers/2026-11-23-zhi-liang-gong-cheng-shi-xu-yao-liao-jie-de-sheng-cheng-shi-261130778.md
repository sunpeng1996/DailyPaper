---
title: 'What Quality Engineers Need to Know About Generative AI: Structured Data Extraction'
title_zh: 质量工程师需要了解的生成式AI知识：结构化数据提取
authors:
- Fadel M. Megahed
- Ying-Ju Chen
- Yamin Dahwich
- Zhao-Wei Chen
- Lucas K. Hung
- Arthur Carvalho
- L. Allison Jones-Farmer
- Ibrahim Yousif
- Inez M. Zwetsloot
affiliations:
- Miami University
- University of Dayton
- University of Cambridge
- University of Amsterdam
arxiv_id: '2611.30778'
url: https://arxiv.org/abs/2611.30778
pdf_url: https://arxiv.org/pdf/2611.30778
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM应用 · 结构化数据提取
tags:
- Structured Data Extraction
- LLM
- VLM
- Data Quality
- JSON Schema
one_liner: 提供LLM/VLM结构化数据提取落地方案，开源两个场景应用与代码，验证高提取准确率
practical_value: '- 电商场景可复用该方案提取用户评论、售后工单、客服对话的结构化字段，替代传统规则抽取降低维护成本

  - 做结构化提取时可引入人工校验环节核验字段准确率，分类、数学表达式等易出错字段需单独优化

  - 可参考其开源实现快速搭建业务自定义的结构化抽取工具，支持R/Python双语言适配不同工程栈'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
工业场景存在大量非结构化文本/多模态数据，传统规则式结构化提取适配性差、维护成本高，质量工程师群体缺乏可直接落地的生成式AI提取方案指引。

### 方法关键点
从测量系统视角梳理LLM/VLM结构化提取核心概念，提供R/Python双语言实现示例，落地两个开源web应用覆盖汽车召回通知提取、arXiv领域文献监测两个场景，引入人工校验流程保障提取质量。

### 关键结果
- 汽车召回场景：30份召回通知共720个字段的提取结果中，98.6%被判定为完全正确
- arXiv论文提取场景：45篇论文的摘要提取结果全部被评为正确/基本正确，仅分类字段、数学表达式存在误差

---
title: 'The Narrative Gap: Can LLMs Help Us Navigate Diverse Narratives Across Languages?'
title_zh: 《叙事鸿沟：大语言模型能否助力跨语言多元叙事浏览？》
authors:
- Nikhil Sharma
- Kelly Marchisio
- Kenton Murray
- Ziang Xiao
affiliations:
- Johns Hopkins University
- Cohere
- George Mason University
arxiv_id: '2611.12750'
url: https://arxiv.org/abs/2611.12750
pdf_url: https://arxiv.org/pdf/2611.12750
published: '2026-11-09'
collected: '2026-11-10'
category: Eval
direction: LLM跨语言信息获取能力评估
tags:
- LLM
- Cross-lingual
- Narrative Processing
- Benchmark
- Information Seeking
one_liner: 定义跨语言多元信息获取6项核心能力，发布NarrativeBench基准，实测14款LLM存在显著能力缺口
practical_value: '- 跨境电商/出海搜索推荐场景可复用6项叙事能力维度，优化多语言内容的视角平衡性，避免单一信息茧房导致的用户体验下降

  - 多语言搜索推荐系统的多样性评测可参考NarrativeBench的构建范式，覆盖争议话题、多语言query、多源内容的完整评测链路

  - 跨境服务Agent的信息查询模块可引入缺失叙事识别能力，补充不同语言区域的差异化信息，提升回答的全面性和可信度'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前LLM已成为用户获取信息的核心中介，但不同语言、区域对争议话题的叙事存在显著碎片化差异，现有系统难以支撑用户跨语言获取多元视角，易催生语言过滤泡、信息差等问题。
### 方法关键点
1. 定义跨语言多元信息获取的6项核心能力：3项基础能力（叙事纳入、叙事排除、缺失叙事识别）+3项高阶能力（多元叙事呈现、验证性查询下叙事覆盖保留、跨语言信息对等）
2. 发布NarrativeBench基准，包含23个争议话题下23种语言的1333篇新闻、460条Reddit真实用户query
### 关键结果
覆盖24种查询语言对14款LLM的评测显示，现有模型无法稳定支撑多元叙事导航，即使用户明确要求多样性，仍存在大量竞争视角暴露缺口，不同查询框架、语言的信息访问差异显著

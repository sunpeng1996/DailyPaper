---
title: 'Collaborative Search Meets Large Language Models: An Empirical Study'
title_zh: 大语言模型赋能协同搜索的实证对比研究
authors:
- Peiyuan Gong
- Jiamian Li
- Erhan Zhang
- Fengming Liang
- Kexin Liu
- Yue Chen
- Jiaxin Mao
affiliations:
- Renmin University of China
arxiv_id: '2611.04619'
url: https://arxiv.org/abs/2611.04619
pdf_url: https://arxiv.org/pdf/2611.04619
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: Agent 协同搜索效果实证研究
tags:
- Collaborative Search
- LLM Agent
- User Study
- Conversational Search
- RAG
one_liner: 通过80人分组用户实验对比4类协同搜索工具，明确LLM Agent的体验、行为及产出权衡
practical_value: '- 设计IM内嵌协同搜索Agent时，优先选择「上下文改写+澄清+RAG+来源引用」的CoSearchAgent架构，其整体用户满意度比纯参数QA
  Agent高12%，比纯搜索插件高16%，平衡体验与信息可信度

  - 内部协作场景优先上线轻量QAAgent：可降低21%用户感知工作量，提升39%团队沟通轮次，大幅提高信息共享与协作效率

  - 面向内容创作的搜索工具必须保留原始网页跳转入口：仅靠Agent合成回答会导致产出内容丰富度下降7%，无法满足深度内容创作需求

  - 优化Agent主动澄清阈值：过度澄清会增加20%+任务耗时，反而抵消信息合成带来的效率收益，需根据场景控制澄清触发条件'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的Agent已具备对话内协同信息检索能力，但缺乏系统实证研究对比其与传统搜索工具（独立搜索引擎、对话内嵌搜索插件）在用户体验、协作行为、产出质量上的差异，无法指导协同搜索Agent的产品设计与优化。

### 方法关键点
- 设计4类对比搜索场景：独立Google搜索、对话内嵌返回结果列表的SearchAgent、仅靠LLM参数知识回答的QAAgent、带多轮上下文改写+主动澄清+RAG+来源引用的CoSearchAgent
- 招募80名学生组成40组双人搭档，通过拉丁方设计平衡任务顺序，每组完成4类开放知识探索任务（AI绘画、儿童自闭症、浪漫主义音乐、空气污染）
- 从感知工作负载、协作体验、Agent体验、沟通行为、证据使用、产出报告质量6个维度量化效果，结合半结构化访谈定性挖掘用户需求

### 关键实验
对比基线为Google搜索、SearchAgent，核心结果：CoSearchAgent整体满意度达5.48/7，为所有方案最高；QAAgent降低21%用户感知工作量，团队沟通轮次提升39%；传统搜索工具产出的报告丰富度比LLM Agent高7%，但内容重复度高40%以上；CoSearchAgent的报告独立性达83.84%，比传统搜索工具高23个百分点。

### 核心结论
协同搜索Agent的核心价值是降低协作门槛而非替代用户判断，需要在合成效率、来源可验证性、交互可控性三者之间做场景化权衡。

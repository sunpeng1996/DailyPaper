---
title: 'On the Maintenance and Co-evolution of Agent Plugins: An Empirical Study of
  Claude Code Plugin Marketplaces'
title_zh: Claude Code插件市场Agent插件维护与协同演化实证研究
authors:
- Ahmed Hereiz
- Yingzhe Lyu
- Hao Li
- Bram Adams
- Ahmed E. Hassan
affiliations:
- Queen's University, Canada
arxiv_id: '2608.28497'
url: https://arxiv.org/abs/2608.28497
pdf_url: https://arxiv.org/pdf/2608.28497
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent · 插件生态维护与演化
tags:
- Agent Plugin
- Plugin Marketplace
- Software Evolution
- Claude Code
- Empirical Study
one_liner: 首次大规模实证分析Claude Code插件市场特征与维护规律，揭示Agent插件与传统软件的差异
practical_value: '- 搭建企业内部Agent插件市场时，可优先覆盖软件工程类插件（占生态61.3%），满足研发侧提效需求

  - 维护混合自然语言指令+执行脚本的Agent技能时，需建立两类文件的同步校验机制，避免78%的协同变更不同步导致的静默故障

  - 管理Agent插件提交时，需调整传统代码提交分类规则，原docs/style/refactor等标签在AI原生软件中含义已发生偏移

  - 做Agent辅助开发时可重点覆盖插件的功能迭代场景，该类提交占比是传统开源软件的2倍以上，AI辅助效率更高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent插件是扩展Agent能力、沉淀可复用工作流的核心载体，但这类AI原生软件由自然语言指令、执行脚本、配置文件混合构成，与传统代码软件的形态差异极大，过往没有针对其维护、协同演化规律的大规模实证研究，无法支撑插件生态的健康治理、配套工具研发。
### 方法关键点
- 爬取GitHub上星数≥10的1926个Claude Code插件市场仓库，覆盖8351个插件、77773次插件相关提交
- 结合正则匹配、人工分层抽样标注、LLM分类，按传统Conventional Commits Specification（CCS）对提交分类，对比传统开源软件的提交特征
- 采用关联规则分析不同组件的协同变更概率，识别跨组件的功能耦合关系
### 关键结果
- 插件市场上线6个月内提交量增长8.8倍，仍处于高速增长期，61.3%的插件面向软件工程类任务
- 插件的功能类提交占比39.6%，是传统开源软件的2.3倍，34.9%的提交由Claude参与协同编写
- 传统CCS的docs、perf、style、refactor四类标签在插件仓库中含义发生显著偏移，74%的docs提交实际修改的是AI执行用的指令而非面向人类的文档
- 技能目录下的Markdown指令与执行脚本的协同变更中78%为强功能耦合，是传统软件工程中不存在的新型维护依赖
### 核心结论
以自然语言为核心交付物的AI原生软件，其维护规则与传统代码软件存在本质差异，现有软件工程方法论无法直接复用。

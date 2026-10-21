---
title: Unsupervised Tool Evolution for Coding Agents in Data-Lake Analytics
title_zh: 面向数据湖分析编码Agent的无监督工具演化框架TEAL
authors:
- Yuqing Yang
- Yurong Liu
- Deqing Fu
- Manav Garg
- Sravan Babu Bodapati
- Fatma Ozcan
- Alon Y. Halevy
- Jiani Zhang
affiliations:
- University of Southern California
- Google
- New York University
arxiv_id: '2610.27327'
url: https://arxiv.org/abs/2610.27327
pdf_url: https://arxiv.org/pdf/2610.27327
published: '2026-10-18'
collected: '2026-10-21'
category: Agent
direction: Agent 无监督工具演化优化
tags:
- LLM Agent
- Tool Evolution
- Unsupervised Learning
- Data Lake
- Synthetic Data Generation
one_liner: 提出无监督工具演化框架TEAL，无需标注即可生成可复用工具库提升编码Agent数据湖分析表现
practical_value: '- 双路工具生成设计可复用：业务Agent开发中，可同时从全局业务资源（如全量商品库、用户行为库）生成通用工具，从历史请求的Agent运行轨迹提取场景化工具优化需求，兼顾通用性和针对性

  - 无监督工具验证机制可直接落地：无需标注即可验证工具有效性，仅保留满足「工具被主动调用、任务无额外步骤完成、答案有轨迹证据支撑」的工具更新，适配电商/广告场景标注成本高的现状

  - 紧预算训练技巧可迁移：训练工具库时给Agent设置更严格的step/响应延迟预算，可获得更有效的工具优化信号，训练出的工具库在宽松预算下表现更优，适配搜索推荐等高响应要求场景

  - 合成训练数据方案可复用：业务冷启动阶段真实请求不足时，可基于少量种子问题和业务资源生成合成训练问题，演化出的工具库效果与真实数据训练的效果相当'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
数据湖分析场景下的编码Agent每次处理请求都要从零完成数据发现、清洗、融合流程，重复工作多、效率低；现有工具生成方法要么依赖高成本的专家标注，要么仅验证工具可运行性，无法判断工具实际效用，易引入无效甚至负向工具。

### 方法关键点
- 双路工具生成：Explorer Agent全局扫描数据湖生成通用工具（如元数据目录、检索工具），Critic Agent分析Worker Agent运行轨迹，针对性提出工具新增/修复/优化建议
- 无监督验证机制：工具更新后重跑触发更新的请求，仅保留同时满足三个条件的更新：Worker主动调用新工具、任务完成无额外步骤、答案变更有轨迹证据支撑
- 配套TEAL-Q合成问题生成器：基于少量种子问题，从数据湖集群生成可回答、有难度的合成训练问题，解决真实请求不足的冷启动问题

### 关键实验
在KramaBench、LakeQA两个数据集上测试4款Worker LLM，15步紧预算下，Sonnet-5在KramaBench精度提升9.3个点，LakeQA提升21.7个点；20步紧预算训练的工具库放到30步宽松预算下使用，精度达68.3，优于基线（59.6）和直接在30步训练的版本（64.2）；50个合成问题训练的工具库效果和真实问题训练的基本持平。

### 核心结论
无监督工具演化在紧step预算下效果最优，预算压力可替代标注作为有效训练信号。

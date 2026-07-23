---
title: 'CIR at iKAT SCAI 2026: Exploring Clarification Need Prediction in Agentic
  Conversational Search'
title_zh: iKAT SCAI 2026参赛方案：Agent对话搜索的澄清需求预测探索
authors:
- Nolwenn Bernard
- Jüri Keller
- Philipp Schaer
affiliations:
- TH Köln, Cologne, Germany
arxiv_id: '2607.19801'
url: https://arxiv.org/abs/2607.19801
pdf_url: https://arxiv.org/pdf/2607.19801
published: '2026-07-22'
collected: '2026-07-23'
category: Agent
direction: Agent 对话式搜索交互优化
tags:
- Conversational Search
- Clarification Need Prediction
- Agentic Search
- Mixed Initiative
- LLM4IR
one_liner: 基于Agent架构搭建对话搜索系统，对比两款澄清需求预测模型的竞赛表现
practical_value: '- 电商对话导购/搜索场景可直接复用「澄清需求二分类+零-shot生成澄清问题」的交互逻辑，解决用户模糊query导致的召回不相关问题，降低用户跳出率

  - 低成本落地Agent搜索系统时，可参考将传统pipeline（query改写、召回、排序、生成）封装为工具、用开源大模型做无训练orchestrator的架构，大幅降低开发门槛

  - 澄清需求预测模型可按需选型：追求回复相关性与用户满意度选Zef-CNP BERT，追求对话交互活跃度选MuSIc，两者性能差距极小'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的对话式搜索逐渐普及，但用户输入模糊、上下文指代不清等问题长期存在，传统固定流程的搜索pipeline无法灵活判断是否需要主动发起澄清交互，容易导致召回结果偏差、用户满意度低。iKAT SCAI 2026竞赛聚焦个性化、上下文感知的对话搜索系统评估，为验证澄清需求预测模块的实际价值提供了标准化测试环境。

### 方法关键点
- 采用轻量Agent架构：将传统搜索pipeline的query改写、个人偏好匹配、召回排序、回答生成，以及澄清需求预测、澄清问题生成全部封装为工具，由Gemma-4-26B大模型作为orchestrator基于预设提示词调度，无需额外训练调度器
- 对比两款成熟的澄清需求二分类模型：① MuSIc模型，输入全对话历史，基于MSDialog预训练、ClariQ数据集微调；② Zef-CNP BERT模型，输入改写后的独立query，基于LLM生成的合成数据集训练
- 偏好匹配、澄清问题生成、回答生成均采用开源大模型零-shot实现，降低开发成本

### 关键结果
在iKAT官方测试集上，两组仅澄清模型不同的跑分结果差距极小：
- 对话交互维度：Zef-CNP组混合主动策略平均分3.0/5，个性化得分3.91/5，用户满意度3.16/5；MuSIc组交互活跃度得分更高，混合主动策略平均分3.16/5
- 召回排序为核心短板：Zef-CNP组仅41.5%的用户query触发了召回流程，全组最高AP仅0.0308；MuSIc组仅14.5%的query触发召回，基础检索能力不足会完全抵消交互模块的优化效果

### 核心结论
对话搜索系统中，澄清需求预测是提升交互体验的低投入高回报模块，但召回排序的基础能力仍是决定整体效果的核心瓶颈

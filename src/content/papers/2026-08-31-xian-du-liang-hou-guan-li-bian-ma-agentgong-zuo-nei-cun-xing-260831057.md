---
title: 'Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents'
title_zh: 《先度量后管理：编码Agent工作内存性能评估》
authors:
- Le Chen
- Zishen Wan
- Baixi Sun
- Xiaolong Ma
- Chih-Hsuan Yang
- Feng Yan
- Sheng Di
- Franck Cappello
- Rajeev Thakur
affiliations:
- Argonne National Laboratory
- Columbia University
- University of Houston
arxiv_id: '2608.31057'
url: https://arxiv.org/abs/2608.31057
pdf_url: https://arxiv.org/pdf/2608.31057
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent 工作内存评估与优化
tags:
- Agent Memory
- Working Memory
- Memory Management
- Agent Evaluation
- Coding Agent
one_liner: 揭示编码Agent工作内存的语义异质性，提出4层评估框架避免内存管理策略效果误判
practical_value: '- 搭建业务Agent（比如电商导购Agent、推荐解释Agent）的内存系统时，不要将所有上下文视为同质化token池，可按语义类型（用户指令、商品/内容特征、工具返回结果、Agent推理状态）分类做差异化压缩/召回，比如静态商品特征可设置更高压缩率，工具返回的实时结果可设置更短生命周期

  - 评估内存优化策略不能仅对标称token预算，需同时统计三个维度：实际投递到LLM的上下文量、额外管理开销（比如RAG的embedding计算、重要性打分的LLM调用成本）、业务效果，避免出现标称预算相同但实际效率/效果差异大的问题

  - 新内存策略的效果必须做跨任务/跨场景验证，调参集上的收益大概率无法直接迁移到未见过的业务场景，不要过度拟合开发集指标'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent工作内存管理普遍将不同语义类型的上下文作为同质化token池处理，忽略语义异质性对留存、压缩效率的影响；且现有评估体系仅对标称token预算，无法准确衡量策略的真实收益，极易出现开发集效果显著但上线后无收益甚至负向的问题。
### 方法关键点
- 对工作内存对象做语义分类：指令、工件、工具输出、Agent生成状态4类，分别统计容量、留存时长、压缩比等特征
- 验证两类语义感知内存策略：①对象感知压缩策略：按对象类型、年龄、访问次数、过期状态打分，分层降级为压缩/摘要/指针形式；②检索式管理策略：融合时效性、相关性、重要性三个维度打分做上下文召回
- 提出4层评估框架：从存储状态、投递上下文、管理开销、任务/流程结果四个维度全链路衡量内存策略的真实效果
### 关键实验结果
- 数据集：55条SWE-bench编码Agent历史轨迹，包含15条调参任务、8条跨域held-out任务、24条检索策略验证任务
- 对比Baseline：FIFO、LRU、统一压缩策略
- 核心数字：对象感知策略在调参集上比FIFO减少1.63次重复工具调用，但是在held-out集上效果无统计显著性；检索式策略相比FIFO额外增加285次重要性打分LLM调用，端到端延迟平均高67s，无显著效果收益
### 最值得记住的结论
Agent工作内存不是同质化的token池，评估内存管理策略不能只看标称token预算，必须先度量再管理。

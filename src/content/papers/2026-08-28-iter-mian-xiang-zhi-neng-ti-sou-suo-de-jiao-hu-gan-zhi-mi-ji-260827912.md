---
title: 'ITER: Interaction-Aware Retrieval for Agentic Search'
title_zh: ITER：面向智能体搜索的交互感知密集检索器
authors:
- Haodong Chen
- Shuai Wang
- Yu Yin
- Shengyao Zhuang
- Guido Zuccon
- Teerapong Leelanupab
affiliations:
- The University of Queensland
arxiv_id: '2608.27912'
url: https://arxiv.org/abs/2608.27912
pdf_url: https://arxiv.org/pdf/2608.27912
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent 多步搜索交互感知检索优化
tags:
- Agentic Search
- Dense Retrieval
- Trajectory Learning
- Contrastive Learning
- Multi-step Reasoning
one_liner: 结合交互历史与轨迹分层负例训练的检索器，大幅提升多步智能体搜索成功率
practical_value: '- 多步检索场景（如电商导购Agent、多轮搜索）可直接复用「主query+当前子query+历史子query」的query表示，避免重复召回已浏览的商品/内容，提升新信息召回率

  - 训练多轮交互场景的检索模型时可采用分层负例策略：已访问有效内容作为冗余负例（权重最高）、已访问无效内容作为硬负例、未访问内容作为弱负例，加权对比损失能更好适配动态效用需求

  - 不要把已浏览的商品/内容文本直接加入query编码，会降低召回效果，用历史子query表示已探索方向的泛化性更强

  - 跨Agent迁移场景优先使用结构化交互历史（主query、子query序列），不要依赖Agent的自由式预搜索推理，后者泛化性更差'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有面向Agentic Search的检索器仅以当前子query为输入训练，完全忽略历史交互信息，导致多步搜索时频繁重复召回已访问过的内容，遗漏未访问的关键证据，大幅拉低智能体任务成功率。

### 方法关键点
- **历史感知Query表示**：默认组合主问题、当前子query、历史子query构造检索输入，精准识别已探索的搜索方向，避免重复召回
- **轨迹分层正负例构造**：基于智能体交互轨迹定义：当前搜索后访问的有效文档为正例；已访问有效文档为冗余负例、已访问无效文档为硬负例、未访问文档为弱负例
- **加权对比损失**：负例按置信度分配权重(3.0/1.0/0.3)，正例按后访问推理长度动态加权，适配多轮交互下文档效用的动态变化

### 关键结果
在InfoSeek-Eval、BrowseComp-Plus两个基准上跨3个模型家族6个Agent backbone测试：相比SOTA LRAT平均提升7.5% InfoSeek-Eval任务成功率、13.5% BrowseComp-Plus成功率；相比AgentIR跨Agent鲁棒性更强，5个未见过的Agent上任务成功率均更高。

### 核心结论
面向智能体的多步检索应该优化整个搜索轨迹的进展，而非孤立步骤的相关性。

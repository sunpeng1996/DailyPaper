---
title: 'ReCite: Agentic Reasoning for Faithful Citation'
title_zh: 面向可信引用的智能体推理框架ReCite
authors:
- Yuyang Huang
- Bobo Li
- Jiajia Song
- Yuzhe Ding
- Chong Teng
- Fei Li
- Donghong Ji
affiliations:
- 武汉大学
- 新加坡国立大学
arxiv_id: '2609.09156'
url: https://arxiv.org/abs/2609.09156
pdf_url: https://arxiv.org/pdf/2609.09156
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: Agent 检索校验闭环架构优化
tags:
- Agentic Reasoning
- Citation Recommendation
- Self-Correction
- GRPO
- RAG
one_liner: 提出解耦式Agent推理框架ReCite，基于验证反思闭环解决引用误归因问题，性能超越百亿级大模型
practical_value: '- 可复用解耦Agent设计思路：将复杂任务拆分为定位、查询生成、调度校验三个独立轻量化模块，每个模块仅需小模型SFT+轻量RL即可完成，相比端到端黑盒大模型Agent成本降低80%以上，可控性更强，可直接迁移到电商导购Agent、售后工单匹配Agent等场景

  - 可直接复用GRPO优化Query生成的奖励设计：将查询生成的奖励拆分为格式合规、实体召回、意图对齐三个维度，无需额外训练critic网络，电商搜索Query改写、RAG系统查询重写模块可直接套用该策略，大幅提升检索相关性

  - 可新增检索后校验闭环解决RAG的逻辑不匹配问题：检索结果返回后先做claim-evidence一致性校验，不匹配则自动重写查询二次检索，可解决电商场景下用户问题匹配商品卖点、评价归因等场景中常见的语义相似但逻辑不匹配的问题，降低错误率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前自动引用推荐系统普遍基于语义相似度检索，虽已解决伪造不存在文献的问题，但核心痛点是误归因：推荐的文献真实存在，但逻辑上无法支撑用户论点。本质是行业将引用任务错误定义为检索任务，忽略了引用需要基于场景意图的逻辑验证，且现有单向流水线架构无自纠错能力，错误一旦产生无法挽回。
### 方法关键点
- 解耦架构：拆分三个独立模块，CiteLocator识别文本中需要加引用的逻辑断点，区分强制/可选引用；QueryPlanner基于8类引用意图生成精准检索关键词；Master Brain负责调度检索工具、校验候选文献与论点的一致性，校验失败则触发反思重查闭环。
- 数据构造：爬取10893篇2024-2025年顶会LaTeX论文，构造包含位置感知、意图推理、反思轨迹三类标注的专用数据集，用大模型后验标注的方式生成高质量训练数据，大幅降低人工标注成本。
- 训练策略：三个模块均基于4B参数的Qwen3小模型，CiteLocator用加权交叉熵解决引用标记样本稀疏问题，QueryPlanner用SFT+GRPO优化，奖励融合格式合规、实体召回、意图对齐三个维度，Master Brain基于反思轨迹做SFT训练工具调用和自纠错逻辑。
### 关键结果
在200段跨领域未见过的测试文本上，ReCite严格引用准确率F1达39.15%，超过1.6T参数的DeepSeek-V4-Pro（31.77%）和27B参数的Qwen3.6-27B（25.83%），宽松准确率（接受逻辑匹配的替代文献）达55.14%，引用位置识别F1达89.71%，远超所有零-shot大模型基线。
**最值得记住的一句话**：对于要求事实准确性的检索类任务，小模型+解耦模块化+自校验闭环的Agent架构，效果可以远超过参数大两个量级的通用大模型，同时成本和可控性更优

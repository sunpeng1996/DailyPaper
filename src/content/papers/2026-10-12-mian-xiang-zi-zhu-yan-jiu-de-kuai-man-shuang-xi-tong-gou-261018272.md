---
title: 'JevGPT: Thinking Fast and Slow in Autonomous Research'
title_zh: 面向自主研究的快慢双系统Agent架构JevGPT
authors:
- Yasheng Sun
- Yanning Dai
- Yimeng Chen
- Nanbo Li
- Firas Laakom
- Yifan Xu
- Piotr Piękos
- Mateusz Ostaszewski
- Wenyi Wang
- Cheng Luo
affiliations:
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2610.18272'
url: https://arxiv.org/abs/2610.18272
pdf_url: https://arxiv.org/pdf/2610.18272
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: Agent 双系统架构优化
tags:
- Dual-System Reasoning
- Autonomous Research Agent
- Evidence Retrieval
- Cost Efficiency
- LLM Agent
one_liner: 提出耦合快证据处理与慢研究规划的双系统自主研究Agent，兼顾性能与成本效率
practical_value: '- 可直接复用双系统分工架构做搜索/导购Agent：轻量小模型做System One完成召回片段相关性判断、候选粗筛、query意图匹配，大模型做System
  Two完成排序决策、多轮规划、结果生成，最多可降低70%以上大模型调用成本

  - Hybrid BM25召回trick可直接落地电商搜索：将文档级BM25得分与段落级最大BM25得分等权归一化后融合排序，无需引入新模型即可提升候选集的相关段落覆盖率

  - 异步证据发现机制可迁移到长会话推荐场景：后台异步挖掘用户潜在需求相关的商品/内容证据，无需打断主会话交互流，即可提升推荐结果的覆盖度和新颖性

  - 明确证据请求+阈值过滤的上下文管理方法可优化RAG效果：仅将满足相关性阈值的原始段落送入大模型，既减少无效token消耗，又避免信息压缩带来的事实错误'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自主研究Agent普遍存在检索覆盖率与证据使用率的Gap：检索到的大量相关源未被有效利用，直接用大模型处理全量检索内容则成本高、速度慢，无法在有限预算下充分挖掘证据价值，同时检索到的信息也难以有效反哺后续研究规划。

### 方法关键点
- 双系统分工架构：System Two（大模型，如GPT-5.5）负责全局研究规划、设定证据目标、整合多源证据输出最终结果；System One（轻量快思考模型Jev）负责并行完成证据定位、相关性打分、自适应阅读，同时异步执行证据发现任务。
- 混合召回策略：将文档级BM25得分与段落级最大BM25得分分别做min-max归一化后等权融合排序，兼顾全文匹配度和局部关键段落的匹配度。
- 证据处理流水线：QA场景下按System Two提出的局部证据问题定位关键段落，排序场景下按4级相关性标签筛选有效文档；后台异步评估检索到的前K个候选挖掘新证据，主动供给System Two优化后续规划。

### 关键实验
在BrowseComp-Plus（830个事实问答）、NeuCLIRBench（105个文档排序）两个数据集上，对比ReAct、Pi-Serini、AtlasNav、RankGPT等7个SOTA基线：问答任务上准确率达90.48%，比最优基线高0.48pp，单query API成本0.668美元，比同性能基线低40%+，推理速度快20%；排序任务上nDCG@20达0.539，比最优基线高1.5pp，单主题API成本0.5838美元，为所有GPT类方法最低。

### 核心结论
局部证据判断和全局研究规划对信息范围的需求天然不同，将二者拆分到不同能力的模型处理，是兼顾Agent性能和成本效率的核心路径

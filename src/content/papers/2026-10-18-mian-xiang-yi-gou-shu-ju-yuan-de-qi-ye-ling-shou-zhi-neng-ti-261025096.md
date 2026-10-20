---
title: Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows
  over Heterogeneous Data Sources
title_zh: 面向异构数据源的企业零售智能体RAG基准与框架
authors:
- Jeonghwan Choi
- Jibin Hwang
- Hayoon Park
- Hyeonjae Cheon
- Hwanjun Song
affiliations:
- KAIST
- Cluvion
- GS Retail
arxiv_id: '2610.25096'
url: https://arxiv.org/abs/2610.25096
pdf_url: https://arxiv.org/pdf/2610.25096
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: Agent 零售异构数据源RAG优化
tags:
- Agentic RAG
- Retail AI
- Heterogeneous Data
- Benchmark
- Multi-hop Reasoning
one_liner: 提出零售多源异构RAG基准RetailBridge与配套框架RetailRAG，定位跨源编排为核心瓶颈
practical_value: '- 构建内部电商多源异构RAG评测集时，可复用原子QA递归合成方法，通过实体链接、答案链接算子生成难度可控的多跳测试用例，规避真实数据隐私风险

  - 搭建企业级电商RAG系统时，可直接复用RetailRAG三个核心设计：前置auto-schema briefing注入库表元数据、跨源路由规划链、局部失败诊断修订，大幅提升跨表+文本混合查询准确率

  - 选型零售智能体LLM backbone时，优先测试Qwen3.6-Plus、Gemma-4-31B-IT这类跨源编排表现更优的模型，无需盲目堆大模型参数，性价比更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agentic RAG多适配单一同源语料，缺乏针对零售企业异构数据源（结构化订单/商品表、非结构化评价/咨询文本）的可控评测基准，跨源证据链编排能力难以量化，且现有框架在零售场景下错误率极高，无法支撑商家分析、智能客服等实际业务 workflow。
### 方法关键点
- 数据侧：构建RetailBridge多源零售QA基准，基于persona驱动的模拟生成无隐私风险的异构零售数据集，通过两步合成QA：第一步生成单源原子QA并经过执行校验+LLM校验双过滤，第二步通过实体链接、答案链接算子递归合成1~3跳多源复合查询，最终得到1680条标注完备的测试用例，覆盖推理深度、跨源能力、证据模态三个评估维度。
- 框架侧：提出RetailRAG零售专属Agentic RAG框架，核心三个模块：1）auto-schema briefing：提前提取库表元数据、跨源关联键、枚举值约束、KPI计算公式注入规划prompt；2）source-routed plan chaining：提前规划全链路每一步的数据源、查询类型，显式传递中间结果；3）diagnostic plan revision：失败步骤局部诊断修订，无需全链路重跑。
### 关键结果
在RetailBridge上对比6个主流RAG baseline，RetailRAG的LLM-judge准确率达0.429，比最优baseline HetaRAG高出46%；评测10款开源/闭源LLM，发现从1跳到3跳准确率平均下降50%以上，跨源查询比单源查询准确率平均低20%，多源编排而非模型规模是核心瓶颈，最优模型Qwen3.6-Plus准确率仅0.511，仍有较大优化空间。

企业零售RAG的核心瓶颈不是大模型参数规模，而是显式的跨异构数据源证据编排能力。

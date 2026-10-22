---
title: 'Code Comprehensor: Hierarchical Documentation and Cross-Modal Retrieval for
  Large Repositories'
title_zh: Code Comprehensor：面向大型代码仓库的分层文档生成与跨模态检索框架
authors:
- Sujoy Roychowdhury
- Joseph H. R. Isaac
- Jiangning Gao
- Martin Klitte
- Diarmuid Corcoran
affiliations:
- Ericsson R&D
arxiv_id: '2610.30016'
url: https://arxiv.org/abs/2610.30016
pdf_url: https://arxiv.org/pdf/2610.30016
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 代码智能 · Agent 检索编排
tags:
- Code Retrieval
- Contrastive Learning
- RAG
- Agent Orchestration
- Hierarchical Documentation
one_liner: 整合分层代码文档生成、跨模态对比检索与Agent编排的大型代码库理解方案
practical_value: '- 后序遍历分块算法可直接迁移到电商长文本商品库、运营规则库的多粒度文档生成场景，在保留层级关联的同时适配LLM上下文窗口限制，避免长上下文性能衰减

  - 带语义锚定的合成query生成方法可复用在跨模态检索的训练数据增强环节，比如query-商品、query-广告的对齐训练，大幅提升长尾query的召回准确率

  - 基于MCP的多Agent编排架构（专用Agent分工+主Agent调度）可直接迁移到电商智能客服、商品知识库问答、大促规则答疑等业务场景，平衡检索效率与回答准确率

  - 多正例InfoNCE损失的设计可复用在跨模态检索模型训练中，解决同一实体对应多视角描述的对齐问题，提升跨域匹配效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大型代码库规模普遍远超LLM上下文窗口，全量输入不仅成本高昂，还会因长上下文性能衰减导致结果不可靠；现有代码检索方案仅针对孤立代码片段，缺乏全局层级关联与上下文信息，无法支撑复杂代码理解需求，大幅拖慢开发人员的onboarding、维护、重构效率，也难以对接Agent实现自动化代码问答。

### 方法关键点
- 静态分析生成CodeGraph，保留代码调用、层级关联，暴露API支持灵活遍历
- CodeScribe模块采用后序遍历分块算法处理超大调用树，生成多视角分层文档，支持git commit驱动的增量更新，大幅降低重复生成成本
- CodeContrast为CLIP风格双编码器，采用多正例InfoNCE损失训练，对齐文本与代码嵌入空间；训练数据加入父/兄弟节点上下文、语义锚定的合成query增强，覆盖更多真实查询意图
- 基于MCP的Master Agent调度3个专用Agent（CodeScribe RAG、CodeGraph遍历、CodeContrast检索），自动组装上下文生成准确的自然语言回答

### 关键实验
在OpenCV（1.2M LOC）和爱立信5M行私有C代码库上测试，对比仅用方法+原生注释的基线D1：
- D2（加入CodeScribe生成的自注释）在OpenCV非合成query的Text→Code Top1准确率达94.45%，较D1提升1.77个百分点
- D3（额外加入父/兄弟上下文+合成query）在合成query场景下Top1准确率较D2提升14.59个百分点（OpenCV）、8.72个百分点（私有库）
- 整套Agent系统的RAGAS Faithfulness得分超93%，CodeContrast检索延迟<50ms，端到端回答延迟3-5秒

### 核心结论
需根据目标查询分布选择检索增强策略，匹配文档的短query用浅层上下文即可覆盖，复杂推理类query需加入多粒度层级上下文才能获得最优效果。

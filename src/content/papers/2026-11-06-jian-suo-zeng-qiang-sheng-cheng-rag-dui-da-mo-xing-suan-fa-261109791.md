---
title: Assessing the Impact of Retrieval-Augmented Generation on Algorithmic Problem-Solving
title_zh: 检索增强生成（RAG）对大模型算法问题求解能力的影响评估
authors:
- Gabriel Souza Baggio
- Gabriel Machado Lunardi
- Guilherme Medeiros Machado
- Subhankar Maity
- Faiza Belbachir
- José Palazzo Moreira de Oliveira
affiliations:
- Federal University of Santa Maria
- LyRIDS lab, ECE Engineering School, Paris
- Federal University of Rio Grande do Sul
arxiv_id: '2611.09791'
url: https://arxiv.org/abs/2611.09791
pdf_url: https://arxiv.org/pdf/2611.09791
published: '2026-11-06'
collected: '2026-11-09'
category: RAG
direction: RAG · LLM算法推理优化
tags:
- RAG
- Code Generation
- LLM Reasoning
- Membership Inference
- Embedding Retrieval
one_liner: 提出动态阈值RAG框架结合Min-K归因，验证相似案例检索提升LLM算法解题性能
practical_value: '- RAG动态阈值策略可直接复用：在电商文案生成、搜索query改写的RAG系统中，基于当前查询最高相似度动态调整召回阈值（基础70%，高于85%收紧、低于75%放宽），平衡召回率和噪声控制

  - 检索样本量控制策略可迁移：面向生成式推荐、Agent工具调用的few-shot召回，固定最多返回Top3相关样本，避免无关内容占用上下文窗口、干扰模型输出

  - Min-K归因方法可用于业务合规校验：借鉴该方法判断LLM生成的推荐理由、营销文案是否来自授权业务知识库，区分生成内容是记忆、幻觉还是RAG召回的合规内容

  - 无关样本负向效应可指导prompt工程：不要在prompt中加入与当前任务无关的few-shot示例，避免引入噪声拉低生成效果，该结论适用于所有LLM驱动的电商业务场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM在通用代码生成任务上表现优异，但在需要强算法推理的竞赛编程场景下性能极差，即便SOTA模型也难以解决中高难度问题，幻觉问题突出；现有RAG方案未针对算法解题场景做适配优化，也无法区分性能提升是来自真实推理能力增强还是预训练数据记忆，亟需专门的框架验证RAG对算法问题求解的实际价值。
### 方法关键点
- 检索模块：采用all-MiniLM-L6-v2生成问题文本embedding，基于FAISS做L2相似度检索，搭配动态阈值机制：基础相似度阈值70%，若当前查询最高相似度>85%则收紧阈值，<75%则适当放宽（最低不低于70%），最多返回Top3相似样例控制噪声
- 对照实验设计：设置三组对齐的测试条件：仅原始问题描述的零-shot基线、补充随机无关样例的随机检索基线、补充相似样例的RAG方案，覆盖6款主流通用/代码专用LLM
- 归因分析：引入Min-K成员推理方法，通过分析生成代码的最低K% token概率，判断内容是否来自模型预训练记忆，区分真实推理增益和记忆召回效应
### 关键结果
基于CodeContests数据集，取13328道训练题为RAG知识库，筛选81道存在相似训练样例的测试题做评估：整体平均pass@1方面，RAG组达20.37%，较零-shot基线（17.9%）提升2.47个百分点，较随机检索基线（17.28%）提升3.09个百分点，平均Elo得分提升89分；SOTA推理模型DeepSeek-R1采用RAG后pass@1从61.7%提升至64.2%，数论类问题Elo评分从1604暴涨至2191。
### 核心结论
给LLM补充上下文时，无关案例带来的噪声会拉低性能，只有精准匹配的相关案例才能带来正向增益，且增益幅度与任务对关键启发信息的敏感度正相关。

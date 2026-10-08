---
title: 'ExperienceIndex: Artifact-Grounded Memory'
title_zh: ExperienceIndex：面向AI Agent的锚定实体的经验记忆系统
authors:
- Peter Baile Chen
- Geoffrey X. Yu
- Xinming Liu
- Samuel Madden
- Dan Roth
- Jacob Andreas
- Doug Downey
- Michael Cafarella
affiliations:
- MIT
- McKinsey & Company
- Oracle AI & UPenn
- AI2
arxiv_id: '2610.10091'
url: https://arxiv.org/abs/2610.10091
pdf_url: https://arxiv.org/pdf/2610.10091
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent 实体锚定经验记忆优化
tags:
- Agent_Memory
- Experience_Reuse
- LLM_Agent
- RAG
- Middleware
one_liner: 提出锚定实体的Agent经验记忆层，复用历史推理轨迹提升任务效果并降低推理成本
practical_value: '- 电商智能客服/商品知识库Agent可直接复用架构：将商品详情、售后工单、咨询历史作为artifact，构建单实体+实体对经验记忆，减少重复检索成本，提升多轮问答准确率

  - 推荐场景可借鉴记忆结构：单artifact经验对应物品/用户的历史使用记录，artifact-pair经验对应物品共现/关联规则，复用历史排序/召回推理轨迹，降低冷启动阶段的检索开销

  - 工程落地可直接作为中间件：无需修改现有ReAct架构的Agent逻辑，同时支持跨任务经验迁移（如Text-to-SQL经验直接复用给事实QA），适配性强落地成本低

  - 高并发场景可采用强弱模型蒸馏方案：用大模型生成的推理轨迹构建经验库，小模型搭配经验库可达到接近大模型的效果，推理成本最高降90%以上'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有AI Agent记忆系统仅存储用户偏好、通用推理模式，未针对共享实体库（商品库、法律条文、代码库等）的任务优化，新任务需全量检索实体，易出现答案缺漏，且推理成本高、延迟大，无法适配高并发业务场景。

### 方法关键点
- 经验分层存储：①单实体经验：记录每个实体的历史任务贡献摘要、关联任务描述、用到的内容片段，用于快速判断实体相关性；②实体对经验：记录实体间关联关系（共现实体、可连接表、同主题文档等），用于补全检索遗漏的相关实体，提升答案完整性
- 检索流程：先基于新任务query和检索到的artifact ID召回单实体经验，用LLM过滤无关实体，再基于实体对经验召回关联邻居实体，二次过滤后补充到检索结果
- 部署为轻量中间件：对接现有Agent的检索工具和模型上下文，无需修改原有Agent逻辑；新增轻量反射提示，要求模型优先采信当前实体内容，避免历史经验过时或hallucination

### 关键实验
在7个跨领域数据集（代码库Bug修复、科学文献QA、表格Text-to-SQL等）上对比ReAct baseline、抽象记忆基准ReasoningBank、离线实体增强基准EnrichIndex：ExpIdx将答案质量最高提升11.0个点，线上推理成本最高降低50.5%；索引成本比离线增强方案低115倍，存储开销低73倍；跨任务场景下Text-to-SQL生成的经验可直接复用给事实QA，无精度损失；强弱模型迁移场景下，小模型用大模型生成的经验库效果接近大模型，成本降90%以上。

### 核心结论
针对共享实体库的任务，复用锚定实体的历史推理经验，相比通用记忆或离线预增强方案，在效果和成本上都有数量级优势。

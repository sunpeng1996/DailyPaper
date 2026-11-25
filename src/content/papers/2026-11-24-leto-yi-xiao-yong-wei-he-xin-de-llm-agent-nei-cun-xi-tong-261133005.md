---
title: 'Leto: Utility-Centric Agent Memory'
title_zh: Leto：以效用为核心的LLM Agent 内存系统
authors:
- Shuguang Chen
- Salman Paracha
affiliations:
- DigitalOcean
arxiv_id: '2611.33005'
url: https://arxiv.org/abs/2611.33005
pdf_url: https://arxiv.org/pdf/2611.33005
published: '2026-11-24'
collected: '2026-11-25'
category: Agent
direction: Agent 内存管理优化
tags:
- LLM Agent
- Memory System
- Utility Optimization
- Personalization
- Long-Horizon Task
one_liner: 放弃传统内存保真度评估，以未来任务效用为目标设计Agent内存管理框架
practical_value: '- 做电商个性化Agent时，可复用「内存索引+预生成用户静态偏好Profile」的设计，无需等到用户请求再做相似性检索，避免遗漏用户未显式提及的长期偏好（如饮食禁忌、无障碍需求等）。

  - 内存召回排序可放弃传统相似度指标，改用基于历史反馈的效用评分，有效提升长链路任务（如多轮导购、跨场景用户服务）的完成率，效用阈值可灵活适配context token预算。

  - 做用户长周期行为建模时，可复用「保真度不直接对应业务效果」的结论，不要为节省存储丢失低频次高价值的用户行为细节，可采用原子事实关联原始会话的存储结构平衡成本与召回准确率。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent内存系统以保真度为核心，仅衡量对历史会话的还原度，存在两大缺陷：1）存储阶段仅保留符合历史覆盖度的内容，丢弃后续可能有用的细节；2）召回阶段仅按与当前请求的相似度排序，容易遗漏请求未显式提及但对响应至关重要的信息，保真度高的内存并不能直接提升任务效果。

### 方法关键点
- 内存索引：存储全量会话，将会话拆分为自包含的原子事实作为索引键，关联事实对应的原始会话片段，避免提前汇总丢失细节，新旧事实自动标注更新不删除旧记录
- 内存预回放：两次会话间隙自动更新用户静态Profile和长链路任务状态，请求到来时直接作为前置上下文注入，无需等待检索匹配
- 效用闭环：每条内存初始化效用评分，每次调用后根据业务结果（用户确认/修正、任务完成状态等）更新评分，召回时仅返回评分高于阈值的内存，超token预算时按评分降序选择

### 关键实验
在3类场景5个基准数据集上和Mem0、LangMem、Hindsight等6个主流内存系统对比：1）个性化场景，PrefEval准确率比最优基线高16.3个百分点，PERMA多域任务完成率高7.64个百分点；2）长链路任务场景，MemoryArena平均进度得分最高，增益随任务链深度提升，搜索场景8轮任务后增益达14.4个百分点；3）长上下文理解场景，准确率和全量RAG相当，召回token数仅为RAG的1/8~1/1.7。

### 核心结论
Agent内存的价值不在于对历史的还原度，而在于对未来响应的提升效用。

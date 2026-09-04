---
title: 'Transfiver: Human-AI Co-Inference through a Shared Editable State'
title_zh: Transfiver：基于共享可编辑状态的人机协同推理架构
authors:
- Minji Park
- Seunghyun Yoon
- Hyuk Lim
affiliations:
- Korea Institute of Energy Technology (KENTECH)
arxiv_id: '2609.03797'
url: https://arxiv.org/abs/2609.03797
pdf_url: https://arxiv.org/pdf/2609.03797
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: Agent 人机协同共享可编辑状态设计
tags:
- Human-AI Collaboration
- Persistent Agent State
- Editable Memory
- Interactive Inference
one_liner: 提出基于唯一共享可编辑状态的人机协同推理架构，支持用户显式编辑与模型隐式更新无冲突
practical_value: '- 电商个性化导购Agent可复用单状态设计：将用户长期偏好、历史交互、定制化规则统一存入可编辑共享状态，避免RAG召回上下文冲突、参数编辑成本高的问题

  - 推荐系统可借鉴双状态更新机制：模型隐式流更新自动沉淀用户最新行为偏好，用户显式定向编辑可直接修正错误偏好标签，无需重新训练模型

  - Agent记忆审计方法可直接复用：通过history sufficiency校验、编辑目标准确率、无关内容locality三个指标验证记忆修改的有效性，避免隐式记忆路径导致的修改失效'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前长周期人机交互中，Agent/LLM的推理依赖的状态多隐式存储在模型参数、KV cache或独立RAG检索库中，用户无法直接查看、编辑，修正信息常作为新上下文加入窗口，后续推理仍可能调用旧状态，导致交互一致性差、用户修正成本高。
### 方法关键点
- 核心设计单持久化共享状态$S_t$，作为人机交互的唯一可信信息源，模型推理、状态更新完全基于该状态，无其他隐式交互记忆路径
- 双更新机制：模型隐式流更新自动识别新交互信息，决定是更新已有状态条目还是新增条目；用户显式定向编辑直接修改指定状态条目，修改立即生效且无需重训模型参数
- 严格约束history sufficiency：相同状态+相同输入必须产生相同输出分布，所有交互相关信息必须序列化到$S_t$中，禁止缓存、隐藏会话窗口等外部持久化存储
### 关键实验
基于44条多会话人机交互真实记录测试，对比prompt删除（普通RAG常用的上下文过滤方案）与状态撤回两种方案：prompt删除后下一轮旧条目复现率达31/44，Mistral-7B的准确率从0.659降至0.432；状态撤回后旧条目复现率为0，下一轮准确率维持0.659，且支持撤回后恢复、历史值查询，所有状态保存重载后完全一致。合成测试中，上下文携带的状态方案实现100%的上下文感知准确率，无recency崩溃问题。
### 核心结论
人机协同系统的用户可见可编辑状态，必须与模型实际用于推理的状态完全一致，这是长周期交互可靠性的核心前提。

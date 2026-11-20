---
title: 'STARK: Moving towards Personalized Agents That Truly Learn and Remember'
title_zh: STARK：具备长时记忆与跨用户迁移能力的个性化Agent双图架构
authors:
- Aryan Jain
- Abhishek Jha
- Anish Nediyanchath
- Promod Yenigalla
affiliations:
- Amazon RBS Tech Sciences
arxiv_id: '2611.25705'
url: https://arxiv.org/abs/2611.25705
pdf_url: https://arxiv.org/pdf/2611.25705
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 长时记忆与冷启动跨用户迁移
tags:
- Agent-Memory
- Dual-Graph-Architecture
- Cold-Start
- Knowledge-Transfer
- Graph-RAG
one_liner: 提出分离事件与行为洞察的双图Agent记忆架构，支持冷启动跨用户迁移，落地提效显著
practical_value: '- 搭建电商导购、客服类个性化Agent记忆模块时，可直接复用双图拆分思路：将原始交互事件（Episodic Graph）与提炼的用户偏好/行为洞察（Insight
  Graph）分开存储，用事件ID做边关联，既避免每次查询重算偏好，又能追溯洞察来源，降低LLM重复推理成本。

  - 用户偏好可配套证据向量（支持事件数、历史成功率、一致性权重）做排序，过滤低置信度偏好，可直接迁移到电商个性化推荐的偏好召回、排序模块，提升推荐匹配度。

  - 同领域新用户冷启动场景，可借鉴TransR关系嵌入+偏好指纹匹配的迁移方案，不用跨用户共享原始交互数据，符合隐私合规要求，能快速为新用户生成基础偏好画像。

  - 工程落地可参考其分阶段上线流程：先离线回放验证→shadow模式压测→小流量A/B→全量发布，同时固定检索token预算，保证长周期交互下延迟稳定。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Agent长时记忆方案多采用扁平单图结构，仅记录「发生了什么」，用户行为偏好散落在事件节点中，每次查询需LLM重新推导，效率低且一致性差；同时单用户记忆完全隔离，无法利用同领域其他用户的行为规律解决冷启动问题，长周期交互、同领域多用户场景下效果受限。

### 方法关键点
- 双图记忆架构：1）Episodic Graph存储用户交互事件、时间/因果/语义关联，记录事实层面交互历史；2）Insight Graph存储LLM提炼的用户行为信号（偏好、约束、目标等），每个信号附带证据向量（支持事件数、历史成功率、强度、置信度），用事件ID作为两类图的关联边，实现洞察可追溯。
- 跨用户迁移机制：将Insight Graph的节点与关系投影到TransR关系嵌入空间，用仅包含共享信号的偏好指纹计算用户相似度，结合链接预测为冷启动用户推断缺失的行为信号，全程不跨用户共享原始交互数据。
- 检索逻辑：根据查询意图动态分配事件/洞察的context配额，优先返回高置信度行为信号，搭配关联事件做证据支撑。

### 关键结果数字
在LoCoMo、LongMemEval等5个公开benchmark上对比Mem0、MAGMA等主流记忆方案，LongMemEval信息提取任务判分比SOTA高1.48，LoCoMo开放域问答高0.93；5%图稀疏度的冷启动场景下，LongLaMP开放域判分提升0.7，ROUGE-L提升3个点；亚马逊生产环境8周A/B测试，谈判轮次降低18%，周期缩短15%，新用户收益更显著。

**最值得记住的一句话**：把记忆中的「事实记录」和「规律洞察」分层存储，是同时提升长时记忆检索效率、实现跨用户知识迁移的核心。

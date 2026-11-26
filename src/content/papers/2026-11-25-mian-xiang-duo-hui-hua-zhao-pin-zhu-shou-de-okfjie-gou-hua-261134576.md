---
title: 'Procedure Inference as Memory: Learning Recruiter Decision Procedures from
  OKF-Structured Episodes in Multi-Session Hiring Assistants'
title_zh: 面向多会话招聘助手的OKF结构化片段记忆与决策流程学习
authors:
- Praveen Kumar Bodigutla
- Yizhi Zhang
- Sai Vivek Kanaparthy
- Arup De
affiliations:
- LinkedIn
arxiv_id: '2611.34576'
url: https://arxiv.org/abs/2611.34576
pdf_url: https://arxiv.org/pdf/2611.34576
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 长时记忆 · 用户偏好推理
tags:
- Agent Memory
- Episodic Memory
- Procedural Memory
- OKF
- Personalization
- RL
one_liner: 提出OKF结构化片段记忆与Procedure Memory，提升多会话Agent偏好推理效率与准确性
practical_value: '- 可复用OKF结构化事件+依赖链路（lineage）的记忆组织范式，解决纯语义/词法检索无法关联时序因果事件的缺陷，适合电商导购、客服Agent跨会话追踪用户偏好变迁，可降低60%+上下文token消耗

  - Procedure Memory的两种实现方案：无参数Prompt迭代反射、GRPO微调开放权重的决策流程学习，无需人工标注偏好标签，仅用用户行为一致性作为反馈信号，可适配不同算力预算的业务场景

  - 记忆索引导航的效率-效果trade-off参考：轻量Jev-class小模型做索引筛选可减少47% LLM调用次数，但会损失10%左右的低优先级偏好识别精度，可根据业务对延迟/精度需求灵活选择'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多会话交互类Agent（如招聘助手、电商导购）需跨会话、跨项目推断用户动态偏好与决策模式，传统全历史上下文输入token成本高、冗余信息多，纯语义/词法检索无法关联跨会话的时序因果依赖事件，难以准确捕捉偏好变迁，错误推理还会累积影响后续交互效果。

### 方法关键点
- 提出**OKF结构化片段记忆**：将用户交互事件按Open Knowledge Format存储，事件间通过lineage关联依赖关系；检索时先通过LLM或Jev-class轻量模型导航索引筛选相关事件，再沿lineage扩展关联依赖事件，最后经BM25+嵌入检索排序后按时间重放。
- 提出**Procedure Memory**：从历史交互中学习可复用的用户决策流程，两种实现：1）Prompt反射：无参数迭代优化流程，以决策与用户行为一致性为评分指标筛选最优流程；2）RL微调：用GRPO算法微调Qwen3.8-27B生成决策流程，决策一致性为奖励信号。

### 关键结果
在模拟招聘交互数据集（30个招聘者、各5个项目，覆盖低/中/高项目重叠度）+外部PersonaMem-v2基准上：
1. OKF检索较全历史上下文减少69%上下文token，中/高重叠场景低优先级偏好F1达0.93-0.95；
2. Procedure Memory较无记忆最高减少39%会话轮次，RL版本在长时推理任务上正确弃权、精确字段识别均达60%；
3. PersonaMem-v2上Procedure Memory准确率达50.2%，较全历史高1.6个百分点，上下文token减少90.5%。

### 核心结论
跨会话Agent记忆系统需同时解决「筛选时序关联的正确证据」和「解释证据背后的决策模式」两个问题，纯语义检索范式存在天然缺陷。

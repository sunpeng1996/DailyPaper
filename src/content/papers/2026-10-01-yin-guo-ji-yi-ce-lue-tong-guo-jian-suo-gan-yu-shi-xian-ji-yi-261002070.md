---
title: 'Causal Memory Policy: Making Memory Utility Identifiable by Intervening on
  Retrieval'
title_zh: 因果记忆策略：通过检索干预实现记忆效用可识别
authors:
- Arman Behnam
- Binghui Wang
affiliations:
- Illinois Institute of Technology
arxiv_id: '2610.02070'
url: https://arxiv.org/abs/2610.02070
pdf_url: https://arxiv.org/pdf/2610.02070
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent 长期记忆效用评估优化
tags:
- Causal Inference
- Memory Augmented LLM
- Agent Memory
- Propensity Weighting
- Retrieval Intervention
one_liner: 提出因果记忆策略CMP，解决记忆增强LLM的记忆效用不可识别问题
practical_value: '- 做电商Agent用户长期记忆管理时，可复用CMP的随机检索槽位设计，解决低召回高价值记忆（如用户小众偏好）的效用评估问题，避免误删有用记忆

  - 可迁移单侧决策规则到RAG/推荐的记忆淘汰场景：不可逆删除操作设置更严格的负向阈值，对效用不确定的记忆优先保留，降低误删损失

  - 记忆效用评估优先用query维度细粒度效用而非全局平均，尤其在用户意图分散的电商场景，全局平均会严重稀释记忆实际价值

  - 存量检索系统的记忆价值冷启动可参考IPW加权方法，基于历史检索日志无偏估计未召回候选的潜在价值，不需要全量在线实验'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
记忆增强LLM是长周期Agent、个性化RAG系统的核心组件，但现有记忆效用评估完全依赖已召回的记忆，50%+的高价值记忆从未被召回，导致效用评估失效，无法区分「无价值记忆」和「从未获得展示机会的高价值记忆」，直接导致记忆淘汰策略接近随机，误删大量有用记忆。

### 方法关键点
- 构建记忆增强LLM的结构因果模型，明确检索是记忆影响输出的唯一中介变量，检索侧正性违反（记忆从未被召回）是效用不可识别的核心原因
- 设计随机检索曝光机制：固定预留k个上下文槽位，按已知倾向得分采样记忆填充，从构造上保证所有待评估记忆都有被召回的机会，解决正性违反问题
- 采用自归一化逆倾向加权估计记忆的条件效用，推导不可逆记忆删除操作的贝叶斯最优单侧决策规则，只有效用显著为负的记忆才会被删除

### 关键实验
在LongMemEval、LoCoMo两个长周期记忆基准，以及Mem0落地记忆系统上测试：现有系统54%（LongMemEval）~67%（LoCoMo）的必要记忆存在正性违反，完全无法被现有方法识别；CMP将必要/非必要记忆的区分AUC从0.54（接近随机）提升到0.66，query级细粒度效用评估AUC可达0.78；误删必要记忆的比例从10.9%降到5.2%，接近减半。

### 核心结论
记忆效用本质是检索介导的因果效应，仅靠存储侧干预无法识别从未被召回的记忆价值，必须在检索层引入可控随机化。

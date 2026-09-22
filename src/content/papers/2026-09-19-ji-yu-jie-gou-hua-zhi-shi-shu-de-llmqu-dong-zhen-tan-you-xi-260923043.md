---
title: Enforcing Narrative Reliability and Epistemic Pacing in LLM-Driven Detective
  Games via Structured Knowledge Trees
title_zh: 基于结构化知识树的LLM驱动侦探游戏叙事可靠性与节奏控制
authors:
- Parsa Rahmati
- Richard Zhao
affiliations:
- University of Calgary
arxiv_id: '2609.23043'
url: https://arxiv.org/abs/2609.23043
pdf_url: https://arxiv.org/pdf/2609.23043
published: '2026-09-19'
collected: '2026-09-22'
category: MultiAgent
direction: 多Agent交互叙事的边界约束与节奏管控
tags:
- Multi-Agent Pipeline
- Structured Knowledge Tree
- Hallucination Mitigation
- Epistemic Pacing
- Narrative Control
one_liner: 提出结构化知识树+三Agent pipeline，降低LLM交互叙事幻觉、杜绝核心信息提前泄露
practical_value: '- 做需严格控制信息披露的对话Agent（如电商售前咨询、会员权益解释Agent）可直接复用三Agent pipeline：检索合法信息→生成回复→校验输出，大幅减少幻觉、杜绝违规信息泄露

  - 需要按阶段引导用户的场景（如新用户任务引导、分期权益解锁活动）可复用结构化知识树（SKT）设计，给每个信息节点加解锁前置条件、互斥关系，严格控制信息透出顺序，避免用户跳步

  - 对话类场景的幻觉评估可参考本文的定义，排除不影响核心逻辑的良性即兴内容，仅统计破坏业务规则的关键幻觉，大幅降低评估成本

  - 需防用户诱导套取敏感信息的场景（如未公开的活动规则、商品折扣），可借鉴SKT的外部状态校验逻辑，不依赖LLM自身安全约束，用结构化状态作为最终把关关卡'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM开放对话的非确定性输出难以保障预设叙事的事实一致性与信息披露顺序，在侦探游戏等需严格管控信息透出节奏的场景，提前泄露线索、虚构细节会直接破坏用户逻辑体验；现有RAG类方案均以最大化透出正确信息为目标，无法满足刻意隐藏信息、按阶段逐步披露的特殊需求。

### 方法关键点
- 设计结构化知识树（SKT）作为全局唯一事实源，每个线索节点配置ID、事实内容、披露状态、前置解锁条件、互斥矛盾节点、子节点等元数据，仅满足前置条件的节点允许被透出
- 三Agent串行执行pipeline：分析Agent接收用户query，匹配当前可披露的最相关SKT节点，无匹配返回null；对话Agent基于匹配节点生成自然回复，不得透出额外信息；检测Agent校验回复是否仅包含允许披露的内容，验证通过才更新SKT披露状态
- 所有Agent均调用Llama3.1-70B-instruct零样本推理，无额外微调

### 关键结果
基于自研侦探游戏测试床开展33人组内对照实验，对比基线为单LLM加载全量系统提示的开放对话方案：
- 关键幻觉率从17.80%降至6.27%，相对下降64.78%，完全消除系统级崩服类输出
- 基线组30.3%的用户可提前套取最终核心信息，SKT组0用户提前获取核心内容，100%实现叙事节奏管控
- 72.7%的用户可在SKT体系下完成至少1次逻辑矛盾推理，主观进度感知评分显著优于基线

### 核心结论
对于需严格边界约束的对话Agent，不要依赖LLM自身的prompt约束能力，采用外部结构化状态+职能分离的Agent pipeline，可在极低微调成本下实现高可靠性的信息管控

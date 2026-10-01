---
title: 'Cogentic: Multi-Agent Orchestration for Automated Proof Discovery'
title_zh: Cogentic：面向自动证明发现的多智能体编排框架
authors:
- Yang Cai
- Vineet Gupta
- Yanchen Jiang
- Christopher Liaw
- Aranyak Mehta
- Grigoris Velegkas
- Di Wang
affiliations:
- Google Research
- Yale University
- Google DeepMind
arxiv_id: '2609.40324'
url: https://arxiv.org/abs/2609.40324
pdf_url: https://arxiv.org/pdf/2609.40324
published: '2026-09-30'
collected: '2026-10-01'
category: MultiAgent
direction: 多智能体协作 · 复杂推理任务编排
tags:
- MultiAgent
- Orchestration
- LLMReasoning
- AutomatedProof
- AdversarialVerification
one_liner: 提出多智能体编排框架Cogentic，仅输入问题即可自主解决5个理论CS开放研究问题
practical_value: '- 多智能体分工架构可直接复用在广告/推荐机制迭代的理论推导场景：比如电商拍卖机制优化、动态定价规则推导，按「编排器分配方向+多worker并行探路+对抗校验+可信结果沉淀」的流程设计，减少算法工程师重复试错成本

  - 跨轮次可信结果沉淀机制可迁移到长链路Agent任务：比如复杂用户需求的Query解析、多步骤的营销活动规则生成，把校验通过的中间结果存入持久化ledger，避免重复推理，降低LLM调用成本

  - 对抗验证的双校验逻辑可提升Agent输出准确率：比如推荐场景的文案生成、广告投放规则校验，设置独立校验+交叉校验两步，默认假设输出有问题直到验证通过，大幅降低错误规则上线概率'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
单轮LLM生成无法处理需要多方向探索、克服技术障碍、长期沉淀中间结果的开放复杂推理问题，现有自动证明方案要么依赖形式化验证工具、要么需要可机器计算的评分函数，无法覆盖多数无明确量化校验规则的开放研究问题。

### 方法关键点
- 采用迭代证明-校验循环架构，核心组件包括全局调度的编排器、独立并行的证明器、多视角对抗校验的验证器、文献检索组件、记录失败尝试的历史库、沉淀可信中间结果的验证账本、跨轮次优化流程的顾问组件
- 每轮由编排器给证明器分配不同证明方向，仅传递裁剪后的定向简报而非全量历史，降低上下文开销
- 采用双对抗校验逻辑：单证明稿独立校验+同轮所有稿件交叉校验，只有同时通过才进入可信账本；每轮结束后从被拒证明中提取单独验证通过的中间引理，存入账本供后续轮次复用
- 跨轮次由流程顾问分析错误模式，调整后续轮次的证明器/验证器指令，避免重复踩坑

### 关键结果
以Gemini为基座模型，仅输入问题无人工干预，解决了在线学习、拍卖理论、机制设计领域的5个开放研究问题，每个结果均通过领域专家验证；单问题仅需O(100)~O(1000)次Gemini调用，推理成本远低于同类大算力Agent系统。

最值得记住的一句话：复杂开放推理任务的核心突破点不是单模型能力的提升，而是通过合理的多智能体分工、过程校验、知识沉淀机制，把现有大模型的单点推理能力聚合成远超单轮生成的长期探索能力。

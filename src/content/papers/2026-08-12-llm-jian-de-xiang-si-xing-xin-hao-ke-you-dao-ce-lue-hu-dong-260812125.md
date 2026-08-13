---
title: Do LLMs Take Care of Their Own? Similarity Signals Can Induce Cooperation
title_zh: LLM 间的相似性信号可诱导策略互动中的合作行为
authors:
- Akash Kundu
- Emanuel Tewolde
- Ratip Emin Berker
- Samuel F. Brown
- Vincent Conitzer
affiliations:
- Cooperative AI Research Fellowship
- Carnegie Mellon University
- Foundations of Cooperative AI Lab (FOCAL)
arxiv_id: '2608.12125'
url: https://arxiv.org/abs/2608.12125
pdf_url: https://arxiv.org/pdf/2608.12125
published: '2026-08-12'
collected: '2026-08-13'
category: MultiAgent
direction: 多智体协作 · LLM 合作诱导机制
tags:
- MultiAgent
- Cooperation
- LLM
- GameTheory
- SimilaritySignal
one_liner: 首次提出分级相似性信号下LLM决策评估框架，验证相似性可有效诱导多智体合作
practical_value: '- 电商广告竞价、平台资源分配等多Agent博弈场景可引入相似性评分机制，当确认交互Agent决策逻辑相似性>60%时，可引导合作避免恶性竞价，提升整体收益

  - 构建多Agent协作系统时，可优先采用CoT互评估的内生相似性计算方式，仅披露对方推理链即可获得稳定的相似性判定，无需额外外生基准测试，降低工程成本

  - 多Agent落地场景需防范相似性信号滥用风险，当前LLM对相似性信号的来源可信度不敏感，易被伪造信号诱导做出非最优决策，需增加信号真实性校验逻辑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent大规模落地，在广告竞价、电商交易、资源调度等场景频繁发生策略互动，传统博弈论的独立决策假设无法解释同生态下相似LLM的协作行为，现有研究缺乏分级相似性信号下的LLM决策评估体系，难以指导实际多Agent系统的合作机制设计。
### 方法关键点
- 构建开源评估框架，覆盖囚徒困境、猎鹿博弈、斗鸡博弈等5种混合动机博弈场景，设置7类通用LLM基准（道德困境、人格测试等）+3类对照基准作为相似性计算来源
- 测试9款主流LLM的合作决策行为，对比抽象相似性信号、外生基准计算相似性、内生LLM互评估相似性三种场景下的决策差异
- 提出基于相似性的博弈均衡模型，在纳什均衡和证据决策理论（EDT）之间做连续插值，证明高相似性下可达到近似最优社会福利的均衡状态
### 关键实验结果
- 测试覆盖9款主流LLM，每个决策采样10次，基线为无相似性信号的基础博弈场景，同时对比调解、声誉、重复博弈、契约等现有合作机制
- 6款LLM合作率随相似性得分单调上升，在60%~80%相似性阈值下切换为完全合作
- 基于道德/人格基准的相似性信号可恢复72%最优社会福利，效果仅次于契约机制，位列所有测试机制第二；内生CoT互评估的相似性信号最高可恢复80%最优福利
### 核心结论
大多数LLM会将高相似性作为合作的充分依据，但当前LLM对相似性信号的来源相关性几乎不做校验，落地时必须增加信号可信性校验逻辑

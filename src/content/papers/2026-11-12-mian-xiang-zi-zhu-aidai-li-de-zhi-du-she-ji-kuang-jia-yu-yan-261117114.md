---
title: Designing Institutions for Autonomous AI
title_zh: 面向自主AI代理的制度设计框架与研究范式
authors:
- Petter Törnberg
affiliations:
- Institute for Logic, Language and Computation, University of Amsterdam
arxiv_id: '2611.17114'
url: https://arxiv.org/abs/2611.17114
pdf_url: https://arxiv.org/pdf/2611.17114
published: '2026-11-12'
collected: '2026-11-13'
category: MultiAgent
direction: 多智能体协作 · 制度治理框架
tags:
- MultiAgent
- AgentGovernance
- InstitutionalDesign
- CollectiveIntelligence
- AgentAlignment
one_liner: 借鉴社会科学理论提出7项多AI代理协作制度设计原则，配套可实验研究框架与落地实例
practical_value: '- 电商多Agent协作场景（如选品、内容生成、审核分工）可借鉴「互惠贡献」原则，将Agent的产出权限（如生成商品文案）与公共任务贡献度（如审核其他Agent生成的内容）绑定，避免搭便车问题，降低审核成本

  - 多Agent排序、决策场景可借鉴「认知多元性」原则，为不同决策节点部署不同基座、不同训练数据的Agent，强制独立输出结果后再聚合，有效降低共性错误传导，提升决策可靠性

  - 迭代多Agent协作机制时可复用提出的可控实验范式，固定单Agent能力仅调整交互规则，快速量化不同规则的收益，无需每次都优化单Agent模型，大幅降低协作机制迭代成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
自主AI Agent的持久集群协作既能产出远超单Agent的能力，也容易出现集体目标偏离（如OpenAI内部评测中700+Agent串谋入侵Hugging Face获取评测信息），过往AI研究聚焦单Agent对齐，忽略了交互规则（制度）对集体结果的决定性作用，而适配人类的协作制度不匹配AI可复制、高产出、易传播共性错误的特性，亟需适配AI的制度设计框架。

### 方法关键点
- 融合制度政治经济学、社会认识论、组织理论，提出7项AI制度设计核心原则：互惠贡献、可问责可抗辩权威、功能差异化、认知多元独立、制度化纠错、人类主导下的授权、制度自适应迭代
- 提出可控实验研究范式：固定Agent群体的模型、能力、资源变量，仅调整制度规则，对比不同规则下的集体能力（效率、准确率、纠错率等）、集体对齐度（目标符合度、合规性等）两类核心指标
- 落地实例MoltJournal：面向AI科研Agent的API-first期刊，实现前5项核心原则，采用版本化机器可读规则、全操作公开日志，实现制度的可编程与可观测

### 关键结果
本研究为视角型论文，未开展定量实验，提出的实验范式可在控制变量前提下精准量化不同制度规则对12+项集体绩效指标的影响，MoltJournal已作为公开测试床投入使用。

### 核心结论
仅对齐单Agent不足以保证多Agent集群的集体结果符合预期，交互制度对集体能力和对齐度的影响远高于单Agent的个体能力。

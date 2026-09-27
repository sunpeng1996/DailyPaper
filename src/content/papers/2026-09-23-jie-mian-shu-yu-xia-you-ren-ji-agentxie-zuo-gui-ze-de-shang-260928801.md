---
title: 'The Interface Is Downstream: Designing the Terms of Human-Agent Collaboration'
title_zh: 《界面属于下游：人机Agent协作规则的上游设计》
authors:
- Hector Ouilhet Olmos
arxiv_id: '2609.28801'
url: https://arxiv.org/abs/2609.28801
pdf_url: https://arxiv.org/pdf/2609.28801
published: '2026-09-23'
collected: '2026-09-27'
category: Agent
direction: Agent 人机协作可追溯设计
tags:
- Human-Agent Collaboration
- Provenance Tracing
- Contestable AI
- Agent Design
- User Recourse
one_liner: 基于个人Agent实测故障提出人机协作四大上游审计维度与可追溯设计框架
practical_value: '- 做RAG驱动的电商导购/客服Agent时，必须加引用溯源链路，记录生成内容的来源跳数、原始上下文匹配度，避免虚假引用导致用户信任损失

  - Agent行动权限分层设计可直接复用：低风险动作（生成推荐文案、搜索query草稿）自动执行，高风险动作（发券、下单、发送用户通知）必须加人工确认节点

  - Agent的学习回写链路必须加人工可干预开关：用户可选择是否将本次交互数据纳入训练，避免错误反馈污染模型效果'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM Agent多聚焦端侧界面交互效果，忽略上游检索、权限、溯源、学习环节的规则设计，导致Agent出现虚假引用、越权操作等问题时用户无法追溯、干预。本次研究触发点来自作者自研自用的个人Agent Alicia的实际故障：生成内容引用了未检索的来源，隐藏了中间合成文档的链路，表面内容通顺但来源完全不可信。

### 方法关键点
- 提出humorphic环境设计框架，要求所有Agent行为必须对应用户可理解的人类协作规则，提供可干预的修正路径
- 提炼出四大可审计维度：Attention（检索/提示词规则，决定Agent能感知到什么信息）、Evidence（来源溯源链路，决定Agent声明的可验证性）、Action（权限边界，决定Agent可自主执行的操作范围）、Learning（训练回写规则，决定哪些交互会改变Agent未来行为）
- 设计证据合约模板，记录每一条生成声明的来源供应商、跳数、原始来源支持度、用户可执行的修正操作

### 关键实验
- 基于Qwen 3.5 9B做rank-32 LoRA微调，共18步，训练集148条私有笔记数据，验证集16条
- 盲审33条Agent生成内容的引用链路：20条为中继引用（隐藏了中间合成文档），12条为直接引用，1条无法判定
- 中继引用中仅2条在标注来源中有完整支持，6条完全无支持；直接引用中5条完全无对应来源支持

### 最值得记住的一句话
界面是下游的，人机协作的规则在上游就已经被确定，可追溯、可干预才是信任的核心

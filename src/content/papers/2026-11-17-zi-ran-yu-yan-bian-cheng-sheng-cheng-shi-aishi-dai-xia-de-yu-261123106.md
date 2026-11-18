---
title: 'Natural Language Programming: Rethinking Language, Memory, and Cognition in
  the Era of Generative AI'
title_zh: 自然语言编程：生成式AI时代下的语言、记忆与认知重构
authors:
- Giovanni Adorni
- Daniele Grosso
affiliations:
- University of Genoa, Italy
arxiv_id: '2611.23106'
url: https://arxiv.org/abs/2611.23106
pdf_url: https://arxiv.org/pdf/2611.23106
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: LLM认知架构 · 自然语言编程
tags:
- Natural Language Programming
- Dialogic Working Memory
- LLM
- Distributed Cognition
- Prompt Engineering
one_liner: 提出自然语言编程NLPg范式与对话工作记忆框架，重构生成式AI下自然语言的认知媒介定位
practical_value: '- 对话式Agent记忆架构可复用BTMA+SKGE+RMR三层结构：分层存储用户交互时序轨迹、商品/用户语义关系、一致性校验规则，解决电商客服、会话推荐类Agent的长上下文语义漂移问题

  - 优化Prompt工程定位：不要仅将prompt作为查询指令，要嵌入任务约束、验证规则、中间推理状态，提升生成式推荐、营销文案生成的输出可控性，降低幻觉率

  - 长流程LLM工作流可落地推理轨迹留存机制：基于对话工作记忆框架留存全链路交互与推理路径，支持推荐理由、广告文案的合规校验与问题回溯，满足业务监管要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统NLP范式将自然语言仅视为待分析、生成的计算处理对象，无法适配LLM时代下自然语言同时承担人机交互、认知编排、记忆载体的复合功能，长会话交互中的语义漂移、上下文断裂、推理不可追溯等问题长期缺乏统一的认知框架解释。

### 方法关键点
- 定义**NLPg（Natural Language Programming）**范式，将prompt定义为动态可执行认知 artefact，同时承担任务可执行规范、认知脚手架、对话记忆结构、元认知调控工具4种核心功能，替代传统NLP的纯语言处理定位
- 推出**Dialogic Working Memory**框架，将LLM会话状态视为分布式外部工作记忆，通过会话交互动态完成上下文重构、推理轨迹留存、认知状态稳定，适配混合人机协同工作流
- 完成三类现有记忆架构到NLPg框架的映射：BTMA层存储交互时序轨迹对应情景记忆，SKGE层存储实体语义关系对应语义记忆，RMR层做一致性校验对应执行控制，三层融合组装成可执行的会话状态输入LLM

### 关键实验
该研究为纯理论框架研究，暂无定量对比实验，核心结论基于分布式认知、工作记忆等已验证的认知科学理论推导，配套的BTMA、RMR等记忆架构的实验验证将在后续工作中发布。

### 核心结论
生成式AI时代，自然语言不再只是被处理的信息载体，而是同时承担通信介质、可执行规范、认知支架、分布式记忆架构的混合认知基础设施。

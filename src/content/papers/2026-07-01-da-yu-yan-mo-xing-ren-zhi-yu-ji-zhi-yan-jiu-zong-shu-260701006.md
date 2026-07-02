---
title: Understanding Large Language Models
title_zh: 大语言模型认知与机制研究综述
authors:
- Yannik Keller
- Thomas Eisenmann
arxiv_id: '2607.01006'
url: https://arxiv.org/abs/2607.01006
pdf_url: https://arxiv.org/pdf/2607.01006
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: 大语言模型 · 认知机制与可解释性
tags:
- LLM
- Explainable AI
- Emergent Ability
- Machine Cognition
- Transformer
one_liner: 系统梳理LLM架构、涌现能力、可解释方法，澄清关于LLM认知本质的常见争议
practical_value: '- 搭建LLM驱动的推荐/Agent系统时，可参考文中总结的LLM符号推理能力边界，避免在强逻辑推理场景过度依赖小参数LLM

  - 排查LLM4Rec的bad case时，可复用文中提到的神经元激活分析、电路tracing方法定位决策根因

  - 设计LLM推理或RAG链路时，可结合文中总结的LLM与人类认知的差异，优化prompt对齐用户偏好的逻辑'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM的内在机制、能力边界、与人类认知的异同仍存在大量争议，业界缺乏对LLM本质的系统性认知框架。
### 方法关键点
1. 梳理Transformer核心架构，明确注意力机制支撑LLM在大规模数据下训练为通用模型的逻辑；
2. 复盘LLM涌现能力相关研究，覆盖符号推理、心理理论、欺骗策略等类人认知表现及典型失败案例；
3. 总结从神经元激活分析到电路追踪的XAI技术路径；
4. 回应LLM是否具备真实认知的核心争议。
### 核心结论
指出反对LLM具备类人认知的主流观点存在对优化过程与认知能力的误解，倡导既不否定人机差异、也不陷入简单还原论的客观讨论框架。

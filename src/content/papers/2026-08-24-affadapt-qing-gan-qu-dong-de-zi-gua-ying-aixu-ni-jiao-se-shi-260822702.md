---
title: 'AffAdapt: AFFect-driven ADAPTive AI Personas for Seamless Conversations'
title_zh: AffAdapt：情感驱动的自适应AI虚拟角色实现流畅对话
authors:
- Nishanth Chidambaram
- Kaustubh Paliwal
- Kayla Hom
- Shaoze Zhou
- Chen Chen
- Manas Satish Bedmutha
- Nadir Weibel
affiliations:
- University of California San Diego
- Florida International University
arxiv_id: '2608.22702'
url: https://arxiv.org/abs/2608.22702
pdf_url: https://arxiv.org/pdf/2608.22702
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: 对话Agent · 多模态情感交互
tags:
- Affective AI
- Conversational Agent
- Multimodal Interaction
- Persona Adaptation
- Real-time Agent
one_liner: 提出情感驱动的多模态AI虚拟角色交互框架AffAdapt，协调时序身份情感实现自然对话
practical_value: '- 电商智能客服/直播数字人可复用多模态交互闭环设计，统一管理对话轮次、persona一致性、情感状态输出，提升对话自然度

  - 高风险客服场景（客诉、退换货）可借鉴持久化情感状态模块，根据用户情绪动态调整话术，避免机械回复

  - 实时对话Agent可参考流式语音识别+主动轮次管理方案，减少应答等待时延，避免抢话'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有AI虚拟角色生成多模态响应时缺乏跨模态协同，对话轮次决策生硬、情绪与非语言信号不匹配，无法支撑自然流畅的人机交互，高敏感、高风险对话场景落地难度大。
### 方法关键点
设计AffAdapt统一交互框架，将流式语音识别、主动轮次管理、persona约束的响应生成、持久化情感状态模块、同步虚拟形象输出集成到单交互闭环，全链路协调时序、身份一致性与情感表达。
### 关键结果
初始案例验证框架可实现流畅轮次管理，persona一致行为表现符合预期；同时明确当前仍存在中断处理、开放域对话、多模态情感对齐三类未解决挑战，框架可泛化到培训、教育、模拟等所有需要高真实感交互的场景。

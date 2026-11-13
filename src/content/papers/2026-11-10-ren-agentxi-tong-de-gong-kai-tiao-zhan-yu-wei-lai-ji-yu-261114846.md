---
title: Open Challenges and Opportunities in Human-Agent Systems
title_zh: 人-Agent系统的公开挑战与未来机遇
authors:
- Reuth Mirsky
- Sarath Sreedharan
- Nitay Alon
- Stefan Sarkadi
- Munindar P. Singh
- Liz Sonenberg
- Peter Stone
- Silvia Tulli
- Stylianos Loukas Vasileiou
- Shlomo Zilberstein
arxiv_id: '2611.14846'
url: https://arxiv.org/abs/2611.14846
pdf_url: https://arxiv.org/pdf/2611.14846
published: '2026-11-10'
collected: '2026-11-13'
category: Agent
direction: 人-Agent交互 系统设计与优化
tags:
- Human-Agent Interaction
- BDI
- Theory of Mind
- Adjustable Autonomy
- Trust Calibration
one_liner: 梳理人-Agent交互五大核心挑战，结合经典多Agent研究给出落地技术路径
practical_value: '- 搭建电商场景用户智能Agent（如购物助手）时，可复用BDI架构+结构化用户心智模型的混合方案，解决LLM ToM推理不稳定的问题，避免错误理解用户购物意图

  - 做Agent权限管控时，参考可调自治权（Adjustable Autonomy）决策规则，动态判断自主执行/申请用户确认的边界，平衡用户体验与操作风险（如自动退款、改地址等高风险操作必须确认）

  - 推荐解释生成模块可结合计算论证框架，输出可溯源、可质疑的推荐理由，避免无依据的生成式解释误导用户，提升用户对推荐的信任

  - 做用户信任校准的时候，不要盲目追求用户满意度/接受率，需基于任务实际准确率输出置信度，降低用户对Agent的过度依赖风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM驱动的Agent落地时普遍存在用户意图理解不稳定、权限边界模糊、解释不可信、信任校准失衡、双向学习效率低等问题，现有LLM Agent研发多忽略经典多Agent领域数十年积累的人-Agent交互研究成果，导致大量重复造轮子与安全风险。
### 方法关键点
- 归纳五大核心挑战：用户理解（ToM推理不稳定）、权限与承诺管理（自治边界模糊）、分歧与解释传递（解释无依据、共识不合理）、战略影响与欺骗（信任被滥用、虚假承诺）、双向学习（用户与Agent无法长期协同进化）
- 对应落地技术路径：1）混合BDI架构与结构化心智模型记录用户信念/目标/意图，搭配LLM做自然语言理解与推理；2）基于可调自治权框架动态决定控制权转移逻辑，平衡自主执行效率与用户控制需求；3）采用计算论证框架构建可溯源、可质疑的解释与分歧处理流程；4）基于社会认知信任模型做信任校准，结合声誉、机制设计防控欺骗风险；5）依托协同逆强化学习等框架实现用户与Agent的双向反馈学习
### 关键内容
作为AAMAS社区联合产出的Agentic AI报告子章节，整合近40年多Agent领域的人-Agent交互研究成果，覆盖150+篇相关工作，为LLM时代的人-Agent系统设计提供完整技术路线参考
### 核心结论
LLM Agent研发不能只依赖大模型能力，需结合经典多Agent领域的形式化推理、交互协议研究，才能构建可靠、可控的人-Agent协同系统

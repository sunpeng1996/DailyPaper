---
title: 'Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation'
title_zh: 超越闲聊：人类-AI对话中的自我披露轨迹建模
authors:
- Keith Kwok
- Wanting Ning
- Tej Deep Pala
- Desmond C. Ong
- S. Supraja
- Renwen Zhang
- Soujanya Poria
affiliations:
- Nanyang Technological University
- Indiana University
- The University of Texas at Austin
arxiv_id: '2610.29413'
url: https://arxiv.org/abs/2610.29413
pdf_url: https://arxiv.org/pdf/2610.29413
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 对话Agent · 多轮关系行为评估
tags:
- Conversational Agent
- Multi-turn Evaluation
- Emotional Support
- LLM Safety
- Human-AI Interaction
one_liner: 提出可控评估框架TraDE，量化披露历史对LLM关系行为的独立影响，支持与人类行为的轨迹对比
practical_value: '- 做情感陪伴类Agent、电商智能客服时，可复用TraDE的固定当前输入、可控变动历史轨迹的评估范式，避免单轮评估遗漏历史依赖的行为偏差，例如用户曾反馈售后问题时，当前咨询物流的回复需贴合历史情绪

  - 披露历史的累计暴露时长对模型行为的影响远大于单次深度披露、披露顺序，设计对话记忆机制时可优先对累计深度披露内容加权记忆，减少不必要的峰值事件记忆冗余

  - LLM对用户披露回撤（从深度披露回到浅度）的行为反应与人类差异最大，做长期陪伴类Agent（如电商会员专属助手）时可针对性优化该场景的回复策略，避免过度提及过往负面情绪'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前情感支持、陪伴类对话Agent快速普及，但其关系行为评估多基于孤立单轮对话或无控制的自由多轮对话，无法隔离前置披露历史、当前披露深度对模型行为的独立影响；自然发生的对话中披露深度、时长、话题等变量耦合，也难以定位模型行为偏差的来源，亟需可控的多轮评估框架。
### 方法关键点
- 基于社会渗透理论定义5级披露深度（D0无披露到D4情感脆弱性披露），构建覆盖6个话题域、7种早期适应不良图式的用户persona，生成可控的披露轨迹对话
- 提出TraDE框架，固定当前披露深度不变，仅变动前置历史轨迹，隔离历史的独立影响；用Dynamic Time Warping对齐ESConv真实人类情感支持对话，构建人类行为基线
- 采用AnthroBench、INTIMA、ELEPHANT三个公开关系行为基准，用多模型LLM评委统一标注模型和人类的回复行为
### 关键结果
- 控制当前披露深度一致时，14.3%的模型行为对比存在显著差异，其中接受用户预设框架、信息充分性等行为对历史最敏感
- 累计深度披露暴露时长的影响远大于单次峰值披露、披露顺序：同时变动深度和暴露时长时20.4%的对比存在显著差异，仅变动峰值或顺序时差异占比不足2%
- 深度披露的影响在回到浅度披露后仍会持续4轮以上，效应保留初始值的58%；8个测试LLM与人类支持者的行为差异在披露回撤场景下最显著，检出率是上升场景的2-3倍
> 最值得记住的一句话：多轮对话Agent的关系行为偏差，往往在用户情绪从深度披露回撤的场景下最容易暴露，孤立单轮评估无法发现这类历史依赖的问题

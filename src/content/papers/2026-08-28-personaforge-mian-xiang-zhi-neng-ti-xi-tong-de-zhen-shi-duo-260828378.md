---
title: 'PersonaForge: Realistic Multi-Turn User Simulation for Agentic Systems'
title_zh: PersonaForge：面向智能体系统的真实多轮用户模拟框架
authors:
- Hanglong Lv
- Dawei Zhu
- Lei Li
- Bowen Ye
- Huaqiu Liu
- Yifan Song
- Bofei Gao
- Weimin Xiong
- Jinhao Dong
- Chenhong He
affiliations:
- 北京大学
- 香港大学
- 小米
- 中国人民大学
arxiv_id: '2608.28378'
url: https://arxiv.org/abs/2608.28378
pdf_url: https://arxiv.org/pdf/2608.28378
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent 多轮交互用户模拟优化
tags:
- User Simulation
- Persona Modeling
- Multi-turn Interaction
- Agent Evaluation
- LLM Agent
one_liner: 提出四维人格+SOUL控制的多轮用户模拟框架，大幅提升智能体多轮交互性能
practical_value: '- 电商导购/客服Agent训练场景，可直接复用四维人格空间+SOUL行为控制的用户模拟框架，生成符合不同用户画像的多轮交互数据，降低人工标注对话的成本，提升Agent应对模糊需求、用户纠错的能力

  - Agent业务评测环节，可借鉴Reverse Deep Construction思路，从业务真实query反推用户隐藏需求和行为模式，构建贴合实际业务场景的多轮评测基准，避免传统单轮评测与真实用户行为脱节的问题

  - 推荐系统冷启动阶段，可复用渐进式信息披露+执行耦合反馈的用户行为设计，模拟真实用户的浏览、咨询、修订需求等行为，提升推荐策略迭代的效率和真实用户匹配度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前智能体训练与评测普遍假设用户首轮query信息完整、为单轮交互，但对16K真实会话的分析显示，75.9%的交互为多轮，用户会逐步补充需求、修正中间输出、调整任务方向，现有训练数据与真实场景存在巨大gap，是制约智能体落地的核心瓶颈之一。
### 方法关键点
- 四维人格空间：覆盖职业、MBTI性格、技术熟练度、知识背景四个维度，内置一致性校验规则，保证用户特征与任务场景匹配
- SOUL驱动的行为控制：通过信息不对称设计，模拟用户仅逐步披露隐藏需求，同时约束输出短文本、单轮仅提一个问题、主动校验计算/代码结果等真实用户行为
- Reverse Deep Construction：从真实公开的用户seed query反推人格画像和关联场景记忆，保证交互数据的真实性，避免无意义的合成内容
### 关键结果
构建6.3K条高质量多轮训练数据、138个跨20+领域的人工标注评测基准PersonaForge-Bench。训练后Qwen3.5-27B复合得分提升4.1%，其中任务完成率+6.0%、响应质量+6.8%；小米MoE模型MiMo-V2-Flash复合得分提升15.7%，交互轮次减少20.7%、工具调用减少9.2%，效率显著提升。
### 核心结论
真实多轮交互训练对大模型尤其是MoE模型的交互效率和任务完成率提升幅度，远高于传统单轮完备query训练。

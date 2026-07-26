---
title: 'MedGame: Storytelling Gamification Empowered by Large Language Models for
  Medical Education'
title_zh: MedGame：大语言模型赋能的医学教育叙事游戏化框架
authors:
- Qian Wu
- Xinrong Zhou
- Zizhan Ma
- Kai Chen
- Zheyao Gao
- Xun Lin
- Hongqiu Wu
- Longfei Gou
- Yixiao Liu
- Ann Sin Nga Lau
affiliations:
- CUHK
- Southern Medical University
- Peking University
- Tencent
arxiv_id: '2607.21570'
url: https://arxiv.org/abs/2607.21570
pdf_url: https://arxiv.org/pdf/2607.21570
published: '2026-07-23'
collected: '2026-07-26'
category: LLM
direction: LLM 垂类场景游戏化交互设计
tags:
- LLM
- Gamification
- Interactive System
- Benchmark
- Multimodal Orchestration
one_liner: 提出双引擎LLM游戏化框架MedGame，配套5k病例基准，将静态临床病例转为交互式决策学习路径
practical_value: '- 双引擎（内容生成+流程调度）的交互式Agent架构可直接复用，适用于电商导购互动游戏、用户成长路径设计等场景

  - 静态标准化内容（如商品说明、活动规则）转动态交互式叙事的方法，可迁移到内容种草、活动玩法自动生成场景

  - 垂类场景下任务特定微调可大幅缩小开源LLM与商用模型差距的结论，可复用在垂类Agent的低成本优化上'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM医疗教育系统多为单轮问答或局部交互，未将完整临床病例组织为决策导向的连贯学习轨迹，无法满足病例式学习的递进式教学需求。
### 方法关键点
1. 双引擎架构：Medical Narrative Designer基于静态病例生成带状态、决策节点的临床叙事线；Story Director输出依赖感知的多模态编排方案，配套开源交互式平台实现渲染
2. 构建包含5000个临床病例的MedGame Bench基准与配套评估协议，覆盖医学叙事生成、故事调度两类任务
### 关键结果
任务特定微调可将开源LLM在MedGame Bench上的表现大幅提升，缩小与商用LLM的差距；学生试点研究显示，MedGame的用户参与度、实用度感知显著优于纯文本学习方案。

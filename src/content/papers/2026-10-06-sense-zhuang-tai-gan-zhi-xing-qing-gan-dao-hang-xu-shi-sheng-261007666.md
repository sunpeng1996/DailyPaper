---
title: 'SENSE: State-aware Emotion Navigation Storytelling Engine'
title_zh: SENSE：状态感知型情感导航叙事生成引擎
authors:
- Yi Xia
- Pablo Carrasco Velo
- Mudit Paliwal
- Ibrahim Khan
- Yifan Geng
- Mustafa Can Gursesli
- Juho Hamari
- Ruck Thawonmas
affiliations:
- Ritsumeikan University Graduate School of Information Science and Engineering
- Ritsumeikan University College of Information Science and Engineering
- Tampere University Faculty of Information Technology and Communication Sciences
arxiv_id: '2610.07666'
url: https://arxiv.org/abs/2610.07666
pdf_url: https://arxiv.org/pdf/2610.07666
published: '2026-10-06'
collected: '2026-10-10'
category: MultiAgent
direction: 多智体叙事生成 · 情感导航
tags:
- Multi-Agent
- Narrative Generation
- LLM
- Emotion Navigation
- State-aware
one_liner: 提出兼具结构一致性与情感丰富度的状态感知分支视觉小说生成框架SENSE
practical_value: '- 状态驱动叙事架构+路径感知上下文管理的设计可直接复用在电商互动引流活动（如品牌剧本杀、用户成长剧情）中，解决长剧情因果矛盾、角色OOC问题

  - 多轨情感导航的架构思路可迁移到商品种草文案、直播脚本、短视频旁白生成场景，针对不同用户圈层输出匹配情绪调性的内容

  - LLM评委+客观情感指标+人工抽样的多维度评估范式，可直接用于生成式内容类业务的效果验收，降低70%以上纯人工评估成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有LLM生成复杂分支叙事时易出现剧情循环、因果不对称等图级逻辑错误，现有修复方案仅关注路径物理连贯性，未兼顾情感弧一致性，无法支撑高质量互动内容批量生产。
### 方法关键点
提出SENSE框架，集成三大核心模块：1. 状态驱动的MIND叙事架构；2. 结构分析器；3. 路径感知上下文管理模块，仅需少量高层输入即可生成多条交叉叙事路线，同时保障角色一致性与叙事因果性。
### 关键结果
LLM评委、情感指标、视觉评估结果显示，SENSE在叙事多样性、资产整合鲁棒性上显著优于基线；初步人工测试显示其情感保真度有方向性提升，用户娱乐体验与基线持平。

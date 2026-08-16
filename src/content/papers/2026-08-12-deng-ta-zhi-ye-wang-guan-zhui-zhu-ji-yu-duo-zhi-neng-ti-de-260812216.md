---
title: '"Pharos Night: Crown Pursuit": An AI-Native Deck-Building and Tactical Arena
  Game Design Based on Multi-Agent Systems'
title_zh: 《灯塔之夜：王冠追逐》：基于多智能体的AI原生卡组竞技游戏设计
authors:
- Ting-Chen Hsu
- Jueyao Liu
- Yanzi Zhou
- Jiangxu Lin
- Haoyu Xu
- Yuwen Liu
- Yanjia Liu
- Bangjing Xu
affiliations:
- School of Animation and Digital Arts, Communication University of China
arxiv_id: '2608.12216'
url: https://arxiv.org/abs/2608.12216
pdf_url: https://arxiv.org/pdf/2608.12216
published: '2026-08-12'
collected: '2026-08-16'
category: MultiAgent
direction: 多智体系统 · AI原生游戏设计
tags:
- Multi-Agent
- LLM
- Generative AI
- Structured Output
- Game Design
one_liner: 基于多Agent与LLM设计可控生成的AI原生卡组构筑战术竞技游戏，验证高自由度玩法可行性
practical_value: '- LLM可控生成技巧可直接复用：对输出做结构化JSON解析，绑定预定义规则+数值映射，可迁移到电商自定义活动规则生成、UGC内容合规管控、用户自定义权益生成等场景

  - 多Agent交互落地方案可参考：用LLM驱动非玩家角色决策+自然语言交互，可复用在电商多角色导购Agent、直播场控Agent、客服分流Agent的交互逻辑设计

  - 上线前验证方法可借鉴：面向核心用户做小规模功能测试，同步收集体验数据与存在问题，可用于生成式推荐、Agent功能的上线前灰度评估'
score: 6
source: arxiv-cs.HC
depth: abstract
---

## 动机
生成式AI技术发展推动AI原生游戏（玩法规则直接由生成式AI驱动）探索，现有落地案例普遍存在生成内容不可控、规则与AI能力适配性差的问题，缺乏成熟的多Agent驱动玩法框架。
## 方法关键点
1. 核心能力层基于LLM实现三大功能：游戏素材/卡牌自动生成、NPC多Agent自主决策、玩家自然语言交互支持；
2. 可控生成机制：强制LLM输出结构化JSON格式，卡牌效果绑定预定义玩法规则，定性效果等级直接映射为策划预设数值，从链路规避生成结果超出边界；
3. 玩法支持玩家通过自然语言自定义卡牌效果，自主选择与NPC的协商/对战策略。
## 关键结果
13人小规模测试验证：系统可提供有策略深度、高沉浸感的AI驱动玩法，同时暴露可预测性、透明度、玩家控制度三大待优化方向。

---
title: Generating Diverse Personas for User Simulators to Test Interview Dialogue
  Systems
title_zh: 用于面试对话系统测试的用户模拟器多样化人格生成方法
authors:
- Mikio Nakano
- Kazunori Komatani
- Hironori Takeuchi
affiliations:
- C4A Research Institute, Inc.
- SANKEN, University of Osaka
- Musashi University
arxiv_id: '2608.19549'
url: https://arxiv.org/abs/2608.19549
pdf_url: https://arxiv.org/pdf/2608.19549
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent 用户模拟器多样化人格生成
tags:
- User Simulator
- Persona Generation
- LLM
- Dialogue System Testing
- Diversity
one_liner: 基于LLM自动生成带沟通风格特质的用户人格，提升对话多样性，降低面试对话系统测试人力成本
practical_value: '- 测试电商导购、售前客服等对话类Agent时，可复用该思路用LLM自动生成多样化用户人格模拟，大幅降低真人测试成本

  - 生成模拟用户时注入沟通风格标签（如健谈/沉默/挑剔/表达模糊），可覆盖更多边缘测试case，提升对话系统鲁棒性

  - 推荐系统冷启动阶段的用户模拟场景，可借鉴该人格自动生成方法快速扩充虚拟用户画像，用于AB测试前置验证'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
面试对话系统测试高度依赖真人参与，人力成本极高；传统面向任务型对话训练的用户模拟器未关注人格多样性，手动批量构造测试用用户人格耗时耗力，无法覆盖全量测试场景。
### 方法关键点
1. 基于LLM自动生成用户模拟器所需的完整人格信息，完全替代人工构造流程；
2. 人格生成阶段显式注入沟通风格相关的性格特质标签，定向提升模拟用户的对话表达多样性。
### 关键结果
实验验证该方案生成的用户模拟器输出的对话内容变异度显著高于基线方案，可覆盖更多手动构造人格无法覆盖的边缘测试场景，大幅降低测试环节人工投入。

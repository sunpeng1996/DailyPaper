---
title: 'Discovery Foundation Models: Toward Open-Ended Discovery Intelligence'
title_zh: 《发现基础模型：面向开放式探索智能》
authors:
- Ling Yang
- Zhenfei Yin
- Yingcheng Wu
affiliations:
- DFM Scientist Collaboration Program
- phai-labs
arxiv_id: '2609.15973'
url: https://arxiv.org/abs/2609.15973
pdf_url: https://arxiv.org/pdf/2609.15973
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: Agent 开放式探索智能框架
tags:
- Discovery Foundation Model
- Agent System
- Closed Loop Learning
- Skill Memory
- Scientific AI
one_liner: 提出发现基础模型DFM框架及Zetema系统，支持开放式知识发现全流程能力
practical_value: '- 可借鉴DFM的显式研究状态设计，给电商探索类Agent（新品冷启动、新客需求挖掘）加可追溯的状态流转记录，支持分支回溯、失败归因，避免无效重复探索

  - 可复用Zetema的验证门控+技能沉淀机制，推荐系统策略迭代、AB实验归因环节加验证门槛，把经过业务验证的探索策略（人群圈选、特征工程规则）沉淀为可复用Skill，跨业务场景迁移

  - GALILEO的干湿实验闭环逻辑可迁移到电商线上线下联动探索：先做线上小流量实验（干实验）筛选策略，再推全量线下投放（湿实验），根据实际转化数据反向更新策略库，提升探索效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型、科学Agent仅能在人类预定义的任务框架内做优化，无法自主调整问题边界、表征体系、评估逻辑，在开放探索场景下遇到结构性瓶颈时无法突破，亟需支撑全流程自主探索的通用模型系统。
### 方法关键点
- 定义Discovery Foundation Model（DFM）7项耦合核心能力：问题发现、可研究性具象化、表征构建、可验证假设生成、干预设计、证据驱动修订、跨任务探索能力迭代
- 提出Zetema系统架构：以显式可追溯的研究状态为核心，支持探索分支的创建、回溯、合并，引入Research World Model对高成本动作做前置风险收益预评估，加多层验证门控过滤无效探索
- 设计Discovery Skill结构化记忆机制：存储经过验证的探索策略（触发条件、操作动作、预期效果、验证要求），跨任务复用实现探索能力持续进化
- 提出干湿实验闭环范式：干实验负责模拟、方案预验证，湿实验返回真实外部证据，反向更新研究状态与技能库
### 关键实验
基于GALILEO治疗性肽发现系统做实证，经过5轮干湿循环迭代，得到两条有效肽分支：LRRC8C靶点肽IC50达18.922μM，SLC25A1靶点肽IC50达0.736μM；同时沉淀出可复用的Amphiphilic Balance Grammar设计规则，迁移到外部肽设计任务后显著提升输出的几何与能量表现。
### 核心洞见
探索智能的核心不是在预定义框架内找最优解，而是能自主识别并修订框架本身的缺陷，基于真实外部反馈持续迭代探索能力。

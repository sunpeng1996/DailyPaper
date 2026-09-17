---
title: AI for Games in the Foundation Model Era
title_zh: 大模型时代的游戏领域AI技术综述
authors:
- Meng Luo
- Yanlin Li
- Hao Li
- Hongzhan Lin
- Pengfei Zhou
- Tianjie Ju
- Ran Zhang
- Yeying Jin
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- Nanyang Technological University
arxiv_id: '2609.16679'
url: https://arxiv.org/abs/2609.16679
pdf_url: https://arxiv.org/pdf/2609.16679
published: '2026-09-14'
collected: '2026-09-17'
category: Other
direction: 大模型游戏AI · 能力迁移综述
tags:
- Foundation Model
- Game AI
- Survey
- Capability Transfer
one_liner: 系统梳理大模型时代游戏全生命周期AI应用的6类角色，明确跨角色能力迁移的挑战与落地边界
practical_value: '- 可复用「按输出用途划分技术角色」的分类框架，梳理自身业务（如推荐全链路、Agent全生命周期）的技术体系，明确各模块边界

  - 跨场景/跨模块能力迁移时保留核心可复用资产（如trajectory数据、世界模型），仅针对性适配场景专属变量（如业务规则、用户上下文），降低迁移成本

  - 可借鉴游戏AI的评估思路，区分标准化基准场景与业务专属场景的评估指标，避免泛化性结论直接落地带来的效果损失'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
大模型与游戏世界模型技术快速迭代，游戏全生命周期各环节AI应用独立发展，难以区分可跨场景迁移的通用能力与绑定特定游戏、引擎、用户群的专属能力，缺乏统一梳理框架。
### 方法关键点
将游戏领域AI按输出用途划分为6类角色：博弈执行、玩家与游戏建模、游戏设计、开发运维、runtime生成适配、测试评估；逐一分析各角色的输入结构、AI产出、可迁移资产，梳理跨角色的协同链路。
### 关键结果
- 跨角色可复用资产包括trajectory数据、预训练环境、设计规范、用户反馈等
- 控制规则、引擎接口、状态表示、玩家上下文为场景专属变量，下游应用必须在目标场景完成有效性验证
- 当前仅有限边界博弈场景的评估体系实现标准化，玩家建模、动态适配、自动化测试等方向评估体系仍不完善，核心挑战是平衡能力复用与场景适配的有效性

---
title: 'Agent-Editing World Model: Rethinking World Modeling for LLM Agents'
title_zh: Agent编辑型世界模型：重新思考LLM Agent的世界建模范式
authors:
- Shuang Sun
- Guoxin Chen
- Fanzhe Meng
- Jia Deng
- Huatong Song
- Jinhao Jiang
- Wayne Xin Zhao
- Hongteng Xu
- Ji-Rong Wen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2609.28416'
url: https://arxiv.org/abs/2609.28416
pdf_url: https://arxiv.org/pdf/2609.28416
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: LLM Agent · 世界模型优化
tags:
- LLM Agent
- World Model
- Decision Correction
- Trajectory Tuning
- Long-Horizon Task
one_liner: 提出聚焦Agent状态编辑的世界模型AEWM，解决长周期任务状态污染问题，提升跨域Agent性能
practical_value: '- 可复用Action Judge设计：在电商导购/搜索Agent中，将决策分为关键/探索/噪声三类，过滤无效搜索/推荐query，减少冗余工具调用，降低推理成本

  - 可落地EditAct推理框架：在长路径用户需求满足场景（如复杂商品咨询、多步活动推荐）中，实时修正Agent的无效推理动作，避免错误累积导致的任务失败

  - 可迁移AEWM-RFT训练范式：基于修正后的优质轨迹做拒绝采样微调，无需在线部署大模型世界模型即可让小参数Agent获得性能提升，适配业务低延迟要求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有语言世界模型多聚焦预测工具返回结果，但这类结果熵值高、强依赖执行环境，预测价值低且易引入虚假信息；同时长周期Agent任务普遍存在任务状态污染问题，即错误假设、过时计划残留在历史中，会不断放大干扰后续决策，现有方案无法有效解决该痛点。

### 方法关键点
- 提出Agent-Editing World Model（AEWM），核心建模Agent推理动作对后续任务进度的影响，而非模拟环境观测
- 内置两个核心能力：Action Judge将待执行的推理-动作对分为关键/探索/噪声三类；State Revision针对噪声类决策直接生成替换的推理-动作对
- 设计EditAct推理流程：仅保留关键/探索类动作，直接替换噪声类动作后调用真实工具执行，从根源阻断错误状态累积
- 配套两阶段训练：52B tokens域内数据预训练+120K标注数据SFT；额外提出AEWM-RFT，基于AEWM修正后的优质轨迹对Agent做拒绝采样微调，可离线迁移能力

### 关键结果
- Action Judge基准上AEWM取得70.5%的macro-F1，超过最强基线10.6个百分点
- EditAct跨6个基准、3个Agent backbone，平均得分较最强基线提升3.2~6.7个百分点，甚至9B参数Agent加EditAct性能超过35B纯ReAct Agent
- AEWM-RFT无需在线AEWM推理，较Self-RFT跨三个域提升2.2~2.6个百分点，同时平均推理步数降低最多30%

最值得记住的一句话：语言世界模型的核心价值不是模拟环境，而是直接修正Agent的错误决策状态，从根源避免长路径任务的错误累积。

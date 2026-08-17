---
title: Handover of In-Context Learning State Across Session Boundaries
title_zh: 跨会话边界的上下文学习状态移交理论与方法
authors:
- Masahiro Kato
- Taka Kato
affiliations:
- Mizuho-DL Financial Technology
- the University of Tokyo
- RIKEN AIP
- Osaka Metropolitan University
- NP-hard
arxiv_id: '2608.14528'
url: https://arxiv.org/abs/2608.14528
pdf_url: https://arxiv.org/pdf/2608.14528
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: Agent 跨会话状态迁移优化
tags:
- In-Context Learning
- Session Handover
- Agent Memory
- Prompt Compression
- Predictive Sufficiency
one_liner: 建立跨会话ICL状态移交的理论框架，提出三段式记录方案并量化预查询编码损失
practical_value: '- 电商Agent多会话导购/客服场景可复用三段式记录结构：优先精确存储已确定的用户决策、促销约束等不可修改的信息，重复的用户行为/点击数据用任务相关统计量压缩，稀有特殊案例保留原始观测，平衡内存占用与决策准确率

  - 跨会话上下文压缩无需做通用摘要，可基于预测充分性原则仅保留会影响后续推荐/回答结果的信息，无需重构完整历史会话，大幅降低上下文长度压力

  - 设计Agent记忆系统时可明确区分KV cache（仅用于加速计算）和任务状态记录（直接影响决策），避免把缓存和业务记忆混为一谈，降低工程冗余'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent/多会话应用常面临上下文超限、应用重启、跨Agent接力的场景，现有prompt压缩是感知下游查询的，而会话移交需要在不知道后续查询的前提下生成移交记录，通用摘要容易丢失关键约束或决策信息，缺乏量化的信息损失评估与标准的记录构造方法。

### 方法关键点
- 以预测充分性为移交记录核心评价标准：只要移交后输出的目标分布和使用完整上下文时一致，就认为记录有效，不需要精确还原原始会话文本
- 设计三段式移交记录：Exact段精确存储决策、约束、未决问题等不能出错的信息；Stat段用带任务误差保证的统计量替换重复的示例/工具调用结果；Residual段保留无法被统计量覆盖的原始观测
- 从统计理论层面推导记录的内存下界，量化「提前写记录不知道后续查询」带来的信息损失，给出高斯线性回归、非参数回归场景下的精确记录构造方案与误差界

### 关键结果
- 高斯回归场景下，用d(d+1)/2 + d维的充分统计量即可完全替代任意长度的示例序列，无信息损失；量化后的记录长度每增加p比特（p为统计量维度），预测分布的KL散度下降为原来的1/4
- 非参数回归场景下，当内存预算达到O(n^{d/(2β+d)} logn)时，可达到和使用全量数据一致的预测误差率，内存不足时误差下界由预算和样本量共同决定

### 核心结论
跨会话移交的核心是保留任务相关的预测信息，而不是还原原始会话文本，提前写记录的信息损失远高于感知查询的prompt压缩

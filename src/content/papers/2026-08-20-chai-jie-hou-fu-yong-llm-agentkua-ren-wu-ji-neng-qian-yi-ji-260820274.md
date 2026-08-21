---
title: 'Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents'
title_zh: 拆解后复用：LLM Agent跨任务技能迁移机制研究
authors:
- Yiyang Feng
- Biddut Sarker Bijoy
- Niranjan Balasubramanian
- Jiawei Zhou
affiliations:
- Stony Brook University
arxiv_id: '2608.20274'
url: https://arxiv.org/abs/2608.20274
pdf_url: https://arxiv.org/pdf/2608.20274
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent 跨任务技能迁移优化
tags:
- LLM Agent
- Skill Transfer
- Cross-Task
- Skill Memory
- Skill Utility
one_liner: 对比不同技能归纳粒度与存储格式的迁移效果，提出无需执行的技能效用评分
practical_value: '- 建设Agent技能库优先选择子任务粒度而非全任务粒度：全任务技能会拉低1.2~4.1pp的任务成功率，子任务技能可提升0.5~1.9pp，适合电商导购、客服自动化等多流程Agent场景

  - 技能存储优先采用文本格式而非代码格式：文本技能在子任务粒度下相对代码技能多带来1.4pp的成功率提升，无需额外适配代码执行环境，落地成本更低

  - 技能库上线前可通过技能效用评分提前诊断质量：仅通过技能文本和任务描述即可计算，无需执行任务，可快速过滤低效用技能，避免引入负向效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent的跨任务技能迁移效果不稳定，全任务级归纳的技能易绑定源任务，泛化性差甚至作为干扰上下文降低性能，技能迁移的生效条件缺乏系统性验证，不同归纳粒度、存储格式对迁移效果的影响没有统一结论，无法指导工业界技能库落地。

### 方法关键点
- 控制变量对比两个核心维度：① 技能归纳粒度（全任务级/子任务级），② 技能存储格式（文本说明/可执行代码），两类Agent仅在技能归纳粒度上有差异，其余prompt、检索逻辑完全一致。
- 提出技能效用评分：由特异性（技能与真实任务的匹配度）和抽象性（技能跨任务的泛化性）的乘积计算，仅需技能和任务描述，无需任务执行即可完成技能库诊断。

### 关键结果
实验覆盖3个长序列基准（AppWorld、OfficeBench、KramaBench）、11款开源/闭源模型，对比6种实验条件，核心结论：
- 全任务级技能平均拉低1.2pp（文本格式）、4.1pp（代码格式）的任务成功率，子任务级技能平均提升1.9pp（文本）、0.5pp（代码）的成功率。
- 文本格式技能在两种归纳粒度下迁移效果均优于代码技能，中等以上资源预算下子任务级技能的投入产出比显著更高。
- 技能效用评分与任务成功率单调正相关，子任务级、文本格式的技能平均效用更高。

有用的技能需同时满足与真实任务匹配度高、跨场景泛化性好两个条件，缺一不可。

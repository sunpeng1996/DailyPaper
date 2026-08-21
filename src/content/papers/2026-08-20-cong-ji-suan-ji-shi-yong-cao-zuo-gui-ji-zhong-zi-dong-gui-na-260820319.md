---
title: Inducing Task Models from Computer-Use Traces
title_zh: 从计算机使用操作轨迹中自动归纳结构化任务模型
authors:
- Yucheng Jiang
- Zora Zhiruo Wang
- Ruishi Chen
- Diyi Yang
affiliations:
- Stanford University
- Carnegie Mellon University
arxiv_id: '2608.20319'
url: https://arxiv.org/abs/2608.20319
pdf_url: https://arxiv.org/pdf/2608.20319
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent 任务归纳与技能迁移
tags:
- Task Induction
- Computer Use Agent
- Workflow Mining
- Skill Transfer
- LLM Agent
one_liner: 提出TMI框架从无标注人机交互轨迹中拆解交织任务，生成带目标层级与控制流的任务模型
practical_value: '- 梳理用户操作轨迹（如商家后台操作、消费者端浏览点击流）时，可复用TMI的事件接地+分段→潜在任务聚类→目标/流程模型对齐的三段式架构，解决多目标交织的行为拆解问题

  - 生成Agent可复用技能时，优先使用带目标层级和控制流（SEQ/FOR/WHILE）的结构化任务模型，相比原始轨迹或线性流程摘要能提升30%左右的下游任务准确率

  - 处理非连续、交织的行为序列时，可借鉴「任务概要+锚点实体/artifact标识符」的匹配策略，避免同一任务因操作中断/切换被拆分为多个独立任务'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
自然态人机交互轨迹（截图、键鼠操作、工具调用记录）是无标注的高价值行为数据，现有方法要么仅生成线性步骤摘要、要么依赖预设任务标签，无法处理真实场景下多任务交织、目标嵌套的复杂行为，也无法输出可审计、可复用的结构化任务知识，阻碍了Agent从人类操作轨迹中学习通用技能的落地。

### 方法关键点
- 三段式TMI框架：首先做事件接地与分段，用多模态模型结合操作前后的屏幕变化将原始低阶事件映射为语义动作，再分层聚合为对应局部目标的活动单元；
- 潜在任务归纳：通过「任务概要+锚点实体/artifact标识符」增量匹配活动，自动发现无预设的潜在任务，支持非连续交织操作的跨段归并，最后做全局任务合并去重；
- 任务模型构建：独立生成递归目标分解的Objective Model与基于时序模式的Procedure Model（支持SEQ/FOR/WHILE三类可观测控制流），再按边界对齐规则融合为统一的结构化任务模型。

### 关键实验
在HumanWork人类操作数据集和SkillsBench Agent执行数据集上测试，潜在任务聚类与真值的ARI达0.974，步骤还原准确率74.9%，远超最强基线的30.3%；用生成的任务模型提取Agent技能，在SkillLearnBench的跨任务泛化准确率比基线高30%，甚至优于人工编写的固定技能。

### 核心结论
独立构建目标层级与控制流模型再做融合的范式，能同时覆盖行为的「为什么做」和「怎么做」两类信息，比直接端到端生成结构化模型的效果更稳定。

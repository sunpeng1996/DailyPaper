---
title: 'ExpVoyager: Direct Experience Navigation for Dynamic Agent Skill Synthesis'
title_zh: ExpVoyager：面向动态Agent技能合成的直接经验导航框架
authors:
- Kwangwook Seo
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2609.32630'
url: https://arxiv.org/abs/2609.32630
pdf_url: https://arxiv.org/pdf/2609.32630
published: '2026-09-25'
collected: '2026-09-30'
category: Agent
direction: Agent 经验复用与动态技能合成
tags:
- LLM Agent
- Skill Synthesis
- Experience Navigation
- Self-evolving Agent
- Memory Utilization
one_liner: 重构Agent技能合成为经验动态导航问题，按需提取过程知识，跨基准性能显著优于现有方法
practical_value: '- 电商导购/下单Agent场景可放弃预构建固定技能库思路，改用按需从历史交互轨迹动态合成技能的方案，避免预抽象丢失关键上下文

  - 可复用轨迹分层视图设计：将用户行为/Agent交互轨迹拆分为全局流程（轨迹级）和单步决策（步骤级）两种存储视图，支持不同粒度的按需检索

  - 经验规模大的业务场景优先采用动态导航方案替代top-k语义检索，可避免检索冗余、精度下降问题，经验体量越大性能增益越显著

  - 可将现有预构建技能作为动态导航的初始知识，再用导航补充缺失信息，兼顾预构建技能的低token消耗和动态技能的高准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能合成方案均提前将历史经验抽象为固定过程知识，要么丢失后续任务所需的关键信息，要么残留大量无关实例细节；基于相似度的top-k轨迹检索则难以匹配过程性相关经验，无法覆盖散落在不同轨迹的局部关键线索，经验复用效率极低。
### 方法关键点
- 重构技能合成问题为历史经验上的动态导航任务，按需从原始轨迹提取任务相关知识，不做提前预抽象
- 搭建可导航经验接口，将每条轨迹拆分为轨迹级（全局执行流程、结果、元数据）和步骤级（单步观测、推理、动作、结果）两种视图，支持正则搜索、全轨迹查看等导航操作
- 设计导航状态管理机制，每轮更新已获取的目标相关知识列表和待验证开放问题列表，引导下一轮导航方向
- 导航结束后将积累的过程知识合成为定制化技能，输入给冻结的执行Agent提供决策指导
### 关键结果
在ALFWorld、WebShop、ScienceWorld三个跨域Agent基准测试，对比ReAct基础Agent、AWM/RBank/Trace2Skill等预构建技能方法、SkillTTA测试时技能合成方法：
- Qwen3.5-9B作为curator时，ALFWorld成功率达63.7%，较次优方法高12.6pct；WebShop得分达61.2，较次优方法高9.2分
- 经验池规模扩大时性能持续提升，较基线的性能优势拉大15%以上
- 与预构建技能结合时可进一步提效20%以上，token消耗较单独使用动态导航降低30%左右

> 最值得记住的结论：Agent经验复用的核心不是提前将经验压缩为固定知识，而是给Agent提供按需主动探索原始经验的接口与引导机制，经验体量越大增益越显著

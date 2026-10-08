---
title: 'SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles'
title_zh: SkillForge：基于动态技能生命周期的技能与Agent协同进化框架
authors:
- Yuyao Ge
- Yiwei Wang
- Yuchen He
- Baolong Bi
- Lingrui Mei
- Jiayu Yao
- Lizhe Chen
- Shenghua Liu
affiliations:
- 中国科学院计算技术研究所
- University of California, Merced
- 清华大学
arxiv_id: '2610.09832'
url: https://arxiv.org/abs/2610.09832
pdf_url: https://arxiv.org/pdf/2610.09832
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent 技能库生命周期管理与协同进化
tags:
- LLM Agent
- Skill Library
- Reinforcement Learning
- Dynamic Lifecycle
- GRPO
one_liner: 提出适配动态技能生命周期的RL框架，实现技能库与Agent策略协同进化，相对提升最高7.8%
practical_value: '- 技能类资产（召回池、营销话术库、客服Agent工具集）管理可直接复用四状态生命周期（试用/活跃/稳定/退役）逻辑，解决冗余过时内容挤占上下文、误导决策的问题，设置滞回阈值避免频繁波动

  - 预退役+协同迭代流程可复用到业务冷启动：上线前先通过基础模型小流量灰度过滤低质候选，再结合真实业务反馈动态迭代，大幅降低冷启动阶段的负向影响

  - LLM引导的定向突变方法可迁移到prompt优化、搜索query改写、推荐话术迭代场景，基于历史失败案例定向优化候选，提升正向转化率

  - 无需盲目追求技能库/召回池规模：85-100个高适配技能的效果远好于130+的冗余库，质量控制优先级远高于规模扩张'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有技能增强LLM Agent普遍采用仅追加的技能库管理模式，随着策略迭代，过时、低质技能会不断累积，既挤占上下文窗口，还会出现「延迟过时」问题（曾经有效的技能随模型能力提升反而变为负向干扰），严重拉低长周期任务成功率。

### 方法关键点
- 三阶段训练流程：①预退役阶段：用基础模型批量rollout，预过滤适配度低于阈值的初始种子技能，仅保留高适配度技能用于SFT冷启动；②SFT阶段：仅用未依赖预退役技能的成功轨迹微调，得到初始策略；③RL协同进化阶段：基于GRPO做策略优化，每10步执行一次技能库锻造周期。
- 四状态技能生命周期：每个技能在试用/活跃/稳定/退役四个状态间流转，设置滞回阈值避免状态频繁波动，初代种子技能设置更高退役门槛避免误删；适配度处于中等区间的技能由第三方LLM结合失败案例定向突变优化，新生成技能进入试用状态。
- 技能库规模动态封顶：平衡退役和突变速率，始终保持技能库紧凑，控制检索开销和上下文占用。

### 关键实验
在ALFWorld、WebShop、搜索增强QA三个基准测试，对比SkillRL等最强基线，ALFWorld成功率达92.4%（相对提升2.8%），WebShop成功率达78.4%（相对提升7.8%），搜索增强QA微平均准确率达48.7%；技能库规模稳定在85-100之间，仅为无退役方案的75%左右。

### 核心结论
技能库的核心竞争力是与当前策略的适配度而非规模，动态淘汰+定向优化的效果远好于无差别累积。

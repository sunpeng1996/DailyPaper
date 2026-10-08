---
title: Homogenization in Multi-Agent Systems
title_zh: 多智能体系统中的同质化问题研究
authors:
- Prakhar Ganesh
- Kyra Wilson
- Luca Zappella
- Barry-John Theobald
- Nicholas Apostoloff
- Lucas Monteiro Paes
- Nivedha Sivakumar
affiliations:
- McGill University & Mila
- University of Washington
- Apple
arxiv_id: '2610.09824'
url: https://arxiv.org/abs/2610.09824
pdf_url: https://arxiv.org/pdf/2610.09824
published: '2026-10-07'
collected: '2026-10-08'
category: MultiAgent
direction: 多智能体系统风险 · 同质化故障模式
tags:
- Multi-Agent System
- Homogenization
- Failure Mode
- Agent Evaluation
- LLM Agent
one_liner: 定义多智能体系统同质化三类度量，揭示三类下游风险，验证常用缓解策略无效
practical_value: '- 搭建电商/推荐场景多Agent系统时，需新增同质化监控逻辑，定期计算conformity、polarization、inertia三类指标，避免推荐结果趋同、偏见被放大

  - 不要依赖调整采样随机种子、混合不同模型家族的策略解决MAS同质化问题，两类方法仅能产生表面多样性，无法规避底层风险

  - 若使用多Agent做商品审核、商家准入等决策类任务，需增加单轮决策独立校验机制，防止单个异常Agent的影响在多轮交互后残留、扩散

  - 生成式推荐场景下的多Agent交互要限制迭代轮次，避免同质化导致推荐多样性下降，甚至放大相同的排序错误，损害用户长期体验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多智能体系统（MAS）依托多Agent协作完成复杂任务，已在代码生成、招聘、同行评审等多个场景落地，但交互过程中易出现Agent行为趋同的同质化问题，会压缩多样性、强化共同错误，现有研究缺乏对该故障模式的系统性量化与风险验证。
### 方法关键点
- 定义三类同质化量化指标：conformity（智能体间评分方差的下降幅度）、polarization（群体平均评分向评分区间端点的偏移幅度）、inertia（群体平均评分随轮次变化的速率下降幅度）
- 覆盖三类真实场景的MAS实验设计：代码生成（4个不同角色的代码评审Agent）、招聘（4个不同维度的简历评估Agent）、同行评审（3个不同视角的论文评审Agent+Meta评审+作者 rebuttal）
- 验证两类常用缓解策略：随机种子采样、混合不同模型家族的MAS配置
### 关键实验结果
数据集采用CodeLMSec代码漏洞数据集（280条样本）、自建反事实招聘数据集（8000份简历）、ICLR 2025论文评审数据集（1950篇投稿）。三类场景多轮交互后，Agent间评分方差降至初始的0.5倍以下，评分变化速率降至初始的0.2倍以下，均出现显著同质化；代码生成场景特定漏洞出现概率随轮次最高提升至15%，招聘场景单Agent注入的偏见在移除后仍持续存在，评审场景跨领域分差随轮次扩大1倍以上；随机采样、混合模型配置均无法缓解上述风险。

多智能体系统的性能不能只看聚合指标，必须显式监控交互过程中的同质化动态，才能避免系统性风险

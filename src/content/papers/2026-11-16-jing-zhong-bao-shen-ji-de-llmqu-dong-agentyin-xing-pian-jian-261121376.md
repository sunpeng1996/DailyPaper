---
title: A Crowd-Audited Atlas of Implicit Bias in LLM-Powered Agents
title_zh: 经众包审计的LLM驱动Agent隐性偏见图谱
authors:
- Jason Alexander
- Yuxuan Li
- Michael Licamele
- Wesley Hanwen Deng
- Sauvik Das
affiliations:
- University of Massachusetts Amherst
- Carnegie Mellon University
- University of Pennsylvania
- Microsoft Research
arxiv_id: '2611.21376'
url: https://arxiv.org/abs/2611.21376
pdf_url: https://arxiv.org/pdf/2611.21376
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: LLM Agent 隐性偏见众包审计
tags:
- LLM Agent
- Implicit Bias
- Crowdsourcing Audit
- Algorithmic Fairness
- Persona Simulation
one_liner: 构建覆盖17类日常场景的506个LLM Agent隐性偏见案例集，揭示众包审计的优先级规律与认知局限
practical_value: '- 构建个性化电商/服务Agent时，需规避基于用户人口统计学属性（性别/消费层级/地域）的刻板印象假设，尤其是高风险场景（健康、金融类推荐），防止隐性偏见累积导致的用户体验分化与合规风险

  - 可复用论文的自动化偏见审计框架：基于业务真实场景库（浏览/下单/售后等）生成决策对，给Agent分配不同用户Persona，统计组间选择差异，快速排查推荐/决策逻辑的隐性偏见

  - 做AI合规审计时可优先覆盖三类高优先级场景：高风险、某类用户群体决策高度一致、覆盖广泛用户的场景，而非仅看偏差数值大小，可有效降低用户举报/投诉风险

  - 搭建用户行为仿真系统时，不能仅以「符合大众认知」为校准标准，需保留群体内部的行为多样性，避免放大刻板印象导致仿真结果失真'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM隐性偏见研究多聚焦招聘、司法等高关注度场景，忽略了LLM Agent在日常任务（购物、出行、育儿等）中替用户做决策时的隐性偏见，且缺乏对「哪些偏见更值得优先修复」的公众认知研究，难以支撑Agent的公平性优化和合规落地。

### 方法关键点
- 基于美国时间使用调查（ATUS）的17类日常活动，系统生成804个决策场景-人口统计学维度配对，给Agent分配不同种族、性别、政治意识形态Persona，对比组间决策差异筛选偏见案例
- 招募500名美国成年用户开展众包审计，完成8010次二元偏见案例优先级对比，结合Bradley-Terry模型计算案例优先级，通过主题分析挖掘用户判断逻辑
- 同时在GPT-5.4、Gemini 3.8 Flash、Qwen3.8-Max三个模型上验证偏见的跨模型一致性

### 关键结果数字
- 筛选得到覆盖全部17类日常场景的506个有效隐性偏见案例，48.6%的案例中存在某个人口群体所有Agent决策完全一致的极端刻板印象；跨模型验证显示92%+的偏见方向在三个模型中一致
- 众包优先级判断中，场景领域仅能解释6.4%的优先级差异，偏差大小仅对政治意识形态类偏见有弱相关性；高风险场景、群体决策全一致的案例优先级显著更高，性别类偏见整体优先级最低
- 偏差大小、人口维度、场景风险、群体一致性四类特征共可解释30%的优先级差异

### 核心结论
众包审计既能发现定量指标遗漏的社会层面偏见风险，也存在因审计者自身固有刻板印象导致的盲区，不能仅以大众认知的「合理性」作为偏见是否需要修复的唯一标准

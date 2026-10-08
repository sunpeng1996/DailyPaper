---
title: 'SkillSandbox: Skill Verification via Dynamic Scenario Synthesis'
title_zh: SkillSandbox：通过动态场景合成实现Agent技能可复用性验证
authors:
- Serin Kim
- Kwangwook Seo
- Dokyung Song
- Jinyoung Yeo
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2610.10088'
url: https://arxiv.org/abs/2610.10088
pdf_url: https://arxiv.org/pdf/2610.10088
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent · 技能库验证与筛选
tags:
- SkillVerification
- DynamicScenarioSynthesis
- SelfEvolvingAgent
- SkillLibraryCuration
- ReusabilityAssessment
one_liner: 为自进化Agent动态生成技能相关新场景验证可复用性，筛选高价值技能提升下游任务表现
practical_value: '- 电商导购Agent技能库可直接复用该验证框架：针对商品筛选、优惠核算、订单查询等高频技能，动态生成不同商品属性、活动规则的测试场景，过滤仅适配历史活动的无效技能

  - 三维评估标准可直接迁移到业务：从可执行性（技能指导是否能落地为合法操作）、效用（是否提升任务成功率）、效率（是否减少操作/推理步数）三个维度对比有无技能的执行差异，避免只看成功率忽略额外开销

  - 无需依赖更强模型完成技能验证：自进化Agent用自身同规格模型即可完成场景合成与验证，不需要引入外部大模型，大幅降低技能库维护的算力成本

  - 解决技能验证稀疏问题：不需要等下游真实业务场景触发技能，主动合成场景快速完成技能准入，缩短技能库迭代周期'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
自进化Agent会将任务执行经验蒸馏为结构化技能存入库中复用，但蒸馏过程易引入错误流程、过拟合源任务的不可迁移知识，一旦被调用会反复干扰Agent执行。现有验证方法要么仅在源任务上测试无法验证泛化性，要么从现有任务池中选任务，语义相似的任务仅6成能触发技能适用场景，且下游真实场景中技能触发率极低，500个任务后仍有17-32%的技能从未被调用，无法完成验证。

### 方法关键点
- 三模块架构：PROPOSER基于技能的适用条件、源任务与轨迹，指定场景需保留的核心约束、要修改的源任务细节，输出可编程的合成规范
- BUILDER基于规范绑定真实环境数据生成可执行场景，经过校验循环确保场景既触发技能适用条件又与源任务不同，每个技能生成5个有效验证场景
- VERIFIER对比同一Executor在同一场景下有无技能的执行轨迹，综合可执行性、效用、效率三个维度打分，得分>0的技能才准入库

### 关键实验
在ALFWorld（家居交互任务）、WebShop（电商购物任务）两个基准上测试，对比无技能、全量保留技能、ExpeL/ACE/SkillOS等现有技能管理方案，覆盖Qwen3.5-9B/27B、Gemini 3.1 Flash-Lite三个模型：WebShop上成功率相比No Skill最高提升41.4%，相比最强基线最高提升21.4个百分点，回归率（原本能完成的任务用了技能反而失败）最低降到1.8%。

**最值得记住的一句话**：技能验证不能依赖现有任务的被动触发，要围绕技能主动构造相关新场景，才能高效筛选出真正可复用的高价值技能。

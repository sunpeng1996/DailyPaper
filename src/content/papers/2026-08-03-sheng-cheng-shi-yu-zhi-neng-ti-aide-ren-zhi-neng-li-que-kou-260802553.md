---
title: A Taxonomy of Cognitive Capability Gaps in Generative and Agentic AI
title_zh: 生成式与智能体AI的认知能力缺口分类体系
authors:
- Taye Akinrele
- Sindhuja Penchala
- Noorbakhsh Amiri Golilarz
- Sudip Mittal
- Shahram Rahimi
affiliations:
- The University of Alabama
arxiv_id: '2608.02553'
url: https://arxiv.org/abs/2608.02553
pdf_url: https://arxiv.org/pdf/2608.02553
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 认知能力框架与评估
tags:
- Agentic AI
- Cognitive AI
- Taxonomy
- Cognitive Architecture
- LLM Evaluation
one_liner: 梳理生成式与智能体AI五大类认知能力缺口，给出认知AI统一架构与认知导向评估框架
practical_value: '- 设计电商长周期交互Agent（如全旅程导购、售后自动处理Agent）时，可直接参考5类认知缺口做故障埋点，比如新增目标漂移检测、记忆一致性校验规则，减少长交互中的逻辑矛盾、任务偏离问题

  - 搭建Agent架构时可复用ACIA的6组件划分，尤其将元认知模块独立出来做不确定性检测、异常行为拦截，可显著降低高风险场景（如支付引导、售后理赔）的错误率

  - 评估长周期Agent性能时，可复用CPI/CAR/CCS三类认知导向指标，补充传统的任务成功率、用户满意度指标，更全面衡量长交互下的系统稳定性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
生成式AI与Agent已在短周期任务上展现优异表现，但长周期自主运行时频繁出现记忆丢失、目标漂移、推理不一致、环境适配性差等问题，现有研究多聚焦单点能力优化，缺乏统一的认知能力缺口梳理框架，无法支撑高鲁棒性的长周期AI系统设计。
### 方法关键点
- 梳理形成5大类核心认知能力缺口分类，分别为持久状态建模、目标导向自主性、自监控与控制、环境交互、学习与适配，每类下细分3个具体子缺口，覆盖当前Agent绝大多数长周期故障场景
- 给出自适应认知智能架构ACIA，包含感知与注意力、记忆、推理与规划、元认知、行动、学习与适配6个闭环组件，一一对应解决上述5类认知缺口
- 设计认知导向评估体系，包含认知持久性指数CPI、认知适配率CAR、认知一致性得分CCS三类核心指标，弥补传统短任务评估无法衡量长周期认知稳定性的缺陷
### 关键结果
该研究为综述类工作，系统整合近3年Agent、LLM认知相关的100+项研究成果，提出的分类框架已被多个前沿AGI研发团队采纳为系统设计参考标准
### 核心结论
认知AI的核心是构建持续进化的内部状态，而非仅完成孤立的单次任务，长周期稳定性远重于短任务成功率

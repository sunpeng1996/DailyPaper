---
title: 'From Skill Extraction to Multistakeholder Recommendation: A Two-Stage Framework
  for Bias Governance in Skills-Based Job Matching'
title_zh: 面向技能型岗位匹配的两阶段偏见治理框架：覆盖技能抽取与多利益相关方推荐
authors:
- Andrea Forster
- Gregor Autischer
- Dominik Kowald
- Simone Kopeinik
affiliations:
- Know Center Research GmbH, Graz, Austria
arxiv_id: '2607.15707'
url: https://arxiv.org/abs/2607.15707
pdf_url: https://arxiv.org/pdf/2607.15707
published: '2026-07-17'
collected: '2026-07-20'
category: RecSys
direction: 多利益相关方推荐 · 多Agent公平治理
tags:
- Multi-Stakeholder Recommendation
- Bias Governance
- Multi-Agent
- Fairness in RecSys
- EU AI Act
one_liner: 提出两阶段多Agent偏见治理框架，覆盖技能抽取到岗位推荐全链路，适配欧盟AI Act合规要求
practical_value: '- 多利益相关方推荐场景（如电商的用户/商家/平台三方平衡、广告的广告主/流量方/用户诉求对齐）可直接复用「分Agent独立排序+计算社会选择规则聚合」的架构，替代黑盒单目标打分，既兼顾多方诉求，又具备可审计性

  - 全链路合规治理可复用硬/软约束分层机制：硬约束（如资质不符、信息错误）直接拦截修正，软约束（如群体层面的系统性偏差）透传到下游模块动态调整阈值，避免单点公平优化的局限性，可直接迁移到电商合规审核→推荐排序的全链路治理

  - 监管要求高的推荐场景（如招聘、金融、广告合规）可参考「分布审计+反事实测试」的偏见检测方法，提前识别群体层面的公平性风险，降低合规成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
技能导向的岗位匹配系统易从历史劳动数据继承性别、种族等刻板印象偏见，且偏见会从上游技能抽取环节传导到下游推荐排序环节，传统单点公平优化无法覆盖全链路风险；同时欧盟AI Act将招聘类AI列为高风险系统，要求系统可审计、可追溯，现有框架缺乏兼顾全链路偏见治理、多利益相关方诉求平衡、监管合规对齐的统一解决方案。
### 方法关键点
- 两阶段全链路架构：Stage1为技能抽取与画像生成阶段，针对Chatbot对话式技能抽取场景，通过分布审计（统计历史技能分配的群体分布差异）+反事实测试（性别表达替换、刻板印象注入）识别偏见，将问题分为硬约束（缺失信息、错误抽取等直接拦截重采）和软约束（群体层面的系统性偏差，透传到下游）两类；Stage2为多利益相关方推荐阶段，设置三个独立Agent：候选人Agent（匹配个人技能与求职偏好）、公司Agent（匹配岗位招聘要求）、监管Agent（对齐公平性阈值），各自生成独立排序后采用计算社会选择的投票规则聚合为最终可审计的推荐结果
- 统一的硬/软约束流转机制：Stage1识别的软约束直接作为Stage2监管Agent的公平阈值，Stage2的推荐结果也按相同规则校验，硬约束触发重新调整Agent权重/聚合规则，软约束日志用于长期公平性漂移监控
- 全流程对齐Fraunhofer AI评估目录，所有环节操作可追溯，满足欧盟AI Act高风险系统的合规准备要求
### 关键实验说明
本框架目前为概念性设计，尚未完成端到端系统的大规模实证验证；参考相关前置工作的验证效果：分布审计可精准识别历史数据中不同群体的技能分配偏差（如案例中87%的清洁类技能被分配给女性用户、91%的电气工程类技能被分配给男性用户），多Agent投票聚合方案可在保证推荐准确率下降不超过2%的前提下，将群体公平性指标提升18%左右。
### 核心结论
公平性治理不能只局限于推荐排序环节，上游数据抽取阶段的偏见传导、多利益相关方的诉求平衡、长期的合规可审计性共同决定了系统的实际公平表现

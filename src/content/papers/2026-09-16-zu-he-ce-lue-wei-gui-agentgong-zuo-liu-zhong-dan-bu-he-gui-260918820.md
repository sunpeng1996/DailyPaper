---
title: 'Compositional Policy Violations: When Step-Level Compliance Fails In Agentic
  AI Workflows'
title_zh: 组合策略违规：Agent工作流中单步合规失效问题研究
authors:
- Ashwini Kurady
- Sri Sai Charith Grandhi
- Rajesh Gupta
- Sumit Mamoria
affiliations:
- runctrl.ai
arxiv_id: '2609.18820'
url: https://arxiv.org/abs/2609.18820
pdf_url: https://arxiv.org/pdf/2609.18820
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent工作流治理 · 合规检测
tags:
- Agent Governance
- Policy Compliance
- Provenance Tracking
- Runtime Verification
- Workflow Safety
one_liner: 定义Agent工作流四类组合策略违规模式，提出基于全链路溯源的运行时合规检测架构
practical_value: '- 电商/广告Agent工作流（如智能投放、客服审批流）新增合规校验时，不能仅做单步校验，需叠加全链路trace维度的违规检测，避免权限
  creeping、阈值拆分等合规漏洞

  - 架构设计可复用论文提出的2个核心不变性：全链路历史数据不截断、所有策略校验的核心指标从原始溯源数据重算，不依赖pipeline中间衍生值，可大幅降低合规误判率

  - 电商大促多Agent协同的资源分配、优惠发放场景，可直接套用四类CPV分类做风险巡检：比如优惠叠加超限属于Cumulative Sum Violation，可提前配置聚合维度的阈值校验

  - 基于LLM的商品文案生成、商家合规审核链路，需针对Context Collapse类违规保留原始提交数据，终审前重推原始数据校验，避免中间摘要丢失信息导致违规内容过审'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent工作流已在保险、金融等受监管场景规模化落地，现有合规治理几乎全部采用单步粒度校验（如输入输出分类、单轮护栏、片段级评估），但企业实际执行的合规规则（如上报阈值、权限限制、审核要求）均是面向全链路执行过程的属性，二者的结构性错配会产生「所有单步合规但整体执行违规」的风险，且现有单步监控无论精度多高都无法检测这类失效，亟需针对性的治理方案。
### 方法关键点
- 明确定义组合策略违规（CPV）：所有单步满足自身校验规则，但组合后的执行违反全链路策略，且无组件故障，属于架构层面的设计缺陷
- 提出四类CPV分类体系：Authority Creep（权限 creep，多步判断叠加绕过权限路由门限）、Threshold Laundering（阈值洗白，校验后修改指标不再重检）、Cumulative Sum Violation（累计和违规，无聚合维度校验导致单步合规总量超限）、Context Collapse（上下文坍缩，多步摘要累加丢失关键信息导致最终决策错误）
- 提出溯源感知的运行时检测架构，核心含4个阶段：溯源数据摄入归一化、状态重建、策略评估、组合违规检测，严格遵循两个设计不变性：全链路历史数据不截断、所有待校验指标从原始溯源数据重算，不依赖pipeline中间衍生值
### 关键结果
论文暂无公开定量实验验证，核心贡献为问题定义、分类体系与检测架构，同时给出每类CPV的对应修复方案：权限creep从决策点反向溯源、阈值洗白在提交前重校验、累计和违规新增聚合维度校验、上下文坍缩对比原始提交与最终审核数据的决策一致性。
### 核心结论
Agent工作流的合规治理不能仅做单步checkpoint校验，必须将策略 enforcement 作为全链路的固有属性，覆盖完整执行trace而非孤立决策点。

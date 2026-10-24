---
title: Reliable AI-Assisted Decisions via Selective Auditing
title_zh: 基于选择性审计的可信AI辅助决策方法
authors:
- Isaac Gibbs
- Elise L. Han
- Ryan J. Tibshirani
- Tijana Zrnic
affiliations:
- University of Toronto
- Stanford University
- University of California, Berkeley
arxiv_id: '2610.31662'
url: https://arxiv.org/abs/2610.31662
pdf_url: https://arxiv.org/pdf/2610.31662
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: Agent 决策审计与风险控制
tags:
- Selective Auditing
- Online Optimization
- Error Control
- Agent Oversight
- LLM Safety
one_liner: 提出无假设可证误差控制的在线选择性审计算法，在漏审错误率阈值约束下最小化审计成本
practical_value: '- 可直接复用算法框架到LLM用户有害请求、广告合规内容筛查场景，在满足安全阈值的前提下降低30%+人工审核成本

  - 适配生成式推荐/Agent决策链路，增设独立Verifier Agent输出置信分，自动判定是否触发人工/高阶模型复审，平衡业务效果与运营成本

  - 算法无数据分布假设，适配对抗性、i.i.d.数据流，可落地到搜索推荐Bad Case在线抽检、电商高风险交易决策等高要求场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
AI系统规模化落地高风险决策场景时，全量专家审核成本过高，现有审计方案无通用误差控制保证，无法适配对抗性等复杂数据流，难以满足合规与安全要求。
### 方法关键点
将选择性审计任务建模为在线约束优化问题，目标是最小化专家审计频次，同时保证未审计AI决策的错误占比低于用户预设阈值；推导得到无数据分布假设的可证误差控制算法族，其中最优效率版本可在对抗性、i.i.d.数据流下渐近达到理论最优审计率；支持决策生成模块与置信度评估模块解耦，适配Agent+独立Verifier的架构。
### 关键结果
在LLM有害请求筛查、文本标注、数据标注三类场景实验中，相比基线方法降低超30%的人工审计量，同时严格满足预设的漏审错误率约束。

---
title: Toward a Science of AI Agent Societies
title_zh: AI Agent 社会的科学研究框架构建
authors:
- Geon Lee
- Fanchen Bu
- Soo Yong Lee
- Sunwoo Kim
- Kijung Shin
affiliations:
- KAIST, Republic of Korea
arxiv_id: '2611.25404'
url: https://arxiv.org/abs/2611.25404
pdf_url: https://arxiv.org/pdf/2611.25404
published: '2026-11-19'
collected: '2026-11-20'
category: MultiAgent
direction: 多智体社会 · 核心属性与研究框架
tags:
- Multi-Agent
- Agent Society
- Governance
- LLM Agent
- Emergent Behavior
one_liner: 提出AI Agent社会的4项核心属性、4类研究方向及3项落地技术挑战
practical_value: '- 搭建电商Agent交易生态时，可参考4个核心属性做合规校验：需给Agent配置独立用户目标、明确平台规则边界、保障Agent决策自主权、达到可涌现集体行为的规模阈值

  - 做Agent平台治理时，可针对4类典型涌现行为（经济行为、利益冲突、风险行为、系统级行为）提前设计监控与干预机制，比如防范Agent合谋抬价、虚假宣传等

  - 做多Agent仿真时，可参考属性参数化、多属性平衡、鲁棒实现三步法搭建可控测试环境，避免规则过严抑制涌现或过松导致结果不可复现'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent已从孤立个人助手演进为大规模网络交互实体，小范围多Agent仿真已观测到关系建立、合谋、极化等集体行为，但业界缺乏统一的AI Agent社会定义与研究框架，无法系统性解释、预测、调控大规模Agent交互的涌现结果，对未来Agent电商、社交、交易平台的落地造成风险。

### 方法关键点
1. 有效AI Agent社会的4个核心必要属性：独立个性化目标（Agent目标独立于系统全局目标，可与其他Agent/系统目标冲突）、规则与治理（平台统一制定交互约束、奖惩、争议解决机制）、自主性（Agent为决策主体，而非刚性执行预定义策略）、规模与复杂性（足够多Agent长期持续交互，可涌现不可还原到单Agent的集体行为）
2. 划分4类核心研究行为：经济商业行为、利益冲突下行为、不安全不道德行为、系统级行为
3. 落地需突破三大技术挑战：属性参数化、多属性平衡、鲁棒实现
4. 基于该框架回溯现有多Agent系统，当前工作均只覆盖部分属性，尚未形成真正的AI Agent社会

### 关键结果
本研究为观点框架类研究，无量化实验结果，核心判断已被现有多Agent仿真、经济博弈研究的观测结果验证。

### 核心结论
AI Agent社会的涌现结果无法通过单Agent对齐保证，安全与治理需从单模型层面升级到Agent社会的制度设计层面。

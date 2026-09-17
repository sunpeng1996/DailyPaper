---
title: 'Flag Game: A Toy Model for Mechanistic Swarm Interpretability'
title_zh: 旗帜游戏：面向群体智能机制可解释性的玩具模型
authors:
- Elizabeth Pavlova
- Hidenori Tanaka
affiliations:
- Harvard University
- NTT Research, Inc.
- Cambridge Boston Alignment Initiative
arxiv_id: '2609.19124'
url: https://arxiv.org/abs/2609.19124
pdf_url: https://arxiv.org/pdf/2609.19124
published: '2026-09-16'
collected: '2026-09-17'
category: MultiAgent
direction: 多智体 · 群体行为可解释性研究
tags:
- MultiAgent
- Swarm Interpretability
- Collective Belief
- Causal Intervention
- Mechanistic Interpretability
one_liner: 提出旗帜游戏玩具模型，结合两类方法解析多智能体群体信念形成的底层机制
practical_value: '- 多Agent协作的电商选品、广告投放决策场景，可复用群体规模与性能非单调变化的结论，合理控制协作Agent数量避免规模过大导致的决策极化性能下降

  - 调优多Agent业务系统时，可引入social-awareness prompt、配置异质性Agent团队，快速提升集体决策准确率

  - 小体量多Agent集群的效果归因可复用social circuit attribution方法，快速定位影响最终决策的核心Agent节点，降低干预成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
多AI Agent涌现的协同行为存在不可控安全风险，当前缺乏对群体信念形成、传播机制的可解释性研究，无法有效保障群体行为对齐预期目标。
### 方法关键点
1. 提出Flag Game玩具模型：隐藏国旗为真值，每个Agent仅观测局部切片，可交换信念、参考同伴证据，模拟真实群体决策过程；
2. 小群体采用social circuit attribution结合因果干预定位核心影响节点，大群体适配统计力学理论拟合行为相图。
### 关键结果
群体性能随规模呈非单调变化：小群体易出现信念坍缩，规模扩大后转为信念极化导致性能下降；加入社会感知prompt、提升团队多样性可显著提升决策准确率，组织结构对结果影响明显。

---
title: 'Moral Competence Before Moral Content: Why LLM Agents Lack the Prerequisites
  for Coherent Alignment'
title_zh: 先谈道德能力再谈道德内容：LLM Agent尚不满足一致对齐前置条件
authors:
- Arno Libert
- Derck W. E. Prinzhorn
- Daan R. Henselmans
affiliations:
- Aithos Research Foundation
arxiv_id: '2609.05036'
url: https://arxiv.org/abs/2609.05036
pdf_url: https://arxiv.org/pdf/2609.05036
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 行为对齐与道德能力评估
tags:
- LLM Agent
- AI Alignment
- Evaluation
- Moral Competence
- Prompt Robustness
one_liner: 提出无道德基准的Agent行为一致性评估指标，验证当前前沿LLM Agent均未达标
practical_value: '- 电商导购/客服Agent的决策稳定性评估可复用4项结构指标（verdict stability/monotonicity/decisiveness/Pareto
  viability），无需人工标注正确答案即可快速定位决策波动问题

  - Agent上线前必须做语义等价prompt的扰动测试，现有单配置评估最高可漏99pp的决策波动，涉及用户扣费、权益分配等敏感决策场景必须强制覆盖

  - Agent对齐训练可针对缺陷定向优化：稳定性差加prompt扰动训练，决定性差加决策阈值校准，Pareto有效性差补充权威指令override的训练样本

  - 多利益相关方推荐场景（同时满足平台/商家/消费者诉求）可先用这组指标验证策略结构一致性，再调优具体偏好规则'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent对齐研究多聚焦道德内容匹配，忽略核心前置条件：只有Agent决策本身具备结构一致性，对齐目标才有落地可能。现有评估依赖人工道德基线，不适用于价值多元的业务场景，且单配置评估严重低估prompt表面扰动带来的决策波动，无法反映上线后的真实行为稳定性。

### 方法关键点
- 提出无需道德基准的4项结构一致性指标：verdict stability（语义等价扰动下决策分布不变）、monotonicity（道德相关维度变化时决策单调无振荡）、decisiveness（决策分布远离0.5随机态）、Pareto viability（不选所有利益相关方都认为更差的选项），取几何平均为总道德能力得分
- 设计3类Agent决策困境场景（化工泄漏处置、智能家居upsell、金融科技隐私告知），每个场景沿3个正交轴变化：5种语义等价paraphrase、5级道德风险梯度、3种Pareto主导条件（模糊/支持X/反对X）

### 关键结果
评测9款前沿大模型（Claude Sonnet 4.6、GPT-5.4、Gemini 2.5 Pro等），每个模型单场景测3500次：
- 仅语义等价paraphrase就能导致单场景决策率波动最高达99pp，8/9的模型至少在1个场景波动超50pp
- 所有模型的总道德能力得分最高仅0.75，单场景得分跨度0.19~1.00，模型在一个场景的表现完全无法预测其在另一个场景的得分
- 最常见失效维度是decisiveness，6/9的模型在金融隐私场景决策接近随机（D<0.2）

### 最值得记住的一句话
一个决策随无关特征波动99pp的系统，无论采用什么对齐框架，都不可能真正符合对齐目标。

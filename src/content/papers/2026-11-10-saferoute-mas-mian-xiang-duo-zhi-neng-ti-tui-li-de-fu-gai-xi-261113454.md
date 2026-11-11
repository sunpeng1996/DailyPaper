---
title: 'SafeRoute-MAS: Coverage-Aware and Risk-Calibrated Message Routing for Multi-Agent
  Scientific Reasoning'
title_zh: 《SafeRoute-MAS：面向多智能体推理的覆盖感知风险校准消息路由》
authors:
- Zhiming Xue
- Jianan Liu
- Weiran Yan
- Aicheng Xie
- Jing Yang
affiliations:
- Northeastern University (Boston)
- Washington University in St. Louis Olin Business School
- Independent Researcher
arxiv_id: '2611.13454'
url: https://arxiv.org/abs/2611.13454
pdf_url: https://arxiv.org/pdf/2611.13454
published: '2026-11-10'
collected: '2026-11-11'
category: MultiAgent
direction: 多智体系统 · 消息路由与风险校准
tags:
- MultiAgent
- MessageRouting
- RiskCalibration
- SelectivePrediction
- ContextEfficiency
one_liner: 提出覆盖感知+风险校准的多智能体消息路由方案，在不损失精度前提下削减12%以上消息token开销
practical_value: '- 多Agent协作场景可复用「风险校准选择性剪枝+全保留降级」架构，平衡上下文开销与效果损失，适合电商客服、商品选品等多Agent协同业务

  - 消息剪枝无需引入标注的正确性标签，仅用角色、置信度、长度、一致性等可观测特征即可训练，低成本适配业务场景

  - 上线前可复用多维度准入校验规则，覆盖整体效果下界、token削减率、子群风险上限等指标，避免局部子群效果劣化'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
多智能体协作推理依赖大量专家消息交互，冗余或误导性消息会占用上下文空间、降低推理准确率，现有剪枝方案要么依赖后验效果标签无法上线，要么容易丢失少数派有效信息，因此需要一套仅用前置可观测信息、风险可控的消息路由方案，在降低上下文开销的同时不损失推理效果。

### 方法关键点
- 基于三类消息风险（有害/中性/有益）构建效用评估函数，仅用角色、推理视角、置信度、长度、与多数派一致性等前置可见特征训练，不引入答案正确性等后验标签
- 搭配校准的选择性门控与多样性规则，仅当待剪枝消息得分超过冻结阈值、且不属于唯一少数派视角时才执行剪枝，否则降级为保留全部消息
- 上线前设计多维度准入校验流程，要求满足整体效果下界≥-1pp、token削减≥10%、子群风险上界≤5%等条件才可部署

### 关键实验
在SciAgentTrace数据集5328个多智能体委员会的密封缓存测试中，SafeRoute-MAS相比全保留基线提升准确率1.80pp，削减12.76%的消息token，有益剪枝风险95% UCL仅3.61%；在公共gpt-oss-120b端点的4580次受控测试中，加权后准确率提升0.94pp，削减18.72%的输入token，风险上界4.60%，但未达到统计显著性。

### 核心结论
多智能体消息剪枝不要追求最优效果，而是要在严格的风险控制下做收益trade-off，不确定场景直接降级为全量保留是最稳妥的工程选择。

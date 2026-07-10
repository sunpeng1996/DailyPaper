---
title: Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems
title_zh: LLM驱动多智能体系统故障定位框架AgentLocate
authors:
- Yufei Xia
- Anjun Gao
- Yueyang Quan
- Zhuqing Liu
- Minghong Fang
affiliations:
- University of Louisville
- University of North Texas
arxiv_id: '2607.07989'
url: https://arxiv.org/abs/2607.07989
pdf_url: https://arxiv.org/pdf/2607.07989
published: '2026-07-08'
collected: '2026-07-10'
category: MultiAgent
direction: 多智能体 · 故障归因与可靠性优化
tags:
- Multi-Agent System
- Failure Localization
- LLM-as-Judge
- LoRA
- Fault Attribution
one_liner: 提出Judge-Evaluator架构的故障定位框架，同时识别责任Agent与最早决定性错误步
practical_value: '- 多智能体系统debug可直接复用Judge-Evaluator的众包评估逻辑：采用不同prompt风格的多LLM Evaluator做置信度加权投票，比单模型一次性判断准确率提升20%+，适合复杂多步推荐/导购/客服Agent的错误归因

  - 故障归因的自适应优化可复用低成本LoRA微调方案：将Evaluator的反馈作为弱监督信号微调Judge模型，无需人工标注即可持续沉淀故障案例提升归因准确率，适配业务迭代需求

  - 多智能体链路优化可参考「最早决定性错误步」定义：定位到最早的可修正错误节点即可逆转全局失败，无需回溯全链路，能大幅降低多Agent推荐系统的debug和迭代成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM多智能体系统已落地于复杂任务处理，但分布式决策、长链路交互的特性导致故障溯源难度极高：单个Agent的微小错误会沿交互链路传导引发全局失败，现有方法要么依赖反事实回放成本高昂，要么依赖预定义错误模板覆盖度不足，无法同时准确定位责任Agent与最早决定性错误步。
### 方法关键点
- 三阶段归因架构：首先由LLM Judge生成故障假设，支持全链路一次性分析、逐步递进分析两种模式，适配不同长度的交互轨迹
- 多视角验证机制：3个不同prompt风格（基础、简洁、证据优先）的独立Evaluator重新校验Judge假设，输出各自的归因结果、理由和置信度，通过置信度加权投票聚合得到鲁棒定位结果
- 自适应迭代优化：将Judge预测、Evaluator反馈、聚合结果整合成训练样本，通过LoRA微调Judge模型，无需人工标注即可持续提升定位精度
### 关键结果
在Who&When、Aegis-Bench两个基准数据集测试，对比WhichAgent、AgenTracer、AEGIS等4个基线及2个投毒取证方法：Qwen-7B全量分析模式下，Agent级准确率达69.05%，步级准确率达38.10%，较基线最高提升38pct；运行速度比AgenTracer快20倍，成本仅为其1/22。

多智能体故障定位不能依赖单次判断，需将归因过程设计为可验证、可迭代的闭环，才能在复杂交互场景下兼顾精度和效率。

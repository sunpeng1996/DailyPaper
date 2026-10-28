---
title: 'LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation'
title_zh: LCM-Promo：基于大语言模型的促销分配增益模型
authors:
- Nesta Midavaine
- Floris Fok
- Paulo Mendes
- Joao Silva
- Önder Akaçık
- Dimas Lima
- Zülküf Genç
affiliations:
- Prosus, Amsterdam, Netherlands
- iFood, São Paulo, Brazil
arxiv_id: '2610.37570'
url: https://arxiv.org/abs/2610.37570
pdf_url: https://arxiv.org/pdf/2610.37570
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: 电商运营 · LLM驱动促销增益建模
tags:
- LLM
- Uplift Modeling
- Promotion Allocation
- E-commerce
- Large Commerce Model
one_liner: 基于电商领域专用LLM构建促销增益模型，上线后转化提1%促销成本降6%
practical_value: '- 促销分配场景可复用单token预测+阈值累积的方法，天然保证折扣响应曲线单调性，避免传统增益模型输出非单调的不合理问题

  - 可参考将用户表征、会话上下文（时段、城市、生命周期等）直接序列化进LLM输入的方案，无需维护大量分桶规则，可大幅扩展细分人群和促销组合覆盖度

  - 工程落地可采用预计算用户表征+批量GPU推理（vLLM + 开源BESH调度框架）的架构，4B参数量级模型可支撑亿级用户的每日促销触达需求

  - 仅用生产日志训练的LLM增益模型效果可匹敌用RCT数据训练的Uplift Random Forest，可降低对高成本随机实验数据的依赖'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商促销分配的核心是增益建模，即估计不同折扣下用户的转化提升率，传统分桶统计方法（如Segment-EMA）受限于分桶粒度，无法覆盖复杂的会话上下文（时段、城市、用户生命周期）和海量促销组合，且新折扣上线需要大量探索数据，效率极低。

### 方法关键点
- 以4B参数电商领域专用Large Commerce Model（LCM）为基座微调，把促销分配转化为单token预测任务：每个折扣对应唯一字母标识符，无转化对应特殊token，训练用交叉熵损失拟合观测到的转化-折扣标签。
- 推理时仅保留有效标识符的概率分布并重归一化，将其解释为用户转化阈值的概率分布，通过累积概率计算不同折扣下的转化概率，天然保证响应曲线单调非减，可直接用于预算约束下的分配优化。
- 可选waterfall增强训练：对转化用户，所有大于等于其转化折扣的标签都设为正，用软目标交叉熵训练。

### 关键实验
线上A/B测在iFood流失用户召回场景开展，90%用户进对照组（生产用Segment-EMA分桶方案）、10%进实验组，两者用相同预算约束和分配器，仅响应模型不同：实验组转化相对提升1%，促销总成本相对下降6%，后续已全量上线。
离线实验对比用RCT数据训练的Uplift Random Forest，LCM-Promo仅用生产日志训练，AUUC、Qini指标与基线相当，仅Uplift@30略低，waterfall增强方案效果更差，与LLM的next-token预训练目标冲突。

### 最值得记住的结论
领域专用微调LLM可直接作为增益模型落地电商核心运营场景，成本可控且效果优于传统分桶统计方案。

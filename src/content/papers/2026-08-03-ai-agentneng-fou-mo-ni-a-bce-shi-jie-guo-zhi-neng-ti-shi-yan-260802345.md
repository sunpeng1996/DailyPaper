---
title: Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic
  Experimentation
title_zh: AI Agent能否模拟A/B测试结果？智能体实验验证框架
authors:
- Stefan Hut
- Lorenzo Masoero
affiliations:
- Amazon
arxiv_id: '2608.02345'
url: https://arxiv.org/abs/2608.02345
pdf_url: https://arxiv.org/pdf/2608.02345
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 模拟用户行为优化A/B测试流程
tags:
- A-B Testing
- AI Agent
- User Simulation
- S-RCT
- Causal Inference
one_liner: 提出双层误差分解的S-RCT框架，结合校准与组内设计大幅提升A/B测试的Agent模拟准确率
practical_value: '- 做推荐/营销策略预筛时，可先用Agent模拟A/B测试做方向初筛，当前基线就有0.7的符号重合度，能淘汰明显效果为负的方案，节省线上流量成本

  - 可复用两阶段预实验校准trick，用无treatment的预实验数据拟合校正函数修正LLM行为放大偏差，本文实测可降低77倍预测误差，成本远低于全量fine-tune

  - 模拟用户实验优先采用组内设计，让同一个Agent同时暴露给对照组和实验组，消除用户抽样方差，本文实测标准误降低2.4倍，符号准确率提升5个百分点

  - 针对高方差业务指标（如revenue），可采用Neyman分层抽样法分配模拟Agent配额，相比均匀抽样最多可降低5倍方差，减少模拟算力消耗'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
A/B测试是互联网产品迭代的黄金标准，但单实验需消耗大量线上流量、数周时间才能积累统计显著性，大公司每年数千次实验的综合成本极高，且会让用户暴露给可能效果不好的候选方案。现有用Agent模拟A/B测试的方案缺乏系统的误差拆解，难以针对性优化准确率。

### 方法关键点
- 形式化定义模拟随机对照试验（S-RCT）框架，将总预测误差拆分为独立的两层：Agent行为近似误差、抽样误差，支持分别优化。框架兼容任意行为模型，从fine-tune的领域模型到通用大模型都可作为模拟引擎
- 针对抽样误差：采用Neyman分层抽样，按用户子群的方差分配模拟配额，降低小样本估计方差；同时采用组内设计，同一个Agent同时访问对照组和实验组，消除用户构成差异带来的方差
- 针对近似误差：提出两阶段预周期校准流程，先用无treatment的预实验数据拟合校正函数，修正LLM系统性高估用户响应幅度的偏差，再用校正后的模型输出预测实验效果

### 关键实验
在亚马逊67个真实电商营销A/B测试数据集上验证，基准通用大模型不加优化时方向符号重合度达0.7，但效果幅度系统性高估；加入两阶段校准后校正MSE降低77倍，组内设计相比组间设计标准误降低2.4倍，符号准确率从65%提升至70%。

### 最值得记住的一句话
当前Agent模拟A/B测试的核心价值不是完全替代线上实验，而是用极低的成本提前淘汰明显无效的方案，将线上流量留给最有潜力的候选，大幅提升迭代效率。

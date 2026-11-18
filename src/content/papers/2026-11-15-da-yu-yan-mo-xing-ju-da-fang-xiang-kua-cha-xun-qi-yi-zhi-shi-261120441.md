---
title: 'Abstention Direction in Large Language Models: Mechanistic Interpretability
  of Abstention Across Query Ambiguity, Knowledge Limits, and Safety Alignment'
title_zh: 大语言模型拒答方向：跨查询歧义、知识边界与安全对齐的机制可解释性
authors:
- Koki Itai
- Jun Hirako
- Hiroaki Yamagiwa
affiliations:
- SB Intuitions Corp.
arxiv_id: '2611.20441'
url: https://arxiv.org/abs/2611.20441
pdf_url: https://arxiv.org/pdf/2611.20441
published: '2026-11-15'
collected: '2026-11-18'
category: LLM
direction: LLM机制可解释性 · 拒答行为分析
tags:
- Mechanistic Interpretability
- Abstention
- Activation Steering
- LLM Safety
- Query Ambiguity
one_liner: 拓展拒答方向框架至三类拒答场景，验证不同拒答方向存在公共分量
practical_value: '- 可借鉴反事实配对构造方法，为电商导购/客服Agent的三类拒答场景（模糊query、超知识边界咨询、合规违规问题）构建专属拒答方向，提升Agent可靠性

  - 利用中间层激活干预方法，无需全模型微调即可快速调整Agent拒答阈值，适配不同业务场景（如合规场景提拒答率、导购场景降拒答率）

  - 复用不同拒答场景存在公共分量的结论，无需为每个场景单独开发拒答调控模块，降低工程成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM拒答内部表征分析仅聚焦安全对齐场景，未覆盖查询歧义、知识边界两类核心拒答触发场景，无法支撑全局拒答行为的精准调控。

### 方法关键点
1. 针对查询歧义、模型知识边界、安全对齐三类拒答场景，构造同模板、仅拒答触发因子有差异的反事实样本对
2. 计算两类样本平均激活差的归一化向量作为对应场景的拒答方向
3. 通过激活转向实验验证层间干预效果与跨场景迁移性

### 关键结果
- 干预LLM中间层可对三类场景的拒答率实现双向调控
- 不同场景拒答方向存在公共分量，单一场景的激活转向可产生跨场景拒答调控效果

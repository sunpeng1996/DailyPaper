---
title: Hierarchical Group-Conditional Conformal Risk Control for Selective Prediction
  in Language Models
title_zh: 面向大语言模型选择性预测的分层分组条件共形风险控制框架
authors:
- Murilo Salem
- Luísa Böhm
- Daniel Pontes
- Anderson Ferrugem
affiliations:
- Universidade Federal de Pelotas, Brazil
- Centro de Desenvolvimento Tecnológico (CDTec)
arxiv_id: '2607.24562'
url: https://arxiv.org/abs/2607.24562
pdf_url: https://arxiv.org/pdf/2607.24562
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: LLM选择性预测 · 分组风险校准
tags:
- Conformal Risk Control
- Selective Prediction
- LLM Calibration
- Group Fairness
- Post-hoc Processing
one_liner: 提出无重训后处理校准框架HG-CRC，实现LLM选择性预测全分层组的风险同时符合约束
practical_value: '- 电商客服、合规广告生成等高风险LLM落地场景可复用分层分组校准逻辑，按用户分层、query难度、商品品类维度自定义分组结构，避免全局阈值导致小众群体/高难度query错误率超标

  - 无需模型重训的后处理方案可快速上线，仅需数百条标注校准样本即可实现风险约束，适配推荐query生成、营销文案生成等场景的快速迭代需求

  - 流量分布波动场景（如大促期间高难度咨询量突增）下，叶优先回退策略可保证各细分场景错误率不超过预设预算，规避全局阈值的系统性失效风险

  - 可根据分组数量灵活调整Bonferroni校正：浅分层（<10组）场景可关闭校正提升回答率，深分层场景开启校正保证全组风险约束'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有全局共形风险控制（CRC）仅能保证整体平均错误率满足预设预算，在用户异质性强、分组分布偏移的真实部署场景下，会出现部分小众/高难度分组的错误率远超约束的问题，实验显示标准CRC在中等分组分布偏移下违规率最高达47%，无法满足高可靠LLM场景的公平性和可靠性要求。
### 方法关键点
- 提出HG-CRC后处理校准框架，无需模型重训，仅需预留小批量标注校准集即可部署
- 支持用户自定义分层分组结构，对层级内每个节点做独立CRC校准，通过Bonferroni校正实现所有节点的风险同时达标
- 推理时采用叶优先选择策略：优先匹配最细粒度分组的阈值，若细粒度分组无有效阈值则回退到粗粒度节点，无任何有效节点则拒答
### 关键结果
在ARC Challenge、MMLU-Pro两个多选基准上测试3款主流开源LLM，对比全局CRC、平层分组CRC等基线：
- ARC Challenge数据集上，HG-CRC对Qwen3-4B、Llama-3.1-8B实现0%违规率，最差组超额风险（WGER）为0，相比全局CRC违规率从11%降至0，回答率仅损失22~37个百分点
- 分组分布偏移场景下，全局CRC违规率最高达47%，HG-CRC仍保持0违规

高可靠LLM部署场景下，分层分组条件共形校准是兼顾全局效率和细分场景风险约束的低成本落地方案。

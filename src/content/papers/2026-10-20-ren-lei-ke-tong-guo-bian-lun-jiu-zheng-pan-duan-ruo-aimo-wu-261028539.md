---
title: Humans Correct Their Judgments Through Debate, but Weaker AI Models Do Not
title_zh: 人类可通过辩论纠正判断，弱AI模型无法实现同类效果
authors:
- Maria Victoria Carro
- Denise Alejandra Mester
- Facundo Nieto
- Oscar Agustin Stanchi
- Guido Ernesto Bergman
- Giovanni Franco Gabriel Marrafini
- Trinidad Borrell
- Guido Freire
- Joaquin Salvador Machulsky
- Mario Alejandro Leiva
affiliations:
- Università degli Studi di Genova
- Universidad de Buenos Aires
- CONICET
- Inria
- IIIA-CSIC
arxiv_id: '2610.28539'
url: https://arxiv.org/abs/2610.28539
pdf_url: https://arxiv.org/pdf/2610.28539
published: '2026-10-20'
collected: '2026-10-22'
category: MultiAgent
direction: 多智体辩论 · AI可扩展监督
tags:
- Multi-Agent Debate
- Scalable Oversight
- LLM Alignment
- Human-AI Collaboration
- Judgment Correction
one_liner: 实测辩论可显著提升人类法官判断准确率，但对弱LLM无普遍增益，质疑全自动化高风险AI监督可靠性
practical_value: '- 电商/广告合规审核、高风险规则校验等人机协同场景，可引入双Agent对立辩论+人类法官的模式，能将人类判断准确率提升~16pp，效果远优于单Agent咨询的RLHF式监督

  - 多LLM审核陪审团优先采用异构模型配置，同质化同模型面板中错误观点更容易说服正确少数派，会拉低整体判断准确率

  - 多Agent决策的聚合规则优先选置信度加权投票，强制共识的 deliberation 不仅会降低LLM陪审团准确率，还会额外增加推理成本

  - 高风险业务（如电商大额补贴审核、广告投放资质校验）不要使用全LLM辩论监督流程，弱LLM作为法官时辩论无法稳定提升准确率，易触发安全事故'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Scalable Oversight 是超人类AI对齐的核心问题，辩论方案通过双Agent对立论证让法官（人类/弱LLM）判断正确性，但现有研究未明确法官先验信念、多陪审团配置对辩论效果的影响，且人类先验偏差可能被AI利用，全自动化LLM监督的可靠性也缺乏验证。

### 方法关键点
- 构建10个小众科技领域、共100条细分事实对的数据集，确保法官无前置领域知识，平衡设置持有正确/错误先验的 grounded/erroneous 法官分组
- 对比单Agent咨询（RLHF式单方向论证）、单法官辩论、多法官（3/7人）的无共识 deliberation、强制共识、多数投票、置信度加权投票等多种协议
- 分别测试人类法官（N=507）、多款开源/闭源弱LLM法官的效果，额外测试辩论效果的跨子话题泛化性、陪审团多样性的影响

### 关键结果
- 人类法官：单辩论可将准确率从41.3%提升至57.6%（p=0.028），置信度加权投票进一步提升到65.3%，跨子话题泛化无明显准确率损失，单Agent咨询无显著提升
- 弱LLM法官：辩论无普遍增益，多数场景准确率无显著变化甚至下降，多陪审团配置下仅异构模型的7人陪审团有小幅提升，同质化面板中正确少数派放弃正确观点的比例比错误少数派接受正确观点的比例高~8pp，错误观点更容易占上风

### 核心结论
辩论是人类可扩展监督超人类AI的可行路径，但全自动化的LLM辩论监督在高风险场景下不可靠

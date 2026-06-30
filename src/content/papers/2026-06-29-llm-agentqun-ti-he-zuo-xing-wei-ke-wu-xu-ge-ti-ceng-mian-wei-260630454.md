---
title: Collective cooperation without individual fidelity in LLM agents
title_zh: LLM Agent群体合作行为可无需个体层面行为保真
authors:
- Henrique Ferraz de Arruda
- Carlos Gracia Lázaro
- Alberto Aleta
- Yamir Moreno
affiliations:
- ARAID Foundation
- Institute for Biocomputation and Physics of Complex Systems (University of Zaragoza)
- Universidad San Jorge (USJ)
- Department of Theoretical Physics (University of Zaragoza)
arxiv_id: '2606.30454'
url: https://arxiv.org/abs/2606.30454
pdf_url: https://arxiv.org/pdf/2606.30454
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: LLM Agent 群体行为保真度验证
tags:
- LLM Agent
- Multi-Agent
- Behavior Validation
- Prisoner's Dilemma
- Collective Behavior
one_liner: 发现LLM Agent可复现人类群体合作宏观规律，但个体决策机制与人类存在显著偏差
practical_value: '- 做多Agent业务场景仿真（如直播场用户行为、电商大促决策模拟）时，不能仅验证宏观指标匹配，需补充个体决策分布、条件响应规则校验，避免仿真结果不可靠

  - 若多Agent系统出现行为同质化问题，可参考论文引入约20%比例的随机行为Agent，提升整体行为异质性，更贴近真实用户群体特征

  - Agent交互类场景prompt可复用论文技巧：用中性表述替代任务专有名词（如不用「囚徒困境」用颜色选择），避免LLM触发预置知识而非基于当前上下文决策

  - 多Agent系统选型需注意不同LLM的群体行为差异极大，不可直接互换，需先针对业务场景做基准验证再选型'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent 已被广泛应用于社会仿真、群体决策模拟等场景，当前普遍默认只要宏观结果与人类数据对齐即可作为人类行为代理，但缺乏多维度保真度校验，容易导致仿真结论存在系统性偏差，亟需明确不同层级行为匹配的对应关系。
### 方法关键点
- 以已发表的大规模人类网络囚徒困境实验为金标准，完全复用相同的交互协议、收益结构、固定/动态网络拓扑；
- 对比9款覆盖不同参数规模、模型家族、对齐策略的开源LLM，从宏观合作动态、个体行为异质性、条件合作决策规则三个层级校验匹配度；
-  ablation 随机Agent占比，验证引入非策略性行为对提升整体保真度的效果。
### 关键实验结果
基准为人类实验数据与独立伯努利随机决策null模型。核心数据：llama4:16x17b 是所有测试模型中宏观合作率与人类匹配度最高的模型，相关度最高可达0.743；LLM群体的个体合作倾向分布离散度比人类低40%~60%，显著低估人类行为异质性；加入20%比例的随机Agent可将个体分布的Wasserstein距离最多降低30%，短期波动同步率最高提升1倍。
### 核心结论
LLM Agent作为人类行为代理的有效性是分层的，仅宏观指标匹配不足以证明行为保真，必须同时校验个体异质性与底层决策规则。

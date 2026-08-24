---
title: 'No PUN Intended: Plausible Unknown Names for Person-Centred LLM Evaluation'
title_zh: 面向以人为中心LLM评估的可信未知人名构建方案PUN
authors:
- Dimitri Staufer
- David Hartmann
- Ibrahim Baroud
affiliations:
- Technische Universität Berlin
- Weizenbaum Institute for the Networked Society
- Quality & Usability Lab, Technische Universität Berlin
- German Research Center for Artificial Intelligence (DFKI)
arxiv_id: '2608.21206'
url: https://arxiv.org/abs/2608.21206
pdf_url: https://arxiv.org/pdf/2608.21206
published: '2026-08-21'
collected: '2026-08-24'
category: Eval
direction: LLM评估 · 未知人名构建
tags:
- LLM Evaluation
- Privacy Audit
- Factuality Assessment
- Dataset Construction
- Bias Testing
one_liner: 提出PUN协议生成形态可信、无公开人物关联的未知人名，用于LLM事实性、隐私等维度评估
practical_value: '- 做LLM客服、导购Agent的事实性/拒答能力评估时，可直接复用开源的300个PUN未知人名作为基准测试case，降低评估数据构建成本

  - 开展LLM隐私泄露合规测试时，可使用PUN生成的未知人名作为测试变量，避免训练数据记忆干扰测试结果，提升隐私风险检测准确率

  - 生成虚拟用户画像、合成推荐系统训练样本时，可参考PUN的「知识库组件拆分+搜索引擎二次校验」流程，生成无真实对应实体的虚拟身份，规避合规风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM事实性、隐私泄露、偏见、拒答能力等评估场景广泛使用人名作为prompt变量，但人名的公开证据状态不受控时，评估结果会混淆模型记忆、检索、姓名先验、错配人物归因等干扰因素，导致评估结论不可靠。
### 方法关键点
明确未知人名的三大判定标准：符合真实姓名的姓+名结构、无公开索引的全姓名对应人物证据、验证过程中无歧义信号；提出PUN构建验证协议：从Wikidata提取姓/名组件组合生成候选，经联网LLM初筛、受控搜索二次验证两道校验环节。
### 关键结果
204人参与的用户研究显示，生成的人名比对照组更符合真实人名特征，仅3%的案例中受试者能找到对应真实人物证据；已开源300个验证通过的未知人名及对照数据集。

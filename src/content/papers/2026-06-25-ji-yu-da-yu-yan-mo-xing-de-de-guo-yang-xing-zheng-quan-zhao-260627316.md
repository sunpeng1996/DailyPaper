---
title: LLM-Based Examination of Eligibility Criteria from Securities Prospectuses
  at the German Central Bank
title_zh: 基于大语言模型的德国央行证券招股书合格性审查
authors:
- Serhii Hamotskyi
- Akash Kumar Gautam
- Christian Hänig
affiliations:
- Anhalt University of Applied Sciences
arxiv_id: '2606.27316'
url: https://arxiv.org/abs/2606.27316
pdf_url: https://arxiv.org/pdf/2606.27316
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: 大语言模型 · 金融信息抽取与评估
tags:
- Large Language Models
- Information Extraction
- LLM-as-a-Judge
- Financial NLP
one_liner: 首次将LLM用于德国央行证券招股书合格性审查，提出三段式生成式IE流水线与LLM-as-judge评估法
practical_value: '- 生成式IE的「抽取-归一化-解释」三段式拆分，可迁移到电商商品资质审核、广告合规校验场景，解决传统NER难以处理的OCR噪声、多语言混杂、span约束僵化问题

  - 采用LLM-as-judge的价值导向评估替代位置匹配指标，适合商品卖点提取、用户意图识别等语义类抽取任务，评估结果更贴合业务实际需求

  - 高风险审核场景下的保守输出策略（优先控制false acceptance），可复用在电商风控、广告合规等对precision要求高的LLM应用中，通过prompt约束或后处理实现'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**
德国央行承担欧元体系内证券抵押品合格性审核职责，需对照法律与财务标准核验数百页的半结构化招股书，且文档常为德英双语混杂形态，人工审核资源消耗极大、效率低下。传统基于NER的信息抽取方案存在OCR噪声鲁棒性差、语言变体适配难、span提取约束僵化、需为每类标注字段单独制作人工训练数据等痛点，难以适配复杂业务场景。

**方法关键点**
生成式信息提取流水线将任务拆解为抽取、归一化、解释三个阶段，灵活适配噪声文本与跨语言混杂内容，无需为每类字段单独标注训练数据。评估层面采用基于价值的LLM-as-judge方案，从语义维度判断抽取结果的正确性，替代传统基于文本位置匹配的评估指标，更贴合业务实际判断逻辑。

**关键结果**
文档级合格性判断精度最高达91%，系统整体呈现保守运行特性，可最大限度降低false acceptance风险，符合金融场景的高风控要求。

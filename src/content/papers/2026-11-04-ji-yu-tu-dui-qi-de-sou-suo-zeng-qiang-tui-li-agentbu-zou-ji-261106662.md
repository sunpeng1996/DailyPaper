---
title: 'Where Search Agents Go Off the Rails: Graph-Grounded Step-Level Verification'
title_zh: 基于图对齐的搜索增强推理Agent步骤级错误校验框架
authors:
- Hyeseo Jeon
- Seonho Yoo
- Jay-Yoon Lee
affiliations:
- Seoul National University
- Korea University
arxiv_id: '2611.06662'
url: https://arxiv.org/abs/2611.06662
pdf_url: https://arxiv.org/pdf/2611.06662
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent推理校验 · 图结构对齐
tags:
- SearchAgent
- GraphAlignment
- StepVerification
- LLMReasoning
- RAG
one_liner: 无需生成式判别的图对齐框架，实现高召回的搜索Agent步骤级错误校验
practical_value: '- 搭建RAG/搜索Agent校验体系时，可复用「小模型做结构化三元组抽取+规则对齐校验」架构，替代LLM-as-judge方案，在电商商品咨询、虚假宣传检测等高召回要求的场景下，既降低成本又大幅提升错误检出率

  - Q-D-T（问题-证据-推理）三维校验逻辑可直接迁移到多轮推荐Agent过程审计，用于校验用户需求拆解、召回内容匹配、推荐理由生成的一致性，避免推荐理由与商品信息不符的合规风险

  - 离线诊断转在线反馈的方案可直接复用：将校验出的Missing/Unused/Unsupported等状态映射到预设反馈模板，不需要重训底层Agent就能提升推理准确率，适合电商导购、客服Agent的快速迭代'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
搜索增强推理Agent即使输出正确最终答案，也常存在中间步骤无证据支撑、证据误用的问题，现有校验方法要么仅校验推理内在逻辑，要么仅校验证据匹配度，无法同时对齐问题要求、时序累积的检索证据和动态推理过程，召回极低，漏检的错误会传播到后续检索推理环节，最终导致结果不符合预期。

### 方法关键点
- 将问题、检索证据、每步推理都转换为(头实体, 关系, 尾实体)三元组图，问题中的未知答案用ENT占位符，证据图随检索步骤累积，推理图每步单独生成
- 定义三个核心对齐维度：Q-D（问题需求是否有对应证据）、Q-T（推理是否覆盖问题需求）、D-T（推理结论与证据内容是否一致），组合输出6种可落地的诊断状态：冲突、无支撑、已落地、证据未使用、需求未解决、证据缺失
- 仅用LLM做结构化三元组抽取，对齐和诊断全用规则实现，无需生成式判别、无需标准答案，可直接对接现有推理框架无需修改其结构
- 诊断结果可映射到预设反馈模板，在线指导Agent修正下一步推理或检索动作

### 关键实验
在HotpotQA、2WikiMultihopQA、MuSiQue三个多跳QA数据集上，对比Search-R1、ReSearch、ReAct三个推理框架的校验效果，基线采用Self-RAG、IBM-Granite、GPT-4.1-mini等生成式校验器：
- 离线校验召回加权F6值全场景最优，即使是0.5B小模型版本，召回比GPT-4.1-mini最高高37个百分点，F6最高提升36.6个百分点
- 在线反馈场景下，Search-R1在2WikiMultihopQA上EM提升7.6、F1提升7.1
- 0.5B版本单样本耗时仅1.2s，结果稳定性远高于生成式校验器，方差小于0.6

最值得记住的一句话：限制LLM仅做结构化信息抽取、校验逻辑用可解释的规则实现，比直接调用大模型做生成式判别，在高召回要求的校验场景下效果更好、成本更低、可解释性更强

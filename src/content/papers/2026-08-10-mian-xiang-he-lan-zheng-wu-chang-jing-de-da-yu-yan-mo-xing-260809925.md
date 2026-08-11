---
title: 'From Values to Benchmarks: Evaluating Large Language Models for Governmental
  Use in Dutch'
title_zh: 面向荷兰政务场景的大语言模型评估体系与基准测试
authors:
- Laurens Samson
- Iva Gornishka
- Gossa Lô
- Yuki M. Asano
- Sennay Ghebreab
affiliations:
- City of Amsterdam
- University of Amsterdam
- University of Technology Nuremberg
arxiv_id: '2608.09925'
url: https://arxiv.org/abs/2608.09925
pdf_url: https://arxiv.org/pdf/2608.09925
published: '2026-08-10'
collected: '2026-08-11'
category: Eval
direction: LLM场景化评估 · 政务领域
tags:
- LLM Evaluation
- Government LLM
- Benchmark
- Model Selection
- Multilingual LLM
one_liner: 联合荷兰市政专家推出含6维度的政务LLM评估框架，覆盖30+模型并给出选型参考
practical_value: '- 可复用多维度评估框架设计思路，内部LLM选型时除效果外，新增成本、能耗、公平性等业务相关维度，平衡投入与产出

  - factuality与honesty拆分评估的方法可直接迁移到电商导购、客服Agent的效果评测，降低模型幻觉带来的客诉风险

  - 先对齐领域专家需求、再做用户调研的评估指标确认流程，可用于LLM落地前的业务-技术指标对齐，避免评估结果脱离业务实际

  - 可复用「无全优模型、需按业务优先级做trade-off」的选型结论，不用盲目追求大参数模型，匹配业务需求即可'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前政务场景LLM落地缺乏同时对齐公共管理价值、非英语语种适配要求的统一评估框架，无法支撑政务侧合规、可靠的模型选型。
### 方法关键点
联合荷兰阿姆斯特丹市政领域专家，通过顾问委员会研讨、用户调研、公务员聊天bot用户问卷三步，确定factuality、honesty、社会偏见、能耗、成本、训练数据透明度6个核心评估维度，搭建的基准套件覆盖30+多语种及荷兰语专属模型。
### 关键结果数字
- 无单模型在全维度表现最优，效果提升必然伴随更高环境能耗与经济成本，偏见指标与二者无强相关性
- factuality与honesty由完全独立的模型属性决定，高准确率不代表模型会主动承认未知
- 配套发布面向全 stakeholder 的可视化选型工具，覆盖技术人员到政策制定者的全角色使用需求

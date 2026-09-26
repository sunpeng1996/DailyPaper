---
title: The Linear Representation Hypothesis Needs a Group Action
title_zh: 线性表征假设需引入群作用明确定义表征等价标准
authors:
- Louie Hong Yao
- Yuhao Li
- Shengchao Liu
affiliations:
- Independent Researcher
- The Chinese University of Hong Kong
arxiv_id: '2609.27158'
url: https://arxiv.org/abs/2609.27158
pdf_url: https://arxiv.org/pdf/2609.27158
published: '2026-09-21'
collected: '2026-09-26'
category: LLM
direction: 大模型可解释性 · 表征等价性理论
tags:
- Representation_Equivalence
- Linear_Representation_Hypothesis
- Group_Action
- Model_Interpretability
- LLM_Analysis
one_liner: 基于群作用形式化表征等价关系，将线性表征假设细化为按等价性区分的可验证命题系列
practical_value: '- 做LLM表征探针、用户/物品兴趣特征干预时，需先明确表征等价假设，避免不同操作下结论矛盾

  - 跨域/跨模型表征对齐、Semantic ID生成场景下，可基于群作用框架定义统一的等价性度量标准

  - 可复用其审计逻辑，校验现有向量召回、RAG检索、特征探针指标的底层假设一致性'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有线性表征假设（LRH）未明确定义不同表征的等价判定标准，导致不同探针、干预、度量方法看似研究同一表征，实际对应不同隐含假设，所得结论无法泛化到特定训练模型之外。
### 方法关键点
引入群作用形式化框架，将单一LRH拆解为按表征等价性区分的系列命题，同时纳入模型架构带来的天然等价约束，明确区分表征对象、生成流程、待验证属性三个核心维度，统一不同分析方法的假设前提。
### 关键结果
该框架可清晰区分不同度量、读取点、分析阶段的假设差异，已被用于审计常见表征量化指标和近年可解释性分析工作的逻辑一致性，修正了多个过往研究中因等价假设不统一导致的结论偏差。

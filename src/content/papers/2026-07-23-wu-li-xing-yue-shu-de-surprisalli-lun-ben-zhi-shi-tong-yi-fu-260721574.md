---
title: Surprisal Theory is Tautological (without Rational Grounding)
title_zh: 无理性约束的Surprisal理论本质是同义反复
authors:
- Ryan Cotterell
affiliations:
- ETH Zürich
arxiv_id: '2607.21574'
url: https://arxiv.org/abs/2607.21574
pdf_url: https://arxiv.org/pdf/2607.21574
published: '2026-07-23'
collected: '2026-07-26'
category: LLM
direction: 大语言模型认知理论 · 可证伪性分析
tags:
- Surprisal
- Psycholinguistics
- Falsifiability
- Language Model
- Cognitive Constraint
one_liner: 证明无额外约束的Surprisal理论为同义反复，需引入认知理性约束才具备可证伪性
practical_value: '- 用Surprisal做用户query理解成本、文案可读性预估时，不能直接用通用语料训练的LM输出，需引入业务场景用户的认知约束（如领域知识、记忆局限）校准，否则指标无实际解释性

  - 做LLM生成商品文案、Agent对话回复的用户接受度评估时，不可盲目提升预训练语料拟合度，需结合目标人群认知特征调整LM约束，避免出现「困惑度低但用户理解成本高」的反效果

  - 基于Surprisal做用户行为建模时，需提前固定LM的约束条件，不能为拟合效果随意调整LM，否则会陷入同义反复陷阱，模型泛化性为0'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
过往二十年心理语言学研究默认Surprisal理论有效，即人类处理上下文语言单元的难度是其在某LM下Surprisal的仿射函数，且普遍认为提升LM语料拟合度就能更好预测人类行为，但近年实证发现拟合更好的LM反而可能预测效果更差，理论基础存疑。
### 方法关键点
通过数学推导证明：在温和技术条件下，对任意非负的上下文语言单元难度度量，都存在对应的LM使得其Surprisal与该度量呈仿射关系，即无约束的Surprisal理论本质是同义反复，无法做出可证伪的预测。
### 关键结果
1. 推翻了「LM语料拟合度越高，Surprisal对人类语言处理难度预测越准」的默认假设；
2. 明确要让Surprisal理论有效，必须引入不依赖待解释行为数据的理性约束，如理解者的记忆限制、处理目标等认知先验。

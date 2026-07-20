---
title: 'From Plausible to Actionable: A Position on LLM Self-Explanations'
title_zh: 从看似可信到可落地：大语言模型自解释的立场研究
authors:
- Elize Herrewijnen
- Benedetta Muscato
- Gizem Gezici
- Fosca Giannotti
affiliations:
- University of Utrecht
- National Police Lab AI, Netherlands Police
- Scuola Normale Superiore
- University of Pisa
arxiv_id: '2607.15957'
url: https://arxiv.org/abs/2607.15957
pdf_url: https://arxiv.org/pdf/2607.15957
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: LLM可解释性 · 自解释评估体系
tags:
- LLM
- XAI
- Self-Explanation
- Evaluation
- Actionability
one_liner: 明确LLM自解释三重属性，提出评估需新增可行动性维度并配套评估指引
practical_value: '- 对接入LLM的推荐/Agent系统做自解释评估时，可参考双维度校验方法：先验证plausibility（解释是否符合用户常识），再对高风险场景（比如金融推荐、审核决策）额外校验faithfulness（是否匹配模型真实推理逻辑），避免被看似合理的错误解释误导。

  - 面向C端用户的推荐理由生成、面向运营的Agent决策复盘等低风险场景，不用过度纠结解释是否完全对齐模型内部逻辑，优先保障解释的actionability（比如直接告知用户「推荐该商品是因为凑单可减20元」）即可。

  - 做LLM应用的解释功能评估时，可按不同 stakeholder（用户/运营/审核）的需求设置差异化评估标准，不用统一追求高faithfulness，可大幅降低可解释性模块的研发成本。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统XAI方法适配大参数LLM时算力成本过高，LLM自解释作为低成本可解释方案被广泛应用，但现有评估仅关注表面合理性，未匹配落地场景的决策支撑需求。
### 方法关键点
1. 定义LLM自解释三重核心属性：高plausibility（可信度）、faithfulness（忠实度）存疑、高actionability（可行动性）
2. 梳理标准自解释评估协议的局限性，给出可信度与忠实度的实操评估指引
3. 提出评估需新增可行动性维度，针对不同利益相关方设置差异化的解释评估标准
### 关键结论
无需过度追求自解释与LLM内部推理逻辑的完全对齐，只要可行动性达标即可支撑多数场景的决策需求，可大幅降低LLM可解释性的落地成本。

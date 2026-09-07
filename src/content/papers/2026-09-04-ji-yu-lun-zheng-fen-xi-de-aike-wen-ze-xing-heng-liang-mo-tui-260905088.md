---
title: 'Measuring AI Accountability Through Argumentation Analysis: Can Model Reasoning
  Withstand Scrutiny?'
title_zh: 基于论证分析的AI可问责性衡量：模型推理能否经得住审查
authors:
- Daan R. Henselmans
- Derck W. E. Prinzhorn
- Arno Libert
affiliations:
- Aithos Research Foundation
arxiv_id: '2609.05088'
url: https://arxiv.org/abs/2609.05088
pdf_url: https://arxiv.org/pdf/2609.05088
published: '2026-09-04'
collected: '2026-09-07'
category: Eval
direction: LLM可问责性评估 · 歧义场景论证分析
tags:
- LLM Evaluation
- AI Accountability
- Argumentation Analysis
- Moral Reasoning
- Faithful Reasoning
one_liner: 提出基于论证理论的四阶段辩证协议，无ground truth时评估高歧义场景下LLM推理可辩护性
practical_value: '- 电商/Agent高歧义决策（如售后纠纷判责、推荐伦理判定）评估可复用该无ground truth的四阶段质询框架，替代传统依赖标注的评估方案

  - 校验LLM推理一致性时，可借鉴Govier论证效度三标准（前提真实性、相关性、充分性），快速定位推理缺陷，降低人工审核成本

  - 敏感场景LLM对齐（如信贷审核、内容合规）可接入该协议，自动拦截自相矛盾、虚假前提等不可辩护的风险输出'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AI监管评估依赖ground truth验证，无法适配伦理判断等高歧义场景下合理行为边界模糊的问题，传统评估刻意回避现实歧义性。
### 方法关键点
基于Walton论证模式理论和Govier论证效度标准，搭建四阶段辩证评估协议，通过对模型决策的辩护回答进行质询，评估其推理结构质量；覆盖决策前置推理与事后辩护两类输出，适配不同推理框架，不局限于多选题范式。
### 关键结果
9个前沿大模型、200个高歧义道德决策样本共6778个标注单元验证，标注二分类一致性达89.6%；所有模型各维度得分均高于最低标准，失败集中在前提合理性、论证充分性维度，与认知模糊度相关而非论证长度；所有模型各维度下前置推理的可辩护性均优于事后辩护，至少20%的case中事后辩护的论证逻辑与前置推理不一致。

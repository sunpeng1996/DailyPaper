---
title: 'TACT: A Pragmatic Approach to Qualitative Analysis with an AI Council'
title_zh: TACT：基于AI委员会的定性文本分析实用框架
authors:
- Rudrajit Choudhuri
- Christian Bird
- Carmen Badea
- Anita Sarma
affiliations:
- Oregon State University
- Microsoft Research
arxiv_id: '2611.05702'
url: https://arxiv.org/abs/2611.05702
pdf_url: https://arxiv.org/pdf/2611.05702
published: '2026-11-03'
collected: '2026-11-05'
category: MultiAgent
direction: 多智体异构协作 定性文本分析
tags:
- MultiAgent
- LLM
- AI Council
- Thematic Analysis
- Qualitative Analysis
one_liner: 提出异构多Agent协作框架TACT，实现低成本高可控的大规模定性文本分析
practical_value: '- 异构多Agent角色分工（独立分析师/对抗校验者/仲裁者）+ 多数投票的架构，可直接复用在电商用户评论、客服工单、搜索Query的主题挖掘场景，降低单模型
  hallucination 风险

  - 人类先盲标注10%样本再校验模型输出的流程，可迁移到所有LLM辅助标注任务，避免模型输出的锚定效应，大幅提升标注准确率

  - 引用内容与原文匹配的确定性校验逻辑，可复用到RAG、生成式推荐的证据校验环节，确保生成内容的可解释性和真实性

  - 成本优先场景优先使用TACT-Lite（3个异构模型独立标注+多数投票），预算充足时优先加发现阶段的对抗Agent，性价比最高'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
大规模定性文本（用户反馈、客服工单、社区讨论等）的人工主题分析成本随数据量线性增长，单LLM直接分析存在结果不可控、hallucination无溯源性的问题，团队往往只能在放弃分析和接受低可信度结果中二选一，缺乏兼顾效率、可控性、准确性的落地方案。

### 方法关键点
- 双版本设计：TACT-Lite为核心流程，TACT-Full额外增加跨模型家族的对抗Agent（负责critique其他模型输出）和不确定性打分模型，标记高风险标注结果
- 5阶段可控流程：①3个异构模型家族的Agent独立挖掘候选编码，确定性程序校验所有引用片段与原文完全匹配；②仲裁模型合并候选编码生成初始编码本；③人类先盲标注10%样本，再校验修正编码本，避免锚定效应；④3个独立编码Agent基于确认后的编码本批量标注，每个结果附推理依据；⑤多数投票生成最终标注，自动计算多Agent一致性指标Krippendorff's α
- 全程可溯源：所有编码均可追溯到原文对应片段和决策主体（模型/人类），人类保留所有解释权

### 关键结果
基于256条Stack Overflow公开标注数据集验证，对比单GPT-5.6 baseline：TACT-Lite候选编码本F1 0.75，最终标注F1 0.71，与人类标注Cohen's κ 0.79，每100条成本13.77美元；TACT-Full候选编码本F1 0.77，最终标注F1 0.72，与人类标注Cohen's κ 0.85，每100条成本33.59美元，两个版本效果均显著优于单模型baseline（F1 0.65）。

### 核心结论
异构多Agent的高一致性仅能证明标注稳定性，不能证明正确性，必须结合人类盲标注的held-out样本做有效性校验。

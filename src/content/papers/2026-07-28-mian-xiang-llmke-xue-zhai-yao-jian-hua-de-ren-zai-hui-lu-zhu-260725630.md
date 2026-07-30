---
title: A Human-in-the-Loop Corpus for LLM-Based Simplification of Scientific Summaries
title_zh: 面向LLM科学摘要简化的人在回路标注语料库
authors:
- Kyuri Im
- Michael Färber
affiliations:
- ScaDS.AI
- Technische Universität Dresden
arxiv_id: '2607.25630'
url: https://arxiv.org/abs/2607.25630
pdf_url: https://arxiv.org/pdf/2607.25630
published: '2026-07-28'
collected: '2026-07-30'
category: Eval
direction: LLM文本简化 · 人在回路标注
tags:
- Human-in-the-Loop
- Text Simplification
- Corpus Construction
- LLM Evaluation
- Scientific Communication
one_liner: 提出两阶段人在回路标注流程，发布科学摘要LLM简化标注语料及配套评测结果
practical_value: '- 商品详情页、平台规则类用户告知文案的LLM简化场景可复用两阶段人在回路标注流程：先由普通用户反馈难理解片段，再由业务专家修订标准参考文案，平衡易懂性和信息准确性

  - 跨领域专业商品（如数码、医疗、美妆）介绍文案生成优化可参考核心结论：必须保留核心专业术语，不得弱化产品功效、服务承诺类核心论断强度，避免误导用户

  - 构建文案生成类模型的训练/评测数据集时，可复用「LLM生成baseline→普通用户标注偏好→专家修订golden样本」的流水线，降低标注成本同时提升数据集质量'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：跨学科研究快速发展，但专业论文摘要的领域壁垒高，非本领域研究者很难读懂；现有LLM科学文本简化方案容易出现幻觉、丢失核心信息、弱化论断强度等问题，缺乏高质量标注语料支撑模型优化和标准化评测。
**方法关键点**：基于SciSummNet源语料，设计两阶段人在回路标注流程：1）先用GPT-4o-mini生成基准简化版本，邀请计算机领域外的STEM研究者标注难理解片段，对比原摘要和LLM生成版的可理解性、自然度、简洁度；2）由计算机领域专家基于第一阶段用户反馈，修订生成标准参考简化文本。
**关键结果**：第一阶段用户反馈明确偏好LLM生成版本，其可理解性、简洁度显著优于原专家摘要；第二阶段专家修订分析验证了保留领域术语、维持科学论断强度是文本简化的核心要求，最终开源的语料可直接支撑简化系统的训练和基准评测。

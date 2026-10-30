---
title: 'Rubricon: Automated Rubric Generation and Refinement for LLM Evaluation and
  Training'
title_zh: Rubricon：面向LLM评估与训练的自动评分规则生成优化框架
authors:
- Ulyana Tkachenko
- Hui Wen Goh
- Guram Gogia
- Jonas Mueller
affiliations:
- Handshake AI
arxiv_id: '2610.38220'
url: https://arxiv.org/abs/2610.38220
pdf_url: https://arxiv.org/pdf/2610.38220
published: '2026-10-28'
collected: '2026-10-30'
category: Eval
direction: LLM评估 · 自动评分规则生成
tags:
- Rubric Generation
- LLM Evaluation
- Reward Modeling
- RLHF
- Synthetic Annotation
- LLM Alignment
one_liner: 无需人工标注或模型训练的三阶段rubric生成管道，较现有SOTA对齐专家评分高9%
practical_value: '- 做生成式推荐/Agent效果评估时，可复用Generate-and-Select→Add→Prune三阶段流程自动生成评测规则，无需人工从零搭建评估体系，大幅降低标注成本

  - 筛选有效评估维度时，可复用strong-weak edge设计：通过强弱模型的响应通过率差过滤噪声/反直觉评估项，提升评测结果的判别性和一致性

  - 做LLM对齐的RL训练时，可复用Rubric生成的结构化reward信号，比粗粒度人工偏好更稳定，实验验证可提升4.5%的下游任务效果

  - 做电商客服/商品文案生成的自动质检时，可复用Negative Probing+Completeness Probing的对抗探测方法，覆盖易漏判的bad case维度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
开放域LLM任务的人工编写rubric成本极高（医疗/金融场景需数百专家投入），直接让LLM生成的rubric普遍存在判别性弱、易误判劣质响应、无法适配未来更强模型评估的问题，现有方案大多依赖人工偏好标注或生成模型训练，落地成本高。

### 方法关键点
- 三阶段无监督管道：1）Generate-and-Select：生成5个候选rubric，选择强弱模型响应通过率差（strong-weak edge）最高的初始版本；2）Add：通过gap补全、prompt覆盖、负例探测、完整性探测4个步骤扩展覆盖度，补充遗漏的缺陷评估维度；3）Prune：过滤强-弱边低于-0.1的反向规则、可被劣质响应蒙混的无效规则，支持多轮迭代优化
- 无需人工标注、无需训练专属rubric生成模型，可适配任意基座LLM，生成的规则自带Critical/Major/Minor三级权重，可直接用于响应打分或RL奖励计算

### 关键实验
在覆盖专业、消费、医疗、通用场景的5个基准上对比RRDWU、Agentic生成、OpenRubrics、QSRG等SOTA方案：与专家rubric打分排名的Spearman相关系数平均达0.428，较最强基线高9%；人类偏好选择性准确率达59.8%，较次优方案高0.5个百分点；用其生成的rubric做奖励训练Qwen3.5-9B，在HealthBench上较基线奖励训练的模型效果高4.5%。

**最值得记住的一句话**：自动评分规则优化不要只依赖LLM自评估，结合实际强弱模型的响应通过率信号做grounded的筛选迭代，效果优于纯Agentic生成且成本更低。

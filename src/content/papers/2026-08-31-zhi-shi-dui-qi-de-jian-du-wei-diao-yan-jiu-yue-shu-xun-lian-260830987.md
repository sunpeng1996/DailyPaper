---
title: 'Stick to What You Know: A Study of Knowledge-Aligned Supervised Fine-Tuning'
title_zh: 知识对齐的监督微调研究：约束训练目标到基座已知知识范围
authors:
- Arthur Becker
- Jakob Kemmler
- David Thulke
- Christine Schäfer
- Christian Dugast
- Hermann Ney
affiliations:
- AppTek GmbH
- F-Bureaucracy UG
- RWTH Aachen University
arxiv_id: '2608.30987'
url: https://arxiv.org/abs/2608.30987
pdf_url: https://arxiv.org/pdf/2608.30987
published: '2026-08-31'
collected: '2026-09-01'
category: Training
direction: LLM训练 · 知识对齐SFT
tags:
- SFT
- Hallucination Mitigation
- Knowledge Alignment
- Factuality
- LLM Training
one_liner: 提出两种知识对齐SFT新方法，Recall Rewrite可大幅降低幻觉且保留通用能力
practical_value: '- 做电商/推荐场景LLM SFT训练时，可参考Recall Rewrite思路，将训练数据的事实类claim拆解，用QA probing验证基座是否已掌握，过滤超纲内容，避免SFT引入商品/活动相关的事实幻觉

  - 生成式推荐、智能客服等高准确性要求场景，可通过调整训练集中known claim占比，灵活平衡回复的事实准确率和信息量，无需100%对齐即可获得较优收益

  - 优化Agent拒答策略时，可复用Recall Rewrite的多轮QA探测方法，识别基座知识边界，提升对未知商品规则、活动信息等问题的拒答准确率

  - RAG+LLM的电商问答/推荐系统中，SFT阶段仅训练回复格式、话术逻辑，不要注入新事实知识，避免和RAG召回内容冲突引发幻觉'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
SFT是基座LLM转为指令跟随模型的核心步骤，但如果训练目标包含基座未稳定掌握的事实知识，会强制模型生成超出知识边界的内容，是事实性幻觉的核心诱因之一。现有知识对齐SFT方法要么直接用基座生成内容作为训练目标（易带入基座原生幻觉），要么依赖token级置信度过滤（受表述影响大、准确率低），缺少统一框架下的效果对比和更优的对齐方案。

### 方法关键点
- 统一知识对齐SFT框架：将SFT训练目标的所有内容拆解为原子claim，区分知识依赖类（需基座参数知识支撑）和非知识依赖类（上下文、主观、推理类），仅保留基座已掌握的知识依赖类claim，构造对齐后的训练集D*
- 提出两种新对齐方法：①Evidence Rewrite：对基座生成的回复做事实校验，仅保留外部证据支持的claim后重写为流畅回复；②Recall Rewrite：对每个知识依赖类claim生成多个探测问题，采样基座多次回复做蕴含校验，只有能被基座稳定召回的claim才保留
- 对齐过程中完整保留非知识类内容（回复结构、话术风格、推理逻辑），避免破坏SFT的指令跟随能力

### 关键结果
基于Qwen3 4B、OLMo3 7B基座，在OASST1数据集训练，对比标准SFT、FLAME、UNITcut等基线：
- Recall Rewrite在WildHalu数据集FActScore达84.1，较标准SFT提升9.7分，非拒答回复的事实支持率达84.2%；在Biography数据集FActScore达76.4，较标准SFT提升42.3分
- 所有知识对齐SFT方法的通用能力（代码、数学、指令跟随）与标准SFT无显著差异，平均得分仅低0.9分
- 训练集中已知claim占比越高，幻觉率越低，但拒答率越高，可按需调整平衡事实准确率和信息量

> 最值得记住的结论：SFT阶段不适合注入新知识，不仅效率极低还会引入幻觉，事实知识应交给预训练或RAG，SFT只需聚焦训练回复范式、知识边界识别能力即可

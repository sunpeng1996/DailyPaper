---
title: Where Do LLM Ensemble Gains Come From? Decomposing Candidate Value, Diversity,
  and Aggregation
title_zh: LLM集成增益来源分解：候选价值、多样性与聚合效应拆分
authors:
- Donghwan Kim
affiliations:
- Independent Researcher
arxiv_id: '2610.18786'
url: https://arxiv.org/abs/2610.18786
pdf_url: https://arxiv.org/pdf/2610.18786
published: '2026-10-13'
collected: '2026-10-15'
category: LLM
direction: LLM集成 · 增益归因与评估
tags:
- LLM Ensemble
- Gain Decomposition
- Evaluation Baseline
- Aggregation
- Diversity
- RAG
one_liner: 通过4组匹配对照实验拆解LLM集成增益构成，证明增益归因高度依赖所选基线
practical_value: '- 做多Agent/多模型生成结果聚合（如电商文案选优、用户咨询应答）时，不要仅对比重复候选基线的增益，需同时对齐单候选插槽基线，避免高估多样性带来的实际收益

  - 采用RAG+多候选聚合的商品问答/售后方案时，若多候选效果不如直接生成，可尝试将原始检索证据与候选结果同时喂给聚合器，FRAMES任务中该操作可将精度从47.2%提升至65.6%

  - 集成方案选型必须评估整体候选增益CIV（多候选vs无候选直接生成），不要仅看多样性相关DSV指标，避免出现'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM集成研究通常仅基于单一基线报告增益，无法区分新增候选价值、多样性、聚合器行为的各自贡献，甚至会出现「多样性增益为正但整体效果不如直接生成」的矛盾结论，亟需可解释的增益拆解框架指导工程选型。

### 方法关键点
- 设计4组完全匹配的聚合对照条件：Direct（无候选直接生成）、Single-slot（k个插槽仅1个填候选其余为空）、Duplicate（k个插槽重复同一个候选）、Multi-candidate（k个独立生成的候选）
- 定义代数可拆解的指标体系：整体候选增益`CIV = 多候选精度 - 直接生成精度`；多样性增益分两类`DSV_slot`（多候选vs单插槽）、`DSV_dup`（多候选vs重复候选）；重复间隙`Rep = 重复候选精度 - 单插槽精度`，满足恒等式`CIV = DSV + CCV`（候选上下文增益）、`DSV_dup = DSV_slot - Rep`
- 严格控制变量：所有聚合条件使用相同提示模板，仅插槽内容存在差异，排除提示干扰

### 关键实验结果
- 数据集覆盖MultiHopRAG（n=100）、FRAMES（n=200）两类主流任务
- MultiHopRAG模型多样性场景下，`DSV_dup`达+9.3pp但`DSV_slot`仅+1pp，`Rep`为-8.33pp，两类基线的多样性增益结论完全相反
- FRAMES增强候选集实验中，`Rep`从-6.33pp变为+3.33pp，符号发生反转，证明重复候选的影响无统一规律
- 证据聚合场景下，将原始检索证据与候选共同输入聚合器，FRAMES精度从47.2%提升至65.6%，基本抹平候选引入的信息损失

**最值得记住的一句话**：LLM集成的多样性增益没有统一标准答案，所有增益报告必须明确说明对应的基线选择，才能指导实际工程选型。

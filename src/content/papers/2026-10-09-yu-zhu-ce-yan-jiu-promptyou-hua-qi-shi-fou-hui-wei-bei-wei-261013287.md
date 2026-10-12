---
title: Do Prompt Optimizers Break Requirements They Are Not Scored On? A Preregistered
  Study
title_zh: 预注册研究：Prompt优化器是否会违背未纳入评分的要求
authors:
- Sangdo Han
- Moonsoo Kim
affiliations:
- CEO Business School
arxiv_id: '2610.13287'
url: https://arxiv.org/abs/2610.13287
pdf_url: https://arxiv.org/pdf/2610.13287
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM Prompt优化 鲁棒性评估
tags:
- Prompt Optimization
- LLM Evaluation
- Constrained Generation
- Output Parsing
- Single-objective Optimization
one_liner: 揭示单目标Prompt优化的未评分要求违规多源于输出截断，放宽token限制即可大幅改善
practical_value: '- 线上使用Prompt优化器时，除核心业务指标（如推荐准确率、文案点击率）外，必须新增输出可解析率、截断率等非功能指标监控，避免仅看核心指标导致大量不可用输出

  - 对结构化输出要求高的场景（如Agent工具调用参数、推荐卡片JSON解析），Prompt优化时要预留足够输出token上限，200token下HotpotQA任务解析失败率最高达47%，放宽到1024token即可完全消除

  - 简单的零回归要求选择门会完全抵消Prompt优化的效果收益，工程上可采用软约束：把解析率、格式合规率加权进优化目标，而非直接全量过滤候选

  - 不要默认优化后的Prompt保留原要求就不会违规，优化器可能引导模型先输出推理内容再输出结构化结果，需要后处理兼容前置推理文本的解析逻辑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有单目标Prompt优化器仅针对核心任务指标（如Exact Match、准确率）优化，完全忽略Prompt中约定的未被纳入评分的输出要求（如格式、引用、拒答规则），从业者仅监控核心指标时会漏过大量无效输出，目前缺乏对该问题的系统性量化研究。

### 方法关键点
- 预设研究假设、指标定义、统计规则后开展实验，针对3类主流Prompt优化器（GEPA、MIPROv2、TextGrad）在3个公开任务（HotpotQA、SQuAD 2.0、IFEval）上测试
- 初始Prompt包含4类明确要求：JSON格式输出、正确引用来源、无答案时拒答、答案长度≤20词，仅将EM作为优化的唯一目标指标
- 定义净回归率=优化后新增违规数-修复违规数，拆分解析失败类违规与内容类违规，对比200token与1024token输出上限的效果差异

### 关键结果
- 200token输出上限下，HotpotQA任务EM提升21~34个点的同时，引用有效性净回归率达10.7~41.6个点，其中98.4%的新增违规是输出截断导致的JSON解析失败
- 可解析的输出中，所有内容类要求的净回归率均≤3个点；输出上限放宽到1024token后，解析失败率降为0，内容类净回归率<1个点，EM进一步提升8.6~23.3个点
- 两类简单防护门均未达预设标准：零回归选择门完全丢失优化收益，in-loop约束门使EM下降6~14个点

### 核心结论
单目标Prompt优化的非功能违规大多不是内容质量下降，而是输出形态变化与截断的共同作用，给足输出token并做好兼容后处理即可兼顾收益与合规。

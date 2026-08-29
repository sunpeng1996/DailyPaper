---
title: 'Evaluating human and LLM screening workflows in a conceptually complex scoping
  review: Recall--workload trade-offs and run-to-run consistency'
title_zh: 复杂领域综述场景下人类与LLM筛选工作流评估：召回-工作量权衡与一致性
authors:
- Nikol Figalová
- Lynn Huestegge
- Anne Böckler-Raettig
affiliations:
- Institute of Psychology, Julius-Maximilians-Universität Würzburg, Germany
arxiv_id: '2608.26885'
url: https://arxiv.org/abs/2608.26885
pdf_url: https://arxiv.org/pdf/2608.26885
published: '2026-08-27'
collected: '2026-08-29'
category: Eval
direction: LLM工作流评估 · 分类召回率权衡
tags:
- LLM Evaluation
- Workflow Optimization
- Recall Trade-off
- Batch Processing
- Consistency Assessment
one_liner: 对比复杂分类任务下人类与不同配置LLM工作流的召回、工作量、运行稳定性差异
practical_value: '- 高召回要求的分类任务（如合规审核、负样本过滤）不要只看模型选型，要优先验证batch处理等工作流配置的实际效果，避免单独换模型提效的误区

  - 多轮LLM分类任务可复用结论：同配置重复运行仍有10%左右不一致，高风险场景需配置多次校验+人工复核链路，不能完全依赖LLM自动排除

  - 批量处理相比全量一次性输入能提升2-3%的召回率，电商/广告素材审核、候选集过滤场景可优先采用分batch的处理配置'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
证据合成等复杂分类场景中LLM筛选的漏判会直接丢失有效样本，现有评估多聚焦模型本身，缺乏对完整工作流的对比验证。
### 方法关键点
在复杂领域综述筛选场景下，1131条记录分别由2种人类工作流、7种不同模型/配置的LLM工作流（含1组同配置重复运行）处理，对比召回率、保留工作量、运行一致性等指标，基准为316条已验证的合格记录。
### 关键结果数字
人类工作流与GPT-5.4 file-batch处理的性价比最优，保留42.2-45%记录的同时召回率达82.3-82.9%；Gemini 3.1 file-batch召回最高83.9%但需保留56.7%的记录；同配置GPT-5.4重复运行仅91.7%的结果一致，漏判29条仅单次识别的合格样本；batch处理比一次性输入的召回表现更优。

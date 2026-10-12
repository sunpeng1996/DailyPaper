---
title: 'Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing'
title_zh: 相同查询不同结果：语义查询处理的跨运行方差研究
authors:
- Oktie Hassanzadeh
- Dharmashankar Subramanian
affiliations:
- IBM
arxiv_id: '2610.13823'
url: https://arxiv.org/abs/2610.13823
pdf_url: https://arxiv.org/pdf/2610.13823
published: '2026-10-09'
collected: '2026-10-12'
category: Eval
direction: 语义查询 · LLM输出稳定性评测
tags:
- semantic_query_processing
- LLM_nondeterminism
- benchmark_reproducibility
- temperature_0
- query_optimization
one_liner: 量化温度0下语义查询的跨运行方差，揭示查询计划放大效应并给出落地优化指引
practical_value: '- 电商搜索/推荐的LLM query理解、语义召回模块不能默认温度0输出稳定，高敏感场景（如营销query召回、合规审核）可基于单轮请求的决策margin（logprob差）或推理长度识别Top20%易变样本，仅对这部分做3次投票校验，能获得64%的全量投票收益，成本仅提升40%

  - 涉及多步语义算子（如多意图拆分、跨域召回join、排序聚合）的LLM pipeline，波动会被指数级放大，可通过缓存稳定算子输出、对topK结果加LIMIT截断降低波动对业务的影响

  - 做LLM相关算法效果评测时，单次跑批结果不可信，小样本/点查类评测至少跑5次以上取均值，系统选型对比需做显著性校验，避免方差导致的误判'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有语义查询引擎、LLM驱动的搜索推荐语义处理模块均默认温度0下LLM输出确定，行业基准也仅用少数几次运行结果做系统对比。但LLM推理端的浮点计算误差、服务部署差异、动态负载都会引入非确定性，这种波动对上层业务结果、算法选型结论的影响此前未被量化，易导致业务效果不稳定、评测误判。
### 方法关键点
- 提出可能世界模型，解耦单item级输出方差与上层查询结果的可复现性，量化不同算子（全量输出、COUNT、LIMIT、JOIN等）的波动放大系数
- 固定prompt、查询计划、温度0，复现SemBench、LRO-Bench、UDA-Bench 3个主流语义查询基准的全流程，累计记录120万次LLM调用日志，对齐原生评测逻辑
- 从item级算子波动、查询级结果波动、评测结论稳定性三层归因，验证投票、选择性重跑等缓解方案的性价比
### 关键结果
- 温度0下，5次运行的item级输出波动范围为0.07%~10.2%，24分类提取任务波动达24%，GPT-4o、Claude Sonnet 5等商用模型也存在同等量级波动
- 波动随算子复杂度指数级放大：UDA-Bench仅4%的提取值波动会导致67%的SQL查询结果不同；SemBench 21%的文本查询质量跨运行波动超过0.1，16/28的算子选型推荐结论无法通过单次运行验证
- 全量3次投票仅能降低36%的波动，基于单轮推理长度的选择性重跑，仅对20%高波动样本重跑即可获得64%的全量投票收益，成本仅为全量投票的66%

**最值得记住的一句话**：温度0不代表LLM输出确定，多步LLM语义pipeline必须做波动校验，算法评测至少重复5次以上才能避免方差干扰。

---
title: 'TRACES: A Benchmark for Epistemic Reliability in Scientific Reasoning by LLMs'
title_zh: TRACES：面向大模型科学推理认知可靠性的基准测试
authors:
- Valentin Rodionov
- Shamil Assylbekov
affiliations:
- Case Western Reserve University
- Intellicat
arxiv_id: '2608.11415'
url: https://arxiv.org/abs/2608.11415
pdf_url: https://arxiv.org/pdf/2608.11415
published: '2026-08-11'
collected: '2026-08-13'
category: Eval
direction: 大语言模型认知可靠性评估
tags:
- Benchmark
- Epistemic Reliability
- LLM Evaluation
- Scientific Reasoning
- Guardrail
one_liner: 推出TRACES基准测评LLM识别不可靠科学文献的能力，验证现有模型认知可靠性普遍不足
practical_value: '- 做垂域（如商品虚假宣传识别、资质审核）Agent时，可借鉴「问题预设+场景请求」的探针构造方法，测试模型对虚假前提的识别能力

  - 垂域LLM guardrail设计可参考IFR-a/IFR-i两类评分逻辑，区分直接拒答、边响应边提示风险的两类行为，优化风控阈值

  - 业务RAG做源可信度校验时，可复用该基准覆盖的5类虚假内容识别框架，降低错误内容召回率'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前LLM被广泛应用于无下游校验的科学工作流Agent场景，但现有评估基准仅针对有已知答案的事实性问题，缺乏对模型区分可靠/不可靠科学文献能力的直接测评。

### 方法关键点
构建包含42篇撤稿、欺诈、伪科学论文的探针语料，覆盖伪造观测、伪物理机制、伪科学前提、合法性搭桥、 cargo-cult实验5类主张；设计IFR-a（直接拒绝错误前提得分）、IFR-i（响应时识别不可靠得分）、EDI（专业细节复现深度）三类量化指标，开展单轮问答测评。

### 关键结果
30款模型10次重复测试的聚合IFR-a为0.93±0.004、IFR-i为0.809±0.009；95%非空响应会采纳不合理前提，所有模型的Agent类探针失败率超71%，22款模型失败率超90%，拒答仅集中在高知名度问题，本质是主题触发的安全行为而非可靠的认知能力。

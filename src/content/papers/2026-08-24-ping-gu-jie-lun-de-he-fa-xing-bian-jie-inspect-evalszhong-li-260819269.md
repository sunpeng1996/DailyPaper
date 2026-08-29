---
title: What Does an Evaluation License? A Commit-Bound Census of Claim-Relative Inference
  in Inspect Evals
title_zh: 评估结论的合法性边界：Inspect Evals中主张关联推理的提交绑定普查
authors:
- Xi Qin
affiliations:
- Wuhan University
arxiv_id: '2608.19269'
url: https://arxiv.org/abs/2608.19269
pdf_url: https://arxiv.org/pdf/2608.19269
published: '2026-08-24'
collected: '2026-08-29'
category: Eval
direction: 算法评估 · 结论可复现性校验
tags:
- Evaluation
- Reproducibility
- Claim Inference
- Benchmark Audit
- Deterministic Inference
one_liner: 形式化评估主张复现的推理层框架，普查发现88.7%的Inspect Evals单元无法完成确定性推理
practical_value: '- 做RecSys/LLM4Rec效果评估时，需额外固化历史数据集、评估语义规则、对应claim的绑定关系，避免复现偏差

  - 算法迭代AB实验结论归档需绑定代码commit+全链路评估配置，避免后续回溯时因历史证据缺失导致结论无效

  - 跨团队共享的基准评估集需配套主张复现校验层，可快速定位评估结论不稳定的根因是配置问题还是算法本身'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有评估工件仅定义前向计算流程（任务、打分器、指标），未绑定主张复现所需的历史证据与可选语义，导致报告的指标无法直接支撑对应结论的有效性。
### 方法关键点
形式化主张复现层的四要素：冻结基础数据集D、语义接地集合F、主张查询q、可识别结果集；对固定提交下124个符合要求的Inspect Evals单元做全量普查，按终止类型分类判定主张的可推导性。
### 关键结果数字
110个（占比88.7%）单元因历史证据或语义接地缺失，无法完成确定性推理；可正常执行的单元中，精确值、优胜者、全排序、两两关系需按主张解析类型及原始/评审集合拆分，优胜者结论的稳定性显著高于全排序结论。

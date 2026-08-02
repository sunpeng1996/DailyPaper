---
title: Novel Claim or Déjà Vu? Rethinking "Contamination-Free'' Dynamic Evaluation
  for Multimodal Automated Fact-Checking
title_zh: 《是新声明还是旧知识？重审多模态自动事实核查的「无污染」动态评估》
authors:
- Haorui He
- Xinwen Chen
- Dacheng Wen
- Reynold Cheng
- Francis C. M. Lau
- Yupeng Li
affiliations:
- Hong Kong Baptist University
- The University of Hong Kong
- Beijing Normal-Hong Kong Baptist University
arxiv_id: '2607.23514'
url: https://arxiv.org/abs/2607.23514
pdf_url: https://arxiv.org/pdf/2607.23514
published: '2026-07-26'
collected: '2026-08-02'
category: Eval
direction: 多模态事实核查 · 评估数据污染治理
tags:
- Multimodal Fact-Checking
- Evaluation
- Data Contamination
- Dynamic Benchmark
- LLM
one_liner: 实证揭示多模态事实核查动态基准仍存残留污染，给出可信评估实践指引
practical_value: '- 做检索类电商导购Agent的效果评估时，不能仅依赖知识截断后的数据，需额外校验样本是否可通过旧知识组合推导，避免高估检索模块价值

  - 评估依赖外部实时数据的系统（如电商舆情核查、广告内容合规校验系统）时，建议先过滤可通过内部知识库直接回答的样本，避免性能虚高

  - 算法迭代横向对比时若出现异常性能涨幅，可先排查测试集污染风险，避免错误判断新方法的真实收益'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态自动事实核查（MAFC）需基于外部证据做检索推理，现有静态基准多为过时声明，可被LLM内部知识直接验证导致性能虚高，无法反映需实时信息的新声明处理能力；业界普遍假设知识截断后发布的动态基准无污染，该假设尚未被验证。
### 方法关键点
构造覆盖2025Q4的新动态基准ClaimReview2025Q4，对比SOTA静态基准AVeriTeC，系统实证两类基准的污染风险及对评估结果的影响。
### 关键结果
1. 动态评估仅能降低无法消除污染，17.09%~29.30%的截断后声明仍存在潜在污染；
2. 大量新声明可通过截断前公开知识组合推导验证；
3. 污染可使MAFC的Macro-F1最高虚增11.34个点，还会扭曲系统排名。

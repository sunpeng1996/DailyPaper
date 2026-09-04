---
title: 'Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure
  of Black-Box LLM Observers on Shared Endpoints'
title_zh: 共享端点黑盒LLM评审器的预注册实验可靠性失效分析
authors:
- Haoyaun Zhu
- Jie Zhang
affiliations:
- University of Sheffield
- Ranplan Wireless Network Design Ltd.
- Cambridge AI+ Ltd.
arxiv_id: '2609.04198'
url: https://arxiv.org/abs/2609.04198
pdf_url: https://arxiv.org/pdf/2609.04198
published: '2026-09-03'
collected: '2026-09-04'
category: Eval
direction: LLM Judge 可靠性评估与落地指南
tags:
- LLM-Judge
- Evaluation-Reliability
- Black-Box-LLM
- Shared-Endpoint
- Preregistered-Evaluation
one_liner: 通过5万+请求验证共享端点LLM评审一致性极低，给出可靠性设计规则与检查清单
practical_value: '- 用共享端点LLM做RecSys/Agent自动效果评测前，必须先做同输入重复请求一致性校验，避免误判算法迭代效果

  - 若依赖LLM Judge做训练数据过滤/生成内容打分，优先用低负载自托管固定版本模型，不要用公有云共享端点

  - 预注册算法效果评测前，先做2%请求量的小规模试点，可提前暴露LLM评审工具的可靠性问题

  - LLM Judge输出差异远大于候选对象实际效果差异时，不能用其做细粒度排序类评测指标'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前LLM Judge被广泛用于训练数据过滤、生成内容打分、排行榜评测，业内默认同模型名同输入的输出稳定，但该假设从未被严格验证，直接影响所有基于LLM评审的结论可信度。

### 方法关键点
开展两次预注册实验，固定所有评测阈值，覆盖52988次请求，测试同窗口重复请求、跨天同字节请求的输出一致性，对比多家公有云服务商、自托管不同负载场景的表现。

### 关键结果
同窗口重复请求的排序Spearman相关仅0.40（要求≥0.90），跨天同字节请求相关仅0.78（要求≥0.99）；4家公有云服务商的一致性中位数仅0.74~0.88；自托管仅在无并发负载时达标，并发升高后一致性下降8.4倍回到公有云水平；最终提炼出3级快照身份阶梯、8条设计规则与评测检查清单，仅需2%请求量的试点即可提前暴露可靠性问题。

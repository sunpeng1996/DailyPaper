---
title: 'The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement
  Autoformalization'
title_zh: 'The Signal-Coverage Matrix: Stratifying Type and S'
authors:
- Chengxiao Dai
- Zhaokun Yan
- Zhanhui Lin
arxiv_id: '2606.28013'
url: https://arxiv.org/abs/2606.28013
pdf_url: https://arxiv.org/pdf/2606.28013
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Headline type-correctness (TC\%) of LLM autoformalization has climbed from
  $\sim$53\% to $\sim$...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Headline type-correctness (TC\%) of LLM autoformalization has climbed from $\sim$53\% to $\sim$76\% in two years, yet this scalar conceals which errors each method resolves. We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). On ProofNet\# and MiniF2F-test with DeepSeek V4-Pro across Vanilla, Lean-Retry, Sample-Filter, and Stratified Autoformalization (SAF): (1) the +34 to +36 TS gain across the three elab-feedback methods is $\sim$64\% type-stratum recovery, with SO flat on net (87.5\% of original semantic errors rescued, 8 newly created). (2) The TO-to-TS rate is 23/61 for each method (Wilson 95\% CI [26.6\%, 50.3\%]), and this stratum-level recovery rate predicts $Δ$TS on held-out methods to within 2/186 and renders $Δ$TC linear in the Vanilla elab-fail rate across six (model, dataset) cells ($R^2=0.96$). (3) The two judges disagree by 26 to 37 pp on elab-feedback outputs (vs. 7 pp on Vanilla), with 30 to 56\% of symbolic-judge false negatives traceable to elaborator-forced rewrites. The persistent residual reduces to two gold-formalization errors. TC\% gains should be credited by which cell moved, not by the scalar alone.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

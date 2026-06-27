---
title: 'Forecasting With LLMs: Improved Generalization Through Feature Steering'
title_zh: 'Forecasting With LLMs: Improved Generalization Thr'
authors:
- Humzah Merchant
- Bradford Levy
arxiv_id: '2606.27199'
url: https://arxiv.org/abs/2606.27199
pdf_url: https://arxiv.org/pdf/2606.27199
published: '2026-06-25'
collected: '2026-06-27'
category: Reasoning
direction: Reasoning
tags:
- Reasoning
- LLM
one_liner: Successful forecasting involves identifying patterns between historical
  and future states of th...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Successful forecasting involves identifying patterns between historical and future states of the world which generalize to future observations. We apply LLMs to a variety of forecasting tasks and inspect their internal states using sparse autoencoders to understand whether they appear to rely on time-specific pieces of knowledge versus generalizable patterns. Our analyses identify features associated with both time-aware reasoning and look-ahead-biased reasoning. We then apply the LLMs to an entirely different domain and intervene on these features. We find that amplifying time-awareness features substantially reduces look-ahead bias on forecasting prompts while preserving general reasoning performance. In contrast, steering the candidate look-ahead-bias features does not produce an effect. These results suggest that interpretable temporal features can be used to causally shift LLMs toward more historically grounded reasoning.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

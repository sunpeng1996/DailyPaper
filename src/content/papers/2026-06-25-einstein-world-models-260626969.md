---
title: Einstein World Models
title_zh: Einstein World Models
authors:
- Munachiso Samuel Nwadike
- Zangir Iklassov
- Ali Mekky
- Zayd M. Kawakibi Zuhri
- Kentaro Inui
arxiv_id: '2606.26969'
url: https://arxiv.org/abs/2606.26969
pdf_url: https://arxiv.org/pdf/2606.26969
published: '2026-06-25'
collected: '2026-06-26'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: Does intelligence require the ability to reason about phenomena beyond
  direct experience? It is...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Does intelligence require the ability to reason about phenomena beyond direct experience? It is natural to suspect that some complex thought cannot be captured through language alone. However, of particular concern to this work, is whether visualising counterfactual events can complement language as a mechanism for complex thought. We ask whether LLMs can be trained to utilise such visualisation mechanisms, in a way that benefits their reasoning abilities. Motivated by this question, we propose Einstein World Models. EWMs are a blueprint for LLM-based reasoning systems that place visual-temporal rollouts inside the reasoning trace, allowing them to reason in ways that text alone may not support well. In an EWM, the LLM calls a world-module (not to be confused with a world model), to produce short rollouts of scenes under consideration. The returned rollout is treated not as the answer, but as an inspectable hypothesis that can support later reasoning. Einstein World Models extend the capability of LLMs for tool calling (such as web search or code execution), into the domain of visual thought experiments.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

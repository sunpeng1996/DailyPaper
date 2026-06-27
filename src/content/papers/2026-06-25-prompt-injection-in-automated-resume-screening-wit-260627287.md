---
title: 'Prompt Injection in Automated Résumé Screening with Large Language Models:
  Single and Multi-Injection Settings'
title_zh: Prompt Injection in Automated Résumé Screening wit
authors:
- Preet Baxi
- Jiannan Xu
- Jane Yi Jiang
- Stefanus Jasin
arxiv_id: '2606.27287'
url: https://arxiv.org/abs/2606.27287
pdf_url: https://arxiv.org/pdf/2606.27287
published: '2026-06-25'
collected: '2026-06-27'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Large language models (LLMs) are increasingly used to screen and rank job
  applicants, creating...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Large language models (LLMs) are increasingly used to screen and rank job applicants, creating incentives for candidates to strategically manipulate algorithmic hiring systems. We study prompt injection in automated résumé screening, defined as subtle self-promotional text that introduces no new qualifications but is designed to influence LLM evaluations. Using controlled experiments, we show that prompt injection reliably improves applicant rankings when résumé quality is homogeneous and few candidates inject. However, its effectiveness rapidly diminishes as more candidates inject, collapsing when manipulation becomes widespread. When candidate quality is heterogeneous, prompt injection is less effective on average, but can occasionally allow lower-quality candidates to outrank higher-quality ones, raising fairness concerns. Overall, LLM-based screening is most vulnerable when manipulation is rare and candidate quality differences are small. Code and resources are publicly available at: https://github.com/preetb1199/Prompt_Injection_ACL26

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: 'Same Scrutiny, More Time: Eye Tracking Insights into Reviewing LLM-Labelled
  Code'
title_zh: 'Same Scrutiny, More Time: Eye Tracking Insights in'
authors:
- Ranim Khojah
- Francisco Gomes de Oliveira Neto
- Mazen Mohamad
- Julian Frattini
- Philipp Leitner
arxiv_id: '2606.26505'
url: https://arxiv.org/abs/2606.26505
pdf_url: https://arxiv.org/pdf/2606.26505
published: '2026-06-25'
collected: '2026-06-27'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Modern software development increasingly involves the use of large language
  models (LLMs) to ge...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 摘要

Modern software development increasingly involves the use of large language models (LLMs) to generate code. Despite their rapid advancement, LLMs remain prone to errors and hallucinations, emphasizing the importance of careful code inspection. However, in practice, developers' trust in LLM-generated code and their willingness to review it thoroughly may differ from these recommendations. How developers actually behave when reviewing LLM-generated code remains largely unexplored. In this study, we conduct a Wizard-of-Oz experiment to examine how software engineers behave when code is explicitly labeled as LLM-generated during a code review task. We collect both behavioral data and participant feedback through eye-tracking and exit interviews. Combining Bayesian data analysis with qualitative analysis, we found that while the thoroughness of code review did not change for participants, they spent more time fixating on LLM-labelled code, indicating that the label itself influences attention. Practitioners also adapted their review strategy for LLM-labelled code by assessing the code based on specific criteria (e.g., logical correctness), or using the prompt to guide their review. These findings inform LLM-based tool design on labelling while incorporating the prompt as a software artifact. Our study reveals a gap between reviewers' intentions and actual reviewing behaviour, highlighting the need for software companies to revisit their AI policies (particularly regarding LLM-assisted development) to better support developers in reviewing LLM-generated code.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

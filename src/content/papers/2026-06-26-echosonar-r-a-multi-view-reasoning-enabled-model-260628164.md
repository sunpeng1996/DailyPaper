---
title: 'EchoSonar-R: A Multi-View Reasoning-Enabled Model for Disease Classification
  and Report Generation in Echocardiography'
title_zh: 'EchoSonar-R: A Multi-View Reasoning-Enabled Model'
authors:
- Darya Taratynova
- Ahmed Aly
- Numan Saeed
- Mohammad Yaqub
arxiv_id: '2606.28164'
url: https://arxiv.org/abs/2606.28164
pdf_url: https://arxiv.org/pdf/2606.28164
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Echocardiography is the most widely used non-invasive cardiac imaging modality,
  providing essen...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Echocardiography is the most widely used non-invasive cardiac imaging modality, providing essential information for cardiovascular diagnosis. Interpreting an echocardiogram requires synthesizing complementary evidence across multiple heart views to identify abnormalities and produce structured clinical reports. While recent efforts focus on improving classification performance, most models lack explicit diagnostic reasoning and spatially grounded anatomical evidence, limiting clinician trust. We present EchoSonar-R, a multi-view reasoning-enabled vision-language model that jointly performs multi-label disease classification and report generation from echocardiography studies. EchoSonar-R combines a spatiotemporal video encoder with a structure-aware cardiac detector that provides spatially grounded anatomical cues to improve interpretability and clinician trust during cross-view reasoning. EchoSonar-R is trained in two stages: supervised fine-tuning (SFT) on reasoning-annotated targets, followed by Group Relative Policy Optimization (GRPO) with task-specific rewards that jointly align classification and report generation within a unified reinforcement-learning framework. Across a private multi-view dataset and two public benchmarks, EchoSonar-R improves macro balanced accuracy by 17.1% on the private set and 6.1% on MIMICEchoQA over the strongest baseline, achieves a GREEN clinical faithfulness score of 0.800, and produces interpretable reasoning traces grounded in multi-view visual evidence.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

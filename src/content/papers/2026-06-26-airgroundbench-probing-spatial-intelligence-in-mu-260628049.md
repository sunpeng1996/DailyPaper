---
title: 'AirGroundBench: Probing Spatial Intelligence in Multimodal Large Models under
  Heterogeneous Multi-View Embodied Collaboration'
title_zh: 'AirGroundBench: Probing Spatial Intelligence in Mu'
authors:
- Haotian Li
- Yida Wang
- Leyuan Wang
- Jinshan Lai
- Keyang Wang
- Zonghao Guo
- Qiang Ma
- Liuyu Xiang
- Jianwei Hu
- Zhaofeng He
arxiv_id: '2606.28049'
url: https://arxiv.org/abs/2606.28049
pdf_url: https://arxiv.org/pdf/2606.28049
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: In recent years, multimodal large language models (MLLMs) have shown strong
  potential for embod...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.CV
depth: abstract
---

### 摘要

In recent years, multimodal large language models (MLLMs) have shown strong potential for embodied intelligence, yet their ability to maintain geometrically consistent spatial understanding across heterogeneous views remains under-evaluated. Existing benchmarks largely focus on single-agent, single-view perception, leaving a gap in the systematic assessment of collaborative air-ground settings, where multi-scale observations are complementary but introduce scale mismatch, asymmetric occlusion, and reference-frame inconsistencies. We present AirGroundBench, a diagnostic benchmark for evaluating multi-view spatial intelligence in heterogeneous UAV-UGV collaboration. AirGroundBench is built from 11 high-fidelity simulated environments with 1,021 synchronized air-ground observation pairs, yielding approximately 62,000 dual-view, four-option single-choice visual question answering instances and 115 closed-loop vision-language navigation episodes. It covers 10 task types organized into four progressively demanding capability dimensions: spatial perception, cross-view alignment, spatial transformation and reasoning, and embodied decision-making. To support geometry-grounded evaluation and analysis, we provide structured spatial annotations, including cross-view object identities and metric 2D and 3D bounding boxes. Evaluations of 13 representative MLLMs under UAV-only, UGV-only, and dual-view input settings reveal consistent bottlenecks: models perform relatively well on spatial perception but struggle with cross-view alignment and transformation-intensive reasoning, and these deficits propagate to sequential decision-making in vision-language navigation. Although dual-view inputs provide measurable gains over single-view variants, a persistent gap from human performance remains, highlighting geometric consistency as a key limitation of current embodied MLLMs.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

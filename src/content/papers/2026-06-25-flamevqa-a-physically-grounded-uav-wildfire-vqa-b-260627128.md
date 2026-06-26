---
title: 'FlameVQA: A Physically-Grounded UAV Wildfire VQA Benchmark with Radiometric
  Thermal Supervision'
title_zh: 'FlameVQA: A Physically-Grounded UAV Wildfire VQA B'
authors:
- Mobin Habibpour
- John Spodnik
- Niloufar Alipour Talemi
- Fatemeh Afghah
arxiv_id: '2606.27128'
url: https://arxiv.org/abs/2606.27128
pdf_url: https://arxiv.org/pdf/2606.27128
published: '2026-06-25'
collected: '2026-06-26'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: Wildfire monitoring from UAVs requires reliable reasoning over complex
  aerial scenes, where smo...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Wildfire monitoring from UAVs requires reliable reasoning over complex aerial scenes, where smoke, scale variation, and occlusions often limit RGB-only interpretation. We introduce FlameVQA, a multiple-choice visual question answering benchmark for UAV-based wildfire intelligence built on FLAME 3, leveraging paired RGB imagery and radiometric thermal TIFFs for temperature-grounded, safety-critical reasoning. FlameVQA includes 34 multiple-choice questions per image spanning six operational capability groups, covering tasks such as detection, localization, distribution/coverage estimation, cross-modal reasoning, and flight planning. To ensure label reliability, we combine MLLM-assisted annotation with deterministic thermal rules and cross-question consistency checks, followed by human auditing. We also evaluate representative MLLMs on FlameVQA to provide baselines for future work. Results show strong performance when explicit cross-modal cues are available, but notable failures on presence detection under heavy smoke and on coverage estimation. These findings suggest that current MLLMs require domain-specific adaptation to better support disaster and wildfire monitoring. The dataset and benchmark code are open-source at github.com/mobiiin/WildFire_VQA

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

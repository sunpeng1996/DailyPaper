---
title: 'CORTEX: A Structured Reasoning Benchmark for Trustworthy 3D Chest CT MLLMs'
title_zh: 'CORTEX: A Structured Reasoning Benchmark for Trust'
authors:
- Hashmat Shadab Malik
- Anees Ur Rehman Hashmi
- Numan Saeed
- Muzammal Naseer
- Salman Khan
- Christoph Lippert
arxiv_id: '2606.27264'
url: https://arxiv.org/abs/2606.27264
pdf_url: https://arxiv.org/pdf/2606.27264
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Reasoning in multimodal large language models (MLLMs) has shown strong
  promise in medical imagi...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Reasoning in multimodal large language models (MLLMs) has shown strong promise in medical imaging. However, this reasoning is usually free-form text judged only by its final answer, making it hard to interpret and verify, especially in 3D radiology, where a diagnosis should be traceable to evidence in the scan. Existing chest CT question-answering datasets compound this by reducing expert radiology reports to answer-only pairs, dropping the reasoning that links findings to conclusions and omitting the patient history clinicians rely on. As a result, reasoning-capable 3D chest CT MLLMs remain out of reach, as neither the structured supervision needed to train them nor the protocol needed to verify their reasoning yet exists. We introduce CORTEX (Clinically Organized Reasoning and sTructured EXplanation), a structured reasoning benchmark for 3D chest CT. For each question, CORTEX restores the missing reasoning as a four-stage diagnostic trace mirroring a radiologist's workflow: task understanding, visual observation, diagnostic reasoning, and answer synthesis. We generate these traces using frontier large language models with broad medical and general-domain knowledge, then filter and verify them with a stage-level evaluation protocol combining automated rubric scoring with expert radiologist review. Crucially, both the reasoning structure and evaluation rubrics are designed in close collaboration with clinicians. Built on CT-RATE, a large, publicly available chest CT dataset without reasoning annotations, CORTEX comprises 76,177 validated reasoning traces across open-ended VQA, closed-ended VQA, and report generation, providing both the structured supervision and the stage-level evaluation protocol needed to build and evaluate trustworthy reasoning models for 3D chest CT. Our dataset and evaluation code will be made publicly available upon acceptance.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

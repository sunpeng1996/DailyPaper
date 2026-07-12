---
title: ICDAR 2026 HIPE-OCRepair Competition on LLM-Assisted OCR Post-Correction for
  Historical Documents
title_zh: ICDAR 2026 HIPE-OCRepair 历史文档LLM辅助OCR后校正竞赛报告
authors:
- Maud Ehrmann
- Emanuela Boros
- Juri Opitz
- Andrianos Michail
- Florian Wagner
- Simon Clematide
affiliations:
- École Polytechnique Fédérale de Lausanne (EPFL)
- University of Zurich
arxiv_id: '2607.08143'
url: https://arxiv.org/abs/2607.08143
pdf_url: https://arxiv.org/pdf/2607.08143
published: '2026-07-09'
collected: '2026-07-12'
category: Eval
direction: LLM评测 · OCR后校正多语言基准
tags:
- LLM
- OCR Post-Correction
- Multilingual Benchmark
- Evaluation Framework
- Historical Document
one_liner: 发布多语言历史文档OCR校正基准及检索导向的LLM辅助OCR后校正评测框架
practical_value: '- 电商商品说明书、历史评价、老旧商品档案的OCR文本校正场景，可采用检索导向的评估指标，避免单纯降低字符错误率引发的过校正问题

  - 低噪声文本的纠错任务可参考竞赛结论，优先用轻量级prompt策略而非全量微调，兼顾效果与过校正风险控制

  - 多语言跨场景的文本纠错类任务，可复用本次开源的评测pipeline快速完成方案迭代与效果验证'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
大规模历史数字化文档存在大量遗留OCR错误，全量重扫成本极高，LLM为OCR后校正提供了新路径，但跨语言、跨噪声场景的效果及幻觉风险缺乏系统性评估。
### 方法关键点
竞赛构建覆盖英/法/德三语、17-20世纪历史报纸/印刷品的统一基准数据集，任务要求仅输入OCR文本（无原图）完成段落级校正，采用面向检索实用场景的评分标准而非纯字符精度，对比了从zero-shot prompting到持续预训练、微调的四类参赛方案。
### 关键结果
LLM辅助校正方案可显著提升OCR质量，但效果在不同数据集、语言、噪声水平下差异明显，低噪声输入下过校正问题突出，仅优化字符错误率的评估维度存在明显缺陷，配套数据集、评分器、评测pipeline已全量开源。

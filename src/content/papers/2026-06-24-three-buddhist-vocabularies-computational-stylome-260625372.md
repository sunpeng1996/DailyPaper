---
title: 'Three Buddhist Vocabularies: Computational Stylometry of the English Pali
  Canon across Sutta, Vinaya, and Abhidhamma'
title_zh: 'Three Buddhist Vocabularies: Computational Stylome'
authors:
- Joy Bose
arxiv_id: '2606.25372'
url: https://arxiv.org/abs/2606.25372
pdf_url: https://arxiv.org/pdf/2606.25372
published: '2026-06-24'
collected: '2026-06-28'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: We present a computational stylometric analysis of the Tipitaka across
  all three Pitakas in Eng...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 摘要

We present a computational stylometric analysis of the Tipitaka across all three Pitakas in English translation, extending earlier work on the Sutta Pitaka alone. The corpus spans 134,831 segments from Bhikkhu Sujato's Sutta Pitaka (114,591 segments, CC0), Bhikkhu Brahmali's Vinaya Pitaka (7,923 segments, CC0 2026), I.B. Horner's 1938 Vinaya translation (2,826 segments), three English translations of the Abhidhammattha Sangaha compendium (2,077 segments), and cross-tradition Vinaya texts from the Dharmaguptaka and Mulasarvastivada schools. We compute Zipf rank-frequency distributions with OLS-fitted exponents, Moving Average TTR (MATTR-500), numeral-word density, and vocabulary overlap (Jaccard and Szymkiewicz-Simpson coefficients). Main findings: (1) all corpora show Zipf-consistent distributions (R2 > 0.989); the Vinaya is closest to ideal Zipf slope -1 and the Sangaha corpus deviates most, with 'consciousness' displacing grammatical particles at rank 8; (2) MATTR-500 shows the Sutta and Vinaya Theravada are nearly identical in lexical diversity (0.399 and 0.400), while the Sangaha corpus is genuinely more diverse (0.560), confirmed by size-controlled subsampling; (3) the Sangaha corpus has the highest numeral-word density (3.26%), consistent with its systematic enumeration of mental and material categories; (4) the Mulasarvastivada Vinaya shares 20.0% vocabulary (Jaccard) and 49.1% (overlap coefficient) with the Theravada Vinaya, reflecting shared legal heritage across two millennia; (5) two English translations of the same Vinaya source text share only 24.2% of their vocabulary across 88 years, with 'musing' versus 'absorption' for jhana and 'defeat' versus 'expulsion' for parajika as the most diagnostic shifts. All results are point estimates; no significance testing is conducted. Code and data are released as open-source extensions to the Darshana Graph corpus (arXiv:2606.18222).

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: 'Dialogue to Detection: A Multimodal Hybrid NLP Pipeline for Insurance Fraud
  Detection'
title_zh: 'Dialogue to Detection: A Multimodal Hybrid NLP Pip'
authors:
- Muhammad Shakeel Akram
- Amal Htait
- Abdul Hamid Sadka
- Emma Meisingseth
- Karishma Jaitly
arxiv_id: '2606.28002'
url: https://arxiv.org/abs/2606.28002
pdf_url: https://arxiv.org/pdf/2606.28002
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Insurance fraud imposes substantial financial losses and operational inefficiencies,
  raising pr...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Insurance fraud imposes substantial financial losses and operational inefficiencies, raising premiums and impacting trust among legitimate policyholders. Early detection at FNOL remains a persistent challenge. Existing approaches rely largely on private, text-only datasets, limiting progress on multimodal methods that integrate linguistic, behavioural, and speaker-based indicators. We introduce a synthetic multimodal framework that replicates FNOL conditions. It generates agent-customer dialogue transcripts and two-speaker audios, performs ASR and diarisation. Downstream modules combine NER, regex-based feature extraction, LLM-RAG retrieval, and speaker embeddings in a rule-based risk score to flag narrative reuse, structural inconsistencies, and cross-case voice repetition while balancing sensitivity and false positives. Dataset validation and component-level evaluations show stability and transfer potential, offering a reproducible baseline beyond text-only fraud detection.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: 'Speaker Identity in Non-Verbal Vocalizations: Conditional Distillation and
  Mixture of Experts Approach'
title_zh: 'Speaker Identity in Non-Verbal Vocalizations: Cond'
authors:
- Tzu-Chieh Wei
- Yi-Cheng Lin
- Huang-Cheng Chou
- Kuan-Yu Chen
- Hsin-Yen Sung
- Shrikanth Narayanan
- Hung-yi Lee
arxiv_id: '2606.21215'
url: https://arxiv.org/abs/2606.21215
pdf_url: https://arxiv.org/pdf/2606.21215
published: '2026-06-18'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: As expressive text-to-speech (TTS) and voice conversion (VC) systems increasingly
  generate non-...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: huggingface-daily
depth: abstract
---

### 摘要

As expressive text-to-speech (TTS) and voice conversion (VC) systems increasingly generate non-verbal vocalizations (NVVs) to enhance naturalness, reliable speaker verification (SV) becomes essential to objectively assess identity consistency across both verbal and non-verbal segments. Yet current SV systems generalize poorly to NVVs, and fine-tuning on NVV data causes catastrophic forgetting of speech performance. We present the first systematic study across 10 NVV types and propose a framework combining frozen Data2Vec self-supervised features with ECAPA-TDNN, enhanced by a Mixture of Experts (MoE) module with learned domain-aware routing. A conditional distillation loss on speech inputs via a pretrained teacher retains speech-to-speech accuracy, while a contrastive loss bridges the speech-NVV domain gap. Our method reduces speech-NVV EER from 38.93% to 22.66% over a pretrained baseline, and improves speech EER from 13.17% to 9.24% via distillation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

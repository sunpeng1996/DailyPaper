---
title: 'RedVox: Safety and Fairness Gaps in Speech Models Across Languages'
title_zh: 'RedVox: Safety and Fairness Gaps in Speech Models'
authors:
- Beatrice Savoldi
- Sara Papi
- Wafa Aissa
- Matteo Negri
- Luisa Bentivogli
arxiv_id: '2606.26968'
url: https://arxiv.org/abs/2606.26968
pdf_url: https://arxiv.org/pdf/2606.26968
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Speech-capable models are increasingly deployed in real-world applications
  across languages. Ye...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Speech-capable models are increasingly deployed in real-world applications across languages. Yet their safety and fairness beyond English settings and under naturalistic conditions remain understudied. We survey safety reporting practices across state-of-the-art speech model releases, finding that only 8% document any multilingual analysis. To address this gap, we introduce RedVox, a multilingual safety and fairness benchmark for audio and speech built on real voices, covering unsafe and unfair stereotypical requests across five languages (English, French, Italian, Spanish, and German). Evaluating eight state-of-the-art models, we find that vulnerabilities persist even under non-adversarial conditions, worsen in non-English languages, and are amplified when the request comes from a spoken input. Finally, by surveying the participants who contributed to RedVox, we document the unique personal and privacy challenges of collecting speech data with human participants, pointing to broader sociotechnical challenges in naturalistic speech safety research.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

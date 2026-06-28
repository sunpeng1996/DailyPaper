---
title: 'Beyond Artifacts: Towards Generalizable Synthetic Song Detection via Music-Intrinsic
  Features'
title_zh: 'Beyond Artifacts: Towards Generalizable Synthetic'
authors:
- Yan Han
- Zhibin Wen
- Yuan Wang
- Shuangrun Shao
- Xiaobing Li
- Yang Xu
- Wei Li
arxiv_id: '2606.16612'
url: https://arxiv.org/abs/2606.16612
pdf_url: https://arxiv.org/pdf/2606.16612
published: '2026-06-15'
collected: '2026-06-28'
category: LLM
direction: LLM
tags:
- LLM
- AI
one_liner: The rapid advancement of AI music generators highlights the urgent need
  for reliable Synthetic...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 5
source: arxiv-cs.MM
depth: abstract
---

### 摘要

The rapid advancement of AI music generators highlights the urgent need for reliable Synthetic Song Detection (SSD). Existing SSD methods often rely on low-level artifacts or fixed feature assumptions, struggling to capture generator-agnostic cues. To address this, we propose Sofia (Synthetic-song detection framework via music features), a flexible framework that models music-intrinsic attributes via feature-specific experts and an adaptive Mixture-of-Experts (MoE) module. By configuring Sofia with representative Vocal, Audio-effect, Global structure features, and their combinations, we present their individual and complementary contributions. To comprehensively evaluate our framework, we further construct MUSIC8K, a challenging benchmark featuring lastest emerging generators and realistic audio perturbations. Experiments show that Sofia learns generator-agnostic representations from music-intrinsic features, improving the F1 score by 18.5 points over the strongest baseline on MUSIC8K-O while maintaining strong robustness.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

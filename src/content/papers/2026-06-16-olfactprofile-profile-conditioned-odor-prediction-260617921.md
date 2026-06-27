---
title: 'OlfactProfile: Profile-Conditioned Odor Prediction from Audiovisual Content'
title_zh: 'OlfactProfile: Profile-Conditioned Odor Prediction'
authors:
- Zhengyu Lou
- Bosheng Qin
- Yanan Wang
- Duanduan Yin
- Wentao Ye
- Yu Xin
arxiv_id: '2606.17921'
url: https://arxiv.org/abs/2606.17921
pdf_url: https://arxiv.org/pdf/2606.17921
published: '2026-06-16'
collected: '2026-06-27'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Automated video-odor matching predicts scents aligned with audiovisual
  content for scent-enhanc...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.MM
depth: abstract
---

### 摘要

Automated video-odor matching predicts scents aligned with audiovisual content for scent-enhanced media. Existing methods usually treat odor labels as determined only by scene content, but odor judgment also depends on individual olfactory profiles, including scent sensitivity, tolerance to unpleasant odors, and affective preference. Ignoring this observer context limits current systems' ability to predict scents that match perceived experience. We present OlfactProfile, a framework for profile-conditioned odor prediction from audiovisual content. Our results show that olfactory profiles are not beneficial by default: with matched feature backbones, naive profile concatenation and uniform profile modulation can degrade performance, while structured field-wise profile conditioning consistently improves prediction. Thus, the key challenge is not merely whether observer context is available, but how it is integrated into multimodal reasoning. To study this setting, we construct an audiovisual benchmark pairing temporally aligned odor annotations with annotator olfactory preference profiles. It contains 1,350 video clips, a 99-class scent vocabulary, and three semantic odor tracks: Foreground Odor, Background Odor, and Emotion Odor. We also propose OAR (Olfactory-Aware Routing), a multimodal fusion module that performs track-aware audiovisual routing with field-wise profile modulation, allowing profile dimensions to influence odor reasoning according to perceptual role. Experiments show that OlfactProfile outperforms supervised baselines and general-purpose multimodal large models, is competitive with odor experts in a small human comparison, and improves perceived scent fit in scent-enhanced applications without task-specific fine-tuning. Per-track analysis shows that gains are strongest for Background Odor and Emotion Odor, where observer-dependent judgment is most important.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

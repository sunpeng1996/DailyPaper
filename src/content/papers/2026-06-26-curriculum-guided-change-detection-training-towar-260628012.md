---
title: 'Curriculum-guided Change Detection Training: Toward Accurate Serac Fall Monitoring'
title_zh: 'Curriculum-guided Change Detection Training: Towar'
authors:
- Arthur Dérédel
- Carlos Crispim-Junior
- Pierre Lemaire
- Johan Berthet
- Laure Tougne Rodet
arxiv_id: '2606.28012'
url: https://arxiv.org/abs/2606.28012
pdf_url: https://arxiv.org/pdf/2606.28012
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Change Detection (CD) aims to identify semantic or structural changes from
  nearly registered mu...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Change Detection (CD) aims to identify semantic or structural changes from nearly registered multi-temporal images. While recent advances in training methodologies have largely focused on semi-supervised learning and consistency regularization, alternative training paradigms remain underexplored. In particular, most deep CD methods rely on uniform sampling during training, implicitly assuming that all training samples contribute equally to the optimization process. However, such naive sampling can introduce noisy gradients and hinder robust representation learning. To address this limitation, we propose a curriculum learning framework tailored for change detection. Our approach investigates two complementary difficulty measures: the Solar Angular Gap (SAG), a physically grounded proxy for acquisition-condition variability, and the Structural Similarity Index Measure (SSIM), which evaluates appearance similarity between image pairs. Based on these criteria, the framework progressively introduces challenging samples during training, enabling models to learn robust representations in a coarse-to-fine manner. We evaluate our method on the challenging SeracFallDet benchmark, where results demonstrate consistent improvements of the proposed approach over standard uniform-sampling strategies for both pixel-based and object-based approaches. These results highlight the potential of curriculum learning to improve robustness in deep change detection. Importantly, our training framework is orthogonal to existing CD architectures, making it readily applicable to a broad range of methods.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

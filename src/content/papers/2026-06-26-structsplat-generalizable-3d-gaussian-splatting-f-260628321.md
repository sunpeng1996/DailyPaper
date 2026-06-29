---
title: 'StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse
  Views'
title_zh: 'StructSplat: Generalizable 3D Gaussian Splatting f'
authors:
- Jia-Chen Zhao
- Beiqi Chen
- Xinyang Chen
- Guangcong Wang
- Liqiang Nie
arxiv_id: '2606.28321'
url: https://arxiv.org/abs/2606.28321
pdf_url: https://arxiv.org/pdf/2606.28321
published: '2026-06-26'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: We present StructSplat, a feed-forward and generalizable 3D Gaussian reconstruction
  framework t...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 摘要

We present StructSplat, a feed-forward and generalizable 3D Gaussian reconstruction framework that operates directly on uncalibrated images without requiring camera parameters. Existing methods either rely on per-scene optimization or assume known camera poses, and often entangle geometry and appearance within a unified backbone, limiting reconstruction fidelity and generalization. Our key idea is to adopt a structured representation that organizes geometry, semantic, and texture cues with explicit roles in the reconstruction process. Specifically, we introduce a pixel-aligned feature injection mechanism to enable accurate texture modeling from 2D observations, incorporate semantic-aware priors to improve global consistency, and design a camera alignment strategy to prevent information leakage and improve generalization. Experiments show that our method significantly outperforms prior approaches on challenging benchmarks. On DL3DV, our method achieves 28.045 PSNR, surpassing AnySplat (22.377) by +5.67 dB. In cross-dataset evaluation, our method achieves +1.94 dB over AnySplat on ACID and +1.72 dB on RealEstate10K. Project page: https://structsplat.github.io Code: https://github.com/J-C-Zhao/StructSplat

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

---
title: 'RayPE: Ray-Space Positional Encoding for 3D-Aware Video Generation'
title_zh: 'RayPE: Ray-Space Positional Encoding for 3D-Aware'
authors:
- Minghao Yin
- Jiahao Lu
- Wenbo Hu
- Wang Zhao
- Shan Ying
- Kai Han
arxiv_id: '2606.27345'
url: https://arxiv.org/abs/2606.27345
pdf_url: https://arxiv.org/pdf/2606.27345
published: '2026-06-25'
collected: '2026-06-26'
category: QueryRec
direction: QueryRec
tags:
- QueryRec
- LLM
one_liner: Modern video diffusion transformers position their tokens through RoPE
  on the (u,v,t) axes -- a...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Modern video diffusion transformers position their tokens through RoPE on the (u,v,t) axes -- a description of the camera's sampling grid that says nothing about the 3D structure of the scene. We observe that the geometric relation between two camera rays is captured by the Plucker reciprocal product, which is bilinear in the two rays -- the same algebraic form as the dot product in Transformer attention. Building on this analogy, we propose RayPE, a positional-encoding extension that injects per-token 6D Plucker coordinates additively into the queries and keys of self-attention, with a query/key flip arrangement under which the symmetric identity configuration coincides exactly with the reciprocal product. The injection is additive, the resulting attention score decomposes into a content term, a geometry term, and two content and geometry cross-terms -- all of which our experiments find individually necessary. To make the encoding stable across video data with heterogeneous camera-translation scales (SfM, deep SLAM, metric), we further decouple ray direction from moment magnitude, gate the encoding by a learned function of the log-magnitude, and apply RMSNorm to align it with the QKNorm-normalized content branch. The full module adds less than 0.1% parameters to a pretrained video DiT, is zero-initialized to start from the pretrained weights, and improves camera controllability, cross-frame 3D consistency, and overall video quality on a four-dataset training mixture.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。

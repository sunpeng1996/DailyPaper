---
title: 'HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent
  Collaboration'
title_zh: 'HAT-4D: Lifting Monocular Video for 4D Multi-Objec'
authors:
- Jiaxin Li
- Yuxiang Wu
- Zhenkai Zhang
- Xinrui Shi
- Haoyuan Wang
- Yichen Zhao
- Su Linxiang
- Chenyang Yu
- Mingyu Zhang
- Yifan Ding
arxiv_id: '2606.28215'
url: https://arxiv.org/abs/2606.28215
pdf_url: https://arxiv.org/pdf/2606.28215
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Extracting dynamic 4D object interactions from massive, in-the-wild monocular
  videos offers a h...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 10
source: arxiv-cs.AI
depth: abstract
---

### 摘要

Extracting dynamic 4D object interactions from massive, in-the-wild monocular videos offers a highly efficient data collection pathway for scaling Embodied AI and training VLAs. However, existing monocular 4D reconstruction methods primarily focus on isolated objects, often failing under the severe occlusions and complex dynamics inherent in multi-object interactions. To bridge this gap, we propose HAT-4D, the first agentic framework designed to reconstruct the 3D geometry, temporal dynamics, and physical interactions of multiple objects from a single video. By integrating VLMs with a multi-level human-in-the-loop feedback mechanism, HAT-4D efficiently resolves depth ambiguities and interaction-induced occlusions during 3D generation and 4D propagation, yielding physically plausible assets without relying on expensive multicamera rigs. As a scalable data engine, HAT-4D facilitates the creation of MVOIK-4D, an open-world benchmark for monocular 4D interaction reconstruction, accompanied by a novel multi-dimensional evaluation protocol focused on physical plausibility and temporal consistency. Extensive experiments demonstrate that HAT-4D achieves SOTA performance on most evaluation metrics, while maintaining competitive semantic alignment. Ablation studies show that introducing a small amount of human feedback improves interaction reconstruction. Moreover, the data produced by HAT-4D effectively improves baseline performance when used for fine-tuning. Our data and code are available at https://lijiaxin0111.github.io/HAT4D/

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。

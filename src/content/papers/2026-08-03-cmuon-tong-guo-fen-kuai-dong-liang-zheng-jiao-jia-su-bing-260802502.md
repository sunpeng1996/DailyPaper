---
title: 'CMuon: Accelerating and Stabilizing Diffusion Transformer Training via Chunked
  Momentum Orthogonalization'
title_zh: CMuon：通过分块动量正交加速并稳定Diffusion Transformer训练
authors:
- Chuyan Chen
- Peng Sun
- Kun Yuan
affiliations:
- Peking University
- Westlake University
- Zhejiang University
arxiv_id: '2608.02502'
url: https://arxiv.org/abs/2608.02502
pdf_url: https://arxiv.org/pdf/2608.02502
published: '2026-08-03'
collected: '2026-08-05'
category: Training
direction: 大模型训练 · 优化器性能优化
tags:
- DiT
- Optimizer
- Training Speedup
- Momentum Orthogonalization
- Convergence
one_liner: 提出分块动量正交优化器CMuon，解决Muon在DiT上后期收敛差问题，训练速度较AdamW提升2倍以上
practical_value: '- 训练生成式推荐、多模态商品生成类DiT结构大模型时，可直接用CMuon替换AdamW，获得2倍以上训练提速，降低预训练成本

  - 对含融合权重（如QKV、AdaLN层统一张量）的Transformer结构应用Muon类优化器时，先按功能拆分融合张量再做正交化，避免子空间耦合导致的后期收敛停滞

  - 大参数LLM、多模态推荐模型预训练调优时，可验证CMuon的收敛效果与速度优势，替代AdamW减少训练资源消耗'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
DiT在生成任务上达到SOTA性能但训练算力开销极高；现有Muon优化器相比AdamW有收敛速度优势，但直接应用于DiT时存在后期收敛效果差的问题，根因是DiT为提升计算效率，将功能不同的权重（如AdaLN、QKV层参数）融合为统一张量，Muon直接对融合张量做正交化会引发隐式子空间耦合，扭曲参数更新方向，劣化全局优化效果。
### 方法关键点
提出CMuon策略，在执行正交化操作前，将融合权重矩阵按功能拆分为独立子组件，分别对各子组件做动量正交化，彻底避免子空间耦合问题。
### 关键结果
675M参数DiT用CMuon训练，ImageNet 256生成任务仅200 epoch就达到FID 1.18，训练速度相比AdamW提升2倍以上，同时完全解决了原生Muon的后期收敛停滞问题。

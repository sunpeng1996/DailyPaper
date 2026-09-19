---
title: 'PhGS: Post-Hoc Pruning and Refinement of Single-View Feed-Forward 3D Gaussian
  Reconstructions'
title_zh: PhGS：单视图前馈3D高斯重建的事后剪枝与优化方案
authors:
- Rinto Yagawa
- Han Cheng
- Dieter Schmalstieg
- Hideo Saito
- Shohei Mori
affiliations:
- Keio University
- University of Stuttgart
arxiv_id: '2609.20623'
url: https://arxiv.org/abs/2609.20623
pdf_url: https://arxiv.org/pdf/2609.20623
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 单视图3DGS 事后压缩优化
tags:
- 3D Gaussian Splatting
- Model Pruning
- Post-hoc Compression
- Single-view Reconstruction
- Efficient Inference
one_liner: 提出冻结预训练基座的单视图3DGS事后剪枝优化管道，降显存同时保留新视角渲染质量
practical_value: '- 「冻结基座+轻量后处理优化」的范式可直接迁移到LLM4Rec、RAG系统迭代，无需重训大基座即可优化输出效果，大幅降低迭代成本

  - 基于重要度打分剪枝+迭代修正留存结果的思路，可用于推荐召回/粗排阶段候选集压缩，在无损效果的前提下降低后续链路计算开销

  - 推理阶段可灵活配置压缩比例的设计，适配不同算力的云侧/端侧推荐场景部署需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有单视图前馈3DGS生成方案每相机射线预测固定数量高斯，存在严重空间冗余；多视图3DGS压缩策略依赖跨视图一致性，无法适配单视图场景；重新训练基座输出紧凑表示的方案成本极高。
### 方法关键点
1. 设计与主干无关的压缩管道，全程冻结预训练3DGS基座，无需重训
2. 先基于重要度打分剪枝冗余高斯基元，再通过轻量可训练循环优化模块迭代更新留存基元，恢复渲染质量
3. 推理阶段支持灵活配置高斯留存比例，适配不同部署需求
### 关键结果数字
可无缝对接Flash3D、Niagara等主流单视图3DGS基线，留存50%高斯时PSNR仅从27.55dB降至27.41dB，几乎无感知损失，同时实现高显存压缩

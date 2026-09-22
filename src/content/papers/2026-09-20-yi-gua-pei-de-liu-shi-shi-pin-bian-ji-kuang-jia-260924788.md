---
title: Streaming Video Editing with Easy Adaptation
title_zh: 易适配的流式视频编辑框架
authors:
- Yujia Hu
- Jiajun Li
- Zihao He
- Songhua Liu
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2609.24788'
url: https://arxiv.org/abs/2609.24788
pdf_url: https://arxiv.org/pdf/2609.24788
published: '2026-09-20'
collected: '2026-09-22'
category: Other
direction: 流式视频生成 · 扩散模型适配
tags:
- Video Diffusion
- Streaming Generation
- Feature Disentanglement
- Auto-Regressive Generation
- Real-time Editing
one_liner: 提出SVEET框架，基于预训练双向视频扩散模型实现低延迟高质量流式视频编辑
practical_value: '- 直播电商实时特效、短视频批量风格化场景可复用SVEET的低延迟流式编辑架构，单H100即可实现15FPS推理，无需额外加速组件

  - 约束优化方向正交性的跨模型知识迁移思路可复用在推荐系统跨域迁移场景，降低不同域特征空间的冲突

  - 特征解耦、条件帧独立的设计原则可迁移到生成式推荐的流式内容生成场景，减少时序依赖带来的推理延迟'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有双向视频扩散模型多为离线设计，无法满足直播、互动视频等场景的低延迟流式编辑需求，直接改造为自回归流式架构易出现特征冲突、生成质量下降问题。
### 方法关键点
1. 提炼流式适配两大核心原则：backbone特征解耦、条件帧独立性；
2. 新增辅助分支采用时序独立自注意力编码源视频，将中间特征注入主干块实现流式兼容控制；
3. 设计解耦训练方案，显式约束视频可控性与模型因果性优化方向正交，消除双向与流式模型特征空间差异，支持跨架构零样本知识迁移。
### 关键结果
单H100 GPU无额外加速下推理速度达15FPS，支持风格化、上色、修复等5类视频编辑任务，编辑质量优于现有流式方案。

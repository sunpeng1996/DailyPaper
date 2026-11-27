---
title: Diffusion Steering via Adaptive Reward Estimation and Resampling
title_zh: 基于自适应奖励估计与重采样的扩散模型引导方法
authors:
- Abinitha Gourabathina
- Sana Tonekaboni
- Marzyeh Ghassemi
- Akbar Rafiey
affiliations:
- Massachusetts Institute of Technology
- RBC Borealis
- NYU
arxiv_id: '2611.34839'
url: https://arxiv.org/abs/2611.34839
pdf_url: https://arxiv.org/pdf/2611.34839
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 多模态生成 · 扩散模型推理优化
tags:
- Diffusion Model
- Text-to-Image Generation
- Reward Guidance
- Controllable Generation
- Training-free
one_liner: 提出免训练TrailMix方法，通过并行轨迹重采样提升扩散生成的文本对齐度与可控编辑效果
practical_value: '- 免训练的并行轨迹打分+重采样思路可直接迁移到生成式推荐的推理优化场景，如个性化商品文案、营销图生成时，无需微调大模型即可提升结果与业务/用户需求的对齐度

  - 自适应奖励强度估计逻辑可复用在推荐多目标生成场景，避免固定奖励阈值带来的生成多样性损失或约束过严问题

  - 多候选轨迹的轻量预评估方法可借鉴到Agent工具调用的结果筛选环节，用小体量judge模型提前淘汰不符合要求的候选路径，降低后续链路成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
文本到图像扩散模型生成结果常遗漏prompt指定的物体、属性、关系，现有奖励引导方案要么需微调易损害模型通用能力，要么推理侧优化对齐效果不足。

### 方法关键点
1. 提出免训练方法TrailMix，去噪阶段生成多并行轨迹的低成本前瞻图像，用外部judge模型打分评估与prompt的对齐度
2. 基于奖励分数分布自适应计算引导强度，对生成轨迹重加权、重采样，向高对齐度结果偏移
3. 可扩展到定向图像编辑场景，同时提出SEAM-Bench评估语义编辑时非编辑内容的保留能力

### 关键结果
- 在3个文本生成图像基准上全面优于现有基线，罕见多物体组合场景增益尤为突出
- 在SEAM-Bench、PIE-Bench两个图像编辑基准上验证了可控编辑的有效性

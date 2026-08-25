---
title: 'E2S-Pruner: Progressive Two-Stage Evidence Fusion for Visual Token Pruning
  in Vision-Language Models'
title_zh: E2S-Pruner：面向VLM视觉Token剪枝的渐进式两阶段证据融合框架
authors:
- Taoyu Qian
- Qi Wang
- Daqian Shi
- Yuanhao Jiang
- Shang Gao
- Hualong Yu
affiliations:
- 江苏科技大学
- 伦敦玛丽女王大学
- 华东师范大学
- 南洋理工大学
arxiv_id: '2608.23253'
url: https://arxiv.org/abs/2608.23253
pdf_url: https://arxiv.org/pdf/2608.23253
published: '2026-08-24'
collected: '2026-08-25'
category: Multimodal
direction: 多模态大模型 · VLM推理效率优化
tags:
- VLM
- Token Pruning
- Inference Acceleration
- D-S Evidence Theory
- Multimodal LLM
one_liner: 无需训练的两阶段证据融合视觉Token剪枝框架，大幅降低VLM推理开销且性能损失极低
practical_value: '- 电商多模态商品理解、图文推荐场景可直接复用该剪枝方案，无需微调现有VLM即可获得1.96~2.09倍吞吐量提升，大幅降低大流量场景的推理成本

  - 推荐系统多域、多兴趣信号融合可借鉴D-S证据理论思路，显式建模不同信号源的冲突与不确定性，避免简单平均抹平互补特征

  - 空间新颖性约束可迁移到内容/商品召回排序场景，给不同类目/区域的高优候选加软权重，在不破坏原有排序逻辑的前提下提升结果覆盖度'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
视觉语言模型（VLM）将单张图像编码为数百个视觉Token，导致推理时延和显存开销极高，难以部署在资源受限场景。现有剪枝方法直接聚合不同注意力头、不同层的注意力分数，无法建模证据的不确定性与冲突，容易误剪包含互补语义的关键Token，造成性能大幅下降，亟需无需训练、性能损失可控的鲁棒剪枝方案。

### 方法关键点
- 第一阶段头内融合：将每个注意力头作为独立证据源，基于证据清晰度和头间一致性计算可靠性，为每个Token分配重要、不重要、不确定三种状态的质量分配值
- 第二阶段层间融合：基于D-S证据理论量化层间冲突，递归融合浅层纹理、中层物体、深层语义的互补证据，采用 plausibility 而非置信度作为剪枝依据，保护冲突度高的潜在重要Token
- 新增空间新颖性约束：将图像划分为网格，给每个网格内优先级最高的Token加软权重，避免保留Token集中在少数高响应区域，提升全局信息覆盖

### 关键结果
在LLaVA-1.5-7B上对比FastV、V2Drop等SOTA剪枝方法，平均保留192/128/64个Token时，分别保留98.0%/96.8%/90.6%的基准性能；128/64Token场景下吞吐量分别提升1.96倍、2.09倍，端到端时延降低48.5%/51.5%。在Qwen2-VL-7B上同样实现SOTA性能，具备跨模型通用性。

> 最值得记住：无需训练的Token剪枝通过显式建模多源信号冲突与不确定性，可在几乎无性能损失的前提下实现VLM推理效率翻倍

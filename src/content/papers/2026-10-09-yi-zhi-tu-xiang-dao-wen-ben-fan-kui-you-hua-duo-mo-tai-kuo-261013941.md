---
title: 'Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback'
title_zh: 抑制图像到文本反馈优化多模态扩散Transformer生成效果
authors:
- Yucheng Yang
- Xiaoxiao Sun
- Shusheng Yang
- Jiakang Chen
- Serena Yeung-Levy
affiliations:
- Stanford University
- Tsinghua University
- New York University
arxiv_id: '2610.13941'
url: https://arxiv.org/abs/2610.13941
pdf_url: https://arxiv.org/pdf/2610.13941
published: '2026-10-09'
collected: '2026-10-13'
category: Multimodal
direction: 多模态生成 · MMDiT对齐优化
tags:
- MMDiT
- Diffusion Model
- Text-to-Image
- Text-to-Video
- Alignment Optimization
one_liner: 提出SFG与零开销iSFG策略，通过抑制MMDiT的I2T反馈大幅提升图文生成对齐效果
practical_value: '- 电商商品图/种草短视频生成场景可直接复用iSFG策略，零额外推理开销即可提升生成内容与prompt的匹配度，优化素材质量

  - 多模态Agent的内容生成模块可参考SFG时序干预逻辑，仅在采样前20%步开启辅助分支，仅增加20%计算量即可获得显著对齐收益

  - 涉及多模态交叉反馈的生成系统可复用核心结论：无需盲目保留生成中间态到条件输入的反馈，抑制错误反馈反而能提升输出符合度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
MMDiT通过交叉注意力允许生成中的图像更新内部文本表征、再指导后续生成，此前未明确该I2T反馈的作用，研究发现其会保留生成图像已有的错误，无法纠正prompt偏离。
### 方法关键点
1. 提出Semantic Feedback Guidance（SFG），引导模型远离强化I2T反馈、弱化文生图条件的辅助分支，抑制错误反馈
2. 推出零额外推理开销的in-place变体iSFG，直接抑制I2T反馈同时强化文生图条件
3. 时序优化下仅需在前20%采样步运行SFG分支，仅带来1.2倍基础NFE开销
### 关键结果
- FLUX上SFG+CFG将GenEval从0.6661提升至0.7479
- SD3.5M上iSFG+CFG在零额外NFE下HPSv2.1提升1.33
- 策略可迁移至文生视频、图生视频场景，提升VBench得分

---
title: 'All modalities are equal, but video is more equal: Closing the Cross-Attention
  Gap in Joint Video Generation'
title_zh: 多模态平等但视频优先级更高：填补联合视频生成的跨注意力缺口
authors:
- Ohad Rahamim
- Dvir Samuel
- Idan Schwartz
- Gal Chechik
affiliations:
- Bar-Ilan University
- NVIDIA
arxiv_id: '2609.27901'
url: https://arxiv.org/abs/2609.27901
pdf_url: https://arxiv.org/pdf/2609.27901
published: '2026-09-22'
collected: '2026-09-24'
category: Multimodal
direction: 多模态联合视频生成 · 跨注意力正则化
tags:
- Multimodal Generation
- Diffusion Transformer
- Cross-Attention
- Regularization
- Video Generation
one_liner: 提出RecCAR跨模态注意力正则化方法，对齐双向对应关系，提升联合视频生成的多模态同步性
practical_value: '- 电商商品短视频（带讲解音频/3D动效）生成场景可直接复用RecCAR正则化，提升音画同步性、动作合理性，降低生成内容的违和感

  - 多模态匹配/召回任务的跨模态特征对齐模块，可借鉴双向对应差距的定义思路，用信息密度更高的模态为基准对齐弱模态特征，提升匹配精度

  - 多模态生成训练无需新增标注，仅通过正则化即可提升对齐效果，适合低标注成本的业务内容生成场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
联合多模态扩散Transformer存在跨模态对应不对称问题：从属模态（音频、3D人体运动等）到视频的约束远弱于视频到从属模态的对应，导致生成内容不同步、物理逻辑错误。

### 方法关键点
1. 将双向跨模态对应转换为视频token上的可比较分布，定义二者差值为 reciprocal correspondence gap
2. 提出RecCAR正则化，通过KL散度约束将弱的从属模态→视频对应分布，向已收敛的视频→从属模态对应分布对齐，无需新增数据或模型结构改动

### 关键结果
- 视频-运动生成任务：Human Anatomy score从0.69提升至0.75
- 视频-音频生成任务：音视频不同步度从0.804降至0.752，整体生成质量同步提升

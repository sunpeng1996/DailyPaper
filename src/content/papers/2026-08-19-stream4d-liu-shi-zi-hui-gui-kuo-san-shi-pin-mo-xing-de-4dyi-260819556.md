---
title: 'Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models'
title_zh: Stream4D：流式自回归扩散视频模型的4D一致性优化
authors:
- Yuanhao Ban
- Jiaqi Feng
- Hengguang Zhou
- Xiaohuan Pei
- Justin Cui
- Cho-Jui Hsieh
affiliations:
- UCLA
- Tsinghua University
arxiv_id: '2608.19556'
url: https://arxiv.org/abs/2608.19556
pdf_url: https://arxiv.org/pdf/2608.19556
published: '2026-08-19'
collected: '2026-08-27'
category: Other
direction: 流式视频生成 · 4D一致性优化
tags:
- Autoregressive Diffusion
- Streaming Video Generation
- 4D Consistency
- Motion Prior
- Dynamic Reconstruction
one_liner: 提出4D重建奖励+运动先验框架，解决流式自回归视频生成的几何漂移、运动失真问题
practical_value: '- 做AR商品展示、3D商品动态视频流式生成的场景，可借鉴4D动态奖励替代静态3D重建评价的思路，避免将正常的商品展示运动误判为生成误差

  - 做时序生成类业务（如直播商品切片自动生成、商品展示序列生成）时，可复用「显式运动先验+轻量感知锚」的损失设计，缓解长时序生成的抖动、漂移问题

  - 长序列自回归生成任务可参考全局一致性约束+局部生成目标结合的优化框架，降低长序列误差累积效应'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
流式自回归扩散视频支持实时长时序生成，但现有训练目标仅优化局部帧预测，长序列生成易出现几何漂移、静态/非自然运动；原有基于静态3D高斯溅射重建的奖励会误判正常物体运动为误差，甚至倾向生成静止视频，对AR等动态场景负面影响极大。
### 方法关键点
1. 用前馈4D重建奖励替代静态评价器，显式建模场景动态，对连贯运动给予高一致性奖励
2. 新增显式运动先验，奖励自然场景流幅度，惩罚抖动、非刚性伪影
3. 结合轻量感知锚，平衡全局一致性与生成质量
### 关键结果
跨多种自回归视频主干、多生成长度测试，4D重建质量、运动保留效果均优于基线，人类偏好得分更高

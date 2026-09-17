---
title: 'Copy What Is Seen, Generate What Is Not: Training-Free Anomaly-Aware Video
  Restoration'
title_zh: 所见即拷贝、缺失即生成：免训练异常感知视频修复方法
authors:
- Zhida Qu
- Shengchao Chen
affiliations:
- New York University
- University of Technology Sydney
arxiv_id: '2609.18836'
url: https://arxiv.org/abs/2609.18836
pdf_url: https://arxiv.org/pdf/2609.18836
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 免训练监控视频异常检测与修复联动
tags:
- Training-Free
- Anomaly Detection
- Video Inpainting
- Diffusion Model
- Pretrained Model
one_liner: 仅基于冻结预训练模型实现免训练监控视频异常检测与修复端到端联动
practical_value: '- 可复用免训练跨任务联动思路，落地多模态内容风控场景的违规内容自动抹除链路，无需额外fine-tune预训练模型，降低适配成本

  - 「先拷贝已有信息再生成缺失内容」的范式可迁移到电商商品图/短视频瑕疵修复场景，优先复用同素材正常区域像素，降低diffusion生成的不可控性

  - 多修复通路自动选择机制可借鉴到AIGC内容生产质量校验链路，根据内容特征自动匹配合适的生成通路，提升输出稳定性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有监控场景下异常检测与视频修复任务完全割裂：免训练异常检测器仅输出分数或标签，免训练视频编辑依赖用户prompt而非检测器输出，无法端到端完成异常自动抹除修复。
### 方法关键点
1. 仅用冻结预训练模型搭建AVR框架，先基于运动证据过滤开放词汇候选，生成时空异常掩码
2. 优先提取视频片段的背景先验，填充所有异常覆盖过的像素，仅对全帧未出现的缺失区域调用diffusion生成
3. 引入冻结校验器，逐片段自动选择经典修复、先验锚定修复、背景条件修复三种通路
### 关键结果
在三个监控数据集上，oracle掩码下全帧保真度领先SOTA；编辑区域效果与3个有监督训练的视频修复模型持平；自生成掩码下效果优于独立检测+生成的pipeline，同时有效抑制残留异常和diffusion生成的闪烁问题

---
title: 'Video Generation Models: A Survey of Post-Training and Alignment'
title_zh: 视频生成模型后训练与对齐技术综述
authors:
- Chaoyu Li
- Xiaoyi Gu
- Yogesh Kulkarni
- Eun Woo Im
- Mohammadmahdi Honarmand
- Zeyu Wang
- Juntong Song
- Fei Du
- Xilin Jiang
- Kexin Zheng
affiliations:
- Arizona State University
- Twitch
- Stanford University
- eBay
- NewsBreak
arxiv_id: '2610.00812'
url: https://arxiv.org/abs/2610.00812
pdf_url: https://arxiv.org/pdf/2610.00812
published: '2026-09-29'
collected: '2026-10-03'
category: Training
direction: 视频生成 · 后训练与对齐技术综述
tags:
- VideoGeneration
- PostTraining
- Alignment
- SupervisedFinetuning
- RLHF
- InferenceOptimization
one_liner: 首次系统性梳理视频生成领域后训练与对齐技术，给出统一分类框架与落地指导
practical_value: '- 视频生成的四类后训练对齐框架可直接迁移到生成式推荐（商品短视频/营销文案生成）的大模型对齐流程，无需从零设计对齐方案

  - 偏好奖励类对齐方法可复用在电商商品短视频的人眼偏好优化场景，解决生成内容不符合用户审美、营销转化要求的问题

  - 推理时对齐的技术思路可用于降低短视频流推荐、商品内容生成的推理成本，平衡生成质量与端到端响应速度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
预训练视频生成模型虽已能生成高分辨长时序内容，但普遍存在无法精准对齐人类意图、时序一致性差、不满足物理/安全约束等问题；且视频对齐相较图文面临时序误差累积、运动外观耦合、时序监督信号稀缺等独有挑战，亟需无需全量重训的后训练方案解决。
### 方法关键点
首次构建视频生成后训练对齐统一框架，按对齐信号实现方式分为隐式对齐、显式对齐两大类别，进一步梳理出四类主流技术路径：监督微调、自训练与蒸馏、偏好奖励驱动方法、推理时优化方法，覆盖训练到部署全流程。同时汇总了领域常用数据集、基准测试集与评估范式，明确了可扩展奖励设计、长时序一致性、稳定性与生成表现力权衡等核心开放挑战。
### 关键结果
配套开源了覆盖全领域的视频生成后训练技术资源库，为可控视频生成落地提供结构化指导。

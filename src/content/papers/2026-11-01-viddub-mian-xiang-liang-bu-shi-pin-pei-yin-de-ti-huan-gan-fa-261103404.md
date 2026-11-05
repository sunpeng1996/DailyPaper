---
title: 'VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing'
title_zh: VidDub：面向两步视频配音的替换感知蒸馏方法
authors:
- Yexin Liu
- Yunlong Lin
- Zehan Wang
- Guangxin He
- Xinli Xu
- Jiajun Zha
- Yaofu Liu
- Yueze Wang
- Bowen Ping
- Yuanming Li
affiliations:
- HKUST
- Tencent
- ZJU
- Tsinghua University
- KAUST
arxiv_id: '2611.03404'
url: https://arxiv.org/abs/2611.03404
pdf_url: https://arxiv.org/pdf/2611.03404
published: '2026-11-01'
collected: '2026-11-05'
category: Multimodal
direction: 多模态生成 · 视频口型同步配音
tags:
- Diffusion Model
- Knowledge Distillation
- Audio-Visual Alignment
- Video Editing
- Low Latency Inference
one_liner: 提出替换感知监督与两步蒸馏策略，实现低延迟高同步性的跨音频视频口型配音
practical_value: '- 跨模态生成任务遇到源信号与目标任务冲突的场景（如电商短视频配音、虚拟主播口型生成），可复用冲突区域损失掩码策略，屏蔽源干扰信号，提升目标任务（如口型同步）的准确率

  - 离线生成类业务可借鉴「全上下文教师模型训练+轨迹匹配蒸馏压缩」的范式，将多步扩散模型压缩到极低推理步数，在不明显损失生成质量的前提下大幅降低推理成本

  - 多模态对齐任务的评估可参考配对/跨场景双评估范式，同时覆盖原生场景和替换场景的效果，避免单一评估维度导致的效果偏差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频配音模型基于原始配对音频做自重建训练，当驱动语音被替换时，源口型会成为冲突信号导致同步效果差；同时扩散模型推理步数多、延迟高，无法适配离线配音的效率要求。
### 方法关键点
1. 替换感知跨音频监督：配对音频样本采用全帧重建损失，非配对替换音频样本掩码源口型的重建损失，仅通过音视频同步信号监督口型生成，其余面部、背景区域保留原有重建约束。
2. 两步蒸馏压缩：先训练替换感知教师模型获得高精度口型同步能力，再通过匹配轨迹回归将教师CFG引导的生成轨迹迁移到2步去噪的学生模型，搭配分布匹配蒸馏恢复步压缩后的视觉质量。
### 关键结果
掩码源口型重建损失使跨音频Sync-C指标提升0.833±0.040；最终2步模型在4个基准数据集上同时达到最优的口型同步、视觉质量、身份保留和视觉语音识别效果

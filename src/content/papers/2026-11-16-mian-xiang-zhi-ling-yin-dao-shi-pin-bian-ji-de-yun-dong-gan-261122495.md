---
title: Motion-Aware Reward Modeling for Instruction-Guided Video Editing
title_zh: 面向指令引导视频编辑的运动感知奖励模型
authors:
- Li Li
- Xiangbo Gao
- Bo Ni
- Samyadeep Basu
- Viet Dac Lai
- Jing Shi
- Seunghyun Yoon
- Gang Wu
- Yu Wang
- Thien Huu Nguyen
affiliations:
- University of Southern California
- Texas A&M University
- Vanderbilt University
- Adobe
- Amazon
arxiv_id: '2611.22495'
url: https://arxiv.org/abs/2611.22495
pdf_url: https://arxiv.org/pdf/2611.22495
published: '2026-11-16'
collected: '2026-11-23'
category: Multimodal
direction: 多模态视频生成 · 奖励模型优化
tags:
- Reward Model
- Video Editing
- Motion Perception
- Preference Training
- Multimodal Generation
one_liner: 提出融合RGB帧差流的运动感知奖励模型，解决视频编辑奖励偏好抑制运动结果的缺陷
practical_value: '- 电商短视频生成、商品演示视频编辑等多模态生成业务的奖励模型，可新增RGB帧差输入分支，规避生成结果丢失动态信息的问题

  - 偏好对齐训练阶段，可针对性构造动态信息受损/伪造的负样本，提升奖励模型对细粒度动态质量的判别能力

  - 新增专项判别分支后，可通过蒸馏锚点保留原奖励模型与人类偏好的对齐度，避免专项优化带来的整体质量偏移'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有指令引导视频编辑的奖励模型过度偏好时序一致性，存在运动崩溃缺陷：在VE-Bench上97%的场景会优先选择运动被抑制的编辑结果，传统VLM judge、基础奖励骨干对轻度运动抑制的识别准确率接近随机水平，无法支撑生成结果的动态质量管控。

### 方法关键点
1. 新增RGB帧差流作为帧间动态特征输入，显式建模运动信息；2. 偏好训练阶段引入运动抑制、运动伪造两类负样本，强化模型对运动质量的判别能力；3. 加入蒸馏锚点，避免专项优化后奖励模型偏离原有的人类整体质量偏好。

### 关键结果
在VE-Bench运动评测集上，运动抑制候选选择率降至0%，与人类质量评分的Spearman相关系数达0.57，可适配两类编辑pipeline的奖励引导微调，有效保留生成视频的运动信息。

---
title: 'FADRA: Frequency-Aware Diffusion with Residual Adaptation for Video Face Restoration'
title_zh: FADRA：面向视频人脸修复的频率感知残差自适应扩散模型
authors:
- Jin Jiang
- Jia Wang
- Panwen Hu
- Weiran Zhao
- Shengcai Liao
affiliations:
- UAEU
- OUC
- MBZUAI
arxiv_id: '2607.06389'
url: https://arxiv.org/abs/2607.06389
pdf_url: https://arxiv.org/pdf/2607.06389
published: '2026-07-07'
collected: '2026-07-09'
category: Other
direction: 视频人脸修复·扩散模型下游适配
tags:
- Diffusion Model
- LoRA
- Frequency-aware Loss
- Video Restoration
- Temporal Consistency
one_liner: 提出融合LoRA适配、逐步残差头、频率感知损失的扩散框架，提升视频人脸修复的精度与时序一致性
practical_value: '- 冻结基座+轻量LoRA+独立残差头的微调范式，可直接复用到生成式推荐、多模态商品内容生成场景，在降低训练成本的同时保留大模型原生泛化能力

  - 分频谱加权的损失函数设计，可迁移到电商短视频/直播画质增强、3D商品建模细节保真优化，强化人眼敏感区域的生成质量

  - 逐生成步引入原始低质输入特征引导的思路，可用于RAG生成、推荐个性化文案生成的事实性对齐，减少生成内容偏离原始信息的问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频人脸修复方法在复杂退化场景下无法平衡空间细节保真度与时序一致性，预训练大模型的生成先验迁移到下游任务时，容易出现原生能力丢失或适配不足的问题。
### 方法关键点
1. 基于预训练文生视频扩散基座，引入轻量LoRA适配器+低质像素对齐特征融合模块，在冻结主干的前提下实现高效任务适配，保留基座原生时序一致性能力；
2. 新增重复残差适配头（RRAH），在每步流匹配阶段输入低质隐特征与当前速度预测，逐步引入原始退化信息引导残差更新，同时兼顾面部细节修复与预训练时序先验保留；
3. 设计频率感知损失，对多个频谱带提供差异化监督，强化人眼敏感、易出现时序抖动的频率分量的约束。
### 关键结果
效果全面优于现有SOTA方法，量化指标与人工视觉感知均有明确提升，还原的人脸结构更准确，生成视频的时序连贯性更强。

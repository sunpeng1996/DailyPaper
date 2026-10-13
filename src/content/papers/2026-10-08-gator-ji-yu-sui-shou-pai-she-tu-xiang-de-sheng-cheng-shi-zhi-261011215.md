---
title: 'GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images'
title_zh: GATOR：基于随手拍摄图像的生成式智能体3D物体重建
authors:
- Qirui Wu
- Stan Birchfield
- Hesam Rabeti
- Angel X. Chang
- Bowen Wen
affiliations:
- NVIDIA
- Simon Fraser University
arxiv_id: '2610.11215'
url: https://arxiv.org/abs/2610.11215
pdf_url: https://arxiv.org/pdf/2610.11215
published: '2026-10-08'
collected: '2026-10-13'
category: Other
direction: 3D物体重建 · 生成式+智能体混合架构
tags:
- 3D Reconstruction
- Generative AI
- Multimodal Agent
- Text Conditioning
- Pose Estimation
one_liner: 提出融合生成能力与智能体迭代优化的GATOR框架，从随手拍图像恢复带姿态的纹理3D物体资产
practical_value: '- 可复用「生成初始结果+智能体迭代优化」的架构，迁移到电商商品3D建模业务，大幅降低商家3D素材制作成本

  - 局部模态融合模块的设计思路可借鉴到多模态商品特征提取任务，提升复杂背景下的商品识别精度

  - 分阶段适配器注入文本语义的方案可迁移到多模态生成任务，降低不同生成阶段的微调成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
从无标定、非孤立拍摄的日常图像重建对齐场景的完整3D物体，需解决稀疏观测不确定性、遮挡区域推理、背景干扰三大核心问题。
### 方法关键点
1. 局部模态混合器融合对齐后的RGB、目标掩码、点云特征，保留场景上下文同时精准区分目标与周边环境；
2. 引入分阶段适配器注入类别名称、物体描述等文本语义，补充空间cue以支撑结构、几何、外观多阶段生成；
3. 生成的初始资产初始化多模态智能体，通过观察引导的「编辑-渲染-校验」迭代循环完成结构、纹理的精细化调整。
### 关键结果
在合成物体、杂乱桌面、室内场景三类数据集上实现高几何与外观保真度，同时可精准恢复场景相对姿态，重建效率与仿真可用性优于纯生成、纯智能体基线方案。

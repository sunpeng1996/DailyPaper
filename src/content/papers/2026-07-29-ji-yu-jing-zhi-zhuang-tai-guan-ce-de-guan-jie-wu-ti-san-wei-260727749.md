---
title: Articulated Object Reconstruction from Rest-State Observation
title_zh: 基于静止状态观测的关节物体三维重建
authors:
- Daeun Lee
- Jaeah Lee
- Woosung Kim
- Haebeom Jung
- Jaesik Park
affiliations:
- Seoul National University
arxiv_id: '2607.27749'
url: https://arxiv.org/abs/2607.27749
pdf_url: https://arxiv.org/pdf/2607.27749
published: '2026-07-29'
collected: '2026-08-13'
category: Other
direction: 3D视觉 · 关节物体数字孪生重建
tags:
- 3D Reconstruction
- Digital Twin
- Diffusion Model
- Mesh Segmentation
- Vision-Language
one_liner: 仅用单张静止状态观测即可重建带关节参数的3D关节物体，性能比肩需运动输入的基线
practical_value: '- 若业务涉及电商可交互3D商品（如可开合家具、折叠电子设备）建模，该方案仅需单张静止图即可生成带关节参数的3D模型，可大幅降低3D素材采集成本

  - 用显式Mesh作为中间表示做跨模型输出校验融合的思路，可复用在多模态输入的3D内容生成 pipeline 中，缓解异源预训练模型输出噪声不一致问题

  - 扩散模型生成候选假设+几何一致性校验的范式，可借鉴到缺乏标注的3D结构估计任务中，减少对人工标注的依赖'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
交互式数字孪生构建需同时恢复物体3D几何与关节运动学结构，现有关节物体重建方法依赖多状态可观测运动输入，采集成本高，难以规模化落地。
### 方法关键点
1. 采用仅用单张静止闭合状态观测的重建范式，借助几何、语义、运动先验弥补运动 cues 缺失的问题
2. 用显式Mesh作为中间表示做跨模型校验融合，将视觉语言、分割模型的噪声输出整合为空间一致的部件结构
3. 引入视频扩散模型生成关节运动假设，通过几何一致性校验估算关节参数，无需观测实际运动
### 关键结果
部件分解精度、关节运动物理合理性表现优异，性能与依赖运动观测的重建类、生成类、模块化预训练模型基线相当。

---
title: 'WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models'
title_zh: WorldForge V2：实现视频扩散模型的相机轨迹对齐方法
authors:
- Chenxi Song
- Yanming Yang
- Tong Zhao
- Ruibo Li
- Joey Tianyi Zhou
- Chi Zhang
arxiv_id: '2610.31640'
url: https://arxiv.org/abs/2610.31640
pdf_url: https://arxiv.org/pdf/2610.31640
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 多模态生成 · 视频扩散相机轨迹对齐
tags:
- Video Diffusion Model
- LoRA
- Camera Control
- Trajectory Alignment
- Generative Model
one_liner: 提出无训练引导框架与Trajectory LoRA，实现视频扩散模型精准相机控制且泛化性更强
practical_value: '- 电商商品3D展示短视频生成可复用光流分离运动/外观通道的思路，固定商品外观下自由切换拍摄视角，大幅降低素材拍摄成本

  - 小样本定制场景视频生成可复用Trajectory LoRA+两阶段训练策略，单场景标注即可泛化到同品类新商品，减少训练数据需求

  - 批量视频生成推理时可复用v-cache优化思路，用前序去噪结果近似修正，省去额外模型推理步骤，降低计算开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
预训练视频扩散模型具备丰富3D/4D先验，但存在相机控制精度低、时空不一致、相机运动与场景动态纠缠的问题，现有微调/后处理方案普遍存在伪影多、泛化差、算力开销大的缺陷。
### 方法关键点
1. 无训练引导框架：基于扭曲参考帧沿目标相机路径迭代优化，通过光流分析识别运动相关隐层通道做选择性引导，搭配双路径对比引导/无引导预测修正参考帧缺陷，实现视角控制与场景外观、物体运动的解耦
2. 引入v-cache机制，用前序去噪预测结果近似修正，省去额外模型推理步骤，降低迭代优化的计算开销
3. 提出Trajectory LoRA，仅适配对轨迹引导最敏感的网络块，搭配两阶段训练策略，用极少量标注即可学习相机轨迹对齐能力
### 关键结果
多数据集评测下生成质量与轨迹精度均达SOTA，仅需单场景训练数据即可泛化到未见过的新场景。

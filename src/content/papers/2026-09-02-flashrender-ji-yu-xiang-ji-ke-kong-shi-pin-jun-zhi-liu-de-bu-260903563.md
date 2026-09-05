---
title: 'FlashRender: Few-Step Generative Rendering via Camera-Controlled Video MeanFlow'
title_zh: FlashRender：基于相机可控视频均值流的少步生成渲染
authors:
- Byeongjun Park
- Byung-Hoon Kim
- Hyungjin Chung
affiliations:
- EverEx
- Yonsei University
- Korea University
arxiv_id: '2609.03563'
url: https://arxiv.org/abs/2609.03563
pdf_url: https://arxiv.org/pdf/2609.03563
published: '2026-09-02'
collected: '2026-09-05'
category: Other
direction: 生成式视频渲染 · 少步采样优化
tags:
- GenerativeRendering
- VideoGeneration
- FewStepSampling
- CameraControl
- Distillation
one_liner: 提出少步生成渲染框架FlashRender，采样成本降25倍的同时保障画质与几何一致性，提升相机可控性
practical_value: '- 少步采样+蒸馏的加速思路可迁移到LLM4Rec、生成式商品文案/短视频生成场景，大幅降低推理成本

  - 表征变换对齐（RETA）的思路可复用在跨域推荐特征对齐、多模态商品表征融合的工程实现中

  - 解决采样步骤依赖不一致性的优化逻辑，可参考用于提升RAG系统多轮检索结果的稳定性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多步生成渲染模型存在采样步骤依赖的相机控制不一致问题，离散化误差高，推理速度慢，难以满足实时场景需求。

### 方法关键点
1. 提出表征变换对齐模块RETA，将源视频隐层表征与冻结视觉几何模型的目标视频特征对齐，实现采样步骤一致的相机控制，降低去噪轨迹曲率；
2. 在低曲率去噪轨迹上用MeanFlow目标微调，进一步缓解离散化误差；
3. 引入同策略流图蒸馏，修正固定少步采样下的自展开误差。

### 关键结果
仅需4步推理即可达到与多步基线相当的视频质量与几何一致性，采样成本降低25倍，在分布外目标相机轨迹下仍具备更优的相机可控性，单NVIDIA B200 GPU上480×832分辨率渲染仅需数秒。

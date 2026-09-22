---
title: 'WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory'
title_zh: WorldCrafter：带隐式3D感知记忆的一致性视频世界模型
authors:
- Wangbo Yu
- Kunhao Liu
- Wenbo Hu
- Shenghai Yuan
- Chaoran Feng
- Haiyang Zhou
- Yukun Huang
- Yiran Wang
- Wang Zhao
- Yingmin Luo
affiliations:
- ARC Lab, Tencent IEG
- Peking University
arxiv_id: '2609.24984'
url: https://arxiv.org/abs/2609.24984
pdf_url: https://arxiv.org/pdf/2609.24984
published: '2026-09-20'
collected: '2026-09-22'
category: Multimodal
direction: 多模态生成 · 3D感知视频世界模型
tags:
- VideoWorldModel
- 3DAwareMemory
- ControllableGeneration
- TemporalConsistency
- ViewConsistency
one_liner: 提出带隐式3D感知记忆的视频世界模型，大幅提升长时序多视角生成一致性与相机控制精度
practical_value: '- 3D感知记忆按请求视角压缩多源信息的思路，可迁移到AR电商虚拟逛店、3D商品展示的多视角内容生成，保证商品外观、场景结构跨视角一致性

  - 姿态条件读出模块的设计可复用在可控广告素材生成场景，支持指定运镜路径、视角的短视频/直播素材自动生成

  - 长时序历史信息压缩为固定数量token的方法，可优化交互Agent的上下文记忆管理，降低长对话/长时间交互的KV cache占用'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频世界模型在长时序生成、跨视角切换场景下，难以对齐历史观测信息，无法支撑长时间的场景交互式探索。
### 方法关键点
1. 设计相机可查询的隐式3D感知记忆，根据目标请求视角指导多视角观测证据压缩，适配视频生成器的有限token预算；
2. 记忆编码器、姿态条件读出模块与视频生成器联合训练，无需显式深度对应关系，即可在降噪前将历史观测整合为目标视角专属的固定token集合；
3. 结合3D感知记忆、短时上下文与少步蒸馏，支持单张输入图像或文本prompt驱动的流式场景探索。
### 关键结果数字
分钟级场景探索任务中，长时序生成一致性、相机控制精度均实现显著提升，同时不损失生成内容的视觉质量。

---
title: 'MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling'
title_zh: MotionCraft：基于稀疏注意力隐式世界建模的视觉超分方法
authors:
- Rong Fu
- Chunlei Meng
- Yangchen Zeng
- Xiaowen Ma
- Yongtai Liu
- Wangyu Wu
- Shuo Yin
- Zijian Zhang
- Sicheng Li
- Yingrui Ji
affiliations:
- Independent Researcher
arxiv_id: '2608.08553'
url: https://arxiv.org/abs/2608.08553
pdf_url: https://arxiv.org/pdf/2608.08553
published: '2026-08-09'
collected: '2026-08-13'
category: Other
direction: 视频超分 · 稀疏注意力隐式世界建模
tags:
- Video Super-Resolution
- Sparse Attention
- Latent World Model
- Generative Vision
one_liner: 提出融合运动感知隐状态预测、自适应稀疏注意力的可控视频超分框架，平衡效果效率与可控性
practical_value: '- 电商商品短视频、直播低清转高清场景可复用其运动融合+自适应稀疏注意力的时序建模思路，降低超分运算量的同时保证帧间一致性，避免画面抖动

  - 端侧流媒体低清内容实时上采样需求可借鉴其流式约束下的紧凑条件解码器设计，平衡推理 latency 与重建质量

  - 可控的时序平滑度/保真度 trade-off 机制可复用到内容生成后处理模块，适配不同业务场景的画质偏好（如短视频优先流畅度、商品展示优先清晰度）'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频超分方案存在多维度权衡困境：卷积对齐方法对大运动、复杂退化场景效果差；Transformer类长程建模方案算力开销高，需额外优化才能落地；隐扩散类生成方案纹理丰富但时序一致性差，无法同时满足流媒体场景的效果、效率、可控性需求。
### 方法关键点
1. 受世界模型启发，将超分任务重构为运动感知隐状态预测过程；
2. 核心由三大组件构成：鲁棒运动融合模块、兼顾局部交互与目标非局部关联的Latent World Transformer、紧凑条件解码器；
3. 集成自适应稀疏注意力，搭配显式用户可控接口，支持自定义画质偏好。
### 关键结果
流式约束下时序一致性与重建质量均优于现有方案，同时支持时序平滑度与重建保真度的可预测权衡，感知效果与重建精度达到SOTA水平。

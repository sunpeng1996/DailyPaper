---
title: 'EventEgoHands++: Event-based Egocentric 3D Hand Mesh Reconstruction with Real
  Dataset'
title_zh: EventEgoHands++：基于事件相机的第一视角3D手部网格重建及真实数据集
authors:
- Ryosei Hara
- Wataru Ikeda
- Masashi Hatano
- Mariko Isogawa
affiliations:
- Graduate School of Science and Technology, Keio University
- JST Presto
arxiv_id: '2609.17189'
url: https://arxiv.org/abs/2609.17189
pdf_url: https://arxiv.org/pdf/2609.17189
published: '2026-09-14'
collected: '2026-09-20'
category: Other
direction: 事件相机 · 第一视角3D手部重建
tags:
- Event Camera
- 3D Reconstruction
- Egocentric Vision
- Adaptive Attention
- Dataset Construction
one_liner: 提出带左右手实例检测的事件相机手部重建框架，构建当前最大的真实场景标注数据集
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
常规RGB/深度相机的第一视角3D手部重建方案在弱光、强运动模糊场景表现极差；现有事件相机方案仅用二值分割掩码，无法区分左右手实例，易误判双手存在性，导致重建精度低。
### 方法关键点
1. 内置左右手实例检测器，输出实例级边界框与分割掩码，提供手部细粒度标识
2. 提出Adaptive Attention，基于检测结果动态门控注意力权重，精准建模双手空间关系与交互逻辑
3. 扩展合成N-HOT3D数据集，构建当前最大的真实世界第一视角事件相机手部数据集EEH-R，覆盖弱光等场景，含约100万标注帧
### 关键结果
在合成、真实数据集上的多维度实验证明，方案效果全面优于所有基线方法

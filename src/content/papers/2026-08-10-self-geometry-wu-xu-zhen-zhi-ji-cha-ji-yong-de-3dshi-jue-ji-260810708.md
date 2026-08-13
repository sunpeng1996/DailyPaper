---
title: 'Self-Geometry: GT-Free and Plug-and-Play Test-Time Adaptation for Geometrically
  Consistent 3D Vision Foundation Models'
title_zh: Self-Geometry：无需真值、即插即用的3D视觉基础模型测试时自适应方法
authors:
- Seokhyun Youn
- Dahyeon Kye
- Sung-Ho Bae
- Jihyong Oh
affiliations:
- Chung-Ang University
- Kyung Hee University
arxiv_id: '2608.10708'
url: https://arxiv.org/abs/2608.10708
pdf_url: https://arxiv.org/pdf/2608.10708
published: '2026-08-10'
collected: '2026-08-13'
category: Other
direction: 3D视觉基础模型 · 测试时自适应
tags:
- Test-Time Adaptation
- Vision Foundation Model
- LoRA
- 3D Vision
- Geometric Consistency
one_liner: 提出无真值即插即用的3D视觉基础模型测试时自适应框架，通过显式多视图约束提升位姿与几何估计性能
practical_value: '- 若业务涉及3D商品建模、AR试穿等3D视觉相关场景，可复用该无真值、即插即用的测试时自适应方案，提升预训练3D VFM的推理精度

  - 多目标优化场景可借鉴其梯度解耦策略，避免多个约束损失之间的梯度冲突导致的效果劣化

  - 测试时轻量适配场景可参考其用LoRA实现低开销微调的方案，无需调整主干模型权重'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D视觉基础模型（VFM）预训练阶段未引入计算开销极高的显式多视图几何一致性约束，推理时存在几何不一致问题；此前测试时自适应方案依赖模型输出的隐式自一致性信号，在预训练VFM效果较差的场景增益十分有限。
### 方法关键点
1. 以2D像素对应关系作为伪真值，直接引入显式多视图几何约束；
2. 设计几何解耦优化模块，结合多视图一致性、极线一致性损失与梯度解耦策略，避免多损失间梯度冲突；
3. 提出基于SO(3)测地距离的帧角近邻视图采样器，降低约束施加的额外开销；
4. 基于LoRA实现轻量测试时自适应，即插即用且无需标注真值。
### 关键结果
在6款预训练VFM（VGGT、π³、DA3全系列）、4个基准数据集上，位姿与几何估计效果均获得一致提升；DA3-Giant模型单场景自适应耗时<2分钟（单PRO 6000显卡）。

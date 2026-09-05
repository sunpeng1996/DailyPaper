---
title: 'Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States'
title_zh: Puffin-World：原生3D世界状态驱动的可扩展统一多模态模型
authors:
- Kang Liao
- Yihang Luo
- Xiao-Ming Wu
- Linyi Jin
- Size Wu
- Chunyu Lin
- Yao Zhao
- Fei Wang
- Wei Li
- Chen Change Loy
affiliations:
- S-Lab, Nanyang Technological University
- University of Michigan
- Beijing Jiaotong University
- ACE Robotics
arxiv_id: '2609.04196'
url: https://arxiv.org/abs/2609.04196
pdf_url: https://arxiv.org/pdf/2609.04196
published: '2026-09-02'
collected: '2026-09-05'
category: Multimodal
direction: 多模态大模型 · 3D世界生成与物理仿真
tags:
- Multimodal_Model
- 3D_World_Modeling
- Physics_Simulation
- Omni-Camera
- Open_Dataset
one_liner: 提出原生3D世界状态联合建模的统一多模态框架，配套开源16M量级训练数据集与代码模型
practical_value: '- 电商3D商品展示、虚拟试逛/试穿场景可复用物理+几何+外观联合建模思路，替代多离线模块拼接方案，降低渲染误差

  - 具身Agent、虚拟场景交互类业务可直接借鉴Omni-Camera表征与跨帧物理动态传播策略，提升生成场景的物理一致性

  - 多模态数据集构建团队可参考Puffin-16M的「视觉-语言-相机三元组+运动轨迹」构造范式，适配3D场景类训练需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D世界生成、仿真方案依赖多个独立离线模块拼接，物理一致性差、跨任务适配成本高，无法支撑需要多任务协同的闭环交互类应用。
### 方法关键点
1. 联合建模三类原生3D世界状态：物理（重力场、纬度）、几何（深度）、外观（图像），配套统一Omni-Camera表征支持多任务与灵活运动需求；
2. 引入跨帧物理动态传播策略，锚定真实世界相机属性保障生成内容的物理一致性与视觉稳定性；
3. 单生成流程内耦合外观与几何，同步生成未来视图并重建底层几何，适配闭环交互需求。
### 关键结果
- 构建Puffin-16M数据集，包含15M视觉-语言-相机三元组、1M复杂运动轨迹；
- 支持模拟仿真、自校准世界探索等多任务协同闭环应用，全量代码、模型、数据集开源。

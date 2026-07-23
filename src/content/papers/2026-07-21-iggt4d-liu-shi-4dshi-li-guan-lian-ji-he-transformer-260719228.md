---
title: 'IGGT4D: Streaming 4D Instance-Grounded Geometry Transformer'
title_zh: IGGT4D：流式4D实例关联几何Transformer
authors:
- Zhengyu Zou
- Hao Li
- Kuixuan Jiao
- Liu Liu
- Tingyang Xiao
- Xiaolin Zhou
- Fangzhou Hong
- Zhizhong Su
- Dingwen Zhang
- Ziwei Liu
affiliations:
- Horizon Robotics
- S-Lab, Nanyang Technological University
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
arxiv_id: '2607.19228'
url: https://arxiv.org/abs/2607.19228
pdf_url: https://arxiv.org/pdf/2607.19228
published: '2026-07-21'
collected: '2026-07-23'
category: Agent
direction: 空间Agent · 4D动态场景流式理解
tags:
- 4D Scene Understanding
- Transformer
- Spatial Agent
- Streaming Perception
- Dataset Construction
one_liner: 提出流式4D场景理解模型IGGT4D及147K规模4D实例标注数据集InsScene4D
practical_value: '- 线下AR导购、实体配送机器人等空间Agent的感知模块，可复用其流式时序上下文复用、实例ID统一表示的设计，提升动态场景下商品/障碍物跟踪的时序一致性

  - 需构建时序关联的多模态标注数据集时，可借鉴其几何引导的自动化标注Pipeline，大幅降低人工标注成本

  - 长序列流输入的增量更新机制可迁移到实时推荐系统的用户兴趣在线建模，降低长序列推理的计算开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有流式3D重建方法以几何为核心，缺乏时序一致的实例级理解；语义重建与3D视觉语言方法依赖外部2D语义线索、几何输入耦合松散，无法支撑长动态场景下的几何-实例统一学习，同时行业缺少高质量4D监督数据集。
### 方法关键点
1. 设计IGGT4D流式4D实例关联几何Transformer，逐帧处理视频流，通过因果时空建模复用历史上下文，增量更新相机运动、几何、物体ID的统一表示，保证动态环境下长序列前馈重建的几何-实例一致性
2. 构建InsScene4D-147K大规模数据集，覆盖真实/合成、静态/动态场景，包含RGB、深度、位姿与时序一致的实例掩码，由几何引导的自动化标注Pipeline生成
### 关键结果
在3D重建、位姿估计、实例空间跟踪、开放词汇分割任务上性能全面优于现有流式基线，同时支持长动态序列的可扩展在线推理

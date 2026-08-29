---
title: 'TADP: Task-Aware Deformable Prediction for Single-Stage 3D Object Detection'
title_zh: TADP：面向单阶段3D目标检测的任务感知可变形预测方法
authors:
- Su Wang
- Yaochen Li
- Min Yang
- Jiaohao Nie
- Chang Liu
- Yuehu Liu
affiliations:
- Xi'an Jiaotong University
- Nanyang Technological University
- CSSC Systems Engineering Research Institute
arxiv_id: '2608.27282'
url: https://arxiv.org/abs/2608.27282
pdf_url: https://arxiv.org/pdf/2608.27282
published: '2026-08-27'
collected: '2026-08-29'
category: Other
direction: 3D目标检测 · 单阶段模型优化
tags:
- 3D Object Detection
- Single-stage Detector
- Task-aware
- Feature Aggregation
- Plug-and-play
one_liner: 提出即插即用的任务感知可变形预测头，提升单阶段3D目标检测精度同时保持低计算成本
practical_value: '- 多任务预测场景可借鉴任务感知可变形头设计思路，为不同任务分支定制特征变换逻辑，规避共用特征空间的性能瓶颈

  - 尺度感知的多尺度特征融合策略可迁移到推荐系统多域特征融合、多粒度用户兴趣建模场景

  - 即插即用的模块化头设计思路可复用在算法迭代中，降低存量模型的改造升级成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
单阶段3D目标检测通常使用同一套提取特征完成多任务预测，无法适配所有任务的特征空间需求，难以平衡检测精度与推理计算成本。
### 方法关键点
1. 设计三重特征精炼聚合模块，自适应提取三级特征；
2. 提出尺度感知的多尺度特征聚合块，实现多尺度特征的自适应融合；
3. 开发即插即用的任务感知可变形预测头，可感知不同任务的侧重与交互关系，配套3种差异化变形模块适配不同场景。
### 关键结果
在KITTI数据集上汽车检测mAP达到80.91%，超过多数同期SOTA方法，且提出的可变形头可直接迁移到其他检测方法，实现性能提升。

---
title: 'MC-DeTra: Motion-Consistent Joint Object Detection and Socially-Aware Trajectory
  Forecasting in Bird''s-Eye-View Images'
title_zh: MC-DeTra：鸟瞰图下运动一致的联合目标检测与社会感知轨迹预测
authors:
- Vladislav Diuzhev
- Dmitry Yudin
affiliations:
- Moscow Institute of Physics and Technology
- Artificial Intelligence Research Institute
arxiv_id: '2609.11717'
url: https://arxiv.org/abs/2609.11717
pdf_url: https://arxiv.org/pdf/2609.11717
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: BEV感知 · 联合检测与轨迹预测优化
tags:
- Object Detection
- Trajectory Forecasting
- BEV
- Auxiliary Loss
- Autonomous Driving
one_liner: 开源DeTra复现，提出训练端加运动一致性约束的MC-DeTra，无推理延迟提升BEV感知性能
practical_value: '- 训练阶段加辅助约束、推理阶段移除的范式可迁移至多任务推荐模型（如联合召回+排序），在不增加线上耗时的前提下提升多任务效果

  - 多任务共享backbone时的梯度校准方案可复用，解决多目标优化的梯度冲突问题

  - 引入上下文信号做辅助监督的思路可迁移到用户动态兴趣建模、用户行为序列预测任务'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
BEV视角下联合目标检测与轨迹预测的统一模型解决了级联方案的误差累积问题，但对动态运动主体的预测精度仍有瓶颈，且此前SOTA方案DeTra无公开实现。
### 方法关键点
1. 开源DeTra的完整复现代码、配置与评测工具链；
2. 提出MC-DeTra，新增三类仅训练阶段生效的约束：历史运动监督信号、周围交通occupancy社会上下文监督、预测航向与运动方向一致性损失，推理阶段完全移除无额外延迟；
3. 配套梯度校准分析方法，定位多任务在共享backbone上的优化冲突。
### 关键结果
在Waymo Open Dataset的检测条件预测协议下，MC-DeTra显著提升动态场景轨迹预测精度，同时检测精度不降反升，消融实验验证社会上下文信号贡献最高

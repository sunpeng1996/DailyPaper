---
title: 'Spatial-Interactor: Learning Spatial Reasoning through Interaction with the
  Observable Physical World'
title_zh: Spatial-Interactor：通过与可观测物理世界交互学习空间推理
authors:
- Kaixiang Yao
- Xu Wang
- Miao Pan
- Hu Xiyue
- Weishi Wang
- Daniel Dahlmeier
- Jintao Chen
- Yongliang Shen
- Xuhong Zhang
- Wenqi Zhang
affiliations:
- Zhejiang University
- SAP
arxiv_id: '2609.23038'
url: https://arxiv.org/abs/2609.23038
pdf_url: https://arxiv.org/pdf/2609.23038
published: '2026-09-18'
collected: '2026-09-24'
category: Reasoning
direction: 视觉语言模型 · 动态空间推理优化
tags:
- VLM
- Spatial Reasoning
- Curriculum Learning
- Knowledge Distillation
- SFT
- Interaction Trajectory
one_liner: 提出三级课程+两阶段训练框架，利用交互轨迹提升VLM动态空间推理能力
practical_value: '- 做多模态商品理解/AR导购Agent时，可复用三级课程学习范式，先静态物体空间关系建模，再主动视角变化下的状态迁移，最后长序列交互轨迹推理，逐步提升场景理解能力

  - 长序列状态整合任务可借鉴On-Policy Distillation策略，用带分段标注的教师分支监督学生的CoT推理，降低长轨迹建模的训练难度

  - 多模态交互类任务可复用「交互轨迹-动作-后续观测」配对的监督数据构造方法，大幅降低动态状态迁移任务的标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM的空间推理训练多聚焦静态物体属性/关系问答，缺少动态环境下物体运动、视角变化导致的局部状态迁移监督，无法支撑长轨迹下的空间状态更新。
### 方法关键点
1. 设计三级课程学习框架：L1学习被动世界状态迁移，L2学习主动自身状态迁移，L3学习长horizon交互轨迹整合
2. 构造LSI-108K数据集，覆盖仿真+真实交互轨迹，匹配三级课程的任务目标
3. 采用两阶段训练：先对L1/L2做SFT学习局部迁移，再用On-Policy Distillation，由带分段迁移描述的教师分支监督学生的on-policy CoT，实现长轨迹连续迁移整合
### 关键结果
在多类VLM、多个空间推理基准上，局部状态迁移建模、长序列整合能力均获得一致性提升。

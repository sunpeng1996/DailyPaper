---
title: 'MvT: Event-based Multi-view Projection for Multiple Object Tracking'
title_zh: MvT：基于事件相机的多视图投影多目标跟踪方法
authors:
- Muxi Zha
- Banglei Guan
- Minzu Liang
- Zibin Liu
- Yang Shang
- Qifeng Yu
- Laurent Kneip
arxiv_id: '2610.37309'
url: https://arxiv.org/abs/2610.37309
pdf_url: https://arxiv.org/pdf/2610.37309
published: '2026-10-27'
collected: '2026-10-29'
category: Other
direction: 事件相机 · 多目标跟踪技术研究
tags:
- Multi-object Tracking
- Event Camera
- Multi-view Fusion
- Training-free
- 3D Association
one_liner: 提出免训练的事件多视图跟踪框架，解决单视图轨迹重叠时的跟踪歧义问题
practical_value: '- 主要是计算机视觉多目标跟踪领域的学术贡献，电商/推荐/Agent业务可借鉴点有限'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
事件相机因高动态范围、低延迟特性被用于多目标跟踪，主流伪帧处理范式可直接复用图像技术，但轨迹重叠/空间接近时易出现跟踪失效。
### 方法关键点
免训练多视图跟踪框架MvT包含两个核心模块：1）MvP模块将事件编码为3种互补时空视图，缓解模式离散化，保留2D格式可直接适配现有图像类跟踪方法；2）MvF阶段将多视图结果统一映射至3D坐标系，通过带多准则约束的优化模型关联轨迹片段，消解单视图跟踪歧义。
### 关键结果
在4个测试数据集（含自采小目标数据集SOD）上效果优于现有非学习、学习类跟踪器，无需标注数据即可落地，数据效率突出。

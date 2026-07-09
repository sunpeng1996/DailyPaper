---
title: 'SceneFrom3D: Geometry-Conditioned Outdoor 3D Scene Generation via View Scheduling
  with Object-Level Control'
title_zh: SceneFrom3D：基于视角调度与对象级控制的几何约束户外3D场景生成
authors:
- Geonung Kim
- Jeongeun Park
- Nuri Ryu
- Di Liu
- Sunghyun Cho
affiliations:
- POSTECH, Republic of Korea
- Meta Reality Labs, United States of America
arxiv_id: '2607.04540'
url: https://arxiv.org/abs/2607.04540
pdf_url: https://arxiv.org/pdf/2607.04540
published: '2026-07-04'
collected: '2026-07-09'
category: Other
direction: 3D场景生成 · 视角调度与对象级控制
tags:
- 3D Generation
- View Scheduling
- Geometry Conditioning
- Object-level Control
- 3D Scene Synthesis
one_liner: 提出带自动视角调度与对象级控制的几何约束户外3D场景生成框架
practical_value: '- 电商3D虚拟场景/商品展示场景：可借鉴对象级外观绑定+几何贴合度参数方案，实现自定义商品快速摆放到虚拟户外场景的可控生成，大幅降低3D营销素材制作成本

  - AR户外广告落地：可复用自动视角调度生成多视角一致3D场景的方法，解决户外AR广告中场景渲染覆盖不全、视角切换视觉不稳定的问题

  - 虚拟主播户外背景生成：可直接复用该框架快速生成符合结构要求的3D户外背景，支持任意视角切换，适配虚拟直播动态镜头需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有几何约束3D场景生成普遍采用「视角调度→多视角合成→3D重建」三阶段流程，其中视角调度是户外场景的核心瓶颈：户外大尺度、非结构化、无边界的几何特性，很难找到同时满足覆盖度足够、生成过程稳定的视角序列，且现有方案对象级可控性不足。
### 方法关键点
1. 构建有向生成图：节点为锚点视角、边为插值轨迹，自动定义需合成的视角、插值视角对、生成顺序，解决户外场景视角调度难题；
2. 新增对象级条件控制：为每个对象绑定身份图像做外观引导，同时设置几何贴合度参数，实现分区域的输入几何贴合度灵活控制。
### 关键结果
在几何约束户外3D场景生成任务上达到SOTA，生成的场景视觉质量高，同时支持可控的对象外观调整与几何贴合度控制。

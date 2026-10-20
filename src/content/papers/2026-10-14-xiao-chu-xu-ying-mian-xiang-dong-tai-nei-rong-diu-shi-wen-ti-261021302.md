---
title: 'Dusting the Phantom: Gaussian Allocation for Fading Dynamic Content'
title_zh: 消除虚影：面向动态内容丢失问题的高斯分配优化方法
authors:
- Minhyeok Roh
- Minseo Lee
- Jun Young Jeong
- Byeonghyeon Lee
- Lucas Yunkyu Lee
- Jaesik Park
- Eunbyung Park
affiliations:
- Yonsei University
- Electronics and Telecommunications Research Institute (ETRI)
- Pohang University of Science and Technology (POSTECH)
- Seoul National University
arxiv_id: '2610.21302'
url: https://arxiv.org/abs/2610.21302
pdf_url: https://arxiv.org/pdf/2610.21302
published: '2026-10-14'
collected: '2026-10-20'
category: Other
direction: 4D动态场景 · 高斯重建分配策略优化
tags:
- 4DGS
- Gaussian Splatting
- Dynamic Scene Reconstruction
- Volumetric Video
- Resource Allocation
one_liner: 提出两种互补高斯分配策略，固定预算下解决4D动态场景高斯重建中小高速物体丢失、细节模糊问题
practical_value: '- 固定预算下优先向高变化、高误差区域倾斜资源的分配思路，可迁移到电商推荐的算力/流量配额优化，给高转化动态品类、活动资源倾斜

  - 不依赖现有分布的Seed Injection冷启动资源注入逻辑，可迁移到新用户/新商品冷启动流量分配，用多信号交叉确定投放位置，降低历史行为依赖

  - Temporal Biased Relocation的时间偏置资源重定位思路，可迁移到短时效内容（直播商品、限时活动）的推荐资源动态调整，用实时信号优化投放时空分布'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
动态4D高斯表征已支撑高质量实时 volumetric 视频落地，但高速运动小物体易消失、高动态区域纹理丢失问题突出，单纯增加高斯数量、延长训练无法解决，核心瓶颈是高斯基元的时空分配策略，现有方法仅依赖当前高斯位置，忽略重定位的时空目标点。
### 方法关键点
1. Seed Injection：基于时序外观变化、重建误差识别重建不足的动态区域，通过多视图观测在几何合理的3D位置独立初始化新高斯，不依赖现有高斯分布；
2. Temporal Biased Relocation：用时序解析的优化信号引导重定位高斯的时空放置，全程保持高斯总预算固定，无需改动底层表征。
### 关键结果
在多个动态场景数据集上验证，高动态区域重建质量显著提升，可完整恢复小高速运动物体和细粒度外观细节。

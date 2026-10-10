---
title: 'LVS: Local View Synthesis from Relative Camera Pose by Reusing Previous Views'
title_zh: LVS：基于相对相机位姿与历史视图复用的局部视图合成方法
authors:
- Qizhou Huo
- Xuan Sun
- Yongfei Guo
- Zhipeng Wang
- Yuanhao Gong
affiliations:
- 中国科学院长春光学精密机械与物理研究所
- 中国科学院大学（北京）
- 中国科学院（北京）
arxiv_id: '2610.12127'
url: https://arxiv.org/abs/2610.12127
pdf_url: https://arxiv.org/pdf/2610.12127
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 新视图合成 · 低延迟渲染优化
tags:
- Novel View Synthesis
- 3D Gaussian Splatting
- Geometric Warping
- Residual Learning
- Low Latency Rendering
one_liner: 提出复用历史渲染视图结合残差修正的低延迟局部视图合成框架LVS
practical_value: '- 仅面向有3D商品渲染、AR试穿/试戴需求的电商交互场景有参考价值，普通搜索推荐业务可借鉴点有限

  - 高频小幅交互场景可复用「缓存历史计算结果+轻量网络修正残差」的架构思路，大幅降低响应延迟

  - 缓存已有特征避免重复计算的优化思路，可迁移到端侧低延迟交互类业务的工程实现'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
交互式场景探索中小幅度相机移动会产生大量视图内容重叠，传统3D高斯渲染对每个目标视图独立渲染，未利用已有冗余内容；纯几何扭曲方法无法补全新暴露区域内容，且对深度误差敏感。
### 方法关键点
1. 提出相对位姿引导的RGB-D图像复用框架，替代邻近视图的重复渲染流程
2. 先通过几何扭曲基于深度和相对位姿迁移源视图内容，再用轻量多尺度网络预测RGB残差修正伪影、补全缺失外观
3. 缓存源视图特征避免重复计算，进一步降低开销
### 关键结果
在GS-render基准上相比纯几何扭曲方法PSNR提升0.72dB，实拍与合成场景测试均实现更低查询延迟，可支撑高响应度场景探索。

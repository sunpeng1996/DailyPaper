---
title: Color Pass-Through via Camera-Display Coupling
title_zh: 基于相机-显示耦合的色彩直通技术
authors:
- Ruikang Li
- Molin Li
- Jiarui Wu
- Zhe Wei
- Pengpeng Liu
- Tianfan Xue
affiliations:
- CUHK MMLab
- 浙江大学
- 华为中央媒体技术研究院
arxiv_id: '2607.12746'
url: https://arxiv.org/abs/2607.12746
pdf_url: https://arxiv.org/pdf/2607.12746
published: '2026-07-13'
collected: '2026-07-27'
category: Other
direction: 计算摄影 · 色彩还原优化
tags:
- Computational Photography
- Color Calibration
- End-to-End Optimization
- Camera Display Coupling
one_liner: 提出端到端相机显示耦合色彩校准框架，大幅降低拍显链路的色彩失真
practical_value: '- 电商商品实拍场景可借鉴耦合校准思路，替代现有相机、显示端分步校准流程，减少商品图色彩偏差，降低色差导致的退货率

  - 涉及AR试穿/试妆、虚实融合的业务可参考该端到端优化思路，避免多模块分步校准带来的误差累积，提升色彩对齐效果

  - 纯搜索推荐/Agent算法方向从业者无直接可复用方案，主要为计算摄影领域技术贡献'
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
现有拍摄到显示的链路将相机、显示模块分开独立校准，通过低维色彩变换连接两个环节，存在明显信息瓶颈与误差累积问题，即便当前传感器、显示硬件性能大幅提升，最终显示画面和真实场景在色彩、亮度、对比度上仍有显著差异。

### 方法关键点
提出Color Pass-Through端到端学习框架，核心思路是将相机与显示作为耦合系统而非独立模块校准，直接对拍摄后的原始图像做优化，支持为不同观测者做单步全拍显路径校准。

### 关键结果
5分制用户研究得分较基准方法平均提升2.0分，量化指标提升超2倍，原始场景感知色彩还原效果显著优于现有方案。

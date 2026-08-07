---
title: Whence the Voice? Self-supervised Dual-source Audio-Visual Localisation via
  Selective Convergence
title_zh: 基于选择性收敛的自监督双源视听定位方法
authors:
- Han Hu
- Dongheng Lin
- Yuqi Hou
- Haotian Li
- Hyung Jin Chang
- Jianbo Jiao
affiliations:
- University of Birmingham
arxiv_id: '2608.05816'
url: https://arxiv.org/abs/2608.05816
pdf_url: https://arxiv.org/pdf/2608.05816
published: '2026-08-06'
collected: '2026-08-07'
category: Multimodal
direction: 多模态感知 · 自监督视听定位
tags:
- Self-supervised Learning
- Audio-Visual Localization
- Contrastive Learning
- Multimodal Perception
- Benchmark
one_liner: 发现自监督视听学习选择性收敛现象，提出无标注双阶段双源视听定位框架
practical_value: '- 双阶段渐进式自监督定位思路可迁移至电商短视频/直播的声源商品识别场景，无需人工标注即可定位视频中正在发声的商品区域，支撑商品弹窗、边看边买等功能

  - 选择性收敛思路可复用至多模态召回排序模块，优先对齐高显著性跨模态匹配对，降低多源多模态内容匹配的计算复杂度

  - 多模态定位类任务的评估指标设计可借鉴其修正逻辑，采用像素级对齐标注替代bounding box标注，大幅降低系统评估偏差'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多声源视觉定位存在固有循环依赖：分离混合音频需先获取声源位置，而识别发声区域又依赖已分离的音频信号，现有方案需标注支撑或难以适配双声源场景。
### 方法关键点
1. 发现自监督视听学习的选择性收敛现象：对比模型会自然收敛到最显著的视听对应关系，而非平均表征所有声源，类比人类选择性听觉注意，可打破循环依赖
2. 构建双阶段渐进框架：第一阶段利用选择性收敛识别主导声源，第二阶段基于学到的先验挖掘剩余声源，全程无需人工标注
3. 针对现有基准的评估偏差问题，引入像素级分割掩码实现空间对齐的无偏评估
### 关键结果
无人工标注前提下，在双源基准上取得自监督方法最优性能，部分指标超过现有弱监督方案

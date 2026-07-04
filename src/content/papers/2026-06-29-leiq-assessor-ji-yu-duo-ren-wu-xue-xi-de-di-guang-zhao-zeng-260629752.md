---
title: 'LEIQ-Assessor: Multi-dimensional Quality Assessment of Low-light Enhanced
  Images via Multi-task Learning'
title_zh: LEIQ-Assessor：基于多任务学习的低光照增强图像多维度质量评估模型
authors:
- Wei Sun
- Yanwei Jiang
- Dandan Zhu
- Jinqiu Sang
- Jikai Xu
- Weixia Zhang
- Guangtao Zhai
affiliations:
- East China Normal University
- Shanghai Jiao Tong University
arxiv_id: '2606.29752'
url: https://arxiv.org/abs/2606.29752
pdf_url: https://arxiv.org/pdf/2606.29752
published: '2026-06-29'
collected: '2026-07-04'
category: Other
direction: 低光照图像增强 · 多任务质量评估
tags:
- Image-Quality-Assessment
- Multi-task-Learning
- Vision-Transformer
- SigLIP2
- No-Reference-IQA
one_liner: 基于SigLIP2 ViT做多任务学习，同时预测低光照增强图像整体MOS和6项感知子属性，获QoMEX2026挑战赛第二名
practical_value: '- 电商商品低光照图增强后的效果自动质检可复用该多任务评估框架，同时检测亮度、色彩保真、噪点等多维度问题，替代部分人工审核

  - 多任务联合优化采用PLCC损失关联主目标（整体质量分）和子属性的思路，可迁移到推荐系统多目标排序任务，强化共享表征的关联性

  - 无参考图像质量评估方案可直接复用于UGC内容平台的低质内容自动过滤，减少用户上传暗图、过曝图的展示概率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
低光照图像增强算法易引入噪点放大、色偏、结构损伤、过曝等伪影，现有质量评估指标可靠性不足，难以支撑算法迭代和落地应用。

### 方法关键点
1. 以预训练SigLIP2 Vision Transformer为骨干，采用多任务学习架构，同时预测整体Mean Opinion Score（MOS）和亮度、色彩保真度、噪点水平、曝光质量、自然度、内容恢复6项感知子属性；
2. 采用PLCC损失联合优化多个相关目标，共享表征比单任务模型提取的质量感知特征更丰富。

### 关键结果数字
在MLE基准上显著优于现有无参考IQA模型和手工设计的质量描述符，获得QoMEX 2026低光照增强图像质量评估挑战赛第二名。

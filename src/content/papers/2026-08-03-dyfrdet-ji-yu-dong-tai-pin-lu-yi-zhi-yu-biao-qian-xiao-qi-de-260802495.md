---
title: 'DyFrDet: Towards Accurate Small Object Detection via Dynamic Frequency Suppression
  with Label Disambiguation'
title_zh: DyFrDet：基于动态频率抑制与标签消歧的精准小目标检测
authors:
- Zihan Yang
- Yang Guo
- Hongxing Zhang
- Dan Lu
- Siyuan Yao
affiliations:
- Hangzhou International Innovation Institute of Beihang University
- Beijing University of Posts and Telecommunications
- Shenzhen Campus of Sun Yat-sen University
arxiv_id: '2608.02495'
url: https://arxiv.org/abs/2608.02495
pdf_url: https://arxiv.org/pdf/2608.02495
published: '2026-08-03'
collected: '2026-08-05'
category: Other
direction: 小目标检测 · 频域特征与标注优化
tags:
- Small Object Detection
- Frequency Domain Feature
- Label Disambiguation
- Feature Pyramid Network
one_liner: 提出融合动态频域特征金字塔与标签消歧的小目标检测框架，性能达SOTA
practical_value: '- 电商主图/直播场景小商品识别可复用DyFrFPN频域降噪思路，抑制背景冗余噪声提升小物体召回率

  - 密集小商品标注歧义场景可借鉴LDM的概率分布建模方法优化损失函数，降低标注歧义对精度的影响

  - 现有FPN架构优化可直接集成动态频带预测模块，无需大幅改结构即可提升低分辨率目标的特征辨识度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
小目标检测因视觉信息不足精度受限，现有方案普遍忽略频域噪声干扰与标签歧义问题，严重阻碍定位准确性提升。
### 方法关键点
1. 设计动态频域感知特征金字塔（DyFrFPN）：将层级特征转换到频域空间，通过动态频带预测器（DBP）自适应抑制低频冗余和过度高频噪声，保留小目标识别所需的判别性特征分量；
2. 新增标签消歧模块（LDM）：基于概率分布显式建模并缓解目标标签固有歧义，大幅提升低分辨率小目标的定位精度。
### 关键结果
在多个公开小目标检测基准上达到SOTA性能，复杂场景下的鲁棒性得到充分验证。

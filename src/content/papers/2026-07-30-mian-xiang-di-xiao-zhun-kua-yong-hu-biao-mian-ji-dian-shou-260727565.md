---
title: A Montage-Agnostic Encoder for Calibration-Light Cross-User Gesture Recognition
  from Surface Electromyography
title_zh: 面向低校准跨用户表面肌电手势识别的电极排布无关编码器
authors:
- Jethro Odeyemi
- W. J. Zhang
affiliations:
- University of Saskatchewan
arxiv_id: '2607.27565'
url: https://arxiv.org/abs/2607.27565
pdf_url: https://arxiv.org/pdf/2607.27565
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 生物信号识别 · 跨用户少样本迁移
tags:
- cross-domain transfer
- few-shot learning
- encoder
- signal processing
- transfer learning
one_liner: 提出共享权重、按物理坐标定位电极的排布无关编码器，降低跨用户肌电手势识别的校准要求
practical_value: '- 跨域/跨用户迁移场景中，可借鉴「用输入的物理属性而非位置索引编码」的思路，优化跨域推荐的特征对齐效果，减少域定制参数

  - 少样本任务下，共享权重+全局属性编码的编码器架构，可复用在用户/物品冷启动的表征建模中，降低小样本过拟合风险

  - 模型性能边界验证的样本量扫描方法，可用来量化推荐冷启动所需的最少训练样本阈值，减少训练资源浪费'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
表面肌电手势识别落地假肢控制场景的核心瓶颈是跨用户迁移性差，新用户需完成大量标注校准才能获得可用性能，技术长期停留在实验室阶段。
### 方法关键点
1. 设计电极排布无关编码器，对所有电极采用共享权重处理，用电极物理坐标而非通道索引做位置编码，无需为不同电极排布定制参数，支持任意通道数输入；
2. 跨用户统一训练，仅需3-shot标注即可快速适配新用户。
### 关键结果
在DB1数据集上较单用户Hudgins+LDA基线macro-F1高0.234，DB2高0.108；消融实验显示3个核心组件各自贡献超过3-shot性能的一半；训练用户数从9到39时性能增益基本持平，仅低于9时训练不收敛；监督训练充分时自监督预训练无额外增益。

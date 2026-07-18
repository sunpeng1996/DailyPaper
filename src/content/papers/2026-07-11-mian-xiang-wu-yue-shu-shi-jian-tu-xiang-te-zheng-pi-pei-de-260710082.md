---
title: Label-Free Target-Domain Adaptation for Unconstrained Event-Image Feature Matching
  via Dual-Stage Distillation
title_zh: 面向无约束事件-图像特征匹配的无标注目标域适配双阶段蒸馏方法
authors:
- Zhonghua Yi
- Hao Shi
- Qi Jiang
- Yufan Zhang
- Kailun Yang
- Kaiwei Wang
affiliations:
- Zhejiang University
- Hunan University
- National University of Defense Technology
- Ant Group
arxiv_id: '2607.10082'
url: https://arxiv.org/abs/2607.10082
pdf_url: https://arxiv.org/pdf/2607.10082
published: '2026-07-11'
collected: '2026-07-18'
category: Multimodal
direction: 多模态跨域特征匹配 · 无监督蒸馏
tags:
- Cross-Modal Matching
- Knowledge Distillation
- Unsupervised Domain Adaptation
- Event Camera
- Self-Training
one_liner: 提出双阶段蒸馏范式，实现无标注无约束场景下事件-图像跨模态特征匹配SOTA
practical_value: '- 两阶段蒸馏（通用预训练+目标域自蒸馏）范式可复用在缺乏标注的跨模态商品匹配/多模态召回场景，大幅降低标注成本

  - 引入外部业务先验（如商品类目/属性规则替代文中极线几何先验）引导自蒸馏的思路，可提升跨域特征对齐效果

  - 分布损失+对比损失组合的预训练优化目标，可迁移至多模态通用表征预训练，增强表征泛化性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有事件-图像跨模态匹配方法高度依赖匹配标注或严格对齐的硬件设备，无法适配无标注、无传感器对齐先验的真实开放场景。
### 方法关键点
1. 第一阶段标签无关蒸馏预训练：基于大规模数据，采用分布损失+对比损失组合优化目标，学习高泛化性通用表征
2. 第二阶段极线引导自蒸馏：针对无标注下游目标域数据，通过一致性校验筛选鲁棒匹配对，引入外部极线几何先验的置信度信号，实现无监督下模型在目标域自进化
3. 构建基于TUM-VIE的跨模态评估基准，覆盖物理分离、内参与分辨率差异的真实相机场景
### 关键结果
在MVSEC、TUM-VIE两个姿态估计任务上均实现SOTA性能，相关代码与基准数据集已开源

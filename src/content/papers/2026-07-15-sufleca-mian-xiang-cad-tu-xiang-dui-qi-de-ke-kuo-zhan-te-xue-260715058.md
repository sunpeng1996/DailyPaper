---
title: 'SUFLECA: Scaling Up Feature Learning for CAD-to-image Alignment'
title_zh: SUFLECA：面向CAD-图像对齐的可扩展特征学习框架
authors:
- Saad Ejaz
- Miguel Fernandez-Cortizas
- Javier Civera
- Holger Voos
- Jose Luis Sanchez-Lopez
arxiv_id: '2607.15058'
url: https://arxiv.org/abs/2607.15058
pdf_url: https://arxiv.org/pdf/2607.15058
published: '2026-07-15'
collected: '2026-07-19'
category: Other
direction: 三维视觉 · CAD到图像对齐
tags:
- ComputerVision
- Zero-shot Learning
- Weakly Supervised Learning
- Feature Learning
- Pose Estimation
one_liner: 提出弱监督零样本CAD-图像对齐框架，用几何感知特征与一致匹配算法，精度超现有零样本及全监督基线
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有零样本CAD-图像对齐方法依赖外观驱动匹配，在遮挡、sim-to-real域偏移场景下性能退化，全监督方案标注成本高、跨域泛化性差。
### 方法关键点
1. 基于预训练视觉表征，通过覆盖12个真实/合成数据集共674K张图像的Normalized Object Coordinates (NOCs)监督，扩展几何驱动的特征学习，得到跨域泛化的紧凑几何感知特征；
2. 提出几何一致性匹配算法，建立可靠的一对一CAD-图像对应关系，无需迭代姿态优化即可实现亚秒级单实例对齐。
### 关键结果
在ScanNet25k基准上取得33.4%类别精度、42.3%实例精度，比最优零样本基线分别高10.3、12.2个百分点，计算开销更低，且首次在该基准上性能超过全监督方法。

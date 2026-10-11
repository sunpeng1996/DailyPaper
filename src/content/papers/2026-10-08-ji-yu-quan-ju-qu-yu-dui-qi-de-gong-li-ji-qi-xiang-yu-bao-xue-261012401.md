---
title: Learning Kilometer-Scale Weather Prediction with Global-Regional Alignment
title_zh: 基于全局-区域对齐的公里级气象预报学习方法
authors:
- Guowen Li
- Yang Liu
- Yujie Wang
- Qiuyan Sun
- Haoyuan Liang
- Juepeng Zheng
- Hong Cheng
- Haohuan Fu
affiliations:
- Tsinghua University
- The Chinese University of Hong Kong
- Sun Yat-Sen University
- NSCC-SZ
arxiv_id: '2610.12401'
url: https://arxiv.org/abs/2610.12401
pdf_url: https://arxiv.org/pdf/2610.12401
published: '2026-10-08'
collected: '2026-10-11'
category: Other
direction: 气象预报 · 多尺度特征对齐
tags:
- weather forecasting
- multi-scale alignment
- pretrained model reuse
- domain adaptation
one_liner: 提出ScaleCast全局-区域对齐框架，复用预训练全局气象模型实现高精度公里级区域预报
practical_value: 主要是气象领域学术贡献，电商/推荐/Agent业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有数据驱动的公里级区域气象预报要么依赖数值预报提供全局引导，要么需额外训练全局预测组件，预训练全局气象模型复用存在跨网格表征对齐、全局引导与局部交互融合的核心难点。
### 方法关键点
提出ScaleCast区域预报框架：1）全局-区域转换模块对齐跨网格的全局、区域表征与区域位置；2）全局-区域对齐与动力学模块融合对齐后的全局引导信息与区域邻域交互信息。
### 关键结果
在5.5km分辨率CERRA数据集上，地表、高空气象变量预报精度优于基线；单模型可适配盘古气象、GraphCast、HRES等3种全局预报驱动无需重训；3km分辨率HRRR数据集微调验证跨域跨分辨率适配性；风暴案例中气旋定位、核心气压估计精度提升，站点温湿度观测拟合度更优。

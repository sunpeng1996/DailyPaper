---
title: Oriented Semi-DETR for Semi-Supervised Aerial Object Detection
title_zh: Oriented Semi-DETR：半监督航空图像定向目标检测方法
authors:
- Yuqiu Li
- Jian Xue
- Fan Li
- Ke Lu
affiliations:
- University of Chinese Academy of Sciences
- Peng Cheng Laboratory
arxiv_id: '2611.21223'
url: https://arxiv.org/abs/2611.21223
pdf_url: https://arxiv.org/pdf/2611.21223
published: '2026-11-16'
collected: '2026-11-22'
category: Other
direction: 半监督目标检测 · 定向框DETR优化
tags:
- Semi-supervised Learning
- DETR
- Oriented Object Detection
- Aerial Image
- Pseudo Label
one_liner: 解决半监督DETR定向框参数二义性问题，提出三个无额外前向传播的无参数优化策略，全标注比例下优于基线
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.MM
depth: abstract
---

## 动机
半监督DETR拓展到航空图像定向目标检测场景时存在定向框参数二义性问题：同一空间位置的旋转框可对应两组完全不同的参数，导致回归损失误罚正确定位的学生框，GMM过滤模块也会因匹配成本虚高丢弃有效样本，严重影响训练稳定性与效果。
## 方法关键点
提出3个无参数、无额外前向传播开销的优化策略：
1. Swap-aligned Target Selection：选择与学生预测编码更接近的定向框参数作为回归目标
2. Swap-invariant Reliability Cost：匹配成本计算时取两组等价编码的最小值，仅基于几何特征做过滤决策
3. Swap-aware Pseudo-label Denoising：提前启动去噪，线性抬升损失权重，基于教师打分和编码边际加权每个query
## 关键结果
在DOTA-v2.0数据集所有标注比例下，性能全面优于基于DETR的监督、半监督基线，严格IoU阈值下增益最大。

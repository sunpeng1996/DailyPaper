---
title: 'Beyond Feature Fusion: Sensor-Grounded Semantic-Spiking Learning for Robust
  Object Detection'
title_zh: 超越特征融合：基于传感器的语义脉冲学习实现鲁棒目标检测
authors:
- Hanwen Liang
- Wenxuan Liu
- Wenxin Huang
- Jingling Yuan
- Zhaofei Yu
- Xian Zhong
- Tiejun Huang
affiliations:
- Wuhan University of Technology
- Peking University
- Hubei University
arxiv_id: '2611.34828'
url: https://arxiv.org/abs/2611.34828
pdf_url: https://arxiv.org/pdf/2611.34828
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 极端光照鲁棒 · 脉冲相机目标检测
tags:
- Object Detection
- Spike Camera
- Illumination Robustness
- Lightweight Model
- Feature Fusion
one_liner: 提出SPIRE语义脉冲框架，基于脉冲相机单流实现极端光照下低算力鲁棒目标检测
practical_value: '- 长短时序列互补特征提取思路可迁移至用户行为建模，分别挖掘长周期静态偏好与短周期动态兴趣

  - 实测值与模型预测值的残差做特征校正的trick，可用于排序阶段多源特征融合降噪

  - 双分支联合监督的训练范式可借鉴至多任务推荐模型的损失函数设计，提升多目标一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有帧基相机目标检测在过曝、欠曝等极端光照场景下存在细节丢失、边界模糊问题，检测精度大幅下降；脉冲相机虽具备高动态范围、高时间分辨率优势，但现有方法未充分利用长短时间窗口脉冲信号的互补价值，算力开销较高。

### 方法关键点
SPIRE传感器驱动的语义脉冲框架设计思路：① 对全脉冲包做检测导向的光照自适应生成外观视图，同时构建逐步变长前缀的累计视图序列，提取率图、边缘图、率差三类动态特征；② 选定尺度下将ANN语义特征与脉冲初始化参数共同设置膜电位与发放阈值，实现语义引导的时域编码；③ 用局部脉冲计数对比监督双分支训练，结合实测与ANN预测的对比残差对融合特征金字塔做有界校正。

### 关键结果
模拟VOC/COCO数据集上，4类过曝/欠曝场景下SPIRE-D较最强基线AP50提升4.00~5.50；真实PKU-Vidar-DVS数据集上AP50达67.07、AP75达40.10，MACs较SPFD降低50.4%。
